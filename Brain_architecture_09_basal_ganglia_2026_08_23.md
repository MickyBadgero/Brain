# Brain architecture — 09 basal ganglia

**Date:** 2026-08-23
**Derived from:** `human_brain_09_basal_ganglia_2026_08_22.md` — two entries: the basal ganglia
action-selection / value loop, and the ventral pallidum. **One source file, and no other content
source.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file is checked against this one; an endpoint with no stem is unchecked, and that is
not a claim that none exists.

**Counting basis is mixed, and it is not per hemisphere.**
The basal ganglia is one of the structures the convention names as reported **whole**, so entry 1
declares **both hemispheres** with the per-side value alongside. Entry 2 has no count at all.
**The section total is therefore labelled mixed and is not presented as one number.**

**Cross-file checks contained in this file.** One line per far file whose shared edges with this one
are diffed and stemmed below. Each is checked at this rung; the findings sit at the entries.

- `01_visual_pathway`
- `05_sensorimotor_loop`
- `08_medial_temporal_lobe`
- `11_frontal_lobe`
- `12_thalamus`
- `13_neuromodulatory_systems`
- `14_brainstem_midbrain_hypothalamus`
- `17_insula_claustrum_habenula`

**The files named below as unchecked at the source carry no line above and no stemmed endpoint
anywhere in this file.** A file absent from the list is not checked, and that is not a claim that no
shared edge exists.

**Far ends.** Edges leave into `01_visual_pathway`, `05_sensorimotor_loop`,
`08_medial_temporal_lobe`, `11_frontal_lobe`, `12_thalamus`, `13_neuromodulatory_systems`,
`14_brainstem_midbrain_hypothalamus` and `17_insula_claustrum_habenula`. **A stemmed endpoint is one
whose far file is checked against this one**; an unstemmed endpoint names the file its far end sits
in and the state of that far end's declaration as the source gives it. **No far end's content is
written from memory. The source's own caution is inherited:** its claims about
`01_visual_pathway`, `02_auditory_pathway`, `03_other_senses`,
`04_dorsal_visual_parietal_stream`, `10_cerebellum`, `15_cranial_nerve_nuclei`, `16_spinal_cord`,
`19_cross_modal_integration` and `20_loop_structure` are unchecked at the source.

---

## The bundling question, and where this file leaves it

**This entry is the bundling case the design file names by name.** One source entry covers the
striatum, the pallidum, the subthalamic nucleus and the substantia nigra, and sizing runs per
structure while the dangling-edge diff needs one unique name per structure. The two permitted
responses are to write several entries here, or to record it as **a bundle whose split is owed at the
source** — and splitting is forbidden at this rung because splitting invents the arity.

**The response taken is the second, and the source has moved in a way that makes it the only
available one.** The source now names **six** sub-elements — so the arity would not be invented — and
in the same slot records that **whether these should be six entries rather than six sub-elements is a
real question and is not settled.** Splitting here would answer a question the source explicitly
holds open. **So: one entry, six sub-elements, and the split recorded as owed at the source.**

**And a second boundary problem, which is worse, because it is not a question but an inconsistency
already in force.** The **ventral pallidum** is the ventral counterpart of two of those six nuclei —
the internal globus pallidus and the substantia nigra pars reticulata — and it is a **separate entry**
while they are sub-elements. **The boundary between "sub-element of the basal ganglia" and "entry in
its own right" is drawn in one place for the dorsal loop and another for the ventral one, inside a
single file.**

**This is a name-uniqueness failure of exactly the class the dangling-edge diff cannot survive, and
it arrives through a different door than the abbreviation case.** The diff collects every structure
named on an edge and diffs that set against the set of structures with entries. Here one functional
stage — the pallidal output of the basal ganglia — carries **two names at two levels of the
hierarchy**, and the diff cannot tell that they match. The abbreviation rule guards against two
strings for one structure; this is two *levels* for one structure, and no rule currently catches it.
*(That this is the same failure mode as the abbreviation case is Claude's reading; the boundary
inconsistency itself is Class 1, stated by the source.)*

**It is consequential on the wire, not merely in the naming.** **And the two candidate sources do not
carry the same payload:** tonic inhibition alone from the dorsal nuclei, inhibition **plus a computed
relative value** from the ventral pallidum, which the source records as computing value rather than
relaying it. **So the unresolved boundary is not a labelling preference; it decides what is on a wire
that four other files already read.**

**Two of the three edges that carried the conflation are now distinguished at their far ends.**
`12_thalamus` declares a separate limbic limb reaching the mediodorsal nucleus **via the ventral
pallidum**, beside its dorsal basal-ganglia line rather than inside it; `17_insula_claustrum_habenula`
declares the ventral pallidum's habenular output on its own line beside the dorsal pallidal source.
**The two loops are told apart at the far ends now. The boundary question itself is untouched by
that** — it is still drawn in one place for the dorsal loop and another for the ventral one, and the
third edge, the internal globus pallidus's own habenular output, is the dorsal limb of the same pair.

---

## Structural invariants

**Whole-pathway co-instantiation.** Every structure here is present and active from the outset. The
loops are the substance of this section rather than a property of it:

