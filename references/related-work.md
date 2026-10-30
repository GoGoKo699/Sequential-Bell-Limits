# Related work and attribution

The results in this repository concern one common Alice outcome and an ordered sequence of Bob outcomes, with fresh independent uniform Bob inputs and joint time-ordered nonsignalling constraints. Earlier settings and outcomes are averaged in each ordinary Alice–Bob marginal. The [model](../science/model.md) allows arbitrary dimension and forward memory on Bob's wing.

The main distinction from constructive sharing results is a universal restriction on those marginals. The [causal bound](../science/causal-bound.md) proves

$$
\sum_{i=1}^{K}2^{i-1}(S_i-2)\le2
$$

and a stronger version retaining initial and final conditional-predictability terms. Here each $S_i$ is maximized separately over the eight CHSH orientations. Combined with an inherited Hardy protocol, the bound gives the [exact nonsignalling region](../science/attainment.md) of simultaneous nonnegative gaps and the common-gap optimum $2/(2^K-1)$.

The quantum implementation also uses that existing Hardy protocol. Optimizing its one-sided allocation gives a common gap asymptotic to $64/(e^2K^2 2^K)$ with a two-qubit source and classical trit memory. Together with the converse, this establishes the [optimal exponential quantum rate](../science/quantum-rate.md), while leaving the exact finite-depth quantum optimum and its polynomial factor open.

The [statistical consequences](../science/statistical-evidence.md) use established relative-entropy and hypothesis-testing tools. They concern separate certificates based on individual Alice–Bob marginals. They do not bound randomness or key obtainable from the complete sequential transcript. The [general evidence budget](../science/general-evidence-budget.md) likewise uses standard information chain rules, the Holevo bound and entanglement accounting.

| Ingredient | Prior source | Use in this repository |
|---|---|---|
| Sequential causal models and unbounded sharing | Gallego et al.; Silva et al.; Brown and Colbeck | Defines the physical question and the distinction between strict violation and a resolved finite margin. |
| Hardy sharing with local memory | Steffinlongo, D'Alessandro and Renner | Supplies the attaining mechanism; the allocation is specialized and optimized here. |
| Complete binary Bell-local characterization | Fine | Turns a bound on the largest CHSH value into an explicit local alternative. |
| Relative entropy as Bell-test evidence | van Dam, Gill and Grünwald; Gallego and Aolita | Supplies the statistical quantity and its dependence on the actual input design. |
| Information gain and residual entanglement | Holevo; Badziąg et al. | Supplies the inherited entropy inequalities used in the quantum evidence budget. |

Equation and theorem pointers below refer to the explicitly linked source versions. Published bibliographic metadata is used where available; the matching entries are in [references.bib](references.bib).

## Sequential sharing and the inherited construction

### GallegoEtAl2014

