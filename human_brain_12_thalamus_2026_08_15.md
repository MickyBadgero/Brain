# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-15
---

---

# FILE 12 OF 20 — THALAMUS

**What is in this file.** The thalamic nuclei that are not sensory relays: mediodorsal, pulvinar, the posterior/ventromedial-posterior interoceptive relay, the motor ventral anterior/ventral lateral group, the anterior and intralaminar nuclei, the reticular nucleus, and the zona incerta.

**Size:** 1140 lines, ~25.7k tokens / ~100 kB (estimated from bytes, not tokenised; kB = 1024 bytes, truncated). **Entries:** 9. **Edge lines:** 82 — 37 in, 45 out. **Internal structure slots:** 9 of 9. **Pass stamps:** 9 of 9. *(The nucleus reuniens entry was created 2026-08-15 with five edges, four of them written at their far end in file 8 the same day and all four two-ended at both ends; two further limbs — the prefrontal return and the reticular collateral — were deliberately not written and are recorded as research owed.)* **Reference keys:** 36, over 40 mentions. **Abbreviations:** cleared 2026-07-27, case-exact grep returning nothing.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file, with the date each was last worked:**

- **Mediodorsal nucleus — the prefrontal relay** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: the class output "prefrontal cortex (all divisions)" split into five named consumers declared in file 11; the compound amygdala / olfactory input split; the basal-ganglia input given its two named source nuclei from file 9; missing Internal structure slot added
- **Pulvinar — the large visual / associative nucleus** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: the class output split into four named consumers declared in files 1, 4 and 5; a **false internal cross-reference corrected** — this entry cited a superior colliculus entry "elsewhere in this file" and that entry is in file 14; missing Internal structure slot added
- **Posterior / ventromedial-posterior thalamus (posterior nuclear group) — the interoceptive relay** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-19: prose slots converted to typed edges — three labelled lines with measured conduction latencies, thalamic separation of thermal from nociceptive
- **Ventral anterior / ventral lateral nuclei — the motor relay** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: prose Inputs and Outputs converted to typed edges; four edges typed from far ends that had marked them **owed at this file**; missing Internal structure slot added
- **Anterior nuclei — the limbic / memory relay** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: prose slots converted to typed edges against files 8 and 17; missing Internal structure slot added
- **Intralaminar nuclei (centromedian / parafascicular) — arousal + striatal drive** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: prose slots converted to typed edges; the striatal output given its sector split, which file 9 records this end as owing; the "cortex (diffuse)" class recorded as unresolved; missing Internal structure slot added
- **Nucleus reuniens — the midline hippocampal–prefrontal conduit** — pass 2026-08-15 — **entry created**; the midline nuclei had no entry anywhere in the source and the string *reuniens* appeared in none of the twenty files, while four edges in file 8 terminated here; all four written and two-ended, the area 25 input written with its far end owed at file 11, and the matrix / core cell classes named as sub-elements
- **Thalamic reticular nucleus — the inhibitory gate** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: the prose Outputs slot converted to typed edges naming four relay-nucleus consumers; the perigeniculate naming collision stated at the entry that owns it; missing Internal structure slot added
- **Zona incerta — the subthalamic inhibitory hub (ventral diencephalon / subthalamus)** — pass 2026-07-27 — abbreviations cleared; standard, from 2026-07-24: prose Inputs and Outputs converted to typed edges; the near-whole-brain afferent class recorded as unresolved; missing Internal structure slot added

**Files read beside this one in the 2026-08-15 pass and not modified:** 8 (medial temporal lobe), 11 (frontal lobe). **The same pass removed eight marks that made a data claim wait on a person's reading** and replaced each with the state the line is actually in; **verification of data runs to the literature and stops there, and nothing in this file waits on a reader.** One mark survived the pass as an appeal to Micky and is correct to: the per-area gating conclusion at the mediodorsal entry is **instruction** about how this source treats gating, not a claim about the brain, and instruction has no rung above him.

**Files read for reference in the 2026-07-24 pass and not modified:** 1 (visual pathway), 2 (auditory pathway), 4 (dorsal visual / parietal stream), 5 (sensorimotor loop), 8 (medial temporal lobe), 9 (basal ganglia), 10 (cerebellum), 11 (frontal lobe), 13 (neuromodulatory systems), 14 (brainstem / midbrain / hypothalamus), 17 (insula / claustrum / habenula / cingulate remainder), 20 (loop structure). **Not read, so unchecked:** 3 (other senses), 6, 7, 15, 16, 18, 19.

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