- **The three canonical pathways are a race, and all three limbs must be live.** Direct, indirect and
  hyperdirect converge on the same output nuclei with opposite net signs. Staging any one of them
  gives a different computation, not a partial one.
- **The pallidohabenular loop closes, and every stage of it has an entry.** The internal globus
  pallidus sends a no-reward signal to the lateral habenula; the habenula brakes the dopamine cells
  of the pars compacta; the pars compacta sets the striatal balance that determines what the internal
  globus pallidus releases. **The whole loop is inside this entry except for the habenula in
  `17_insula_claustrum_habenula` and the rostromedial tegmental nucleus in
  `14_brainstem_midbrain_hypothalamus`**, through which the habenular suppression is delivered.

  **The relay is described where it lives.** `14_brainstem_midbrain_hypothalamus` types the
  rostromedial tegmental nucleus as precisely the stage this loop needs: **the GABAergic inverting
  relay** that converts the habenula's glutamatergic bad-outcome signal into inhibition of the
  dopamine cells, **which is where the sign inversion happens.** It carries a 72%-GABAergic projection
  figure and a reported core / periphery division. `13_neuromodulatory_systems` names the same route
  independently, its ventral tegmental entry declaring `← lateral habenula, via the rostromedial
  tegmental nucleus`. **So three files name the relay and one of them describes it.**

  **The loop is traceable and co-instantiation is satisfiable for it.** **What this entry still does
  not do is connect to the relay**: its own edge names it inside an endpoint rather than terminating
  on it, so **a two-hop route is written as one edge here and as an entry there.** **This loop is
  therefore unlike the cerebro-cerebellar and Papez loops, which are missing a described stage; this
  one is not.**
- **The ventral limbic loop closes through the other entry and both limbs are written at both ends.**
  The nucleus accumbens is the ventral pallidum's dominant input, and the producing entry now declares
  it as `→ the ventral pallidum, from the nucleus accumbens`; the return onto the accumbens and the
  subthalamic limb are declared there too. **Co-instantiation is satisfiable for this loop**, which it
  was not while its dominant limb had one end.

**Per-edge latency.** Every edge carries a nonzero, finite, heterogeneous latency in real time units.
**Every edge in this section reads *to derive*. There is not one timing figure of any kind in the
file.**

**And this section states a latency *ordering* as its mechanism, which makes the absence
load-bearing rather than merely untidy.** The **hyperdirect pathway** is described as a **fast global
stop**, and its speed is structural: it reaches the subthalamic nucleus from cortex directly,
bypassing the striatum, so it traverses fewer stages than either of the other two. The direct pathway
facilitates and the indirect suppresses, and which of the three arrives first at the output nuclei
determines whether an action proceeds. **A stop that arrives after the go it was meant to cancel is
not a stop.**

**So the function is a race between three routes, and the architecture can state the ordering the
biology requires and cannot state one number.** This is the same defect the amygdala entry carries
for its three arrival times, arriving here on the section's central mechanism rather than on one of
its inputs. **Recorded as a dangling requirement on the entry.**

**Three named tracts carry these edges and none has an entry**: the **ansa lenticularis**, the
**lenticular fasciculus** and the **nigrostriatal bundle**. The white-matter file's four entries are
the corpus callosum, the internal capsule, the fornix and the arcuate / superior longitudinal
fasciculus. **A tract is where the physical substrate of a latency lives**, so the three routes whose
relative timing is the mechanism have no carrier described anywhere. The source marks this
**unchecked rather than missing** — whether those three warrant entries is a decision, not a finding.

**Three endpoints in this section are classes rather than structures, and they are in two different
states.** Two are defects the source marks for repair — **"the brainstem"** and **"reticular and
extrapyramidal motor systems"**, both checked against `14_brainstem_midbrain_hypothalamus` with no
far end declaring the edge, both **owed: name the target or withdraw**. **The third is different and
is not written as a
defect:** the input from **"nearly all of cortex"** is recorded by the source as an **open question,
asked and not answered**, on the ground that splitting it would produce dozens of edges asserting one
payload and that the claim the line makes — a convergence of *nearly all* cortex — may not be
expressible as a list. **Nothing here is built on a guess at it, and it is not split.**

---

## Basal ganglia — the action-selection / value loop

*(striatum, pallidum, subthalamic nucleus, substantia nigra — carried as a bundle, per the section
head above.)*

