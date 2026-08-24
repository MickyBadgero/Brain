# Brain architecture — 05 sensorimotor loop

**Date:** 2026-08-23
**Derived from:** `human_brain_05_sensorimotor_loop` — the dorsal column nuclei and
trigeminal relay, the ventral posterior thalamus, primary and second somatosensory cortex, superior
parietal area 5, and primary motor cortex. **One source file, and no other content source.**

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed below.

- `06_posterior_parietal`, `11_frontal_lobe`. **Thirteen shared edges diffed and stemmed; three
stale marks discharged, two producer-only
  edges confirmed absent at this file's consumers, one class endpoint narrowed onto a named consumer,
  and one in-file asymmetry found while reading the far ends.**
- `10_cerebellum`. **Two shared edges diffed. The cuneocerebellar edge is two-ended and invisible to
  the edge index, because this file names its target as the whole cerebellum where that file's entries
  are the cerebellar cortex, the deep nuclei and the inferior olive. And a consumer-only edge at that
  file is confirmed absent here: its inferior olive declares an input from these nuclei and this entry
  declares no olivary target.**
- `09_basal_ganglia`. **Checked and closed as a negative covering this whole file. That file's
  striatal input line names a class of cortical producers, and of the nine files checked against it
  five cortical entries declare the edge — none of them here. All six entries of this file declare no
  output to the striatum, the primary motor cortex among them**, so the motor sector of that input has
  no producer end at the one region the motor sector is named for. **Owed here: declare the edge or
  record its absence at the primary motor entry**, since a negative this size is a claim about this
  file and is currently written only at the far end.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file is checked against this one; an endpoint with no stem is unchecked, and it is not
a claim that none exists.

**Counting basis: per hemisphere throughout, and one structure is unpriced.** Five of six rows carry
a count; the second somatosensory area carries none.

**This is the first section in the map whose count partitions onto sub-elements.** Primary
somatosensory cortex is not given a total — it is given **four separate counts**, one per
cytoarchitectonic area: **3a ~15M, 3b ~25M, area 1 ~20M, area 2 ~20M.** Chunks 01 through 04 all
failed allocation at the same place, a stated total with no partition across the sub-elements the
edges terminate on. **Here the partition is what is stated and the total is what is derived.**

**And this is the section where the loop leaves the brain.** Primary motor cortex drives muscles;
the muscles, the skeleton and their dynamics have no entry anywhere; and the return path is
**through the world** — the movement's consequence read back through proprioception. The description
states it plainly: **the loop closes through the body, not inside the brain.**

---

## Structural invariants

**Whole-pathway co-instantiation, in its strongest form yet, and it points outside the map.** In the
auditory section a staged bring-up left a gain loop open; in the other-senses section neither
vestibular transducer's payload was defined without its sibling. **Here the pathway does not close at
all without a body.** The motor output edge's consumer is not in the map, and the description calls
it **the map's largest open boundary on the output side, the mirror image of the retina's input
edge.** A sensorimotor loop instantiated without a body is not a degraded loop — **the return edge
has no producer.**

**A second co-instantiation fact, and it is about learning rather than signal.** Proprioception
leaves the first relay on **two edges carrying one payload to destinations of different kinds**: the
cerebellum, by the cuneocerebellar tract from the external cuneate nucleus, and the thalamus onward
to cortical area 3a. The description is explicit that this is unlike the other senses, whose branches
carry **different** content — the retina sends orienting transients to the colliculus and a
luminance scalar to the pretectum, not two copies of the image. **The two copies differ in what kind
of memory they write, not in whether they are used:** the cortical copy becomes **reportable**, and
the cerebellar copy writes **procedural** change, motor learning being cerebellum-dependent. **A
learning channel that operates without perceptual access is an architectural fact, not an absence of
one** — and a build that folded the cerebellar branch into the motor loop and dropped the sense would
still pass a consistency check on that entry unless the duplication is stated.

**Per-edge latency: every edge reads *to derive*.** No time constant and no ordering constraint is
stated anywhere in this section — the first section since chunk 01 of which that is true. **What this
section constrains instead is the graph.**

**The topology itself is contested here, which is new.** Chunk 04 found contested payloads, one
contested route and one contested frame. This section finds a dispute about **whether the four
primary somatosensory areas form a chain or four partly independent lines.** All four receive direct
thalamic input, which is not disputed; what is disputed is whether the later areas can work without
the earlier. **Ablation** in macaque and marmoset abolishes cutaneous responsiveness in area 1 and
the second somatosensory cortex when area 3b is removed, which reads serial; **reversible lidocaine
inactivation** in cat, rabbit and marmoset leaves second-somatosensory responses substantially
intact, which reads parallel, and parallel thalamic activation is reported in prosimian primates and
tree shrews. **Irreversible ablation and reversible inactivation are not measuring the same thing**,
and **the entry keeps both the intracortical and the direct thalamic edges rather than choosing.**

