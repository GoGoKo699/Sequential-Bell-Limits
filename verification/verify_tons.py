#!/usr/bin/env python3
"""Finite verification of the sequential CHSH converse and its TONS attainment.

The exact kernel checks use fractions. The independent linear programs optimize
over every normalized conditional table satisfying the stated joint causal
equalities, without assuming an instrument or the attaining construction.
The proof for arbitrary K is in science/causal-bound.md.
"""

from __future__ import annotations

import argparse
from collections import Counter
from fractions import Fraction
import hashlib
import itertools
import json
from pathlib import Path
import platform

import numpy as np
import scipy
from scipy.optimize import linprog
from scipy.sparse import coo_matrix, csr_matrix, hstack, vstack


ORIENTATIONS = tuple(
    signs
    for signs in itertools.product((-1, 1), repeat=4)
    if np.prod(signs) == -1
)
CANONICAL = (1, 1, 1, -1)


class TONSProblem:
    """Probability coordinates and all defining joint TONS equalities."""

    def __init__(self, k: int):
        self.k = k
        self.side = 1 << k
        self.bits = tuple(itertools.product((0, 1), repeat=k))
        self.bit_index = {bits: i for i, bits in enumerate(self.bits)}
        self.n_variables = 4 * self.side * self.side
        self.rows: list[tuple[str, list[tuple[int, int]], int]] = []
        self._build_equalities()
        rr, cc, vv = [], [], []
        for row_number, (_, entries, _) in enumerate(self.rows):
            for column, value in entries:
                rr.append(row_number)
                cc.append(column)
                vv.append(value)
        self.a_eq = coo_matrix(
            (vv, (rr, cc)), shape=(len(self.rows), self.n_variables)
        ).tocsr()
        self.b_eq = np.asarray([row[2] for row in self.rows], dtype=float)
        self.scores = self._build_scores()

    def index(self, x: int, y_index: int, a: int, b_index: int) -> int:
        return ((x * self.side + y_index) * 2 + a) * self.side + b_index

    def _add(self, kind: str, entries: list[tuple[int, int]], rhs: int = 0):
        self.rows.append((kind, entries, rhs))

    def _build_equalities(self):
        for x in (0, 1):
            for yi in range(self.side):
                self._add(
                    "normalization",
                    [
                        (self.index(x, yi, a, bi), 1)
                        for a in (0, 1)
                        for bi in range(self.side)
                    ],
                    1,
                )

        # The complete Bob output string, not just each pairwise marginal.
        for yi in range(self.side):
            for bi in range(self.side):
                self._add(
                    "alice_to_all_bobs",
                    [(self.index(0, yi, a, bi), 1) for a in (0, 1)]
                    + [(self.index(1, yi, a, bi), -1) for a in (0, 1)],
                )

        # Alice remains in the marginal when future Bob outcomes are summed.
        for prefix in range(self.k):
            for yp in itertools.product((0, 1), repeat=prefix):
                ys = [
                    yi for yi, y in enumerate(self.bits) if y[:prefix] == yp
                ]
                reference_y = ys[0]
                for x in (0, 1):
                    for a in (0, 1):
                        for bp in itertools.product((0, 1), repeat=prefix):
                            bs = [
                                bi
                                for bi, b in enumerate(self.bits)
                                if b[:prefix] == bp
                            ]
                            for yi in ys[1:]:
                                self._add(
                                    "alice_and_prefix_no_future_input",
                                    [(self.index(x, yi, a, bi), 1) for bi in bs]
                                    + [
                                        (self.index(x, reference_y, a, bi), -1)
                                        for bi in bs
                                    ],
                                )

    def _build_scores(self) -> np.ndarray:
        """Canonical CHSH, with all other Bob inputs uniformly averaged."""
        scores = np.zeros((self.k, self.n_variables))
        scale = 2.0 ** (1 - self.k)
        for x in (0, 1):
            for yi, y in enumerate(self.bits):
                for a in (0, 1):
                    for bi, b in enumerate(self.bits):
                        column = self.index(x, yi, a, bi)
                        for i in range(self.k):
                            scores[i, column] = (
                                scale * (-1) ** (a + b[i] + x * y[i])
                            )
        return scores

    def exact_residuals(self, probability: list[Fraction]) -> dict[str, str]:
        residuals: dict[str, Fraction] = {}
        for kind, entries, rhs in self.rows:
            error = abs(
                sum(coefficient * probability[column]
                    for column, coefficient in entries) - rhs
            )
            residuals[kind] = max(residuals.get(kind, Fraction(0)), error)
        return {kind: str(value) for kind, value in residuals.items()}

    def exact_correlators(self, probability: list[Fraction]):
        correlators = [
            [Fraction(0) for _ in range(4)] for _ in range(self.k)
        ]
        denominator = 1 << (self.k - 1)
        for x in (0, 1):
            for yi, y in enumerate(self.bits):
                for a in (0, 1):
                    for bi, b in enumerate(self.bits):
                        value = probability[self.index(x, yi, a, bi)]
                        if not value:
                            continue
                        for i in range(self.k):
                            correlators[i][2 * x + y[i]] += (
                                Fraction((-1) ** (a + b[i]), denominator) * value
                            )
        return correlators

    def exact_potentials(self, probability: list[Fraction]) -> list[Fraction]:
        """Compute M_i from separate conditional Alice means, without A0,A1."""
        potentials = []
        for prefix in range(self.k + 1):
            value = Fraction(0)
            for yp in itertools.product((0, 1), repeat=prefix):
                # Joint TONS makes the chosen future input completion irrelevant.
                yi = self.bit_index[yp + (0,) * (self.k - prefix)]
                for bp in itertools.product((0, 1), repeat=prefix):
                    bs = [
                        bi for bi, b in enumerate(self.bits)
                        if b[:prefix] == bp
                    ]
                    numerators = [
                        sum(
                            (-1) ** a * probability[self.index(x, yi, a, bi)]
                            for a in (0, 1) for bi in bs
                        )
                        for x in (0, 1)
                    ]
                    # Common Bob-history probabilities cancel the conditional
                    # denominator in p(h) * max_x |E[A | x,h]|.
                    value += max(abs(n) for n in numerators) / (1 << prefix)
            potentials.append(value)
        return potentials

    def consumption_kernel(self, j: int) -> list[Fraction]:
        """P^(j), with j counted from one as in science/attainment.md."""
        out = [Fraction(0)] * self.n_variables
        stage = j - 1
        for x in (0, 1):
            for yi, y in enumerate(self.bits):
                for a in (0, 1):
                    for bi, b in enumerate(self.bits):
                        if (
                            b[stage] == (a ^ (x * y[stage]))
                            and all(z == b[stage] for z in b[stage + 1:])
                        ):
                            out[self.index(x, yi, a, bi)] = Fraction(1, 1 << j)
        return out

    def simplex_kernel(self, gaps: list[Fraction]):
        weights = [Fraction(0)] * self.k
        future = Fraction(0)
        for i in range(self.k - 1, -1, -1):
            weights[i] = gaps[i] / 2 + future
            future += weights[i]
        local_weight = 1 - sum(weights)
        if local_weight < 0 or min(weights) < 0:
            raise ValueError("Requested gaps are outside the nonnegative simplex.")

        out = [Fraction(0)] * self.n_variables
        for j, weight in enumerate(weights, start=1):
            if weight:
                component = self.consumption_kernel(j)
                out = [p + weight * q for p, q in zip(out, component)]
        zero_output = self.bit_index[(0,) * self.k]
        for x in (0, 1):
            for yi in range(self.side):
                out[self.index(x, yi, 0, zero_output)] += local_weight
        return out, weights, local_weight