- **Function → structure.** Action selection and gating, plus reinforcement learning driven by a
  dopaminergic reward-prediction-error signal. Desired actions are selected and competing ones
  suppressed through three canonical pathways. Dopamine from the **substantia nigra pars compacta**
  sets the balance between the two striatal cell classes and carries the reward-prediction error that
  trains the loop.

  **Divisional sub-elements: six named nuclei.** The **striatum** (caudate nucleus, putamen, and the
  **nucleus accumbens / ventral striatum**), the **external globus pallidus**, the **internal globus
  pallidus**, the **subthalamic nucleus**, the **substantia nigra pars compacta**, and the
  **substantia nigra pars reticulata**.

  **Cell-class sub-elements inside the striatum: two, and they are sub-elements rather than
  properties.** **D1-expressing medium spiny neurons** and **D2-expressing medium spiny neurons**.
  The data-flow test is met exactly: the two classes **project to different targets** — D1 to the
  internal globus pallidus and pars reticulata, D2 to the external globus pallidus — and carry the
  two competing pathways. Medium spiny neurons are **85–95%** of the striatal population, D1 and D2
  roughly equal.

  **Laminar sub-elements: not applicable** — subcortical nuclei, not cortex. A positive statement.

  **Tangential sub-elements: owed.** The cortical input is **topographically mapped** onto the
  striatum in **motor, associative and limbic sectors**, which is a tangential organisation an edge
  could terminate on — and the intralaminar input's producer already addresses two of those sectors
  separately, a sub-element-level statement this end does not carry. **The sectors are named and
  their boundaries and internal edges are not written.** Striosome / matrix compartmentation is not
  recorded at all.

  **Internal edges — the three canonical pathways:**
  - **Direct: D1 medium spiny neurons → internal globus pallidus**, and **→ substantia nigra pars
    reticulata** — inhibition of the output nuclei, which **disinhibits** the thalamus and so
    **facilitates** the selected action. Fan-in / fan-out: to derive.
  - **Indirect, three transfers: D2 medium spiny neurons → external globus pallidus → subthalamic
    nucleus → internal globus pallidus and pars reticulata** — a net **excitation** of the output
    nuclei, which **inhibits** the thalamus and so **suppresses** competing actions. **Written as
    three transfers because the sign alternates across them**; a single line naming the pathway hides
    that the net sign is a product rather than a property. Fan-in / fan-out: to derive.
  - **Hyperdirect: cortex → subthalamic nucleus → internal globus pallidus and pars reticulata** — a
    fast global **stop**. **Only the second half is an internal edge.** The first half is an
    inter-region edge that this entry's Inputs do not declare, because the cortical input line as
    worded says the projection is topographically mapped onto the striatum and the hyperdirect
    pathway bypasses the striatum entirely. **Owed at the source: write the cortex → subthalamic
    nucleus edge in Inputs. Not written here** — that would patch an inherited gap.
  - **The indirect and hyperdirect pathways share their final limb.** Both terminate through
    **subthalamic nucleus → internal globus pallidus** and **→ pars reticulata**. Those are two
    edges carrying two pathways, not four edges. **A count of pathways and a count of edges give
    different numbers here**, and the architecture carries edges.
  - **Nigrostriatal: substantia nigra pars compacta → striatum**, onto **both** cell classes — the
    **reward-prediction error**: a scalar, broadcast. *The outcome was better or worse than expected,
    by this much.* **One number, no content, no address — which is exactly why it can train the whole
    array at once and exactly why it cannot say what to do.** Fan-in / fan-out: to derive.
    **Its opposite signs on the two cell classes are the mechanism the Function field calls setting
    the balance, and they are owed** — the same scalar reaching two targets with different effects is
    a payload statement the source does not currently make.

  **What is selected, and where, is not written.** Candidate actions arrive in parallel; tonic
  inhibition leaves, selectively released. **The competition that reduces the set to one has no edge
  here** — the lateral interactions within the striatum, and the subthalamic nucleus's role in the
  global stop, are the obvious substrates and neither is typed. **This is the seventh entry in the
  source whose stated function has no declared internal substrate.**

