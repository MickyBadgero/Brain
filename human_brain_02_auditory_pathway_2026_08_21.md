# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-21
---

---

# FILE 2 OF 20 — AUDITORY PATHWAY

**What is in this file.** The auditory line from the cochlea and cochlear nucleus through the
superior olive, inferior colliculus and medial geniculate to primary auditory cortex, then belt,
parabelt, and the two superior-temporal streams, ending with the right-hemisphere prosodic
homologues. Several entries here carry human-versus-animal disputes that go to their central claims.

**Size:** 2060 lines, ~42.3k tokens (estimated from bytes, not tokenised). **Entries:** 11.

**This file is one section of the source. Edges cross into other files; an endpoint named here that
has no entry here lives in another file. Do not treat a missing endpoint as a missing region without
checking the other files.**

**Entries in this file:**

- **Cochlea — the acoustic transducer (membranous labyrinth, sensory front end)**
- **Cochlear nucleus — first central auditory station (brainstem)**
- **Superior olivary complex — first binaural station (brainstem)**
- **Inferior colliculus — obligatory midbrain auditory hub**
- **Medial geniculate nucleus — auditory thalamus (also called the medial geniculate body)**
- **Primary auditory cortex — the auditory core (Heschl's gyrus, isocortex)**
- **Auditory belt — secondary auditory cortex (isocortex)**
- **Auditory parabelt — tertiary auditory cortex (lateral superior temporal gyrus, isocortex)**
- **Anterior superior temporal gyrus and sulcus — the auditory "what" endpoint (isocortex)**
- **Posterior superior temporal gyrus and the Sylvian parieto-temporal area — the auditory dorsal stream's origin (isocortex)**
- **Right-hemisphere prosodic homologues — prosody and affect (isocortex)**

---

# AUDITORY PATHWAY (through the temporal lobe)

## Cochlea — the acoustic transducer (membranous labyrinth, sensory front end)

- **Function:** turns sound-pressure vibration into a neural signal, and performs a **mechanical
  frequency analysis before any neural processing happens**. A coiled fluid-filled tube in the
  temporal bone, about **35 mm** long and **0.2 mm** in diameter, making about **two and a half
  turns**, partitioned along its length into three compartments — the scala vestibuli and scala
  tympani, and between them the **scala media**, which holds **endolymph**, a fluid with an unusually
  high potassium concentration held at a standing positive voltage, the **endocochlear potential**.
  That standing voltage is the battery the transduction current runs on: it is supplied by the
  tissue, not by the stimulus, which is why the cochlea can respond to vibrations of atomic
  dimension. **The frequency decomposition is done by the mechanics** — position along the tube maps
  to frequency, base to apex, high to low — so what leaves the cochlea is already tonotopically
  sorted, and every auditory entry downstream inherits that map rather than computing it.
  *(Class 1 — dimensions and compartments: Fettiplace 2017; tonotopy: Gillespie & Müller 2009.
  Candidates — awaiting Micky's verification.)*
- **Two sensory cell types with different jobs, and this is the entry's central structural fact.**
  A single row of **inner hair cells** (~3,500 in human) are the **transducers** — they carry the
  afferent load and essentially all sound information reaching the brain. Three rows of **outer hair
  cells** (~12,000) are the **amplifier** — they are motile, and their job is to add mechanical
  energy back into the travelling wave. Treating the organ as one sheet of receptors would lose the
  distinction between a sensor and a servo built into the sensor.
- **The hair cells do not spike.** Mature cochlear hair cells produce **graded receptor potentials**
  and have no action potentials at all; the first spikes on the auditory line are in the spiral
  ganglion neurons. This is the same analogue-front-end arrangement the retina uses, where
  photoreceptors and bipolar cells are graded and the ganglion cell is the first spiking stage.
  *(Class 1 — Fettiplace 2017. Class 2 — the parallel drawn to the retina is Claude's. Candidate.)*
- **Inputs:**
  - **← sound-pressure vibration, via the middle ear** — **carries:** acoustic pressure over time,
    the full audible band, unanalysed. **This is a mechanical input, not a neural edge** — the same
    case as light at the retina and blood chemistry at the solitary nucleus. The outer and middle ear
    are outside this file's scope. **Fan-in:** not applicable.
  - **← Superior olivary complex**, the **medial olivocochlear efferents**, onto the **outer hair
    cells** — **carries:** no stimulus content; a **gain command** that reduces the amplifier's
    contribution. This is the descending limb of a loop whose ascending limb starts here, and it is
    the mechanism by which the brain turns its own front end down. **Fan-in:** unknown.
    *(The superior olivary complex entry declares these efferents as an output onto the outer hair
    cells. Candidate.)*
  - **← Branchiomotor / visceromotor nuclei**, indirectly, via the **stapedius muscle** of the middle
    ear — **carries:** no stimulus content; the acoustic reflex's attenuation of transmission into
    the cochlea. **The effector is a middle-ear muscle, outside this file's scope**, so this is
    recorded as an influence on the input above rather than as an edge onto neural tissue.
    **Fan-in:** not applicable.
- **Outputs:**
  - **→ Cochlear nucleus**, via the **auditory nerve**, from the **inner hair cells** through the
    **type I spiral ganglion neurons** (~30,000 fibres) — **carries:** sound pressure at one place on
    the tonotopic map — that is, **energy in one narrow frequency band, as a function of time**, with
    the timing of the waveform preserved by phase-locking at low frequencies. Tonotopically ordered.
    **Fan-out:** each inner hair cell drives **5–30 type I neurons** (reported as 10–20 in some
    material), and each type I neuron contacts **exactly one** inner hair cell — so this is a
    **pure divergence with no convergence at all**, one of the few exactly stated arities in the
    file, and the mirror image of the endbulb of Held's fan-in of one or two at the far end.
    *(Class 1 — Carricondo & Romero-Gómez 2019; Barclay, Ryan & Housley 2011; Sun et al. 2018.
    **Species: the 5–30
    range is mammalian, largely rodent.** Candidates.)*
  - **→ Cochlear nucleus**, via the auditory nerve, from the **outer hair cells** through the
    **type II spiral ganglion neurons** (~5–10% of the ganglion, unmyelinated) — **carries:** not
    sound. These fibres are **not required for hearing**; the current reading is that they signal
    **cochlear damage — a nociceptive line from the ear**. **Payload owed:** what a damage signal
    from the organ of Corti is, as a type with a range and a frame, is not established.
    **Fan-out:** each type II neuron branches onto roughly **a dozen outer hair cells**, and each
    outer hair cell contacts **one** type II neuron — the opposite arity to the inner hair cell line.
    *(Class 1 — Flores et al. 2015; Liu et al. 2015; Carricondo & Romero-Gómez 2019. Candidate.)*
- **Internal structure and internal data flow:** the **organ of Corti**, riding on the **basilar
  membrane**, whose graded stiffness and mass along the tube produce the tonotopic map; one row of
  inner hair cells; three rows of outer hair cells; the **stereocilia** bundles carrying the
  mechanoelectrical transduction channels, a fraction of which stand open at rest so that the cell
  reports deflection in both directions.
  - **Internal edge — basilar-membrane travelling wave → outer hair cells: carries:** local
    displacement at that place on the map. **Fan-in / fan-out:** unknown.
  - **Internal edge — outer hair cells → basilar-membrane travelling wave (the cochlear amplifier):
    carries:** mechanical force, added back in phase. **This is a mechanical feedback loop inside a
    sensory organ, not a neural one.** The motor is **prestin**, a voltage-driven membrane protein
    that changes the cell's length directly, without a motor protein cycle. Its contribution is
    large and measurable: abolishing it costs **40–60 dB** of sensitivity, an amplification of
    roughly a hundredfold. The loop's output is also directly observable from outside the head as
    **otoacoustic emissions** — sound the ear emits — which is what newborn hearing screening
    measures. **Fan-in / fan-out:** not applicable; the transfer is mechanical.
  - **Internal edge — basilar-membrane travelling wave → inner hair cells: carries:** the amplified,
    sharpened local displacement; the signal that is actually transduced. **Fan-in / fan-out:**
    unknown.
  *(Class 1 — prestin and electromotility: Zheng et al. 2000; Dallos et al. 2008; Ashmore 2008. **Species:
  mouse and guinea pig for the amplifier figures.** Candidates — awaiting Micky's verification.)*
- **Neurons:** the hair cells are **not neurons** — they are sensory epithelial cells, and the
  neurons of this entry are the **spiral ganglion**, ~30,000–35,000 per ear in human, of which
  90–95% are type I. Hair cells: ~3,500 inner and ~12,000 outer per ear.
- **Synapses:** unknown. **Axons:** ~30,000 per auditory nerve. **Grey-matter volume:** not
  applicable — this is not central tissue. **White-matter volume:** not applicable.
  **Myelination:** type I spiral ganglion fibres are myelinated; type II are unmyelinated; and
  unusually, the **somata** of human spiral ganglion neurons are largely **unmyelinated**, unlike
  other mammals. *(Class 1 — Carricondo & Romero-Gómez 2019. Candidate.)*

## Cochlear nucleus — first central auditory station (brainstem)

- **Function:** first central processing of the auditory-nerve signal, split into **parallel
  labelled lines** — each cell class a different message on a different wire. **Bushy cells**
  preserve precise timing, for the interaural time and level differences computed downstream.
  **Stellate cells** (also called chopper cells) encode the spectrum. **Octopus cells** signal
  broadband onset by coincidence detection, at the highest temporal precision in the brain.
  **Fusiform cells**, in the dorsal division, carry monaural spectral-notch cues for sound
  elevation and are where body signals — somatosensory from face and neck, and vestibular — first
  enter hearing, associated with cancelling self-generated sound (chewing, vocalising, head and
  pinna motion).
  **The parallel lines are not parallel processing of different inputs — they are different
  readings of the same input**, and that is the entry's central structural fact. Every auditory
  nerve fibre bifurcates on entry and reaches **all three divisions**, so each cell class receives
  the same afferent and extracts something different from it. What differs between the lines is the
  **terminal type and the receiving cell's intrinsic properties**, not the source. *(Class 1 —
  Fekete et al. 1984; Ryugo & Parks 2003; cat.)*
- **Inputs:**
  - **← Cochlea**, via the **auditory nerve** (~30,000 fibres, tonotopic) — **carries:** the cochlea's
    frequency-decomposed output: firing rate per characteristic frequency (a tonotopic spectral
    vector) with **phase locking** to the fine structure at low frequencies — that is, the timing
    *is* part of the payload, not just its carrier. **This is one edge that terminates in three
    places** (see Internal structure); it is written once here because it is one fibre population,
    and the divisions it reaches are sub-elements of this entry. **Fan-in:** **known for one
    target and it is very low** — a spherical bushy cell receives **one or two** axosomatic endbulbs
    of Held and little else, which is what makes its timing secure; unknown for the other classes.
  - **← dorsal column nuclei and trigeminal relay** (into the dorsal division) — **carries:**
    somatosensory state of the head, face, neck, and pinna — a proprioceptive and tactile copy of
    self-generated movement, used to cancel self-generated sound. It arrives **by way of the granule
    cells**, not directly onto the output cells (see Internal structure). **Fan-in:** unknown.
  - **← semicircular canals, otolith organs, and vestibular nuclei** (into the dorsal division) —
    **carries:** head rotation rate and gravito-inertial acceleration — the same self-motion copy,
    for the same cancellation, on the same granule-cell route. **Fan-in:** unknown.
  - **← auditory cortex and inferior colliculus** (descending) — **carries:** gain and expectation;
    no new stimulus content. **Payload otherwise unknown — owed.** **Fan-in:** unknown.
  - **← medial nucleus of the trapezoid body and other glycinergic sources in the superior olivary
    complex** — **carries:** inhibition; no content. Recorded because glycine is demonstrated as a
    transmitter in the human and chimpanzee cochlear nucleus, with receptors on somata and processes
    across all three divisions.
    **The source of the human glycinergic input is candidate, not established** — the trapezoid body
    is one proposed origin among others. **Fan-in:** unknown. *(Class 1 for the receptors and
    transmitter — Front Neuroanat 18:1331230, 2024, human and chimpanzee;
    Class 2 for the attribution of source. Not yet verified for the source.)*
- **Outputs:** the split into **parallel labelled lines is the payload structure**:
  - **→ superior olivary complex**, from **bushy cells** — **carries:** the spectral vector with
    **sub-millisecond arrival timing preserved** (the whole point of the bushy cell); monaural, one
    per ear. This is the payload from which interaural time and level differences are computed
    downstream — it is *not* itself a localisation signal. **Two sub-classes leave on this edge with
    three destinations**, declared at the far end: **spherical** bushy cells drive the medial
    superior olive **bilaterally** and the lateral superior olive **ipsilaterally**; **globular**
    bushy cells drive the medial nucleus of the trapezoid body **contralaterally**. The three
    differ in sign and side, not in content — the same monaural payload, routed so that the two
    differences can be taken. **Fan-out:** unknown.
  - **→ inferior colliculus** (via the lateral lemniscus), from **stellate cells** — **carries:**
    the sound **spectrum** — rate-coded energy per frequency band, timing not preserved.
    **Fan-out:** unknown.
  - **→ inferior colliculus**, from **octopus cells** — **carries:** broadband **onset** — a
    coincidence event marking a transient, at the highest temporal precision in the brain.
    **Fan-out:** unknown.
  - **→ inferior colliculus**, from **fusiform cells** (dorsal division) — **carries:** monaural
    **spectral-notch** cues for sound **elevation** — the payload the pinna imposes on the spectrum,
    with the self-motion signal already subtracted. **In human this edge's source cell class is
    itself disputed** — see Internal structure. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. **The circuit work is cat, rat and mouse; the
  human work is immunohistochemistry on post-mortem material and it disagrees with the animal
  circuit in ways this entry has to carry.** Nothing here is yet verified for the source.)*

  **Divisional sub-elements: three, defined by where the auditory nerve terminates.** The
  **anteroventral cochlear nucleus**, the **posteroventral cochlear nucleus** — together the ventral
  cochlear nucleus — and the **dorsal cochlear nucleus**. Each holds a complete tonotopic map, so
  there are **three maps of frequency per side**, not one. *(Class 1 — Ryugo & Parks 2003; cat.)*

  **The bifurcation, and why it is the entry's most load-bearing internal fact.** Each auditory
  nerve fibre divides on entry into an **ascending branch**, which terminates in the anteroventral
  division as the **endbulb of Held** — a giant axosomatic ending enveloping a spherical bushy cell
  — and a **descending branch**, which gives off ordinary bouton terminals in the posteroventral
  division and continues to terminate in the dorsal division. **One fibre, three terminal fields,
  three terminal types.** The endbulb is large enough to generate an extracellular prepotential
  before the bushy cell's own spike, and the delay between the two has exceptionally low jitter —
  the timing fidelity the whole binaural pathway rests on is bought here, by synapse morphology.
  *(Class 1 — Fekete et al. 1984; Ryugo & Fekete 1982; Rouiller et al. 1986; Molnar & Pfeiffer 1968;
  cat.)*

  **Cell-class sub-elements, by division.** Ventral: **spherical bushy cells** (anteroventral),
  **globular bushy cells**, **octopus cells** (posteroventral), and **stellate cells** in two kinds
  — **T-stellate**, which project out of the nucleus and carry the spectrum, and **D-stellate**,
  which are inhibitory and stay. Dorsal: **fusiform cells** (also called pyramidal cells) as the
  principal output, plus **giant cells**, and the interneurons — **cartwheel**, **tuberculoventral**
  (also called vertical), **superficial stellate**, **Golgi**, and **granule** cells.

  **Laminar sub-elements of the dorsal division: three layers, in the animals it was described in.**
  A superficial **molecular layer** holding the granule cells' parallel fibres; a middle **fusiform
  cell layer**; and a **deep layer** holding the auditory-nerve fibres, the fusiform cells' basal
  dendrites, giant cells and tuberculoventral cells. *(Class 1 — Osen & Mugnaini lineage; cat and
  rodent.)*

  **The fusiform cell is a two-domain cell, and that is the mechanism of the cancellation.** Its
  **basal** dendrites, in the deep layer, are smooth and take the **auditory** input from the nerve.
  Its **apical** dendrites, in the molecular layer, are spine-covered and take the **non-auditory**
  input by way of the granule cells' parallel fibres. **One cell, two input streams, segregated by
  dendritic compartment** — the same place-versus-owner geometry this file records for cortical
  layer 1, and here it is the whole functional point: the self-motion copy and the sound arrive on
  physically different parts of the same neuron. Three interneuron classes divide the cell's surface
  between them: superficial stellate cells inhibit the **apical dendrites**, cartwheel cells the
  **soma and proximal dendrites**, tuberculoventral cells the **soma and basal dendrites**.
  *(Class 1 — Rubio & Juiz 2004; Wouterlood et al. 1984; Manis lineage; rat and mouse.)*

  **Internal edges:**
  - **auditory nerve, ascending branch → spherical bushy cell soma** (anteroventral division;
    endbulb of Held) — **carries:** the phase-locked spectral vector, transmitted with minimal added
    jitter. **Fan-in:** **one or two.** **Fan-out:** unknown.
  - **auditory nerve, descending branch → octopus and stellate cells** (posteroventral division;
    bouton terminals) — **carries:** the same payload, on ordinary synapses. The octopus cell's
    reading of it is coincidence across many fibres; the stellate cell's is rate per band.
    **Fan-in:** unknown, and **high for the octopus cell by construction** — coincidence detection
    across the tonotopic array is what it does. **Fan-out:** unknown.
  - **auditory nerve, descending branch → fusiform cell basal dendrites and giant cells** (dorsal
    division, deep layer) — **carries:** the same payload again, onto the auditory domain of the
    two-domain cell. **Fan-in:** unknown. **Fan-out:** unknown.
  - **granule cells → parallel fibres → fusiform cell apical dendrites and cartwheel cells**
    (molecular layer) — **carries:** the **non-auditory** signal — the somatosensory and vestibular
    self-motion copy the Inputs field declares — arriving on a cerebellum-like expansion. **This is
    the edge the cancellation is performed on**, and it is the one the human evidence disputes.
    **Fan-in:** unknown. **Fan-out:** unknown. *(Class 1 — Oertel & Young 2004; PMC6573148; rodent.)*
  - **cartwheel cells → fusiform cell soma and proximal dendrites** — **carries:** inhibition,
    predominantly glycinergic, driven by the parallel fibres. Cartwheel cells are described as
    homologues of the cerebellar Purkinje cell. **Fan-in:** unknown. **Fan-out:** unknown.
  - **tuberculoventral cells → fusiform cell soma and basal dendrites** — **carries:** inhibition
    scoped to the **auditory** domain of the cell, separately from the cartwheel cells' inhibition
    of the soma and the superficial stellate cells' inhibition of the apical dendrites.
    **Fan-in:** unknown. **Fan-out:** unknown.
  - **D-stellate cells (ventral division) → dorsal division** — **carries:** inhibition, crossing
    between divisions — so the three divisions are **not** three independent readings after their
    first synapse. **Fan-in:** unknown. **Fan-out:** unknown.

  **The human divergence, and it reaches the Function field of this entry.** Almost everything above
  is cat and rodent. The human and primate literature disagrees with it at three points, and the
  disagreement is not a gap:
  - **The granule cell domain is decreased or absent in primates.** If the granule cells are largely
    absent, the parallel-fibre edge that carries the self-motion copy has no source.
  - **The laminar organisation of the dorsal division is much less well defined in human.**
    Immunohistochemistry on human material found **two** layers rather than three, and found **no
    evidence of the inhibitory interneurons** described in cat and rodent — no cartwheel,
    tuberculoventral, stellate or Golgi population was labelled. In the same material a clearly
    demarcated molecular layer was present with fine beaded fibres, **but no dendrites of projection
    neurons or interneurons were seen extending into it** — which argues directly against the
    parallel-fibre-onto-apical-dendrite arrangement.
  - **The fusiform cells themselves are disputed.** In primates they lack the orderly row and
    orientation seen in other species; one report describes large projection neurons in **clusters**
    rather than a single row; another states fusiform neurons are **absent** from the human dorsal
    division altogether.

  **What this entry therefore claims and does not claim.** The three-division structure and the
  auditory-nerve bifurcation hold across species and are safe. The **two-domain fusiform cell and
  the cerebellum-like granule/parallel-fibre/cartwheel circuit are cat-and-rodent anatomy that the
  human material has not confirmed and in part contradicts** — and the Function field's claim that
  this is where body signals enter hearing rests on exactly that circuit. It is **recorded as
  contested for human, not deleted**: the somatosensory and vestibular inputs to the dorsal division
  are independently attested, so something receives them; what, in a human, is **owed**. *(Class 1 —
  Baizer et al. 2014, human/macaque/cat/rodent; Baizer et al., Anat Rec 2018; Heiman-Patterson &
  Strominger 1985; Adams 1986; Moore & Osen 1979;
  Wagoner & Kulesza 2009. Not yet verified for the source.)*

  **A second human divergence, in the ventral division.** Spherical bushy, globular bushy and
  stellate cells in the human ventral cochlear nucleus lie **intermixed within the cochlear nerve
  branches**, which makes the anteroventral/posteroventral boundary — sharp in other mammals and the
  basis on which the divisions are *defined* — difficult to draw. **So the divisional sub-elements
  above may not be separable structures in a human brain**, even though the cell classes inside them
  are present. Recorded because an edge terminating "on the anteroventral division" is checkable in
  a cat and may not be in a human. *(Class 1 — Baizer et al., Anat Rec 2018, human.)*
- **Neurons:** ~0.5M per hemisphere (best available; no clean human count — soft
  but recorded). **The human material for a count exists** — the immunohistochemical studies above
  worked from a normal human brain collection and identified the divisions and their large cells —
  so this is a gap in what has been counted rather than in what has been sectioned.
- **Synapses:** unknown, except that the endbulb of Held gives a **fan-in of one or two** onto the
  spherical bushy cell, one of the few exactly known convergence figures in this file.
  **Axons:** the auditory nerve at ~30,000 fibres per side entering; the three acoustic striae
  leaving (counts unknown). **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Superior olivary complex — first binaural station (brainstem)

- **Function:** the **first site of binaural convergence** — where the two ears' signals meet — and
  the origin of horizontal **sound localisation**. Two principal nuclei compute the two localisation
  cues.
  The **medial superior olive** extracts **interaural time differences** by coincidence detection:
  it receives bilateral *excitation* from the spherical bushy cells of both cochlear nuclei, and a
  cell fires maximally when the two arrive together. This is the low-frequency cue and the dominant
  human one.
  The **lateral superior olive** extracts **interaural level differences**: ipsilateral *excitation*
  against contralateral *inhibition*, the latter relayed and sign-inverted through the **medial
  nucleus of the trapezoid body**, whose glycinergic cells are driven by the giant, ultrafast
  **calyx of Held** from contralateral globular bushy cells. This is the high-frequency cue.
  The complex is also the source of the **medial olivocochlear efferents** — descending feedback
  onto the outer hair cells that sets cochlear gain — and drives the **stapedius (acoustic)
  reflex**.
  **Human note: this is the least species-transferable structure in the auditory pathway, and the
  disagreement is about what nuclei exist, not only about their size.** Stated in full under
  Internal structure. What is agreed: a **medial superior olive is present in every human specimen
  examined**, consistent with humans localising by time at low frequencies. What is disputed: the
  lateral superior olive's prominence, and whether the medial nucleus of the trapezoid body exists
  in human at all.
- **Inputs:**
  - **← cochlear nucleus, spherical bushy cells, bilaterally**, onto the **medial superior olive** —
    **carries:** the spectral vector with phase-locked timing intact, from **both** ears — two
    copies of the same message, differing only in arrival time. **This edge's payload is a pair, and
    the pairing is the point**: neither copy alone carries azimuth, and the difference between them
    is not computed until it arrives here. **Fan-in:** unknown.
  - **← cochlear nucleus, globular bushy cells, contralateral**, onto the **medial nucleus of the
    trapezoid body** — **carries:** the same phase-locked spectral vector, which the trapezoid body
    then **sign-inverts** (excitation becomes glycinergic inhibition) before passing it to the
    lateral superior olive — and that inversion is what makes a *level difference* computable as a
    subtraction. **Fan-in:** the calyx of Held is a one-to-one giant terminal — a fan-in of
    **one**, one of the two exactly known convergence figures in this file (the other is the endbulb
    of Held at the cochlear nucleus, at one or two).
  - **← cochlear nucleus, spherical bushy cells, ipsilateral**, onto the **lateral superior olive** —
    **carries:** the same monaural spectral vector, as **excitation**, uninverted. Recorded
    separately from the line above because the level-difference computation is a subtraction of two
    edges with opposite sign, and writing them as one line hid one of its two terms. **Fan-in:**
    unknown.
  - **← auditory cortex and inferior colliculus** (descending) — **payload unknown — owed.**
    **Fan-in:** unknown.
- **Outputs:**
  - **→ inferior colliculus** (lateral lemniscus, bilaterally) — **carries:** **horizontal sound
    location (azimuth)**, derived from interaural time in the medial superior olive and interaural
    level in the lateral superior olive. **This is the edge where timing stops being the payload and
    azimuth starts being it.** Elevation is not on this edge — it arrives at the colliculus from the
    dorsal cochlear nucleus's spectral notches. **What form the azimuth takes on this wire is
    contested, and this entry does not assert a place code** — see Internal structure. **Fan-out:**
    unknown.
  - **→ cochlea** (medial olivocochlear efferents) — **carries:** a gain command onto the outer hair
    cells — no content, a control signal that sets cochlear gain. **Fan-out:** unknown.
  - **→ cochlear nucleus** (glycinergic, descending) — **carries:** inhibition; no content.
    Declared at the cochlear nucleus's end, where glycine is demonstrated as a transmitter across
    all three divisions in human and chimpanzee. **The trapezoid body is a candidate origin among
    others and this edge is recorded as candidate, not established** — the human work shows the
    receptors, not the source, and the trapezoid body's own existence in human is disputed below.
    **Fan-out:** unknown. *(Class 1 for the transmitter — Front Neuroanat 18:1331230, 2024, human
    and chimpanzee; Class 2 for the origin. Not yet verified for the source.)*
  - **→ the acoustic-reflex arc** (stapedius) — **carries:** a loudness-triggered attenuation
    command. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. Physiology is gerbil, cat, guinea pig and
  chinchilla; the human work is cytoarchitecture and immunostaining on post-mortem material.
  **Nothing here is yet verified for the source.**)*

  **Nuclear sub-elements: two principal nuclei, two trapezoid-body nuclei, and a ring of periolivary
  groups.** **Medial superior olive**, **lateral superior olive**, **medial nucleus of the trapezoid
  body**, **lateral nucleus of the trapezoid body**, and the **periolivary nuclei** surrounding
  them, of which the **superior paraolivary nucleus** is the one most consistently named. The
  periolivary groups vary more between mammal species than the principal nuclei do, and the human
  ones were delineated only recently, on myeloarchitecture, location and cell morphology.
  *(Class 1 — Kulesza 2008, human.)*

  **The medial superior olive's cell is a two-sided cell, and the geometry is the computation.**
  Its principal neurons are **bipolar**, with a **lateral** dendrite and a **medial** dendrite
  extending in opposite directions from a soma lying in a thin sagittal sheet. The **ipsilateral**
  excitation arrives on one dendrite and the **contralateral** excitation on the other, so a single
  cell's two inputs are segregated by compartment — the same place-versus-owner geometry recorded
  for the cortical layer 1 tuft and the fusiform cell's two dendritic domains, and here it is what
  lets one cell compare two ears. **Glycinergic inhibition arrives separately, on the soma.**

  **Internal edges:**
  - **contralateral spherical bushy cells → medial dendrites of medial superior olive neurons** —
    **carries:** the phase-locked spectral vector from the far ear. **Fan-in:** unknown.
    **Fan-out:** unknown.
  - **ipsilateral spherical bushy cells → lateral dendrites of medial superior olive neurons** —
    **carries:** the same, from the near ear. **Fan-in:** unknown. **Fan-out:** unknown.
  - **medial nucleus of the trapezoid body → medial superior olive somata** (contralaterally
    driven, glycinergic) — **carries:** **precisely timed inhibition, and it is not a gain control —
    it sets what the cell is tuned to.** Blocking glycinergic inhibition shifts a cell's best
    interaural time difference toward zero; with the inhibition intact, the best value is displaced.
    **So the tuning of the coincidence detector is manufactured by an inhibitory input rather than
    by a difference in axonal path length**, which is the mechanism the classical account assumed.
    **Fan-in:** unknown. **Fan-out:** unknown. *(Class 1 — Brand et al. 2002; Pecka et al. 2008; gerbil.)*
  - **lateral nucleus of the trapezoid body → medial superior olive somata** (ipsilaterally driven,
    glycinergic) — **carries:** the second inhibitory term, from the near ear. Recording and
    labelling in gerbil found these neurons carrying large dendritic trees that take most of their
    synaptic input, running through and medial to the medial superior olive, and a subpopulation
    itself **binaural and sensitive to interaural time differences** — so the inhibitory supply is
    not a simple monaural relay. **Fan-in:** unknown. **Fan-out:** unknown. *(Class 1 — PMC4995217,
    gerbil.)*
  - **medial nucleus of the trapezoid body → lateral superior olive** (glycinergic) — **carries:**
    the contralateral ear's level, sign-inverted; the negative term of the subtraction. The
    projection is **topographic and consistent with the tonotopic map**, so the subtraction is
    performed frequency band by frequency band rather than on broadband loudness. **Fan-in:**
    unknown. **Fan-out:** unknown. *(Class 1 — Spangler, Warr & Henkel lineage.)*

  **The payload dispute, and it reaches this entry's Outputs.** The reading that the tonotopic sheet
  becomes a map of interaural delay — a **place code**, in which the location of peak activity is
  the azimuth — is the Jeffress model of 1948, and it is **verified in birds and disputed in
  mammals**:
  - Mammals evolved interaural-time processing **independently** of birds, so the avian
    verification does not transfer.
  - The anatomical **delay lines** the model requires are clearly demonstrated in the avian nucleus
    laminaris and are **much less clearly demonstrated in mammals**.
  - In guinea pig and gerbil, best interaural time differences depend on the cell's best frequency
    and lie **mostly outside the range the animal's head can physically produce**, while the
    **steepest slopes** of the tuning curves fall inside it — so what varies usefully with azimuth
    is the **rate of change of firing**, not which cell peaks. This supports a **population rate
    code**, and specifically a **hemispheric** one: azimuth read out as the difference in overall
    activity between the two sides, rather than as a position in a map.
  - **But this is not settled either.** Axonal recordings from medial superior olive fibres in
    chinchilla found **no clustering** of best delays at the value the hemispheric account predicts,
    and an abundance of best delays near zero and **inside** the physiological range.

  **What this file therefore records.** The **mechanism** — bilateral excitation onto a bipolar
  cell, coincidence detection, tuning set by timed glycinergic inhibition — is well supported. The
  **format of the output** is **decoded and disputed**: it has been measured, and three readings of
  it are live. That is not the same state as *owed*, and the edge is marked accordingly — the
  azimuth payload leaving this complex is real, and **whether a downstream stage should read it as a
  position in a map or as a two-sided rate difference is unresolved**. This matters more than a
  nomenclature dispute: the two readings imply different things about what the inferior colliculus
  receives. *(Class 1 — Jeffress 1948; McAlpine, Jiang & Palmer 2001; Brand et al. 2002; Pecka et
  al. 2008; Joris 2013, chinchilla; Carr & Soares 2002 for the avian case. Not yet verified for the
  source.)*

  **The human structural dispute, stated with both sides named.** Three claims are in the
  literature and they do not agree:
  - **The medial superior olive is present in every human study.** One examination of eight human
    brainstems confirms a conserved nucleus; another, of twelve brains from a normal brain
    collection, found it in **all** cases, though varying in rostro-caudal extent. This is the
    secure part.
  - **The lateral superior olive is described as prominent and highly ordered by one group and as
    not consistently identifiable by another** — the second could not reliably see a grouping of
    neurons answering to it in Nissl-stained sections. Calling the lateral superior olive
    "comparatively reduced" takes the second side of this without saying so, and this entry does
    not.
  - **The medial nucleus of the trapezoid body is the sharpest disagreement in this entry.** One
    line of work reports a well-established human nucleus with a surprisingly high cell count, and
    argues explicitly that its non-existence has been accepted too readily. Against it: an early
    count found too few cells to identify or count reliably; a 1983 study asked the question in its
    title and largely confirmed that; a 2004 description found only a small trapezoid-body nucleus
    with a few neurons and did not name a medial one; and a 2009 study reports a dramatic reduction
    of the nucleus as a compact structure in human.

  **Why the trapezoid-body dispute is load-bearing and not bookkeeping.** Every inhibitory internal
  edge above originates there. If the human nucleus is absent or vestigial, then the sign-inverting
  term of the level-difference computation, and the timed inhibition that sets interaural-time
  tuning, either arrive from somewhere else or work differently in us — and the entry's whole
  account of both cues is animal anatomy carried across a gap it cannot yet justify. **The
  disagreement is recorded, not resolved**, and the edges are kept because the function they carry
  is attested in human psychophysics even where its substrate is disputed. *(Class 1 — Kulesza 2007;
  Kulesza 2008; Kulesza & Grothe 2015; PMC12378517; Moore & Moore 1971; Richter et al. 1983;
  Koutcherov et al. 2004; Hilbig et al. 2009. Not yet verified
  for the source.)*
- **Neurons:** **medial superior olive ~15,500, lateral superior olive ~5,600 per side** (human; Kulesza 2007) — small, firm human counts, among the few in the auditory
  brainstem. **Carried with a caveat:** the lateral
  superior olive figure is a count of a structure another group could not consistently delineate in
  human, so its uncertainty is not the usual stereological band — it includes disagreement about
  what was counted. Periolivary groups uncounted. Medial nucleus of the trapezoid body: **counted
  as substantial by one group and as too sparse to count by others** (see Internal structure); no
  figure is carried here.
- **Synapses:** the calyx of Held is one of the largest synapses in the brain (one of the rare
  named, characterised terminals) and gives a **fan-in of one**; absolute counts unknown.
  **Axons:** the lateral lemniscus and olivocochlear bundle (counts unknown). **Grey-matter
  volume:** the two principal nuclei are small — histological estimates under ~6 mm³ per side
  (soft; 7-tesla magnetic-resonance probabilistic labels run larger). **White-matter volume:**
  unknown. **Myelination:** the trapezoid body and lateral lemniscus are heavily myelinated — speed
  matters for a computation working at tens of microseconds; g-ratio unknown.

## Inferior colliculus — obligatory midbrain auditory hub

- **Function:** the obligatory hub of the ascending auditory pathway — every ascending line passes
  through it. The **central nucleus** carries tonotopic isofrequency laminae, integrates the
  binaural cues, tunes for periodicity and duration in the time domain, and applies strong local
  inhibition (contrast). The surrounding **dorsal cortex** and **external cortex** are multimodal
  and non-lemniscal.
  **Two claims that read as fact elsewhere are qualified here**: that an auditory **space map** is
  present, and that this is where the brainstem's parallel lines are **summed into one
  representation**. Both are stated under Internal structure with what supports them.
- **Inputs:**
  - **← cochlear nucleus** (stellate, octopus and fusiform cells, via the lateral lemniscus), onto
    the **central nucleus** — **carries:** spectrum (rate-coded per band), broadband onset, and
    monaural spectral-notch **elevation** cues. **Fan-in:** unknown.
  - **← superior olivary complex** (lateral lemniscus, bilateral), onto the **central nucleus** —
    **carries:** **horizontal location** (azimuth), derived from interaural time and level
    differences. **This line does not read "as a place code."** Whether azimuth arrives here as a
    position in a map or as a two-sided population rate difference is **decoded and disputed**, and
    the competing readings are stated in full at the superior olivary complex. A consumer of this
    edge should not assume a map. **Fan-in:** unknown.
  - **← nuclei of the lateral lemniscus**, bilaterally, onto the **central nucleus** — **carries:**
    payload **owed**. These nuclei sit directly in the ascending path; the ventral nucleus of the
    lateral lemniscus takes the
    contralateral anteroventral cochlear nucleus and the ipsilateral medial nucleus of the trapezoid
    body and projects to the ipsilateral colliculus. **They have no entry of their own in this file,
    so this edge currently points at an unnamed structure — owed.** **Fan-in:** unknown.
    *(Class 3 — general anatomy; ScienceDirect topic overviews. Not yet verified for the source.)*
  - **← auditory cortex** (heavy descending), terminating **mainly in the dorsal and external
    cortices, not the central nucleus** — **carries:** gain and expectation; no new stimulus
    content. **Payload otherwise unknown — owed.** **The laminar target matters and the entry did
    not record it**: cortical feedback demonstrably changes the response properties of central-
    nucleus cells while terminating largely outside it, so it must act **through the internal edges
    below** rather than directly. **Fan-in:** unknown. *(Class 1 — Coomes et al.; the Palmer
    lineage, the Nakamoto lineage and the Wu & Yan lineage, as reported in PMC3422721. Not yet
    verified for the source.)*
  - **← contralateral inferior colliculus** (commissural) — **carries:** the same assembled scene
    from the other side, for bilateral comparison. Declared at the producing end as an output.
    **Fan-in:** unknown.
- **Outputs:**
  - **→ ventral division of the medial geniculate nucleus** (via the brachium; and the medial
    division, bilateral), from the **central nucleus** — **carries:** the assembled auditory scene
    on one lemniscal line — tonotopic frequency, periodicity and duration tuning, and the binaural
    cues bound together with the monaural elevation cue. **Fan-out:** unknown.
    **One measured fact about who leaves on this edge:** cholecystokinin-containing **disc-shaped**
    neurons make up about **63%** of the excitatory population of the central nucleus and project
    **exclusively** to the ventral division — so this edge has a named majority source cell class
    rather than drawing from the nucleus at large. *(Class 1 — as reported in PMC8592287, mouse. Not
    yet verified for the source.)*
  - **→ dorsal and medial divisions of the medial geniculate nucleus**, from the dorsal and external
    cortices — **carries:** the non-lemniscal, multimodal signal — broadly tuned, less precise.
    **Payload otherwise unknown — owed.** **Fan-out:** unknown.
  - **→ contralateral inferior colliculus** (commissural) — **carries:** the same auditory scene,
    for bilateral comparison. **Fan-out:** unknown.
  - **→ superior colliculus** — **carries:** auditory **azimuth and elevation**, in a frame the
    orienting map can register against the visual one. **This edge does not read "the auditory space
    map"; that phrase is
    withdrawn** — see Internal structure; what is secure is that
    spatial information reaches the orienting structure, not that it arrives as a topographic map.
    Declared at the superior colliculus's end. **Fan-out:** unknown.
  - **→ superior olivary complex and cochlear nucleus** (descending) — **payload unknown — owed.**
    **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. Species: guinea pig, cat, mouse; one squirrel-
  monkey description. **Nothing here is yet verified for the source.**)*

  **Divisional sub-elements: three.** The **central nucleus**, the **dorsal cortex**, and the
  **external cortex** (also called the lateral cortex). The first is lemniscal and tonotopic; the
  other two are non-lemniscal, multimodal, and are where the descending cortical projection lands.

  **Laminar sub-elements of the central nucleus: 10–12 fibrodendritic laminae.** Each is a sheet of
  neurons whose dendrites lie parallel to one another and to the sheet, and each sheet is an
  **isofrequency** plane. So the tonotopic axis runs *across* the laminae and each lamina is one
  frequency band. *(Class 1 — Morest 1964; Rockel & Jones 1973; Oliver & Morest 1984; Malmierca
  et al. 1995; cat.)*

  **Cell-class sub-elements: two by dendrite, and the classification cuts across transmitter.**
  **Disc-shaped** (flat, also called laminar) cells have dendrites confined to a single lamina;
  **stellate** (less flat) cells have dendrites crossing two or more. **Both classes can be
  glutamatergic or glycinergic/GABAergic**, so morphology does not predict sign — a point worth
  carrying, because the file's other entries usually get sign from cell class. Juxtacellular
  labelling in guinea pig split 32 filled cells into **laminar, 44%** — axon and dendrites inside
  one lamina — and **translaminar, 56%**, whose axons terminated in two or more laminae or in the
  surrounding cortices. Among the translaminar cells were **basket-like** cells with clusters of
  large terminal boutons. Chemically identified subsets: cholecystokinin disc-shaped cells at ~63%
  of the excitatory population; neuropeptide-Y-containing stellate cells at **38–50% of the
  GABAergic** population; a vasoactive-intestinal-peptide stellate subset with its own input and
  output pattern. *(Class 1 — Frontiers Neural Circuits 15:721015, 2021, guinea pig; PMC4220032,
  mouse; PMC3422721.)*

  **Internal edges:**
  - **disc-shaped cell → within its own lamina** — **carries:** the frequency band's signal,
    redistributed among cells tuned to the same frequency. Over 90% of laminar cells have an
    extensive local axonal tree inside their own lamina. **This is the substrate of the entry's
    "strong local inhibition (contrast)" claim** — but only partly, since a disc-shaped cell may be
    excitatory or inhibitory. **Fan-in:** unknown. **Fan-out:** unknown.
  - **stellate and other translaminar cells → two or more laminae, and into the dorsal and external
    cortices** — **carries:** payload **owed**; the only recorded route by which one frequency band
    reaches another inside this nucleus, and therefore the route any across-frequency integration
    must take. **Fan-in:** unknown. **Fan-out:** unknown.
  - **dorsal and external cortices → central nucleus** — **carries:** payload **owed** — the
    descending cortical influence, arriving in the cortices and reaching the central nucleus
    intrinsically. **This edge is inferred from a functional result, not traced**: cortical
    inactivation changes central-nucleus responses while the cortical terminals lie mostly outside
    it, and intrinsic connections are the proposed route. **Recorded as a candidate mechanism, not
    a traced projection.** **Fan-in:** unknown. **Fan-out:** unknown. *(Class 2 — the inference;
    Class 1 for the two facts it rests on.)*

  **The "everything is summed here" claim is over-stated, and the correction is specific.** The
  tempting reading is that this is the edge where the brainstem's parallel labelled lines become a
  single convergent representation, and that the hub is obligatory precisely because everything must
  be summed here. **Obligatory is right; summed is not established.** Terminals
  from the different ascending pathways are reported to be **interleaved, terminating in different
  sublaminae** within the central nucleus, with the pathways remaining **functionally segregated**
  at this level. So the lines all arrive, and they arrive in a shared tonotopic frame, and whether
  they are combined here or merely brought into register is a different question that the anatomy
  does not settle in favour of summation. **The parallel structure the cochlear nucleus creates may
  survive this stage.** *(Class 1 — Oliver et al.; Davis, as reported in PMC3422721. Not yet
  verified for the source.)*

  **The auditory space map: the phrase is barn-owl anatomy, and it does not carry to a mammal
  without the species tag.** In the barn owl there is a genuine, well-characterised topographic map
  of
  two-dimensional auditory space, and it is in the **external nucleus** of the inferior colliculus,
  built by space-specific neurons that integrate the localisation cues across frequency, and passed
  by point-to-point projection to the optic tectum — the avian counterpart of the superior
  colliculus. **In mammals the evidence is far thinner**: one study reports a topographically
  ordered representation of contralateral azimuth in the external nucleus of the guinea pig,
  explicitly as the *first* such evidence in a mammal. **Nothing read establishes a space map in the
  central nucleus of any mammal**, and nothing establishes one in human at all.
  **What this entry claims:** the localisation cues are present here and are bound into a common
  tonotopic frame; a topographic **map** of space is owl anatomy with a single mammalian report, and
  that report is in the **external** nucleus rather than the central one. Recorded as **contested
  and mis-sited**, not deleted. Note the shape of the error — it is the same one the superior
  olivary complex entry
  carried: **a code verified in birds, asserted for mammals.** *(Class 1 — Knudsen & Knudsen 1983;
  Wagner et al. 1987; PMC3913906 and PMC3394089 for the owl; Binns et al. 1992, guinea pig, for the
  mammalian report. Not yet verified for the source.)*