def exact_kernel_check(problem: TONSProblem, probability, expected_scores):
    correlators = problem.exact_correlators(probability)
    orientation_scores = [
        [
            sum(Fraction(c) * e for c, e in zip(signs, values))
            for signs in ORIENTATIONS
        ]
        for values in correlators
    ]
    scores = [max(values) for values in orientation_scores]
    m = problem.exact_potentials(probability)
    r = [1 - value for value in m]
    residuals = problem.exact_residuals(probability)

    one_step = all(
        value <= 4 * m[i + 1] - 2 * m[i]
        for i, values in enumerate(orientation_scores)
        for value in values
    )
    weighted = sum(
        2**i * (value - 2) for i, value in enumerate(scores)
    )
    subsequences = 0
    subsequence_bounds = True
    for length in range(1, problem.k + 1):
        for selected in itertools.combinations(range(problem.k), length):
            lhs = sum(
                2**rank * (scores[index] - 2)
                for rank, index in enumerate(selected)
            )
            lhs += 2 ** (length + 1) * r[selected[-1] + 1]
            subsequence_bounds &= lhs <= 2 * r[0]
            subsequences += 1

    checks = {
        "nonnegative": min(probability) >= 0,
        "all_joint_tons_equalities": all(
            Fraction(value) == 0 for value in residuals.values()
        ),
        "all_maximal_chsh_values_match": scores == expected_scores,
        "potential_in_unit_interval": all(0 <= value <= 1 for value in m),
        "potential_nondecreasing": all(a <= b for a, b in zip(m, m[1:])),
        "all_eight_orientations_obey_one_step_bound": one_step,
        "refined_weighted_bound": (
            weighted + 2 ** (problem.k + 1) * r[-1] <= 2 * r[0]
        ),
        "all_selected_subsequence_bounds": subsequence_bounds,
    }
    return {
        "checks": checks,
        "passed": all(checks.values()),
        "maximal_chsh_values": [str(value) for value in scores],
        "potentials_M": [str(value) for value in m],
        "initial_R": str(r[0]),
        "final_R": str(r[-1]),
        "weighted_gap": str(weighted),
        "max_exact_residual_by_constraint": residuals,
        "selected_subsequences_checked": subsequences,
    }