- **Inputs.**
  - **← nearly all of cortex** (glutamatergic, topographically mapped onto the striatum) — the
    **candidate actions**: every action currently proposed by every cortical area, in parallel. **The
    payload is a set of competitors, not a decision.** Fan-in: to derive. **A class endpoint, held
    open by the source as an unanswered question and not split here.** *(A checked finding at the
    source: of the cortical entries in the nine files checked against it, five declare an output to this
    structure — premotor, dorsolateral prefrontal and ventrolateral prefrontal cortex in file 11, the
    midcingulate cortex and the insula in file 17. **All six entries of the sensorimotor-loop file
    declare none, including the primary motor cortex.** So the motor sector of this input has no
    producer end at the one region the motor sector is named for. **Owed at `05_sensorimotor_loop`.**)*
    **The source's inventory of five is short, and the count read directly off the far files is
    seven or more.** **`11_frontal_lobe` declares four, not three**: premotor cortex to the **motor**
    striatum, the dorsolateral prefrontal cortex to the **associative** striatum, the ventrolateral
    prefrontal cortex to the structure unqualified, and the orbitofrontal / ventromedial entry to the
    **ventral** striatum — the last written as its own line below rather than inside this class.
    **Three of those four name a striatal sector**, which is the tangential axis this entry marks
    *owed* under Shape: **the producers are already addressing a partition this end does not carry**,
    and the intralaminar producer named above addresses two of the same sectors. Each of the four
    also records from its side that this consumer declares its cortical source as a class, **so all
    four are two-ended in one direction only and every one of them says so.**
    **`01_visual_pathway` declares one more that the source's inventory does not count** — its
    inferotemporal cortex entry reads *→ striatum, putting the ventral stream's output into the
    action-selection loop and not only into memory and evaluation*. That matters beyond arithmetic:
    the uncounted producer is the one carrying object **identity**, which is the payload this entry's
    class line does not describe, since it types the class as *candidate actions* and not as identity.
    **The cortical producers named in files checked against this one are therefore: premotor,
    dorsolateral prefrontal, ventrolateral prefrontal and orbitofrontal / ventromedial cortex in
    `11_frontal_lobe`; the midcingulate cortex and the insula in `17_insula_claustrum_habenula`; and
    inferotemporal cortex in `01_visual_pathway`.**
  - **← intralaminar nuclei of the thalamus** (centromedian and parafascicular) — arousal and a
    thalamostriatal drive parallel to cortex; payload otherwise owed. Fan-in: to derive. *(File 12;
    the producer gives a sector split — centromedian → motor striatum, parafascicular → associative /
    limbic striatum — that this end does not carry. Owed here.)*
  - **← amygdala** (`08_medial_temporal_lobe`), onto the **ventral striatum** — the **valence tag**,
    a gain on perception, attention and memory encoding, **carrying no identity information of its
    own**. Fan-in: to derive. **Two-ended**, and this end is the fuller of the two: the producer
    types the payload as *the valence tag* and stops, where this end adds that it carries no identity
    of its own — **which is what makes it a gain and not a code.**
  - **← insula**, onto the **ventral striatum** — payload owed at both ends. Fan-in: to derive.
    *(File 17; two-ended.)*
  - **← orbitofrontal and ventromedial prefrontal cortex** (`11_frontal_lobe`), onto the **ventral
    striatum** — **value**, the expected value of the options; payload otherwise owed and untyped at
    the producer. Fan-in: to derive. *(Written separately from the cortical class because the producer
    names the ventral striatum specifically, which the class does not.)* **Two-ended, and asymmetric**:
    that entry's line reads `→ the ventral striatum` and carries no payload at all, **so this end
    types the edge alone** and the *untyped at
    the producer* note holds exactly as written.
  - **← ventral tegmental area** (`13_neuromodulatory_systems`), onto the **nucleus accumbens /
    ventral striatum** — payload owed; dopamine carrying reward-prediction error, in the producer's
    terms. Fan-in: to derive. **The two dopamine systems split by loop** — pars compacta to the motor
    loop, ventral tegmental area to the reward / limbic loop — and only one of them is inside this
    entry. **Two-ended**, the producer declaring the mesolimbic limb in the same terms and owing the
    payload from its side too.
    **The producer declares a second striatal limb that this end does not carry**: `→ the striatum's
    dopamine-modulated projection neurons`, typed as the same reward-prediction error acting as a
    **three-factor plasticity signal** gating cortico-striatal change on the direct and indirect
    pathways. **That is a payload this entry has a use for and no edge for** — the direct and indirect
    pathways are internal edges here and the D1 / D2 classes are named sub-elements, **so the far end's
    line terminates on a partition this file already carries.** The producer marks whether its two
    limbs are one projection at two grains or two targets as owed. **Owed here: accept the plasticity
    limb against the two cell classes, or establish that the nigrostriatal line below already carries
    it** — that line makes the same claim for the pars compacta and marks the opposite signs on the two
    classes owed.
  - **← lateral habenula**, via the **rostromedial tegmental nucleus**, onto the **substantia nigra
    pars compacta** — a **negative reward-prediction error**, the mirror image of the dopamine signal,
    **delivered as inhibition of the dopamine cells**. Fan-in: to derive. *(File 17.)*
    **The intermediate stage has an entry** — the rostromedial tegmental nucleus, in
    `14_brainstem_midbrain_hypothalamus`, where the sign inversion this line depends on is described
    in full. See the invariant above. **What this line still does not do is connect
    to it**: the relay is named inside the endpoint rather than written as two edges. **Owed: split it,
    or record that a named intermediate holding its own entry may stand inside an endpoint.**
  - **← ventral pallidum**, onto the **nucleus accumbens / ventral striatum** — payload owed at both
    ends. Fan-in: to derive. *(Producer is the other entry in this file, which declares it as the
    return limb of its own output line.)*
  - **← ventral pallidum**, onto the **subthalamic nucleus** — the limbic-motor interface signal;
    payload otherwise owed. Fan-in: to derive. *(Producer is the other entry in this file.)*
  - **A serotonergic input is asserted at its producer and is not written here.**
    `13_neuromodulatory_systems`'s raphe entry declares `→ striatum`, the serotonergic modulatory
    signal, and marks the endpoint a class this file was not confirmed to declare. **It does not: no
    entry here declares a serotonergic or raphe input under any name**, and the only neuromodulatory
    inputs in this section are the two dopaminergic ones — the pars compacta internally and the ventral
    tegmental area above. **Not written in**, on the same rule as the brainstem class below. **Owed at
    the source**, and the producer records its own debt as inherited, so neither architecture end may
    repair it.

