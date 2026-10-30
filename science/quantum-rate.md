# Quantum sharing at the optimal exponential rate

The [causal CHSH bound](causal-bound.md) forces the smallest marginal violation in a chain of $K$ observers to be at most $2/(2^K-1)$. This page supplies a quantum construction with common excess of order $K^{-2}2^{-K}$. Together, the two results determine the optimal exponential rate, while leaving the finite-$K$ quantum optimum and its polynomial correction open.

The measurement mechanism is inherited from **Steffinlongo, D'Alessandro and Renner, _Almost all pure entangled states enable unbounded nonlocality sharing_**, [arXiv:2607.24700v1](https://arxiv.org/pdf/2607.24700v1), particularly Eqs. (9)–(18), Table III and Appendices D–F. The contribution here is a one-sided specialization, an exact equal-margin allocation within that protocol, and its combination with a universal converse. The source's general two-sided sufficient condition is not imposed on this one-sided optimization. See the [source comparison](../references/related-work.md) and bibliography entry `SteffinlongoDAlessandroRenner2026`.

## Resource and probability contract

Each trial begins with one pure two-qubit state shared by Alice and Bob's wing. Alice performs one of two fixed binary projective measurements and records one outcome. Her two measurements are the same for every Alice–Bob marginal in that trial. Bob's qubit passes through $K$ observers together with a classical trit whose possible values are $N,0,1$. The trit starts at $N$ and is initially uncorrelated with the pair. Alice's Hilbert-space dimension is two; the transmitted Bob carrier has dimension $2\times3=6$.

Every Bob receives a fresh independent uniform input. Alice's input can also be chosen uniformly, as it is in the verification below. An observer's control depends only on his position, the predetermined protocol parameters, his own input and the incoming trit. Fresh local coins implement specified probabilities. No observer obtains Alice's input or outcome. All trials and all Bob outcomes are retained: the marginal probabilities average earlier Bob inputs and outcomes and do not condition on a favorable history.

The trit records the basis in which the qubit was first measured. It carries no additional entanglement. It is a real forward communication resource, included in the [model](model.md), rather than an uncharged assumption that each Bob receives only a qubit. No complete history register or growing carrier dimension is needed.

The target depth $K$ is fixed before the trial. The state, Alice's measurement pair and the Bob probabilities may depend on $K$. Once chosen, they remain fixed for repetitions of that experiment. Repeating the experiment $n$ times consumes $n$ prepared pairs; the result below concerns the violation from each pair, not the number of repetitions needed to certify it.

## State, projectors and CHSH convention

Let $a>0$ be a real shape parameter. Outcome labels below are $s,t\in\{+1,-1\}$, so the symbol $a$ is not an outcome. Rewriting the source's Eqs. (9)–(10) using $a=\tfrac12\cot^2\theta$ gives

$$
|\psi_a\rangle=
\frac{|00\rangle+\sqrt a\,|01\rangle+\sqrt a\,|10\rangle}
{\sqrt{1+2a}}.
\tag{Q1}
$$

Both wings use the projectors

$$
M_{+|0}=|0\rangle\langle0|,
\qquad
M_{+|1}=|v_a\rangle\langle v_a|,
\qquad
|v_a\rangle=\frac{|0\rangle+\sqrt a\,|1\rangle}{\sqrt{1+a}},
\qquad
M_{-|y}=I-M_{+|y}.
\tag{Q2}
$$

For the untouched state, define $P_{\mathrm I}(s,t|x,y)=\langle\psi_a|M_{s|x}\otimes M_{t|y}|\psi_a\rangle$. The Hardy probabilities are

$$
\begin{aligned}
P_{\mathrm I}(-,-|0,0)&=0,\\
P_{\mathrm I}(-,+|1,0)&=0,\\
P_{\mathrm I}(+,-|0,1)&=0,\\
P_{\mathrm I}(-,-|1,1)&=\gamma,
\end{aligned}
\qquad
\gamma=\frac{a^2}{(1+2a)(1+a)^2},
\qquad
\beta=P_{\mathrm I}(-,+|1,1)=a\gamma.
\tag{Q3}
$$

These are the source's Eq. (12) parameters. Its CHSH orientation is

$$
C^{\mathrm H}(P)=-E_{00}+E_{01}+E_{10}+E_{11},
\qquad
E_{xy}=\sum_{s,t}st\,P(s,t|x,y).
\tag{Q4}
$$

