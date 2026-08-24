# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-21
---

---

# FILE 5 OF 20 — SENSORIMOTOR LOOP

**What is in this file.** The body-side sensorimotor loop, front to back: the dorsal column nuclei and trigeminal relay, the ventral posterior thalamus, primary and second somatosensory cortex, superior parietal area 5, and primary motor cortex.

**Size:** 758 lines, ~15.3k tokens (estimated from bytes, not tokenised). **Entries:** 6. **Edge lines:** 51 — 20 in, 31 out.

**The scope of the standard laminar block's failure is established across five files and recorded identically in each; the note sits in the primary motor cortex entry's Internal structure slot.**

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Dorsal column nuclei and trigeminal relay (first somatosensory relay, medulla)**
- **Ventral posterior nuclear complex (somatosensory thalamus)**
- **Primary somatosensory cortex (postcentral gyrus, isocortex)**
- **Second somatosensory area, with the parietal ventral and ventral somatosensory areas (isocortex)**
- **Superior parietal area 5 — areas PE, PEa and PEc (isocortex)**
- **Primary motor cortex (area 4, isocortex)**

---

# SENSORIMOTOR LOOP (body-side)

## Dorsal column nuclei and trigeminal relay (first somatosensory relay, medulla)

- **Function:** first central relay of somatosensory afferents — body via the **dorsal column
  nuclei**, face via the trigeminal sensory nuclei (described in their own entry, *Trigeminal
  sensory complex*). **The dorsal column nuclei are three, not two:** the **gracile nucleus**
  (lower body), the **cuneate nucleus** (upper body, neck and forelimb), and the **external
  cuneate nucleus**, which lies dorsolateral to the cuneate and is the origin of the
  proprioceptive projection to the cerebellum. Treating the complex as a two-part cuneate/gracile
  pair loses the sub-element the cerebellar edge leaves from. *(Class 1 — Loutit et al. 2021;
  Tracey & Waite, cited therein. Candidate — awaiting Micky's verification.)*
- **It is not a passive relay.** The complex is described in the current literature as a
  **sensorimotor integration and distribution hub**: it carries descending input from sensorimotor
  cortex, intrinsic inhibitory interneurons, and recurrent collaterals, and the signal that leaves
  is not the signal that arrived. *(Class 1 — Loutit et al. 2021, as above. Class 2 — the reading
  that this makes the entry a processing stage rather than a relay is Claude's. Candidate.)*
- **Inputs:**
  - **← mechanoreceptor and proprioceptor afferents** (body via the dorsal columns, face via the
    trigeminal nerve) — **carries:** two distinct payloads on one relay: **cutaneous** (touch,
    pressure, vibration — intensity per skin location, somatotopic) and **proprioceptive** (muscle
    spindle length and rate, Golgi tendon force, joint angle — the body's *configuration*, not the
    world's). **Fan-in:** no contacts-per-neuron figure found. A **convergence** figure exists and
    is not the same measurement: in anaesthetised macaque, **87% of 317 recorded cuneate and
    external-cuneate cells responded to stimulation of two or more peripheral nerves**, so a single
    relay cell reads from more than one nerve territory. *(Class 1 — J Neurophysiol 106:2233, 2011;
    macaque. Candidate.)*
  - **← primary sensorimotor cortex** (corticocuneate, from the hand regions of areas 3b, 3a, 1/2
    and the forelimb region of the primary motor cortex; **bilateral** — contralateral and
    ipsilateral) — **carries:** no new stimulus content; a **movement-contingent gain signal**. In
    monkey performing voluntary hand movement, somatosensory transmission through the cuneate is
    **attenuated**, by an amount comparable to that seen in cerebral cortex and larger than that
    seen in the spinal cord. The cortical fibres produce a **central zone of facilitation
    surrounded by a peripheral zone of inhibition**, which is a spatial sharpening operation and not
    a scalar gain. **Fan-in:** unknown. *(Class 1 — Cell Reports 43:113827, 2024, macaque;
    corticocuneate origin from J Comp Neurol 529:1401, 2021, New World monkey; centre–surround
    organisation from Canedo 1999, cat. Candidate.)*
    **This edge is the one every comparable first relay in this file also declares.**
- **Outputs:**
  - **→ ventral posterior thalamus** (medial lemniscus / trigeminothalamic tract) — **carries:** both payloads,
    somatotopic, relayed with the cutaneous and deep submodalities kept separate. **Fan-out:**
    unknown.
  - **→ cerebellum** (cuneocerebellar tract, **from the external cuneate nucleus**) — **carries:**
    proprioception only — body configuration, unconscious. **Fan-out:** unknown.

    *(**Structural note.** This edge and the thalamocortical one above carry **the same payload to
    two destinations of different kinds** — and proprioception is the only sense in this file that
    does so. The other senses branch too, but their branches carry **different** content: the retina
    sends orienting transients to the superior colliculus and a luminance scalar to the pretectum,
    not two copies of the image. Here one signal — body configuration — goes to the cerebellum as
    controller feedback and to area 3a as a percept. **The two copies differ in what kind of memory
    they write, not in whether they are used.** The cortical copy becomes something **reportable**,
    available to the rest of cognition as a described state. The cerebellar copy writes
    **procedural** change: motor learning is cerebellum-dependent, so that branch is not a discard
    path but plausibly the one accumulating the larger behavioural trace. **A learning channel that
    operates without perceptual access is an architectural fact, not an absence of one.** That is
    worth recording because it answers a question the file's structure otherwise invites: whether
    proprioception is a sense or a limb of the motor feedback system. **It is declared here as both,
    on two edges, with one payload.** A lower rung that folded the cerebellar branch into the motor
    loop and dropped the sense would still pass a consistency check on this entry unless the
    duplication is stated.)*
  - **→ dorsal cochlear nucleus** — **carries:** the head / face / neck configuration copy used to
    cancel self-generated sound. **Fan-out:** unknown. **Contested at the receiving end** — the
    cochlear nucleus entry records that the granule-cell domain carrying this copy is decreased or
    absent in primates, so what receives this edge in a human is owed.
- **Internal structure and internal data flow:** the gracile and cuneate nuclei are each divided
  into **two territories with different input regimes**, and the division is the entry's central
  structural fact:
  - **Cluster region** (the middle third of each nucleus; **pars rotunda** in the primate cuneate) —
    discrete clusters of tightly packed cells forming **cytochrome-oxidase-dense patches separated
    by cell-poor, oxidase-light septa**. Afferents from **glabrous skin of the digits and pads**
    terminate preferentially in these clusters. Punctate, high-acuity, one body part per cluster.
  - **Reticular region** (rostral and caudal to the clusters) — small and large **multipolar** cells,
    receiving diffuse terminations with **intersegmental overlap** rather than a somatotopic
    lamination.
  - **Internal edge — cluster region → medial lemniscus projection cells: carries:** the punctate,
    high-acuity cutaneous payload. **Fan-in / fan-out:** unknown.
  - **Internal edge — reticular region → medial lemniscus projection cells: carries:** the
    convergent, multi-territory payload the 87% figure above measures. **Fan-in / fan-out:** unknown.
  - **Internal edge — intrinsic inhibitory interneurons → projection cells: carries:** inhibition,
    no content; the substrate of the centre–surround sharpening the corticocuneate edge drives.
    **Fan-in / fan-out:** unknown.
  - **Internal edge — recurrent projection-cell collaterals → projection cells with overlapping
    receptive fields: carries:** synchronisation, no new content. **Fan-in / fan-out:** unknown.
  *(Class 1 — cluster/reticular division and the oxidase-dense patches: PNAS 120:e2222076120, 2023,
  macaque, owl monkey, squirrel monkey and galago; Maslany et al. 1991, rat. Interneurons, recurrent
  collaterals and the centre–surround: Canedo 1999, cat. Candidates — awaiting Micky's verification.
  Species note: the cluster/reticular division is primate and rodent; the internal edges are typed
  from cat physiology.)*
- **Contested for human, recorded not smoothed — a nociceptive character in the human cuneate.**
  The human cuneate nucleus contains discrete subregions, present from prenatal life to old age,
  whose neurochemistry — substance P, calcitonin-gene-related peptide, met- and leu-enkephalin,
  somatostatin, galanin, glial-cell-line-derived and brain-derived neurotrophic factor,
  polysialylated neural cell adhesion molecule, growth-associated protein 43 — closely resembles
  **the superficial layers of the caudal spinal trigeminal nucleus**, which is a nociceptive relay.
  The authors state the arrangement has never been formalised in the human brain and has not been
  described in another species. If it relays nociception, the entry's two-payload claim (cutaneous
  and proprioceptive) is incomplete for human. **Payload of any such third line — owed.**
  *(Class 1 — Del Fiacco et al. 2013; human medulla. Class 2 — the inference that this bears on the
  entry's payload claim is Claude's. Candidate — awaiting Micky's verification.)*
- **Neurons:** ~0.5M per hemisphere (best available; no clean human count — soft). No separate
  count for the external cuneate nucleus was found.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown. **Dimension found and not otherwise
  recorded:** the cuneate nucleus is about **4 mm long**, its midpoint near the level of the obex.
  *(Class 1 — Tracey & Waite, as cited in the ScienceDirect dorsal column nuclei overview; rat.
  Candidate, and a rat figure, so it is not a human number.)*

## Ventral posterior nuclear complex (somatosensory thalamus)

- **Function:** somatosensory thalamic relay to the primary somatosensory cortex — the body's
  counterpart of the lateral and medial geniculate nuclei. The complex has four named subnuclei,
  not two: the **ventral posterior lateral nucleus** relaying the body, the **ventral posterior
  medial nucleus** relaying the face, the **ventral posterior inferior nucleus** beneath
  them, and the **basal ventral medial nucleus** medially. Drives layer 4 of
  the primary somatosensory cortex; gated by the thalamic reticular nucleus.
  *(Class 1 — subnuclear division: Brain Struct Funct 2025, human; Rausell & Jones 1991, monkey.
  Candidate — awaiting Micky's verification.)*
- **The complex is built in two chemically distinct compartments, and this is its central
  structural fact.** A **core** of large and medium parvalbumin-positive relay cells, staining
  densely for cytochrome oxidase, and a **matrix** of smaller calbindin-positive cells staining
  weakly for it. The two take different afferents and project to different cortical layers, so a
  single edge from this complex to the cortex describes two different transfers. *(Class 1 — Rausell
  et al. 1992, monkey ventral posterior lateral nucleus; Jones 1998, review. Candidate.)*
- **Inputs:**
  - **← dorsal column nuclei and trigeminal relay** (medial lemniscus / trigeminothalamic tract) —
    **carries:** cutaneous touch, pressure and vibration, and proprioceptive configuration,
    somatotopic; the body to the ventral posterior lateral nucleus, the face to the ventral
    posterior medial nucleus. The **driver**, and as at the lateral and medial geniculate nuclei a
    minority of the synapses. **Terminates in the parvalbumin core**, and its terminals form
    **triadic synapses with GABAergic presynaptic dendrites** — a synaptic arrangement the
    spinothalamic input below does not have. **Fan-in:** unknown.
    *(Class 1 — compartment: Rausell et al. 1992, as above. Triads: Ralston & Ralston 1994, monkey.
    Candidate.)*
  - **← spinal cord grey matter** (spinothalamic tract, from laminae I and IV–VIII) and the
    **spinal trigeminal nucleus** — **carries:** pain, temperature and crude touch. **Terminates
    diffusely and preferentially in the calbindin matrix**, concentrated in the cytochrome-oxidase-
    weak cap over the posterior surface of the ventral posterior medial nucleus and in the ventral
    posterior inferior and basal ventral medial nuclei. About **10% of ventral posterior lateral
    neurons are nociceptive**, of wide-dynamic-range type. **Fan-in:** unknown.
    *(Class 1 — Rausell et al. 1992, monkey, spinothalamic terminations correlated with the
    compartments. The ~10% figure carries no primary human source — it stands unverified and is a
    candidate for removal or sourcing. Candidate.)*
    **Contested, recorded not smoothed.** Whether the lamina-I pain and temperature stream relays
    here at all is disputed: Craig and colleagues hold that lamina-I terminations concentrate in a
    separate posterior ventral medial nucleus and are near-exclusive to it, which is the dispute the
    *Posterior / ventromedial-posterior thalamus* entry already records. Jones's compartmental
    account routes spinothalamic input into the matrix of this complex. **The two accounts are not
    reconciled here.**
  - **← primary somatosensory cortex** (corticothalamic feedback) and **← thalamic reticular
    nucleus** — **carries:** no stimulus content; the same **driver/modulator gate** declared at the
    lateral geniculate nucleus. **Fan-in:** unknown.
- **Outputs:**
  - **→ the primary somatosensory cortex, onto layers 3B and 4**, from the **parvalbumin core** — **carries:** the somatotopic
    cutaneous and proprioceptive payload, gated, not transformed, sorted onto its cortical targets
    by submodality: **proprioception → area 3a**, **cutaneous → area 3b**. Topographically
    organised — this is the edge that carries the map. **Fan-out:** unknown.
    *(Class 1 — laminar target and topography: Rausell et al. 1992; Jones 1998. Candidate.)*
  - **→ the primary somatosensory cortex and adjacent cortex, onto layer 1**, from the **calbindin matrix** — **carries:** the
    diffusely terminating stream, **not topographic** and not confined to one cortical area; the
    matrix cells can also be labelled retrogradely from motor cortex. Its payload is **owed**: what
    a non-topographic thalamic broadcast to layer 1 delivers, as a type with a range and a frame,
    is not established here. **Fan-out:** unknown.
    *(Class 1 — laminar target and diffuseness: Rausell et al. 1992; Jones 1998. Class 2 — the
    reading that this is a second edge rather than a variant of the first is Claude's, and it is
    what splits the entry's single output line in two. Candidate.)*
    **This split changes the edge's arity at the far end.** The primary somatosensory cortex entry
    declares one input onto layer 4; it now needs two, with different payloads and different
    laminar targets. The matching change is made there.
  - **→ the second somatosensory area and the parietal ventral area**, from the **ventral posterior inferior nucleus** and the
    ventral posterior superior territory — **carries:** **deep-receptor** signals from muscles and
    joints; **little if any cutaneous content**, which is why the second somatosensory fields get
    their cutaneous payload from cortex rather than from here. **Fan-out:** unknown.
    *(Class 1 — Disbrow et al. 2002, macaque. Candidate — awaiting Micky's verification.)*
- **Internal structure and internal data flow:**
  - **Parvalbumin core** (cytochrome-oxidase-rich) — large and medium relay cells; recipient of the
    medial and trigeminal lemniscus; projects to layers 3B and 4.
  - **Calbindin matrix** (cytochrome-oxidase-weak) — smaller relay cells; recipient of the
    spinothalamic and spinal trigeminal streams; projects to layer 1. **The matrix is not bounded by
    this region.** It runs uninterrupted from the ventral posterior medial and lateral nuclei into
    the ventral posterior inferior and basal ventral medial nuclei, and on into the anterior
    pulvinar, posterior and ventral lateral nuclei. **A compartment that crosses region boundaries
    cannot be expressed by this file's per-region edges**, and that is a finding about the file's
    representation, not only about the thalamus.
  - **Internal edge — medial lemniscal terminals → core relay cells: carries:** the driver payload;
    via triadic synapses with GABAergic presynaptic dendrites, so the transfer is locally
    inhibition-shaped rather than a simple relay. **Fan-in / fan-out:** unknown.
  - **Internal edge — spinothalamic terminals → matrix relay cells: carries:** the nociceptive and
    thermal payload; **no triads**. **Fan-in / fan-out:** unknown.
  - **Internal edge — local GABAergic interneurons → relay cells: carries:** inhibition, no content.
    **Species note:** interneuron density differs sharply — the rat ventral posterior complex has
    very few, primates have many, so a rodent-derived internal circuit does not transfer here.
    **Fan-in / fan-out:** unknown.
  *(Class 1 — Rausell et al. 1992; Rausell & Jones 1991; Ralston & Ralston 1994; interneuron species
  difference from Harris & Hendrickson 1987 and Price 1995, as cited in the ScienceDirect ventral
  posteromedial overview. Candidates — awaiting Micky's verification.)*
- **Neurons:** ~2.5M per hemisphere (best available, soft — the largest primary sensory relay, above
  the lateral and medial geniculate nuclei (~1.8–2.3M), its body-surface and proprioceptive afferent
  load exceeding the retina's or cochlea's). No separate core-versus-matrix count was found.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Primary somatosensory cortex (postcentral gyrus, isocortex)

- **Function:** four cytoarchitectonic areas, each a complete body map. **Area 3a** — proprioceptive
  core (limb, muscle and joint state), at the border with the primary motor cortex, receiving group
  Ia muscle-spindle afferents. **Area 3b** — cutaneous core (point and pressure, slowly- vs
  rapidly-adapting), the true primary, with the finest somatotopic map. **Area 1** — cutaneous
  secondary (texture and motion across the skin). **Area 2** — cutaneous-and-deep tertiary (size,
  shape, stereognosis), where cutaneous and deep/joint inputs converge. The somatotopic map is
  self-organising and highly plastic, reorganising after input change. Thalamic input is a minority
  of long-range input (~32% of layer-1 long-range input); most input is intracortical.
- **The serial/parallel organisation is disputed, and the dispute is load-bearing here** because it
  determines whether the four areas form a chain or four partly independent lines.
  **All four areas receive direct thalamic input** — that is not in dispute. What is disputed is
  whether the later areas can work without the earlier ones. Ablation studies in macaque and
  marmoset found that removing area 3b abolishes cutaneous responsiveness in area 1 and in the
  second somatosensory cortex, which reads as a serial chain. Reversible inactivation with
  lidocaine, in cat, rabbit and marmoset, found second-somatosensory responses substantially
  survive, which reads as parallel; and parallel thalamic activation of the first and second
  somatosensory areas is reported in prosimian primates and tree shrews. **The methods disagree,
  and irreversible ablation and reversible inactivation are not measuring the same thing.** The
  entry keeps both intracortical and direct thalamic edges rather than choosing.
  *(Class 1 — serial: Pons et al. 1987, macaque ablation; Garraghty et al. 1990. Parallel: Rowe
  et al. 1996, reversible lidocaine inactivation; Garraghty et al. 1991, prosimian and tree shrew.
  Class 2 — the reading that method explains the disagreement is Claude's. Candidates — awaiting
  Micky's verification.)*
- **Inputs:**
  - **← ventral posterior thalamus, onto layers 3B and 4**, from its **parvalbumin core** (a **minority** of
    long-range input — most input is intracortical) — **carries:** somatotopic cutaneous intensity,
    slowly- and rapidly-adapting, to **area 3b** and **area 1**; and proprioceptive configuration to
    **area 3a** and **area 2**. Topographic, point-to-point. **Fan-in:** unknown.
  - **← ventral posterior thalamus, onto layer 1**, from its **calbindin matrix** — **carries:** the diffusely
    terminating, **non-topographic** stream; payload **owed** at both ends. Terminates on apical
    tuft dendrites belonging to cells whose somata sit in layers 2/3 and 5; no second internal edge
    is written for the propagation to those somata. **Fan-in:** unknown.
    *(The ventral posterior thalamus entry declares core and matrix as two outputs with different
    laminar targets. Class 1 — Rausell et al. 1992, monkey. Candidate.)*
- **Outputs:**
  - **→ the second somatosensory area and the parietal junction**, along the intracortical chain **3b → 1 → 2** — **carries:**
    a rising code: **area 3b** point pressure and adaptation rate; **area 1** texture and motion
    *across* the skin; **area 2** size, shape and stereognosis — cutaneous and deep/joint input
    **combined**, which is the first place the payload describes an *object* rather than the skin.
    **The modality split is preserved along the way:** cutaneous reaches the second somatosensory
    cortex via areas 3b and 1, deep via areas 3a and 2, as parallel channels rather than one merged
    stream. **Fan-out:** unknown.
    *(Class 1 — modality-specific parallel channels to the second somatosensory cortex:
    J Neurophysiol 68:518, 1992, rhesus macaque. Candidate.)*
  - **→ the primary motor cortex and → premotor cortex**, from **area 3a** — **carries:** limb and joint
    configuration — the feedback signal that closes the sensorimotor loop. **A payload type, not
    just a label:** single-unit recording during controlled digit movement in macaque distinguishes
    **single-digit position-scaled**, **multi-digit position-scaled**, and **posture-selective**
    cells, so what leaves is a graded position variable per digit plus a categorical posture signal,
    not an undifferentiated "proprioception." **Fan-out:** unknown.
    *(Class 1 — Kim et al. 2015, macaque. Candidate.)*
    **The two far ends differ in status.** The primary motor entry declares an input from area 3a and
    agrees. **The premotor entry does not declare this input at all** — its Inputs name posterior
    parietal area 5 and the intraparietal areas, not this one. **Owed as a cross-file edit at the
    premotor entry (file 11).** **No → area 2 limb belongs on this line**: that edge is *internal*
    rather than inter-region and is written as such under Internal structure. Carrying it in Outputs
    would declare a region-crossing transfer that does not cross a region boundary.
  - **→ superior parietal area 5**, principally from **area 2**, with **area 3a** — **carries:** limb
    configuration and tactile object properties, in a **skin / joint** frame — the frame that is
    re-expressed downstream. **Fan-out:** unknown.
    *(Two-ended; the superior parietal area 5 entry declares it. Candidate.)*
  - **→ the insula**, from **area 3a**, and **→ posterior parietal cortex**, from areas 1 and 2 —
    **payload unknown — owed.** **Fan-out:** unknown.
  - **→ ventral posterior thalamus** (corticothalamic feedback) — **carries:** no content; the gate. **Fan-out:**
    unknown.
  - **→ dorsal column nuclei** (corticocuneate, from the hand regions of areas 3b, 3a and 1/2;
    **bilateral** — both the contralateral and the ipsilateral nucleus) — **carries:** no new
    stimulus content; a **movement-contingent gain signal** that attenuates transmission through
    the first relay during voluntary movement, organised as a **central zone of facilitation with a
    surrounding zone of inhibition**. **Fan-out:** unknown. *(Class 1 — J Comp Neurol 529:1401,
    2021, New World monkey; Cell Reports 43:113827, 2024, macaque; Canedo 1999, cat. Candidate —
    awaiting Micky's verification. Two-ended; the dorsal column nuclei entry declares this edge on
    its Inputs side.)*
- **Internal structure and internal data flow:** the four areas are the sub-elements, each a
  complete body map, arranged anterior-to-posterior across the postcentral gyrus (3a at the motor
  border, then 3b, 1, 2). Within areas 3b and area 1 the map is further divided into **modules —
  discrete representations of individual digits**, resolvable in imaging and separately affected by
  deafferentation.
  - **Internal edge — area 3b → area 1: carries:** the cutaneous payload, elaborated from point
    pressure toward texture and motion across the skin. **Fan-in / fan-out:** unknown.
  - **Internal edge — area 1 → area 2: carries:** the cutaneous payload, elaborated toward size and
    shape. **Fan-in / fan-out:** unknown.
  - **Internal edge — area 3a → area 2: carries:** the deep/proprioceptive payload, converging in
    area 2 with the cutaneous stream — the transfer that makes stereognosis possible.
    **Fan-in / fan-out:** unknown.
  - **Internal edge — area 3b → area 2: carries:** cutaneous input, direct. **Fan-in / fan-out:**
    unknown.
  *(Class 1 — inter-areal projections: Kaas 1983, and the review lineage cited above; digit modules:
  PMC5041163, macaque. Candidates — awaiting Micky's verification.)*
- **Contested — the naming of the thalamic source.** This entry and the ventral posterior thalamus entry use the
  **ventral posterior lateral / medial / inferior / basal ventral medial** division. A parallel
  literature (Kaas and colleagues) divides the same territory into a **ventroposterior** nucleus
  relaying cutaneous slowly- and rapidly-adapting signals to areas 3b and 1, a **ventroposterior
  superior** nucleus relaying muscle-spindle signals to areas 3a and 2, and a **ventroposterior
  inferior** nucleus relaying spinothalamic signals to the second somatosensory and parietal ventral
  areas. **The two schemes are not a relabelling of each other** — they cut the proprioceptive relay
  out as a separate nucleus. Recorded as contested; the edges above carry the function either way.
  *(Class 1 — Kaas scheme, Springer 1993. Candidate.)*
- **Neurons:** area 3a ~15M; area 3b ~25M; area 1 ~20M; area 2 ~20M — per
  hemisphere (best available, soft).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Second somatosensory area, with the parietal ventral and ventral somatosensory areas (isocortex)

- **Function:** tactile object identity and stereognosis — texture, shape, material, invariant to
  the exact contact point. **The name covers more than one field.** The parietal operculum, on the
  upper bank of the lateral sulcus, holds at least three: the **second somatosensory area**
  caudally, the **parietal ventral area** rostral to it, and the **ventral somatosensory area**
  deeper in the sulcus, its inner edge adjoining insular cortex. The second somatosensory and
  parietal ventral areas are **mirror-symmetric body maps joined at the hand, foot and face
  representations**, with the face near the entrance to the sulcus and the hands and feet deeper.
  In human they occupy parts of Brodmann areas 40 and 43. *(Class 1 — field division and mirror
  symmetry: Disbrow et al. 2000, human; human cytoarchitectonic subdivision of the parietal
  operculum: Eickhoff et al. 2006. Candidates — awaiting Micky's verification.)*
- **Receptive fields are large and frequently bilateral**, spanning multiple digits, the whole hand,
  or both hands — the first place in this pathway where the two body sides converge. Neurons here
  are also **less modality-specific** than in the primary somatosensory cortex.
  *(Class 1 — Krubitzer & Kaas 1990, macaque; Krubitzer et al. 1995, macaque; Disbrow et al. 2001,
  human. Candidate.)*
- **Inputs:**
  - **← the primary somatosensory cortex** (cutaneous via areas 3b and 1; deep via areas 3a and 2 — **two parallel channels, not
    one merged stream**) — **carries:** texture, shape, size, and contact configuration,
    somatotopic. **Fan-in:** unknown.
    **Whether this edge is necessary for this region to respond is disputed** — macaque ablation of
    area 3b abolishes cutaneous responsiveness here, while reversible lidocaine inactivation in cat,
    rabbit and marmoset leaves much of it intact, and direct thalamic activation of this region is
    reported in prosimian primates and tree shrews. The dispute is recorded in full at the primary somatosensory entry.
    *(Class 1 — as cited at the primary somatosensory entry. Candidate — awaiting Micky's verification.)*
  - **← ventral posterior thalamus**, from the **ventral posterior inferior nucleus** and the ventral posterior
    superior territory, and **← the anterior pulvinar** — **carries:** **deep-receptor** signals
    from muscles and joints, not cutaneous. **This is the entry's correction:** these fields receive
    **little if any cutaneous input from the thalamus**, so their cutaneous payload must arrive
    through the cortical edge above, while their thalamic edge carries the deep stream. An account
    that treats this region as a second cutaneous relay fed from the thalamus has the modality
    backwards. **Fan-in:** unknown.
    *(Class 1 — Disbrow et al. 2002, macaque. Class 2 — the reading that this corrects the entry's
    picture is Claude's. Candidate.)*
    **The anterior-pulvinar limb is declared at this end only.** The pulvinar entry declares its
    outputs as "multiple visual, parietal and temporal cortical areas" and **names no somatosensory
    target**, so this edge has no producer end. **Owed as a
    cross-file edit at the pulvinar entry (file 12), or withdraw the limb.** It is also a second
    endpoint on a shared line, so **splitting this line in two is owed** — a thalamic relay and a
    higher-order nucleus are not one source.
  - **← the contralateral second somatosensory area, area 3b and area 7b** (callosal) — **carries:**
    the opposite side's tactile payload, which is what makes the bilateral receptive field. The
    parietal ventral area's callosal connections are **restricted to its own homologue**, while the
    second somatosensory area's are not — the two fields differ in how much of the other hemisphere
    they see. **Fan-in:** unknown.
    *(Class 1 — Disbrow et al. 2003, macaque. Candidate.)*
- **Outputs:**
  - **→ area 7b (the supramarginal gyrus)** — **carries:** the object-level tactile payload —
    texture, shape and material, contact-point invariant. **The far end agrees and names this
    area**: the supramarginal gyrus entry declares an input from this area and areas 2 and 5, carrying tactile object
    identity and body configuration. Untyped there. **Fan-out:** unknown.
  - **→ the anterior intraparietal area** — **carries:** tactile object identity and contact state.
    **Two-ended** — the anterior intraparietal entry names this area explicitly among its inputs.
    Payload transcribed from that end.
    **Fan-out:** unknown.
  - **→ posterior parietal cortex** (remainder, beyond the two named above) — **carries:** the
    object-level tactile payload. **This endpoint is a class**; the two members that resolve are
    written as their own edges above. **Owed: name any others, or withdraw.** **Fan-out:** unknown.
  - **→ premotor cortex**, principally from the **parietal ventral area** — **carries:** tactile and
    proprioceptive information in a form usable for reaching and grasping. **Payload otherwise
    unknown — owed.** **Declared at this end only:** the premotor entry's Inputs name posterior
    parietal area 5 and the grasp/reach intraparietal areas, prefrontal cortex, and the motor
    thalamus — not this area. **Owed as a cross-file edit at the premotor entry (file 11).**
    **Fan-out:** unknown.
  - **→ the parietal rostroventral area** — **carries:** payload **owed**. Split from the line
    above; the far end has no entry in any file checked here, so it is unchecked. **Fan-out:** unknown.
  - **→ the insula**, from the **ventral somatosensory area**, whose inner edge adjoins it —
    **payload unknown — owed.** **Fan-out:** unknown.
  - **→ the primary somatosensory cortex** (reciprocal, principally to area 3b) — **carries:** feedback; no new stimulus content.
    **Payload otherwise unknown — owed.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** three fields, described above, plus the
  mirror-symmetric map arrangement.
  - **Internal edge — parietal ventral area ↔ second somatosensory area: carries:** tactile payload
    across the seam where the two maps join at the hand, foot and face. Reciprocal and dense.
    **Fan-in / fan-out:** unknown.
  - **Internal edge — second somatosensory area → ventral somatosensory area: carries:** payload
    **owed**; the deeper field is the least characterised of the three. **Fan-in / fan-out:**
    unknown.
  *(Class 1 — dense interconnection of the two fields: Disbrow et al. 2003, macaque. Class 2 — the
  direction assigned to the second internal edge is Claude's reading and is weakly supported.
  Candidates.)*
- **A finding about the file's stream model, recorded because it cuts against it.** The authors of
  the connection study conclude that these patterns suggest the somatosensory system **may not be
  segregated into two separate streams** in the way hypothesised for vision — the fields' cortical
  and thalamic connections overlap rather than sorting into a "what" and a "where." This file
  carries an explicit dorsal/ventral split for vision. **Whether the same split is imported into
  touch is a claim this entry does not support.** *(Class 1 — Disbrow et al. 2003, discussion.
  Candidate.)*
- **Neurons:** unknown. **Synapses:** unknown. **Axons:** unknown.
  **Grey-matter volume:** unknown. **White-matter volume:** unknown. **Myelination:** unknown.

## Superior parietal area 5 — areas PE, PEa and PEc (isocortex)

- **Function:** limb position, body schema, and the coordinates in which a reach is specified.
  **Three architectonic subdivisions, and they are not interchangeable:** **PE** on the gyral
  convexity, **PEa** on the medial bank of the intraparietal sulcus, and **PEc** caudally. In human
  the corresponding territory is **Brodmann area 5**, lateral and medial superior parietal cortex
  including the medial part of the intraparietal sulcus, overlapping all three; human subareas 5L
  and 5m correspond to PE and 5Ci to the cingulate area PEci. Human area 5 is distinguished by a
  dense concentration of **SMI-32-immunoreactive pyramidal neurons in layers III and V**.
  *(Class 1 — macaque subdivisions: Pandya & Seltzer 1982. Human correspondence: Scheperjans et al.
  2005; Saleem & Logothetis 2012. Candidates — awaiting Micky's verification.)*
- **It is not a purely sensory area.** Movement-related activity in area 5 neurons **persists in the
  absence of sensory stimulation**, so it is internally generated rather than driven, and the area
  is active in movement *preparation*. *(Class 1 — Seal et al. 1982, awake macaque; Burbaud et al.
  1991. Candidate.)*
- **The reference frame is contested and this entry does not assert one side of it.** Typing it as
  "reach coordinates in a body-centered frame" would pick a side. The reported frames are **body-,
  shoulder- and hand-centred across different studies**, and in area PE specifically a memorised target's
  distance is encoded **relative to the initial hand position rather than to the body** — a
  hand-centred frame. **Recorded as contested; the file does not pick a side.** This matters more
  here than a nomenclature dispute would, because on this file's payload rule the **coordinate frame
  is part of the payload**, so an unsettled frame is an unsettled payload.
  *(Class 1 — hand-centred encoding of target distance: Ferraina et al. 2009, macaque; the
  body/shoulder/hand spread: Ferraina & Bianchi 1994; Lacquaniti et al. 1995; Kalaska 1996; Graziano
  et al. 2000; Bremner & Andersen 2012. Class 2 — the inference that this unsettles the payload is
  Claude's. Candidate.)*
- **Inputs:**
  - **← the primary somatosensory cortex** (principally **area 2**, with area 3a) — **carries:** limb configuration and tactile
    object properties, in a **skin / joint** frame. **Fan-in:** unknown.
  - **← the medial bank of the intraparietal sulcus** (including the medial intraparietal area),
    **the parietal opercular areas PGop and PFop, and the retroinsular area** — **carries:** payload
    **owed**; these are afferents demonstrated by tracer injection whose content has not been typed
    here. **Fan-in:** unknown. **The medial intraparietal limb has no producer end**: that entry's
    Outputs declare only a projection to dorsal premotor area F2 and thence to primary motor cortex. **Owed as a cross-file edit at
    that entry (file 6).** This line also names four sources at once and **splitting it is owed**.
  - **← the precuneus**, from its anterior sensorimotor sector — **carries:** reach and
    body-configuration signals, body-centred. **Two-ended** — that entry calls it "the one edge out of
    this entry whose payload *can* be written." **Fan-in:** unknown.
    *(Class 1 — Bakola et al. 2013, macaque. Candidate.)*
  - **← the primary motor cortex, the supplementary motor area, and caudal dorsal premotor cortex** — **carries:** motor
    and premotor signals, plausibly including an efference copy; **payload owed — the studies
    establish the projection, not its content.** **Fan-in:** unknown.
    *(Class 1 — Bakola et al. 2013, as above. Class 2 — the efference-copy reading is Claude's and
    is not established. Candidate.)*
  - **← the posterior cingulate area PEci and cingulate areas 23 and 24** — **payload unknown —
    owed.** **Fan-in:** unknown. For **PEc** this is a substantial share: about 15% of its labelled
    afferent neurons lie in PEci and a further 10% elsewhere on the medial surface.
    *(Class 1 — Bakola et al. 2010, macaque. Candidate.)*
  - **← gaze-position signals**, reaching PEc and PEa — **carries:** eye position, and for PEc the
    **interaction** of gaze with hand position rather than either alone. **Fan-in:** unknown.
    *(Class 1 — eNeuro 9:ENEURO.0362-21, 2022, macaque. Candidate.)*
- **Outputs:**
  - **→ dorsal premotor cortex** (reach) — **carries:** limb position and the reach specification,
    in a frame that is **contested** as recorded above. The payload change across this region is the
    **frame**, not the content. **Fan-out:** unknown.
  - **→ the primary motor cortex** (reciprocal with area PE) — **carries:** limb state for the ongoing command.
    **Payload otherwise unknown — owed.** **Fan-out:** unknown.
    *(Class 1 — Johnson et al. 1996, macaque. Candidate.)*
  - **→ the medial intraparietal area** — **carries:** the limb state against which visual targets
    must be expressed. **The far end declares it and names this area** — its Inputs name the primary
    somatosensory cortex, superior parietal area 5, the primary motor cortex and the medial motor fields — but **types the frame as body-centred**, which this
    entry has just withdrawn as contested. **The two ends disagree about the frame, and on this
    file's payload rule the frame is part of the payload, so this is a payload disagreement and not
    a wording one.** Not repaired here. **Fan-out:** unknown.
  - **→ the anterior intraparietal area** — **carries:** the same limb state. **Declared at this end
    only:** that entry's Inputs name the caudal and lateral intraparietal areas, the lower-bank
    superior temporal sulcus, the second somatosensory area, the ventral intraparietal area, and prefrontal areas 46 and 12 —
    not this one. **Owed as a cross-file edit at that entry (file 6).** **Fan-out:** unknown.
  - **→ the ventral intraparietal area** — **carries:** the same limb state. **Declared at this end
    only** — that entry's Inputs name no superior parietal source.
    **Owed as a cross-file edit at that entry (file 4).** **Fan-out:** unknown.
  - **→ the lateral intraparietal area** — **carries:** the same limb state. **Declared at this end
    only**, same status as the ventral intraparietal edge above. **Owed at file 4.** **Fan-out:**
    unknown.
  - **→ the supramarginal gyrus** — **carries:** body configuration. **Two-ended**: that entry's
    Inputs name the second somatosensory area and areas 2 and 5. **Fan-out:** unknown.
  - **→ the precuneus** — **carries:** body configuration and spatial layout, body-centred.
    **Two-ended** — the precuneus entry names "superior parietal lobule (areas 5/7)" among its
    inputs. Note the same frame disagreement as the medial intraparietal edge: that end says body-centred and this entry holds
    the frame contested. **Fan-out:** unknown.
- **Internal structure and internal data flow:** the three subdivisions form an **anterior-to-caudal
  functional gradient**, and the gradient is the entry's structural claim.
  - **PE** — most sensitive to limb **proprioception**; encodes arm position with the most
    independence from gaze.
  - **PEa** (medial bank of the intraparietal sulcus) — proprioceptive and kinematic, heavily
    interconnected with the medial intraparietal area; the reach-planning end.
  - **PEc** — sensitive to **proprioception and gaze together**, linked to lower-limb motor and
    premotor representations, to vestibular cortex, and to areas analysing optic flow. Its proposed
    role is **locomotion and limb coordination in the environment**, not reaching alone.
  - **Internal edge — PEc → PE: carries:** multimodal limb and gaze signals feeding the
    proprioceptive representation. **Fan-in / fan-out:** unknown.
    *(Class 1 — Marconi et al. 2001, macaque. Candidate.)*
  - **Internal edge — PE → PEa and the medial intraparietal area: carries:** proprioceptive and kinematic limb state for reach
    planning. **Fan-in / fan-out:** unknown.
  *(Class 1 — gradient: eNeuro 9:ENEURO.0362-21, 2022; PEc connections and role: Bakola et al. 2010. Candidates.)*
- **Neurons:** ~25M per hemisphere (best available, soft). No per-subdivision count found.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Primary motor cortex (area 4, isocortex)

- **Function:** primary motor output — corticospinal drive to muscles; a
  somatotopic motor map and movement primitives. Agranular cortex (thin/absent
  layer 4, layer-5 pyramidal / Betz-cell heavy) because it is output-dominated.
- **Inputs:**
  - **← the primary somatosensory cortex (area 3a)** — **carries:** proprioceptive and cutaneous feedback — limb configuration and
    contact, the consequence of the last command. **Fan-in:** unknown.
  - **← premotor** — **carries:** the planned action — a movement, already sequenced and shaped, not
    yet a muscle command. **Fan-in:** unknown. **The far end declares it** — the premotor entry's
    Outputs name this area — and is untyped there. **Owed at file 11: type it.**
  - **← superior parietal area 5** (reciprocal with area PE) — **carries:** limb position and the reach
    specification, in a **contested** reference frame — reported as body-, shoulder- and
    hand-centred across studies, and hand-centred for target distance in area PE. The dispute is
    recorded in full at the superior parietal area 5 entry. **Fan-in:** unknown.
    *(Class 1 — Johnson et al. 1996, macaque. Candidate — awaiting Micky's verification.
    Two-ended.)*
  - **← thalamus (ventral anterior / ventral lateral)** — **carries:** the basal-ganglia *selection* (which action is released)
    and the cerebellar *correction* (how it is shaped), combined on one relay. **Fan-in:** unknown.
    **The far end declares this edge and names this area**, but untyped — its Outputs slot reads
    primary motor, premotor and supplementary motor cortex as prose, with no typed payload and no fan-out. **Owed as a cross-file edit at
    the ventral anterior / ventral lateral entry (file 12): type it.**
- **Outputs:**
  - **→ muscles**, via the corticospinal tract — **carries:** the motor command — somatotopic drive
    to muscles and movement primitives. **The consumer at the far end of this edge is not in this
    map**: the muscles, the skeleton, and their dynamics have no entry, so this edge's payload is
    declared with no one to receive it. It is the mirror image of the retina's input edge, and it is
    the map's largest open boundary on the output side. **Fan-out:** unknown.
  - **→ (returning through the world) → the primary somatosensory cortex** — **carries:** the movement's *consequence*, read back
    through proprioception; the loop closes through the body, not inside the brain. **Fan-out:**
    not applicable.
  - **→ thalamus (ventral anterior / ventral lateral)** (corticothalamic, reciprocal) — **carries:** payload **owed**. **Two-ended**: the
    ventral anterior / ventral lateral entry lists "reciprocal motor cortex" among its inputs.
    **Payload owed at both ends.** **Fan-out:** unknown.
  - **→ dorsal column nuclei** (corticocuneate, from the forelimb region) — **carries:** no new
    stimulus content; the same movement-contingent gain signal the primary somatosensory cortex declares, arriving on the same
    target. Its distinctness from the somatosensory limb is **owed** — the retrograde study labelled both, and
    whether they carry the same or different content is not established. **Fan-out:** unknown.
    *(Class 1 — J Comp Neurol 529:1401, 2021, New World monkey. Candidate. Two-ended.)*
- **Internal structure and internal data flow:** *(**Nothing here is verified for the source.**)*

  **Laminar sub-elements: seven, not eight, and that is this entry's structural fact.** This area
  is **agranular** — layer 4 is thin or absent — so the set is **1, 2, 3, 5a, 5b, 6a, 6b**, with
  layer 5 heavy in large pyramidal and Betz cells because the area is output-dominated. Taken from
  this entry's own Function field, which already states it. *(Class 3.)*

  **Internal edges: owed, and the file's standard laminar block may not be copied here.** Every
  other cortical entry in the source carries the same Class-3 set — **4 → 2/3**, **2/3 → 5a and
  5b** with reciprocal **5a → 2/3**, **6a → 4** and **6a → 5a**, **6b → 6a**, within-sub-element
  recurrence in 4 and 2/3. **Three of those edges terminate on or leave from layer 4, which this
  entry says is thin or absent**, so transcribing the block would assert a circuit the entry's own
  Function denies. It is therefore **not** written, and the internal edges read **owed**. This is a
  finding about the boilerplate as much as about this area: a laminar set copied across entries is
  a Class-3 claim that has to be checked against each entry's own laminar description, and here it
  fails. *(Class 2 — the incompatibility is Claude's reading of the entry's own Function statement,
  offered to be checked.)*

  **The scope of this exception, recorded identically in five files.**
  The file's standard Class-3 laminar block — **1, 2, 3, 4, 5a, 5b, 6a, 6b** with **4 → 2/3**,
  **2/3 → 5a and 5b**, **6a → 4**, **6a → 5a**, **6b → 6a** and within-sub-element recurrence — is
  **not a default. It is a claim about granular isocortex**, and three of its edges route through
  layer 4. **Nine entries across five files cannot take it**: primary motor cortex (file 5,
  agranular throughout); the temporal pole (file 7, agranular medially on a gradient); the
  hippocampal formation (file 8, three-layered allocortex); the cerebellar cortex (file 10,
  three-layered and not isocortex at all); and five entries in the frontal lobe (file 11) — premotor
  cortex, Broca's area, the right inferior frontal gyrus, the orbitofrontal / ventromedial entry and
  the anterior cingulate. **They fail it in four different ways** — uniformly agranular, agranular
  across a gradient, agranular across an internal border, and not isocortex — **so a single
  exception clause would not cover them.** **Owed at the design file: state where the block is
  defined that it applies to granular isocortex only**, rather than leaving each entry to discover
  the incompatibility on its own.


  **Tangential sub-elements: owed.** The Function field asserts a somatotopic motor map and
  movement primitives; whether either is a compartmentation that an edge could terminate on, or a
  continuous map of the kind recorded at the anterior inferotemporal cortex, is not established
  here.
- **Neurons:** ~30M per hemisphere (best available, soft).
- **Synapses:** unknown. **Axons:** corticospinal tract (count unknown).
  **Grey-matter volume:** unknown. **White-matter volume:** unknown.
  **Myelination:** unknown.

---

---

## References

*(Every line below is a **candidate** awaiting Micky's verification; none is verified.)*

**How to read a line.** A line **without** an **owed** mark was taken from a publisher or journal
record that was opened. A line marked **owed** was **not searched**, and whatever it carries —
journal, volume, page, year, species, method — is transcribed from this file's own citing lines and
from nothing else. That is the file gathering what it already says in one place, so that the search,
when it is run, has a starting point. **It is not a reference, and it is not evidence that anything
was opened.**

**50 distinct keys, 74 mentions. 3 carry a searched reference; 47 owed.**

**The short form inline is the key here, exactly.** An entry cites *Bakola et al. 2010*; the
authors, journal, volume, page, year and method sit on that key's line below and nowhere else.
Species stays inline, because several entries argue from it — that a figure is rat and not human,
that internal edges are typed from cat physiology — and an argument cannot be read with its premise
on another page.

**Four keys are malformed as extracted and cannot be searched until they are repaired at the citing
line.** Two are unattributed web overviews rather than papers — the *ScienceDirect dorsal column
nuclei overview* and the *ScienceDirect ventral posteromedial overview*. Two name a book or a scheme
without a locatable paper: *Tracey & Waite, The Rat Nervous System*, cited second-hand through
another work at both citing lines and carrying no edition or chapter, and the *Kaas scheme, Springer
1993*, which gives a chapter title and a publisher and no author, editor or page.

**One key is doing double duty and the file marks the problem itself.** *Rausell & Jones 1991* names
**two** papers — J Neurosci 11:210 and 11:226 — written as one key. It needs to become two before
either can be checked.

**Eight keys are written as a journal, volume and page with no author** — *Cell Reports 43:113827,
2024*, *J Comp Neurol 529:1401, 2021*, *PNAS 120:e2222076120, 2023* and the rest. For these the
volume and page **are** the short form: they are what pins one paper, so they stay inline rather
than moving down here. They are a different case from the four above, which have no far end at all.

**Two keys sit under the file's own examination marks and the reference section does not disturb
them.** The internal edges of the dorsal column nuclei are typed from *Canedo 1999*, cat physiology,
and the cuneate's 4 mm length rests on *Tracey & Waite*, a rat figure the entry already flags as not
a human number. Both are recorded here as keys like any other; their standing as evidence is a
matter for the citing lines, where it is already marked.

- **Bakola et al. 2010** — Bakola, Gamberini, Passarelli et al., *Cerebral Cortex* 20:2592, 2010.
  Macaque; retrograde tracing into area PEc. **owed.**
- **Bakola et al. 2013** — Bakola, Passarelli, Gamberini et al., *Journal of Neuroscience* 33:6648,
  2013. Macaque; retrograde tracing into architectonically defined area PE. **owed.**
- **Brain Struct Funct 2025** — Identification and characterization of the thalamic ventral
  posterior complex by 11.7 T ex vivo diffusion tensor imaging. *Brain Structure and Function*,
  2025; doi 10.1007/s00429-025-02915-7. **Human**; ex vivo diffusion tensor imaging at 11.7 tesla.
  *(Springer publisher record. **The author list is owed** — the record was reached through its own
  reference list rather than its masthead.)*
- **Bremner & Andersen 2012** — **owed.** The citing line carries nothing beyond the key.
- **Burbaud et al. 1991** — **owed.** The citing line carries nothing beyond the key.
- **Canedo 1999** — Canedo, *Physiology* 14:231, 1999. Cat. **owed.**
- **Cell Reports 43:113827, 2024** — *Cell Reports* 43:113827, 2024. Macaque; single-unit recording
  during voluntary hand movement. **owed.**
- **Del Fiacco et al. 2013** — Del Fiacco, Quartu, Serra et al., *Brain Structure and Function*, doi
  10.1007/s00429-013-0625-4, 2013. **Human** medulla; immunohistochemistry with three-dimensional
  reconstruction. **owed.**
- **Disbrow et al. 2000** — Disbrow, Roberts & Krubitzer, *Journal of Comparative Neurology* 418:1,
  2000. **Human**; functional imaging. **owed.**
- **Disbrow et al. 2001** — **owed.** **Human**; the citing line carries nothing beyond the key and
  the species.
- **Disbrow et al. 2002** — Disbrow, Litinas, Recanzone, Slutsky & Krubitzer, *Somatosensory and
  Motor Research* 19:31, 2002. Macaque; thalamocortical tracer injections into physiologically
  identified fields. **owed.**
- **Disbrow et al. 2003** — Disbrow, Litinas, Recanzone, Slutsky & Krubitzer, *Journal of
  Comparative Neurology* 462:382, 2003. Macaque; tracer injections, ipsilateral and contralateral
  labelling. **owed.**
- **Eickhoff et al. 2006** — Eickhoff et al., *Cerebral Cortex* 16:254, 2006. **Human**;
  cytoarchitectonic subdivision of the parietal operculum. **owed.**
- **eNeuro 9:ENEURO.0362-21, 2022** — *eNeuro* 9:ENEURO.0362-21, 2022. Macaque; single-unit
  recording during a fixation-to-reach task. **owed.**
- **Ferraina & Bianchi 1994** — **owed.** The citing line carries nothing beyond the key.
- **Ferraina et al. 2009** — Ferraina, Brunamonti, Giusti et al., *Journal of Neuroscience*
  29:11461, 2009. Macaque. **owed.**
- **Garraghty et al. 1990** — Garraghty, Florence & Kaas, *Brain Research* 528:165, 1990. **owed.**
- **Garraghty et al. 1991** — Garraghty et al., *Journal of Comparative Neurology* 311:289, 1991.
  Prosimian primate and tree shrew. **owed.**
- **Graziano et al. 2000** — **owed.** The citing line carries nothing beyond the key.
- **Harris & Hendrickson 1987** — **owed.** Reached only as cited in the *ScienceDirect ventral
  posteromedial overview*.
- **J Comp Neurol 529:1401, 2021** — *Journal of Comparative Neurology* 529:1401, 2021. New World
  monkey; retrograde tracing. **owed.**
- **J Neurophysiol 106:2233, 2011** — *Journal of Neurophysiology* 106:2233, 2011. Macaque;
  extracellular recording, independent Poisson stimulus trains on the median, ulnar, deep radial and
  superficial radial nerves. **owed.**
- **J Neurophysiol 68:518, 1992** — *Journal of Neurophysiology* 68:518, 1992. Rhesus macaque.
  **owed.**
- **Johnson et al. 1996** — **owed.** Macaque.
- **Jones 1998** — Jones, *Neuroscience* 85:331, 1998. Review. **owed.**
- **Kaas 1983** — Kaas, *Physiological Reviews* 63:206, 1983. **owed.**
- **Kaas scheme, Springer 1993** — "Parallel and Serial Processing in the Somatosensory System,"
  Springer, 1993. **owed** — a chapter title and a publisher, with no author, editor or page.
- **Kalaska 1996** — **owed.** The citing line carries nothing beyond the key.
- **Kim et al. 2015** — Kim, Callier, Tabot, Gaunt, Tenore & Bensmaia, 2015. Macaque; controlled
  individual digit movement. **owed.**
- **Krubitzer & Kaas 1990** — **owed.** Macaque; single-unit recording.
- **Krubitzer et al. 1995** — **owed.** Macaque; single-unit recording.
- **Lacquaniti et al. 1995** — **owed.** The citing line carries nothing beyond the key.
- **Loutit et al. 2021** — Loutit, Vickery & Potas, *Journal of Comparative Neurology* 529:187–220,
  2021. Review of dorsal column nuclei organisation and connectivity. **owed.**
- **Marconi et al. 2001** — **owed.** Macaque.
- **Maslany et al. 1991** — **owed.** Rat.
- **Pandya & Seltzer 1982** — Pandya & Seltzer, *Journal of Comparative Neurology* 204:196, 1982.
  Macaque. **owed.**
- **PMC5041163** — **owed.** Macaque; intrinsic-signal imaging after dorsal column lesion. A PubMed
  Central identifier rather than a citation — authors, title, journal and year are all still to be
  read off the record.
- **PNAS 120:e2222076120, 2023** — *Proceedings of the National Academy of Sciences*
  120:e2222076120, 2023. Macaque, owl monkey, squirrel monkey and galago; serial histology.
  **owed.**
- **Pons et al. 1987** — Pons, Garraghty, Friedman & Mishkin, *Science* 237:417, 1987. Macaque;
  ablation. **owed.**
- **Price 1995** — **owed.** Reached only as cited in the *ScienceDirect ventral posteromedial
  overview*.
- **Ralston & Ralston 1994** — **owed.** Monkey; electron microscopy.
- **Rausell & Jones 1991** — **Two papers under one key, and only the first was located.** Rausell,
  E. & Jones, E.G. (1991). Histochemical and immunocytochemical compartments of the thalamic VPM
  nucleus in monkeys and their relationship to the representational map. *Journal of Neuroscience*
  11(1): 210–225. **Monkey.** *(Located in a publisher reference listing — a secondary listing. Note
  the page range ends at 225, where the file writes 210 for the first paper and 226 for the
  second.)* The companion at 11:226 was not located and is **owed**; the key must be split before
  either can be checked.
- **Rausell et al. 1992** — Rausell, E., Bae, C.S., Viñuela, A., Huntley, G.W. & Jones, E.G. (1992).
  Calbindin and parvalbumin cells in monkey VPL thalamic nucleus: distribution, laminar cortical
  projections, and relations to spinothalamic terminations. *Journal of Neuroscience* 12(10):
  4088–4111; doi 10.1523/JNEUROSCI.12-10-04088.1992; PubMed 1328563; PMC6575950. **Monkey.**
  Cytochrome-oxidase histochemistry with parvalbumin and 28 kDa calbindin immunocytochemistry, plus
  anterograde and retrograde tracing. *(Society for Neuroscience publisher record and PubMed
  Central.)* Note for the internal-structure slot of the ventral posterior nuclear complex: the
  abstract states that parvalbumin cells and parvalbumin-positive lemniscal terminations are
  **confined** to the oxidase-rich compartment, but that **calbindin cells occur in both**
  compartments — so the file's core/matrix pairing is tighter on the parvalbumin side than on the
  calbindin side.
- **Rowe et al. 1996** — Rowe et al., *Clinical and Experimental Pharmacology and Physiology* 23,
  1996. Cat, rabbit and marmoset; reversible lidocaine inactivation. **owed.**
- **Saleem & Logothetis 2012** — **owed.** The citing line carries nothing beyond the key.
- **Scheperjans et al. 2005** — **owed.** **Human**; cytoarchitecture.
- **ScienceDirect dorsal column nuclei overview** — **owed** — an unattributed web overview rather
  than a paper, cited second-hand for a *Tracey & Waite* figure.
- **ScienceDirect ventral posteromedial overview** — **owed** — an unattributed web overview rather
  than a paper, cited second-hand for *Harris & Hendrickson 1987* and *Price 1995*.
- **Seal et al. 1982** — Seal, Gross & Bioulac, 1982. Awake macaque; single-unit recording.
  **owed.**
- **Tracey & Waite, The Rat Nervous System** — **owed** — a book, cited second-hand through another
  work at both citing lines and carrying no edition or chapter. Rat.