- **Outputs.** All leave from the **internal globus pallidus** and / or the **substantia nigra pars
  reticulata**, and all carry the same payload, which is the best-typed payload in the section:
  **tonic inhibition, selectively released.** The payload is a **negative** — the output nuclei fire
  constantly and the selected action is the one whose inhibition **pauses**. **Nothing here carries
  the action itself**; the action lives in cortex, and this line only says which one is allowed to
  proceed. **A consumer that expects a positive command on this edge has misread the structure.**
  - **→ ventral anterior / ventral lateral thalamus** (onward to frontal and motor cortex), from the
    internal globus pallidus and pars reticulata. Fan-out: to derive. *(File 12; the consumer names
    both source nuclei, untyped there. Owed there: type it.)*
  - **→ mediodorsal thalamus**, from the internal globus pallidus and pars reticulata — the same
    payload, here a gate on which prefrontal loops may proceed. Fan-out: to derive. *(File 12;
    typed at the consumer's end, which is why it can be typed here rather than left owed.)*
  - **→ superior colliculus**, from the pars reticulata — the same payload, released to permit a
    saccade; the gate on the lateral intraparietal area's priority map. Fan-out: to derive. *(File
    14. **Two-ended and agreeing**, and the consumer types it in the same terms: the saccade is
    permitted by a pause, and its informative event is a **cessation**.)*
  - **→ lateral habenula**, from the internal globus pallidus — the basal-ganglia **"no-reward"
    signal**, in the consumer's terms; payload otherwise owed. Fan-out: to derive. *(File 17.)*
  - **→ ventral pallidum**, from the **nucleus accumbens / ventral striatum** (GABAergic,
    substance-P) — the limbic loop's selection: which motivated action has been chosen. Fan-out: to
    derive. *(Consumer is the other entry in this file.)* **This edge does not leave from the internal
    globus pallidus or the pars reticulata**, and it is the first output of this entry that does not.
    **The slot's opening sentence is therefore no longer true of every line under it**, which is the
    bundling question arriving as a formatting fact: the ventral loop's output stage is a sub-element
    of this entry and a peer entry at once.
  - **→ ventral pallidum**, from the **subthalamic nucleus** — payload owed at both ends. Fan-out: to
    derive. *(Consumer is the other entry in this file.)*
  - **→ thalamic reticular nucleus**, from the internal globus pallidus and pars reticulata —
    GABAergic inhibition; payload owed. Fan-out: to derive. *(File 12, which records that **whether
    these terminate on that nucleus or directly on the relay nuclei is not distinguished and is
    owed** there. **Carried with the same ambiguity here: if they terminate on the relay nuclei
    directly, this edge and the two thalamic edges above are the same projection described
    twice.**)*
  - **→ the brainstem** — payload owed. **A class endpoint that does not resolve**; no entry in
    `14_brainstem_midbrain_hypothalamus` declares an input from this structure as a class. **One
    entry there declares a named one and it is written at neither end here**: the rostromedial
    tegmental nucleus declares `← the substantia nigra`, a lesser input with the payload owed, and
    marks its far end owed at this file. **That nucleus is already load-bearing in this section** —
    it is the inverting relay the pallidohabenular loop runs through. **Owed: name the target of
    this line or withdraw it, and write the substantia nigra limb. Not written as an edge here.**

- **Sizing.** Basis: **whole — both hemispheres**, with the per-side value alongside.

  | sub-element | count | basis | bits | parameter memory |
  |---|---|---|---|---|
  | striatum (caudate, putamen, accumbens) | **no count of its own** | — | ≤ 16 | to derive |
  | external globus pallidus | order 10⁵ | per side | ≤ 16 | to derive |
  | internal globus pallidus | order 10⁵ | per side | ≤ 16 | to derive |
  | subthalamic nucleus | ~560,000 | per side | ≤ 16 | ≤ 1.12 MB |
  | substantia nigra pars compacta (dopaminergic) | ~400,000–500,000 | per side | ≤ 16 | ≤ 0.80–1.00 MB |
  | substantia nigra pars reticulata | order 10⁵ | per side | ≤ 16 | to derive |
  | **structure total** | **>200M** | **both hemispheres** | ≤ 16 | **≤ 400 MB whole, ≤ 200 MB per side** |

  **The partition does not close, and it fails in the opposite direction to the amygdala's.** Two of
  six sub-elements have a count; three have an **order of magnitude and not a number**; the striatum
  — which holds nearly the whole population — has no count of its own and exists in the table only as
  the residual of a headline. **Taking the stated order at its ends, the non-striatal nuclei come to
  1.26M to 3.76M per side, so the striatum is 96.2% to 98.7% of the count.** The headline is
  therefore a striatal count wearing the whole structure's name.

  **And the sub-elements the edges leave from are exactly the ones with no count.** Every output edge
  in this entry departs from the internal globus pallidus, the pars reticulata, or both. **Both read
  *hundreds of thousands*.** In the amygdala the emitting nucleus is the best-measured of the small
  ones; here it is the worst. **Allocation is blocked precisely at the emitting sub-elements**, which
  is the least useful place for it to be blocked.

  **The convergence the source calls "the selection" inherits that 9× spread.** Something over 100M
  striatal cells per side reduce onto output nuclei of order 10⁵ per side: **1,000:1 at 10⁵,
  200:1 at 5×10⁵, 111:1 at 9×10⁵.** The source states the ratio *is* the selection, in the sense
  that it is the arithmetic the competition has to perform — **so the one number the mechanism rests
  on is open across a factor of nine**, and every fan-in and fan-out slot in this entry reads unknown.

  **Sensitivity, re-derived.** Fan-in is absent throughout, so 16 bits is the log₂ ceiling doing all
  the work and 400 MB is a ceiling rather than an estimate. What would move it is a synapse count: at
  a fan-in of 30,000 the store is 15 bits and 375 MB; at 10,000, 14 bits and 350 MB; at 1,000, 10
  bits and 250 MB. **The count is the sensitive term and the fan-in is not** — the same result the
  design file measured at V1, measured again here.

