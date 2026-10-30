# Finite-sample limits for marginal Bell certification

All logarithms on this page are natural. Relative entropy, binary relative entropy, and Shannon entropy are therefore measured in nats.

The weighted CHSH law implies an exponential necessary number of source repetitions for certifying every unconditional Alice--Bob marginal. The conclusion applies to arbitrary statistical tests of each pair's own records, including tests that use its complete probability table. It does not require a sample-mean CHSH test. The data restriction and the sampling design are part of the theorem.

## 1. The observed distribution and its local alternatives

Use the causal experiment in [model.md](model.md): one binary Alice input $X$, one binary Alice output $A$, and $K$ sequential binary Bob inputs and outputs. Each Bob input is fresh and uniform. Alice's input has a fixed full-support distribution $\mu_X$, independent of the source and all Bob inputs. Uniform Alice inputs are a useful special case, but are not necessary below.

Let

$$
P_i(a,b\mid x,y)
=P(A=a,B_i=b\mid X=x,Y_i=y)
$$

be the unconditional marginal behavior: all other Bob settings and outcomes are averaged with their actual probabilities. Its observed one-row distribution is

$$
p_i(x,y,a,b)=\mu_X(x)\mu_i(y)P_i(a,b\mid x,y),
\qquad \mu_i(0)=\mu_i(1)=\tfrac12.
$$

The local set $\mathcal L$ consists of behaviors

$$
Q(a,b\mid x,y)
=\sum_\lambda q(\lambda)q_A(a\mid x,\lambda)
q_B(b\mid y,\lambda).
$$

Every alternative uses the same prescribed input law as the observed experiment. Define the actual-design relative entropy to this set by

$$
\nu_i
=\inf_{Q\in\mathcal L}
\sum_{x,y}\mu_X(x)\mu_i(y)
D\!\left(P_i(\cdot,\cdot\mid x,y)
\middle\|Q(\cdot,\cdot\mid x,y)\right).
\tag{1}
$$

Thus $\nu_i=\inf_{Q\in\mathcal L}D(p_i\|q_i)$, with $q_i=\mu_X\mu_iQ$. The conventions are $0\ln(0/q)=0$ and $p\ln(p/0)=+\infty$ for $p>0$.