***A note on the 2026-07-27 pass.*** *Every abbreviation in this file was spelled out in full,
case-exact, under §6a. The six entry headings that carried a bare letter-string no longer do —
an abbreviation in a heading is the worst place for one, because a heading is what other files
quote when they name an endpoint. Strings removed, with the meaning that condemned each where
one exists:* **SNr** *(signal-to-noise ratio, one letter of case away),* **STN** *(spatial
transformer network),* **Pf** *(petaflop),* **Po** *(polonium),* **MD** *(Doctor of Medicine),*
**PFC** *(perfluorocarbon),* **DBS** *(database),* **GPi**, **SMA**, **S1**, **VP** *and*
**VMpo** *(each already on §6a's offender list),* **LGN**, **MGN**, **TRN**, **ZI**, **VA**,
**VL**, **VPL**, **VPM**, **VPI**, **CM**, **DLPFC**, **VLPFC**, **OFC**, **MT**, **V5**,
**CGRP**, **SD**, *and the journal and method strings* **PNAS**, **J Neurophysiol**, **J
Neurosci**, **Cre**. *Nothing was kept as an abbreviation, so no per-string cross-field
research is owed — spelling out is collision-proof by construction. No claim, edge, payload,
number or slot state was changed.*

***A note on the 2026-07-24 pass.*** *Before it, four of this file's eight entries carried their
Inputs and Outputs as **prose lists** — "internal globus pallidus / substantia nigra pars
reticulata (basal-ganglia output), cerebellar deep nuclei (dentate); reciprocal motor cortex"
was the whole of the ventral anterior / ventral lateral Inputs slot. A prose list makes no
checkable claim, so it cannot fail a two-ended diff, and four other files had already recorded
edits **owed at this file** against exactly those slots — files 5, 9, 10 and 11 each name a
thalamic nucleus here, declare the payload at their own end, and record that this end carries
it untyped. The conversion did not discover most of what is marked owed below; it made
it visible. **Seven of the eight entries had no Internal structure slot**, which §3 requires of
every entry.*

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
    source nuclei** (file 9), which is where the two names come from — this end read "basal ganglia
    (internal globus pallidus / substantia nigra pars reticulata)" as a single line until
    this pass. **Split now.**
  - **← the amygdala** — **carries:** limbic value / significance context. **Payload otherwise
    unknown — owed. Fan-in:** unknown. **The producer declares it** (file 8, written there
    2026-07-23 from this entry's own declaration), so this edge is now two-ended.
    *(Caution under §4: both ends descend from the same sentence at this end, so the agreement
    certifies nothing. It is two-ended in form, not yet in evidence.)*
  - **← olfactory / limbic cortex** — **carries:** limbic value / significance context. **Payload
    otherwise unknown — owed. Fan-in:** unknown. **This endpoint names a class, not a region with
    an entry of its own**, and cannot be checked as written. **Owed: resolve it to named
    producers.** *(Split this pass from a line that named the amygdala and this class together;
    their far ends have different statuses — one declares the edge, one is not a region.)*
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
    *(All five split this pass from one line reading "→ prefrontal cortex (all divisions)" — a
    class endpoint under §9b, answered by five named consumers in file 11. The payload is
    unchanged and is the one this entry already carried; only the arity changed. Class 1 —
    "amplifies local connectivity, sustains representations without relaying
    categorical information, scaffold not source": Schmitt / Halassa et al., Nature 2017,
    optogenetic silencing with prefrontal electrophysiology, mouse; the principle is taken as
    general to the mediodorsal–prefrontal loop. The framing as amplification-and-modulation
    rather than a content
    payload was Micky's reading, which is not itself verification of anything — the measurement under
    it is the Schmitt / Halassa study named above, **verified against the journal record 2026-08-12**.
    **Whether the five consumers receive
    the same amplification or differently-tuned ones is not stated at either end — owed.**)*
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only** — that entry's Inputs take "collaterals of cortico-thalamic and thalamo-cortical
    axons" as a class covering every thalamic nucleus including this one. **Written now**, and the
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: the class output "prefrontal cortex (all divisions)" split into five named consumers declared in file 11; the compound amygdala / olfactory input split; the basal-ganglia input given its two named source nuclei from file 9; the reticular-nucleus collateral written from its consumer; missing Internal structure slot added

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
    not stated at either end. Owed.** *(Split this pass from a line that named the reticular
    nucleus and this class together.)*
    *(Input laminar / driver-modulator identities: Class 3 general thalamic anatomy plus Class 1
    mouse rabies tracing (Journal of Neuroscience 2025); verified for the source 2026-07-14.)*
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
    Gattass, cebus) and for the inactivation effects (Zhou 2016, Saalmann 2012, awake macaque,
    causal) — silencing the pulvinar leaves cortical receptive fields intact but removes the
    attentional gain, the gamma synchrony, and the inter-areal coherence. Class 2 for the two-part
    "reflects content + adds coordination" framing — Claude's synthesis of those two result sets,
    offered to be checked. **The framing was accepted by Micky on 2026-07-14; that is not verification,
    and the two result sets under it carry their own keys above.** Targets reciprocal, onto
    layer 4 and the input layers.)*
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input. **Written now.**
- **Internal structure and internal data flow:** **owed.** The subdivisions are named in this
  file's own material — an **anterior pulvinar** is named at the output edge to the second
  somatosensory area, and the medial, lateral and inferior divisions are standard in the
  literature the number slots draw on — but no sub-element set and no internal edges are written.
  **This slot is load-bearing here rather than cosmetic**, because two of this entry's output
  edges declare different payloads (visual/coordinating versus deep-receptor) and the most likely
  reconciliation is that they leave from different subdivisions.
- **A false cross-reference, corrected 2026-07-24.** Until this pass the provenance note on the
  collicular input read that the colliculo-pulvinar-cortical route "is already stated elsewhere in
  this file at the superior colliculus entry." **There is no superior colliculus entry in this
  file.** It is in file 14. This is the same defect class corrected on 2026-07-23 at file 14's
  preamble and file 10's closing paragraph, both of which reported the pontine nuclei as described
  where they were not: **a file asserting that it contains a region it does not contain reads as
  complete from inside, and no check that stays within one file can catch it.**
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: the class output split into four named consumers declared in files 1, 4 and 5, with a payload disagreement at the anterior-pulvinar edge recorded not resolved; the compound inhibitory input split; a false internal cross-reference to a superior colliculus entry corrected — that entry is in file 14; missing Internal structure slot added

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
    The morphology–physiology correspondence is near-total in the material: every fusiform cell
    recovered was nociceptive-specific and every pyramidal cell was thermoreceptive-specific.
    A **pruriceptive** (itch) population responding differentially to histamine and cowage is
    reported within the nociceptive group. **Fan-in:** unknown.
    **Latency, measured — one of the few real time figures in this file.** Mean central conduction
    latencies differ by class: **thermoreceptive-specific ≈ 59 ms** (standard deviation 25,
    n = 136), **polymodal nociceptive ≈ 72 ms** (standard deviation 28, n = 128),
    **nociceptive-specific ≈ 131 ms** (standard deviation 56, n = 100). So the three lines do
    not arrive together, and the cold signal precedes the nociceptive one by roughly 70 ms.
    *(Class 1 — morphology/physiology: Han, Zhang & Craig, Nature Neuroscience 1:218, 1998, cat,
    intracellular recording and labelling of 38 lamina I neurons. Latencies and response classes:
    Craig, Krout & Andrew, Journal of Neurophysiology 86:1459, 2001, cat, antidromically
    identified spinothalamic neurons with quantitative thermal and mechanical stimuli. Primate
    confirmation of the three classes projecting here: Dostrovsky & Craig 1996; Journal of Neuroscience
    17:3274, 1997, monkey.
    **Species: cat for the numbers. Candidates:** of the four keys on this line, two are searched to a
    full reference and two read **owed** in the reference section — so the line is part verified and
    part unopened, and it does not currently say which claim rests on which.)*
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
    end only**, as part of that entry's class input. **Written now.**
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-19: prose slots converted to typed edges — three labelled lines with measured conduction latencies, thalamic separation of thermal from nociceptive

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
    nuclei** (file 9), and recorded **"Owed at file 12: type it"** against this end. **Typed now.**
  - **← the deep cerebellar nuclei, chiefly the dentate** (via the superior cerebellar peduncle,
    decussating) — **carries:** the cerebellar **correction** — the forward-model error correction
    that shapes an action already selected. **Fan-in:** unknown. **Fan-out at the producer:** the
    cerebellar-cortex to output-nucleus areal ratio is **~85 : 1**, a massive convergence. **The
    producer declares it** (file 10) and recorded **"Owed at file 12: type it"** against this end.
    **Typed now.** **Because both the corticopontine input and this output cross, each cerebellar
    hemisphere serves the contralateral cortex and the ipsilateral body.**
  - **← the primary motor cortex** (corticothalamic, reciprocal) — **carries:** payload **owed** at
    both ends. **Fan-in:** unknown. **The producer declares it** (file 5), which wrote this edge on
    2026-07-23 having found that this entry listed "reciprocal motor cortex" while the far end
    declared only the ascending limb.
  - **← the thalamic reticular nucleus** — **carries:** inhibition; a gain/gate control, no
    content. **Fan-in:** unknown. **The producer is in this file** and declares this nucleus among
    its named consumers.
