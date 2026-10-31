# Sequential Bell Limits

How large can the Bell violation remain when many observers successively use the same side of a shared resource?

Arbitrarily many observers can each have a strictly positive violation. The quantitative question is more restrictive: with fresh independent uniform settings, the weakest ordinary Alice–Bob CHSH violation must fall exponentially with the number of observers. This repository proves a dimension-independent causal bound, identifies the exact nonnegative-gap projection of the nonsignalling sharing region, and determines the optimal exponential rate for quantum sharing.

Alice uses one fixed pair of binary measurements and produces one binary outcome per source use. Each Bob produces one binary outcome and may pass arbitrary quantum systems and classical memory forward. The complete behavior obeys joint time-ordered nonsignalling. All other settings and outcomes are averaged when forming an Alice–Bob marginal; every trial is retained. The [model](science/model.md) states these assumptions precisely.

## Principal results

Let $S_i$ be the maximum over the eight CHSH orientations of the ordinary Alice–Bob $i$ marginal. The local bound is two. For every allowed chain of length $K$,

```math
\boxed{\sum_{i=1}^{K}2^{i-1}(S_i-2)\le2.}
```

The gaps are signed. The stronger [predictability form](science/causal-bound.md#the-weighted-converse) retains Alice's initial bias and a final history-dependent residual. The same law applies to an ordered subsequence, with positions counted within that subsequence.

| Result | Consequence | Authoritative account |
|---|---|---|
| Exact nonsignalling region | Nonnegative gaps are precisely the weighted simplex in the equation below. | [Attainment and exact region](science/attainment.md) |
| Optimal quantum exponential rate | The best common quantum gap has exponential base one half. Its polynomial correction remains undetermined. | [Quantum construction and rate](science/quantum-rate.md) |
| Necessary source repetitions | Certifying every pair from its own iid records requires an exponential number of source uses at fixed nontrivial error levels. | [Finite-sample evidence](science/statistical-evidence.md) |
| Exact nonsignalling contamination threshold | Independent replacement of Alice's output by a fair bit permits all pairs to remain nonlocal only below the threshold stated below. | [Noise and boundaries](science/noise-and-boundaries.md) |
| General evidence budgets | For finite alphabets, the sum of marginal KL distances is limited by Alice's output entropy; a quantum refinement accounts for residual entanglement. | [General evidence and residual entanglement](science/general-evidence-budget.md) |

### Exact nonsignalling sharing

The attainable region of nonnegative gaps $\delta_i=S_i-2$ is

```math
\mathcal D_K=
\left\{\boldsymbol\delta\in[0,\infty)^K:
\sum_{i=1}^{K}2^{i-1}\delta_i\le2\right\}.
```

Consequently, the largest common nonsignalling gap is exactly

```math
\delta_K^{\mathrm{NS}}=
\max_{P\in\mathcal T_K}\min_i(S_i-2)
=\frac{2}{2^K-1}.
```

The realizing mechanism is inherited from a one-sided PR specialization of the Hardy protocol of [Steffinlongo, D'Alessandro and Renner](references/related-work.md#steffinlongodalessandrorenner2026). The universal converse establishes its optimality. An explicit causal probability kernel supplies a second direct verification of attainment.

### Quantum systems attain the same exponential rate

Let $\delta_K^{\mathrm Q}$ denote the supremum of the common gap over quantum realizations in the stated model. A two-qubit source and a transmitted qubit plus classical trit give

```math
\frac{64/K^2}
{(1+8/K)(1+4/K)\bigl[(2+4/K)^K-1\bigr]}
\le\delta_K^{\mathrm Q}\le\frac{2}{2^K-1}.
```

The lower expression is asymptotic to $64/(e^2K^2 2^K)$. Thus

```math
\boxed{\lim_{K\to\infty}(\delta_K^{\mathrm Q})^{1/K}=\frac12.}
```

The state, Alice's projectors and Bob's controls may depend on the chosen finite depth. The carrier dimension is six, while the smallest control probability is exponentially small. This proves an optimal exponential rate under the stated resources, without determining the finite-depth quantum optimum or a fixed-state optimum. [The complete instrument and allocation proof](science/quantum-rate.md) identifies every inherited ingredient.

### Evidence and noise have explicit operational meanings

Suppose $n$ independent source repetitions are used, and each link is certified using only its own records $(X,A,Y_i,B_i)$. If each test has type-I error at most $\alpha$ against every iid local alternative and power at least $1-\beta$, where $0<\alpha<1-\beta<1$, then

```math
n\ge
\frac{d(1-\beta\|\alpha)}{-\ln(1-2^{-K})}.
```

Here $d$ is binary relative entropy in nats. The same source rows can be reused by all tests; decisions within one row need not be independent. This is a necessary bound for marginal-data tests. It does not establish the optimal quantum sample complexity or constrain arbitrary tests of the whole transcript.

For a separate noise model, replace Alice's output by an independent fair bit with probability $p$, retaining the input and all Bob records. Every pair remains CHSH nonlocal only if

```math
p<2^{-K}.
```

This threshold is exact over the nonsignalling model. Quantum protocols attain its exponential rate up to a polynomial factor. Other source or instrument noise requires its own analysis.

## Reading routes

The scientific account is organized by question; each proof has one authoritative home.

| Question | Read |
|---|---|
| What is the experiment, and which causal assumptions matter? | [Sequential Bell scenario](science/model.md) |
| Why does each additional observer impose a stronger restriction? | [Causal CHSH bound](science/causal-bound.md) |
| Is the bound sharp, and for which theory? | [Attainable nonsignalling region](science/attainment.md) |
| How close can physical quantum instruments come? | [Quantum sharing rate](science/quantum-rate.md) |
| What does the result imply for finite statistical tests? | [Marginal Bell certification](science/statistical-evidence.md) |
| What survives beyond binary CHSH, or with correlated settings? | [General evidence budgets](science/general-evidence-budget.md) |
| Which noise model is covered, and what breaks outside the assumptions? | [Noise and model boundaries](science/noise-and-boundaries.md) |
| Which ingredients come from earlier work? | [Related work](references/related-work.md) and [BibTeX bibliography](references/references.bib) |
| How can the finite calculations be reproduced? | [Verification guide](verification/README.md) |

For a short route, read the model, causal bound, attainment and quantum-rate pages in that order. The statistical page and general evidence budget then explain distinct operational consequences. [llms.txt](llms.txt) maps common questions to these sources.

## Learning route

The [learning entrypoint](learning/README.md) connects Valerio Scarani's _Bell Nonlocality_ (2019), the single educational anchor, to this project's experiment and proofs. The [source bridge](learning/scarani-bridge.md) selects relevant sections, translates conventions, and develops a complete two-observer example. The [30-milestone map](learning/milestones.md) contains ten background milestones followed by twenty narrative milestones, with dependencies and canonical scientific sources. It is a shared understanding map, not a personal assessment record.

## Reproduction

The reference environment is Python 3.12 with pinned NumPy and SciPy versions. In an existing suitable environment, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/run_all.py
```

The suite checks full finite TONS linear programs, exact rational attaining distributions, direct density-matrix propagation of the quantum instruments, complete short-chain transcripts, and numerical evidence budgets. Expected values and explicit tolerances are included. The default commands read fixtures and print reports without rewriting them.

Finite calculations test the implementation and expose assumption failures. The arbitrary-depth bounds and asymptotic rate follow from the analytic proofs. See [the verification guide](verification/README.md) for case coverage, expected outputs, and limitations.

## Scope

Fresh uniform Bob settings are essential to the exponential CHSH theorem. Pairwise nonsignalling does not substitute for the stated joint causal conditions. Shared or correlated settings can repeatedly expose the same correlation, and full-record tests can recover information absent from every ordinary pairwise table. The [boundary examples](science/noise-and-boundaries.md) make these distinctions concrete.

The exact nonsignalling optimum and the quantum exponential-rate statement are different claims. The evidence theorem concerns certification of ordinary marginal distributions. None of these claims bounds the device-independent randomness or secret key available from an arbitrary joint-transcript protocol.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
