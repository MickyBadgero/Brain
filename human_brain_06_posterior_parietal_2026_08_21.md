# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-21
---

---

# FILE 6 OF 20 — POSTERIOR PARIETAL

**What is in this file.** The remaining posterior parietal areas: the anterior and medial
intraparietal areas for grasp and reach, the supramarginal and angular gyri, and the precuneus.

**Size:** 877 lines, ~17.4k tokens (estimated from bytes, not tokenised). **Entries:** 5. **Edge
lines:** 55 — 39 in, 16 out.

**This file is one section of the source. Edges cross into other files; an endpoint named here that
has no entry here lives in another file. Do not treat a missing endpoint as a missing region without
checking the other files.**

**Entries in this file:**

- **Anterior intraparietal area (grasp; rostral lateral bank of the intraparietal sulcus)**
- **Medial intraparietal area / parietal reach region (reach; medial bank of the intraparietal sulcus)**
- **Supramarginal gyrus (Brodmann area 40 / von Economo PF; ≈ macaque 7b)**
- **Angular gyrus (Brodmann area 39 / von Economo PG, subareas PGa + PGp; ≈ macaque 7a / Opt–PG)**
- **Precuneus (medial parietal — area 7m / PGm, areas 7Am / 7Pm; caudal Brodmann area 31)**

**Files whose shared edges are checked against this one:** 1 (visual pathway), 4 (dorsal visual /
parietal stream), 5 (sensorimotor loop), 7 (anterior temporal lobe), 8 (medial temporal lobe), 11
(frontal lobe), 17 (insula / claustrum / habenula / cingulate remainder). **Unchecked:** 2
(auditory), 3 (other senses), 9 (basal ganglia), 10 (cerebellum), 12 (thalamus), 13–16, 18–20.

---

# POSTERIOR PARIETAL (remainder — inferior parietal lobule, grasp/reach intraparietal, precuneus)

*The posterior parietal cortex behind the somatosensory areas splits into two families.
**(1) Two parieto-frontal sensorimotor channels** run in parallel through the intraparietal
sulcus: a **dorso-medial "reach" channel** (V6A → the medial intraparietal area / parietal
reach region → dorsal premotor cortex → primary motor cortex) and a **dorso-ventral "grasp"
channel** (the anterior intraparietal area → ventral premotor cortex, area F5 → primary motor
cortex) — reach transports the hand, grasp shapes it (Jeannerod et al. 1995; Rizzolatti &
Luppino 2001; Andersen). These join the already-described ventral intraparietal area
(peripersonal space → F4) and lateral intraparietal area (saccade priority map) on the
intraparietal walls. **(2) The inferior parietal lobule**
convexity — supramarginal (Brodmann area 40) and angular (Brodmann area 39) gyri — is
high-level polymodal
association cortex, greatly expanded and reorganised in humans relative to the macaque, and a
node of the ventral-attention and default-mode networks rather than a sensorimotor relay.
Medially, the **precuneus** is a default-mode / self-referential hub. Human per-area neuron
counts for these association areas barely exist (as with the prefrontal cortex): the anatomy
and data flow are verified, the counts stay soft or unknown.*

*Macaque↔human note. The macaque inferior parietal lobule convexity is Brodmann area 7,
classically split into 7a (caudal = von Economo PG/Opt: visual + oculomotor, eye-position gain
fields) and 7b (rostral
= PF/PFG: somatosensory, arm/hand/face, part of the mirror system) — Vogt & Vogt 1919;
Hyvärinen 1981. Architectonic and connectivity work maps macaque Opt/PG onto the human
angular gyrus (PGp/PGa) and macaque PF/PFG onto the human supramarginal gyrus (Caspers et al.
2008; Niu et al. 2021). This doc therefore folds "7a/7b" into the human supramarginal and
angular entries below rather than listing them as separate walls, to avoid double-counting the
same cortex.*

***Three endpoints named in this file have no entry in any of the seven files checked against this one:
V6, the dorsal and ventral subdivisions of V6A, and the caudal intraparietal area.*** *The
visual-pathway file holds eight entries — retina, chiasm, lateral geniculate nucleus, V1, V2,
V3 / V3A, V4, inferotemporal cortex — and the dorsal-stream file holds four — the middle
temporal area, the medial superior temporal area, the ventral intraparietal area, the lateral
intraparietal area. **None of the three regions is among them**, and the section head above
names V6A as the origin of the whole reach channel. Two independent corroborations that these
are regions the source is missing rather than regions filed elsewhere: V1's Inputs name*
caudal intraparietal cortex *among its long-range feedback sources with no entry to point at,
and V3's Outputs name* the posterior intraparietal area *the same way. **Owed: give V6, the two
subdivisions of V6A, and the caudal intraparietal area entries, and decide which file owns
them.** This is a statement about the source's coverage, not about this file, and it is
recorded here because this file is where the dangling edges are.*

## Anterior intraparietal area (grasp; rostral lateral bank of the intraparietal sulcus)

- **Function:** the parietal node of the visuomotor grasping circuit — transforms an object's
  3-D physical properties (size, shape, orientation) into a hand configuration for grasp.
  Neurons are selective for object shape/size/orientation and for grip type (precision vs
  whole-hand) (Taira et al. 1990; Murata et al. 2000). Object attributes are encoded as a
  gradient along this area → ventral premotor area F5 → primary motor cortex — object first in
  visual terms, then as
  an appropriate grip.
