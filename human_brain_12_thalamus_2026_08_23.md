# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-23
---

---

# FILE 12 OF 20 — THALAMUS

**What is in this file.** The thalamic nuclei that are not first-order sensory relays, plus the one first-order relay whose cortical target is described later: mediodorsal, pulvinar, the posterior / ventromedial-posterior interoceptive relay, the motor ventral anterior / ventral lateral group, the anterior nuclei, the intralaminar nuclei, the nucleus reuniens of the midline group, the thalamic reticular nucleus, and the zona incerta.

**Size:** 1192 lines, ~25.1k tokens / ~98 kB (estimated from bytes, not tokenised; kB = 1024 bytes, truncated). **Entries:** 9. **Edge lines:** 88 — 39 in, 49 out. **Internal structure slots:** 9 of 9. **Reference keys:** 38, over 46 mentions.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Mediodorsal nucleus — the prefrontal relay**
- **Pulvinar — the large visual / associative nucleus**
- **Posterior / ventromedial-posterior thalamus (posterior nuclear group) — the interoceptive relay**
- **Ventral anterior / ventral lateral nuclei — the motor relay**
- **Anterior nuclei — the limbic / memory relay**
- **Intralaminar nuclei (centromedian / parafascicular) — arousal + striatal drive**
- **Nucleus reuniens — the midline hippocampal–prefrontal conduit**
- **Thalamic reticular nucleus — the inhibitory gate**
- **Zona incerta — the subthalamic inhibitory hub (ventral diencephalon / subthalamus)**

---

# THALAMUS (higher-order, motor, limbic, and gating nuclei)

*The thalamus is the cortical relay hub — nearly every cortical area has a paired thalamic
nucleus, and cortico-thalamo-cortical (transthalamic) routing runs alongside direct
cortico-cortical connections. Three of the four first-order **sensory relays are already
described in their pathways**: the lateral geniculate nucleus (vision), the medial
geniculate nucleus (audition), the ventral posterior complex (discriminative
somatosensation). The fourth — the **posterior / ventromedial-posterior** relay carrying
the lamina-I
interoceptive stream to the insula — is described **here**, because unlike the other three its
cortical target (the insula) is described later, so there is no earlier pathway section to hold
it. Beyond the relays, this section covers
the higher-order, motor, limbic, and gating nuclei the cortical loops above depend on.
Thalamic neuron density is low (~1–1.8×10⁴/mm³ — the loose subcortical packing of the
lateral and medial geniculate nuclei),
and clean human control counts live mainly in the Pakkenberg / Dorph-Petersen stereology
lineage (much of it framed against schizophrenia); per-nucleus entries below are
volume-verified with order-estimate, soft neuron counts. Appended at the end is the adjacent
**zona incerta** — subthalamus, not thalamus, but grouped here as the *extrathalamic*
gamma-aminobutyric-acid-releasing (GABAergic) gate on the higher-order thalamus, the
companion to the intrinsic thalamic reticular gate.*

## Mediodorsal nucleus — the prefrontal relay

- **Function:** the higher-order relay for prefrontal cortex — reciprocal with the whole of it
  (dorsolateral, ventrolateral and orbitofrontal), supporting working memory, executive
  control, and value/limbic processing. A cognitive gateway, not a sensory relay. Its defining
  property, and the reason it is not a relay in the payload sense at all: it **does not relay
  categorical content to the cortex.** Silencing it does not stop the prefrontal cortex from
  receiving task information; it stops that cortex from *holding* it. What this nucleus
  supplies is amplification of the cortex's own recurrent dynamics —
  a gain applied to a cortical loop, not a message carried on a wire.
- **Inputs:**
  - **← the internal globus pallidus** and **← the substantia nigra pars reticulata** (the
    associative and limbic basal-ganglia output) — **carries:** tonic
    inhibition, selectively released — a gate on which prefrontal loops may proceed, not a
    positive content signal (the same negative payload the basal-ganglia output carries at all
    its thalamic targets). **Fan-in:** unknown. **The producer declares this edge and names both
    source nuclei** (file 9), which is where the two names come from.
  - **← the amygdala** — **carries:** limbic value / significance context. **Payload otherwise
    unknown — owed. Fan-in:** unknown. **The producer declares it** (file 8, from this
    entry's own declaration), so this edge is two-ended.
    *(Caution under §4: both ends descend from the same sentence at this end, so the agreement
    certifies nothing. It is two-ended in form, not yet in evidence.)*
  - **← olfactory / limbic cortex** — **carries:** limbic value / significance context. **Payload
    otherwise unknown — owed. Fan-in:** unknown. **This endpoint names a class, not a region with
    an entry of its own**, and cannot be checked as written. **Owed: resolve it to named
    producers.**
  - **← prefrontal cortex (layer 6, reciprocal), the modulator** — **carries:** no
    receptive-field content; corticothalamic feedback. **Fan-in:** unknown. **This endpoint names a
    class.** The five prefrontal entries in file 11 that declare this nucleus as an input are named
    at Outputs below; whether all five also send the layer-6 modulator limb is **not stated at
    either end. Owed.**
  - **← prefrontal cortex (layer 5, the driver)** — **carries:** the cortical driver signal that
    makes this nucleus a higher-order (cortically-driven) nucleus rather than a first-order
    sensory relay. A subset of its relay cells instead have subcortical drivers. **Fan-in:** unknown.
    **Same class endpoint as the line above, and the same owed resolution.**
    *(The driver / subcortical-driver split: Class 3 — general thalamic anatomy, Sherman &
    Guillery. **Unverified: the key reads owed in the reference section — no source has been
    opened for it**, and a textbook attribution is recall until the text is. The layer-5-vs-layer-6
    driver/modulator identity of the corticothalamic inputs is not separately measured here —
    owed.)*
- **Outputs:**
  - **→ the frontal eye fields** — **carries:** **no categorical content.** A **modulatory
    amplification** — it raises the gain of the consumer's local recurrent connectivity, sustaining
    rule and working-memory representations that are generated in, and belong to, the cortex.
    **Fan-out:** unknown. **The consumer declares it** (file 11).
  - **→ the dorsolateral prefrontal cortex** — **carries:** the same modulatory amplification.
    **Fan-out:** unknown. **The consumer declares it** (file 11).
  - **→ the ventrolateral prefrontal cortex** — **carries:** the same modulatory amplification.
    **Fan-out:** unknown. **The consumer declares it** (file 11).
  - **→ the orbitofrontal / ventromedial prefrontal cortex** — **carries:** the same modulatory
    amplification. **Fan-out:** unknown. **The consumer declares it** (file 11), which also
    declares a separate limbic limb reaching it **via the ventral pallidum → this nucleus**.
  - **→ the frontopolar cortex** — **carries:** the same modulatory amplification. **Fan-out:**
    unknown. **The consumer declares it** (file 11), and marks its own copy as inherited from this
    entry's output declaration.
    *(The five named consumers answer what would otherwise be the class endpoint "prefrontal
    cortex (all divisions)" under §9b; all five declare the edge in file 11. Class 1 —
    "amplifies local connectivity, sustains representations without relaying
    categorical information, scaffold not source": Schmitt / Halassa et al., Nature 2017,
    optogenetic silencing with prefrontal electrophysiology, mouse; the principle is taken as
    general to the mediodorsal–prefrontal loop, **verified against the journal record 2026-08-12**.
    The framing as amplification-and-modulation rather than a content payload is Class 2 — a reading
    placed on that measurement, not a second measurement.
    **Whether the five consumers receive
    the same amplification or differently-tuned ones is not stated at either end — owed.**)*
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only** — that entry's Inputs take "collaterals of cortico-thalamic and thalamo-cortical
    axons" as a class covering every thalamic nucleus including this one, and the
    class at the far end is **owed** there.
- **Internal structure and internal data flow:** **unknown.** The magnocellular, parvocellular and
  densocellular divisions are named in the literature this entry's number slots draw on
  (Dorph-Petersen, Byne, Popken), but no sub-element set and no internal edges are described in the
  material read for this entry. **Owed: name the divisions and say which prefrontal consumer each
  reaches** — the five named outputs above make that a checkable question rather than an open one.
- **The gating question, at the mediodorsal nucleus.** This nucleus is the far end of the
  per-area split the first-order relays opened. Where the lateral geniculate nucleus gates the
  *passage* of a content it relays, this nucleus relays no
  content and instead *amplifies* a cortical loop. Both scale a signal; the difference is what is
  scaled — a through-payload at the lateral geniculate nucleus, a cortical recurrence here. So
  a learning rule written
  for it is not about content and not about passage: it is about the amplification's setting.
  *(Class 2 — the three-way lateral geniculate / pulvinar / mediodorsal framing is Claude's
  synthesis, offered to be
  checked. The per-area conclusion is Micky's standing position, which makes it **instruction about
  how this source treats gating** rather than a claim about the brain — and so it verifies against
  him and needs no literature. **Where it is read as a claim about the brain instead, it is
  unverified.**)*
- **Neurons:** order ~10M per side (soft — volume × low thalamic density). Human control
  stereology exists (Dorph-Petersen et al. 2004), but its counts vary substantially study to
  study (the Pakkenberg / Byne / Popken lineages), so no single figure is pinned here.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** ~680–990 mm³ (Byne 2001; Danos 2003; Kemether 2003).
- **White-matter volume:** unknown.
- **Myelination:** unknown.

## Pulvinar — the large visual / associative nucleus

- **Function:** the largest thalamic nucleus — higher-order visual and attentional processing,
  and transthalamic routing among visual, parietal, and temporal cortex (a
  cortico-pulvinar-cortico relay that helps synchronize and bind across areas). Central to
  selective visual attention. It sits **between** the lateral geniculate nucleus and a
  content-transformer: unlike that
  nucleus it has cortex-like selective units of its own (orientation, direction, motion — measured
  directly in primate pulvinar), but unlike a cortical area its output content largely *reflects*
  its cortical driver rather than building a representation the cortex lacks. What it adds on top
  of that reflected content is *coordination* — attentional gain and cross-areal synchrony.
- **Inputs:**
  - **← visual cortex, layer 5 (V1 and higher visual areas), the driver** — **carries:** a
    feedforward cortical visual signal — the driver that sets the pulvinar cell's receptive
    field. **Fan-in:** unknown. **This endpoint names a class** — "V1 and higher visual areas" —
    and cannot be checked as written. **Owed: resolve it to named producers in files 1 and 4.**
  - **← the superior colliculus** (subdivision-specific), an ascending driver to part of the
    nucleus — **carries:** a collicular visual signal (retinotopic salience / motion), on the
    colliculo-pulvinar-cortical route parallel to the geniculostriate one. **Fan-in:** unknown.
    **The producer declares it** (file 14), from its intermediate and deep layers.
  - **← visual cortex, layer 6, the modulator** — **carries:** no receptive-field content; sets
    response gain and frequency. **Fan-in:** unknown. **Same class endpoint as the driver line
    above, and the same owed resolution.**
  - **← the thalamic reticular nucleus** — **carries:** inhibitory
    gating of specific transthalamic pathways; no content. **Fan-in:** unknown. **The producer is
    in this file** and declares this nucleus among its named consumers.
  - **← long-range inhibitory sources other than the thalamic reticular nucleus** — **carries:**
    inhibition; no content. **Fan-in:** unknown. **This endpoint names a class.** The zona incerta
    entry in this file declares an incerto-thalamic projection whose signature target is the
    higher-order thalamus, and may be one of these sources; **whether it reaches this nucleus is
    not stated at either end. Owed.**
    *(Input laminar / driver-modulator identities: Class 3 general thalamic anatomy plus Class 1
    mouse rabies tracing (Journal of Neuroscience 2025). **Unverified: the key reads owed in the
    reference section — no source has been opened for it.**)*
- **Outputs:**
  - **→ V4** — **carries:** two things on the same wire. **(a) A
    visual signal that largely reflects its cortical driver's content** — selective (orientation
    / direction / motion) but not a new representation the cortex lacks. **(b) A coordinating
    payload** — attentional gain and cross-areal synchrony (alpha / low-beta and gamma) that
    binds the areas it connects. **Fan-out:** unknown. **The consumer declares it** (file 1) and
    marks its own payload **owed**, naming contextual and state-dependent modulation as a
    candidate — **a payload disagreement with this end, which types it. Owed at file 1: adopt the
    producer's declaration or say why not.**
  - **→ the middle temporal area** — **carries:** the same two-part payload. **Fan-out:**
    unknown. **The consumer declares it** (file 4), citing this entry's own declaration, and
    separately declares a di-synaptic superior-colliculus route through this nucleus whose payload
    it marks **owed**.
  - **→ the lateral intraparietal area** — **carries:** the same two-part payload. **Fan-out:**
    unknown. **The consumer declares it** (file 4), citing this entry's declaration.
  - **→ the second somatosensory area, with the parietal ventral and ventral somatosensory areas**,
    from the **anterior pulvinar** — **carries:** the consumer declares **deep-receptor** signals on
    this edge, which is **not** the two-part visual/coordinating payload this entry declares for its
    other targets. **Fan-out:** unknown. **A payload disagreement, recorded not resolved:** this
    entry describes a visual/associative nucleus and the anterior pulvinar is a non-visual
    subdivision, so the two declarations may both be right about different sub-elements. **Owed:
    name the subdivisions in Internal structure and assign each output edge to one** (file 5 holds
    the far end).
  - **→ further visual, parietal and temporal cortical areas beyond the four named above** —
    **carries:** the same two-part payload. **Fan-out:** each pulvinar cell → input layers of ~2–3
    cortical areas (Class 1, mouse — the primate count is not pinned here). **This endpoint names a
    class**, and is the residue of the class line the four named edges were split out of. **Owed:
    resolve it, or delete it if the named four exhaust it** — files 2, 6 and 7 were not read this
    pass and may hold consumers.
    *(Class 1 for the primate selectivity (single-unit recordings, Petersen / Robinson rhesus,
    Gattass, cebus). **The two causal keys are different methods and are separated here:**
    *Zhou 2016* is a reversible muscimol deactivation in the awake macaque; *Saalmann 2012* is
    correlational recording with connectivity mapping and **inactivates nothing**, so it supports
    the synchrony and inter-areal coherence claim and not a silencing one. **Class 2 for the
    two-part "reflects content + adds coordination" framing — Claude's synthesis, and it is now
    contested by its own strongest key.** Zhou 2016 reports that pulvinar deactivation *reduced*
    sensory-evoked responses and gamma coherence within V4 and produced severe behavioural
    deficits, concluding that the pulvinar is necessary for normal sensory processing as well as
    for attention — **so cortical responses are not left intact, and the "reflects, does not
    build" half of the framing does not follow from it. Owed: re-state the framing against the
    paper, or withdraw it.** Targets reciprocal, onto layer 4 and the input layers.)*
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input.
- **Internal structure and internal data flow:** **owed.** The subdivisions are named in this
  file's own material — an **anterior pulvinar** is named at the output edge to the second
  somatosensory area, and the medial, lateral and inferior divisions are standard in the
  literature the number slots draw on — but no sub-element set and no internal edges are written.
  **This slot is load-bearing here rather than cosmetic**, because two of this entry's output
  edges declare different payloads (visual/coordinating versus deep-receptor) and the most likely
  reconciliation is that they leave from different subdivisions.
