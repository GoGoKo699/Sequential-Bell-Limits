# Causal bound on CHSH sharing

The joint causal conditions in the [model](model.md) force a weighted restriction on the CHSH values of successive Alice–Bob marginals. The weights grow with the observer's position even though all settings remain independent and uniform.

## The predictability potential

For a Bob history $h$, let $m_x(h)=\mathbb E[A\mid X=x,H=h]$ and define
```math
u(h)=\frac{m_0(h)+m_1(h)}2,
\qquad
v(h)=\frac{m_0(h)-m_1(h)}2.
```
The elementary identity
```math
|u(h)|+|v(h)|
=
\max\{|m_0(h)|,|m_1(h)|\}
```
shows that this quantity lies between zero and one. Set
```math
M_i=
\mathbb E_{H_i}\!\left[
\max\{|m_0(H_i)|,|m_1(H_i)|\}
\right],
\qquad
R_i=1-M_i.
```
For a fixed history, $(1+\max_x|m_x(h)|)/2$ is the better of the two conditional guessing probabilities for Alice's outcome. It is used here as a mathematical potential; Alice does not choose her experimental setting using the history.

In particular,
```math
R_0
=
1-\max_{x\in\{0,1\}}|\mathbb E[A\mid X=x]|.
```
The residual $R_K$ depends on the full Bob history while still referring to Alice's one fixed pair of measurement rules.

### Lemma 1: monotonicity under an additional Bob record

For every $i$,
```math
0\le M_{i-1}\le M_i\le1,
\qquad
1\ge R_{i-1}\ge R_i\ge0.
```