- **Shape.** **Non-laminated nucleus, rank 2: (cell class, N)** for the pallidal, subthalamic and
  nigral sub-elements — no orderly map is recorded for any of them.
  **The striatum is a different shape from the rest of its own entry, and the axis is owed.** The
  cortical input is topographically mapped onto motor, associative and limbic sectors, which is a
  tangential organisation; no boundaries, no pitch and no internal edges between sectors are written.
  So the striatum reads **(cell class, sector, N)** with the cell-class axis at extent 2 (D1, D2,
  populated only as a percentage of the whole) and **the sector axis named but unbounded.**
  **The tile calculation cannot start:** no thickness, no surface area, and no pitch anywhere in the
  section.
  **Density cross-check, re-derived:** >200M over ~10 cm³ is **~20,000 neurons/mm³**, closing against
  the source's figure — ordinary grey-matter packing. Across a soft 8–12 cm³ the range is
  **16,667 to 25,000/mm³**. The pallidum, subthalamic nucleus and substantia nigra have soft
  per-nucleus volumes, so **the cross-check covers the striatum and nothing else** — which is
  consistent, since the striatum is where nearly all the neurons are.
  **The cross-species ladder is the one place a figure has an independent check**, and it holds: the
  subthalamic nucleus runs ~5,400 mouse, ~25,000 rat, ~155,000 macaque, ~560,000 human — the
  human-to-macaque step re-derives as **3.61×** against the source's ~3.6×.

- **Edge latency.** All edges **to derive.** No timing figure of any kind. **The ordering the
  hyperdirect pathway requires is stated and unnumbered** — see the invariants above.

- **Invariant conformance.** Co-instantiation: satisfied for the three canonical pathways, which are
  all internal and all live; **satisfiable for the pallidohabenular loop**, whose intermediate stage
  — the rostromedial tegmental nucleus — holds a full entry in
  `14_brainstem_midbrain_hypothalamus`, **though this entry names it inside an endpoint rather than
  terminating on it, so the route is one edge here and two stages there.** Per-edge latency:
  satisfied in form, all to derive — **and the section's mechanism is a race with no times on it.**

- **Justification (biological).** The counts carry the architecture and they say something the prose
  does not. **A structure that is 96–99% striatum by cell count emits entirely from nuclei that are
  fractions of a percent of it.** Whatever the selection is, it is not a transformation that preserves
  dimensionality: it is a reduction of order 10²–10³ performed by a population three orders of
  magnitude smaller than the one proposing candidates. **The payload agrees independently**: what
  arrives is a *set of competitors* and what leaves is *which one is allowed to proceed* — the
  identity of the action is never on the output wire at all. **Count ratio and payload loss are the
  same fact measured two ways**, which is the same pattern the amygdala's 11:1 funnel carries in
  `08_medial_temporal_lobe`.
  The second justification is about the training signal and is a structural claim about breadth. The
  nigrostriatal edge carries **one scalar to the entire striatal array** — no address, no content.
  **A signal with no address can train everything simultaneously and can specify nothing**, which is
  precisely the division of labour the entry describes: cortex proposes what, the striatum learns how
  much, and dopamine says only better-or-worse-than-expected.

## Ventral pallidum

- **Function → structure.** The **output stage of the limbic (ventral) basal-ganglia loop** — the
  ventral counterpart of the internal globus pallidus and substantia nigra pars reticulata named in
  the entry above, and the chief target of the nucleus accumbens. The limbic final common pathway by
  which motivational value is translated toward action.
  **But it is not a passive relay**: its neurons **code the relative value of reward outcomes faster
  and more robustly than the upstream accumbens**, carrying reward-prediction-like signals. **A value
  hub in its own right**, and this is what makes the boundary question consequential rather than
  cosmetic.
  Its **posterior pole holds an opioid "hedonic hotspot"** where μ-opioid stimulation amplifies the
  **liking** reaction to reward, while GABAergic disinhibition drives **wanting** — incentive
  salience.

  **Divisional sub-elements: one, and it is spatial.** The **posterior pole** holding the hedonic
  hotspot; the rest of the structure is undivided here. **Owed: whether the anterior / posterior
  division is a boundary or a gradient**, and what the remainder should be called.
  **The hotspot is a sub-element by the data-flow test and not merely a region of interest** — the
  Function field assigns it a payload the rest of the structure does not carry, and two dissociable
  outputs follow from it. **Every output edge below is written as leaving the structure as a whole.
  Owed: establish which outputs leave the hotspot.**
  **Laminar sub-elements: not applicable.** **Cell-class sub-elements: unknown** — GABAergic
  disinhibition and μ-opioid receptors are named without saying whether they belong to separable
  populations. **Internal edges: owed, all of them.**

  **Liking and wanting are a payload claim the Outputs slot does not carry, and neither word appears
  on any edge.** If the dissociation is real on the wire then two different payloads leave this
  structure and the source declares one. **Owed: type them, or record that they are behavioural
  categories rather than payloads.** They are the entry's most distinctive claim and the completion
  test passes on neither — *liking* and *wanting* are phrases, not types with a range and a frame.