- **Inputs:**
  - **← caudal intraparietal area** — **carries:** 3-D surface shape from disparity and
    texture — the object's geometry, not its identity. **Fan-in:** unknown.
    **The edge is sourced; the far end has no entry in any file checked against this one** — see the note at
    the head of this section. The same tracer study that supplies this entry's input list reports a
    connection with the caudal intraparietal area, so the missing endpoint is a gap in the source's
    coverage and not a doubtful edge. **Owed: give the caudal intraparietal area an entry.**
    *(Class 1 — Borra et al. 2008, macaque. Located by web search; abstract only. Candidate —
    awaiting Micky's verification.)*
  - **← the rostral part of the lateral intraparietal area** — **carries:** the priority map (which
    object is the current target). **Fan-in:** unknown. **The far end agrees and names this area**:
    the lateral intraparietal entry's Outputs declare "→ the anterior intraparietal area — carries:
    the priority map — which object is the current target," and record that it leaves from the
    rostral part. Two-ended, and the two ends agree in the same words — *which, per the payload
    rule's caution, certifies less than a diff of two independently written ends.*
  - **← lower-bank superior temporal sulcus / middle temporal gyrus** (ventral stream) — **carries:**
    object **identity**. **Fan-in:** unknown.
    **The edge is sourced and the producer declares nothing, so the repair belongs at the producer
    and withdrawal is not an option.** The tracer study this entry's whole input list derives from
    reports major connections with ventral visual stream areas of the lower bank of the superior
    temporal sulcus and the middle temporal gyrus, and its authors treat that as the paper's
    headline: direct anatomical connections with the inferotemporal cortex, giving this area a role
    linking the parieto-frontal grasping network to object recognition. So visuomotor transformation
    here draws on **ventral**-stream object identity as well as **dorsal**-stream object geometry.
    **The visual-pathway file is checked against this one, and the inferotemporal entry's Outputs name the
    distributed conceptual / semantic system via the temporal pole, the hippocampal formation,
    ventrolateral prefrontal cortex, the amygdala, perirhinal cortex and the striatum — no parietal
    target of any kind.** **Owed as a cross-file edit at the inferotemporal entry (file 1): write
    this output edge, and name the sub-element it leaves from** — the projecting cells are in the
    lower bank of the superior temporal sulcus and the middle temporal gyrus, a ventrolateral sector
    that entry's two divisional sub-elements (posterior and anterior inferotemporal cortex) do not
    name. *(Class 1 — Borra et al. 2008, macaque. Located by web search; **abstract only, no
    full paper opened**. Candidate — awaiting Micky's verification.)*
  - **← the secondary somatosensory cortex** — **carries:** tactile object identity and contact
    state. **Fan-in:** unknown.
    **The far end agrees and names this area**: the secondary somatosensory cortex entry's Outputs
    declare "→ the anterior
    intraparietal area — carries: tactile object identity and contact state," transcribed there from
    this entry's declaration. **The agreement certifies nothing** — that end was transcribed from
    this one.
  - **← the ventral intraparietal area** — **carries:** object location and motion in head- and
    body-centred coordinates. **Fan-in:** unknown. **The far end agrees in the same words**: the
    ventral intraparietal entry's Outputs record this as "the one edge out of this entry whose two
    ends agree."
  - **← superior parietal area 5** (principally area PE) — **carries:** limb state — the arm and
    hand configuration against which the object's geometry has to be expressed. **Payload otherwise
    unknown — owed. Declared at the producer's end; written here so the edge has two ends**: the
    superior parietal area 5 entry's Outputs declare "→ the anterior intraparietal area — carries:
    the same limb state." **Fan-in:** unknown. *(Transcribed from the superior parietal area 5
    entry, file 5, which marks it Class 1 — Johnson et al. 1996; Bakola et al. 2013; macaque.
    Candidate — awaiting Micky's
    verification.)*
  - **← prefrontal areas 46 and 12** — **carries:** goal / task context. **Payload otherwise unknown
    — owed.** **Fan-in:** unknown.
    **Neither producer declares this edge, and they fail differently.** The frontal-lobe file is
    checked against this one. The dorsolateral prefrontal entry (areas 9 / 46) declares its Outputs
    as
    "parietal and sensory cortex (top-down bias)" — **a class that is compatible with this payload
    and does not name this area**; the ventrolateral prefrontal entry (areas 45 / 47, the entry that
    owns area 12) declares its Outputs as Broca, temporal cortex and the basal-ganglia loop —
    **no parietal target at all**. **Owed as a cross-file edit at both entries (file 11): name this
    area at the dorsolateral entry, and either write the parietal edge at the ventrolateral entry or
    withdraw area 12 from this line.** This line also names two sources at once and **splitting it
    is owed** once the far ends are settled.
- **Outputs:**
  - **→ ventral premotor area F5** → primary motor cortex hand representation — **carries:** a **hand
    configuration** — grip type (precision vs whole-hand) and the wrist/finger posture the object
    affords. **The payload change here is a translation between ontologies**: an object's physical
    properties go in, and a *posture of the body* comes out. The object attributes are encoded along
    a gradient from this area through F5 to the primary motor cortex, visual at one end and motor
    at the other.
    **Fan-out:** unknown.
    **The far end declares the edge only as a class and does not use the name F5.** The premotor
    entry's Inputs read as prose — "posterior parietal (SPL area 5, and the grasp/reach intraparietal
    areas), prefrontal (goals), and basal-ganglia + cerebellar output via VA/VL thalamus" — which
    covers this area under a class, carries no `carries:` line and no fan-in, and names no
    sub-element. **Owed as a cross-file edit at the premotor entry (file 11): type this input, name
    this area rather than a class, and give F5 a sub-element, since this edge and three edges in the
    dorsal-stream file terminate on it and the entry that owns the name does not use it.**
  - **→ the medial intraparietal area** — **carries:** payload **owed**; grasp-related object
    geometry into the reach channel, which is where the two parieto-frontal channels described at
    the head of this section actually meet. **Fan-out:** unknown. **The consumer's end declares it**,
    in this file, as its own named edge, and marks the payload owed there too. *(Class 1 — eNeuro
    4:ENEURO.0344-17, 2017, macaque. Not yet verified for the source.)*
  - **→ the dorsal subdivision of V6A** — **carries:** payload **owed**; the same grasp-related
    object geometry. **Fan-out:** unknown. **The far end has no entry in any file checked against
    this one** —
    see the note at the head of this section. **Owed: give V6A an entry, or withdraw this edge.**
    *(This edge and the one above have far ends of different status, and one of those far ends has
    no entry. Class 1 — eNeuro 4:ENEURO.0344-17, 2017, macaque. Not yet verified
    for the source.)*