**Three classes of non-neural or out-of-map edge.** Mechanoreceptor and proprioceptor afferents
arrive from a body that has no entry; the corticospinal command leaves to muscles that have no entry;
and the return path runs **through the world.**

**The standard laminar block is not a default, and this section is where that was established.** The
file's Class-3 laminar set — **1, 2, 3, 4, 5a, 5b, 6a, 6b** with **4 → 2/3**, **2/3 → 5a and 5b**,
**6a → 4**, **6a → 5a**, **6b → 6a** and within-sub-element recurrence — **is a claim about granular
isocortex**, and three of its edges route through layer 4. **Primary motor cortex is agranular:
seven laminae, not eight**, so transcribing the block would assert a circuit the entry's own Function
denies, and it is **withheld, with the internal edges left owed.** **Nine entries across five files
cannot take the block** — primary motor cortex, the temporal pole, the hippocampal formation, the
cerebellar cortex, and five frontal-lobe entries — **and they fail it in four different ways:**
uniformly agranular, agranular across a gradient, agranular across an internal border, and not
isocortex at all. **So a single exception clause would not cover them**, and stating the block's
scope is owed at the design file.

---

## Dorsal column nuclei and trigeminal relay

- **Function → structure.** First central relay of somatosensory afferents. **The dorsal column
  nuclei are three, not two:** the **gracile nucleus** (lower body), the **cuneate nucleus** (upper
  body, neck and forelimb), and the **external cuneate nucleus**, which is **the origin of the
  proprioceptive projection to the cerebellum.** Treating the complex as a two-part pair **loses the
  sub-element the cerebellar edge leaves from.**
  **It is not a passive relay.** The current literature describes it as a **sensorimotor integration
  and distribution hub**: descending input from sensorimotor cortex, intrinsic inhibitory
  interneurons and recurrent collaterals, and **the signal that leaves is not the signal that
  arrived.**
  **Internal division, and it is the entry's central structural fact.** Each of the gracile and
  cuneate nuclei splits into two territories with different input regimes: a **cluster region** — the
  middle third, **pars rotunda** in the primate cuneate — of tightly packed cells in
  **cytochrome-oxidase-dense patches separated by cell-poor, oxidase-light septa**, receiving
  afferents from **glabrous skin of the digits and pads**, punctate and high-acuity, **one body part
  per cluster**; and a **reticular region** rostral and caudal to it, of small and large
  **multipolar** cells receiving diffuse terminations with **intersegmental overlap** rather than
  somatotopic lamination.
- **Inputs.**
  - **← mechanoreceptor and proprioceptor afferents** — **two distinct payloads on one relay**:
    **cutaneous** (touch, pressure, vibration — intensity per skin location, somatotopic) and
    **proprioceptive** (muscle spindle length and rate, Golgi tendon force, joint angle — **the
    body's configuration, not the world's**). **Fan-in: no contacts-per-neuron figure found.** A
    **convergence** figure exists **and is not the same measurement**: in anaesthetised macaque,
    **87% of 317 recorded cuneate and external-cuneate cells responded to stimulation of two or more
    peripheral nerves** — 276 cells, recomputed — so a single relay cell reads from more than one
    nerve territory.
  - **← primary sensorimotor cortex**, corticocuneate, from the hand regions of areas 3b, 3a and 1/2
    and the forelimb region of primary motor cortex, **bilateral** — **no new stimulus content; a
    movement-contingent gain signal.** Somatosensory transmission through the cuneate is
    **attenuated** during voluntary hand movement, by an amount **comparable to that seen in cerebral
    cortex and larger than in the spinal cord.** **And it is not a scalar gain:** the cortical fibres
    produce **a central zone of facilitation surrounded by a peripheral zone of inhibition**, which
    is **a spatial sharpening operation.**
- **Outputs.**
  - **→ ventral posterior thalamus**, by the medial lemniscus and trigeminothalamic tract — both
    payloads, somatotopic, **with the cutaneous and deep submodalities kept separate.**
    - **→ cerebellum**, by the cuneocerebellar tract **from the external cuneate nucleus**
    (`10_cerebellum`) — **proprioception only, body configuration, unconscious.** **Two-ended:** that
    file's cerebellar cortex entry declares `← the external cuneate nucleus` in the same words and
    names this entry as the producer. **The endpoint here names the whole cerebellum and that file has
    no entry of that name** — its entries are the cerebellar cortex, the deep cerebellar nuclei and
    the inferior olive — **so the edge index resolves this endpoint to nothing and the pair is
    invisible from both directions.** **Owed: name the receiving entry.**
  - **No olivary output, and it is a recorded negative rather than an omission.** That file's inferior
    olive entry declares `← the dorsal column nuclei`, carrying somatosensory error, and marks it owed
    at this end. **This entry's outputs were read end to end and name no olivary target under any
    name.** **Owed at the source: write the limb, or the far end withdraws it.**
  - **→ dorsal cochlear nucleus** — the head, face and neck configuration copy **used to cancel
    self-generated sound**. **Contested at the receiving end**: the granule-cell domain carrying this
    copy is decreased or absent in primates, **so what receives this edge in a human is owed.**