- **Inputs.**
    - **← nucleus accumbens / ventral striatum** (GABAergic, substance-P) — **the dominant input** —
    the limbic loop's selection: which motivated action has been chosen. Fan-in: to derive. **The
    producer is a sub-element of the other entry in this file and declares it** — this is the ventral
    loop's equivalent of the direct pathway and **is the reason this entry exists.**
  - **← amygdala** (`08_medial_temporal_lobe`) — the **valence tag**; payload otherwise owed.
    Fan-in: to derive. **Two-ended and checked: the producer declares it and marks the payload owed at
    its end too**, so both ends agree the edge exists and both agree it is untyped.
  - **← hippocampal formation** (`08_medial_temporal_lobe`), from the **subiculum** — episodic
    **context**; payload otherwise
    owed. Fan-in: to derive. *(File 8.)*
  - **← orbital and medial prefrontal cortex, including infralimbic cortex** (`11_frontal_lobe`) —
    **value**, the expected value of the options; payload otherwise owed. Fan-in: to derive.
    **Two-ended.** That file's orbitofrontal / ventromedial entry declares `→ the ventral pallidum`
    **on its own line**, separately from its ventral-striatal one.
    **The producer carries this line's parenthesis from its own side**, recording that this
    consumer's line names infralimbic cortex, that infralimbic cortex is area 25, and that area 25 is
    therefore **a sub-element of that structure which its heading names and no edge of its own uses.**
    **So both ends agree the sub-element is named at one end and used at neither**, which is a
    sharper statement of the debt than either end could make alone. **Payload owed at the producer**,
    whose line is untyped.
  - **← lateral hypothalamus** — **need state**; payload otherwise owed. Fan-in: to derive. **The
    producer declares a class that covers this structure without naming it.** *(Owed at file 14.)*
  - **← ventral tegmental area** (`13_neuromodulatory_systems`) — **prediction error**; payload
    otherwise owed. Fan-in: to derive. **The producer declares no such edge.** Its Outputs field
    declares five: the nucleus accumbens, the striatum's dopamine-modulated
    projection neurons, prefrontal cortex, the amygdala and the hippocampus. **This structure is not
    among them under any name.** **Consumer-only, and the count is exact rather than a matter of an
    unread far end.** *(Owed at the source: declare it there, or withdraw the limb here.)*
    **The asymmetry with the return limb below is the finding.** This structure's projection *to* that
    one is declared at both ends and typed at both; the projection *from* it is declared here alone.
    **So one arm of the ventral-pallidum / ventral-tegmental-area / accumbens motivational loop is
    two-ended and the other has one end**, and the loop cannot be traced without the missing half.
  - **← lateral parabrachial nucleus** — payload owed. Fan-in: to derive. **The producer names a
    basal-forebrain class that may or may not include this structure**, since this entry's own heading
    places it in the basal forebrain. *(Owed at file 14: say whether the substantia innominata target
    includes this structure.)*
    - **← subthalamic nucleus** — payload owed. Fan-in: to derive. **The producer is a sub-element of
    the other entry in this file and declares it.**

  *(The first four are separate lines rather than one: a single line naming **eight** sources and
  carrying one payload — "valence, context, need state, and prediction error" — across all of them
  assigns **the four payload terms one each to four of the eight**, which is why such a line reads as
  complete and is not. Four of the eight are assigned nothing at all.)*