def hardy_parameters(gaps: list[Fraction]):
    q = Fraction(1)
    ps, qs = [], [q]
    feasible = True
    reproduced = []
    for gap in gaps:
        if q:
            p = gap / (2 * q)
        else:
            feasible &= gap == 0
            p = Fraction(0)
        feasible &= 0 <= p <= 1
        reproduced.append(2 * q * p)
        ps.append(p)
        q = q * (1 - p) / 2
        feasible &= q >= 0
        qs.append(q)
    return {
        "feasible": feasible,
        "gaps_reproduced": reproduced == gaps,
        "p": [str(value) for value in ps],
        "q": [str(value) for value in qs],
    }


def exact_profiles(problem: TONSProblem):
    k = problem.k
    profiles = [
        ("local_vertex", [Fraction(0)] * k),
        ("fair_boundary", [Fraction(2, 2**k - 1)] * k),
        ("positive_interior", [Fraction(1, k * 2**i) for i in range(k)]),
    ]
    for selected in range(k):
        gaps = [Fraction(0)] * k
        gaps[selected] = Fraction(2, 2**selected)
        profiles.append((f"axis_{selected + 1}", gaps))

    reports = []
    for name, gaps in profiles:
        probability, weights, local_weight = problem.simplex_kernel(gaps)
        report = exact_kernel_check(
            problem, probability, [2 + gap for gap in gaps]
        )
        parameters = hardy_parameters(gaps)
        report.update(
            {
                "profile": name,
                "target_gaps": [str(gap) for gap in gaps],
                "consumption_weights": [str(weight) for weight in weights],
                "local_weight": str(local_weight),
                "hardy_parameters": parameters,
            }
        )
        report["passed"] &= (
            parameters["feasible"] and parameters["gaps_reproduced"]
        )
        reports.append(report)
    return reports


def lp_record(result, a_eq, b_eq, expected, tolerance, scores=None):
    if not result.success:
        return {
            "passed": False,
            "status": int(result.status),
            "message": result.message,
        }
    value = float(-result.fun)
    eq_residual = float(np.max(np.abs(a_eq @ result.x - b_eq)))
    probabilities = result.x if scores is None else result.x[:-1]
    minimum = float(np.min(probabilities))
    score_slack = None
    if scores is not None:
        score_slack = float(
            np.min(scores @ probabilities - 2 - result.x[-1])
        )
    passed = (
        abs(value - float(expected)) <= tolerance
        and eq_residual <= tolerance
        and minimum >= -tolerance
        and (score_slack is None or score_slack >= -tolerance)
    )
    return {
        "passed": bool(passed),
        "status": int(result.status),
        "message": result.message,
        "optimum": value,
        "expected_exact": str(expected),
        "objective_error": abs(value - float(expected)),
        "max_equality_residual": eq_residual,
        "minimum_probability": minimum,
        "minimum_fair_gap_slack": score_slack,
    }


