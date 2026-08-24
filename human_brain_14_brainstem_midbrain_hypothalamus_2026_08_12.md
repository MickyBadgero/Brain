# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-12
---

---

# FILE 14 OF 20 — BRAINSTEM / MIDBRAIN / HYPOTHALAMUS

**What is in this file.** The brainstem, midbrain and hypothalamus: superior colliculus, the lateral parabrachial nucleus and the three ventrolateral-medulla and solitary-nucleus entries added on 2026-07-19, periaqueductal gray, hypothalamus, pineal gland, the reticular formation, and the rostromedial tegmental nucleus.

**Size:** 1235 lines, ~27.2k tokens / ~109 kB (estimated from bytes, not tokenised). **Entries:** 10. **Edge lines:** 80 — 39 in, 41 out. **Internal structure slots:** 10 of 10. **Pass stamps:** 10 of 10. **Reference keys:** 66, over 69 mentions — the largest key list in the source.

**Full conversion pass 2026-07-24.** The four entries still in pre-conversion prose — periaqueductal gray, hypothalamus, pineal gland, reticular formation — were converted to typed edges with Internal-structure slots, and the superior colliculus (converted 2026-07-19 but never stamped) was stamped. The other four original entries (parabrachial, the two ventrolateral-medulla entries, the solitary nucleus) were already converted on 2026-07-19 and are unchanged. The rostromedial tegmental nucleus was added earlier on 2026-07-24. **All ten entries now carry typed edges, Internal-structure slots, and pass stamps.** The 2026-07-23 preamble correction (pontine nuclei and red nucleus are *not* described in the Cerebellum section) stands, and **both remain owed as new entries** — this pass did not add them.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**An abbreviation pass, 2026-07-27, and it changed no content.** Every abbreviation in the file now carries its full name, and none stands as the only label for anything. Expanded at first use, with the abbreviation kept in parentheses where a reader will meet it elsewhere: **γ-aminobutyric acid (GABA)**, the **hypothalamic–pituitary–adrenal (HPA) axis**, **cerebrospinal fluid (CSF)**, **cyclic adenosine monophosphate (cAMP)**, the **melatonin receptors MT1 and MT2**, **magnetic resonance imaging (MRI)** and computed tomography, messenger **ribonucleic acid (RNA)**, the **ascending reticular activating system (ARAS)**, and **substantia nigra pars compacta (SNc)**. Written out wherever they previously stood alone: the ventral tegmental area, the suprachiasmatic nucleus, the substantia nigra pars reticulata, the paraventricular and supraoptic nuclei, the intermediolateral cell column, the lateral intraparietal area, the frontal eye fields, the rostral ventromedial medulla, the ventrolateral periaqueductal gray, and the rostromedial tegmental nucleus. **The closing paragraph carried the densest cluster and was the largest single repair.** Citation accessions now name their databases once — **PubMed identifier**, **PubMed Central**, **bioRxiv preprint**. No edge, count, payload, owed mark or pass stamp was touched.

**Two things were left standing on purpose.** Journal-title abbreviations in citations — *PLoS Comput Biol*, *PNAS*, *J Neurophysiol*, *Prog Brain Res* and the rest — are a citation convention rather than names of regions, tracts, nuclei or methods, and expanding them would rewrite every provenance mark in the file. And **the file spells the same structure two ways**: *periaqueductal **gray*** in the entry headings and edges, *Grey-matter volume* in every sizing slot, alongside British *defence*. **That is the same defect an abbreviation is** — two strings for one thing, which a dangling-edge diff cannot match — but it is orthography rather than an abbreviation, no research settles it, and picking a house spelling is Micky's.

**Entries in this file, with the date each was last worked:**

- **Superior colliculus (SC) — midbrain orienting / gaze hub (layered tectum)** — pass 2026-07-24 — stamp added to an entry already fully converted on 2026-07-19; edges verified against far ends, no change
- **Lateral parabrachial nucleus — the ascending nociceptive and interoceptive relay to limbic forebrain (pons)** — pass 2026-07-19 — new entry — closes the dominant lamina-I edge; collateral rather than independent population
- **Caudal ventrolateral medulla — baroreflex inhibitory relay and second lamina-I target (medulla)** — pass 2026-07-19 — new entry — baroreflex inhibitory relay and second lamina-I target; territory boundary recorded as contested
- **Nucleus of the solitary tract — the visceral and gustatory entry point (dorsal medulla)** — pass 2026-07-19 — new entry — rostral gustatory / caudal visceral, viscerotopy qualified, blood-borne chemical input recorded as a non-axonal input
- **Rostral ventrolateral medulla — the sympathetic vasomotor drive (medulla)** — pass 2026-07-19 — new entry — presympathetic drive is intrinsically generated, not relayed
- **Periaqueductal gray (PAG) — midbrain defence / analgesia column** — pass 2026-07-24 — prose converted to typed edges; amygdala-central, prefrontal, spinal and locus-coeruleus edges two-ended; rostral ventromedial medulla flagged as a region with no entry; four defence columns recorded as sub-elements; Internal structure slot added
- **Hypothalamus — the homeostatic / neuroendocrine hub (diencephalon)** — pass 2026-07-24 — prose converted to typed edges; retinal/suprachiasmatic, mammillothalamic, amygdala, hippocampal and solitary edges two-ended; pituitary arms and blood-borne sensing recorded as endocrine/non-axonal; eleven sub-nuclei recorded as the file's heaviest owed internal conversion; Internal structure slot added
- **Pineal gland — the circadian endocrine output / melatonin (epithalamus)** — pass 2026-07-24 — prose converted to typed edges; sympathetic efferent chain typed as one clock-gated input; melatonin split into endocrine terminal and suprachiasmatic feedback; Internal structure recorded not applicable (transduces, not computes)
- **Reticular formation — arousal core + autonomic / premotor pattern generators (brainstem tegmentum)** — pass 2026-07-24 — prose converted to typed edges; fastigial, periaqueductal and intralaminar edges two-ended; discrete sub-nuclei named, diffuse remainder marked a borderless network; Internal structure slot added
- **Rostromedial tegmental nucleus (RMTg, tail of the ventral tegmental area) — the aversive brake on dopamine (mesopontine tegmentum)** — pass 2026-07-24 — new entry; the habenula → dopamine-inhibition relay, typed from far ends in files 9, 13, 17; two outputs confirmed two-ended

---

# BRAINSTEM / MIDBRAIN / HYPOTHALAMUS

*The subcortical core beneath the thalamus — the oldest part of the brain and the last large gap
in this map. Much of it is **already described where a pathway needed it**: the auditory cochlear
nucleus and inferior colliculus, the somatosensory dorsal-column / trigeminal nuclei, the
gustatory nucleus of the solitary tract, the four vestibular nuclei, the substantia nigra pars
compacta (SNc, in Basal ganglia), the **inferior olive** (in Cerebellum), and the
neuromodulatory nuclei (ventral tegmental area, locus coeruleus, raphe, basal forebrain, just
above).

***Corrected 2026-07-23.*** *This paragraph previously named the **pontine nuclei** and the **red
nucleus** alongside the inferior olive as already described in the Cerebellum section. **They are
not.** Neither has an entry in that section or in any other file, and the cerebellum file's own
closing paragraph made the matching claim, which has also been corrected. Both are named on edges
in that file — the mossy-fibre input to the cerebellar cortex, the deep nuclei's output, and both
limbs of the dentato-rubro-olivary loop — and **naming a region on an edge is not describing it.***

***Both belong to this section and to Cerebellum, because the loop they sit on crosses the boundary
between them.*** *Anatomically they are here: the pontine nuclei occupy the ventral two-thirds of
the pons, the red nucleus the ventral midbrain. Functionally they are cerebellar-loop stations —
the corticopontocerebellar relay in one case, and in the other a nucleus whose large parvocellular
part belongs to the olivo-cerebellar circuitry while its magnocellular part, the motor one, is
vestigial in humans. **The section split is by data flow and this loop runs through two sections,
so neither owns these two alone.** **Owed: write both entries, and decide which file physically
carries each — the other must then reference it and must not treat the endpoint as missing.** The
researched material for both is recorded at the cerebellum file's entries, so writing them is a
transcription rather than new research.*

*This section adds the four stations that were still open: the **superior colliculus** (midbrain orienting /
gaze hub), the **periaqueductal gray** (midbrain defence / analgesia column), the **hypothalamus**
(the homeostatic / neuroendocrine hub), and the **reticular formation** (the arousal core plus the
autonomic and premotor pattern generators) — plus, appended after the hypothalamus, the
**pineal gland**, the circadian system's endocrine output arm (epithalamus), which closes the
suprachiasmatic-nucleus → melatonin loop. These are small, ill-bordered, or many-nucleus
structures, so counts here
are mostly **soft** — the exceptions are the suprachiasmatic nucleus and the pineal, which carry
firm human figures (a neuron count and a volume respectively). **Number convention:** these are midline / bilateral structures;
paired nuclei are given per side, midline structures whole (both sides), tagged as such.*

## Superior colliculus (SC) — midbrain orienting / gaze hub (layered tectum)

- **Function:** the layered midbrain hub for **orienting gaze and attention** to salient events,
  in two functional tiers. The **superficial layers** (stratum griseum / album superficiale) are
  purely **visual** — a retinotopic map driven by the retina and V1, and the structure through
  which residual "blindsight" orienting acts after V1 damage (Weiskrantz). **Both halves of that
  sentence are now qualified**: direct measurement in the awake macaque puts the visual drive
  through the geniculate and V1 rather than through the retinal input, and the blindsight role is
  evidenced in the *chronically* lesioned brain. Stated in full under Internal structure. The
  **intermediate and
  deep layers** (stratum griseum / album intermediale and profundum) hold **spatially-aligned
  multisensory maps** (visual, auditory, and somatosensory space in register) and a **motor map**
  for saccades and head/orienting movements — the classic site of **multisensory enhancement** (a
  weak cross-modal pair drives a deep-layer cell more than the sum of either alone; Stein & Meredith).
  Functionally it is a retinotopic **priority/salience map** whose active locus specifies the next
  gaze target — the subcortical complement to the lateral intraparietal area's cortical priority
  map.
- **Inputs:**
  - **← retina, onto the stratum griseum superficiale** (the retinotectal projection) —
    **carries:** retinotopic luminance transients for orienting; **payload otherwise unknown —
    owed.** Not more than **10%** of macaque retinal ganglion cells contribute, about **6%** near
    the fovea; the input is largely a **branch of axons that also reach the lateral geniculate
    nucleus** rather than a separate population. It terminates in the **upper** part of the
    superficial gray, just below the stratum zonale, and is segregated by eye into alternating
    columns and strata even though cells here respond to either eye. **Fan-in:** unknown.
    *(Class 1 — Perry & Cowey 1984; Zheng, Adams, Horton et al., J Neurosci 44, 2024; Hubel, LeVay
    & Wiesel 1975; macaque. Not yet verified for the source.)*
  - **← V1, from 5b, onto the superficial layers** — **carries:** retinotopic salience for
    orienting; **payload otherwise unknown — owed.** Declared at the V1 end as a layer-5b output.
    The corticotectal projection originates predominantly in layer 5 and is reported as strongly
    magnocellular-driven. **Fan-in:** unknown. *(Class 1 — Lund et al. 1975; Fries 1984; macaque.)*
  - **← extrastriate and parietal cortex, and specifically the ventral lateral intraparietal
    area, onto the intermediate layers** — **carries:** the **priority (salience) map** — one
    scalar per retinotopic location ranking it by behavioural priority, modality-free. Declared at
    the lateral intraparietal area's end. The ventral subdivision is the one with the strong
    projection to the deep layers here; the dorsal subdivision is not. **Fan-in:** unknown.
    *(Class 1 — Chen et al., PNAS 113, 2016; Blatt, Andersen & Stoner 1990; macaque.)*
  - **← frontal eye field, onto the intermediate layers** — **carries:** a saccade goal — the
    cortically selected target location, in eye-centred coordinates. **Payload otherwise unknown —
    owed.** **Fan-in:** unknown. *(Class 3 — general anatomy.)*
  - **← inferior colliculus** — **carries:** auditory **azimuth and elevation** — azimuth derived
    from the interaural cues in the superior olivary complex, elevation from the dorsal cochlear
    nucleus's spectral notches — in a frame this structure's orienting map can register against the
    visual one. **This line previously read "the auditory space map" and the phrase is withdrawn**:
    a topographic map of auditory space is well characterised in the barn owl's external nucleus and
    has one report in a mammal, in a subdivision other than the one that sends this edge. Stated in
    full at the inferior colliculus. **The registration between the auditory and visual maps at this
    structure is separately attested and is not affected by the withdrawal.**
    **Corrected 2026-07-19, later the same day: the withdrawal was too broad, and this is the place
    the correction belongs.** A topographic **auditory space map does exist in the mammalian
    superior colliculus** — it is the *only* mammalian subcortical structure in which one has been
    found. So the map is real here; what was wrong was attributing it to the **inferior colliculus**
    and treating it as arriving on this edge already formed. **The map is built at this structure,
    not relayed into it**, which is consistent with what the colliculus is for: the visual,
    auditory and somatosensory maps are registered here to drive orienting, and the auditory one has
    to be in the same frame as the others to be of any use. **The consequence for this edge stands
    unchanged** — what arrives from the inferior colliculus is azimuth and elevation, not a map —
    and the consequence for this entry is that its Function field's spatial-map language is now
    supported rather than merely tolerated. *(Class 1 — King & Palmer 1983; Middlebrooks & Knudsen
    1984, as reported in Cerebral Cortex 26:450, 2016. Not yet verified for the source.)*
    **Fan-in:** unknown.
  - **← somatosensory afferents** — **carries:** body-surface location of touch, somatotopic.
    **Payload otherwise unknown — owed.** **Fan-in:** unknown. *(Class 3.)*
  - **← olivary pretectal nucleus, onto the stratum griseum intermediale** — **carries:** payload
    **owed** — the luminance scalar, arriving in the premotor rather than the visual layers.
    Declared at the pretectum's end, where the tracing is **rat** and no macaque confirmation was
    read. Recorded because it is a light signal reaching the orienting map by a route that is not
    the retinotectal one. **Fan-in:** unknown. *(Class 1 — Klooster et al., PubMed identifier 8542320, albino
    rat. Not yet verified for the source.)*
  - **← substantia nigra pars reticulata** (basal-ganglia output) — **carries:** **tonic
    inhibition, and its release** — no content whatever. The saccade is not commanded by this edge;
    it is **permitted** by a pause in the tonic firing arriving on it, so what is on this wire is a
    gate, and its informative event is a *cessation*. **Fan-in:** unknown. *(Class 1 — Hikosaka &
    Wurtz lineage, macaque.)*