- **Neurons:** central nucleus ~420,000, in a volume of ~22.4 mm³ (verified, exact primary source:
  Wong et al. 2019, human). Whole colliculus with the dorsal and external cortices ~0.6M
  (best-available extension).
- **Synapses:** unknown. **Axons:** unknown.
- **Grey-matter volume:** central nucleus ~22.4 mm³ (verified, same source). Whole-colliculus
  volume: ~0.02 cm³ range; total magnetic-resonance figures exist but are not recorded here
  per-slot yet.
- **White-matter volume:** unknown. **Myelination:** unknown.
- **Density cross-check available:** ~420,000 neurons / 22.4 mm³ ≈ 18,750
  neurons/mm³ (far below V1's ~60,000/mm³ — subcortical nuclei are less densely
  packed).

## Medial geniculate nucleus — auditory thalamus (also called the medial geniculate body)

- **Function:** auditory thalamic relay to cortex — the auditory counterpart of the lateral
  geniculate nucleus. Three divisions: the **ventral division** (tonotopic, sharply tuned,
  lemniscal, to the auditory core — the "what"); the **dorsal division** (non-tonotopic, to the
  belt and secondary cortex); and the **medial division** (also called magnocellular — broadly
  tuned, multisensory and vestibular, a fast route projecting widely and to the amygdala).
  **The three divisions are not three flavours of one relay, and the difference is what drives
  them.** The ventral division is a **first-order** relay: its driving input is subcortical, from
  the inferior colliculus, exactly as the lateral geniculate nucleus is driven by the retina. The
  dorsal and medial divisions are substantially **higher-order** relays: their driving input comes
  from **layer 5 of auditory cortex**, so they carry cortical output back into the thalamus and out
  to another cortical area — a cortico-thalamo-cortical, or transthalamic, route between cortical
  areas rather than a stage on the way up from the ear. **This distinction was absent from the
  entry and it changes what one of its edges carries** (see Inputs). *(Class 1 — Sherman & Guillery
  1996; Sherman & Guillery 1998; Sherman 2017; Frontiers Neural Circuits 15:721186, 2021.
  Not yet verified for the source.)*