def solve_linear_programs(problem: TONSProblem, expected, tolerance):
    k, nv = problem.k, problem.n_variables
    weights = 2.0 ** np.arange(k)
    objective = weights @ problem.scores
    weighted = linprog(
        -objective,
        A_eq=problem.a_eq,
        b_eq=problem.b_eq,
        bounds=(0, None),
        method="highs",
    )

    fair_a_eq = hstack(
        [problem.a_eq, csr_matrix((len(problem.rows), 1))], format="csr"
    )
    fair_a_ub = hstack(
        [-csr_matrix(problem.scores), csr_matrix(np.ones((k, 1)))],
        format="csr",
    )
    fair = linprog(
        np.r_[np.zeros(nv), -1.0],
        A_eq=fair_a_eq,
        b_eq=problem.b_eq,
        A_ub=fair_a_ub,
        b_ub=-2 * np.ones(k),
        bounds=[(0, None)] * nv + [(None, None)],
        method="highs",
    )

    # A separate LP fixes both Alice means to 1/2, so R0=1/2.
    bias_rows = np.zeros((2, nv))
    for x in (0, 1):
        for a in (0, 1):
            for bi in range(problem.side):
                bias_rows[x, problem.index(x, 0, a, bi)] = (-1) ** a
    biased_a_eq = vstack(
        [problem.a_eq, csr_matrix(bias_rows)], format="csr"
    )
    biased_b_eq = np.r_[problem.b_eq, 0.5, 0.5]
    biased = linprog(
        -objective,
        A_eq=biased_a_eq,
        b_eq=biased_b_eq,
        bounds=(0, None),
        method="highs",
    )

    return {
        "weighted_chsh": lp_record(
            weighted, problem.a_eq, problem.b_eq,
            Fraction(expected["max_weighted_chsh"]), tolerance,
        ),
        "fair_gap": lp_record(
            fair, fair_a_eq, problem.b_eq,
            Fraction(expected["fair_gap"]), tolerance, problem.scores,
        ),
        "weighted_chsh_with_alice_bias_half": lp_record(
            biased, biased_a_eq, biased_b_eq,
            Fraction(expected["max_weighted_chsh_with_bias_half"]), tolerance,
        ),
    }


