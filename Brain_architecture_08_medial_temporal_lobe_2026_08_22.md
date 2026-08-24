# Brain architecture — 08 medial temporal lobe

**Date:** 2026-08-22
**Derived from:** `human_brain_08_medial_temporal_lobe_2026_08_22.md` — three structures: the
hippocampal formation, the amygdala, and the bed nucleus of the stria terminalis. **One source file,
and no other content source.**

**Cross-file checks contained in this file.** One line per far file whose shared edges with this one
are diffed and stemmed.

- `01_visual_pathway`
- `07_anterior_temporal_lobe`
- `09_basal_ganglia`
- `11_frontal_lobe`
- `12_thalamus`
- `13_neuromodulatory_systems`
- `14_brainstem_midbrain_hypothalamus`
- `17_insula_claustrum_habenula`

**Counting basis is uniform: per hemisphere**, and it is verified human stereology for two of the
three structures.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file is checked against this one; an endpoint with no stem is unchecked, and that is
not a claim that none exists.

**Far ends: edges leave this section into twelve files.** `01_visual_pathway`,
`02_auditory_pathway`, `03_other_senses`, `06_posterior_parietal`, `07_anterior_temporal_lobe`,
`09_basal_ganglia`, `11_frontal_lobe`, `12_thalamus`, `13_neuromodulatory_systems`,
`14_brainstem_midbrain_hypothalamus`, `17_insula_claustrum_habenula` and `18_white_matter_tracts`.
**Eight of the twelve carry a check line above and their edges are stemmed and diffed below**;
`02_auditory_pathway`, `03_other_senses`, `06_posterior_parietal` and `18_white_matter_tracts` do
not, and their endpoints name the far file without asserting anything about its contents.

**An owed mark against a file with no check line reads *unverified*, never *outstanding*.** A
one-file-at-a-time reading can only leave a note naming what it could see of the far end from one
side, and a note of that kind is discharged as often as it is upheld when the two files are finally
opened together. **The mark records what this file can see of another file, and nothing more.**

**Twelve edges cross between this file and `17_insula_claustrum_habenula`, and every one of the
twelve is declared at both ends.** **Not one edge dangles in either direction, which holds for no
other file pair in this section.**