- **Inputs:**
  - **← inferior colliculus** (via the brachium; the ventral division is the main lemniscal relay
    from the central nucleus) — **carries:** the assembled auditory scene — tonotopic spectrum,
    periodicity and duration tuning, and the binaural localisation cues bound with the monaural
    elevation cue. **"The auditory space map" is withdrawn from this line**, for the reasons stated
    at the inferior colliculus. The **driver** for the ventral division, and as at the lateral
    geniculate nucleus a minority of the synapses. **Fan-in:** unknown.
    **This ascending driver is partly inhibitory, which is unusual and is not what "driver"
    normally implies.** GABAergic cells make up roughly **20%** of the collicular input to the
    ventral and medial divisions, about **11%** to the dorsal division, and **4%** to the
    suprageniculate nucleus; in rat the GABAergic share of the whole tectothalamic pathway runs to
    ~40%, in cat ~20%. **So the edge that sets what the message is also carries a substantial
    inhibitory component**, and a downstream stage modelling it as purely excitatory drive would be
    wrong about a fifth of it. *(Class 1 — PMC4220731 and PMC3978371, guinea pig; Peruzzi et al.,
    rat; Winer et al., cat. Not yet verified for the
    source.)*
    **The collicular projection is itself three parallel pathways, not one** — described as a
    lemniscal or tonotopic pathway, a polysensory pathway, and a diffuse pathway, terminating
    preferentially in the ventral, medial and dorsal divisions respectively. This is the same
    parallel structure the inferior colliculus entry records as possibly surviving that stage rather
    than being summed there, and here it is still three. **Fan-in:** unknown.
  - **← primary auditory cortex, layer 6** (corticothalamic feedback, small terminals) —
    **carries:** no new content; **modulatory** — it sets whether and how strongly the driver
    payload passes, the same driver/modulator arrangement declared at the lateral geniculate
    nucleus. Reaches **all three divisions**. **Fan-in:** unknown.
  - **← auditory cortex, layer 5** (giant terminals), onto the **dorsal and medial divisions** —
    **carries:** **cortical content — this is a driver, not a modulator, and it does not
    carry "no new content."** Layer-5 corticothalamic axons end in large
    terminals and behave as feedforward drivers, which is what makes the dorsal and medial
    divisions higher-order relays. The payload is whatever that cortical area computed, on its way
    to another cortical area. **What it is, as a type, is owed** — the same hole this file records
    at the pulvinar and at every higher-order relay. **Merging this edge with the layer-6 one and
    calling the pair
    "massive corticothalamic feedback, giant terminals ... modulatory" is internally
    contradictory**: giant terminals are the signature of a driver. The two are kept split.
    **Fan-in:** unknown. *(Class 1 — Sherman & Guillery lineage;
    Rovó et al. 2012 for the vesicular-glutamate-transporter separation of the two terminal classes;
    Rouiller & Welker 2000 for the species variability in which cortical area supplies the giant
    terminals. Not yet verified for the source.)*
  - **← thalamic reticular nucleus** — **carries:** inhibition; the gate. The auditory sector of
    that nucleus is itself layered by relay class — a central layer taking first-order input, inner
    and outer layers taking higher-order — so the gate is applied separately to the two relay
    types. **Fan-in:** unknown. *(Class 1 — Guillery et al. 1998. Not yet verified for the source.)*
- **Outputs:**
  - **→ auditory core**, from the **ventral division** — **carries:** the lemniscal payload,
    sharply tonotopic and substantially unchanged in content — the auditory "what," relayed and
    **gated**, not transformed. **Fan-out:** unknown.
  - **→ belt and parabelt**, from the **dorsal division** — **carries:** the non-tonotopic,
    broadly-tuned signal, **and, on the higher-order limb, cortical content returning from layer
    5.** **Payload otherwise unknown — owed.** **The parabelt limb is the one to note**: this
    division is not tonotopically organised and therefore cannot be what imposes a frequency map on
    that tier.
    **Fan-out:** unknown. *(Class 1 — Hackett, Stepniewska & Kaas 1998b, macaque.)*
  - **→ wide cortical targets and the amygdala**, from the **medial division** — **carries:** a
    coarse, broadly tuned, multisensory alarm signal — enough to say *something loud and sudden
    happened, roughly there*, and not enough to identify it. This is the fast subcortical "low
    road," and its payload is deliberately impoverished: that is what makes it fast. **Fan-out:**
    unknown.
  - **→ inferior colliculus** (descending), from the **medial division** and the associated
    suprageniculate, posterior intralaminar and subparafascicular nuclei — **carries:** payload
    **owed**. Recorded with a specific negative alongside it: **the ventral and dorsal divisions
    send no return projection to the colliculus**, so the descending limb of this relay does not
    mirror its ascending one. **Fan-out:** unknown. *(Class 1 — Senatorov & Hu 2002; Winer et al.
    2002. Not yet verified for the source.)*
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. Species: cat, monkey, rat, bat, guinea pig; the
  species spread is itself a finding here. **Nothing here is yet verified for the source.**)*

  **Divisional sub-elements: three**, as the Function field names — **ventral**, **dorsal**, and
  **medial**. The medial division is heterogeneous in cell size and shape, from tiny cells to
  magnocellular ones intermingled, and **no further subdivision of it could be made**; it holds the
  largest neurons of the complex. The ventral division may divide further into lateral-ventral and
  ovoid parts, on the pattern described in other species, but definitive human evidence is not
  presented. *(Class 1 — Winer et al. 1999; Morest 1964.)*

  **Laminar sub-elements of the ventral division, and the same geometry appears for the third time
  in this pathway.** The principal cells are **bi-tufted** neurons: an elongated soma with
  **diametrically opposed dendritic fields** extending from its two poles. They sit closely spaced
  in **rows about 50–100 µm wide**, dendritic fields oriented dorsolateral to ventromedial, forming
  **fibrodendritic laminae** hypothesised to correspond to the ordered projection arriving from the
  central nucleus of the inferior colliculus — which is what makes the division tonotopic.
  **Note the recurrence:** the medial superior olive's bipolar cell, the inferior colliculus's
  disc-shaped cell, and this bi-tufted cell all build isofrequency sheets out of cells whose
  dendrites lie in the plane of the sheet. Three stages, one geometry, and the file has not
  remarked on it before. *(Class 1 — Winer et al. 1999, cat and monkey.)*

  **Cell-class sub-elements: principal cells and local interneurons — and the interneuron
  proportion is the most species-variable number in this pathway.** The principal cells are
  glutamatergic. The GABAergic local interneurons run from **under 1% in bat and rat — with some
  divisions in bat having none at all — to 25% or more in cat and monkey**, with primate thalamus
  generally reported around 25–30%. **This is specific to the auditory thalamus:** the lateral
  geniculate nucleus holds about the same proportion across species, and the inferior colliculus and
  auditory cortex likewise. Only the medial geniculate body swings this way.
  **Why this matters more than a species caveat usually does.** Rodent work is the bulk of modern
  circuit physiology, and in the rodent this nucleus has **essentially no interneurons** — its
  inhibition comes from the reticular nucleus alone. In cat, monkey and by extension human, a
  quarter of the cells are local inhibitory ones and there are **two independent inhibitory
  systems**. A circuit for this nucleus taken from mouse would be missing an entire population that
  is present in us. Recorded as the sharpest transfer hazard in the auditory pathway so far.
  *(Class 1 — Winer & Larue 1996; Fitzpatrick et al. 1984; Benson et al. 1991; Hunt
  et al. 1991; Arcelli et al. 1997; Braak & Bachmann 1985. Not yet verified for the source.)*

  **Internal edges: owed, and the gap is now specific rather than general.** No internal edge is
  recorded here. What the interneurons contact, whether this nucleus builds the triadic glomerulus
  its visual counterpart does, and whether the three divisions exchange signal, are not established.
  **The triad question is the pointed one**: the lateral geniculate entry in
  this file carries a detailed triadic circuit — retinal terminal onto both a relay dendrite and an
  interneuron dendrite, that interneuron dendrite onto the same relay dendrite, all wrapped in a
  glial sheath — and whether the auditory relay does the same is exactly the kind of thing the
  interneuron figures above make answerable in primates and unanswerable in rodents.
- **Functional robustness (bilateral pathway).** The ascending auditory pathway is
  heavily crossed and bilateral from the cochlear nucleus upward, so each ear reaches
  this nucleus in *both* hemispheres. A unilateral lesion therefore causes little or no
  hearing loss; central ("thalamic") deafness requires *bilateral* damage, which is
  clinically rare — a compact, obligatory relay whose small size is offset by this
  redundancy (lesion literature: bilateral thalamic infarction → central deafness with
  a normal peripheral audiogram and brainstem auditory evoked response). The same holds
  one level up: cortical deafness needs bilateral damage to Heschl's gyrus or to the
  thalamocortical radiation.
