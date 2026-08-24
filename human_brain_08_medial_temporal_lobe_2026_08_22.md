# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-22
---

---

# FILE 8 OF 20 — MEDIAL TEMPORAL LOBE

**What is in this file.** The medial temporal lobe: hippocampal formation, amygdala, and the bed nucleus of the stria terminalis — episodic memory and the threat/valence system.

**Size:** 922 lines, ~21.9k tokens / ~85 kB (estimated from bytes, not tokenised; kB = 1024 bytes, truncated). **Entries:** 3. **Edge lines:** 72 — 36 in, 36 out.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Hippocampal formation (medial temporal lobe, allocortex — three-layered)**
- **Amygdala (amygdaloid complex, medial temporal lobe — subcortical nuclei)**
- **Bed nucleus of the stria terminalis (extended amygdala, basal forebrain)**

**Files whose shared edges are diffed against this one:** `06_posterior_parietal`,
`07_anterior_temporal_lobe`, `09_basal_ganglia`, `11_frontal_lobe`, `12_thalamus`,
`13_neuromodulatory_systems`, `14_brainstem_midbrain_hypothalamus`,
`17_insula_claustrum_habenula`, `18_white_matter_tracts`. **Unchecked:**
`01_visual_pathway`, `02_auditory_pathway`, `03_other_senses`,
`04_dorsal_visual_parietal_stream`, `05_sensorimotor_loop`, `10_cerebellum`,
`15_cranial_nerve_nuclei`, `16_spinal_cord`, `19_cross_modal_integration`,
`20_loop_structure`.

***A cross-file mark records what this file can see of another file, and nothing more.*** *Two
files worked in separate sessions each read the other's state as it stood, so a debt recorded
here may already be discharged at the far end and neither file can see it. **A mark naming a
file unchecked against this one is unverified rather than outstanding** — the same caution
the cross-file check list at the architecture rung states, arriving here from the other
direction.*

---

# MEDIAL TEMPORAL LOBE

*Two systems that share a lobe and a set of afferents and do different things with them. The
**hippocampal formation** binds what is present into a retrievable episode; the **amygdala** and its
forebrain extension, the **bed nucleus of the stria terminalis**, assign significance to what is
present and act on it. They are reciprocally connected, and the direction of that connection is the
architecture: episodic **context** goes to the amygdala, and a valence **tag** comes back as a gain
on encoding.*

***A caution about this file's inputs.*** *Both major entries take their sensory afferents from
files unchecked against this one — `01_visual_pathway` and `02_auditory_pathway`.
Every edge below whose far end lies in one of those two is marked* **unchecked** *rather than
confirmed or refuted, and there are five of them. They are the largest block of* **unchecked** *edge
in this file — a far end unchecked, which is a different state from the* **candidate** *marks
elsewhere. **Three states are used in this file and they are not degrees of the same thing.***
***unchecked*** *— the far end of the edge is in a file unchecked against this one, so the edge's
agreement with its other end is unknown.* ***candidate*** *— no source has been opened for the
claim; the citation, where there is one, was written from recall and its key reads* **owed** *in the
reference section.* ***verified*** *— a source was opened or searched, and the line names which and
when. **The test is whether something was opened, not who read the result** (CLAUDE.md), so a line
does not become verified by being reviewed, and does not stay a candidate because it has not been.*

## Hippocampal formation (medial temporal lobe, allocortex — three-layered)

- **Function:** the trisynaptic memory circuit. **Entorhinal cortex** is the input/output port (all
  neocortical input in, all hippocampal output out; its layer II carries the grid representation).
  The **dentate gyrus** performs sparse pattern separation. **CA3** is the recurrent autoassociator
  — pattern completion and one-shot episodic binding, the brain's largest associational recurrent
  network. **CA1** is the comparator and main output; the **subiculum** is the principal output. A
  content-addressable episodic store, not a relay.
- **Inputs:**
  - **← inferotemporal cortex**, via entorhinal cortex and the perforant path — **carries:** object
    and scene identity, invariant to position, size, pose and lighting. **Fan-in:** unknown.
    **Far end in `01_visual_pathway`, unchecked.** *(Separate lines rather than one: the class endpoint "← neocortical association areas via entorhinal
    cortex / perforant path (including IT [inferotemporal cortex] for object and scene identity, and
    parietal)" names no region with an entry, and its parenthesis names two members of it.)*
  - **← the temporal pole**, onto entorhinal cortex — **carries:** an **amodal concept** — a
    representation of the thing that is no longer visual or auditory or tactile. **Payload unknown —
    owed** at the producer's end, where the modality-loss is recorded as the only checkable property
    in hand. **Fan-in:** unknown. **Declared at the producer's end as well as here**: the temporal pole entry's Outputs (`07_anterior_temporal_lobe`) declare "→ entorhinal cortex (toward the
    hippocampal formation)" and record that this entry's Inputs name the inferotemporal cortex
    instead and cover the temporal pole only under a class — marked there as an owed cross-file edit
    at this entry. **That owed edit is discharged.** *(Transcribed from the temporal
    pole entry, `07_anterior_temporal_lobe` — a derivation from another file in this source, not a literature check.
    **Candidate:** no source has been opened for this edge at either end.)*
  - **← the angular gyrus** — **carries:** payload **unknown — owed**, and the producer marks it the
    loudest owed payload in its own file: what the angular gyrus emits is described as concepts and
    events, which are not types. **Fan-in:** unknown. **Declared at the producer's end as well as here**: the angular gyrus entry's Outputs (`06_posterior_parietal`) name the hippocampal
    formation among four targets and record that this entry's Inputs cover it only under the class
    "parietal" — marked there as an owed cross-file edit at this entry.
    *(Transcribed from the angular gyrus entry, `06_posterior_parietal`. Candidate.)*
  - **← the precuneus** — **carries:** payload **unknown — owed. Fan-in:** unknown. **Declared at
    the producer's end only**: the precuneus entry's Outputs (`06_posterior_parietal`) name "medial prefrontal cortex
    and the medial temporal lobe" and mark the payload owed and the line as owing a split. *(Transcribed from the precuneus entry, `06_posterior_parietal`. Candidate.)*
  - **← the posterior cingulate cortex** — **carries:** payload **owed. Fan-in:** unknown. **The
    producer declares this edge**: the posterior cingulate entry's Outputs (`17_insula_claustrum_habenula`) name "the
    hippocampal system (memory)" and the medial temporal lobe among the default-mode partners,
    untyped there. **Owed at `17_insula_claustrum_habenula`: type it.**
  - **← the retrosplenial cortex**, via parahippocampal and entorhinal cortex — **carries:** payload
    **owed**; in the producer's terms the **return arm of the spatial-memory loop**, carrying
    heading and landmark information after the egocentric-to-allocentric translation that entry
    performs. **Fan-in:** unknown. **Declared at the producer's end as well as here**: the retrosplenial entry's Outputs (`17_insula_claustrum_habenula`) name this structure explicitly. *(Transcribed from the retrosplenial entry, `17_insula_claustrum_habenula`. Candidate.)*
  - **← perirhinal cortex** and **← parahippocampal cortex** — **carries:** payload **owed. Fan-in:**
    unknown. **Neither has an entry in any file checked against this one**, and both are named as producers by
    two other files: the temporal pole entry (`07_anterior_temporal_lobe`) declares an output to rostral perirhinal and
    posterior parahippocampal cortex, and quotes the inferotemporal entry (`01_visual_pathway`) declaring
    "→ perirhinal cortex (areas 35 and 36)" and naming it as the anatomical step by which the
    ventral stream reaches this structure. **So the source describes a route into this entry through
    two regions it does not describe.** **Owed: give perirhinal and parahippocampal cortex entries,
    and decide which file owns them.**
  - **← the medial septum, parvalbumin-expressing GABAergic pacemaker cells**, via the fornix
    (pre-commissural limb), terminating on **hippocampal inhibitory interneurons** in CA1, CA3 and
    the dentate gyrus — **carries:** the **theta timing reference** — the phase of a 4–12 Hz clock,
    not content. **The clock is not made by the transmitter.** Its tick is an **intrinsic membrane
    oscillation** in these cells, generated by the hyperpolarization-activated cyclic-nucleotide-
    gated (HCN) channel and its current I_h, whose gating kinetics set the frequency; the individual
    pacemakers frequency-lock to one rhythm by mutual inhibition (Huygens synchronization).
    Gamma-aminobutyric acid is the wire the phase is delivered on and the coupling that synchronizes the cells — it is **not**
    the origin of the rhythm. Delivering the timing onto the hippocampus's *own* interneurons is
    what paces principal-cell firing relative to theta phase. **Fan-in:** unknown. *(Class 1 —
    HCN/I_h intrinsic rhythmicity: PMC2538919, rat, combined anatomy + electrophysiology; Huygens
    frequency-synchronization of parvalbumin pacemakers: Cell Reports 2022, S2211-1247(22)00958-5,
    mouse/rat, optogenetic tagging; GABAergic septal targeting of hippocampal interneurons: Nature
    Communications 2023, s41467-023-41746-0. **Candidates:** all three keys read **owed** in the
    reference section — none has been searched, and all three were written from recall.)*
  - **← the medial septum, glutamatergic cells**, via the fornix — **carries:** a **tonic
    excitatory gate** — not a per-cycle signal and not content, but the depolarizing drive that
    determines whether the pacemakers oscillate at all; waxing and waning of this tonic excitation
    toggles the hippocampus between theta and non-theta states. **Fan-in:** unknown. *(Class 1 —
    Cell Reports 2022, S2211-1247(22)00958-5, mouse/rat, optogenetics. Candidate.)*
  - **← the medial septum, cholinergic cells** (the nucleus's namesake population), via the
    fornix — **carries:** a **tonic gain / arousal-state signal**, delivered largely by **volume
    transmission** (≈93% of cholinergic varicosities in the hippocampus form no classic synapse), not
    a timing reference. It biases hippocampal state and theta amplitude and gates the theta-vs-ripple
    regime — driving it during rest suppresses sharp-wave ripples — but **optogenetically activating
    it has little effect on theta frequency**, so it does not make the clock. **This is the
    "acetylcholine" the producer (`13_neuromodulatory_systems`) named**: real, but the slow chemical envelope on the
    rhythm rather than the rhythm itself. **Fan-in:** unknown. *(Class 1 — volume transmission and
    ripple suppression: J Neurosci 40:3591, 2020, mouse, optogenetics + long-term recording;
    little-effect-on-theta: consistent across the 2020/2022 optogenetic series. Candidate.)*
    *(Three lines rather than one: the septo-hippocampal projection is **three transmitter limbs with
    three different payloads**, and a single line naming either the pacing signal or the
    acetylcholine names one true limb and takes it for the whole — the shape a two-ended diff cannot
    catch, since each end can name a different true limb and neither disagrees with the other. The
    producer entry (`13_neuromodulatory_systems`) carries the reciprocal split as an owed edit: its
    single "→ hippocampus (medial septum) — acetylcholine" output must become these three. The
    finding is rodent throughout and is marked candidate.)*
  - **← the ventral tegmental area** — **carries:** payload **owed**; dopamine, in the producer's
    terms. **Fan-in:** unknown. **Declared at the producer's end as well as here**: that entry's Outputs (`13_neuromodulatory_systems`) name the hippocampus.
  - **← the locus coeruleus** — **carries:** payload **owed**; noradrenaline, setting global gain
    and signalling salience or surprise, in the producer's terms. **Fan-in:** unknown. **The producer
    declares its target as a class** — "brain-wide — the entire cortex, thalamus, hippocampus,
    cerebellum, and spinal cord" (`13_neuromodulatory_systems`) — which does name this structure inside the class.
  - **← the raphe nuclei** — **carries:** payload **owed. Fan-in:** unknown. **The producer declares
    its targets as a class** — "brain-wide (dorsal / median → cortex, striatum, limbic system)"
    (`13_neuromodulatory_systems`) — which covers this structure without naming it. **Owed as a cross-file edit at that
    entry (`13_neuromodulatory_systems`).**
  - **← the nucleus reuniens** (midline thalamus), terminating on **CA1** and the **subiculum** —
    **carries:** payload **owed**, and it is the **return arm of the prefrontal loop**: this is the
    stage through which medial prefrontal cortex reaches this structure, since it has no direct
    projection here. **Fan-in:** unknown. **Declared at the producer's end as well as here**: the
    nucleus reuniens has an entry of its own in `12_thalamus`, written from this file's four reuniens
    edges, and it declares this one. **The gap this line recorded — that the midline nuclei were
    named nowhere in the source and the string *reuniens* occurred in none of the twenty files — is
    closed, and all four of this file's reuniens edges are two-ended.** *(Class 1 — Joyce et al. 2022,
    rhesus macaque, bidirectional dextran-amine tracing with stereological termination density and
    electron microscopy: the macaque reuniens has bidirectional connections with the hippocampus,
    and hippocampal terminations there form multisynaptic complexes onto both excitatory projection
    neurons and the dendrites of local inhibitory neurons. The nucleus is **matrix-dominant** —
    calbindin and calretinin cells, which project to layers I–IIIa — with a sparse core-associated
    parvalbumin population, so its cortical arm is modulatory in form. **Verified against the Society
    for Neuroscience journal record, 2026-08-15; full text read.**)*
  - **← the amygdala**, from the basal and accessory basal nuclei — **carries:** the **valence tag**
    — a gain on perception, attention and memory encoding, carrying no identity information of its
    own. **This is the payload that makes emotional events better remembered**, and it is a
    modulator, not a content line. **Fan-in:** unknown. **The producer is in this file and declares
    it.** *(The two ends are copies of one declaration, so their agreement certifies nothing.)*
