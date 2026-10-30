# Reproducing the scientific checks

The analytical proofs are in [science/](../science/model.md). This directory supplies finite checks of the causal optimization, exact attaining distributions, actual quantum instruments, and evidence formulas. The checks are designed to address different possible errors: missing causal constraints, incorrect mixtures or normalization, an unphysical instrument recurrence, a wrong CHSH orientation, or an unsupported numerical KL optimum.

## Run the complete suite

The reference environment is **Python 3.12.14, NumPy 2.3.5 and SciPy 1.17.0**. The numerical package versions are pinned in [requirements.txt](requirements.txt). Use a suitable Python environment, then run from the repository root:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The coordinator runs each program, parses its JSON report, and returns exit status zero only when all three programs report success. A normal run reads the expected fixtures and prints results without modifying repository files. To retain a new report explicitly, redirect stdout to a chosen path:

```bash
python verification/run_all.py > /tmp/sequential-bell-verification.json
```

The checked-in [reference report](results/suite.json) records one complete run in the reference environment. Floating-point diagnostics can vary across platforms; success depends on the mathematical conditions and stated tolerances, rather than bytewise equality with that report.

## Coverage

| Program | Independent construction or check | Default coverage |
|---|---|---|
| [verify_tons.py](verify_tons.py) | Constructs the full conditional-probability polytope from normalization, Alice-to-whole-Bob nonsignalling and joint-prefix causal equalities. | Three LPs at each depth from one through five; exact attaining profiles, orientations, residual potentials and selected subsequences. |
| [verify_quantum_protocol.py](verify_quantum_protocol.py) | Builds the state and projectors, then propagates outcome-labelled Kraus maps on the actual Alice–Bob–trit density matrix. | Nine parameter/depth cases through depth twenty; five complete-transcript enumerations through depth four. |
| [verify_evidence.py](verify_evidence.py) | Optimizes actual-design KL over all sixteen deterministic binary local vertices and checks concrete quantum histories. | Analytic CHSH examples, all sixty-four local input/output relabellings, biased-design whitening, independent and correlated-input chains, and finite-sample formulas. |

### Causal polytope and exact profiles

At each tested depth, the three LP objectives are the weighted CHSH score, the largest common gap, and the weighted score with both Alice means fixed to one half. The optimization variables are every probability in the complete conditional table; the attaining construction is not assumed by the LP. Solver status, normalization and causal residuals, nonnegative probabilities, fair-gap feasibility and objective agreement are checked.

The [expected values](expected/tons.json) are analytic rationals. Separate exact-arithmetic checks cover the local origin, the common-gap boundary, an interior profile, and every axis vertex of the positive-sector simplex: thirty profiles in total. Each profile is checked under all eight CHSH orientations and every ordered subsequence. The explicit PR kernel and the inherited Hardy parameter recursion are checked separately.

Three boundary fixtures establish that the verifier detects the intended distinctions: a valid signed-gap example rejects positive-part replacement at the original indices; simultaneously PR pairwise tables violate collective nonsignalling; and a future-dependent Alice correlation violates joint-prefix causality even when the Bob-only record is input independent.

The floating-point tolerance is stored in the expected fixture. Exact Fraction calculations require equality, not a numerical tolerance.

### Physical quantum instruments

The quantum program simulates a two-dimensional Alice system and a six-dimensional Bob qubit–trit carrier. The marginal probabilities arise from matrix propagation under the instruments in [quantum-rate.md](../science/quantum-rate.md). The analytic scalar recurrence is not used to generate the simulated probabilities.

Every marginal probability cell is compared with an independently evaluated analytic table. Every CHSH value is checked in both the source convention and the explicitly relabelled canonical convention. State trace, Hermiticity, positivity, instrument completeness and flag weights are checked as well.

The complete-transcript cases separately test normalization, positivity, collective nonsignalling, all joint-prefix causal constraints, and agreement with the marginal propagation. The probability absolute tolerance is $2\times10^{-12}$. Gap comparisons use absolute tolerance $10^{-13}$ and relative tolerance $10^{-5}$; the deepest case has a predicted gap well above these absolute tolerances.

The [quantum fixture](expected/quantum_protocol.json) contains exact rational shape parameters, schedules and expected margins. Intentional regeneration is a separate action:

```bash
python verification/verify_quantum_protocol.py --write-expected
```

This option runs the physical checks before writing the fixture. Routine verification does not use it.

### Statistical and information budgets

All evidence calculations use **natural logarithms**. The KL program first checks exact local-polytope feasibility numerically. For a nonlocal behavior, it minimizes the convex KL objective over local-vertex mixture weights. It then verifies primal feasibility and a first-order convex optimality-gap bound; optimizer success alone is insufficient. The permitted optimality gap is $5\times10^{-7}$ nats, and the actual largest gap appears in the report.

Four CHSH-symmetric behaviors have analytic KL reference values. Twelve additional nonsignalling mixtures test the whitening bound under a biased Alice input law. A fixed random seed, `20261030`, specifies twelve short quantum chains using independent or correlated external settings. The checks compare the marginal KL values with the actual Shannon-entropy decrease and pure-branch entanglement decrease, including the setting total-correlation correction.

A chain with thirty-two identical external settings explicitly violates the uncorrected output-entropy budget while satisfying the corrected one. A masked-record example has local individual marginals and a nonlocal decoded joint record. Finite-sample calculations check the equivalent logarithmic formulas and the weighted evidence constraint at its stated lower bound.

These quantum examples verify pure-branch entropy accounting. They do not numerically solve a mixed-state entanglement-of-formation convex roof. The mixed-state theorem follows from the common-ensemble proof in [general-evidence-budget.md](../science/general-evidence-budget.md).

## Run individual checks

```bash
python verification/verify_tons.py
python verification/verify_quantum_protocol.py
python verification/verify_evidence.py
```

The TONS program also accepts `--max-k` from one through five and an explicit `--output PATH`. The evidence program accepts an explicit `--output PATH`. These options are useful when diagnosing a particular calculation; the default complete run is the reference verification.

## Interpretation and limits

Finite optimization does not prove the arbitrary-depth theorem. Matrix simulations do not establish an asymptotic limit, and optimizer agreement does not establish literary priority. The mathematical proofs, resource accounting and [source comparisons](../references/related-work.md) are separate parts of the scientific record.

The suite does not claim an exact finite-depth quantum optimum, a matching quantum sample complexity, robustness to unspecified physical noise, or an upper bound on full-transcript randomness. Each of those is outside the proved statement or uses a different operational model.
