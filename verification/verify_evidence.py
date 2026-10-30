#!/usr/bin/env python3
"""Numerical checks of the analytical evidence theorems.

Requires numpy and scipy. All information quantities use natural logarithms.
The default invocation writes one JSON report to stdout and creates no files.
Use --output PATH only to request an additional report file explicitly.

Checks:
* KL optimization over all 16 binary Bell-local deterministic vertices, with
  primal feasibility and a convex first-order global optimality-gap bound;
* an analytic CHSH-symmetric KL example, all relabellings, and Fine whitening;
* Shannon and pure-branch Holevo budgets for sequential quantum instruments,
  including correlated externally generated settings;
* repeated common-setting measurements and a masked full-record example;
* the finite-n formula and its consistent logarithm units.

Finite computations corroborate the proofs in science/. They do not prove
priority, optimal quantum statistical complexity, or arbitrary-dimensional
entanglement-of-formation formulas.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import itertools
import json
import math
from pathlib import Path
from typing import Callable

import numpy as np
import scipy
from scipy.optimize import linprog, minimize


SEED = 20261030
ATOL = 2e-9
GAP_TOL = 5e-7
I2 = np.eye(2, dtype=complex)
PAULI_X = np.array([[0, 1], [1, 0]], dtype=complex)
PAULI_Z = np.diag([1.0, -1.0]).astype(complex)
BITS = tuple(itertools.product(range(2), repeat=4))


def entropy(probabilities: np.ndarray | list[float]) -> float:
    p = np.asarray(probabilities, dtype=float)
    if np.min(p, initial=0.0) < -1e-10:
        raise AssertionError("Negative probability in entropy.")
    p = np.maximum(p, 0.0)
    mask = p > 0.0
    return float(-np.sum(p[mask] * np.log(p[mask])))


def binary_kl(s: float, t: float) -> float:
    if not (0.0 < s < 1.0 and 0.0 < t < 1.0):
        raise ValueError("This verifier uses interior binary probabilities.")
    return s * math.log(s / t) + (1.0 - s) * math.log((1.0 - s) / (1.0 - t))


def conditional_kl(p: np.ndarray, q: np.ndarray, setting_law: np.ndarray) -> float:
    """Weighted KL between conditional output tables of shape (x,y,a,b)."""
    mask = p > 0.0
    if np.any(q[mask] <= 0.0):
        return math.inf
    weight = np.broadcast_to(setting_law[:, :, None, None], p.shape)
    return float(np.sum(weight[mask] * p[mask] * np.log(p[mask] / q[mask])))


def assert_behavior(p: np.ndarray) -> None:
    assert p.shape == (2, 2, 2, 2)
    assert np.min(p) >= -ATOL
    assert np.max(np.abs(p.sum(axis=(2, 3)) - 1.0)) < ATOL
    alice = p.sum(axis=3)
    bob = p.sum(axis=2)
    assert np.max(np.abs(alice[:, 0, :] - alice[:, 1, :])) < ATOL
    assert np.max(np.abs(bob[0, :, :] - bob[1, :, :])) < ATOL


LOCAL_VERTICES = []
for a0, a1, b0, b1 in BITS:
    table = np.zeros((2, 2, 2, 2))
    for x, y in itertools.product(range(2), repeat=2):
        table[x, y, (a0, a1)[x], (b0, b1)[y]] = 1.0
    LOCAL_VERTICES.append(table)
LOCAL_VERTICES = np.stack(LOCAL_VERTICES)
V = LOCAL_VERTICES.reshape(16, 16).T
CHSH_ORIENTATIONS = np.array(
    [signs for signs in itertools.product((-1.0, 1.0), repeat=4)
     if np.prod(signs) == -1.0]
).reshape(8, 2, 2)
UNIFORM = np.full((2, 2, 2, 2), 0.25)
UNIFORM_INPUTS = np.full((2, 2), 0.25)


def correlators(p: np.ndarray) -> np.ndarray:
    signs = np.array([[1.0, -1.0], [-1.0, 1.0]])
    return np.einsum("xyab,ab->xy", p, signs)


def chsh_values(p: np.ndarray) -> np.ndarray:
    return np.einsum("kxy,xy->k", CHSH_ORIENTATIONS, correlators(p))


def maximum_chsh(p: np.ndarray) -> float:
    return float(np.max(chsh_values(p)))


def isotropic_box(correlation: float) -> np.ndarray:
    table = np.zeros((2, 2, 2, 2))
    for x, y, a, b in BITS:
        table[x, y, a, b] = (
            1.0 + correlation * (-1.0) ** (a + b + x * y)
        ) / 4.0
    assert_behavior(table)
    return table


def pr_box(alpha: int, beta: int, gamma: int) -> np.ndarray:
    table = np.zeros((2, 2, 2, 2))
    for x, y, a, b in BITS:
        if (a ^ b) == ((x * y) ^ (alpha * x) ^ (beta * y) ^ gamma):
            table[x, y, a, b] = 0.5
    assert_behavior(table)
    return table


PR_VERTICES = np.stack(
    [pr_box(*parameters) for parameters in itertools.product(range(2), repeat=3)]
)


def local_kl(p: np.ndarray, setting_law: np.ndarray = UNIFORM_INPUTS) -> dict:
    """Minimize actual-design KL and certify the convex optimization gap.

    For a convex differentiable f on the probability simplex, the value
    <lambda,grad f>-min_j grad_j f upper-bounds f(lambda)-min f.
    Thus optimizer success alone is not used as a certificate.
    """
    assert_behavior(p)
    assert setting_law.shape == (2, 2)
    assert np.min(setting_law) > 0.0
    assert abs(float(setting_law.sum()) - 1.0) < ATOL
    flat = p.ravel()
    local = linprog(
        np.zeros(16),
        A_eq=np.vstack((V, np.ones(16))),
        b_eq=np.concatenate((flat, [1.0])),
        bounds=(0.0, None),
        method="highs",
    )
    if local.success:
        residual = float(max(
            np.max(np.abs(V @ local.x - flat)),
            abs(local.x.sum() - 1.0),
            max(0.0, -float(local.x.min())),
        ))
        if residual < 5e-11:
            return {
                "nu_nats": 0.0,
                "convex_optimality_gap_nats": 0.0,
                "locality_feasibility_residual": residual,
                "method": "local_feasibility",
            }

    weight = np.broadcast_to(setting_law[:, :, None, None], p.shape).ravel()
    observed = weight * flat
    positive = flat > 0.0

    def objective(lam: np.ndarray) -> float:
        q = np.maximum(V @ lam, 1e-15)
        return float(np.sum(
            observed[positive] * np.log(flat[positive] / q[positive])
        ))

    def gradient(lam: np.ndarray) -> np.ndarray:
        q = np.maximum(V @ lam, 1e-15)
        return -(V.T @ (observed / q))

    initial = np.full(16, 1.0 / 16.0)
    last_message = ""
    for _ in range(2):
        opt = minimize(
            objective,
            initial,
            jac=gradient,
            method="SLSQP",
            bounds=[(0.0, 1.0)] * 16,
            # The tiny support floor stabilizes intermediate numerical steps.
            # The final gap is still computed against the unrestricted simplex,
            # so the auxiliary constraint cannot hide a suboptimal solution.
            constraints=[
                {
                    "type": "eq",
                    "fun": lambda lam: lam.sum() - 1.0,
                    "jac": lambda lam: np.ones(16),
                },
                {
                    "type": "ineq",
                    "fun": lambda lam: V[positive] @ lam - 1e-10,
                    "jac": lambda lam: V[positive],
                },
            ],
            options={"ftol": 1e-13, "maxiter": 3000},
        )
        lam = np.maximum(opt.x, 0.0)
        lam /= lam.sum()
        q = V @ lam
        if np.any(q[positive] <= 0.0):
            raise AssertionError("KL candidate has zero mass on observed support.")
        grad = gradient(lam)
        gap = float(np.dot(lam, grad) - grad.min())
        primal = float(max(abs(lam.sum() - 1.0), max(0.0, -float(lam.min()))))
        value = objective(lam)
        last_message = f"{opt.message}; primal={primal}; convex gap={gap}"
        if primal < ATOL and -ATOL <= gap <= GAP_TOL and opt.success:
            assert value >= -ATOL
            return {
                "nu_nats": max(0.0, value),
                "convex_optimality_gap_nats": max(0.0, gap),
                "simplex_feasibility_residual": primal,
                "method": "convex_kl",
            }
        initial = 0.999 * lam + 0.001 / 16.0
    raise AssertionError("Uncertified KL optimization: " + last_message)


def whitening(p: np.ndarray, setting_law: np.ndarray) -> tuple[np.ndarray, float]:
    s = maximum_chsh(p)
    if s <= 2.0:
        return p.copy(), 0.0
    t = 2.0 / s
    q = t * p + (1.0 - t) * UNIFORM
    assert_behavior(q)
    assert maximum_chsh(q) <= 2.0 + ATOL
    bound = math.log(s / 2.0)
    assert conditional_kl(p, q, setting_law) <= bound + ATOL
    return q, bound


def relabel(p: np.ndarray, parameters: tuple[int, ...]) -> np.ndarray:
    swap_a, swap_b, flip_a0, flip_a1, flip_b0, flip_b1 = parameters
    flips_a = (flip_a0, flip_a1)
    flips_b = (flip_b0, flip_b1)
    result = np.zeros_like(p)
    for x, y, a, b in BITS:
        result[x, y, a, b] = p[
            x ^ swap_a, y ^ swap_b, a ^ flips_a[x], b ^ flips_b[y]
        ]
    return result


def alice_reduction(psi: np.ndarray) -> np.ndarray:
    matrix = psi.reshape(2, 2)
    return matrix @ matrix.conj().T


def effects(angle: float, strength: float) -> list[np.ndarray]:
    effect = (
        I2 + strength * (math.cos(angle) * PAULI_Z + math.sin(angle) * PAULI_X)
    ) / 2.0
    return [effect, I2 - effect]


def positive_square_root(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    assert values.min() >= -ATOL
    return (vectors * np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T


@dataclass
class Branch:
    weight: float
    state: np.ndarray
    settings: tuple[int, ...]


InputPolicy = Callable[[int, tuple[int, ...]], np.ndarray]


def independent_inputs(stage: int, settings: tuple[int, ...]) -> np.ndarray:
    return np.array([0.5, 0.5])


def common_input(stage: int, settings: tuple[int, ...]) -> np.ndarray:
    if stage == 0:
        return np.array([0.5, 0.5])
    return np.array([float(settings[0] == 0), float(settings[0] == 1)])


def markov_inputs(stage: int, settings: tuple[int, ...]) -> np.ndarray:
    if stage == 0:
        return np.array([0.5, 0.5])
    return np.array([0.8, 0.2]) if settings[-1] == 0 else np.array([0.2, 0.8])


def analyze_quantum_chain(
    alice_angles: list[float],
    bob_specs: list[list[tuple[float, float]]],
    theta: float = math.pi / 4.0,
    input_policy: InputPolicy = independent_inputs,
    mu_x: np.ndarray | None = None,
) -> dict:
    """Born-rule tree with one pure initial state and one Kraus operator/outcome.

    Distinct branch objects retain the complete hidden outcome history even
    though only their setting tuples are needed by the external input policy.
    That policy cannot depend on outcomes or future settings.
    """
    if mu_x is None:
        mu_x = np.array([0.5, 0.5])
    assert np.min(mu_x) > 0.0 and abs(mu_x.sum() - 1.0) < ATOL
    psi = np.array([math.cos(theta), 0.0, 0.0, math.sin(theta)], dtype=complex)
    branches = [Branch(1.0, psi, ())]
    alice = [effects(angle, 1.0) for angle in alice_angles]

    def statistics(items: list[Branch]) -> tuple[float, float]:
        entanglement = 0.0
        conditional_entropy = 0.0
        for branch in items:
            rho = alice_reduction(branch.state)
            entanglement += branch.weight * entropy(np.linalg.eigvalsh(rho))
            conditional_entropy += branch.weight * sum(
                mu_x[x] * entropy([float(np.trace(e @ rho).real) for e in alice[x]])
                for x in range(2)
            )
        return entanglement, conditional_entropy

    initial_entanglement, initial_entropy = statistics(branches)
    stages = []
    tc_total = 0.0
    for index, spec in enumerate(bob_specs):
        e_before, h_before = statistics(branches)
        bob = [effects(angle, strength) for angle, strength in spec]
        kraus = [[positive_square_root(e) for e in measurement] for measurement in bob]
        observed = np.zeros((2, 2, 2, 2))
        mu_y = np.zeros(2)
        conditional_setting_entropy = 0.0
        children = []
        for branch in branches:
            law = input_policy(index, branch.settings)
            assert np.min(law) >= 0.0 and abs(law.sum() - 1.0) < ATOL
            mu_y += branch.weight * law
            conditional_setting_entropy += branch.weight * entropy(law)
            for y, b in itertools.product(range(2), repeat=2):
                if law[y] == 0.0:
                    continue
                child = np.kron(I2, kraus[y][b]) @ branch.state
                probability = float(np.vdot(child, child).real)
                if probability < 1e-14:
                    continue
                child /= math.sqrt(probability)
                weight = branch.weight * law[y] * probability
                children.append(Branch(weight, child, branch.settings + (y,)))
                rho = alice_reduction(child)
                for x, a in itertools.product(range(2), repeat=2):
                    observed[x, y, a, b] += (
                        weight * mu_x[x] * float(np.trace(alice[x][a] @ rho).real)
                    )
        assert abs(sum(b.weight for b in children) - 1.0) < ATOL
        assert abs(observed.sum() - 1.0) < ATOL
        assert np.min(mu_y) > 0.0
        design = np.outer(mu_x, mu_y)
        behavior = observed / design[:, :, None, None]
        assert_behavior(behavior)
        kl = local_kl(behavior, design)
        _, white_bound = whitening(behavior, design)
        branches = children
        e_after, h_after = statistics(branches)
        tc_increment = entropy(mu_y) - conditional_setting_entropy
        assert tc_increment >= -ATOL
        tc_increment = max(0.0, tc_increment)
        tc_total += tc_increment
        classical_drop = h_before - h_after
        quantum_drop = e_before - e_after
        assert classical_drop >= -ATOL
        assert quantum_drop >= -ATOL
        assert kl["nu_nats"] <= tc_increment + classical_drop + 2e-7
        assert kl["nu_nats"] <= tc_increment + quantum_drop + 2e-7
        if maximum_chsh(behavior) > 2.0:
            assert kl["nu_nats"] <= white_bound + 2e-7
        stages.append({
            **kl,
            "maximum_CHSH": maximum_chsh(behavior),
            "setting_information_nats": tc_increment,
            "classical_entropy_drop_nats": classical_drop,
            "pure_branch_entanglement_drop_nats": quantum_drop,
        })
    final_entanglement, final_entropy = statistics(branches)
    sum_kl = sum(stage["nu_nats"] for stage in stages)
    classical_slack = initial_entropy + tc_total - final_entropy - sum_kl
    quantum_slack = initial_entanglement + tc_total - final_entanglement - sum_kl
    assert classical_slack >= -2e-7
    assert quantum_slack >= -2e-7
    return {
        "initial_alice_entropy_nats": initial_entropy,
        "final_alice_conditional_entropy_nats": final_entropy,
        "initial_entanglement_nats": initial_entanglement,
        "final_pure_branch_entanglement_nats": final_entanglement,
        "setting_total_correlation_nats": tc_total,
        "sum_nu_nats": sum_kl,
        "classical_budget_slack_nats": classical_slack,
        "quantum_budget_slack_nats": quantum_slack,
        "stages": stages,
    }


def masked_record_check() -> dict:
    """A valid quantum TONS behavior with local pairs and nonlocal decoded record."""
    base = isotropic_box(1.0 / math.sqrt(2.0))
    # Axes x,y1,y2,a,b1,b2. Bob1's fair bit masks Bob2's CHSH outcome.
    full = np.zeros((2,) * 6)
    for x, y1, y2, a, b1, b2 in itertools.product(range(2), repeat=6):
        full[x, y1, y2, a, b1, b2] = 0.5 * base[x, y2, a, b1 ^ b2]
    assert np.max(np.abs(full.sum(axis=(3, 4, 5)) - 1.0)) < ATOL
    bob_string = full.sum(axis=3)
    assert np.max(np.abs(bob_string[0] - bob_string[1])) < ATOL
    prefix = full.sum(axis=5)
    assert np.max(np.abs(prefix[:, :, 0] - prefix[:, :, 1])) < ATOL
    first = full.sum(axis=5).mean(axis=2)
    second = full.sum(axis=4).mean(axis=1)
    assert_behavior(first)
    assert_behavior(second)
    assert np.max(np.abs(first - UNIFORM)) < ATOL
    assert np.max(np.abs(second - UNIFORM)) < ATOL
    decoded = np.zeros_like(base)
    for x, y1, y2, a, b1, b2 in itertools.product(range(2), repeat=6):
        decoded[x, y2, a, b1 ^ b2] += 0.5 * full[x, y1, y2, a, b1, b2]
    assert np.max(np.abs(decoded - base)) < ATOL
    return {
        "first_marginal_nu_nats": local_kl(first)["nu_nats"],
        "second_marginal_nu_nats": local_kl(second)["nu_nats"],
        "decoded_CHSH": maximum_chsh(decoded),
    }


def run_checks() -> dict:
    rng = np.random.default_rng(SEED)
    optimizer_records = []
    analytic = []
    for correlation in (0.4, 0.8 / math.sqrt(2.0), 1.0 / math.sqrt(2.0), 1.0):
        box = isotropic_box(correlation)
        result = local_kl(box)
        optimizer_records.append(result)
        win = (1.0 + correlation) / 2.0
        if correlation <= 0.5:
            expected = 0.0
        elif correlation == 1.0:
            expected = math.log(4.0 / 3.0)
        else:
            expected = binary_kl(win, 0.75)
        assert abs(result["nu_nats"] - expected) < 3e-8
        analytic.append({
            "correlation": correlation,
            "maximum_CHSH": maximum_chsh(box),
            "analytic_nu_nats": expected,
            **result,
        })

    # Relabelling invariance of S_max and validity of whitening at a biased design.
    biased_design = np.outer([0.3, 0.7], [0.5, 0.5])
    reference = isotropic_box(1.0 / math.sqrt(2.0))
    relabelling_count = 0
    for parameters in itertools.product(range(2), repeat=6):
        box = relabel(reference, parameters)
        assert_behavior(box)
        assert abs(maximum_chsh(box) - 2.0 * math.sqrt(2.0)) < ATOL
        white, _ = whitening(box, biased_design)
        assert maximum_chsh(white) <= 2.0 + ATOL
        relabelling_count += 1

    ns_boxes = []
    for index in range(12):
        local_mix = np.einsum("i,ixyab->xyab", rng.dirichlet(np.ones(16)), LOCAL_VERTICES)
        strength = float(rng.uniform(0.55, 0.98))
        box = strength * PR_VERTICES[index % 8] + (1.0 - strength) * local_mix
        assert_behavior(box)
        result = local_kl(box, biased_design)
        optimizer_records.append(result)
        white, white_bound = whitening(box, biased_design)
        white_result = local_kl(white, biased_design)
        assert white_result["nu_nats"] < 1e-10
        assert result["nu_nats"] <= white_bound + ATOL
        ns_boxes.append({
            "maximum_CHSH": maximum_chsh(box),
            "whitening_upper_bound_nats": white_bound,
            **result,
        })

    two_bob = analyze_quantum_chain(
        [0.0, math.pi / 2.0],
        [
            [(math.pi / 4.0, 0.8), (-math.pi / 4.0, 0.8)],
            [(math.pi / 4.0, 1.0), (-math.pi / 4.0, 1.0)],
        ],
    )
    expected_two = binary_kl((1.0 + 0.8 / math.sqrt(2.0)) / 2.0, 0.75)
    for stage in two_bob["stages"]:
        assert abs(stage["nu_nats"] - expected_two) < 3e-8
        assert abs(stage["maximum_CHSH"] - 1.6 * math.sqrt(2.0)) < ATOL
        optimizer_records.append(stage)

    random_chains = []
    for index in range(12):
        alice = rng.uniform(-math.pi, math.pi, 2).tolist()
        specs = [
            list(zip(rng.uniform(-math.pi, math.pi, 2), rng.uniform(0.05, 0.99, 2)))
            for _ in range(3)
        ]
        chain = analyze_quantum_chain(
            alice, specs, float(rng.uniform(0.1, math.pi / 4.0)),
            markov_inputs if index % 2 else independent_inputs,
            np.array([0.3, 0.7]) if index % 3 else np.array([0.5, 0.5]),
        )
        random_chains.append(chain)
        optimizer_records.extend(chain["stages"])

    repeated_count = 32
    repeated = analyze_quantum_chain(
        [0.0, math.pi / 2.0],
        [[(math.pi / 4.0, 1.0), (-math.pi / 4.0, 1.0)]] * repeated_count,
        input_policy=common_input,
    )
    max_chsh_kl = binary_kl((2.0 + math.sqrt(2.0)) / 4.0, 0.75)
    assert abs(repeated["sum_nu_nats"] - repeated_count * max_chsh_kl) < 2e-7
    assert repeated["sum_nu_nats"] > math.log(2.0)
    assert abs(repeated["setting_total_correlation_nats"]
               - (repeated_count - 1) * math.log(2.0)) < ATOL
    assert all(abs(s["maximum_CHSH"] - 2 * math.sqrt(2.0)) < ATOL
               for s in repeated["stages"])
    optimizer_records.extend(repeated["stages"])

    alpha, beta = 0.05, 0.1
    c = binary_kl(1.0 - beta, alpha)
    sample_bounds = []
    for count in (1, 2, 4, 8, 12, 20):
        denominator = -math.log1p(-2.0 ** (-count))
        lower = c / denominator
        assert abs(
            denominator - math.log1p(1.0 / (2 ** count - 1))
        ) < 1e-14
        assert abs(
            (2 ** count - 1) * math.expm1(c / lower) - 1.0
        ) < 1e-10
        sample_bounds.append({
            "K": count,
            "continuous_lower_bound": lower,
            "integer_lower_bound": math.ceil(lower),
        })

    return {
        "status": "pass",
        "scope": "Finite numerical checks; analytical proofs are in science/.",
        "units": "nats",
        "seed": SEED,
        "dependencies": {"numpy": np.__version__, "scipy": scipy.__version__},
        "optimizer_gap_tolerance_nats": GAP_TOL,
        "max_convex_optimality_gap_nats": max(
            row["convex_optimality_gap_nats"] for row in optimizer_records
        ),
        "analytic_CHSH_checks": analytic,
        "CHSH_relabellings_checked": relabelling_count,
        "biased_design_whitening_cases": ns_boxes,
        "two_bob_quantum_example": two_bob,
        "random_quantum_chains": random_chains,
        "common_setting_boundary": repeated,
        "masked_record_example": masked_record_check(),
        "finite_sample_calibration": {
            "alpha": alpha, "beta": beta, "binary_KL_nats": c,
            "bounds": sample_bounds,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, help="Explicit optional JSON output path.")
    args = parser.parse_args()
    report = run_checks()
    encoded = json.dumps(report, indent=2, sort_keys=True, allow_nan=False)
    if args.output is not None:
        args.output.write_text(encoded + "\n", encoding="utf-8")
    print(encoded)


if __name__ == "__main__":
    main()
