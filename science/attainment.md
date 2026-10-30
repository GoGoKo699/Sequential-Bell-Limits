# The attainable nonsignalling region

The universal converse determines an exact region for simultaneous nonnegative CHSH gaps. Its attainability is already supplied by a specialization and parameter choice within the Hardy protocol of [SteffinlongoDAlessandroRenner2026](../references/related-work.md#steffinlongodalessandrorenner2026). This section identifies that specialization and gives an explicit probability-kernel realization.

The conclusion concerns the time-ordered nonsignalling set $\mathcal T_K$ defined in [the model](model.md). Exact quantum saturation is not asserted; the quantum comparison is developed in [quantum-rate.md](quantum-rate.md).

## Exact projection onto nonnegative gaps

For the stagewise maxima $S_i$ over all eight CHSH orientations, define
```math
\mathcal D_K=
\left\{(S_1-2,\ldots,S_K-2):
P\in\mathcal T_K,\ S_i\ge2\ \text{for every }i
\right\}.
```

### Theorem 2: positive-sector projection

```math
\boxed{
\mathcal D_K
=
\left\{
\boldsymbol\delta\in[0,\infty)^K:
\sum_{i=1}^K2^{i-1}\delta_i\le2
\right\}.
}
```

The inclusion from left to right is [Theorem 1](causal-bound.md#theorem-1-chsh-sharing-with-a-residual-predictability-term). The constructions below give the other inclusion.

One fixed CHSH orientation suffices for attainment. To see why its computed value is also the maximum, let $c,d\in\mathcal C$ be distinct and not opposite. Their sign matrices agree on exactly two entries, so
```math
C_i(c)+C_i(d)
=
2\sum_{(x,y):c_{xy}=d_{xy}}c_{xy}E_i^{xy}
\le4.
```
If $C_i(c)\ge2$, every such $C_i(d)$ is at most $2$; the opposite orientation has value $-C_i(c)$. Thus $S_i=C_i(c)$ whenever the attained canonical value is at least two, including the boundary.

## Attainment from the existing Hardy protocol

[SteffinlongoDAlessandroRenner2026](../references/related-work.md#steffinlongodalessandrorenner2026), Section III, Table III and Appendix E, describe a protocol that records whether the incoming system has already been measured in basis 0 or basis 1. For a single Alice, keep her strategy fixed at their strategy I. Bob $i$ uses the protocol's two projective settings or a fixed output, controlled by a local history flag and a parameter $p_i$.

The source uses a CHSH winning-probability convention with local bound $3/4$. The correlator convention used here is $C_i=8W_i-4$. After a fixed relabelling of settings or outcomes, its Hardy table has the same CHSH orientation as ours.

For the PR specialization of their Hardy parameters, $\gamma=1/2$ and $\beta=0$. If $q_i$ is the probability that the incoming resource is still unmeasured, their equations reduce to
```math
q_1=1,\qquad
q_{i+1}=\frac{q_i(1-p_i)}2,
\qquad
C_i-2=2q_i p_i.
```
The factor $1/2$ is the probability of the input that can leave the resource unmeasured. Every Bob input is still an independent uniform bit. The local flag is internal forward memory; it is not an additional measurement outcome or a condition on retained trials.

Given any target vector $\boldsymbol\delta$ in the right-hand side of Theorem 2, choose recursively
```math
p_i=\frac{\delta_i}{2q_i}
```
whenever $q_i>0$. The recursion implies
```math
q_i
=
2^{1-i}
\left(
1-\frac12\sum_{j<i}2^{j-1}\delta_j
\right).
```
The nonnegative weighted-prefix sums are at most the full sum, so every $q_i$ is nonnegative. Whenever $q_i>0$, the condition $p_i\le1$ is exactly
```math
\sum_{j\le i}2^{j-1}\delta_j\le2.
```
Thus $0\le p_i\le1$. If $q_i=0$, all subsequent target gaps are zero; setting the remaining $p_i=0$ completes the prescription without division by zero. The protocol then has $C_i=2+\delta_i$ for every observer.

This derives attainment from the existing construction. The universal converse, rather than a new physical recycling mechanism, is what makes the projected region an optimality statement.

### Equal gaps

For
```math
\delta_i=\frac{2}{2^K-1},
```
the parameters are
```math
p_i=\frac{1}{2^{K-i+1}-1},
\qquad
q_i=\frac{2^{K-i+1}-1}{2^K-1}.
```
In particular, $p_K=1$ and $q_i p_i=1/(2^K-1)$. This is the one-sided PR specialization of the source's geometric schedule, with parameter $\mu=2$; it is not an invocation of the source's stronger sufficient condition for sharing on both wings.

Consequently,
```math
\boxed{
\max_{P\in\mathcal T_K}
\min_{1\le i\le K}(S_i-2)
=
\frac{2}{2^K-1}.
}
```

## An explicit causal probability kernel

An alternative realization makes every probability and causal constraint explicit. In this subsection use bit-valued outputs $a,b_i\in\{0,1\}$, with signs $(-1)^a,(-1)^{b_i}$ when evaluating correlators.

For each $j\in\{1,\ldots,K\}$, define
```math
P^{(j)}(a,\mathbf b\mid x,\mathbf y)
=
2^{-j}\,
\mathbf1\{a\oplus b_j=xy_j\}
\prod_{\ell=j+1}^{K}\mathbf1\{b_\ell=b_j\}.
```
An empty product equals one. Before stage $j$, the Bob outputs are independent fair bits. At stage $j$, the PR relation is used with Alice. Every later Bob copies $b_j$ and ignores his own fresh input. The index $j$ is fixed before the setting choices or chosen by source randomness independent of them.

### Normalization and causal conditions

For each input string, the free output bits are $a,b_1,\ldots,b_{j-1}$. There are $2^j$ allowed strings, each with probability $2^{-j}$, so the kernel is normalized.

Summing Alice's output gives
```math
\sum_aP^{(j)}(a,\mathbf b\mid x,\mathbf y)
=
2^{-j}
\prod_{\ell=j+1}^{K}\mathbf1\{b_\ell=b_j\},
```
which is independent of $x$. For a prefix ending before $j$, summing the later Bob outcomes gives
```math
P^{(j)}(a,b_1,\ldots,b_r\mid x,\mathbf y)
=
2^{-(r+1)},
\qquad r<j.
```
This is independent of every later input. For $r\ge j$, the prefix is
```math
2^{-j}\,
\mathbf1\{a\oplus b_j=xy_j\}
\prod_{\ell=j+1}^{r}\mathbf1\{b_\ell=b_j\},
```
which only depends on inputs up to $r$. Thus $P^{(j)}\in\mathcal T_K$.

### Marginal CHSH values

For the canonical orientation, the values are
```math
C_i(P^{(j)})=
\begin{cases}
0,&i<j,\\
4,&i=j,\\
2,&i>j.
\end{cases}
```
Before $j$, Alice and Bob $i$ are independent. At $j$, the PR relation gives $E^{xy}=(-1)^{xy}$. After $j$, averaging the independent uniform $Y_j$ gives
```math
E_i^{00}=E_i^{01}=1,\qquad
E_i^{10}=E_i^{11}=0,
```
because Bob $i$ copies $b_j$. Its own fresh setting has no effect on that output.

### Mixing the kernels

Let $D$ be the deterministic local kernel with $a=b_1=\cdots=b_K=0$. It has canonical CHSH value two for every pair.

For a target vector in Theorem 2, define weights backwards:
```math
w_i=\frac{\delta_i}{2}+\sum_{j>i}w_j,
\qquad
\ell=1-\sum_{i=1}^K w_i.
```
They obey
```math
\sum_{i=1}^K w_i
=
\frac12\sum_{i=1}^K2^{i-1}\delta_i
\le1,
```
so all weights, including $\ell$, are nonnegative. The mixture
```math
P=\ell D+\sum_{j=1}^K w_jP^{(j)}
```
is time-ordered nonsignalling and has
```math
C_i
=
2\ell+4w_i+2\sum_{j<i}w_j,
\qquad
C_i-2
=
2w_i-2\sum_{j>i}w_j
=
\delta_i.
```
As shown above, these values are the maxima $S_i$ because they are all at least two. This finishes a direct kernel proof of Theorem 2.

For the equal-gap boundary, the weights simplify to
```math
w_j=\frac{2^{K-j}}{2^K-1},
\qquad \ell=0.
```

## Sharpness of the initial-bias refinement

In the general mixture above, Alice's marginal mean is $\ell$ for both inputs: the deterministic component has output $+1$, and every PR component is unbiased. Hence
```math
R_0=1-\ell=\sum_i w_i.
```
For Alice input $x=0$, every component satisfies $a=b_K$ in bit notation. The full Bob history therefore determines Alice's output for that input, so $M_K=1$ and $R_K=0$. Consequently,
```math
\sum_i2^{i-1}\delta_i
=
2\sum_i w_i
=
2R_0.
```
Thus the initial-bias coefficient in the converse is attained as well. This does not assert a characterization for an arbitrarily prescribed pair of Alice marginal biases.

## Resources and reproducibility

The exact attaining kernels use a nonsignalling PR resource and are not quantum implementations. They require only causal forward processing: the source's choice of $j$ and the recorded PR output can be carried forward, while Alice receives no Bob input or history. All observed outputs remain binary; every fresh setting and every trial is retained.

The [quantum construction](quantum-rate.md) uses the cited Hardy protocol with an entangled two-qubit source and a finite local history flag. Its gap is compared with the same universal upper bound without claiming equality of the finite-$K$ quantum and nonsignalling optima.

[verify_tons.py](../verification/verify_tons.py) checks normalization, both classes of causal equalities, all eight marginal orientations, the residual potential and selected subsequences for exact rational kernels. It also solves the full finite TONS linear program for small $K$, providing a computation independent of the kernel parametrization.