- **The gating question, at the pulvinar.** Neither a first-order gate nor a content-transformer.
  Because its output content substantially mirrors its cortical driver, the pulvinar is not the
  clean "payload changes, therefore content-learning" case the higher-order nuclei were suspected
  to be; but because it adds a genuine coordinating payload (cross-areal gain and synchrony) that
  the lateral geniculate nucleus's simple passage-gate does not, it is not gate-only either.
  Whether the coordinating
  role is something the pulvinar *learns about* is exactly the per-area judgment reserved to
  Micky. *(Class 2 — synthesis, offered to be checked.)*
- **Neurons:** order ~13–26M per side (soft — density-derived).
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** ~840–1640 mm³ (~2× the mediodorsal nucleus).
- **White-matter volume:** unknown.
- **Myelination:** unknown.

## Posterior / ventromedial-posterior thalamus (posterior nuclear group) — the interoceptive relay

- **Function:** the thalamic relay for the body's **physiological condition** — the fourth
  first-order sensory relay, carrying the **lamina-I spinothalamic and trigeminothalamic**
  stream (pain, temperature, itch, visceral and cardiorespiratory sensation, air hunger,
  sensual touch, muscle and vasomotor state) up to the **dorsal posterior insula**, which is
  primary interoceptive cortex. It is **distinct from the ventral posterior relay**: the
  body's two ascending
  streams stay separate at the thalamus — the discriminative dorsal-column stream relaying
  through the ventral posterior complex onto primary somatosensory cortex, the lamina-I
  interoceptive stream relaying through this territory onto insular cortex — and their
  topographies differ (this territory antero-posterior, head-to-foot, with trigeminal input
  anterior and lumbar posterior; the ventral posterior complex medio-lateral). In the human
  thalamus the
  region is identified by a dense plexus of **calbindin-immunoreactive** fibres coinciding with
  a distinct field of small-to-medium round / oval cells clustered between cell-sparse zones
  (Blomqvist, Zhang & Craig 2000, the primary human cytoarchitectonic / immunohistochemical
  description); bursts of **calcitonin-gene-related-peptide**-immunoreactive terminals (the
  vagal / solitary /
  parabrachial visceral afferents) are intercalated between the calbindin clusters with little
  overlap — two closely related but separate interoceptive termination fields. The
  calbindin-negative band separating it from the ventral posterior lateral and ventral
  posterior medial nuclei is the posterior nucleus proper.
- **Contested — recorded, not resolved.** Whether this territory is a *distinct nucleus* is
  genuinely disputed, and the dispute is part of the finding. Craig and colleagues (macaque
  anterograde / retrograde tracing plus microelectrode recording; Craig 2004, Craig & Zhang
  2006) hold that lamina-I terminations concentrate in a cytoarchitectonically separate
  ventromedial-posterior nucleus
  that is the near-exclusive lamina-I target and projects topographically to dorsal posterior
  insula. Willis and colleagues (2001/2002), Ralston (2003), and Graziano & Jones (2004) hold
  that classical thalamic anatomy already assigned this territory to the **posterior
  nuclear group**, and that lamina-I fibres also terminate in the ventral posterior lateral
  and ventral posterior inferior nuclei, and in the mediodorsal and intralaminar nuclei,
  rather than in one dedicated relay; rebuttals and counter-evidence have
  been published on the Craig side. Independent of the naming question, the **data flow is not
  in dispute**: a lamina-I spinothalamic stream ascends through posterior thalamus and reaches
  the posterior insula. This document records the pathway and leaves the nucleus question open —
  the borders themselves are indistinct (the region reads as a poorly outlined area rather than
  a circumscribed nucleus), which is also why its number slots stay blank.
- **Inputs:**
  - **← spinal cord grey matter, lamina I** (crossed anterolateral / spinothalamic system) and
    **← the caudal spinal trigeminal nucleus** (trigeminothalamic, for the face) — **carries:**
    **not one payload but three labelled lines**, distinguishable by cell morphology, by response
    class, and by conduction velocity:
    **nociceptive-specific** — fusiform cells, responding only to pinch and/or heat;
    **thermoreceptive-specific** — pyramidal cells, responding only to innocuous cooling (a warming
    class is also reported);
    **polymodal nociceptive** — multipolar cells, responding to heat, pinch and cold.
    The morphology–physiology correspondence is near-total in the material, and the exception is
    the multipolar class: **all 12 fusiform cells were nociceptive-specific; all 11 pyramidal cells
    were thermoreceptive-specific; of 10 multipolar cells six were polymodal and four
    nociceptive-specific**, with five unclassified cells consistent with the pattern.
    A **pruriceptive** (itch) population responding differentially to histamine and cowage is
    reported within the nociceptive group — **this claim carries no key. Owed: cite it, or drop
    it.** **Fan-in:** unknown.
    **Latency, measured — one of the few real time figures in this file.** Mean central conduction
    latencies differ by class: **thermoreceptive-specific ≈ 59 ms** (standard deviation 25,
    n = 136), **polymodal nociceptive ≈ 72 ms** (standard deviation 28, n = 128),
    **nociceptive-specific ≈ 131 ms** (standard deviation 56, n = 100). So the three lines do
    not arrive together, and the cold signal precedes the nociceptive one by roughly 70 ms.
    *(Class 1 — morphology/physiology: Han, Zhang & Craig, Nature Neuroscience 1:218, 1998, cat,
    intracellular recording and labelling of 38 lamina I neurons. Latencies and response classes:
    Craig, Krout & Andrew, Journal of Neurophysiology 86:1459, 2001, cat, antidromically
    identified spinothalamic neurons with quantitative thermal and mechanical stimuli.
    **Primate work reaches only the morphology, not the physiology:** Journal of Neuroscience
    17:3274, 1997, monkey, recognises the three **morphological** types in the primate and reports
    **greater variation than in the cat, with more subtypes noted** — so it is not a confirmation
    that the three **response** classes carry over. Dostrovsky & Craig 1996 is named alongside it
    and reads **owed**.
    **Species: cat for the numbers**, and the morphology–physiology correspondence above is cat
    work whose primate counterpart is looser. Of the four keys on this line, three are searched to a
    full reference and one reads **owed** in the reference section.)*
    **The three lines do not all go to the same place.** Antidromic mapping of lamina I
    trigeminothalamic and spinothalamic cells to three thalamic targets found that **nearly all
    thermoreceptive cells project to the dorsomedial part of the ventral posterior medial nucleus,
    and almost no nociceptive cells do** — 20 of 23 thermoreceptive cells versus 1 of 9
    nociceptive-specific and 0 of 8 polymodal. Both classes reach the ventral aspect of the
    ventroposterior complex and the submedius nucleus. **Temperature and pain therefore separate at
    the thalamus rather than travelling as one "pain and temperature" payload**, and an edge
    declaring them as a single stream is under-specified.
    *(Class 1 — Craig & Dostrovsky, Journal of Neurophysiology 86:856, 2001, cat, antidromic
    activation mapping of 40 lamina I projection cells. Candidate.)*
  - **← the vagal / solitary / parabrachial visceral line** — **carries:** visceral and
    cardiorespiratory state. Its terminals are **calcitonin-gene-related-peptide immunoreactive**
    and are **intercalated between the calbindin clusters with little overlap**, so this is a
    second interoceptive termination field rather than a convergent input onto the same cells.
    **Payload otherwise unknown — owed.** **Fan-in:** unknown.
    *(Class 1 — Blomqvist, Zhang & Craig, Brain 123:601, 2000, human thalamus, cytoarchitecture and
    immunohistochemistry. Candidate.)*
  - **← the insula** (corticothalamic feedback) — **carries:** no stimulus content; the
    driver/modulator gate declared at the lateral geniculate nucleus. **Fan-in:** unknown.
  - **← thalamic reticular nucleus** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-in:** unknown. **The producer is in this file** and declares this nucleus among its named
    consumers.
  - **← zona incerta** (incerto-thalamic GABAergic projection, whose signature target is precisely
    this higher-order posterior thalamus) — **carries:** inhibition, no content. **Payload
    otherwise unknown — owed.** **Fan-in:** unknown. **The producer is in this file** and declares
    this territory as its signature thalamic target.
