# Brain architecture — 15 cranial nerve nuclei

**Date:** 2026-08-23
**Derived from:** `human_brain_15_cranial_nerve_nuclei_2026_07_25.md` — four entries covering the
ocular motor nuclei, the branchiomotor and visceromotor pools, the trigeminal sensory complex, and
the pretectum with the gaze-integrator cell groups. **One source file, and no other content source.**

*One input was not re-read this session and is named rather than glossed:* `Brain_architecture_design_2026_07_27.md`
was handed over and **was not read in full on this pass**, because the session's budget went to the
source file and to four other deliverables. The template, the four shape classes, the bundle rule,
the *to derive* / *not applicable* distinction and the do-not-repair-the-source rule are applied from
the two architecture files written against that spec in prior sessions. **If a field name or a rule
has changed since, this file will not reflect it, and that is a real risk rather than a formality.**

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed.

- `02_auditory_pathway`, `14_brainstem_midbrain_hypothalamus`. **Nine shared edges
  diffed and stemmed. Four two-ended; the acoustic reflex found to be declared at both ends of another
  file and at neither end of the middle stage, which is here; and **this file found to hold, inside a
  bundled entry, the relay that `14_brainstem_midbrain_hypothalamus` records as having no entry
  anywhere**.**
- `10_cerebellum`. **Diffed end to end at that rung, and it carries no edge into this file. The
  cerebellar term of the four-producer bullet at the ocular motor entry has no producer there: no
  entry in that file declares any output reaching this section, so the term is consumer-only from
  this side and unsupported from the other.** **The bullet's split-by-producer is owed here**, and
  the cerebellar term is the one of the four now known to have no far end.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number**, where the far
file has been read against this one. An endpoint with no stem is one whose far end has not been opened
beside this file, and it is not a claim that none exists.

**Counting basis: per side**, following the source's own convention for this section — these are
paired bilateral nuclei. **One entry breaks it**: the spinal accessory nucleus is upper cervical
cord, gathered here for the nerve rather than for its location.

**Twenty-four edges — 13 in, 10 out, and 1 internal.** The internal edge is the only one in the
section, and it is the only edge in the section that crosses the midline.

**This is the section where the map exits the nervous system.** Six endpoints are **peripheral**:
extraocular and orofacial striated muscle, the ciliary ganglion, the cranial parasympathetic ganglia,
the trigeminal ganglion, and the jaw-muscle spindles and periodontal receptors. The source records
each as a **terminus rather than an owed edge**, and that treatment is carried unchanged. Everywhere
else in the map a well-formed edge pointing at nothing is a defect; here it is the boundary.

**All four entries are bundles**, which is a higher rate than anywhere else in the map: three motor
nuclei plus a visceral subnucleus; **eight** motor pools spread from pons to upper cervical cord;
three trigeminal nuclei of which one subdivides further; and — the extreme case — **two structures
that share no edge with each other**, gathered by anatomical neighbourhood rather than by data flow.
The source marks the split owed at every one of them. Per §6 none is split here, because splitting
invents the arity.

*A transcription cross-check.* The source's header states **24 edge lines — 13 in, 10 out, 1
internal**, and transcription agrees, with one subtlety worth recording because it is the second
instance of a pattern: **one of the thirteen incoming bullets is explicitly not a typed edge.** The
ocular-motor entry lists the superior colliculus and frontal eye fields among its inputs and then says
in the same bullet that there is **no direct edge** — the route reaches this nucleus only through the
burst generators. It is a recorded *absence* of an edge, occupying an edge line. File 14's lateral
parabrachial entry has the same shape, a bullet in an Inputs list that names no producer. **Two files,
two bullets that are not edges, both in Inputs lists**, and a mechanical count that does not know the
difference will drift by one each time.

---

## Structural invariants

**Whole-pathway co-instantiation.** All four structures exist and are active from the outset, and
**this section is where the oculomotor loop finally closes onto its effector.** The lateral
intraparietal area, the frontal eye field and the superior colliculus all pointed at a motor
terminus; it is here, and the last stage before muscle is the abducens and oculomotor pools. The loop
is now traceable end to end **except for one joint**: the burst generators that drive these pools are
sub-elements of file 14's reticular formation, whose sub-element boundaries are partly uncountable,
and file 14 names the cranial-nerve motor nuclei only as a class. **The source records that as owed at
file 14, and it is inherited here rather than repaired.**

A second loop closes wholly inside this file and is worth naming because it is the smallest complete
loop in the map: **jaw-muscle spindle → mesencephalic nucleus → trigeminal motor nucleus → jaw
muscle**. Two stages, monosynaptic, both ends peripheral. The pupillary light reflex is nearly as
short — retina → olivary pretectal nucleus → Edinger-Westphal nucleus → ciliary ganglion → sphincter
pupillae — and three of its four joints are in this file.

