# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-12
---

---

# FILE 15 OF 20 — CRANIAL-NERVE NUCLEI AND FINER BRAINSTEM DETAIL

**What is in this file.** Finer brainstem detail: the ocular motor nuclei, branchiomotor and visceromotor nuclei, the trigeminal sensory complex, and the pretectum with the gaze-integrator tegmental cell groups.

**Size:** 496 non-blank lines, ~12.1k tokens / 48 kB. **Entries:** 4. **Edge lines:** 24 — 13 in, 10 out, 1 internal. **Internal structure slots:** 4 of 4. **Reference keys:** 9, over 12 mentions — the smallest and best-formed key list in the source; one of them shared with file 14.

**A recurring pattern in this file:** many endpoints are *peripheral* — extraocular and orofacial muscle, autonomic ganglia, sensory ganglia — recorded as peripheral termini rather than owed edges, because they are motor and sensory ends of the nervous system, not central-nervous-system regions with entries.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**A second abbreviation pass, 2026-07-27, and it changed no content.** The 2026-07-25 pass expanded the abbreviations in the four entries; this one closes what it left. Three bare cranial-nerve numerals in the ocular-motor Internal-structure slot — *oculomotor (III), trochlear (IV), abducens (VI)*, and then *III*, *IV* and *VI* standing alone in the following sentence — now carry the nerve name, which is the convention that pass's own stamp records. The citation accessions now name their databases once: **PubMed Central**, **PubMed identifier**, and **digital object identifier suffix**. No edge, count, payload, owed mark or pass stamp was touched. **The cranial-nerve numerals elsewhere in the file are correct as they stand** — a numeral qualified by its nerve name is a second label alongside a written-out name, which is what §3 asks for, and the file uses that form consistently everywhere else.

**Entries in this file, with the date each was last worked:**