- **Sizing.** Basis: **per hemisphere.** **~0.5M neurons**, soft, no clean human count, and **no
  separate count for the external cuneate nucleus** — the sub-element the cerebellar edge leaves
  from. Fan-in **to derive**. At the 16-bit ceiling: **1.00 MB.**
- **Shape.** Rank 3: **(nucleus, territory, somatotopic position)** — three nuclei, two territories,
  and a somatotopic axis that is **punctate in the cluster region and overlapping in the reticular
  one**, so the axis means different things in the two territories.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the descending gain edge closes a loop from cortex on
  to the first relay, and **this edge is the one every comparable first relay in the map also
  declares.** Per-edge latency: satisfied.
- **Justification (biological).** **Four internal edges converge on the same projection cells with
  different payloads:** the cluster region delivering the punctate high-acuity cutaneous payload; the
  reticular region delivering the convergent multi-territory payload the 87% figure measures;
  **intrinsic inhibitory interneurons** delivering inhibition with no content — **the substrate of
  the centre–surround sharpening the corticocuneate edge drives**; and **recurrent projection-cell
  collaterals** between cells with overlapping receptive fields, carrying **synchronisation, no new
  content.** **Species note carried:** the cluster/reticular division is primate and rodent; the
  internal edges are typed from cat physiology.
  **Contested for human, recorded not smoothed.** The human cuneate contains discrete subregions,
  present from prenatal life to old age, whose neurochemistry closely resembles **the superficial
  layers of the caudal spinal trigeminal nucleus, a nociceptive relay.** The authors state the
  arrangement **has never been formalised in the human brain and has not been described in another
  species.** **If it relays nociception, the entry's two-payload claim is incomplete for human, and
  the payload of any such third line is owed.**

## Ventral posterior thalamus

- **Function → structure.** The body's counterpart of the lateral and medial geniculate nuclei.
  **Four named subnuclei, not two:** the ventral posterior lateral nucleus relaying the body, the
  ventral posterior medial nucleus relaying the face, the ventral posterior inferior nucleus beneath
  them, and the basal ventral medial nucleus medially. Drives layer 4 of primary somatosensory
  cortex; gated by the thalamic reticular nucleus.
  **It is built in two chemically distinct compartments, and this is its central structural fact.**
  A **core** of large and medium **parvalbumin-positive** relay cells staining densely for
  cytochrome oxidase, and a **matrix** of smaller **calbindin-positive** cells staining weakly.
  **They take different afferents and project to different cortical layers, so a single edge from
  this complex to the cortex describes two different transfers.**
- **Inputs.** **← dorsal column nuclei and trigeminal relay** — the driver, and **as at the lateral
  and medial geniculate nuclei a minority of the synapses**; it **terminates in the parvalbumin
  core**, and its terminals form **triadic synapses with GABAergic presynaptic dendrites — an
  arrangement the spinothalamic input does not have.** **← spinal cord grey matter** (spinothalamic,
  from laminae I and IV–VIII) and the **spinal trigeminal nucleus** — pain, temperature and crude
  touch, **terminating diffusely and preferentially in the calbindin matrix**; about **10% of ventral
  posterior lateral neurons are nociceptive**, of wide-dynamic-range type, **and that figure is
  carried forward unverified and is a candidate for removal or sourcing.** **Contested:** whether the
  lamina-I pain and temperature stream relays here at all is disputed — one account concentrates
  lamina-I terminations in a separate posterior ventral medial nucleus, the other routes
  spinothalamic input into this complex's matrix. **The two accounts are not reconciled.**
  **← primary somatosensory cortex** and **← thalamic reticular nucleus** — no stimulus content; **the
  same driver/modulator gate declared at the lateral geniculate nucleus.**
- **Outputs.** **→ primary somatosensory cortex, onto layers 3B and 4, from the parvalbumin core** —
  the somatotopic payload, **gated, not transformed**, and **sorted onto its cortical targets by
  submodality: proprioception → area 3a, cutaneous → area 3b. This is the edge that carries the
  map.** **→ primary somatosensory cortex and adjacent cortex, onto layer 1, from the calbindin
  matrix** — **not topographic and not confined to one cortical area**, and the matrix cells can also
  be labelled from motor cortex; **its payload is owed** — what a non-topographic thalamic broadcast
  to layer 1 delivers, as a type with a range and a frame, is not established. **→ second
  somatosensory and parietal ventral areas**, from the ventral posterior inferior nucleus and the
  ventral posterior superior territory — **deep-receptor signals from muscles and joints, little if
  any cutaneous content.**