Rodrigo Gallego, Lars Erik Würflinger, Rafael Chaves, Antonio Acín and Miguel Navascués, **“Nonlocality in sequential correlation scenarios,”** *New Journal of Physics* **16**, 033037 (2014). [DOI](https://doi.org/10.1088/1367-2630/16/3/033037); [arXiv:1308.0477v2](https://arxiv.org/pdf/1308.0477v2), 20 January 2014.

This work develops sequential correlation scenarios, their causal structure and appropriate local resource models. Its sequential Bell facets involve full histories; Eq. (51), for example, separates a time-ordered local set from more general sequential behaviors. Such a local-set facet has different premises from a restriction satisfied by every joint time-ordered nonsignalling behavior. The present model inherits this sequential perspective; its converse constrains ordinary pairwise marginal CHSH values for arbitrary chain length.

### SilvaEtAl2015

Ralph Silva, Nicolas Gisin, Yelena Guryanova and Sandu Popescu, **“Multiple Observers Can Share the Nonlocality of Half of an Entangled Pair by Using Optimal Weak Measurements,”** *Physical Review Letters* **114**, 250401 (2015). [DOI](https://doi.org/10.1103/PhysRevLett.114.250401); [arXiv:1408.2272v2](https://arxiv.org/pdf/1408.2272v2), 23 September 2015.

This paper establishes sequential Bell sharing using weak measurements, including the two-observer relations $S_1=2\sqrt2G$ and $S_2=\sqrt2(1+F)$ for optimal measurement parameters with $F^2+G^2=1$. Its arbitrary-length construction uses increasingly biased Bob inputs. The violation recursion in its Eq. (12) describes decay within that construction. The uniform-input converse here instead bounds all allowed time-ordered behaviors, including those with arbitrary forward memory and postquantum resources. The biased-input construction is outside that converse's input assumptions.

### BrownColbeck2020

Peter J. Brown and Roger Colbeck, **“Arbitrarily Many Independent Observers can Share the Nonlocality of a Single Maximally Entangled Qubit Pair,”** *Physical Review Letters* **125**, 090401 (2020). [DOI](https://doi.org/10.1103/PhysRevLett.125.090401); [arXiv:2003.12105v2](https://arxiv.org/pdf/2003.12105v2), 26 August 2020.

Brown and Colbeck achieve arbitrarily many strict CHSH violations with uniform independent inputs, a maximally entangled qubit pair and no transmission of previous classical inputs or outcomes. The construction uses unequal measurement sharpness; Appendix F estimates the parameter recursion, including double-exponential scales for that choice. An existence construction and its decay estimates do not determine a universal upper bound on the best common margin.

The quantum comparison here allows a classical trit in addition to the transmitted qubit, and its state and Alice measurements vary with the target depth. Its improved exponential comparison therefore does not establish the optimum under Brown and Colbeck's qubit-only resource contract or for a prescribed fixed maximally entangled source.

### SteffinlongoDAlessandroRenner2026

Anna Steffinlongo, Nicola D'Alessandro and Martin J. Renner, **“Almost all pure entangled states enable unbounded nonlocality sharing,”** *Physical Review Letters*, accepted 20 October 2026. [DOI](https://doi.org/10.1103/pvcy-pc82); construction and equation numbers from [arXiv:2607.24700v1](https://arxiv.org/pdf/2607.24700v1), submitted 27 July 2026.

This is the direct source of the attaining mechanism. Eqs. (9)–(10) give the two-qubit state and projectors; Eq. (12) gives the Hardy parameters. Section III uses a local trit recording whether the incoming system has remained unmeasured or has been measured in either of the two bases. Table III supplies the resulting CHSH winning probabilities. Eq. (14) gives the flag recursion, Eqs. (16)–(18) the sharing conditions and geometric allocation, and Appendix E the associated derivation. Section IV includes postquantum Hardy resources such as PR boxes.

Keeping Alice at the source's strategy I gives the one-sided protocol used here. Its PR specialization has $\gamma=1/2$, $\beta=0$ and

$$
q_{i+1}=\frac{q_i(1-p_i)}2,\qquad S_i-2=2q_ip_i.
$$

The allocation $p_i=(2^{K-i+1}-1)^{-1}$ is the source's Eq. (18) at $\mu=2$ and attains the exact common gap $2/(2^K-1)$. The source's larger sufficient lower bound on $\mu$ ensures sharing on both wings; it is unnecessary in this one-sided specialization. More general choices of $p_i$ attain the entire nonnegative region proved here.

For the quantum family, write $a=\beta/\gamma$ and choose the same geometric schedule with $\mu=2+a$. The [quantum derivation](../science/quantum-rate.md) proves exact equal-margin optimality within this fixed Hardy protocol and then chooses $a=4/K$. The universal converse converts the resulting lower bound into an optimal exponential rate over all quantum realizations. Neither the memory mechanism nor the existence of quantum unbounded sharing is claimed as a new construction here. The exact quantum statistical sample-complexity exponent is not determined by this margin calculation.

### BowlesBaccariSalavrakos2020

Joseph Bowles, Flavio Baccari and Alexia Salavrakos, **“Bounding sets of sequential quantum correlations and device-independent randomness certification,”** *Quantum* **4**, 344 (2020). [DOI](https://doi.org/10.22331/q-2020-10-19-344); [arXiv:1911.11056v4](https://arxiv.org/pdf/1911.11056v4), 9 October 2020.

This work develops methods to bound sequential quantum correlations. Section 4.2 and Eq. (24) study the two-Bob CHSH tradeoff with earlier settings averaged uniformly, with numerical evidence for arbitrary-dimensional optimality of the displayed quantum curve. Section 4.3 treats a full-history Bell functional from Gallego et al. These are relevant predecessors for sequential tradeoffs. The result here concerns every chain length and the larger time-ordered nonsignalling set; its sharp projection does not assert an exact quantum two-Bob tradeoff. The paper's joint-transcript randomness task is also distinct from separate marginal certification.

### CaiEtAl2026

Zinuo Cai, Jianxin Song, Ali Asadian and Changliang Ren, **“Unified Framework for Quantum Resource Recycling via Instrument-Dependent Back-action,”** [arXiv:2605.03513v2](https://arxiv.org/pdf/2605.03513v2), 22 October 2026.

The cited version's PDF lists these four authors. It organizes sharing strategies through their quantum instruments and treats unilateral sharing and bilateral feedback. Its Eq. (5) gives an explicit CHSH recursion for a pure two-qubit state and a specified measurement family; Theorem 1 supplies parameter conditions giving strict violations for arbitrarily many observers. These constructive sufficient conditions answer a different question from a finite-margin upper bound holding for every causal behavior. In the one-sided setting with the common fixed Alice interface, the universal converse permits arbitrary instruments and forward Bob information without depending on a qubit ansatz. A two-sided chain or communication across the Alice–Bob partition requires a different model.

## Causal models and marginal projections

### RamanathanEtAl2022

Ravishankar Ramanathan, Michał Banacki, Ricard Ravell Rodríguez and Paweł Horodecki, **“Single trusted qubit is necessary and sufficient for quantum realization of extremal no-signaling correlations,”** *npj Quantum Information* **8**, 119 (2022). [DOI](https://doi.org/10.1038/s41534-022-00633-0); [arXiv:2004.14782v2](https://arxiv.org/pdf/2004.14782v2), 17 May 2022.

Theorem 8 of the cited preprint excludes nonlocal extremal time-ordered nonsignalling behaviors from the closure of the corresponding sequential quantum set. This is a statement about vertices and quantum realizability. It does not determine the projection onto the collection of ordinary Alice–Bob CHSH values. The distinction is relevant here: the exact projection is nonsignalling, while the quantum lower construction establishes only the matching exponential rate.

### Spee2021

Cornelia Spee, **“Signaling between time steps does not allow for nonlocality beyond hidden nonlocality,”** *Journal of Physics A: Mathematical and Theoretical* **54**, 455303 (2021). [DOI](https://doi.org/10.1088/1751-8121/ac2aea); [arXiv:2011.12774v2](https://arxiv.org/pdf/2011.12774v2), 25 October 2021.

The model permits signalling between the two wings at different time steps. Lemma 1 accordingly describes vertices by conditional products depending on the previous two-wing history. The present model retains nonsignalling between Alice and the complete Bob transcript, while permitting forward signalling within Bob's wing. Applying a vertex decomposition that exposes Alice's past input and output to future Bobs would change that model. The two characterizations therefore concern different causal sets.

### Weilenmann2025

Mirjam Weilenmann, **“Monogamy relations for relativistically causal correlations,”** *Nature Communications* **16**, 269 (2025). [DOI and version of record](https://doi.org/10.1038/s41467-024-54855-1), published 2 January 2025.

The main monogamy relations, including Eqs. (10)–(11), concern entropic Bell witnesses under spatial relativistic-causality constraints that can permit a setting to affect another pair's joint correlations. Those assumptions and witnesses differ from the complete Alice-versus-Bob nonsignalling condition and ordinary marginal CHSH values used here. The temporal weighted inequality should consequently be understood in its stated causal model, rather than as a consequence of a general use of the word “monogamy.”

## Bell locality, relative entropy and statistical evidence

### Fine1982

Arthur Fine, **“Hidden Variables, Joint Probability, and the Bell Inequalities,”** *Physical Review Letters* **48**, 291–295 (1982). [DOI and version of record](https://doi.org/10.1103/PhysRevLett.48.291).

For a valid nonsignalling behavior with two binary settings and outcomes on each wing, the CHSH inequalities provide the complete nontrivial local characterization. This inherited fact is essential to the statistical argument. Whitening a table until its largest CHSH value reaches two produces a Bell-local comparator, yielding $\nu_i\le\ln(1+(S_i-2)/2)$ for a nonlocal marginal. A small violation of one inequality would not provide the same complete-table upper bound in a general Bell scenario.

### vanDamGillGrunwald2005

Wim van Dam, Richard D. Gill and Peter D. Grünwald, **“The Statistical Strength of Nonlocality Proofs,”** *IEEE Transactions on Information Theory* **51**, 2812–2835 (2005). [DOI](https://doi.org/10.1109/TIT.2005.851738); [arXiv:quant-ph/0307125v2](https://arxiv.org/pdf/quant-ph/0307125v2), 1 June 2004; [author repository](https://escholarship.org/uc/item/9tw968rq).

This work develops relative entropy to local models as a measure of statistical strength, including the role of setting distributions. That interpretation is inherited. Here $\nu_i$ uses each experiment's actual setting distribution, and finite-sample testing data processing turns the causal restriction into a necessary source count for certifying every selected marginal. The temporal aggregate and its exponential dependence on the number of observers are the additional conclusions. The published author order is used in the bibliography.

### GallegoAolita2017

Rodrigo Gallego and Leandro Aolita, **“Nonlocality free wirings and the distinguishability between Bell boxes,”** *Physical Review A* **95**, 032118 (2017). [DOI](https://doi.org/10.1103/PhysRevA.95.032118); [arXiv:1611.06932v2](https://arxiv.org/pdf/1611.06932v2), 5 January 2017.

The paper distinguishes free operations and relative-entropy notions of Bell-box distinguishability, including effects of communication before the inputs are chosen. These distinctions matter for the quantity used here: the fixed-design marginal divergence is not asserted to be a monotone under every possible wiring or input redesign. Earlier Bob settings control the later marginal behavior, so optimizing a different experimental setting distribution independently for each marginal cannot simply be inserted into the temporal sum.

### ChitambarEtAl2021

Eric Chitambar, Gilad Gour, Kuntal Sengupta and Rana Zibakhsh, **“Quantum Bell nonlocality as a form of entanglement,”** *Physical Review A* **104**, 052208 (2021). [DOI](https://doi.org/10.1103/PhysRevA.104.052208); [accepted manuscript of the published article](https://link.aps.org/accepted/10.1103/PhysRevA.104.052208).

The published article treats Bell nonlocality through a channel/resource framework and introduces relative-entropy measures with input optimization. It also establishes nonadditivity for relevant bipartite classical channels. A static resource monotonicity statement therefore does not by itself give a sum over ordinary temporal marginals sharing one Alice output. The evidence proof here constructs a local comparison model separately at each stage, conditioned on the actual past, and charges that comparison to a common information budget. The published title and author order are used rather than those of an earlier preprint.

### KaurWildeWinter2020

Eneet Kaur, Mark M. Wilde and Andreas Winter, **“Fundamental limits on key rates in device-independent quantum key distribution,”** *New Journal of Physics* **22**, 023039 (2020). [DOI](https://doi.org/10.1088/1367-2630/ab6eaa); [arXiv:1810.05627v3](https://arxiv.org/pdf/1810.05627v3), 27 February 2020.

Definitions 4–5 introduce intrinsic nonlocality quantities through conditional mutual information and nonsignalling extensions. Propositions 12–13 establish superadditivity under a fully nonsignalling multipartite structure with separate Alice outputs. The temporal process here reuses one Alice output and allows forward Bob signalling. Those are different premises, so the multipartite superadditivity statement does not directly supply the temporal marginal evidence budget. The information-theoretic techniques are related; the operational targets, extension classes and input conventions must be kept explicit.

### SolymosEtAl2026

Adrian Solymos, Carlos Vieira, Cristhiano Duarte and Zoltán Zimborás, **“No-local-broadcasting theorem for nonsignaling behaviors and assemblages,”** *Physical Review A* **113**, 032209 (2026). [DOI](https://doi.org/10.1103/q5gp-yjkd); [arXiv:2211.14351v3](https://arxiv.org/html/2211.14351v3), 18 March 2026.

Theorem 1 forbids exact local broadcasting of a behavior into two copies with distinct Alice and Bob outputs under the specified locality-preserving operations. Proposition 2 proves strict growth of relative-entropy nonlocality for an exact broadcast behavior; Appendix B uses the KL chain rule in this argument. Those split-output nonsignalling hypotheses differ from a sequential Bob chain sharing one Alice outcome. The chain rule is an inherited tool, while the local comparator and quantitative temporal allocation address a different approximate sharing task.

## Information accounting and task boundaries

### Holevo1973

A. S. Holevo, **“Bounds for the Quantity of Information Transmitted by a Quantum Communication Channel,”** *Problems of Information Transmission* **9**(3), 177–183 (1973). Original Russian publication: *Problemy Peredachi Informatsii* **9**(3), 3–11 (1973). [Primary bibliographic record](https://www.mathnet.ru/eng/ppi903).

The Holevo bound limits the classical information obtainable by measuring a quantum ensemble. The quantum evidence budget uses this standard bound after refining the initial state into a pure-state ensemble and the Bob instruments into consistent outcome branches. The resulting telescoping entropy calculation is not claimed as a new information inequality.

### BadziagEtAl2003

Piotr Badziąg, Michał Horodecki, Aditi Sen(De) and Ujjwal Sen, **“Locally Accessible Information: How Much Can the Parties Gain by Cooperating?”** *Physical Review Letters* **91**, 117901 (2003). [DOI](https://doi.org/10.1103/PhysRevLett.91.117901); [arXiv:quant-ph/0304040v3](https://arxiv.org/pdf/quant-ph/0304040v3), 18 September 2003.

Lemma 1 bounds information gained in a local measurement by the decrease of average Holevo information; Eq. (2) uses the information chain rule. These are direct predecessors of information-versus-entanglement accounting for sequences of local operations. The additional step in the present quantum evidence theorem converts each Bell marginal's divergence from a local model into a charged information increment and keeps the initial entanglement-of-formation ensemble and residual branch state consistent.

### PadovanEtAl2024

Matteo Padovan, Giulio Foletto, Lorenzo Coccia, Marco Avesani, Paolo Villoresi and Giuseppe Vallone, **“Secure and robust randomness with sequential quantum measurements,”** *npj Quantum Information* **10**, 94 (2024). [DOI and version of record](https://doi.org/10.1038/s41534-024-00879-w), published 30 September 2024.

This work illustrates that joint sequential correlations can certify randomness not captured by a particular ordinary Alice–Bob marginal. Its two-Bob analysis also employs a later score conditioned on an earlier Bob setting, rather than the unconditional marginal score studied here. The distinction sets the operational boundary of the evidence results: a cost for separate marginal Bell certificates is not a bound on total randomness extracted from the full transcript, and it does not preclude advantages in that different task.
