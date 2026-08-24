# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-22
---

---

# FILE 9 OF 20 — BASAL GANGLIA

**What is in this file.** The basal ganglia as a single entry, with the ventral pallidum separated out. Action selection and value.

**Size:** 437 lines, ~9.5k tokens (estimated from bytes, not tokenised). **Entries:** 2. **Edge lines:** 30 — 17 in, 13 out.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Basal ganglia — the action-selection / value loop (striatum, pallidum, subthalamic nucleus, substantia nigra)**
- **Ventral pallidum — limbic basal-ganglia output / hedonic hotspot (basal forebrain)**

**Which cross-file claims here are checked, and which are not.** Claims made about files 5 (sensorimotor loop), 6 (posterior parietal), 7 (anterior temporal lobe), 8 (medial temporal lobe), 11 (frontal lobe), 12 (thalamus), 13 (neuromodulatory systems), 14 (brainstem / midbrain / hypothalamus), 17 (insula / claustrum / habenula / cingulate remainder) and 18 (white-matter tracts) are checked against those files. **Claims about files 1 (visual pathway), 2 (auditory), 3 (other senses), 4 (dorsal visual / parietal stream), 10 (cerebellum), 15, 16, 19 and 20 are unchecked.**

---

# BASAL GANGLIA

## Basal ganglia — the action-selection / value loop (striatum, pallidum, subthalamic nucleus, substantia nigra)

- **Function:** action selection and gating, plus reinforcement learning driven by a dopaminergic
  reward-prediction-error signal. Desired actions are selected and competing ones suppressed through
  three canonical pathways, now written as internal edges under Internal structure rather than as
  prose here. Dopamine from the **substantia nigra pars compacta** sets the balance between the two
  striatal cell classes and carries the reward-prediction error (Schultz) that trains the loop — the
  brain's value / reinforcement system.