- **Internal structure and internal data flow:** *(**Nothing here is yet verified
  for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. *(Class 3.)*

  **Divisional sub-elements: none established.** Receptor-architectonic mapping of the whole
  intraparietal sulcus divides its neighbours — the ventral intraparietal area into medial and
  lateral parts, the lateral into dorsal and ventral, the medial into dorsal and ventral — and
  leaves **this area undivided**, sitting on the most anterior part of the fundus and extending onto
  the lateral bank. **That is a negative result from a study that would have found a division, which
  is worth more than silence**, and it is recorded as such rather than as "unknown." *(Class 1 —
  eLife 9:e55979, 2020, macaque.)*

  **Tangential sub-elements: owed.** The Function field asserts selectivity for **grip type** —
  precision versus whole-hand — which is a categorical property of the kind that is columnar
  elsewhere in this file. Whether grip types cluster spatially here is not established.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — the transform itself: owed, and it is the whole entry.** Object geometry
  arrives on one set of edges and a hand posture leaves on another, and **nothing here says what
  happens in between**. This is the completion test biting: the payloads at both ends are writable,
  and the step that converts one to the other is not described at any level this file records.
- **Neurons:** soft — order ~15M per hemisphere by analogy to the neighbouring measured
  intraparietal areas (lateral ~20M, ventral ~12M); no clean human count.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Medial intraparietal area / parietal reach region (reach; medial bank of the intraparietal sulcus)

- **Function:** the parietal node of the reach channel — encodes the direction (and, more
  weakly, amplitude) of an intended reach in a mixture of gaze-centred, hand-centred, and
  intermediate reference frames, and is effector-specific (more active before contralateral-arm
  than eye movements). With the medial parieto-occipital area V6A it forms the **parietal reach
  region** (Snyder, Batista & Andersen 1997; Galletti).
  **The "parietal reach region" is a functional label over more than one area, and the areas
  differ.** Myeloarchitecture and retrograde tracing divide the medial bank of the sulcus into
  **three**: the dorsal subdivision of V6A, this area, and the intraparietal subdivision of area PE.
  This area is moderately myelinated with two distinct bands of Baillarger. Against V6A's dorsal
  subdivision it receives **denser input from somatosensory areas, primary motor cortex, and the
  medial motor fields**, while V6A takes the stronger visual input; the intraparietal subdivision of
  PE emphasises anterior parietal and ventral premotor connections and, unlike this area, **projects
  to the spinal cord**. **So the three are ordered by how close to movement they sit**, and treating
  the reach region as one thing loses that ordering. *(Class 1 — eNeuro 4:ENEURO.0344-17, 2017;
  PMC8266221; macaque. Not yet verified for the source.)*
  **Two of those three have no entry in the source** — the dorsal subdivision of V6A, and V6 itself;
  the third, the intraparietal subdivision of area PE, is a sub-element of the superior parietal
  area 5 entry (file 5), which names PE, PEa and PEc. See the note at the head of this section.
- **Inputs:**
  - **← V6, and the ventral subdivision of V6A** — **carries:** target location in the visual field,
    retinotopic. **Fan-in:** unknown. **Neither far end has an entry in any file checked against
    this one** —
    see the note at the head of this section. This is the edge that supplies the *visual* half of
    the frame mixture the output declares, so its absence is not a bookkeeping gap: **the reach
    channel's visual input has no producer anywhere in the source.** **Owed: give V6 and V6A
    entries.**
  - **← the primary somatosensory cortex, superior parietal area 5, the primary motor cortex and
    the medial motor fields** — **carries:** current arm
    configuration. **This is the edge that makes the frame mixture in the output possible**, and it
    is why this area and not V6A carries the mixture. **Fan-in:** unknown.
    **The frame on this edge is contested and this line does not assert one side of it.** Typing it
    as "in a body-centered frame" would pick a side. The superior parietal area 5 entry — the
    producer of the area-5 limb — holds body-centred contested: the reported frames are
    **body-, shoulder- and hand-centred across different studies**, and in area PE specifically a
    memorised target's distance is encoded relative to the initial hand position, which is
    hand-centred. **On this file's payload rule the coordinate frame is part of the payload, so an
    unsettled frame is an unsettled payload**, and this line is therefore **payload contested — not
    owed**: the frame has been measured repeatedly and the measurements disagree, which is a
    different state from nobody having looked. **Not resolved here; which end is right is a source
    judgment.** *(The dispute is recorded in full at the superior parietal area 5 entry, file 5.
    Class 1 — Ferraina et al. 2009; Ferraina & Bianchi 1994; Lacquaniti et al. 1995; Kalaska 1996;
    Graziano et al. 2000; Bremner & Andersen 2012;
    macaque. Candidate.)*
    **This line names four sources at once and splitting it is owed.** The area-5 limb has a
    declared producer; the primary somatosensory, primary motor and medial-motor-field limbs are
    unchecked, and the medial motor fields are a class rather than a named region.
  - **← the anterior intraparietal area** — **carries:** payload **owed**; grasp-related object
    geometry into the reach channel. **Fan-in:** unknown. **The producer declares it**, in this file.
    *(Class 1 — eNeuro
    4:ENEURO.0344-17, 2017, macaque.)*
  - **← the ventral intraparietal area** — **carries:** **body-centred locations, for reach**, per
    the producer's own declaration. **Fan-in:** unknown. **Typed from the producer's declaration**,
    which is the more specific of the two: the ventral intraparietal entry declares this payload,
    and records that the two ends disagree and that its own is the sharper. *(Class 1 at the
    producer's end — eNeuro
    4:ENEURO.0344-17, 2017, macaque.)*
  - **← the medial superior temporal area** — **carries:** payload **owed at both ends**. **Fan-in:**
    unknown. **The producer's end declares this edge and marks it owed.** *(Class 1 — eNeuro
    4:ENEURO.0344-17, 2017, macaque.)*
  - **← superior parietal area PEc** — **carries:** payload **owed**; spatial context and self-motion.
    **Fan-in:** unknown. **The producer declares an edge to this area**, as part of the superior
    parietal area 5 entry, whose PEc subdivision is described there as sensitive to proprioception
    and gaze together and linked to optic-flow analysis — which is what "self-motion" on this line
    would have to mean. **Whether the area-5 output edge and this line are the same edge or two is
    owed**, since the producer writes one edge to this area and this entry now carries two (the
    four-source arm-configuration line above also names area 5). *(Class 1 — eNeuro
    4:ENEURO.0344-17, 2017; Bakola et al. 2010; macaque.)*
  - **← the angular gyrus** — **carries:** payload **owed**. **Fan-in:** unknown. **The producer is in this file and carries an owed output edge**, marked there as asserted from this end. *(Class 1 for the projection — eNeuro
    4:ENEURO.0344-17, 2017, macaque.)*
  - **← the precuneus (area 7m / PGm)** — **carries:** payload **owed**. **Fan-in:** unknown. **Same
    status as the angular gyrus line**: the producer is in this file, declared nothing, and now
    carries an owed output edge written from this end. *(Class 1 — eNeuro 4:ENEURO.0344-17, 2017,
    macaque.)*
  - **← temporo-parieto-occipital cortex** — **carries:** payload **owed**. **This endpoint is a
    class and does not resolve to a named region with an entry.** **Owed: name it, or withdraw.**
    **Fan-in:** unknown. *(Class 1 for the projection — eNeuro 4:ENEURO.0344-17, 2017, macaque.)*
  - **← cingulate area 23, dorsocaudal premotor area F2, and ventral premotor areas F4 and F5**
    (long-range, including descending) — **carries:** payload **owed**. Recorded because these are
    frontal sources on an entry whose others are parietal and sensorimotor, and because they are a
    **return** limb from the very areas the output edge targets. **Fan-in:** unknown. *(Class 1 —
    same source.)*
    **None of the three far ends declares this edge.** The posterior cingulate entry (file 17) owns
    area 23 and declares its Outputs as the default-mode partners, the hippocampal system and the
    cognitive-control network, naming no intraparietal target; the premotor entry (file 11) declares
    its Outputs as the primary motor cortex, some direct corticospinal fibres, and the
    basal-ganglia motor loop, naming no
    parietal target and no sub-elements F2, F4 or F5. **Owed as cross-file edits at the posterior
    cingulate entry (file 17) and the premotor entry (file 11).** This line also names three sources
    at once and **splitting it is owed**.