- **Sizing.** Basis: **per hemisphere.** **~2.5M neurons**, soft — **the largest primary sensory
  relay, above the lateral and medial geniculate nuclei at ~1.8–2.3M**, about **1.2× the geniculate
  midpoint**, recomputed, **its body-surface and proprioceptive afferent load exceeding the retina's
  or cochlea's.** **No separate core-versus-matrix count was found.** At the 16-bit ceiling:
  **5.00 MB.**
- **Shape.** Rank 3: **(subnucleus, compartment, somatotopic position)** — **and the compartment axis
  does not fit inside this structure.** The matrix **runs uninterrupted** from the ventral posterior
  medial and lateral nuclei into the ventral posterior inferior and basal ventral medial nuclei, and
  on into **the anterior pulvinar, posterior and ventral lateral nuclei.** **A compartment that
  crosses region boundaries cannot be expressed by per-region edges, and that is a finding about the
  description's representation and not only about the thalamus.**
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the corticothalamic gate closes here. Per-edge
  latency: satisfied.
- **Justification (biological).** Three internal edges, and the difference between the first two is
  synaptic rather than topological: **medial lemniscal terminals → core relay cells** by **triadic
  synapses with GABAergic presynaptic dendrites**, so **the transfer is locally inhibition-shaped
  rather than a simple relay**; **spinothalamic terminals → matrix relay cells**, **no triads**; and
  **local GABAergic interneurons → relay cells**, inhibition with no content. **Species note, and it
  is load-bearing:** interneuron density differs sharply — **the rat complex has very few, primates
  have many — so a rodent-derived internal circuit does not transfer here.**
  **And the naming of this territory is contested.** The four-subnucleus scheme used here and a
  parallel literature's **ventroposterior / ventroposterior superior / ventroposterior inferior**
  scheme **are not a relabelling of each other: they cut the proprioceptive relay out as a separate
  nucleus.** The edges carry the function either way.

## Primary somatosensory cortex

- **Function → structure.** **Four cytoarchitectonic areas, each a complete body map.** **Area 3a** —
  proprioceptive core, at the border with primary motor cortex, receiving group Ia muscle-spindle
  afferents. **Area 3b** — cutaneous core, **the true primary, with the finest somatotopic map.**
  **Area 1** — cutaneous secondary, texture and motion across the skin. **Area 2** —
  cutaneous-and-deep tertiary, size, shape and stereognosis, **where cutaneous and deep inputs
  converge.** **The map is self-organising and highly plastic, reorganising after input change.**
  **Thalamic input is a minority of long-range input — ~32% of layer-1 long-range input — and most
  input is intracortical.** Within areas 3b and 1 the map divides further into **modules — discrete
  representations of individual digits**, resolvable in imaging and separately affected by
  deafferentation.
- **Inputs.** **← ventral posterior thalamus, onto layers 3B and 4, from the parvalbumin core** —
  cutaneous intensity to areas 3b and 1, proprioceptive configuration to areas 3a and 2, topographic
  and point-to-point. **← the same complex, onto layer 1, from the calbindin matrix** —
  non-topographic, **payload owed at both ends**, terminating on **apical tuft dendrites belonging to
  cells whose somata sit in layers 2/3 and 5**, with **no second internal edge written for the
  propagation to those somata.**
- **Outputs.** **→ second somatosensory area and the parietal junction** along the intracortical
  chain **3b → 1 → 2** — a rising code: point pressure and adaptation rate, then texture and motion
  *across* the skin, then size, shape and stereognosis with cutaneous and deep input **combined,
  which is the first place the payload describes an object rather than the skin.** **The modality
  split is preserved along the way**, cutaneous by areas 3b and 1 and deep by 3a and 2, **as parallel
  channels rather than one merged stream.** **→ primary motor and premotor cortex, from area 3a**
  (the premotor consumer in `11_frontal_lobe`) — limb and joint configuration, **the feedback signal
  that closes the sensorimotor loop**, and **a
  payload type rather than a label**: single-unit recording distinguishes **single-digit
  position-scaled, multi-digit position-scaled, and posture-selective** cells, so what leaves is **a
  graded position variable per digit plus a categorical posture signal, not an undifferentiated
  proprioception.** **→ superior parietal area 5**, principally from area 2 with area 3a — limb
  configuration and tactile object properties **in a skin / joint frame, the frame that is
  re-expressed downstream.** **This payload also leaves the section**: the medial intraparietal entry
  in `06_posterior_parietal` declares a primary somatosensory source of its own, on the four-source
  line noted under the parietal class below. **→ the insula** from area 3a and **→ posterior
  parietal cortex** from
  areas 1 and 2 — **owed.** **The parietal class is checked against `06_posterior_parietal` and has
  one named consumer there**: the medial intraparietal area declares
  `← the primary somatosensory cortex` on a four-source line. **No other entry in that file declares a
  primary somatosensory source** — the angular gyrus declares only a *somatosensory association
  cortex* class, which is itself unresolved. **So the class narrows to one named member and one class
  facing a class**; naming the medial intraparietal area here is owed. **The insular endpoint was not
  tested** — that far end is in `17_insula_claustrum_habenula`, which has not been opened beside this
  file. **→ ventral posterior thalamus** — the gate, no content. **→ dorsal
  column nuclei**, corticocuneate, bilateral — the movement-contingent gain signal with its
  **centre–surround** organisation.