**Three claustral edges the far end declares are not written here**, and they are listed at the
entries they belong to: amygdala `→ claustrum`, hippocampal formation `→ claustrum`, and hippocampal
formation `← claustrum`. **They are not written as edges, and the repair is at the source rung, not
here.** **All four claustral cross-edges — those three and the `← claustrum` this file does declare —
derive from a single sentence in `17_insula_claustrum_habenula`'s claustrum Function slot, carrying a
single citation.** That citation is a **diffusion-tractography study**, and diffusion tractography is
undirected — it cannot distinguish an afferent from an efferent connection. **So the citation supports
the existence of a claustro-amygdalar and a claustro-hippocampal connection and supports no direction
on either**: one undirected prose claim stands behind four directed edges. **Owed at
`17_insula_claustrum_habenula`'s source, and it is a citation repair rather than an edge decision.**
Writing the three edges here would propagate the unwarranted direction into a second file and make it
read as corroborated. *(The tractography limitation was searched and confirmed against several
independent methodological sources; the claim that the primate tracing literature describes the
amygdala and hippocampus as projecting **to** the claustrum rather than reciprocally with it is a
candidate awaiting Micky's verification and is not written into any slot.)*

Each edge below names the file its far end sits in and the state of the far end's own declaration; no
far end's content is written from memory. **The source's own caution is inherited: five edges have far
ends in `01_visual_pathway` and `02_auditory_pathway`, which are unchecked against this file, and
those are marked *unchecked* rather than confirmed.**

**Eighty-one edges are declared here, and the source carries seventy-two edge lines.** The two counts
are not the same quantity and neither is derived from the other. **The source counts bullets**, and
its own header states 72 — 36 in and 36 out. **This rung counts edges**: some source bullets name more
than one target structure, the largest naming five at once, and the arity is explicit in the source in
every case, so splitting invents nothing.

**A count of this file returns eighty-four arrow-headed endpoints, of which three are declined as
edges** — the claustral pair at the hippocampal formation and the outgoing claustral limb at the
amygdala, all three withheld because four directed edges rest on one undirected
diffusion-tractography sentence. **84 less 3 is the eighty-one above.** **A further endpoint is not an
edge and is recorded as owed instead**: the bed nucleus's "brainstem autonomic and neuromodulatory
centres" is a class that does not resolve to any named structure.

**Ten edges arrived at this rung after they were written at the source, and the count is what made
them findable.** They are the output of the source's 2026-08-15 research pass — the four **nucleus
reuniens** edges, the two hippocampal projections to medial and orbital prefrontal cortex, and the
four amygdalar projections to lateral prefrontal, premotor and precentral opercular cortex. **This
file had reconciled its own count against the source's and reported a difference of one**, which is
what a ten-edge gap looks like when both totals are counted the same way and one of them is stale.
**`Brain_08_medial_temporal_lobe` declares 72 edges and has not received them either: the same carry
is owed at the code design's contract block and at the module.**

---

## Structural invariants

**Whole-pathway co-instantiation.** Every structure here is present and active from the outset, and
this section is the densest set of closed loops the project has met. **Three loops close entirely
inside this file**, with both limbs written at both ends:

- **hippocampal formation ↔ amygdala** — episodic context out from the subiculum and entorhinal
  cortex, the valence tag back from the basal and accessory basal nuclei.
- **hippocampal formation → bed nucleus of the stria terminalis**, from the subiculum, closing
  through the amygdala rather than directly.
- **amygdala ↔ bed nucleus of the stria terminalis**, from the basolateral nuclei via the stria
  terminalis and the ventral amygdalofugal pathway.

**And one loop closes through a stage this section does not own and the source does describe** — the
theta loop: the medial septum paces the hippocampal formation via the fornix, and the pre-commissural
fornix carries the return limb back to the septum and basal forebrain. **That return limb's far end
declares its sources as a class**, so the loop is closed here and half-declared there.

**A fifth loop closes through a stage outside this section, and it could not be stated at all until
the far end existed.** The hippocampal formation projects to medial and orbital prefrontal cortex by
the fornix and by no other route, and **medial prefrontal cortex has no return projection here** — the
return runs through the **nucleus reuniens**, which both major structures of this section also
project to and receive from. **So the medial-temporal–to-prefrontal connection is a one-way cortical
edge whose loop closes through the thalamus**, and every limb of it is now declared at both ends:
four reuniens edges in `12_thalamus` and two cortical edges in `11_frontal_lobe`. **Co-instantiation
is satisfiable for this loop**, which it was not while the thalamic stage had no entry.

**The Papez circuit leaves this section and does not return inside it.** The post-commissural fornix
reaches the mammillary bodies and anterior thalamic nuclei, and the return arm runs via
parahippocampal cortex, **which has no entry in any file**. **Co-instantiation cannot be satisfied
for that loop at this rung**, and the repair is the source's. It is the same defect the design file
records for the cerebro-cerebellar loop, and it is the second file in which the missing region is
this same one.

**Per-edge latency.** Every edge carries a nonzero, finite, heterogeneous latency in real time units.
**Every edge latency in this section reads *to derive*.** No conduction time and no synaptic delay is
recorded on any of the eighty-one.

**This section nonetheless contains a real-time figure, and it is
not an edge latency.** The medial septum's parvalbumin-expressing pacemaker cells deliver a **theta
timing reference — the phase of a 4–12 Hz rhythm**, a period of **83 to 250 ms**. Three properties of
it matter at this rung and each is stated in the source:

1. **The clock is not made by the transmitter.** Its tick is an **intrinsic membrane oscillation**
   generated by the hyperpolarization-activated cyclic-nucleotide-gated channel and its current, whose
   gating kinetics set the frequency. The individual pacemakers frequency-lock to one rhythm by
   mutual inhibition.
2. **It is delivered on an edge, onto the hippocampal formation's own inhibitory interneurons**, and
   that edge has a latency like any other — unrecorded.
3. **It paces one structure, not the system.** Nothing in the source extends it beyond the
   hippocampal formation's principal cells.

**So this is a payload, not a scheduler, and the distinction is the whole of the no-global-clock
argument.** A phase arriving on a wire with a propagation delay is content; a shared beat that
advances every structure together is a register. **The first is what the source describes and the
second is what may not be assumed** — and the temptation here is real, because a 4–12 Hz rhythm
looks like exactly the update rate a scheduler would want. It is not one, and reading it as one would
substitute a global clock for the heterogeneous delays the invariant exists to protect. *(That theta
is a payload rather than a scheduling signal is Claude's reading, offered to be checked; the three
properties above are Class 1 from the source.)*

**One edge here is a routing statement rather than a transfer.** The fornix has its own entry in the
white-matter file and computes nothing; it splits at the anterior commissure into a post-commissural
limb and a pre-commissural limb. Fan-in and fan-out on it read **none**, and **the regions it reaches
are written as their own edges** rather than being collapsed into it.

---

## Hippocampal formation

- **Function → structure.** The trisynaptic memory circuit, and **a content-addressable episodic
  store rather than a relay.** **Five divisional sub-elements in series, each with its own job**:
  **entorhinal cortex** is the input and output port — all neocortical input in, all hippocampal
  output out — and its **layer II carries the grid representation**; the **dentate gyrus** performs
  sparse pattern separation; **CA3** is the recurrent autoassociator doing pattern completion and
  one-shot episodic binding, and is **the brain's largest associational recurrent network**; **CA1**
  is the comparator and main output; the **subiculum** is the principal output.
  **Laminar sub-elements: three, and the standard eight-layer block does not apply.** This is
  **allocortex** — three-layered — so transcribing the granular-isocortex block would assert a
  laminar circuit this structure does not have. **The three layers' names and their per-sub-element
  differences are owed**, and entorhinal cortex is itself layered differently from the fields it
  feeds.
  **Tangential sub-elements: unknown, with one named exception that is owed** — the **grid**
  representation in entorhinal layer II is a spatially periodic organisation, which is tangential
  structure by definition and is not yet written as one.
  **Internal edges — the trisynaptic circuit, and they are the point of the structure:**
  - **entorhinal cortex → dentate gyrus**, via the perforant path — the current **multimodal scene**,
    the identity codes of everything present plus a **metric of space** from the layer II grid code.
    Fan-in / fan-out: to derive.
  - **dentate gyrus → CA3**, via the mossy fibres — the same scene, **sparsified**. **The payload
    change is the operation**: what enters and what leaves denote the same episode and the difference
    is the representational distance between neighbours. Fan-in / fan-out: to derive.
  - **CA3 → CA3**, recurrent — the stored pattern under completion, a partial cue in and the whole
    pattern out. **Fan-in: ~6,000–12,000 recurrent contacts per cell** — the only measured fan-in in
    this section. Fan-out: to derive.
  - **CA3 → CA1**, via the Schaffer collaterals — the completed pattern. Fan-in / fan-out: to derive.
  - **entorhinal cortex → CA1**, direct, the temporoammonic path — the unsparsified current scene
    arriving alongside the completed pattern. **This edge is what makes the next one a comparison
    rather than a relay.** Fan-in / fan-out: to derive.
  - **CA1 → subiculum** — the result of the comparison. **Payload owed, and it is the one internal
    payload here that cannot be written**: what a comparison result is on a wire — a scalar mismatch,
    a gated copy of the completed pattern, or something else — is not stated. **The entry's claim to
    be a comparator rests on this step**, and an internal edge has both ends inside one entry and
    therefore no mechanical two-ended check.
  - **subiculum → entorhinal cortex** — the completed episode, leaving through the port it came in
    by. Fan-in / fan-out: to derive.

- **Inputs.**
  - **← inferotemporal cortex** (`01_visual_pathway`), via entorhinal cortex and the perforant path —
    object and scene identity, invariant to position, size, pose and lighting. Fan-in: to derive.
    **Two-ended.** The producer declares it and types it *the identity code
    as one element of an episode* — **the same code, described from the other side**: this end names
    what the code is invariant to, the producer names what the code is for. **Neither end contradicts
    the other and neither is complete alone.** The producer also declares a **separate** edge to
    perirhinal cortex, calling it *the anatomical step by which the ventral stream reaches the
    hippocampal formation*, and **perirhinal cortex has no entry in any file** — so the route this
    edge takes is declared at the producer and unrepresentable at either end.
  - **← temporal pole**, onto entorhinal cortex (`07_anterior_temporal_lobe`) — an **amodal
    concept**, payload owed at the producer, where modality-loss is the only checkable property in
    hand. Fan-in: to derive. **Two-ended.** **This line names the producer and the same sub-element.** The
    inferotemporal edge is a separate line here.
  - **← angular gyrus** — payload owed, and the producer marks it the loudest owed payload in its own
    file. Fan-in: to derive. *(`06_posterior_parietal`.)*
  - **← precuneus** — payload owed. Fan-in: to derive. *(`06_posterior_parietal`; the producer's
  line owes a split.)*
  - **← posterior cingulate cortex** (`17_insula_claustrum_habenula`) — payload owed. Fan-in: to
    derive. **Two-ended**, and the mark stands: the producer declares this
    edge by name and its payload reads owed at that end too. **Owed at both, and naming the consumer
    is not typing the edge** — the producer's own line says so.
  - **← retrosplenial cortex** (`17_insula_claustrum_habenula`), via parahippocampal and entorhinal
    cortex — the **return arm of the spatial-memory loop**, carrying heading and landmark information
    after that entry's egocentric-to-allocentric translation. Payload otherwise owed. Fan-in: to
    derive. **Two-ended.** The producer declares it in near-identical terms
    and names the same route. **This is the strongest agreement in the pair** — a typed payload, an
    agreed route, and each end written from its own side. **The route still runs through
    parahippocampal cortex, which has no entry in any file**, and both ends say so independently.
  - **← perirhinal cortex** and **← parahippocampal cortex** — payload owed. Fan-in: to derive.
    **Neither has an entry in any file**, and two other files' edges point at them. **Inherited gap;
    not patched here.**
  - **← claustrum** — **not written as an edge, and the repair is not at this rung.**
    `17_insula_claustrum_habenula` declares `→ hippocampus / subiculum` at its claustrum entry,
    payload owed, and correctly records that this entry declares no such input. **Same warrant and
    same finding as the outgoing limb above: one sentence, one diffusion-tractography citation, no
    direction.** **Owed at `17_insula_claustrum_habenula`, not here.**
  - **← medial septum, parvalbumin-expressing GABAergic pacemaker cells**
    (`13_neuromodulatory_systems`), via the pre-commissural fornix, terminating on **hippocampal
    inhibitory interneurons** in CA1, CA3 and the dentate gyrus — the **theta timing reference**, the
    phase of a 4–12 Hz rhythm, **not content**. Fan-in: to derive. **Two-ended**, and the producer
    names the same sub-element, the same target class and the same
    payload, including that GABA is the wire and not the oscillator.
    **The three septal edges disagree with the producer about which fornix limb carries which, and
    neither end notices.** This file routes the **parvalbumin** edge via the **pre-commissural**
    fornix and leaves the cholinergic and glutamatergic edges on the fornix unqualified. The producer
    routes the **cholinergic** edge via the **fornix, pre-commissural limb** and leaves the
    parvalbumin and glutamatergic edges unqualified. **Each end names one edge with the finer route
    and they name different edges.** Neither is a contradiction — all three may run the same limb —
    but **the finer route is asserted on one edge at each end and on no edge at both.** **Owed:
    which limb carries which, at the source.**
  - **← medial septum, glutamatergic cells**, via the fornix — a **tonic excitatory gate**, the
    depolarizing drive that determines whether the pacemakers oscillate at all. Fan-in: to derive.
  - **← medial septum, cholinergic cells**, via the fornix — a **tonic gain and arousal-state
    signal**, delivered largely by **volume transmission** — about 93% of cholinergic varicosities
    here form no classic synapse. It gates the theta-versus-ripple regime and **does not set theta
    frequency**. Fan-in: to derive.
  - **← ventral tegmental area** (`13_neuromodulatory_systems`) — dopamine as a **novelty / salience
    signal gating what is encoded**; payload otherwise owed. Fan-in: to derive. **Two-ended, and the
    producer types it where this
    end does not.** The type above is the
    producer's wording, taken here.
  - **← locus coeruleus** (`13_neuromodulatory_systems`) — payload owed; noradrenaline, global gain
    and salience or surprise. Fan-in: to derive. **Two-ended.** **The producer declares `→
    hippocampus` on its own line**, separately from the
    brain-wide cortical class it also carries. **A named edge, not a class member.**
  - **← raphe nuclei** (`13_neuromodulatory_systems`) — payload owed. Fan-in: to derive. **The mark
  stands.** The producer's nearest declaration is `→ the limbic system`, a
    class it marks as inherited and unresolved, and it records that this file's entries name the raphe
    from their side. **Owed there, and the debt is the source's**, since the producer marks the class
    inherited and forbidden to repair at its own rung.
  - **← nucleus reuniens** (`12_thalamus`), terminating on **CA1** and the **subiculum** — payload
    owed. Fan-in: to derive. **This is the return arm of the prefrontal loop**: medial prefrontal
    cortex has no direct projection here, so this is the stage through which it reaches this
    structure. **Two-ended.** That entry was created from this file's four reuniens edges and
    declares this one; **the gap this line once recorded — a nucleus named nowhere in the source —
    is closed.**
  - **← amygdala**, from the basal and accessory basal nuclei — the **valence tag**, a gain on
    perception, attention and memory encoding, **carrying no identity information of its own**. **This
    is the payload that makes emotional events better remembered, and it is a modulator rather than a
    content line.** Fan-in: to derive. *(Producer is in this file. Both ends written together, so
    their agreement certifies nothing.)*

- **Outputs.**
  - **→ fornix** — the completed episode in transit. **A routing statement, not a transfer**: fan-out
    **none**, no synapse. *(`18_white_matter_tracts`.)*
  - **→ mammillary bodies** (`14_brainstem_midbrain_hypothalamus`) and **→ anterior thalamic nuclei**
    (`12_thalamus`), via the post-commissural fornix, the Papez circuit — a **completed episode**:
    the bound,
    retrievable pattern. **Payload only partly writable — owed**: an episode has no units and no frame,
    and what makes it checkable is a property rather than a type — it is **content-addressable**, which
    the upstream identity codes are not. Fan-out: to derive.
    **The mammillary endpoint is inside a bundle at the far end, and this file and that one disagree
    about how many edges there are..** That file has **no mammillary entry**: the
    mammillary bodies are one of eleven named sub-nuclei of its **hypothalamus** entry, which it
    records as a bundle whose split is owed at its source and explicitly declines to split. **So this
    line and the hypothalamic line below both terminate on the same far entry**, while that entry
    declares **one** hippocampal input — `← hippocampal formation, via the fornix` — not two.
    **Neither end is wrong and the arity does not match**: this file separates the Papez limb from the
    hypothalamic one because they leave by different fornix divisions, and that file cannot separate
    them because the target is undivided there. **The mismatch is a consequence of the bundle and
    resolves when the bundle splits; it is not repaired at either architecture file.**
  - **→ hypothalamus**, via the fornix (`14_brainstem_midbrain_hypothalamus`) — payload owed. Fan-out:
    to derive. **Two-ended, and the mark stands**: the consumer declares
    `← hippocampal formation, via the fornix` and marks the payload owed, so **both ends name the same
    tract and neither can type it.** **See the arity note above** — that one declaration may be
    standing for this edge, the mammillary edge, or both.
  - **→ angular gyrus** and **→ precuneus** — the completed episode, same owed limit. Fan-out: to
    derive. *(`06_posterior_parietal`; both consumers declare it.)*
  - **→ posterior cingulate cortex** and **→ retrosplenial cortex**
    (`17_insula_claustrum_habenula`) — the same completed episode. Fan-out: to derive.
    **Two-ended, and both consumers type it**, as the completed episode, *addressable by any fragment
    of itself*, with the payload marked only partly writable for the same reason this end gives — an
    episode has no units and no frame. **The agreement is transmission, not corroboration**: both
    consumers attribute the type to this file's declaration, so what is confirmed is that the payload
    crossed the file boundary intact, not that two derivations met.
    **The retrosplenial consumer names the sub-element at this end and this end does not** — it reads
    *from the subiculum*, and this line attributes the output to the structure whole. The
    posterior-cingulate consumer names no sub-element either way. **Owed here: whether both edges
    leave from the subiculum, or only the retrosplenial one.**
  - **→ claustrum** — **not written as an edge, and the repair is not at this rung.**
    `17_insula_claustrum_habenula` declares `← hippocampus / subiculum` at its claustrum entry,
    payload owed, and correctly records that this entry declares no such output. **Its warrant: that
    edge and its three claustral siblings all derive from one sentence in
    `17_insula_claustrum_habenula`'s claustrum Function slot, carrying one citation — a
    diffusion-tractography
    study, which is undirected and cannot support a directed edge in either direction.** **Owed at
    `17_insula_claustrum_habenula`, not here.** Writing this edge from the far end's declaration would
    propagate a direction the cited work does not establish.
  - **→ amygdala**, onto the lateral nucleus and via entorhinal cortex — episodic **context**, which
    is what makes the same stimulus threatening in one place and not another. Fan-out: to derive.
  - **→ bed nucleus of the stria terminalis**, from the subiculum — context; payload otherwise owed.
    Fan-out: to derive.
  - **→ nucleus reuniens** (`12_thalamus`), from **CA1** and the **subiculum** — payload owed.
    Fan-out: to derive. **Two-ended.** The outgoing limb of the pair whose return is written in
    Inputs. **Termination density is topographic** — denser in rostral reuniens, and denser again
    when the injection includes the subicular complex, which is consistent with the subicular
    attribution on the prefrontal edges below and is not evidence for it.
  - **→ orbitofrontal / ventromedial prefrontal cortex** (`11_frontal_lobe`), from the **subiculum**
    with the adjacent **prosubiculum** and distal **CA1**, via the **fornix**, terminating
    principally in **layer III** of Brodmann areas **11**, **13**, **14** and **25** — the completed
    episode, same owed limit as the parietal and cingulate limbs. Fan-out: to derive. **Two-ended.**
    The consumer declares it, written from this producer, and **it terminates by name in four of
    that entry's five previously unused divisional sub-elements** — the first edge in the source
    with a claim on them.
  - **→ anterior cingulate cortex** (`11_frontal_lobe`), from the **subiculum**, via the **fornix**,
    terminating in **layer III of Brodmann area 24a only** — the same completed episode. Fan-out: to
    derive. **Two-ended.** **The sub-element restriction is finer than either end's divisional
    set**: that entry holds Brodmann areas 24 and 32, and this edge lands in 24a and not 24b or 24c.
    **Owed there: divide area 24, or record that an incoming edge is finer than the entry's own
    partition.**
  - **→ ventral pallidum** (`09_basal_ganglia`) — payload owed. Fan-out: to derive. **Two-ended and
    checked: the consumer declares it and types it the valence tag, payload otherwise owed** — so
    both ends now agree, and both agree the payload is incomplete.
  - **→ basal forebrain** and **→ septum** (`13_neuromodulatory_systems`), via the pre-commissural
    fornix — payload owed. Fan-out: to derive. **This is the return limb of the theta loop**: the
    pacing signal arrives from there and this is the path back. **The mark stands.** The consumer's
    basal forebrain entry declares four inputs and none of them is this one;
    the nearest is `← limbic and prefrontal cortex`, a class it marks inherited and unresolved across
    this file, 11 and 17. **So the theta loop is declared closed at this end and open at that one**,
    and the septal half is worse than the basal-forebrain half: **the medial septum is a named
    division of that entry, and it declares no input at all.** **Owed there, and inherited from its
    source.**

- **Sizing.** Basis: **per hemisphere**, verified human stereology.
  **This structure's count partitions to its divisional sub-elements, and the partition closes.**
  The lateral geniculate nucleus is the other such case, and unlike
  that one this partitions across sub-elements the edges actually terminate on.

  | sub-element | neurons | fan-in | bits | parameter memory |
  |---|---|---|---|---|
  | dentate gyrus, granule cells | ~15M | to derive | ≤ 16 | ≤ 30.00 MB |
  | CA3 | ~2.5M | **~6,000–12,000** | **13–14** | **4.06–4.38 MB** |
  | CA1 | ~16M | to derive | ≤ 16 | ≤ 32.00 MB |
  | subiculum | ~4M | to derive | ≤ 16 | ≤ 8.00 MB |
  | entorhinal cortex (layers II/III) | ~6M | to derive | ≤ 16 | ≤ 12.00 MB |
  | **structure total** | **43.5M** | | | **86.06–86.38 MB** |

  **Re-derived rather than carried: the parts sum to 43.5M and the source's headline reads ~43M.**
  The 0.5M is rounding at the headline, not a missing population — the source's own hippocampus-proper
  figure of ~37.5M is exactly 43.5 − 6 with entorhinal cortex removed, so the arithmetic is
  internally consistent in both directions.
  **CA3 carries the only measured fan-in in the section**, and it is one of the few places where
  the log₂ bound bites below 16 bits. A 2× spread in contacts costs **one bit**, moving CA3's store
  by 1.08× — the same insensitivity the design file records.
  **Recorded, not resolved:** human CA3 *pyramidal* cells specifically are ~1.7M per
  hemisphere against the ~2.5M total-CA3 figure. Pyramidal-versus-total, not a conflict, and the
  table uses the total.

- **Shape.** **Sheet, and an allocortical one — rank 4: (lamina, division, H, W).** Three laminae,
  not eight, and **the lamina names are owed and differ by division**, so the axis is ordered and not
  labelled. Five divisions, **and this is the one shape axis in the project so far whose extent is
  both known and populated**: 5, with a neuron count against each.
  **H, W: to derive.** No tangential pitch is measured. The grid in entorhinal layer II is a
  spatially periodic organisation and would be the place a pitch first appears, and none is recorded.
  **The tile calculation is short one term.** Volumetric density is in hand — hippocampus proper
  ~37.5M over ~3.55 cm³ is **~10,563 neurons/mm³**, closing against the source's ~10,500 — but no
  thickness and no surface area is recorded, so surface density does not follow.
  **The volume is soft and the density moves with it**: ~11,364/mm³ at 3.3 cm³ and ~9,868/mm³ at
  3.8 cm³ across the primary range, and **~6,579 to ~22,059/mm³ across the full literature span of
  1.7–5.7 cm³**, which is a 3.4× spread. Right exceeds left by a few percent.

- **Edge latency.** All edges **to derive.** The section's one real-time figure — the 4–12 Hz theta
  period, 83–250 ms — is a **rhythm carried as a payload on one input edge**, not a latency on it and
  not a schedule for anything.

- **Invariant conformance.** Co-instantiation: satisfied for the loops with the amygdala and the bed
  nucleus, both closed inside this file; **satisfied internally**, since the trisynaptic circuit plus
  the CA3 recurrence and the subiculum-to-entorhinal return are all present and none can be staged —
  a recurrent autoassociator with its recurrence deferred is not an autoassociator. **Not satisfiable
  for the Papez loop**, whose return arm runs through parahippocampal cortex, which has no entry.
  Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** The structural claim the counts support is the **funnel and the
  expansion**: entorhinal cortex ~6M feeds a dentate gyrus of ~15M, which feeds a CA3 of ~2.5M, which
  feeds a CA1 of ~16M. **The wide-narrow-wide profile is the pattern-separation and
  pattern-completion architecture read off the cell counts** — expansion into a sparse code, then
  compression into the smallest field in the structure, which is also the one carrying the largest
  recurrent network. **CA3 being both the smallest principal field and the most densely
  interconnected is what makes one-shot binding affordable**: ~6,000–12,000 recurrent contacts per
  cell over 2.5M cells is a recurrent net whose cost is bounded by the count, not by the connectivity,
  because log₂ caps the per-cell store at 14 bits.

## Amygdala

- **Function → structure.** Assigns emotional and motivational significance to stimuli — threat
  detection and fear conditioning, and the affective and social evaluation of faces and voices —
  drives autonomic, endocrine and behavioural responses, and modulates perception, attention and
  memory elsewhere. **Division of labour by nucleus, and it is the best-quantified sub-element set in
  the section**: the **lateral nucleus** is the main sensory-input zone; the **basal** and **accessory
  basal** nuclei do intermediate processing and carry most of the two-way cortical traffic; the
  **central nucleus** is the main output to hypothalamus and brainstem; the **medial nucleus** is
  olfactory and social; **intercalated cells** are inhibitory gates.
  **Laminar sub-elements: not applicable** — subcortical nuclei, not cortex. A positive statement,
  not an unknown.
  **Tangential sub-elements: unknown.**
  **Internal edges — the division of labour:**
  - **lateral nucleus → basal and accessory basal nuclei** — the sensory identity codes arriving from
    cortex and thalamus, entering intermediate processing. **Payload change owed:** what the
    intermediate stage does to the identity code is the step at which a stimulus becomes a
    significance, and nothing says what happens. Fan-in / fan-out: to derive.
  - **basal and accessory basal nuclei → central nucleus** — the evaluated signal on its way to the
    output stage. Payload owed. Fan-in / fan-out: to derive.
  - **intercalated cells → central nucleus** — **inhibition**, the gate on the output stage. Fan-in /
    fan-out: to derive.
  **Where the significance is assigned is not written, and it is the entry's whole claim.** Identity
  codes and an affective-pain signal arrive; a valence and urgency signal leaves carrying no identity.
  **Somewhere between the lateral nucleus and the central nucleus the identity is discarded and a
  value is produced, and no edge says where or how.**

- **Inputs.**
  - **← inferotemporal cortex** (`01_visual_pathway`), onto the **lateral nucleus** —
    fully-processed object and face identity. Slow, and specific. Fan-in: to derive.
    **Two-ended.** The producer declares it and types it *identity, for
    affective evaluation* — **so the producer names this end's function and this end names the
    payload**, and the two compose without conflict. **The producer does not name the lateral
    nucleus**; it declares the amygdala whole. The sub-element endpoint exists only at this end, which
    is the arrangement the design file warns of: the diff sees two structure names agreeing while one
    end is finer than the other.
  - **← anterior superior temporal gyrus and sulcus** — **voice identity and vocal affect, not speech
    content**. **The two payloads that share that territory separate here, at their destinations**,
    which is the clearest available evidence that they are separate payloads at all. Fan-in: to
    derive. *(`02_auditory_pathway`; unchecked.)*
  - **← auditory parabelt, rostral division** — sound-object identity, already invariant to talker,
    pitch and level. **A third auditory route**, one tier earlier in the hierarchy than the temporal
    endpoint, so faster and less abstracted. Fan-in: to derive. *(`02_auditory_pathway`; unchecked.)*
  - **← medial geniculate nucleus, magnocellular division** — the fast subcortical route: a coarse,
    broadly-tuned, barely-processed signal. **The payload is deliberately impoverished and that is
    what buys the speed** — this edge and the cortical ones carry the same event at different levels
    of description, and **the architecture depends on their latency difference, not on their content
    difference.** Fan-in: to derive. *(`02_auditory_pathway`; unchecked.)*
  - **← posterior thalamus** (`12_thalamus`) — payload owed. Fan-in: to derive. **The producer
    declares no such edge**: that entry's Outputs name the dorsal posterior insula and area 3a and no
    amygdala target of any kind. **Owed there, or withdraw this limb.** **The mark holds exactly** —
    three outputs, the two named above
    plus the reticular collaterals, and nothing amygdalar. **The far end records the
    assertion from its own side and likewise declines to write the edge in**, so the limb stands
    declared at this end alone with both ends aware of it.
  - **← lateral olfactory tract**, onto the **medial nucleus** — the odour object. Fan-in: to derive.
    *(`03_other_senses`; unchecked.)*
  - **← insula** (`17_insula_claustrum_habenula`) — payload owed at both ends. Fan-in: to derive.
    **Two-ended, and the mark stands exactly as written.** The producer
    declares `→ amygdala` and marks it *payload owed at both ends* in the same words. **Both ends
    agree, and what they agree on is that neither can say what is on the wire.**
  - **← gustatory pathway** — taste quality and intensity. Fan-in: to derive. *(`03_other_senses`;
  unchecked.)*
  - **← hippocampal formation**, via entorhinal cortex — episodic **context**. Fan-in: to derive.
  - **← lateral parabrachial nucleus** (`14_brainstem_midbrain_hypothalamus`), onto the **central
    nucleus** — the **affective dimension of pain**: the unpleasantness, as distinct from the
    location and intensity the thalamocortical line
    carries. Monosynaptic and excitatory, with feed-forward inhibition here. Payload beyond aversive
    value owed at both ends. Fan-in: to derive. **Contested at the producer's end**: one report holds
    that this nucleus reaches the intralaminar thalamus and **not** this structure. **Two-ended; the
    contest is recorded at the producer in the same terms, and the edge is
    kept at both ends for the same reason** — human tractography and rodent circuit mapping both
    support it. **The producer adds what this end does not**: the human evidence is a first in-vivo
    diffusion-tractography delineation of the trigeminal → parabrachial → central-amygdala circuit,
    with the right-side circuit stronger in males than females. **That asymmetry sits on an edge this
    file counts per hemisphere and that file counts per side**, and neither end draws the consequence.
  - **← temporal pole** (`07_anterior_temporal_lobe`) — an **amodal concept**, for affective
    evaluation. Payload owed. Fan-in: to derive. **Two-ended.** **This line names the producer.**
  - **← ventromedial and orbital prefrontal cortex** — a **regulatory signal**: suppression or
    licensing of the response. Payload otherwise owed. Fan-in: to derive. *(`11_frontal_lobe`;
    untyped there.)*
  - **← ventral tegmental area** (`13_neuromodulatory_systems`) — payload owed. Fan-in: to derive.
    **Two-ended. Payload owed at both ends.**
  - **← locus coeruleus** (`13_neuromodulatory_systems`) — the **gain and salience signal**; payload
    otherwise owed. Fan-in: to derive. **Two-ended.** **Both limbs are written
    there**: the producer declares `→ amygdala` and `← amygdala, central nucleus` and names them
    reciprocal with each other. **The reciprocal pair is complete at both ends** — one of the few in
    this file that is.
  - **← nucleus reuniens** (`12_thalamus`), onto the **basal** and **basomedial (accessory basal)**
    nuclei — payload owed. Fan-in: to derive. **Two-ended**, and the same entry carries the
    hippocampal pair above. **The primate finding is that this pathway is stronger than in rat or
    mouse**, which is a species claim rather than a payload.
  - **← claustrum** (`17_insula_claustrum_habenula`) — payload owed. Fan-in: to derive.
    **Two-ended.** **The producer now carries it as a
    typed edge line** in the claustrum's Outputs slot, payload owed, fan-out to derive. **The far
    end carries it at the
    architecture rung.** *(Whether the mark holds at the source rung is unchecked;
    `17_insula_claustrum_habenula`\'s source is unchecked against this file.)*

- **Outputs.** All from the **central nucleus** unless stated. The valence-and-urgency signal —
  *this is bad (or good), act now* — **carries no identity information: what leaves is the
  significance, not the thing.**
  - **→ hypothalamus** (`14_brainstem_midbrain_hypothalamus`), via the **stria terminalis** and the
    **ventral amygdalofugal pathway** — valence and urgency, driving autonomic, endocrine and freezing
    responses. Fan-out: to derive. **Two-ended.** **The consumer types it in this file's own words** — *a
    valence and urgency signal, this is bad or good, act now*, with **no identity information** — and
    names both tracts. **It also records that neither tract has an entry anywhere**, which this line
    does not say.
  - **→ periaqueductal gray** (`14_brainstem_midbrain_hypothalamus`) — the same signal, here driving
    the defensive response. Fan-out: to derive. **Two-ended.** **The consumer types it** — *a valence and
    urgency signal, this is bad, act now*, no identity information — and names this structure's
    **central nucleus** as the producing sub-element. **Two of this entry\'s five brainstem consumers
    carry a fuller type than this end does**, which is the direction a one-file reading cannot
    anticipate: it records what it can see of the far file rather than the far file.
  - **→ locus coeruleus** (`13_neuromodulatory_systems`) — the same signal. Fan-out: to derive.
    **Two-ended.** **The consumer types it**, as *a threat / salience signal, the amygdala recruiting global
    arousal in proportion to detected threat*, and names this structure's **central nucleus** as the
    producing sub-element — which this line does not, though the Outputs heading above declares the
    central nucleus as the default. **The consumer's type is this end's payload in fuller words.**
  - **→ lateral parabrachial nucleus** (`14_brainstem_midbrain_hypothalamus`) — payload owed.
    Fan-out: to derive. **The consumer declares no such edge. Confirmed absent**: that entry
    declares three inputs — spinal lamina I, the caudal spinal trigeminal
    nucleus, and the solitary nucleus — and no forebrain source of any kind. Recorded rather than
    dropped because it is **the return limb of the affective-pain input**, and a reciprocal pair with
    one limb missing is the recurring shape here. **Owed at `14_brainstem_midbrain_hypothalamus`.**
  - **→ basal forebrain** (`13_neuromodulatory_systems`) — payload owed. Fan-out: to derive.
    **Two-ended.** **The consumer declares `← amygdala, central nucleus`
    as a named input line**, and explicitly records it as *one named member of what the class was
    standing in for*. **The class and the named edge both exist there**; this file saw only the class.
    **Payload owed at both ends, and that is the only thing still owed on this edge.**
  - **→ nucleus of the solitary tract**, descending (`14_brainstem_midbrain_hypothalamus`) — payload
    owed at both ends. Fan-out: to derive. **Two-ended.** The consumer declares
    it inside a compound — `← insula, hypothalamus and amygdala (descending)` — and marks its own
    arity: **the bullet names three producers and the split is owed there.** **So this edge is
    two-ended and the far end is one third of a line.**
  - **→ bed nucleus of the stria terminalis**, from the **basolateral** nuclei, via the stria
    terminalis and the ventral amygdalofugal pathway — the valence / threat signal. **The heaviest
    edge of the extended amygdala.** Fan-out: to derive.
  - **→ temporal pole** (`07_anterior_temporal_lobe`), from the **basal / accessory basal** nuclei —
    the **valence tag**. Fan-out: to derive. **Two-ended.** **The class is split here and this is
    the named limb**,
    attributed to the basal and accessory basal nuclei.
    **With the input limb above, the temporal pole ↔ amygdala loop is closed at both ends**.
    
  - **→ insula** and **→ midcingulate cortex** (`17_insula_claustrum_habenula`), **→ anterior
    cingulate cortex**, **→ orbitofrontal / ventromedial prefrontal cortex**, **→ right inferior
    frontal gyrus** (`11_frontal_lobe`) — the same valence tag, five edges. Fan-out: to derive.
    **The two consumers in `17_insula_claustrum_habenula` both declare
    and type it**, the insula as *a gain on perception, attention and memory encoding, carrying no
    identity information — what arrives is the significance, not the thing*, and the midcingulate as
    *the valence tag, carrying no identity information*. **Both are this end's payload returned in
    fuller words, and the far file names them among the agreements that certify something**, because
    they cross a file boundary and a date.
    **The three in `11_frontal_lobe` all three declare the edge.** The
    anterior cingulate cortex, the orbitofrontal / ventromedial prefrontal cortex and the right
    inferior frontal gyrus each carry `← the amygdala` as a named input. **All three are untyped
    there, so this end's *valence tag* is the only payload on all three wires.**
    **Two of the three are more specific than this line in the other direction, and that is the
    finding.** The orbitofrontal and right-inferior-frontal entries both write the edge as arriving
    **from the basal and accessory basal nuclei** — the attribution this entry uses on its
    temporal-pole limb and omits on this five-target line. **So the consumers name the nucleus this
    producer does not, while the producer types the payload the consumers do not.** Neither end is
    the fuller one. **Owed at the source: carry the nuclear attribution onto this line, and split it**
    — five targets in two files, and the cingulate consumer names no nucleus while the other two do.
    **The class is not fully resolved**: "feedback to sensory areas" remains a class and is unchecked.
  - **→ claustrum** — **not written as an edge, and the repair is not at this rung.**
    `17_insula_claustrum_habenula` declares `← amygdala`, onto the **ventral claustrum**, payload
    owed, and correctly records that this entry declares no such output. **Same warrant and same
    finding as the two hippocampal limbs: one sentence, one diffusion-tractography citation, no
    direction.** **Owed at `17_insula_claustrum_habenula`, not here.** **And the direction this file already
    declares is the one the tracing literature supports** — the amygdala is described there as
    projecting *to* the claustrum, which is the `← claustrum` limb's mirror and not this one.
  - **→ nucleus reuniens** (`12_thalamus`), from the **basal** and **basomedial (accessory basal)**
    nuclei — payload owed. Fan-out: to derive. **Two-ended.** **This is where this section's two
    major structures and their prefrontal target converge on one stage**: the same nucleus receives
    the hippocampal formation and medial prefrontal area 25.
  - **→ dorsolateral prefrontal cortex** (`11_frontal_lobe`), from the **intermediate and
    magnocellular divisions of the basal nucleus** — the same valence tag; payload otherwise owed.
    Fan-out: to derive. Terminations in **Brodmann area 9** medially and laterally and **patchily in
    area 46**. **The lightest and least consistent of the four lateral limbs**: the area 46 label was
    present in one hemisphere and absent in the other of the same animal. **Two-ended**, written from
    this producer.
  - **→ ventrolateral prefrontal cortex** (`11_frontal_lobe`), from the same two divisions — the same
    valence tag; payload otherwise owed. Fan-out: to derive. **The densest of the four.**
    Terminations across **area 12**, which that file resolves to **Brodmann area 47**, in deep layer
    I, layer II and layer VI, continuing dorsally into much of **Brodmann area 45**. **Two-ended.**
    **The endpoint is a sub-element claim that entry records itself unable to receive**, and it is
    the second such assignment to arrive there from a different file and a different modality.
    **And the consumer may be the wrong entry by that file's own record**: Brodmann area 45 is
    claimed by both it and the Broca's-area entry, an overlap that file marks as proposed rather than
    settled.
  - **→ premotor cortex** (`11_frontal_lobe`), from the same two divisions — the same valence tag;
    payload otherwise owed. Fan-out: to derive. Terminations in **ventral area 6**, continuous with
    the area 45 label above, and lighter label in **dorsal area 6**. **Two-ended**, written from this
    producer. **Which sub-element receives it is owed**: that entry names F2, F4 and F5, and the
    study divides area 6 dorsally and ventrally rather than by those names.
  - **→ precentral opercular cortex**, from the same two divisions — the same valence tag; payload
    otherwise owed. Fan-out: to derive. **Particularly dense**, and continuous with the area 45 and
    ventral area 6 label rather than separate from it. **This region has no entry in any file.** The
    nearest thing the source describes is the frontal operculum as half of the primary gustatory
    cortex, and the precentral opercular area is a different field from gustatory cortex in the
    parcellation this claim comes from. **Inherited gap; not patched here.**
  - **→ mediodorsal thalamus** (`12_thalamus`) — **limbic value / significance context**; payload
    otherwise owed. Fan-out: to derive. **Two-ended**, and the far end types
    it in **the same words and owes the same remainder.** **Neither end names the nucleus of origin**,
    which this entry does name on its temporal-pole and cortical limbs — so the attribution is
    available here and is not used on this edge.
  - **→ zona incerta** (`12_thalamus`), onto its parvalbumin neurons — payload owed. Fan-out: to
    derive. **Two-ended**, and both ends name the parvalbumin target.
    **The consumer attributes this edge to the central nucleus and this end names no nucleus**, so the
    far end is the more specific one — the reverse of the usual direction. It also carries a partial
    payload this end does not: *the producer's role in the pair is given as fear.* **Owed at the
    source: name the nucleus here, or establish that the far end's attribution is narrower than the
    evidence.**
  - **→ raphe nuclei** (`13_neuromodulatory_systems`) — payload owed. Fan-out: to derive.
    **Two-ended.** The consumer declares `← amygdala` and attributes it to
    this structure's **central-nucleus defence output**. **Payload owed at both ends.**
  - **→ ventral pallidum** — payload owed. Fan-out: to derive. *(`09_basal_ganglia`.)*
  - **→ ventral striatum** (`09_basal_ganglia`) — the valence tag. Fan-out: to derive.
    **Two-ended.** The consumer (`09_basal_ganglia`) declares this edge as **its own separate input
    line** rather than inside its cortical class, types it *the valence tag, a gain on perception,
    attention and memory encoding, carrying no identity information of its own*, and **records in its
    own margin why the edge sits outside the class: because this structure is not cortex and the
    class did not cover it.** The consumer's payload is the fuller of the two — it adds that the tag
    carries no identity of its own, which is what makes it a gain and not a code.
  - **→ hippocampal formation**, from the **basal / accessory basal** nuclei — the valence tag.
    Fan-out: to derive.

- **Sizing.** Basis: **per hemisphere**, verified human stereology by optical fractionator.
  **This structure's count also partitions, and it closes to three significant figures.**

  | sub-element | neurons | fan-in | bits | parameter memory |
  |---|---|---|---|---|
  | lateral nucleus | 4.00M | to derive | ≤ 16 | ≤ 8.00 MB |
  | basal nucleus | 3.24M | to derive | ≤ 16 | ≤ 6.48 MB |
  | accessory basal nucleus | 1.28M | to derive | ≤ 16 | ≤ 2.56 MB |
  | central nucleus | 0.36M | to derive | ≤ 16 | ≤ 0.72 MB |
  | remaining nuclei | 3.33M | to derive | ≤ 16 | ≤ 6.66 MB |
  | **structure total** | **12.21M** | | | **≤ 24.42 MB** |

  **Re-derived: the parts sum to 12.21M against a stated ~12.2M.** The partition is finer than the
  sub-element list, and not finer in the way the edges need — **the medial nucleus and the
  intercalated cells are both inside "remaining nuclei" and neither has a count of its own**, and
  both are edge endpoints: the lateral olfactory tract terminates on the medial nucleus and the
  intercalated cells are the source of an internal inhibitory edge. **So four of the six sub-elements
  are allocatable and two are not.**
  **The internal convergence is measured and is not written as a fan-in.** The **central nucleus is
  the smallest counted nucleus and carries the entire subcortical output** — 0.36M against the
  lateral nucleus's 4.00M, an **11.11:1** convergence across the internal edges. **That ratio is a
  constraint on the fan-in slots that currently read *to derive***, and the source records that they
  do not reflect it.

- **Shape.** **Non-laminated nucleus, rank 2: (cell class, N)** — no orderly map is recorded, so
  there is no H or W to derive and recording one would assert a map that is not described. **The cell
  class axis has extent 6 and is populated for 4.** Tangential sub-elements unknown.
  **Density cross-check, re-derived:** ~12.21M over ~1.26 cm³ is **~9,690 neurons/mm³**, closing
  against the source's ~9,700 — loose subcortical packing, below the lateral geniculate nucleus's
  ~17,000/mm³. In-vivo volume runs 1.2–1.7 cm³, so the density is soft in the same direction.

- **Edge latency.** All edges **to derive** — **and this structure is where that hurts most.** The
  entry states that the fast subcortical route and the cortical routes **carry the same event at
  different levels of description and that the architecture depends on their latency difference.**
  **Three arrival times are asserted to exist and none of the three has a number.** This is not one
  more unrecorded latency: it is a latency ordering the function is built on, stated as a requirement
  and unfilled.

- **Invariant conformance.** Co-instantiation: satisfied; the loops with the hippocampal formation
  and with the bed nucleus are both closed inside this file, and the internal lateral → basal →
  central chain plus the intercalated gate are all present. Per-edge latency: satisfied in form, all
  to derive — **and see above: the ordering the function requires is unstated.**

- **Justification (biological).** The counts carry the architecture. **A 4.00M input nucleus feeding
  a 0.36M output nucleus is an 11:1 funnel**, and what is discarded across it is identity: identity
  codes arrive at the lateral nucleus, a valence and urgency signal with no identity leaves the
  central one. **The compression ratio and the payload loss are the same fact measured two ways** —
  the structure cannot be preserving identity across an 11:1 convergence, and the entry independently
  says it does not. That is a rare case in the source where a count corroborates a payload claim.

## Bed nucleus of the stria terminalis

- **Function → structure.** The forebrain hub of the **extended amygdala**, the anatomical and
  functional partner of the central amygdala and continuous with it through the sublenticular
  extended amygdala. **Where the central amygdala drives phasic, cued fear, this structure drives
  sustained responses to unpredictable, ambiguous or diffuse threat** — the state properly called
  anxiety — continuing to shape behaviour long after the trigger is gone. The sustained mode is
  **corticotropin-releasing-factor-dependent**. A classic **sexually dimorphic** nucleus.
  **Divisional sub-elements: owed.** The structure is heterogeneous and the literature divides it into
  anterior and posterior divisions with multiple subnuclei; **none is written here.** This is *owed*
  and not *unknown* — the sub-elements are known to exist and to have been described.
  **Laminar sub-elements: not applicable** — a basal-forebrain nucleus, not cortex.
  **Cell-class sub-elements: one is named and it is load-bearing** — the
  **corticotropin-releasing-factor-expressing** population, on which the Function field makes the
  sustained mode depend. That is a claim that a cell class, and not the structure as a whole, carries
  the payload the Outputs describe. **Owed: establish whether the four output edges leave from this
  population.**
  **Sexual dimorphism is not a sub-element.** A difference between two populations' instances of one
  structure is not a division within one instance. **What is owed is whether the dimorphism changes
  any edge.**
  **Internal edges: owed, all of them.** None is described, in either direction.

- **Inputs.**
  - **← amygdala**, from the **basolateral** nuclei, via the **stria terminalis** and the ventral
    amygdalofugal pathway — the valence / threat signal. Fan-in: to derive.
  - **← hippocampal formation**, from the **subiculum** — episodic **context**; payload otherwise
    owed. Fan-in: to derive.
  - **← anterior insula** (`17_insula_claustrum_habenula`) — **interoceptive state**; payload
    otherwise owed. Fan-in: to derive. **Two-ended.** **The producer
    declares it**, as `→ bed nucleus of the stria terminalis`, **from the anterior insula** —
    attributing it to the same sub-element this end names — and types it **interoceptive state**, the
    same two words. **This is the only one of this structure\'s five
    incoming and outgoing far-end marks whose far file is checked against this one.**
  - **← ventromedial and orbital prefrontal cortex** — **regulatory control**, the same kind of signal
    that entry sends the amygdala; payload otherwise owed. Fan-in: to derive. **The producer declares
    no such edge.** *(Owed at `11_frontal_lobe`.)*
  - **← lateral parabrachial nucleus** (`14_brainstem_midbrain_hypothalamus`) — payload owed at both
    ends. Fan-in: to derive. **The same nucleus supplies the central amygdala's affective-pain input,
    so the phasic and sustained arms of the extended amygdala share a producer, and the difference
    between them cannot be a difference in this source.** **Two-ended**: that
    entry declares `→ amygdala, central nucleus` and `→ bed nucleus of the stria terminalis` as
    **separate output lines**, types the amygdalar one and leaves this one owed. **So the producer
    makes the same two-way split this file does and types only one side of it** — which is the same
    asymmetry, arriving from the other end and confirming that the difference is not stated there
    either.

- **Outputs.** All carry a **sustained threat state** — the same valence the central amygdala emits
  but **held over time and not tied to a cue**. **The payload difference between this structure and
  the central amygdala is duration and cue-binding, not content**, and that is a real distinction on
  the wire and the reason both entries exist.
  - **→ hypothalamus** (`14_brainstem_midbrain_hypothalamus`), to the **paraventricular nucleus** and
    the feeding and autonomic nuclei. Fan-out: to derive. **The consumer declares no such edge.
    Confirmed absent**: that entry declares six inputs and the only forebrain
    ones are the central amygdala, the hippocampal formation and a septal class. **Owed at
    `14_brainstem_midbrain_hypothalamus`.**
  - **→ periaqueductal gray** (`14_brainstem_midbrain_hypothalamus`). Fan-out: to derive. **The
    consumer declares no such edge. Confirmed absent**: four inputs, and the
    forebrain ones are the central amygdala and ventromedial / orbital prefrontal cortex. **Owed at
    `14_brainstem_midbrain_hypothalamus`.**
  - **→ lateral parabrachial nucleus** (`14_brainstem_midbrain_hypothalamus`) — payload otherwise
    owed. Fan-out: to derive. **The consumer declares no such edge. Confirmed absent**: that entry
    declares no forebrain input at all. **Owed at `14_brainstem_midbrain_hypothalamus`.**
    **All three of this entry's file-14 targets declare the central amygdala and not this structure**,
    which is the pattern the block below describes — now checked at every one of the three rather than
    inferred from one.
  - **→ ventral tegmental area** (`13_neuromodulatory_systems`) — a **sustained threat / defence
    state**, a persistent aversive-state signal and **not a discrete stimulus**; payload otherwise
    owed. Fan-out: to derive.
    **Two-ended, and the edge is carried under two structure names.** The consumer declares it at
    its ventral tegmental area entry as `← amygdala`. **Each end looks for its own name and does not
    find it**: this end names the bed nucleus; that end names the amygdala and takes this file to
    have declared it. **A name mismatch produces a false negative at both ends simultaneously, and
    neither end can see it alone.**
    **The consumer's own payload is the evidence that it means this structure and not the amygdala.**
    It types the edge *sustained*, *persistent*, and *not a discrete stimulus* — which is precisely
    the distinction this entry exists to carry, and which this file states as the difference between
    the central amygdala's phasic arm and this structure's sustained one. **The payload was written
    at the far end from the far end's source and it lands on this entry, not the one it names.**
    **Owed at `13_neuromodulatory_systems`: rename the endpoint to the bed nucleus of the stria
    terminalis**, or state that the projection arises from both and is one edge at a coarse grain.
  - **"Brainstem autonomic and neuromodulatory centres" is a class and does not resolve to a named
    structure, so it is not written as an edge here.** **Owed: name them.**
    **One member has now been located, and it was pointing back..**
    `14_brainstem_midbrain_hypothalamus`'s **rostromedial tegmental nucleus** declares
    `← extended amygdala, lateral septum, and periaqueductal grey`, payload owed, typed as
    aversion-related and defensive-state input. ***Extended amygdala* is the term this file uses for
    the central amygdala and this structure together**, so that endpoint names this entry, the amygdala
    entry, or both — and it is unstemmed there.
    **The two class endpoints are each other's missing far end.** This one names a class of brainstem
    consumers and resolves to none; that one names a class of forebrain producers and resolves to
    none; **and each is a member of the other's class.** Neither file could see it, because on both
    sides the far end is hidden inside a class name rather than absent.
    **Owed at both sources, and the two repairs are one question**: whether the aversive drive to the
    rostromedial tegmental nucleus arises from this structure, from the central amygdala, or from both.
    **Answering it names a member of this class and splits that endpoint at the same time.**

  **Three of the four declared output far ends are undeclared at the other end, and that is a finding
  about this entry rather than about three other files.** Every one of this structure's targets is also
  a target of the central amygdala, and those three declare the central amygdala and not this.
  **The fourth is not among them.** The ventral tegmental area **does** declare this edge, under the
  name *amygdala*, and types it with this structure's own signature — sustained, persistent, not
  discrete.
  **So the sustained arm reaches at least one declared far end, and the finding is not that it is
  better connected than recorded.** It is that **a structure-name mismatch can hide an edge from both
  sides at once**, and that a count of undeclared far ends is only as good as the names it was counted
  under.
  **Owed: the other three checked the same way** — `14_brainstem_midbrain_hypothalamus` holds all of
  them, and a mismatch of the same shape is available there, since the central amygdala is the name
  each of them carries.
  The alternative the source raises is not idle: the two structures are described as continuous
  through the sublenticular extended amygdala, and **a continuous structure may not have two
  separable projections to divide.**

- **Sizing.** Basis: **per hemisphere.** **Neurons: to derive.** No clean human control count is
  recorded — human work reports volumes and sex differences rather than an absolute. **Parameter
  memory: to derive.** Synapses unknown; axons are the stria terminalis and the ventral
  amygdalofugal pathway, counts unknown, **the same two pathways the amygdala names**, which is
  consistent with the continuity claim and is not evidence for it.

- **Shape.** **Non-laminated nucleus, rank 2: (cell class, N)** — **and no axis has an extent.** The
  cell-class axis has one member named, the corticotropin-releasing-factor population, and no count;
  N is to derive. Grey-matter volume is small — sub-cm³ — with no single verified human figure, so
  **no density cross-check can be run and this is the one structure in the section with no
  independent arithmetic available at all.**

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: satisfied for the loop with the amygdala, which is
  closed inside this file, and for the input from the hippocampal formation. **Internally
  unstatable** — no internal edge is described, so there is nothing to co-instantiate below the
  structure level. Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** The distinction this structure exists to carry is **temporal, not
  representational**: phasic and cued at the central amygdala, sustained and diffuse here, and the
  dissociation is supported by the two responses depending on different structures and by human
  imaging reproducing the split. **Its defining property is a time constant rather than a content
  type** — and the architecture records
  no time constant for it anywhere. The sustained state is measured in behaviour and unmeasured on
  any edge, which is the same gap the per-edge-latency invariant records, arriving here as the
  structure's whole identity rather than as a missing number on a wire.

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Hippocampal formation — dentate gyrus | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB |
| Hippocampal formation — CA3 | per hemisphere | ~2.5M | 13–14 | 4.06–4.38 MB |
| Hippocampal formation — CA1 | per hemisphere | ~16M | ≤ 16 | ≤ 32.00 MB |
| Hippocampal formation — subiculum | per hemisphere | ~4M | ≤ 16 | ≤ 8.00 MB |
| Hippocampal formation — entorhinal cortex | per hemisphere | ~6M | ≤ 16 | ≤ 12.00 MB |
| Amygdala | per hemisphere | 12.21M | ≤ 16 | ≤ 24.42 MB |
| Bed nucleus of the stria terminalis | per hemisphere | to derive | ≤ 16 | to derive |
| **stated total** | per hemisphere | **~55.7M** | | **110.48–110.80 MB** |

**The total is a floor.** One of three structures is uncounted, and every fan-in but CA3's sits at
the 16-bit ceiling rather than at a measured value. **State memory and edge storage are not in this
table**, and edge storage cannot be sized until the scheduling discipline is set, which it is not.

**Two of the three structures partition to their sub-elements and the partitions close.**
`01_visual_pathway` carries one closed
partition in eight structures and `07_anterior_temporal_lobe` none.
**It is what makes sub-element arrays allocatable in this section** — for
nine of the eleven sub-elements that have counts, the two exceptions being the amygdala's medial
nucleus and intercalated cells, which sit inside an aggregated remainder and are both edge endpoints.

**Memory is not a binding constraint here and the figure is not to be reduced.** It is a derived
requirement recorded as found.