**Proof.** For either current setting $y$, the conditioning identities in [the model](model.md#conditioning-on-a-bob-history) give
```math
(m_0(h),m_1(h))
=
\sum_b r_i(b\mid y,h)
(m_0(h,y,b),m_1(h,y,b)).
```
The maximum of the two absolute coordinates is a convex function. Jensen's inequality, followed by averaging $y$ and $h$, proves $M_{i-1}\le M_i$. The endpoint bounds follow from $|m_x|\le1$. $\square$

## The one-step CHSH inequality

### Lemma 2: a uniform fresh setting forces a stronger recursion

For every CHSH orientation $c\in\mathcal C$ at stage $i$,
```math
C_i(c)\le4M_i-2M_{i-1}.
```
Consequently,
```math
S_i-2\le2R_{i-1}-4R_i.
```

**Proof for the canonical orientation.** Fix a positive-probability past $h=H_{i-1}$. Write $\mathbb E_y$ for averaging the new outcome $b$ with $r_i(b\mid y,h)$. The CHSH expression of the conditional table is
```math
C_i(h)
=
2\mathbb E_0[b\,u(h,0,b)]
+
2\mathbb E_1[b\,v(h,1,b)].
```
The common weights $r_i(b\mid y,h)$ for the two Alice inputs are essential to this identity. Since $b\in\{-1,+1\}$,
```math
C_i(h)
\le
2\mathbb E_0|u(h,0,b)|
+
2\mathbb E_1|v(h,1,b)|.
```
The two complementary terms satisfy
```math
\mathbb E_0|v(h,0,b)|
+
\mathbb E_1|u(h,1,b)|
\ge |v(h)|+|u(h)|.
```
Here Jensen's inequality applies separately for each $y$, because
$\mathbb E_y u(h,y,b)=u(h)$ and
$\mathbb E_y v(h,y,b)=v(h)$.

Adding the complementary terms therefore gives
```math
C_i(h)
\le
2\sum_{y=0}^1
\mathbb E_y\bigl[|u(h,y,b)|+|v(h,y,b)|\bigr]
-
2\bigl[|u(h)|+|v(h)|\bigr].
```
The current setting is uniform. The first term is four times the conditional expectation of the new potential. Averaging the past with $p_{i-1}(h)$ proves
```math
C_i\le4M_i-2M_{i-1}.
```
No joint assignment of Alice's two possible outcomes has entered the argument.

**All eight orientations.** Every sign matrix $c\in\mathcal C$ factors as
```math
c_{xy}=s_x\,t_y\,(-1)^{xy},
\qquad s_x,t_y\in\{-1,+1\}.
```
For example, take $s_0=1$, $t_0=c_{00}$, $t_1=c_{01}$ and $s_1=c_{10}c_{00}$. The product condition on $c$ fixes the remaining entry.

Algebraically relabel Alice's outcome by $a\mapsto s_xa$ and the current Bob's outcome by $b\mapsto t_yb$. This turns $C_i(c)$ into the canonical expression. Alice's two conditional means change only by signs, so the potential $\max(|m_0|,|m_1|)$ is unchanged. Relabelling the current Bob outcome is a bijection of histories and also leaves its average unchanged. Thus the same $M_{i-1},M_i$ bound every orientation.

This is a separate algebraic argument for each stage; it does not require performing different Alice measurements or different Alice outcome relabellings simultaneously. Taking the maximum over $c$ gives the stated bound for $S_i$. $\square$

## The weighted converse

### Theorem 1: CHSH sharing with a residual predictability term

For every $P\in\mathcal T_K$ and every selection of fixed CHSH orientations $c_1,\ldots,c_K$,
```math
\boxed{
\sum_{i=1}^K2^{i-1}\bigl(C_i(c_i)-2\bigr)
+
2^{K+1}R_K
\le2R_0.
}
```
In particular, independent maximizing choices at the different stages give
```math
\boxed{
\sum_{i=1}^K2^{i-1}(S_i-2)
+
2^{K+1}R_K
\le2R_0
\le2.
}
```
The gaps in this theorem are signed. No assumption $S_i\ge2$ is needed.

**Proof.** Lemma 2 gives
```math
C_i(c_i)-2\le2R_{i-1}-4R_i.
```
Multiply by $2^{i-1}$ and sum:
```math
\sum_{i=1}^K2^{i-1}\bigl(C_i(c_i)-2\bigr)
\le
\sum_{i=1}^K(2^iR_{i-1}-2^{i+1}R_i)
=
2R_0-2^{K+1}R_K.
```
The intermediate terms cancel. The same argument applies to the stagewise maxima, because Lemma 2 uses one common potential for every orientation. $\square$

The argument also applies to every initial segment of the chain. Increasing the carrier dimension, changing the instruments or adding forward classical memory cannot weaken the converse, since none of those resources changes the defining causal identities.

### Corollary 1: the largest common gap

If $S_i\ge2+\delta$ for every $i$, then
```math
\delta
\le
\frac{2R_0-2^{K+1}R_K}{2^K-1}
\le
\frac{2R_0}{2^K-1}
\le
\frac{2}{2^K-1}.
```
The [attainment result](attainment.md) reaches the final bound in $\mathcal T_K$. Quantum realizations obey the same upper bound; their lower comparison is given in [quantum-rate.md](quantum-rate.md).

The initial bias refinement matters when one of Alice's outcomes is rare. If either Alice input has a deterministic outcome, then $R_0=0$. There can then be no selected marginal with a positive CHSH gap.

## Selecting observers from a longer chain

The weights count the position within the selected collection, not the original laboratory index.

### Corollary 2: an ordered subsequence

Let $1\le i_1<\cdots<i_r\le K$. For independently chosen CHSH orientations at those stages,
```math
\boxed{
\sum_{j=1}^r2^{j-1}\bigl(C_{i_j}(c_j)-2\bigr)
+
2^{r+1}R_{i_r}
\le2R_0.
}
```
The same statement holds with $C_{i_j}(c_j)$ replaced by $S_{i_j}$.

**Proof.** Put $i_0=0$. Monotonicity gives
```math
R_{i_j-1}\le R_{i_{j-1}}
```
for every $j$, with $R_{i_0}=R_0$. Lemma 2 therefore implies
```math
C_{i_j}(c_j)-2
\le2R_{i_{j-1}}-4R_{i_j}.
```
Weighting by $2^{j-1}$ and summing proves the claim. $\square$

Equivalently, one may average the omitted settings and sum the omitted outcomes to obtain a shorter time-ordered behavior. Its ordinary marginals are exactly the selected $P_{i_j}$. Omitted physical operations are retained in the experiment; they are simply part of the causal process between the selected observers.

In particular, if a longer chain contains $r$ observers each with gap at least $\delta>0$, then
```math
\delta\le\frac{2}{2^r-1}.
```

## Why negative gaps cannot be discarded at their original indices

Consider two Bobs. Bob 1 outputs an independent fair bit and does nothing to an unused PR resource. Bob 2 uses that resource with Alice. Then
```math
S_1=0,\qquad S_2=4.
```
This is time-ordered nonsignalling. Its signed weighted sum is
```math
(S_1-2)+2(S_2-2)=-2+4=2.
```
Replacing the first gap by its positive part would give $4$, which violates the proposed replacement bound. To discuss only Bob 2, use the subsequence corollary: he becomes the first selected observer and has weight one.

The proof and finite checks are reproduced by [verify_tons.py](../verification/verify_tons.py). The checks evaluate the full causal polytope for small $K$ and exact attaining tables; the all-$K$ statement follows from the analytic argument above.