- **Sizing.** Basis: **per hemisphere. Four counts, not one: area 3a ~15M, area 3b ~25M, area 1
  ~20M, area 2 ~20M**, summing to **80M**, recomputed. At the 16-bit ceiling: **30.00, 50.00, 40.00
  and 40.00 MB, total 160.00 MB.** **This is the first structure in the map that can be allocated
  sub-element by sub-element.**
- **Shape.** Rank 3: **(area, lamina, somatotopic position)**, with a fourth level inside areas 3b
  and 1 — **digit modules** — and **the somatotopic axis is plastic**, reorganising after input
  change. **An extent that moves with experience is not the same kind of extent as one that does
  not.**
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the corticothalamic gate and the corticocuneate gain
  edge both close here, and the return limb of the motor loop arrives from the world. Per-edge
  latency: satisfied.
- **Justification (biological).** **Four internal edges implement the rising code** — 3b → 1
  (elaborating toward texture and motion), 1 → 2 (toward size and shape), **3a → 2** carrying the
  deep payload that converges with the cutaneous stream — **the transfer that makes stereognosis
  possible** — and 3b → 2 direct. **Whether these are a chain or four parallel lines is the disputed
  topology recorded above**, and the entry keeps both readings.

## Second somatosensory area

- **Function → structure.** Tactile object identity and stereognosis — texture, shape, material,
  **invariant to the exact contact point.** **The name covers more than one field:** the parietal
  operculum holds at least three — the **second somatosensory area** caudally, the **parietal ventral
  area** rostral to it, and the **ventral somatosensory area** deeper in the sulcus, its inner edge
  adjoining insular cortex. The first two are **mirror-symmetric body maps joined at the hand, foot
  and face representations.** In human they occupy parts of Brodmann areas 40 and 43.
  **Receptive fields are large and frequently bilateral** — spanning multiple digits, the whole hand,
  or both hands: **the first place in this pathway where the two body sides converge** — and neurons
  here are **less modality-specific** than in primary somatosensory cortex.
- **Inputs.** **← primary somatosensory cortex** — cutaneous by areas 3b and 1, deep by areas 3a and
  2, **two parallel channels, not one merged stream**; **whether this edge is necessary for the
  region to respond is the disputed topology above.** **← ventral posterior thalamus** and **← the
  anterior pulvinar** — **deep-receptor signals, not cutaneous. This is the entry's correction:**
  these fields receive **little if any cutaneous input from the thalamus**, so their cutaneous
  payload must arrive through the cortical edge, **and an account that treats this region as a second
  cutaneous relay fed from the thalamus has the modality backwards.** **The anterior-pulvinar limb is
  declared at this end only** and the pulvinar entry names no somatosensory target, **so it is owed
  or withdrawn — and it is a second endpoint on a shared line, so splitting the line is owed too.**
  **← the contralateral second somatosensory area, area 3b and area 7b**, callosal — **the opposite
  side's tactile payload, which is what makes the bilateral receptive field.** **The parietal ventral
  area's callosal connections are restricted to its own homologue and the second somatosensory
  area's are not**, so the two fields **differ in how much of the other hemisphere they see.**
- **Outputs.** **→ area 7b**, **→ the anterior intraparietal area** (`06_posterior_parietal`),
  **→ posterior parietal cortex** (a class, **owed**), **→ premotor cortex** from the parietal ventral
  area (`11_frontal_lobe`), **→ the parietal rostroventral area** (**owed**, far end unchecked), **→
  the insula** from
  the ventral somatosensory area (**owed**), and **→ primary somatosensory cortex** reciprocally
  (feedback, no new stimulus content).
- **Sizing.** Basis: per hemisphere. **Neurons: unknown — the only unpriced structure in this
  section.** Everything else in its slot list is unknown too. **Structure total: to derive.**
