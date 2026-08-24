# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-12
---

---

# FILE 17 OF 20 — INSULA, CLAUSTRUM, HABENULA, CINGULATE remainder

**What is in this file.** The salience, interoception and limbic-midline wall: insula, claustrum, habenula, and the midcingulate, posterior cingulate and retrosplenial cortices.

**Size:** 832 non-blank lines, ~19.7k tokens / 79 kB. **Entries:** 6. **Reference keys:** 30, over 32 mentions.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file, with the date each was last worked:**

- **Insula — interoceptive / salience / emotional core (paralimbic cortex, buried in the Sylvian fissure)** — pass 2026-07-25 — abbreviations expanded to full names; compound limbic input line split into four named producers; cortical output class split into four named consumers; amygdala payload typed as the valence tag from file 8; auditory-parabelt input written from file 2; four cross-file edits owed at this entry by files 7, 8 and 11 discharged
- **Claustrum — the most-connected hub (thin subcortical sheet)** — pass 2026-07-25 — prose slots converted to typed edges; amygdala limb made two-ended, discharging the edit owed by file 8; the all-to-all cortical endpoint recorded as a class the source has no convention for; Internal structure slot added
- **Habenula (epithalamus — medial and lateral habenular nuclei)** — pass 2026-07-25 — prose slots converted to typed edges; medial and lateral limbs separated onto their own lines; rostromedial-tegmental and raphe limbs confirmed two-ended against files 13 and 14; ventral-pallidum input written, discharging the edit owed by file 9; interpeduncular nucleus recorded as having no entry in any of the twenty files; Internal structure slot added
- **Midcingulate cortex — caudal cingulate, areas 24′ / 32′; the cingulate-motor / action–outcome hub** — pass 2026-07-25 — prose slots converted to typed edges; the anterior-cingulate input typed as a scalar reward-value signal from file 11 and the amygdala input as the valence tag from file 8; cingulate-motor output confirmed two-ended against file 11; Internal structure slot added and the standard laminar block withheld as agranular-to-dysgranular
- **Posterior cingulate cortex — areas 23 / 31; default-mode hub, dorsal / ventral split** — pass 2026-07-25 — prose slots converted to typed edges; the hippocampal input typed as the completed episode from file 8; the default-mode-partner class split into four named consumers, discharging edits owed by files 6 and 8; the residual network endpoint recorded as unrepairable by naming; Internal structure slot added
- **Retrosplenial cortex — areas 29 granular and 30 dysgranular; spatial / Papez node behind the splenium** — pass 2026-07-25 — prose slots converted to typed edges; hippocampal, anterior-thalamic and precuneus limbs confirmed two-ended against files 8, 12 and 6; the parahippocampal producer recorded as having no entry; Internal structure slot added and the standard laminar block withheld as spanning a granular / dysgranular border

---

# INSULA, CLAUSTRUM, HABENULA, CINGULATE remainder (the salience / interoception / value-brake / limbic-midline wall)