The use of KL divergence to quantify Bell-test evidence follows van Dam, Gill and Grünwald, [*The Statistical Strength of Nonlocality Proofs*](https://doi.org/10.1109/TIT.2005.851738) (`vanDamGillGrunwald2005`). Equation (1) fixes the actual input distribution. It does not optimize the Alice input distribution separately for different links. Operational distinctions between definitions of statistical strength are discussed by Gallego and Aolita, [PRA 95, 032118](https://doi.org/10.1103/PhysRevA.95.032118) (`GallegoAolita2017`).

## 2. A finite-$n$ testing lemma

Suppose the complete experiment is repeated independently $n$ times with the same behavior and input law. Different links in the same source row may be arbitrarily correlated. The data available to test $i$ are

$$
Z_i^n=((X_r,Y_{i,r},A_r,B_{i,r}))_{r=1}^n.
$$

A randomized test $\varphi_i$ takes these data and randomness independent of the experiment, and returns $1$ to certify nonlocality. Assume

$$
\Pr_{p_i^{\otimes n}}[\varphi_i=1]\ge1-\beta_i,
\qquad
\sup_{Q\in\mathcal L}
\Pr_{q_i^{\otimes n}}[\varphi_i=1]\le\alpha_i,
\tag{2}
$$

where $0<\alpha_i<1-\beta_i<1$. The type-I requirement can be stronger, for example validity against local devices with memory; requiring validity against all iid local alternatives already suffices for the lower bound.

Define

$$
d(s\|t)=s\ln\frac{s}{t}+(1-s)\ln\frac{1-s}{1-t},
\qquad c_i=d(1-\beta_i\|\alpha_i)>0.
$$

**Lemma 1.** Every test satisfying (2) obeys

$$
\boxed{n\nu_i\ge c_i.}
\tag{3}
$$

**Proof.** Fix any local $Q$, and let $s$ and $t$ be the certification probabilities under the true and local distributions. The test, including its independent randomization, is a stochastic channel. Relative-entropy data processing gives

$$
nD(p_i\|q_i)
=D(p_i^{\otimes n}\|q_i^{\otimes n})
\ge d(s\|t)
\ge d(1-\beta_i\|\alpha_i).
$$

The last inequality follows because $s\ge1-\beta_i>\alpha_i\ge t$: in this region binary relative entropy increases with $s$ and decreases with $t$. Taking the infimum over $Q$ proves (3). No asymptotic approximation is used. □

If the true source rows are correlated, the equality $D(p_i^{\otimes n}\|q_i^{\otimes n})=nD(p_i\|q_i)$ is unavailable. A separate analysis of conditional row laws is then needed; a one-row value $\nu_i$ does not by itself supply (3).

## 3. A CHSH gap controls the complete marginal KL distance

Let $S_i$ be the largest of the eight signed CHSH orientations of $P_i$, and set $\delta_i=S_i-2$. The complete two-input, two-output local characterization is used here: a valid nonsignalling behavior is local exactly when all its CHSH inequalities hold. This is the content of Fine's theorem; see [PRL 48, 291](https://doi.org/10.1103/PhysRevLett.48.291) (`Fine1982`).

**Lemma 2.** If $S_i>2$, then

$$
\boxed{\nu_i\le\ln(1+\delta_i/2).}
\tag{4}
$$

If $S_i\le2$, then $\nu_i=0$.

**Proof.** Write $P=P_i$, $S=S_i$, and let $U(a,b\mid x,y)=1/4$. For $S>2$, set

$$
t=\frac{2}{S},\qquad Q=tP+(1-t)U.
$$

This is a valid nonsignalling behavior. Each CHSH expression is linear in the correlators and vanishes on $U$, so every orientation of $Q$ is at most $tS=2$. The eight orientations include their negatives. Fine's theorem therefore implies $Q\in\mathcal L$.

For every outcome and input with $P>0$, $Q\ge tP$, hence $\ln(P/Q)\le-\ln t$. Averaging with the actual setting distribution gives $D(p\|q)\le-\ln t$, proving (4). □

This is an upper bound on the full-table distance to the local set, not a lower bound obtained from the CHSH score. The direction is essential for a necessary sample-size result. A small violation of one chosen Bell inequality need not give an upper KL bound in larger scenarios. The argument works here because all nontrivial local facets are CHSH facets.

The bound is conservative. It does not assert that the whitening alternative is KL optimal, nor that $\nu_i$ is always linear in a small CHSH gap.

## 4. Exponential necessary source count

The [weighted causal bound](causal-bound.md) remains valid when the CHSH orientation is maximized separately at each stage. Its posterior potential is invariant under these relabellings. Therefore

$$
\sum_{i=1}^K2^{i-1}\delta_i\le2.
\tag{5}
$$

Tests satisfying (2) have $\nu_i>0$ by Lemma 1. Each marginal is consequently nonlocal, so $\delta_i>0$, and Lemma 2 can be rearranged to give

$$
\delta_i\ge2(e^{\nu_i}-1).
$$

Combining this inequality with (5) proves the evidence constraint

$$
\boxed{
\sum_{i=1}^K2^{i-1}(e^{\nu_i}-1)\le1
}
\qquad\text{when every selected marginal is nonlocal.}
\tag{6}
$$

For unequal error requirements, (3) yields the finite-$n$ necessary condition

$$
\boxed{
\sum_{i=1}^K2^{i-1}\left(e^{c_i/n}-1\right)\le1.
}
\tag{7}
$$

In particular, if all tests have common levels $\alpha_i=\alpha$, $\beta_i=\beta$, then

$$
\boxed{
n\ge
\frac{d(1-\beta\|\alpha)}
{\ln\!\left(1+\dfrac{1}{2^K-1}\right)}
=\frac{d(1-\beta\|\alpha)}{-\ln(1-2^{-K})}.
}
\tag{8}
$$

The ceiling of the right-hand side is understood for integer $n$. At fixed nontrivial error probabilities this is $\Omega(2^K)$. For fixed $0<\beta<1$ and $\alpha\to0$,

$$
d(1-\beta\|\alpha)
=(1-\beta)\ln(1/\alpha)-h(\beta)+o(1),
$$

where $h$ is binary Shannon entropy in nats. Thus the joint scaling is $\Omega(2^K\ln(1/\alpha))$ in that regime.

These are necessary bounds for all marginal-data tests, not matching achievable sample complexities. The quantum construction in [quantum-rate.md](quantum-rate.md) concerns CHSH gaps and uniform-contamination tolerance. It does not establish matching quantum statistical complexity.

### Selected subsequences

The signed weighted CHSH inequality cannot be converted to a positive-part inequality while retaining arbitrary physical indices. If only $K$ specified observers are to be certified, first take their ordered subsequence and marginalize all omitted settings and records. This produces another valid time-ordered experiment. Equations (5)--(8) then use ranks $1,\ldots,K$ within that subsequence.

## 5. Individual and simultaneous guarantees

The proof applies one test at a time. The same source rows can be reused by every test, and their decisions need not be independent.

If the desired power is simultaneous,

$$
\Pr_P[\varphi_1=\cdots=\varphi_K=1]\ge1-\beta,
$$

then each component test has power at least $1-\beta$, so (8) applies with that $\beta$. Conversely, individual power $1-\beta$ does not imply this simultaneous-power guarantee. Requiring each miss probability to be at most $\beta/K$ is a sufficient union-bound design, not a necessary consequence of the causal theorem.

A familywise false-positive guarantee that implies a level-$\alpha$ guarantee for each marginal test also permits (8) with $\alpha$. Allocating $\alpha/K$ to each test is one sufficient way to obtain familywise control. An extra $\ln K$ factor from that allocation is not forced by this lower bound. If individual levels $\alpha_i$ are specified, use (7) directly.

An output vector from a single global test is covered only if each component decision is a function of its own marginal records and independent randomization. A component that uses other Bob records is a different statistical task.

## 6. What changes when more records are available

Conditioning on a valid pre-input history can reveal rare useful branches. Testing a conditional behavior and charging the probability of its history are legitimate operations, but they do not test the unconditional $P_i$ defined in Section 1. The exponential theorem does not cover such tests. The [general evidence budget](general-evidence-budget.md) gives a separate bound for history-conditioned evidence.

Nor does a small marginal $\nu_i$ imply proximity of the full sequential distribution to a globally causal null distribution. A KL-optimal local marginal need not extend to a nearby full distribution with the required causal constraints. The [masked-record example](noise-and-boundaries.md#global-records-can-reveal-correlations-hidden-in-every-pair) illustrates information present in the joint records but absent from all pairwise tables.

The sum in (6) accounts for separate marginal certification tasks. It is not the KL divergence of one global test, and it should not be interpreted as a sum of statistically independent pieces of evidence.

## 7. More general evidence budgets

For arbitrary finite alphabets and independent input settings, the companion theorem gives $\sum_i\nu_i\le H(A\mid X)$. Combining it with Lemma 1 yields

$$
n\ge\frac{\sum_i c_i}{H(A\mid X)}
$$

when the denominator is positive. For externally correlated Bob inputs revealed only causally, replace the denominator by $H(A\mid X)+\operatorname{TC}(Y_1,\ldots,Y_K)$. The quantum companion supplies the alternative budget

$$
E_F(\rho_{\mathsf A\mathsf B})
-\mathbb E_h E_F(\rho^{\mathrm{res}}_{\mathsf A\mathsf B\mid h})
+\operatorname{TC}(Y_1,\ldots,Y_K).
$$

The exact assumptions and the meaning of the residual state are given in [general-evidence-budget.md](general-evidence-budget.md). A zero budget rules out the nontrivial testing requirements (2).

## 8. Reproducible numerical checks

[verify_evidence.py](../verification/verify_evidence.py) checks the KL minimization over all 16 deterministic binary local vertices, certifies a convex first-order optimization gap, verifies the whitening construction under all orientations, and checks the Shannon and pure-branch quantum budgets on concrete sequential instruments. It also evaluates (8) with consistent logarithm units. These checks corroborate the formulas; Lemmas 1 and 2 and the causal theorem provide the proofs.