- **Outputs:**
  - **→ the primary motor cortex** — **carries:** the basal-ganglia *selection* (which action is
    released) and the cerebellar *correction* (how it is shaped), **combined on one relay.**
    **Fan-out:** unknown. **The consumer declares it and types it** (file 5), and recorded **"Owed
    as a cross-file edit at the ventral anterior / ventral lateral entry (file 12): type it."**
    **Typed now, from the consumer's declaration.**
  - **→ the premotor cortex and the supplementary motor areas** — **carries:** the same combined
    selection-and-correction payload. **Fan-out:** unknown. **The consumer declares it and types
    it** (file 11), and recorded **"Owed at file 12: type it."** **Typed now.**
  - **→ prefrontal cortex** — **carries:** payload **owed. Fan-out:** unknown. **This endpoint
    names a class.** File 10 declares the cerebellar limb of this relay as reaching "motor,
    premotor and prefrontal cortex," and no prefrontal entry in file 11 declares this nucleus as an
    input — the five that declare a thalamic input name the **mediodorsal** nucleus instead.
    **So either this limb is missing at its consumers or it does not exist. Owed, and it is the
    load-bearing gap in this entry**, because it decides whether the cerebellar loop reaches
    prefrontal cortex at all.
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input. **Written now.**
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: prose Inputs and Outputs converted to typed edges; four edges typed from far ends in files 5, 9, 10 and 11 that had recorded them as owed at this file; the prefrontal output found to be declared by no consumer and recorded as the entry's load-bearing gap; missing Internal structure slot added

## Anterior nuclei — the limbic / memory relay

- **Function:** the memory relay of the Papez circuit — mammillary bodies → anterior thalamus
  → cingulate / retrosplenial cortex; supports episodic memory and spatial orientation.
- **Inputs:**
  - **← the mammillary bodies**, via the **mammillothalamic tract** — **carries:** payload
    **owed. Fan-in:** unknown. **The producer has an entry in file 14** (hypothalamus), which names
    the Papez limb; whether it declares this edge with a payload was **not checked at that end this
    pass. Owed as a cross-file check at file 14.**
  - **← the subiculum**, via the **post-commissural fornix** — **carries:** a **completed
    episode** — the bound, retrievable pattern, addressable by any fragment of itself. **Payload
    only partly writable — owed:** "an episode" has no units and no frame, and what makes it
    checkable is a property rather than a type — it is **content-addressable**, which the upstream
    identity codes are not. **Fan-in:** unknown. **The producer declares it and types it** (file 8),
    which names the mammillary bodies and this nucleus together on one edge. **Typed now from the
    producer's declaration.**
- **Outputs:**
  - **→ the retrosplenial cortex** — **carries:** payload **owed. Fan-out:** unknown. **The
    consumer declares it** (file 17), naming this nucleus as the anterior-thalamus limb of the
    Papez circuit and declaring the return arm below.
  - **→ the anterior cingulate cortex** — **carries:** payload **owed. Fan-out:** unknown. **The
    consumer is in file 11**, whose anterior cingulate entry declares a thalamic input from the
    **midline / intralaminar** thalamus and **not** from this nucleus. **So this edge is declared at
    one end only, and the cingulate half of the classical Papez target is unconfirmed at its
    consumer. Owed as a cross-file edit at file 11.**
  - **← → the retrosplenial cortex, reciprocally** — the consumer declares a return projection to
    "the anterior thalamus" (file 17), which is this nucleus. **Recorded here as an input this
    entry does not carry: owed** — the Inputs slot above has no cortical line at all, and a
    reciprocal loop needs one.
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this nucleus's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's
    end only**, as part of that entry's class input. **Written now.**
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: prose slots converted to typed edges against files 8 and 17; the subicular input typed from its producer; the cingulate output found undeclared at its consumer and recorded as owed at file 11; the retrosplenial return limb recorded as a missing input; missing Internal structure slot added

## Intralaminar nuclei (centromedian / parafascicular) — arousal + striatal drive

- **Function:** the "nonspecific" nuclei — arousal and alertness, plus a major direct
  excitatory input to the striatum (a thalamostriatal drive parallel to cortex): the
  centromedian nucleus → motor striatum, the parafascicular nucleus → associative / limbic
  striatum.
- **Inputs:**
  - **← the reticular formation** (brainstem) — **carries:** payload **owed**; the arousal drive
    this entry's Function names. **Fan-in:** unknown. **The producer has an entry in file 14**,
    whose closing summary names the ascending reticular activating system reaching the intralaminar
    thalamus. **Whether that entry declares this edge with a payload was not checked this pass.
    Owed as a cross-file check at file 14.**
  - **← the deep cerebellar nuclei** — **carries:** payload **owed. Fan-in:** unknown. **The
    producer declares it** (file 10), which wrote this edge on 2026-07-23 from this entry's prose
    list and marked its own payload owed.
  - **← the lateral parabrachial nucleus** — **carries:** payload **unknown — owed. Fan-in:**
    unknown. **The producer declares it** (file 14), naming this group and the ventroposterior
    parvicellular thalamus together. **Recorded now from the producer's declaration**; this entry's
    prose list did not name it.
  - **← the internal globus pallidus and the substantia nigra pars reticulata** — **carries:**
    payload **owed. Fan-in:** unknown. This entry's prose list named "basal-ganglia" as an input
    class; **whether file 9 declares an output to this group was not confirmed this pass** — that
    file's declared thalamic targets are the ventral anterior / ventral lateral group, the
    mediodorsal nucleus and the reticular nucleus. **Owed: confirm or delete.**
  - **← cerebral cortex** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint names a
    class** and cannot be checked as written. **Owed: resolve it to named producers.**