The local bound is two, and $P_{\mathrm I}$ has $C^{\mathrm H}(P_{\mathrm I})=2+4\gamma$. The source reports the winning probability $w$ instead; the conversion is $C^{\mathrm H}=8w-4$. This fixed orientation is distinguished from $S_i$, the maximum over all eight CHSH orientations in the [model](model.md). To use the standard orientation in the [causal theorem](causal-bound.md), Bob replaces his setting by $y'=1-y$ and reports $t'=(-1)^{y'}t$. This Bob-only relabeling turns (Q4) into $E'_{00}+E'_{01}+E'_{10}-E'_{11}$ and preserves fresh uniform settings.

## The inherited memory-controlled instrument

Alice always performs (Q2). Bob $i$ uses a number $p_i\in[0,1]$. The source's Section III instrument acts as follows; an identity operation reports $+1$.

| Incoming trit | Bob input $y=0$ | Bob input $y=1$ |
|---|---|---|
| $N$ | Measure $M_0$; set trit to $0$ | With probability $p_i$, measure $M_1$ and set trit to $1$; otherwise apply the identity and retain $N$ |
| $0$ | Measure $M_0$; retain $0$ | Apply the identity; retain $0$ |
| $1$ | Apply the identity; retain $1$ | Measure $M_1$; retain $1$ |

The measured outcome is reported whenever a measurement occurs. The register prevents a previously measured qubit from subsequently being measured in the incompatible basis. Repeating the same projective measurement preserves its outcome correlations.

For an explicit completely positive implementation, write

$$
L_{f'\leftarrow f}(O)=O\otimes|f'\rangle\langle f|
\tag{Q5}
$$

on the qubit and trit. A table entry that measures $M_y$ contributes $L_{f'\leftarrow f}(M_{t|y})$ to reported outcome $t$. An identity entry contributes $L_{f\leftarrow f}(I)$ only to outcome $+1$. For the probabilistic $N,y=1$ entry, multiply the measurement Kraus operators by $\sqrt{p_i}$ and the identity Kraus operator by $\sqrt{1-p_i}$. Distinct old flags and coin branches are separate Kraus labels. For each fixed input, the sum of $L^\dagger L$ over both reported outcomes and all hidden Kraus labels is $I_6$.

Let $\mathcal I^{(i)}_{t|y}$ denote the resulting outcome map. The full behavior is therefore

$$
P(s,t_1,\ldots,t_K|x,y_1,\ldots,y_K)
=\operatorname{Tr}\!\left[
(M_{s|x}\otimes I_6)
\bigl(\mathcal I^{(K)}_{t_K|y_K}\circ\cdots\circ
\mathcal I^{(1)}_{t_1|y_1}\bigr)
\bigl(|\psi_a\rangle\langle\psi_a|\otimes|N\rangle\langle N|\bigr)
\right],
\tag{Q6}
$$

where each Bob map acts as the identity on Alice. Complete positivity and trace preservation of the summed instruments establish positivity, normalization and the required temporal no-signalling. Alice's local measurement commutes with every Bob operation, so she cannot signal to the Bob transcript and the Bob wing cannot change her marginal.

## From the instrument to the marginal Bell value

Before Bob $i$, let $q_i$ be the probability that the flag is $N$, and let $Z_i$ be the probability that it is $1$. Define

$$
X_i=q_i p_i.
\tag{Q7}
$$

The flag transition depends on the setting and local coin, not on the measurement outcome. Averaging the earlier settings and outcomes gives the exact state decomposition

$$
\rho_i=q_i\rho\otimes|N\rangle\langle N|
+(1-q_i-Z_i)\mathcal D_0(\rho)\otimes|0\rangle\langle0|
+Z_i\mathcal D_1(\rho)\otimes|1\rangle\langle1|,
\tag{Q8}
$$

where $\rho=|\psi_a\rangle\langle\psi_a|$ and $\mathcal D_y(\rho)=\sum_t(I\otimes M_{t|y})\rho(I\otimes M_{t|y})$. Idempotence of each $\mathcal D_y$ and the instrument table prove (Q8) by induction.

Let $P_{\mathrm {II}}$ be the behavior in which Bob measures $M_0$ for input zero and outputs $+1$ for input one. Let $P_{\mathrm {III}}$ instead output $+1$ for input zero and measure $M_1$ for input one. The source's Table III and Appendix D give

$$
C^{\mathrm H}(P_{\mathrm I})=2+4\gamma,
\qquad
C^{\mathrm H}(P_{\mathrm {II}})=2,
\qquad
C^{\mathrm H}(P_{\mathrm {III}})=2-4\beta.
\tag{Q9}
$$

More strongly, the entire marginal probability table is

$$
P_i=X_iP_{\mathrm I}+(1-X_i-Z_i)P_{\mathrm {II}}+Z_iP_{\mathrm {III}}.
\tag{Q10}
$$

Thus

$$
C_i^{\mathrm H}-2=4\gamma(X_i-aZ_i),
\qquad C_i^{\mathrm H}=C^{\mathrm H}(P_i).
\tag{Q11}
$$

Equation (Q11) is a fixed-orientation identity for arbitrary control schedules. If its right-hand side is positive, then $C_i^{\mathrm H}=S_i$: two distinct nonopposite CHSH orientations sum to at most four, so a value above two excludes a larger value in another orientation. In fact, $P_{\mathrm {II}}$ and $P_{\mathrm {III}}$ are Bell-local because one Bob setting is deterministic, while $P_{\mathrm I}$ can violate only the Hardy orientation. Convexity of (Q10) therefore shows that this is the only orientation that can exceed two for any schedule. When $C_i^{\mathrm H}\le2$, it need not equal $S_i$.

The fresh uniform Bob settings give the source's Eq. (14), specialized to one wing:

$$
q_1=1,\qquad Z_1=0,\qquad
q_{i+1}=\frac{q_i-X_i}{2},\qquad
Z_{i+1}=Z_i+\frac{X_i}{2}.
\tag{Q12}
$$

Equations (Q10)–(Q12) follow from the physical instrument, including the disturbance it causes. They are not an assumption of an unchanged shared state.

## Exact equal-margin allocation

**Proposition.** For every integer $K\ge1$ and every $a>0$, the probabilities

$$
p_i=\frac{1+a}{(2+a)^{K-i+1}-1},
\qquad i=1,\ldots,K,
\tag{Q13}
$$

are valid, and the construction gives every Bob the same CHSH excess

$$
\delta_K(a)=S_i-2
=\frac{4\gamma(1+a)}{(2+a)^K-1}
=\frac{4a^2}{(1+2a)(1+a)\bigl[(2+a)^K-1\bigr]}.
\tag{Q14}
$$

This is the largest common excess within the specified one-sided fixed-Hardy protocol when only its probabilities $p_i$ are varied.

**Proof.** Put $b=2+a$, $r=b/2$ and $c=\delta/(4\gamma)$. Requiring $X_i-aZ_i=c$ in (Q12) gives

$$
Z_i=\frac ca(r^{i-1}-1),
\qquad X_i=cr^{i-1},
\qquad
q_i=2^{1-i}\left(1-c\sum_{j=0}^{i-2}b^j\right),
\tag{Q15}
$$

with an empty sum interpreted as zero. Choosing $p_K=1$, or equivalently $q_K=X_K$, yields

$$
c=\frac{1}{\sum_{j=0}^{K-1}b^j}
=\frac{1+a}{(2+a)^K-1}.
\tag{Q16}
$$

Substituting into $p_i=X_i/q_i$ gives (Q13). Its denominator is at least $1+a$, so $0<p_i\le1$, with $p_K=1$. Equation (Q11) gives a strictly positive Hardy excess, hence $C_i^{\mathrm H}=S_i$, proving (Q14).

To prove optimality within this protocol, suppose every excess is at least $4\gamma c$. Then $X_i\ge c+aZ_i$. Induction in (Q12) gives $X_i\ge cr^{i-1}$. Also, the nonnegative terminal probability $q_{K+1}$ implies

$$
\sum_{i=1}^{K}2^{i-1}X_i\le1.
\tag{Q17}
$$

Therefore $c\sum_{j=0}^{K-1}b^j\le1$. The schedule (Q13) saturates this condition, proving the stated restricted optimality. It makes no assertion that the entire Hardy family is optimal among quantum protocols. $\square$

The source's Eq. (18) has $p_i=(\mu-1)/(\mu^{K-i+1}-1)$. Equation (Q13) is precisely its specialization to $\mu=2+a$. The source chooses a larger $\mu$ to guarantee all pairs in a two-sided chain violate CHSH. The direct one-sided calculation above establishes why that larger sufficient condition is unnecessary here.

For the source's separate PR-box Hardy table, $\gamma=1/2$ and $\beta=0$. Apply the general allocation (Q13) with ratio $a=\beta/\gamma=0$, retaining $\gamma=1/2$ in (Q11); equation (Q3) describes only the quantum family. This gives $p_i=1/(2^{K-i+1}-1)$ and $S_i-2=2/(2^K-1)$. It is an inherited realizing protocol for the exact no-signalling optimum, as discussed in [attainment](attainment.md), and uses a postquantum resource.

## Optimal exponential quantum rate

Let $\delta_K^{\mathrm Q}$ be the supremum of the smallest CHSH excess over quantum realizations satisfying the [model](model.md), including arbitrary carrier dimension and forward memory. The preceding construction gives a lower bound using carrier dimension six, while the causal theorem gives an upper bound:

$$
\delta_K(4/K)\le\delta_K^{\mathrm Q}
\le\frac{2}{2^K-1}.
\tag{Q18}
$$

For the choice $a_K=4/K$,

$$
\delta_K(4/K)
=\frac{64/K^2}
{(1+8/K)(1+4/K)\bigl[(2+4/K)^K-1\bigr]}
\sim\frac{64}{e^2K^2\,2^K},
\tag{Q19}
$$

because $(2+4/K)^K=2^K(1+2/K)^K\sim e^2 2^K$. Taking $K$th roots in (Q18) proves

$$
\boxed{\lim_{K\to\infty}(\delta_K^{\mathrm Q})^{1/K}=\frac12.}
\tag{Q20}
$$

Equivalently, $-\log_2\delta_K^{\mathrm Q}=K+O(\log K)$. The exact quantum margin can still differ from the no-signalling value by a polynomial factor; (Q20) does not determine that factor.

This is a family of finite-depth experiments. Specifically, $\cot^2\theta_K=8/K$, and the state approaches a product state as $K$ grows. Alice's projectors change with that state. For a fixed $a>0$ independent of $K$, (Q14) instead has exponential base $2+a$. The calculation does not establish the optimum with any prescribed fixed initial state.

## Source count, control precision and statistical scope

The construction uses one pair per trial and a constant-dimensional transmitted carrier. Its local controls still depend strongly on the target depth. At $a_K=4/K$,

$$
p_1=\frac{1+4/K}{(2+4/K)^K-1}\sim e^{-2}2^{-K}.
\tag{Q21}
$$

Maintaining fixed relative accuracy in this smallest probability requires absolute accuracy of the same exponential order. The ideal theorem does not supply an error-tolerant method for implementing these coins or the state and projectors. It therefore separates the number of source pairs per trial from the precision of the controls.

The positive margin in (Q14) does not specify a fixed-confidence sample size. The [statistical evidence bounds](statistical-evidence.md) use a different quantity, the distance of the entire marginal distribution from the local set. Near different local boundary points, that distance need not scale in the same way with the CHSH excess. No exact quantum statistical-complexity exponent follows from (Q20). Likewise, the statement does not bound the randomness that can be certified from the joint transcript.

For the precise behavioral white-noise model and its rate consequence, see [noise and boundaries](noise-and-boundaries.md). A noise claim requires its stated channel or probability model; adding noise to a state or intermediate instrument is not automatically equivalent to rescaling every marginal CHSH value.

## Independent physical verification

Run

```bash
python verification/verify_quantum_protocol.py
```

The [verification program](../verification/verify_quantum_protocol.py) constructs (Q1)–(Q2), implements the outcome-labelled Kraus maps on the twelve-dimensional Alice–Bob–trit system, and propagates the actual density matrix. It averages earlier settings according to their uniform distribution. Every cell of every resulting marginal probability table is compared with (Q10), and every CHSH excess is compared with (Q14). The simulated probabilities are not obtained by updating the scalar recurrence (Q12).

For selected short chains, the program additionally enumerates the complete conditional distribution in (Q6). It checks normalization, nonnegativity, no signalling from Alice to the entire Bob transcript, and independence of every Alice-plus-Bob prefix from future Bob settings. Marginalizing that complete distribution must reproduce the separately propagated marginal tables. The source and standard CHSH orientations are checked against the explicit Bob-only relabeling.

The [expected fixture](../verification/expected/quantum_protocol.json) stores exact rational reference values for the declared finite cases. The suite covers different positive shape parameters, depths through twenty, and the schedule $a=4/K$. These numerical checks address the physical implementation and probability conventions; the asymptotic statement is established by the proof above.