- **Outputs.** Almost exclusively **inhibitory (GABAergic)**.
  - **→ mediodorsal thalamus** (onward to prefrontal cortex) — **released inhibition, closing the
    limbic loop; and, on the same cells, a computed relative-value signal.** **Value is computed here,
    not merely passed.** Fan-out: to derive. **The consumer declares a separate limbic limb
    reaching it via this structure** (`12_thalamus`), beside its dorsal basal-ganglia line rather
    than inside it — **and this is where the boundary question reached the wire**, because the two
    sources carry different payloads: tonic inhibition alone from the dorsal nuclei, inhibition plus
    a computed relative value from here. **The two are distinguished at that end now.**
    **The third file on the route agrees.** `11_frontal_lobe`'s orbitofrontal / ventromedial entry
    declares `← the basal ganglia, via the ventral pallidum → mediodorsal thalamus limb of the limbic
    loop`, naming this structure as the origin. **So all three stages of the route now name the same
    source**, where the middle stage once contradicted its two ends. **What remains is the boundary
    question above rather than a per-edge repair**: the limb is attributed to this structure at three
    rungs, and whether this structure is a peer of the dorsal entry or a sub-element set of it is
    still undecided.
  - **→ ventral tegmental area** (`13_neuromodulatory_systems`) — disinhibition of dopamine; the
    ventral-pallidum → ventral-tegmental-area → accumbens motivational limb. Fan-out: to derive.
    **Two-ended, and the far end is the more specific of the two.** That entry
    declares `← ventral pallidum`, types it in this line's own words as disinhibition of the dopamine
    cells, names the same three-stage motivational limb, **and states the termination this end does
    not: it lands on the structure's local GABAergic population**, which is what makes the
    disinhibition mechanical rather than nominal. **That population is a named sub-element there and
    the internal inhibitory edge from it onto the dopamine cells is described but not typed.**
    **Owed here: take the sub-element target into this line**, since the payload word *disinhibition*
    is only checkable against it.
    - **→ lateral habenula** — payload owed. Fan-out: to derive. **Two-ended:** the consumer declares
    this structure on its own line beside the dorsal pallidal source, with the payload owed at both
    ends. *(File 17. Same shape as the mediodorsal edge above, and resolved the same way.)*
    - **→ subthalamic nucleus** and **→ nucleus accumbens** (back) — the limbic-motor interface signal;
    payload otherwise owed. Fan-out: to derive. **Both are sub-elements of the other entry in this
    file, and both limbs are declared there.**
  - **A return edge from the accumbens is asserted at `13_neuromodulatory_systems` and is written at
    neither end here.** That file's ventral tegmental entry declares `← nucleus accumbens / ventral
    striatum` and records that this file was not confirmed to declare it. **It does not: the
    accumbens is a sub-element of the other entry in this file, whose every output leaves from the
    internal globus pallidus or the pars reticulata**, and no line anywhere here sends the accumbens to
    the midbrain. **Consumer-only at that file.** The absence is no longer structural: **the other
    entry's Outputs slot
    now carries an accumbens-sourced edge** — `→ the ventral pallidum, from the nucleus accumbens` —
    so a midbrain limb from the accumbens has somewhere to be written and is simply not written.
    **Owed at the source.**
  - **→ reticular and extrapyramidal motor systems** — payload owed. **A class endpoint that does not
    resolve**: the reticular formation entry declares no input from this structure, and
    "extrapyramidal motor systems" names no region at all. **Owed: name the targets, or withdraw. Not
    written as an edge here.**

- **Sizing.** Basis: would be **per hemisphere**. **Neurons: to derive** — soft and unrecorded, no
  clean human count. **Parameter memory: to derive.** Synapses unknown. Axons: the **ansa
  lenticularis** and the ventral-pallidal efferents, counts unknown. **Grey-matter volume: small,
  sub-cm³, no verified human figure**, so **no density cross-check can be run and this structure has
  no independent arithmetic available at all** — the same state the bed nucleus of the stria
  terminalis is in.

- **Shape.** **Non-laminated nucleus, rank 2: (cell class, N)** — **and no axis has an extent.** The
  cell-class axis is *unknown* rather than owed: it is not established that separable populations
  exist. The divisional axis has one member named — the posterior pole — with no boundary and no
  count. N is to derive.

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: satisfied for the loop with the ventral tegmental area
  and the accumbens as described, though **the accumbens limbs are written at one end only in both
  directions**. **Internally unstatable** — no internal edge is described, so there is nothing to
  co-instantiate below the structure level, and the hotspot's separate outputs are asserted and
  unassigned. Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** The reason this structure is not a relay is a **timing** claim
  stated without a time: it codes relative value **faster and more robustly** than the accumbens that
  feeds it. **A downstream stage that represents something sooner than its own input is doing work,
  not passing it** — that is the argument, and it is the entry's whole basis for existing separately
  from the accumbens. **It is also the only latency claim in this section**, and like the hyperdirect
  race it has no number. Two comparative timing claims carry two structures' functions in this file
  and neither is measured.

---

## Section totals

**The basis is mixed and the total is not one number.**

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Basal ganglia (six nuclei, bundled) | **whole — both hemispheres** | >200M | ≤ 16 | ≤ 400 MB |
| — the same, per side | per hemisphere | >100M | ≤ 16 | ≤ 200 MB |
| Ventral pallidum | per hemisphere | to derive | ≤ 16 | to derive |
| **stated total** | **mixed** | **>200M whole, plus one uncounted structure** | | **≤ 400 MB whole, plus to derive** |

**A floor and a ceiling at once, in different respects.** It is a **ceiling** on the counted part,
because fan-in is absent everywhere and 16 bits is the log₂ cap rather than a measured width. It is a
**floor** on the section, because one of two structures has no count and four of the six sub-elements
in the other have no count either.

**Two of the six sub-elements carry the only real numbers in the section** — the subthalamic nucleus
at ~560,000 per side and the pars compacta at ~400,000–500,000 per side — and **neither is on an
output edge of this entry.** Every output leaves from a sub-element whose count is an order of
magnitude.

**State memory and edge storage are not in this table**, and edge storage cannot be sized until the
scheduling discipline is set, which it is not.

**Memory is not a binding constraint here and the figure is not to be reduced.** It is a derived
requirement recorded as found.