- **Outputs:**
  - **→ the motor striatum**, from the **centromedian nucleus** — **carries:** arousal and a
    thalamostriatal drive parallel to cortex. **Payload otherwise unknown — owed. Fan-out:**
    unknown. **The consumer declares it** (file 9) and records that the sector split —
    centromedian to motor striatum — is **"a sub-element-level statement this end does not carry,"**
    with **"Owed here: say which striatal sector each nucleus reaches."** **Written now from this
    end, which is the end that holds the split.**
  - **→ the associative / limbic striatum**, from the **parafascicular nucleus** — **carries:** the
    same thalamostriatal drive. **Payload otherwise unknown — owed. Fan-out:** unknown. **Same
    consumer declaration and the same owed sector split** (file 9).
  - **→ the anterior cingulate cortex** — **carries:** payload **unknown — owed. Fan-out:**
    unknown. **The consumer declares it** (file 11) as an input from "the midline / intralaminar
    thalamus," and records that **the producer declares its cortical target as a class** —
    "cortex (diffuse)" — **"which covers this area without naming it,"** with the edit **owed at
    this file. Named now**, which discharges that owed edit for this consumer only.
  - **→ further cortex, diffusely, beyond the anterior cingulate** — **carries:** payload
    **owed. Fan-out:** unknown. **This endpoint names a class** and is the residue of the "cortex
    (diffuse)" line the named edge above was split out of. **Owed: resolve it to named consumers**
    — files 2, 3, 4, 8 and 17 all name the intralaminar nuclei and were not all checked for
    consumer declarations this pass.
  - **→ the thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:**
    a copy of this group's outgoing traffic. **Fan-out:** unknown. **Declared at the consumer's end
    only**, as part of that entry's class input. **Written now.**
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: prose slots converted to typed edges; the striatal output split by sector, which file 9 records this end as owing; the anterior cingulate named out of the "cortex (diffuse)" class, discharging file 11's owed edit for that consumer; the parabrachial input recorded from its producer in file 14; the basal-ganglia input recorded as unconfirmed; missing Internal structure slot added

## Nucleus reuniens — the midline hippocampal–prefrontal conduit

