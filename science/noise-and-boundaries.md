# Uniform noise tolerance and boundaries of the theorems

The sharp weighted law concerns unconditional pairwise CHSH values in a specific causal experiment: one common binary Alice input/output interface, fresh uniform binary settings at each sequential Bob, and nonsignalling between Alice and the entire Bob wing. This page derives its noise consequence and gives explicit examples showing why the assumptions and data access matter.

## 1. Uniform contamination of the observed behavior

Let

$$
U_{\mathrm{seq}}(a,b_1,\ldots,b_K\mid x,y_1,\ldots,y_K)
=2^{-(K+1)}
$$

be independent uniform outputs at every interface. For $0\le p\le1$, define

$$
P^{(p)}=(1-p)P+pU_{\mathrm{seq}}.
\tag{1}
$$

This is a mixture of two valid time-ordered nonsignalling behaviors. Each pairwise marginal is

$$
P_i^{(p)}=(1-p)P_i+pU,
\qquad U(a,b\mid x,y)=\tfrac14.
$$

Every correlator, and hence every signed CHSH orientation, is multiplied by $1-p$. If $S_i$ is the largest CHSH orientation of $P_i$, then

$$
S_i^{(p)}=(1-p)S_i.
\tag{2}
$$

Write $\delta_{\min}=\min_i(S_i-2)$. If every original marginal is nonlocal, all remain nonlocal under (1) exactly when

$$
p< p_*(P):=\frac{\delta_{\min}}{2+\delta_{\min}}.
\tag{3}
$$