- **Ocular motor nuclei — the oculomotor, trochlear and abducens nuclei (cranial nerves III, IV and VI), with the Edinger-Westphal nucleus (extraocular / pupillary motor pools)** — pass 2026-07-25 — abbreviations expanded to full names, cranial-nerve numerals always qualified by nerve name; the abducens internuclear yoking edge typed as an internal edge, discharging the owed item and closing the far end declared at file 18; the medial longitudinal fasciculus recorded as now having an entry
- **Branchiomotor / visceromotor nuclei — cranial nerves V, VII, IX, X, XI and XII (orofacial / visceral motor pools)** — pass 2026-07-25 — abbreviations expanded to full names, cranial-nerve numerals always qualified by nerve name; the claim that the corticobulbar tract has an entry in file 18 corrected — it has none, and what that file holds is the internal-capsule entry naming corticobulbar fibres through the genu
- **Trigeminal sensory complex — mesencephalic, principal (pontine), and spinal trigeminal nuclei (the face's sensory column)** — pass 2026-07-25 — abbreviations expanded to full names; the thalamic and cortical endpoints written out in full (ventral posteromedial nucleus, primary somatosensory cortex); no edge changed
- **Pretectum and gaze-integrator tegmental cell groups (pupillary light reflex; the oculomotor neural integrators)** — pass 2026-07-25 — abbreviations expanded to full names, including the four-abbreviation gaze-machinery string in the closing paragraph; the eye-position output edge's tract attribution recorded as owed at both ends against file 18's medial longitudinal fasciculus entry

---

# CRANIAL-NERVE NUCLEI AND FINER BRAINSTEM DETAIL (segmental motor / sensory nuclei, pretectum, gaze integrators)

*The finer subcortical layer the brainstem section flagged as residual: the individual cranial-nerve
motor and sensory nuclei, the pretectum, and the small tegmental gaze-integrator cell groups. Several
cranial-nerve nuclei are **already in the map where a pathway needed them** — the cochlear nucleus and
the four vestibular nuclei (cranial nerve VIII; Auditory pathway, Other senses), the nucleus of the solitary tract
(taste and visceral afferents, cranial nerves VII, IX and X; Other senses, Reticular formation), and the dorsal-column /
trigeminal first somatosensory relay (cranial nerve V; Sensorimotor loop) — so this section adds the ones still open
and gathers the set. These are small nuclei defined by nerve and function; **counts are
firm only where human stereology exists** (the facial nucleus), else soft — most cranial-nerve nuclei are
uncounted in human. **Number convention:** these are paired (bilateral) nuclei, given **per side** unless
tagged.*

## Ocular motor nuclei — the oculomotor, trochlear and abducens nuclei (cranial nerves III, IV and VI), with the Edinger-Westphal nucleus (extraocular / pupillary motor pools)

- **Function:** the somatic-motor final common path for **eye movement**, plus parasympathetic pupil
  control. **Oculomotor nucleus (cranial nerve III, midbrain)** drives four of the six extraocular muscles (medial, inferior,
  and superior recti; inferior oblique) and the levator palpebrae; its visceral partner the
  **Edinger-Westphal (accessory oculomotor) nucleus** holds the **parasympathetic preganglionics** for
  pupillary constriction and lens accommodation. **Trochlear nucleus (cranial nerve IV, midbrain)** drives the superior oblique
  — the only cranial nerve that is **crossed and exits dorsally**. **Abducens nucleus (cranial nerve VI, pons)** drives the
  lateral rectus and, through its **internuclear neurons** (ascending the contralateral medial
  longitudinal fasciculus to the oculomotor medial-rectus pool), **yokes the two eyes** for conjugate
  horizontal gaze. This is the **motor terminus of the oculomotor loop** the lateral-intraparietal,
  frontal-eye-field and superior-colliculus entries pointed to — the place where a gaze *command*
  becomes muscle innervation.
- **Inputs:**
  - **← the brainstem saccade burst generators** — the **paramedian pontine reticular formation**
    (horizontal → abducens) and the **rostral interstitial nucleus of the medial longitudinal
    fasciculus** (vertical → oculomotor / trochlear) — **carries:** a **timed burst driving eye
    muscles** — the pulse that moves the eye, in temporal (rate) code, the output side of the
    spatial-to-temporal conversion the superior colliculus performs. **Fan-in:** unknown. **The
    producers are in the reticular-formation entry (file 14)**, which names these burst generators as
    the common final path the frontal eye fields, superior colliculus and vestibulo-ocular reflex all
    drive; that entry declares the cranial-nerve motor nuclei among its outputs as a class. **Owed at
    file 14: name this nucleus out of that class.**
  - **← the gaze neural integrators** — the **nucleus prepositus hypoglossi** (horizontal) and the
    **interstitial nucleus of Cajal** (vertical) — **carries:** an eye-**position** command, the time
    integral of the velocity command, the signal that holds the eye still between saccades.
    **Fan-in:** unknown. **The producer is in this file** (the pretectum / gaze-integrator entry,
    which declares "→ the ocular motor nuclei (oculomotor, trochlear and abducens)" carrying eye position). **Two-ended
    within-file.**
  - **← the vestibular nuclei**, via the **medial longitudinal fasciculus** — **carries:** the
    **vestibulo-ocular reflex command** — an eye-velocity signal equal and opposite to head rotation,
    driven chiefly by the semicircular-canal line; the fastest gaze-stabilising reflex. **Fan-in:**
    unknown. **The producer declares it and names this structure** (file 3), whose vestibular Outputs
    read "→ oculomotor nuclei (oculomotor, trochlear and abducens), via the medial longitudinal fasciculus." **Two-ended.**
    **The tract now has an entry** (file 18), which records this edge as one of the few in the source
    declared, named and typed at both region ends before its tract had an entry at all.
  - **← the superior colliculus and frontal eye fields** (via the burst generators above) —
    **carries:** the saccade goal that the burst generators convert into the pulse; **no direct
    edge** — this is the loop those entries traced, and it reaches this nucleus **only through** the
    burst generators, not monosynaptically. **Recorded as an indirect route, not a typed direct
    edge**; the direct producers are the burst generators line above.
  - **← the pretectum**, onto the **Edinger-Westphal nucleus** — **carries:** the **pupillary light
    reflex** drive — a luminance scalar as a drive to constrict, monosynaptic, excitatory and
    **bilateral** (the source of the consensual response). **Fan-in:** unknown. **The producer is in
    this file** (the pretectum entry, which declares "→ Edinger-Westphal nucleus, preganglionic
    subdivision, bilaterally" onto a distinct pupillary subpopulation). **Two-ended within-file.**
- **Outputs:**
  - **→ the extraocular muscles** (medial / inferior / superior recti and inferior oblique from
    oculomotor; superior oblique from trochlear; lateral rectus from abducens) and the levator
    palpebrae — **carries:** the **motor command to the eye muscles** — the terminus of the
    oculomotor loop. **Fan-out:** unknown. **These are peripheral striated muscle, not a central-nervous-system region**,
    so this is a motor terminus, not an owed edge — the same treatment the spinal ventral horn's
    output to muscle gets.
  - **→ the ciliary ganglion**, from the **Edinger-Westphal nucleus** → the sphincter pupillae and
    ciliary muscle — **carries:** the parasympathetic preganglionic command for **pupil constriction
    and lens accommodation**. **Fan-out:** unknown. **The ciliary ganglion is a peripheral
    parasympathetic ganglion with no entry**; recorded as a peripheral autonomic terminus, not an
    owed edge.
- **Internal structure and internal data flow:** **owed.** This entry holds **three motor nuclei plus
  a visceral subnucleus** as sub-elements — oculomotor (cranial nerve III), trochlear (cranial
  nerve IV), abducens (cranial nerve VI), and the Edinger-Westphal — gathered by shared function
  (eye movement) rather than by neighbourhood; the oculomotor nucleus and the Edinger-Westphal are
  contiguous, but the trochlear and abducens nuclei sit at different brainstem levels. They are
  load-bearing: the burst-generator and integrator inputs above segregate by axis (horizontal →
  abducens, vertical → oculomotor / trochlear), and the light-reflex input goes specifically to the
  Edinger-Westphal. **One internal edge is real and describable, and it is typed here.**
  - **Internal edge — abducens internuclear neurons → the contralateral oculomotor medial-rectus
    pool**, ascending in the **medial longitudinal fasciculus: carries:** the **yoking signal** — a
    copy of the abducens nucleus's own lateral-rectus drive, delivered to the medial rectus of the
    other eye so the two eyes rotate together in conjugate horizontal gaze. It carries **no
    independent command**: what travels is the same drive the abducens is already sending to its own
    muscle, which is why a lesion of the tract produces **internuclear ophthalmoplegia** — adduction
    fails while abduction survives, and the eyes come apart. **This edge crosses the midline**, the
    only one in this entry that does. **Fan-in / fan-out:** unknown. **The tract it rides has an
    entry** (file 18), which declares this limb from its end and marks it owed here; **typed now, and
    that owed item is discharged.** *(Class 3 — general brainstem anatomy; the reading that the
    payload is a copy rather than an independent command is Claude's, Class 2, offered to be
    checked.)*

  **Owed: split the sub-nuclei formally and assign each input by axis.**
- **Neurons:** soft — the extraocular somatic-motor pools are small, order **10³–10⁴ per side** (no
  clean human absolute count pulled here); Edinger-Westphal is a small visceromotor group.
- **Synapses:** unknown.
- **Axons:** the oculomotor, trochlear and abducens nerves (cranial nerves III, IV and VI; counts unknown).
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** the oculomotor, trochlear and abducens nerves myelinated; g-ratio unknown.
- **Pass:** 2026-07-25 — abbreviations expanded to full names, cranial-nerve numerals always qualified by nerve name; the abducens internuclear yoking edge typed as an internal edge, discharging the owed item and closing the far end declared at file 18; the medial longitudinal fasciculus recorded as now having an entry

## Branchiomotor / visceromotor nuclei — cranial nerves V, VII, IX, X, XI and XII (orofacial / visceral motor pools)

- **Function:** the motor pools for the jaw, face, throat, tongue, and viscera. **Trigeminal motor nucleus
  (cranial nerve V, pons)** — muscles of mastication (plus tensor tympani / tensor veli palatini). **Facial nucleus (cranial nerve VII, pons)**
  — the muscles of facial expression and the stapedius; the branchiomotor pool with the clinical
  upper-face-bilateral / lower-face-contralateral corticobulbar rule. **Nucleus ambiguus (cranial nerves IX, X and XI,
  medulla)** — striated **pharyngeal and laryngeal** muscle (swallowing, phonation), plus cardioinhibitory
  vagal preganglionics. **Superior and inferior salivatory nuclei (cranial nerves VII and IX)** — parasympathetic to the
  lacrimal / nasal and the salivary glands. **Dorsal motor nucleus of the vagus (cranial nerve X, medulla)** — the
  **largest parasympathetic preganglionic source** of the lower brainstem, to the thoracoabdominal viscera
  (the vagal visceromotor arm). **Hypoglossal nucleus (cranial nerve XII, medulla)** — the intrinsic and extrinsic **tongue**
  muscles, the final common path for speech and swallowing. **Spinal accessory nucleus (cranial nerve XI, upper cervical cord — the first through fifth or sixth cervical segments)** — sternocleidomastoid and trapezius (technically cord, gathered here for the nerve). This is
  the orofacial and cranial-parasympathetic **motor terminus**, the counterpart of the spinal ventral
  horn and the spinal-cord intermediolateral sympathetic column.
- **Inputs:**
  - **← the cerebral cortex**, via the **corticobulbar tract** (through the internal-capsule genu) —
    **carries:** the voluntary motor command for the jaw, face, larynx, and tongue — the cranial
    analogue of the corticospinal command. The **facial pool** carries the clinical rule on this edge:
    upper-face motoneurons receive **bilateral** corticobulbar input, lower-face **contralateral
    only**. **Fan-in:** unknown. **This endpoint names a class** — "the cerebral cortex" — and the
    **corticobulbar tract has no entry of its own**: what file 18 holds is the **internal capsule**
    entry, which names corticobulbar fibres passing through the genu as one of the fibre systems it
    routes. Checked 2026-07-25 across all twenty files. **Owed: resolve the cortical origin to named producers** (the primary motor and
    premotor face/tongue/larynx representations in files 5 and 11 are the candidates).
  - **← the nucleus of the solitary tract** (reflex loops: gag, swallow, baroreflex) — **carries:**
    the **afferent limb of vagal reflexes** — visceral and gustatory afferent state driving the
    reflex motor response; **payload otherwise owed. Fan-in:** unknown. **The producer declares it and
    names this structure** (file 14), whose solitary-nucleus Outputs read "→ Branchiomotor /
    visceromotor nuclei, to the dorsal motor nucleus of the vagus — carries: the afferent limb of
    vagal reflexes." **Two-ended.**
  - **← the spinal trigeminal nucleus** (reflex loops: corneal, jaw) — **carries:** the afferent limb
    of the corneal and jaw reflexes; **payload owed. Fan-in:** unknown. **The producer is in this file**
    (the trigeminal sensory complex entry), whose mesencephalic → trigeminal-motor jaw-jerk edge is
    the monosynaptic member of this reflex family. **Owed: type the reflex edges at the trigeminal
    entry.**
  - **← the reticular premotor pattern generators** for chewing, swallowing, respiration and
    vocalisation — **carries:** the **rhythmic motor pattern** that sequences these pools; **payload
    owed. Fan-in:** unknown. **The producer is in the reticular-formation entry (file 14)**, which
    names the chewing / swallowing / facial / laryngeal patterns among its premotor coordinators.
    **Owed at file 14: name these pools out of the cranial-nerve-motor-nuclei class.**
- **Outputs:**
  - **→ the orofacial striated muscle** — muscles of mastication (trigeminal), facial expression and stapedius
    (facial), pharynx and larynx (nucleus ambiguus — glossopharyngeal, vagus, accessory), tongue (hypoglossal), sternocleidomastoid and
    trapezius (accessory) — **carries:** the **motor command to those muscles**; the final common path for
    chewing, facial expression, swallowing, phonation and speech articulation. **Fan-out:** unknown.
    **Peripheral striated muscle, not a central-nervous-system region** — a motor terminus, not an owed edge.
  - **→ the cranial parasympathetic ganglia**, from the **dorsal motor nucleus of the vagus** and the
    **nucleus ambiguus** (cardiac, respiratory, gastrointestinal preganglionics) and the **salivatory
    nuclei** (→ pterygopalatine / submandibular / otic ganglia → lacrimal, nasal and salivary glands)
    — **carries:** the **cranial (vagal) parasympathetic outflow** — the counterpart of the spinal
    intermediolateral sympathetic column; **payload otherwise owed. Fan-out:** unknown. **These are
    peripheral autonomic ganglia and end organs with no entry**; recorded as peripheral autonomic
    termini, not owed edges. *(The cardioinhibitory vagal outflow is the efferent limb of the
    baroreflex whose afferent limb arrives from the solitary nucleus above — the loop closes across
    this entry.)*
- **Internal structure and internal data flow:** **owed.** This entry gathers **eight distinct motor
  nuclei** as sub-elements — trigeminal motor, facial, nucleus ambiguus, superior and inferior
  salivatory, dorsal motor vagus, hypoglossal, and spinal accessory — spread from pons to upper
  cervical cord and sharing only the property of being cranial (or cranial-like) motor pools. They
  are load-bearing: the inputs above target specific pools (corticobulbar → facial with its
  bilateral/contralateral rule; solitary → dorsal motor vagus; pattern generators → the rhythmic
  pools). **No internal edge among them is described**, and most likely few exist — these are parallel
  effectors, not a chain — **except the reflex arcs** that pass *through* the sensory entries rather
  than within this one. **Owed: split the eight pools formally and assign every input edge to its
  pool.** The split matters more here than usual because the pools have very different clinical
  signatures (the facial rule, the ambiguus swallowing/phonation role, the vagal cardiac outflow).
- **Neurons:** the **facial motor nucleus ~10,000 per side** — the one **firm human count** in this
  section (Sherwood 2005, comparative-anatomy review; the primary human quantitative source is
  Blinkov & Ponomarev 1965, facial + vestibular nuclei), corroborated by the matching
  myelinated-axon count of the facial nerve. *(This count is for one sub-element, the facial nucleus —
  the per-sub-element figure the Internal-structure slot calls for, recorded here until that slot is
  typed.)* The other somatic-motor pools (trigeminal motor, hypoglossal) are the **same order**
  (~10³–10⁴ per side, soft — no clean human absolute pulled); the visceromotor pools (salivatory,
  dorsal motor vagus, ambiguus) are soft, the dorsal motor vagus the largest.
- **Synapses:** unknown.
- **Axons:** the branchiomotor / visceromotor cranial nerves (facial-nerve myelinated-axon count
  corroborates the facial nucleus figure; others unknown).
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** branchiomotor / visceromotor cranial nerves myelinated; g-ratio unknown.
- **Pass:** 2026-07-25 — abbreviations expanded to full names, cranial-nerve numerals always qualified by nerve name; the claim that the corticobulbar tract has an entry in file 18 corrected — it has none, and what that file holds is the internal-capsule entry naming corticobulbar fibres through the genu

## Trigeminal sensory complex — mesencephalic, principal (pontine), and spinal trigeminal nuclei (the face's sensory column)

- **Function:** the **face's somatosensory column**, the cranial counterpart of the dorsal-column /
  anterolateral split. The **principal (pontine) nucleus** takes discriminative touch (the face's
  dorsal-column analogue); the **spinal trigeminal nucleus** (descending into the upper cervical cord)
  takes **pain / temperature** from the face — the trigeminal side of the first somatosensory relay the
  Sensorimotor-loop entry named. The **mesencephalic nucleus** is a singular exception: its cells are
  **primary sensory neurons whose somata sit inside the central nervous system** (the only ones in the body), carrying
  jaw-muscle-spindle proprioception and periodontal mechanoreception, with a monosynaptic reflex onto the
  trigeminal motor nucleus (the jaw-jerk).
- **Inputs:**
  - **← the trigeminal ganglion** (peripheral afferents from the face), onto the **principal** and
    **spinal** nuclei — **carries:** face somatosensation, split by submodality — **discriminative
    touch** to the principal nucleus, **pain / temperature** to the spinal nucleus, the cranial
    mirror of the dorsal-column / anterolateral separation. **Fan-in:** unknown. **The trigeminal
    ganglion is the peripheral first-order sensory ganglion**; recorded as a peripheral sensory
    source, the afferent counterpart of a dorsal-root ganglion, not an owed central-nervous-system edge.
  - **← the face's jaw-muscle spindles and periodontal receptors**, as the **mesencephalic
    nucleus's own peripheral processes** — **carries:** jaw-muscle-spindle **proprioception** and
    periodontal mechanoreception. **This is not a synaptic input**: the mesencephalic cells *are* the
    primary sensory neurons, with their somata inside the central nervous system and a peripheral process reaching the
    receptor — so the "input" is the cell's own dendrite, not an edge from another region. **Recorded
    as a primary-afferent terminus with no producer region**, the unique case this entry's Function
    flags.
- **Outputs:**
  - **→ the ventral posteromedial thalamus** (the trigeminothalamic tract), from the **principal**
    and **spinal** nuclei → the primary somatosensory cortex, face representation — **carries:** face somatosensation onward to cortex, the two
    submodalities kept separate. **Fan-out:** unknown. **The consumer declares the spinal-nucleus
    half** (file 12), whose posterior / ventromedial-posterior entry names "← the caudal spinal trigeminal nucleus
    (trigeminothalamic, for the face)" carrying the three labelled pain/temperature lines; the
    discriminative-touch half via the principal nucleus reaches the main ventral posteromedial
    nucleus and is named in the sensorimotor-loop entry (file 5). **Two-ended for the pain/temperature
    limb** (file 12); **owed for the discriminative-touch limb** — confirm file 5's ventral
    posteromedial entry names the principal nucleus.
  - **→ the trigeminal motor nucleus**, from the **mesencephalic nucleus** — **carries:** the
    **jaw-jerk reflex** — a monosynaptic proprioceptive reflex, jaw-muscle stretch driving jaw-muscle
    contraction; the one internal reflex arc this complex closes by itself. **Fan-out:** unknown.
    **The consumer is the branchiomotor entry in this file** (the trigeminal motor pool), which names
    the corneal and jaw reflexes among its inputs. **Two-ended within-file** — this is the
    monosynaptic member of that reflex family.
  - **→ the branchiomotor pools** (reflex arcs: corneal blink, jaw), from the **spinal** nucleus —
    **carries:** the afferent limb of the corneal and jaw-opening reflexes; **payload owed.
    Fan-out:** unknown. **The consumer is in this file** (the branchiomotor entry names the corneal
    and jaw reflexes among its inputs). **Two-ended within-file.**
- **Internal structure and internal data flow:** **owed.** Three sub-elements with distinct payloads,
  named in the entry's own Function: the **mesencephalic** nucleus (primary proprioceptive somata,
  jaw-jerk), the **principal (pontine)** nucleus (discriminative touch), and the **spinal** trigeminal
  nucleus (pain / temperature, descending into the cervical cord). They are load-bearing — the output
  edges leave from specific ones (mesencephalic → trigeminal motor; principal → ventral posteromedial
  touch; spinal → ventral posteromedial pain/temperature) — and the spinal nucleus is itself further
  divided (pars oralis, interpolaris, caudalis), with **pars caudalis** the pain/temperature part
  continuous with the spinal dorsal horn. **One internal edge is describable** — the mesencephalic →
  trigeminal-motor monosynaptic reflex is internal to the reflex arc but crosses to the motor entry;
  within the sensory complex proper, no internal edge is described. **Owed: split the three nuclei
  formally, sub-divide the spinal nucleus, and assign each output edge.**
- **Neurons:** soft — the mesencephalic nucleus is a small, distinctive population (order 10³,
  uncounted cleanly in human here); the principal / spinal trigeminal nuclei are the relay recorded
  soft in the Sensorimotor-loop entry. *(The remaining cranial sensory nuclei — cochlear + four
  vestibular nuclei, cranial nerve VIII, and the solitary nucleus, cranial nerves VII, IX and X — are already in the map.)*
- **Synapses:** unknown.
- **Axons:** the trigeminothalamic tract (counts unknown).
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.
- **Pass:** 2026-07-25 — abbreviations expanded to full names; the thalamic and cortical endpoints written out in full (ventral posteromedial nucleus, primary somatosensory cortex); no edge changed

## Pretectum and gaze-integrator tegmental cell groups (pupillary light reflex; the oculomotor neural integrators)

- **Function:** two small midbrain / tegmental groups completing the pupillary and oculomotor
  circuitry. The **pretectum** (midbrain–diencephalon junction) is the sensory limb of the
  **pupillary light reflex**: its **olivary pretectal nucleus** receives a minority of retinal
  ganglion cells and projects to the **Edinger-Westphal nucleus bilaterally** — hence the
  **consensual** response — → ciliary ganglion → sphincter pupillae; neighbouring pretectal nuclei
  serve the optokinetic response and accommodation. This is the **third non-image-forming retinal
  target** in the map, alongside the suprachiasmatic nucleus (retinohypothalamic, circadian) and the
  superior colliculus (retinotectal, orienting).
  **What the olivary pretectal nucleus computes is a scalar, and the computation is spatial
  integration.** Its cells are **luminance neurons**: tonic, on-centre, with very large receptive
  fields — a mean of about **31°** — driven by broad-field melanopsin-containing ganglion cells.
  Single-unit recording and microstimulation in the alert rhesus monkey identified these cells as
  the ones mediating the reflex, and electrical stimulation of the nucleus constricts the pupil.
  **The payload change here is dimensional**: a spatially resolved retinal signal arrives and a
  single number — how much light — leaves. *(Class 1 — Gamlin, Zhang & Clarke, Exp Brain Res
  106:169, 1995, rhesus; Clarke & Ikeda 1985, rat; Trejo & Cicerone 1984.)*
  The **gaze integrators** are the "velocity-to-position" cell groups that hold the eye at an
  eccentric position between saccades: the **nucleus prepositus hypoglossi** with the medial
  vestibular nucleus (horizontal) and the **interstitial nucleus of Cajal** (vertical), working
  with the **paramedian pontine reticular formation** and **rostral interstitial nucleus of the
  medial longitudinal fasciculus** burst generators (named in the Reticular formation entry) to
  feed the ocular motor nuclei.
- **Inputs:**
  - **← retina, onto the olivary pretectal nucleus** — **carries:** **ambient luminance as a
    scalar** — a slow, broad-field measure of light falling on one eye, from intrinsically
    photosensitive broad-field ganglion cells containing melanopsin that also take rod and cone
    input. **Does not carry:** hue, form, motion, or a usable eye of origin. **The chiasm's split
    applies:** temporal retina to the ipsilateral nucleus, nasal retina to the contralateral one,
    at **nearly equal density** in macaque. Declared at the retina's end. **Fan-in:** unknown, but
    it is **high by construction** — retinal terminals concentrate inside the nucleus's borders and
    the projection cells' dendrites branch heavily through that core, which is the stated substrate
    for the very large receptive fields. *(Class 1 — Brain Struct Funct, digital object identifier suffix
    s00429-019-02003-7, anterograde and retrograde tracer plus electron microscopy, macaque. Not
    yet verified for the source.)*
  - **← superior colliculus, frontal eye fields, vestibular nuclei, and cerebellum**, onto the
    **integrators and burst generators** — **carries:** payload **owed**; eye-movement commands and
    head-velocity signals requiring the position hold. **Fan-in:** unknown. *(Class 3.)*
- **Outputs:**
  - **→ Edinger-Westphal nucleus, preganglionic subdivision, bilaterally**, from the olivary
    pretectal nucleus — **carries:** the luminance scalar, as a **drive to constrict**. The
    connection is **monosynaptic, excitatory, and bilateral**, onto a **distinct subpopulation** of
    preganglionic motoneurons — the pupillary ones, not the lens-accommodation ones sharing the
    nucleus. The terminals hold clear spherical vesicles with scattered dense-core vesicles,
    suggesting a peptide co-transmitter alongside the fast excitation. **The bilaterality is where
    the consensual response comes from**, and in macaque it is achieved by this projection rather
    than by a commissure: anterograde and retrograde tracing found **little evidence of a pretectal
    commissural projection**, which is attributed to each retina already supplying both nuclei
    almost equally. **A quantitative asymmetry worth carrying:** pupillary motoneurons receive
    **more inhibitory input** than the lens motoneurons beside them. **Fan-out:** unknown.
    *(Class 1 — Brain Struct Funct, PubMed Central PMC6957570 and digital object identifier
    suffix s00429-019-02003-7, macaque. Not yet verified
    for the source.)*
  - **→ intermediate gray layer of the superior colliculus, periaqueductal gray, interstitial
    nucleus of Cajal, and the ventral lateral geniculate / intergeniculate leaflet**, from the
    olivary pretectal nucleus — **carries:** payload **owed**. Recorded because the entry
    previously declared **one** output for this nucleus and the tracing shows several, ascending
    and descending; the luminance signal reaches the orienting and circadian machinery as well as
    the pupil. **These are rat**, and no macaque confirmation was read. **Fan-out:** unknown.
    *(Class 1 — Klooster et al., Phaseolus vulgaris leucoagglutinin, PubMed identifier 8542320,
    albino rat.
    Not yet verified for the source.)*
  - **→ the ocular motor nuclei** — oculomotor, trochlear and abducens — from the nucleus prepositus hypoglossi, the
    interstitial nucleus of Cajal, and the burst generators — **carries:** an eye-**position**
    command, the time integral of the velocity command arriving at the burst generators. **The
    payload change is an integration in time**, and it is what holds the eye still between
    saccades. **Payload otherwise unknown — owed.** **Fan-out:** unknown.
    **The tract this edge rides is not stated at either end.** The medial longitudinal fasciculus
    entry (file 18) records the integrator limb as **Class 3** at its end for exactly this reason —
    it carries the vestibulo-ocular and yoking traffic on declared authority and the integrator
    traffic on general anatomy alone. **Owed at both ends: name the tract, or record that it is
    unknown.**
- **Internal structure and internal data flow:** *(Added 2026-07-19. **Nothing here is yet verified
  for the source.**)*

  **Sub-elements: this entry holds two structures that share no edge with each other**, and that is
  worth stating plainly rather than leaving implicit in the title. The **olivary pretectal
  nucleus** (with its neighbouring pretectal nuclei serving optokinesis and accommodation) and the
  **gaze integrators** — nucleus prepositus hypoglossi, interstitial nucleus of Cajal — were
  gathered here by anatomical neighbourhood, not by data flow. **Splitting them into separate
  entries is owed**, on the same grounds as V3 and the ventral posterior area, and the two
  inferotemporal divisions.

  **Inside the olivary pretectal nucleus: a shell of somata around a core of neuropil.** The cells
  projecting to the Edinger-Westphal nucleus have somata at the **periphery** of the nucleus, with
  heavily branched dendrites extending **into the core**; the retinal terminals concentrate within
  the nucleus's borders, making asymmetric contacts with clear spherical vesicles. **The place a
  cell's body sits and the place it receives are therefore different**, which is the same
  owner/place distinction this file records for cortical layer 1 — and, as there, **no second
  internal edge is written for it**: there is no second synapse, the signal reaches the soma by
  propagation within one cell. The projection cells received **relatively few somatic contacts**.
  *(Class 1 — Brain Struct Funct, digital object identifier suffix s00429-019-02003-7, macaque.)*

  **Internal edges:**
  - **retinal terminal → the dendritic core of the olivary pretectal nucleus** — **carries:** the
    luminance signal, converging from a very wide retinal field onto a heavily branched dendritic
    tree. **This convergence is the computation the entry's Function claims** — it is where the
    spatial resolution is discarded and the scalar is formed. **Fan-in:** unknown, high.
    **Fan-out:** unknown.
  - **commissural, olivary pretectal nucleus ↔ contralateral olivary pretectal nucleus** —
    **carries:** in some species, the balancing signal that equalises the direct and consensual
    responses. **In macaque this edge is largely absent**, and the balance comes from the near-equal
    bilateral retinal input instead. Recorded as a **species difference, not a gap**. **Fan-in:**
    unknown. **Fan-out:** unknown. *(Class 1 — same source, macaque; Klooster et al. for the rat
    pattern.)*
  - **Inside the gaze integrators: unknown.** Nothing read in this pass describes the internal
    circuit that performs the integration, and the integration is the whole function. **Owed**, and
    it is the more interesting of the two gaps here: a mechanism that holds a value against decay
    is exactly the kind of thing a lower rung has to build.
- **Neurons:** soft / unknown throughout — small, ill-bordered tegmental cell groups, uncounted in
  human here. **The olivary pretectal nucleus is the one that could be counted**: it has definite
  borders in macaque, its projection cells were retrogradely labelled and localised, and no human
  figure was searched for in this pass.
- **Synapses / Axons / volumes / Myelination:** unknown.
- **Pass:** 2026-07-25 — abbreviations expanded to full names, including the four-abbreviation gaze-machinery string in the closing paragraph; the eye-position output edge's tract attribution recorded as owed at both ends against file 18's medial longitudinal fasciculus entry

**The cranial-nerve nuclei and finer brainstem detail are described:** the **ocular motor nuclei**
(oculomotor with the Edinger-Westphal nucleus, trochlear, abducens — the extraocular and pupillary motor pools, the **motor terminus of the
oculomotor loop**), the **branchiomotor / visceromotor pools** (trigeminal motor, facial, ambiguus,
salivatory, dorsal motor vagus, hypoglossal, accessory — the orofacial and **cranial-parasympathetic**
outflow, complementing the spinal intermediolateral sympathetic column and receiving the **corticobulbar** terminus), the
**trigeminal sensory complex** (mesencephalic / principal / spinal — the face's sensory column into the ventral posteromedial thalamus),
and the **pretectum + gaze integrators** (the pupillary light reflex — the third non-image-forming retinal
target — and the nucleus-prepositus-hypoglossi, interstitial-nucleus-of-Cajal, paramedian-pontine-reticular-formation and rostral-interstitial-nucleus machinery driving the ocular motor nuclei). This **closes the
oculomotor loop onto its muscles**, adds the **pupillary-light-reflex** retinal target, and lands the
**corticobulbar** and **cranial-parasympathetic** termini. The one firm human count is the **facial motor
nucleus ~10,000 / side** (Sherwood 2005; Blinkov & Ponomarev 1965); the rest are soft — small nuclei,
mostly uncounted in human. What remains subcortically is the even-finer long tail (minor tegmental and
periaqueductal cell groups), added as a pathway needs it.

---


## References

*(Section added 2026-08-12 under source design §2a. Every line below is a **candidate**
awaiting Micky's verification; none is verified. Each full reference given here was obtained by
a web search run in this pass against publisher, journal or PubMed records — no reference is
written from recall. Keys reading **owed** were not searched in this pass.)*

**9 distinct keys, 12 mentions. 4 resolved to a full reference; 5 owed.** The smallest key list in
the source so far, and the best-formed: **every key carries either an author name or a resolvable
identifier**, which is not true of files 12, 13 or 14. Three of the nine carry a digital object
identifier or a PubMed identifier outright, which is why four could be closed in one short pass.

**One key names two different papers, and this is the finding.** Line 330–331 reads *Brain Struct
Funct, PubMed Central PMC6957570 and digital object identifier suffix s00429-019-02003-7*. **Those
two identifiers are not two labels for one paper.** The digital object identifier is May & Warren
on the **olivary pretectal nucleus**; the PubMed Central accession is May, Sun, Wright & Erichsen
on the **preganglionic Edinger–Westphal nucleus**. They are companion papers, same journal, same
issue, overlapping authors, published a week apart — which is exactly how they came to be written
as one key, and exactly why a reader will not untangle them. **The claims on lines 319–329 span
both.** See the two entries below. **Owed at the citing line: split it into two keys and say which
supports which claim.**

**One key is shared with file 14, and it is the cleanest instance of the shared-source case in the
source so far.** *Klooster et al.* appears here at line 339 and in file 14 at line 143, **with the
same PubMed identifier at both ends**, supporting the two halves of one edge — the olivary
pretectal nucleus's projection to the superior colliculus's intermediate gray, declared as an
output here and as an input there. Unlike the bare accessions shared between files 12 and 13, this
one carries an author name at both ends, so either file can find it alone. **Recorded as working,
not as a defect.**

**A caution for whoever searches the remaining five.** The pretectal-luminance literature has a
tight cluster of papers by overlapping author sets in different orders — this file carries
*Gamlin, Zhang & Clarke 1995* and *Clarke & Ikeda 1985*, and the searching here also surfaced a
*Clarke, Zhang & Gamlin 2003* paper on pretectal luminance-neuron receptive fields. **Three papers,
three orderings of overlapping names, one topic.** The ~31° receptive-field figure at line 291 is
the one to watch; see the *Gamlin* entry.

**Species composition of the four resolved: two macaque, one albino rat.** Both May papers are
macaque; Klooster is rat, and the file already says so on the line. **The file's species discipline
is good** — every provenance mark here names a species. Five keys are unsearched.


- **Blinkov & Ponomarev 1965** — **owed**: not searched in this pass. **It is the primary human
  quantitative source behind the file's one firm human count** — the facial motor nucleus at
  ~10,000 per side — with *Sherwood 2005* named on the same line as the review through which it was
  read. The citing line already declares that relationship, which is §2a's required practice.
  **Highest-value owed key in the file**, and likely the hardest: a 1965 Russian-language monograph
  may not have a resolvable modern record. *(Lines 199, 406.)*
- **Brain Struct Funct, digital object identifier suffix s00429-019-02003-7** — May, P.J. & Warren,
  S. (2020). Pupillary light reflex circuits in the Macaque Monkey: the olivary pretectal nucleus.
  *Brain Structure and Function* 225(1): 305–320; doi 10.1007/s00429-019-02003-7; PubMed 31848686;
  free in PubMed Central. Received 10 September 2019, accepted 5 December 2019, published online
  17 December 2019 — **so the work is often cited as 2019 and the issue is 2020**, which is worth
  fixing in one direction before it becomes two keys. **Macaque**, anterograde and retrograde
  tracers with ultrastructural examination. *(Springer publisher record and PubMed.)* **Both citing
  lines check out against the paper's own abstract, closely.** Line 363–370's shell-of-somata-
  around-a-core-of-neuropil description is the paper's: neurons projecting to the preganglionic
  Edinger–Westphal nucleus have somata at the periphery with heavily branched dendrites extending
  into the core, retinal terminals concentrate within the borders and make asymmetric contacts with
  clear spherical vesicles, and the projection cells received relatively few somatic contacts.
  **Line 310–312's substrate claim is the paper's own conclusion almost word for word** — that the
  concentration of retinal terminals together with the extensive dendritic trees provides the
  substrate for very large receptive fields. **Nothing here needs changing.** *(searched
  2026-08-12; candidate. Lines 312, 371.)*
- **Brain Struct Funct, PubMed Central PMC6957570 and digital object identifier suffix
  s00429-019-02003-7** — **this key names two papers.** The digital object identifier is the May &
  Warren olivary-pretectal paper in the entry above. **The accession is a different work:** May,
  P.J., Sun, W., Wright, N.F. & Erichsen, J.T. (2020). Pupillary light reflex circuits in the
  macaque monkey: the preganglionic Edinger–Westphal nucleus. *Brain Structure and Function* 225(1):
  403–425; doi 10.1007/s00429-019-02000-w; PubMed 31875262; PMC6957570. **Macaque**, motoneurons
  labelled from ciliary-ganglion and orbital injections, with pretectal tracer placements.
  *(Springer publisher record, PubMed and PubMed Central.)* **The claims on lines 319–329 divide
  between the two papers**, and separating them would let each be checked: the pupillary-versus-lens
  motoneuron asymmetry at line 328–329 is an Edinger–Westphal finding and belongs to the accession;
  the pretecto-Edinger–Westphal projection and its bilaterality belong to both. **One thing the
  accession's paper adds that this file does not carry, and it bears on an internal edge here.**
  Line 379–384 records the pretectal commissure as largely absent in macaque, with the balance
  coming from near-equal bilateral retinal input. The Edinger–Westphal paper reports that pretectal
  terminals reach the contralateral preganglionic nucleus **by crossing above and below the cerebral
  aqueduct** — which supports the file's "by this projection rather than by a commissure" reading
  and gives it a route — **and that pretectal terminals also end in the lateral visceral column, a
  ventrolateral periaqueductal-gray region whose neurons project to the contralateral pretectum.**
  **That is an indirect pretecto-pretectal route**, which does not contradict "largely absent" as a
  statement about a direct commissure but does qualify it. **Owed: split this key, and decide
  whether the indirect route belongs on the internal-edge line.** *(searched 2026-08-12; candidate.
  Line 330.)*
- **Clarke & Ikeda 1985** — **owed**: not searched in this pass. Rat, per the citing line. **See the
  author-cluster caution above** before searching it. *(Line 296.)*
- **Gamlin, Zhang & Clarke, Exp Brain Res 106:169, 1995** — **owed**: not searched in this pass.
  Rhesus, per the citing line; it carries the luminance-neuron identification and the
  microstimulation result the pretectum entry's Function slot rests on. **One thing to check when it
  is searched.** The searching in this pass surfaced a later paper by the same three authors in a
  different order — Clarke, Zhang & Gamlin, *Primate pupillary light reflex: receptive field
  characteristics of pretectal luminance neurons*, *Journal of Neurophysiology* 89(6): 3168–3178,
  2003, PubMed 12611972 — **whose title is the receptive-field characteristics of exactly these
  cells.** Line 289–291 attributes a mean receptive field of about **31°** to the 1995 key. **That
  figure may belong to the 2003 paper instead.** **No line in this file cites the 2003 paper and
  none is added here**, per §2a; it is named so that the 31° can be checked against the right work.
  *(Line 295.)*
- **Klooster et al.** — **the same work as the key below**, cited in short form at the internal-edge
  line for the rat commissural pattern. See that entry. **Owed at the citing lines: use one key.**
  *(Line 383.)*
- **Klooster et al., Phaseolus vulgaris leucoagglutinin, PubMed identifier 8542320** — Klooster, J.,
  Vrensen, G.F.J.M., Müller, L.J. & van der Want, J.J.L. (1995). Efferent projections of the olivary
  pretectal nucleus in the albino rat subserving the pupillary light reflex and related reflexes: a
  light microscopic tracing study. *Brain Research* 688(1–2): 34–46; doi
  10.1016/0006-8993(95)00497-e; PubMed 8542320. **Albino rat**, iontophoretic *Phaseolus vulgaris*
  leucoagglutinin anterograde tracing. *(Elsevier publisher record and PubMed.)* **One method detail
  the file does not carry, and it strengthens a claim the file makes elsewhere.** The paper localised
  the nucleus **by physiological recording of its neurons under luminance stimulation before
  injecting the tracer** — so the cells whose projections it maps were confirmed to be
  luminance-responsive in the same animals. **That is direct support for the Function slot's
  "its cells are luminance neurons," which line 295–296 currently rests on the macaque keys alone.**
  **This key is shared with file 14** (line 143), where it supports the far end of the same edge,
  with the same identifier. **Same work as *Klooster et al.* at line 383.** *(searched 2026-08-12;
  candidate. Line 339.)*
- **Sherwood 2005** — **owed**: not searched in this pass. A comparative-anatomy review, declared as
  one on the citing line, standing in for *Blinkov & Ponomarev 1965*. *(Lines 198, 406.)*
- **Trejo & Cicerone 1984** — **owed**: not searched in this pass; the citing line gives no species.
  **See the author-cluster caution above.** *(Line 296.)*