*(Entry added 2026-08-15. **It did not exist, and four edges written in file 8 on the same day
terminate on it.** The midline thalamic nuclei were named nowhere in the source before this entry:
a case-exact search of all twenty files for* reuniens *returned nothing, and the intralaminar entry
above holds the centromedian and parafascicular nuclei only, recording the remaining **intralaminar**
members as owed and the **midline** group not at all. **The two groups are not the same group**, and
the file's coverage statement did not distinguish them.)*

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
    its own 2026-07-24 research note records **"virtually all nuclei" *and the midline caveat*** as
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
  **White-matter volume:** unknown. **Myelination:** unknown. *(No stereological figure was sought
  in this pass; the Pakkenberg / Dorph-Petersen lineage this file leans on elsewhere may carry one.
  **Owed.**)*
- **What this entry does to the file's coverage claim.** This file's opening statement lists the
  nuclei it holds and did not name a midline group, so **the absence read as a decision about scope
  rather than as a gap.** It was a gap: four edges in another file had nowhere to land, and the one
  loop in the source that runs hippocampus → prefrontal cortex → thalamus → hippocampus could not be
  followed around. **A file's own contents list is not evidence that what it omits was considered**,
  and this is the second region-shaped hole found by writing an edge from the far end rather than by
  reading the file that should have held it.
- **Pass:** 2026-08-15 — entry created from the primate tracing that produced file 8's four reuniens
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
  *(This sentence read "Every cortico-thalamic and thalamo-cortical axon passes through and drives
  it" until 2026-07-24. The universal form is contradicted by the literature searched that day and
  is corrected here; the exceptions are the reason the correction matters, because a sheet that
  monitors *most* traffic is a different gate from one that monitors all of it.)*
- **Inputs:**
  - **← collaterals of cortico-thalamic and thalamo-cortical axons** — **carries:** a copy of the
    traffic in both directions, which is what lets this sheet gate what it monitors. **Fan-in:**
    unknown. **This endpoint names a class, and the class is not exempt from §3, because the
    universal claim that would have exempted it is false.** Researched 2026-07-24. The exceptions,
    on both halves:
    - **Corticothalamic, layer 6a** — collateralises here. This is the canonical top-down input to
      this sheet.
    - **Corticothalamic, layer 5** — generally does **not** innervate this sheet; the layer-5
      driver axons reach the higher-order nuclei without the feed-forward inhibition the layer-6
      route carries. **One region-specific exception:** layer 5 pyramidal cells of **frontal
      cortex**, and not of other cortical regions, make **monosynaptic** connections here — a
      direct connection rather than a passing collateral, with morphology and physiology distinct
      from the layer-6 route.
    - **Corticothalamic, layer 6b** — targets higher-order thalamus and sends **no** collaterals
      here, confirmed by single-cell tracing.
    - **Thalamocortical** — collaterals arise from *virtually* all thalamic nuclei, not all: in the
      one nucleus where the fraction was counted, **76% of ventrobasal relay axons followed into
      the internal capsule gave visible collaterals here**, so roughly a quarter did not. Midline
      nuclei are the least strictly organised, and a paraventricular projection to this sheet has
      **not been described** though the reverse projection has.
    **So the six thalamic collaterals written this pass** — mediodorsal, pulvinar,
    posterior / ventromedial-posterior, ventral anterior / ventral lateral, anterior nuclei
    and intralaminar — **are individually
    warranted rather than instances of a universal, and the cortical half must be resolved to named
    producers by layer. Owed: split this line by producer and layer.**
    *(Class 1 — layer-5 frontal exception: Nature Neuroscience 2022 (PMC9829539), mouse,
    optogenetics with paired recording; layer-6b absence: PMC6018949, mouse,
    Cre-recombinase-dependent viral and single-cell tracing; ventrobasal 76%: intracellular
    horseradish-peroxidase fill with serial reconstruction, rat, PubMed 3584546; "virtually
    all nuclei" and the midline caveat: a review summary. **Web search was run on 2026-07-24
    and these are secondary and abstract-level reads — no primary paper was opened in full.**
    **Candidates:** what was opened was not the record that would settle these exceptions.)*
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
    it** (file 9), which wrote this edge on 2026-07-23 and carried this end's ambiguity with it:
    **whether these terminate on this nucleus or directly on the relay nuclei is not distinguished
    at either end and is owed.** File 9 states the consequence plainly — if they terminate on the
    relay nuclei directly, this edge and its two thalamic edges are the same projection described
    twice. *(Class 1 — PMC4463930.)*
  - **← the zona incerta** — **carries:** GABAergic inhibition; **payload owed. Fan-in:** unknown.
    **The producer is in this file**, and declares its signature target as the higher-order
    posterior thalamus rather than this sheet. **The same terminate-here-or-on-the-relay ambiguity
    applies and is owed.** *(Split this pass from a line that named the pallidal, nigral and
    incertal sources together.)*
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
  - **→ the anterior nuclei and the intralaminar nuclei** — **carries:** inhibition. **Fan-out:**
    unknown. **Neither consumer in this file declares an input from this sheet**, though Function
    claims this nucleus inhibits the other thalamic nuclei generally. **Owed: confirm at those two
    entries or narrow the Function claim.**
    *(All eight split this pass from one prose line reading "inhibitory → the thalamic relay nuclei
    (not cortex)" — a class endpoint under §9b. The seven consumers that declare an input from this
    sheet supplied the names; the eighth line records the two that do not.)*
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: the Function slot's universal claim that every corticothalamic and thalamocortical axon drives this sheet corrected to "most, but not all," with the layer-5, layer-6b and thalamocortical exceptions researched and recorded; the prose Outputs slot converted to eight typed edges naming seven consumers that declare an input and two that do not; the extrathalamic GABAergic input split into pallidal, nigral and incertal lines, each carrying file 9's terminate-here-or-on-the-relay ambiguity; the perigeniculate naming collision stated at the entry that owns it; missing Internal structure slot added

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
  flight), sleep, visceral activity, and pain gating** (the "integrative node for global
  behavioural modulation" reading; Mitrofanis 2005).
- **Inputs:**
  - **← the central nucleus of the amygdala**, onto this structure's **parvalbumin neurons** —
    **carries:** payload **owed**; this producer's role in the pair is given at this end as fear.
    **Fan-in:** unknown. **The producer declares it** (file 8), written there 2026-07-23 from this
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
    entry in file 14; whether it declares this edge was not checked this pass. Owed as a cross-file
    check.**
  - **→ the periaqueductal gray** (defensive behaviour) — **carries:** payload **owed. Fan-out:**
    unknown. **The consumer has an entry in file 14; not checked this pass. Owed.**
    *(Class 1 — Chou et al. 2018.)*
  - **→ the ventral tegmental area** (feeding drive) — **carries:** payload **owed. Fan-out:**
    unknown. **The consumer has an entry in file 13; not checked this pass. Owed.**
  - **→ the rostral ventromedial medulla** (descending pain control) — **carries:** payload
    **owed. Fan-out:** unknown. **File 14 holds the rostral and caudal ventrolateral medulla
    entries; whether the ventromedial medulla has an entry was not confirmed this pass. Owed —
    this may be a named region with no entry**, in which case it belongs in §9a of the design file.
  - **→ the cerebral cortex** — **carries:** payload **owed. Fan-out:** unknown. **This endpoint
    names a class. Owed: resolve to named consumers.**
  - **→ the spinal cord** — **carries:** payload **owed. Fan-out:** unknown. **The consumer has an
    entry in file 16; not checked this pass. Owed as a cross-file check.**
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
- **Pass:** 2026-07-27 — abbreviation clearance under §6a: every letter-string in this entry spelled out in full, no content changed; standard, from 2026-07-24: prose Inputs and Outputs converted to typed edges, eight outputs from one prose line; the amygdalar input typed against file 8; the near-whole-brain afferent field recorded as seven unresolved class endpoints; the rostral ventromedial medulla flagged as a possible region with no entry; missing Internal structure slot added

---

## References

*(Section added 2026-08-12 under source design §2a; **statuses corrected 2026-08-15.** Each full
reference given here was obtained by a web search run against publisher, journal or PubMed records —
so **a key given in full is verified against that record**, per §2a's rule that searching *is* the
verification. Keys reading **owed** were not searched, and the citation text for those keys, wherever
it appears in this file, was written from recall. Keys reading **partial** were resolved only against
a secondary listing and remain candidates, because a secondary listing can propagate an error in the
very fields it is consulted for.)*

***What was corrected on 2026-08-15.*** *This section previously read that every line below was a
candidate* **awaiting Micky's verification** *and that none was verified. Both halves were wrong: the
searched keys were verified at the moment they were searched, and verification of data does not run
to a person at all — the ladder tops out at the literature for a source file. **The same pass removed
eight such marks from this file's entries**, replacing each with the state the line is actually in.
**Two of the eight were not wording at all**: one attributed a payload framing to Micky as though the
attribution verified it, and one attributed a per-area conclusion to him as a standing position —
**the second of those turns out to be instruction rather than data**, and so is the one place in this
file where verifying against him is correct.*

**37 distinct keys, 45 mentions. 6 verified against a publisher, journal or PubMed record; 3 partial
— secondary listings only, still candidates; 1 resolved as not a separate source; 27 owed.** *(One key
added 2026-08-15 with the nucleus reuniens entry.)* *(Revised 2026-08-12 later the same day: *PMC4371918* was resolved
while working file 13, which cites the same accession, and that resolution also identified the
orphan *Proceedings of the National Academy of Sciences* key and gave a partial for *PMC4463930*.
**Three of this file's bare accessions are shared with file 13** — *PMC4371918*, *PMC4463930* and
*PMC4764559* — and the two files independently support the same two edges from opposite ends.)*

**This file's keys are the least well-formed in the source so far, and the shape of that is the
finding.** Of the thirty-six, **six are a bare accession number with no author, title or year
anywhere in the file** — *PMC4371918*, *PMC4463930*, *PMC4764559*, *PMC6018949*, *PMC9829539*
and *PubMed 3584546*. **Two more are a journal, volume and page with no author** — *Journal of
Neuroscience 17:3274, 1997* and *Journal of Neuroscience 2025*, the latter carrying no volume or
page either. **Six are a lineage or an author string with no paper at all** — *Sherman &
Guillery*, *Petersen / Robinson rhesus*, *Gattass, cebus*, and the three stereology-lineage
forms below. **So fourteen of thirty-six keys cannot be matched to a paper by reading the file**,
which is the condition §2a's both-directions check exists to expose. It is not a defect in any
claim; it is a defect in what a reader can do with the claim.

**Five keys name one body of work under five different short forms.** *Pakkenberg /
Dorph-Petersen stereology lineage* (46), *Dorph-Petersen, Byne, Popken* (152), *Dorph-Petersen et
al. 2004* (166), *Pakkenberg / Byne / Popken lineages* (167) and *Dorph-Petersen's review* (505)
are all the human thalamic stereology literature this file's neuron and volume slots rest on.
Only one of the five (line 166) carries a year. **Owed at the citing lines: one key, or say what
distinguishes them.**

**One key appears in two forms.** *Blomqvist, Zhang & Craig 2000* (294) and *Blomqvist, Zhang &
Craig, Brain 123:601, 2000* (357, 387) are the same paper, and both entries below point at each
other.

**One key is shared with file 11, which is §2a's stated case.** *Schmitt / Halassa et al., Nature
2017* carries the mediodorsal payload at both ends of the same edges — five output edges here,
five input edges there — so the two files independently record one source, and a disagreement
between them would be a finding. There is none: the reference and the payload statement match.

**Two searched references confirm the file's numbers exactly, which is worth recording because
most reference work turns up discrepancies.** See the *Craig, Krout & Andrew* entry (three means,
three standard deviations and three sample sizes, all matching) and the *Craig & Dostrovsky*
entry (three projection counts, matching). **One of the two also carries a figure this file does
not** — conduction velocities — noted there.

**Species composition of what has been searched:** of the five papers behind the six
searched-or-partial keys, **three are cat** (the two 2001 Craig papers and, by the file's own
declaration, the Han et al. 1998 morphology work that remains owed), **one is human** (Blomqvist
et al. 2000), **one is macaque** (Craig 2004, partial), and **one is mouse** (Schmitt et al.
2017). **The file already declares "Species: cat for the numbers" at line 341**, and the searching
so far bears that out rather than softening it. Thirty keys are unsearched, so the balance is not
yet legible.


- **Blomqvist, Zhang & Craig 2000** — **the same paper as the key below**, cited under a shorter
  form at one line. See that entry for the full reference. **Owed at the citing lines: use one
  key.** *(searched 2026-08-12; candidate. Line 294.)*
- **Blomqvist, Zhang & Craig, Brain 123:601, 2000** — Blomqvist, A., Zhang, E.-T. & Craig, A.D.
  (2000). Cytoarchitectonic and immunohistochemical characterization of a specific pain and
  temperature relay, the posterior portion of the ventral medial nucleus, in the human thalamus.
  *Brain* 123(Pt 3): 601–619; doi 10.1093/brain/123.3.601; PubMed 10686182. **Human thalamus,
  post-mortem.** Cytoarchitectonics with immunohistochemical labelling for **calbindin, substance P
  and calcitonin gene-related peptide**. *(Oxford University Press publisher record and PubMed.)*
  **The entry uses two of the three markers and not the third.** Lines 292–300 and 378–383 carry
  calbindin and calcitonin gene-related peptide; **substance P is in the paper's own method
  statement and appears nowhere in this file.** Whether it distinguishes a third field, or
  co-distributes with one of the two, is not something this pass established. **Owed: say what
  substance P showed, or say the entry does not use it.** **This is also the same paper as
  *Blomqvist, Zhang & Craig 2000* at line 294.** *(searched 2026-08-12; candidate. Lines 357,
  387.)*
- **Byne 2001** — **owed**: not searched in this pass. One of three keys on a single volume figure
  at line 170. *(Line 170.)*
- **Chou et al. 2018** — **owed**: not searched in this pass. *(Line 737.)*
- **Craig 2004** — **partial.** Craig, A.D. (2004). Distribution of trigeminothalamic and
  spinothalamic lamina I terminations in the macaque monkey. *Journal of Comparative Neurology*
  477: 119–148. **Macaque.** *(**Taken from a secondary reference list, not from the publisher's
  record** — the search that surfaced it was for the Blomqvist paper, and no journal or publisher
  page for this one was opened. Volume, pages and year are therefore unconfirmed, and §2a requires
  saying so.)* **Owed: confirm against the publisher.** *(searched 2026-08-12; candidate, partial.
  Line 303.)*
- **Craig & Dostrovsky, Journal of Neurophysiology 86:856, 2001** — Craig, A.D. & Dostrovsky, J.O.
  (2001). Differential projections of thermoreceptive and nociceptive lamina I trigeminothalamic
  and spinothalamic neurons in the cat. *Journal of Neurophysiology* 86(2): 856–870; doi
  10.1152/jn.2001.86.2.856; PubMed 11495956. **Cat**, barbiturate-anaesthetised. Antidromic
  activation from a mobile electrode array, mapping the thalamic projections of **40**
  trigeminothalamic or spinothalamic lamina I neurons. *(American Physiological Society publisher
  record and PubMed.)* **The entry's counts check out.** Lines 342–349 give 20 of 23
  thermoreceptive cells reaching the dorsomedial ventral posterior medial nucleus against 1 of 9
  nociceptive-specific and 0 of 8 polymodal; the paper's characterised sample is nociceptive-
  specific n = 9, polymodal n = 8, thermoreceptive-specific n = 22 plus one warm cell — **which is
  where the 23 comes from**, and the file does not say that the twenty-third is a warm cell rather
  than a cool one. **One thing the entry does not record:** the paper mapped its cells from a total
  identified sample considerably larger than 40, so the 40 is the mapped subset and not the
  recording yield. Neither point changes a claim. *(searched 2026-08-12; candidate. Line 350.)*
- **Craig & Zhang 2006** — **owed**: not searched in this pass. The secondary material surfaced
  while searching Blomqvist describes it as the retrograde-tracing report confirming the selective
  lamina I input and the antero-posterior head-to-foot topography, which is what line 303 uses it
  for; **that is a description, not a reference, and no reference is written from it.** *(Line
  303.)*
- **Craig, Krout & Andrew, Journal of Neurophysiology 86:1459, 2001** — Craig, A.D., Krout, K. &
  Andrew, D. (2001). Quantitative response characteristics of thermoreceptive and nociceptive
  lamina I spinothalamic neurons in the cat. *Journal of Neurophysiology* 86(3): 1459–1480; doi
  10.1152/jn.2001.86.3.1459; PubMed 11535691. **Cat**, barbiturate-anaesthetised. Antidromically
  identified lamina I spinothalamic neurons in the lumbosacral cord, quantitative thermal and
  mechanical stimuli. *(American Physiological Society publisher record and PubMed.)* **Every
  number on the citing line matches the paper.** Nociceptive-specific 130.8 ± 55.5 ms, n = 100;
  polymodal nociceptive 72.1 ± 28.0 ms, n = 128; thermoreceptive-specific 58.6 ± 25.3 ms, n = 136 —
  which lines 330–334 give as ≈131 / 56 / 100, ≈72 / 28 / 128 and ≈59 / 25 / 136. **Nine figures,
  nine matches.** **And the paper carries one the file does not.** It gives the corresponding
  **conduction velocities — 2.5, 4.6 and 5.6 m/s** — which is the transportable form of the same
  measurement, since a latency depends on the path length of the preparation and a velocity does
  not. **Owed: carry the velocities alongside the latencies**, which would also let the cat figures
  be scaled to a human path length rather than transferred whole. *(searched 2026-08-12; candidate.
  Line 337.)*
- **Danos 2003** — **owed**: not searched in this pass. One of three keys on a single volume figure
  at line 170. *(Line 170.)*
- **Dorph-Petersen, Byne, Popken** — **owed**, and **one of five short forms for one lineage**; see
  the note above the list. *(Line 152.)*
- **Dorph-Petersen et al. 2004** — **owed**: not searched in this pass. **The only one of the five
  lineage keys that carries a year**, and therefore the one a search should start from. *(Line
  166.)*
- **Dorph-Petersen's review** — **owed**, and **one of five short forms for one lineage**. Whether
  the review is the 2004 paper above or a separate publication is not stated in the file. *(Line
  505.)*
- **Dostrovsky & Craig 1996** — **owed**: not searched in this pass. Named at line 339 alongside a
  1997 journal string as the primate confirmation of the three classes. *(Line 339.)*
- **Gattass, cebus** — **owed**: not searched in this pass; the key carries no year and no title.
  *(Line 239.)*
- **Graziano & Jones 2004** — **owed**: not searched in this pass. One of the three keys carrying
  the rebuttal side of the contested-nucleus dispute at line 307. *(Line 307.)*
- **Han, Zhang & Craig, Nature Neuroscience 1:218, 1998** — **owed**: not searched in this pass.
  **This is the load-bearing owed key in the file**: it carries the morphology–physiology
  correspondence at lines 322–327 — fusiform, pyramidal and multipolar cells against the three
  response classes — which the entry describes as near-total in the material, on a stated sample of
  38 cat lamina I neurons. *(Line 335.)*
- **Joyce et al. 2022 (Journal of Neuroscience 42(6):1068)** — Joyce, M.K.P., Marshall, L.G., Banik, S.L., Wang, J., Xiao, D., Bunce, J.G. & Barbas, H. (2022). Pathways for memory, cognition and emotional context: hippocampal, subgenual area 25, and amygdalar axons show unique interactions in the primate thalamic reuniens nucleus. *Journal of Neuroscience* 42(6): 1068–1089; doi 10.1523/JNEUROSCI.1724-21.2021; PubMed 34903572. **Rhesus macaque**, 12 animals, both sexes; bidirectional dextran-amine tracer injections into hippocampus, medial prefrontal area 25 and amygdala, with immunohistochemistry, stereological termination density, confocal and electron microscopy. *(Society for Neuroscience journal record; full text read; searched 2026-08-15.)* **Verified.** **This is the sole source for the nucleus reuniens entry**, which is a whole entry resting on one paper — a concentration this file has nowhere else, and worth knowing before the entry's payloads are leaned on. **It also supplies the negative that makes the entry necessary**: medial prefrontal cortex does not project directly to the hippocampus, for which the study cites Cassel et al. 2013. **Owed: read Cassel et al. 2013, since that negative is doing structural work here and is carried at second hand.** *(Nucleus reuniens entry, all lines.)*
- **Journal of Neuroscience 17:3274, 1997** — **owed**: not searched in this pass, **and the key
  names no author.** *(Line 339.)*
- **Journal of Neuroscience 2025** — **owed**: not searched in this pass, **and the key names no
  author, no volume and no page** — a journal and a year only, for the mouse rabies-tracing result
  that types the pulvinar's driver and modulator input laminae. **This is the least identifiable
  key in the file.** *(Line 208.)*
- **Kemether 2003** — **owed**: not searched in this pass. One of three keys on a single volume
  figure at line 170. *(Line 170.)*
- **Mitrofanis 2005** — **owed**: not searched in this pass. *(Lines 704, 712.)*
- **Nature Neuroscience 2022 (PMC9829539)** — **owed**: not searched in this pass. The citing line
  already declares its own limit — web search 2026-07-24, secondary and abstract-level reads, no
  primary paper opened in full. *(Line 616.)*
- **Pakkenberg / Byne / Popken lineages** — **owed**, and **one of five short forms for one
  lineage**. *(Line 167.)*
- **Pakkenberg / Dorph-Petersen stereology lineage** — **owed**, and **one of five short forms for
  one lineage**. *(Line 46.)*
- **Petersen / Robinson rhesus** — **owed**: not searched in this pass; the key carries no year and
  no title. It supports the primate single-unit selectivity claim the pulvinar entry's Function
  slot turns on. *(Line 238.)*
- **PMC4371918** — Kim, T., Thankachan, S., McKenna, J.T., McNally, J.M., Yang, C., Choi, J.H.,
  Chen, L., Kocsis, B., Deisseroth, K., Strecker, R.E., Basheer, R., Brown, R.E. & McCarley, R.W.
  (2015). Cortically projecting basal forebrain parvalbumin neurons regulate cortical gamma band
  oscillations. *Proceedings of the National Academy of Sciences* 112(11): 3535–3540; doi
  10.1073/pnas.1413625112; PubMed 25733878; PMC4371918. **Mouse.** Viral transduction of basal
  forebrain parvalbumin neurons with optogenetic stimulation and cortical recording. **Correction:
  *Proceedings of the National Academy of Sciences* 112(21): E2848; doi 10.1073/pnas.1507465112;
  PubMed 25918414 — an acknowledgments change naming funding support, with no change to any
  result.** *(National Academy of Sciences publisher record, PubMed and PubMed Central. **Resolved
  on 2026-08-12 while working file 13**, which cites the same accession three times.)* **Both of
  this entry's uses check out.** The paper found dense innervation of the reticular nucleus by basal
  forebrain parvalbumin fibres, which is the input at line 623; and stimulating the reticular
  nucleus's own parvalbumin neurons **preferentially enhanced cortical power at 10 Hz**, consistent
  with spindle activity and **not** gamma, which is the negative result at lines 684–689 — the
  paper's own conclusion being that the direct cortical projection carries the gamma effect.
  **File 13 states the same paper independently at its own end of these edges and agrees.**
  **This accession is also what the orphan key *Proceedings of the National Academy of Sciences*
  below names.** *(searched 2026-08-12; candidate. Lines 630, 689.)*
- **PMC4463930** — **partial.** A review titled *Turning a Negative into a Positive: Ascending
  GABAergic Control of Cortical Activation and Arousal*; PMC4463930. **Rodent-based review.**
  *(**Author list, journal, volume, pages and year not obtained from a publisher record** — only
  the title and the accession. Resolved this far on 2026-08-12 while working file 13, which cites
  the same accession.)* **Two findings.** **First, it is a review and line 643 calls it Class 1**,
  which in this source means primary measurement; **owed: reclassify, or name the primary paper it
  stands in for.** **Second, it bears on the ambiguity this entry itself declares as owed.** Lines
  637–643 cite it for a pallidal and nigral input to this nucleus and record that whether those
  fibres terminate here or directly on the relay nuclei is not distinguished at either end. **The
  passage of the review surfaced by the search states that the substantia nigra pars reticulata's
  output tonically inhibits the motor thalamus and the centromedian–parafascicular nucleus** —
  relay nuclei, not this sheet — **which leans toward the second horn.** **One retrieved passage,
  not a reading of the paper: a candidate for opening the review, not a resolution.** It remains
  the case that the accession is used at line 630 for a different claim about a different source,
  which the partial resolution does not explain. *(searched 2026-08-12; candidate, partial. Lines
  630, 643.)*
- **PMC4764559** — **owed**: not searched in this pass. **A bare accession**, carrying the
  cholinergic sleep-promotion result, which the entry itself flags as the surprising sign. *(Line
  636.)*
- **PMC6018949** — **owed**: not searched in this pass. **A bare accession.** *(Line 617.)*
- **Proceedings of the National Academy of Sciences** — **resolved: not a separate source.** Line
  629 gives the journal name with no volume, page, year or author, attached to accession
  *PMC4371918*. **It is that accession's journal** — Kim et al. 2015, *Proceedings of the National
  Academy of Sciences* 112(11): 3535–3540 — see that entry for the full reference. **Owed at the
  citing line: fold it into the accession's reference, or drop it.** *(Resolved 2026-08-12 while
  working file 13; candidate. Line 629.)*