- **Outputs:**
  - **→ the brainstem saccade burst generators**, from the intermediate and deep layers — the
    **paramedian pontine reticular formation** (horizontal) and the **rostral interstitial nucleus
    of the medial longitudinal fasciculus** (vertical) — **carries:** a **saccade displacement
    vector, as a place code**. The vector is specified by *where* the active population sits in the
    motor map, not by how fast it fires: amplitude runs rostral (small) to caudal (large) and
    direction runs medial to lateral, and the population is a two-dimensional activity hill whose
    locus is the message. **The payload change at this stage is spatial-to-temporal**: a location on
    a map goes in, a timed burst driving eye muscles comes out. **This is the one place in the
    visual line where a payload is a position in tissue rather than a value on a line**, and a
    consumer reading firing rate alone would recover nothing. **Fan-out:** unknown. *(Class 1 —
    Wurtz & Goldberg 1972; Van Opstal/Goossens lineage, PLoS Comput Biol 8:e1002508, 2012;
    macaque.)*
    **Contested, recorded not smoothed:** whether the *rate* on top of the place code is itself
    payload is disputed. One line of work reports peak firing rate falling and burst duration
    rising systematically from rostral to caudal, and reads the kinematics of the saccade out of
    that gradient; another reports that the motor burst does not dictate movement kinematics. The
    place code is not in dispute; what the rate adds to it is. *(Class 1 — PLoS Comput Biol 2012;
    bioRxiv preprint 2021.06.24.449726 / PubMed Central PMC9652463; macaque.)*
  - **→ the tectospinal tract → cervical spinal cord**, from the deep layers — **carries:** a head
    and body orienting command, in the same map's coordinates. **Payload otherwise unknown —
    owed.** **Fan-out:** unknown.
  - **→ pulvinar and other thalamus → cortex**, from the intermediate and deep layers —
    **carries:** payload **owed**. This is the colliculo-pulvinar-cortical route that runs parallel
    to the geniculostriate one, and it is a **candidate** carrier for residual vision after V1
    damage — declared as a candidate at the middle temporal area's entry too, where it competes
    with the direct geniculate route. **Fan-out:** unknown.
  - **→ V3 and the middle temporal area, di-synaptically via the pulvinar** — **carries:** payload
    **owed**. Declared at the V3 end. The relay reaches those two areas **selectively**.
    **Fan-out:** unknown. *(Class 1 — Lyon, Nassi & Callaway 2010, macaque.)*
  - **→ frontal eye field and the lateral intraparietal area**, reciprocally, via the thalamus —
    **carries:** **corollary discharge of the saccade command** — *the eye is about to move, by this
    vector*. Declared at the lateral intraparietal area's end, where it is the signal that permits
    predictive remapping, and its usefulness depends on arriving **before** the movement.
    **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(Added 2026-07-19 from web search. No full paper
  was opened — abstracts and search excerpts only. Species noted per line; the interlaminar circuit
  work is rat, hamster and ferret. **Nothing here is yet verified for the source.**)*

  **Laminar sub-elements: seven, and they are not cortical layers.** From the surface down:
  **stratum zonale**, **stratum griseum superficiale**, **stratum opticum**, **stratum griseum
  intermediale**, **stratum album intermediale**, **stratum griseum profundum**, **stratum album
  profundum** — alternating grey (cell) and white (fibre) laminae. The grouping the Function field
  uses maps onto them: superficial = stratum zonale through stratum opticum; intermediate = the
  two intermediale layers; deep = the two profundum layers. **These are not the six-layer cortical
  scheme and nothing in this entry should be read against it** — the colliculus is tectum, and its
  laminae are a different object that happens to share the word. *(Class 3 — May, Prog Brain Res
  151:321, 2006.)*

  **Tangential sub-elements: one map, twice over, in register.** The superficial layers carry a
  retinotopic **visual** map; the intermediate and deep layers carry **auditory and somatosensory**
  maps spatially aligned with it, and a **motor** map of saccade vectors aligned with all three.
  Alignment is the structure: a location in the tissue means the same direction in the world at
  every depth. **The rostral pole is functionally distinct** — small saccades and microsaccades are
  represented there, and it is described in behavioural work as a **fixation zone** whose cells fire
  continuously during fixation. *(Class 1 — Stein & Meredith lineage; Munoz & Wurtz 1995; Hafed &
  Krauzlis 2012; cat and macaque.)*

  **Cell classes in the intermediate layers, by discharge rather than by place.** **Burst**
  neurons fire a vigorous burst locked to saccade execution and little before it; **buildup**
  (visuomotor prelude) neurons fire continuously from target onset until the saccade begins.
  **These are two payloads on one map** — a decision accumulating, and a movement being issued —
  and they are not separated spatially. This is the same difficulty the medial superior temporal
  area's congruent and opposite cells raise for the slot: what it would mean for an edge to
  terminate on the buildup cells and not the burst cells is **owed**. *(Class 1 — Munoz & Wurtz
  1995; Basso & Wurtz 1998; macaque.)*

  **Internal edges:**
  - **stratum griseum superficiale and stratum opticum → stratum griseum intermediale** —
    **carries:** the visual map into the premotor map; this is the edge on which "see it, look at
    it" depends, and it is the whole reason the structure is one structure and not two.
    Photostimulation with caged glutamate evokes synaptic excitatory currents in intermediate-layer
    cells, abolished by sodium-channel block, confirming a real synaptic pathway rather than shared
    afferents. **The geometry is a column with a wide skirt:** stimulation within roughly a 500 µm
    column directly above the recorded cell gives the largest and most reliable response, but
    off-axis stimulation up to **1,000 µm** away is still effective, matching the dendritic spread
    of the superficial **wide-field vertical** cells. **Fan-in:** unknown. **Fan-out:** unknown.
    *(Class 1 — Helms, Ozen & Hall, J Neurophysiol 91:1706, 2004, rat; Isa & Hall 2009 review.)*
  - **superficial wide-field vertical cells → the deep laminae** (the interlaminar projection's
    main carrier) — **carries:** the same visual signal, and the class composition is measured:
    of superficial cells with well-filled axons, **43%** sent at least one collateral to the deep
    laminae, but the contribution is **not even across cell types** — about **79%** of wide-field
    vertical cells did, **55%** of narrow-field vertical cells, and under 20% of stellate and
    horizontal cells. **So the interlaminar edge is carried by a named minority of the superficial
    population, not by the layer as a whole**, and an account that says "the superficial layers
    project to the intermediate layers" over-declares its source. **Fan-in:** unknown. **Fan-out:**
    unknown. *(Class 1 — Mooney/Rhoades lineage, J Neurosci 8:1384, 1988, intracellular horseradish
    peroxidase, hamster.)*
  - **stratum griseum intermediale, upper part → its middle part** — **carries:** the same signal,
    relayed. Cells in the middle of the intermediate gray responded to visual-layer stimulation
    **less** reliably than those just above and below them, while responding to focal stimulation
    within the upper intermediate gray — so part of the intermediate layer reaches the visual
    layers **indirectly**, through the rest of its own layer. **Fan-in:** unknown. **Fan-out:**
    unknown. *(Class 1 — Helms, Ozen & Hall 2004, rat.)*
  - **within the intermediate layers: lateral excitation and inhibition across the map** —
    **carries:** the competition that selects one location. Horizontal connections within the
    intermediate gray are documented, and the rostral fixation zone and the caudal saccade zone are
    described as mutually inhibitory. **Whether the selection is winner-take-all is disputed** —
    in the double-step paradigm a saccade sometimes starts toward the first target and curves
    toward the second, which a strict winner-take-all does not produce. **Fan-in:** unknown.
    **Fan-out:** unknown. *(Class 1 — J Neurosci 26:4763, 2006, in vitro; Port & Wurtz 2000; Keller
    2004; rat and macaque.)*

  **The serial model is the textbook reading and is not the only one on offer.** Three schemes have
  been proposed for how the layers relate: superficial → intermediate → out; superficial and
  intermediate converging on an intercalated layer that provides the output; and the layers having
  **independent inputs and outputs**. The evidence above establishes that the superficial →
  intermediate pathway **exists**; it does not establish that it is the route the deep layers'
  output normally rides on. Recorded as unsettled. *(Class 1 — Mohler & Wurtz 1976, as reviewed in
  PubMed 19710376.)*

  **A 2026 result that contradicts this entry's own Function field, recorded rather than smoothed.**
  The Function field says the superficial layers are a retinally driven visual map and the
  subcortical arm of vision that survives V1 damage. A direct causal test disputes the first half of
  that. Reversibly inactivating the lateral geniculate nucleus in awake macaque **abolished visually
  evoked spiking in the colliculus** — a 98% mean reduction, significant in **115 of 115** neurons —
  while leaving **saccade-related bursts unchanged**, including within single cells that carried
  both. The loss extended into the **retinorecipient superficial layers themselves**, persisted for
  motion, flicker and looming stimuli chosen to favour the magnocellular cells the retinotectal
  tract arises from, and was not relieved by silencing the opposite colliculus. Inactivating V1
  reduced collicular visual responses in proportion to how much of the stimulus fell inside the
  V1-induced scotoma. Retrograde labelling confirmed the retinotectal axons were structurally
  intact. **The conclusion drawn is that direct retinal input is not sufficient to drive spiking
  here in the intact awake primate, and that the visual drive arrives through the geniculate and
  V1.**
  **What this does and does not settle, stated carefully.** It is a **preprint, not peer-reviewed**,
  in **two animals**, under **acute** inactivation and passive viewing. It does not eliminate the
  retinotectal edge, which is anatomically present and was verified present in the same animals; the
  authors' own reading is that its contribution may be **permissive or modulatory** — biasing
  excitability, timing, or the competition across the map — rather than additive spiking, or may be
  developmental. It does not refute blindsight either: chronic V1 lesions are followed by weeks to
  months of circuit reweighting, and collicular visual activity **is** preserved in chronically
  lesioned animals. It also runs against an earlier anaesthetised study that found superficial
  retinorecipient responses spared by magnocellular geniculate block. **The effect on this file is
  specific:** the payload on the retina → superior colliculus edge is now **owed and contested**,
  not merely owed, and the Function field's "subcortical arm of vision" is a claim about the
  chronically lesioned brain rather than the intact one. *(Class 1 — Katz, Yu & Krauzlis, bioRxiv
  10.64898/2026.04.27.721202, posted 2026-04-30, macaque, muscimol inactivation; the full text was
  opened for this entry. Schiller, Malpeli & Schein 1979 for the contrary anaesthetised result.
  **Post-dates this file's other sources; not yet verified for the source, and worth verifying
  before anything downstream is built on the retinotectal edge.**)*
