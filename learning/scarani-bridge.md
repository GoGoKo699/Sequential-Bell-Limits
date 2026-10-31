# From Scarani's Bell Nonlocality to sequential sharing

[Learning entrypoint](README.md) · [Thirty milestones](milestones.md) · [Scientific overview](../README.md)

## The single anchor

Valerio Scarani, _Bell Nonlocality_ (Oxford University Press, 2019), DOI [10.1093/oso/9780198788416.001.0001](https://doi.org/10.1093/oso/9780198788416.001.0001), is the sole educational anchor. Use the [official open-access edition](https://academic.oup.com/book/36528). The route below selects portions of the book; reading it from cover to cover is not a prerequisite.

| Source location | Foundation used here | Project continuation |
|---|---|---|
| [Chapter 1](https://academic.oup.com/book/36528/chapter/321331193), Sections 1.2–1.3 | Inputs, outputs, Bell-local explanations and the CHSH test | [Model](../science/model.md): one Alice outcome is reused in several pairwise tables. |
| [Chapter 2](https://academic.oup.com/book/36528/chapter/321331393), Sections 2.1–2.3 | Behaviors, nonsignalling and local mixtures | [Model](../science/model.md): joint prefix causality and the entire Bob transcript. |
| Chapter 2, Sections 2.4–2.5 | Convex geometry and all CHSH facets | [Attainment](../science/attainment.md) and [local comparison for testing](../science/statistical-evidence.md). |
| Chapter 2, Section 2.6 | Distinguishing an ideal behavior from finite-data evidence | [Statistical evidence](../science/statistical-evidence.md): the explicitly iid marginal-testing theorem. |
| [Chapter 3](https://academic.oup.com/book/36528/chapter/321331577), Sections 3.1–3.2 | Quantum behaviors, measurements and quantum CHSH values | [Quantum rate](../science/quantum-rate.md): instruments, disturbance and the transmitted trit. |
| [Chapter 9](https://academic.oup.com/book/36528/chapter/321332374), Sections 9.1–9.2 | The nonsignalling set and hypothetical PR resources | [Exact causal kernels](../science/attainment.md), kept distinct from physical quantum attainment. |

The book supplies Bell foundations, not the arbitrary-length theorem proved here. Conditional-mean bookkeeping, the temporal telescope, the optimized sequential allocation and the precise KL testing reduction are supplied locally. The Shannon chain rule, Holevo bound and entanglement of formation enter the [companion proof](../science/general-evidence-budget.md), which states their roles and cites their primary sources. They do not create a second textbook prerequisite.

## One experiment, several marginal tables

In one run, Alice receives one setting and records one output. The same Bob-side system then passes from observer to observer. Each Bob receives a new independent uniform setting, records one output and may transmit a quantum system and classical memory forward. Alice receives no Bob history and does not change her measurement pair between links.

A table for Alice and Bob 3 is formed by forgetting the recorded settings and outcomes of the other Bobs, not by pretending those Bobs did nothing. Their physical disturbance remains. Selecting only a favorable past record produces a different conditional experiment; it is not the ordinary marginal in the main theorem. The [model](../science/model.md) specifies the averaging and both joint causal conditions.

Spatial monogamy theorems cannot be imported without checking their hypotheses: later Bobs here can receive messages from earlier Bobs. Conversely, pairwise nonsignalling is insufficient. Alice must not signal to their combined record, and the joint distribution of Alice with a Bob prefix must not depend on later settings.

## Notation dictionary

| Bell-language object | Repository notation and convention |
|---|---|
| A behavior | Conditional output probabilities given the inputs. The complete sequential table is written in `science/model.md`; its ordinary pair tables are denoted by P with a stage subscript. |
| Inputs and outputs | Uppercase letters denote random variables; lowercase letters denote their values. Alice inputs and all Bob inputs are bits. Outputs are signs unless a construction explicitly switches to bits. |
| CHSH expression | C denotes one fixed orientation. S denotes the maximum over all eight orientations of a given pair table. The local bound is two. |
| CHSH gap | Delta is S minus two. It is signed; a local table can have a negative gap. |
| Past and residual uncertainty | H is the Bob setting/outcome history. M is the mean posterior predictability potential, and R equals one minus M. Neither is a physical measurement chosen by Alice. |
| Statistical strength | Nu is the KL distance to the local set using the actual input law. Logs and entanglement entropies in the evidence pages use nats. |
| Quantum shape parameter | The quantum page uses a positive parameter named a; that parameter is not an output. Its outcomes are labeled s and t. |

For the canonical CHSH orientation and sign outputs,

```math
C_i=E_i^{00}+E_i^{01}+E_i^{10}-E_i^{11},
\qquad E_i^{xy}=\mathbb E[AB_i\mid X=x,Y_i=y].
```

With bit outputs, replace each output bit by its sign before evaluating a correlator. For uniform input pairs the CHSH game-winning probability is related by

```math
C_i=8W_i-4.
```

Thus a value of three quarters in the game convention is a correlator value of two, not a violation. The quantum construction uses a different fixed orientation, denoted by a superscript H. Its page gives an explicit relabeling; it agrees with the maximum S only in the regimes proved there.

## From conditional means to a causal bound

At a past history h, consider Alice's mean output separately for her two possible input choices:

```math
m_x(h)=\mathbb E[A\mid X=x,H=h],
\qquad
u(h)=\frac{m_0(h)+m_1(h)}2,
\qquad
v(h)=\frac{m_0(h)-m_1(h)}2.
```

These are means from different conditional experiments. They do not assign simultaneous values to incompatible Alice outcomes. In this display, u is a coordinate of the conditional-mean vector; the Greek letter nu used for KL evidence is a different symbol.

The quantity that will telescope is

```math
M_i=\mathbb E_{H_i}\max\{|m_0(H_i)|,|m_1(H_i)|\},
\qquad R_i=1-M_i.
```

Refining a history cannot lower M on average, by convexity. More importantly, the two equally likely current Bob settings require a stronger one-step relation:

```math
S_i-2\le 2R_{i-1}-4R_i.
```

The factor four is not an entanglement measure or a statement that the physical state loses half its entanglement. It comes from the CHSH decomposition and averaging the two fresh uniform settings. Multiplying the step-i relation by the corresponding power of two cancels the intermediate residuals:

```math
\sum_{i=1}^K2^{i-1}(S_i-2)+2^{K+1}R_K\le2R_0\le2.
```

The [causal proof](../science/causal-bound.md) establishes the conditional identities, both Jensen steps and invariance under independent CHSH orientations. The finite calculations check cases; they are not the all-depth proof.

## Two observers: a complete example

For two Bobs the causal constraint becomes

```math
(S_1-2)+2(S_2-2)\le2.
```

To make both gaps equal, each can be at most two thirds. A hypothetical nonsignalling realization chooses, before all settings, which Bob will use one PR resource. With probability two thirds, Bob 1 uses it and Bob 2 copies his outcome. With probability one third, Bob 1 outputs an independent fair bit and Bob 2 uses the untouched resource. Inputs remain independent uniform bits in both branches.

| Branch | Probability | Bob 1 CHSH value | Bob 2 CHSH value |
|---|---:|---:|---:|
| PR use at Bob 1, then copy | 2/3 | 4 | 2 |
| Idle Bob 1, PR use at Bob 2 | 1/3 | 0 | 4 |
| Unconditioned mixture | 1 | 8/3 | 8/3 |

Copying the first output does not copy a PR box: averaging Bob 1's independent setting reduces the later CHSH value to two in the first branch. The mixture retains every trial and saturates the weighted bound. It is a nonsignalling probability model, not a quantum device.

For a physical comparison, the [quantum construction](../science/quantum-rate.md) at depth two and shape parameter two uses

```math
|\psi_2\rangle=
\frac{|00\rangle+\sqrt2|01\rangle+\sqrt2|10\rangle}{\sqrt5},
\qquad p_1=\frac15,
\qquad p_2=1.
```

Alice uses the projectors given in that page. Each Bob follows its trit-controlled instrument, rather than just measuring an unchanged state. With Hardy parameters and initial flag probabilities,

```math
\gamma=\frac4{45},\quad a=2,\quad
(q_1,Z_1)=(1,0),\quad(q_2,Z_2)=\left(\frac25,\frac1{10}\right).
```

Both excesses are consequently

```math
4\gamma(q_i p_i-aZ_i)=\frac{16}{225}.
```

This is one valid quantum construction, not the optimal depth-two quantum value. The trit is an explicit forward-memory resource. There is no postselection on its value.

## From an exact causal region to a quantum exponential rate

The [attainment proof](../science/attainment.md) realizes every nonnegative gap vector inside the weighted simplex. Its realizing Hardy mechanism is inherited from Steffinlongo, D'Alessandro and Renner; the universal converse supplies the optimality statement.

For quantum devices, a two-qubit source and a qubit-plus-trit carrier achieve the common gap

```math
\delta_K(a)=
\frac{4a^2}{(1+2a)(1+a)[(2+a)^K-1]}.
```

The schedule is optimized within that specified one-sided protocol. Choosing the source parameter separately for each target depth gives

```math
\delta_K(4/K)\sim\frac{64}{e^2K^2 2^K},
\qquad
\delta_K(4/K)\le\delta_K^{\mathrm Q}\le\frac2{2^K-1}.
```

The two bounds have the same Kth-root limit, one half. They do not have the same polynomial prefactor. A fixed-state optimum and the exact finite-depth quantum optimum are separate questions. Constant carrier dimension also does not imply depth-independent control precision: the earliest control probabilities become exponentially small.

## Violation, noise and evidence are different quantities

Replacing Alice's recorded output by an independent fair bit with probability p multiplies every correlator by one minus p. For a common minimum gap delta, all links remain nonlocal exactly below the corresponding threshold:

```math
p\lt\frac{\delta}{2+\delta}.
```

The best nonsignalling common gap therefore gives the sharp threshold one over two to the Kth power. This is a statement about that specified channel, not generic loss or arbitrary instrument noise.

To obtain a necessary sample count, the proof needs an **upper** bound on the full marginal's KL distance to locality. A small score violation alone would not provide that bound for an arbitrary Bell scenario. Here the complete CHSH facet characterization allows mixing the behavior with uniform output noise until every facet is local. The resulting comparator yields

```math
\nu_i\le\ln(1+(S_i-2)/2)
```

for a nonlocal marginal. Relative-entropy data processing through any test of its own iid records then gives

```math
n\nu_i\ge d(1-\beta\|\alpha),
\qquad
n\ge\frac{d(1-\beta\|\alpha)}{-\ln(1-2^{-K})}.
```

Alpha bounds false certification against every iid local alternative, and one minus beta is the required power. Different link tests may reuse the same rows; their decisions are not assumed independent. The proof does not construct a matching quantum test or establish a cost for arbitrary tests of the full transcript. See the [finite-sample proof](../science/statistical-evidence.md).

## Where the bridge ends

The [companion evidence budget](../science/general-evidence-budget.md) extends to finite alphabets, nonuniform independent settings and causally revealed correlated external settings under its own stated assumptions. Its residual entanglement is defined before Alice's deferred measurement, with a separate post-readout variant. Do not apply those broader assumptions to the sharper uniform-input CHSH law without a new argument.

The [boundary examples](../science/noise-and-boundaries.md) show how correlated inputs can repeat one correlation and how a full transcript can reveal a Bell correlation hidden in every individual pair. These examples explain the scope, rather than defeating the stated theorem. The [milestone map](milestones.md) brings the mechanisms together; the [verification guide](../verification/README.md) states what the executable checks establish.