- **Neurons:** **~1.8–2.3M per hemisphere, soft** (no direct human count). Two cues bracket
  it: it is usually taken as comparable to the lateral geniculate nucleus's firm ~1.8M
  (Dorph-Petersen et al. 2008); and a volume cross-check at that nucleus's ~17,000 neurons/mm³ ×
  this one's verified ~134 mm³ implies ~2.3M (this being the larger nucleus). Both sit above the old
  ~1M placeholder, but no primary human stereology anchors it. **A partition is now available in
  principle:** if the primate interneuron proportion holds in human, roughly a quarter of whatever
  the total is are local inhibitory cells that project nowhere outside the nucleus, and are
  therefore not part of the thalamocortical output count.
- **Synapses:** unknown. **Axons:** unknown.
- **Grey-matter volume:** ~134 ± 7 mm³ per hemisphere (human; PMC9504316). Slightly larger than the lateral
  geniculate nucleus (~100 mm³), consistent with the auditory relay's three-division bulk.
- **White-matter volume:** unknown. **Myelination:** unknown.

## Primary auditory cortex — the auditory core (Heschl's gyrus, isocortex)

- **Function:** the auditory core — the koniocortical, tonotopic fields taking the lemniscal
  thalamic drive. A tonotopic map carrying **spectrotemporal receptive fields**: frequency tuning,
  onset and offset, the direction and rate of **frequency-modulated sweeps**, bandwidth,
  intensity, and temporal modulation. Shortest cortical latency of any auditory field.
  A left/right asymmetry begins here as a **processing bias**: the left favours finer temporal
  resolution, the right finer spectral resolution (Zatorre & Belin 2001; Poeppel 2003 — framed as a
  bias and a trade-off, not a hard dichotomy).
  **How many fields the core contains, and how its map is laid out, are both unsettled in human** —
  see Internal structure.
- **Inputs:**
  - **← medial geniculate nucleus, ventral division**, point-to-point onto layer 4 (a **minority**
    driver — ~20% of this area's excitatory input is thalamic, ~80% intracortical) — **carries:**
    the tonotopic spectrum with periodicity and duration tuning, and the binaural localisation cues
    bound with the monaural elevation cue. **"The space map" is withdrawn from this line**, for the
    reasons stated at the inferior colliculus. **Fan-in:** unknown.
  - **← belt** (descending), principally onto **layer 1** — **carries:** payload **owed**. Declared at the belt's end as a corticofugal output to the core. **Fan-in:**
    unknown. *(Class 3 — general cortical pattern.)*
  - **← contralateral primary auditory cortex** (callosal; through the central body, posterior body
    and dorsal splenium of the corpus callosum) — **carries:** **the same frequency band's activity
    from the other hemisphere, and what it does with it is sharpen rather than add.** Stated in
    full under Internal structure. **Fan-in:** unknown. *(Class 1 — sources at the internal-edge
    entry below. Not yet verified for the source.)*
- **Outputs:**
  - **→ auditory parabelt** — **carries:** payload **owed**, and the edge is **weak**: tracer
    injections confined to the parabelt label only **few** neurons here, against large numbers in
    the belt. Recorded against the tempting strict hierarchy — nothing reaching the parabelt
    directly from the core — because *few is not none*. **Fan-out:** unknown, and
    small. *(Class 1 — Hackett, Stepniewska & Kaas 1998a, macaque. Not yet
    verified for the source.)*
  - **→ belt** — **carries:** the **spectrotemporal receptive-field code** — frequency tuning,
    onset and offset, frequency-modulated sweep direction and rate, bandwidth, intensity, temporal
    modulation, on a tonotopic map. This is the auditory counterpart of V1's oriented-edge code:
    local features, not objects. Left and right differ as a **bias**, not a dichotomy — the left
    favours finer temporal resolution, the right finer spectral resolution — so the two hemispheres'
    payloads are **no longer identical from here on**. **Fan-out:** unknown.
  - **→ medial geniculate nucleus, from layer 6, and inferior colliculus** (corticofugal) —
    **carries:** no new content; the modulatory / gating signal. The geniculate limb reaches all
    three divisions; the collicular limb lands mainly in the dorsal and external cortices rather
    than the central nucleus. **Fan-out:** unknown.
  - **→ medial geniculate nucleus, dorsal and medial divisions, from layer 5** (giant terminals) —
    **carries:** **cortical content, as a driver** — the payload this area computed, routed back
    into the thalamus and out to another cortical area rather than down the descending control
    path. **What it is, as a type, is owed.** **This edge did not exist in this entry and its
    absence made the corticofugal output look purely modulatory**; the two limbs leave from
    different layers and do different jobs. Declared at the geniculate's end. **Fan-out:** unknown.
    *(Class 1 — Sherman & Guillery lineage; Rovó et al. 2012. Not yet verified for the source.)*
  - **→ contralateral primary auditory cortex** (callosal), from **layers 3 and 5** — **carries:**
    this hemisphere's activity in a given frequency band, delivered to the band that matches.
    Stated in full below. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. **Unusually for this pathway, most of what
  follows is human** — cytoarchitecture on post-mortem brains and functional imaging in living
  subjects. Nothing here is yet verified for the source.)*

  **Areal sub-elements: three in human, named, and they are not the macaque's three under different
  labels.** Observer-independent cytoarchitectonic mapping of ten human brains divides the primary
  auditory cortex (**area Te1**, corresponding to Brodmann area 41) into **Te1.1**, **Te1.0** and
  **Te1.2**, following each other in a **medial-to-lateral sequence along the long axis of Heschl's
  gyrus**, which itself runs posteromedial to anterolateral. All three are koniocortical with a
  well-developed layer 4; the borders come from quantitative differences, not from a change in
  character. **Te1.0**, in the middle, is the one usually equated with the auditory core proper, and
  it carries the **highest myelination of any area in the temporal cortex**. *(Class 1 — Morosan et
  al. 2001; Schleicher et al. 1999 for the border algorithm; eLife 9:e56963,
  2020, for the myelination measure. Human.)*

  **The correspondence to the macaque core is not established.** In
  macaque the core is three fields — the **primary auditory field**, the **rostral field** and the
  **rostrotemporal field**
  — stacked posterior to anterior. Human cytoarchitecture is consistent with three primary-like
  fields along Heschl's gyrus, but **functional imaging mostly finds two**, read as the homologues
  of the primary auditory field and the rostral field, and a third is rarely seen. One reading maps
  Te1.0 to the core and
  treats **Te1.1 and Te1.2 as medial junction and lateral belt** rather than as primary fields at
  all — which would make the human core **one** area, not three. **Naming the core by the macaque field
  abbreviations for the primary, rostral and rostrotemporal fields, without saying that this is a
  macaque scheme applied to human on an unsettled homology, is the error to avoid here.** Recorded
  as unsettled. *(Class 1 — PMC4585487, human and macaque; Moerel et al. 2014. Not yet verified for
  the source.)*

  **The tonotopic map's orientation in human is genuinely disputed, and the disagreement is about
  the map's geometry, not its existence.** Proposals on record: the gradient runs **parallel** to
  Heschl's gyrus; it runs **perpendicular** to it; it is **circular**; and it is a
  **high-low-high** gradient along the posteromedial-to-anterolateral axis, with the high-frequency
  regions forming an inverted V around the gyrus. Intracranial recording with depth electrodes finds
  a high-to-low gradient within **posteromedial** Heschl's gyrus specifically. Candidate causes of
  the disagreement are named in the literature: the limited temporal resolution of functional
  imaging, different synthetic stimuli, and the limited coverage of the gyrus that depth electrodes
  achieve.
  **Why this belongs in a data-flow file rather than an atlas.** The entry declares a tonotopic map
  as the payload arriving on the thalamic edge and leaving on the edge to the belt. **A map is a
  spatial claim**, and if the axis is unknown then "tonotopic" is a statement that frequency is
  ordered somehow, not a statement of what is where. That is weaker than the payload rule wants,
  and it is weaker than what a downstream rung would need to build one. **Owed: the axis.**
  *(Class 1 — the four proposals as reviewed in PMC8608271, human; Da Costa et al. 2011; Moerel
  et al. 2014; depth-electrode results in the same review. Not yet verified for the source.)*

  **A gradient that is not frequency, and it runs along the same axis.** Response **latency
  increases from the posteromedial to the anterolateral** part of Heschl's gyrus, for tones and for
  isolated syllables. The lateral part responds more to speech than to other sounds, and the
  posteromedial part encodes the temporal modulation of speech differently from the anterolateral
  part. **So the long axis of the gyrus carries a processing gradient regardless of how the
  frequency map sits on it** — which is a candidate explanation for why the frequency map has been
  hard to pin: the axis may be doing more than one job. Recorded as a candidate, not a finding.
  *(Class 1 — as reviewed in PMC8608271, human.)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided but
  **koniocortical**, meaning unusually dense and granular, which is the architectural signature of
  a heavy thalamic driver. *(Class 3 for the eight; Class 1 for the koniocortical character.)*

  **Tangential sub-elements: unknown in human.** No repeating compartmentation of the kind V1's
  cytochrome-oxidase patches or the middle temporal area's direction columns represent is
  established for this area.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout. **These matter more here
  than usual**: only ~20% of this area's excitatory input is thalamic, so roughly four fifths of what
  drives it arrives on intracortical edges, and the laminar set above is the only description this
  file has of them.

  **The callosal edge, stated here once for the whole auditory cortex.** *(Species: cat, ferret,
  mouse, bat, macaque; human only for the tract's route and the clinical evidence. Nothing here is
  yet verified for the source.)*

  **Audition's callosal wiring is not like vision's or touch's, and the difference is the first
  thing to record.** In visual and somatosensory cortex, callosal connections are **restricted** —
  to the representation of the **vertical meridian** in vision, and to **proximal body**
  representations in somatosensation. Both restrict the connection to the representational
  **midline**, because that is where the two half-maps must be stitched. **Audition has no such
  midline to stitch**, and correspondingly its callosal connections are **widespread across the
  entire tonotopic map** — essentially every part of the primary field projects contralaterally.
  **So the auditory callosum is not a seam, and treating it as one would be a category error.**
  *(Class 1 — Code & Winer 1985; Code & Winer 1986; Hackett & Phillips 2011; contrasted with Hubel & Wiesel
  1967 and Jones & Powell 1968.)*

  **What it connects: matched frequency, mostly matched area.** Callosal axons connect tonotopic
  regions to the **corresponding frequency domains** across the hemispheres. The projections are
  principally **homotopic** — primary field to primary field — with heterotopic connections (say,
  primary to a secondary field) **less prevalent**. In the association fields the balance shifts:
  heterotopic interaction plays a larger role there, and **sensory association cortices are
  altogether more callosally connected than the primary sensory cortices**. *(Class 1 — Diamond
  et al. 1968; Imig & Brugge 1978; Rouiller et al. 1991; Morel et al. 1993; Lee & Winer 2008;
  Gazzaniga 1987.)*

  **Laminar routing, and it is not the thalamic pattern.** Origin: **layers 3 and 5**, with nearly
  **90%** of the projection arising from those two. Termination: **throughout layers 2–6** at the
  homotopic locus, densest in **layers 2 and 3**, and **sparsest in layer 4**. **So the callosal
  input deliberately avoids the layer the thalamic driver targets** — it arrives where the local
  computation is, not where the message enters. That is a laminar signature distinguishing this
  edge from the ascending one, and it is the kind of fact this file's layer stack exists to carry.
  *(Class 1 — Ravizza et al. 1976; Kelly & Wong 1981; Code & Winer 1985; Code & Winer 1986; Games &
  Winer 1988;
  Aitkin et al. 1988; Lee & Winer 2008a; cat.)*

  **Where it lands tangentially: on the binaural columns, selectively.** Callosal projection
  neurons and their terminals are **patchy**, and the patches correlate with the patchy
  distribution of **binaural columns** — preferentially over regions showing **binaural summation**
  or **ipsilateral dominance and suppression**, and *not* over regions of monaural contralateral
  response or contralateral dominance. **The callosum talks to the parts of the map that already
  care about both ears**, which is a strong constraint on what the edge can be for. *(Class 1 —
  Imig & Brugge 1978, cat; Fitzpatrick & Imig 1980; Liu & Suga 1997, bat;
  Wallace & Harper 1997.)*

  **The sign is mixed, and the mechanism for the mixture is known.** **Every callosal fibre is
  excitatory** — they arise from pyramidal cells and are glutamatergic — so any inhibitory effect
  must be **feedforward, through local interneurons the callosal fibres excite**. That is what is
  observed: in awake mouse, brief activation of callosal input drove **short-latency inhibition in
  the majority of responsive regular-spiking cells**, while **fast-spiking parvalbumin cells were
  almost exclusively excited**; slice work locates the mechanism in layer-5 parvalbumin cells
  mediating feedforward inhibition of pyramidal cells; intracellular recording in cat shows
  excitatory postsynaptic potentials **often followed by** inhibitory ones. Against that, cooling
  one hemisphere in anaesthetised cat **reduced** sound-evoked activity in the other, implying net
  excitatory drive — though anaesthesia is a live confound there, and ferret stimulation gives
  excitatory, inhibitory and mixed effects depending on parameters. **Recorded as: excitatory
  fibre, net effect disputed and probably cell-type-dependent.** *(Class 1 — eNeuro
  7:ENEURO.0256-20, 2020, awake mouse; Rock & Apicella 2015; Mitani & Shimokouchi
  1985; Carrasco et al. 2013; Kitzes & Doherty 1994.)*

  **What the payload is, and it is not content.** The measured consequences of the edge are
  **sharpened frequency tuning** and **enforced signal-to-noise ratio** — the awake-mouse study's
  own summary. In the bat's delay-tuned area, focal stimulation on one side shifted best delays in
  all three subdivisions of the contralateral area, described as **focused facilitation with
  widespread lateral inhibition**. **So this edge carries a normalisation, not a message**: it is
  the same computation lateral inhibition performs within a map, executed across the midline. **A
  consumer that treats it as a second copy of the other hemisphere's percept would be wrong about
  what it does.** *(Class 1 — eNeuro 7:ENEURO.0256-20, 2020, mouse; J Neurosci 27:8405, 2007,
  mustached bat.)*

  **And it is what maintains the hemispheric asymmetry — which bears directly on the lateralisation
  disputes recorded three entries downstream.** In rhesus monkey, the **left** dorsotemporal pole of
  the superior temporal gyrus is more active for species-specific calls than the right.
  **Callosotomy increases the right pole's activity and eliminates the asymmetry.** So the
  asymmetry is not an intrinsic property of each hemisphere operating alone — it is **actively
  maintained by interhemispheric inhibition**, and it disappears when the edge is cut. **This is
  the mechanism the anterior temporal and prosodic entries were arguing about the existence of**,
  and it suggests the right framing for both: lateralisation is a *dynamic equilibrium held by an
  edge*, not a *static division of labour between two tissues*. Recorded as a candidate reading of
  those disputes, not as their resolution. *(Class 1 — Poremba et al. 2004, rhesus, as reported in
  J Neurosci 27:8405, 2007. Not yet verified for the source.)*

  **Internal edges — between Te1.1, Te1.0 and Te1.2: owed.** Whether the three exchange signal, in
  which direction, and carrying what, is not established — and under the reading that
  Te1.1 and Te1.2 are junction and belt rather than core, two of these would be **inter-region**
  edges rather than internal ones. **The slot cannot be filled until the areal question above is
  settled**, which is a case of a sub-element boundary being load-bearing for edge classification.