def boundary_fixtures():
    problem = TONSProblem(2)
    signed = exact_kernel_check(
        problem, problem.consumption_kernel(2), [Fraction(0), Fraction(4)]
    )
    signed_scores = [Fraction(value) for value in signed["maximal_chsh_values"]]
    positive_part = sum(
        2**i * max(Fraction(0), score - 2)
        for i, score in enumerate(signed_scores)
    )
    signed["positive_part_weighted_sum"] = str(positive_part)
    signed["signed_weighted_sum"] = signed["weighted_gap"]
    signed["invalid_positive_part_replacement_detected"] = positive_part > 2
    signed["passed"] &= positive_part > 2

    broadcast_pr = [Fraction(0)] * problem.n_variables
    future_pr = [Fraction(0)] * problem.n_variables
    for x in (0, 1):
        for yi, y in enumerate(problem.bits):
            for a in (0, 1):
                for bi, b in enumerate(problem.bits):
                    column = problem.index(x, yi, a, bi)
                    if all(b[i] == (a ^ (x * y[i])) for i in range(2)):
                        broadcast_pr[column] = Fraction(1, 2)
                    if b[0] == b[1] and a ^ b[1] == x * y[1]:
                        future_pr[column] = Fraction(1, 2)

    broadcast_errors = problem.exact_residuals(broadcast_pr)
    future_errors = problem.exact_residuals(future_pr)
    broadcast_correlators = problem.exact_correlators(broadcast_pr)
    broadcast_scores = [
        max(sum(Fraction(c) * e for c, e in zip(signs, values))
            for signs in ORIENTATIONS)
        for values in broadcast_correlators
    ]
    future_correlators = problem.exact_correlators(future_pr)
    future_scores = [
        max(sum(Fraction(c) * e for c, e in zip(signs, values))
            for signs in ORIENTATIONS)
        for values in future_correlators
    ]
    bob_record_is_input_independent = all(
        sum(future_pr[problem.index(x, yi, a, bi)] for a in (0, 1))
        == sum(future_pr[problem.index(0, 0, a, bi)] for a in (0, 1))
        for x in (0, 1)
        for yi in range(problem.side)
        for bi in range(problem.side)
    )
    broadcast_checks = {
        "normalized": Fraction(broadcast_errors["normalization"]) == 0,
        "both_marginal_chsh_values_are_4": broadcast_scores == [4, 4],
        "joint_alice_to_bobs_constraint_rejects": (
            Fraction(broadcast_errors["alice_to_all_bobs"]) > 0
        ),
    }
    future_checks = {
        "normalized": Fraction(future_errors["normalization"]) == 0,
        "whole_bob_string_is_independent_of_alice": (
            Fraction(future_errors["alice_to_all_bobs"]) == 0
        ),
        "whole_bob_string_is_independent_of_all_settings": (
            bob_record_is_input_independent
        ),
        "marginal_chsh_values_are_2_and_4": future_scores == [2, 4],
        "joint_alice_prefix_constraint_rejects": (
            Fraction(
                future_errors["alice_and_prefix_no_future_input"]
            ) > 0
        ),
    }
    return {
        "valid_signed_gap_example": signed,
        "pairwise_pr_tables_do_not_imply_joint_tons": {
            "checks": broadcast_checks,
            "passed": all(broadcast_checks.values()),
            "max_exact_residual_by_constraint": broadcast_errors,
        },
        "bob_only_time_ordering_is_insufficient": {
            "checks": future_checks,
            "passed": all(future_checks.values()),
            "max_exact_residual_by_constraint": future_errors,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-k", type=int, default=5)
    parser.add_argument(
        "--expected", type=Path,
        default=Path(__file__).parent / "expected" / "tons.json",
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    expected = json.loads(args.expected.read_text())
    expected_cases = {case["k"]: case for case in expected["cases"]}
    if not 1 <= args.max_k <= max(expected_cases):
        parser.error("max-k must lie within the archived expected cases.")

    cases = []
    tolerance = float(expected["floating_tolerance"])
    for k in range(1, args.max_k + 1):
        problem = TONSProblem(k)
        reference = expected_cases[k]
        dimensions_match = (
            problem.n_variables == reference["variables"]
            and len(problem.rows) == reference["equalities"]
        )
        exact = exact_profiles(problem)
        linear_programs = solve_linear_programs(
            problem, reference, tolerance
        )
        case_passed = (
            dimensions_match
            and all(item["passed"] for item in exact)
            and all(item["passed"] for item in linear_programs.values())
        )
        cases.append(
            {
                "k": k,
                "variables": problem.n_variables,
                "equalities": len(problem.rows),
                "constraint_counts": dict(
                    Counter(kind for kind, _, _ in problem.rows)
                ),
                "archived_dimensions_match": dimensions_match,
                "exact_profiles": exact,
                "linear_programs": linear_programs,
                "passed": case_passed,
            }
        )
    boundaries = boundary_fixtures()
    passed = (
        all(case["passed"] for case in cases)
        and all(case["passed"] for case in boundaries.values())
    )
    report = {
        "schema_version": 1,
        "scope": (
            "Exact rational finite kernels and full finite TONS LPs. "
            "The arbitrary-K theorem is analytic; these checks do not "
            "establish historical priority or exact quantum attainability."
        ),
        "environment": {
            "python": platform.python_version(),
            "numpy": np.__version__,
            "scipy": scipy.__version__,
        },
        "source_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "expected_sha256": hashlib.sha256(args.expected.read_bytes()).hexdigest(),
        "orientation_count": len(ORIENTATIONS),
        "floating_tolerance": tolerance,
        "cases": cases,
        "boundary_fixtures": boundaries,
        "status": "pass" if passed else "fail",
        "all_passed": passed,
    }
    payload = json.dumps(report, indent=2, allow_nan=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload)
    print(payload, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