- **Shape.** Rank 3: **(field, map position, lamina)** — three fields, and **the map axis reverses at
  the seam**, since the second somatosensory and parietal ventral areas are mirror-symmetric maps
  joined at the hand, foot and face.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the reciprocal edge to primary somatosensory cortex
  closes here. Per-edge latency: satisfied.
- **Justification (biological).** **A finding that cuts against the description's own stream model.**
  The authors of the connection study conclude that these patterns suggest the somatosensory system
  **may not be segregated into two separate streams** in the way hypothesised for vision — the
  fields' cortical and thalamic connections **overlap rather than sorting into a "what" and a
  "where."** The map carries an explicit dorsal/ventral split for vision, and **whether the same
  split is imported into touch is a claim this entry does not support.**

## Superior parietal area 5

- **Function → structure.** Limb position, body schema, **and the coordinates in which a reach is
  specified.** **Three architectonic subdivisions, and they are not interchangeable:** **PE** on the
  gyral convexity, **PEa** on the medial bank of the intraparietal sulcus, and **PEc** caudally, with
  human area 5 overlapping all three. Human area 5 is distinguished by **a dense concentration of
  SMI-32-immunoreactive pyramidal neurons in layers III and V.**
  **It is not a purely sensory area:** movement-related activity **persists in the absence of
  sensory stimulation**, so it is **internally generated rather than driven**, and the area is active
  in movement **preparation**.
- **Inputs.** **← primary somatosensory cortex** (principally area 2, with 3a) — limb configuration
  and tactile object properties in a **skin / joint** frame. **← the medial bank of the
  intraparietal sulcus, the parietal opercular areas PGop and PFop, and the retroinsular area** —
  (the medial-bank limb in
  `06_posterior_parietal`) — **payload owed**, and **this line names four sources at once, so
  splitting it is owed.** **The medial intraparietal limb does have a producer end.** That entry
  declares `→ superior parietal area 5, onto the
  medial bank (area PEa)`, naming the medial bank and area PEa in the same terms this line uses, and
  marks its own payload owed. **So the limb is two-ended and untyped at both ends**, which is a
  different state from having no producer. **The other three sources on this line were not tested** —
  PGop, PFop and the retroinsular area have far ends outside the two files opened here, so they are
  unchecked rather than absent, and the split this line owes is now between one two-ended limb and
  three unchecked ones. **← the precuneus** (`06_posterior_parietal`), from its anterior
  sensorimotor sector — reach and body-configuration signals, body-centred; **that entry calls it the
  one edge out of itself whose payload can be written.** **Two-ended and confirmed**, and
  that entry records that this end was transcribed from it, **so the agreement between the two ends
  certifies nothing about the payload** — it is one statement written twice, not two readings that
  matched. **← primary motor cortex, the supplementary
  motor area and caudal dorsal premotor cortex** (the two frontal limbs in `11_frontal_lobe`) —
  **payload owed; the studies establish the projection, not its content.** **The three sources are in
  three different states, which is why splitting this line is owed.** The
  supplementary motor area and caudal dorsal premotor cortex are one structure in that file, and it
  declares `→ superior parietal area 5` — **two-ended, untyped there as here.** **The primary motor
  limb has no producer end, and the producer is in this file**: that entry's Outputs slot declares
  muscles, the return through the world to primary somatosensory cortex, the ventral anterior /
  ventral lateral thalamus and the dorsal column nuclei, **and no parietal target of any kind.**
  **An in-file edge declared at one end only is a weaker state than a cross-file one**, because
  nothing about file boundaries explains it. **Owed at the source: declare it at primary motor
  cortex, or withdraw it here.** **← the posterior cingulate area PEci and cingulate areas 23 and
  24** — owed, and for **PEc** substantial: **about 15% of its labelled afferent neurons lie in PEci
  and a further 10% elsewhere on the medial surface — 25% in total**, recomputed. **← gaze-position
  signals**, reaching PEc and PEa — eye position, and for PEc **the interaction of gaze with hand
  position rather than either alone.**