- **Inputs:**
  - **← nearly all of cortex** (glutamatergic, topographically mapped onto the striatum — motor,
    associative and limbic sectors, the limbic sector being the ventral striatum / nucleus
    accumbens) — **carries:** the **candidate actions** — every action currently proposed by every
    cortical area, in parallel. The payload is a *set of competitors*, not a decision. **Fan-in:**
    unknown.
    **This endpoint is a class, and whether it is a defect is an open question, asked and not yet
    answered.** §3 requires a named region with an entry of its own. Splitting this line would
    produce dozens of edges asserting the same payload, and the claim the line makes — that this is
    a convergence of *nearly all* cortex — is not obviously expressible as a list. **Not resolved
    here, and nothing is built on a guess at it.**
    **The class is not covered from the other side.** Of the cortical entries in the nine
    files checked against this one, **five declare an output to this structure**: premotor cortex ("the basal-ganglia motor loop"), dorsolateral prefrontal cortex
    ("basal-ganglia associative loop") and ventrolateral prefrontal cortex ("basal-ganglia loop") in
    file 11; the midcingulate cortex ("basal-ganglia and brainstem autonomic targets") and the
    insula ("→ Basal ganglia, to the ventral striatum") in file 17. **All six entries of the
    sensorimotor-loop file declare none — including the primary motor cortex**, whose
    Outputs name the muscles, the
    ventral anterior / ventral lateral thalamus, the dorsal column nuclei, and the return through
    the body. **So the motor sector of this input has no producer end at the one region the motor
    sector is named for.** That is a finding independent of how the class question is settled:
    however the line is written, the corticostriatal edge from the primary motor cortex is missing
    at its source. **Owed as a cross-file edit at the primary motor cortex entry (file 5).**
  - **← the intralaminar nuclei of the thalamus** (centromedian and parafascicular) — **carries:**
    arousal and a thalamostriatal drive parallel to cortex. **Payload otherwise unknown — owed.**
    **Fan-in:** unknown. **The producer declares it and names this structure**, at the
    sector level: the **centromedian nucleus** reaches the **motor striatum** and the
    **parafascicular nucleus** the **associative and limbic striatum** (file 12), where each is
    written as its own edge. **This end carries the sector split now and its two ends agree**; the
    striatal sectors themselves remain unwritten as sub-elements here, which is recorded under
    Internal structure.
  - **← the amygdala**, onto the **ventral striatum** — **carries:** the **valence tag** — a gain on
    perception, attention and memory encoding, carrying no identity information of its own.
    **Fan-in:** unknown. **Declared at the producer's end too**: the amygdala entry (file 8)
    declares this output and records that this entry's cortical class does not cover it, since the
    amygdala is not cortex. *(Transcribed from the amygdala entry, file 8. Candidate — awaiting
    Micky's verification.)*
  - **← the insula**, onto the **ventral striatum** — **carries:** payload **unknown — owed** at both
    ends. **Fan-in:** unknown. **The producer declares it and names this structure** (file 17).
  - **← the orbitofrontal and ventromedial prefrontal cortex**, onto the **ventral striatum** —
    **carries:** value — the expected value of the options, in the producer's terms; **payload
    otherwise owed**, and untyped at that end. **Fan-in:** unknown. **The producer declares it and
    names this structure** — "amygdala, hypothalamus, ventral striatum (value → action), autonomic
    centers" (file 11). *(This edge is arguably inside the
    cortical class above; it is written separately because the producer names the ventral striatum
    specifically, which the class does not.)*
  - **← the ventral tegmental area**, onto the **nucleus accumbens / ventral striatum** (the
    mesolimbic projection) — **carries:** payload **owed**; dopamine carrying
    reward-prediction-error signals alongside the substantia nigra pars compacta, in the producer's
    terms. **Fan-in:** unknown. **The producer declares it and names this structure** (file 13).
    **The two dopamine systems split by loop** — pars compacta to the motor loop, ventral tegmental
    area to the reward / limbic loop — **and only one of them is inside this entry**, the pars
    compacta.
  - **← the lateral habenula**, via the **rostromedial tegmental nucleus**, onto the **substantia
    nigra pars compacta** — **carries:** a **negative reward-prediction error** — the mirror image
    of the dopamine signal, delivered as inhibition of the dopamine cells. **Fan-in:** unknown.
    **Declared at the producer's end too**: the habenula entry (file 17) describes this as the
    negative-value brake and names the pars compacta as a target.
    **The intermediate stage has an entry.** The **rostromedial tegmental nucleus** — described at
    the habenula entry as the gamma-aminobutyric-acid-releasing (GABAergic) "tail of the ventral
    tegmental area" through which the suppression is delivered — **holds a full entry in file 14**,
    typed there as the GABAergic relay that inverts the habenula's glutamatergic bad-outcome signal
    into inhibition of the dopamine cells. **What this line still does not do is connect to it**: the
    relay is named inside the endpoint rather than written as two edges. **Owed: split it, or record
    that a named intermediate holding its own entry may stand inside an endpoint.** *(Checked against file 14. Candidate — awaiting Micky's verification.)*
  - **← the ventral pallidum**, onto the **nucleus accumbens / ventral striatum** — **carries:**
    payload **owed** at both ends. **Fan-in:** unknown. **The producer is in this file and declares
    it** as the return limb of its own output line. **Written here from that declaration**, which
    the other entry records as owed at this one.
  - **← the ventral pallidum**, onto the **subthalamic nucleus** — **carries:** the limbic-motor
    interface signal; **payload otherwise unknown — owed. Fan-in:** unknown. **The producer is in
    this file and declares it**.
- **Outputs:**
  - **→ the ventral anterior / ventral lateral thalamus → frontal and motor cortex**, from the
    **internal globus pallidus** and the **substantia nigra pars reticulata** — **carries:** **tonic
    inhibition, selectively released.** The payload is a *negative*: the output nuclei fire
    constantly and the selected action is the one whose inhibition **pauses**. Nothing here carries
    the action itself — the action lives in cortex, and this line only says *which one is allowed to
    proceed*. A consumer that expects a positive command on this edge has misread the structure.
    **Fan-out:** unknown. **The consumer declares it and names both source nuclei** (file 12),
    untyped there. **Owed at file 12: type it.**
  - **→ the mediodorsal thalamus**, from the **internal globus pallidus** and the **substantia nigra
    pars reticulata** (the associative and limbic output) — **carries:** the same tonic inhibition,
    selectively released — here a gate on which prefrontal loops may proceed. **Fan-out:** unknown.
    **Declared at the consumer's end too**: that entry's Inputs (file 12) read "← basal ganglia
    (GPi [internal globus pallidus] / SNr [substantia nigra pars reticulata] — associative and
    limbic output) — carries: tonic inhibition, selectively released … (the same negative payload
    the basal-ganglia output carries at all its thalamic targets)." The consumer's parenthesis is
    the reason it can be typed rather than left owed.
  - **→ the superior colliculus**, from the **substantia nigra pars reticulata** — **carries:** the
    same tonic inhibition, released to permit a saccade — the gate on the lateral intraparietal
    area's priority map. **Fan-out:** unknown. **The consumer declares it and names the source
    nucleus** (file 14), where the payload is typed in the same terms: "the saccade is not commanded
    by this edge; it is **permitted** by a pause in the tonic firing arriving on it … its
    informative event is a *cessation*." Two-ended and agreeing.
  - **→ the lateral habenula**, from the **internal globus pallidus** — **carries:** the
    basal-ganglia **"no-reward" signal**, in the consumer's terms. **Payload otherwise unknown —
    owed. Fan-out:** unknown. **Declared at the consumer's end too**: the habenula entry (file 17) names the internal globus
    pallidus as a principal source of the lateral habenula's negative-value input, noting the rodent
    homologue is the entopeduncular nucleus.
    **This edge closes a loop.** The internal globus pallidus sends a no-reward signal to the lateral
    habenula, which brakes the dopamine cells of the pars compacta, which set the striatal balance
    that determines what the internal globus pallidus releases. **The whole loop is inside this entry
    except for the habenula in file 17 and the rostromedial tegmental nucleus in file 14**, and every
    stage of it has an entry.
  - **→ the ventral pallidum**, from the **nucleus accumbens / ventral striatum** (GABAergic,
    substance-P) — **carries:** the limbic loop's selection — which motivated action has been
    chosen. **Fan-out:** unknown. **The consumer is in this file and declares it**, and records that
    this end did not. **This is the ventral loop's equivalent of the direct pathway** and the reason
    the ventral pallidum holds an entry of its own.
  - **→ the ventral pallidum**, from the **subthalamic nucleus** — **carries:** payload **owed** at
    both ends. **Fan-out:** unknown. **The consumer is in this file and declares it.**
  - **→ the thalamic reticular nucleus**, from the **internal globus pallidus** and the **substantia
    nigra pars reticulata** — **carries:** GABAergic inhibition; **payload owed. Fan-out:** unknown.
    **Declared at the consumer's end too**: that entry's Inputs (file 12) name "the internal globus
    pallidus, substantia nigra pars reticulata, and zona incerta" as extrathalamic GABAergic
    sources, and record that **whether they terminate on that nucleus or directly on the relay
    nuclei is not distinguished and is owed** there. The same ambiguity is carried at this end: if
    they terminate on the relay nuclei directly, this edge and the two thalamic edges above are the
    same projection described twice.
  - **→ the brainstem** — **payload unknown — owed. Fan-out:** unknown. **This endpoint is a class
    and does not resolve.** No entry in the brainstem file declares an input from this structure as
    a class. **One brainstem entry does declare a named one, and it is not written here**: the
    rostromedial tegmental nucleus (file 14) declares "← the substantia nigra," a lesser input with
    the payload owed, and marks its far end as owed at this file. **Owed here: write the substantia
    nigra → rostromedial tegmental nucleus edge, and name the target of this line or withdraw it.**
- **Internal structure and internal data flow:**

  **Divisional sub-elements: six named nuclei, and the entry is a lump of six regions under one
  heading** — the **striatum** (caudate nucleus, putamen, and the **nucleus accumbens / ventral
  striatum**), the **external globus pallidus**, the **internal globus pallidus**, the
  **subthalamic nucleus**, the **substantia nigra pars compacta**, and the **substantia nigra pars
  reticulata**. Taken from this entry's own heading and Function field.
  **Whether these should be six entries rather than six sub-elements is a real question and is not
  settled here.** The file already treats the **ventral pallidum** — which is the ventral
  counterpart of the internal globus pallidus and pars reticulata — as its own entry, so the
  boundary between "sub-element of the basal ganglia" and "entry in its own right" is currently
  drawn in one place for the dorsal loop and another for the ventral one. **Recorded as an
  inconsistency in the file, not resolved.**

  **Cell-class sub-elements inside the striatum: two, and they are sub-elements rather than
  properties** — **D1-expressing medium spiny neurons** and **D2-expressing medium spiny neurons**.
  On the floor-of-the-hierarchy rule the test is the data flow, and it is met exactly: the two
  classes **project to different targets** — D1 to the internal globus pallidus and pars reticulata,
  D2 to the external globus pallidus — and carry the two competing pathways. Medium spiny neurons
  are **85–95%** of the striatal population, D1 and D2 roughly equal. *(Class 3 — general
  basal-ganglia anatomy, as stated in this entry's Function and Neurons slots.)*

  **Laminar sub-elements: not applicable.** Subcortical nuclei, not cortex.

  **Tangential sub-elements: owed.** The Function field asserts that the cortical input is
  **topographically mapped** onto the striatum in motor, associative and limbic sectors, which is a
  tangential organisation an edge could terminate on — and the intralaminar input's producer already
  addresses two of those sectors separately. **The sectors are named and their boundaries and
  internal edges are not written.** The striosome / matrix compartmentation is not recorded here at
  all.

  **Internal edges — the three canonical pathways:**
  - **the direct pathway: D1 medium spiny neurons → the internal globus pallidus and the substantia
    nigra pars reticulata** — **carries:** inhibition of the output nuclei, which **disinhibits** the
    thalamus and so **facilitates** the selected action. **Fan-in / fan-out:** unknown.
  - **the indirect pathway: D2 medium spiny neurons → the external globus pallidus → the subthalamic
    nucleus → the internal globus pallidus and pars reticulata** — **carries:** across three
    internal edges, a net **excitation** of the output nuclei, which **inhibits** the thalamus and so
    **suppresses** competing actions. **Fan-in / fan-out:** unknown. **Written as three edges
    because it is three transfers**, and the sign alternates across them; a single line naming the
    pathway hides that the net sign is a product rather than a property.
  - **the hyperdirect pathway: cortex → the subthalamic nucleus → the internal globus pallidus and
    pars reticulata** — **carries:** a fast global **stop**. **Fan-in / fan-out:** unknown. **Only
    the second half of this is an internal edge**; the first half is an inter-region edge from
    cortex that this entry's Inputs slot does **not** declare — the cortical input line above says
    the projection is "topographically mapped onto the striatum," and the hyperdirect pathway
    bypasses the striatum entirely. **Owed: write the cortex → subthalamic nucleus edge in Inputs,
    since the class as worded excludes it.**
  - **the nigrostriatal edge: the substantia nigra pars compacta → the striatum**, onto both cell
    classes — **carries:** the **reward-prediction error** — a scalar, broadcast: *the outcome was
    better or worse than expected, by this much*. One number, no content, no address — which is
    exactly why it can train the whole array at once, and exactly why it cannot say **what** to do.
    **Fan-in / fan-out:** unknown. **This is not an input edge**: the pars compacta is inside this
    entry, so the edge does not cross a region boundary.
    **Its opposite signs on the two cell classes are the mechanism the Function field refers to as
    setting the balance, and they are owed** — the same scalar reaching two targets with different
    effects is a payload statement this file does not currently make.

  **What is selected, and where, is not written.** Candidate actions arrive in parallel; tonic
  inhibition leaves, selectively released. **The competition that reduces the set to one has no edge
  here** — the lateral interactions within the striatum, and the subthalamic nucleus's role in the
  global stop, are the obvious substrates and neither is typed. This is the **seventh** entry in the
  source where the stated function has no declared internal substrate, after the anterior and medial
  intraparietal areas, the angular gyrus, the temporal pole, the anterior insula and the amygdala.
  *(Class 3 for the pathway anatomy, which is textbook and was already in this entry's Function.
  **Class 2** — the observation that the selection step itself is unlocated is Claude's, offered to
  be checked.)*
- **Neurons:** the basal-ganglia nuclei together hold **>200M neurons** (both hemispheres; human
  putamen-morphometry lineage), the large majority in the **striatum** (caudate plus putamen), where
  **medium spiny neurons are 85–95%** of the population (D1 direct versus D2 indirect, roughly
  equal). **Substantia nigra pars compacta dopaminergic neurons ≈ 400,000–500,000 per side**
  (~0.9–1.0M bilateral; verified — the population lost in Parkinson's disease). The relay and output
  nuclei are far smaller: the **subthalamic nucleus ~560,000 neurons** (human — the standard figure,
  on the cross-species ladder ~5,400 mouse / ~25,000 rat / ~155,000 macaque / ~560,000 human, ~3.6×
  the macaque; predominantly glutamatergic), with the external and internal globus pallidus and the
  pars reticulata each of the same order (hundreds of thousands), from the Hardman et al. 2002 human
  stereology series.
  **The convergence across the internal edges is extreme and the fan slots do not record it.**
  Something over 200M striatal cells (both sides) reduce onto output nuclei of order 10⁵ per side.
  **That ratio is the selection**, in the sense that it is the arithmetic the competition has to
  perform, and every fan-in and fan-out slot in this entry reads unknown.
- **Synapses:** unknown. **Axons:** the loop tracts (ansa lenticularis, lenticular fasciculus,
  nigrostriatal bundle); counts unknown. **None of the three has an entry in the white-matter-tracts
  file**, whose four entries are the corpus callosum, the internal capsule, the fornix and the
  arcuate / superior longitudinal fasciculus; its preamble records the tracts already described
  where a pathway needed them and these are not among them. **Unchecked rather than missing** — whether these
  three warrant entries is a decision, not a finding.
- **Grey-matter volume:** striatum ~10 cm³ (the largest subcortical grey structure; ~5 cm³ per
  hemisphere, soft). Rough density cross-check: >200M / ~10 cm³ ≈ ~20,000 neurons/mm³ — ordinary
  grey-matter packing. The pallidum, subthalamic nucleus and substantia nigra are much smaller;
  per-nucleus volumes soft.
- **White-matter volume:** unknown. **Myelination:** unknown.

## Ventral pallidum — limbic basal-ganglia output / hedonic hotspot (basal forebrain)

- **Function:** the **output stage of the limbic (ventral) basal-ganglia loop** — the ventral
  counterpart of the internal globus pallidus and substantia nigra pars reticulata the main entry
  names, and the chief target of the **nucleus accumbens / ventral striatum**. It is the "limbic
  final common pathway" (Mogenson) by which motivational value is translated toward action. But it
  is **not a passive relay**: its neurons **code the relative value of reward outcomes faster and
  more robustly than the upstream accumbens**, carrying reward-prediction-like signals — a value hub
  in its own right. Its **posterior pole holds an opioid "hedonic hotspot"** where μ-opioid
  stimulation amplifies the *"liking"* reaction to reward, while GABAergic disinhibition drives
  *"wanting"* (incentive salience) — the liking / wanting dissociation (Smith, Tindell, Aldridge &
  Berridge 2009; Berridge). Central to natural reward, motivation and addiction.
- **Inputs:**
  - **← the nucleus accumbens / ventral striatum** (GABAergic, substance-P — the dominant input) —
    **carries:** the limbic loop's selection — which motivated action has been chosen. **Fan-in:**
    unknown. **The producer is a sub-element of the other entry in this file and declares
    it**, as the ventral loop's equivalent of the direct pathway and the reason this entry exists.
  - **← the amygdala** — **carries:** valence — the **valence tag**, per the producer's declaration.
    **Payload otherwise unknown — owed. Fan-in:** unknown. **The producer declares it and names this
    structure** (file 8). *(Separate lines rather than one: a single line naming
    the amygdala, hippocampal formation, orbital and medial prefrontal cortex, lateral hypothalamus,
    ventral tegmental area, parabrachial nucleus and subthalamic nucleus together carries one
    payload — "valence, context, need state, and prediction error" — across **eight** sources, and
    **the four payload terms belong one each to four of them**. Such a line reads as complete and is
    not: the reader cannot tell which source supplies which term, and four of the eight are assigned
    nothing at all.)*
  - **← the hippocampal formation**, from the **subiculum** — **carries:** episodic **context**.
    **Payload otherwise unknown — owed. Fan-in:** unknown. **The producer declares it and names this
    structure** (file 8).
  - **← the orbital and medial prefrontal cortex, including infralimbic cortex** — **carries:**
    value — the expected value of the options. **Payload otherwise unknown — owed. Fan-in:**
    unknown. **The producer declares it and names this structure**
    (file 11), typed there as **value** with the remainder owed, so the two ends agree on the one
    term and mark the rest owed in the same place. Infralimbic cortex is area 25, which that entry
    covers as a sub-element without naming it as one, and that entry records the same.
  - **← the lateral hypothalamus** — **carries:** **need state. Payload otherwise unknown — owed.**
    **Fan-in:** unknown. **The producer declares no such edge.** The hypothalamus entry's Outputs
    (file 14) name the pituitary, autonomic preganglionic centres via the periaqueductal gray,
    brainstem and spinal cord, the mammillary bodies and anterior thalamus, and "widespread limbic /
    cortical projections shaping motivated behaviour" — **a class that covers this structure without
    naming it**. **Owed as a cross-file edit at that entry (file 14).**
  - **← the ventral tegmental area** (dopamine) — **carries:** **prediction error. Payload otherwise
    unknown — owed. Fan-in:** unknown. **The producer declares no such edge.** That entry's Outputs
    (file 13) name the nucleus accumbens / ventral striatum, prefrontal cortex, the amygdala and the
    hippocampus — **not this structure**. **Owed as a cross-file edit at that entry (file 13), or
    withdraw the limb.**
  - **← the lateral parabrachial nucleus** — **carries:** payload **owed. Fan-in:** unknown. **The
    producer declares no such edge.** That entry's Outputs (file 14) name the amygdala, the bed
    nucleus of the stria terminalis, the hypothalamus, the intralaminar and ventroposterior
    parvicellular thalamus, the insula and infralimbic cortex, and the basal forebrain / nucleus
    basalis — **the last of which is a basal-forebrain class that may or may not include this
    structure**, since this entry's own heading places it in the basal forebrain. **Owed as a
    cross-file edit at that entry (file 14): say whether the substantia innominata target includes
    this structure.**
  - **← the subthalamic nucleus** — **carries:** payload **owed. Fan-in:** unknown. **The producer is
    a sub-element of the other entry in this file and declares it.**
- **Outputs:** almost exclusively **inhibitory (GABAergic)**:
  - **→ the mediodorsal thalamus → prefrontal cortex** — **carries:** released inhibition, closing
    the limbic loop; and, on the same cells, a **relative-value signal** — this structure codes the
    value of reward outcomes faster and more robustly than the accumbens upstream, so this is **not**
    a pure relay: value is computed here, not merely passed. **Fan-out:** unknown. **The consumer declares a separate limbic limb
    reaching it via this structure** (file 12), beside the dorsal basal-ganglia line rather than
    inside it. **The two sources are now distinguished at that end, which matters because they carry
    different payloads**: tonic inhibition alone from the dorsal nuclei, inhibition **plus a computed
    relative value** from here. **The frontal-lobe file names the same limb from the far side**, as
    "← the basal ganglia, via the ventral pallidum → mediodorsal thalamus limb of the limbic loop."
  - **→ the ventral tegmental area** — **carries:** disinhibition of dopamine — the
    ventral-pallidum → ventral-tegmental-area → accumbens motivational limb. **Fan-out:** unknown.
    **The consumer declares it and names this structure** (file 13), typed there as the same
    disinhibition of dopamine, so the motivational limb is written at both ends.
  - **→ the lateral habenula** — **carries:** payload **owed. Fan-out:** unknown. **The consumer declares it and names this
    structure** (file 17), on its own line beside the dorsal pallidal source rather than folded into
    it, with the payload owed at both ends. **The dorsal and limbic limbs are now separate edges at
    that end.** *(Separate lines rather than one: a single line "→ subthalamic nucleus, reticular /
    extrapyramidal motor systems, lateral habenula, and back to the accumbens" names four targets
    and types none of them.)*
  - **→ the subthalamic nucleus** and **→ the nucleus accumbens** (back) — **carries:** the
    limbic-motor interface signal; **payload otherwise unknown — owed. Fan-out:** unknown. **Both
    are sub-elements of the other entry in this file, and both limbs are written there.**
  - **→ reticular and extrapyramidal motor systems** — **payload unknown — owed. Fan-out:** unknown.
    **This endpoint is a class and does not resolve.** The reticular formation entry (file 14)
    declares no input from this structure; "extrapyramidal motor systems" names
    no region at all. **Owed: name the targets, or withdraw.**
- **Internal structure and internal data flow:**

  **Divisional sub-elements: one is named by the entry's own Function and it is spatial** — the
  **posterior pole**, which holds the opioid **hedonic hotspot**. The rest of the structure is
  undivided here. **Owed: whether the anterior / posterior division is a boundary or a gradient**,
  and what the remainder should be called.

  **The hotspot is a sub-element by the data-flow test, not merely a region of interest.** The
  Function field assigns it a payload the rest of the structure does not carry: μ-opioid stimulation
  there amplifies the **"liking"** reaction, while GABAergic disinhibition drives **"wanting"** —
  two dissociable outputs. **On the floor-of-the-hierarchy rule that makes them sub-element-level
  claims**, and every output edge above is written as leaving the structure as a whole. **Owed:
  establish which outputs leave the hotspot.**

  **And the liking / wanting pair is a payload claim the Outputs slot does not carry.** Neither word
  appears on any edge above. If the dissociation is real on the wire then two different payloads
  leave this structure, and the file currently declares one — "released inhibition, plus a
  relative-value signal." **Owed: type liking and wanting, or record that they are behavioural
  categories rather than payloads.** They are the entry's most distinctive claim and the completion
  test does not pass on either: *liking* and *wanting* are phrases, not types with a range and a
  frame.

  **Laminar sub-elements: not applicable.** A basal-forebrain nucleus without cortical lamination,
  as the Neurons slot already records.

  **Cell-class sub-elements: unknown.** The Function field names GABAergic disinhibition and
  μ-opioid receptors without saying whether these belong to separable populations.

  **Internal edges: owed, all of them.** None is described, in either direction.
- **Neurons:** soft / unknown — no clean human count recorded here; a basal-forebrain structure
  without cortical lamination.
- **Synapses:** unknown. **Axons:** the ansa lenticularis and the ventral-pallidal efferents (counts
  unknown). **Grey-matter volume:** small (sub-cm³); no verified human figure recorded.
  **White-matter volume:** unknown. **Myelination:** unknown.

**A finding about this file's own boundary, recorded because it is not a finding about any one
entry.** The two entries here are **the same loop described at two scales**:
the first holds six nuclei as sub-elements under one heading, the second holds the ventral
counterpart of two of those six as an entry in its own right. The consequence was visible in the
edges — the mediodorsal thalamic output and the lateral habenular output were both attributed at
their far ends to the dorsal structure and claimed here by the ventral one. **Both far ends now
distinguish the two sources and name this structure on its own line**, so the two loops are told
apart at four rungs rather than conflated at one. **The boundary question itself is not settled by
that**: it is still drawn in one place for the dorsal loop and another for the ventral one. Owed: decide whether the ventral loop is a sub-element set of the first entry or a
peer of it, and make the far ends match.

---

---

## References

*(Every line below is a **candidate** awaiting Micky's verification; none is verified. Each full
reference given here was obtained against publisher or journal records — **no reference is written
from recall.** Keys reading **owed** have no reference yet. **No line here carries a line number**: a
pointer into the file goes stale on the next edit and fails silently, so the section is joined to the
entries by the key alone, and a claim with no key is named by what it asserts.)*

**6 distinct keys, 6 mentions. 2 searched; 4 owed.**

**This file is sparsely cited, and the sparseness is the finding.** Six keys across the whole file —
against 190 in file 02 and 50 in file 05 — and **four of the six are not usable as keys.** *Schultz*
(the reward-prediction error, in the main entry's Function), *Mogenson* (the limbic final common
pathway) and *Berridge* (liking versus wanting) are **bare surnames with no year**, each attached to
a named idea. *Human putamen-morphometry lineage* is not even a surname: it is a description of a
literature, and it supports the entry's largest number.

**Six numerical claims in this file carry no key at all.** Named by what they assert, because a
reference section can only list keys that exist and this is what its absence looks like:
**>200M basal-ganglia neurons**, keyed only to the lineage phrase above; **medium spiny neurons
85–95%, D1 and D2 roughly equal**, marked Class 3 by pointing back at this entry's own Function and
Neurons slots, which is circular; **substantia nigra pars compacta dopaminergic neurons
≈400,000–500,000 per side**, marked *verified*; the **subthalamic nucleus at ~560,000**, marked *the
standard figure*; the **cross-species ladder** ~5,400 mouse / ~25,000 rat / ~155,000 macaque /
~560,000 human; and **striatum ~10 cm³**. One key — *Hardman et al. 2002* — stands beside the last
three by sentence position and is attached to the pallidal and reticulata figures only.

**A candidate was checked against the sourceless 560,000 and does not support it.** Bokulić, E.,
Medenica, T., Knezović, V., Štajduhar, A., Almahariq, F., Baković, M., Judaš, M. & Sedmak, G.
(2021). The stereological analysis and spatial distribution of neurons in the human subthalamic
nucleus. *Frontiers in Neuroanatomy* 15: 749390; doi 10.3389/fnana.2021.749390; PubMed 34970124;
PMC8712451. **Human**, adult, Nissl and eight immunohistochemical markers with design-based
stereology. Its headline count is **281,308 ± 38,967 neurons**, and that figure is **the
nNOS-positive subpopulation, not the total** — the paper reports subpopulation densities of roughly
3,300 and 2,200 neurons/mm³ and does not state a total neuronal number for the structure. **So this
paper cannot stand behind the ~560,000**, and the number remains sourceless. Recorded here as a
**negative result.**

**Where the ~560,000 might come from instead, offered as a lead and not as a finding.** *Hardman et
al. 2002* — already a key of this file — is titled *volume and neuronal number for the **output,
internal relay**, and striatal modulating nuclei*, and the subthalamic nucleus is the basal ganglia's
internal relay nucleus. The file attaches that key by sentence position to the pallidal and
reticulata figures only. **Whether it also carries the subthalamic figure and the cross-species
ladder was not checked**; the paper's own scope is the reason to look there first.

- **Berridge** — **owed**.
- **Hardman et al. 2002** — Hardman, C.D., Henderson, J.M., Finkelstein, D.I., Horne, M.K., Paxinos, G. & Halliday, G.M. (2002). Comparison of the basal ganglia in rats, marmosets, macaques, baboons, and humans: volume and neuronal number for the output, internal relay, and striatal modulating nuclei. *Journal of Comparative Neurology* 445(3): 238–255. **Rat, marmoset, macaque, baboon and human** — comparative stereology. *(Located in several independent publisher reference listings — a secondary listing; the Wiley record itself was not opened.)* **The species list does not match the cross-species ladder this file gives**, which reads **mouse / rat / macaque / human** (~5,400 / ~25,000 / ~155,000 / ~560,000). Hardman et al. compare **rats, marmosets, macaques, baboons and humans** — **no mouse**, and two species the ladder omits. So either the ladder draws on a source this file does not name, or the mouse figure comes from somewhere else and has been folded in. **Which, is owed at the citing line.** The key is attached by sentence position to the pallidal and reticulata figures, not to the ladder, so the ladder may have no key at all. *(candidate.)*
- **human putamen-morphometry lineage** — **owed**.
- **Mogenson** — **owed**.
- **Schultz** — **owed**.
- **Smith, Tindell, Aldridge & Berridge 2009** — Smith, K.S., Tindell, A.J., Aldridge, J.W. & Berridge, K.C. (2009). Ventral pallidum roles in reward and motivation. *Behavioural Brain Research* 196(2): 155–167; doi 10.1016/j.bbr.2008.09.038. **Review; rodent (rat) throughout** — which the citing line does not say, in an entry whose other slots carry human figures. *(Elsevier record via the journal listing and the authors' own posted copy.)* **The dissociation is not quite the one the Function field states, and the difference bears on the payload question the entry itself raises.** The file writes it as opioid → *liking*, GABAergic disinhibition → *wanting*. This paper's own map is asymmetric: μ-opioid stimulation of the posterior hotspot enhances **both** liking and wanting, while blocking ventral-pallidal GABA raises **wanting** across virtually the whole structure and **leaves liking unchanged**. So the clean two-way split the entry describes is, on this source, a one-way one — GABA moves wanting only, opioid moves both. **That is directly relevant to the entry's own owed item under Internal structure** (“type liking and wanting, or record that they are behavioural categories”), because it says the two are not independently addressable by the two manipulations. *(candidate.)*
