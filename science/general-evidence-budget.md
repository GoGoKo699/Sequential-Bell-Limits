# General evidence budgets and residual entanglement

The binary CHSH theorem has a companion that applies to arbitrary finite input and output alphabets. It bounds the sum of actual-design KL distances of sequential marginals to the Bell-local set. Independent settings give a Shannon-information budget. Correlations among externally generated Bob settings contribute their total correlation. For quantum implementations, a Holevo argument replaces the classical budget by the initial entanglement of formation minus its remaining value.

All logarithms are natural. The quantum statements below assume finite-dimensional systems; no dimension bound is otherwise imposed.

## 1. Causal model and notation

Alice receives one input $X$ and returns one output $A$. Bob $i$ receives $Y_i$ and returns $B_i$, for $i=1,\ldots,K$. Set

$$
H_i=(Y_1,B_1,\ldots,Y_i,B_i),\qquad H_0=\varnothing.
$$

Let $W(a,b_1,\ldots,b_K\mid x,y_1,\ldots,y_K)$ be the conditional behavior. It obeys the following constraints.

1. **Alice-to-all-Bob nonsignalling.** The joint law of the entire Bob output string, conditional on the Bob inputs, is independent of $x$.
2. **Joint prefix causality.** For each $i$, the joint distribution of $(A,B_1,\ldots,B_i)$ depends only on $x,y_1,\ldots,y_i$. The case $i=0$ states that Alice's marginal depends only on $x$.
3. **External input law.** The inputs have distribution $\mu_X(x)\mu_Y(y_1,\ldots,y_K)$, independent of the initial source. Bob settings are generated externally and revealed in temporal order. In a physical implementation, no device has access to future inputs beyond what is predictable from already revealed inputs.

The first theorem uses a product law $\mu_Y=\prod_i\mu_i$. The later theorem allows arbitrary correlations within $\mu_Y$. These are the same causal conditions as in [model.md](model.md), with the indicated relaxation of the setting law and of alphabet sizes.

The marginal behavior is

$$
P_i(a,b\mid x,y)=P(A=a,B_i=b\mid X=x,Y_i=y).
$$

For $\mu_i$ the actual marginal law of $Y_i$, define

$$
\nu_i
=\inf_{Q\in\mathcal L_i}
\sum_{x,y}\mu_X(x)\mu_i(y)
D(P_i(\cdot,\cdot\mid x,y)\|Q(\cdot,\cdot\mid x,y)).
\tag{1}
$$