- **Outputs:**
  - **→ the dorsal posterior insula** — **carries:** the body's physiological condition, **somatotopically
    ordered** — this territory's topography runs antero-posterior, head-to-foot, with trigeminal
    input anterior and lumbar posterior, which is a different axis from the ventral posterior
    complex's medio-lateral map. Whether the three labelled lines above stay separate on this edge
    or are merged here is **owed**. **Fan-out:** unknown.
  - **→ area 3a** (a reported lesser projection) — **payload unknown — owed.** **Fan-out:** unknown.
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this territory's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input.
- **Internal structure and internal data flow:** two termination fields that do not overlap — a
  **calbindin-immunoreactive** field of small-to-medium round and oval cells clustered between
  cell-sparse zones, receiving the lamina-I stream, and a **calcitonin-gene-related-peptide** field
  intercalated between those clusters, receiving the vagal / solitary / parabrachial visceral line.
  The calbindin-negative band separating this territory from the ventral posterior lateral and
  medial nuclei is the posterior nucleus proper.
  - **Internal edge — none typed.** No internal transfer between the two fields is described in the
    material read for this entry, and their reported near-non-overlap is a reason to expect none;
    but absence of a described edge is not evidence of absence. **Owed.**
  *(Class 1 — Blomqvist, Zhang & Craig, Brain 123:601, 2000, human. Class 2 — the inference that
  non-overlap argues against an internal edge is Claude's. Candidate.)*
- **Neurons:** unknown — no clean human count; the region's contested and indistinct borders
  make an unbiased whole-structure figure unavailable, as with the extrastriate V3 / V3A tier.
  Thalamic packing (~1–1.8×10⁴/mm³) applies if a volume is ever pinned.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown — no verified human figure recorded (the human work
  characterises the field cytoarchitectonically and immunohistochemically rather than
  volumetrically).
- **White-matter volume:** unknown.
- **Myelination:** unknown.

## Ventral anterior / ventral lateral nuclei — the motor relay

- **Function:** the motor relay — carries basal-ganglia (internal globus pallidus /
  substantia nigra pars reticulata) and cerebellar (dentate) output up to motor, premotor,
  and supplementary motor cortex, closing the two great motor loops. The ventral lateral
  nucleus is the cerebellar-recipient, the ventral anterior the pallidal-recipient (with
  overlap).
- **Inputs:**
  - **← the internal globus pallidus** and **← the substantia nigra pars reticulata** —
    **carries:** **tonic inhibition, selectively released.** The payload is a *negative*: the
    output nuclei fire constantly and the selected action is the one whose inhibition **pauses**.
    Nothing here carries the action itself — the action lives in cortex, and this line only says
    *which one is allowed to proceed*. A consumer that expects a positive command on this edge has
    misread the structure. **Fan-in:** unknown. **The producer declares it and names both source
    nuclei** (file 9).
  - **← the deep cerebellar nuclei, chiefly the dentate** (via the superior cerebellar peduncle,
    decussating) — **carries:** the cerebellar **correction** — the forward-model error correction
    that shapes an action already selected. **Fan-in:** unknown. **Fan-out at the producer:** the
    cerebellar-cortex to output-nucleus areal ratio is **~85 : 1**, a massive convergence. **The
    producer declares it** (file 10). **Because both the corticopontine input and this output cross, each cerebellar
    hemisphere serves the contralateral cortex and the ipsilateral body.**
  - **← the primary motor cortex** (corticothalamic, reciprocal) — **carries:** payload **owed** at
    both ends. **Fan-in:** unknown. **The producer declares it** (file 5).
  - **← the thalamic reticular nucleus** — **carries:** inhibition; a gain/gate control, no
    content. **Fan-in:** unknown. **The producer is in this file** and declares this nucleus among
    its named consumers.
- **Outputs:**
  - **→ the primary motor cortex** — **carries:** the basal-ganglia *selection* (which action is
    released) and the cerebellar *correction* (how it is shaped), **combined on one relay.**
    **Fan-out:** unknown. **The consumer declares it and types it** (file 5).
  - **→ the premotor cortex and the supplementary motor areas** — **carries:** the same combined
    selection-and-correction payload. **Fan-out:** unknown. **The consumer declares it and types
    it** (file 11).
  - **→ prefrontal cortex** — **carries:** payload **owed. Fan-out:** unknown. **This endpoint
    names a class.** File 10 declares the cerebellar limb of this relay as reaching "motor,
    premotor and prefrontal cortex," and no prefrontal entry in file 11 declares this nucleus as an
    input — the five that declare a thalamic input name the **mediodorsal** nucleus instead.
    **So either this limb is missing at its consumers or it does not exist. Owed, and it is the
    load-bearing gap in this entry**, because it decides whether the cerebellar loop reaches
    prefrontal cortex at all.
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input.
- **Internal structure and internal data flow:** **owed.** Two sub-elements are named in this
  entry's own Function slot — **ventral lateral**, the cerebellar-recipient, and **ventral
  anterior**, the pallidal-recipient, "with overlap" — but no internal edges are written and the
  input and output edges above are typed at the level of the combined nucleus rather than assigned
  to one division or the other. **This matters for the payload rather than the anatomy:** the
  output edges declare selection and correction *combined on one relay*, and whether that combining
  happens by convergence onto shared cells or by two segregated channels leaving side by side is
  exactly what the sub-element assignment would settle. The literature's "with overlap" is the
  contested part and is recorded as contested, not resolved.
- **Neurons:** unknown — soft; no clean human per-nucleus count recorded. Thalamic packing
  (~1–1.8×10⁴/mm³) applies if a volume is pinned.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.

## Anterior nuclei — the limbic / memory relay

- **Function:** the memory relay of the Papez circuit — mammillary bodies → anterior thalamus
  → cingulate / retrosplenial cortex; supports episodic memory and spatial orientation.
- **Inputs:**
  - **← the mammillary bodies**, via the **mammillothalamic tract** — **carries:** payload
    **owed. Fan-in:** unknown. **The producer has an entry in file 14** (hypothalamus), which names
    the Papez limb; whether it declares this edge with a payload is **unverified at that end. Owed
    as a cross-file check at file 14.**
  - **← the subiculum**, via the **post-commissural fornix** — **carries:** a **completed
    episode** — the bound, retrievable pattern, addressable by any fragment of itself. **Payload
    only partly writable — owed:** "an episode" has no units and no frame, and what makes it
    checkable is a property rather than a type — it is **content-addressable**, which the upstream
    identity codes are not. **Fan-in:** unknown. **The producer declares it and types it** (file 8),
    which names the mammillary bodies and this nucleus together on one edge.
  - **← the retrosplenial cortex** (the return limb of the Papez loop) — **carries:** payload
    **owed. Fan-in:** unknown. **The producer declares it and names this nucleus** (file 17), whose
    retrosplenial entry writes a return projection to "the anterior thalamic nuclei" and records
    that this end does not carry it. **Written here from the producer's declaration, which
    discharges that owed edit; the payload is owed at both ends.**
  - **← the thalamic reticular nucleus** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-in:** unknown. **The producer is in this file** and names this nucleus among its
    consumers, while recording that this end did not declare the input. **Written here from that
    declaration.** *(Caution under §4: both ends now sit in one file, so the agreement certifies
    nothing on its own. The producer's own line records the pair as owed against the literature,
    and that mark stands.)*
- **Outputs:**
  - **→ the retrosplenial cortex** — **carries:** payload **owed. Fan-out:** unknown. **The
    consumer declares it** (file 17), naming this nucleus as the anterior-thalamus limb of the
    Papez circuit; its return arm is the retrosplenial input above.
  - **→ the anterior cingulate cortex** — **carries:** payload **owed. Fan-out:** unknown. **The
    consumer is in file 11**, whose anterior cingulate entry declares a thalamic input from the
    **midline / intralaminar** thalamus and **not** from this nucleus. **So this edge is declared at
    one end only, and the cingulate half of the classical Papez target is unconfirmed at its
    consumer. Owed as a cross-file edit at file 11.**
  - **→ the posterior cingulate cortex** — **carries:** payload **owed. Fan-out:** unknown. **The
    consumer declares it** (file 17), whose posterior cingulate entry takes an input from "the
    anterior thalamus" and records that this end declared no such edge. **Written here from the
    consumer's declaration, which discharges that owed edit.** **This is the third cingulate /
    retrosplenial target of this nucleus and the last of the classical limbic-thalamic projection
    to be written; the payload is owed at both ends of all three.**
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input.
- **Internal structure and internal data flow:** **unknown.** The anterodorsal, anteroventral and
  anteromedial nuclei are the standard divisions and are not named in the material read for this
  entry, and no internal edges are described. **Owed.** *(The head-direction signal the
  retrosplenial consumer describes is classically carried by one of these divisions rather than by
  the group; naming them is what would let that be written as an edge.)*
- **Neurons:** unknown — soft; anterior-nucleus counts have been consistently normal
  across schizophrenia stereology, per Dorph-Petersen's review, but no control figure is pinned
  here.
- **Synapses:** unknown.
- **Axons:** the mammillothalamic tract and the fornix limb reaching this nucleus (counts
  unknown).
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.

## Intralaminar nuclei (centromedian / parafascicular) — arousal + striatal drive

- **Function:** the "nonspecific" nuclei — arousal and alertness, plus a major direct
  excitatory input to the striatum (a thalamostriatal drive parallel to cortex): the
  centromedian nucleus → motor striatum, the parafascicular nucleus → associative / limbic
  striatum.
- **Inputs:**
  - **← the reticular formation** (brainstem) — **carries:** payload **owed**; the arousal drive
    this entry's Function names. **Fan-in:** unknown. **The producer has an entry in file 14**,
    whose closing summary names the ascending reticular activating system reaching the intralaminar
    thalamus. **Whether that entry declares this edge with a payload is unverified.
    Owed as a cross-file check at file 14.**
  - **← the deep cerebellar nuclei** — **carries:** payload **owed. Fan-in:** unknown. **The
    producer declares it** (file 10), which marks its own payload owed.
  - **← the lateral parabrachial nucleus** — **carries:** payload **unknown — owed. Fan-in:**
    unknown. **The producer declares it** (file 14), naming this group and the ventroposterior
    parvicellular thalamus together. **Recorded from the producer's declaration.**
  - **← the internal globus pallidus and the substantia nigra pars reticulata** — **carries:**
    payload **owed. Fan-in:** unknown. This entry's prose list named "basal-ganglia" as an input
    class; **file 9 declares no output to this group** — its declared thalamic targets are the
    ventral anterior / ventral lateral group, the mediodorsal nucleus and the reticular nucleus.
    **So this edge is declared at one end only. Owed: confirm at the producer, or delete.**
  - **← cerebral cortex** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint names a
    class** and cannot be checked as written. **Owed: resolve it to named producers.**
  - **← the thalamic reticular nucleus** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-in:** unknown. **The producer is in this file** and names this group among its consumers,
    while recording that this end did not declare the input. **Written here from that declaration.**
    *(Caution under §4: both ends now sit in one file, so the agreement certifies nothing on its own.
    The producer's own line records the pair as owed against the literature, and that mark stands.)*
- **Outputs:**
  - **→ the motor striatum**, from the **centromedian nucleus** — **carries:** arousal and a
    thalamostriatal drive parallel to cortex. **Payload otherwise unknown — owed. Fan-out:**
    unknown. **The consumer declares it** (file 9) and records that the sector split —
    centromedian to motor striatum — is **"a sub-element-level statement this end does not carry,"**
    with **"Owed here: say which striatal sector each nucleus reaches."** **This end holds the
    split; the owed edit stands at file 9.**
  - **→ the associative / limbic striatum**, from the **parafascicular nucleus** — **carries:** the
    same thalamostriatal drive. **Payload otherwise unknown — owed. Fan-out:** unknown. **Same
    consumer declaration and the same owed sector split** (file 9).
  - **→ the anterior cingulate cortex** — **carries:** payload **unknown — owed. Fan-out:**
    unknown. **The consumer declares it** (file 11) as an input from "the midline / intralaminar
    thalamus," and records that **the producer declares its cortical target as a class** —
    "cortex (diffuse)" — **"which covers this area without naming it,"** with the edit **owed at
    this file. Named here**, which discharges that owed edit for this consumer only.
  - **→ further cortex, diffusely, beyond the anterior cingulate** — **carries:** payload
    **owed. Fan-out:** unknown. **This endpoint names a class** and is the residue of the "cortex
    (diffuse)" line the named edge above was split out of. **Owed: resolve it to named consumers**
    — files 2, 3, 4, 8 and 17 all name the intralaminar nuclei and their consumer declarations are
    unverified here.
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this group's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's end
    only**, as part of that entry's class input.
- **Internal structure and internal data flow:** **owed.** Two sub-elements are named in this
  entry's own Function and Outputs slots — the **centromedian** and **parafascicular** nuclei — and
  they are already load-bearing, because the two striatal output edges above leave from different
  ones and reach different striatal sectors. **No internal edge between them is described**, and
  the wider intralaminar group (central lateral, paracentral, central medial) is named neither here
  nor in the material read. **Owed: name the remaining members and say whether any internal edge
  exists.**
- **Neurons:** unknown — soft; no clean human per-nucleus count recorded.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.

## Nucleus reuniens — the midline hippocampal–prefrontal conduit

- **Function:** the ventral midline relay between the hippocampal formation and the medial prefrontal
  cortex. **Its defining property is what it makes possible rather than what it computes:** medial
  prefrontal cortex has **no direct projection to the hippocampus**, so every prefrontal signal that
  reaches the hippocampus reaches it through here. **The hippocampal–prefrontal loop closes at this
  nucleus and nowhere else in the source.** *(The direct hippocampus → medial and orbital prefrontal
  limb is written at file 8 and is one-way; this nucleus is the return.)* **What it does to the
  signal on the way through is not established here — the payloads below are owed at both ends.**
- **Inputs:**
  - **← the medial prefrontal cortex, from subgenual area 25** (Brodmann area 25, infralimbic) —
    **carries:** payload **owed. Fan-in:** unknown. **The producer declares no such edge**: file 11's
    orbitofrontal / ventromedial entry, which holds Brodmann area 25, declares ten outputs and names
    no thalamic target of any kind other than the mediodorsal nucleus as an input. **Owed as a
    cross-file edit at that entry (file 11).**
    **This edge lands on a sub-element that entry names and no edge of its own uses.** Brodmann area
    25 is one of the five it lists; file 9 already addresses it as **infralimbic cortex**. **So the
    endpoint exists under three names in three files and had no edge until now.** *(Class 1 — **Joyce et al. 2022**, *Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus*, **Journal of Neuroscience 42(6):1068–1089**; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. Rhesus macaque, 12 animals, both sexes; bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. **Verified against the Society for Neuroscience journal record, 2026-08-15**; full text read.)*
  - **← the hippocampal formation**, from **CA1** and the **subiculum** — **carries:** payload
    **owed. Fan-in:** unknown. **The producer declares it** (file 8, written 2026-08-15), which
    records the termination density as topographic — denser rostrally, and denser again when the
    injection includes the subicular complex. **Two-ended.** **The terminations form multisynaptic
    complexes onto both excitatory projection neurons and the dendrites of local inhibitory neurons**,
    which is a statement about what the input contacts rather than about what it carries, and is the
    kind of claim the Internal structure slot below would hold if the slot were filled. *(Class 1 — **Joyce et al. 2022**, *Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus*, **Journal of Neuroscience 42(6):1068–1089**; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. Rhesus macaque, 12 animals, both sexes; bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. **Verified against the Society for Neuroscience journal record, 2026-08-15**; full text read.)*
  - **← the amygdala**, from the **basal** and **basomedial (accessory basal)** nuclei — **carries:**
    payload **owed. Fan-in:** unknown. **The producer declares it** (file 8, written 2026-08-15).
    **Two-ended.** **The primate finding is that this pathway is stronger than in rat or mouse** — a
    species claim rather than a payload, and the reason both ends were written from a primate study
    rather than carried from the rodent literature. Amygdalar terminations here are enriched with
    mitochondria and often form successive synapses onto the same postsynaptic structure, which the
    producing study reads as an active and robust pathway; **that reading is the study's, not this
    entry's.** *(Class 1 — **Joyce et al. 2022**, *Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus*, **Journal of Neuroscience 42(6):1068–1089**; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. Rhesus macaque, 12 animals, both sexes; bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. **Verified against the Society for Neuroscience journal record, 2026-08-15**; full text read.)*
- **Outputs:**
  - **→ the hippocampal formation**, onto **CA1** and the **subiculum** — **carries:** payload
    **owed**, and it is the **return arm of the prefrontal loop**: this is the stage through which
    medial prefrontal cortex reaches the hippocampus, since it has no direct projection there.
    **Fan-out:** unknown. **The consumer declares it** (file 8, written 2026-08-15). **Two-ended.**
    **What this edge carries is the loudest owed payload this entry has**, because the entry's whole
    reason for existing is that a signal passes here and the source cannot say what it is. *(Class 1 — **Joyce et al. 2022**, *Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus*, **Journal of Neuroscience 42(6):1068–1089**; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. Rhesus macaque, 12 animals, both sexes; bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. **Verified against the Society for Neuroscience journal record, 2026-08-15**; full text read.)*
  - **→ the amygdala**, onto the **basal** and **basomedial** nuclei — **carries:** payload **owed.
    Fan-out:** unknown. **The consumer declares it** (file 8, written 2026-08-15). **Two-ended.**
  - **→ the medial prefrontal cortex** — **not written. Unverified.** The producing study establishes
    that area 25 sends axons *here* and that this nucleus reaches the hippocampus; **whether the
    return limb to prefrontal cortex exists was not established by what was read**, and writing it
    from the general expectation that thalamic relays are reciprocal would be inventing an edge from
    a pattern. **Owed: research it.** **If it exists it is the third side of the loop**, and its
    absence or presence changes whether this nucleus is a relay in the ordinary thalamic sense or a
    one-way conduit into the hippocampus.
  - **→ the thalamic reticular nucleus** (collaterals) — **not written, and the reason is a finding
    about the entry below rather than about this one.** That entry's Inputs slot takes "collaterals
    of cortico-thalamic and thalamo-cortical axons" as a class covering every thalamic nucleus, and
    its own research note records **"virtually all nuclei" *and the midline caveat*** as
    the summary it rests on. **The midline group is the named exception to that class, and this file
    had no midline entry for the exception to attach to.** **Owed: state at the reticular entry
    whether this nucleus is inside or outside its gate**, which is now a checkable question rather
    than a caveat in a citation.
- **Internal structure and internal data flow:** **partly known, and unusually for this file the
  known part is a cell-class statement rather than a divisional one.**

  **Cell-class sub-elements: two, and they divide by projection target.** This nucleus is
  **matrix-dominant** — **calbindin**- and **calretinin**-expressing projection cells, which target
  cortical **layers I–IIIa** — with a **sparse core-associated parvalbumin population**. **On the
  floor-of-the-hierarchy rule these are sub-elements if they have different targets, and the laminar
  statement says they do.** **What follows is a claim about the *form* of this nucleus's cortical
  output rather than its content: a matrix-dominant nucleus is modulatory in the layer-I sense, not
  a driver onto layer 4.** **Owed: whether the hippocampal and amygdalar outputs above leave from
  the same population, and which.** *(Class 1 — **Joyce et al. 2022**, *Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus*, **Journal of Neuroscience 42(6):1068–1089**; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. Rhesus macaque, 12 animals, both sexes; bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. **Verified against the Society for Neuroscience journal record, 2026-08-15**; full text read.)*

  **Divisional sub-elements: owed, and the boundary of this entry is part of what is owed.** The
  midline group is conventionally the **reuniens**, **rhomboid**, **paraventricular** and
  **paratenial** nuclei. **This entry is written for the reuniens because that is where the four
  edges land**, and whether the other three belong here, in the intralaminar entry above, or in
  entries of their own is **not settled**. **Owed: decide the grouping.** **The question is not
  cosmetic**: file 11's anterior cingulate entry declares an input from "the **midline** /
  intralaminar thalamus," a compound whose midline half has had no referent anywhere in the source
  until this entry, and which this entry does not yet claim.

  **Laminar sub-elements: not applicable.** A thalamic nucleus, not cortex. Recorded as a positive
  statement rather than as unknown.

  **Internal edges: owed, all of them.** None between the two cell classes, and none between this
  nucleus and any other midline member, is recorded.
- **Neurons:** unknown. **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown. *(No stereological figure is recorded;
  the Pakkenberg / Dorph-Petersen lineage this file leans on elsewhere may carry one. **Owed.**)*
  edges; all four written and two-ended at both ends; the prefrontal input written with its far end
  owed at file 11; the reticular-collateral and prefrontal-return limbs deliberately **not** written
  and recorded as research owed; the matrix / core cell classes named as sub-elements; the midline
  group's membership and this entry's boundary recorded as owed

## Thalamic reticular nucleus — the inhibitory gate

- **Function:** the GABAergic inhibitory shell around the thalamus — the one thalamic
  structure that does **not** project to cortex; instead it inhibits the other thalamic
  nuclei, gating thalamocortical traffic and implementing attentional selection (the
  "searchlight"). **Most, but not all, cortico-thalamic and thalamo-cortical axons passing through
  give it collaterals** — the exceptions are specific and are set out at the first input edge below.
  *(The universal form — that **every** such axon drives it — is contradicted by the literature
  and is not written here; the exceptions are why that matters, because a sheet that monitors
  *most* traffic is a different gate from one that monitors all of it.)*
- **Inputs:**
  - **← collaterals of cortico-thalamic and thalamo-cortical axons** — **carries:** a copy of the
    traffic in both directions, which is what lets this sheet gate what it monitors. **Fan-in:**
    unknown. **This endpoint names a class, and the class is not exempt from §3, because the
    universal claim that would have exempted it is false.** The exceptions, on both halves:
    - **Corticothalamic, layer 6a** — collateralises here. This is the canonical top-down input to
      this sheet.
    - **Corticothalamic, layer 5** — **contested, recorded not resolved (§6).** One laboratory
      reports that layer 5 generally does **not** innervate this sheet, the layer-5 driver axons
      reaching the higher-order nuclei without the feed-forward inhibition the layer-6 route
      carries, with **one region-specific exception**: layer 5 pyramidal cells of **frontal
      cortex**, and not of other cortical regions, make **monosynaptic** connections here, with
      morphology and physiology distinct from the layer-6 route. **A second laboratory reports the
      opposite general case** — that layer-5 terminals from *multiple* cortical regions form bona
      fide synapses here, demonstrated by electron microscopy, and that they target the
      higher-order-projecting cells. **Both are mouse.** **What turns on it is whether this sheet
      is gated by frontal cortex specifically or by cortex at large**, which is a different
      searchlight. **Owed: give the second report a key, and say what separates the two results —
      method, cortical sampling, or the sheet's own subdivisions.**
    - **Corticothalamic, layer 6b** — targets higher-order thalamus and sends **no** collaterals
      here, confirmed by single-cell tracing.
    - **Thalamocortical** — collaterals arise from *virtually* all thalamic nuclei, not all: in the
      one nucleus where the fraction was counted, **76% of ventrobasal relay axons followed into
      the internal capsule gave visible collaterals here**, so roughly a quarter did not. Midline
      nuclei are the least strictly organised, and a paraventricular projection to this sheet has
      **not been described** though the reverse projection has.
    **So the six thalamic collaterals declared here** — mediodorsal, pulvinar,
    posterior / ventromedial-posterior, ventral anterior / ventral lateral, anterior nuclei
    and intralaminar — **are individually
    warranted rather than instances of a universal, and the cortical half must be resolved to named
    producers by layer. Owed: split this line by producer and layer.**
    *(Class 1 — layer-5 frontal exception: Nature Neuroscience 2022 (PMC9829539), mouse,
    optogenetics with paired recording; layer-6b absence: PMC6018949, mouse,
    Cre-recombinase-dependent viral and single-cell tracing; ventrobasal 76%: intracellular
    horseradish-peroxidase fill with serial reconstruction, rat, PubMed 3584546; "virtually
    all nuclei" and the midline caveat: a review summary. **These are secondary and abstract-level
    reads — no primary paper has been opened in full. Candidates:** what was opened is not the
    record that would settle these exceptions.)*
  - **← the basal forebrain, parvalbumin-expressing GABAergic neurons** — **carries:** inhibition of
    this nucleus, and therefore **disinhibition of the relay nuclei it inhibits**. These are
    fast-firing cells, distinct from the sleep-active GABAergic population, and they densely
    innervate this sheet. The functional logic is double-negative: a tonic inhibitory hold on the
    relay nuclei is **transiently released** when attention or arousal demands it. **Fan-in:**
    unknown. **The producer declares it** (file 13) and marks it declared at both ends. *(Class 1 —
    viral tracing and optogenetics, mouse; Proceedings of the National Academy of Sciences /
    PMC4371918; PMC4463930. **PMC4371918 verified against its record 2026-08-12** while working file 13,
    which cites the same accession; **PMC4463930 partial — a secondary listing only.**)*
  - **← the basal forebrain, cholinergic neurons** — **carries:** payload **owed**, and the **sign is
    the surprise**: selectively driving cholinergic fibres optically within this nucleus
    **promotes sleep**, which is opposite to acetylcholine's general arousal role and opposite to
    the parvalbumin edge above. Two projections from one source region to one target, with
    opposite behavioural consequences. **Fan-in:** unknown. **The producer declares it** (file 13).
    *(Class 1 — PMC4764559, rodent. **Unverified: the key reads owed in the reference section — not
    searched.**)*
  - **← the internal globus pallidus** and **← the substantia nigra pars reticulata** —
    **carries:** GABAergic inhibition; **payload owed. Fan-in:** unknown. **The producer declares
    it** (file 9), which carries this end's ambiguity with it:
    **whether these terminate on this nucleus or directly on the relay nuclei is not distinguished
    at either end and is owed.** File 9 states the consequence plainly — if they terminate on the
    relay nuclei directly, this edge and its two thalamic edges are the same projection described
    twice. *(Class 1 — PMC4463930.)*
  - **← the zona incerta** — **carries:** GABAergic inhibition; **payload owed. Fan-in:** unknown.
    **The producer is in this file**, and declares its signature target as the higher-order
    posterior thalamus rather than this sheet. **The same terminate-here-or-on-the-relay ambiguity
    applies and is owed.**
- **Outputs:**
  - **→ the mediodorsal nucleus** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-out:** unknown. **The consumer is in this file** and declares an inhibitory input.
  - **→ the pulvinar** — **carries:** inhibitory gating of specific transthalamic pathways; no
    content. **Fan-out:** unknown. **The consumer is in this file** and declares it.
  - **→ the posterior / ventromedial-posterior thalamus** — **carries:** inhibition; a gain/gate
    control, no content. **Fan-out:** unknown. **The consumer is in this file** and declares it.
  - **→ the ventral anterior / ventral lateral thalamus** — **carries:** inhibition; a gain/gate
    control, no content. **Fan-out:** unknown. **The consumer is in this file** and declares it.
  - **→ the lateral geniculate nucleus** — **carries:** inhibition; a gain/gate control, no
    content. **Fan-out:** unknown. **The consumer declares it** (file 1). **The visual sector of
    this sheet is the perigeniculate nucleus** — see the naming note below.
  - **→ the medial geniculate nucleus** — **carries:** inhibition; the gate. **Fan-out:** unknown.
    **The consumer declares it** (file 2), which names the auditory sector of this sheet.
  - **→ the ventral posterior nuclear complex** — **carries:** inhibition; a gain/gate control, no
    content. **Fan-out:** unknown. **The consumer declares it** (file 5).
  - **→ the anterior nuclei** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-out:** unknown. **The consumer is in this file** and declares it from this end's
    declaration rather than from its own material.
  - **→ the intralaminar nuclei** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-out:** unknown. **The consumer is in this file** and declares it on the same basis.
    *(Both of these last two are two-ended in form only. Neither consumer's own material named this
    sheet, and both ends now descend from this line, so under §4 the agreement certifies nothing.
    **Owed: confirm each against the literature, or narrow the Function claim** — the exceptions
    researched at the first input edge above show the "inhibits the other thalamic nuclei" claim is
    not universal, and the midline group is the one this file has already found outside it.)*
    *(The eight lines replace what would otherwise be the class endpoint "the thalamic relay
    nuclei (not cortex)" under §9b. Seven consumers declare an input from this sheet and supply
    the names; the eighth line records the two that do not.)*
- **Internal structure and internal data flow:** **owed.** This sheet is **sectored by modality**,
  and the sectors are already load-bearing because the output edges above leave from different
  ones: the **perigeniculate nucleus** is the visual sector, an **auditory sector** is named at
  file 2's medial geniculate entry, and the somatosensory and motor sectors are implied by the
  remaining outputs. **No sector is given as a named sub-element here and no internal edge between
  sectors is described** — which matters, because intra-reticular connectivity is what would let
  the "searchlight" select one modality *against* another rather than gating each independently.
- **A naming collision, stated at the entry that owns the name.** The visual sector of this sheet
  **is** the perigeniculate nucleus, named separately at the lateral geniculate entry (file 1). The
  two are the same structure described at different scales, and this file had been using both names
  without saying so. Recorded here rather than resolved by preference, per §6: the sector name and
  the nucleus name are both in common use, and the **edges** above carry the function either way.
- **One negative result, recorded because it constrains the payload.** The basal forebrain's
  parvalbumin neurons drive cortical gamma-band activity, and this projection was tested as the
  route by which they do it. Stimulating the parvalbumin neurons **of this nucleus** instead
  enhanced cortical power at about **10 Hz** — spindle frequency — and **not** gamma. So this edge
  is not the carrier of the basal forebrain's gamma effect; the direct cortical projection is.
  *(Class 1 — PMC4371918, mouse.)*
- **Neurons:** unknown — soft; a thin sheet, no clean human count recorded.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** not applicable — the structure is a thin grey sheet lying within the
  internal capsule's fibre path rather than a nucleus with its own white-matter compartment.
  *(Class 2 — Claude's reading of the described anatomy, not a measured figure. Candidate.)*
- **Myelination:** unknown.

## Zona incerta — the subthalamic inhibitory hub (ventral diencephalon / subthalamus)

- **Function:** a largely **GABAergic** cell sheet of the **subthalamus** (ventral diencephalon),
  lying dorsal to the subthalamic nucleus — an **integrative inhibitory hub** with unusually
  wide-ranging inputs and outputs whose precise role is still debated (Mitrofanis's "zone of
  uncertainty", 2005). Grouped here because its signature projection is the **incerto-thalamic**
  GABAergic input to the **higher-order thalamus** (the posterior group), gating
  thalamocortical and thalamostriatal transmission — an *extrathalamic* inhibitory gate that
  complements the thalamic reticular nucleus's intrinsic one above (though the zona incerta
  itself is subthalamus, not a thalamic nucleus). Different sectors of it have been tied to
  **arousal and attention, posture and locomotion, feeding, defensive behaviour (fear /
  flight), sleep, visceral activity, and pain gating** (Mitrofanis 2005, **a review — Class 3**).
  *(The "integrative node for global behavioural modulation" phrase is the title of a separate and
  later review, not of Mitrofanis 2005. **Owed: give that review a key, or drop the phrase.**)*
- **Inputs:**
  - **← the central nucleus of the amygdala**, onto this structure's **parvalbumin neurons** —
    **carries:** payload **owed**; this producer's role in the pair is given at this end as fear.
    **Fan-in:** unknown. **The producer declares it** (file 8), from this
    entry's own declaration. *(Caution under §4: both ends descend from the same sentence at this
    end, so the agreement certifies nothing.)*
  - **← a near-whole-brain afferent field — cerebral cortex, basal ganglia, thalamus,
    hypothalamus, brainstem, cerebellum, and spinal cord** — **carries:** payload **owed. Fan-in:**
    unknown. **Every endpoint here names a class**, seven of them, and none can be checked as
    written. **Owed: resolve to named producers.** This is the largest single block of class
    endpoints in the file, and the entry's own Function slot gives the reason it is written this
    way — the afferent field is unusually wide — which is an explanation and not a resolution.
- **Outputs:**
  - **→ the posterior / ventromedial-posterior thalamus** (the incerto-thalamic projection) —
    **carries:** inhibition, no content. **Payload otherwise unknown — owed. Fan-out:** unknown.
    **The consumer is in this file** and declares it, naming this structure's signature target.
  - **→ the thalamic reticular nucleus** — **carries:** GABAergic inhibition; **payload owed.
    Fan-out:** unknown. **The consumer is in this file** and declares it, with the
    **terminate-here-or-on-the-relay ambiguity owed at both ends.**
  - **→ the hypothalamus** — **carries:** payload **owed. Fan-out:** unknown. **The consumer has an
    entry in file 14; whether it declares this edge is unverified. Owed as a cross-file check.**
  - **→ the periaqueductal gray** (defensive behaviour) — **carries:** payload **owed. Fan-out:**
    unknown. **The consumer has an entry in file 14; unverified there. Owed as a cross-file check.**
    *(Class 1 — Chou et al. 2018.)*
  - **→ the ventral tegmental area** (feeding drive) — **carries:** payload **owed. Fan-out:**
    unknown. **The consumer has an entry in file 13; unverified there. Owed as a cross-file check.**
  - **→ the rostral ventromedial medulla** (descending pain control) — **carries:** payload
    **owed. Fan-out:** unknown. **File 14 holds the rostral and caudal ventrolateral medulla
    entries; whether the ventromedial medulla has an entry is unverified. Owed —
    this may be a named region with no entry**, in which case it belongs in §9a of the design file.
  - **→ the cerebral cortex** — **carries:** payload **owed. Fan-out:** unknown. **This endpoint
    names a class. Owed: resolve to named consumers.**
  - **→ the spinal cord** — **carries:** payload **owed. Fan-out:** unknown. **The consumer has an
    entry in file 16; unverified there. Owed as a cross-file check.**
- **Internal structure and internal data flow:** **owed.** The entry's Function slot states that
  **different sectors** carry different functions — arousal and attention, posture and locomotion,
  feeding, defensive behaviour, sleep, visceral activity, pain gating — and a **parvalbumin
  population** is named as the target of the amygdalar input, so sub-elements are described. **None
  is named and no internal edge is written.** The sectors are load-bearing for the same reason the
  pulvinar's are: eight output edges leave this structure for eight different targets, and the
  functional list implies they do not all leave from the same sector. **Owed: name the sectors and
  assign each output edge to one.** The rostral / caudal division is already in use in this entry's
  own clinical note.
- **Clinical note:** the **caudal zona incerta** is an established **deep-brain-stimulation target
  for tremor** (Parkinson's disease and essential tremor), in some series superior to
  subthalamic-nucleus stimulation — the second subthalamic deep-brain-stimulation target
  alongside the subthalamic nucleus named in the basal-ganglia entry.
- **Neurons:** unknown — soft; no clean human count; a diffuse, ill-bordered subthalamic sheet.
- **Synapses:** unknown.
- **Axons:** the incerto-thalamic and descending incertal projections (counts unknown).
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.

---

---

## References

*(The literature this file's own entries cite, one line per distinct key, ordered by short form.
A key given in full was read off a publisher, journal or PubMed record, and searching is the
verification — so those lines carry **verified against ⟨record⟩ ⟨date⟩**. A key reading **owed**
has not been searched, and the citation text for it, wherever it appears in this file, rests on
recall. A key reading **partial** was resolved only against a secondary listing and is a
**candidate**, because a secondary listing can propagate an error in the very fields it is
consulted for.)*

**38 distinct keys, 46 mentions. 12 verified against a publisher, journal or PubMed record; 3
partial — secondary listings only, still candidates; 1 resolved as not a separate source; 22
owed.**

**This file's keys are the least well-formed in the source so far, and the shape of that is the
finding.** **Six were a bare accession number with no author, title or year anywhere in the
file** — *PMC4371918*, *PMC4463930*, *PMC4764559*, *PMC6018949*, *PMC9829539* and
*PubMed 3584546*; two of the six are now resolved to papers. **Two more are a journal, volume and
page with no author** — *Journal of Neuroscience 17:3274, 1997*, now resolved, and *Journal of
Neuroscience 2025*, which carries no volume or page either and remains the least identifiable key
in the file. **Six are a lineage or an author string with no paper at all** — *Sherman &
Guillery*, *Petersen / Robinson rhesus*, *Gattass, cebus*, and the three stereology-lineage forms
below. **So a large minority of keys cannot be matched to a paper by reading the file**, which is
the condition §2a's both-directions check exists to expose. It is not a defect in any claim; it is
a defect in what a reader can do with the claim.

**Five keys name one body of work under five different short forms.** *Pakkenberg /
Dorph-Petersen stereology lineage*, *Dorph-Petersen, Byne, Popken*, *Dorph-Petersen et al. 2004*,
*Pakkenberg / Byne / Popken lineages* and *Dorph-Petersen's review* are all the human thalamic
stereology literature this file's neuron and volume slots rest on. Only one of the five carries a
year. **Owed at the citing lines: one key, or say what distinguishes them.**

**One key appears in two forms.** *Blomqvist, Zhang & Craig 2000* and *Blomqvist, Zhang & Craig,
Brain 123:601, 2000* are the same paper. **Owed at the citing lines: use one.**

**One key is shared with file 11, which is §2a's stated case.** *Schmitt / Halassa et al., Nature
2017* carries the mediodorsal payload at both ends of the same edges — five output edges here,
five input edges there — so the two files independently record one source, and a disagreement
between them would be a finding. There is none: the reference and the payload statement match.
**Three bare accessions are shared with file 13** — *PMC4371918*, *PMC4463930* and *PMC4764559* —
and the two files independently support the same two edges from opposite ends.

**Three searched references confirm the file's numbers exactly, which is worth recording because
most reference work turns up discrepancies.** The *Craig, Krout & Andrew* entry (three means,
three standard deviations and three sample sizes, all matching), the *Craig & Dostrovsky* entry
(three projection counts, matching) and the *Han, Zhang & Craig* entry (the morphology–physiology
correspondence, matching, with the paper's own cell counts now recoverable). **Two of the three
also carry a figure this file does not** — conduction velocities, and the fusiform / pyramidal /
multipolar counts — noted at those entries.

**Four searched references disagree with the file, and each is recorded at its own line below.**
*Zhou 2016* does not support the claim that silencing the pulvinar leaves cortical sensory
responses intact; *Zhang & Craig 1997* supports the three **morphological** classes in primate and
not the three **response** classes; *Hádinger et al.* carries a 2023 issue year against the key's
2022; and a second laboratory contradicts the layer-5 exception the reticular entry rests on.
**These are the yield of the searching, and they are the argument for it** — none was visible from
inside the file.

**Species composition of what has been searched:** of the papers behind the searched-or-partial
keys, **four are cat** (the two 2001 Craig papers, the Han et al. 1998 morphology work, and by
inheritance the response classes), **one is human** (Blomqvist et al. 2000), **three are macaque**
(Craig 2004, partial; Zhang & Craig 1997; Zhou et al. 2016 and Saalmann et al. 2012), and **three
are mouse** (Schmitt et al. 2017, Kim et al. 2015, Hádinger et al. 2023). **The file declares
"Species: cat for the numbers"** at the interoceptive relay's latency line, and the searching bears
that out rather than softening it. The unsearched keys are the human stereology lineage, so the
balance is not yet legible.

**One claim in the file carries no key at all.** The **pruriceptive (itch) population responding
differentially to histamine and cowage**, at the interoceptive relay's lamina-I input. The search
for the Han et al. paper surfaced the likely source — Andrew, D. & Craig, A.D. (2001),
*Spinothalamic lamina I neurons selectively sensitive to histamine: a central neural pathway for
itch*, *Nature Neuroscience* 4(1): 72–77; doi 10.1038/82924 — but §2a forbids adding a source no
line cites, so **the repair is at the citing line: give it a key, or drop the claim.**

- **Blomqvist, Zhang & Craig 2000** — **the same paper as the key below**, cited under a shorter
  form at one line. See that entry for the full reference. **Owed at the citing lines: use one
  key.**
- **Blomqvist, Zhang & Craig, Brain 123:601, 2000** — Blomqvist, A., Zhang, E.-T. & Craig, A.D.
  (2000). Cytoarchitectonic and immunohistochemical characterization of a specific pain and
  temperature relay, the posterior portion of the ventral medial nucleus, in the human thalamus.
  *Brain* 123(Pt 3): 601–619; doi 10.1093/brain/123.3.601; PubMed 10686182. **Human thalamus,
  post-mortem.** Cytoarchitectonics with immunohistochemical labelling for **calbindin, substance P
  and calcitonin gene-related peptide**. *(Verified against the Oxford University Press publisher
  record and PubMed, 2026-08-12.)* **The entry uses two of the three markers and not the third.**
  The interoceptive relay's Function and Internal structure slots carry calbindin and calcitonin
  gene-related peptide; **substance P is in the paper's own method statement and appears nowhere in
  this file.** Whether it distinguishes a third field, or co-distributes with one of the two, is not
  established here. **Owed: say what substance P showed, or say the entry does not use it.**
- **Byne 2001** — **owed**: not searched. One of three keys on a single volume figure at the
  mediodorsal entry.
- **Chou et al. 2018** — **partial.** Chou, X.-L. et al. (2018). Inhibitory gain modulation of
  defense behaviors by zona incerta. *Nature Communications* 9(1). **Rodent.** *(**Title, journal,
  volume and year taken from a secondary reference list, not from the publisher's record** — the
  search that surfaced it was for the Mitrofanis review. The full author list, the article number
  and the doi were not obtained, and §2a requires saying so.)* **Owed: confirm against the
  publisher.**
- **Craig 2004** — **partial.** Craig, A.D. (2004). Distribution of trigeminothalamic and
  spinothalamic lamina I terminations in the macaque monkey. *Journal of Comparative Neurology*
  477: 119–148. **Macaque.** *(**Taken from a secondary reference list, not from the publisher's
  record** — the search that surfaced it was for the Blomqvist paper. Volume, pages and year are
  unconfirmed.)* **Owed: confirm against the publisher.**
- **Craig & Dostrovsky, Journal of Neurophysiology 86:856, 2001** — Craig, A.D. & Dostrovsky, J.O.
  (2001). Differential projections of thermoreceptive and nociceptive lamina I trigeminothalamic
  and spinothalamic neurons in the cat. *Journal of Neurophysiology* 86(2): 856–870; doi
  10.1152/jn.2001.86.2.856; PubMed 11495956. **Cat**, barbiturate-anaesthetised. Antidromic
  activation from a mobile electrode array, mapping the thalamic projections of **40**
  trigeminothalamic or spinothalamic lamina I neurons. *(Verified against the American Physiological
  Society publisher record and PubMed, 2026-08-12.)* **The entry's counts check out.** The
  interoceptive relay gives 20 of 23 thermoreceptive cells reaching the dorsomedial ventral
  posterior medial nucleus against 1 of 9 nociceptive-specific and 0 of 8 polymodal; the paper's
  characterised sample is nociceptive-specific n = 9, polymodal n = 8, thermoreceptive-specific
  n = 22 plus one warm cell — **which is where the 23 comes from**, and the file does not say that
  the twenty-third is a warm cell rather than a cool one. **One thing the entry does not record:**
  the paper mapped its cells from a total identified sample considerably larger than 40, so the 40
  is the mapped subset and not the recording yield. Neither point changes a claim.
- **Craig & Zhang 2006** — **owed**: not searched. The secondary material surfaced while searching
  Blomqvist describes it as the retrograde-tracing report confirming the selective lamina I input
  and the antero-posterior head-to-foot topography, which is what the contested-nucleus line uses
  it for; **that is a description, not a reference, and no reference is written from it.**
- **Craig, Krout & Andrew, Journal of Neurophysiology 86:1459, 2001** — Craig, A.D., Krout, K. &
  Andrew, D. (2001). Quantitative response characteristics of thermoreceptive and nociceptive
  lamina I spinothalamic neurons in the cat. *Journal of Neurophysiology* 86(3): 1459–1480; doi
  10.1152/jn.2001.86.3.1459; PubMed 11535691. **Cat**, barbiturate-anaesthetised. Antidromically
  identified lamina I spinothalamic neurons in the lumbosacral cord, quantitative thermal and
  mechanical stimuli. *(Verified against the American Physiological Society publisher record and
  PubMed, 2026-08-12.)* **Every number on the citing line matches the paper.**
  Nociceptive-specific 130.8 ± 55.5 ms, n = 100; polymodal nociceptive 72.1 ± 28.0 ms, n = 128;
  thermoreceptive-specific 58.6 ± 25.3 ms, n = 136 — which the entry gives as ≈131 / 56 / 100,
  ≈72 / 28 / 128 and ≈59 / 25 / 136. **Nine figures, nine matches.** **And the paper carries one
  the file does not.** It gives the corresponding **conduction velocities — 2.5, 4.6 and 5.6 m/s** —
  which is the transportable form of the same measurement, since a latency depends on the path
  length of the preparation and a velocity does not. **Owed: carry the velocities alongside the
  latencies**, which would also let the cat figures be scaled to a human path length rather than
  transferred whole.
- **Danos 2003** — **owed**: not searched. One of three keys on a single volume figure at the
  mediodorsal entry.
- **Dorph-Petersen, Byne, Popken** — **owed**, and **one of five short forms for one lineage**; see
  the note above the list.
- **Dorph-Petersen et al. 2004** — **owed**: not searched. **The only one of the five lineage keys
  that carries a year**, and therefore the one a search should start from.
- **Dorph-Petersen's review** — **owed**, and **one of five short forms for one lineage**. Whether
  the review is the 2004 paper above or a separate publication is not stated in the file.
- **Dostrovsky & Craig 1996** — **owed**: not searched. Named alongside the 1997 journal string
  below as the primate confirmation of the three classes.
- **Gattass, cebus** — **owed**: not searched; the key carries no year and no title.
- **Graziano & Jones 2004** — **owed**: not searched. One of the three keys carrying the rebuttal
  side of the contested-nucleus dispute.
- **Han, Zhang & Craig, Nature Neuroscience 1:218, 1998** — Han, Z.-S., Zhang, E.-T. & Craig, A.D.
  (1998). Nociceptive and thermoreceptive lamina I neurons are anatomically distinct. *Nature
  Neuroscience* 1(3): 218–225; doi 10.1038/665. **Cat**, intracellular recording and labelling of
  **38** lamina I neurons. *(Verified against the Nature publisher record, 2026-08-23.)* **The
  entry's claim checks out and the paper carries the counts the file does not.** All **12** fusiform
  cells were nociceptive-specific; all **11** pyramidal cells were thermoreceptive-specific; of
  **10** multipolar cells, six were polymodal and four nociceptive-specific; **five** unclassified
  cells were consistent with the pattern. **So "near-total" is the right word and the exception is
  named: it is the multipolar class, which splits.** **Owed at the citing line: carry the four
  counts**, which convert a qualitative claim into a checkable one.
- **Joyce et al. 2022 (Journal of Neuroscience 42(6):1068)** — Joyce, M.K.P., Marshall, L.G.,
  Banik, S.L., Wang, J., Xiao, D., Bunce, J.G. & Barbas, H. (2022). Pathways for memory, cognition
  and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique
  interactions in the primate thalamic reuniens nucleus. *Journal of Neuroscience* 42(6):
  1068–1089; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. **Rhesus macaque**, 12 animals,
  both sexes; bidirectional dextran-amine tracer injections into the hippocampus, medial prefrontal
  area 25 and the amygdala, with immunohistochemistry, stereological termination density, confocal
  and electron microscopy. *(Verified against the Society for Neuroscience journal record,
  2026-08-15; full text read.)* **This one paper carries the whole nucleus reuniens entry** — all
  four of its edges, its cell-class sub-elements, and the species claim about the amygdalar limb.
- **Journal of Neuroscience 17:3274, 1997** — Zhang, E.-T. & Craig, A.D. (1997). Morphology and
  distribution of spinothalamic lamina I neurons in the monkey. *Journal of Neuroscience* 17(9):
  3274–3284; doi 10.1523/JNEUROSCI.17-09-03274.1997. **Monkey**, retrograde labelling with cholera
  toxin subunit b. *(Verified against the Society for Neuroscience journal record, 2026-08-23.)*
  **And it does not support what the citing line uses it for.** The citing line names it as the
  **primate confirmation of the three classes projecting here**, where "the three classes" on that
  line are the three **response** classes — nociceptive-specific, thermoreceptive-specific,
  polymodal. This paper recognises the three **morphological** types — fusiform, pyramidal,
  multipolar — in the monkey and reports **greater variation than in the cat, with more subtypes
  noted**. It is a morphological confirmation, not a physiological one, and the primate
  morphology is **less** clean than the cat's rather than equally clean. **Owed at the citing line:
  narrow the claim to morphology, and carry the greater-variation caveat.**
- **Journal of Neuroscience 2025** — **owed**: not searched, **and the key names no author, no
  volume and no page** — a journal and a year only, for the mouse rabies-tracing result that types
  the pulvinar's driver and modulator input laminae. **This is the least identifiable key in the
  file.**
- **Kemether 2003** — **owed**: not searched. One of three keys on a single volume figure at the
  mediodorsal entry.
- **Mitrofanis 2005** — Mitrofanis, J. (2005). Some certainty for the "zone of uncertainty"?
  Exploring the function of the zona incerta. *Neuroscience* 130(1): 1–15; doi
  10.1016/j.neuroscience.2004.08.017; PubMed 15561420. **A review**, not a primary report.
  *(Verified against the Elsevier publisher record and PubMed, 2026-08-23.)* **The paper supplies
  the "zone of uncertainty" phrase and the sector-function list** — visceral activity, shifting
  attention, arousal, posture and locomotion are named in its own abstract, which is what the zona
  incerta entry's Function slot uses it for. **Two corrections it forces.** First, being a review it
  is **Class 3**, general anatomy, wherever the citing line calls it Class 1. Second, **the
  "integrative node for global behavioural modulation" phrase the entry attributes to this paper is
  the title of a different and later review** — *Zona Incerta: An Integrative Node for Global
  Behavioral Modulation*, PubMed 31864676 — surfaced by the same search. **Owed at the citing line:
  re-attribute the phrase, or drop it.**
- **Nature Neuroscience 2022 (PMC9829539)** — Hádinger, N., Bősz, E., Tóth, B., Vantomme, G.,
  Lüthi, A. & Acsády, L. (2023). Region-selective control of the thalamic reticular nucleus via
  cortical layer 5 pyramidal cells. *Nature Neuroscience* 26(1): 116–130; doi
  10.1038/s41593-022-01217-z; PubMed 36550291; PMC9829539. **Mouse**, optogenetics with paired
  recording and single-cell reconstruction. *(Verified against the Nature publisher record and
  PubMed, 2026-08-23.)* **The frontal exception checks out**: layer-5 pyramidal cells of frontal
  cortex, and not of other cortical regions, make monosynaptic connections with the reticular
  nucleus, morphologically and physiologically distinct from the layer-6 route — which is the
  reticular entry's claim. **Two corrections.** First, **the year on the key is the online year and
  the paper is a 2023 issue** — the key should read 2023, or carry both. Second, **a second
  laboratory contradicts the general half of the same claim.** Carroll, B.J., Sampathkumar, V.,
  Kasthuri, N. & Sherman, S.M. (2022), *Layer 5 of cortex innervates the thalamic reticular nucleus
  in mice*, *Proceedings of the National Academy of Sciences* 119(38): e2205209119; doi
  10.1073/pnas.2205209119; PubMed 36095204, demonstrate by electron microscopy that layer-5
  terminals from **multiple** cortical regions make bona fide synapses in the reticular nucleus,
  targeting the higher-order-projecting cells. **So "layer 5 generally does not innervate this
  sheet, except from frontal cortex" is contested, not settled**, and the reticular entry states it
  as settled. **Owed at that entry: record the dispute under §6's contested rule, and give the
  second paper a key** — §2a forbids adding it here until a line cites it.
- **Pakkenberg / Byne / Popken lineages** — **owed**, and **one of five short forms for one
  lineage**.
- **Pakkenberg / Dorph-Petersen stereology lineage** — **owed**, and **one of five short forms for
  one lineage**.
- **Petersen / Robinson rhesus** — **partial.** Petersen, S.E., Robinson, D.L. & Keys, W. Pulvinar
  nuclei of the behaving rhesus monkey: visual responses and their modulation. *Journal of
  Neurophysiology*. **Rhesus monkey**, single-unit recording in the behaving animal.
  *(**Author list, title and journal taken from the reference list of the Saalmann et al. 2012
  paper, not from a publisher record**; volume, pages and year were not obtained.)* **Owed: confirm
  against the publisher.** It supports the primate single-unit selectivity claim the pulvinar
  entry's Function slot turns on.
- **PMC4371918** — Kim, T., Thankachan, S., McKenna, J.T., McNally, J.M., Yang, C., Choi, J.H.,
  Chen, L., Kocsis, B., Deisseroth, K., Strecker, R.E., Basheer, R., Brown, R.E. & McCarley, R.W.
  (2015). Cortically projecting basal forebrain parvalbumin neurons regulate cortical gamma band
  oscillations. *Proceedings of the National Academy of Sciences* 112(11): 3535–3540; doi
  10.1073/pnas.1413625112; PubMed 25733878; PMC4371918. **Mouse.** Viral transduction of basal
  forebrain parvalbumin neurons with optogenetic stimulation and cortical recording. **Correction:
  *Proceedings of the National Academy of Sciences* 112(21): E2848; doi 10.1073/pnas.1507465112;
  PubMed 25918414 — an acknowledgments change naming funding support, with no change to any
  result.** *(Verified against the National Academy of Sciences publisher record, PubMed and PubMed
  Central, 2026-08-12.)* **Both of this file's uses check out.** The paper found dense innervation
  of the reticular nucleus by basal forebrain parvalbumin fibres, which is that entry's input edge;
  and stimulating the reticular nucleus's own parvalbumin neurons **preferentially enhanced cortical
  power at 10 Hz**, consistent with spindle activity and **not** gamma, which is the negative result
  recorded there — the paper's own conclusion being that the direct cortical projection carries the
  gamma effect. **File 13 states the same paper independently at its own end of these edges and
  agrees.** **This accession is also what the orphan key *Proceedings of the National Academy of
  Sciences* below names.**
- **PMC4463930** — **partial.** A review titled *Turning a Negative into a Positive: Ascending
  GABAergic Control of Cortical Activation and Arousal*; PMC4463930. **Rodent-based review.**
  *(**Author list, journal, volume, pages and year not obtained from a publisher record** — only
  the title and the accession.)* **Two findings.** **First, it is a review and the citing line calls
  it Class 1**, which in this source means primary measurement; **owed: reclassify, or name the
  primary paper it stands in for.** **Second, it bears on the ambiguity the reticular entry itself
  declares as owed.** That entry cites it for a pallidal and nigral input and records that whether
  those fibres terminate on the sheet or directly on the relay nuclei is not distinguished at either
  end. **The passage surfaced by the search states that the substantia nigra pars reticulata's
  output tonically inhibits the motor thalamus and the centromedian–parafascicular nucleus** —
  relay nuclei, not this sheet — **which leans toward the second horn.** **One retrieved passage,
  not a reading of the paper: a candidate for opening the review, not a resolution.** It remains the
  case that the accession is used at two lines for different claims about different sources, which
  the partial resolution does not explain.
- **PMC4764559** — **owed**: not searched. **A bare accession**, carrying the cholinergic
  sleep-promotion result, which the reticular entry itself flags as the surprising sign.
- **PMC6018949** — **owed**: not searched. **A bare accession**, carrying the layer-6b absence.
- **Proceedings of the National Academy of Sciences** — **resolved: not a separate source.** The
  citing line gives the journal name with no volume, page, year or author, attached to accession
  *PMC4371918*. **It is that accession's journal** — Kim et al. 2015 — see that entry for the full
  reference. **Owed at the citing line: fold it into the accession's reference, or drop it.**
- **PubMed 3584546** — **owed**: not searched. **A bare accession**, and it carries the most
  specific quantitative claim in the reticular-nucleus entry — that 76% of ventrobasal relay axons
  gave visible collaterals, so roughly a quarter did not.
- **Ralston 2003** — **owed**: not searched. One of the three rebuttal-side keys in the
  contested-nucleus dispute.
- **Saalmann 2012** — Saalmann, Y.B., Pinsk, M.A., Wang, L., Li, X. & Kastner, S. (2012). The
  pulvinar regulates information transmission between cortical areas based on attention demands.
  *Science* 337(6095): 753–756; doi 10.1126/science.1223082; PubMed 22879517. **Macaque**,
  behaving, spatial-attention task. Diffusion-tensor mapping of pulvino-cortical networks with
  simultaneous spike and field-potential recording from the connected sites. *(Verified against the
  Science publisher record and PubMed, 2026-08-23.)* **And the method is not what the citing line
  says it is.** The pulvinar entry groups this paper with *Zhou 2016* as **"the inactivation
  effects … causal"**. **This study inactivates nothing** — it is correlational recording plus
  connectivity mapping, and its causal language is about directed influence inferred from
  synchrony, not about a manipulation. **Owed at the citing line: separate the two keys** — one
  supports the synchrony and inter-areal coherence claim, the other the silencing claim, and only
  the second is an inactivation.
- **Schmitt / Halassa et al., Nature 2017** — Schmitt, L.I., Wimmer, R.D., Nakajima, M., Happ, M.,
  Mofakham, S. & Halassa, M.M. (2017). Thalamic amplification of cortical connectivity sustains
  attentional control. *Nature* 545(7653): 219–223; doi 10.1038/nature22073; PubMed 28467827;
  PMC5570520. **Mouse.** Representation of two attention-guiding rules recorded in prefrontal
  cortex, with optogenetic manipulation of the mediodorsal nucleus. *(Verified against the Nature
  publisher record, PubMed and PubMed Central, 2026-08-12.)* **The paper's own summary is the
  payload the mediodorsal entry declares** — the mediodorsal nucleus amplifies the functional
  connectivity of prefrontal cortex, sustaining cortical representations of rule sets **without
  relaying categorical information**. **The key names the first and the senior author and no one
  between**, which is a compound short form; the full list is above. **This key is shared with file
  11**, where the same paper carries the consumer end of these five edges, and the two files'
  statements of it agree. **The species caveat is already in the file** and it is the load-bearing
  one: one mouse study supplies the payload on five human thalamocortical edges here and five more
  there.
- **Sherman & Guillery** — **partial, and the key resolves to two editions of one work.**
  Sherman, S.M. & Guillery, R.W. (2000). *Exploring the Thalamus*. Academic Press; ISBN
  978-0-12-305460-9. And Sherman, S.M. & Guillery, R.W. (2006). *Exploring the Thalamus and Its Role
  in Cortical Function*, second edition. MIT Press; ISBN 0-262-19532-1. **Both define the
  driver / modulator distinction and the first-order / higher-order relay distinction**, which is
  what this file's four citing entries use the key for; the second edition expands the cortical-
  function argument. *(Verified against the MIT Press and Elsevier publisher records, 2026-08-23,
  for the existence and identity of the two editions. **Which edition any citing line rests on is
  not recoverable from the file, and no page was opened** — so the binding of claim to source is
  unverified and the resolution between editions is a reading, Class 2.)* **Owed at the citing
  lines: name the edition.** **It is a synthesis, not a primary report**, which is what the citing
  lines' Class 3 already says. It is used at four entries in this file, so **it is the most
  load-bearing of the untitled keys.**
- **Willis and colleagues 2001/2002** — **partial.** The search for the Blomqvist paper surfaced a
  critical review of the proposed ventromedial-posterior nucleus's role in pain, hosted as a 2002
  Willis document, which is consistent with what the contested-nucleus line cites it for. **No
  author list, journal, volume, pages or year was obtained from a publisher record**, and the
  file's own key hedges between two years. **Owed: resolve the year and get the reference.**
- **Zhou 2016** — Zhou, H., Schafer, R.J. & Desimone, R. (2016). Pulvinar-cortex interactions in
  vision and attention. *Neuron* 89(1): 209–220; doi 10.1016/j.neuron.2015.11.034; PubMed 26748092;
  PMC4723640. **Macaque**, awake, spatial-attention task. Simultaneous recording from the pulvinar,
  V4 and inferotemporal cortex, with reversible pulvinar deactivation by muscimol.
  *(Verified against the Cell Press publisher record, PubMed and PubMed Central, 2026-08-23.)*
  **Half of what the citing line rests on it does not say, and this is the sharpest finding of the
  reference pass.** The pulvinar entry's two-part payload — that the pulvinar's output *reflects*
  its cortical driver's content and *adds* coordination — is argued from the claim that **"silencing
  the pulvinar leaves cortical receptive fields intact but removes the attentional gain, the gamma
  synchrony, and the inter-areal coherence."** The paper's own abstract gives the second half and
  **contradicts the first**: deactivation produced *a reduction of sensory-evoked responses and
  overall gamma coherence within V4*, and *severe behavioural deficits in the affected portion of
  the visual field*, alongside an increase in low-frequency oscillations associated with inattention
  or sleep — its conclusion being that the pulvinar is necessary *for normal sensory processing* as
  well as for attention. **Cortical responses are not left intact.** **Owed at the pulvinar entry:
  the "reflects content, adds coordination" framing is the entry's Class-2 synthesis and its
  strongest supporting result does not hold as stated. Re-state the claim against the paper, or
  withdraw the framing.** *(That the citing line misreads the paper is Class 1, read off the
  abstract. That the framing above it is thereby weakened is Class 2 — Claude's reading, offered to
  be checked.)*
