# Thirty milestones for Sequential Bell Limits

[Learning entrypoint](README.md) · [Scarani source bridge](scarani-bridge.md) · [Scientific overview](../README.md)

## Allocation and reading order

**M01–M10 are background/preliminaries; M11–M30 are narrative/innovation.** Ten background milestones assemble the single experiment, the possible models and the meaning of evidence. Twenty narrative milestones connect the posterior mechanism to sharp nonsignalling sharing, physical quantum scaling and scoped operational consequences. This allocation follows the project’s causal and statistical story, not the book’s chapter count or a learner’s prior knowledge.

Within each phase, local objects precede global conclusions. M10 integrates the experimental contract; M30 integrates the complete result and its limits. Dependencies refer only to earlier milestones. Each record is an understanding target for any reader, not a test, pass, schedule or personal coaching instruction. Detailed proofs and primary attribution remain in the linked scientific pages.

“Scarani” means the single selected 2019 educational anchor identified in the [bridge](scarani-bridge.md#the-single-anchor). A source described as a foundation does not contain the project theorem; the linked project page supplies that continuation.

## Background and preliminaries

<a id="m01"></a>

### M01 — One source use

**Phase:** Background/preliminaries.

**Central question:** What is actually recorded in one run?

**Understanding target:** Identify one Alice input and output, the ordered Bob inputs and outputs, and the distinction between chain length and repeated source preparations.

**Dependencies:** None.

**Story role and conceptual connection:** Start with physical operations and a data row before introducing a Bell score.

**Source pointers:** Scarani §§1.2–1.3; [experiment](../science/model.md).

<a id="m02"></a>

### M02 — Local explanations

**Phase:** Background/preliminaries.

**Central question:** What would a Bell-local explanation have to reproduce?

**Understanding target:** Explain a mixture of local response functions and why the shared-variable distribution must be independent of the tested settings.

**Dependencies:** M01.

**Story role and conceptual connection:** Connect observed probabilities to an explicit alternative model, rather than equating locality with weak correlation.

**Source pointers:** Scarani §§2.1–2.3; [local comparison tables](../science/model.md).

<a id="m03"></a>

### M03 — Scores and conventions

**Phase:** Background/preliminaries.

**Central question:** How does a probability table become a CHSH value?

**Understanding target:** Translate between bit and sign outputs, four correlators, a fixed orientation C, the eight-orientation maximum S, and the signed gap S minus two.

**Dependencies:** M01, M02.

**Story role and conceptual connection:** Separate a relabeling from changing the physical experiment; prepare the convention used by every later result.

**Source pointers:** Scarani §1.3 and §2.5; [notation bridge](scarani-bridge.md#notation-dictionary).

<a id="m04"></a>

### M04 — The local polytope

**Phase:** Background/preliminaries.

**Central question:** Why must all CHSH orientations be checked?

**Understanding target:** Explain convex mixtures of deterministic responses and the completeness of the CHSH facets for valid binary nonsignalling tables.

**Dependencies:** M02, M03.

**Story role and conceptual connection:** Link convex geometry to the later construction of a local statistical alternative.

**Source pointers:** Scarani §§2.4–2.5; [statistical Lemma 2](../science/statistical-evidence.md).

<a id="m05"></a>

### M05 — Three correlation sets

**Phase:** Background/preliminaries.

**Central question:** How do local, quantum and nonsignalling behaviors differ?

**Understanding target:** Distinguish their CHSH limits and explain why a PR behavior can establish nonsignalling sharpness without being a physical quantum construction.

**Dependencies:** M03, M04.

**Story role and conceptual connection:** Identify which theory an optimum belongs to before interpreting an attaining example.

**Source pointers:** Scarani §§3.1–3.2 and §§9.1–9.2; [attainment](../science/attainment.md).

<a id="m06"></a>

### M06 — Measurement disturbance

**Phase:** Background/preliminaries.

**Central question:** Why are outcome probabilities insufficient to describe a sequential device?

**Understanding target:** Distinguish a POVM effect from its outcome-conditioned instrument, and explain why the summed instrument is a channel that changes the state reaching later Bobs.

**Dependencies:** M01, M05.

**Story role and conceptual connection:** Extend the book’s single Bell measurement to a state-and-record transformation; the explicit instrument construction is supplied by the project.

**Source pointers:** Scarani §3.1; [quantum realizations](../science/model.md) and [instrument](../science/quantum-rate.md).

<a id="m07"></a>

### M07 — Conditioning on a history

**Phase:** Background/preliminaries.

**Central question:** What can be inferred about Alice after a Bob record is known?

**Understanding target:** Use conditional means from two actual input choices without assuming simultaneous values for incompatible Alice outcomes; omit zero-probability histories.

**Dependencies:** M02, M03, M06.

**Story role and conceptual connection:** Connect probability conditioning to the posterior quantities in the causal proof.

**Source pointers:** Scarani §§2.1–2.2; [history identities](../science/model.md#conditioning-on-a-bob-history).

<a id="m08"></a>

### M08 — Fresh inputs and ordinary marginals

**Phase:** Background/preliminaries.

**Central question:** Which causal assumptions survive when other records are forgotten?

**Understanding target:** Explain joint prefix causality, nonsignalling to the entire Bob record, and averaging earlier settings with their actual independent uniform law.

**Dependencies:** M05, M06, M07.

**Story role and conceptual connection:** Assemble the temporal model; forgetting a record does not undo its measurement disturbance.

**Source pointers:** Scarani §2.2; [ordinary marginals](../science/model.md#ordinary-pairwise-marginals).

<a id="m09"></a>

### M09 — Evidence from finite data

**Phase:** Background/preliminaries.

**Central question:** Why does a positive ideal violation not specify a sample cost?

**Understanding target:** Distinguish a behavior from empirical frequencies, KL distance from a CHSH gap, and false-positive probability from statistical power; use one common actual input design.

**Dependencies:** M02, M04, M08.

**Story role and conceptual connection:** Connect Bell geometry with hypothesis testing. The project supplies the KL definition and data-processing argument rather than assigning a second educational source.

**Source pointers:** Scarani §2.6; [observed law and testing lemma](../science/statistical-evidence.md).

<a id="m10"></a>

### M10 — Background synthesis

**Phase:** Background/preliminaries.

**Central question:** Which experiment and which certification task are being compared?

**Understanding target:** Describe one common Alice interface, fresh Bob settings, allowed forward memory, retained trials, and the differences among marginal-only, past-conditioned and full-transcript data.

**Dependencies:** M01–M09.

**Story role and conceptual connection:** Integrate the background into the exact operational contract used by the main theorem and its consequences.

**Source pointers:** Scarani Chapters 1–3 and §9.2; [model](../science/model.md), [data boundaries](../science/noise-and-boundaries.md).

## Narrative and innovation

<a id="m11"></a>

### M11 — Posterior predictability

**Phase:** Narrative/innovation.

**Central question:** Which scalar quantity tracks the causal argument?

**Understanding target:** Interpret M as the average maximum absolute Alice conditional mean and R as its complement, including the initial-bias term; do not identify R with entanglement.

**Dependencies:** M07, M10.

**Story role and conceptual connection:** Introduce the common proof quantity without granting Alice an adaptive measurement choice.

**Source pointers:** Scarani §2.2 as foundation; [predictability potential](../science/causal-bound.md#the-predictability-potential).

<a id="m12"></a>

### M12 — Averaging the new record

**Phase:** Narrative/innovation.

**Central question:** Why can the predictability potential only increase on average?

**Understanding target:** Recover each parent conditional mean by averaging its children with the same Bob weights for both Alice inputs, then apply convexity.

**Dependencies:** M08, M11.

**Story role and conceptual connection:** Turn the joint causal conditions into the conditional-mean identity needed by the one-step proof.

**Source pointers:** Scarani §§2.1–2.2 as foundation; [Lemma 1](../science/causal-bound.md#lemma-1-monotonicity-under-an-additional-bob-record).

<a id="m13"></a>

### M13 — The one-step restriction

**Phase:** Narrative/innovation.

**Central question:** Where does the factor of two between successive residuals come from?

**Understanding target:** Explain the CHSH decomposition into u and v, the complementary Jensen terms, and how a fresh uniform setting gives S minus two at most twice the old residual minus four times the new one.

**Dependencies:** M03, M11, M12.

**Story role and conceptual connection:** Locate the decisive mechanism; mere monotonicity would not yield the exponential law.

**Source pointers:** Scarani §2.5 as foundation; [Lemma 2](../science/causal-bound.md#lemma-2-a-uniform-fresh-setting-forces-a-stronger-recursion).

<a id="m14"></a>

### M14 — Independent orientations

**Phase:** Narrative/innovation.

**Central question:** Can each link choose its own strongest CHSH orientation?

**Understanding target:** Explain why the same potential is invariant under the relabelings needed for each stage, without physically changing Alice’s measurement pair between links.

**Dependencies:** M03, M11, M13.

**Story role and conceptual connection:** Make the one-step bound apply to the maxima used in the headline statement.

**Source pointers:** Scarani §2.5; [all-orientation proof](../science/causal-bound.md#the-one-step-chsh-inequality).

<a id="m15"></a>

### M15 — The weighted telescope

**Phase:** Narrative/innovation.

**Central question:** How do the local inequalities become an all-depth converse?

**Understanding target:** Explain the powers-of-two weights, cancellation of intermediate residuals, and the roles of initial bias and final residual in the stronger theorem.

**Dependencies:** M13, M14.

**Story role and conceptual connection:** Build the global causal restriction from the single-step mechanism.

**Source pointers:** Scarani §§2.2 and 2.5 as foundation; [weighted theorem](../science/causal-bound.md#the-weighted-converse).

<a id="m16"></a>

### M16 — Signed gaps and selected observers

**Phase:** Narrative/innovation.

**Central question:** Why cannot negative gaps simply be replaced by zero?

**Understanding target:** Use an idle observer followed by a PR use to distinguish signed sums from positive-part sums; reindex a selected subsequence by its own rank.

**Dependencies:** M05, M15.

**Story role and conceptual connection:** Preserve the theorem under the practically important choice of which observers are to be certified.

**Source pointers:** Scarani §9.2 as foundation; [subsequences](../science/causal-bound.md#selecting-observers-from-a-longer-chain).

<a id="m17"></a>

### M17 — Finite-resolution sharing depth

**Phase:** Narrative/innovation.

**Central question:** How many observers can all retain a prescribed nonzero margin?

**Understanding target:** Deduce the common-gap ceiling from the weighted sum and explain why arbitrarily many strictly positive violations do not imply arbitrarily many violations above a fixed threshold.

**Dependencies:** M15, M16.

**Story role and conceptual connection:** Translate a weighted inequality into the central physical consequence.

**Source pointers:** Scarani §1.3 as foundation; [common-gap corollary](../science/causal-bound.md#corollary-1-the-largest-common-gap).

<a id="m18"></a>

### M18 — Two-observer attainment

**Phase:** Narrative/innovation.

**Central question:** How can both observers reach the nonsignalling common-gap boundary?

**Understanding target:** Explain the two consumption-time branches and their unconditioned mixture; show why copying an earlier outcome gives a local CHSH value after averaging its setting.

**Dependencies:** M05, M08, M17.

**Story role and conceptual connection:** Make exact attainment concrete before extending it to arbitrary profiles.

**Source pointers:** Scarani §9.2; [worked example](scarani-bridge.md#two-observers-a-complete-example), [causal kernels](../science/attainment.md).

<a id="m19"></a>

### M19 — The full nonnegative-gap region

**Phase:** Narrative/innovation.

**Central question:** Why is the entire attainable projection a weighted simplex?

**Understanding target:** Describe the converse inclusion and the nonnegative backward mixture weights that attain any feasible nonnegative gap vector. Distinguish the projection from the full sequential polytope.

**Dependencies:** M04, M15, M18.

**Story role and conceptual connection:** Promote a balanced example to an exact region without claiming more than the proved projection.

**Source pointers:** Scarani §§2.4 and 9.1 as foundation; [Theorem 2](../science/attainment.md#theorem-2-positive-sector-projection).

<a id="m20"></a>

### M20 — Initial bias and final residual

**Phase:** Narrative/innovation.

**Central question:** Can the refinement of the bound also be saturated?

**Understanding target:** Explain how the deterministic local mixture sets Alice’s marginal bias and why the final record determines one Alice setting, making the final residual vanish.

**Dependencies:** M11, M19.

**Story role and conceptual connection:** Connect the proof’s remainder terms to an explicit attaining family, without claiming arbitrary prescribed-bias classification.

**Source pointers:** Scarani §§2.1 and 9.2 as foundation; [bias sharpness](../science/attainment.md#sharpness-of-the-initial-bias-refinement).

<a id="m21"></a>

### M21 — A physical Hardy family

**Phase:** Narrative/innovation.

**Central question:** Which quantum state and measurements replace the PR resource?

**Understanding target:** Identify the two-qubit state, its positive shape parameter, the two projectors and the Hardy CHSH orientation; separate the quantum family from the PR parameter specialization.

**Dependencies:** M05, M06, M14.

**Story role and conceptual connection:** Begin physical attainability with an explicitly specified state and measurement interface.

**Source pointers:** Scarani §§3.1–3.2; [state and projectors](../science/quantum-rate.md#state-projectors-and-chsh-convention).

<a id="m22"></a>

### M22 — The transmitted trit

**Phase:** Narrative/innovation.

**Central question:** What does the forward memory accomplish?

**Understanding target:** Explain the unmeasured, basis-zero and basis-one flags, the permitted operations in each case, and how Kraus completeness includes hidden coin outcomes.

**Dependencies:** M06, M08, M21.

**Story role and conceptual connection:** Account for disturbance and communication rather than treating later observers as sharing an untouched pair.

**Source pointers:** Scarani §3.1 as foundation; [memory-controlled instrument](../science/quantum-rate.md#the-inherited-memory-controlled-instrument).

<a id="m23"></a>

### M23 — Equal-margin allocation

**Phase:** Narrative/innovation.

**Central question:** How are the control probabilities chosen?

**Understanding target:** Connect the unmeasured and adverse-branch probabilities to the marginal CHSH value, explain the equal-margin recursion and terminal probability one, and identify its restricted optimization domain.

**Dependencies:** M21, M22.

**Story role and conceptual connection:** Turn the inherited instrument into a balanced finite-depth construction while charging the small control probabilities.

**Source pointers:** Scarani §3.2 as foundation; [allocation proof](../science/quantum-rate.md#exact-equal-margin-allocation).

<a id="m24"></a>

### M24 — The optimal quantum exponent

**Phase:** Narrative/innovation.

**Central question:** What exactly is closed by the upper and lower comparisons?

**Understanding target:** Explain why choosing the shape parameter as four divided by depth gives Kth-root limit one half, while a polynomial gap and the fixed-source problem remain.

**Dependencies:** M17, M23.

**Story role and conceptual connection:** Integrate the causal converse and physical construction without overstating finite-depth optimality.

**Source pointers:** Scarani Chapters 3 and 9 as foundation; [rate comparison](../science/quantum-rate.md#optimal-exponential-quantum-rate).

<a id="m25"></a>

### M25 — Specified readout noise

**Phase:** Narrative/innovation.

**Central question:** What kind of robustness follows from the common gap?

**Understanding target:** Derive correlator attenuation when Alice’s output is randomly replaced, distinguish replacement probability from bit-flip probability, and explain the strict threshold for every link to remain nonlocal.

**Dependencies:** M03, M17, M24.

**Story role and conceptual connection:** Translate ideal violations into a channel-specific robustness statement, not a generic hardware threshold.

**Source pointers:** Scarani §§2.1 and 3.2 as foundation; [noise channels](../science/noise-and-boundaries.md#1-uniform-contamination-of-the-observed-behavior).

<a id="m26"></a>

### M26 — A nearby local alternative

**Phase:** Narrative/innovation.

**Central question:** Why does a small maximum CHSH gap limit the full-table evidence?

**Understanding target:** Explain uniform-output mixing, use all CHSH facets to certify locality of the comparator, and obtain the upper KL bound in the direction needed for a sample lower bound.

**Dependencies:** M04, M09, M14.

**Story role and conceptual connection:** Connect the causal score restriction to a statement about arbitrary marginal-data tests.

**Source pointers:** Scarani §§2.5–2.6; [whitening lemma](../science/statistical-evidence.md#3-a-chsh-gap-controls-the-complete-marginal-kl-distance).

<a id="m27"></a>

### M27 — Necessary source repetitions

**Phase:** Narrative/innovation.

**Central question:** Which error guarantees force an exponential number of rows?

**Understanding target:** Combine iid relative-entropy additivity with testing data processing and the causal law; distinguish individual power, simultaneous power and optional union-bound allocations.

**Dependencies:** M09, M17, M26.

**Story role and conceptual connection:** State the operational statistical consequence without inferring independence across link decisions or a matching achievable rate.

**Source pointers:** Scarani §2.6; [finite-n theorem](../science/statistical-evidence.md#4-exponential-necessary-source-count), [guarantees](../science/statistical-evidence.md#5-individual-and-simultaneous-guarantees).

<a id="m28"></a>

### M28 — General evidence budgets

**Phase:** Narrative/innovation.

**Central question:** What survives beyond uniform binary CHSH?

**Understanding target:** Explain the local comparator built from past history, the Shannon telescope, probability-weighted conditional histories, the residual entanglement refinement and the correction for correlated external settings.

**Dependencies:** M07, M09, M10, M27.

**Story role and conceptual connection:** Compare broader evidence statements with the sharper, more specialized CHSH law. Use the locally supplied chain-rule and Holevo proofs.

**Source pointers:** Scarani §§2.2–2.3 and §3.1 as foundation; [companion theorems](../science/general-evidence-budget.md).

<a id="m29"></a>

### M29 — Boundaries, attribution and verification

**Phase:** Narrative/innovation.

**Central question:** Which comparisons could invalidate an overbroad interpretation?

**Understanding target:** Use correlated settings, jointly signalling PR marginals and masked records to identify the failed premise; distinguish inherited constructions, new converses, finite checks and analytic proof.

**Dependencies:** M16, M19, M22, M24, M27, M28.

**Story role and conceptual connection:** Test the global story against counterexamples and primary attribution rather than against the number of passing tests.

**Source pointers:** Scarani §§2.2, 2.6 and 9.2; [boundaries](../science/noise-and-boundaries.md), [related work](../references/related-work.md), [verification](../verification/README.md).

<a id="m30"></a>

### M30 — Global synthesis

**Phase:** Narrative/innovation.

**Central question:** What does sequential reuse permit, what does it limit, and what remains open?

**Understanding target:** Explain the common experimental contract, exact nonsignalling projection, quantum exponential rate, channel-specific noise threshold and marginal-testing lower bound as distinct conclusions. Identify the unresolved quantum polynomial factor, finite-depth optimum and statistical attainability.

**Dependencies:** M11–M29.

**Story role and conceptual connection:** Integrate the narrative into one qualified physical conclusion: indefinite strict sharing does not preserve fixed marginal resolution, but joint-transcript tasks remain different.

**Source pointers:** Scarani Chapters 1–3 and 9 as foundation; [overview](../README.md) and all canonical [scientific routes](../README.md#reading-routes).