**Per-edge latency.** Every edge carries a nonzero, finite, heterogeneous latency in real time units,
and **this section can name none of them: every latency reads *to derive*.** No conduction time and
no synaptic delay appears anywhere in file 15.

**Two edges carry a stated timing requirement with no number, and one of them is the tightest in the
map.** The vestibulo-ocular reflex is described at the source as **the fastest gaze-stabilising
reflex**, and its whole function is to produce an eye-velocity signal equal and opposite to head
rotation — which is a requirement that the loop's total delay be short enough that the correction has
not gone stale. And the jaw-jerk is **monosynaptic**, which is a latency claim expressed as an
anatomical one: one synapse is the floor. **Neither has a figure**, so the section states the
constraint that would size a scheduler and does not supply the parameter.

**There is no global clock.** Nothing in this section supplies a period, and the one structure that
might look like it does — the gaze integrator — is the opposite of a clock: it holds a value *still*.

**A new endpoint class appears, and it is not the same as file 14's.** File 14 recorded an endocrine
terminal: an edge with a producer, a payload, and **no target region at all**. This section records a
**motor terminus** and a **peripheral sensory source**, which are different — they have a definite,
named, single target or origin (the lateral rectus; the trigeminal ganglion) that is simply **outside
the scope boundary by rule**. The distinction matters for a build: an edge to nowhere has no consumer
to write, while an edge to a named out-of-scope effector has a well-defined interface that a later
rung must supply. *(That the two are different classes is Claude's reading; both treatments are
Class 1 from the source.)*

---

## Ocular motor nuclei

- **Function → structure.** The somatic-motor **final common path for eye movement**, plus
  parasympathetic pupil control — **the motor terminus of the oculomotor loop**, the place where a
  gaze command becomes muscle innervation. Four sub-elements gathered by shared function rather than
  by neighbourhood: the **oculomotor nucleus** (cranial nerve III, midbrain) driving four of the six
  extraocular muscles and the levator palpebrae; its visceral partner the **Edinger-Westphal
  nucleus**, holding the parasympathetic preganglionics for pupillary constriction and lens
  accommodation; the **trochlear nucleus** (cranial nerve IV, midbrain) driving the superior oblique,
  **the only cranial nerve that is crossed and exits dorsally**; and the **abducens nucleus** (cranial
  nerve VI, pons) driving the lateral rectus and, through its **internuclear neurons**, yoking the two
  eyes for conjugate horizontal gaze. **The oculomotor nucleus and the Edinger-Westphal are
  contiguous; the trochlear and abducens sit at different brainstem levels** — so this entry's
  sub-elements are not even co-located.
- **Inputs.**
  - **← the brainstem saccade burst generators** — the **paramedian pontine reticular formation**
    (horizontal → abducens) and the **rostral interstitial nucleus of the medial longitudinal
    fasciculus** (vertical → oculomotor and trochlear) — **a timed burst driving eye muscles**, the
    pulse that moves the eye, **in temporal (rate) code**. This is the output side of the
    spatial-to-temporal conversion the superior colliculus performs. Fan-in: to derive.
    **Checked 2026-08-14, and the state is better at the producer than this line assumed and worse in
    one respect.** `14_brainstem_midbrain_hypothalamus` **names both generators as sub-elements of its
    reticular formation, by the same two names** — the paramedian pontine reticular formation and the
    rostral interstitial nucleus of the medial longitudinal fasciculus — **so the producers are named
    structures there and not merely implied.** Its superior colliculus additionally declares
    `→ the brainstem saccade burst generators, from the intermediate and deep layers`, and its
    reticular formation entry records that the generators are its own sub-elements, so **that loop
    closes inside that file.**
    **What remains owed is narrower and unchanged in force:** the reticular formation's only output
    toward this section is `→ cranial-nerve motor nuclei`, **a class**, payload owed there as here.
    **So the producers are named and the edge to this entry is not.** The far end records that the
    individual nuclei are described in this file. **Owed at the source, at that file: split the class
    to the pools each generator drives**, which this entry's axis assignment — horizontal to abducens,
    vertical to oculomotor and trochlear — already supplies.
  - **← the gaze neural integrators** — the **nucleus prepositus hypoglossi** (horizontal) and the
    **interstitial nucleus of Cajal** (vertical) — an eye-**position** command, **the time integral of
    the velocity command**, the signal that holds the eye still between saccades. Fan-in: to derive.
    Two-ended within this file.
  - **← the vestibular nuclei**, via the **medial longitudinal fasciculus** — the **vestibulo-ocular
    reflex command**: an eye-velocity signal equal and opposite to head rotation, driven chiefly by
    the semicircular-canal line, **the fastest gaze-stabilising reflex**. Fan-in: to derive.
    Two-ended against file 3, and the tract has an entry in file 18.
  - **← the superior colliculus and frontal eye fields** — **and this is a recorded absence, not an
    edge.** The saccade goal reaches this nucleus **only through** the burst generators, not
    monosynaptically. The source states it explicitly so that the loop those entries traced is not
    read as terminating here directly.
  - **← the pretectum**, onto the **Edinger-Westphal nucleus** — the **pupillary light reflex** drive:
    a luminance scalar as a drive to constrict, **monosynaptic, excitatory and bilateral** — the
    source of the consensual response. Fan-in: to derive. Two-ended within this file.