- **Neurons:** ~20M per hemisphere (best available; Heschl's gyrus is small and
  highly variable, with a left>right volume asymmetry). **The variability is not measurement
  noise** — the gyrus's morphology differs markedly between individuals and between the two
  hemispheres of one brain, including in the number of transverse gyri present.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown
  (Heschl's gyrus, small, variable). **White-matter volume:** unknown.
  **Myelination:** koniocortical (heavily granular); **Te1.0 carries the highest myelin-related
  contrast in the temporal cortex**, with the value falling off with distance from the gyrus
  (human, ratio of T1- to T2*-weighted magnetic-resonance signal). A g-ratio is not recorded.

## Auditory belt — secondary auditory cortex (isocortex)

- **Function:** nonlinear spectral and temporal integration — tuning to band-passed-noise
  bandwidth, to the rate and direction of **frequency-modulated sweeps**, and to a limited
  set of species-specific vocalizations; broader tuning than the core. Lateral belt neurons respond
  better to broad spectral stimuli — broadband and narrowband noise — than to pure tones, which is
  the operational difference from the core. **Tonotopy survives here but only shows itself with the
  right probe**: with narrowband noise, the best centre frequency does vary systematically, with
  reversals at the borders between lateral belt fields, and those reversals are how the field
  borders are drawn.
  The auditory **"what" / "where" split** opens here: the **anterolateral** field is
  call- and identity-selective ("what"); the **caudolateral** field is location-selective ("where").
  **The split is real and graded rather than clean** — see Internal structure — and stating it as a
  dichotomy between two fields would misdescribe a belt that has eight.
- **Inputs:**
  - **← primary auditory cortex (the core)** — **carries:** the spectrotemporal feature code,
    tonotopic. **Fan-in:** unknown.
  - **← medial geniculate nucleus, dorsal division** (diffuse) — **carries:** the non-tonotopic
    thalamic signal. **Payload otherwise unknown — owed.** **This is the belt's preferential
    thalamic source**, and it is the same division the geniculate entry identifies as a
    substantially **higher-order** relay driven by cortical layer 5 — so part of what arrives here
    is cortical output returning through the thalamus, not a fresh ascending signal. **Fan-in:**
    unknown. *(Class 1 — Burton & Jones 1976; Morel & Kaas 1992; de la Mothe et al. 2012, marmoset.)*
  - **↔ the contralateral counterpart of this area** (callosal, reciprocal) — **carries:** a
    **normalisation, not a message** — sharpening and signal-to-noise enforcement, delivered from
    layers 3 and 5 onto layers 2/3 of the far side and avoiding layer 4. Mechanism, sign and
    evidence are stated once, in full, at the primary auditory cortex. **Association fields are
    more heavily callosally connected than primary fields, and carry proportionally more
    heterotopic traffic**, so this edge is denser here than there and less strictly area-to-area.
    **Fan-in / fan-out:** unknown. *(Class 1 — Gazzaniga 1987; Lee & Winer 2008; Hackett et al.
    1999 for the parabelt specifically. Not yet verified for the source.)*
- **Outputs:** **the what/where split opens on the first two edges, and the payloads differ:**
  - **→ rostral parabelt**, from the **anterolateral** field — **carries:** call and **identity**
    features — bandwidth, frequency-modulated sweep rate, and a limited set of species-specific
    vocalizations; broader tuning than the core, and no location. **Fan-out:** unknown.
  - **→ caudal parabelt**, from the **caudolateral** field — **carries:** **sound-source location
    (azimuth)**; not identity. **This edge does not read "the space map, now cortical"; that phrase
    is withdrawn** — there is no map. What is on this wire is an **opponent hemifield rate
    code**, stated in full under Internal structure. **Fan-out:** unknown.
  - **→ prefrontal cortex, directly** — **carries:** the same two payloads, split by origin and
    kept split at the destination: the **anterior** belt reaches the frontal pole (area 10), the
    rostral principal sulcus (area 46) and ventral prefrontal areas 12 and 45; the **caudal** belt
    reaches the caudal principal sulcus and the **frontal eye field** (area 8a). **This edge does
    not run through the parabelt**, and it matters because it shows the two streams are separated by
    their *targets* and not only by their response properties, and because the caudal target being
    the frontal eye field says plainly what the
    "where" payload is for — moving the eyes to the sound. **Fan-out:** unknown. *(Class 1 —
    Romanski et al. 1999, rhesus. Not yet verified for the source.)*
  - **→ primary auditory cortex (the core), medial geniculate nucleus and inferior colliculus**
    (corticofugal) — **payload unknown — owed.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. Species: macaque and marmoset for the field
  scheme, cat and macaque for the spatial code, human functional imaging where noted. **Nothing here
  is yet verified for the source.**)*

  **Areal sub-elements: eight fields, not two.** The belt is a
  ring around the core, divided into a **lateral belt** — **caudolateral**, **middle lateral**,
  **anterolateral**, and **rostrotemporal lateral** — and a **medial belt** — **caudomedial**,
  **middle medial**, **rostromedial**, and **rostrotemporal medial**. Each lateral field sits beside
  a core field and each medial field beside the same core field on the other side, so the ring is
  organised by its relation to the core rather than as a sequence of its own. Earlier versions of
  the scheme counted seven. *(Class 1 — Kaas & Hackett 2000; Kaas et al. 1999;
  de la Mothe et al. 2012, marmoset.)*

  **The medial belt is poorly characterised in the literature.** The four medial fields have been
  less well defined physiologically than the
  lateral ones; what is reported is that they show broad **spatial** tuning. So the "where" function
  may be distributed around the medial half of the ring as well as sitting in the caudolateral
  field. **Owed: what the medial belt carries, and to where.** *(Class 1 — Kosaki et al.
  1997; Woods et al. 2006, macaque.)*

  **The spatial payload is not a map, and this is the third stage in this pathway where a map is
  asserted and is not there.**
  The auditory cortex has been searched for a topographic map of auditory space and none has been
  found — one review of years of negative results by several groups concludes flatly that there
  isn't one. What is there instead is an **opponent hemifield population rate code**: two broadly
  tuned populations, one preferring the left hemifield and one the right, with location read out
  from the **balance between them**. Two properties of that code matter to a consumer:
  - **Location is carried by the region of steepest change in the response-azimuth function, not by
    the peak.** A downstream stage looking for a maximum finds nothing useful.
  - **It is robust to sound level.** Because location is encoded by the slope rather than the peak
    response, changing loudness does not move the represented position — which a peak code would
    not survive.
  Its resolution is correspondingly coarse: cortical units discriminate left from right reliably
  and confuse locations *within* a hemifield, with median localisation errors near the theoretical
  limit for perfect left/right discrimination with within-hemifield confusion.
  *(Class 1 — Middlebrooks 2021; Stecker, Harrington & Middlebrooks 2005, cat; Werner-Reiss & Groh
  2008, macaque; human, in the Salminen lineage and the Krumbholz lineage. Not yet verified for the
  source.)*

  **Why this one is worth more than the two before it.** The place code withdrawn at the superior
  olive and the space map withdrawn at the inferior colliculus were both **replacements of an
  asserted code with an unsettled one**. This is different: the replacement code is **positively
  established**, in several species including human, and it is *the same form of code* the
  contested reading at the superior olive proposes — two opponent populations, read out by slope
  rather than peak. **That does not settle the olive**, which is about a different structure at a
  different stage and remains disputed. But it does mean the opponent-slope format is demonstrably
  what the mammalian auditory system uses somewhere, which was not established when that entry was
  written. Recorded as **bearing on the olive's dispute, not resolving it.**

  **The what/where split: supported, and graded rather than clean.** The functional evidence is that
  when species-specific calls are played from varying locations, anterolateral neurons are more
  specific for **call type** and caudolateral neurons more responsive to **location** than either
  the core or the anterior belt. The anatomical evidence is the prefrontal targeting above. **But
  the belt's projections to the parabelt are described as overlapping patterns**, and the
  temporal-field connections of the two streams overlap more than the frontal ones do. **So the
  streams separate progressively rather than at a border**, and the entry's clean two-edge
  presentation over-states the separation at this stage. *(Class 1 — Tian et al. 2001; Kaas &
  Hackett 2000; Romanski et al. 1999; macaque.)*

  **What the payload on the prefrontal edges actually is: sound, not meaning, and the test was
  run.** The belt's identity payload is described in this file, and in the literature, using the
  phrase *species-specific vocalizations* — which invites reading it as communication content.
  **Three results say it is acoustic:**
  - Single units in ventrolateral prefrontal cortex, one target of this edge, respond **more
    similarly to acoustically similar calls than to acoustically dissimilar but semantically
    similar ones**. Warbles and coos — alike in sound — cluster together; warbles and harmonic
    arches — both high-value food calls, unlike in sound — do not. **The clustering follows
    acoustics, not referent.**
  - Functional imaging of the vocalization network found that **spectrotemporal control sounds
    derived from the calls — "scrambled calls," which mean nothing — also activated the frontal
    and parietal regions.** The authors record this as surprising. Call-*selective* responses were
    most prevalent in the anterior superior temporal gyrus, that is, in temporal cortex and not in
    frontal cortex.
  - At the low stages of the pathway, vocalizations are **not represented any differently from
    other sounds**; the overrepresentation of behaviourally relevant stimuli emerges only at the
    highest stages. So call selectivity is built gradually and this tier is partway along it, not
    at its end.
  **But the opposite pole is excluded too, and by a directly relevant control.** Prefrontal
  auditory neurons **do not readily respond to simple acoustic stimuli**: they are preferentially
  driven by species-specific vocalizations **compared with pure tones, noise bursts, and other
  complex sounds**, and pure tones scarcely drive them at all. **So the destination of this edge is
  not responding to sound in general either.** *(Class 1 — Romanski & Goldman-Rakic 2002; Averbeck
  & Romanski 2004; Russ et al. 2008; rhesus.)*

  **The honest payload for this edge is therefore neither "sound" nor "meaning" but a third thing:
  the complex, call-like spectrotemporal *class*** — abstracted well above tones and noise, and not
  yet organised by referent.
  **The scrambled-call result does not discriminate as sharply as it first appears, and the reason
  is worth stating.** A scramble derived from a call **retains the call-like spectrotemporal
  statistics**; it is not a random sound. A region that responds to the call-like acoustic class
  and a region that **attempts to interpret anything call-like** predict the *same* result — both
  activate. The study cannot separate them, and the decisive control would be sounds matched in
  complexity that are **not call-derived**; none is on record here. **Recorded as a limit of
  the evidence, not as a finding against meaning.**
  **Two further caveats.** In the rhesus repertoire, specific spectrotemporal features distinguish
  the call types, so acoustic and semantic clustering are **confounded in the natural stimulus
  set** — the acoustic result shows that meaning is not *needed* to explain the responses, not that
  it is absent. And one line of work reports that behavioural context *is* encoded prefrontally, on
  the evidence of similar responses to semantically similar calls. **Recorded as contested, with
  the weight on the acoustic side and the negative case weaker than the positive one.**
  **And "language" is not an available answer at this stage of this file.** Every result above is
  macaque. Whatever the human homologue of this edge carries, calling it language would be the
  same species-transfer move this pathway's pass has caught five times already. *(Class 1 —
  Romanski et al. 2005; Romanski 2006, rhesus, as reviewed in PMC2778283; PMC4381638, awake macaque;
  PMC8238193 for the hierarchy
  gradient; Gifford et al. 2005 for the contrary reading. Not yet verified for the source.)*

  **The human field scheme is macaque geometry projected onto a human brain, and that should be
  said plainly.** Human functional imaging identifies two clearly defined tonotopic regions joined
  at a shared low-frequency area, plus a third, less reliable one. The **belt fields are then
  delimited by extending the borders between adjacent core fields laterally to the superior
  temporal sulcus**, exactly as in the macaque studies — that is, the human belt's internal
  boundaries are **inherited from the monkey model rather than measured in human**. A separate
  caution runs the other way: a large expanse of human lateral superior temporal cortex may have
  **no clear monkey homologue** at all. **So the eight fields above are a macaque parcellation, and
  their application to human is an assumption this file should carry as one.** *(Class 1 — Kaas &
  Hackett 2000 for the model; PMC3001989 for the human delimitation method; Wallace et al. 2002 and
  Howard et al. 2000 for the human histochemistry. Not yet verified for the source.)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 present but **less
  granular than the core's**, which is the architectural signature of a field one step off the
  thalamic driver. *(Class 3.)*

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — between the eight fields: owed, and the frequency reversals are the clue.**
  Adjacent lateral fields meet at tonotopic reversals, which means neighbouring fields share a
  frequency border — the same relationship V1 and V2 have. Whether signal crosses those borders
  directly, in which direction, and carrying what, is not established. **The
  "where" stream in particular has no stated route from the caudolateral field to the medial belt
  fields that share its spatial tuning.**

  **Partly answered at the parabelt:** the **rostromedial** field of the medial
  belt projects to **both** divisions of the parabelt — caudal and rostral tracer injections there
  both label it. So the medial belt does have a declared output, and notably it **ignores the
  caudorostral topography** the lateral belt observes, reaching both streams rather than one. The
  edge is declared at the parabelt's end. What it carries is still **owed**.
- **Neurons:** ~25M per hemisphere (best available; rings the core). **The figure is for the belt as
  a whole and no per-field partition exists here** — which is now a visible gap rather than an
  implicit one, since the entry names eight fields.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** less than the core's; no figure recorded.

## Auditory parabelt — tertiary auditory cortex (lateral superior temporal gyrus, isocortex)

- **Function:** complex sound-objects and sequences, with invariance building — sound-object
  identity invariant to talker, pitch and level ("what"); location and motion ("where").
  Species-specific vocalizations preferentially drive the ventral route. Up the
  core → belt → parabelt hierarchy: tuning bandwidth, latency and stimulus specificity rise;
  temporal precision falls (verified gradient).
  It occupies the **posterior two thirds** of the superior temporal gyrus. **That fraction is
  worth stating, because the remaining third is auditory-responsive territory this whole scheme
  does not cover** — the rostral supratemporal plane and dorsal temporal pole respond to sound but
  have not been shown to receive significant input from the medial geniculate nucleus, so they are
  neither core, belt, nor parabelt. **Owed: what that territory is and what reaches it.**
  *(Class 1 — Poremba et al. 2003; Poremba et al. 2004; Kikuchi et al. 2010; Molinari et al.; macaque.)*
- **Inputs:**
  - **← anterolateral belt**, onto the **rostral** division — **carries:** call and identity
    features. **Fan-in:** unknown.
  - **← caudolateral belt**, onto the **caudal** division — **carries:** sound-source location, as
    an opponent hemifield rate code and not as a map (see the belt's entry). **Fan-in:** unknown.
    **The belt-to-parabelt connections are topographic in the caudorostral dimension** — caudal
    injections label caudal belt, rostral injections label rostral belt — which is what makes the
    two divisions two streams rather than two samples of one. *(Class 1 — Hackett, Stepniewska &
    Kaas 1998a, macaque.)*
  - **← rostromedial field of the medial belt**, onto **both** divisions — **carries:** payload
    **owed**; the medial belt is characterised chiefly by broad spatial tuning. **Recorded because
    it partly answers a question left open at the belt**: the medial belt has an output, it goes
    here, and it goes to both divisions rather than respecting the caudorostral topography the
    lateral belt observes. **A source that ignores the split is a different kind of input from one
    that honours it.** **Fan-in:** unknown. *(Class 1 — Hackett et al. 1998, macaque. Not yet
    verified for the source.)*
  - **← primary auditory cortex (the core)** — **carries:** payload **owed**, and the edge is
    **weak rather than absent**. A strict hierarchy — *not directly from the core* — does
    not hold as an absolute. The measurement is that injections confined to the parabelt
    labelled **few** neurons in the core, and large numbers in the belt. **Few is not none**, and
    the correction matters for anything that would treat the three tiers as strictly serial.
    **Fan-in:** unknown, and small. *(Class 1 — Hackett et al. 1998, macaque. Not yet verified for
    the source.)*
  - **← medial geniculate nucleus, dorsal division** — **carries:** the non-tonotopic thalamic
    signal. **Payload otherwise unknown — owed.** **This is the parabelt's own thalamic source**, so
    the tier is not fed through the belt alone. It also bears on the tonotopy question below: this
    thalamic division is not tonotopically
    organised, so it cannot be what imposes a frequency map here. **Fan-in:** unknown. *(Class 1 —
    Hackett, Stepniewska & Kaas 1998b, macaque.)*
  - **↔ the contralateral counterpart of this area** (callosal, reciprocal) — **carries:** a
    **normalisation, not a message** — sharpening and signal-to-noise enforcement, delivered from
    layers 3 and 5 onto layers 2/3 of the far side and avoiding layer 4. Mechanism, sign and
    evidence are stated once, in full, at the primary auditory cortex. **Association fields are
    more heavily callosally connected than primary fields, and carry proportionally more
    heterotopic traffic**, so this edge is denser here than there and less strictly area-to-area.
    **Fan-in / fan-out:** unknown. *(Class 1 — Gazzaniga 1987; Lee & Winer 2008; Hackett et al.
    1999 for the parabelt specifically. Not yet verified for the source.)*
- **Outputs:**
  - **→ anterior superior temporal gyrus and sulcus**, from the **rostral** division —
    **carries:** **sound-object identity, invariance-building** — increasingly invariant to talker,
    pitch and level. Up the core → belt → parabelt hierarchy, tuning bandwidth, latency and
    stimulus specificity **rise** and temporal precision **falls** — that gradient *is* the payload
    transformation, and it is verified. **Fan-out:** unknown.
  - **→ posterior superior temporal gyrus and the Sylvian parieto-temporal area**, from the
    **caudal** division — **carries:** location and motion of the sound. **Fan-out:** unknown.
  - **→ the rostrally-directed stream: temporal pole, ventral, rostral and medial prefrontal
    cortex, rostral cingulate, parahippocampal areas, and the amygdala** — **carries:** the
    identity payload, distributed. **The amygdala target is the one worth naming**: a cortical
    identity signal reaching the amygdala directly is a second route
    to affective evaluation alongside the fast subcortical one declared at the medial geniculate's
    medial division — and unlike that one, this route has already done the invariance work.
    **Fan-out:** unknown. *(Class 1 — PMC4001064, macaque.
    Not yet verified for the source.)*
  - **→ the caudally-directed stream: temporoparietal junction, posterior parietal and occipital
    regions including secondary visual cortex, caudal and dorsal prefrontal cortex, dorsal
    cingulate, and parahippocampal areas** — **carries:** the location payload, distributed.
    **The projection into secondary visual cortex is the structurally interesting one**: an auditory
    area writing into visual cortex is a cross-modal
    edge running the opposite way from the ones this file usually records. **Fan-out:** unknown.
    *(Class 1 — same source.)*
  - **→ upper bank of the superior temporal sulcus** (laterally) **and the insula and retroinsular
    areas** (medially) — **carries:** payload **owed**; two further output streams beyond the
    rostral and caudal pair. **Fan-out:** unknown. *(Class 1 — Galaburda & Pandya 1983; Hackett
    et al.; de la Mothe et al.; Smiley et al.)*

  **Arity warning on the three stream edges above.** Each is written as one edge with many named
  targets, because that is how the source describes them. **That is not the form this file's rule
  wants** — an edge has one producer and one consumer, and a line naming eight destinations is
  eight edges whose far ends mostly have no matching declaration. The amygdala and secondary visual
  cortex ends are declared, being the two that change something; **the rest are undeclared and are owed.**
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. Macaque throughout except where human is
  named. **Nothing here is yet verified for the source.**)*

  **Divisional sub-elements: two, "at least."** A **rostral** and a **caudal** division, on the
  dorsal surface of the superior temporal gyrus. The hedge is the literature's own — the tracer
  work supports *at least* two and does not exclude more. *(Class 1 — Hackett et al. 1998.)*

  **The parabelt is a third stage by its staining as well as by its connections.** Parvalbumin,
  acetylcholinesterase and cytochrome-oxidase staining fall off in **steps**: heaviest in the core,
  moderate in the belt, lightest here. That is a graded architectural signature of distance from
  the thalamic driver, and it agrees with the connectional hierarchy rather than merely
  accompanying it. **Cytoarchitecturally the parabelt is distinguished from the lateral belt by
  large pyramidal cells in layer IIIc and layer V** — the layers this file elsewhere identifies as
  the feedforward and the driver-output layers, which is consistent with a stage whose job is to
  project widely. *(Class 1 — Hackett 2003; Seltzer & Pandya 1978; Galaburda & Pandya 1983.)*

  **Internal edge — caudal division → rostral division, and it is a hierarchy inside the entry.**
  Response latencies form a gradient **from the caudal to the rostral** division, and the
  activation pattern in the rostral division begins in **layer 4** — the signature of feedforward
  input. Two readings are on offer: that the parabelt merely **inherits** the gradient already
  present in the belt, or that there is **an additional hierarchical step** from caudal to rostral
  within the parabelt itself. Both are consistent with the layer-4 finding. **carries:** payload
  **owed** under either reading. **Fan-in:** unknown. **Fan-out:** unknown.
  **If the second reading is right, this entry is two stages and not one**, and the "where" and
  "what" divisions are not siblings but sequential — which would contradict the parallel-streams
  picture the Function field assumes. Recorded as unsettled. *(Class 1 — J Neurosci 35:4140, 2015,
  awake macaque; Hackett 2011; Camalier et al. 2012; Hackett et al. 2014.)*

  **And the human evidence contradicts the macaque arrangement.** Electrocorticography in human
  finds the **shortest** latencies to clicks and vowels in the **middle** portion of the superior
  temporal gyrus — not at the caudal end, where the macaque gradient starts. The authors' own
  reading is that the specific anatomical arrangement of parabelt areas **differs between the
  species**. **So the internal edge above may run the wrong way, or from the wrong place, in a
  human brain.** Recorded as a species conflict, not smoothed. *(Class 1 — Nourski et al. 2014,
  human, as reported in J Neurosci 35:4140, 2015. Not yet verified for the
  source.)*

  **Tonotopy here is weaker and less orderly than in the core or belt, and that is a positive
  finding rather than a gap.** The belt-to-parabelt connections are not specific enough to say
  whether they favour tonotopically matched locations, and the thalamic input arrives from a
  division that is not tonotopically organised — so there is no obvious source for an orderly map.
  Mapping in awake macaque nevertheless found high-best-frequency sites clustered at the
  **posterior and anterior** ends of the gyrus with lower frequencies between them, which is read
  as marking the **border between the two divisions**. **So frequency is still ordered enough to
  locate a border, and not ordered enough to call a map.** *(Class 1 — J Neurosci 35:4140, 2015.)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, with layer 4 present but
  thinner and less granular than the belt's, and with the enlarged pyramidal population in **3c**
  and **5** noted above. *(Class 3 for the eight; Class 1 for the pyramidal cells and the staining
  gradient.)*

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.
- **Neurons:** ~56M per hemisphere (best available; lateral superior temporal gyrus, the largest
  territory of the three tiers; part of the Brodmann area 22 / von Economo area TA association group
  — see the
  anchor under the anterior superior temporal entry. Raised with the group scaled to the verified
  ~145M total.) **No per-division partition exists**, and the entry names two divisions plus a
  possible hierarchy between them.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** lightest of the three tiers by
  acetylcholinesterase and cytochrome-oxidase staining; no g-ratio recorded.

