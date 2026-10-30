#!/usr/bin/env python3
"""Verify the Hardy construction by direct quantum-instrument propagation.

The physical calculation starts with the state and projectors in
Steffinlongo--D'Alessandro--Renner, arXiv:2607.24700v1, Eqs. (9)--(10),
and implements their Section III classical-trit instrument table. It does
not update the scalar q/Z recurrence to obtain the simulated probabilities.

Every Alice--Bob marginal is compared, cell by cell, with the analytic
mixture in science/quantum-rate.md. Selected short chains are independently
enumerated as complete conditional transcripts and checked for TONS.

Run from any directory:
    python verification/verify_quantum_protocol.py

The checked-in expected file contains exact rational predictions. To
regenerate it after an intentional change, first run the physical checks:
    python verification/verify_quantum_protocol.py --write-expected

Requires Python >= 3.10 and NumPy. Tested with Python 3.12.14 / NumPy 2.3.5.
This is a finite numerical implementation check, not a proof of the
asymptotic theorem or a statistical-complexity calculation.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
import itertools
import json
from pathlib import Path

import numpy as np


ATOL = 2.0e-12
GAP_ATOL = 1.0e-13
GAP_RTOL = 1.0e-5
EXPECTED_PATH = Path(__file__).resolve().parent / "expected" / "quantum_protocol.json"
SOURCE_URL = "https://arxiv.org/pdf/2607.24700v1"
OUTCOMES = (1, -1)  # Array index 0 means +1; index 1 means -1.
NO, ZERO, ONE = range(3)
I2 = np.eye(2, dtype=complex)
I6 = np.eye(6, dtype=complex)

# Short-chain cases exercise distinct shapes and all history branches.
# Longer cases include the asymptotic schedule a=4/K while keeping the
# predicted positive margin well above double-precision roundoff.
CASE_SPECS = (
    (1, 1, 4, True),
    (2, 1, 1, True),
    (3, 1, 8, True),
    (4, 3, 1, True),
    (4, 1, 1, True),
    (6, 2, 3, False),
    (8, 1, 2, False),
    (12, 1, 3, False),
    (20, 1, 5, False),
)


def real_trace(matrix: np.ndarray) -> float:
    value = np.trace(matrix)
    if abs(value.imag) > ATOL:
        raise AssertionError(f"Unexpected imaginary trace: {value}")
    return float(value.real)


def require_close(actual: np.ndarray | float, expected: np.ndarray | float,
                  label: str, atol: float = ATOL, rtol: float = 0.0) -> float:
    actual_array = np.asarray(actual)
    expected_array = np.asarray(expected)
    error = float(np.max(np.abs(actual_array - expected_array)))
    if not np.allclose(actual_array, expected_array, atol=atol, rtol=rtol):
        raise AssertionError(f"{label}: maximum absolute error {error:.6g}")
    return error


def source_state_and_projectors(shape: float) -> tuple[np.ndarray, np.ndarray]:
    """Born-model inputs, rewritten from source Eqs. (9)--(10).

    a=cot(theta)^2/2, so |Psi>=(|00>+sqrt(a)|01>+sqrt(a)|10>)/sqrt(1+2a).
    The basis-1 plus vector is (|0>+sqrt(a)|1>)/sqrt(1+a).
    """
    if shape <= 0:
        raise ValueError("The quantum shape parameter must be positive.")
    ket = np.array([1.0, np.sqrt(shape), np.sqrt(shape), 0.0], dtype=complex)
    ket /= np.sqrt(1.0 + 2.0 * shape)
    rho_ab = np.outer(ket, ket.conj())
    plus_zero = np.array([1.0, 0.0], dtype=complex)
    plus_one = np.array([1.0, np.sqrt(shape)], dtype=complex)
    plus_one /= np.sqrt(1.0 + shape)
    projectors = np.zeros((2, 2, 2, 2), dtype=complex)
    for setting, plus in enumerate((plus_zero, plus_one)):
        projectors[setting, 0] = np.outer(plus, plus.conj())
        projectors[setting, 1] = I2 - projectors[setting, 0]
        require_close(projectors[setting].sum(axis=0), I2,
                      "projector completeness")
        for outcome in range(2):
            projector = projectors[setting, outcome]
            require_close(projector @ projector, projector,
                          "projector idempotence")
    require_close(real_trace(rho_ab), 1.0, "initial state normalization")
    return rho_ab, projectors


def flag_transition(new_flag: int, old_flag: int) -> np.ndarray:
    transition = np.zeros((3, 3), dtype=complex)
    transition[new_flag, old_flag] = 1.0
    return transition


def bob_instrument(projectors: np.ndarray, probability: float,
                   setting: int) -> dict[int, list[np.ndarray]]:
    """Outcome-labelled Kraus operators on B (qubit) times F (trit).

    The old flag is read in its classical basis. Distinct old flags and
    coin branches remain distinct Kraus labels, even when the reported
    outcome or the new flag agrees. This implements a classical control,
    not a coherent superposition of branches.
    """
    if not 0.0 <= probability <= 1.0:
        raise AssertionError("A mixing probability is outside [0,1].")
    operations: dict[int, list[np.ndarray]] = {0: [], 1: []}

    def add(outcome: int, operator: np.ndarray,
            new_flag: int, old_flag: int, weight: float = 1.0) -> None:
        operations[outcome].append(
            np.sqrt(weight) * np.kron(operator, flag_transition(new_flag, old_flag))
        )

    if setting == 0:
        for outcome in range(2):
            add(outcome, projectors[0, outcome], ZERO, NO)
            add(outcome, projectors[0, outcome], ZERO, ZERO)
        add(0, I2, ONE, ONE)  # Already measured in basis 1: output +1.
    elif setting == 1:
        for outcome in range(2):
            add(outcome, projectors[1, outcome], ONE, NO, probability)
            add(outcome, projectors[1, outcome], ONE, ONE)
        add(0, I2, NO, NO, 1.0 - probability)
        add(0, I2, ZERO, ZERO)  # Already measured in basis 0: output +1.
    else:
        raise ValueError("Bob's input must be binary.")

    completeness = sum(
        operator.conj().T @ operator
        for group in operations.values() for operator in group
    )
    require_close(completeness, I6, "instrument trace preservation")
    return operations


def lift_instrument(instrument: dict[int, list[np.ndarray]]) -> dict[int, list[np.ndarray]]:
    return {
        outcome: [np.kron(I2, operator) for operator in operators]
        for outcome, operators in instrument.items()
    }


def apply_operation(rho: np.ndarray, operators: list[np.ndarray]) -> np.ndarray:
    result = np.zeros_like(rho)
    for operator in operators:
        result += operator @ rho @ operator.conj().T
    return result


def analytic_base_table(shape: Fraction) -> np.ndarray:
    """Exact Hardy table for Eqs. (9)--(10), independent of matrix algebra.

    The source's Table I has alpha=beta=a*gamma and
    delta=epsilon=a/[(1+2a)(1+a)] for this symmetric quantum family.
    Array axes are x, y, Alice outcome, Bob outcome.
    """
    a = shape
    gamma = a * a / ((1 + 2 * a) * (1 + a) ** 2)
    beta = a * gamma
    d = a / ((1 + 2 * a) * (1 + a))
    table = np.empty((2, 2, 2, 2), dtype=float)
    table[0, 0] = [[float(1 / (1 + 2 * a)), float(a / (1 + 2 * a))],
                   [float(a / (1 + 2 * a)), 0.0]]
    table[0, 1] = [[float((1 + a) / (1 + 2 * a)), 0.0],
                   [float(d), float(beta + gamma)]]
    table[1, 0] = [[float((1 + a) / (1 + 2 * a)), float(d)],
                   [0.0, float(beta + gamma)]]
    table[1, 1] = [[float(1 - 2 * beta - gamma), float(beta)],
                   [float(beta), float(gamma)]]
    return table


def analytic_marginals(depth: int, shape: Fraction) -> np.ndarray:
    """Closed form from source Tables IV--VI and the solved allocation.

    No simulated density matrices or simulated flag weights are used here.
    """
    base = analytic_base_table(shape)
    alice = base[:, 0].sum(axis=-1)
    strategy_two = base.copy()
    strategy_two[:, 1, :, 0] = alice
    strategy_two[:, 1, :, 1] = 0.0
    strategy_three = base.copy()
    strategy_three[:, 0, :, 0] = alice
    strategy_three[:, 0, :, 1] = 0.0
    a = shape
    c = (1 + a) / ((2 + a) ** depth - 1)
    ratio = 1 + a / 2
    marginals = []
    for position in range(1, depth + 1):
        x_weight = c * ratio ** (position - 1)
        z_weight = c * (ratio ** (position - 1) - 1) / a
        marginals.append(float(x_weight) * base
                         + float(1 - x_weight - z_weight) * strategy_two
                         + float(z_weight) * strategy_three)
    return np.asarray(marginals)


def chsh_values(marginals: np.ndarray, source_orientation: bool = True) -> np.ndarray:
    signs = np.outer(OUTCOMES, OUTCOMES)
    correlators = np.einsum("ixyst,st->ixy", marginals, signs)
    coefficients = np.array([[-1, 1], [1, 1]]) if source_orientation else np.array([[1, 1], [1, -1]])
    return np.einsum("ixy,xy->i", correlators, coefficients)


def canonical_relabel(marginals: np.ndarray) -> np.ndarray:
    """Fresh canonical y uses source setting 1-y and reports (-1)^y b."""
    relabeled = np.empty_like(marginals)
    relabeled[:, :, 0] = marginals[:, :, 1]
    relabeled[:, :, 1] = marginals[:, :, 0, :, ::-1]
    return relabeled


def initial_with_flag(rho_ab: np.ndarray) -> np.ndarray:
    initial_flag = np.zeros((3, 3), dtype=complex)
    initial_flag[NO, NO] = 1.0
    return np.kron(rho_ab, initial_flag)


def born_marginals(depth: int, shape: Fraction, probabilities: list[Fraction]) -> tuple[np.ndarray, dict]:
    """Propagate the actual 12-dimensional state under complete instruments."""
    rho_ab, projectors = source_state_and_projectors(float(shape))
    initial_base = np.empty((2, 2, 2, 2), dtype=float)
    for x, y, s, t in itertools.product(range(2), repeat=4):
        initial_base[x, y, s, t] = real_trace(
            np.kron(projectors[x, s], projectors[y, t]) @ rho_ab
        )
    base_error = require_close(initial_base, analytic_base_table(shape),
                               "source Born probability table")
    rho = initial_with_flag(rho_ab)
    alice_effects = np.array([
        [np.kron(projectors[x, s], I6) for s in range(2)]
        for x in range(2)
    ])
    table = np.zeros((depth, 2, 2, 2, 2), dtype=float)
    max_state_trace_error = 0.0
    min_state_eigenvalue = 0.0
    max_flag_error = 0.0
    for i in range(depth):
        max_state_trace_error = max(max_state_trace_error,
                                    require_close(real_trace(rho), 1.0, "state trace"))
        require_close(rho, rho.conj().T, "state Hermiticity")
        minimum = float(np.linalg.eigvalsh(rho).min())
        min_state_eigenvalue = min(min_state_eigenvalue, minimum)
        if minimum < -ATOL:
            raise AssertionError(f"Nonpositive propagated state: eigenvalue {minimum}")

        # Directly measured flag probabilities are an additional comparison,
        # not the inputs to the simulated state update.
        flag_weights = []
        for flag in (NO, ZERO, ONE):
            flag_weights.append(real_trace(np.kron(np.eye(4), flag_transition(flag, flag)) @ rho))
        a = shape
        c = (1 + a) / ((2 + a) ** depth - 1)
        q = Fraction(1, 2 ** i) * (1 - c * sum((2 + a) ** j for j in range(i)))
        z = c * ((1 + a / 2) ** i - 1) / a
        max_flag_error = max(max_flag_error,
                             require_close(flag_weights, [float(q), float(1 - q - z), float(z)],
                                           "physical flag probabilities"))

        next_state = np.zeros_like(rho)
        for y in range(2):
            instrument = lift_instrument(bob_instrument(projectors, float(probabilities[i]), y))
            for t in range(2):
                post = apply_operation(rho, instrument[t])
                for x, s in itertools.product(range(2), repeat=2):
                    table[i, x, y, s, t] = real_trace(alice_effects[x, s] @ post)
                next_state += post / 2.0  # Fresh uniform Bob input.
        rho = next_state
    require_close(real_trace(rho), 1.0, "final state trace")
    return table, {
        "source_table_max_abs_error": base_error,
        "state_trace_max_abs_error": max_state_trace_error,
        "state_min_eigenvalue": min_state_eigenvalue,
        "flag_max_abs_error": max_flag_error,
    }


def enumerate_transcripts(depth: int, shape: Fraction,
                          probabilities: list[Fraction]) -> np.ndarray:
    """Enumerate P(A,B_1,...,B_K | X,Y_1,...,Y_K) by CP branches.

    Axes are Alice input, binary-ordered Bob input string, Alice outcome,
    binary-ordered Bob outcome string. No averaged-state recurrence is used.
    """
    rho_ab, projectors = source_state_and_projectors(float(shape))
    rho_initial = initial_with_flag(rho_ab)
    effects = [[np.kron(projectors[x, s], I6) for s in range(2)] for x in range(2)]
    instruments = {
        (i, y): lift_instrument(bob_instrument(projectors, float(probabilities[i]), y))
        for i in range(depth) for y in range(2)
    }
    input_strings = list(itertools.product(range(2), repeat=depth))
    transcript = np.empty((2, 2 ** depth, 2, 2 ** depth), dtype=float)
    for y_index, settings in enumerate(input_strings):
        branches = [rho_initial]
        for i, y in enumerate(settings):
            branches = [apply_operation(branch, instruments[i, y][t])
                        for branch in branches for t in range(2)]
        for b_index, branch in enumerate(branches):
            for x, s in itertools.product(range(2), repeat=2):
                transcript[x, y_index, s, b_index] = real_trace(effects[x][s] @ branch)
    return transcript


def check_transcripts(transcript: np.ndarray, depth: int,
                      expected_marginals: np.ndarray) -> dict:
    minimum = float(transcript.min())
    if minimum < -ATOL:
        raise AssertionError(f"Negative transcript probability {minimum}")
    normalization_error = require_close(transcript.sum(axis=(2, 3)), 1.0,
                                         "full transcript normalization")
    bob_no_signal_error = require_close(transcript[0].sum(axis=1), transcript[1].sum(axis=1),
                                         "Alice cannot signal to the complete Bob transcript")
    input_strings = list(itertools.product(range(2), repeat=depth))
    outcome_strings = list(itertools.product(range(2), repeat=depth))
    maximum_prefix_error = 0.0
    for prefix_length in range(depth + 1):
        reference = {}
        for x in range(2):
            for y_index, settings in enumerate(input_strings):
                distribution = transcript[x, y_index].reshape((2,) + (2,) * depth)
                distribution = distribution.sum(axis=tuple(range(prefix_length + 1, depth + 1)))
                key = (x, settings[:prefix_length])
                if key not in reference:
                    reference[key] = distribution
                else:
                    maximum_prefix_error = max(
                        maximum_prefix_error,
                        require_close(distribution, reference[key],
                                      "Alice plus Bob prefix independent of future inputs")
                    )
    marginals = np.zeros_like(expected_marginals)
    other_setting_weight = 1.0 / 2 ** (depth - 1)
    for x in range(2):
        for y_index, settings in enumerate(input_strings):
            for b_index, outcomes in enumerate(outcome_strings):
                for i in range(depth):
                    marginals[i, x, settings[i], :, outcomes[i]] += (
                        other_setting_weight * transcript[x, y_index, :, b_index]
                    )
    marginal_error = require_close(marginals, expected_marginals,
                                    "full-transcript marginalization")
    return {
        "conditional_entries": int(transcript.size),
        "minimum_probability": minimum,
        "normalization_max_abs_error": normalization_error,
        "alice_to_bob_max_abs_error": bob_no_signal_error,
        "tons_prefix_max_abs_error": maximum_prefix_error,
        "marginalization_max_abs_error": marginal_error,
    }


def exact_fixture() -> dict:
    cases = []
    for depth, numerator, denominator, full_transcript in CASE_SPECS:
        shape = Fraction(numerator, denominator)
        gamma = shape ** 2 / ((1 + 2 * shape) * (1 + shape) ** 2)
        margin = 4 * gamma * (1 + shape) / ((2 + shape) ** depth - 1)
        probabilities = [(1 + shape) / ((2 + shape) ** (depth - i) - 1)
                         for i in range(depth)]
        cases.append({
            "id": f"K{depth}_a{numerator}_{denominator}",
            "depth": depth,
            "shape": str(shape),
            "enumerate_full_transcript": full_transcript,
            "gamma": str(gamma),
            "beta": str(shape * gamma),
            "probabilities": [str(probability) for probability in probabilities],
            "common_chsh_excess": str(margin),
            "common_chsh_value": str(2 + margin),
        })
    return {
        "schema": 1,
        "source": SOURCE_URL,
        "reference_type": "Exact rational closed forms; physical verification is independent matrix propagation.",
        "outcome_order": [1, -1],
        "source_chsh_coefficients": [[-1, 1], [1, 1]],
        "carrier_dimensions": {"Alice": 2, "Bob_qubit": 2, "Bob_classical_flag": 3},
        "cases": cases,
    }


def run_suite(fixture: dict) -> dict:
    # Detect accidental editing of a reference input or its exact prediction.
    if fixture != exact_fixture():
        raise AssertionError("Expected fixture differs from the declared exact reference cases.")
    results = []
    for case in fixture["cases"]:
        depth = case["depth"]
        shape = Fraction(case["shape"])
        probabilities = [Fraction(value) for value in case["probabilities"]]
        margin = float(Fraction(case["common_chsh_excess"]))
        require_close(float(probabilities[-1]), 1.0, "terminal measurement probability")
        quantum, physical_checks = born_marginals(depth, shape, probabilities)
        analytic = analytic_marginals(depth, shape)
        probability_error = require_close(quantum, analytic, "full marginal probability table")
        require_close(quantum.sum(axis=(-2, -1)), 1.0, "marginal normalization")
        if float(quantum.min()) < -ATOL:
            raise AssertionError("A marginal probability is negative.")
        observed_chsh = chsh_values(quantum)
        canonical_chsh = chsh_values(canonical_relabel(quantum), source_orientation=False)
        require_close(observed_chsh, canonical_chsh, "Bob-only CHSH relabeling")
        gap_error = require_close(observed_chsh - 2.0, margin, "common positive CHSH margin",
                                  atol=GAP_ATOL, rtol=GAP_RTOL)
        if np.min(observed_chsh) <= 2.0:
            raise AssertionError("A configured finite-case CHSH value is not a strict violation.")
        result = {
            "id": case["id"],
            "depth": depth,
            "shape": float(shape),
            "expected_common_margin": margin,
            "observed_margin_min": float(np.min(observed_chsh - 2.0)),
            "observed_margin_max": float(np.max(observed_chsh - 2.0)),
            "marginal_probability_max_abs_error": probability_error,
            "chsh_margin_max_abs_error": gap_error,
            "physical_checks": physical_checks,
        }
        if case["enumerate_full_transcript"]:
            transcript = enumerate_transcripts(depth, shape, probabilities)
            result["full_transcript_checks"] = check_transcripts(transcript, depth, quantum)
        results.append(result)
    return {
        "status": "pass",
        "source": SOURCE_URL,
        "number_of_cases": len(results),
        "full_transcript_cases": sum("full_transcript_checks" in case for case in results),
        "tolerances": {"probability_absolute": ATOL, "gap_absolute": GAP_ATOL,
                       "gap_relative": GAP_RTOL},
        "cases": results,
        "scope": "Finite Born/instrument verification and exact rational reference checks; no statistical-rate claim.",
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-expected", action="store_true",
                        help="Regenerate the exact reference fixture only after physical checks pass.")
    args = parser.parse_args()
    if args.write_expected:
        fixture = exact_fixture()
    else:
        with EXPECTED_PATH.open(encoding="utf-8") as handle:
            fixture = json.load(handle)
    report = run_suite(fixture)
    if args.write_expected:
        EXPECTED_PATH.parent.mkdir(parents=True, exist_ok=True)
        EXPECTED_PATH.write_text(json.dumps(fixture, indent=2) + "\n", encoding="utf-8")
        report["expected_fixture_written"] = str(EXPECTED_PATH.relative_to(EXPECTED_PATH.parents[2]))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