- **Outputs.** **→ dorsal premotor cortex** — limb position and the reach specification; **the
  payload change across this region is the frame, not the content.** **→ primary motor cortex**
  (reciprocal with area PE), **→ the medial, anterior, ventral and lateral intraparietal areas**, **→
  the supramarginal gyrus** (`06_posterior_parietal`), **→ the precuneus**
  (`06_posterior_parietal`) — the same limb state.
  **Four of the six named limbs are declared at their far ends in `06_posterior_parietal`**, so they
  are not declared at this end only: the anterior
  intraparietal area (`← superior parietal area 5`, principally area PE), the medial intraparietal
  area (on its four-source arm-configuration line), the supramarginal gyrus (`← superior parietal area
  5`, body configuration) and the precuneus (`← superior parietal area 5`, body configuration and
  spatial layout). **The ventral and lateral intraparietal limbs are unchecked** — their far ends are
  in `04_dorsal_visual_parietal_stream`, which has not been opened beside this file — **and the
  dorsal premotor limb
  above is two-ended** with `11_frontal_lobe`.
  **Two of the four discharged ends warn that they certify nothing.** The supramarginal and precuneus
  entries both record that their end was transcribed from this one, **so those two are one statement
  written twice.** The two intraparietal ends were written independently. **Replacing a false absence
  with a true declaration is not the same as replacing it with agreement**, and only two of the four
  are agreement.
  **Splitting the intraparietal line is owed and now has a reason**: it names four areas in two files
  and three states.
- **Sizing.** Basis: **per hemisphere. ~25M neurons**, soft, **no per-subdivision count found** —
  so this structure has the sub-elements and not the partition, the ordinary case. At the 16-bit
  ceiling: **50.00 MB.**
- **Shape.** Rank 2: **(subdivision, position)** — three subdivisions forming an
  **anterior-to-caudal functional gradient**: **PE** most sensitive to limb proprioception and
  encoding arm position with **the most independence from gaze**; **PEa** proprioceptive and
  kinematic, **the reach-planning end**; **PEc** sensitive to **proprioception and gaze together**,
  linked to lower-limb motor representations, vestibular cortex and optic-flow areas, with a proposed
  role in **locomotion and limb coordination in the environment, not reaching alone.**
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: reciprocal with primary motor cortex and with the
  intraparietal areas. Per-edge latency: satisfied.
- **Justification (biological).** **The reference frame is contested and the entry has withdrawn its
  earlier assertion.** The reported frames are **body-, shoulder- and hand-centred across different
  studies**, and in area PE specifically a memorised target's distance is encoded **relative to the
  initial hand position rather than to the body.** **This matters more than a nomenclature dispute
  would, because on this description's payload rule the coordinate frame is part of the payload, so
  an unsettled frame is an unsettled payload.** And the far ends have not withdrawn: the medial
  intraparietal area and the precuneus both **type the frame as body-centred**, so **the two ends
  disagree about the frame, which is a payload disagreement and not a wording one.**

## Primary motor cortex

- **Function → structure.** Corticospinal drive to muscles; a somatotopic motor map and movement
  primitives. **Agranular cortex — thin or absent layer 4, layer-5 pyramidal and Betz-cell heavy —
  because it is output-dominated.** **Laminar sub-elements: seven, not eight — 1, 2, 3, 5a, 5b, 6a,
  6b** — and that is this entry's structural fact.