## Anterior superior temporal gyrus and sulcus — the auditory "what" endpoint (isocortex)

- **Function:** the top of the auditory ventral stream — phonemes (short timescale, mid-superior
  temporal gyrus) integrated into words (anterior superior temporal gyrus) and phrases (anterior
  superior temporal sulcus), with invariant phonetic-form representation. An **auditory word-form
  area** in the left anterior superior temporal gyrus holds word-selective representations that
  sharpen with familiarity (parallel to the visual word-form area), plus **voice identity** (the
  temporal voice areas).
  **The entry's "left-lateralised for segmental speech" is one side of a live dispute, and it was
  stated as settled.** It is also applied to **two payloads that lateralise in opposite
  directions**. Both problems are stated under Internal structure. The corrected short form:
  **speech content is left-biased on one influential model and bilateral on another; voice identity
  is right-biased on both.**
- **Inputs:**
  - **← auditory parabelt, rostral division**, by way of the **mid-superior temporal gyrus** —
    **carries:** talker-invariant sound-object identity. **The route runs through the mid-superior
    temporal gyrus, and that is two edges rather than one**: under this entry's own three-stage
    internal model the intermediate stage is a sub-element *of this entry*, so the edge from the
    parabelt terminates at the mid gyrus and the rest is internal. **Fan-in:** unknown.
  - **↔ the contralateral counterpart of this area** (callosal, reciprocal) — **carries:** a
    **normalisation, not a message** — sharpening and signal-to-noise enforcement, delivered from
    layers 3 and 5 onto layers 2/3 of the far side and avoiding layer 4. Mechanism, sign and
    evidence are stated once, in full, at the primary auditory cortex. **Association fields are
    more heavily callosally connected than primary fields, and carry proportionally more
    heterotopic traffic**, so this edge is denser here than there and less strictly area-to-area.
    **Fan-in / fan-out:** unknown. *(Class 1 — Gazzaniga 1987; Lee & Winer 2008; Hackett et al.
    1999 for the parabelt specifically. Not yet verified for the source.)*
- **Outputs:**
  - **→ the distributed semantic system** (lexical access) — **carries:** **invariant phonetic
    form** — phonemes at the short timescale composed into words and phrases, plus voice identity.
    **This is the auditory line's inferotemporal cortex**, and the payload hardens the same way:
    "the word that was said" and "who said it" are **phrases, not types** — no units, no frame.
    Recorded as such. **Fan-out:** unknown.
  - **→ temporal pole and middle temporal gyrus → ventrolateral prefrontal cortex** — **carries:**
    the same identity code, toward amodal concept and controlled retrieval. **Fan-out:** unknown.
  - **→ amygdala, and inferior prefrontal cortex, on the voice-identity payload** — **carries:**
    speaker identity and vocal affect. Recorded because the voice-sensitive network is reported to
    extend beyond the temporal lobe to bilateral inferior prefrontal cortex and the amygdalae, and
    because the amygdala's entry already declares an auditory identity input from the temporal
    "what" endpoint — this names which payload of this entry's two that edge carries. **Fan-out:**
    unknown. *(Class 1 — Pernet et al. 2015, human. Not yet verified for the source.)*
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. **Human throughout**, which is unusual for this
  file and is the reason the disputes below are about interpretation rather than about species
  transfer. Nothing here is yet verified for the source.)*

  **Sub-elements along the posterior-to-anterior axis: three stages, on a timescale hierarchy.**
  A coordinate-based meta-analysis of more than a hundred functional imaging experiments places
  **phoneme**-length processing in the **mid** superior temporal gyrus, lateral to Heschl's gyrus;
  **word**-length processing in the **anterior** superior temporal gyrus; and **phrase**-length
  processing beginning in the **anterior superior temporal sulcus**. The same analysis finds the
  mid-to-anterior gyrus reliably implicated in invariant phonetic-form representation and
  responding preferentially to phonetic sounds over artificial or environmental control sounds.
  **The organising variable is the length of the pattern being integrated**, which makes this a
  hierarchy of temporal receptive windows rather than of feature complexity. *(Class 1 — DeWitt &
  Rauschecker 2012, human.)*

  **Internal edges — mid gyrus → anterior gyrus → anterior sulcus.** **carries:** the phonetic
  payload, at successively longer integration windows — phonemes, then words, then phrases.
  **This is the entry's payload transformation and it happens inside the entry**, which is why the
  incoming edge from the parabelt had to be split off at the mid gyrus. **Fan-in:** unknown.
  **Fan-out:** unknown. **Direction is inferred from the anterior progression of peak effects
  across stimulus lengths, not traced** — recorded as Class 2 for the edges, Class 1 for the
  progression they are inferred from.

  **A second sub-element system in the same territory: three voice patches, and they are
  bilateral.** Cluster analysis of individual peaks in a large cohort gives **three** voice-sensitive
  patches in **each hemisphere** — posterior, mid, and anterior — along the superior temporal
  sulcus and gyrus. **The greatest peak density is in the right posterior sulcus.** So this entry's
  territory carries two overlapping sub-element systems: a speech hierarchy running
  posterior-to-anterior, and a voice-patch series running along the same axis, and **they are not
  the same three things.** *(Class 1 — Pernet et al. 2015, human.)*

  **The lateralisation problem, stated properly.** Two claims are easily carried in one phrase, and
  they are separate:
  - **For speech content, the literature is divided.** The meta-analytic
    three-stage model above is explicitly **left-biased** and its authors note that it diverges
    from the dual-stream model — both on lateralisation and on where word recognition sits. The
    dual-stream model holds that the **ventral stream is largely bilaterally organised**, with
    computational differences between the hemispheres rather than a division of labour, and that
    it is the **dorsal** stream that is strongly left-dominant. Lesion evidence is cited on both
    sides: severe phonological-level receptive deficit — word deafness — most commonly follows
    **bilateral** superior temporal damage, which the bilateral account predicts and the strong
    left account does not; against that, documented **unilateral** cases exist and were the basis
    of the classical left-dominance argument. A recent review states plainly that whether speech
    perception relies on lateralised mechanisms **remains a topic of debate**. **Recorded as
    contested. The entry's claim is not withdrawn — it is one of the two positions — but it is no
    longer stated as settled.** *(Class 1 — DeWitt & Rauschecker 2012; Hickok & Poeppel 2007;
    Cerebral Cortex 34:bhae087, 2024; human.)*
  - **For voice identity, the direction is the other one.** The voice work reports right
    lateralisation, consistent with the prosody findings, and the densest patch is right posterior.
    **So a single "left-lateralised" label on this entry is wrong regardless of how the speech
    dispute resolves**, because it is applied to a region carrying two payloads that lateralise
    oppositely. **This is the error that does not depend on taking a side, and it is the one worth
    fixing first.**
    **Note the consistency check this restores.** The primary auditory cortex entry describes the
    asymmetry as a **bias and a trade-off, not a dichotomy** — left for finer temporal resolution,
    right for finer spectral resolution. A hard "left-lateralised" three stages later is that bias
    hardened into a categorical claim with nothing in between to justify the hardening.

  **Voice selectivity is itself contested, and the dispute is about which tissue is selective.**
  One study, using equivalence testing against environmental-sound controls, concluded that the
  only temporal-lobe candidates for **true** voice selectivity were the anterior middle temporal
  gyrus, and explicitly ruled out the upper bank of the superior temporal sulcus and the more
  posterior middle temporal gyrus because those respond strongly to other environmental sounds.
  Separately, **damage to the posterior sulcus does not impair voice recognition**, which argues
  that its voice representations are not necessary for the identification and sit downstream of
  the feature detectors, possibly serving face-voice integration instead. **So of the three voice
  patches, the most active one may not be the one doing the recognising.** *(Class 1 — Front Hum
  Neurosci 8:499, 2014; S002839321730088X; human.)*

  **Inter-individual variability is high and it is not noise.** The voice patches are highly
  reproducible **within** an individual on test-retest, and highly variable **between**
  individuals in precise anatomical location. **For a file that sizes regions and routes edges
  between them, that combination is the awkward one**: the structure is real and stable in a given
  brain, and its coordinates are not shared across brains — so a per-region unit count is
  meaningful and a per-coordinate one is not.

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, homotypical association cortex,
  layer 4 present and thin. *(Class 3.)*

  **Tangential sub-elements: unknown**, beyond the voice patches above, whose status as a repeating
  compartmentation rather than as three separate areas is not established.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — between the speech hierarchy and the voice patches: owed, and this is the
  interesting gap.** The two sub-element systems occupy the same tissue along the same axis and
  carry payloads that must at some point be separated — *what was said* and *who said it* leave on
  different edges to different targets. Nothing read says whether they are separated by different cells
  in the same place, by different places, or not separated at all until later.
- **Neurons:** ~48M per hemisphere (best available; a subregion of the Brodmann area 22 / von Economo area TA anchor
  below).
- **Brodmann area 22 / von Economo area TA anchor (verified human stereology — reconciled).** The superior temporal gyrus homotypical
  association cortex Brodmann area 22 / von Economo area TA carries ~91M ± 15M *pyramidal* neurons
  in layers III/V/VI,
  plus ~54M in the granular layers II/IV ≈ **~145M total neurons per hemisphere**
  (Wu & Amaral; cf. temporal pole Brodmann area 38 ~103M, entorhinal
  ~13M in the same lineage). Brodmann area 22 / von Economo area TA is the *lateral association*
  superior temporal gyrus (von Economo area TA;
  cytoarchitectonic areas Te3–Te4) — it spans **parabelt + anterior superior temporal gyrus +
  posterior superior temporal gyrus**, so it anchors that
  group's *sum*, not the anterior superior temporal gyrus alone. The doc's soft split sums to the
  ~145M *total* (parabelt ~56 + anterior ~48 + posterior ~40 ≈ 145M, in 7:6:5 proportions).
  The ~91M *pyramidal* figure and the ~145M *total* differ by the ~54M granular-layer
  (II/IV) neurons the doc's per-region slots also include, so the total is the right anchor.
  The division among the three stays soft. **Primary auditory cortex (core, Brodmann area 41 / area
  Te1) and belt (Brodmann area 42 / area Te2) are
  koniocortex, outside Brodmann area 22 / von Economo area TA — not firmed by this anchor.**
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Posterior superior temporal gyrus and the Sylvian parieto-temporal area — the auditory dorsal
stream's origin (isocortex)

- **Function:** auditory space and motion, and the sensorimotor interface for sound. The
  **Sylvian parieto-temporal area** (abbreviated **Spt** in the literature; at the posterior planum
  temporale, around the anterior end of the temporo-parietal junction) is the auditory-motor hinge —
  it mediates between the sensory representation of the superior temporal sulcus and the motor
  representations of frontal cortex. Carries sound localisation, speech production and repetition,
  and phonological working memory. Strongly left-dominant.
  **Three qualifications**, all stated under Internal structure: the **"where" and "audiomotor"
  labels come from two competing models of this stream and are not two functions of one**; the hinge
  area is **not speech-specific**; and it is
  defined **functionally rather than anatomically**, so its borders move with the task used to find
  it.
- **Inputs:**
  - **← auditory parabelt, caudal division**, onto the **posterior superior temporal gyrus** —
    **carries:** sound location and motion — as an opponent hemifield rate code and not as a map,
    per the belt's entry — and the sensory (auditory) form of speech. **The chain caudal parabelt →
    posterior gyrus → posterior sulcus → the hinge area is not one edge.** Three of those four are
    sub-elements of this entry, so the incoming edge terminates at the posterior gyrus and the rest
    is internal.
    **Fan-in:** unknown.
  - **← visual and somatosensory cortex** — **carries:** payload **owed**. Recorded because the
    hinge area responds to **silent lip-reading** and to **reading written words**, neither of which
    can arrive on an auditory edge. **The region demonstrably has more than one input.** **Fan-in:**
    unknown. *(Class 1 for the responses — Pa & Hickok 2008; Hickok et al. 2009;
    Class 2 for the attribution to those sources. Not yet verified for the source.)*
  - **↔ the contralateral counterpart of this area** (callosal, reciprocal) — **carries:** a
    **normalisation, not a message** — sharpening and signal-to-noise enforcement, delivered from
    layers 3 and 5 onto layers 2/3 of the far side and avoiding layer 4. Mechanism, sign and
    evidence are stated once, in full, at the primary auditory cortex. **Association fields are
    more heavily callosally connected than primary fields, and carry proportionally more
    heterotopic traffic**, so this edge is denser here than there and less strictly area-to-area.
    **Fan-in / fan-out:** unknown. *(Class 1 — Gazzaniga 1987; Lee & Winer 2008; Hackett et al.
    1999 for the parabelt specifically. Not yet verified for the source.)*
- **Outputs:**
  - **→ inferior parietal lobule (supramarginal gyrus) → premotor and inferior frontal cortex
    (area 44, Broca's area)** — **carries:** the **auditory-to-motor mapping**: a sound target
    expressed in terms the motor system can act on — the coordinate transform *is* the payload
    change at this hinge, from a sensory code to an articulatory or spatial-motor one. Also
    phonological working memory. Strongly left-dominant. **Fan-out:** unknown.
    **Whether "transform" is the right word is itself an open question** — see the interface
    problem below.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. **Human throughout.** Nothing here is yet
  verified for the source.)*

  **Sub-elements: three, in series along the posterior axis** — the **posterior superior temporal
  gyrus**, the **posterior superior temporal sulcus**, and the **Sylvian parieto-temporal area** at
  the far end. The internal edges run in that order, and they are the chain that a single incoming
  edge would otherwise collapse. **carries:** the auditory payload, progressively re-expressed for
  motor use. **Fan-in** and **fan-out** unknown. **Direction is taken from the model, not traced.**
  *(Class 2 for the internal edges; Class 1 for the areas.)*

  **The hinge area is defined functionally, not anatomically, and this file should treat that as a
  property rather than a detail.** It is specified as the region at the posterior end of the
  lateral sulcus, near the anterior temporo-parietal junction, **that responds to both auditory
  perception and silent vocal-tract gestures**. That is a definition by response profile. **A
  region so defined has no border independent of the task used to elicit it**, which means an edge
  declared as terminating "on the Sylvian parieto-temporal area" is anchored to a functional
  criterion and not to a piece of tissue — unlike, say, the medial superior olive. Recorded because
  the file's other entries mostly name structures that would still be there if nobody ran an
  experiment. *(Class 1 — Hickok et al. 2009; Hickok 2012.)*

  **Tangential sub-elements: a patchy sensory/motor mosaic, and it is measured.** Multivariate
  analysis of functional imaging shows **distinct spatial activation patterns during the sensory
  and the motor phases** of the same task, described as a **patchy organisation** of
  sensory-weighted versus motor-weighted voxels and attributed to different neuronal
  subpopulations. **So the hinge is not a homogeneous converter — it is two interdigitated
  populations occupying one territory**, which is the same arrangement this file records for the
  medial superior temporal area's congruent and opposite cells and for the superior colliculus's
  burst and buildup neurons. **The recurring difficulty is the same one:** an edge that should
  terminate on the motor-weighted patches and not the sensory-weighted ones has no way to say so.
  *(Class 1 — Hickok, Okada & Serences 2009; Dahl et al. 2009; human.)*

  **It is not speech-specific, and the evidence is direct.** Sensorimotor responses here are
  **equally robust when the sensory stimulus is a tonal melody and the motor task is covert
  humming** as when they are speech. The area also activates during **silent lip-reading** and
  during **reading written words**, and during covert rehearsal in phonological short-term memory
  tasks. In skilled musicians it activates for covert humming and, less strongly, for covert
  playing. **So the function is auditory-to-vocal-tract guidance in general, and speech is one use
  of it, not its definition.** *(Class 1 — Hickok et al. 2003; Pa & Hickok 2008; human.)*

  **Interface or integrator: an open question about what the payload actually is.** The literature
  explicitly distinguishes **an area that acts as an interface between two tasks — a shared level
  of processing both draw on — from an area that integrates one level of processing into another**.
  The entry asserts the second: that the coordinate transform *is* the payload change here. **The
  first reading would mean there is no transform at this stage at all** — only a common
  representation that the sensory and motor systems each read and write, with the conversion
  happening elsewhere or nowhere. **The patchy sensory/motor mosaic above is compatible with
  either**, and is arguably more suggestive of the shared-representation reading, since a converter
  would not obviously need two segregated populations. **Recorded as unsettled. This is the one
  place in the auditory line where the file's central question — what does this stage do to the
  payload — has a named alternative answer of "nothing."** *(Class 1 for the distinction being
  drawn — Front Hum Neurosci 8:24, 2014; Buchsbaum et al. 2011. Not yet verified for the source.)*

  **The two models the "where" and "audiomotor" labels fuse.** One account makes the auditory dorsal
  stream a
  **spatial** ("where") pathway, by analogy with vision. The other makes it a **sensorimotor
  integration** pathway mapping phonological representations onto articulatory motor
  representations, with no spatial role assigned. Taking both labels together without noting that
  they are **competing accounts of the same stream**, not two functions of it, is the error to
  avoid. **This file does not need to choose**, since the edges carry the traffic
  either way, but it should not present a disputed identity as an inventory. Recorded as contested.
  *(Class 1 — Rauschecker & Tian 2000 lineage for the spatial account; Hickok & Poeppel 2007, for
  the sensorimotor account.)*

  **Lesion evidence, and it supports the sensorimotor account specifically.** Damage to the left
  dorsal superior temporal gyrus or the temporo-parietal junction is associated with **conduction
  aphasia** — good comprehension with frequent phonemic errors in production. That is the profile
  predicted by breaking a sensory-to-motor interface while leaving comprehension intact. It has
  classically been read instead as a **disconnection** syndrome from damage to the arcuate
  fasciculus, so the lesion evidence does not by itself locate the deficit in this grey matter
  rather than in the fibre bundle passing it. *(Class 1 — as reviewed in Hickok & Poeppel 2007.)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, homotypical association cortex.
  *(Class 3.)*

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.
- **Neurons:** ~40M per hemisphere (best available; part of the Brodmann area 22 / von Economo area TA ~145M
  group). **No partition across the three sub-elements exists**, and the hinge area's functional
  definition means one may not be constructible in the usual way.