- **Neurons:** soft / no clean human total — historically counted only in **single midbrain
  sections** (e.g. at the level of the third-nerve exit / superior colliculus / red nucleus), never
  as an unbiased whole-structure stereological figure. Layered like cortex but with subcortical
  packing.
- **Synapses:** unknown. **Axons:** the tectospinal and tecto-oculomotor tracts (counts unknown).
  **Grey-matter volume:** small paired elevation of the tectal plate; specific human figure not
  recorded. **White-matter volume:** unknown. **Myelination:** the alternation of grey (griseum)
  and fibre (album) laminae defines the layering; g-ratio unknown.
- **Pass:** 2026-07-24 — stamp added; this entry was already converted to typed edges and a full Internal-structure slot on 2026-07-19 (with the retinotectal-payload contest and the geniculate-inactivation result recorded then and later) but carried no pass stamp; edges verified against their far ends this pass, no change needed

## Lateral parabrachial nucleus — the ascending nociceptive and interoceptive relay to limbic forebrain (pons)

- **Function:** the pontine relay that carries body-state and nociceptive signals to **limbic**
  targets rather than to sensory cortex. It is the destination of the great majority of the spinal
  cord's superficial-dorsal-horn output, and its projection to the **central nucleus of the
  amygdala** is held to carry the **affective** dimension of pain — the unpleasantness, as distinct
  from the location and intensity that the thalamocortical line carries. It also relays pruritic
  (itch) and gustatory signals, and participates in aversive learning and feeding.
  *(Class 1 — Sugimura, Takahashi, Watabe & Kato, J Neurophysiol 115:2721, 2016, rat, review and
  channelrhodopsin-assisted circuit mapping; human tract delineation below. Candidates — awaiting
  Micky's verification.)*
- **Human evidence exists and is recent.** The trigeminal-nerve → lateral parabrachial → central
  amygdala circuit was delineated **in vivo in humans for the first time** by diffusion tractography,
  with the right-side circuit showing stronger connectivity in males than females.
  *(Class 1 — Imaging Neuroscience, doi 10.1162/imag_a_00567, 2025, human diffusion tractography at
  3 T and 7 T. Candidate.)*
- **Inputs:**
  - **← Spinal cord grey matter, lamina I**, and **← the caudal spinal trigeminal nucleus** —
    **carries:** the nociceptive, thermoreceptive and pruritic payload typed at the spinal entry.
    **This is the dominant destination of that output, and the proportion is disputed in detail
    while agreed in kind:** one quantitative study finds ~85% of rat lumbar lamina I projection
    cells labelled from here **or** the caudal ventrolateral medulla; a review of the same
    literature states ~95% of ascending lamina I neurons target this nucleus. **Fan-in:** unknown.
  - **A large fraction of the ascending fibres reaching other targets send axon collaterals here**,
    so this nucleus receives what has been described as a **carbon copy** of most nociceptive
    information the cord sends anywhere. That is a structural claim with consequences: an
    architecture that treats the spinothalamic and spinoparabrachial lines as independent channels
    would double-count the source population.
    *(Class 1 — Spike, Puskár, Andrew & Todd, 2003, rat; Sugimura et al. 2016, review. Class 2 —
    the double-counting consequence is Claude's reading. Candidate.)*
  - **← Nucleus of the solitary tract** (visceral and gustatory) — **payload unknown — owed.**
    **Fan-in:** unknown. Typed at the *Nucleus of the solitary tract* entry.
- **Outputs:**
  - **→ Amygdala**, to the **central nucleus** — **carries:** the affective nociceptive payload;
    monosynaptic and excitatory, with feed-forward inhibition in the target. **Payload beyond
    "aversive value" — owed**, and the completion test is not passed: *unpleasantness* is a phrase,
    not a type with a range and a frame. **Fan-out:** unknown.
  - **→ Bed nucleus of the stria terminalis** — **payload unknown — owed.** **Fan-out:** unknown.
  - **→ Hypothalamus** (lateral, ventromedial, dorsomedial and arcuate nuclei; median and lateral
    preoptic) — **carries:** body-state signals driving autonomic and ingestive responses.
    **Payload otherwise unknown — owed.** **Fan-out:** unknown.
  - **→ Intralaminar nuclei** and the ventroposterior parvicellular thalamus — **payload unknown —
    owed.** **Fan-out:** unknown.
  - **→ Insula** and infralimbic cortex — **payload unknown — owed.** **Fan-out:** unknown.
  - **→ Basal forebrain / nucleus basalis of Meynert**, to the substantia innominata — **payload
    unknown — owed.** **Fan-out:** unknown.
- **Contested — whether the spinal nociceptive signal reaches the amygdala through this nucleus or
  only the thalamus.** One report in the literature holds that the parabrachial nucleus channels
  spinal nociceptive signals directly to the intralaminar thalamic nuclei **but not** to the
  amygdala, against the mainstream spino-parabrachio-amygdaloid account above. Recorded as
  contested; the edges are kept because the human tractography and the rodent circuit mapping both
  support them. *(Candidate.)*
- **Internal structure and internal data flow:** several subnuclei are distinguished, of which the
  **subparabrachial nucleus (Kölliker–Fuse)** and the **lateral crescent** are the ones with
  separately described output: they project to the solitary nucleus, the ventrolateral medulla and
  the spinal cord, onto respiratory and autonomic cell groups. **Internal edges — owed;** no
  transfer between subnuclei has been typed here.
- **Neurons:** unknown — no human count found. **Synapses / Axons / Grey-matter volume /
  White-matter volume / Myelination:** unknown.
- **Pass:** 2026-07-19 — new entry — closes the dominant lamina-I edge; collateral rather than independent population

## Caudal ventrolateral medulla — baroreflex inhibitory relay and second lamina-I target (medulla)

- **Function:** **two functions in one territory, described by two literatures that rarely cite each
  other, and the doubling is itself the finding.** In cardiovascular physiology it is the
  **inhibitory link of the arterial baroreflex**: glutamatergic input from the solitary nucleus
  drives **GABAergic** (γ-aminobutyric acid, GABA) neurons here, which tonically inhibit the
    presympathetic neurons of the
  **rostral ventrolateral medulla**, and that inhibition is what converts a rise in arterial
  pressure into withdrawal of sympathetic vasomotor drive. In pain anatomy the same region — lying
  between the lateral reticular nucleus and the spinal trigeminal nucleus — is one of the two
  **dominant supraspinal targets of lamina I**. Whether the lamina-I input and the baroreflex
  neurons are the same cells is not established here. **Owed.**
  *(Class 1 — baroreflex role: Schreihofer & Guyenet, Clin Exp Pharmacol Physiol 29:514, 2002,
  review, rat; Sved, Ito & Madden, Brain Res Bull 51:129, 2000. Lamina-I target: Spike, Puskár,
  Andrew & Todd, 2003, rat retrograde tracing. Class 2 — the observation that the two literatures
  describe one territory is Claude's. Candidates — awaiting Micky's verification.)*
- **Inputs:**
  - **← Spinal cord grey matter, lamina I** — **carries:** the nociceptive and thermoreceptive
    payload typed at the spinal entry. **Fan-in:** unknown.
  - **← the nucleus of the solitary tract**, carrying arterial baroreceptor afferents —
    **carries:** arterial pressure, as a tonic excitatory (likely glutamatergic) drive proportional
    to baroreceptor firing. **Fan-in:** unknown. Typed at the *Nucleus of the solitary tract* entry.
- **Outputs:**
  - **→ the rostral ventrolateral medulla** (presympathetic neurons) — **carries:** **inhibition,
    and it is tonic, not phasic.** This is a sign-inverting edge: excitation here becomes
    suppression of sympathetic vasomotor drive there. Its magnitude is measurable — lesioning these
    neurons in baroreceptor-denervated rats raises arterial pressure by about **40 mmHg** and
    splanchnic sympathetic nerve activity by about **200%**, so the inhibition is load-bearing even
    with the baroreflex removed. **Fan-out:** unknown.
    *(Class 1 — rat lesion study, tonic sympathoinhibition; Schreihofer & Guyenet 2002 review.
    Candidate.)*
    **Name collision, recorded because the file is exposed to it.** The target here is the rostral
    ventro**lateral** medulla, the sympathetic vasomotor source, which has its own entry. Other
    entries in this file refer to the rostral ventro**medial** medulla, the descending-analgesia
    source that acts on the spinal dorsal horn. Two different structures, near-identical names, and
    the same three-letter abbreviation is used for both in the literature.
- **Contested — whether the baroreflex's GABAergic neurons are in this territory at all.** A more
  recent parcellation from the same laboratory lineage divides the lower ventrolateral medulla into
  three segments and places the bulk of those GABAergic neurons, together with the cardiovagal motor
  neurons, in an **intermediate ventrolateral medulla** lying between the rostral and caudal
  territories — reserving "caudal ventrolateral medulla" for the region of **A1 noradrenergic**
  cells. The data flow is not in dispute; where the middle term is drawn on a map is.
  **Recorded as contested at both entries; the file does not pick a side.**
  *(Class 1 — Autonomic Neuroscience 236:102893, 2021. Candidate — awaiting Micky's verification.)*
- **Internal structure and internal data flow:** most baro-activated neurons here are **GABAergic**,
  identified by glutamic-acid-decarboxylase-67 messenger ribonucleic acid (RNA); cholinergic
  cardiovagal motor neurons
  are also present in the region. **Internal edges — owed.**
  *(Class 1 — Schreihofer & Guyenet, J Neurophysiol 89:1265, 2003, rat, whole-cell recording with
  in-situ hybridisation. **Species: rat.** Candidate.)*
- **Neurons:** unknown — no human count found. **Synapses / Axons / Grey-matter volume /
  White-matter volume / Myelination:** unknown.
- **Pass:** 2026-07-19 — new entry — baroreflex inhibitory relay and second lamina-I target; territory boundary recorded as contested

## Nucleus of the solitary tract — the visceral and gustatory entry point (dorsal medulla)

- **Function:** the first central relay for **everything the body reports about itself** —
  cardiovascular, respiratory, gastrointestinal, gustatory and orotactile afferents arriving on the
  facial, glossopharyngeal and vagus nerves. It runs from the pyramidal decussation rostrally to the
  caudal dorsal cochlear nucleus, spanning the midline caudally as the **commissural subnucleus**
  and splitting into left and right halves rostral to the area postrema. Functionally it divides in
  two: a **rostral (gustatory)** part, the first relay of the central taste pathway, and a **caudal
  (visceral)** part receiving vagal afferents from the viscera.
  *(Class 1 — Norgren, in* The Rat Nervous System*, 1995; Holt, J Neuroendocrinology 34:e13132,
  2022, review. Candidates — awaiting Micky's verification.)*
- **A classical claim that recent work qualifies.** The nucleus has long been described as
  **viscerotopic** — each organ system terminating in its own subnucleus. Organ-specific viral
  tracing finds vagal afferents from the gastrointestinal, cardiovascular and respiratory systems
  **distributed broadly across multiple subnuclei rather than confined to organ-exclusive
  subregions**. The gradient is real; exclusive organ compartments are not.
  *(Class 1 — Bassi et al. 2022, organ-specific viral tracing, rodent. Candidate.)*
- **Inputs:**
  - **← taste afferents on the facial, glossopharyngeal and vagus nerves** — **carries:** taste
    quality and intensity, **topographically ordered by oral location**: anterior oral cavity most
    rostrally, posterior oral cavity more caudally, pharynx and larynx more caudally still.
    **Fan-in:** unknown. The receptors lie outside this file's central-nervous-system scope.
  - **← vagal and glossopharyngeal visceral afferents** — **carries:** arterial pressure from
    baroreceptors, blood chemistry from chemoreceptors, lung inflation, and gastrointestinal
    distension; glutamatergic onto second-order cells. **Fan-in:** unknown.
  - **← the bloodstream, directly** — **carries:** glucose, leptin and angiotensin II concentrations.
    **This is a chemical input, not a neural edge** — the second such case in the file after the
    retina's photon flux, and it is recorded because a consumer that assumes every input is an axon
    would miss it. **Fan-in:** n/a.
  - **← Insula, Hypothalamus and Amygdala** (descending) — **payload unknown — owed.**
    **Fan-in:** unknown.
- **Outputs:**
  - **→ Lateral parabrachial nucleus** — **carries:** the visceral and gustatory payload, for relay
    to limbic forebrain. **Fan-out:** unknown.
  - **→ Caudal ventrolateral medulla** — **carries:** arterial pressure, as the excitatory
    (glutamatergic) drive that makes the baroreflex's inhibitory limb work. **Fan-out:** unknown.
  - **→ Gustatory pathway**, via the parvicellular ventral posteromedial thalamus to insular taste
    cortex — **carries:** taste quality and intensity; typed in the gustatory entry.
    **Fan-out:** unknown.
  - **→ Branchiomotor / visceromotor nuclei**, to the dorsal motor nucleus of the vagus —
    **carries:** the afferent limb of vagal reflexes. **Payload otherwise unknown — owed.**
    **Fan-out:** unknown.
  - **→ Hypothalamus** — **payload unknown — owed.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** named subnuclei include the **interstitial**
  (longest and most rostral, gustatory in monkey and human), **central**, **dorsomedial**,
  **medial**, **parvicellular**, **ventrolateral** and **commissural** subnuclei.
  - **Internal edge — caudal (visceral) subnuclei → rostral (gustatory) subnuclei: carries:**
    visceral state onto the taste relay — **this is where taste and viscera first interact**, and the
    projection carries all three phenotypes, glutamatergic, GABAergic and catecholaminergic, so it is
    not a single sign. **Payload otherwise unknown — owed.** **Fan-in / fan-out:** unknown.
    *(Class 1 — mouse, cre-dependent viral tracing from caudal to rostral solitary nucleus, 2018.
    **Species: mouse.** Candidate.)*
- **Neurons:** unknown — no human count found. **Synapses / Axons / Grey-matter volume /
  White-matter volume / Myelination:** unknown. In rat the nucleus extends more than **4 mm**
  rostrocaudally. *(Rat figure; not human.)*
- **Pass:** 2026-07-19 — new entry — rostral gustatory / caudal visceral, viscerotopy qualified, blood-borne chemical input recorded as a non-axonal input

## Rostral ventrolateral medulla — the sympathetic vasomotor drive (medulla)

- **Function:** the source of the **tonic excitatory drive to the sympathetic nervous system**, and
  therefore of resting arterial pressure. Defined over forty years ago as the territory of the **C1
  adrenergic** cell group. Its **presympathetic bulbospinal** neurons are glutamatergic — some of
  them also adrenergic — are **barosensitive**, and project directly onto the sympathetic
  preganglionic neurons of the spinal intermediolateral cell column that control the heart, kidney,
  resistance vessels and adrenal medulla. **Not all presympathetic neurons here are C1 cells, and
  presympathetic neurons are also found elsewhere** — spinal cord, raphe, ventromedial medulla, pons
  and hypothalamus — so this is the principal source, not the only one.
  *(Class 1 — Guyenet et al., Hypertension 72:559, 2018, review; Guyenet, Am J Physiol
  305:R187, 2013. Candidates — awaiting Micky's verification.)*
- **Its cells beat on their own.** In tissue slices these neurons show **intrinsic pacemaker
  activity**, upregulated by slow transmitters such as angiotensin II. So the sympathetic tone this
  region supplies is **generated**, not merely relayed — the inhibition arriving from the caudal
  ventrolateral medulla acts on a drive that exists without input. *(Class 1 — rat brainstem slice
  recording. Candidate.)*
- **Inputs:**
  - **← Caudal ventrolateral medulla** — **carries:** **GABAergic inhibition**, tonic; the
    baroreflex's sign inversion. **Fan-in:** unknown.
  - **← Nucleus of the solitary tract** (direct, alongside the indirect route above) — **payload
    unknown — owed.** **Fan-in:** unknown.
  - **← Hypothalamus** and **← Periaqueductal gray** — **payload unknown — owed.**
    **Fan-in:** unknown.
- **Outputs:**
  - **→ Spinal cord grey matter**, onto the **intermediolateral cell column** — **carries:** the
    excitatory presympathetic drive that sets vasomotor tone and cardiac sympathetic output.
    **Fan-out:** unknown.
  - **→ Hypothalamus**, to the paraventricular nucleus, from the non-bulbospinal C1 group —
    **carries:** a signal regulating vasopressin and adrenocorticotropic hormone release and sodium
    intake. **Payload otherwise unknown — owed.** **Fan-out:** unknown.
  - **→ Locus coeruleus, Raphe nuclei** and the dorsal vagal complex — **payload unknown — owed.**
    **Fan-out:** unknown. **The bulbospinal neurons have brainstem collaterals**, so these are not
    necessarily separate populations.
- **Internal structure and internal data flow:** three functionally distinct C1 groups are
  described — a **bulbospinal presympathetic** group, a **hypothalamus-projecting** group, and a
  group **regulating parasympathetic efferents**. **Internal edges — owed.**
- **Contested — where the baroreflex's inhibitory neurons actually sit.** The account in the
  *Caudal ventrolateral medulla* entry places the GABAergic baroreflex neurons there. A more recent
  parcellation from the same laboratory lineage divides the lower ventrolateral medulla into three
  segments and places **the bulk of those GABAergic neurons, and the cardiovagal motor neurons, in
  an intermediate ventrolateral medulla** between the rostral and caudal territories — reserving
  "caudal ventrolateral medulla" for the region of **A1 noradrenergic** cells. **Recorded as
  contested at both entries; the file does not pick a side.** The data flow — solitary nucleus →
  GABAergic cells → presympathetic cells here — is not in dispute; where the middle term is drawn on
  a map is. *(Class 1 — Autonomic Neuroscience 236:102893, 2021. Candidate.)*
- **Neurons:** unknown — no human count found. **Synapses / Axons / Grey-matter volume /
  White-matter volume / Myelination:** unknown.
- **Pass:** 2026-07-19 — new entry — presympathetic drive is intrinsically generated, not relayed

## Periaqueductal gray (PAG) — midbrain defence / analgesia column

- **Function:** the midbrain grey surrounding the cerebral aqueduct — the integrating hub for
  **defensive behaviour, autonomic reaction, innate vocalisation, and descending pain modulation**.
  It is organised as **four longitudinal columns** with distinct jobs (Bandler & Shipley 1994;
  Behbehani 1995; Bandler & Keay 1996): the **dorsolateral / lateral** columns drive **active
  defence** (fight-or-flight, sympathetic / hypertensive response, non-opioid analgesia), the
  **ventrolateral** column drives **passive coping** (freezing / quiescence, hypotensive response,
  opioid analgesia). The descending-analgesia circuit runs **ventrolateral column → rostral
  ventromedial medulla → spinal dorsal horn** (laminae I / II), gating incoming nociception at the
  first synapse (Reynolds 1969, stimulation-produced analgesia; Fields & Basbaum).
- **Inputs:**
  - **← the amygdala central nucleus** — **carries:** a **valence and urgency signal** — *this is
    bad, act now* — here driving the defensive response; **no identity information**. **Fan-in:**
    unknown. **The producer declares it and names this structure** (file 8), and recorded **"Owed at
    file 14: type it."** **Typed now**, discharging that owed edit. **Two-ended.**
  - **← the hypothalamus** — **carries:** payload **owed**; defensive and autonomic drive. **Fan-in:**
    unknown. **The producer is in this file** (the hypothalamus entry below, whose Outputs reach the
    autonomic preganglionic centres via this structure). **Owed: confirm the hypothalamus entry
    declares this specific edge with a payload.**
  - **← ventromedial and orbital prefrontal cortex** — **carries:** payload **owed**; top-down
    control of defence and analgesia. **Fan-in:** unknown. **The producer declares it** (file 11),
    whose orbitofrontal / ventromedial entry names this structure among the autonomic centres.
    **Two-ended.**
  - **← the spinal cord, lamina I**, via the spinomesencephalic tract — **carries:** payload
    **owed**; ascending nociceptive input. **Fan-in:** unknown. **The producer declares it** (file
    16), which records that about **120** lamina-I cells per side (rat L4) project here and **over
    90% are collaterals** of the cells also projecting to the caudal ventrolateral medulla and
    lateral parabrachial area — a branching axon, not an independent population. **Two-ended.**
    *(Class 1 — Spike et al. 2003, rat. Candidate.)*
- **Outputs:**
  - **→ the rostral ventromedial medulla**, from the **ventrolateral column** — **carries:** the
    **descending analgesic command** — the drive that, relayed through the medulla, gates
    nociception at the spinal first synapse; no stimulus content. **Fan-out:** unknown. **The rostral
    ventromedial medulla has no entry in any file read** — the spinal cord entry (file 16) names it
    as a producer of the descending analgesic gate, and this entry names it as the relay, but it owns
    no slot. **Owed: give it an entry (candidate §9a), and decide which file owns it** — it is medulla
    and would sit here in file 14.
  - **→ the spinal dorsal horn**, laminae I / II (directly and via the medullary relay above) —
    **carries:** the **analgesic gate** — a gain applied to incoming nociception at the first
    synapse, no content. **Fan-out:** unknown. **The consumer declares it** (file 16), naming
    "periaqueductal gray and the rostral ventromedial medulla (descending modulatory)" onto the
    dorsal horn. **Two-ended.**
  - **→ the locus coeruleus**, from the **ventrolateral column** — **carries:** payload **owed**; a
    noradrenergic limb of descending analgesia. **Fan-out:** unknown. **The consumer declares it**
    (file 13), whose locus coeruleus entry names a ventrolateral-periaqueductal-gray input.
    **Two-ended.**
  - **→ vocal and autonomic premotor targets** (in the reticular formation and lower brainstem) —
    **carries:** payload **owed**; the innate vocalisation and freezing motor pattern. **Fan-out:**
    unknown. **This endpoint names a class**; the reticular formation entry is in this file but does
    not declare this input. **Owed: resolve to named consumers, or narrow.**
  - **→ the thalamus**, ascending — **carries:** payload **owed**; the affective / "pain" projection.
    **Fan-out:** unknown. **This endpoint names a class**; no thalamic entry in file 12 was confirmed
    to declare this input this pass. **Owed as a cross-file check at file 12.**
- **Internal structure and internal data flow:** described but not typed — **owed.** The entry's own
  Function names **four longitudinal columns** as sub-elements with distinct payloads —
  **dorsolateral** and **lateral** (active defence, sympathetic, non-opioid analgesia) and
  **ventrolateral** (passive coping, opioid analgesia, the descending-analgesia origin) — plus a
  **dorsomedial** column. They are load-bearing: the analgesia outputs above leave specifically from
  the ventrolateral column, which the edges now record. **No internal edge between columns is
  described**, and it is not established that one exists (they may be parallel effectors selected by
  input). **Owed: name all four columns formally, assign each output edge to its column, and state
  whether internal edges exist.**
- **Neurons:** soft / unknown — no clean human count; a thin sleeve of grey around the aqueduct,
  defined by function and column, not by a countable border.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.
- **Pass:** 2026-07-24 — prose Inputs and Outputs converted to typed edges; the amygdala-central and prefrontal inputs and the spinal and locus-coeruleus edges confirmed two-ended (files 8, 11, 13, 16); the rostral ventromedial medulla flagged as a named region with no entry; the four defence columns recorded as sub-elements with the analgesia outputs assigned to the ventrolateral one; missing Internal structure slot added

## Hypothalamus — the homeostatic / neuroendocrine hub (diencephalon)

- **Function:** the master regulator of **homeostasis and the basic drives** — temperature, feeding,
  thirst, sleep / wake, circadian timing, stress, sex / reproduction, and defensive behaviour —
  acting through **two great output arms**. **(1) Neuroendocrine:** *magnocellular* neurons of the
  supraoptic and paraventricular nuclei send oxytocin and vasopressin down their axons to the
  **posterior pituitary** (direct release into blood); *parvocellular* neurons (paraventricular and
  arcuate) release releasing / inhibiting hormones into the **hypophyseal portal** blood to command
  the **anterior pituitary** — including the paraventricular **corticotropin-releasing hormone →
  adrenocorticotropic hormone → cortisol** stress axis (the hypothalamic–pituitary–adrenal, or
  HPA, axis). **(2) Autonomic /
  behavioural:** descending control of the autonomic preganglionic neurons (via the periaqueductal
  gray, brainstem, and spinal cord) and of motivated behaviour. It works as a set of small nuclei:
  the **suprachiasmatic nucleus** is the circadian master clock (entrained by a direct retinal
  input, the retinohypothalamic tract); the **arcuate** senses metabolic state and runs the feeding
  balance (orexigenic agouti-related-peptide / neuropeptide-Y vs anorexigenic
  pro-opiomelanocortin neurons, reading blood leptin and ghrelin at the leaky median eminence); the
  **lateral hypothalamus** holds the **orexin / hypocretin** neurons for wakefulness and feeding
  (their loss is narcolepsy); the **ventromedial** nucleus signals satiety and defensive rage; the
  **medial preoptic** area governs thermoregulation and sexual behaviour, and the neighbouring
  **ventrolateral preoptic** nucleus is the sleep switch; the **posterior hypothalamus / mammillary
  bodies** are the memory relay of the Papez circuit.
- **Inputs:**
  - **← the amygdala central nucleus**, via the **stria terminalis** and the **ventral
    amygdalofugal pathway** — **carries:** a **valence and urgency signal** — *this is bad (or good),
    act now* — driving autonomic, endocrine and freezing responses; **no identity information**.
    **Fan-in:** unknown. **The producer declares it and names this structure** (file 8), and recorded
    **"Owed at file 14: type it."** **Typed now**, discharging that owed edit. **Two-ended.**
  - **← the hippocampal formation**, via the **fornix** — **carries:** payload **owed**. **Fan-in:**
    unknown. **The producer declares it** (file 8), whose hippocampal Outputs name "→ the
    hypothalamus, via the fornix" with payload owed. **Two-ended.**
  - **← the septum** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint names a
    class**; the medial and lateral septum are in the basal-forebrain material but the lateral septum
    has no entry in any file read. **Owed: resolve to a named producer, or record the lateral septum
    as a §9a candidate** (it is already so recorded from file 14's rostromedial-tegmental-nucleus
    entry).
  - **← the nucleus of the solitary tract** (brainstem visceral afferents) — **carries:** payload
    **owed**; visceral and cardiovascular state. **Fan-in:** unknown. **The producer is in this
    file**, whose solitary-nucleus Outputs name the hypothalamus among its ascending targets.
    **Two-ended** within-file.
  - **← the retina**, to the **suprachiasmatic nucleus**, via the **retinohypothalamic tract** —
    **carries:** an **irradiance / "lights-on" signal** — ambient luminance for clock entrainment,
    from melanopsin-expressing retinal ganglion cells; not spatial vision. **Fan-in:** unknown.
    **The producer declares it** (file 1), whose retina Outputs name "→ suprachiasmatic nucleus
    (retinohypothalamic tract, melanopsin ganglion cells)." **Two-ended.**
  - **← blood-borne signals** — leptin, ghrelin, glucose, osmolality, temperature — **sensed
    directly** at the circumventricular organs (median eminence, organum vasculosum of the lamina
    terminalis, subfornical organ) where the blood-brain barrier is open — **carries:** metabolic and
    osmotic state, as chemical concentration rather than a neural code. **This is a non-axonal input**,
    the same kind the solitary-nucleus entry records for its blood-borne chemical sensing: there is no
    producer region and no fan-in, because the "edge" is diffusion from blood. **Recorded as an input
    with no source region by design, not as an owed edge.**
- **Outputs:**
  - **→ the posterior pituitary**, from the **magnocellular supraoptic and paraventricular neurons**
    — **carries:** **oxytocin and vasopressin**, released directly into blood — a hormonal output, not
    a neural code. **Fan-out:** unknown. **The posterior pituitary has no entry**; it is an endocrine
    release site, not a processing region. **Recorded as an endocrine terminal, not an owed edge** —
    the same treatment the pineal's melatonin output gets.
  - **→ the anterior pituitary**, from **parvocellular** neurons, via the **hypophyseal portal
    blood** — **carries:** releasing and inhibiting hormones (including corticotropin-releasing
    hormone driving the hypothalamic–pituitary–adrenal axis) — a hormonal output into a private
    portal circulation. **Fan-out:**
    unknown. **Recorded as an endocrine terminal, not an owed edge.**
  - **→ the periaqueductal gray, brainstem and spinal cord** (autonomic preganglionic control) —
    **carries:** payload **owed**; descending autonomic and defensive drive. **Fan-out:** unknown.
    **The periaqueductal gray is in this file** and declares a hypothalamic input above; the spinal
    cord consumer (file 16) declares "raphe nuclei and hypothalamus (modulatory, onto the dorsal horn
    and the intermediolateral cell column)." **Two-ended** for those two; the "brainstem" remainder
    **names a class — owed.**
  - **→ the mammillary bodies → the anterior thalamic nuclei**, via the **mammillothalamic tract** —
    **carries:** payload **owed**; the Papez memory relay. **Fan-out:** unknown. **The consumer
    declares it** (file 12), whose anterior-nuclei entry names "← the mammillary bodies, via the
    mammillothalamic tract" and recorded the payload owed and a cross-file check owed at this file.
    **Two-ended now.** *(The mammillary bodies are a sub-element of this entry, named in Function;
    the tract itself has an entry in file 18.)*
  - **→ the brainstem tegmentum** — **carries:** payload **owed. Fan-out:** unknown. **This endpoint
    names a class.** **Owed: resolve to named consumers** — the reticular formation and the
    neuromodulatory nuclei (file 13) are candidates; file 13's locus coeruleus, raphe and ventral
    tegmental entries each name a hypothalamic input, so some far ends exist and are owed there.
  - **→ the pineal gland**, functionally, via the **paraventricular nucleus → intermediolateral cell
    column → superior cervical ganglion** chain — **carries:** the circadian "it is night"
    disinhibition that drives melatonin. **Fan-out:** unknown. **The consumer is in this file** (the
    pineal entry below) and declares the full chain as its input. **Two-ended within-file.** *(This is
    a multi-synaptic functional route, not a direct axon; the payload rides the chain, and the pineal
    entry holds the mechanism.)*
  - **→ widespread limbic and cortical targets shaping motivated behaviour** — **carries:** payload
    **owed. Fan-out:** unknown. **This endpoint names a class** and does not resolve. **Owed: name
    the consumers, or narrow.**
- **Internal structure and internal data flow:** described but not typed — **owed, and it is the
  heaviest internal-structure debt in the file.** The entry's Function names **at least eleven
  sub-nuclei**, each with a distinct payload and distinct edges — **suprachiasmatic** (clock),
  **arcuate** (feeding sensor), **lateral hypothalamus** (orexin), **ventromedial** (satiety /
  rage), **medial preoptic** (thermoregulation / sex), **ventrolateral preoptic** (sleep switch),
  **paraventricular** and **supraoptic** (magno- and parvocellular neuroendocrine), and the
  **mammillary bodies** (Papez relay). These are load-bearing sub-elements, not properties: the
  input and output edges above already leave from or arrive at specific ones (retina → suprachiasmatic;
  mammillothalamic tract from the mammillary bodies; magnocellular neurons → posterior pituitary).
  **Internal edges among them are described in the literature** — suprachiasmatic → paraventricular
  → the pineal chain, arcuate → paraventricular feeding control, preoptic → the defensive and
  thermoregulatory effectors — **and none is written here.** **Owed: name the sub-nuclei formally,
  assign every inter-region edge above to its nucleus, and type the internal edges.** This is the
  single largest owed conversion remaining in the file after this pass, and it is recorded rather
  than attempted here because each sub-nucleus is effectively its own region.
- **Neurons:** the **suprachiasmatic nucleus ~50,000 per side** (human; Hofman & Swaab lineage —
  cf. ~20,000 in mouse) — one of the smallest nuclei with a defined, mapped function, and a rare
  firm human figure here. Other hypothalamic nuclei are soft / uncounted in human. *(This count is
  for one sub-element, the suprachiasmatic nucleus — the per-sub-element figure the
  Internal-structure slot calls for, recorded here until that slot is typed.)*
- **Synapses:** unknown.
- **Axons:** the supraopticohypophyseal / tuberoinfundibular tracts, fornix, mammillothalamic tract
  (counts unknown).
- **Grey-matter volume:** whole hypothalamus **~4 g / ~4 cm³ (both sides)** — a secondary
  compilation figure (Afifi & Bergman lineage), soft; per-nucleus human volumes are sparse. The
  suprachiasmatic nucleus is sub-cubic-millimetre; note that its ~50k count and the small reported
  volume do **not** cleanly reconcile into a plausible density (they imply an implausibly high
  packing), so no density cross-check is asserted — the count is the honest anchor, the volume soft.
- **White-matter volume:** unknown.
- **Myelination:** unknown.
- **Pass:** 2026-07-24 — prose Inputs and Outputs converted to typed edges; the amygdala-central, hippocampal, solitary-nucleus, retinal (suprachiasmatic) and mammillothalamic edges confirmed two-ended (files 1, 8, 12, 16); blood-borne sensing and the two pituitary arms recorded as non-axonal / endocrine terminals rather than owed edges; three class endpoints (septum, brainstem tegmentum, limbic/cortical) recorded owed; the eleven sub-nuclei recorded as the file's heaviest owed internal-structure conversion; missing Internal structure slot added

## Pineal gland — the circadian endocrine output / melatonin (epithalamus)

- **Function:** the **neuroendocrine output arm of the circadian system** — a small midline
  **epithalamic** gland (dorsal diencephalon, just behind the third ventricle near the habenula)
  that converts the suprachiasmatic clock's neural signal into a **hormonal** one, secreting
  **melatonin** into blood and cerebrospinal fluid (CSF) at night. It is a **neuroendocrine
  transducer**: darkness raises
  melatonin, light suppresses it. Melatonin is the body's principal **"it is night" signal /
  chronobiotic**, entraining peripheral clocks and timing sleep (and additionally an antioxidant /
  free-radical scavenger). Its **pinealocytes (~95% of cells) are secretory endocrine cells, not
  neurons** (derived from neuroepithelium) — so the gland *transduces*, it does not compute; this
  closes the suprachiasmatic → pineal output arm the Hypothalamus entry's circadian clock left open.
- **Inputs:**
  - **← the superior cervical ganglion** (sympathetic / conarian fibres onto pinealocytes),
    terminating the **multisynaptic circadian efferent chain** retina (melanopsin ganglion cells) →
    retinohypothalamic tract → **suprachiasmatic nucleus** → **paraventricular nucleus** →
    **intermediolateral cell column** of the upper-thoracic spinal cord → superior cervical ganglion
    → here — **carries:** **norepinephrine**, gated by the clock — darkness *disinhibits* the
    paraventricular nucleus, so the ganglion releases norepinephrine, which via β-adrenergic
    cyclic adenosine monophosphate (cAMP) – protein-kinase-A drives arylalkylamine
    N-acetyltransferase (the rate-limiting melatonin
    enzyme); light re-imposes suprachiasmatic inhibition and shuts synthesis off. The payload is a
    **"darkness / night" permission signal**, not content. **Fan-in:** unknown. **The superior
    cervical ganglion is peripheral autonomic ganglion and has no entry**; the chain's upstream
    stations are in this file (suprachiasmatic, paraventricular) and file 16 (intermediolateral cell
    column). **The loop file (20) declares this exact chain.** **Two-ended against the loop
    statement**; the final ganglionic limb is peripheral and recorded as such. *(Class 1 / Class 3 —
    Moore; Kalsbeek & Buijs. Candidate.)*
- **Outputs:**
  - **→ the general circulation and cerebrospinal fluid** — **carries:** **melatonin**, an
    **endocrine, not synaptic,
    output** — the "it is night" hormone reaching targets brain-wide and peripherally. **Fan-out:**
    unknown. **Recorded as an endocrine terminal, not an owed edge** — there is no target region and
    no fan-out because the output is a hormone into blood, the same treatment the hypothalamic
    pituitary arms get.
  - **→ the suprachiasmatic nucleus** (melatonin feedback, via the melatonin receptors MT1 and
    MT2) — **carries:**
    melatonin as a **phase-feedback signal** closing the circadian loop. **Fan-out:** unknown. **The
    consumer is in this file** (the hypothalamus entry's suprachiasmatic clock) and the loop file
    (20) names this return limb explicitly. **Two-ended.** *(This limb is a hormonal action on a
    receptor-bearing target, so it is a real edge with a consumer, unlike the diffuse circulation
    output above.)*
- **Internal structure and internal data flow:** **not applicable** for a neural microcircuit — the
  gland is ~95% **pinealocytes**, secretory endocrine cells rather than neurons, with no
  intra-glandular projection circuit; the one transduction step (norepinephrine → cyclic adenosine
  monophosphate → enzyme →
  melatonin) is intracellular biochemistry within pinealocytes, not an inter-cellular edge. **The
  gland transduces rather than computes**, so it has no internal data flow of the kind this slot
  records. *(This is a positive "not applicable," a statement about the tissue, not an unfilled gap.)*
- **Neurons:** **none** — pinealocytes are secretory endocrine cells, not neurons; the gland is
  *innervated by* sympathetic fibres but contains no projection neurons (like the tract entries, a
  "none" slot rather than a soft one).
- **Synapses:** the sympathetic terminals onto pinealocytes (counts unknown).
- **Axons:** the conarian (sympathetic) nerves in; no neural output axons.
- **Grey-matter volume:** **total pineal ~90–210 mm³** across human magnetic-resonance-imaging
  (MRI) and computed-tomography cohorts (MRI-stereology mean ~100 ± 40–51 mm³, Acer et al. 2012;
  older-men cohort mean ~207 mm³,
  parenchyma ~178 mm³, AGES-Reykjavik) — a soft-tissue **parenchyma** fraction plus an
  **age-increasing calcified** fraction (corpora arenacea, "brain sand"); gland weight
  ~100–150 mg. A rare verified physical number for a structure this small.
- **White-matter volume:** not applicable.
- **Myelination:** not applicable — an endocrine gland, not neural tissue.
- **Pass:** 2026-07-24 — prose Inputs and Outputs converted to typed edges; the sympathetic efferent chain typed as one input carrying a clock-gated norepinephrine "darkness" signal, two-ended against the loop file; melatonin split into a diffuse endocrine terminal (no consumer) and a suprachiasmatic feedback edge (a real consumer); Internal structure recorded as not applicable with the transduce-not-compute reason; missing Internal structure slot added

## Reticular formation — arousal core + autonomic / premotor pattern generators (brainstem tegmentum)

- **Function:** the diffuse, phylogenetically old **core of the brainstem tegmentum** — not one
  nucleus but a mesh of ill-bordered cell groups running from medulla to midbrain, with two great
  roles. **Ascending — the arousal engine:** the **ascending reticular activating system** (ARAS;
  Moruzzi
  & Magoun 1949) sets **arousal, wakefulness, and consciousness**, driving the **intralaminar
  thalamus** and, diffusely, the cortex; its transmitter arms are the cholinergic **pedunculopontine
  and laterodorsal tegmental** nuclei plus the already-described monoaminergic systems
  (locus-coeruleus noradrenaline, raphe serotonin, ventral-tegmental dopamine) and the histaminergic
  tuberomammillary nucleus. **Descending — pattern generators and premotor control:**
  **reticulospinal** control of postural tone and locomotion; the **central pattern generators** for
  breathing (the pre-Bötzinger complex) and cardiovascular tone (the rostral ventrolateral medulla,
  vasomotor); and the **premotor coordinators** that sequence the cranial-nerve motor nuclei — the
  saccade **burst generators** (paramedian pontine reticular formation and rostral interstitial
  nucleus of the medial longitudinal fasciculus, the common final path that the frontal eye fields,
  superior colliculus, and vestibulo-ocular reflex all drive) and the chewing, swallowing, and
  facial / laryngeal patterns.
- **Inputs:**
  - **← collaterals of the ascending sensory systems** — **carries:** payload **owed**; the
    non-specific sensory drive that maintains arousal (a stimulus in any modality raises the
    ascending reticular activating system).
    **Fan-in:** unknown. **This endpoint names a class**, and — like the reticular nucleus's
    "all thalamocortical collaterals" — the class may be close to the real claim, but it is not
    exempt. **Owed: resolve to named producers as the sensory files are worked.**
  - **← the cerebellum, from the fastigial nucleus** — **carries:** payload **owed**; the cerebellar
    limb onto the reticular formation. **Fan-in:** unknown. **The producer declares it** (file 10),
    whose deep-nuclei Outputs name "→ the reticular formation (fastigial, via the inferior [cerebellar
    peduncle])." **Two-ended.**
  - **← the periaqueductal gray** — **carries:** payload **owed**; the vocal and freezing motor
    patterns the periaqueductal gray drives through premotor targets here. **Fan-in:** unknown. **The
    producer is in this file** and names this structure among its premotor targets. **Two-ended
    within-file.**
  - **← the hypothalamus** — **carries:** payload **owed**; descending autonomic and arousal drive.
    **Fan-in:** unknown. **The producer is in this file**, whose Outputs name "→ the brainstem
    tegmentum" as a class covering this structure. **Owed at the hypothalamus entry: name this
    structure out of that class.**
  - **← the cerebral cortex** — **carries:** payload **owed**; top-down control of arousal and of the
    premotor pattern generators (the frontal eye fields onto the saccade burst generators is the
    sharpest case). **Fan-in:** unknown. **This endpoint names a class**; the frontal eye field
    (file 11) is a candidate named producer for the saccade limb. **Owed: resolve to named
    producers.**
- **Outputs:**
  - **→ the intralaminar thalamus** (ascending arousal) — **carries:** payload **owed**; the
    ascending-reticular-activating-system arousal drive. **Fan-out:** unknown. **The consumer declares it** (file 12), whose intralaminar
    entry names "← the reticular formation (brainstem)" carrying the arousal drive, and recorded a
    cross-file check owed at this file. **Two-ended now.**
  - **→ the cerebral cortex** (diffuse ascending arousal) — **carries:** the arousal / gain signal;
    no content. **Fan-out:** unknown. **This endpoint names a class** covering every cortical entry —
    but note that much of the diffuse cortical arousal is delivered by the monoaminergic and
    cholinergic nuclei (file 13) rather than by reticular cells directly. **Owed: resolve, and
    distinguish the direct reticulo-cortical limb from the neuromodulator-relayed one.**
  - **→ the spinal cord** (reticulospinal, postural and autonomic) — **carries:** payload **owed**;
    postural tone, locomotion drive, and autonomic control. **Fan-out:** unknown. **The far end is in
    file 16**; the reticulospinal tract is named there among the descending motor systems but was not
    confirmed to type this edge with a payload. **Owed as a cross-file check at file 16.**
  - **→ the cranial-nerve motor nuclei** — **carries:** payload **owed**; the premotor sequencing
    signal (saccade bursts, chewing, swallowing, facial / laryngeal patterns). **Fan-out:** unknown.
    **This endpoint names a class**; the individual cranial-nerve motor nuclei are described in file
    15. **Owed: resolve to named consumers in file 15.**
- **Internal structure and internal data flow:** described but not typed — **owed**, with a caveat
  that makes it different from the other entries. The Function slot names many sub-elements — the
  **pedunculopontine** and **laterodorsal tegmental** cholinergic nuclei, the **pre-Bötzinger
  complex**, the **paramedian pontine reticular formation** and **rostral interstitial nucleus of
  the medial longitudinal fasciculus** (saccade burst generators), and the **parabrachial nucleus**
  (named in Outputs as included here) — several of which have distinct payloads and their own edges.
  But the entry's own Function calls this **"not one nucleus but a mesh of ill-bordered cell
  groups,"** so the sub-element boundaries are genuinely indistinct rather than merely unwritten.
  **Owed: name the discrete sub-nuclei that do have borders (the burst generators, the pre-Bötzinger
  complex, the cholinergic nuclei) and type their edges; mark the diffuse remainder as a network
  without countable sub-elements** — the honest state, not a deferral. The saccade burst generators
  in particular are load-bearing, because the superior colliculus entry already declares outputs
  onto them by name.
- **Neurons:** soft / unknown — a distributed, ill-bordered network defined by connectivity and
  transmitter, not a countable nucleus.
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.
- **Pass:** 2026-07-24 — prose Inputs and Outputs converted to typed edges; the fastigial, periaqueductal and intralaminar edges confirmed two-ended (files 10, 12); four class endpoints (ascending sensory, cortex in and out, cranial-nerve nuclei) recorded owed; the discrete sub-nuclei (burst generators, pre-Bötzinger, cholinergic tegmental) named as sub-elements with the diffuse remainder marked a borderless network; missing Internal structure slot added

## Rostromedial tegmental nucleus (RMTg, tail of the ventral tegmental area) — the aversive brake on dopamine (mesopontine tegmentum)

- **Function:** the **GABAergic inverting relay** that converts the lateral habenula's "bad-outcome"
  signal into inhibition of midbrain dopamine neurons. It is the structure that lets a *negative*
  reward-prediction error suppress dopamine: the habenula fires to worse-than-expected outcomes and
  excites this nucleus, and this nucleus inhibits the dopamine cells, so their firing dips below
  baseline. Without it there is no route from the habenula's glutamatergic (excitatory) output to a
  *decrease* in dopamine — the sign inversion happens here. It encodes aversive events and
  reward-omission and inhibits motor responding to them, and is a µ-opioid-receptor-rich site
  (opioids disinhibit dopamine partly by silencing it). A recently defined nucleus (first delineated
  2009), also called the **tail of the ventral tegmental area (tVTA)**.
- **Inputs:**
  - **← the lateral habenula** — **carries:** a **negative / aversive value signal** — a
    glutamatergic excitatory drive encoding worse-than-expected outcome, the major input and the one
    that defines the nucleus. **Fan-in:** unknown. **The producer declares it** (file 17), naming the
    lateral habenula → rostromedial tegmental nucleus limb of the "bad-outcome" pathway. **Two-ended.**
  - **← the laterodorsal and pedunculopontine tegmental nuclei** — **carries:** payload **owed**; a
    cholinergic input (acting partly through α7 nicotinic receptors on the glutamatergic afferents).
    **Fan-in:** unknown. **The far end is the reticular-formation entry in this file**, which names
    the pedunculopontine / laterodorsal tegmental nuclei as its cholinergic arm but does not yet type
    an edge to this nucleus. **Owed as a cross-file edit at that entry (this file).**
  - **← the extended amygdala, the lateral septum, and the periaqueductal gray** — **carries:**
    payload **owed**; aversion-related and defensive-state inputs. **Fan-in:** unknown. **These
    endpoints name regions with entries** — the periaqueductal gray in this file, the bed nucleus of
    the stria terminalis in file 8 — **whose far ends were not confirmed to declare this edge this
    pass. Owed as cross-file checks** at those entries. *(The lateral septum has no entry in any file
    read; recorded as a §9a candidate.)*
  - **← the substantia nigra** — **carries:** payload **owed**; a lesser input. **Fan-in:** unknown.
    **The far end is in file 9** (basal ganglia); not confirmed this pass. **Owed as a cross-file
    check at file 9.**
- **Outputs:**
  - **→ the ventral tegmental area**, synapsing on its **tyrosine-hydroxylase-positive (dopamine)
    neurons** — **carries:** **inhibition** — a GABAergic brake, the sign-inverted image of the
    habenular input; no content, a negative gain on the dopamine cells' firing. **Fan-out:** unknown.
    **The consumer declares it** (file 13), naming the lateral habenula → rostromedial tegmental
    nucleus → ventral tegmental area dopamine-inhibition limb. **Two-ended.**
  - **→ the substantia nigra pars compacta**, on its dopamine neurons — **carries:** the same
    GABAergic inhibition; stimulation suppresses ~90% of pars-compacta dopamine cells. **Fan-out:**
    unknown. **The consumer declares it** (file 9), which names the lateral habenula → rostromedial
    tegmental nucleus → substantia nigra pars compacta limb carrying a negative reward-prediction
    error. **Two-ended.**
  - **→ the hypothalamus and other targets beyond the dopamine midbrain** — **carries:** payload
    **owed. Fan-out:** unknown. **This endpoint names a class** (the literature reports minor
    projections beyond the dopamine cells). **Owed: resolve to named consumers or confirm the dopamine
    midbrain is the whole story.**
- **Internal structure and internal data flow:** **unknown.** A core / periphery distinction is
  reported (the core is more strongly shock-cue-responsive), and ~72% of projection neurons are
  GABAergic, but no sub-element set with distinct targets or payloads is established in the material
  read. **Owed** for the core/periphery division; the GABAergic / non-GABAergic split is a candidate
  sub-element if the non-GABAergic cells prove to project. No internal edge is described.
- **Neurons:** soft / no clean human absolute count recorded — a small, recently defined nucleus.
  Human anatomical mapping now exists (a 2026 midbrain-mapping preprint locating the human
  rostromedial tegmental nucleus among
  the inhibitory afferents to dopamine neurons), reporting location rather than an unbiased count.
- **Synapses:** unknown — the output synapses onto dopamine dendrites are described as **symmetric**
  (the morphology of inhibition), consistent with the GABAergic payload; count unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.
- **Pass:** 2026-07-24 — new entry, created to resolve a §9a "named region with no entry" that had grown to four files' edges (9, 13, 17, 20) with no slot; inputs and outputs typed from the far ends that already declared them, two of them (→ ventral tegmental area, → substantia nigra pars compacta) confirmed two-ended; researched 2026-07-24, rodent throughout except a human location study, marked candidate

**The brainstem / midbrain / hypothalamus core is described:** the **superior colliculus** (layered
tectum — superficial visual retinotopic map, deep multisensory + saccade / orienting motor map,
gated by the substantia nigra pars reticulata, → brainstem gaze generators and pulvinar), the
**periaqueductal gray** (four defence / analgesia columns, ventrolateral periaqueductal gray →
rostral ventromedial medulla → dorsal-horn descending pain control), the **hypothalamus** (the
homeostatic and neuroendocrine hub — suprachiasmatic clock, arcuate feeding, lateral orexin,
preoptic thermoregulation / sleep, paraventricular and supraoptic neuroendocrine and
hypothalamic–pituitary–adrenal axis, mammillary Papez relay), and the **reticular formation** (the
ascending-reticular-activating-system arousal core plus the respiratory / cardiovascular pattern
generators and the cranial-nerve premotor coordinators), and the **pineal gland** (the circadian
endocrine output — suprachiasmatic nucleus → paraventricular nucleus → intermediolateral cell
column → superior cervical ganglion → melatonin, with melatonin feeding back to the suprachiasmatic
nucleus), and the **rostromedial tegmental nucleus** (the GABAergic tail of the ventral tegmental
area — lateral habenula → rostromedial tegmental nucleus → dopamine-neuron inhibition, the
sign-inverting brake that lets a negative reward-prediction error suppress dopamine). This **closes
the dangling hooks** from the retina (→ superior colliculus), inferior colliculus (→ superior
colliculus), the lateral intraparietal area and frontal eye fields (→ superior colliculus, the gaze
loop), the substantia nigra pars reticulata (→ superior colliculus, gating), the amygdala central
nucleus (→ periaqueductal gray and → parabrachial), the anterior thalamus (← mammillary bodies),
the intralaminar thalamus (← the ascending reticular activating system), and the suprachiasmatic
clock (→ pineal output), and the lateral habenula (→ rostromedial tegmental nucleus → ventral
tegmental area and substantia nigra pars compacta dopamine inhibition, previously a region named on
four files' edges with no entry). Counts are soft except the suprachiasmatic nucleus (~50,000 /
side) and the pineal volume (~90–210 mm³). The finer subcortical layer — the
individual cranial-nerve motor and sensory nuclei, the pretectum (pupillary light reflex), and
the gaze-integrator tegmental cell groups — is described in the following section; what remains
beyond it is the even-finer long tail, added as a pathway needs it.

---


## References

*(Section added 2026-08-12 under source design §2a. Every line below is a **candidate**
awaiting Micky's verification; none is verified. Each full reference given here was obtained by
a web search run in this pass against publisher, journal or preprint-server records — no
reference is written from recall. Keys reading **owed** were not searched in this pass.)*

**66 distinct keys, 69 mentions. 2 searched to a full reference; 1 partial; 63 owed.** This is the
largest key list in the source so far — very nearly as many keys as files 11, 12 and 13 carry
between them (68) — and the searching done here is a first bite, not a pass.

**Six keys name no work at all.** Four are a method and a species with no author, title, year or
identifier — *rat lesion study, tonic sympathoinhibition* (391), *rat brainstem slice recording*
(488), *mouse, cre-dependent viral tracing from caudal to rostral solitary nucleus, 2018* (466),
and *a 2026 midbrain-mapping preprint* (912–914). Two more are an author with no year and no
title — *Weiskrantz* (81) and *Fields & Basbaum* (533); *Moore* (742) and *Kalsbeek & Buijs* (742)
are the same case. **None of these can be found by a reader.** They are not weak citations; they
are absent ones with a citation's shape.

**Ten keys are one work written two ways.** *Helms, Ozen & Hall* with and without the journal
string (227, 243); *Spike, Puskár, Andrew & Todd, 2003* and *Spike et al. 2003* (329/375, 552);
*Sugimura* with and without the journal string (309, 329); *Schreihofer & Guyenet 2002* with and
without (374, 391); *Stein & Meredith* and *Stein & Meredith lineage* (89, 205); and the
*Van Opstal/Goossens lineage, PLoS Comput Biol 8:e1002508, 2012* / *PLoS Comput Biol 2012* pair
(161, 167). Each pair gets one entry below with the other cross-referenced. **Owed at the citing
lines: one key per work.**

**Two keys are a reporting or reviewing paper standing in for a primary one**, which §2a names as
its own case and which this file handles better than most: *Cerebral Cortex 26:450, 2016* (135) is
declared as where King & Palmer 1983 and Middlebrooks & Knudsen 1984 were read, and *PubMed
19710376* (259) as where Mohler & Wurtz 1976 was reviewed. **The file says so on the line**, which
is the right practice; the entries below record it rather than correct it.

**The single most consequential finding of this pass is at the *Katz, Yu & Krauzlis* entry**, and
it cuts in the file's favour: the 2026 preprint the superior colliculus entry treats as a lone
unreviewed result **has a peer-reviewed 2024 paper behind it from the same laboratory reporting
the same core effect.** The entry's caution is more warranted than it needs to be. See that entry.

**A second finding is at the *Spike, Puskár, Andrew & Todd, 2003* entry**, and it cuts the other
way: two percentages this file carries appear in the source literature attached to **different
quantities** than the file attaches them to. See that entry — it needs the paper opened, not
another search.

**Species composition of what has been searched: two macaque, one rat** — *Katz et al.* (rhesus,
reversible inactivation), *Zheng et al.* (macaque, double retrograde label, resolved incidentally
and recorded at its key), and *Spike et al.* (rat, retrograde tracing). **The file's own species
discipline is the best in the source** — nearly every provenance mark already names a species, and
the four unnamed-work keys above name a species even where they name nothing else. Sixty-three keys
are unsearched, so no balance can be stated yet.


- **Acer et al. 2012** — **owed**: not searched in this pass. Carries the pineal
  magnetic-resonance-stereology mean of ~100 ± 40–51 mm³, one of the file's two firm human
  figures. *(Line 770.)*
- **Afifi & Bergman lineage** — **owed**: not searched; the key carries no year and no title. The
  citing line already declares it a secondary compilation figure and marks it soft. *(Line 707.)*
- **AGES-Reykjavik** — **owed**: not searched. A cohort name rather than a paper; carries the
  older-men pineal means (~207 mm³ gland, ~178 mm³ parenchyma). *(Line 772.)*
- **Autonomic Neuroscience 236:102893, 2021** — **owed**: not searched, **and the key names no
  author.** It carries the contested three-segment parcellation of the lower ventrolateral medulla
  that both the caudal and rostral entries record as unresolved. **Cited at two entries and
  load-bearing at both.** *(Lines 405, 518.)*
- **Bandler & Keay 1996** — **owed**: not searched. One of three keys on the four-column
  periaqueductal organisation. *(Line 528.)*
- **Bandler & Shipley 1994** — **owed**: not searched. *(Line 527.)*
- **Basso & Wurtz 1998** — **owed**: not searched. Carries the burst-versus-buildup cell-class
  distinction. *(Line 215.)*
- **Bassi et al. 2022** — **owed**: not searched. Carries the viscerotopy qualification — that
  vagal afferents distribute across subnuclei rather than into organ-exclusive compartments — which
  is a correction the entry makes to a classical claim, so it is load-bearing. *(Line 432.)*
- **Behbehani 1995** — **owed**: not searched. *(Line 528.)*
- **bioRxiv preprint 2021.06.24.449726 / PubMed Central PMC9652463** — **owed**: not searched. A
  bare preprint identifier with an accession and no author or title. It carries one side of the
  recorded dispute over whether firing rate adds payload on top of the collicular place code. **Note
  that a PubMed Central accession alongside a preprint identifier usually means the work was later
  published**, in which case the published version is the reference and this key is out of date.
  *(Line 168.)*
- **Blatt, Andersen & Stoner 1990** — **owed**: not searched. *(Line 112.)*
- **Cerebral Cortex 26:450, 2016** — **owed**: not searched, **and the key names no author.** It is
  the **reporting paper** through which *King & Palmer 1983* and *Middlebrooks & Knudsen 1984* were
  read — the citing line says so, which is §2a's required practice. **Owed: name its authors**, so
  that the reader can tell the reporting paper from the primary ones it reports. *(Line 135.)*
- **Chen et al., PNAS 113, 2016** — **owed**: not searched. Carries the ventral-versus-dorsal
  lateral-intraparietal split on which the priority-map input's arity depends. *(Line 112.)*
- **Fields & Basbaum** — **owed**: not searched; **the key carries no year and no title**, and no
  work can be found from it. It supports the descending-analgesia circuit that the periaqueductal
  entry's Function slot is built on. *(Line 533.)*
- **Fries 1984** — **owed**: not searched. *(Line 106.)*
- **Guyenet, Am J Physiol 305:R187, 2013** — **owed**: not searched. *(Line 483.)*
- **Guyenet et al., Hypertension 72:559, 2018** — **owed**: not searched. A review, declared as one
  on the citing line. Carries the rostral ventrolateral medulla's definition and the qualification
  that presympathetic neurons exist elsewhere too. *(Line 483.)*
- **Hafed & Krauzlis 2012** — **owed**: not searched. Carries the rostral fixation zone. *(Line
  205.)*
- **Helms, Ozen & Hall 2004** — **the same work as the key below**, cited without the journal
  string at one line. See that entry. **Owed at the citing lines: use one key.** *(Line 243.)*
- **Helms, Ozen & Hall, J Neurophysiol 91:1706, 2004** — **owed**: not searched. It carries the
  most quantitative internal-edge claim in the superior colliculus entry — the ~500 µm column with
  effective off-axis stimulation out to 1,000 µm — and the caged-glutamate control that makes the
  superficial-to-intermediate pathway synaptic rather than shared-afferent. **Highest-value owed
  key in that entry after the two below.** **Same work as *Helms, Ozen & Hall 2004* at line 243.**
  *(Line 227.)*
- **Hikosaka & Wurtz lineage** — **owed**: not searched; **the key carries no year and no title.**
  It supports the nigral gating payload — the claim that the informative event on that edge is a
  cessation — which is one of the file's sharper payload statements. *(Line 148.)*
- **Hofman & Swaab lineage** — **owed**: not searched; the key carries no year and no title. It
  carries the suprachiasmatic ~50,000 per side, which the file's preamble names as one of its two
  firm human figures and which the Grey-matter-volume slot at line 708 already flags as not
  reconciling with the reported volume. **Owed and load-bearing.** *(Line 698.)*
- **Holt, J Neuroendocrinology 34:e13132, 2022** — **owed**: not searched. A review, declared as
  one. *(Line 425.)*
- **Hubel, LeVay & Wiesel 1975** — **owed**: not searched. Carries the eye-segregated columns and
  strata in the superficial gray. *(Line 101.)*
- **Imaging Neuroscience, doi 10.1162/imag_a_00567, 2025** — **owed**: not searched, **and the key
  names no author** — a journal, a digital object identifier and a year. It is **the only human
  in-vivo evidence in the parabrachial entry**, and the entry leans on it for the claim that the
  trigeminal → parabrachial → central amygdala circuit was delineated in humans for the first time.
  **Highest-value owed key in that entry**; the identifier makes it a one-search job. *(Line 315.)*
- **Isa & Hall 2009 review** — **owed**: not searched. Declared as a review on the citing line.
  *(Line 227.)*
- **J Neurosci 26:4763, 2006** — **owed**: not searched, **and the key names no author.** It carries
  the in-vitro evidence for horizontal connections within the intermediate gray. *(Line 250.)*
- **Kalsbeek & Buijs** — **owed**: not searched; **the key carries no year and no title.** *(Line
  742.)*
- **Katz, Yu & Krauzlis, bioRxiv 10.64898/2026.04.27.721202** — Katz, L.N., Yu, G. & Krauzlis, R.J.
  **Visual activity in primate superior colliculus requires geniculostriate input.** bioRxiv
  2026.04.27.721202; doi 10.64898/2026.04.27.721202; posted 2026-04-30. **Preprint, not peer
  reviewed**, as the citing line says. **Rhesus macaque** (*Macaca mulatta*), reversible
  inactivation of the ipsilateral lateral geniculate nucleus with collicular recording.
  *(bioRxiv server record, abstract and full text.)* **Three findings.** **First, the unusual
  digital object identifier prefix is correct and is not a transcription error** — bioRxiv is now
  operated by openRxiv and its identifiers no longer carry the Cold Spring Harbor prefix, so a
  reader checking this against an older bioRxiv identifier will think it wrong and it is not.
  **Second, and this is the one that matters: the entry's caution is more warranted than it needs
  to be.** Lines 275–276 rest the qualification on the work being an unreviewed preprint. **The same
  laboratory published the same core effect in a peer-reviewed journal in 2024** — Yu, Katz, Quaia,
  Messinger & Krauzlis, *Short-latency preference for faces in primate superior colliculus depends
  on visual cortex*, *Neuron* 112(16): 2814–2822.e4, doi 10.1016/j.neuron.2024.06.005, PubMed
  38959893 — which reports that inactivating the lateral geniculate nucleus virtually eliminates
  visual responses in the colliculus. **No line in this file cites that paper and none is added
  here**, per §2a; it is named so that the preprint's status can be weighed against a published
  result rather than treated as standing alone. **Third**, the preprint's own framing of the
  contralateral-colliculus control is that it tested a Sprague-effect interhemispheric-inhibition
  account and did not find it, which is what line 269's "not relieved by silencing the opposite
  colliculus" records — **correctly, and the reason it was done is worth carrying.** *(searched
  2026-08-12; candidate. Line 286.)*
- **Keller 2004** — **owed**: not searched. *(Line 250.)*
- **King & Palmer 1983** — **owed**: not searched. Read through the reporting paper at line 135, as
  that line declares. *(Line 134.)*
- **Klooster et al., PubMed identifier 8542320** — **owed**: not searched, though **the identifier
  makes this a one-search job.** Albino rat; the citing line already declares that no macaque
  confirmation was read. *(Line 143.)*
- **Lund et al. 1975** — **owed**: not searched. *(Line 106.)*
- **Lyon, Nassi & Callaway 2010** — **owed**: not searched. Carries the selectivity of the
  di-synaptic collicular relay to V3 and the middle temporal area. *(Line 179.)*
- **May, Prog Brain Res 151:321, 2006** — **owed**: not searched. Carries the seven-lamina scheme
  the whole superior colliculus entry is organised on. *(Line 196.)*
- **Middlebrooks & Knudsen 1984** — **owed**: not searched. Read through the reporting paper at
  line 135. *(Line 134.)*
- **Mohler & Wurtz 1976** — **owed**: not searched. Read through the reviewing paper at line 259,
  as that line declares. *(Line 258.)*
- **Mooney/Rhoades lineage, J Neurosci 8:1384, 1988** — **owed**: not searched. **It carries the
  file's sharpest arity correction** — that 43% of superficial cells with well-filled axons send a
  collateral to the deep laminae, unevenly by cell class (79% wide-field vertical, 55% narrow-field
  vertical, under 20% stellate and horizontal) — which is the basis for the entry's statement that
  "the superficial layers project to the intermediate layers" over-declares its source. **Four
  percentages rest on this key.** *(Line 236.)*
- **Moore** — **owed**: not searched; **the key carries no year and no title.** *(Line 742.)*
- **Moruzzi & Magoun 1949** — **owed**: not searched. The founding ascending-reticular-activating-
  system reference. *(Line 784.)*
- **mouse, cre-dependent viral tracing from caudal to rostral solitary nucleus, 2018** — **owed, and
  the key names no work** — a species, a method and a year. It carries the solitary nucleus's only
  typed internal edge, including the claim that the projection carries all three transmitter
  phenotypes. **Owed: name the paper.** *(Line 466.)*
- **Munoz & Wurtz 1995** — **owed**: not searched. Cited at two lines, for the fixation zone and for
  the burst/buildup classes. *(Lines 205, 214.)*
- **Norgren, in *The Rat Nervous System*, 1995** — **owed**: not searched. A book chapter, which the
  citing line indicates by naming the volume. *(Line 425.)*
- **Perry & Cowey 1984** — **owed**: not searched. Carries the "not more than 10%, about 6% near the
  fovea" retinal-ganglion-cell fractions. *(Line 101.)*
- **PLoS Comput Biol 2012** — **the same work as *Van Opstal/Goossens lineage, PLoS Comput Biol
  8:e1002508, 2012*** at line 161, cited without authors or article number at line 167. See that
  entry. **Owed at the citing lines: use one key.** *(Line 167.)*
- **Port & Wurtz 2000** — **owed**: not searched. Carries the double-step curved-saccade evidence
  against strict winner-take-all. *(Line 250.)*
- **PubMed 19710376** — **owed**: not searched, **and the key names no author** — a bare identifier.
  It is the **reviewing paper** through which *Mohler & Wurtz 1976* was read and the source of the
  three-scheme account of how the collicular layers relate. **Owed: name it**; the identifier makes
  it a one-search job. *(Line 259.)*
- **rat brainstem slice recording** — **owed, and the key names no work** — a species and a method.
  It carries the claim that the rostral ventrolateral medulla's presympathetic cells are intrinsic
  pacemakers, which is the basis for the entry's statement that sympathetic tone is generated
  rather than relayed. **A structural claim on an unnamed source. Owed: name the paper.** *(Line
  488.)*
- **rat lesion study, tonic sympathoinhibition** — **owed, and the key names no work.** It carries
  the ~40 mmHg pressure rise and ~200% splanchnic sympathetic increase — **two of the few hard
  numbers in the medullary entries** — on a citation that names no author, year or journal. **Owed:
  name the paper.** *(Line 391.)*
- **Reynolds 1969** — **owed**: not searched. The stimulation-produced-analgesia reference. *(Line
  533.)*
- **Schiller, Malpeli & Schein 1979** — **owed**: not searched. It is the **contrary** anaesthetised
  result the Katz entry is weighed against, so it is half of a recorded disagreement and should be
  searched alongside that key rather than separately. *(Line 288.)*
- **Schreihofer & Guyenet 2002 review** — **the same work as the key below**, cited without the
  journal string. See that entry. **Owed at the citing lines: use one key.** *(Line 391.)*
- **Schreihofer & Guyenet, Clin Exp Pharmacol Physiol 29:514, 2002** — **owed**: not searched. A
  review, declared as one. Carries the baroreflex-inhibitory-link account that the caudal
  ventrolateral medulla entry's Function slot rests on. **Same work as *Schreihofer & Guyenet 2002
  review* at line 391.** *(Line 374.)*
- **Schreihofer & Guyenet, J Neurophysiol 89:1265, 2003** — **owed**: not searched. Primary, rat,
  whole-cell recording with in-situ hybridisation; carries the glutamic-acid-decarboxylase-67
  identification of the baro-activated cells. *(Line 410.)*
- **Spike et al. 2003** — **the same work as the key below**, cited in short form at the
  periaqueductal entry. See that entry. **Owed at the citing lines: use one key.** *(Line 552.)*
- **Spike, Puskár, Andrew & Todd, 2003** — Spike, R.C., Puskár, Z., Andrew, D. & Todd, A.J. (2003).
  A quantitative and morphological study of projection neurons in lamina I of the rat lumbar spinal
  cord. *European Journal of Neuroscience* 18(9): 2433–2448; doi 10.1046/j.1460-9568.2003.02981.x;
  PubMed 14622144. **Rat**, L4 lumbar segment, retrograde tracing with paired tracers into two
  separate sites. *(Wiley publisher record and PubMed.)* **The paper's three supraspinal targets are
  exactly the three entries in this file that cite it** — caudal ventrolateral medulla, lateral
  parabrachial area and periaqueductal grey — which is a good sign that the key is being used
  correctly at the level of *which* edges it supports. **But two percentages may be attached to the
  wrong quantities, and this needs the paper opened rather than another search.** Lines 320–323
  state that one quantitative study finds ~85% of rat lumbar lamina I projection cells labelled
  **from the parabrachial nucleus or the caudal ventrolateral medulla**, and that a review states
  ~95% of ascending lamina I neurons target the parabrachial nucleus. **The later literature citing
  this paper states both figures differently:** that a parabrachial injection **alone** labels ~85%
  of all lamina I projection neurons in rat L4, and that those include **more than 95% of the cells
  projecting to the periaqueductal grey.** On that reading the 85% belongs to the parabrachial
  injection without the medulla, and the 95% is a statement about the spino-periaqueductal subset
  rather than about ascending lamina I neurons in general. **This is read from a secondary citation
  of the paper, not from the paper**, so it is a candidate discrepancy and not a correction.
  **Owed: open Spike et al. and settle both numbers.** *(searched 2026-08-12; candidate. Lines 329,
  375; same work at line 552.)*
- **Stein & Meredith** — **owed**: not searched; **the key carries no year and no title.** It
  supports multisensory enhancement, which the Function slot names as the classic property of this
  structure. **Same lineage as the key below.** *(Line 89.)*
- **Stein & Meredith lineage** — **the same body of work as the key above**, written as a lineage at
  the Internal-structure slot. **Owed at the citing lines: use one key, and give it a year.** *(Line
  205.)*
- **Sugimura et al. 2016, review** — **the same work as the key below**, cited in short form. See
  that entry. **Owed at the citing lines: use one key.** *(Line 329.)*
- **Sugimura, Takahashi, Watabe & Kato, J Neurophysiol 115:2721, 2016** — **owed**: not searched.
  Declared on the citing line as both a review and channelrhodopsin-assisted circuit mapping, which
  is two kinds of source in one key; **owed: say which part supports which claim.** **Same work as
  *Sugimura et al. 2016, review* at line 329.** *(Line 309.)*
- **Sved, Ito & Madden, Brain Res Bull 51:129, 2000** — **owed**: not searched. *(Line 375.)*
- **Van Opstal/Goossens lineage, PLoS Comput Biol 8:e1002508, 2012** — **owed**: not searched. It
  carries the saccade place-code payload — the claim that the message is where the population sits
  rather than how fast it fires, which the entry calls the one place in the visual line where a
  payload is a position in tissue. **Highest-value owed key in the superior colliculus entry.**
  **Same work as *PLoS Comput Biol 2012* at line 167.** *(Line 161.)*
- **Weiskrantz** — **owed**: not searched; **the key carries no year and no title**, and no work can
  be found from it. It is the blindsight attribution in the Function slot — a claim the entry itself
  goes on to qualify twice. *(Line 81.)*
- **Wurtz & Goldberg 1972** — **owed**: not searched. *(Line 161.)*
- **Zheng, Adams, Horton et al., J Neurosci 44, 2024** — **partial, resolved incidentally.** The
  search for the Katz preprint surfaced what is evidently this paper: *Retinal Input to Macaque
  Superior Colliculus Derives from Branching Axons Projecting to the Lateral Geniculate Nucleus*,
  *Journal of Neuroscience* 44(44): e0888242024. **Macaque**, two males, double retrograde labelling
  with cholera toxin subunit B conjugates into physiologically identified collicular sites and
  retinotopically matched geniculate sites. *(**Journal page surfaced in a search for a different
  paper; the author list was not confirmed against the publisher record and the key's author string
  is unverified.** Owed: confirm.)* **What the citing line does and does not drop, stated after a
  re-check.** Line 97–98 says the input is largely a branch of axons that also reach the lateral
  geniculate nucleus, without naming a lamina. **The magnocellular specificity is not missing from
  the entry** — line 268 has the Katz stimuli chosen to favour "the magnocellular cells the
  retinotectal tract arises from," line 283 records the contrary result as a magnocellular
  geniculate block, and line 106 calls the corticotectal projection strongly magnocellular-driven.
  **So the fact is carried, and carried at the point where it does the work.** **What is missing is
  smaller, and is a cross-reference:** line 268 states the fact without pointing at this key, so a
  reader cannot tell whether that clause is part of the Katz result or an anatomical premise
  imported from here. **A separate question is live at line 97, and it is about wording rather than
  a missing fact.** This paper's own framing is stronger than "largely" — that the collicular
  projection arises entirely from collaterals of magnocellular-projecting axons — while its
  abstract notes the double-labelled percentage varied locally with tracer efficiency and
  retinotopic overlap, which is itself a reason to hedge. **"Largely" may be the more defensible
  word. Owed: open the paper and settle it**; no search will.
  *(searched 2026-08-12; candidate, partial. Line 101.)*
- **a 2026 midbrain-mapping preprint** — **owed, and the key names no work** — no author, title,
  server or identifier. It is the file's only human anatomical evidence for the rostromedial
  tegmental nucleus. **Owed: name it.** *(Lines 912–914.)*