Here $\mathcal L_i$ is the Bell-local set for the relevant finite alphabets. Every link uses the same actual $\mu_X$. Formula (1) does not optimize the input distribution separately for different links. The operational background for relative-entropy Bell evidence is [van Dam, Gill and Grünwald (2005)](https://doi.org/10.1109/TIT.2005.851738), with distinctions between resource-theoretic definitions discussed by [Gallego and Aolita (2017)](https://doi.org/10.1103/PhysRevA.95.032118).

All conditionals below are needed only on events with positive probability; arbitrary response functions can be assigned on zero-probability events.

## 2. Independent settings: a Shannon budget with a remainder

**Theorem 1.** If $\mu_Y=\prod_i\mu_i$, then

$$
\boxed{
\sum_{i=1}^K\nu_i+H(A\mid X,H_K)
\le H(A\mid X).
}
\tag{2}
$$

In particular, $\sum_i\nu_i\le H(A\mid X)\le\ln|\mathcal A|$.

**Proof.** Fix stage $i$ and write $H=H_{i-1}$. Causality and the input law imply

$$
P(H=h\mid X=x,Y_i=y)=p(h),
$$

$$
P(A=a\mid X=x,Y_i=y,H=h)=P(a\mid x,h),
$$

and

$$
P(B_i=b\mid X=x,Y_i=y,H=h)=P(b\mid y,h).
\tag{3}
$$

The last identity follows from nonsignalling of the entire Bob transcript, rather than merely each Bob's individual marginal.

Construct

$$
Q_i(a,b\mid x,y)
=\sum_h p(h)P(a\mid x,h)P(b\mid y,h).
\tag{4}
$$

This is Bell local, with the past history serving as a hidden variable whose distribution is independent of the current inputs. On the lifted space $(H,X,Y_i,A,B_i)$, compare the true law with

$$
\widetilde q_i(h,x,y,a,b)
=p(h)\mu_X(x)\mu_i(y)
P(a\mid x,h)P(b\mid y,h).
$$

Using (3), its relative entropy from the true lifted law is exactly

$$
D(\widetilde p_i\|\widetilde q_i)
=I(A:B_i\mid X,Y_i,H_{i-1}).
\tag{5}
$$

Discarding $H$ and using data processing yields

$$
\nu_i\le I(A:B_i\mid X,Y_i,H_{i-1}).
\tag{6}
$$

Also $I(A:Y_i\mid X,H_{i-1})=0$. The chain rule therefore gives

$$
\begin{aligned}
\sum_i I(A:B_i\mid X,Y_i,H_{i-1})
&=I(A:H_K\mid X)\\
&=H(A\mid X)-H(A\mid X,H_K).
\end{aligned}
$$

Combining this identity with (6) proves (2). $\square$

The proof uses a classical local comparator, relative-entropy data processing, and the chain rule. It applies to all time-ordered nonsignalling behaviors satisfying the model, including quantum behaviors of arbitrary finite dimension.

## 3. Evidence conditioned on a valid past history

For independent settings, define

$$
\bar\nu_i
=\sum_h p(h)\inf_{Q_h\in\mathcal L_i}
\sum_{x,y}\mu_X(x)\mu_i(y)
D(P_i(\cdot,\cdot\mid x,y,h)\|Q_h(\cdot,\cdot\mid x,y)).
\tag{7}
$$

Each conditional behavior is nonsignalling across Alice and Bob $i$. Its product-of-marginals comparator gives

$$
\bar\nu_i
\le I(A:B_i\mid X,Y_i,H_{i-1}).
$$

Convexity of relative entropy and of the local set also gives $\nu_i\le\bar\nu_i$. Hence

$$
\boxed{
\sum_i\bar\nu_i+H(A\mid X,H_K)\le H(A\mid X).
}
\tag{8}
$$

Equation (7) is averaged per original source use: a rare history contributes its occurrence probability. It does not assign unit weight to every postselected branch. The history must precede the tested input, and the choice of a branch cannot use future settings or outcomes. Statistical tests using these histories are different from the marginal-only tests in [statistical-evidence.md](statistical-evidence.md).

### A setting-independent initial herald

Suppose an initial classical register $J$ is independent of all settings and, for every $j$ of positive probability, the conditional behavior given $J=j$ satisfies the causal assumptions. Apply Theorem 1 separately to each conditional experiment and average over $j$. This gives

$$
\sum_{i,j}p(j)\nu_i^{(j)}
+H(A\mid X,J,H_K)
\le H(A\mid X,J)\le H(A\mid X).
$$

The same argument applies to the averaged conditional-history quantities. The conditional-causality premise is explicit: an arbitrary extra variable is not automatically a valid pre-input herald merely because its unconditional distribution is independent of settings.

## 4. Externally correlated settings

Define the total correlation of the input vector by

$$
\operatorname{TC}(Y_1,\ldots,Y_K)
=\sum_{i=1}^K H(Y_i)-H(Y_1,\ldots,Y_K)
=\sum_{i=1}^K I(Y_{<i}:Y_i).
\tag{9}
$$

The initial source remains independent of the entire input vector. Correlations here are between Bob settings, not between the source and its measurement settings.

**Theorem 2.** Under the correlated external-input model of Section 1,

$$
\boxed{
\sum_i\nu_i+H(A\mid X,H_K)
\le H(A\mid X)+\operatorname{TC}(Y_1,\ldots,Y_K).
}
\tag{10}
$$

**Proof.** Write $H=H_{i-1}$. Joint prefix causality and the external input law imply

$$
P(y_i\mid x,a,h)=\mu(y_i\mid y_{<i}),\qquad
P(y_i\mid h)=\mu(y_i\mid y_{<i}).
\tag{11}
$$

In particular,

$$
I(A:Y_i\mid X,H)=0,\qquad
I(H:Y_i)=I(Y_{<i}:Y_i).
\tag{12}
$$

The history distribution is independent of $X$, although it may be correlated with $Y_i$. The lifted comparator

$$
\widetilde q_i(h,x,y,a,b)
=p(h)\mu_X(x)\mu_i(y)
P(a\mid x,h)P(b\mid y,h)
\tag{13}
$$

is normalized, and its marginal after discarding $H$ is Bell local with the actual marginal input law. Expanding the log likelihood ratio gives

$$
\begin{aligned}
D(\widetilde p_i\|\widetilde q_i)
&=I(H:Y_i)
+I(A:B_i\mid X,Y_i,H)\\
&=I(Y_{<i}:Y_i)
+I(A:B_i\mid X,Y_i,H).
\end{aligned}
\tag{14}
$$

The first term comes from replacing $p(h,y)$ by $p(h)\mu_i(y)$; the second comes from replacing the joint conditional output law by its two marginals. Equation (11) makes $P(a\mid x,h)$ the correct Alice marginal in that second term. Nonsignalling makes $P(b\mid y,h)$ the correct Bob marginal.

Data processing, summation, (9), and the same chain rule as in Theorem 1 prove (10). $\square$

### Conditional evidence with correlated inputs

For this design, replace $\mu_i(y)$ in (7) by the actual conditional law $\mu(y\mid y_{<i})$ and retain the average over $p(h)$. Call the resulting quantity $\bar\nu_i^{\mathrm{cond}}$. The product comparator still shows

$$
\sum_i\bar\nu_i^{\mathrm{cond}}+H(A\mid X,H_K)
\le H(A\mid X).
\tag{15}
$$

However, forgetting the history no longer preserves the input distribution inside each branch. The correct comparison is

$$
\nu_i\le I(Y_{<i}:Y_i)+\bar\nu_i^{\mathrm{cond}},
\tag{16}
$$

obtained by using the optimized local $Q_h$ in (13). This explains why the total-correlation term is required for unconditional marginals.

### Boundary example

Take one Bell pair and one external uniform bit $S$, with $Y_i=S$ for every $i$. Bob 1 measures the chosen sharp CHSH observable; every later Bob repeats the same observable. The outputs repeat, and every Alice--Bob marginal is the same maximally violating quantum CHSH behavior. Thus $\sum_i\nu_i=K\nu_{\mathrm{CHSH}}$, while $\operatorname{TC}(Y)=(K-1)\ln2$.

After the first setting is revealed, later settings are deterministic conditional on the history, so their conditional evidence in (15) vanishes. The example shows necessity of an input-correlation correction. It does not prove optimality of the coefficient in (10).

## 5. Quantum implementation and the residual state

Let $\rho_0=\rho_{\mathsf A\mathsf B_0}$ contain all quantum systems initially shared across Alice's wing and the entire Bob wing, including shared classical registers if present. No later cross-wing entangled resource is added. Bob operations may use arbitrary local ancillas, memories, channels, and forward feedback, and are instruments

$$
\{\mathcal I^{\,h}_{i,b\mid y}:\mathsf B_{i-1}\longrightarrow\mathsf B_i\}_b.
$$

They depend only on already revealed settings and records. Alice's output is generated by a fixed POVM $\{M_{a\mid x}\}_a$ on $\mathsf A$. Alice receives no Bob transcript before choosing or performing this measurement.

For defining the residual state, defer Alice's measurement until the Bob chain ends. Alice's operation commutes with the Bob instruments, so this deferral leaves every recorded joint probability unchanged. Let

$$
\rho^{\mathrm{res}}_{\mathsf A\mathsf B_K\mid h}
$$

be the normalized state after the Bob chain, conditioned on the public history $H_K=h$, before Alice's deferred measurement. The residual can include all Bob quantum registers that are physically retained. Registers that are actually discarded are not included.

With natural logarithms, entanglement of formation is

$$
E_F(\rho_{\mathsf A\mathsf B})
=\inf_{\rho=\sum_\lambda p_\lambda|\psi_\lambda\rangle\langle\psi_\lambda|}
\sum_\lambda p_\lambda
S(\operatorname{Tr}_{\mathsf B}|\psi_\lambda\rangle\langle\psi_\lambda|).
\tag{17}
$$

One ebit has value $\ln2$ in this convention.

**Theorem 3.** For the quantum implementation just specified,

$$
\boxed{
\sum_i\nu_i
+\sum_h p(h)E_F(\rho^{\mathrm{res}}_{\mathsf A\mathsf B_K\mid h})
\le E_F(\rho_0)+\operatorname{TC}(Y_1,\ldots,Y_K).
}
\tag{18}
$$

For independent settings the total-correlation term is zero.

## 6. Proof of the quantum budget

Fix $\varepsilon>0$ and an initial pure-state ensemble whose average entanglement is at most $E_F(\rho_0)+\varepsilon$. Introduce its label $\Lambda$ for the proof. Refine each Bob instrument into individual Kraus operators

$$
\mathcal I^{\,h}_{i,b\mid y}(\sigma)
=\sum_r K^{h}_{i,b,r\mid y}\sigma
(K^{h}_{i,b,r\mid y})^\dagger.
$$

The refined outcome is $C_i=(B_i,R_i^{\mathrm K})$. The superscript distinguishes the Kraus label from the unrelated posterior potential $R_i$ in the CHSH theorem. Let

$$
T_i=(\Lambda,Y_1,C_1,\ldots,Y_i,C_i).
$$

Every normalized branch conditioned on $T_i=t$ is pure on $\mathsf A\mathsf B_i$. The hidden labels need not be observed or communicated; they only specify a decomposition of the actual output state.

For a fixed parent branch $t$ and current input $y$, completeness of the instrument gives

$$
\rho_{\mathsf A}^{\,t}
=\sum_c p(c\mid t,y)\rho_{\mathsf A}^{\,t,y,c}.
\tag{19}
$$

Measuring Alice with any of her POVMs produces classical information about $C_i$ bounded by the Holevo quantity:

$$
I(A:C_i\mid X=x,Y_i=y,T_{i-1}=t)
\le
S(\rho_{\mathsf A}^{\,t})
-\sum_c p(c\mid t,y)S(\rho_{\mathsf A}^{\,t,y,c}).
\tag{20}
$$

This is the standard [Holevo bound](https://www.mathnet.ru/eng/ppi903). Related information-versus-entanglement accounting for local measurements appears in Badziąg et al., [PRL 91, 117901](https://doi.org/10.1103/PhysRevLett.91.117901) (bibliography key BadziagEtAl2003).

Average (20) over the actual $x,t,y$ distribution. Its right-hand side is the decrease $\Delta_i$ in the average pure-branch entropy of entanglement. Coarse-graining $C_i$ to $B_i$ cannot increase mutual information. Applying the lifted local-comparator argument with $T_{i-1}$ as the hidden record yields

$$
\nu_i
\le I(T_{i-1}:Y_i)
+I(A:B_i\mid X,Y_i,T_{i-1})
\le I(T_{i-1}:Y_i)+\Delta_i.
\tag{21}
$$

The causal external-input model continues to hold after this refinement:

$$
P(y_i\mid T_{i-1}=t)
=\mu(y_i\mid y_{<i}),
$$

because the initial ensemble label is independent of the entire input vector, and the Kraus records are generated only from past revealed inputs. Thus

$$
I(T_{i-1}:Y_i)=I(Y_{<i}:Y_i).
\tag{22}
$$

The entropy drops telescope. If

$$
\mathcal E_K=\sum_t p(t)S(\rho_{\mathsf A}^{\,t}),
$$

then

$$
\sum_i\nu_i+\mathcal E_K
\le E_F(\rho_0)+\varepsilon+\operatorname{TC}(Y).
\tag{23}
$$

For each coarse public history $h$, the refined pure states form an ensemble decomposition of the physical $\rho^{\mathrm{res}}_{\mathsf A\mathsf B_K\mid h}$. The convex-roof definition therefore gives

$$
\sum_h p(h)E_F(\rho^{\mathrm{res}}_{\mathsf A\mathsf B_K\mid h})
\le\mathcal E_K.
\tag{24}
$$

Combining (23) and (24), and taking $\varepsilon\downarrow0$, proves (18). $\square$

The proof must use one common initial ensemble and one consistent refinement through the chain. Independently minimizing different ensembles at different steps would not justify telescoping.

## 7. Residual entanglement after Alice actually measures

Suppose Alice implements an instrument with the required POVM effects and retains an output quantum system $\mathsf A'$. Let $\omega_{\mathsf A'\mathsf B_K\mid x,a,h}$ be the actual final state. Strong monotonicity of the convex-roof entanglement under this local instrument gives, for each $x,h$,

$$
\sum_a p(a\mid x,h)
E_F(\omega_{\mathsf A'\mathsf B_K\mid x,a,h})
\le E_F(\rho^{\mathrm{res}}_{\mathsf A\mathsf B_K\mid h}).
$$

For completeness, the monotonicity follows by applying the local instrument to a near-optimal pure ensemble: concavity of the unmeasured wing's entropy bounds the average pure-state entanglement after the measurement, and the convex roof bounds the coarse conditional output states from above.

Consequently, (18) remains true with the residual term replaced by

$$
\mathbb E_{X,A,H_K}
E_F(\omega_{\mathsf A'\mathsf B_K\mid X,A,H_K}).
\tag{25}
$$

If Alice's instrument destroys all entanglement, (25) is zero. The pre-Alice residual in (18) refers to the explicitly deferred experiment; it should not be described as entanglement left after a destructive Alice readout.

## 8. Scope and use in finite-sample bounds

The following features are essential to these statements.

- The complete Bob transcript is nonsignalling from Alice's input, and the joint Alice--Bob prefix is independent of future inputs.
- The input vector is independent of the initial source. For the quantum refinement, the implementation also has the stated causal access to inputs; hidden Kraus records are not allowed to depend on future settings.
- Every KL quantity here uses the actual setting distribution. Separate input optimizations do not describe the common experimental design and are outside the shared-data statistical statements. The Shannon proof specifically uses one common $\mu_X$.
- All histories are charged with their probabilities. Future postselection records and arbitrary full-transcript tests are outside (7).

Combining any of these budgets with the finite-sample lemma in [statistical-evidence.md](statistical-evidence.md) gives a necessary source count for the corresponding marginal-data test model. The quantum remainder tightens a known-state resource budget; it does not turn the calculation into a device-independent estimator of entanglement of formation.

These bounds do not bound the total device-independent randomness extractable from the complete transcript. Sequential quantum correlations can certify randomness through joint features absent from a particular pairwise marginal, as illustrated by [Padovan et al. (2024)](https://doi.org/10.1038/s41534-024-00879-w) (bibliography key PadovanEtAl2024).