- **Inputs.** **← primary somatosensory cortex, area 3a** — proprioceptive and cutaneous feedback,
  **the consequence of the last command.** **← premotor cortex** (`11_frontal_lobe`) — **the planned
  action, already
  sequenced and shaped, not yet a muscle command**; the far end declares it and is **untyped**.
  **Two-ended, and untyped there.**
  **← superior parietal area 5** (reciprocal with area PE) — limb position and the reach
  specification **in a contested frame.** **← thalamus, ventral anterior / ventral lateral** — **the
  basal-ganglia selection (which action is released) and the cerebellar correction (how it is
  shaped), combined on one relay**; the far end names this area but is **untyped**.
  **Two inbound edges are declared at producers in `11_frontal_lobe` and are not declared here.**
  Broca's area declares `→ premotor cortex and primary motor cortex, for
  articulation`, and the right inferior frontal gyrus declares the homologous edge for affective
  prosody. **That file already records that its own premotor structure declares neither, and marks
  both as inherited gaps owed at the source. This end is the second consumer on both, and it does
  not declare them either** — so each edge is producer-only at **both** of its two named targets
  rather than at one. **They are not written in above**,
  because writing an edge whose only support is the far end's declaration would assert a
  connection this file has read nothing for. **Owed at the source: accept both here, or narrow the
  producers' endpoint to premotor cortex alone.**
- **Outputs.** **→ muscles**, by the corticospinal tract — the motor command. **The consumer at the
  far end is not in this map**: the muscles, the skeleton and their dynamics have no entry, **so this
  edge's payload is declared with no one to receive it.** **→ (returning through the world) →
  primary somatosensory cortex** — the movement's **consequence**, read back through proprioception;
  **fan-out not applicable.** **→ thalamus, ventral anterior / ventral lateral**, corticothalamic and
  reciprocal — **owed at both ends.** **→ dorsal column nuclei**, corticocuneate from the forelimb
  region — the same movement-contingent gain signal primary somatosensory cortex declares, **arriving
  on the same target**, and **its distinctness from the somatosensory limb is owed**: the retrograde
  study labelled both and whether they carry the same content is not established.
- **Sizing.** Basis: **per hemisphere. ~30M neurons**, soft. At the 16-bit ceiling: **60.00 MB.**
- **Shape.** Rank 2: **(lamina, somatotopic position)** — seven laminae, and **tangential
  sub-elements owed**: whether the somatotopic motor map and the movement primitives are a
  compartmentation an edge could terminate on, or a continuous map, **is not established.**
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: **this is the structure whose output loop does not
  close inside the map.** Per-edge latency: satisfied.
- **Justification (biological).** **The standard laminar block is withheld here and the withholding
  is the finding.** Three of its edges terminate on or leave from layer 4, which this entry says is
  thin or absent, **so transcribing it would assert a circuit the entry's own Function denies.** The
  internal edges therefore read **owed**. **A laminar set copied across entries is a Class-3 claim
  that has to be checked against each entry's own laminar description, and here it fails** — with
  eight further entries across four other files failing it in three more ways.

---

## Section totals

| # | structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Dorsal column nuclei and trigeminal relay | per hemisphere | ~0.5M | ≤ 16 | ≤ 1.00 MB |
| 2 | Ventral posterior thalamus | per hemisphere | ~2.5M | ≤ 16 | ≤ 5.00 MB |
| 3 | Primary somatosensory cortex — area 3a | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB |
| 3 | Primary somatosensory cortex — area 3b | per hemisphere | ~25M | ≤ 16 | ≤ 50.00 MB |
| 3 | Primary somatosensory cortex — area 1 | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB |
| 3 | Primary somatosensory cortex — area 2 | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB |
| 4 | Second somatosensory area | per hemisphere | **unknown** | ≤ 16 | **to derive** |
| 5 | Superior parietal area 5 | per hemisphere | ~25M | ≤ 16 | ≤ 50.00 MB |
| 6 | Primary motor cortex | per hemisphere | ~30M | ≤ 16 | ≤ 60.00 MB |
| | **stated total** | per hemisphere | **~138M** | | **276.00 MB**, one row unpriced |

Recomputed: **138M neurons and 276.00 MB**, with the four somatosensory areas summing to **80M and
160.00 MB.** All reproduce. Against the earlier sections: **2.2× chunk 04, 0.57× chunk 02.**

**The first partition in the map, and it is worth saying exactly what makes it one.** Every previous
section stated a total for a structure and named sub-elements the edges terminate on, with nothing
connecting them — eight belt fields sharing one count, two parabelt divisions sharing another, a
lateral intraparietal subdivision border established by two independent stains with no count split
across it. **Here primary somatosensory cortex is given no total at all: it is given four counts, one
per area, and the total is what has to be derived.** So `allocate` closes at the sub-element level
for the first time, for four sub-elements.

**And the partition stops there.** The dorsal column nuclei have three nuclei, two territories and
**no separate count for the external cuneate nucleus** — which is the sub-element the cerebellar edge
leaves from, so **the one edge whose source is a named sub-element cannot be sized.** The thalamus
has core and matrix and **no core-versus-matrix count.** Area 5 has three subdivisions and **no
per-subdivision count.** Primary motor cortex has seven laminae and no laminar count. **One structure
in six partitions; the other five are the ordinary case.**

**Three findings about representation, and none of them is a gap in the description.**

1. **A compartment that is not contained in a structure.** The calbindin matrix runs uninterrupted
   out of the ventral posterior complex into the anterior pulvinar and the posterior and ventral
   lateral nuclei. **Per-region edges cannot express a population that crosses region boundaries**,
   and the description says so.
2. **A topology that is contested rather than a payload.** Whether the four somatosensory areas are
   serial or parallel is disputed by two methods that are not measuring the same thing, and the
   description **keeps both edge sets rather than choosing** — so the graph has more edges than the
   anatomy may.
3. **A laminar template that is a claim, not a default.** Nine entries across five files cannot take
   the standard block, failing in four distinct ways, **so a single exception clause would not cover
   them.**

**Two arithmetic cautions carried from the description.** The **87% convergence figure is not a
fan-in measurement** — it counts cells responding to two or more nerve territories, not contacts per
neuron, and the description says the two are different measurements. And the **~10% nociceptive
figure at the thalamus is carried forward unverified**, flagged there as a candidate for removal or
sourcing. **Neither may be promoted into a width or a fraction at a lower rung.**

**The section's largest fact is not in the table.** The motor output edge has no consumer in the map,
the return path runs through the world, and proprioception is delivered twice — once as a reportable
percept and once as procedural change in a cerebellum this section does not describe. **Memory is not
a binding constraint and none of these figures is to be reduced; state memory and edge storage are
not in the total.**