- **Synapses:** unknown. **Axons:** the arcuate fasciculus carries this stream forward; fibre count
  unknown. **Grey-matter volume:** unknown. **White-matter volume:** unknown.
  **Myelination:** unknown.

## Right-hemisphere prosodic homologues — prosody and affect (isocortex)

- **Function:** the right counterparts of the two temporal endpoints above, weighted toward
  **prosody and affect** rather than segmental content: the right anterior superior temporal gyrus
  and sulcus (affective-voice and prosodic-contour identity) and the right posterior superior
  temporal gyrus (prosodic-spatial).
  **The entry's two strongest claims are both weaker than they were stated.** It said prosody is a
  right-hemisphere function, and that this is the first place the two hemispheres genuinely diverge
  in computation. **Neither survives intact**: the lateralisation of prosody is one of the more
  contested claims in this file, with three competing accounts and aggregate evidence that is
  bilateral with a right lean at best; and under one of those accounts the divergence here is **not
  new** but is the primary auditory cortex's spectral/temporal bias showing its consequences three
  stages later. Both are stated in full under Internal structure. **The edges below are the same
  under every account**
  — the traffic runs the same way — but the entry does not assert a clean segmental-left /
  prosodic-right split.
- **Inputs:**
  - **← right auditory parabelt**, onto the right superior temporal gyrus and sulcus — **carries:**
    the same acoustic feature stream as the left, but read with a **finer spectral and coarser
    temporal** bias — the primary auditory cortex asymmetry, compounded up the hierarchy. **The
    receiving areas are this entry's own sub-elements**, so this edge terminates at them rather than
    running through to the parabelt as one line. **Fan-in:**
    unknown.
  - **↔ the contralateral counterpart of this area** (callosal, reciprocal) — **carries:** a
    **normalisation, not a message** — sharpening and signal-to-noise enforcement, delivered from
    layers 3 and 5 onto layers 2/3 of the far side and avoiding layer 4. Mechanism, sign and
    evidence are stated once, in full, at the primary auditory cortex. **Association fields are
    more heavily callosally connected than primary fields, and carry proportionally more
    heterotopic traffic**, so this edge is denser here than there and less strictly area-to-area.
    **Fan-in / fan-out:** unknown. *(Class 1 — Gazzaniga 1987; Lee & Winer 2008; Hackett et al.
    1999 for the parabelt specifically. Not yet verified for the source.)*
- **Outputs:**
  - **→ semantic and limbic targets** (and, for production, the right inferior frontal gyrus) —
    **carries:** **prosodic and affective identity** — the contour of pitch, loudness, timing and
    stress, and the emotional category it signals; **not** segmental content. **This is the first
    edge in the file whose payload is claimed to differ between the hemispheres** — the left
    endpoint carries words, the right carries how they were said. **Whether the difference is as
    categorical as that sentence makes it is what the Internal structure section disputes.**
    **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only. **Human throughout**, and unusually for this
  file the evidence base is largely **meta-analytic** — several syntheses of dozens of studies,
  which is why the negative findings below carry weight. Nothing here is yet verified for the
  source.)*

  **Sub-elements: two, named in the Function field** — the right anterior superior temporal gyrus
  and sulcus, and the right posterior superior temporal gyrus. **They are the right-side
  counterparts of two entries above, and this file gives them one entry between them** — which is a
  packaging decision, not a finding, and it makes the two right areas harder to check against their
  left partners than they would be as separate entries. **Splitting them is owed**, on the same
  grounds as the pretectum's two unrelated structures.

  **Three competing accounts of why prosody lateralises at all, and the file should name them
  rather than pick one silently.**
  - **The biological, or right-hemisphere, account:** prosody — especially affective prosody — is
    predominantly right-lateralised as a matter of hemispheric specialisation. This is what the
    entry asserted.
  - **The functional, or task-dependent, account** (Van Lancker's functional lateralisation
    hypothesis): lateralisation follows the **communicative function**. Prosody with an *emotional*
    function goes right; prosody with a *linguistic* function goes left, to the
    language-dominant hemisphere. It adds a second dimension: the right hemisphere is held to
    operate on **larger units** — phrases and sentences — and the left on **smaller** ones such as
    syllables. **So under this account the right side is not "the prosody side" but the
    affective-and-long-window side**, and lexical stress, which is prosody by any definition,
    should be and is reported to be left.
  - **The acoustic, or cue-dependent, account:** lateralisation follows the **acoustic cue** — left
    for timing and temporal structure, right for pitch and spectral structure.
  *(Class 1 — Van Lancker 1980; Van Lancker Sidtis et al.; Zatorre and Poeppel lineages; as
  reviewed in the aprosodia literature and PMC3989730.)*

  **The cue-dependent account is the one with a consequence for this file, and it is a deflationary
  one.** That account's claim — left for temporal, right for spectral — is **word for word the
  asymmetry this file already declares at the primary auditory cortex**, where it is correctly
  described as a **bias and a trade-off, not a dichotomy**. If prosodic lateralisation is that same
  bias working on longer stimuli, then **this entry is not a new divergence between the hemispheres
  but a downstream consequence of one already recorded three stages earlier** — and the entry's
  claim to be "the first place the two hemispheres genuinely diverge in computation" is
  double-counting. **The same hardening stands twice in this pathway**: a bias declared as a bias at
  the core, stated as a categorical claim at the anterior temporal entry and again here. Recorded as
  the pattern it is.

  **The aggregate evidence is bilateral with a right lean at best, and several syntheses find no
  reliable lateralisation at all.**
  - A meta-analysis of 21 studies of the effects of left- and right-hemisphere damage found **not
    strong evidence** for lateralisation of linguistic prosodic production, linguistic prosodic
    comprehension, **or emotional prosodic production**.
  - A meta-analysis of 38 lesion studies — 450 patients with left-hemisphere damage, 534 with
    right, 491 controls — found that **both** left and right damage compromise **both** emotional
    and linguistic prosodic perception.
  - A systematic review comparing right-hemisphere-damaged patients with controls found right
    damage had **no reliable effect** on word- and phrase-level linguistic prosody or on the
    production of speech-act prosody; it did affect **discrimination and identification** of
    speech-act and emotional prosody.
  - An effect-size meta-analysis of the functional imaging literature describes activity for
    emotional versus neutral prosody as **highly bilateral, with subtle right lateralisation at
    best**.
  **The pattern across these is that comprehension and identification of affective prosody lean
  right, and production and linguistic prosody do not lean reliably at all** — which is narrower
  than this entry's claim in both directions. *(Class 1 — Witteman et al. 2011; Witteman et al.
  2014; Sheppard et al.; as compiled in MedLink 2025 and bioRxiv 2024.10.29.620829 / Neurosci
  Biobehav Rev 2025. Not yet verified for the source.)*

  **Part of the reported lateralisation is an artefact of experimental design, which is worth
  carrying because it tells you how much to trust the rest.** Emotional-valence effects are
  **strongly right-lateralised in studies using blocked presentation** of emotional stimuli and
  **bilateral or left-accented in event-related studies**. Separately, **explicit** attention to
  prosody gives left-lateralised posterior superior temporal activity while **implicit** perception
  gives no lateralisation. **So the same tissue lateralises differently depending on how it is
  asked**, and any single figure quoted for this entry is a figure about a paradigm as much as
  about a brain. *(Class 1 — as reviewed in Prog Brain Res 156 and Frühholz & Grandjean 2013.)*

  **What survives, and it is not nothing.** Right-hemisphere stroke patients do show impairments in
  affective prosody; distinct right-hemisphere regions are argued to be necessary for affective
  prosody comprehension and production; and the voice-identity work recorded at the anterior
  temporal entry independently finds the densest voice patch in the **right** posterior sulcus.
  **The right lean for affective and voice-identity material is real; what fails is the clean
  reciprocal split** — that the left does segmental content and the right does prosody, as two
  complementary halves.

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, homotypical association cortex,
  as at the left-side counterparts. *(Class 3.)* **No cytoarchitectural difference between the two
  hemispheres' versions of these areas is established**, which is itself worth recording: the
  claimed functional divergence has no declared structural correlate here.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — between the hemispheres, and they bear on this entry's own dispute.** The
  callosal edge is declared at all six auditory cortical entries and stated in full at the primary
  auditory cortex. Two of its properties matter here:
  - **The edge carries a normalisation, not a percept.** Its measured effects are sharpened tuning
    and enforced signal-to-noise, with excitatory fibres producing net inhibition through local
    interneurons. **So it is not the place where *what was said* and *how it was said* are
    combined** — that recombination is still **owed**, and the callosum is not the answer to it.
  - **The edge is what holds the asymmetry in place.** In rhesus, callosotomy raises the right
    dorsotemporal pole's activity and **abolishes** the left-right difference for species-specific
    calls. **If that transfers, the lateralisation this entry disputes is a dynamic equilibrium
    maintained by interhemispheric inhibition rather than a fixed division of labour** — which
    would explain both why the effect is real and why it measures as weak, bilateral and
    paradigm-dependent: an equilibrium can be pushed. Recorded as a candidate reading of the
    dispute, not its resolution.
- **Neurons:** ~50M per hemisphere for the two right homologues combined (best available).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

**The auditory pathway is described and verified complete through the temporal
lobe:** cochlea → cochlear nucleus → superior olivary complex (the binaural / sound-localisation
branch) → inferior colliculus → medial geniculate →
primary auditory cortex → belt → parabelt → anterior superior temporal gyrus and sulcus (ventral
"what") and posterior superior temporal gyrus and the Sylvian parieto-temporal area
(dorsal "where") + the perceptual prosodic homologues. The frontal termini are described too:
the **right inferior frontal gyrus** for affective-prosody *production* and Broca / area 44 for
segmental speech (both Frontal lobe), joined to the temporal cortex by the arcuate fasciculus
(White-matter tracts). The pathway is closed end to end, perception and production.

**Five payload claims in this section are withdrawn or downgraded, and they are listed here because
each is carried in more than one entry and a reader arriving at any single entry would not see the
pattern.** The "verified complete" above refers to the pathway's closure, not to the content of the
slots; **the per-edge payloads, the internal-structure slots and the full names are not verified.**
1. **The place code for interaural time** at the superior olivary complex — Jeffress's model,
   verified in birds, disputed in mammals. Now contested, with three readings live.
2. **The auditory space map** at the inferior colliculus — barn-owl anatomy, with one mammalian
   report in a different subdivision. Withdrawn from the colliculus, the geniculate, the primary
   auditory cortex, and the superior colliculus edge — then **partly restored** at the superior
   colliculus, where a mammalian auditory space map is in fact attested and is built rather than
   relayed.
3. **The cortical space map** at the belt — withdrawn outright. There is no cortical map of
   auditory space; the code is an opponent hemifield population rate code read out by slope.
4. **"Modulatory" on the corticothalamic edge** at the medial geniculate — that edge is two edges,
   from layers 6 and 5, and the layer-5 limb is a driver carrying cortical content.
5. **Clean hemispheric splits** at the anterior temporal and prosodic entries — a bias correctly
   described at the primary auditory cortex was hardened into a categorical claim twice downstream.
**The common shape:** a code or map established in one species asserted for another, or a bias
asserted as a dichotomy. **The remaining sensory sections are not checked on this axis.**

---

---

## References

*(Section under source design §2a: the citing line carries the key, and the authors, title,
journal, volume, pages and method sit here. Species stays inline, where the entries argue from it.
Every line below is a **candidate** awaiting Micky's verification; none is verified for the source.
**12 lines carry a reference obtained by a web search against the publisher's or journal's
record.** The rest read **owed**: what follows the key on those lines is **transcribed from this
file's own citing lines**, not from any record. A transcribed line is not a searched one and does
not become one by sitting in this section. **No line here carries a line number.** A pointer into
the file goes stale on the next edit and fails silently, so the section is joined to the entries by
the key alone.)*

**196 distinct keys, 267 mentions. 12 searched; 184 owed.**

**Nineteen keys name a source that cannot be looked up from what the file holds.** Two shapes. **A
bare lineage or surname with no year** — *Osen & Mugnaini lineage*, *Manis lineage*, *Spangler,
Warr & Henkel lineage*, *Coomes et al.*, *Oliver et al.*, *Davis*, *Peruzzi et al.*, *Winer et
al.*, *Molinari et al.*, *Smiley et al.*, *Hackett et al.*, *de la Mothe et al.*, *Wu & Amaral*,
*Van Lancker Sidtis et al.*, *Zatorre and Poeppel lineages*, *Sheppard et al.*, *Salminen lineage*,
*Krumbholz lineage*, *Palmer lineage*, *Nakamoto lineage*, *Wu & Yan lineage*, *Sherman & Guillery
lineage*, and the source named only as *ScienceDirect topic overviews*. **A journal standing where
an author belongs** — *Prog Brain Res 156*. A lineage is a pointer at a body of work, not at a
paper, so it cannot take a reference line; **the repair is naming the paper the citing claim rests
on, and that repair belongs at the line making the claim.**

**Two collisions, and both are settled here rather than left in the keys.** *Hackett, Stepniewska
& Kaas 1998* named **two** papers in the same journal and year, told apart inline only by the
volume — and §2a moves the volume down here. They now carry the ordinary **a** and **b**
disambiguators, ordered by volume: **1998a** is J Comp Neurol 394:475, **1998b** is 400:271. A
third key, bare *Hackett et al. 1998*, is a third citing form with no volume given, and **which of
the two it means is owed at the citing line** — it is kept separate rather than guessed at.
Separately, *Hickok et al. 2009* and *Hickok, Okada & Serences 2009* may be one paper written two
ways; the file gives the volume only at the second, so they are kept separate too.

**Nine keys were written two ways inline and are now written one way in both places** — four losing
a diacritic on the way down (*Gillespie & Müller*, *Carricondo & Romero-Gómez*, *Rovó et al.*,
*Frühholz & Grandjean*), and five where a bare journal or lineage name stood at one citing line and
the identified paper at another (*Pecka et al. 2008* for J Neurosci 28:6914; *eNeuro
7:ENEURO.0256-20, 2020*; *Joris 2013* for the Joris lineage; *PMC4381638* for the Ortiz-Rios /
Rauschecker lineage; *PMC4001064* for the Hackett lineage). A key written two ways defeats the
string match this section is built on, in both directions and silently.