- **Outputs.**
  - **→ the extraocular muscles** and the levator palpebrae — the motor command to the eye muscles,
    the terminus of the oculomotor loop. Fan-out: to derive. **Peripheral striated muscle: a motor
    terminus, not an owed edge**, the same treatment the spinal ventral horn's output gets.
  - **→ the ciliary ganglion**, from the **Edinger-Westphal nucleus** → sphincter pupillae and
    ciliary muscle — the parasympathetic preganglionic command for pupil constriction and lens
    accommodation. Fan-out: to derive. **A peripheral autonomic terminus.**
- **Internal edge — the only one in the section, and the only midline crossing.** **Abducens
  internuclear neurons → the contralateral oculomotor medial-rectus pool**, ascending in the medial
  longitudinal fasciculus — the **yoking signal**. What travels is **a copy of the drive the abducens
  is already sending to its own muscle**, carrying **no independent command**, which is why a lesion
  of the tract produces internuclear ophthalmoplegia: adduction fails, abduction survives, and the
  eyes come apart. Fan-in and fan-out: to derive. *(The reading that the payload is a copy rather than
  an independent command is marked at the source as Claude's, offered to be checked.)*
- **Sizing.** Basis: **per side.** **Soft** — the extraocular somatic-motor pools are small, order
  **10³–10⁴ per side**, with no clean human absolute count; the Edinger-Westphal is a small
  visceromotor group. Every fan-in unknown, so the width is the 16-bit bound and the store is **to
  derive for want of a count**. At the top of the stated order the whole entry would be tens of
  thousands of neurons and well under a megabyte, but that is an order and not a figure, and the
  architecture does not promote it.
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-element, N)** with four sub-elements —
  oculomotor, trochlear, abducens, Edinger-Westphal. **The sub-elements are load-bearing and the edges
  prove it**: the burst-generator and integrator inputs segregate by axis, horizontal to abducens and
  vertical to oculomotor and trochlear, and the light-reflex input goes specifically to the
  Edinger-Westphal. **N to derive for every one of them.** No map axis is recorded — and note that a
  motor pool plausibly has one, since muscles are discrete and a motoneuron pool maps to a muscle, but
  the source records no such axis and the architecture does not invent it.
- **Edge latency.** All seven edges **to derive**, including the vestibulo-ocular limb whose stated
  property is that it is the fastest reflex of its kind.
- **Invariant conformance.** Co-instantiation: satisfied for the joints present; the loop closes onto
  muscle here, and its remaining open joint is the class endpoint at file 14. Per-edge latency:
  satisfied, all to derive.
- **Justification (biological).** **The payload arriving here is a rate and the payload arriving two
  stages back was a place**, and this entry is where that conversion has already happened. The
  superior colliculus specifies a saccade by *where* its active population sits; the burst generators
  turn that into *when and how hard*; this nucleus receives the second form only. **An implementation
  that carried the place code all the way to the muscle would have skipped a computation the source
  names**, and the entry that would have skipped it is this one.
  The yoking edge is the cleanest instance in the map of a payload that is **a copy rather than a
  command**, and it has a build consequence: the medial-rectus pool must not be given an independent
  input that could disagree with the lateral-rectus drive, because the whole point of the edge is that
  the two cannot disagree.

## Branchiomotor and visceromotor nuclei

- **Function → structure.** The motor pools for jaw, face, throat, tongue and viscera — **the orofacial
  and cranial-parasympathetic motor terminus**, counterpart of the spinal ventral horn and the spinal
  intermediolateral sympathetic column. **Eight sub-elements**: **trigeminal motor** (cranial nerve V,
  pons, mastication); **facial** (cranial nerve VII, pons, facial expression and stapedius, carrying
  the clinical upper-face-bilateral / lower-face-contralateral rule); **nucleus ambiguus** (cranial
  nerves IX, X and XI, medulla, pharyngeal and laryngeal muscle plus cardioinhibitory vagal
  preganglionics); **superior and inferior salivatory nuclei** (cranial nerves VII and IX); **dorsal
  motor nucleus of the vagus** (cranial nerve X, medulla — **the largest parasympathetic preganglionic
  source of the lower brainstem**); **hypoglossal** (cranial nerve XII, medulla, tongue); and **spinal
  accessory** (cranial nerve XI, **upper cervical cord**, sternocleidomastoid and trapezius).