- **Outputs:**
  - **→ dorsal premotor cortex (area F2)** → primary motor cortex — **carries:** a **reach
    vector** — the direction
    (and, more weakly, amplitude) of an intended reach, in a **mixture** of gaze-centred,
    hand-centred, and intermediate frames, and **effector-specific** (arm, not eye). The mixed frame
    is not sloppiness in the description: the source says the code genuinely is intermediate, and a
    consumer that assumes one pure frame will be wrong. **Fan-out:** unknown.
    **The far end declares it only as a class and does not name F2.** The premotor entry's Inputs
    read "posterior parietal (SPL area 5, and the grasp/reach intraparietal areas)" — untyped, no
    fan-in, no sub-element. **Owed as a cross-file edit at the premotor entry (file 11), the same
    edit the grasp channel's output needs.**
  - **→ superior parietal area 5**, onto the medial bank (area PEa) — **carries:** payload **owed**.
    **Declared at the consumer's end; written here so the edge has two ends**: the superior parietal
    area 5 entry's Inputs name "the medial bank of the intraparietal sulcus (including the medial
    intraparietal area)" among its tracer-demonstrated afferents and marks the content untyped.
    **Fan-out:** unknown. *(Transcribed from the superior parietal area 5 entry, file 5, which marks
    it Class 1 — Bakola et al. 2013, macaque. Candidate — awaiting Micky's verification.)*
    **The reciprocal pair is now closed and the two limbs are not symmetric in what is known about
    them.** The descending limb — area 5 → this area — carries limb state in a contested frame; this
    limb has no typed payload at all. That asymmetry is the finding, not an artefact of the writing
    order: the reach literature reads the parietal-to-frontal direction and has not read this one.
- **Internal structure and internal data flow:** *(**Nothing here is yet verified
  for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided, with **two
  distinct bands of Baillarger** visible in myelin stain — a laminar feature this file records
  nowhere else, and one that belongs to the fibre plexus in layers 4 and 5b rather than to a cell
  population. *(Class 1 for the bands — eNeuro 4:ENEURO.0344-17, 2017; Class 3 for the eight.)*

  **Divisional sub-elements: two, by receptor architecture** — a **dorsal** and a **ventral** part,
  separated in the same mapping that divides the lateral and ventral intraparietal areas. **Their
  separate payloads are owed**; nothing read distinguishes what each carries, and the
  reach literature does not use the division at all. **Recorded as a division the physiology has
  not caught up with.** *(Class 1 — eLife 9:e55979, 2020, macaque.)*

  **A second, incompatible parcellation of the same tissue, recorded not resolved.** Tracer plus
  tractography work divides this area instead into an **anterior** and a **posterior sector**, on
  gradient-like connectivity profiles rather than on a border. **A gradient with sectors and a
  receptor border with two parts are not the same claim about the same tissue**, and this file has
  no basis for choosing. Both are recorded; the region's **edges** carry the function either way,
  which is the treatment this file already gives 4B's disputed layer number. *(Class 1 —
  PMC8266221, macaque.)*

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — divisional: owed**, under either parcellation.

  **The frame mixture has no declared internal mechanism.** The output payload is stated to be a
  mixture of gaze-centred and hand-centred frames. Two incoming edges supply the two frames — the
  visual one from V6 and V6A, the postural one from the somatosensory and motor areas — and **no
  edge here says where they meet**. Same hole as the gain-field edge at the ventral intraparietal
  area and the transform at the anterior intraparietal area: three neighbouring entries whose stated
  function is a coordinate change, and none of the three can say where the change happens.
  **The hole is deeper than a missing mechanism**, because the visual limb's producer has no entry
  either: the mixture lacks both a mechanism and one of its two inputs.
- **Neurons:** soft — order ~15M per hemisphere (as the anterior intraparietal area, by
  intraparietal-neighbour analogy); no clean human count.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** moderately myelinated, with two bands of
  Baillarger; g-ratio unknown.

## Supramarginal gyrus (Brodmann area 40 / von Economo PF; ≈ macaque 7b)

- **Function:** polymodal somato-motor association at the anterior inferior parietal lobule —
  tactile/proprioceptive
  integration, praxis and tool use, and (left-lateralised) phonological processing; the
  frontoparietal mirror / action-observation system runs through PF/PFG. Its ventral part, with
  the posterior superior temporal sulcus, forms the right-dominant **temporoparietal junction**
  of the ventral-attention network — stimulus-driven reorienting to behaviourally relevant events
  outside the current focus (Corbetta & Shulman 2002). The left supramarginal gyrus anchors the
  temporoparietal (dorsal) phonological route of language via the arcuate fasciculus.
  Cytoarchitectonically it is now resolved into ~5 areas (PFop, PFt, PF, PFcm, PFm; Caspers et
  al. 2008), not one.
- **Inputs:**
  - **← the secondary somatosensory cortex** — **carries:** the object-level tactile payload —
    texture, shape and material, contact-point invariant. **Fan-in:** unknown. **The far end agrees
    and names this area**: the secondary somatosensory cortex entry's Outputs declare "→ area 7b
    (the supramarginal gyrus) — carries: the object-level tactile payload — texture, shape and
    material, contact-point invariant," and record that this end is
    untyped. Typed here now from the producer's declaration. *(Transcribed from the secondary
    somatosensory cortex entry, file 5. Candidate — awaiting Micky's verification.)*
  - **← superior parietal area 5** — **carries:** body configuration. **Fan-in:** unknown. **The far
    end declares it and names this area**: the superior parietal area 5 entry's Outputs declare
    "→ the supramarginal gyrus — carries: body configuration," transcribed there from this entry's
    declaration. **The agreement certifies nothing** — that end was transcribed from this one.
    *(The area-2 limb belongs with the secondary somatosensory line above, since that entry's own
    payload is what areas 3b, 1 and 2 deliver to it; **whether a
    separate direct area-2 edge exists is owed**.)*
  - **← posterior superior temporal gyrus / Spt** (the auditory "where" / audiomotor endpoint) —
    **carries:** the auditory-to-motor mapping and phonological form. **Fan-in:** unknown.
    **Far end in the auditory file, unchecked.**
  - **← the medial superior temporal area** — **carries:** payload **owed at both ends**. **Fan-in:**
    unknown. **The producer declares it and marks it owed**, and records that this end declares an
    input from that area and the middle temporal area jointly, carrying motion and the priority map,
    untyped and uncited.
  - **← the lateral intraparietal area** — **carries:** the **priority (salience) map** — one scalar
    per retinotopic location, ranking it by behavioural priority. **Fan-in:** unknown. **The far end
    agrees and names this area**: the lateral intraparietal entry's Inputs name this area as a
    source of a return limb, and record that the only supramarginal link the source describes runs
    from there to here.
  - **← the middle temporal area** — **carries:** payload **owed**; motion. **Fan-in:** unknown.
    **The producer declares nothing.** The middle temporal entry's Outputs name the medial superior
    temporal area, smooth-pursuit oculomotor circuitry, the ventral and lateral intraparietal areas,
    and feedback to V1 and V2 — **no inferior parietal target**. **Owed as a cross-file edit at the
    middle temporal entry (file 4), or withdraw this limb.** *(A single payload — "motion and the
    priority map" — cannot be asserted across this source and the two above it, since this one has
    no producer end at all.)*
  - **← ventrolateral prefrontal cortex (Brodmann areas 44 and 45)**, reciprocal via the arcuate
    fasciculus / superior longitudinal fasciculus III —
    **carries:** task and articulatory context. **Payload otherwise unknown — owed.** **Fan-in:**
    unknown. **The producer declares nothing.** The ventrolateral prefrontal entry's Outputs read
    "Broca (language), temporal cortex (retrieval bias), basal-ganglia loop" — no parietal target;
    the Broca entry's Outputs read "premotor / motor cortex (articulation); reciprocal
    temporoparietal," which is **a class covering this area without naming it**. **Owed as a
    cross-file edit at both entries (file 11).**
- **Outputs:**
  - **→ ventrolateral prefrontal / Broca (44/45) and premotor cortex** — **carries:** two things
    that this file can name and not type: a **praxis / action-sequence code** (the learned structure
    of a skilled act, tool use), and, on the left, a **phonological code** (the sound-form of words
    for the articulatory route). **Payload only partly writable — owed:** "the plan of a skilled
    action" has no units and no frame, and calling it a code does not make it one. **This is the
    first entry where the slot cannot be filled honestly**, and the detector is working, not
    failing. **Fan-out:** unknown.
    **The far ends declare this only as a class.** The Broca entry's Inputs name "posterior STG /
    Spt (audiomotor, via the arcuate fasciculus), VLPFC, premotor" — **this area is not among them**,
    although its Outputs name a reciprocal temporoparietal link. The premotor entry's Inputs name
    posterior parietal as a class. **Owed as cross-file edits at both (file 11).** This line also
    names two targets at once and **splitting it is owed**, since the praxis code and the
    phonological code go to different places and only one of them is left-lateralised.
  - **→ the ventral-attention frontoparietal network** (the right-dominant temporoparietal
    junction, with the posterior superior temporal sulcus) —
    **carries:** a **reorienting signal** — *something behaviourally relevant just happened outside
    the current focus*. A one-bit interrupt with a location attached, as far as this file can
    determine. **Fan-out:** unknown. **This endpoint is a network, not a region, and it does not
    resolve.** **Owed: name the regions this edge terminates on.** The nearest candidate found in
    the files checked against this one is the insula entry (file 17), whose anterior pole anchors
    the salience
    network and whose Inputs name no parietal source — so if this edge reaches it, that end is
    undeclared too.
  - **→ the lateral intraparietal area** — **carries:** payload **owed**. **Fan-out:** unknown.
    **This edge is asserted at the consumer's end and has no independent support here.** The lateral
    intraparietal entry's Inputs declare "← the supramarginal gyrus — carries: payload owed," and
    record that "the producer declares nothing, and declares the opposite direction instead," and
    that the only supramarginal link the source describes runs from there to here. **Written at this
    end so the edge has two ends, and marked: nothing read establishes that this
    projection exists.** **Owed: find a source for it, or withdraw it at both ends.** *(Class 2 —
    the edge is transcribed from the consumer's declaration; no primary source names it.)*
- **Internal structure and internal data flow:** *(**Absent
  entirely**. **Nothing here is verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. Granular
  association isocortex, so the standard set applies — unlike the primary motor cortex, where the
  agranular laminar
  description makes the standard block incompatible with the entry's own Function. *(Class 3.)*

  **Divisional sub-elements: five, and they are cytoarchitectonic before they are functional** —
  **PFop, PFt, PF, PFcm and PFm**. Taken from this entry's own Function field, which already states
  the division and its source. **Their separate payloads are owed**: nothing in this file
  distinguishes what each carries, and every edge above terminates on the whole gyrus. **The entry's
  own Function field asserts at least three functionally distinct jobs** — tactile/proprioceptive
  integration, praxis and tool use, and left-lateralised phonological processing — **so an edge
  terminating "on the supramarginal gyrus" is under-specified in the same way an edge terminating
  "on the lateral intraparietal area" would be without that entry's split by subdivision.** **Splitting
  is owed**, and the basis for it already exists. *(Class 1 for the parcellation — Caspers et al.
  2008, human, as cited in this entry's Function. Class 2 — the reading that the
  functional list and the architectonic list should be brought into correspondence is Claude's,
  offered to be checked.)*

  **A second division cross-cuts the first: the ventral part belongs to the temporoparietal
  junction and the rest does not.** The Function field assigns the ventral part, with the posterior
  superior temporal sulcus, to the right-dominant ventral-attention network, while the left gyrus
  anchors the phonological route. **So this entry carries a left/right functional asymmetry and a
  dorsal/ventral one, and neither maps cleanly onto the five architectonic areas.** Recorded as
  unresolved rather than forced into one scheme — the same treatment the medial intraparietal entry
  gives its two incompatible parcellations. *(Class 2 — the observation that the three schemes do
  not align is Claude's reading of this entry's own Function field.)*

  **Tangential sub-elements: unknown.** No columnar or compartmental repeat is recorded for this
  area.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — divisional: owed.** No edge between any two of the five areas is recorded
  anywhere, in either direction.

  **Internal edges — the somato-to-praxis conversion: owed, and it is this entry's version of the
  hole at the anterior intraparietal area.** Object-level tactile payload and body configuration
  arrive; a praxis / action-sequence code leaves. Nothing here says what happens between them, and
  unlike the grasp entry the *output* payload is not writable either — so this entry fails the
  completion test at both the transform and the output.
- **Neurons:** soft/unknown — no clean human per-area count (as for prefrontal association
  cortex); association-cortex packing (order ~20,000 neurons/mm³, cf. the temporal pole), the
  human inferior parietal lobule greatly enlarged over the macaque.
- **Synapses:** unknown. **Axons:** the arcuate fasciculus / superior longitudinal fasciculus
  III (counts unknown). **Grey-matter volume:** unknown. **White-matter volume:** unknown.
  **Myelination:** unknown.

## Angular gyrus (Brodmann area 39 / von Economo PG, subareas PGa + PGp; ≈ macaque 7a / Opt–PG)

- **Function:** a high-level cross-modal integration and semantic hub at the
  temporo-parieto-occipital junction — binds information across modalities and over time into
  concepts and events. Central to semantic processing, reading, and number/arithmetic, and to
  the vivid re-experiencing of episodic memory (the parietal "recollection" signal); a core
  node of the **default-mode network**. The left angular gyrus is a semantic-integration hub
  (complementing the anterior-temporal semantic hub at the temporal pole); the right angular
  gyrus contributes to
  spatial/attentional and social cognition. A rostro-caudal gradient runs from
  ventrolateral-prefrontal-coupled (PGa, more attentional) to hippocampal /
  default-mode-network-coupled (PGp,
  more mnemonic) — the "attention-to-memory" account (Cabeza).
- **Inputs:**
  - **← occipitotemporal cortex** (visual) — **carries:** object and face **identity**. Note what
    has already been discarded upstream: no hue. **Fan-in:** unknown.
    **The producer declares nothing.** The inferotemporal entry's Outputs (file 1) name the
    distributed conceptual / semantic system via the temporal pole, the hippocampal formation,
    ventrolateral prefrontal cortex, the amygdala, perirhinal cortex and the striatum — **no
    parietal target**. **Owed as a cross-file edit at the inferotemporal entry (file 1), or withdraw
    this edge.** This is the same missing producer the anterior intraparietal entry's ventral-stream
    input has — **the source currently describes no edge at all from the ventral stream into the
    parietal lobe**, while two parietal entries declare one — **but the two are not in the same
    evidential state and should not be repaired as one.** That edge carries a primary tracer source
    naming its origin sector; **this one carries none**, and nothing read or searched establishes
    it. **So: repair the anterior intraparietal edge at file 1, and treat this one
    as still open at both ends.**
  - **← superior temporal sulcus** (auditory) — **carries:** word / sound identity. **Fan-in:**
    unknown. **Far end in the auditory file, unchecked.**
  - **← somatosensory association cortex** — **carries:** tactile object identity. **Fan-in:**
    unknown. **The producers declare this only as a class.** The primary somatosensory cortex
    entry (file 5) declares "→ posterior parietal cortex, from areas 1 and 2 — payload unknown —
    owed," and the secondary somatosensory cortex entry
    declares "→ posterior parietal cortex (remainder, beyond the two named above) — carries: the
    object-level tactile payload. **This endpoint is a class**; owed: name any others, or withdraw."
    **This entry is a member of that class and is not named at either producer. Owed as cross-file
    edits at both (file 5).** *(The three modality lines above are kept separate rather than
    compounded because their far ends have three different statuses — undeclared, unchecked, and
    declared-as-a-class.)*
  - **← the lateral intraparietal area** — **carries:** the **priority (salience) map** — one scalar
    per retinotopic location, ranking it by behavioural priority (bottom-up salience + top-down
    attention + reward), modality-free. **Fan-in:** unknown. **Declared at the producer's end only
    and written here so the edge has two ends**: the lateral intraparietal entry's Outputs declare "→ the
    angular gyrus — carries: the same priority map. **The far end declares nothing** … **Owed as a
    cross-file edit at the angular gyrus entry (file 6).**" **That owed edit is discharged by this
    line.** **This is the one input to this entry whose payload is
    fully typed**, which is worth noting against the entry's output slot below. *(Transcribed from
    the lateral intraparietal entry, file 4. Candidate — awaiting Micky's verification.)*
  - **← the hippocampal formation** — **carries:** a **completed episode** — the bound, retrievable
    pattern, addressable by any fragment of itself. **Payload only partly writable — owed**, per the
    producer's own declaration: "an episode" has no units and no frame, and the one checkable
    property in hand is that it is **content-addressable**, which the identity codes arriving on the
    other inputs are not. **Fan-in:** unknown. **The producer declares its target as a class** —
    "→ neocortex via subiculum / entorhinal cortex" — which covers this area without naming it.
    **Owed as a cross-file edit at the hippocampal formation entry (file 8).** *(Payload transcribed
    from that entry, file 8.)*
  - **← the posterior cingulate cortex** — **carries:** payload **owed**. **Fan-in:** unknown. **The
    producer declares this edge and names this area**: the posterior cingulate entry's Outputs read
    "the DMN partners (medial prefrontal, angular gyrus, precuneus, medial temporal lobe)" — untyped
    there, no `carries:` line and no fan-out. **Owed at file 17: type it.**
  - **← the precuneus** — **carries:** payload **owed**. **Fan-in:** unknown. **The producer is in
    this file and declares this edge**, also owed there.
  - **← medial prefrontal cortex** — **carries:** payload **owed**. **Fan-in:** unknown. **The
    producer declares nothing.** The orbitofrontal / ventromedial prefrontal entry (file 11)
    declares its Outputs as the amygdala, hypothalamus, ventral striatum and autonomic centres —
    no parietal or default-mode target. **Owed as a cross-file edit at that entry (file 11), or
    withdraw this limb.** *(The three lines above are kept separate rather than named as one
    default-mode-network line, because their far ends differ.)*
- **Outputs:**
  - **→ default-mode partners, the hippocampal formation, ventrolateral prefrontal cortex, lateral
    temporal semantic cortex** — **PAYLOAD UNKNOWN — OWED, AND THIS IS THE LOUD ONE.** The Function
    slot says the angular gyrus "binds information across modalities and over time into concepts and
    events." That sentence reads as complete right up until you try to say **what leaves it on a
    wire**, and then it fails: a "concept" and an "event" have no units, no range, no coordinate
    frame, and no channel structure. This file cannot currently say what this region emits, and the
    honest record of that is a hole, not a paraphrase. **Fan-out:** unknown.
    **Three of the four far ends are checked and none declares this edge.** The
    hippocampal formation's Inputs (file 8) name "neocortical association areas via entorhinal
    cortex / perforant path (including IT for object and scene identity, and parietal)" — **a class
    that covers this area without naming it**. The ventrolateral prefrontal entry's Inputs (file 11)
    name the anterior temporal lobe, inferotemporal cortex, mediodorsal thalamus and the anterior
    auditory belt — **not this area**. The temporal pole entry's Inputs (file 7) name the rostral
    superior temporal gyrus, anterior inferotemporal cortex, and orbitofrontal / insular cortex and
    the amygdala — **not this area**. The fourth, "default-mode partners," is a network and does not
    resolve. **Owed: name the members, and write the cross-file edits at files 7, 8 and 11.**
    **Splitting this line is owed** — it names four targets and one non-payload.
    **A note on why the hole is worth what it costs.** Every typed input to this entry — the
    priority map, the identity codes, the completed episode — arrives with a frame or an explicit
    absence of one. The output has neither. So the untypable step is located precisely: it is
    *inside* this entry, not inherited from a vague input. That is the same shape as the temporal
    pole's amodal concept (file 7) and the anterior insula's subjective feeling (file 17), and the
    three together are the source's clearest statement of where its description stops.
  - **→ the lateral intraparietal area** — **carries:** payload **owed**. **Fan-out:** unknown.
    **This edge is asserted at the consumer's end and has no independent support here.** The lateral
    intraparietal entry's Inputs declare "← the angular gyrus — carries: payload owed. **The producer
    declares nothing** … **Owed as a cross-file edit at the angular gyrus entry (file 6), or withdraw
    the edge.**" **Written at this end so the edge has two ends, and marked: nothing read
    establishes that this projection exists.** *(Class 2 — transcribed from the consumer's
    declaration; no primary source names it.)*
  - **→ the medial intraparietal area** — **carries:** payload **owed**. **Fan-out:** unknown.
    **Asserted at the consumer's end, in this file**, where it sits among the tracer-demonstrated
    afferents to the reach region. Unlike the lateral intraparietal edge above, this one **does**
    have a primary source at the consumer's end. *(Class 1 — eNeuro 4:ENEURO.0344-17, 2017, macaque.
    Not yet verified for the source.)*
- **Internal structure and internal data flow:** *(**Absent
  entirely**. **Nothing here is verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. Granular
  association isocortex. *(Class 3.)*

  **Divisional sub-elements: two** — **PGa** (rostral) and **PGp** (caudal). Taken from this entry's
  own heading and Function field, which already name them.

  **The two divisions carry different payloads, and the difference is one of coupling rather than of
  content.** The Function field states a **rostro-caudal gradient**: PGa is
  ventrolateral-prefrontal-coupled and more attentional, PGp is hippocampal / default-mode-coupled
  and more mnemonic. **That maps directly onto the input edges above and splits them**: the
  prefrontal and priority-map inputs would be PGa's, the hippocampal and default-mode inputs PGp's.
  **Which edge reaches which division is owed** — nothing read assigns any of them —
  but the division is not idle, because assigning them would change the arity of six edges at once.
  *(Class 1 for the gradient — the Cabeza "attention-to-memory" lineage cited in this entry's
  Function. Class 2 — the reading that the gradient sorts this entry's existing input edges is
  Claude's, offered to be checked.)*

  **A gradient is not a border, and the entry should not be read as claiming one.** The Function
  field says gradient. Whether PGa and PGp are compartments an edge can terminate on, or two ends of
  a continuum with no boundary, is **not established here** — the same limit the inferotemporal
  entry records for its continuous feature map, where a position is a coordinate and not a
  compartment.

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — divisional: owed.** No PGa ↔ PGp edge is recorded in either direction. **This
  is the load-bearing one in this entry.** The Function field's claim is that this region *binds*
  across modalities and over time; the attentional and mnemonic streams arrive on different
  divisions by the gradient account; **so the binding, if it happens here, happens on an edge
  between the two divisions, and that edge is not written.** Same shape as the frame-mixture hole at
  the medial intraparietal area and the transform at the anterior intraparietal area — a stated
  function with no declared substrate — and it is the fourth in this file.

  **The left/right functional asymmetry is not a sub-element and is recorded separately.** The
  Function field assigns semantic integration to the left gyrus and spatial / attentional and social
  cognition to the right. That is a difference between two hemispheres' instances of this entry, not
  a division within one, and the file's per-hemisphere convention already covers it. It is noted
  here only because it interacts with the divisional question: **whether the PGa/PGp gradient is the
  same on both sides is unknown.**
- **Neurons:** soft/unknown — no clean human count; the macaque has no angular gyrus in the
  strict sense (human-expanded), so even a homology-based estimate is loose.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Precuneus (medial parietal — area 7m / PGm, areas 7Am / 7Pm; caudal Brodmann area 31)

- **Function:** a medial-wall association hub and **default-mode network core** (with the
  posterior cingulate and medial prefrontal cortex) — self-referential processing, first-person
  perspective and sense of agency, episodic-memory retrieval, and visuospatial mental imagery /
  scene construction. Functionally graded: an anterior sensorimotor sector (reach / area-5
  coupled), a central cognitive / default-mode-network sector, and a posterior visual sector
  (occipital-coupled)
  (Cavanna & Trimble 2006). One of the most metabolically active cortical regions at rest and a
  highly connected cortical hub.
- **Inputs:**
  - **← superior parietal area 5** — **carries:** body configuration and spatial layout,
    body-centred. **Fan-in:** unknown. **The far end declares it and names this area**: the superior
    parietal area 5 entry's Outputs declare "→ the precuneus — carries: body configuration and
    spatial layout, body-centred," transcribed there from this entry's declaration, **and flag the
    same frame disagreement the medial intraparietal edge carries** —
    that end holds the frame contested across body-, shoulder- and hand-centred readings, while this
    line says body-centred. **On this file's payload rule the frame is part of the payload, so the
    two ends disagree about the payload.** Not repaired here; which end is right is a source
    judgment. *(Class 1 — the frame dispute is recorded in full at the superior parietal area 5
    entry, file 5.)*
  - **← dorsal-stream visual areas** — **carries:** spatial layout. **Payload otherwise unknown —
    owed.** **Fan-in:** unknown. **This endpoint is a class and does not resolve.** The
    dorsal-stream file is checked against this one: none of its four entries — the middle temporal
    area, the medial superior
    temporal area, the ventral intraparietal area, the lateral intraparietal area — declares an
    output to this area. **Owed: name the dorsal-stream regions this edge comes from, or withdraw
    it.** *(Kept separate from the superior parietal area 5 line above, the two limbs having
    different statuses.)*
  - **← the posterior cingulate cortex** — **carries:** payload **owed**. **Fan-in:** unknown. **The
    producer declares this edge and names this area**: the posterior cingulate entry's Outputs read
    "the DMN partners (medial prefrontal, angular gyrus, precuneus, medial temporal lobe)" —
    untyped there. **Owed at file 17: type it.**
  - **← the retrosplenial cortex** — **carries:** payload **owed**; the return arm of the
    spatial-memory loop — egocentric-to-allocentric translated heading and landmark information, in
    the producer's terms. **Fan-in:** unknown. **Declared at the producer's end and written here so
    the edge has two ends**: the retrosplenial entry's Outputs (file 17) read "back to the hippocampal
    formation (via parahippocampal / entorhinal cortex), the anterior thalamus, and parietal /
    medial-parietal (precuneus) cortex — the return arm of the spatial-memory loop," naming this
    area explicitly. *(Transcribed from the retrosplenial entry, file 17. Candidate —
    awaiting Micky's verification.)*
    **This edge matters more than an added line usually does.** This entry's Function claims
    visuospatial mental imagery and scene construction, and the retrosplenial entry is where the
    source puts the egocentric↔allocentric frame translation those depend on. **So the one incoming
    edge that could supply the entry's headline function is untyped at both ends.**
  - **← the angular gyrus** — **carries:** payload **owed**. **Fan-in:** unknown. **The producer is
    in this file** and marks its output payload the loudest owed in the file.
  - **← medial prefrontal cortex** — **carries:** payload **owed**. **Fan-in:** unknown. **The
    producer declares nothing** — the orbitofrontal / ventromedial prefrontal entry (file 11) names
    the amygdala, hypothalamus, ventral striatum and autonomic centres, and no parietal target.
    **Owed as a cross-file edit at that entry (file 11), or withdraw this limb.**
  - **← the medial temporal lobe** — **carries:** payload **owed**. **Fan-in:** unknown. **The
    producer declares its target as a class** — the hippocampal formation's Outputs (file 8) read
    "→ neocortex via subiculum / entorhinal cortex" — which covers this area without naming it.
    **Owed as a cross-file edit at that entry (file 8).** *(The four lines above are kept separate
    rather than named as one "posterior cingulate and the default-mode partners" line, because their
    far ends have four different statuses.)*
- **Outputs:**
  - **→ the posterior cingulate cortex** — **payload unknown — owed.** "Self-referential
    processing," "first-person perspective," and "scene construction" are functions, not payloads;
    nothing here says what is on the wire. **Fan-out:** unknown. **The far end declares it and names
    this area**: the posterior cingulate entry's Inputs read "posterior parietal (action / spatial),
    precuneus, medial temporal lobe / hippocampal formation, anterior thalamus, ACC / MCC" —
    untyped there. **Owed at file 17: type it.**
  - **→ the angular gyrus** — **payload unknown — owed.** **Fan-out:** unknown. **The consumer is in
    this file** and now declares this edge, also owed there.
  - **→ the medial intraparietal area** — **carries:** payload **owed**. **Fan-out:** unknown.
    **Asserted at the consumer's end, in this file**, among the tracer-demonstrated afferents to the
    reach region. **Written at this end so the edge has two ends.** *(Class 1 at the
    consumer's end — eNeuro 4:ENEURO.0344-17, 2017, macaque. Not yet verified for
    the source.)*
  - **→ medial prefrontal cortex and the medial temporal lobe** — **payload unknown — owed.**
    **Fan-out:** unknown. **Neither far end was found to declare it.** The orbitofrontal /
    ventromedial prefrontal entry's Inputs (file 11) name the amygdala, gustatory and olfactory
    cortex, inferotemporal / temporal cortex, the basal-ganglia limbic loop and mediodorsal
    thalamus — not this area; the hippocampal formation's Inputs (file 8) name neocortical
    association areas as a class. **Owed as cross-file edits at both (files 8 and 11).** **Splitting
    this line is owed.** *(A single "→ the default-mode network" line would name four targets and
    type none of them.)*
  - **→ superior parietal area 5 and premotor cortex**, from the anterior sensorimotor sector —
    **carries:** reach and body-configuration signals, body-centred — the one edge out of this entry
    whose payload *can* be written, and it is the one coupled to area 5 rather than to the
    default-mode network. **Fan-out:** unknown. **The area-5 end agrees and names this area**: the
    superior parietal area 5 entry's Inputs declare "← the precuneus, from its anterior sensorimotor
    sector — carries: reach and body-configuration signals, body-centred," transcribed there from
    this entry's declaration, with a primary source. **The agreement certifies
    nothing** — that end was transcribed from this one. **The premotor end declares nothing**: the
    premotor entry's Inputs name posterior parietal as a class without naming this area. **Owed as a
    cross-file edit at the premotor entry (file 11).** **Splitting this line is owed.**
    *(Class 1 at the area-5 end — Bakola et al. 2013, macaque.)*
- **Internal structure and internal data flow:** *(**Absent
  entirely**. **Nothing here is verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. Granular
  medial association isocortex. *(Class 3.)*

  **Divisional sub-elements: three functional sectors, and the entry's own Function field names
  them** — an **anterior sensorimotor sector** (reach, area-5 coupled), a **central cognitive /
  default-mode sector**, and a **posterior visual sector** (occipital-coupled). *(Class 1 — Cavanna
  & Trimble 2006, as cited in this entry's Function.)*

  **The sectors sort this entry's edges, and that is what makes them load-bearing rather than
  descriptive.** The Outputs slot already assigns one edge to a sector by name — the area-5 and
  premotor edge leaves from the anterior sensorimotor sector — and it is the only edge in the entry
  whose payload can be written. **The correlation is exact and worth stating plainly: the one sector
  with a sensorimotor coupling is the one sector whose payload is typed, and the default-mode
  sectors account for every owed payload in the entry.** That is not a coincidence about this region
  so much as a statement about where the source's decoding stops. **Which sector each remaining edge
  reaches or leaves from is owed.** *(Class 2 — the sorting is Claude's reading of this entry's own
  Function and Outputs fields, offered to be checked.)*

  **A separate architectonic division exists and does not obviously align with the three sectors.**
  This entry's heading names **areas 7Am and 7Pm** alongside area 7m / PGm — an anterior/posterior
  architectonic pair against a three-sector functional gradient. **Two schemes over one piece of
  cortex, and this file has no basis for choosing**; both are recorded, as at the medial
  intraparietal area. **Owed: establish whether 7Am and 7Pm are the anterior and posterior sectors
  under other names, or a cross-cutting division.**

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — between the sectors: owed.** No edge between any two of the three sectors is
  recorded, in either direction. The entry's Function claims scene construction and visuospatial
  imagery, which would have to combine the posterior visual sector's content with the central
  sector's retrieved episodic content — **so an inter-sector edge is demanded by the stated function
  and is not recorded anywhere.** This is a **dangling requirement** in the payload rule's sense, and
  it is the fifth in this file.
- **Neurons:** soft/unknown — no clean human per-area count; a large medial-parietal
  association territory.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

**The posterior-parietal remainder is described:** the two intraparietal sensorimotor channels
(the anterior intraparietal area→F5 grasp; the medial intraparietal area / V6A→dorsal premotor
cortex reach) closing onto the already-described premotor / primary motor cortex and joining the
ventral and lateral intraparietal areas; the inferior parietal lobule association cortex
(supramarginal Brodmann area 40 and angular Brodmann area 39, incorporating the macaque 7a/7b
homology) as ventral-attention and
default-mode / semantic nodes; and the precuneus as a default-mode hub. Neuron counts for the
association areas remain the open gap — no clean human per-area stereology, as with prefrontal
cortex.

**Two findings are about the source rather than about this file, and are recorded here because this
is where they surfaced.** First, **three regions this
file's edges point at have no entry anywhere in the seven files checked** — V6, the two subdivisions
of V6A, and the caudal intraparietal area — and one of them is named in this file's own section
head as the origin of the reach channel. Second, **no edge from the ventral stream into the
parietal lobe is declared at any producer**: two entries here (the anterior intraparietal area and
the angular gyrus) declare an input carrying object identity from occipitotemporal cortex, and the
inferotemporal entry names no parietal target at all.

---

---

## References

*(Section under source design §2a: the citing line carries the key, and the authors, journal,
volume, pages and method sit here. Species stays inline, where the entries argue from it. Every
line below is a **candidate** awaiting Micky's verification; none is verified. **1 line carries a
reference obtained by a web search.** The rest read **owed**: what follows the key on those lines is
**transcribed from this file's own citing lines**, not from any record, and a transcribed line is
not a searched one. **No line here carries a line number.** A pointer into the file goes stale on
the next edit and fails silently, so the section is joined to the entries by the key alone.)*

**27 distinct keys, 48 mentions. 1 searched; 26 owed.**

**Three keys name a source that cannot be looked up from what the file holds.** *Andersen* and
*Galletti* are **bare surnames with no year at all**, each appended to a list of properly formed
keys, and each pointing at a body of work rather than a paper. The third, *Cabeza*, is cited once as a bare surname and once as *the Cabeza "attention-to-memory" lineage*, which names a lineage explicitly and has the same defect in a more honest
form. **The repair is naming the paper the citing claim rests on, and it belongs at the line making
the claim.**

**One key carries most of this file.** *eNeuro 4:ENEURO.0344-17, 2017* is cited at thirteen places
across three entries — it is the retrograde-tracer study the medial intraparietal entry's whole
input list derives from, and the single most load-bearing citation here. It is also the only
searched line in this section. **It was written two ways** — once as a bare *eNeuro 2017* — which
defeats the string match this section is built on; it now reads one way throughout.

**Six keys are inherited from file 5 rather than sourced here.** *Ferraina & Bianchi 1994*,
*Lacquaniti et al. 1995*, *Kalaska 1996*, *Graziano et al. 2000*, *Bremner & Andersen 2012* and
*Ferraina et al. 2009* all sit inside the contested-frame block at the medial intraparietal entry,
which states that the dispute is recorded in full at the superior parietal area 5 entry. They are
keys of this file under §2a's per-file rule and are listed, but their far end is a passage in
another file, and repairing any of them there should propagate here.

- **Andersen** — **owed**: not searched.
- **Bakola et al. 2010** — Bakola, Gamberini, Passarelli et al., Cerebral Cortex 20:2592, 2010; macaque. **owed**: not searched.
- **Bakola et al. 2013** — Bakola, Passarelli, Gamberini et al., J Neurosci 33:6648, 2013; macaque; retrograde tracing into architectonically defined area PE. Written in full author form at one citing line and as the *et al.* key at another; now one way in both. **owed**: not searched.
- **Borra et al. 2008** — Borra, Belmalih, Calzavara, Gerbella, Murata, Rozzi & Luppino, Cerebral Cortex 18:1094, 2008; retrograde tracer; macaque. Located by web search, abstract only. The same key is used in file 1. **owed**: not searched.
- **Bremner & Andersen 2012** — **owed**: not searched.
- **Cabeza** — The "attention-to-memory" lineage; **no year at any citing line**, and the file writes it as a bare surname at one place and as *the Cabeza "attention-to-memory" lineage* at the other. **owed**: not searched.
- **Caspers et al. 2008** — Human cytoarchitecture. **owed**: not searched.
- **Cavanna & Trimble 2006** — **owed**: not searched.
- **Corbetta & Shulman 2002** — **owed**: not searched.
- **eLife 9:e55979, 2020** — Receptor autoradiography; macaque. The same key is used in files 1 and 4. **owed**: not searched.
- **eNeuro 4:ENEURO.0344-17, 2017** — Bakola, S., Passarelli, L., Huynh, T., Impieri, D., Worthy, K.H., Fattori, P., Galletti, C., Burman, K.J. & Rosa, M.G.P. (2017). Cortical afferents and myeloarchitecture distinguish the medial intraparietal area (MIP) from neighboring subdivisions of the macaque cortex. *eNeuro*; doi 10.1523/ENEURO.0344-17.2017; PMC5779118; published 8 December 2017. **Macaque.** *(PubMed Central record, found incidentally while searching file 07. **The volume and article number written inline as 4:ENEURO.0344-17 were not separately confirmed** — the record gives the digital object identifier without them.)* A note on the bare key *Galletti*: *Galletti*, the bare surname cited there with no year, is an author on this paper — which does not resolve that key, since a surname still names no paper, but it is where a repair would start. *(searched; candidate.)*
- **Ferraina & Bianchi 1994** — **owed**: not searched.
- **Ferraina et al. 2009** — Ferraina, Brunamonti, Giusti et al., J Neurosci 29:11461, 2009. **owed**: not searched.
- **Galletti** — **owed**: not searched.
- **Graziano et al. 2000** — **owed**: not searched.
- **Hyvärinen 1981** — **owed**: not searched.
- **Jeannerod et al. 1995** — **owed**: not searched.
- **Johnson et al. 1996** — **owed**: not searched.
- **Kalaska 1996** — **owed**: not searched.
- **Lacquaniti et al. 1995** — **owed**: not searched.
- **Murata et al. 2000** — **owed**: not searched.
- **Niu et al. 2021** — **owed**: not searched.
- **PMC8266221** — Tracer plus diffusion tractography; macaque. **owed**: not searched.
- **Rizzolatti & Luppino 2001** — **owed**: not searched.
- **Snyder, Batista & Andersen 1997** — **owed**: not searched.
- **Taira et al. 1990** — **owed**: not searched.
- **Vogt & Vogt 1919** — **owed**: not searched.