- **Adams 1986** — **owed**: not searched.
- **Aitkin et al. 1988** — **owed**: not searched.
- **Arcelli et al. 1997** — **owed**: not searched.
- **Ashmore 2008** — Physiological Reviews 88:173, 2008; review. **owed**: not searched.
- **Averbeck & Romanski 2004** — **owed**: not searched.
- **Baizer et al. 2014** — Baizer, Wong, Paolone, Witelson, Sherwood & Hof, Anat Rec 297:1865, 2014; immunohistochemistry for nonphosphorylated neurofilament protein, nitric oxide synthase and three calcium-binding proteins; Witelson Normal Brain Collection. **owed**: not searched.
- **Baizer et al., Anat Rec 2018** — **owed**: not searched.
- **Barclay, Ryan & Housley 2011** — Neural Development 6:33, 2011. **owed**: not searched.
- **Benson et al. 1991** — **owed**: not searched.
- **Binns et al. 1992** — PubMed 1393591, 1992; guinea pig. **owed**: not searched.
- **bioRxiv 2024.10.29.620829** — The ALE meta-analysis; also written *Neurosci Biobehav Rev 2025* at the same citing line. **owed**: not searched.
- **Braak & Bachmann 1985** — **owed**: not searched.
- **Brand et al. 2002** — Brand, A., Behrend, O., Marquardt, T., McAlpine, D. & Grothe, B. (2002). Precise inhibition is essential for microsecond interaural time difference coding. *Nature* 417(6888): 543–547. **Mongolian gerbil.** *In vivo* recording from the medial superior olive with iontophoretic application of glycine and strychnine. *(Nature publisher record.)* *(searched; candidate.)*
- **Buchsbaum et al. 2011** — **owed**: not searched.
- **Burton & Jones 1976** — **owed**: not searched.
- **Camalier et al. 2012** — **owed**: not searched.
- **Carr & Soares 2002** — **owed**: not searched.
- **Carrasco et al. 2013** — **owed**: not searched.
- **Carricondo & Romero-Gómez 2019** — Carricondo, F. & Romero-Gómez, B. (2019). The cochlear spiral ganglion neurons: the auditory portion of the VIII nerve. *The Anatomical Record* 302(3): 463–471. **Review** (spiral ganglion across mammals, with human material discussed). *(Wiley publisher record.)* Note for the citing lines: this review gives type II neurons as **5%** of the ganglion, where line 90 writes ~5–10%. *(searched; candidate.)*
- **Cerebral Cortex 34:bhae087, 2024** — **owed**: not searched.
- **Code & Winer 1985** — **owed**: not searched.
- **Code & Winer 1986** — **owed**: not searched.
- **Coomes et al.** — **owed**: not searched.
- **Da Costa et al. 2011** — **owed**: not searched.
- **Dahl et al. 2009** — **owed**: not searched.
- **Dallos et al. 2008** — Dallos, P., Wu, X., Cheatham, M.A., Gao, J., Zheng, J., Anderson, C.T., Jia, S., Wang, X., Cheng, W.H.Y., Sengupta, S. et al. (2008). Prestin-based outer hair cell motility is necessary for mammalian cochlear amplification. *Neuron* 58(3): 333–339. **Mouse.** *(Reference located in publisher reference listings, not the Neuron record itself.)* **Class 2 — a resolution note, not a correction to the claim.** The citing line at 108 attaches the **40–60 dB** figure to this key and calls it a prestin *knockout*. The search returned that figure in the abstract of a different paper — Liberman, M.C. et al. (2002), Prestin is required for electromotility of the outer hair cell and for the cochlear amplifier, *Nature* 419: 300–304, which is the targeted-deletion study. Which paper line 108 rests on is **owed at the citing line**; both are candidates and neither is verified. *(searched; candidate.)*
- **Davis** — **owed**: not searched.
- **de la Mothe et al.** — **No year at the citing line**; cited for the parabelt's further output streams. The dated key *de la Mothe et al. 2012* is used elsewhere in the file. **owed**: not searched.
- **de la Mothe et al. 2012** — **owed**: not searched.
- **DeWitt & Rauschecker 2012** — PNAS 109:E505, 2012; a meta-analysis of more than a hundred experiments; human. **owed**: not searched.
- **Diamond et al. 1968** — **owed**: not searched.
- **Dorph-Petersen et al. 2008** — **owed**: not searched.
- **eLife 9:e56963, 2020** — **owed**: not searched.
- **eNeuro 7:ENEURO.0256-20, 2020** — Awake-mouse optogenetics. Written as *eNeuro 2020* at one citing line and in full at the other; now one way in both. **owed**: not searched.
- **Fekete et al. 1984** — Fekete, Rouiller, Liberman & Ryugo, 1984; intracellular horseradish peroxidase after characteristic-frequency measurement; cat. Written in full author form at one citing line and as the *et al.* key at the other; now one way in both. **owed**: not searched.
- **Fettiplace 2017** — Fettiplace, R. (2017). Hair cell transduction, tuning, and synaptic transmission in the mammalian cochlea. *Comprehensive Physiology* 7(4): 1197–1227. **Mammalian; review.** *(Wiley/publisher record and PubMed listing.)* *(searched; candidate.)*
- **Fitzpatrick & Imig 1980** — **owed**: not searched.
- **Fitzpatrick et al. 1984** — **owed**: not searched.
- **Flores et al. 2015** — **owed**: not searched.
- **Front Hum Neurosci 8:24, 2014** — **owed**: not searched.
- **Front Hum Neurosci 8:499, 2014** — **owed**: not searched.
- **Front Neuroanat 18:1331230, 2024** — Immunohistochemistry; human and chimpanzee. **owed**: not searched.
- **Frontiers Neural Circuits 15:721015, 2021** — **owed**: not searched.
- **Frontiers Neural Circuits 15:721186, 2021** — **owed**: not searched.
- **Frühholz & Grandjean 2013** — **owed**: not searched.
- **Galaburda & Pandya 1983** — **owed**: not searched.
- **Games & Winer 1988** — **owed**: not searched.
- **Gazzaniga 1987** — **owed**: not searched.
- **Gifford et al. 2005** — **owed**: not searched.
- **Gillespie & Müller 2009** — Cited for cochlear tonotopy. **owed**: not searched.
- **Guillery et al. 1998** — **owed**: not searched.
- **Hackett 2003** — **owed**: not searched.
- **Hackett 2011** — **owed**: not searched.
- **Hackett & Phillips 2011** — **owed**: not searched.
- **Hackett et al.** — **No year at the citing line**; cited for the parabelt's further output streams. Which of the dated Hackett keys it means is owed at the citing line. **owed**: not searched.
- **Hackett et al. 1998** — **owed**: not searched.
- **Hackett et al. 1999** — **owed**: not searched.
- **Hackett et al. 2014** — **owed**: not searched.
- **Hackett, Stepniewska & Kaas 1998a** — J Comp Neurol 394:475, 1998; tracer injections; macaque. **The a/b disambiguator is this pass's**: the file cites two papers by these authors in this journal and year, told apart inline only by the volume, and §2a moves the volume down here. Ordered by volume. **owed**: not searched.
- **Hackett, Stepniewska & Kaas 1998b** — J Comp Neurol 400:271, 1998; macaque. See the note at 1998a. **owed**: not searched.
- **Heiman-Patterson & Strominger 1985** — **owed**: not searched.
- **Hickok 2012** — **owed**: not searched.
- **Hickok & Poeppel 2007** — Nat Rev Neurosci 8:393, 2007. **owed**: not searched.
- **Hickok et al. 2003** — Hickok, Buchsbaum, Humphries & Muftuler, J Cogn Neurosci 15:673, 2003; human. **owed**: not searched.
- **Hickok et al. 2009** — **owed**: not searched.
- **Hickok, Okada & Serences 2009** — J Neurophysiol 101:2725, 2009; human. **owed**: not searched.
- **Hilbig et al. 2009** — Hilbig, H., Beil, B., Hilbig, H., Call, J. & Bidmon, H.-J. (2009). Superior olivary complex organization and cytoarchitecture may be correlated with function and catarrhine primate phylogeny. *Brain Structure and Function* 213(4–5): 489–497. **Catarrhine primates including human.** *(PubMed Central record.)* *(searched; candidate.)*
- **Howard et al. 2000** — **owed**: not searched.
- **Hubel & Wiesel 1967** — **owed**: not searched.
- **Hunt et al. 1991** — **owed**: not searched.
- **Imig & Brugge 1978** — J Comp Neurol 182:637, 1978; cat. **owed**: not searched.
- **J Neurosci 27:8405, 2007** — **owed**: not searched.
- **J Neurosci 35:4140, 2015** — Awake-macaque survey. **owed**: not searched.
- **Jeffress 1948** — Jeffress, L.A. (1948). A place theory of sound localization. *Journal of Comparative and Physiological Psychology* 41(1): 35–39. **Theoretical; no species.** *(Located only in publisher reference listings — a secondary listing.)* *(searched; candidate.)*
- **Jones & Powell 1968** — **owed**: not searched.
- **Joris 2013** — J Neurosci 33:17506, 2013; chinchilla. Cited as *Joris lineage* at the citing line; the volume and year identify the paper and the key now names it. **owed**: not searched.
- **Kaas & Hackett 2000** — PNAS 97:11793, 2000. **owed**: not searched.
- **Kaas et al. 1999** — **owed**: not searched.
- **Kelly & Wong 1981** — **owed**: not searched.
- **Kikuchi et al. 2010** — **owed**: not searched.
- **Kitzes & Doherty 1994** — **owed**: not searched.
- **Knudsen & Knudsen 1983** — **owed**: not searched.
- **Kosaki et al. 1997** — **owed**: not searched.
- **Koutcherov et al. 2004** — **owed**: not searched.
- **Krumbholz lineage** — Human magnetoencephalography and functional imaging. **owed**: not searched.
- **Kulesza 2007** — Kulesza, R.J. Jr. (2007). Cytoarchitecture of the human superior olivary complex: medial and lateral superior olive. *Hearing Research* 225(1–2): 80–90. **Human.** Cytoarchitecture with unbiased stereology. *(Elsevier listing; the abstract was seen, the full record was not opened.)* *(searched; candidate.)*
- **Kulesza 2008** — Hear Res 241:52, 2008; human. **owed**: not searched.
- **Kulesza & Grothe 2015** — Front Neuroanat 9:35, 2015. **owed**: not searched.
- **Lee & Winer 2008** — **owed**: not searched.
- **Lee & Winer 2008a** — **owed**: not searched.
- **Liu & Suga 1997** — **owed**: not searched.
- **Liu et al. 2015** — **owed**: not searched.
- **Malmierca et al. 1995** — **owed**: not searched.
- **Manis lineage** — **owed**: not searched.
- **McAlpine, Jiang & Palmer 2001** — McAlpine, D., Jiang, D. & Palmer, A.R. (2001). A neural code for low-frequency sound localization in mammals. *Nature Neuroscience* 4(4): 396–401. **Species not established by this search.** *(Located only in publisher reference listings, not the Nature Neuroscience record itself — a secondary listing.)* *(searched; candidate.)*
- **MedLink 2025** — The aprosodia review. **owed**: not searched.
- **Middlebrooks 2021** — J Neurosci 41:5772, 2021; a review of negative results. **owed**: not searched.
- **Mitani & Shimokouchi 1985** — **owed**: not searched.
- **Moerel et al. 2014** — **owed**: not searched.
- **Molinari et al.** — **owed**: not searched.
- **Molnar & Pfeiffer 1968** — **owed**: not searched.
- **Moore & Moore 1971** — **owed**: not searched.
- **Moore & Osen 1979** — **owed**: not searched.
- **Morel & Kaas 1992** — **owed**: not searched.
- **Morel et al. 1993** — **owed**: not searched.
- **Morest 1964** — **owed**: not searched.
- **Morosan et al. 2001** — NeuroImage 13:684, 2001; human. **owed**: not searched.
- **Nakamoto lineage** — **No year or identifier at the citing line**; cited for cortical feedback to the inferior colliculus, as reported in PMC3422721. **owed**: not searched.
- **Neurosci Biobehav Rev 2025** — **owed**: not searched.
- **Nourski et al. 2014** — Human electrocorticography. **owed**: not searched.
- **Oertel & Young 2004** — **owed**: not searched.
- **Oliver & Morest 1984** — **owed**: not searched.
- **Oliver et al.** — **owed**: not searched.
- **Osen & Mugnaini lineage** — **owed**: not searched.
- **Pa & Hickok 2008** — **owed**: not searched.
- **Palmer lineage** — **No year or identifier at the citing line**; cited for cortical feedback to the inferior colliculus, as reported in PMC3422721. **owed**: not searched.
- **Pecka et al. 2008** — Pecka, M., Brand, A., Behrend, O. & Grothe, B. (2008). Interaural time difference processing in the mammalian medial superior olive: the role of glycinergic inhibition. *Journal of Neuroscience* 28(27): 6914–6925. **Gerbil.** *(Located only in publisher reference listings — a secondary listing.)* *(searched; candidate.)*
- **Pernet et al. 2015** — Pernet, McAleer, Latinus, Belin et al., NeuroImage 119:164, 2015; human functional magnetic resonance imaging, large cohort. **owed**: not searched.
- **Peruzzi et al.** — **owed**: not searched.
- **PMC2778283** — **owed**: not searched.
- **PMC3001989** — **owed**: not searched.
- **PMC3394089** — **owed**: not searched.
- **PMC3422721** — **owed**: not searched.
- **PMC3913906** — **owed**: not searched.
- **PMC3978371** — Immunochemistry with retrograde tracer; guinea pig. **owed**: not searched.
- **PMC3989730** — **owed**: not searched.
- **PMC4001064** — Hackett lineage, Front Neurosci, 2014; macaque. Also cited in file 1. **owed**: not searched.
- **PMC4220032** — **owed**: not searched.
- **PMC4220731** — Immunochemistry with retrograde tracer; guinea pig. **owed**: not searched.
- **PMC4381638** — The Ortiz-Rios / Rauschecker lineage, functional imaging; awake macaque. Cited as the lineage name at the citing line; the accession identifies the paper and the key now names it. **owed**: not searched.
- **PMC4585487** — Functional magnetic resonance imaging with pattern classification and objective gradient-reversal detection; human and macaque. **owed**: not searched.
- **PMC4995217** — In vivo whole-cell recording with electron microscopy; gerbil. **owed**: not searched.
- **PMC6573148** — Granule-cell stimulation from the cuneate and spinal trigeminal nuclei; rodent. **owed**: not searched.
- **PMC8238193** — **owed**: not searched.
- **PMC8592287** — Mouse transgenic line. **owed**: not searched.
- **PMC8608271** — Intracranial recording; human. **owed**: not searched.
- **PMC9504316** — 2022; human structural magnetic-resonance imaging, whole nucleus segmented, 11 subjects. **owed**: not searched.
- **PMC12378517** — Farid, Y., Lukyanenko, B., Witelson, S.F. & Baizer, J.S. (2025). Individual variability in the nuclei of the human superior olivary complex. *Brain Structure and Function*, published 25 August 2025; doi 10.1007/s00429-025-03005-4. **Human**, 12 brains, Witelson Normal Brain Collection. Nissl and immunostained sections. *(PubMed Central record.)* *(searched; candidate.)*
- **Poeppel 2003** — "Asymmetric sampling in time," 2003. **owed**: not searched.
- **Poremba et al. 2003** — **owed**: not searched.
- **Poremba et al. 2004** — **owed**: not searched.
- **Prog Brain Res 156** — **owed**: not searched.
- **Rauschecker & Tian 2000** — **owed**: not searched.
- **Ravizza et al. 1976** — **owed**: not searched.
- **Richter et al. 1983** — Am J Anat 168, 1983. **owed**: not searched.
- **Rock & Apicella 2015** — **owed**: not searched.
- **Rockel & Jones 1973** — **owed**: not searched.
- **Romanski 2006** — Rhesus single units. **owed**: not searched.
- **Romanski & Goldman-Rakic 2002** — **owed**: not searched.
- **Romanski et al. 1999** — Romanski, Tian, Fritz, Mishkin, Goldman-Rakic & Rauschecker, Nat Neurosci 2:1131, 1999; microelectrode mapping with tract tracing; rhesus. **owed**: not searched.
- **Romanski et al. 2005** — Rhesus single units. **owed**: not searched.
- **Rouiller & Welker 2000** — **owed**: not searched.
- **Rouiller et al. 1986** — **owed**: not searched.
- **Rouiller et al. 1991** — **owed**: not searched.
- **Rovó et al. 2012** — **owed**: not searched.
- **Rubio & Juiz 2004** — **owed**: not searched.
- **Russ et al. 2008** — **owed**: not searched.
- **Ryugo & Fekete 1982** — **owed**: not searched.
- **Ryugo & Parks 2003** — Brain Res Bull 60:435, 2003; cat. **owed**: not searched.
- **S002839321730088X** — A Neuropsychologia lesion study; human. The accession stands where an author belongs. **owed**: not searched.
- **Salminen lineage** — Human magnetoencephalography and functional imaging. **owed**: not searched.
- **Schleicher et al. 1999** — **owed**: not searched.
- **ScienceDirect topic overviews** — **No author, year or identifier at the citing line**, so the source cannot be looked up from this file. Cited as Class 3 general anatomy for the nuclei of the lateral lemniscus. **owed**: not searched.
- **Seltzer & Pandya 1978** — **owed**: not searched.
- **Senatorov & Hu 2002** — **owed**: not searched.
- **Sheppard et al.** — **owed**: not searched.
- **Sherman 2017** — Comprehensive Physiology, 2017. **owed**: not searched.
- **Sherman & Guillery 1996** — **owed**: not searched.
- **Sherman & Guillery 1998** — **owed**: not searched.
- **Sherman & Guillery lineage** — **No year at the citing line**; cited for the driver/modulator distinction at the layer-5 corticothalamic edge, where the dated keys *Sherman & Guillery 1996* and *1998* are also used. **owed**: not searched.
- **Smiley et al.** — **owed**: not searched.
- **Spangler, Warr & Henkel lineage** — **owed**: not searched.
- **Stecker, Harrington & Middlebrooks 2005** — PLoS Biol 3:e78, 2005; cat. **owed**: not searched.
- **Sun et al. 2018** — Cell 174:1247, 2018. **owed**: not searched.
- **Tian et al. 2001** — Tian, Reser, Durham, Kustov & Rauschecker, Science 292:290, 2001; macaque. **owed**: not searched.
- **Van Lancker 1980** — **owed**: not searched.
- **Van Lancker Sidtis et al.** — **owed**: not searched.
- **Wagner et al. 1987** — **owed**: not searched.
- **Wagoner & Kulesza 2009** — **owed**: not searched.
- **Wallace & Harper 1997** — **owed**: not searched.
- **Wallace et al. 2002** — **owed**: not searched.
- **Werner-Reiss & Groh 2008** — J Neurosci 28:3747, 2008; macaque. **owed**: not searched.
- **Winer & Larue 1996** — Winer, J.A. & Larue, D.T. (1996). Evolution of GABAergic circuitry in the mammalian medial geniculate body. *Proceedings of the National Academy of Sciences USA* 93(7): 3083–3087. **Bat, rat, cat and monkey** — comparative. Immunocytochemistry with cell counting; the paper also states that the lateral geniculate body, the inferior colliculus and auditory cortex do *not* show the same species range, which is the contrast line 751 draws. *(PNAS publisher record.)* *(searched; candidate.)*
- **Winer et al.** — **owed**: not searched.
- **Winer et al. 1999** — **owed**: not searched.
- **Winer et al. 2002** — **owed**: not searched.
- **Witteman et al. 2011** — **owed**: not searched.
- **Witteman et al. 2014** — **owed**: not searched.
- **Wong et al. 2019** — **owed**: not searched.
- **Woods et al. 2006** — **owed**: not searched.
- **Wouterlood et al. 1984** — **owed**: not searched.
- **Wu & Amaral** — UC Davis; optical fractionator. No year at the citing line. **owed**: not searched.
- **Wu & Yan lineage** — **No year or identifier at the citing line**; cited for cortical feedback to the inferior colliculus, as reported in PMC3422721. **owed**: not searched.
- **Zatorre & Belin 2001** — **owed**: not searched.
- **Zatorre and Poeppel lineages** — **owed**: not searched.
- **Zheng et al. 2000** — Zheng, J., Shen, W., He, D.Z.Z., Long, K.B., Madison, L.D. & Dallos, P. (2000). Prestin is the motor protein of cochlear outer hair cells. *Nature* 405(6783): 149–155. **Gerbil** (prestin cloned from gerbil outer hair cells), expressed heterologously in cultured human kidney cells. Complementary-DNA cloning; voltage-induced shape change and nonlinear capacitance in transfected cells. *(Nature publisher record.)* *(searched; candidate.)*
