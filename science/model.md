# Sequential Bell scenario

One Alice is compared with a sequence of Bobs. Alice produces one binary outcome from one of two fixed measurements. Each Bob receives a fresh binary setting, produces a binary outcome, and may pass a system and a classical record to the next Bob. The quantities of interest are the ordinary Alice–Bob marginals, with every other observer's settings and outcomes averaged according to the experiment.

This is the one-sided sharing problem studied by [SilvaEtAl2015](../references/related-work.md#silvaetal2015) and [BrownColbeck2020](../references/related-work.md#browncolbeck2020). The converse here permits arbitrary forward control and assumes only the joint causal conditions below. It therefore also covers the ancillary registers used by [SteffinlongoDAlessandroRenner2026](../references/related-work.md#steffinlongodalessandrorenner2026).

## Inputs, outputs and causal constraints

Fix a positive integer $K$. Alice's input is $X\in\{0,1\}$ and her output is $A\in\{-1,+1\}$. Bob $i$ has input $Y_i\in\{0,1\}$ and output $B_i\in\{-1,+1\}$. Write $\mathbf y=(y_1,\ldots,y_K)$ and $\mathbf b=(b_1,\ldots,b_K)$.

A behavior is a nonnegative, normalized conditional probability table
```math
P(a,\mathbf b\mid x,\mathbf y).
```
The actual input distribution is
```math
\Pr[X=x,\mathbf Y=\mathbf y]=\pi(x)\,2^{-K},
\qquad \pi(0),\pi(1)>0.
```
The source and the devices are independent of these external setting choices. Bob $i$ receives $Y_i$ only at his stage. In particular, the devices have no advance access to later settings. Alice's measurement rule is fixed before the experiment and does not depend on any Bob history. Uniform $\pi$ is the usual CHSH design, but the causal bound only requires both Alice inputs to be defined.

The table must satisfy both of the following conditions.

**No signalling from Alice to the complete Bob record.** For every $x,x',\mathbf y,\mathbf b$,
```math
\sum_a P(a,\mathbf b\mid x,\mathbf y)
=
\sum_a P(a,\mathbf b\mid x',\mathbf y).
```
Denote this common marginal by $P_B(\mathbf b\mid\mathbf y)$.

**No dependence of an Alice–Bob prefix on later Bob inputs.** For every $i=0,\ldots,K-1$,
```math
\sum_{b_{i+1},\ldots,b_K}
P(a,\mathbf b\mid x,\mathbf y)
=
P^{[i]}(a,b_1,\ldots,b_i\mid x,y_1,\ldots,y_i).
```
The right-hand side is independent of $y_{i+1},\ldots,y_K$. For $i=0$, this says that Alice's distribution $P_A(a\mid x)$ is independent of all Bob settings.

Call the resulting set $\mathcal T_K$. These are **joint time-ordered nonsignalling** constraints: the prefix condition includes Alice's output, and the first condition concerns the whole Bob string. Pairwise nonsignalling of each Alice–Bob table does not imply them. Sequential causal models and their distinction from ordinary multipartite locality are discussed in [GallegoEtAl2014](../references/related-work.md#gallegoetal2014).

The source can contain shared randomness. Each Bob's operation can depend on all information that has reached him from earlier Bobs. There is no bound on the carrier dimension or the size of forward memory. Communication involving Alice during the measurement stage is excluded by the stated causal model.

## Quantum realizations are included

Let $\rho_{AB}$ be an initial quantum state, $\{M_{a\mid x}\}_a$ Alice's fixed POVM, and $\mathcal I^{i,h}_{b\mid y}$ a completely positive instrument on the Bob side. The incoming and outgoing carrier spaces may differ, and the instrument may depend on the available past record $h$. Initial local ancillas are included in the Bob system.

For a specified outcome history, define the composed Bob map
```math
\mathcal J_{\mathbf b\mid\mathbf y}
=
\mathcal I^{K,h_{K-1}}_{b_K\mid y_K}
\circ\cdots\circ
\mathcal I^{1}_{b_1\mid y_1}.
```
The behavior is
```math
P(a,\mathbf b\mid x,\mathbf y)
=
\operatorname{tr}\!\left[
(M_{a\mid x}\otimes I)
\left(\operatorname{id}_A\otimes
\mathcal J_{\mathbf b\mid\mathbf y}\right)(\rho_{AB})
\right].
```
Summing the outcomes of a future instrument gives a trace-preserving map, which proves the prefix condition. Summing Alice's outcome replaces her POVM by the identity, which proves no signalling to the complete Bob record. Alice's fixed measurement can be deferred in this calculation because it acts on a different subsystem. No assumption about the chronological position of her isolated measurement is needed.

The theorem is consequently a bound for all such quantum realizations and for the larger set $\mathcal T_K$. The [attaining nonsignalling construction](attainment.md) uses a PR resource. The [quantum lower construction](quantum-rate.md) is treated separately.

## Ordinary pairwise marginals

For each $i$, define
```math
P_i(a,b\mid x,y)
=
2^{-(K-1)}
\sum_{\mathbf y_{-i},\,\mathbf b_{-i}}
P(a,\mathbf b\mid x,\mathbf y)
\bigg|_{y_i=y,\ b_i=b}.
```
The distribution used to average earlier settings is part of the experiment. Changing that distribution changes the channel seen by later Bobs and, in general, changes their marginals.

The causal constraints imply that $P_i$ is a bipartite nonsignalling behavior. A Bell-local comparison table has the form
```math
Q_i(a,b\mid x,y)
=
\sum_\lambda r(\lambda)\,
Q_A(a\mid x,\lambda)\,
Q_B(b\mid y,\lambda),
```
where $r(\lambda)$ is independent of the settings.

The correlators are
```math
E_i^{xy}=\sum_{a,b}ab\,P_i(a,b\mid x,y).
```
Let
```math
\mathcal C=
\left\{c\in\{-1,+1\}^{2\times2}:
\prod_{x,y}c_{xy}=-1\right\}.
```
There are eight CHSH orientations. For $c\in\mathcal C$, write
```math
C_i(c)=\sum_{x,y}c_{xy}E_i^{xy},
\qquad
S_i=\max_{c\in\mathcal C}C_i(c),
\qquad
\delta_i=S_i-2.
```
Thus $0\le S_i\le4$, and $\delta_i$ is a **signed** gap. A local table can have $S_i<2$. For a valid binary-input, binary-output nonsignalling table, Bell locality is equivalent to $S_i\le2$; this is the relevant form of [Fine1982](../references/related-work.md#fine1982).

The canonical orientation used in the proofs is
```math
C_i=
E_i^{00}+E_i^{10}+E_i^{01}-E_i^{11}.
```
The [causal bound](causal-bound.md) permits a different orientation at each stage and therefore also applies simultaneously to the maxima $S_i$.

## Conditioning on a Bob history

Define
```math
H_i=(Y_1,B_1,\ldots,Y_i,B_i),
\qquad H_0=\varnothing.
```
Let $p_i(h)$ be the actual probability of $H_i=h$, including the uniform probabilities of its setting values. No signalling from Alice implies
```math
\Pr[X=x,H_i=h]=\pi(x)p_i(h).
```
A positive-probability history therefore has the same support for both Alice inputs. On that support define
```math
m_x(h)=\mathbb E[A\mid X=x,H_i=h].
```
Zero-probability histories make no contribution and can be omitted.

At stage $i$, put
```math
r_i(b\mid y,h)=
\Pr[B_i=b\mid Y_i=y,H_{i-1}=h].
```
This conditional outcome law is independent of $x$. The prefix condition and fresh setting choice give
```math
\Pr[A=a,H_{i-1}=h\mid X=x,Y_i=y]
=
\Pr[A=a,H_{i-1}=h\mid X=x].
```
It follows that, for either current setting $y$,
```math
m_x(h)
=
\sum_b r_i(b\mid y,h)\,m_x(h,y,b),
\qquad x=0,1.
```
The updated history weights are
```math
p_i(h,y,b)=\frac12\,p_{i-1}(h)\,r_i(b\mid y,h).
```
Finally, the same past-history distribution averages each conditional pair table:
```math
P_i(a,b\mid x,y)
=
\sum_h p_{i-1}(h)\,
\Pr[A=a,B_i=b\mid X=x,Y_i=y,H_{i-1}=h].
```

These identities are the inputs to the proof. The pair $(m_0(h),m_1(h))$ contains conditional means from two different experimental settings. It does **not** introduce simultaneously existing random variables $A_0,A_1$, or assume a joint distribution for incompatible Alice measurements.

## Which information enters a certificate

The main CHSH and statistical results use the unconditioned tables $P_i$. They retain all trials and all binary outcomes. A test that conditions on a herald or on an earlier Bob record has a different statistical null hypothesis. A test on the complete chain has still more information.

The distinction matters operationally. The repository separately treats [marginal statistical evidence](statistical-evidence.md), the [general evidence budget](general-evidence-budget.md), and [noise and model boundaries](noise-and-boundaries.md). The exponential marginal limit is not a bound on randomness extracted from the complete sequential transcript.