- **PubMed 3584546** — **owed**: not searched in this pass. **A bare accession**, and it carries the
  most specific quantitative claim in the reticular-nucleus entry — that 76% of ventrobasal relay
  axons gave visible collaterals, so roughly a quarter did not. *(Line 619.)*
- **Ralston 2003** — **owed**: not searched in this pass. One of the three rebuttal-side keys at
  line 307. *(Line 307.)*
- **Saalmann 2012** — **owed**: not searched in this pass. Carries the causal inactivation result
  the pulvinar's two-part payload rests on. *(Line 239.)*
- **Schmitt / Halassa et al., Nature 2017** — Schmitt, L.I., Wimmer, R.D., Nakajima, M., Happ, M.,
  Mofakham, S. & Halassa, M.M. (2017). Thalamic amplification of cortical connectivity sustains
  attentional control. *Nature* 545(7653): 219–223; doi 10.1038/nature22073; PubMed 28467827;
  PMC5570520. **Mouse.** Representation of two attention-guiding rules recorded in prefrontal
  cortex, with optogenetic manipulation of the mediodorsal nucleus. *(Nature publisher record,
  PubMed and PubMed Central.)* **The paper's own summary is the payload this entry declares** — the
  mediodorsal nucleus amplifies the functional connectivity of prefrontal cortex, sustaining
  cortical representations of rule sets **without relaying categorical information**. Lines 82–87
  and 121–144 carry exactly that. **The key names the first and the senior author and no one
  between**, which is a compound short form; the full list is above. **This key is shared with file
  11**, where the same paper carries the consumer end of these five edges, and the two files'
  statements of it agree. **The species caveat is already in the file** at lines 139–141, and it is
  the load-bearing one: one mouse study supplies the payload on five human thalamocortical edges
  here and five more there. *(searched 2026-08-12; candidate. Line 139.)*
- **Sherman & Guillery** — **owed**: not searched in this pass; the key carries no year and no
  title. It is the general-thalamic-anatomy authority for the driver/modulator distinction, which
  is used at four entries in this file, so **it is the most load-bearing of the untitled keys.**
  *(Line 116.)*
- **Willis and colleagues 2001/2002** — **partial.** The search for the Blomqvist paper surfaced a
  critical review of the proposed ventromedial-posterior nucleus's role in pain, hosted as a 2002
  Willis document, which is consistent with what line 307 cites it for. **No author list, journal,
  volume, pages or year was obtained from a publisher record**, and the file's own key hedges
  between two years. **Owed: resolve the year and get the reference.** *(searched 2026-08-12;
  candidate, partial. Line 307.)*
- **Zhou 2016** — **owed**: not searched in this pass. The second of the two causal inactivation
  keys at line 239. *(Line 239.)*