*The paralimbic and limbic-integrative belt. The **anterior cingulate cortex** is described in the
frontal-lobe file, and the insula's **sensory** sub-fields are described in the other-senses file
(the gustatory anterior-insular / frontal-opercular field, and the parieto-insular vestibular
cortex). The three pieces this wall's own entries carry are the **insula's interoceptive / salience /
emotional core**, the **claustrum** (the brain's most-connected structure per unit volume), and the
**habenula** (the epithalamic value-brake that closes the ventral-tegmental-area aversive-value
hook) — and, completing the wall, the **cingulate remainder**: **midcingulate** (action–outcome /
cingulate-motor hub), **posterior cingulate** (a default-mode node), and **retrosplenial** (Papez /
spatial) cortex, the three linked along the **cingulum** tract (white-matter-tracts file). Counts
stay soft for the cortical structures (association / paralimbic cortex, uncounted per-region in
human, as with prefrontal cortex); the habenula carries a firm volume.*

## Insula — interoceptive / salience / emotional core (paralimbic cortex, buried in the Sylvian fissure)

- **Function:** the brain's **interoceptive** cortex and, at its anterior pole, a core hub of the
  **salience network** — with a **posterior→anterior gradient** from objective body-state to
  subjective feeling. **Posterior insula = primary interoceptive cortex:** it receives the **lamina I
  spinothalamic** pathway (via the posterior / ventromedial-posterior thalamus) representing the
  physiological condition of the body — pain, temperature, itch, visceral and cardiorespiratory
  sensation, air hunger, sensual touch, muscle and vasomotor state (Craig's "interoception / the
  material me"). **Mid-insula** re-represents and integrates. **Anterior insula:** that interoceptive
  image is re-represented and bound with emotional, cognitive, and social context into **subjective
  feelings** — the felt awareness of body state, and on Craig's account a candidate substrate of
  self-awareness (Craig 2009). With the **dorsal anterior cingulate cortex**, the anterior insula
  anchors the **salience network** — detecting behaviourally relevant events and switching between
  the default-mode and central-executive networks (Seeley et al. 2007; Menon & Uddin 2010); the right
  anterior insula tracks interoceptive accuracy (heartbeat detection; Critchley et al. 2004).
  Affective roles: disgust, empathy for pain, uncertainty / risk, and craving (insula damage can
  abolish cigarette addiction; Naqvi & Bechara 2007). Contains **von Economo (spindle) neurons**,
  large fast projection cells concentrated in the anterior insula and anterior cingulate cortex.
- **Inputs:**
  - **← the posterior / ventromedial-posterior thalamus** (the ventromedial posterior nucleus and the
    posterior nuclear group) — **carries:** the body's physiological condition — the lamina-I
    interoceptive stream, **somatotopically ordered**, onto the **dorsal posterior insula**, which is
    primary interoceptive cortex. Whether the three labelled lines the spinal entry types
    (nociceptive-specific, thermoreceptive-specific, polymodal) stay separate on this edge or are
    merged is **owed at both ends**. **Fan-in:** unknown. **The producer declares it** (file 12), in
    the same terms. **Two-ended.**
  - **← the primary somatosensory cortex**, from **area 3a** — **carries:** payload **unknown —
    owed. Fan-in:** unknown. **The producer declares it and names this region** (file 5), also
    untyped there. **Two-ended, and owed at both ends.**
  - **← the secondary somatosensory cortex**, from the **ventral somatosensory area**, whose inner
    edge adjoins the insula — **carries:** payload **unknown — owed. Fan-in:** unknown. **The
    producer declares it and names this region** (file 5). **Two-ended, and owed at both ends.**
  - **← the gustatory pathway**, onto the **anterior insula / frontal operculum** — **carries:** taste
    quality and intensity, in the gustatory entry's terms. **Fan-in:** unknown. **The producer
    declares it** (file 3), whose gustatory pathway terminates on insular taste cortex.
  - **← the vestibular nuclei and the central vestibular pathway**, onto the **parieto-insular
    vestibular cortex** — **carries:** head rotation rate and gravito-inertial acceleration, in the
    vestibular entry's terms. **Fan-in:** unknown. **The producer declares it** (file 3).
  - **← the auditory parabelt** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **Declared at the producer's end only and absent here until this pass**: the auditory parabelt
    entry (file 2) names "the insula and retroinsular areas" as one of its output streams. **Written
    now**, with the far end's own limitation carried across: that line is a compound naming several
    destinations, and its own entry marks the arity as unresolved, so this edge is **declared but not
    individually typed at either end.** *(Transcribed from the auditory parabelt entry, file 2.
    Candidate — awaiting Micky's verification.)*
  - **← the amygdala** — **carries:** the **valence tag** — a gain on perception, attention and memory
    encoding, carrying **no identity information** of its own: what arrives is the significance, not
    the thing. **Fan-in:** unknown. **Typed this pass from the producer** (file 8), where this region
    is one of five cortical consumers split out of a class endpoint. **Two-ended.** *(Split this pass
    out of the compound line "← Amygdala, Temporal pole, Orbitofrontal / ventromedial prefrontal
    cortex, and Anterior cingulate cortex (reciprocal)", which named four sources, carried one
    payload — "emotional, evaluative and social context" — across all of them, and marked it owed.
    The four far ends have four different statuses, which is why the line is now four lines.)*
  - **← the temporal pole** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The producer
    declares it** (file 7), also owed there. **Two-ended, and owed at both ends.**
  - **← the orbitofrontal / ventromedial prefrontal cortex** — **carries:** payload **unknown —
    owed. Fan-in:** unknown. **The producer declares it** (file 11). **Two-ended, and owed at both
    ends.**
  - **← the anterior cingulate cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **The producer declares no such edge.** That entry's Outputs (file 11) name the dorsolateral
    prefrontal cortex, the midcingulate cortex, and premotor and the supplementary motor areas — not
    this region — while its Inputs do declare the reciprocal limb from here. **So the return arm of a
    relationship this entry calls reciprocal is unconfirmed at its producer. Owed as a cross-file edit
    at that entry (file 11).**
  - **Dangling requirement — "context" was never a payload.** The compound line this pass split
    carried "emotional, evaluative and social context" across four sources and marked it owed, calling
    it the entry's largest gap. **One quarter of it is now closed** — the amygdala limb carries the
    valence tag, which has a stated content (significance) and a stated absence (no identity). The
    other three limbs are owed at both ends, and the Function slot above still consumes a property —
    "emotional, cognitive, and social context" bound into subjective feeling — that no incoming edge
    declares. **The dangling requirement stands, three quarters in size.**
- **Outputs:**
  - **→ the anterior cingulate cortex** (salience → control) — **carries:** the **salience signal** —
    *this event is behaviourally relevant now*. **Payload otherwise unknown — owed**; whether what
    leaves is a scalar, a pointer, or a switching command is not established. **Fan-out:** unknown.
    **The consumer declares it** (file 11), as a salience / control signal. **Two-ended.**
  - **→ the right inferior frontal gyrus** — **carries:** the same **salience signal**; **payload
    otherwise owed. Fan-out:** unknown. **Declared at the consumer's end only until this pass** (file
    11), which named this region's output as a class covering it and recorded the edit owed here.
    **Written now, and that owed edit is discharged.**
  - **→ the orbitofrontal / ventromedial prefrontal cortex** — **carries:** the **salience signal**
    and, reciprocally, the **interoceptive state**; **payload otherwise owed. Fan-out:** unknown.
    **Declared at the consumer's end only until this pass** (file 11), which records "**Owed at file
    17: write the output limb by name.**" **Written now, and that owed edit is discharged.**
  - **→ the temporal pole** — **carries:** **interoceptive context**; **payload otherwise owed.
    Fan-out:** unknown. **Declared at the consumer's end only until this pass** (file 7), which
    records the producer as declaring the relationship from its input side alone. **Written now, and
    that owed edit is discharged.** *(The three lines above were split this pass out of the class
    endpoint "→ Anterior cingulate cortex and prefrontal cortex", which named one region and one
    class. **The class is not fully resolved**: the dorsolateral prefrontal cortex is not among the
    consumers that declare an insular input, so whether the class covers it is **unchecked**.)*
  - **→ the midcingulate cortex** — **carries:** the **salience / affect signal**, in the consumer's
    terms. **Payload otherwise owed. Fan-out:** unknown. **The consumer is in this file and declares
    it**, and **both ends were written in this same pass, so their agreement certifies nothing.**
  - **→ the amygdala** — **carries:** payload **unknown — owed** at both ends. **Fan-out:** unknown.
    **The consumer declares it** (file 8), also owed there. **Two-ended.**
  - **→ the bed nucleus of the stria terminalis**, from the **anterior insula** — **carries:**
    **interoceptive state**; **payload otherwise owed. Fan-out:** unknown. **Declared at the
    consumer's end only until this pass** (file 8), which records "**Owed as a cross-file edit at that
    entry (file 17).**" **Written now, and that owed edit is discharged.**
  - **→ the hypothalamus** (autonomic / affect) — **carries:** payload **unknown — owed. Fan-out:**
    unknown. **The far end is in file 14**; not confirmed this pass. **Owed as a cross-file check at
    that entry.** *(Split this pass out of the compound line "→ Amygdala and Hypothalamus", whose two
    limbs have different statuses.)*
  - **→ the basal ganglia**, onto the **ventral striatum** — **carries:** payload **unknown — owed**
    at both ends. **Fan-out:** unknown. **The consumer declares it** (file 9). **Two-ended.**
  - **→ the habenula**, onto the **lateral habenula** — **carries:** a **bad-outcome expectation** —
    an affective / evaluative signal that an outcome is worse than wanted, in the consumer's terms.
    **Payload otherwise owed. Fan-out:** unknown. **The consumer is in this file and declares it**,
    naming the anterior insula among the affective / evaluative cortical sources of the lateral
    habenula.
  - **→ the posterior / ventromedial-posterior thalamus** (corticothalamic feedback) — **carries:** no
    stimulus content; the driver / modulator gate. **Fan-out:** unknown. **The consumer declares it**
    (file 12), in the same terms. **Two-ended.**
- **Internal structure and internal data flow:** the insula is organised as a **cytoarchitectonic
  gradient**, not a set of blocks: fully **granular** six-layered cortex postero-dorsally,
  **dysgranular** through the middle and dorsal anterior territory, and **agranular** cortex with
  undifferentiated layers II/III antero-ventrally. **The standard laminar block is therefore not
  transcribed here**: it is a claim about granular isocortex and three of its edges route through
  layer 4, which the agranular and dysgranular sectors do not have. Quantitative human mapping in
  postmortem material names the **insular granular areas Ig1 and Ig2** and the **insular dysgranular
  area Id1** in the posterior insula, and **insular granular area Ig3**, the **insular agranular area
  Ia1**, and **insular dysgranular areas Id2 to Id6** through the middle posterior and dorsal anterior
  insula. Intracortical myelin and parvalbumin neuropil in the middle layers follow the **same
  decreasing postero-dorsal to antero-ventral gradient**, so the gradient is chemical and
  myeloarchitectonic as well as laminar. Somatotopic organisation is reported within the dorsal
  posterior sector.
  - **Internal edge — posterior (granular) → mid (dysgranular) insula: carries:** the interoceptive
    body-state image, re-represented and integrated. **Fan-in / fan-out:** unknown.
  - **Internal edge — mid (dysgranular) → anterior (agranular) insula: carries:** the re-represented
    image, bound at the anterior pole with the emotional and cognitive context arriving on the
    limbic edges above, producing what is described as **subjective feeling**. **Payload — owed, and
    the completion test fails here:** "a subjective feeling" is a phrase, not a type. This is the
    same hole the source records at the temporal pole and the prefrontal cortex.
    **Fan-in / fan-out:** unknown.
  *(Class 1 — human cytoarchitecture: Kurth, Zilles, Fox, Laird & Eickhoff, Cerebral Cortex 20:1448,
  2010, ten human postmortem brains, quantitative image analysis; Quabs, Caspers, Schöne et al.,
  NeuroImage 260:119453, 2022, ten human postmortem brains, three-dimensional probability maps;
  Morel, Gallay, Baechler et al., Neuroscience 236:117, 2013, human architectonics with postmortem
  magnetic-resonance-imaging registration. Candidates — awaiting Micky's verification. The withheld
  laminar block is Claude's reading of the gradient against the standard block, Class 2.)*
- **Contested — how many subdivisions there are.** Published parcellations of the human insula range
  from a simple anterior-agranular / posterior-granular pair, through the three-belt granular /
  dysgranular / agranular scheme, to schemes naming sixteen granular areas. **The gradient is not in
  dispute; the boundaries drawn across it are.** Recorded as contested; the edges above are placed on
  the gradient's poles rather than on any one parcellation's areas.
  *(Class 1 — the range of published schemes is set out in the comparison of seven cyto- and
  myeloarchitectonic studies in the primate insula literature. Candidate.)*
- **Correction — von Economo neurons are not confined to agranular cortex.** The entry's Function
  slot places them in the anterior insula and anterior cingulate cortex. Human material puts the von
  Economo neuron field **extending from the anterior agranular insula into the anterior part of the
  dysgranular insula**, so the population crosses the architectonic boundary rather than marking it.
  *(Class 1 — Morel et al., Neuroscience 236:117, 2013, human. Candidate.)*
- **Neurons:** soft / no clean human per-region count — association / paralimbic cortex, uncounted in
  human as with prefrontal and inferior-parietal association areas; cytoarchitecture graded
  (agranular / dysgranular anteriorly → granular posteriorly). Its distinctive countable feature is
  the **von Economo neuron** population (shared with the anterior cingulate cortex), a small
  specialised fraction of the total.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** the insular lobe is a sizeable
  territory; no single verified human figure recorded here (soft). **White-matter volume /
  Myelination:** unknown.
- **Pass:** 2026-07-25 — abbreviations expanded to full names; compound limbic input line split into four named producers; cortical output class split into four named consumers; amygdala payload typed as the valence tag from file 8; auditory-parabelt input written from file 2; four cross-file edits owed at this entry by files 7, 8 and 11 discharged

## Claustrum — the most-connected hub (thin subcortical sheet)

- **Function:** a thin sheet of grey matter in the basolateral forebrain, lateral to the putamen
  (across the external capsule) and medial to the insula (across the extreme capsule) — and, **per
  unit volume, the most densely connected structure in the brain**, with reciprocal projections to
  almost the entire neocortex plus the amygdala, hippocampus / subiculum, and cingulate cortex
  (Torgerson et al. 2015). Its precise function is still **unresolved**; the leading hypotheses are
  cortical **synchronisation / binding** (Crick & Koch 2005 proposed it as the "conductor of the
  cortical orchestra," coordinating distributed activity into unified conscious percepts),
  **multisensory integration**, **salience / attentional control and network switching**, and the
  regulation of **slow (~0.5–4 Hz) cortical oscillations** during mental-state transitions (Narikiyo
  et al. 2020). A single human stimulation case near the claustrum produced a reversible loss of
  consciousness (Koubeissi et al. 2014). It densely expresses serotonin-2A receptors (a psychedelic
  target). No cortical-style lamination — pyramidal-like, fusiform, and circular cells with a
  gap-junction-coupled **GABAergic** (γ-aminobutyric-acid-releasing, inhibitory) interneuron network.
- **Inputs:**
  - **← the cerebral cortex**, near "all-to-all" — **carries:** payload **unknown — owed. Fan-in:**
    unknown. **This endpoint names a class** covering nearly every cortical entry in the source, and
    it is the hardest class endpoint in the file: the connectivity is described as diffuse rather than
    precisely mapped, so resolving it into named producers would assert a specificity the literature
    does not report. **Owed: the source has no convention for an all-to-all endpoint**, and this entry
    is where it is first needed.
  - **← the amygdala**, onto the **ventral claustrum** — **carries:** payload **unknown — owed.
    Fan-in:** unknown. **The producer declares no such edge.** That entry's Outputs (file 8) name the
    hypothalamus, the temporal pole, the insula, the anterior and midcingulate cortices, the
    orbitofrontal / ventromedial prefrontal cortex, the right inferior frontal gyrus and the
    mediodorsal thalamus — not this structure — while its Inputs do declare the reciprocal limb from
    here. **Owed as a cross-file edit at that entry (file 8).**
  - **← the cingulate cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The
    producers are the anterior cingulate entry (file 11) and the midcingulate, posterior cingulate and
    retrosplenial entries in this file; none declares this edge. Owed at all four**, and **owed here
    too: "the cingulate cortex" is a class**, and which cingulate fields project here is not stated.
  - **← the hippocampus / subiculum** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **The far end is in file 8**; that entry's hippocampal formation declares no claustral edge in
    either direction. **Owed as a cross-file check at that entry.**
  - **← neuromodulatory afferents** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **This endpoint names a class.** The four neuromodulatory entries (file 13) each declare a
    brain-wide cortical class that would cover this structure without naming it. **Owed: name the
    nuclei, or record that the brain-wide class is the whole claim.**
- **Outputs:**
  - **→ the cerebral cortex**, near "all-to-all" and reciprocal, on **exceptionally far-reaching
    claustro-cortical axons** — **carries:** payload **unknown — owed. Fan-out:** unknown. **This
    endpoint names a class**, with the same limitation as the input limb above. **This is the edge the
    entry's Function slot depends on**: every hypothesis listed there — binding, synchronisation,
    network switching, slow-oscillation control — is a claim about what travels on this edge, and none
    of them types it. **The completion test fails at this entry**: what leaves the claustrum on a wire
    cannot be said.
  - **→ the amygdala** — **carries:** payload **unknown — owed. Fan-out:** unknown. **The consumer
    declares it** (file 8), which records this edge as "declared at the producer's end only" and asks
    for the prose conversion this pass performs. **Two-ended, and that owed edit is discharged.**
  - **→ the hippocampus / subiculum** — **carries:** payload **unknown — owed. Fan-out:** unknown.
    **The far end is in file 8** and declares no such edge. **Owed as a cross-file edit at that
    entry.**
  - **→ the cingulate cortex** — **carries:** payload **unknown — owed. Fan-out:** unknown. **Same
    class problem and same four unconfirmed far ends as the input limb above.**
- **Internal structure and internal data flow:** **no cortical-style lamination** — this is a positive
  statement about the structure and is why the standard laminar block cannot be written here. Three
  cell classes are described — **pyramidal-like projection neurons**, **fusiform cells**, and
  **circular cells** — together with a **gap-junction-coupled GABAergic interneuron network**. A
  **dorsal / ventral** division is used by the entry's own edges: the ventral claustrum is the limbic
  sector that carries the amygdala and cingulate connections. **Internal edges: owed.** The cell
  classes are described and no edge between them is typed; the gap-junction coupling is an electrical
  coupling among interneurons rather than a directed synaptic edge, and how the source writes a
  non-directed coupling is not settled. Whether the dorsal and ventral sectors project to different
  targets — which is the test §3 sets for a sub-element — is **owed**: the limbic attribution above
  says they may, and no source read here confirms it.
  *(Class 3 — general anatomy for the cell classes and the dorsal / ventral division; the reading that
  the all-to-all output edge is where the completion test fails is Claude's, Class 2. No primary
  source was opened and no search was run for this entry in this pass.)*
- **Neurons:** soft / no clean human count recorded here — its defining quantitative fact is
  **connectivity density** (most-connected per unit volume), not a firm neuron number; a thin,
  hard-to-segment sheet.
- **Synapses:** unknown. **Axons:** the long claustro-cortical projections (counts unknown).
  **Grey-matter volume:** thin sheet; no verified human figure recorded (soft, segmentation-dependent).
  **White-matter volume:** unknown. **Myelination:** flanked by the extreme and external capsules;
  g-ratio unknown.
- **Pass:** 2026-07-25 — prose slots converted to typed edges; amygdala limb made two-ended, discharging the edit owed by file 8; the all-to-all cortical endpoint recorded as a class the source has no convention for; Internal structure slot added

## Habenula (epithalamus — medial and lateral habenular nuclei)

- **Function:** a small **epithalamic** hub that converts "things are going badly" into a brake on the
  brain's value chemistry — the anatomical counterweight to the dopamine reward system. Two divisions.
  The **lateral habenula** is the **negative-value / "anti-reward" node**: its neurons are excited by
  aversive events, pain, and loss, and by the **omission of expected reward** — a **negative
  reward-prediction error**, the mirror image of midbrain dopamine neurons (Matsumoto & Hikosaka
  2007). It suppresses dopamine chiefly *indirectly*, driving the GABAergic **rostromedial tegmental
  nucleus** (the "tail of the ventral tegmental area"), which inhibits dopamine cells in the **ventral
  tegmental area** and the **substantia nigra pars compacta** (Jhou et al. 2009) — the direct closure
  of the ventral-tegmental-area entry's "lateral habenula = negative value" hook — and it is
  reciprocally tied to raphe **serotonin**. Sustained lateral-habenular overactivity is a leading
  circuit account of **depression / learned helplessness** (Li et al. 2011) and an emerging
  deep-brain-stimulation and ketamine target. The **medial habenula** is a cholinergic /
  substance-P system projecting to the **interpeduncular nucleus**; it is tied to **nicotine aversion
  and withdrawal**, anxiety, and sleep-state modulation, and links to the pineal gland.
- **Inputs:** all arriving over the **stria medullaris**, from limbic and basal-ganglia forebrain.
  - **← the septal nuclei**, onto the **medial habenula** — **carries:** payload **unknown — owed.
    Fan-in:** unknown. **This producer has no entry in any of the twenty files**, checked 2026-07-25.
    The **lateral septum** is already recorded as a region named on edges with no entry — file 14's
    rostromedial tegmental entry names it as an input, and file 14's hypothalamus entry names it as
    well — and this is a **third** file naming a septal producer that owns no slot. **Owed: the septal
    nuclei need an entry, and it is not clear which file owns them.**
  - **← the internal globus pallidus**, onto the **lateral habenula** — **carries:** the basal-ganglia
    **"no-reward" signal. Payload otherwise unknown — owed. Fan-in:** unknown. **The producer declares
    it and names this structure** (file 9), which wrote its end specifically to close this diff and
    notes the rodent homologue is the entopeduncular nucleus. **Two-ended.**
  - **← the ventral pallidum**, onto the **lateral habenula** — **carries:** payload **unknown —
    owed. Fan-in:** unknown. **Declared at the producer's end only and absent here until this pass**
    (file 9), whose ventral-pallidum entry records "**Owed as a cross-file edit at that entry (file
    17)**" because this entry attributed the whole pallidal input to the dorsal structure. **Written
    now, and that owed edit is discharged.** *(Transcribed from the ventral pallidum entry, file 9.
    Candidate — awaiting Micky's verification.)*
  - **← the lateral hypothalamus** and the lateral septo-hypothalamic continuum, onto the **lateral
    habenula** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The far end is the
    hypothalamus entry (file 14)**; not confirmed this pass. **Owed as a cross-file check at that
    entry.**
  - **← the suprachiasmatic nucleus**, onto the **lateral habenula** — **carries:** payload **unknown
    — owed. Fan-in:** unknown. **The far end is a named sub-element of the hypothalamus entry (file
    14)**, which lists the suprachiasmatic nucleus as the circadian master clock among eleven
    sub-nuclei and does not declare this edge. **Owed as a cross-file edit at that entry.**
  - **← the anterior cingulate cortex**, onto the **lateral habenula** — **carries:** a **bad-outcome
    expectation. Payload otherwise unknown — owed. Fan-in:** unknown. **The producer declares no such
    edge** (file 11). **Owed as a cross-file edit at that entry.**
  - **← the anterior insula**, onto the **lateral habenula** — **carries:** a **bad-outcome
    expectation. Payload otherwise unknown — owed. Fan-in:** unknown. **The producer is in this file
    and declares it. Two-ended**, though **both ends were confirmed in the same pass.**
  - **← the ventromedial prefrontal cortex**, onto the **lateral habenula** — **carries:** a
    **bad-outcome expectation. Payload otherwise unknown — owed. Fan-in:** unknown. **The producer
    declares no such edge** (file 11), whose orbitofrontal / ventromedial entry names the amygdala,
    hypothalamus, ventral striatum, temporal pole, insula, right inferior frontal gyrus and
    periaqueductal gray among its outputs. **Owed as a cross-file edit at that entry.** *(The three
    cortical lines above were split this pass out of "affective / evaluative cortex (anterior
    cingulate cortex, anterior insula, ventromedial prefrontal cortex — the 'bad-outcome' expectation
    signals)", which named three sources and typed none of them; two of the three far ends are
    missing and one is present, which is why the line is now three lines.)*
- **Outputs:** all leaving over the **fasciculus retroflexus**, the habenulo-interpeduncular tract.
  - **→ the interpeduncular nucleus**, from the **medial habenula** — **carries:** payload **unknown
    — owed. Fan-out:** unknown. **This consumer has no entry in any of the twenty files**, checked
    2026-07-25 — the string appears nowhere in the source outside this entry. **The medial habenula's
    principal output therefore terminates on a region the source does not describe**, which means the
    whole medial-habenular limb — nicotine aversion and withdrawal, and the cholinergic /
    substance-P arm — is described from its origin only. **Owed: the interpeduncular nucleus needs an
    entry**; its anatomical owner is the ventral midbrain tegmentum, which is file 14.
  - **→ the rostromedial tegmental nucleus**, from the **lateral habenula** — **carries:** a
    **negative / aversive value signal** — a glutamatergic excitatory drive encoding a
    worse-than-expected outcome, which that nucleus inverts in sign into inhibition of the dopamine
    cells. **Fan-out:** unknown. **The consumer declares it** (file 14), where it is named the major
    input and the one that defines the nucleus. **Two-ended.** *(This consumer had no entry when this
    file was last worked and now has one; the relay is no longer a name on an edge.)*
  - **→ the raphe nuclei**, from the **lateral habenula** — **carries:** the same **negative /
    aversive value signal**, here modulating serotonin rather than dopamine. **Payload otherwise
    owed. Fan-out:** unknown. **The consumer declares it** (file 13). **Two-ended.**
  - **→ the pineal gland**, from the **medial habenula** — **carries:** payload **unknown — owed.
    Fan-out:** unknown. **The consumer declares no such edge** (file 14), whose pineal entry types its
    input as a sympathetic efferent chain gated by the circadian clock. **The link is stated here in
    prose — "links to the pineal" — and that is not an edge**: neither its direction nor its content
    is established at this end either. **Owed at both ends, and owed here first: state what this
    connection is before asking the consumer to carry it.**
  - **No direct dopamine edge is written.** The Function slot says the lateral habenula suppresses
    dopamine **chiefly indirectly**, through the rostromedial tegmental nucleus, and the source
    records the relay as the edge. A sparse direct habenula → ventral-tegmental-area projection is
    reported in the literature and is **not** written here, because it was not confirmed this pass at
    either end. **Owed: confirm or refuse it.**
- **Internal structure and internal data flow:** two sub-elements, the **medial habenula** and the
  **lateral habenula**, each with several subnuclei that are not named here. They are sub-elements in
  §3's sense on the strongest possible ground: **they have different transmitters, different inputs
  and entirely different targets** — the medial habenula is cholinergic and substance-P and projects
  to the interpeduncular nucleus; the lateral habenula is glutamatergic and projects to the
  rostromedial tegmental nucleus and the raphe. Every edge in this entry is already attributed to one
  or the other. **Internal edges: owed.** Whether the two divisions communicate at all is not
  established in the material read, and the subnuclei of each are described in the literature and not
  named here, so the level below the division is **owed** as well.
  *(Class 3 — general anatomy for the two divisions and their transmitters; the attribution of each
  edge to a division is Class 2, Claude's reading of which limb each source or target belongs to,
  offered to be checked. No primary source was opened and no search was run for this entry in this
  pass.)*
- **Neurons:** soft / no clean absolute human count recorded here — human stereology exists (Ranft et
  al. 2010) but reports volumes and disease-related *changes* rather than a control absolute. Medial
  and lateral habenula, several subnuclei each.
- **Synapses:** unknown. **Axons:** the stria medullaris (in) and the fasciculus retroflexus (out);
  counts unknown.
- **Grey-matter volume:** medial and lateral habenula combined, **~30–36 mm³ per side** (post-mortem
  ~31 mm³ left / ~33 mm³ right, uncorrected for shrinkage, Ranft et al. 2010; high-resolution magnetic
  resonance imaging ~29–36 mm³, Savitz et al. 2011) — about the size of a single functional
  magnetic-resonance-imaging voxel; a slight **right > left** asymmetry, with a soft functional
  lateralisation (left more affective, right more arousal). **White-matter volume:** unknown.
  **Myelination:** the fasciculus retroflexus is a compact myelinated tract; g-ratio unknown.
- **Pass:** 2026-07-25 — prose slots converted to typed edges; medial and lateral limbs separated onto their own lines; rostromedial-tegmental and raphe limbs confirmed two-ended against files 13 and 14; ventral-pallidum input written, discharging the edit owed by file 9; interpeduncular nucleus recorded as having no entry in any of the twenty files; Internal structure slot added

## Midcingulate cortex — caudal cingulate, areas 24′ / 32′; the cingulate-motor / action–outcome hub

- **Function:** the dorsal-cingulate "doing" zone between the emotional anterior cingulate cortex and
  the mnemonic posterior cingulate cortex — the hub that links **reinforcement outcomes to action**.
  Its anterior part is the convergence point where **negative affect, pain, and cognitive control
  overlap** — effortful / feedback-mediated decision-making, conflict, and the drive to adjust
  behaviour (Shackman et al. 2011; Vogt 2016). It houses the **cingulate motor areas** (rostral and
  caudal), cingulate cortex that projects onto the supplementary and premotor fields and the primary
  motor cortex, so the midcingulate cortex is **output-capable**, not just a monitor. On Rolls's
  (2019) reading the cingulate cortex as a whole performs **action–outcome learning**: the anterior
  cingulate cortex supplies reward / non-reward outcome (from orbitofrontal cortex), the posterior
  cingulate cortex supplies action / spatial information (from parietal cortex), and the
  **midcingulate motor area** turns their convergence into a motor plan sent to premotor cortex.
- **Inputs:**
  - **← the anterior cingulate cortex** (reward / outcome) — **carries:** a **scalar reward-value
    signal** — expected reward magnitude, and a response to the mismatch between expected and received
    reward (firing to unexpected reward and to expected-but-omitted reward). It has a coordinate frame
    — a scalar value axis — but the axis's zero and slope are set by bodily and motivational state, so
    the frame is **body-relative**. **Fan-in:** unknown. **The producer declares it and types it**
    (file 11), where the payload is verified for the source by Micky 2026-07-15 and the body-relative
    reading is marked Class 2. **Two-ended, and the producer's note applies here too: the two ends are
    copies, so their agreement certifies nothing on its own.**
  - **← the amygdala** — **carries:** the **valence tag** — a gain on perception, attention and memory
    encoding, carrying **no identity information** of its own. **Fan-in:** unknown. **The producer
    declares it and names this region** (file 8), where this region is one of five cortical consumers
    split out of a class endpoint. **Two-ended.**
  - **← the anterior insula** — **carries:** the **salience / affect signal**; **payload otherwise
    owed. Fan-in:** unknown. **The producer is in this file**, and **both ends were written in this
    same pass, so their agreement certifies nothing.** *(The amygdala and insula limbs above were
    split this pass out of "amygdala and anterior insula (salience / affect)", which named two sources
    and carried one payload across both; the amygdala limb now carries a payload typed at its far end
    and the insular limb does not.)*
  - **← the posterior parietal cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **This endpoint names a class.** The candidate producers are in file 6 — the anterior and medial
    intraparietal areas, the supramarginal and angular gyri, and the precuneus — and none was
    confirmed this pass. **Owed: resolve to named producers, or withdraw.**
  - **← the posterior cingulate cortex** (action / spatial) — **carries:** payload **unknown — owed.
    Fan-in:** unknown. **The producer is in this file and declares the reciprocal relationship**;
    both ends are owed and both were written in this pass.
  - **← the midline and intralaminar thalamus** — **carries:** payload **unknown — owed. Fan-in:**
    unknown. **The producer declares its cortical target as a class** — "striatum (major) and cortex
    (diffuse)" (file 12) — which covers this region without naming it. **Owed as a cross-file edit at
    that entry.**
  - **← the mediodorsal thalamus** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The
    far end is in file 12**, whose mediodorsal entry is described as the prefrontal relay and was not
    confirmed to name this region this pass. **Owed as a cross-file check at that entry.** *(Split
    this pass out of "midline / intralaminar and mediodorsal thalamus", which named two thalamic
    sources with different far-end statuses.)*
  - **← the cingulum**, carrying dense intracingulate traffic — **this is a tract, not a producer.**
    The cingulum has an entry in file 18 as transmission without processing, so the traffic on it
    belongs to the cingulate edges above and below rather than to a line of its own. **Recorded here
    as routing, not as an edge**, in the same way file 16 records tract routing.
- **Outputs:**
  - **→ the supplementary and pre-supplementary motor areas and premotor cortex**, via the
    **cingulate motor areas** — **carries:** payload **unknown — owed**; at this end it is the
    convergence of reward or non-reward outcome with action and spatial information, turned into a
    motor plan. **Fan-out:** unknown. **The consumer declares it** (file 11), which wrote its end to
    close this diff and names this region and its cingulate motor areas explicitly. **Two-ended.**
  - **→ the primary motor cortex**, via the **cingulate motor areas** — **carries:** payload
    **unknown — owed. Fan-out:** unknown. **The far end is in file 5**; not confirmed this pass.
    **Owed as a cross-file check at that entry.**
  - **→ the anterior cingulate cortex**, reciprocally, via the **cingulum** — **carries:** payload
    **unknown — owed. Fan-out:** unknown. **The consumer declares it** (file 11), which wrote its end
    this pass naming this region. **Two-ended, and owed at both ends.**
  - **→ the posterior cingulate cortex**, reciprocally — **carries:** payload **unknown — owed.
    Fan-out:** unknown. **The consumer is in this file**; both ends written in this pass.
  - **→ the basal ganglia** — **carries:** payload **unknown — owed. Fan-out:** unknown. **The far end
    is in file 9**; not confirmed this pass, and **"the basal ganglia" is a class** — the striatal
    target is the likely one and is not stated. **Owed: name the target nucleus, then check the far
    end.**
  - **→ brainstem autonomic targets** — **carries:** payload **unknown — owed. Fan-out:** unknown.
    **This endpoint names a class.** File 14 holds the candidates — the periaqueductal gray, the
    solitary nucleus, the rostral and caudal ventrolateral medulla — and none was confirmed this pass.
    **Owed: name them.**
- **Internal structure and internal data flow:** sub-elements are Vogt's "prime" midcingulate fields
  — **area 24′** (with its a′, b′ and c′ divisions) and **area 32′** — together with the **rostral
  cingulate motor area** and the **caudal cingulate motor area**, which are the entry's
  output-capable sectors and are already named on the motor edges above. An **anterior / posterior
  midcingulate** division is used by the Function slot, the anterior part carrying the negative
  affect, pain and cognitive-control convergence. **The standard laminar block is not transcribed
  here**: this tissue is **agranular to dysgranular** across its extent, and three of the block's
  edges route through layer 4, so transcribing it would assert a circuit this entry denies.
  **Internal edges: owed** — the sub-elements are named and no edge between them is typed.
  *(Class 3 — general anatomy for the field divisions and the cingulate motor areas; the withheld
  laminar block is Claude's reading of the entry's own cytoarchitecture against §3a's rule, Class 2.
  No primary source was opened and no search was run for this entry in this pass.)*
- **Neurons:** soft / unknown — paralimbic association cortex, uncounted per-region in human (as with
  prefrontal and insular cortex). Cytoarchitecture is Vogt's "prime" midcingulate pattern (areas 24′
  and 32′), agranular to dysgranular.
- **Synapses:** unknown. **Axons:** the cingulate-motor corticofugal fibres (counts unknown).
  **Grey-matter volume:** unknown. **White-matter volume:** unknown. **Myelination:** unknown.
- **Pass:** 2026-07-25 — prose slots converted to typed edges; the anterior-cingulate input typed as a scalar reward-value signal from file 11 and the amygdala input as the valence tag from file 8; cingulate-motor output confirmed two-ended against file 11; Internal structure slot added and the standard laminar block withheld as agranular-to-dysgranular

## Posterior cingulate cortex — areas 23 / 31; default-mode hub, dorsal / ventral split

- **Function:** a core hub of the **default-mode network** and part of the brain's structural
  connectivity core — internally-directed cognition, self-reference, autobiographical memory, and
  regulation of the balance between internal and external attention. It is **not homogeneous**: the
  **ventral posterior cingulate cortex** is tied into the default-mode network proper and the **medial
  temporal lobe / hippocampus** (memory retrieval, internally-directed thought), while the **dorsal
  posterior cingulate cortex** connects additionally to the fronto-parietal **cognitive-control and
  attention networks** and helps modulate the switch between internal and external focus (Leech,
  Kamourieh, Beckmann & Sharp 2011; Leech, Braga & Sharp 2012). Its neurons also track decision
  variables and exploratory choice (Platt 2009). It usually **deactivates** as externally-focused task
  demand rises — the signature default-mode response.
- **Inputs:**
  - **← the hippocampal formation** — **carries:** the **completed episode** — the bound, retrievable
    pattern, addressable by any fragment of itself. **Payload only partly writable — owed:** "an
    episode" has no units and no frame, and what makes it checkable is a property rather than a type,
    namely that it is **content-addressable**. **Fan-in:** unknown. **The producer declares it and
    types it** (file 8), which names this region and the retrosplenial cortex on one edge and records
    "**Owed at file 17: type them.**" **Typed now from the producer's declaration, and that owed edit
    is discharged.**
  - **← the anterior cingulate cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **The producer declares no such edge** (file 11), whose outputs name the dorsolateral prefrontal
    cortex, the midcingulate cortex, and premotor and supplementary motor areas. **Owed as a
    cross-file edit at that entry.**
  - **← the midcingulate cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The
    producer is in this file**; both ends written in this pass. *(Split this pass out of "anterior
    cingulate cortex / midcingulate cortex", whose two limbs have different far-end statuses.)*
  - **← the precuneus** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The far end is
    in file 6**; that entry's precuneus declares an input from this region but was not confirmed this
    pass to declare the return limb. **Owed as a cross-file check at that entry.**
  - **← the posterior parietal cortex** (action / spatial) — **carries:** payload **unknown — owed.
    Fan-in:** unknown. **This endpoint names a class**, with the same candidate producers in file 6 as
    the midcingulate entry's parietal input. **Owed: resolve to named producers, or withdraw.**
  - **← the anterior thalamus** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The
    producer declares no such edge** (file 12), whose anterior nuclei name the retrosplenial cortex
    and the anterior cingulate cortex as their cortical targets — **not this region**. **So the
    posterior-cingulate limb of the classical limbic thalamic projection is unconfirmed at its
    producer. Owed as a cross-file edit at that entry (file 12).**
  - **← the cingulum** — **this is a tract, not a producer**, recorded as routing rather than as an
    edge, as at the midcingulate entry above.
- **Outputs:**
  - **→ the hippocampal formation** — **carries:** payload **unknown — owed. Fan-out:** unknown. **The
    consumer declares it** (file 8) and records "**Owed at file 17: type it.**" **Written by name now
    — the class it was hidden in is gone — but the payload is still owed at both ends**, which is the
    honest state: naming the consumer is not typing the edge.
  - **→ the precuneus** — **carries:** payload **unknown — owed. Fan-out:** unknown. **The consumer
    declares it and names this region** (file 6), recording "**Owed at file 17: type it.**"
    **Two-ended by name, payload owed at both ends.**
  - **→ the angular gyrus** — **carries:** payload **unknown — owed. Fan-out:** unknown. **The far end
    is in file 6**; not confirmed this pass. **Owed as a cross-file check at that entry.**
  - **→ the orbitofrontal / ventromedial prefrontal cortex** — the medial-prefrontal default-mode
    partner — **carries:** payload **unknown — owed. Fan-out:** unknown. **The far end is in file
    11**; not confirmed this pass. **Owed as a cross-file check at that entry.** *(The four lines
    above were split this pass out of the endpoint "the default-mode-network partners (medial
    prefrontal, angular gyrus, precuneus, medial temporal lobe)", which named a network and four of
    its members in one line and typed none of them.)*
  - **→ the cognitive-control network**, via the **dorsal posterior cingulate cortex** — **carries:**
    payload **unknown — owed. Fan-out:** unknown. **This endpoint names a network, not a region, and
    it is not repairable by naming the members**: a network is a set of regions defined by correlated
    activity rather than by a projection, so listing its members would turn one edge into several and
    assert that each member receives the same payload, which is not what the claim says. **How the
    source writes an edge to a network, or whether it refuses to, is open and unasked.** Recorded, not
    resolved.
- **Internal structure and internal data flow:** sub-elements are the **dorsal posterior cingulate
  cortex** (area 23d and area 31) and the **ventral posterior cingulate cortex** (areas 23a and 23b).
  They meet §3's test for sub-elements rather than properties: **they project to different targets** —
  the ventral sector to the default-mode partners and the medial temporal lobe, the dorsal sector
  additionally to the fronto-parietal control network — and the entry's own Function slot and its
  output edges are already written on that division. This is **granular isocortex**, unlike the
  agranular anterior and midcingulate cortices, so the standard laminar block is admissible here; it
  is **not transcribed** because this entry's own laminar description has not been read against it,
  and §3a makes that check part of writing the slot rather than an optional refinement. **Internal
  edges: owed** — including, specifically, whether the dorsal and ventral sectors are connected to
  each other, which is what a switch between internal and external focus would need.
  *(Class 3 — general anatomy for the area numbering; the dorsal / ventral functional split is from
  the entry's own Function slot and its cited sources, Class 1 at that end. The reading that the two
  sectors qualify as sub-elements, and the note about what the switch would require, are Claude's,
  Class 2. No primary source was opened and no search was run for this entry in this pass.)*
- **Neurons:** soft / unknown — association cortex, uncounted per-region in human (granular isocortex,
  unlike the agranular anterior and midcingulate cortices).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown. **White-matter volume:**
  unknown. **Myelination:** unknown.
- **Pass:** 2026-07-25 — prose slots converted to typed edges; the hippocampal input typed as the completed episode from file 8; the default-mode-partner class split into four named consumers, discharging edits owed by files 6 and 8; the residual network endpoint recorded as unrepairable by naming; Internal structure slot added

## Retrosplenial cortex — areas 29 granular and 30 dysgranular; spatial / Papez node behind the splenium

- **Function:** a small cortical strip behind the splenium of the corpus callosum, central to **spatial
  navigation and memory** — translating between **egocentric (viewpoint) and allocentric (world / map)
  reference frames**, anchoring **head-direction** and landmark information, and supporting **scene
  construction** and the spatial-contextual side of episodic / autobiographical memory (Vann, Aggleton
  & Maguire 2009). It fuses **internal self-motion cues** (vestibular, proprioceptive, motor efference)
  with **external visual landmarks** to keep heading current; the human retrosplenial cortex shows
  navigation-related theta during heading changes. Its connectional signature — reciprocal with the
  **hippocampal formation, parahippocampal region, anterior (limbic) thalamus, and parietal cortex** —
  is conserved across mammals, and it is one of the **first regions to show Alzheimer pathology**
  (Buckner et al. 2005).
- **Inputs:**
  - **← the hippocampal formation**, from the **subiculum** — **carries:** the **completed episode** —
    the bound, retrievable pattern, addressable by any fragment of itself; **payload only partly
    writable — owed**, on the same ground as at the posterior cingulate entry above. **Fan-in:**
    unknown. **The producer declares it and types it** (file 8), which names this region and the
    posterior cingulate cortex on one edge and records "**Owed at file 17: type them.**" **Typed now
    from the producer's declaration, and that owed edit is discharged.**
  - **← the anterior thalamic nuclei** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **The producer declares it and names this region** (file 12), as the anterior-thalamus limb of the
    Papez circuit — the mammillary bodies → mammillothalamic tract → anterior thalamus →
    cingulate / retrosplenial limb that the anterior-nuclei and hypothalamus entries point to.
    **Two-ended, and owed at both ends.** **A specific gap sits under this edge:** the
    **head-direction** signal this entry's Function slot depends on is classically carried by one
    division of the anterior nuclei rather than by the group, and that entry records its own divisions
    as unnamed and owed. **Until they are named, the entry's headline input cannot be written as an
    edge from the division that carries it.**
  - **← the parahippocampal cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **This producer has no entry in any of the twenty files**, checked 2026-07-25; it is named as a
    producer by the temporal-pole entry (file 7), the inferotemporal entry (file 1) and the
    hippocampal formation (file 8) as well. **Owed: the parahippocampal region needs an entry**, and
    file 8 is its anatomical owner.
  - **← the posterior parietal cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **This endpoint names a class**, with the same candidate producers in file 6 as the two cingulate
    entries above. **Owed: resolve to named producers, or withdraw.**
  - **← visual areas** — **carries:** payload **unknown — owed. Fan-in:** unknown. **This endpoint
    names a class.** The entry's Function slot requires **external visual landmarks**, so this is the
    edge that would supply half of what the region is said to fuse; the medial parieto-occipital
    candidates that would most plausibly supply it are themselves regions the source names on edges
    and does not describe. **Owed: name the producers.**
  - **← the cingulum** — **this is a tract, not a producer**, recorded as routing rather than as an
    edge, as at the two cingulate entries above.
  - **Dangling requirement — the self-motion half of the fusion.** The Function slot fuses **internal
    self-motion cues (vestibular, proprioceptive, motor efference)** with external landmarks, and
    **no incoming edge above declares any of the three.** Whether they arrive by way of the anterior
    thalamic head-direction signal, the parietal class endpoint, or a producer not yet named is not
    stated. **Owed, and it is this entry's largest gap**: both halves of the fusion the entry exists
    to perform are undeclared at their sources.
- **Outputs:**
  - **→ the hippocampal formation**, via **parahippocampal and entorhinal cortex** — **carries:** the
    **return arm of the spatial-memory loop** — heading and landmark information after the
    egocentric-to-allocentric translation this region performs. **Payload otherwise owed. Fan-out:**
    unknown. **The consumer declares it** (file 8), written there from this entry's declaration.
    **Two-ended.**
  - **→ the anterior thalamic nuclei** — **carries:** payload **unknown — owed. Fan-out:** unknown.
    **The consumer records this edge as one it does not carry** (file 12): its Inputs slot has no
    cortical line at all, and it marks the reciprocal limb owed at that end. **Two-ended in intent
    only; owed at the consumer.**
  - **→ the precuneus** — **carries:** the **return arm of the spatial-memory loop**, in the same
    terms as the hippocampal limb above. **Payload otherwise owed. Fan-out:** unknown. **The consumer
    declares it** (file 6), written there from this entry's declaration, and records that this is the
    one incoming edge that could supply that entry's headline visuospatial-imagery function.
    **Two-ended.** *(The three lines above were split this pass out of "back to the hippocampal
    formation (via parahippocampal / entorhinal cortex), the anterior thalamus, and parietal /
    medial-parietal (precuneus) cortex", which named three targets and one payload; their far ends
    have three different statuses.)*
- **Internal structure and internal data flow:** two sub-elements, **area 29**, which is **granular**,
  and **area 30**, which is **dysgranular** — the division is architectonic and is in the entry's own
  heading. **The standard laminar block is not transcribed here**: the entry spans a granular /
  dysgranular internal border, so a single block would assert a layer-4 circuit across tissue that
  has layer 4 on one side of the border and not the other — the same failure mode §3a records for
  Broca's area. **Internal edges: owed**, and so is the prior question of whether areas 29 and 30
  project to different targets, which is §3's test for a sub-element as against a property.
  *(Class 3 — general anatomy for the two areas and their granularity; the reading that this entry
  belongs with §3a's across-an-internal-border cases is Claude's, Class 2. No primary source was
  opened and no search was run for this entry in this pass.)*
- **Neurons:** soft / unknown — a small granular / dysgranular peri-allocortical strip, no clean human
  per-region count.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown. **White-matter volume:**
  unknown. **Myelination:** unknown.
- **Pass:** 2026-07-25 — prose slots converted to typed edges; hippocampal, anterior-thalamic and precuneus limbs confirmed two-ended against files 8, 12 and 6; the parahippocampal producer recorded as having no entry; Internal structure slot added and the standard laminar block withheld as spanning a granular / dysgranular border

**This wall is described:** the **insula** (posterior interoceptive → anterior salience / feeling
gradient, with von Economo neurons), the **claustrum** (the most-connected structure per unit volume,
function still debated — Crick–Koch binding / consciousness, synchronisation, salience), the
**habenula** (medial habenula → interpeduncular nucleus; lateral habenula → rostromedial tegmental
nucleus → ventral tegmental area and substantia nigra pars compacta dopamine inhibition, the
negative-value brake — closing the ventral-tegmental-area "lateral habenula = negative value" hook),
and the **cingulate remainder** — **midcingulate** (action–outcome / cingulate-motor hub),
**posterior cingulate** (default-mode), and **retrosplenial** (Papez / spatial) — the three linked
along the **cingulum** tract (white-matter-tracts file). Counts are soft for all the cortical members
(association / paralimbic cortex, uncounted per-region in human) and for the claustrum (thin sheet);
the habenula carries a firm volume (~30–36 mm³ per side). The medial limbic-midline belt is described,
and the cingulate cortex is described end to end (subgenual / pregenual anterior cingulate cortex in
the frontal-lobe file → midcingulate → posterior cingulate → retrosplenial).

**Two regions this file's edges point at have no entry in any of the twenty files**, checked
2026-07-25: the **interpeduncular nucleus**, which is the medial habenula's principal output and
appears nowhere else in the source, and the **septal nuclei**, which are the medial habenula's
principal input and are named as producers by two other files as well. A third, the
**parahippocampal cortex**, is named as a producer here and by three other files. **Every payload in
the claustrum entry is owed**, including the one its function depends on, so the completion test
fails at that entry: what leaves the claustrum on a wire cannot be said.

---


## References

*(Section added 2026-08-12 under source design §2a. Every line below is a **candidate**
awaiting Micky's verification; none is verified. Each full reference given here was obtained by
a web search run in this pass against publisher, journal or PubMed records — no reference is
written from recall. Keys reading **owed** were not searched in this pass.)*

**30 distinct keys, 32 mentions. 2 searched to a full reference; 1 partial; 27 owed.**

**The habenula's one firm volume is two figures that do not agree, presented as one range.** Lines
384–387 give ~30–36 mm³ per side, with post-mortem ~31/33 mm³ from *Ranft et al. 2010* and
magnetic-resonance imaging ~29–36 mm³ from *Savitz et al. 2011*, reading as a converged range
across two methods. **The literature citing those two papers puts the post-mortem figure at ~32 mm³
per hemisphere and the in-vivo figure at ~18.5 mm³ per hemisphere** — roughly half, not
overlapping — **and states a reason for the gap.** This is the sharpest finding in this pass. See
the two entries.

**And *Savitz et al. 2011* is two papers.** Both appeared in 2011 with overlapping author lists on
habenula volume by high-resolution magnetic resonance imaging, and the literature distinguishes
them as 2011a and 2011b. The key as written names neither. **Same shape as the two-papers-one-key
case in file 15.**

**The claustrum's headline fact divides by a denominator this file already marks as soft.**
*Torgerson et al. 2015* is confirmed exactly — the claustrum has the highest connectivity in the
brain by regional volume — but the measurement is **diffusion tractography with the claustrum mask
drawn by hand**, because the segmentation software used assigns no voxels to the structure at all.
**A per-unit-volume claim is a ratio, and its denominator is that hand-drawn volume.** Line 277 of
this file already records the claustral volume as *soft, segmentation-dependent*. **The two
statements are about the same number and the file does not connect them.** See that entry.

**Two keys are one work written two ways, twice over.** *Morel, Gallay, Baechler et al.* and
*Morel et al.* (179, 193); *Crick & Koch 2005* and *Crick–Koch* (211, 654). And *Craig* at line 48
carries no year while *Craig 2009* four lines later does — either two works or one key written
twice. **Owed at the citing lines.**

**One key names no work.** Line 187–188's *the comparison of seven cyto- and myeloarchitectonic
studies in the primate insula literature* is the sole support for the **Contested** block on how
many insular subdivisions there are — a block that governs where every insular edge is placed.
**It has no author, year, title or identifier. Owed: name it.**

**A note on what this file's own marks already say.** Five of the six entries carry, in their
Internal-structure slots, the words *no primary source was opened and no search was run for this
entry in this pass* — claustrum, habenula, midcingulate, posterior cingulate, retrosplenial. **That
is the file declaring its own reference state before this section existed**, and it is accurate:
twenty-seven of thirty keys remain unsearched. **The insula entry is the exception** and carries
three named human cytoarchitecture sources with sample sizes and methods on the line, which is the
best-formed citation block in this file.

**Species composition of the three searched: all human.** *Ranft* post-mortem, *Savitz* in vivo,
*Torgerson* in vivo — which is unusual for this source and reflects that this file's quantitative
claims are volumes and connectivity rather than cell counts.


- **Buckner et al. 2005** — **owed**: not searched in this pass. Carries the retrosplenial
  Alzheimer-pathology claim. *(Line 580.)*
- **Craig** — **owed**, **and the key carries no year**, written possessively at line 48 for the
  "interoception / the material me" formulation. **Either the same work as *Craig 2009* below or a
  different one; the file does not say.** *(Line 48.)*
- **Craig 2009** — **owed**: not searched in this pass. **It is the source of the insula entry's
  organising claim** — the posterior-to-anterior gradient from body state to subjective feeling, and
  the self-awareness reading. **Highest-value owed key in the file**, because the Function slot, the
  two internal edges, and the failed completion test at line 172 all rest on it. *(Line 52.)*
- **Crick & Koch 2005** — **owed**: not searched in this pass. The "conductor of the cortical
  orchestra" proposal. **Same work as *Crick–Koch* at line 654.** *(Line 211.)*
- **Crick–Koch** — **the same work as the key above**, written as a hyphenated pair in the closing
  paragraph. **Owed at the citing lines: use one key.** *(Line 654.)*
- **Critchley et al. 2004** — **owed**: not searched in this pass. Carries the right-anterior-insula
  interoceptive-accuracy result. *(Line 55.)*
- **Jhou et al. 2009** — **owed**: not searched in this pass. **It carries the indirect-suppression
  mechanism that the habenula entry's Function slot turns on** — the lateral habenula driving the
  rostromedial tegmental nucleus, which inverts sign onto dopamine cells. That edge is declared
  two-ended against file 14. *(Line 291.)*
- **Koubeissi et al. 2014** — **owed**: not searched in this pass. **A single human stimulation
  case**, which the citing line says. *(Line 216.)*
- **Kurth, Zilles, Fox, Laird & Eickhoff, Cerebral Cortex 20:1448, 2010** — **owed**: not searched
  in this pass. Ten human post-mortem brains, quantitative image analysis, per the citing line.
  **One of three keys carrying the insular area nomenclature (Ig1, Ig2, Id1, Ig3, Ia1, Id2–Id6) that
  the Internal-structure slot is written in.** *(Line 176.)*
- **Leech, Braga & Sharp 2012** — **owed**: not searched in this pass. *(Line 494.)*
- **Leech, Kamourieh, Beckmann & Sharp 2011** — **owed**: not searched in this pass. With the 2012
  paper, the source of the dorsal/ventral posterior-cingulate split, **which the Internal-structure
  slot uses as its §3 sub-element test** — the two sectors projecting to different targets. **The
  test's evidence is these two keys.** *(Line 493.)*
- **Li et al. 2011** — **owed**: not searched in this pass. The learned-helplessness / depression
  circuit account. **Note the key is a bare "Li et al." with a year**, which is among the least
  distinctive author strings possible; searching it will need the claim as well as the name.
  *(Line 294.)*
- **Matsumoto & Hikosaka 2007** — **owed**: not searched in this pass. **It carries the lateral
  habenula's defining payload** — excitation by aversive events and by omitted reward, the negative
  reward-prediction error mirroring midbrain dopamine neurons — **which is the payload written onto
  the rostromedial-tegmental and raphe output edges and consumed in files 13 and 14.** **Highest-value
  owed key after Craig 2009**, because it is the one whose content travels furthest across the
  source. *(Line 288.)*
- **Menon & Uddin 2010** — **owed**: not searched in this pass. With Seeley, the salience-network
  and network-switching account. *(Line 54.)*
- **Morel et al., Neuroscience 236:117, 2013** — **the same work as the key below**, cited in short
  form at the von Economo correction. See that entry. **Owed at the citing lines: use one key.**
  *(Line 193.)*
- **Morel, Gallay, Baechler et al., Neuroscience 236:117, 2013** — **owed**: not searched in this
  pass. Human architectonics with post-mortem magnetic-resonance registration, per the citing line.
  **It is the sole source of the Correction block at lines 189–193** — that the von Economo neuron
  field crosses from agranular into dysgranular insula rather than marking the boundary — which
  amends the entry's own Function slot. **A correction resting on one unsearched key.** **Same work
  as *Morel et al.* at line 193.** *(Line 179.)*
- **Naqvi & Bechara 2007** — **owed**: not searched in this pass. The insula-damage / smoking-
  cessation result. *(Line 57.)*
- **Narikiyo et al. 2020** — **owed**: not searched in this pass. The slow-oscillation regulation
  hypothesis. *(Line 214.)*
- **Platt 2009** — **owed**: not searched in this pass. *(Line 495.)*
- **Quabs, Caspers, Schöne et al., NeuroImage 260:119453, 2022** — **owed**: not searched in this
  pass. Ten human post-mortem brains, three-dimensional probability maps, per the citing line. **The
  most recent of the three insular cytoarchitecture keys and the one with a full journal string**, so
  the cheapest of the three to search. *(Line 177.)*
- **Ranft et al. 2010** — Ranft, K., Dobrowolny, H., Krell, D., Bielau, H., Bogerts, B. &
  Bernstein, H.-G. Evidence for structural abnormalities of the human habenular complex in affective
  disorders but not in schizophrenia. *Psychological Medicine* 40(4): 557–567. **Human, post-mortem**,
  in a mixed sample of unipolar and bipolar depression patients with controls. *(Cambridge University
  Press record as cited in three independent reference lists; **the publisher's own page was not
  opened this pass and the digital object identifier was not captured** — owed.)* **The year on this
  key is not stable in the literature**: reference lists give both 2009 and 2010 for volume 40,
  pages 557–567, which is the epub-versus-issue split. **Two findings.** **First, the citing line's
  characterisation is exactly right** — line 379–381 says this is stereology reporting volumes and
  disease-related changes rather than a control absolute, and that is what the paper is. **Second,
  and this is the one to act on: the ~31/33 mm³ figures are consistent with the literature's ~32 mm³
  per hemisphere, but they do not span the same range as the magnetic-resonance figure the file pairs
  them with.** See the *Savitz* entry. *(searched 2026-08-12; candidate. Lines 379, 385.)*
- **Rolls's (2019)** — **owed**: not searched in this pass. It carries the three-way action–outcome
  account — anterior cingulate supplying outcome, posterior cingulate supplying action and space,
  midcingulate motor area converting the convergence into a plan — **which is the frame the whole
  midcingulate entry is organised on.** *(Line 400.)*
- **Savitz et al. 2011** — **partial, and the key names two papers.** Two 2011 reports with
  overlapping author lists measured habenula volume by high-resolution magnetic resonance imaging:
  Savitz, J.B., Nugent, A.C., Bogers, W., Roiser, J.P., Bain, E.E., Neumeister, A., Zarate, C.A.,
  Manji, H.K., Cannon, D.M., Marrett, S., Henn, F., Charney, D.S. & Drevets, W.C. (2011), *Habenula
  volume in bipolar disorder and major depressive disorder: a high-resolution magnetic resonance
  imaging study*, *Biological Psychiatry* 69(4): 336–343, doi 10.1016/j.biopsych.2010.09.027; and
  Savitz, J.B., Bonne, O., Nugent, A.C., Vythilingam, M., Bogers, W., Charney, D.S. & Drevets, W.C.
  (2011), *Habenula volume in post-traumatic stress disorder measured with high-resolution MRI*,
  *Biology of Mood & Anxiety Disorders* 1: 7, doi 10.1186/2045-5380-1-7. **Human, in vivo**, 3-tesla
  imaging at approximately 0.4 mm³ resolution with manual segmentation by a single blinded rater.
  *(BioMed Central publisher record for the second; the first from three independent reference
  lists, publisher page not opened — owed.)* **The finding: the file's ~29–36 mm³ does not match what
  the literature reports these papers to have found.** Two independent sources citing them give the
  in-vivo figure as **approximately 18.5 mm³ per hemisphere**, against approximately 32 mm³
  post-mortem, **and one states the reason** — that the in-vivo value may be an underestimate,
  because the lateral and anterior boundaries of the habenula are hard to resolve at this scale.
  **So the two methods disagree by nearly a factor of two, for a stated methodological reason, and
  line 384's "~30–36 mm³ per side" presents them as one converged range.** **If this holds, the
  file's one firm volume is not firm** — it is a post-mortem figure and an in-vivo figure that
  bracket nothing in common, and the entry's own remark that the structure is about the size of a
  single functional-imaging voxel is exactly why. **Read from secondary citations, not from either
  paper: a candidate, and the one worth opening a paper for.** **Owed: which of the two 2011 papers
  the key means, and what number each actually reports.** *(searched 2026-08-12; candidate, partial.
  Line 386.)*
- **Seeley et al. 2007** — **owed**: not searched in this pass. The salience-network identification.
  *(Line 54.)*
- **Shackman et al. 2011** — **owed**: not searched in this pass. Carries the negative-affect / pain
  / cognitive-control convergence in anterior midcingulate cortex. *(Line 398.)*
- **the comparison of seven cyto- and myeloarchitectonic studies in the primate insula literature**
  — **owed, and the key names no work** — no author, year, title, journal or identifier. **It is the
  sole support for the Contested block at lines 182–188**, which records that published insular
  parcellations range from a two-part scheme to one naming sixteen granular areas, and which is why
  this entry places its edges on the gradient's poles rather than on any one parcellation. **A
  structural decision resting on an unnamed source. Owed: name it.** *(Line 187.)*
- **Torgerson et al. 2015** — Torgerson, C.M., Irimia, A., Goh, S.Y.M. & Van Horn, J.D. (2015). The
  DTI connectivity of the human claustrum. *Human Brain Mapping* 36(3): 827–838; doi
  10.1002/hbm.22667; PubMed 25339630; PMC4324054. **Human, in vivo**, N = 100 healthy subjects,
  structural and diffusion tensor imaging with network-theoretic analysis. *(Wiley publisher record,
  PubMed and PubMed Central.)* **The claim is the paper's own, verbatim in substance**: the claustrum
  has the highest connectivity in the brain by regional volume. The paper adds two results the file
  does not carry — that the claustrum is a primary contributor to global network architecture, and
  that its strongest connectivity dependencies are with the frontal lobe and the cingulate regions,
  **which is the specificity the entry's all-to-all class endpoint says the literature does not
  report.** **The finding is methodological, and this file already has half of it.** The claustrum
  mask had to be **drawn by hand** — the paper records that the segmentation software used assigns no
  voxels to the claustrum at all — and was delineated by one author, then reviewed by two others.
  **A per-unit-volume claim is a ratio whose denominator is that hand-drawn volume.** Line 277 of
  this entry already records the claustral grey-matter volume as **soft and segmentation-dependent**
  and declines to give a figure. **Those two statements are about the same number.** The entry's
  headline fact, quoted three times in this file, is a ratio over a quantity the entry itself refuses
  to state. **Owed: say so at line 208, or give the denominator.** **Note also that "connectivity"
  here is diffusion-derived streamline count, not counted projections** — which matters for an entry
  whose completion test already fails on what travels on the wire. *(searched 2026-08-12; candidate.
  Line 210.)*
- **Vann, Aggleton & Maguire 2009** — **owed**: not searched in this pass. **It carries the entire
  retrosplenial Function slot** — the egocentric-to-allocentric translation, head-direction and
  landmark anchoring, and scene construction — **and therefore the requirement that entry's largest
  gap is measured against**: the self-motion half of the fusion that no incoming edge declares.
  **Highest-value owed key in that entry.** *(Line 574.)*
- **Vogt 2016** — **owed**: not searched in this pass. *(Line 398.)*
- **Vogt's "prime" midcingulate fields** — **owed**, written as a possessive lineage with no year at
  both citing lines. **Either the same work as *Vogt 2016* or an earlier parcellation paper; the file
  does not say.** It supplies the areas 24′ and 32′ nomenclature the midcingulate entry's
  Internal-structure slot and heading are written in. *(Lines 466, 479.)*