- **Inputs.**
  - **← the cerebral cortex**, via the **corticobulbar tract** through the internal-capsule genu — the
    voluntary motor command for jaw, face, larynx and tongue, the cranial analogue of the
    corticospinal command. **The facial pool carries the clinical rule on this edge**: upper-face
    motoneurons receive bilateral input, lower-face contralateral only. Fan-in: to derive. **This
    endpoint names a class**, and **the corticobulbar tract has no entry of its own** — file 18 holds
    the internal capsule, which names corticobulbar fibres through the genu as one of the systems it
    routes. The source checked this across all twenty files on 2026-07-25 and corrected a prior claim
    that the tract had an entry. Inherited.
  - **← the nucleus of the solitary tract** (gag, swallow, baroreflex loops) — the **afferent limb of
    vagal reflexes**; payload otherwise **owed**. Fan-in: to derive. Two-ended against file 14.
  - **← the spinal trigeminal nucleus** (corneal and jaw reflexes) — payload **owed**. Fan-in: to
    derive. Two-ended within this file.
  - **← the reticular premotor pattern generators** (`14_brainstem_midbrain_hypothalamus`) for
    chewing, swallowing, respiration and vocalisation — the **rhythmic motor pattern** that sequences
    these pools; payload **owed**. Fan-in: to derive. **Two-ended and confirmed 2026-08-14, payload
    owed at both ends**, the producer declaring `→ cranial-nerve motor nuclei` and typing it as the
    premotor sequencing signal for saccade bursts, chewing, swallowing and facial/laryngeal patterns.
    **It names these pools only inside a class and records that the individual nuclei are described
    here.** **Owed there; inherited.**
  - **An auditory input to the facial pool is declared at both ends of another file and at neither end
    here. Found 2026-08-14.** `02_auditory_pathway`'s superior olivary complex declares
    `→ the acoustic-reflex arc (stapedius) — a loudness-triggered attenuation command`, and that
    file's cochlea entry declares `← branchiomotor / visceromotor nuclei, indirectly via the stapedius
    muscle`, **naming this entry by its heading.** **So that file declares the drive into the reflex
    and the consequence out of it, and names this entry as the stage between — while this entry
    declares no auditory input at all.**
    **This entry does carry the efferent half.** Its Function field names the facial nucleus as driving
    **stapedius**, and its output line to orofacial striated muscle includes it. **What is missing is
    the afferent limb: nothing here says what makes the stapedius fire.**
    **The producer's endpoint is part of why.** It names `the acoustic-reflex arc`, **which is an arc
    and not a structure** — a route rather than a consumer — so an endpoint that should have landed on
    this entry landed on a description of the loop instead. **A structure with an entry was addressed
    by the name of the circuit it belongs to.**
    **Not written in**, because writing the edge on the far end's declaration alone would assert a
    projection this section has read nothing for. **Owed at the source: declare the superior olivary
    complex's drive onto the facial motor nucleus here, or retype the producer's endpoint to name this
    pool.** **The far file has been given the finding from this side.**
- **Outputs.**
  - **→ the orofacial striated muscle** — mastication, facial expression and stapedius, pharynx and
    larynx, tongue, sternocleidomastoid and trapezius — the final common path for chewing, facial
    expression, swallowing, phonation and speech articulation. Fan-out: to derive. **A motor terminus.**
  - **→ the cranial parasympathetic ganglia**, from the dorsal motor nucleus of the vagus, the nucleus
    ambiguus and the salivatory nuclei — the **cranial (vagal) parasympathetic outflow**, counterpart
    of the spinal intermediolateral sympathetic column; payload otherwise **owed**. Fan-out: to
    derive. **A peripheral autonomic terminus.** *(The cardioinhibitory vagal outflow is the efferent
    limb of the baroreflex whose afferent limb arrives from the solitary nucleus above — so the
    baroreflex loop closes across this entry, having had its inhibitory and excitatory limbs described
    in file 14.)*
- **Sizing.** Basis: **per side.** **The facial motor nucleus is ~10,000 per side — the one firm human
  count in this section**, from a comparative-anatomy review resting on a 1965 human quantitative
  source, and **corroborated by the matching myelinated-axon count of the facial nerve**. At the
  16-bit fan-in bound that is **≤ 0.02 MB per side**. The other somatic-motor pools (trigeminal motor,
  hypoglossal) are the **same order**, 10³–10⁴ per side and soft; the visceromotor pools (salivatory,
  dorsal motor vagus, ambiguus) are soft, the dorsal motor vagus the largest. **Structure total: to
  derive**, seven of eight sub-elements uncounted.
  **The corroboration is worth naming as a method.** A motor nucleus is the one kind of structure
  whose neuron count has an independent physical check: every motoneuron sends one axon out a named
  nerve, so counting myelinated axons in the nerve counts the pool. **That is the only cross-check in
  the map so far that closes against a different measurement rather than against a second statement of
  the same one**, and it is available in principle for every pool in this entry. *(Claude's reading of
  why the corroboration works; the corroboration itself is Class 1 from the source.)*
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-element, N)** with eight sub-elements. Extents:
  ~10,000 for the facial nucleus per side, **to derive for the other seven**. **The sub-elements are
  load-bearing and the source says the split matters more here than usual**: the inputs target specific
  pools — corticobulbar to the facial with its bilateral/contralateral rule, solitary to the dorsal
  motor vagus, pattern generators to the rhythmic pools — and the pools have very different clinical
  signatures. **No internal edge among them is described, and the source judges that few exist**:
  these are parallel effectors, not a chain, and the reflex arcs that connect them run *through* the
  sensory entries rather than within this one.
- **Edge latency.** All six edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; the solitary-nucleus input closes against
  file 14, the trigeminal input within this file, and both outputs terminate peripherally. Per-edge
  latency: satisfied, all to derive.
- **Justification (biological).** **The bilateral/contralateral facial rule is a connectivity fact
  carried on a payload line, and the architecture has to keep it there.** It says that one sub-element
  of one pool receives from both hemispheres and the rest of the pool from one — a statement about
  `fan_in`, not about what the wire carries, arriving in a Function field because that is where
  clinical anatomy states it. **An architecture that recorded only "cortex → facial nucleus" would
  lose the one detail on this edge that a build could get wrong**, and the rule is why upper-face
  weakness distinguishes a brainstem lesion from a cortical one.

## Trigeminal sensory complex

- **Function → structure.** The **face's somatosensory column**, the cranial counterpart of the
  dorsal-column / anterolateral split. Three sub-elements: the **principal (pontine) nucleus** taking
  discriminative touch; the **spinal trigeminal nucleus**, descending into the upper cervical cord,
  taking **pain and temperature** from the face; and the **mesencephalic nucleus**, which is **a
  singular exception in the whole nervous system** — its cells are **primary sensory neurons whose
  somata sit inside the central nervous system, the only ones in the body**, carrying jaw-muscle-spindle
  proprioception and periodontal mechanoreception, with a monosynaptic reflex onto the trigeminal
  motor nucleus. The spinal nucleus subdivides further into **pars oralis, interpolaris and caudalis**,
  with pars caudalis the pain-and-temperature part **continuous with the spinal dorsal horn**.
- **Inputs.**
  - **← the trigeminal ganglion**, onto the **principal** and **spinal** nuclei — face somatosensation
    **split by submodality at the point of entry**: discriminative touch to the principal nucleus,
    pain and temperature to the spinal nucleus, the cranial mirror of the dorsal-column /
    anterolateral separation. Fan-in: to derive. **The trigeminal ganglion is the peripheral
    first-order sensory ganglion** — a peripheral sensory source, the afferent counterpart of a dorsal
    root ganglion, not an owed edge.
  - **← the jaw-muscle spindles and periodontal receptors**, as the **mesencephalic nucleus's own
    peripheral processes** — jaw-muscle-spindle proprioception and periodontal mechanoreception.
    **This is not a synaptic input.** The mesencephalic cells *are* the primary sensory neurons, with
    somata inside the central nervous system and a peripheral process reaching the receptor, **so the
    "input" is the cell's own dendrite and not an edge from another region.** Recorded as a
    primary-afferent terminus with no producer region.
- **Outputs.**
  - **→ the ventral posteromedial thalamus** via the trigeminothalamic tract, from the **principal**
    and **spinal** nuclei, onward to the primary somatosensory cortex face representation — face
    somatosensation, **the two submodalities kept separate**. Fan-out: to derive. **Two-ended for the
    pain-and-temperature limb** against file 12; **owed for the discriminative-touch limb**, pending
    confirmation that file 5's ventral posteromedial entry names the principal nucleus.
  - **→ the trigeminal motor nucleus**, from the **mesencephalic nucleus** — the **jaw-jerk reflex**:
    a monosynaptic proprioceptive reflex, jaw-muscle stretch driving jaw-muscle contraction. Fan-out:
    to derive. Two-ended within this file.
  - **→ the branchiomotor pools** (corneal blink and jaw-opening reflexes), from the **spinal**
    nucleus — the afferent limb; payload **owed**. Fan-out: to derive. Two-ended within this file.
- **Sizing.** Basis: **per side.** **Soft throughout.** The mesencephalic nucleus is a small
  distinctive population, order **10³**, uncounted cleanly in human; the principal and spinal nuclei
  are the relay recorded soft at the sensorimotor-loop entry. Zero derivable parameter memory, a gap.
- **Shape.** **Non-laminated nucleus**, and it wants **rank 3: (sub-element, sub-division, N)** —
  three nuclei, with the spinal one further divided into pars oralis, interpolaris and caudalis. The
  sub-elements are load-bearing: **each output edge leaves from a specific one.** N to derive
  everywhere.
  **And one sub-element does not belong to this shape class at all.** The mesencephalic nucleus holds
  **transducers**, not threshold gates: under the §6 model a transducer stores no threshold and the
  log₂ cost does not apply. **But these transducers also project monosynaptically**, which the
  retina's photoreceptors do not. So the section contains a cell that is a primary afferent and a
  projection neuron at once, and **the element-class vocabulary — transducer, threshold gate, graded
  non-spiking — assigns it to one class while its edges require another.** *(Claude's reading; the
  singular-exception status of the nucleus is Class 1 from the source.)*
- **Edge latency.** All five edges **to derive**, and one carries its latency claim as anatomy: the
  jaw-jerk is **monosynaptic**, which sets a floor without naming it.
- **Invariant conformance.** Co-instantiation: satisfied, and this entry closes **the smallest complete
  loop in the map** — jaw-muscle spindle → mesencephalic nucleus → trigeminal motor nucleus → jaw
  muscle, two central stages with both ends peripheral. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **Submodality separation is done before the first synapse and is
  maintained through the relay**, which is a structural claim rather than a functional one: the
  architecture cannot merge the principal and spinal nuclei into one face-touch stage without
  destroying a split the periphery already made. That the split mirrors the body's dorsal-column /
  anterolateral organisation, in different tissue and on a different nerve, is the strongest evidence
  in the section that the separation is architectural rather than incidental.

## Pretectum and gaze-integrator tegmental cell groups

- **Function → structure.** **Two structures that share no edge with each other**, gathered by
  anatomical neighbourhood rather than by data flow, and the source states so plainly and marks the
  split owed.
  The **pretectum** is the sensory limb of the **pupillary light reflex**: its **olivary pretectal
  nucleus** receives a minority of retinal ganglion cells and projects to the **Edinger-Westphal
  nucleus bilaterally** — hence the consensual response. **This is the third non-image-forming retinal
  target in the map**, alongside the suprachiasmatic nucleus (circadian) and the superior colliculus
  (orienting). **What it computes is a scalar, and the computation is spatial integration**: its cells
  are tonic on-centre **luminance neurons with very large receptive fields, a mean of about 31°**,
  driven by broad-field melanopsin-containing ganglion cells. **The payload change is dimensional** —
  a spatially resolved retinal signal arrives and a single number leaves.
  The **gaze integrators** are the **velocity-to-position** cell groups that hold the eye at an
  eccentric position between saccades: the **nucleus prepositus hypoglossi** with the medial vestibular
  nucleus (horizontal) and the **interstitial nucleus of Cajal** (vertical).
- **Inputs.**
  - **← retina, onto the olivary pretectal nucleus** — **ambient luminance as a scalar**: a slow,
    broad-field measure of light falling on one eye. **Does not carry** hue, form, motion, or a usable
    eye of origin. The chiasm's split applies, temporal retina ipsilateral and nasal contralateral, at
    **nearly equal density** in macaque. Fan-in: **to derive, but high by construction** — retinal
    terminals concentrate inside the nucleus's borders and the projection cells' dendrites branch
    heavily through that core, which is the stated substrate for the very large receptive fields.
  - **← superior colliculus** (`14_brainstem_midbrain_hypothalamus`)**, frontal eye fields, vestibular
    nuclei and cerebellum**, onto the **integrators and burst generators** — payload **owed**;
    eye-movement commands and head-velocity signals requiring the position hold. Fan-in: to derive.
    **This bullet names four producers.**
    **Checked 2026-08-14 against the collicular producer, and it splits: two-ended for the burst
    generators, consumer-only for the integrators.** That entry declares `→ the brainstem saccade burst
    generators` and names both by name — **but the burst generators are that file's own sub-elements,
    not this entry's**, so the confirmed limb lands there and not here. **No collicular output to the
    nucleus prepositus hypoglossi or to the interstitial nucleus of Cajal is declared at that end under
    any name.** **So the integrator half of this bullet has no producer end**, and the bullet is
    carrying two different states under one line. **Owed: split this bullet by target**, since the
    producers reach two structures that this entry itself records as sharing no edge with each other.
- **Outputs.**
  - **→ Edinger-Westphal nucleus, preganglionic subdivision, bilaterally**, from the olivary pretectal
    nucleus — the luminance scalar as a **drive to constrict**. **Monosynaptic, excitatory and
    bilateral**, onto a **distinct subpopulation** of preganglionic motoneurons — the pupillary ones,
    not the lens-accommodation ones sharing the nucleus. **The bilaterality is where the consensual
    response comes from, and in macaque it is achieved by this projection rather than by a
    commissure**: tracing found little evidence of a pretectal commissural projection, attributed to
    each retina already supplying both nuclei almost equally. **A quantitative asymmetry carried:**
    pupillary motoneurons receive **more inhibitory input** than the lens motoneurons beside them.
    Fan-out: to derive. Two-ended within this file.
  - **→ intermediate grey layer of the superior colliculus** (`14_brainstem_midbrain_hypothalamus`)**,
    periaqueductal grey, interstitial nucleus of Cajal, and the ventral lateral geniculate /
    intergeniculate leaflet**, from the olivary pretectal nucleus — payload **owed**.
    **The collicular limb is two-ended and confirmed 2026-08-14, and confirming it withdraws a claim at
    the far end.** That entry declares `← olivary pretectal nucleus → stratum griseum intermediale`,
    types it as a luminance scalar arriving in the **premotor rather than the visual** layers by a
    route that is not the retinotectal one, and records that **the two-hop route retina → olivary
    pretectal nucleus → superior colliculus is declared at its origin and its destination with no entry
    anywhere for the relay between them.**
    **The relay has a description, and it is this entry.** The olivary pretectal nucleus is described
    here at full length — its retinal input, its ~31° receptive fields, its shell-of-somata-around-a-
    neuropil-core geometry, and the dimensional payload change from a spatially resolved retinal signal
    to a single number. **That change is exactly the transform the far end says is missing.**
    **What it does not have is a heading.** It is one of two structures inside an entry named for
    neither of them, in a file whose subject is cranial-nerve nuclei — **so a search for a structure
    called the olivary pretectal nucleus finds nothing, and the file that owns it is not the file
    anyone would look in.** **This is the second instance of this failure found today**, after the
    thalamic relay recorded as missing that is a bundled stage in `03_other_senses`. **In both, the
    structure is described, the description is complete enough to be load-bearing, and it is invisible
    because it sits below a heading.**
    **Owed at the source, and it is a decision rather than a repair:** give the olivary pretectal
    nucleus an entry of its own — which this entry's own text already argues for, recording that its
    two structures share no edge and marking the split owed — or record at the far file that the relay
    is described here. **Not split here**, per §6.
    **This bullet names four consumers** and is recorded because
    the entry previously declared **one** output for this nucleus and tracing shows several, ascending
    and descending: **the luminance signal reaches the orienting and circadian machinery as well as the
    pupil.** The tracing is **rat**, with no macaque confirmation read. Fan-out: to derive.
  - **→ the ocular motor nuclei**, from the nucleus prepositus hypoglossi, the interstitial nucleus of
    Cajal and the burst generators — an eye-**position** command, **the time integral of the velocity
    command**. **The payload change is an integration in time**, and it is what holds the eye still
    between saccades. Payload otherwise **owed**. Fan-out: to derive. Two-ended within this file.
    **The tract this edge rides is not stated at either end**, and file 18's medial longitudinal
    fasciculus entry records the integrator limb as general anatomy for exactly that reason. **Owed at
    both ends.**
- **Sizing.** Basis: **per side.** **Soft or unknown throughout** — small, ill-bordered tegmental cell
  groups, uncounted in human. Zero derivable parameter memory, a gap.
  **One of the two is the most countable structure left in this section, and the source says why.**
  The olivary pretectal nucleus **has definite borders in macaque**, its projection cells were
  retrogradely labelled and localised, and **no human figure was searched for in this pass.** That is
  a different state from the file-14 structures whose counts are missing because they have no border:
  here the border exists and the count has simply not been looked up.
- **Shape.** **Two shapes, because this is two structures.**
  The olivary pretectal nucleus is a **non-laminated nucleus** with an internal geometry the source
  describes precisely: **a shell of somata around a core of neuropil**, the projecting cells' somata at
  the periphery with heavily branched dendrites extending into the core where the retinal terminals
  concentrate. **The place a cell's body sits and the place it receives are different**, and the source
  records that this is the same owner/place distinction cortical layer 1 raises — and that, as there,
  **no second internal edge is written for it, because there is no second synapse**: the signal reaches
  the soma by propagation within one cell. So the shape is rank 2, **(cell class, N)**, N to derive,
  **with a radial position that is a property of the dendrite rather than an index into an array.**
  The gaze integrators are **non-laminated nuclei**, rank 2, **(sub-element, N)** — nucleus prepositus
  hypoglossi and interstitial nucleus of Cajal — N to derive. **And their internal circuit is unknown
  at the source**, which matters more than the missing count; see the Justification.
- **Edge latency.** All five edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied for both halves separately, and **there is no
  loop between them** — the entry's two structures do not connect. The pupillary reflex closes through
  the Edinger-Westphal nucleus and the ciliary ganglion; the integrator limb closes through the ocular
  motor nuclei. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **Two payload transformations sit in this one entry, and they pull
  the sizing model in opposite directions.**
  **The first fits the model exactly, and it is worth saying so after two files of gaps.** The olivary
  pretectal nucleus discards spatial resolution by converging a very wide retinal field onto a heavily
  branched dendritic tree, and reports how much light there is. **A count of active inputs over a very
  large fan-in, compared against a threshold, is that computation** — not an approximation of it, the
  thing itself. The receptive-field figure of about 31° is a statement about the size of the fan-in.
  **This is the first structure in the map whose described computation the §6 model expresses without
  extension.** *(Claude's reading; the physiology and the ~31° figure are Class 1 from the source.)*
  **The second does not fit, and it is the strongest finding in this file.** A gaze integrator's whole
  function is to **hold a continuously-valued quantity — eye position — against decay, indefinitely,
  between saccades.** The model's state is **one bit per neuron**, `active`; its parameter is a
  threshold that no rule writes. **Neither holds a value that persists and is read back.** This is the
  first structure in the map whose declared function is to store something, and the source says the
  internal mechanism is unknown and that **"a mechanism that holds a value against decay is exactly
  the kind of thing a lower rung has to build."**
  **A candidate, offered to be checked and not asserted.** Recurrence plus delay plus a sign is the
  same machinery in both directions: with the loop gain and sign parity that oscillate, it is file 14's
  relaxation oscillator; with the parity and gain that latch, it is a held state. **So the integrator
  and the pacemaker may want one addition to the model rather than two**, and that addition is the
  inverting term the sign gap already names. **This is GENERATIVE — a connection offered for checking,
  not a verdict** — and what would test it is whether a held eye position degrades gracefully or not
  at all, which the source does not say. *(Claude's reading throughout this paragraph.)*

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Ocular motor nuclei — all four sub-elements | per side | soft, order 10³–10⁴ | ≤ 16 | to derive |
| Branchiomotor / visceromotor — facial nucleus | per side | ~10,000 | ≤ 16 | ≤ 0.02 MB |
| Branchiomotor / visceromotor — the other seven pools | per side | soft, order 10³–10⁴ | ≤ 16 | to derive |
| Trigeminal sensory — mesencephalic nucleus | per side | soft, order 10³ | 0 (transducer) | to derive |
| Trigeminal sensory — principal and spinal nuclei | per side | soft | ≤ 16 | to derive |
| Pretectum — olivary pretectal nucleus | per side | unknown, **bordered and countable** | ≤ 16 | to derive |
| Gaze integrators — prepositus hypoglossi, interstitial nucleus of Cajal | per side | unknown | ≤ 16 | to derive |
| **stated total** | per side | **~10,000 counted** | | **≤ 0.02 MB per side** |

**Four entries, seven sub-element groups, and one number.** The facial motor nucleus at ~10,000 per
side is the section's only firm human count, giving **≤ 0.02 MB** — the smallest section total in the
map so far, and for the same reason as file 14's: **the structures are not known to be small, they are
not counted.**

**But this section's gaps are more repairable than file 14's, and the difference is worth recording.**
File 14 held three structures defined without a countable border, where a count may not be well posed.
**Every structure here has a border**: they are nuclei defined by a nerve. Two of them have a stated
route to a figure — the olivary pretectal nucleus has definite borders in macaque with its projection
cells already labelled and no human figure yet looked up, and **every motor pool in the section can be
cross-checked against the myelinated-axon count of its own nerve**, which is how the facial figure was
corroborated. **This is the one section in the map whose sizing gap has a named method for closing it.**

## Three findings this file records and does not repair

**The map's first memory is here, and the model has nowhere to put it.** A gaze integrator holds eye
position — the time integral of a velocity command — against decay, between saccades. The model's
state is one bit per neuron and its parameter is a threshold nothing writes; **a value held and read
back is neither.** The source records the internal mechanism as unknown and names it as work for a
lower rung. **A candidate connection, marked generative:** recurrence with delay and a sign gives an
oscillator at one parity and a latch at the other, so this and file 14's pacemaker may need one
addition to the model rather than two — and it is the same inverting term the sign gap has been
asking for since the outer retina. *(Claude's reading; the integrator's function and the unknown
mechanism are Class 1 from the source.)*

**And the model fits a described computation exactly, for the first time.** The olivary pretectal
nucleus converges a very wide retinal field onto a branched dendritic tree and emits a scalar — how
much light. **A count of active inputs over a large fan-in against a threshold is not an approximation
of that computation; it is that computation**, and the ~31° receptive field is a statement about the
size of the fan-in. Recording this matters because three consecutive architecture files have recorded
what the model cannot express, and **a model that only ever fails is not being tested.**

**The map exits the nervous system here, and the exit has a different shape from file 14's.** Six
endpoints are peripheral — muscle, autonomic ganglia, a sensory ganglion, and receptors — and each is
recorded as a terminus rather than an owed edge. **This is not the same as file 14's endocrine
terminal.** An endocrine terminal has a producer, a payload and **no target region at all**; a motor
terminus has a definite named target that is **outside the scope boundary by rule**. The build
consequence differs: an edge to nowhere has no consumer to write, while an edge to a named
out-of-scope effector has a well-defined interface a later rung must supply. **And one input case is
neither** — the mesencephalic nucleus's "input" is its own dendrite, with no producer region because
the cell *is* the receptor, which is a transducer sitting inside the central nervous system and
projecting monosynaptically. **The element-class vocabulary assigns that cell to one class while its
edges require another.** *(Claude's reading of the class distinctions; every underlying treatment is
Class 1 from the source.)*