At equality, at least one marginal reaches the local CHSH boundary. In the two-input, two-output nonsignalling scenario, satisfying every CHSH facet is equivalent to Bell locality by [Fine's theorem](https://doi.org/10.1103/PhysRevLett.48.291).

The [weighted causal theorem](causal-bound.md) gives

$$
\delta_{\min}\le\frac{2}{2^K-1}.
$$

Substitution into (3) proves

$$
\boxed{p_*(P)\le2^{-K}.}
\tag{4}
$$

Equivalently, uniform contamination at fraction $p\ge2^{-K}$ makes at least one of the $K$ pairwise marginals local. This holds for every allowed quantum implementation, regardless of finite dimension or the particular instruments, because every such implementation satisfies the causal constraints.

### Sharpness and quantum scaling

The fair nonsignalling construction in [attainment.md](attainment.md) has

$$
S_i=2+\frac{2}{2^K-1}
$$

for every $i$. It therefore attains $p_*=2^{-K}$ over the time-ordered nonsignalling set. The construction uses a PR resource; this equality is not a quantum implementation.

For any quantum construction with common gap $\delta_K$, its tolerance under (1) is exactly $\delta_K/(2+\delta_K)$. The optimized Hardy-based quantum specialization in [quantum-rate.md](quantum-rate.md) reaches the same exponential dependence on $K$, up to polynomial factors. That comparison concerns the gap and the noise tolerance. It does not establish matching quantum sample complexity for the tests in [statistical-evidence.md](statistical-evidence.md).

### Randomizing only Alice's output

The same CHSH consequence has a local operational implementation that retains every Bob record. Independently on each source row, with probability $p$, replace Alice's recorded bit by a fair bit independent of all other variables. If $P_{\mathsf B}(\mathbf b\mid\mathbf y)$ denotes the complete Bob marginal, the resulting behavior is

$$
\widehat P^{(p)}(a,\mathbf b\mid x,\mathbf y)
=(1-p)P(a,\mathbf b\mid x,\mathbf y)
+\frac p2P_{\mathsf B}(\mathbf b\mid\mathbf y).
\tag{5}
$$

Collective nonsignalling makes $P_{\mathsf B}$ independent of $x$. Its prefix marginals obey the original temporal order, so (5) is again a valid time-ordered nonsignalling behavior. Alice's replacement bit has zero correlation with each Bob output. Therefore every pairwise CHSH value still scales exactly as $(1-p)S_i$, and (3)--(4) hold unchanged. The Bob transcript itself is preserved.

Equivalently, flip Alice's bit independently with probability $\eta\in[0,1/2]$. For binary $A$, this channel is exactly (5) with $p=2\eta$. Keeping all $K$ marginals nonlocal therefore requires

$$
\eta<\frac{\delta_{\min}}{2(2+\delta_{\min})}
\le2^{-(K+1)}.
\tag{6}
$$

The fair TONS construction attains these thresholds. Restricting $\eta$ to $[0,1/2]$ matters: for larger flip probabilities a known overall output relabelling can restore correlations.

### Which noise is being modeled

Equation (1) specifies contamination of the complete observed behavior by uniform outputs, while (5) specifies a random replacement of Alice's bit alone. They have the same pairwise CHSH attenuation. Neither formula asserts that every physical depolarizing channel, detector error, loss mechanism, drift, or setting-dependent error produces that attenuation. For a different noise mechanism, one must calculate the resulting pairwise tables before applying the causal law.

No postselection is included in (1). If a no-click event is mapped to one of the two legitimate outputs, the resulting normalized table can be tested directly; if it is discarded, the retained table and the selection procedure require a separate causal model.

## 2. Correlated settings can reuse one measurement record

Let Alice and Bob 1 share a maximally entangled qubit pair. Alice uses observables

$$
A_0=Z,\qquad A_1=X,
$$

and Bob's two sharp observables are

$$
B_0=(Z+X)/\sqrt2,\qquad B_1=(Z-X)/\sqrt2.
$$

Choose one external uniform bit $S$, independent of the state and Alice's input, and set

$$
Y_1=Y_2=\cdots=Y_K=S.
$$

Bob 1 measures $B_S$. Every later Bob repeats the same projective measurement on the transmitted qubit. Projective repeatability gives $B_i=B_1$, and every unconditional Alice--Bob marginal has

$$
S_i=2\sqrt2.
$$

For $K=2$, the fresh-uniform-input weighted inequality would require

$$
3(2\sqrt2-2)\le2,
$$

which is false. The input sequence in this example is correlated, so that inequality does not apply.

The [general evidence theorem](general-evidence-budget.md) instead charges

$$
\operatorname{TC}(Y_1,\ldots,Y_K)=(K-1)\ln2.
$$

Each marginal can have the same nonzero KL evidence rate, because later inputs select a basis already used to create the record. Later Bobs do not receive fresh entanglement conditioned on their input: their incoming postmeasurement state is already correlated with that input.

The source remains independent of the external setting vector. Correlations among the Bob settings alone do not enable a classical measurement-independent source to generate Bell-nonlocal pairwise tables. For a classical hidden variable $\lambda$, averaging a causal Bob response over earlier inputs conditional on $Y_i$ still gives a response $q_i(b\mid y_i,\lambda)$, while Alice has $q_A(a\mid x,\lambda)$. The resulting pair is local. The quantum example reuses correlations established by the first quantum measurement.

For the entropy correction, the setting vector must be revealed causally. Delivering a seed that discloses future settings to devices changes the access model. In particular, the refined Kraus record used in the quantum proof must depend only on past and present revealed settings.

## 3. The entire Bob transcript must be nonsignalling

Pairwise nonsignalling alone is insufficient. In bit notation, consider the conditional distribution

$$
P(a,b_1,\ldots,b_K\mid x,y_1,\ldots,y_K)
=
\begin{cases}
\tfrac12,&b_i=a\oplus xy_i\text{ for every }i,\\
0,&\text{otherwise}.
\end{cases}
\tag{7}
$$

Every individual Alice--Bob marginal is a PR box, and Alice's and each individual Bob's marginals are uniform. Every Alice--past-Bob prefix depends only on the inputs in that prefix.

However, for two Bobs with different inputs,

$$
b_i\oplus b_j=x(y_i\oplus y_j)
$$

reveals $x$ in their joint record. Thus the whole Bob wing is signalling from Alice. Equation (7) violates the collective nonsignalling assumption and is not an allowed process. It shows why checking only individual marginals would miss an essential constraint.

Similarly, no-backwards-signalling must constrain the joint Alice--Bob prefix, not just the Bob prefix after Alice's output has been discarded. The proofs use the joint posterior identity $P(A\mid X,H_{i-1},Y_i)=P(A\mid X,H_{i-1})$.

## 4. The common Alice interface and the actual input law

The weighted CHSH theorem uses the same two Alice settings and the same recorded Alice output for every link. The freedom to choose a CHSH orientation at each stage consists of relabellings of these existing inputs and outputs. It does not supply a different physical Alice measurement pair for each Bob.

To see the distinction, distribute $K$ Bell pairs. Let Alice's input be $X=(j,x)$, where $j\in\{1,\ldots,K\}$ chooses a pair and $x\in\{0,1\}$ chooses a CHSH observable. Alice outputs one bit from the selected pair. Bob $i$ measures pair $i$.

Conditional on $j=i$, every Alice--Bob pair can attain $2\sqrt2$. But this Alice interface has $2K$ inputs, and different links use different subsets. It is not the common two-setting experiment.

If the actual distribution of $j$ is uniform, only a fraction $1/K$ of the source rows select pair $i$; all other rows give an independent Alice outcome for that Bob. For the actual-design KL definition,

$$
\nu_i=\nu_{\mathrm{CHSH}}/K.
$$

One can see equality by restricting any local comparator to the $j=i$ block for the lower bound. For the upper bound, average an optimal comparator on that block with its simultaneous Alice-and-Bob output flip. The CHSH behavior is invariant under that flip, so convexity preserves optimality and makes both comparator marginals uniform. Extend this comparator with independent fair Alice responses on the other blocks; those blocks then match the independent uniform target tables exactly. The sum is constant and obeys the general Shannon budget.

Optimizing a different distribution of $j$ separately for each link would remove this sampling cost and give a constant optimized strength for all $K$ links. Those separately optimized quantities cannot be substituted into the actual-design budget.

## 5. Signed gaps and selected subsequences

The causal law is

$$
\sum_i2^{i-1}(S_i-2)\le2,
$$

with signed gaps. It cannot be changed to

$$
\sum_i2^{i-1}(S_i-2)_+\le2
$$

at the original indices. Let Bob 1 return an independent fair bit and leave a PR resource untouched; let Bob 2 use it. Then

$$
(S_1,S_2)=(0,4).
$$

The signed sum is $-2+2(2)=2$, while the positive-part sum is $4$.

For a specified set of observers whose nonlocality is of interest, take their ordered subsequence and marginalize the unused inputs and outputs. The reduced behavior still obeys the causal assumptions. The theorem then assigns weights $1,2,4,\ldots$ by rank in that subsequence.

## 6. Pre-input heralds and conditional certification

A history recorded before a tested input can be used to define a conditional Bell experiment. Such an experiment can have a different evidence cost from the unconditional marginal.

For example, choose a routing label $J$ uniformly from $\{1,\ldots,K\}$ before all inputs, and provide it as an accessible herald. Route the unmeasured half of a Bell pair to Bob $J$; that Bob performs a CHSH measurement. A test for link $i$ can use only rows with $J=i$. The event is independent of the test inputs, so it is a valid pre-input selection. Each active conditional experiment has the usual CHSH behavior.

The evidence per original source row is weighted by $P(J=i)=1/K$. It is incorrect to assign one full trial of evidence to every conditionally active link on every source row. Nevertheless, these herald-using tests are outside the exponential marginal-data theorem because they use an additional record.

The Shannon bound extends to this initial herald by an explicit conditioning argument. The source label $J$ is independent of all settings, and each conditional experiment at fixed $J=j$ obeys the causal assumptions. Apply the theorem separately at each $j$, then average:

$$
\sum_{i,j}P(J=j)\nu_i^{(j)}
\le H(A\mid X,J)\le H(A\mid X).
$$

Here $\nu_i^{(j)}$ is the actual-design marginal evidence in the conditional experiment. This extension is stated in [general-evidence-budget.md](general-evidence-budget.md); it does not silently redefine the theorem's original empty history $H_0$.

Selection using future settings or outcomes does not have this justification and can change the apparent Bell behavior.

<a id="global-records-can-reveal-correlations-hidden-in-every-pair"></a>

## 7. Global records can reveal correlations hidden in every pair

There is a simple quantum example in which every unconditional Alice--Bob marginal is local, while a function of the full Bob record violates CHSH.

Bob 1 draws an independent fair bit $R$, returns $B_1=R$, and passes the untouched quantum carrier and the bit forward. Bob 2 measures the carrier using input $Y_2$, obtaining $C$, and returns

$$
B_2=R\oplus C.
$$

Alice's binary measurement and Bob 2's unmasked outcome $C$ are chosen to attain the usual quantum CHSH value $2\sqrt2$. The first input $Y_1$ is unused; both Bob inputs remain independent and uniform.

The marginal pairs $(A,B_1)$ and $(A,B_2)$ are independent because of the fair mask, so both marginal KL distances to the local set are zero. But

$$
B_1\oplus B_2=C
$$

recovers the nonlocal Alice--Bob correlation from the joint record. The process obeys collective nonsignalling and joint prefix causality.

This example shows why a sum of marginal KL distances does not control the distance of the complete transcript to a global local model. It also explains why a theorem for tests using only $(X,Y_i,A,B_i)$ cannot be applied to tests using other Bob records. It does not assert that a valid test can certify a genuinely local marginal as nonlocal.

## 8. What the results do not quantify

The resource counted in the statistical theorem is evidence for separate unconditional Bell-nonlocal marginals. It is not total device-independent randomness, secret key, or the amount of nonlocality accessible from arbitrary functions of the transcript. Sequential experiments can certify joint randomness even when an individual pairwise behavior is local; see Padovan et al., [npj Quantum Information 10, 94 (2024)](https://doi.org/10.1038/s41534-024-00879-w).

The sharp TONS gap and contamination threshold also do not establish a sharp quantum sample complexity. The [statistical theorem](statistical-evidence.md) gives a necessary count, and its whitening alternative need not be KL optimal. A matching quantum test analysis remains a distinct question.