- **Outputs:**
  - **→ the fornix** — **carries:** the completed episode, in transit. **Fan-out:** unknown. **This
    endpoint is a tract, not a processing region**, and it has an entry of its own (`18_white_matter_tracts`) which
    describes it as the principal output and return-input pathway of this structure, splitting at
    the anterior commissure into a post-commissural limb to the mammillary bodies and anterior
    thalamus and a pre-commissural limb to the septum and basal forebrain. The tract entries compute
    nothing, so this edge is a routing statement rather than a transfer; **the regions it reaches are
    written as their own edges below.**
    **A third destination set belongs to this tract and the fornix entry does not
    carry it.** The two prefrontal edges below travel by the fornix and, on the evidence of the
    fornix-transection cases, **by no other route** — so the fornix is load-bearing for the direct
    hippocampal–prefrontal connection in a way that entry does not record. **Which limb carries them
    is owed**, not asserted: the study establishing the route did not divide it at the anterior
    commissure, and inferring the limb from the targets' position would be a reading dressed as
    anatomy. **Owed as a cross-file edit at the fornix entry (`18_white_matter_tracts`): add the prefrontal
    destinations, and give the limb if the literature divides it.**
  - **→ the mammillary bodies and the anterior thalamic nuclei**, via the post-commissural fornix
    (the Papez circuit) — **carries:** a **completed episode** — the bound, retrievable pattern,
    addressable by any fragment of itself. **Payload only partly writable — owed:** "an episode" has
    no units and no frame, and what makes it checkable is a property rather than a type — it is
    **content-addressable**, which the upstream identity codes are not. **Fan-out:** unknown. **The
    anterior-nuclei end declares it**: that entry's Inputs (`12_thalamus`) name "mammillary bodies
    (mammillothalamic tract), subiculum / fornix." The mammillary
    bodies are a sub-element of the hypothalamus entry (`14_brainstem_midbrain_hypothalamus`), which names them as the memory
    relay of the Papez circuit.
  - **→ the hypothalamus**, via the fornix — **carries:** payload **owed. Fan-out:** unknown. **The
    consumer declares it and names this structure**: the hypothalamus entry's Inputs (`14_brainstem_midbrain_hypothalamus`) read
    "limbic — amygdala, hippocampal formation (via the **fornix**), and septum," untyped there. **Owed at `14_brainstem_midbrain_hypothalamus`: type it.**
  - **→ the angular gyrus** and **→ the precuneus** — **carries:** the completed episode, same
    payload and same owed limit as above. **Fan-out:** unknown. **Both consumers declare it** (file
    6), the angular gyrus naming this structure directly and the precuneus naming the medial
    temporal lobe. *(Separate lines rather than one: the class endpoint "→ neocortex via subiculum / entorhinal
    cortex" names no region with an entry, and these lines name its members.)*
  - **→ the posterior cingulate cortex** and **→ the retrosplenial cortex** — **carries:** the same
    completed episode. **Fan-out:** unknown. **Both consumers declare it** (`17_insula_claustrum_habenula`), the posterior
    cingulate naming "medial temporal lobe / hippocampal formation" and the retrosplenial naming
    "hippocampal formation / subiculum," both untyped at their ends. **Owed at `17_insula_claustrum_habenula`: type them.**
  - **→ the orbitofrontal / ventromedial prefrontal cortex**, from the **subiculum** (with the
    adjacent **prosubiculum** and distal **CA1**), via the **fornix**, terminating principally in
    **layer III** of Brodmann areas **11**, **13**, **14** and **25** — **carries:** the completed
    episode, same payload and same owed limit as the parietal and cingulate limbs above.
    **Fan-out:** unknown. **Declared at the consumer's end as well as here**: the orbitofrontal /
    ventromedial entry (`11_frontal_lobe`) declares `← the hippocampal formation`, from the subiculum
    with the adjacent prosubiculum and distal CA1, written from this producer and terminating by name
    in four of that entry's five previously unused sub-elements.
    **The termination areas are that entry's own named-but-unused sub-element set**, which it
    records as the largest in its file: areas 11 and 13 orbitally, areas 14, 25 and 32 medially.
    **This edge uses four of the five**, so it is the first edge in the source with a claim on them.
    *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015, macaque (*Macaca fascicularis* and
    *Macaca mulatta*), anterograde tritiated-amino-acid autoradiography, 26 animals across two
    cohorts. Searched 2026-08-15; candidate.)*
  - **→ the anterior cingulate cortex**, from the **subiculum**, via the **fornix**, terminating in
    **layer III of Brodmann area 24a only** — **carries:** the same completed episode. **Fan-out:**
    unknown. **Declared at the consumer's end as well as here**: the anterior cingulate entry
    (`11_frontal_lobe`) declares `← the hippocampal formation`, terminating in area 24a only. **The sub-element restriction is the interesting part and is a claim that
    entry cannot currently receive**: it holds Brodmann areas 24 and 32 as divisional sub-elements
    that no edge uses, and this edge terminates in **24a and not 24b or 24c**, which is finer than
    either heading. *(Class 1 — same study.)*

    **What these two edges establish, and it is stronger than that two entries gained an input.**
    **The direct hippocampal projection to prefrontal cortex is confined to medial and orbital
    areas, is ipsilateral, arises principally from the subiculum, and travels by the fornix and by
    no other route** — established by injecting the tracer in animals whose fornix had been cut
    beforehand, where no prefrontal label appeared at all while comparable intact injections
    labelled it. **There is no lateral-prefrontal limb**: the dorsolateral, ventrolateral, Broca's
    and frontal-eye-field entries receive nothing from this structure directly. **And there is no
    return limb** — medial prefrontal cortex does not project back here, which is why the reuniens
    input above exists and is not redundant with it. **So the hippocampal–prefrontal connection is
    a one-way cortical edge whose loop closes through the thalamus**, and the source can now
    represent both halves: the cortical half is declared at both ends, and the thalamic half passes
    through a nucleus that has an entry. *(The projection facts are Class 1 from the study
    above. **Class 2** — the reading that the two halves are one loop, and that this is why the
    absence went unnoticed, is Claude's, offered to be checked.)*
  - **→ the nucleus reuniens** (midline thalamus), from **CA1** and the **subiculum** — **carries:**
    payload **owed**; the outgoing limb of the pair whose return is written in Inputs above.
    **Fan-out:** unknown. **Declared at the consumer's end as well as here** (`12_thalamus`). **Density is topographic** — terminations are denser in rostral reuniens, and
    denser again when the injection includes the subicular complex, which is consistent with the
    subicular attribution on the prefrontal edges above and is not evidence for it.
    *(Class 1 — Joyce et al. 2022, as above. Searched 2026-08-15; candidate.)*
  - **→ the amygdala**, onto the lateral nucleus and via entorhinal cortex — **carries:** episodic
    **context** — where am I, what is going on — which is what makes the same stimulus threatening
    in one place and not another. **Fan-out:** unknown. **The consumer is in this file and declares
    it.** 
  - **→ the bed nucleus of the stria terminalis**, from the subiculum — **carries:** context, per
    the consumer's declaration; **payload otherwise owed. Fan-out:** unknown. **The consumer is in
    this file and declares it.**
  - **→ the ventral pallidum** — **carries:** payload **owed. Fan-out:** unknown. **Declared at the consumer's end as well as here**: the ventral pallidum entry's Inputs
    (`09_basal_ganglia`) name "hippocampal formation / subiculum" among the convergent value-setting afferents,
    with the payload marked owed there.
  - **→ the basal forebrain and the septum**, via the pre-commissural fornix — **carries:** payload
    **owed. Fan-out:** unknown. **The consumer declares its sources as a class** — the basal
    forebrain entry's Inputs (`13_neuromodulatory_systems`) read "limbic and prefrontal cortex, hypothalamus, brainstem"
    — which covers this structure without naming it. **Owed as a cross-file edit at that entry
    (`13_neuromodulatory_systems`).** Recorded because it is the return limb of the theta loop: the pacing signal arrives
    from there and this is the path back.
- **Internal structure and internal data flow:** *(This entry's internal circuit is described in this slot with its edges
  typed. **The slot exists to collect exactly this** — a circuit that would otherwise sit as an
  untitled bullet between Inputs and Outputs, which is the shape the cerebellar cortex entry
  carries.)*

  **Divisional sub-elements: five in series** — **entorhinal cortex**, the **dentate gyrus**,
  **CA3**, **CA1**, and the **subiculum**. Taken from this entry's own Function field, which already
  names them and assigns each a job. This is the rare entry whose sub-elements were described before
  the slot existed. *(Class 3 — general hippocampal anatomy, as stated in this entry's Function.)*

  **Laminar sub-elements: three, and the standard eight-layer block does not apply.** This is
  **allocortex** — three-layered — as the entry's own heading says, so transcribing the file's
  usual six-to-eight-layer Class-3 block would assert a laminar circuit this structure does not
  have. **This is the third entry in the source where that boilerplate fails**, after primary motor
  cortex (agranular throughout) and the temporal pole (agranular in part); here it fails because the region is not
  isocortex at all. **The three layers' names and their per-sub-element differences are owed** —
  entorhinal cortex is itself layered differently from the fields it feeds, and this entry's
  Function already singles out **entorhinal layer II** as the carrier of the grid representation,
  which is a laminar claim the slot should hold rather than leave in prose.

  **The scope of this exception, recorded identically in five files.**
  The file's standard Class-3 laminar block — **1, 2, 3, 4, 5a, 5b, 6a, 6b** with **4 → 2/3**,
  **2/3 → 5a and 5b**, **6a → 4**, **6a → 5a**, **6b → 6a** and within-sub-element recurrence — is
  **not a default. It is a claim about granular isocortex**, and three of its edges route through
  layer 4. **Nine entries across five files cannot take it**: primary motor cortex (`05_sensorimotor_loop`,
  agranular throughout); the temporal pole (`07_anterior_temporal_lobe`, agranular medially on a gradient); the
  hippocampal formation (`08_medial_temporal_lobe`, three-layered allocortex); the cerebellar cortex (`10_cerebellum`,
  three-layered and not isocortex at all); and five entries in the frontal lobe (`11_frontal_lobe`) — premotor
  cortex, Broca's area, the right inferior frontal gyrus, the orbitofrontal / ventromedial entry and
  the anterior cingulate. **They fail it in four different ways** — uniformly agranular, agranular
  across a gradient, agranular across an internal border, and not isocortex — **so a single
  exception clause would not cover them.** **Owed at the design file: state where the block is
  defined that it applies to granular isocortex only**, rather than leaving each entry to discover
  the incompatibility on its own.


  **Internal edges — the trisynaptic circuit, and they are the point of the structure:**
  - **entorhinal cortex → the dentate gyrus**, via the perforant path — **carries:** the current
    **multimodal scene** — the identity codes of everything currently present, plus, from the
    entorhinal layer II grid code, a **metric of space**. **Fan-in / fan-out:** unknown.
  - **the dentate gyrus → CA3**, via the mossy fibres — **carries:** the same scene, **sparsified**
    — recoded so that similar scenes become dissimilar. **The payload change is the operation**:
    what enters and what leaves denote the same episode, and the difference is the representational
    distance between neighbours. Pattern separation. **Fan-in / fan-out:** unknown.
  - **CA3 → CA3**, recurrent — **carries:** the stored pattern under completion — a partial cue in,
    the whole pattern out. **This is the entry's defining edge and the brain's largest associational
    recurrent network. Fan-in:** ~6,000–12,000 recurrent contacts per cell. **Fan-out:** unknown.
  - **CA3 → CA1**, via the Schaffer collaterals — **carries:** the completed pattern.
    **Fan-in / fan-out:** unknown.
  - **entorhinal cortex → CA1**, direct (the temporoammonic path) — **carries:** the unsparsified
    current scene, arriving alongside the completed pattern. **This edge is what makes the next one
    a comparison rather than a relay**, and the Function field's word *comparator* requires it. **Fan-in / fan-out:** unknown. *(Class 3 — general
    hippocampal anatomy; **Class 2** — the reading that the comparator function requires this second
    input to exist is Claude's, though the path itself is standard. Candidate.)*
  - **CA1 → the subiculum** — **carries:** the result of the comparison — the completed episode,
    with its match against current input resolved. **Payload owed:** what a *comparison result* is,
    on a wire, is not stated anywhere — a scalar mismatch, a gated copy of the completed pattern, or
    something else. **Fan-in / fan-out:** unknown.
  - **the subiculum → entorhinal cortex** — **carries:** the completed episode, on its way back out
    through the port it came in by. **Fan-in / fan-out:** unknown.

  **Tangential sub-elements: unknown**, except that this entry's Function names a **grid**
  representation in entorhinal layer II, which is a spatially periodic organisation and therefore
  exactly the kind of tangential structure the slot is for. **Owed.**

  **The internal edges have no mechanical check and one of them is load-bearing.** The design's
  two-ended diff does not work inside an entry, so the CA1 comparison payload above cannot be caught
  by disagreement — it has to be read. It is the step on which the entry's claim to be a
  *comparator* rests, and it is the one internal payload here that cannot be written.
- **Neurons (per hemisphere, verified human stereology):** dentate gyrus granule ~15M; CA3 ~2.5M;
  CA1 ~16M; subiculum ~4M; entorhinal cortex ~6M (layers II/III) — total ~43M. Sources: West &
  Gundersen 1990; Šimić et al. 1997; West & Slomianka 1998 (entorhinal). (Refinement: human CA3
  *pyramidal* cells specifically ≈ 1.7M per hemisphere — Cell 2024 — against the ~2.5M
  total-CA3 figure above; pyramidal-versus-total, not a conflict.)
- **Synapses:** CA3 recurrent connectivity ~6,000–12,000 recurrent contacts per cell (the largest
  associational recurrent net); absolute count unknown.
- **Axons:** the perforant path (in) and the **fornix** (out and back), the latter with its own entry
  in `18_white_matter_tracts`, where its count is recorded as soft with a classical order
  estimate of ~1M. Perforant path count unknown.
- **Grey-matter volume:** hippocampus **~3.3–3.8 cm³ per hemisphere** (age-dependent). Primary
  anchor: normative magnetic resonance imaging (MRI) of 302 adults, mean 3.81 ± 0.46 cm³ (range 1.9–5.2; PMC7018315).
  Corroborating: ex-vivo MRI plus histology ~3.3 cm³ (Insausti lineage, PMC4476703); young-adult
  means ~2.8–2.9 cm³ (Honeycutt 1995); full literature span ~1.7–5.7 cm³. Right > left by a few
  percent. Density cross-check: hippocampus proper (~37.5M, excluding the separately-located
  entorhinal cortex) / ~3.55 cm³ ≈ ~10,500 neurons/mm³ — allocortex packing, between the subcortical
  nuclei (~10,000) and neocortex.
- **White-matter volume:** unknown. **Myelination:** unknown.

## Amygdala (amygdaloid complex, medial temporal lobe — subcortical nuclei)

- **Function:** assigns emotional and motivational significance to stimuli — threat detection and
  fear conditioning, and the affective and social evaluation of faces and voices. Drives autonomic,
  endocrine and behavioural responses, and modulates perception, attention and memory elsewhere.
  Division of labour by nucleus: the **lateral nucleus** is the main sensory-input zone; the
  **basal** and **accessory basal** nuclei do intermediate processing and carry most of the two-way
  cortical traffic; the **central nucleus** is the main output to hypothalamus and brainstem
  (autonomic, freezing, hypothalamic-pituitary-adrenal axis); the **medial nucleus** is olfactory
  and social; **intercalated cells** are inhibitory gates.
- **Inputs:**
  - **← inferotemporal cortex** — **carries:** fully-processed object and face identity, onto the
    **lateral nucleus**. Slow, and specific. **Fan-in:** unknown. **Far end in `01_visual_pathway`, unchecked.**
  - **← the anterior superior temporal gyrus and sulcus** — **carries:** **voice identity and vocal
    affect**, not speech content: this structure is named as part of the voice-sensitive network in
    human imaging, alongside inferior prefrontal cortex, and the speech-content payload of that
    entry goes to the semantic system instead. **The two payloads that share that territory separate
    here, at their destinations**, which is the clearest available evidence that they are separate
    payloads at all. **Fan-in:** unknown. **Far end in `02_auditory_pathway`, unchecked.** *(Class 1 for the voice network — Pernet, Belin et al. 2015, human. **Candidate:** the key reads **owed** in the reference section — not searched. Separate lines rather than one, out of the compound line "← sensory
    cortices".)*
  - **← the auditory parabelt, rostral division** — **carries:** sound-object identity, already made
    invariant to talker, pitch and level. **This is a third auditory route into this structure.** It
    differs from the two below in where it sits on the speed/detail trade-off: it is a **cortical**
    identity signal like the temporal-endpoint edge, but it arrives from one tier earlier in the
    hierarchy, so it should be **faster and less abstracted** than that one and far more processed
    than the thalamic one. **If the latency ordering matters — and this entry says it does — then
    there are three arrival times here, not two.** **Fan-in:** unknown. **Far end in `02_auditory_pathway`, unchecked.** *(Class 1 — Hackett lineage, PMC4001064, 2014,
    macaque. **Candidate:** the key reads **owed** in the reference section — not searched.)*
  - **← the medial geniculate nucleus, magnocellular division** (the fast subcortical "low road") —
    **carries:** a coarse, broadly-tuned, barely-processed signal — *something sudden, roughly
    there*. **The payload is deliberately impoverished and that is what buys the speed**: this edge
    and the cortical ones carry the same event at different levels of description, and the
    architecture depends on their latency difference, not on their content difference. **Fan-in:** unknown. **Far end in `02_auditory_pathway`, unchecked.**
  - **← the posterior thalamus** — **carries:** payload **owed. Fan-in:** unknown. **The producer
    declares no such edge.** The posterior / ventromedial-posterior thalamus entry (`12_thalamus`) declares
    its Outputs as the dorsal posterior insula and a lesser projection to area 3a — **no amygdala
    target of any kind.** **Owed as a cross-file edit at that entry (`12_thalamus`), or withdraw this
    limb.** *(Separate lines rather than one: the compound line "← MGm [medial geniculate nucleus, magnocellular
    division] / posterior thalamus", whose two limbs
    live in different files and have different statuses: one unchecked, one contradicted.)*
  - **← the lateral olfactory tract**, onto the **medial nucleus** — **carries:** the odour object.
    **Fan-in:** unknown. **Far end in `03_other_senses`, unchecked.**
  - **← the insula** — **carries:** payload **unknown — owed** at both ends. **Fan-in:** unknown.
    **The producer declares it and names this structure**: the insula entry's Outputs (`17_insula_claustrum_habenula`) read
    "→ Amygdala and Hypothalamus (autonomic / affect) — payload unknown — owed." Two-ended, and owed
    at both. *(Separate lines rather than one: "← insula / gustatory"; the gustatory limb is below.)*
  - **← the gustatory pathway** — **carries:** taste quality and intensity. **Fan-in:** unknown.
    **Far end in `03_other_senses`, unchecked.**
  - **← the hippocampal formation**, via entorhinal cortex — **carries:** episodic **context** —
    where am I, what is going on — which is what makes the same stimulus threatening in one place
    and not another. **Fan-in:** unknown. **The producer is in this file and declares it.**
  - **← the lateral parabrachial nucleus**, onto the **central nucleus** — **carries:** the
    **affective dimension of pain** — the unpleasantness, as distinct from the location and
    intensity that the thalamocortical line carries; monosynaptic and excitatory, with feed-forward
    inhibition in this structure. **Payload beyond "aversive value" — owed**, and the producer
    records that the completion test is not passed there either: *unpleasantness* is a phrase, not a
    type with a range and a frame. **Fan-in:** unknown. **Declared at the producer's end as well as here**: the lateral parabrachial entry (`14_brainstem_midbrain_hypothalamus`) declares
    "→ Amygdala, to the central nucleus." **This is the most consequential edge on this entry**
    — it describes a structure that assigns significance to stimuli, and this is the one arriving
    signal whose significance is not inferred. *(Class 1 — Sugimura, Takahashi, Watabe & Kato 2016, rat; plus Imaging Neuroscience doi 10.1162/imag_a_00567, 2025, human — the first in-vivo human
    delineation of the trigeminal → lateral parabrachial → central amygdala circuit. **Contested at the producer's end:** one report
    holds that this nucleus channels spinal nociceptive signals to the intralaminar thalamus but
    **not** to this structure; recorded there as contested and the edge kept. **Candidates:** both keys
    read **owed** in the reference section — neither has been searched.)*
  - **← the temporal pole** — **carries:** an **amodal concept**, for affective evaluation. **Payload
    unknown — owed. Fan-in:** unknown. **Declared at the producer's end as well as here**: the temporal pole entry's Outputs (`07_anterior_temporal_lobe`) declare "→ amygdala" and record that
    this entry's Inputs name that region's own *sources* — inferotemporal cortex and the anterior
    superior temporal gyrus — but not the region itself, marking it an owed cross-file edit at this
    entry. **That owed edit is discharged.** *(Transcribed from the temporal pole
    entry, `07_anterior_temporal_lobe`. Candidate.)*
  - **← the ventromedial and orbital prefrontal cortex** — **carries:** a regulatory signal —
    suppression or licensing of the response. **Payload otherwise unknown — owed. Fan-in:** unknown.
    **The producer declares it and names this structure**: the orbitofrontal / ventromedial
    prefrontal entry's Outputs (`11_frontal_lobe`) name the amygdala first among its targets.
    That entry types the edge in this end's own words — *a regulatory signal, suppression or
    licensing of the response*, payload otherwise owed — and records against its own line that this
    entry had asked it to. **Two-ended, and owed at both ends beyond the word *regulatory*.**
  - **← the ventral tegmental area** — **carries:** payload **owed. Fan-in:** unknown. **Declared at the producer's end as well as here**: that entry's Outputs (`13_neuromodulatory_systems`) name
    the amygdala.
  - **← the locus coeruleus** — **carries:** payload **owed. Fan-in:** unknown. **The producer
    declares a brain-wide class** (`13_neuromodulatory_systems`) that covers this structure; that entry's own Inputs name
    the amygdala, so the pair is reciprocal and only one limb is written there.
  - **← the nucleus reuniens** (midline thalamus), onto the **basal** and **basomedial (accessory
    basal)** nuclei — **carries:** payload **owed. Fan-in:** unknown. **Declared at the producer's end as well as here** (`12_thalamus`); see the hippocampal formation
    entry above, whose two reuniens edges are two-ended in the same way. *(Class 1 — Joyce et al. 2022, rhesus macaque, bidirectional tracing.
    **The primate finding is that this pathway is stronger than in rat or mouse**, which is a
    species claim rather than a payload, and it is the reason this edge is written from a primate
    study rather than carried from the rodent literature. Searched 2026-08-15; candidate.)*
  - **← the claustrum** — **carries:** payload **owed. Fan-in:** unknown. **Declared at the
    producer's end only**: the claustrum entry (`17_insula_claustrum_habenula`) names the ventral claustrum as reciprocally
    connected with this structure, in prose rather than as a typed edge. **Owed at
    `17_insula_claustrum_habenula`: convert that entry's prose slots to typed edges.**
- **Outputs:**
  - **→ the hypothalamus**, from the **central nucleus**, via the **stria terminalis** and the
    **ventral amygdalofugal pathway** — **carries:** a **valence and urgency signal** — *this is bad
    (or good), act now* — driving autonomic, endocrine and freezing responses. It carries **no
    identity information**: what leaves is the significance, not the thing. **Fan-out:** unknown.
    **The consumer declares it and names this structure**: the hypothalamus entry's Inputs (`14_brainstem_midbrain_hypothalamus`)
    read "limbic — amygdala, hippocampal formation (via the fornix), and septum," untyped there.
    **Owed at `14_brainstem_midbrain_hypothalamus`: type it.** *(Separate lines rather than one: a single line naming the hypothalamus, three brainstem targets and
    the basal forebrain together carries one payload across five endpoints whose far ends have four
    different statuses.)*
  - **→ the periaqueductal gray**, from the **central nucleus** — **carries:** the same valence and
    urgency signal, here driving the defensive response. **Fan-out:** unknown. **The consumer
    declares it and names this structure**: the periaqueductal gray entry's Inputs (`14_brainstem_midbrain_hypothalamus`) read
    "the **amygdala central nucleus** (the fear / defence output the Amygdala entry pointed to)."
    Two-ended, and the consumer names the sub-element. **Owed at `14_brainstem_midbrain_hypothalamus`: type it.**
  - **→ the locus coeruleus**, from the **central nucleus** — **carries:** the same signal.
    **Fan-out:** unknown. **The consumer declares it and names this structure** (`13_neuromodulatory_systems`). **Owed at
    `13_neuromodulatory_systems`: type it.**
  - **→ the lateral parabrachial nucleus**, from the **central nucleus** — **carries:** payload
    **owed. Fan-out:** unknown. **The consumer declares no such edge.** That entry's Inputs (`14_brainstem_midbrain_hypothalamus`)
    name lamina I of the spinal cord, the caudal spinal trigeminal nucleus and the nucleus of the
    solitary tract — **not this structure**. **Owed as a cross-file edit at that entry (`14_brainstem_midbrain_hypothalamus`).**
    Recorded rather than dropped because it is the return limb of the affective-pain input above,
    and a reciprocal pair with one limb missing is a shape this file records repeatedly.
  - **→ the basal forebrain**, from the **central nucleus** — **carries:** payload **owed.
    Fan-out:** unknown. **The consumer declares its sources as a class** — "limbic and prefrontal
    cortex, hypothalamus, brainstem" (`13_neuromodulatory_systems`) — which covers this structure without naming it.
    **Owed as a cross-file edit at that entry (`13_neuromodulatory_systems`).**
  - **→ the nucleus of the solitary tract** (descending) — **carries:** payload **owed. Fan-out:**
    unknown. **The consumer declares it and names this structure**: that entry's Inputs (`14_brainstem_midbrain_hypothalamus`)
    read "← Insula, Hypothalamus and Amygdala (descending) — payload unknown — owed." Owed at both ends.
  - **→ the bed nucleus of the stria terminalis**, from the **basolateral** nuclei, via the stria
    terminalis and the ventral amygdalofugal pathway — **carries:** the valence / threat signal.
    **Fan-out:** unknown. **The consumer is in this file and declares it** — the heaviest edge of the extended amygdala, and
    it is declared at both ends.
  - **→ the temporal pole**, from the **basal / accessory basal** nuclei — **carries:** the
    **valence tag** — a gain on perception, attention and memory encoding, carrying no identity
    information of its own. **Fan-out:** unknown. **The consumer declares it** (`07_anterior_temporal_lobe`) and records
    this entry's cortical target as a class that covers it without naming it, marking an owed
    cross-file edit here. **That owed edit is discharged.**
  - **→ the insula**, **→ the anterior cingulate cortex**, **→ the midcingulate cortex**, **→ the
    orbitofrontal / ventromedial prefrontal cortex**, and **→ the right inferior frontal gyrus** —
    **carries:** the same valence tag. **Fan-out:** unknown. **All five consumers declare this
    input**: the insula and midcingulate entries (`17_insula_claustrum_habenula`) and the anterior cingulate,
    orbitofrontal and right inferior frontal gyrus entries (`11_frontal_lobe`); the anterior cingulate marks
    its payload owed, the others are untyped. *(Separate lines rather than one: the class endpoint
    "→ widespread cortex (including feedback to sensory areas)" names no region with an
    entry, and these lines name its members. **The class is not fully resolved**: "feedback to sensory areas" remains a class, and the
    visual and auditory files are unchecked against this one, so any sensory-cortex targets are
    **unchecked**.)*

    ***The residual class is split, and the four lateral edges below are its lateral members.*** *Anterograde tracing in macaque finds this structure
    projecting to **almost all** prefrontal areas — densest medially and orbitally, and reaching the
    lateral surface as well. **What made the split writable rather than a guess is that the study
    names the areas and the source nucleus, and separates them by injection site**: only the
    injections centred in the **intermediate and magnocellular divisions of the basal nucleus**
    produced lateral-prefrontal label at all. Injections in the **accessory basal**, **parvicellular
    basal**, **lateral**, **medial** and **central** nuclei produced **none** — the accessory basal
    cases had no label anterior to the genu of the corpus callosum in any hemisphere. **So the
    lateral limb has a narrower origin than the five cortical edges above**, which this entry
    attributes to the basal and accessory basal nuclei together, and the four edges below are
    attributed accordingly.*

    ***Two properties belong to the whole family and are stated once here rather than on each
    line.*** *The projection is **wholly ipsilateral** — the one case with a unilateral injection
    showed no crossed prefrontal terminations of any kind. And it terminates in **deep layer I,
    layer II and layer VI**, while the hippocampal projection to the medial and orbital areas
    terminates in **layer III** — so **the two medial-temporal inputs to prefrontal cortex are
    laminarly segregated even in the areas that receive both**, which the study reads as allowing
    the two information types to be processed in parallel. *(Class 1 — Aggleton, Wright, Rosene &
    Saunders 2015, macaque, anterograde autoradiography. Searched 2026-08-15; candidate. **Class 2**
    — that the laminar segregation belongs on these edges as a payload-adjacent property rather than
    in prose is Claude's reading.)*
  - **→ the dorsolateral prefrontal cortex**, from the **intermediate and magnocellular divisions of
    the basal nucleus** — **carries:** the same **valence tag** the five cortical edges above carry;
    **payload otherwise owed. Fan-out:** unknown. Terminations in **Brodmann area 9** medially and
    laterally, and **patchily in area 46**, in the lower bank of the principal sulcus. **This is the
    lightest and least consistent of the four**: the area 46 label was present in one hemisphere and
    absent in the other of the same animal, and absent altogether in a second case. **Declared at the consumer's end as
    well as here**: the dorsolateral entry (`11_frontal_lobe`) declares the amygdalar input, written
    from this producer.
  - **→ the ventrolateral prefrontal cortex**, from the **intermediate and magnocellular divisions
    of the basal nucleus** — **carries:** the same valence tag; **payload otherwise owed.
    Fan-out:** unknown. **This is the densest of the four.** Terminations across **area 12** — which
    that entry's own file resolves to **Brodmann area 47** — in deep layer I, layer II and layer VI,
    continuing dorsally into much of **Brodmann area 45**. **Declared at the consumer's end as well as here**
    (`11_frontal_lobe`), written from this producer.
    **The endpoint is a sub-element claim that entry has already said it cannot receive.** Its
    Internal structure slot records its divisional internal edges as owed, on the ground that
    "nothing distinguishes what Brodmann area 45, Brodmann area 47 and area 12 each carry," and
    notes that an auditory input edge already assigns itself to *areas 12 and 45* specifically.
    **This edge is a second such assignment, arriving from a different file and a different
    modality**, which turns an internal-structure gap into a repeated external demand. **Owed
    there: divide the entry, or say why the two assignments cannot be received.**
    **And the consumer may be the wrong entry, by `11_frontal_lobe`'s own record.** Brodmann area 45 is
    claimed by both that entry and the Broca's-area entry, an overlap `11_frontal_lobe` researched and marks
    as having a proposed resolution rather than a settled one. **The area 45 limb of this edge lands
    in the disputed territory.** It is written to the ventrolateral entry because that entry also
    holds area 47, which carries the denser half; **it is not written to the Broca entry, because
    doing so would assert a homology this study cannot support** — the macaque has no Broca's area,
    and area 45 there is a cytoarchitectonic territory, not a language region. **Owed at `11_frontal_lobe`:
    settle the overlap, and re-terminate this edge if the settlement moves area 45.**
  - **→ premotor cortex**, from the **intermediate and magnocellular divisions of the basal
    nucleus** — **carries:** the same valence tag; **payload otherwise owed. Fan-out:** unknown.
    Terminations in **ventral area 6**, continuous with the area 45 label above and denser than it
    dorsally, and lighter label in **dorsal area 6** on the medial wall and dorsal convexity, which
    arrives continuous with the anterior cingulate label rather than separately. **Declared at the consumer's end
    as well as here**: the premotor entry (`11_frontal_lobe`) declares the amygdalar input, written
    from this producer.
    **Which sub-element receives it is owed and is not guessable from here.** That entry names
    **F2**, **F4** and **F5**, and records itself as one heading over at least five areas; **F4 and
    F5 sit in ventral area 6**, which is where this edge's denser half terminates, but the study
    divides area 6 dorsally and ventrally rather than by those names. **Owed: map the two
    divisions onto that entry's sub-elements, or leave the edge on the structure whole and say so.**
  - **→ the precentral opercular cortex**, from the **intermediate and magnocellular divisions of
    the basal nucleus** — **carries:** the same valence tag; **payload otherwise owed. Fan-out:**
    unknown. **Particularly dense**, and continuous with the area 45 and ventral area 6 label above
    rather than separate from it. **This region has no entry in any file.** The frontal operculum is
    named in the source only as half of the **primary gustatory cortex** (`03_other_senses`, "anterior insula +
    frontal operculum") and again at the insula entry (`17_insula_claustrum_habenula`) — and the precentral opercular area
    is a **different** field from gustatory cortex in the parcellation this study uses, which labels
    both separately in the same sections. **So this endpoint names a region the source does not
    describe, and the nearest thing it does describe is a neighbour rather than the same place.**
    **Owed: give the precentral opercular cortex an entry and decide which file owns it** — it is
    frontal by position and opercular by neighbourhood, so `11_frontal_lobe`, `03_other_senses` and `05_sensorimotor_loop` are all
    plausible owners and none is obvious.

    **What remains of the class after the split, and it is not nothing.** The original endpoint read
    "widespread cortex (including feedback to sensory areas)". **The cortical members are nine named edges.** **"Feedback to sensory areas"
remains a class and remains unchecked**: `01_visual_pathway` and `02_auditory_pathway` are unchecked
against this one. **One further named target from the same study is deliberately not written
    here**: the label continued laterally into the **gustatory cortex**, which does have an entry
    (`03_other_senses`) — but `03_other_senses` is unchecked against this one, and writing the edge from one end while
marking the far end unchecked is the state this file does not leave behind. **Owed:
check `03_other_senses` against this one and write it, or establish that the gustatory label is fibres of
    passage.**
  - **→ the nucleus reuniens** (midline thalamus), from the **basal** and **basomedial (accessory
    basal)** nuclei — **carries:** payload **owed**; in the producer's terms the affective-context
    limb of the reuniens convergence. **Fan-out:** unknown. **Declared at the consumer's end as well as here** (`12_thalamus`). **What makes this edge worth writing rather than
    noting**: the same nucleus receives the hippocampal formation and medial prefrontal area 25, so
    **the reuniens is where this file's two major structures and their prefrontal target converge
    on one stage** — and the source cannot say so anywhere, because the stage has no slot.
    *(Class 1 — Joyce et al. 2022. Amygdalar terminations there are enriched with mitochondria and
    often form successive synapses onto the same postsynaptic structure, which that study reads as
    an active and robust pathway; the reading is theirs. Searched 2026-08-15; candidate.)*
  - **→ the mediodorsal thalamus** — **carries:** **limbic value / significance context. Payload
    otherwise unknown — owed. Fan-out:** unknown. **Declared at the consumer's end as well as here**: that entry's Inputs (`12_thalamus`) read "← amygdala; ← olfactory / limbic
    cortex — carries: limbic value / significance context."
  - **→ the zona incerta**, from the **central nucleus**, onto its parvalbumin neurons — **carries:**
    payload **owed**; the producer's role in this pair is given at the consumer's end as fear.
    **Fan-out:** unknown. **Declared at the consumer's end as well as here**
    (`12_thalamus`).
  - **→ the raphe nuclei** — **carries:** payload **owed. Fan-out:** unknown. **Declared at the
    consumer's end only** (`13_neuromodulatory_systems`).
  - **→ the ventral pallidum** — **carries:** payload **owed**; the consumer groups it with valence,
    context, need state and prediction error as "the convergence of everything that sets what an
    outcome is worth." **Fan-out:** unknown. **Declared at the consumer's end as well as here**: the ventral pallidum entry's Inputs (`09_basal_ganglia`) name the amygdala first.
  - **→ the ventral striatum** — **carries:** the valence tag. **Fan-out:** unknown. **The consumer
    declares its sources as a class** — the basal ganglia entry's Inputs (`09_basal_ganglia`) read "← nearly all
    of cortex," and this structure is not cortex, so the class does not even cover it. **Owed as a
    cross-file edit at that entry (`09_basal_ganglia`).**
  - **→ the hippocampal formation**, from the **basal / accessory basal** nuclei — **carries:** the
    valence tag. **Fan-out:** unknown. **The consumer is in this file and declares it.**
- **Internal structure and internal data flow:** *(The sub-elements and counts below come from this entry's own
  Function field, which describes the division of labour; the slot holds them and the edges between
  them.)*

  **Divisional sub-elements: five named nuclei plus one interposed cell class** — the **lateral
  nucleus**, the **basal nucleus**, the **accessory basal nucleus**, the **central nucleus**, the
  **medial nucleus**, and the **intercalated cells**. Taken from this entry's own Function field.
  **This is the best-quantified sub-element set in the file**: the stereology below gives a separate
  neuron count for four of the five nuclei, which no other entry in this file can do.

  **The basal nucleus now needs dividing, and four of the edges above force it.**
  This entry names the **basal nucleus** as one sub-element. The tracing study those four edges come
  from divides it into **parvicellular**, **intermediate** and **magnocellular** divisions, and the
  division is **load-bearing rather than nomenclatural**: injections in the intermediate and
  magnocellular divisions labelled orbital, medial *and* lateral prefrontal cortex, while an
  injection in the parvicellular division labelled only restricted orbital and medial sites and
  **no lateral prefrontal cortex at all**. **So two divisions of one sub-element have different
  targets, which is exactly §3's test for a sub-element in its own right.** **Owed: name the three
  divisions, and re-check the five cortical edges above against them** — those are
  attributed to "the basal and accessory basal nuclei" together, and this study's accessory-basal
  injections produced no prefrontal label anterior to the genu at all, so that attribution may be
  wider than the evidence. **This is the arity re-check §4 warns is the real cost of adding internal
  detail**, arriving in the usual direction: the new detail was found while writing an edge, not
  while writing the slot. *(Class 1 for the injection-by-injection differences — Aggleton, Wright,
  Rosene & Saunders 2015. **Class 2** — that this makes the divisions sub-elements rather than
  properties is Claude's application of the floor-of-the-hierarchy rule, offered to be checked.)*

  **Laminar sub-elements: not applicable.** These are subcortical nuclei, not cortex. Recorded as a
  positive statement rather than as unknown.

  **Tangential sub-elements: unknown.**

  **Internal edges — the division of labour, typed from this entry's own Function field:**
  - **the lateral nucleus → the basal and accessory basal nuclei** — **carries:** the sensory
    identity codes arriving from cortex and thalamus, entering intermediate processing.
    **Fan-in / fan-out:** unknown. **Payload change — owed:** what the intermediate stage does to
    the identity code is the step at which a stimulus becomes a significance, and nothing here says
    what happens.
  - **the basal and accessory basal nuclei → the central nucleus** — **carries:** the evaluated
    signal on its way to the output stage. **Fan-in / fan-out:** unknown. **Payload owed.**
  - **the intercalated cells → the central nucleus** — **carries:** **inhibition** — the gate on
    the output stage. Named as inhibitory gates in the Function field, with no source, target
    detail, or sign-of-effect typed beyond that. **Fan-in / fan-out:** unknown.

  **Where the significance is assigned is not written, and it is the entry's whole claim.** Identity
  codes and an affective-pain signal arrive; a valence and urgency signal leaves, carrying no
  identity. **Somewhere between the lateral nucleus and the central nucleus the identity is
  discarded and a value is produced, and no edge here says where or how.** This is the same shape as
  the transform at the anterior intraparietal area, the frame mixture at the medial intraparietal
  area, the binding at the angular gyrus and the temporal pole, and the subjective feeling at the
  anterior insula — **and it is the sixth**. The pattern across all six is that the entry whose
  output payload cannot be typed is the entry whose internal mechanism is not written.
  *(Class 3 for the nucleus-to-nucleus routing, which is general amygdala anatomy as stated in this
  entry's Function. **Class 2** — the observation that the identity-to-value conversion is unlocated
  is Claude's, offered to be checked.)*
- **Neurons (per hemisphere, verified human stereology):** total amygdaloid complex **~12.2M** —
  lateral 4.00M, basal 3.24M, accessory basal 1.28M, central 0.36M, remaining nuclei 3.33M (Schumann
  & Amaral 2005, optical fractionator; the West et al. 1991 method, as for the hippocampus).
  **The central nucleus is the smallest counted nucleus and carries the entire subcortical output**
  — 0.36M cells against the lateral nucleus's 4.00M, an ~11:1 convergence across the internal
  edges above, which is a constraint the fan-in slots ought to reflect and currently do not.
- **Synapses:** unknown. **Axons:** the **stria terminalis** and the **ventral amygdalofugal
  pathway** (counts unknown). Both are named in `18_white_matter_tracts`'s preamble as already
  recorded where a pathway needed them, so neither has an entry of its own there.
- **Grey-matter volume:** ~1.3 cm³ per hemisphere (ex-vivo histology ~1.26 cm³, Insausti lineage, PMC4476703; in-vivo
  MRI ~1.2–1.7 cm³). Density cross-check: ~12.2M / ~1.26 cm³ ≈ ~9,700 neurons/mm³ — loose
  subcortical / allocortical packing, below the lateral geniculate nucleus's ~17,000/mm³.
- **White-matter volume:** unknown. **Myelination:** unknown.

## Bed nucleus of the stria terminalis (extended amygdala, basal forebrain)

- **Function:** the forebrain hub of the **extended amygdala** — the anatomical and functional
  partner of the central amygdala, continuous with it through the sublenticular extended amygdala.
  Where the central amygdala drives **phasic, cued fear** (a discrete threat), this structure drives
  **sustained responses to unpredictable, ambiguous or diffuse threat** — the state properly called
  **anxiety** — continuing to shape behaviour long after the trigger is gone (the Davis–Walker
  phasic-fear / sustained-anxiety dissociation; Walker & Davis 2008; Davis, Walker, Miles & Grillon
  2010). This sustained mode is **corticotropin-releasing-factor-dependent** (both
  corticotropin-releasing-factor-enhanced and light-enhanced startle depend on this structure and
  not on the central amygdala). Human imaging reproduces the split (phasic versus sustained threat;
  Alvarez et al. 2011), and its connectivity with the amygdala tracks trait anxiety (Fox & Shackman
  2019). It is a classic **sexually dimorphic** nucleus.
- **Inputs:**
  - **← the amygdala**, from the **basolateral** nuclei, via the **stria terminalis** and the ventral
    amygdalofugal pathway — **carries:** the valence / threat signal. **Fan-in:** unknown. **The
    producer is in this file and declares it** — this is the heaviest edge of the extended
    amygdala, and it is declared at both ends.
  - **← the hippocampal formation**, from the **subiculum** — **carries:** episodic **context**.
    **Payload otherwise unknown — owed. Fan-in:** unknown. **The producer is in this file and
    declares it.** *(Separate lines rather than one: a single line "← hippocampal formation / subiculum, anterior
    insula, ventromedial / orbital prefrontal cortex, brainstem viscerosensory" names four sources
    and carries one payload — "context, interoceptive state, and regulatory control" — across all of
    them, and the three payload terms belong one each to three of the four sources, which is why such
    a line reads as complete and is not.)*
  - **← the anterior insula** — **carries:** **interoceptive state. Payload otherwise unknown —
    owed. Fan-in:** unknown. **The producer declares no such edge.** The insula entry's Outputs
    (`17_insula_claustrum_habenula`) name the anterior cingulate and prefrontal cortex, the amygdala and hypothalamus, the
    basal ganglia, the habenula, and the posterior thalamus — **not this structure**. **Owed as a
    cross-file edit at that entry (`17_insula_claustrum_habenula`).**
  - **← the ventromedial and orbital prefrontal cortex** — **carries:** **regulatory control** —
    suppression or licensing of the sustained response, the same kind of signal that entry sends the
    amygdala. **Payload otherwise unknown — owed. Fan-in:** unknown.
    **Two-ended.** The orbitofrontal / ventromedial prefrontal entry (`11_frontal_lobe`) declares
    `→ the bed nucleus of the stria terminalis` on its own line, typed **regulatory control —
    suppression or licensing of the *sustained* response, the same kind of signal this entry sends
    the amygdala**.
    **But the two ends are one end, and that is the part to keep.** That entry wrote its line
    **from this file's declaration**, and quotes as its warrant a four-item description of its own
    Outputs slot that no longer matches it — that slot now names ten targets. **So the payload
    agrees because it was copied, and the agreement certifies nothing** (§4). The edge itself rests
    on a compound prose line with no citation at either end. **Owed: a source for this edge, at
    either end.**
    **That four-item description is still in circulation inside `11_frontal_lobe` itself**, at its
    right-inferior-frontal-gyrus entry, where it asserts that the orbitofrontal entry declares no
    output to that gyrus — which the orbitofrontal entry, twenty-five lines later in the same file,
    declares. **Owed at `11_frontal_lobe`: that entry contradicts itself.**
  - **← the lateral parabrachial nucleus** — **carries:** payload **owed** at both ends. **Fan-in:**
    unknown. **The producer declares it and names this structure**: that entry's Outputs (`14_brainstem_midbrain_hypothalamus`)
    read "→ Bed nucleus of the stria terminalis — payload unknown — owed." *(This resolves the
    former line's fourth endpoint, "brainstem viscerosensory", which was a **class**. Naming it
    matters here more than usual: the same nucleus supplies the central amygdala's affective-pain
    input, so the phasic and sustained arms of the extended amygdala share a producer, and the
    difference between them cannot be a difference in this source.)*
- **Outputs:**
  - **→ the hypothalamus**, to the **paraventricular nucleus** (the hypothalamic-pituitary-adrenal
    axis) and the feeding and autonomic nuclei — **carries:** a **sustained** threat state — the
    same valence the central amygdala emits, but **held over time and not tied to a cue**. The
    payload difference between this structure and the central amygdala is **duration and
    cue-binding, not content**: phasic, cued fear there; sustained, diffuse anxiety here. That is a
    real distinction on the wire and it is the reason both entries exist. **Fan-out:** unknown.
    **The consumer declares no such edge.** The hypothalamus entry's Inputs (`14_brainstem_midbrain_hypothalamus`) read "limbic —
    amygdala, hippocampal formation (via the fornix), and septum" — **this structure is not among
    them**, and the amygdala it does name is the partner this entry exists to be distinguished from.
    **Owed as a cross-file edit at that entry (`14_brainstem_midbrain_hypothalamus`).** *(Separate lines rather than one: a line that named
    the hypothalamus, four brainstem targets and the ventral tegmental area together.)*
  - **→ the periaqueductal gray** — **carries:** the same sustained threat state. **Fan-out:**
    unknown. **The consumer declares no such edge.** The periaqueductal gray entry's Inputs
    (`14_brainstem_midbrain_hypothalamus`) name the amygdala central nucleus, the hypothalamus and ventromedial / orbital
    prefrontal cortex — **not this structure**. **Owed as a cross-file edit at that entry
    (`14_brainstem_midbrain_hypothalamus`).**
  - **→ the lateral parabrachial nucleus** and **→ brainstem autonomic and neuromodulatory centres**
    — **carries:** the same sustained threat state; **payload otherwise owed. Fan-out:** unknown.
    **The parabrachial consumer declares no such edge** (`14_brainstem_midbrain_hypothalamus`, whose Inputs name lamina I, the
    caudal spinal trigeminal nucleus and the solitary nucleus). **"Brainstem autonomic and
    neuromodulatory centres" is a class and does not resolve. Owed: name them, and write the
    cross-file edit at the parabrachial entry (`14_brainstem_midbrain_hypothalamus`).**
  - **→ the ventral tegmental area** — **carries:** a **sustained threat / defence state** — a
    persistent aversive-state signal and **not a discrete stimulus**; **payload otherwise owed.
    Fan-out:** unknown.
    **Two-ended, and the edge is carried under two structure names.** That entry
    (`13_neuromodulatory_systems`) declares it as **← the amygdala**, typed *a sustained threat /
    defence state*, from a producer's declaration. **Each end looked for its own name and did not
    find it**: this end searched for the bed nucleus; that end named the amygdala and took this file
    to have declared it. **A name mismatch produces a false negative at both ends at once, and
    neither end can see it alone.**
    **The consumer's own payload is the evidence that it means this structure and not the amygdala.**
    *Sustained*, *persistent*, *not a discrete stimulus* is precisely the distinction this entry
    exists to carry and that the central amygdala's phasic arm does not. **The type was written at
    the far end, from the far end's own reading, and it lands here.** The type above is now taken
    from it. **Owed at `13_neuromodulatory_systems`: rename the endpoint to this structure, or state that the projection
    arises from both and is one edge at a coarse grain.**

  **Three of the four output far ends are undeclared, and the fourth is the more useful finding.**
  The three `14_brainstem_midbrain_hypothalamus` targets — hypothalamus, periaqueductal gray, lateral
  parabrachial nucleus — are undeclared at their consumers, and every one of them declares the
  central amygdala instead. **The fourth is not.** The ventral tegmental area declares this edge
  under the name *amygdala* and types it with this structure's own signature.

  **The sustained arm therefore reaches at least one declared far end, and the finding is not that
  it is better connected than recorded.** It is that **a structure-name mismatch can hide an edge
  from both sides at once — and that a count of undeclared far ends is only as good as the names it
  was counted under.**

  **Owed: check the other three the same way.** File 14 holds all of them, and a mismatch of exactly
  the same shape is available there, because *the central amygdala* is the name each of them
  carries and *extended amygdala* is the term that covers both structures. **A far end that declares
  "the amygdala" may be declaring this structure**, and nothing in either file distinguishes the two
  readings. **Owed also: write the three, or establish that the sustained arm shares the central
  nucleus's axons rather than having its own.** That second possibility is not idle: the two
  structures are described here as continuous through the sublenticular extended amygdala, and a
  continuous structure may not have two separable projections to divide. **It is now the likelier
  of the two**, since the one far end that has been read resolves the ambiguity by naming the
  amygdala and typing this structure.
- **Internal structure and internal data flow:** *(Almost all of this slot is owed, and the reasons are recorded rather than left blank.)*

  **Divisional sub-elements: owed.** This structure is described in its own Function field as
  **heterogeneous**, and the literature divides it into anterior and posterior divisions with
  multiple subnuclei, but **no subdivision is established by what this file records**, and the entry
  names none. **This is *owed* and not *unknown*:** the sub-elements are known to exist and to have
  been described; they have not been written here.

  **Laminar sub-elements: not applicable.** A basal-forebrain nucleus, not cortex.

  **Cell-class sub-elements: one is named by the entry's own Function and is load-bearing** — the
  **corticotropin-releasing-factor-expressing** population. The Function field makes the sustained
  mode depend on it, which is a claim that a cell class, and not the structure as a whole, carries
  the payload the Outputs describe. **On the floor-of-the-hierarchy rule that makes it a sub-element
  rather than a property**, and the edges out of it should be written separately from the rest.
  **Owed: establish whether the four output edges above leave from this population.**

  **Sexual dimorphism is recorded here rather than as a sub-element.** The Function field calls this
  a classic sexually dimorphic nucleus, and the number slots below record that human work reports
  volume and sex differences rather than absolute counts. **A difference between two populations'
  instances of one structure is not a division within one instance**, so it does not create
  sub-elements — the same treatment the angular gyrus entry gives its left/right functional
  asymmetry. **What is owed is whether the dimorphism changes any edge**, which is a data-flow
  question and is not answered anywhere in this file.

  **Internal edges: owed, all of them.** None is described, in either direction.
- **Neurons:** soft / unknown — a small, heterogeneous, sexually dimorphic basal-forebrain nucleus;
  no clean human control count recorded here (human work reports volumes and sex / identity
  differences rather than an absolute).
- **Synapses:** unknown. **Axons:** the **stria terminalis** and the **ventral amygdalofugal
  pathway** (counts unknown) — the same two pathways the amygdala entry names, which is consistent
  with the continuity claim above and is not evidence for it.
- **Grey-matter volume:** small (sub-cm³), sexually dimorphic; no single verified human figure
  recorded here. **White-matter volume:** unknown. **Myelination:** unknown.

**Two findings here are about the source rather than about this file, and are recorded at this
file because this is the entry set whose edges reach them.**

**First: the two-ended diff has a systematic blind spot, and this file's frontal connection is where
it shows.** The medial-temporal–to–frontal connection exists, is one-way, and closes its loop through
a thalamic nucleus the source does not describe — and **an absence at both ends of an edge passes
every check the two-ended diff can run**, because the diff detects a *disagreement* between two
declarations and is blind to the *absence* of both. **Every edge missing from the whole source is
missing in exactly this way**, and the only instrument that finds one is two files read together
against the literature. *(The edges are Class 1 and cited at their lines. **Class 2** — the reading
that the diff has a blind spot of this shape is Claude's, offered to be checked.)*

**Second: this file is the destination of an unusual number of one-ended edges** — **21** are
declared at a far end across eight other files: **9** at the hippocampal formation, **11** at the
amygdala, **1** at the bed nucleus. The reason is structural rather than accidental: nearly every
limbic and neuromodulatory entry in the source names the amygdala or the hippocampus among its
targets or sources, and those two entries answer few of them. Whether that is the largest such count
in the source is **not established** — no comparable count has been taken for any other file.

---

---

## References

*(Under source design §2a. **No line here carries a line number**: a pointer into the file goes
stale on the next edit and fails silently, so the section is joined to the entries by the key alone. Each full reference given here was obtained by a web search against
publisher or journal records — no reference given in full is written from recall. Keys reading
**owed** were not searched, and the citation text for those keys, wherever it appears in this file,
**was** written from recall.)*

**23 distinct keys, 29 mentions. 5 verified against a publisher or journal
record; 2 located in secondary listings only and still candidates; 16 owed.**

***A reference enters verified against the record it was taken from, and searching is the
verification rather than a step before it*** *(§2a; CLAUDE.md gives the same test in general form —*
**verified when something was opened or searched, not when someone read it**\ *). So a key read off a
publisher or journal record is verified at the moment it is searched, and does not wait on a reader.
Attaching verification to a person would contradict §2's rule that data verifies to the literature
and never to a person, since* **agreement is not evidence** *about a fact outside this project.*

***Two keys are deliberately not promoted, and the distinction is the useful part.*** *West &
Slomianka 1998 and Šimić et al. 1997 are located in **publisher reference listings** — a secondary
listing that repeats a citation, not the record of the paper itself. **Something was opened, but not
the thing that would settle the citation.** They stay candidates. The line between the five and
these two is exactly the line §2a draws, and it is not a matter of confidence: a secondary listing
can propagate an error in the very fields it is being consulted for.*

**Nine keys give a journal and a year, or an accession, with no author** — *Cell Reports 2022,
S2211-124700958-5*; *Nature Communications 2023, s41467-023-41746-0*;
*J Neurosci 40:3591, 2020*; *Cell 2024*; *Imaging Neuroscience doi
10.1162/imag_a_00567, 2025*; and the four bare accessions *PMC2538919*, *PMC7018315*, *PMC4476703* and *PMC4001064*. All nine **are** searchable — an
accession or a manuscript identifier pins one paper — and are listed under the short form the
file uses. *Cell 2024* is the weakest of them: a journal and a year with no volume, page or
identifier, supporting a specific human count.

**Two keys are lineages with a paper attached, which is the form that works.** *Insausti lineage,
PMC4476703* and *Hackett lineage, PMC4001064* both name a body of work **and**
an accession, so the accession is searchable even though the lineage is not. Compare `06_posterior_parietal` and
07, where bare lineages with no accession could not be searched at all.

**One stereology method key is cited but no result is taken from it.** *West et al. 1991*
appears only as the method the amygdala counts follow — “the West et al. 1991 method, as for the
hippocampus.” It is a key of this file and is listed, but nothing in the file rests on its
findings, only on its procedure.


- **Aggleton, Wright, Rosene & Saunders 2015** — Aggleton, J.P., Wright, N.F., Rosene, D.L. & Saunders, R.C. (2015). Complementary patterns of direct amygdala and hippocampal projections to the macaque prefrontal cortex. *Cerebral Cortex* 25(11): 4351–4373; doi 10.1093/cercor/bhv019; PubMed 25715284. **Macaque** (*Macaca fascicularis* and *Macaca mulatta*), 26 animals across two cohorts. Anterograde autoradiography — tritiated proline / leucine injections into the amygdala and the hippocampal formation, with a subset of animals whose fornix had been transected 2–12 months beforehand. *(Oxford Academic publisher record, open access; full text read.)* **This is the sole source for the two hippocampal → prefrontal edges and for the lateral-prefrontal block on the amygdala entry, and three of its properties are load-bearing and are recorded on those lines rather than here:** the fornix-transection cases are what make *the fornix is the only route* a positive finding instead of an untested assumption; the terminations are restricted to areas 11, 13, 14, 24a, 25 and 32 with **no lateral-prefrontal hippocampal limb at all**; and the amygdalar and hippocampal inputs occupy **different laminae** even where they share an area. **A limit of the study belongs here rather than on the lines:** it is macaque, and the source's counting basis is human. The termination areas are Carmichael and Price's macaque parcellation, and whether area 24a, 14r and 14c map cleanly onto the human areas `11_frontal_lobe`'s entries name is **not established by this paper and is not asserted on the edges**. *(**Verified against the Oxford
- **Alvarez et al. 2011** — **owed**: not searched.
- **Cell 2024** — **owed**: not searched.
- **Cell Reports 2022, S2211-1247(22)00958-5** — **owed**: not searched.
- **Davis, Walker, Miles & Grillon 2010** — **owed**: not searched.
- **Fox & Shackman 2019** — **owed**: not searched.
- **Hackett lineage, PMC4001064, 2014** — **owed**: not searched.
- **Honeycutt 1995** — **owed**: not searched.
- **Imaging Neuroscience doi 10.1162/imag_a_00567, 2025** — **owed**: not searched.
- **Insausti lineage, PMC4476703** — **owed**: not searched.
- **J Neurosci 40:3591, 2020** — **owed**: not searched.
- **Joyce et al. 2022** — Joyce, M.K.P., Marshall, L.G., Banik, S.L., Wang, J., Xiao, D., Bunce, J.G. & Barbas, H. (2022). Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus. *Journal of Neuroscience* 42(6): 1068–1089; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. **Rhesus macaque** (*Macaca mulatta*), 12 animals, both sexes. Bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. *(Society for Neuroscience journal record; full text read.)* **This is the sole source for the four nucleus reuniens edges.** Its bearing beyond them: the primate reuniens is **matrix-dominant** — calbindin and calretinin projection cells, targeting cortical layers I–IIIa — with a sparse **parvalbumin** core population, which is a claim about the *form* of its cortical output and not about a payload, and which is the kind of claim `12_thalamus`'s other entries carry in their Internal structure slots. **It also states plainly, and cites Cassel et al. 2013 for it, that medial prefrontal cortex does not project directly to the hippocampus** — the negative that makes the hippocampal → prefrontal edge one-way rather than half of a reciprocal pair nobody had written. *(**Verified against the Society for Neuroscience journal record, 2026-08-15**; full text read.)*
- **Nature Communications 2023, s41467-023-41746-0** — **owed**: not searched.
- **Pernet, Belin et al. 2015** — **owed**: not searched.
- **PMC2538919** — **owed**: not searched.
- **PMC7018315** — **owed**: not searched.
- **Schumann & Amaral 2005** — Schumann, C.M. & Amaral, D.G. (2005). Stereological estimation of the number of neurons in the human amygdaloid complex. *Journal of Comparative Neurology* 491(4): 320–329; doi 10.1002/cne.20704. **Human.** Nissl sections, optical fractionator. *(Wiley publisher record.)* Every figure at matches the paper exactly — lateral 4.00, basal 3.24, accessory basal 1.28, central 0.36, remaining 3.33, total 12.21 million. **But the entry presents this as the human count, and the search returned at least two others.** A later stereological study of 7 controls aged 20–75 (PubMed 22719923, Cavalieri principle plus optical fractionator over 5 nuclear groups and 13 subdivisions) gives the complex **15.3M** neurons; and Schumann & Amaral's own text reports that Vereecken et al. 1994 estimated **10.7M left and 9.8M right** in an older control population, using a different regional definition. So the human amygdala total spans roughly **9.8–15.3M across three studies**, and the differences track the definition of the complex's boundary and the age of the sample. **This is the file's own contested-number shape and the entry does not currently mark it as one.** *(**Verified against the Wiley publisher record, 2026-08-11.**.)*
- **Šimić et al. 1997** — Šimić, G., Kostović, I., Winblad, B. & Bogdanović, N. (1997). Volume and number of neurons of the human hippocampal formation in normal aging and Alzheimer's disease. *Journal of Comparative Neurology* 379: 482–494. **Human.** *(Located in publisher reference listings — a secondary listing.)* Note: the study's design contrasts normal ageing with Alzheimer's disease, so which arm the entry's figures are taken from is not established by the citing line. *(**Candidate:** located 2026-08-11 in publisher reference listings only — a secondary listing, not the record of the paper..)*
- **Sugimura, Takahashi, Watabe & Kato 2016** — **owed**: not searched.
- **Walker & Davis 2008** — **owed**: not searched.
- **West & Gundersen 1990** — West, M.J. & Gundersen, H.J.G. (1990). Unbiased stereological estimation of the number of neurons in the human hippocampus. *Journal of Comparative Neurology* 296(1): 1–22; doi 10.1002/cne.902960102; PubMed 2358525. **Human**, five subdivisions. *(Wiley publisher record and PubMed.)* Method note bearing on the entry's *verified human stereology* label: for each subdivision the total was computed as **the volume of the neuron-containing layers multiplied by the numerical density of neurons in them**, from 3 mm slabs cut transverse to the rostrocaudal axis — a volume-times-density estimate, not the optical fractionator used for the amygdala counts in the same entry. Both are unbiased designs; they are not the same design. *(**Verified against the Wiley publisher record and PubMed, 2026-08-11.**.)*
- **West & Slomianka 1998** — West, M.J. & Slomianka, L. (1998). Total number of neurons in the layers of the human entorhinal cortex. *Hippocampus* 8(1): 69–82; doi 10.1002/(SICI)1098-1063(1998)8:1<69::AID-HIPO7>3.0.CO;2-2. **Human**, by layer — which is what supports the entry's figure being given for layers II/III specifically. *(**Candidate:** located 2026-08-11 in publisher reference listings only — a secondary listing, not the record of the paper, so the citation fields are unconfirmed at their source..)*
- **West et al. 1991** — West, M.J., Slomianka, L. & Gundersen, H.J.G. (1991). Unbiased stereological estimation of the total number of neurons in the subdivisions of the rat hippocampus using the optical fractionator. *Anatomical Record* 231: 482–497; doi 10.1002/ar.1092310411. **Rat.** *(Wiley publisher record.)* This is the paper that introduces the optical fractionator, and cites it as a method rather than for a result — correctly, since the result is rat. Worth recording that the method paper this entry leans on for both its hippocampal and amygdalar counts is **not a human study**; the method transfers, the numbers in it do not. *(**Verified against the Wiley publisher record, 2026-08-11.**.)*
