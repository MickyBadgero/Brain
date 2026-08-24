# Brain architecture — 02 auditory pathway

**Date:** 2026-08-19
**Derived from:** `human_brain_02_auditory_pathway` — the auditory line from the cochlea
through the brainstem and thalamus to the temporal-lobe endpoints. **One source file, and no other
content source.**

**Cross-file checks contained in this file.** Each line names another file that was held open beside
this one and whose shared edges with it are diffed and stemmed below.

- `01_visual_pathway`, `11_frontal_lobe`.
- `07_anterior_temporal_lobe`.
- `14_brainstem_midbrain_hypothalamus`, `15_cranial_nerve_nuclei`. **Nine shared edges diffed and
  stemmed. The acoustic reflex is declared at both ends of this file and at neither end of the motor
  stage between them, and this file's endpoint for it names a circuit rather than the structure that
  has an entry.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file has been read against this one; an endpoint with no stem is one whose far end has
not yet been opened beside this file, and it is not a claim that none exists.

**Counting basis is declared per structure and is not uniform.** **Per ear** at the cochlea, **per
side** through the brainstem and thalamus, **per hemisphere** in cortex — and above the parabelt the
per-hemisphere convention breaks down, because the two hemispheres stop being counterparts and the
source gives the right-side endpoints an entry of their own. See the section totals.

**This section is where timing is the payload rather than a property of it.** Three structures compute
on arrival-time differences at the tens-of-microseconds scale, and the physical facts that make that
possible — a fan-in of one, a giant terminal, heavy myelination — are structural claims, not
performance notes.

---

## Structural invariants

**Whole-pathway co-instantiation.** This section contains the map's most complete descending loop, and
it closes on the transducer itself: the superior olivary complex sends medial olivocochlear efferents
onto the cochlea's **outer hair cells**, so the brain sets the gain of its own front end before
transduction. Above that, every ascending stage has a matching descending one — cortex to the medial
geniculate nucleus and inferior colliculus, colliculus to the olive and cochlear nucleus, olive to the
cochlear nucleus and the cochlea. **A staged bring-up from the ear upward would leave every one of
those loops open**, and the gain loop in particular is not a refinement: without it the front end has
no set point.

**Per-edge latency, and here the invariant is load-bearing rather than formal.**

- The **interaural time difference** computation in the medial superior olive works at **tens of
  microseconds**. The source records the substrate: the trapezoid body and lateral lemniscus are
  heavily myelinated **because speed matters at that scale**.
- **Phase locking** at low frequencies means the timing of the waveform is *part of the payload* on the
  auditory nerve, not merely the schedule on which it arrives.
- The **endbulb of Held** buys timing fidelity by morphology — the terminal is large enough to generate
  an extracellular prepotential before the receiving cell's own spike, and the delay between the two
  has exceptionally low jitter.
- The **octopus cell** detects coincidence across the tonotopic array at the highest temporal precision
  in the brain.

**No numerical edge latency is stated anywhere in this section, so every edge below reads *to derive*.**
That is not a formality here: a stage whose function is to resolve tens of microseconds cannot be built
from a description that does not give its delays, and this section is the strongest case in the map for
why **uniform delay is a substitution and not an approximation** — set every edge equal and the medial
superior olive computes nothing.

**Two non-neural edges, and one of them is mechanical.** The cochlea's input is **sound-pressure
vibration** by way of the middle ear — an acoustic arrival, not a neural edge, fan-in not applicable.
And the **cochlear amplifier** is a *mechanical* feedback loop inside the sensory organ: the outer hair
cells add force back into the basilar-membrane travelling wave through prestin, a voltage-driven
membrane protein that changes cell length directly. Its fan-in and fan-out read **not applicable — the
transfer is mechanical**. With light at the retina and the endocrine limbs elsewhere in the map, this
is the third class of edge that takes real time and is not conduction plus synaptic transmission.

---

## Cochlea

- **Function → structure.** Turns sound-pressure vibration into a neural signal and performs a
  **mechanical frequency analysis before any neural processing happens**. A coiled tube ~35 mm long,
  partitioned into three fluid compartments, the middle one held at a standing positive voltage — the
  **endocochlear potential**, supplied by the structure and not by the stimulus, which is the battery the
  transduction current runs on and the reason the organ responds to vibrations of atomic dimension.
  **Position along the tube maps to frequency**, base to apex, high to low, so what leaves is already
  tonotopically sorted and **every downstream structure inherits that map rather than computing it.**
  Two sensory cell types with different jobs: one row of **inner hair cells** (~3,500) are the
  transducers and carry essentially all sound information; three rows of **outer hair cells**
  (~12,000) are the **amplifier**, motile, adding mechanical energy back into the travelling wave.
  **A sensor with a servo built into it.**
- **Inputs.**
  - **← sound-pressure vibration, via the middle ear** — mechanical, not a neural edge. Fan-in: not
    applicable.
  - **← superior olivary complex**, medial olivocochlear efferents, onto the **outer hair cells** — a
    gain command, no stimulus content. Fan-in: to derive.
  - **← branchiomotor / visceromotor nuclei** (`15_cranial_nerve_nuclei`), indirectly via the
    stapedius muscle — the acoustic reflex's attenuation. The effector is a middle-ear muscle, outside
    scope, so this is an influence on the input above rather than an edge onto neural structure.
    **The named producer has an entry and it declares the muscle, not this loop.**
    That entry's facial nucleus drives **stapedius** and its output line to orofacial striated muscle
    carries it — **so the efferent half of this reflex is written at both ends.** **The afferent half
    is written at neither**: that entry declares no auditory input of any kind, and the drive onto it
    is declared only at this file's superior olivary complex, where the endpoint names an arc rather
    than a nucleus. **See that entry's output line below.**
- **Outputs.**
  - **→ cochlear nucleus**, via the auditory nerve, from the **inner hair cells** through the **type I
    spiral ganglion neurons** (~30,000 fibres) — energy in one narrow frequency band as a function of
    time, tonotopically ordered, with waveform timing preserved by phase locking at low frequencies.
    **Fan-out: 5–30** type I neurons per inner hair cell; **fan-in exactly one** — each type I neuron
    contacts one inner hair cell. **A pure divergence with no convergence at all.**
  - **→ cochlear nucleus**, from the **outer hair cells** through the **type II spiral ganglion
    neurons** (~5–10% of the ganglion, unmyelinated) — **not sound.** These fibres are not required
    for hearing; the current reading is a **damage signal from the organ of Corti**. Fan-out: each
    type II neuron branches onto roughly a dozen outer hair cells; **fan-in ~12**, the opposite arity
    to the line above.
- **Sizing.** Basis: **per ear.**
  - **Type I spiral ganglion, ~31,500: zero.** Fan-in is exactly one, and log₂(1) = 0 — **a neuron
    with a single input stores no threshold, because there is no count to compare against.** This is
    the first structure in the map where a *known* fan-in drives the cost to zero rather than an
    unknown one leaving it open.
  - **Type II spiral ganglion, ~2,500** at fan-in ~12 → 4 bits → **~1.2 kB.**
  - **Hair cells, ~15,500 inner and outer: to derive, and not zero.** They are **not neurons** — they
    are sensory epithelial cells — and they **produce graded receptor potentials with no action
    potentials at all.** Neither the transducer exception nor the threshold-gate model reaches them.
  - **Structure total: ~1.2 kB firm, plus the hair-cell store to derive.**
- **Shape.** **Sheet, and it is one-dimensional**, which is the structural difference between this
  section and the visual one. Rank 2: **(cell class, position along the tube)** — position *is*
  frequency, base to apex, high to low. Extents are measured: **~3,500 inner hair cells** and
  **~12,000 outer** in one row and three rows over a **~35 mm** tube, **~30,000–35,000** spiral
  ganglion neurons. **The tonotopic axis is the only map axis**; there is no second dimension to
  index, where a retinotopic sheet has two.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the mechanical amplifier loop and the olivocochlear gain
  loop both close here and neither can be staged — an unamplified cochlea is 40–60 dB less sensitive,
  which is not a degraded version of the same structure. Per-edge latency: satisfied; the input edge
  and the amplifier loop are non-neural.
- **Justification (biological).** The frequency decomposition is done by the mechanics of the basilar
  membrane's graded stiffness and mass, so the tonotopic map is a property of the organ and not a
  computation any neural stage performs. Abolishing prestin costs 40–60 dB — roughly a hundredfold —
  and the loop's output is observable from outside the head as otoacoustic emissions.

## Cochlear nucleus

- **Function → structure.** First central processing, split into **parallel labelled lines** — each
  cell class a different message on a different wire. **And the lines are not parallel processing of
  different inputs; they are different readings of the same input.** Every auditory nerve fibre
  bifurcates on entry and reaches **all three divisions**, so what differs between the lines is the
  **terminal type and the receiving cell's intrinsic properties**, not the source. Three divisional
  sub-structures — **anteroventral**, **posteroventral**, **dorsal** — each holding a complete
  tonotopic map, so **three maps of frequency per side, not one.** Cell classes: spherical and globular
  bushy cells (timing), T-stellate (spectrum), octopus (broadband onset by coincidence), fusiform
  (monaural spectral-notch elevation cues), plus inhibitory D-stellate and the dorsal interneurons.
- **Inputs.**
  - **← cochlea**, auditory nerve, ~30,000 fibres, tonotopic — **one edge terminating in three
    places.** Fan-in: **one or two** onto the spherical bushy cell, by axosomatic endbulb of Held, and
    little else; unknown for the other classes.
  - **← dorsal column nuclei and trigeminal relay** → the dorsal division, by way of the granule cells
    — somatosensory state of head, face, neck and pinna, for cancelling self-generated sound. Fan-in:
    to derive.
  - **← semicircular canals, otolith organs and vestibular nuclei** → the dorsal division, same
    granule-cell route — head rotation rate and gravito-inertial acceleration. Fan-in: to derive.
  - **← primary auditory cortex and inferior colliculus** (descending) — gain and expectation, no new
    stimulus content. Fan-in: to derive.
  - **← superior olivary complex**, glycinergic — inhibition, no content. Fan-in: to derive.
- **Outputs.**
  - **→ superior olivary complex**, from **bushy cells** — the spectral vector with sub-millisecond
    arrival timing preserved, monaural, one per ear. **Not itself a localisation signal**: it is what
    the differences are computed *from*. Three destinations differing in side and sign, not content —
    spherical bushy cells to the medial superior olive bilaterally and the lateral superior olive
    ipsilaterally, globular bushy cells to the medial nucleus of the trapezoid body contralaterally.
    Fan-out: to derive.
  - **→ inferior colliculus**, from **T-stellate cells** — the spectrum, rate-coded per band, timing
    not preserved. Fan-out: to derive.
  - **→ inferior colliculus**, from **octopus cells** — broadband onset, a coincidence event marking a
    transient. Fan-out: to derive.
  - **→ inferior colliculus**, from **fusiform cells** — monaural spectral-notch cues for elevation,
    with the self-motion signal already subtracted. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~0.5M neurons, soft — no clean human count, and the source
  notes this is a gap in what has been *counted* rather than in what has been sectioned. Fan-in to
  derive for most classes, bounded ≤ 16 bits → **≤ 1.00 MB.**
  **The spherical bushy cell is the exception and it costs 1 bit**: a fan-in of one or two gives
  log₂(2) = 1. **The structure's most timing-critical cell is its cheapest.**
- **Shape.** **Rank 3: (division, cell class, position along the tonotopic axis)** — three divisions,
  **each holding a complete tonotopic map, so three maps of frequency per side rather than one.**
  The cell-class axis is the labelled-line structure: spherical and globular bushy, T- and D-stellate,
  octopus, fusiform, plus the dorsal interneurons. Extents: ~0.5M neurons total, **partition across
  divisions and classes to derive.** **And the division axis may not be indexable in a human** — the
  ventral cell classes lie intermixed within the cochlear nerve branches, so the boundary that defines
  the sub-elements may not be drawable.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; the descending edges from cortex, colliculus
  and olive all close loops through structures present in this section. Per-edge latency: satisfied,
  all to derive — and the octopus cell's coincidence detection makes the *spread* across its afferents
  the computation, which is the invariant's own justification instantiated.
- **Justification (biological).** The timing fidelity the whole binaural pathway rests on is bought
  here, by synapse morphology rather than by circuitry: the endbulb of Held's fan-in of one or two is
  what makes the bushy cell's timing secure, and a stage that averaged many afferents could not do it.
  **A structural caution the source insists on:** the two-domain fusiform cell and the cerebellum-like
  granule / parallel-fibre / cartwheel circuit that carries the self-motion cancellation are **cat and
  rodent anatomy that human material has not confirmed and in part contradicts** — the granule domain
  is decreased or absent in primates, human dorsal division shows two layers rather than three with no
  inhibitory interneurons labelled, and fusiform cells are reported as clustered or absent. The
  somatosensory and vestibular inputs are independently attested, so something receives them; what, in
  a human, is **to derive**. A second divergence: in human the ventral cell classes lie intermixed
  within the cochlear nerve branches, so **the divisional boundary that defines the sub-structures may
  not be drawable in a human brain** — which makes "onto the anteroventral division" a checkable
  endpoint in a cat and possibly not in us.

## Superior olivary complex

- **Function → structure.** **The first site of binaural convergence** and the origin of horizontal
  sound localisation. Nuclear sub-structures: **medial superior olive**, **lateral superior olive**,
  **medial** and **lateral nuclei of the trapezoid body**, and a ring of **periolivary nuclei**.
  The medial superior olive extracts **interaural time differences** by coincidence detection on a
  **bipolar cell whose two dendrites point in opposite directions** — ipsilateral excitation on one,
  contralateral on the other, so one cell's two inputs are segregated by compartment and the
  **geometry is the computation.** The lateral superior olive extracts **interaural level differences**
  as a subtraction: ipsilateral excitation against contralateral inhibition, sign-inverted through the
  medial nucleus of the trapezoid body, whose cells are driven by the giant **calyx of Held**. Also the
  source of the medial olivocochlear efferents and the drive for the stapedius reflex.
- **Inputs.**
  - **← cochlear nucleus, spherical bushy cells, bilaterally** → **medial superior olive** — the
    phase-locked spectral vector from **both** ears. **This edge's payload is a pair and the pairing is
    the point**: neither copy carries azimuth, and the difference is not taken until it arrives.
    Fan-in: to derive.
  - **← cochlear nucleus, globular bushy cells, contralateral** → **medial nucleus of the trapezoid
    body** — the same vector, which that nucleus then sign-inverts. **Fan-in: one** — the calyx of Held
    is a one-to-one giant terminal.
  - **← cochlear nucleus, spherical bushy cells, ipsilateral** → **lateral superior olive** — the same
    monaural vector as excitation, uninverted; the positive term of the subtraction. Fan-in: to derive.
  - **← primary auditory cortex and inferior colliculus** (descending). Fan-in: to derive.
- **Outputs.**
  - **→ inferior colliculus**, lateral lemniscus, bilaterally — **horizontal sound location
    (azimuth).** **This is the edge where timing stops being the payload and azimuth starts being it.**
    Elevation is not on it. **What form azimuth takes on this wire is contested, and the architecture
    must not assume a place code** — see Justification. Fan-out: to derive.
  - **→ cochlea**, medial olivocochlear efferents onto the outer hair cells — a gain command. Fan-out:
    to derive.
  - **→ cochlear nucleus**, glycinergic, descending — inhibition. Fan-out: to derive.
  - **→ the acoustic-reflex arc** (stapedius) — a loudness-triggered attenuation command; the effector
    is outside scope. Fan-out: to derive.
    **This endpoint names a circuit and not a structure, and the structure it should name has an
    entry.** The arc runs through the **facial motor nucleus**, a named sub-element of
    `15_cranial_nerve_nuclei`'s branchiomotor and visceromotor entry — **the one structure in that
    section with a firm human count, ~10,000 per side, corroborated against the myelinated-axon count
    of its own nerve.** That entry declares the efferent limb to stapedius and **declares no auditory
    input at all**, so this edge has a producer here and no consumer there.
    **The failure is in the endpoint's kind rather than in its spelling.** *The acoustic-reflex arc* is
    a route; a route cannot declare an input back, so no diff at either end can pair this edge, and it
    reads as terminating outside scope when in fact its next stage is a counted nucleus two files away.
    **An endpoint naming a loop hides a structure the same way a class endpoint hides a member**, and
    it is worse in one respect: a class is visibly unresolved, while an arc reads as a complete
    description.
    **Owed at the source: retype this endpoint to the facial motor nucleus**, keeping stapedius as the
    terminus beyond it — or establish that the drive reaches the muscle by a route that does not pass
    through that pool. **Not retyped here**, because changing an endpoint at this rung re-terminates an
    edge the source still carries as written. **The far file has been given the finding from this
    side.**
- **Sizing.** Basis: **per side.** **Medial superior olive ~15,500 and lateral superior olive ~5,600**
  — firm human unbiased stereology, among the few in the auditory brainstem. Fan-in to derive, bounded
  ≤ 16 bits → **~0.031 MB and ~0.011 MB.**
  - **The medial nucleus of the trapezoid body carries no count**, because its existence in human is
    disputed (below), and its principal cell's **fan-in is one, which costs zero bits** — so even a
    firm count would add nothing to the parameter store.
  - Periolivary groups: uncounted. **Structure total: ~0.042 MB stated, and the two structures doing
    the localisation arithmetic are together smaller than a rounding error against any cortical area
    in this section.**
- **Shape.** **Rank 2 per nucleus: (nucleus, position along the tonotopic axis)**, and the medial
  superior olive's own geometry is explicit — its somata lie in **a thin sagittal sheet** with the two
  dendrites extending in opposite directions, so the structure is a sheet one cell thick with the
  binaural comparison across its thickness. Extents measured: **~15,500** medial superior olive and
  **~5,600** lateral superior olive per side. Trapezoid body and periolivary groups: **to derive**,
  and for the medial nucleus of the trapezoid body the count is disputed rather than merely absent.
- **Edge latency.** All edges **to derive** — and this is the structure where that is most costly.
- **Invariant conformance.** Co-instantiation: the olivocochlear loop back to the cochlea and the
  glycinergic loop back to the cochlear nucleus both close here. Per-edge latency: satisfied, all to
  derive, and **the computation is a latency difference** — the two bilateral input edges are the same
  payload distinguished only by arrival time, so an architecture that gave them equal latency would
  delete the function rather than approximate it.
- **Justification (biological).** The tuning of the coincidence detector is **manufactured by timed
  glycinergic inhibition, not by a difference in axonal path length** — blocking the inhibition shifts
  a cell's best interaural time difference toward zero. That inverts the classical delay-line account
  and it means the inhibitory internal edges are functional, not modulatory.
  **Two things the source records that constrain what may be built here.** First, the **output format
  is decoded and disputed** — three readings are live: a place code in a map of interaural delay
  (verified in birds, and mammals evolved the computation independently), a hemispheric opponent
  population rate code read out by the slope of the response-azimuth function, and a chinchilla result
  finding best delays clustered near zero and inside the physiological range. **That state is neither
  *to derive* nor settled**: it has been measured and the readings disagree. Second, this is the
  **least species-transferable structure in the pathway**, and the disagreement is about which nuclei
  exist: the medial superior olive is present in every human study examined; the lateral superior
  olive is called prominent by one group and not consistently identifiable by another; and the medial
  nucleus of the trapezoid body is reported as well established by one line of work and as
  vestigial or absent by four others. **Every inhibitory internal edge in this structure originates
  there**, so if the human nucleus is absent, the sign-inverting term of the level computation and the
  timed inhibition that sets time-difference tuning arrive from somewhere else or work differently in
  us. The edges are kept because the *function* is attested in human psychophysics; the substrate is
  recorded as disputed.

## Inferior colliculus

- **Function → structure.** The **obligatory hub** — every ascending auditory line passes through it.
  Three divisional sub-structures: the **central nucleus** (lemniscal, tonotopic), and the **dorsal**
  and **external cortices** (non-lemniscal, multimodal, and where the descending cortical projection
  lands). The central nucleus is built of **10–12 fibrodendritic laminae**, each a sheet of neurons
  whose dendrites lie in the plane of the sheet and each an **isofrequency** plane — so the tonotopic
  axis runs *across* the laminae. Cell classes by dendrite: **disc-shaped**, confined to one lamina,
  and **stellate**, crossing two or more. **Morphology does not predict sign** — both classes can be
  glutamatergic or glycinergic/GABAergic, which is unlike the rest of this section.
- **Inputs.**
  - **← cochlear nucleus** (T-stellate, octopus and fusiform cells, lateral lemniscus) → central
    nucleus — spectrum, broadband onset, and monaural elevation cues. Fan-in: to derive.
  - **← superior olivary complex**, bilateral → central nucleus — azimuth. **A consumer of this edge
    must not assume a map.** Fan-in: to derive.
  - **← nuclei of the lateral lemniscus**, bilaterally → central nucleus. **These have no entry
    anywhere in the source, so this edge terminates at a structure the description does not describe**
    — inherited, and not repaired at this rung. Fan-in: to derive.
  - **← primary auditory cortex** (heavy descending), terminating **mainly in the dorsal and external
    cortices, not the central nucleus** — gain and expectation. Fan-in: to derive.
  - **← contralateral inferior colliculus** (commissural). Fan-in: to derive.
- **Outputs.**
  - **→ medial geniculate nucleus, ventral division** (brachium), from the central nucleus — the
    assembled auditory scene: tonotopic spectrum, periodicity and duration tuning, and the binaural
    cues bound with the monaural elevation cue. **A named majority source class**: cholecystokinin
    disc-shaped neurons, ~63% of the excitatory population, projecting exclusively to that division.
    Fan-out: to derive.
  - **→ medial geniculate nucleus, dorsal and medial divisions**, from the dorsal and external
    cortices — the non-lemniscal, broadly tuned signal. Fan-out: to derive.
  - **→ contralateral inferior colliculus** (commissural). Fan-out: to derive.
  - **→ superior colliculus** — auditory azimuth and elevation in a frame the orienting map can
    register against the visual one. Fan-out: to derive.
  - **→ superior olivary complex and cochlear nucleus** (descending). Fan-out: to derive.
- **Sizing.** Basis: **per side.** **Central nucleus ~420,000 neurons in ~22.4 mm³** — verified human
  primary measurement, one of the firmest figures in the section. Whole colliculus with the dorsal and
  external cortices ~0.6M. Fan-in to derive, bounded ≤ 16 bits → **≤ 1.20 MB.**
  **Density cross-check, recomputed: ~420,000 / 22.4 mm³ ≈ 18,750 neurons/mm³** — consistent with the
  loose packing of subcortical relays and far below cortical density.
- **Shape.** **Laminated nucleus**, rank 3: **(division, lamina, position within lamina)** — three
  divisions, and the central nucleus built of **10–12 fibrodendritic laminae each an isofrequency
  plane**, so **the tonotopic axis runs across the laminae** and each lamina is one frequency band.
  **This structure's partition is derivable and closes**: ~420,000 central-nucleus neurons over 10–12
  laminae is **~35,000 to ~42,000 per lamina**, in ~22.4 mm³ at **~18,750 neurons/mm³**. **The lamina
  axis is the frequency axis** — which is what makes the shape and the map the same thing here.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: obligatory by construction — no ascending auditory line
  reaches the thalamus without it, so it cannot be a later addition. Per-edge latency: satisfied, all
  to derive.
- **Justification (biological).** **Obligatory is right; summed is not established**, and the
  distinction matters for what is built. Terminals from the different ascending pathways are
  interleaved in different sublaminae and remain functionally segregated at this level, so the lines
  all arrive and arrive in a shared tonotopic frame — whether they are **combined** here or merely
  brought into **register** is not settled by the anatomy. **The parallel structure the cochlear
  nucleus creates may survive this stage.** Separately, the **auditory space map** attributed to this
  structure is barn-owl anatomy, in the owl's *external* nucleus, with a single mammalian report in
  guinea pig and none in human — recorded as contested and mis-sited rather than carried. Across
  frequency bands the only stated route is the **translaminar stellate cell**, so any across-frequency
  integration here must take it.

## Medial geniculate nucleus

- **Function → structure.** Auditory thalamic relay, and **three divisions that differ in what drives
  them, not in flavour.** The **ventral division** is a **first-order** relay — driving input
  subcortical, from the inferior colliculus, exactly as the lateral geniculate nucleus is driven by the
  retina — tonotopic, sharply tuned, to the core. The **dorsal** and **medial** divisions are
  substantially **higher-order** relays: their driving input is **layer 5 of auditory cortex**, so they
  carry cortical output back into the thalamus and out to another cortical area — a transthalamic route
  between cortical areas rather than a stage on the way up from the ear. The ventral division's
  principal cell is **bi-tufted**, with diametrically opposed dendritic fields, sitting in rows
  50–100 µm wide that form fibrodendritic laminae. **Third occurrence of one geometry in this section**
  — the medial superior olive's bipolar cell, the colliculus's disc-shaped cell, and this one all build
  isofrequency sheets from cells whose dendrites lie in the plane of the sheet.
- **Inputs.**
  - **← inferior colliculus** (brachium) → principally the ventral division — the assembled auditory
    scene; the **driver**, and a minority of the synapses. **Roughly 20% of that collicular input is
    GABAergic** to the ventral and medial divisions, ~11% to the dorsal — **so the edge that sets what
    the message is also carries a substantial inhibitory component**, and a stage modelling it as pure
    excitatory drive would be wrong about a fifth of it. Itself **three parallel pathways** — lemniscal,
    polysensory, diffuse — terminating preferentially in the ventral, medial and dorsal divisions.
    Fan-in: to derive.
  - **← primary auditory cortex, layer 6** (small terminals), reaching **all three divisions** —
    modulatory, no new content. Fan-in: to derive.
  - **← primary auditory cortex, layer 5** (giant terminals) → **dorsal and medial divisions** —
    **cortical content, as a driver.** Giant terminals are the signature of a driver, and this is what
    makes those two divisions higher-order. Fan-in: to derive.
  - **← thalamic reticular nucleus** — inhibition, the gate; and that nucleus's auditory sector is
    itself layered by relay class, **so the gate is applied separately to the first-order and
    higher-order relays.** Fan-in: to derive.
- **Outputs.**
  - **→ primary auditory cortex**, from the **ventral division** — the lemniscal payload, sharply
    tonotopic, relayed and **gated, not transformed.** Fan-out: to derive.
  - **→ auditory belt and parabelt**, from the **dorsal division** — the non-tonotopic, broadly tuned
    signal, **and on the higher-order limb, cortical content returning from layer 5.** Fan-out: to
    derive.
  - **→ wide cortical targets and the amygdala**, from the **medial division** — a coarse, broadly
    tuned multisensory alarm signal: enough to say *something loud and sudden happened, roughly there*,
    and not enough to identify it. **The payload is impoverished by design, and that is what makes it
    fast.** Fan-out: to derive.
  - **→ inferior colliculus** (descending), from the **medial division** and associated nuclei — with a
    specific negative alongside: **the ventral and dorsal divisions send no return projection to the
    colliculus**, so the descending limb does not mirror the ascending one. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~1.8–2.3M neurons, soft — no direct human count; bracketed by
  comparability with the lateral geniculate nucleus's firm ~1.8M and by a volume cross-check at that
  nucleus's ~17,000 neurons/mm³ against this one's verified ~134 mm³, which gives ~2.3M. Fan-in to
  derive, bounded ≤ 16 bits → **≤ 4.10 MB** at 2.05M.
  **A partition is available in principle and changes the output count, not the store:** if the primate
  interneuron proportion holds, roughly a quarter of the total are local inhibitory cells that project
  nowhere outside the nucleus and are therefore not part of the thalamocortical output.
- **Shape.** **Laminated nucleus**, rank 3: **(division, lamina, position)** — three divisions, and
  the ventral division's principal cells sitting in **rows about 50–100 µm wide** whose bi-tufted
  dendritic fields form fibrodendritic laminae. **Row width is a measured pitch**, one of the few in
  the map. Neuron count ~1.8–2.3M with the **division partition to derive**; the medial division
  admits **no further subdivision at all**, so that axis is rank-1 by the description rather than by
  omission. **A quarter of the total may be local interneurons that project nowhere**, which changes
  the output extent without changing the array.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the layer-6 modulatory loop and the layer-5 driver loop
  both pass through cortex present in this section, and the reticular gate is a third; **the higher-order
  divisions cannot function at all without their cortical driver**, so for them co-instantiation is not
  a discipline but a precondition. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The sharpest species-transfer hazard in the pathway sits here.**
  The GABAergic local interneuron proportion runs from **under 1% in bat and rat — some divisions with
  none at all — to 25% or more in cat and monkey**, with primate thalamus generally 25–30%. This is
  specific to the auditory thalamus: the lateral geniculate nucleus holds about the same proportion
  across species, and so do the colliculus and auditory cortex. **Only this nucleus swings that way.**
  In rodent it has essentially no interneurons and its inhibition comes from the reticular nucleus
  alone; in cat, monkey and by extension human there are **two independent inhibitory systems.** A
  circuit for this structure taken from mouse would be missing an entire population that is present in
  us. **Internal edges are to derive throughout** — including whether this nucleus builds the triadic
  glomerulus its visual counterpart does, which the interneuron figures make answerable in primates and
  unanswerable in rodents.

## Primary auditory cortex

- **Function → structure.** The auditory core — koniocortical, tonotopic, taking the lemniscal thalamic
  drive, with the shortest cortical latency of any auditory field. Carries **spectrotemporal receptive
  fields**: frequency tuning, onset and offset, frequency-modulated sweep rate and direction,
  bandwidth, intensity, temporal modulation. **This is the auditory counterpart of V1's oriented-edge
  code — local features, not objects.** Areal sub-structures in human: **Te1.1, Te1.0, Te1.2** in a
  medial-to-lateral sequence along the long axis of Heschl's gyrus, all koniocortical with a
  well-developed layer 4, Te1.0 in the middle being the one usually equated with the core proper and
  carrying the **highest myelination of any temporal area.** Laminar sub-structures: **eight** —
  1, 2, 3, 4, 5a, 5b, 6a, 6b — layer 4 undivided but koniocortical, the architectural signature of a
  heavy thalamic driver. Tangential sub-structures: **to derive** in human.
- **Inputs.**
  - **← medial geniculate nucleus, ventral division**, point-to-point → **layer 4** — the tonotopic
    spectrum with periodicity and duration tuning and the binaural cues bound with elevation. **A
    minority driver: ~20% of this area's excitatory input is thalamic, ~80% intracortical.** Fan-in: to
    derive.
  - **← auditory belt** (descending), principally → **layer 1.** Fan-in: to derive.
  - **← contralateral primary auditory cortex** (callosal), from **layers 3 and 5**, terminating
    throughout layers 2–6, densest in 2 and 3 and **sparsest in layer 4** — see Justification. Fan-in:
    to derive.
- **Outputs.**
  - **→ auditory belt** — the spectrotemporal receptive-field code on a tonotopic map. **Left and right
    differ as a bias from here on** — left favouring finer temporal resolution, right finer spectral —
    **so the two hemispheres' payloads are no longer identical.** Fan-out: to derive.
  - **→ auditory parabelt** — **weak but not absent**: injections confined to the parabelt label only
    few neurons here against large numbers in the belt. Recorded because *few is not none*, which
    matters for anything treating the three tiers as strictly serial. Fan-out: to derive, and small.
  - **→ medial geniculate nucleus, from layer 6** (all three divisions), **and inferior colliculus**
    (mainly its dorsal and external cortices) — modulatory, no new content. Fan-out: to derive.
  - **→ medial geniculate nucleus, dorsal and medial divisions, from layer 5** (giant terminals) —
    **cortical content as a driver.** The two corticofugal limbs leave from different layers and do
    different jobs. Fan-out: to derive.
  - **→ contralateral primary auditory cortex** (callosal), from **layers 3 and 5.** Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~20M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 40.00
  MB.** **The variability is not measurement noise** — Heschl's gyrus differs markedly between
  individuals and between the two hemispheres of one brain, including in the number of transverse gyri
  present, with a left>right volume asymmetry.
- **Shape.** **Sheet**, rank 3: **(lamina, areal field, position along the tonotopic axis)** — eight
  laminae, three human areal sub-elements in a medial-to-lateral sequence, ~20M neurons per
  hemisphere with the partition **to derive**.
  **The map axis cannot be labelled, and that blocks the shape rather than decorating it.** Four
  proposals for the tonotopic gradient's orientation are on record — parallel to the gyrus,
  perpendicular, circular, and high-low-high with an inverted V. **An axis whose direction is unknown
  cannot be indexed**, so this structure has a rank and no orientation for its principal axis. The
  areal count is unsettled too: the human core may be three fields or **one**.
- **Edge latency.** All edges **to derive.** One gradient is recorded and is not a latency figure:
  response latency **increases from posteromedial to anterolateral** along the gyrus, for tones and for
  isolated syllables.
- **Invariant conformance.** Co-instantiation: satisfied; three loops close through this structure — to
  the geniculate on two separate limbs, to the colliculus, and across the callosum. Per-edge latency:
  satisfied, all to derive.
- **Justification (biological).** **Two structural claims here are weaker than the tier's role
  suggests, and both bear on what can be built.** First, **the correspondence to the macaque core is
  not established**: human cytoarchitecture is consistent with three primary-like fields, functional
  imaging mostly finds two, and one reading treats Te1.1 and Te1.2 as medial junction and lateral belt
  rather than primary fields at all — which would make the human core **one** area, not three. Second,
  and more consequential, **the tonotopic map's axis in human is disputed**: parallel to Heschl's
  gyrus, perpendicular to it, circular, or a high-low-high gradient with an inverted V, are all on
  record. **A map is a spatial claim.** If the axis is unknown then "tonotopic" says frequency is
  ordered somehow, not what is where — which is less than a build needs, and the axis is **to derive.**
  **The callosal edge carries a normalisation, not a message**, and it is stated here once for the
  whole auditory cortex. Audition has **no representational midline to stitch**, unlike vision's
  vertical meridian and somatosensation's proximal body, so its callosal connections are widespread
  across the entire tonotopic map rather than restricted to a seam — **treating the auditory callosum
  as a seam would be a category error.** It connects matched frequency bands, principally homotopically;
  it avoids the layer the thalamic driver targets; it lands preferentially on the patchy **binaural
  columns** and not on monaural regions; every fibre is excitatory, so its net inhibitory effect is
  feedforward through local interneurons; and its measured consequences are **sharpened tuning and
  enforced signal-to-noise ratio.** **A consumer treating it as a second copy of the other hemisphere's
  percept would be wrong about what it does.** It is also what **holds the hemispheric asymmetry in
  place**: callosotomy raises the right pole's activity and abolishes the left-right difference, so
  lateralisation is a dynamic equilibrium maintained by an edge rather than a static division of labour.

## Auditory belt

- **Function → structure.** Nonlinear spectral and temporal integration — tuning to noise bandwidth, to
  frequency-modulated sweep rate and direction, and to a limited set of species-specific vocalisations;
  broader tuning than the core, and responding better to broad spectral stimuli than to pure tones.
  **Areal sub-structures: eight fields, not two.** A **lateral belt** — caudolateral, middle lateral,
  anterolateral, rostrotemporal lateral — and a **medial belt** — caudomedial, middle medial,
  rostromedial, rostrotemporal medial. Each lateral field sits beside a core field and each medial
  field beside the same core field on the other side, **so the ring is organised by its relation to the
  core rather than as a sequence of its own.** Laminar sub-structures: **eight**, layer 4 present but
  **less granular than the core's** — the signature of a field one step off the thalamic driver.
  Tonotopy survives here and only shows itself with the right probe: with narrowband noise the best
  centre frequency varies systematically, **with reversals at the field borders, and those reversals are
  how the borders are drawn.**
- **Inputs.**
  - **← primary auditory cortex** — the spectrotemporal feature code, tonotopic. Fan-in: to derive.
  - **← medial geniculate nucleus, dorsal division** — the belt's **preferential** thalamic source, and
    the same division that is substantially higher-order, **so part of what arrives here is cortical
    output returning through the thalamus rather than a fresh ascending signal.** Fan-in: to derive.
  - **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. **Denser here than at
    the core and less strictly area-to-area**, because association fields are more heavily callosally
    connected and carry proportionally more heterotopic traffic. Fan-in / fan-out: to derive.
- **Outputs.**
  - **→ auditory parabelt, rostral division**, from the **anterolateral** field — call and **identity**
    features; no location. Fan-out: to derive.
  - **→ auditory parabelt, caudal division**, from the **caudolateral** field — **sound-source location
    (azimuth)**; not identity, and **not a map** — see Justification. Fan-out: to derive.
  - **→ auditory parabelt, both divisions**, from the **rostromedial** field of the medial belt — **a
    source that ignores the caudorostral split** the lateral belt observes, which makes it a different
    kind of input from one that honours it. Payload to derive. Fan-out: to derive.
  - **→ prefrontal cortex, directly** (`11_frontal_lobe`), split by origin and kept split at the
    destination — the **anterior** belt to the frontal pole, rostral principal sulcus and ventral
    prefrontal areas; the **caudal** belt to the caudal principal sulcus and the **frontal eye
    field.** **The caudal target being the frontal eye field says plainly what the "where" payload is
    for: moving the eyes to the sound.** Fan-out: to derive.
    **Checked against the consumer file, and all three named prefrontal targets declare this edge at
    their end.** Its frontopolar entry declares `← auditory association cortex — the anterior belt`
    onto its **medial** part; its ventrolateral prefrontal entry declares `← the anterior auditory
    belt, directly, onto areas 12 and 45`; and its frontal eye field entry declares `← the caudal
    auditory belt, directly`.
    **The arity mismatch is at this end.** This is written as **one** output line naming three
    destinations in two groups, while the consumer writes **three separate inputs at three separate
    entries.** So the edge count differs across the boundary by two, and the split is owed here rather
    than there — the consumer has already done it.
    **One consumer-end fact this line does not carry, and it bears on the payload.** The frontopolar
    target is its **medial** part specifically, and that file records audition as **the principal
    external connection of that part** — more than 90% of the *lateral* part's afferents are frontal,
    while the medial surface takes substantial temporal input. So this edge does not reach a supramodal
    area incidentally; it is the main input to the part it reaches.
  - **→ primary auditory cortex, medial geniculate nucleus and inferior colliculus** (corticofugal).
    Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~25M neurons for the belt as a whole. Fan-in to derive,
  bounded ≤ 16 bits → **≤ 50.00 MB.** **No per-field partition exists**, and with eight fields named
  that is a visible gap rather than an implicit one — **eight sub-structures sharing one count.**
- **Shape.** **Sheet**, rank 3: **(lamina, field, position)** — eight laminae against **eight areal
  fields**, four lateral and four medial, arranged as a ring around the core. **The field axis is not
  a sequence**: each lateral field sits beside a core field and each medial field beside the same core
  field on the other side, so the axis is indexed by relation to the core rather than by order.
  ~25M neurons with **no per-field partition — eight sub-elements sharing one count.** Field borders
  are drawn at **tonotopic reversals**, which means the map axis reverses at each boundary rather than
  running monotonically across the structure.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; corticofugal loops to core, thalamus and
  colliculus, plus the callosal loop. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The spatial payload is not a map, and this is the strongest of the
  section's three map withdrawals.** The auditory cortex has been searched for a topographic map of
  auditory space and none has been found. What is there is an **opponent hemifield population rate
  code**: two broadly tuned populations, one preferring each hemifield, with location read from the
  **balance** between them. Two properties bind a consumer: **location is carried by the region of
  steepest change in the response-azimuth function, not by the peak** — a downstream stage looking for
  a maximum finds nothing useful — and **it is robust to sound level**, precisely because it is a slope
  code and not a peak code. Resolution is correspondingly coarse: reliable left-versus-right with
  confusion *within* a hemifield.
  **The what/where split is supported and graded rather than clean** — belt-to-parabelt projections
  overlap, and the temporal-field connections of the two streams overlap more than the frontal ones do,
  so the streams separate progressively rather than at a border. **The identity payload is neither
  "sound" nor "meaning" but a third thing**: the complex, call-like spectrotemporal *class*, abstracted
  well above tones and noise and not yet organised by referent — prefrontal responses cluster by
  acoustics rather than by referent, while pure tones scarcely drive those cells at all.
  **And the eight fields are a macaque parcellation applied to human**: the human belt's internal
  boundaries are drawn by extending the borders between adjacent core fields laterally, inherited from
  the monkey model rather than measured, while a large expanse of human lateral superior temporal cortex
  may have no clear monkey homologue at all. The **medial belt** is poorly characterised in the
  literature and shows broad **spatial** tuning, so the "where" function may be distributed around the
  medial half of the ring — **to derive.**

## Auditory parabelt

- **Function → structure.** Complex sound-objects and sequences with invariance building — identity
  invariant to talker, pitch and level ("what"), and location and motion ("where"). Up the
  core → belt → parabelt hierarchy, **tuning bandwidth, latency and stimulus specificity rise while
  temporal precision falls, and that gradient *is* the payload transformation.** Divisional
  sub-structures: **two, "at least"** — a **rostral** and a **caudal** division, the hedge being the
  literature's own. Laminar sub-structures: **eight**, layer 4 thinner and less granular than the
  belt's, with enlarged pyramidal populations in **3c** and **5** — the feedforward and driver-output
  layers, consistent with a stage whose job is to project widely. It occupies the **posterior two
  thirds** of the superior temporal gyrus; the remaining third responds to sound and has not been shown
  to receive significant thalamic input, so it is neither core, belt nor parabelt — **to derive.**
- **Inputs.**
  - **← anterolateral belt** → **rostral** division — call and identity features. Fan-in: to derive.
  - **← caudolateral belt** → **caudal** division — location, as an opponent rate code. **The
    belt-to-parabelt connections are topographic in the caudorostral dimension**, which is what makes
    the two divisions two streams rather than two samples of one. Fan-in: to derive.
  - **← rostromedial belt** → **both** divisions. Payload to derive. Fan-in: to derive.
  - **← primary auditory cortex** — weak rather than absent. Fan-in: to derive, and small.
  - **← medial geniculate nucleus, dorsal division** — the non-tonotopic thalamic signal, and **it
    cannot be what imposes a frequency map here**, since that division is not tonotopically organised.
    Fan-in: to derive.
  - **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation, denser than at the
    core. Fan-in / fan-out: to derive.
- **Outputs.**
  - **→ anterior superior temporal gyrus and sulcus**, from the **rostral** division — sound-object
    identity, invariance-building. Fan-out: to derive.
  - **→ posterior superior temporal gyrus and the Sylvian parieto-temporal area**, from the **caudal**
    division — location and motion. Fan-out: to derive.
  - **→ the rostrally-directed stream** — temporal pole, ventral/rostral/medial prefrontal cortex,
    rostral cingulate, parahippocampal areas, and the **amygdala**. The amygdala target is the one worth
    naming: **a cortical identity signal reaching the amygdala directly is a second route to affective
    evaluation alongside the fast subcortical one**, and unlike that one this route has already done the
    invariance work. Fan-out: to derive.
  - **→ the caudally-directed stream** — temporoparietal junction, posterior parietal and occipital
    regions **including secondary visual cortex** (`01_visual_pathway`), caudal and dorsal prefrontal
    cortex, dorsal cingulate, parahippocampal areas. **An auditory area writing into visual cortex runs
    opposite to the direction this section otherwise records.** Fan-out: to derive.
    **The secondary-visual-cortex limb has a matching declaration**, which
    qualifies the arity note below: that note says splitting these lines would name far ends that
    *mostly have no matching declaration*, and **this limb is one of the exceptions.** The visual file's
    V2 entry declares `← auditory parabelt, caudal division — an auditory association area writing into
    secondary visual cortex`, and asks a question this end can nearly answer: **which tangential
    compartment it reaches.** That end notes its **thick stripes are the motion and disparity
    channel**, and this end types the caudal division's payload as **location and motion**. **So thick
    stripes are the candidate compartment, on the payloads alone, and neither end states it.** A
    candidate, not a resolution — recorded because the two ends together constrain it and neither does
    alone. **This limb can be split out now; the rest of the line still cannot.**
  - **→ upper bank of the superior temporal sulcus**, and **the insula and retroinsular areas** — two
    further output streams beyond the rostral/caudal pair. Payload to derive. Fan-out: to derive.
  - **Arity note carried from the source:** the three stream edges above are each written as **one edge
    naming many targets**, which is not one edge. Splitting them names far ends that mostly have no
    matching declaration, so the split is **owed at the source** and is not performed here — performing
    it would invent the arity.
- **Sizing.** Basis: **per hemisphere.** ~56M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 112.00
  MB.** **No per-division partition exists** for a structure the source now describes as two divisions
  with a possible hierarchy between them.
- **Shape.** **Sheet**, rank 3: **(lamina, division, position)** — eight laminae against **two
  divisions, "at least"**, the hedge being the description's own, so the division axis has an extent
  that is a lower bound rather than a count. ~56M neurons, partition **to derive**. **The map axis is
  weakly ordered here and that is a positive finding**: frequency is ordered enough to locate the
  border between the two divisions and not ordered enough to index as a map.
- **Edge latency.** All edges **to derive**, and one internal gradient is recorded qualitatively:
  response latencies rise from the caudal to the rostral division.
- **Invariant conformance.** Co-instantiation: satisfied. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The staining agrees with the connectional hierarchy rather than
  merely accompanying it** — parvalbumin, acetylcholinesterase and cytochrome-oxidase fall off in
  steps, heaviest in the core, moderate in the belt, lightest here.
  **Whether this is one stage or two is unsettled, and it matters structurally.** The caudal-to-rostral
  latency gradient plus activation beginning in **layer 4** of the rostral division admits two readings:
  the parabelt inherits the gradient already present in the belt, or there is an additional
  hierarchical step inside it. **Under the second, this structure is two stages in series and the
  "what" and "where" divisions are not siblings** — which contradicts the parallel-streams picture.
  **And the human evidence contradicts the macaque arrangement**: human electrocorticography finds the
  shortest latencies to clicks and vowels in the **middle** of the superior temporal gyrus, not at the
  caudal end where the macaque gradient starts, so the internal edge may run the wrong way or from the
  wrong place in a human brain. **Tonotopy here is weaker and less orderly than in the core or belt,
  and that is a positive finding**: frequency is ordered enough to locate the border between the two
  divisions and not ordered enough to call a map.

## Anterior superior temporal gyrus and sulcus

- **Function → structure.** Top of the auditory ventral stream. **Sub-structures along the
  posterior-to-anterior axis: three stages on a timescale hierarchy** — phoneme-length processing in
  the **mid** superior temporal gyrus, word-length in the **anterior gyrus**, phrase-length beginning
  in the **anterior sulcus**. **The organising variable is the length of the pattern being integrated**,
  which makes this a hierarchy of temporal receptive windows rather than of feature complexity.
  **A second sub-structure system occupies the same structure on the same axis**: three **voice patches**
  per hemisphere — posterior, mid, anterior — densest in the right posterior sulcus. **They are not the
  same three things as the speech stages.** Laminar sub-structures: **eight**, homotypical association
  cortex, layer 4 present and thin.
- **Inputs.**
  - **← auditory parabelt, rostral division** → the **mid** superior temporal gyrus — talker-invariant
    sound-object identity. The edge terminates at the mid gyrus and the rest of the chain is internal.
    Fan-in: to derive.
  - **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. Fan-in / fan-out: to
    derive.
- **Outputs.**
  - **→ the distributed semantic system** (lexical access) — **invariant phonetic form**: phonemes
    composed into words and phrases, plus voice identity. **This is the auditory line's inferotemporal
    cortex, and the payload hardens the same way** — "the word that was said" and "who said it" are
    **phrases, not types**: no units, no frame. Fan-out: to derive.
  - **→ temporal pole** (`07_anterior_temporal_lobe`) **and middle temporal gyrus → ventrolateral
    prefrontal cortex** (`11_frontal_lobe`) — the same identity code, toward amodal concept and
    controlled retrieval. Fan-out: to derive.
    **The temporal-pole limb is two-ended.** That consumer declares
    `← rostral superior temporal gyrus — talker-invariant word and sound-object identity, the auditory
    "what" endpoint`, and records it as **the principal input to its dorsolateral subdivision**.
    **This line is a chained compound and the arity is owed here.** It names two targets and an onward
    hop on one edge: the temporal pole and the middle temporal gyrus are separate destinations, and the
    ventrolateral prefrontal cortex is reached *through* them rather than by this edge. **The consumer
    declares its own onward output to ventrolateral prefrontal cortex separately**, so the hop is a
    second edge at a second producer, not part of this one.
  - **→ amygdala and inferior prefrontal cortex**, on the **voice-identity** payload specifically —
    speaker identity and vocal affect. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~48M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 96.00
  MB.** See the section totals for the anchor this figure belongs to and for the laterality problem it
  runs into.
- **Shape.** **Sheet**, rank 3, and **two sub-element systems compete for the same axis** —
  a three-stage speech hierarchy running posterior to anterior on **integration-window length**, and
  three **voice patches** on the same axis that are not the same three things. **The shape must carry
  both or it will assert they are one.** ~48M neurons, partition **to derive**.
  **And the tangential extent is not shared across individuals**: the voice patches are highly
  reproducible within one brain and highly variable between brains in location. **A per-structure count
  is meaningful and a per-coordinate index is not**, which is a constraint on what any allocation can
  claim to address.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; the callosal loop closes here and the
  internal three-stage chain is a series, not a loop. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **Lateralisation here is contested and the architecture must not
  carry a single label.** For **speech content** the literature is divided: one meta-analytic model is
  explicitly left-biased, while the dual-stream account holds the ventral stream **largely bilateral**
  with computational differences rather than a division of labour, and word deafness most commonly
  follows **bilateral** superior temporal damage. For **voice identity** the direction is the other
  one — right-biased on both accounts. **So a single "left-lateralised" label is wrong regardless of how
  the speech dispute resolves**, because it would be applied to one structure carrying two payloads that
  lateralise oppositely. **Voice selectivity is itself contested about which structure is selective**:
  damage to the posterior sulcus does not impair voice recognition, so of the three voice patches the
  most active may not be the one doing the recognising.
  **One property is awkward specifically for a document that sizes structures and routes edges between
  them:** the voice patches are highly reproducible **within** an individual and highly variable
  **between** individuals in anatomical location. **A per-structure unit count is meaningful and a
  per-coordinate one is not.**
  **Internal edges between the speech hierarchy and the voice patches are to derive**, and that is the
  interesting gap: the two systems occupy the same territory on the same axis and carry payloads that must
  be separated somewhere, since *what was said* and *who said it* leave on different edges to different
  targets.

## Posterior superior temporal gyrus and the Sylvian parieto-temporal area

- **Function → structure.** Auditory space and motion, and the sensorimotor interface for sound.
  **Sub-structures: three in series along the posterior axis** — the posterior superior temporal
  **gyrus**, the posterior superior temporal **sulcus**, and the **Sylvian parieto-temporal area** at
  the far end, the auditory-motor hinge. Laminar sub-structures: **eight**, homotypical association
  cortex. **Tangentially the hinge is a patchy sensory/motor mosaic** — distinct spatial activation
  patterns for the sensory and motor phases of one task, attributed to different neuronal
  subpopulations. **So the hinge is not a homogeneous converter but two interdigitated populations in
  one territory**, and an edge that should terminate on the motor-weighted patches and not the
  sensory-weighted ones has no way to say so.
- **Inputs.**
  - **← auditory parabelt, caudal division** → the **posterior gyrus** — location and motion as an
    opponent rate code, and the auditory form of speech. The edge terminates at the posterior gyrus;
    the rest of the chain is internal. Fan-in: to derive.
  - **← visual and somatosensory cortex** — payload to derive. Recorded because the hinge responds to
    **silent lip-reading** and to **reading written words**, neither of which can arrive on an auditory
    edge. Fan-in: to derive.
  - **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. Fan-in / fan-out: to
    derive.
- **Outputs.**
  - **→ inferior parietal lobule (supramarginal gyrus), and onward to premotor and inferior frontal
    cortex** — the **auditory-to-motor mapping**: a sound target expressed in terms the motor system can
    act on, plus phonological working memory. Strongly left-dominant. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~40M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 80.00
  MB.** **No partition across the three sub-structures exists**, and for the hinge one may not be
  constructible in the usual way — see below.
- **Shape.** **Sheet**, rank 3: **(lamina, sub-element, position)**, three sub-elements in series.
  **The last of the three has no extent that can be stated**: the hinge is defined by response profile
  — the region responding to both auditory perception and silent vocal-tract gestures — so **its
  borders move with the task used to find it**, and an axis bounded by a criterion rather than by a
  boundary cannot be given a length. Tangentially it is a **patchy sensory/motor mosaic**, two
  interdigitated populations in one territory, and an edge that should reach the motor-weighted patches
  and not the sensory-weighted ones has no index to say so. ~40M neurons, partition **to derive**.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The hinge is defined functionally, not anatomically**, and that is a
  property rather than a detail: it is specified as the region that responds to both auditory
  perception and silent vocal-tract gestures. **A structure so defined has no border independent of the
  task used to elicit it**, so an edge terminating "on the Sylvian parieto-temporal area" is anchored to
  a response profile and not to a bounded structure — unlike, say, the medial superior olive. Every other
  structure in this section would still be there if nobody ran an experiment.
  **It is not speech-specific**: sensorimotor responses are equally robust for a tonal melody with
  covert humming as for speech, and it activates for silent lip-reading, for reading, and in musicians
  for covert playing. **So the function is auditory-to-vocal-tract guidance in general.**
  **And the central question has a named alternative answer of "nothing."** The literature distinguishes
  an area that acts as an **interface** between two tasks — a shared level of processing both draw on —
  from one that **integrates** one level into another. Under the first reading **there is no transform
  at this stage at all**, only a common representation the sensory and motor systems each read and
  write. The patchy mosaic is compatible with either and arguably favours the shared-representation
  reading, since a converter would not obviously need two segregated populations. **This is the one
  place in this section where the payload change may be null**, and it is recorded as unsettled rather
  than resolved in favour of a transform.

## Right-hemisphere prosodic homologues

- **Function → structure.** The right counterparts of the two temporal endpoints above, weighted toward
  **prosody and affect** rather than segmental content. **Sub-structures: two** — the right anterior
  superior temporal gyrus and sulcus (affective-voice and prosodic-contour identity), and the right
  posterior superior temporal gyrus (prosodic-spatial). **They are the right-side counterparts of two
  structures that have their own entries, and the source gives them one entry between them, which is a
  packaging decision rather than a finding — the split is owed at the source.** Laminar sub-structures:
  **eight**, homotypical association cortex. **No cytoarchitectural difference between the two
  hemispheres' versions of these areas is established**, which is itself worth recording: the claimed
  functional divergence has no declared structural correlate.
- **Inputs.**
  - **← right auditory parabelt** → the right superior temporal gyrus and sulcus — the same acoustic
    feature stream as the left, read with a **finer spectral and coarser temporal** bias: the primary
    auditory cortex asymmetry compounded up the hierarchy. Fan-in: to derive.
  - **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. Fan-in / fan-out: to
    derive.
- **Outputs.**
  - **→ semantic and limbic targets**, and for production the right inferior frontal gyrus — **prosodic
    and affective identity**: the contour of pitch, loudness, timing and stress and the emotional
    category it signals; **not** segmental content. Fan-out: to derive.
- **Sizing.** Basis: **the right side, both sub-structures combined.** ~50M neurons. Fan-in to derive,
  bounded ≤ 16 bits → **≤ 100.00 MB.** **This figure does not reconcile with the per-hemisphere figures
  of the two structures it is the counterpart of** — see the section totals.
- **Shape.** **Sheet**, rank 3, two sub-elements — and **this structure's shape is where the
  per-hemisphere convention visibly fails.** These are the right-side counterparts of two structures
  that have their own entries and their own per-hemisphere counts, so the same array is described twice
  under two conventions. ~50M for both against ~88M for the same two areas counted per hemisphere: the
  extents cannot both be right. **No cytoarchitectural difference between the two hemispheres' versions
  is established**, so the shapes are identical and only the extents disagree.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied, and the callosal edge is load-bearing here in
  a way it is not elsewhere — if lateralisation is an equilibrium held by interhemispheric inhibition,
  the edge is not an addition to these structures but a condition of their differing at all. Per-edge
  latency: satisfied, all to derive.
- **Justification (biological).** **Three competing accounts of why prosody lateralises, and none may be
  adopted silently.** The **biological** account makes affective prosody right-lateralised as
  hemispheric specialisation. The **functional** account makes lateralisation follow communicative
  function — emotional prosody right, linguistic prosody left — with the right operating on larger units
  and the left on smaller. The **acoustic** account makes it follow the cue: left for timing, right for
  pitch and spectral structure. **The aggregate evidence is bilateral with a right lean at best**:
  meta-analyses across dozens of lesion studies find both left and right damage compromising both
  emotional and linguistic prosodic perception, and imaging meta-analysis describes activity as highly
  bilateral with subtle right lateralisation at best. **Comprehension and identification of affective
  prosody lean right; production and linguistic prosody do not lean reliably at all.**
  **Part of the reported lateralisation is an artefact of paradigm**, which tells a builder how much to
  trust the rest: valence effects are strongly right-lateralised under blocked presentation and
  bilateral or left-accented in event-related designs, and explicit attention to prosody gives left
  lateralisation while implicit perception gives none. **The same structure lateralises differently
  depending on how it is asked.**
  **And the acoustic account is deflationary for this structure's status.** Its claim — left for
  temporal, right for spectral — is the same asymmetry already declared at the primary auditory cortex
  as a **bias and a trade-off**. If prosodic lateralisation is that bias working on longer stimuli, then
  this is **not a new divergence between the hemispheres but a downstream consequence of one recorded
  three stages earlier**, and treating it as new would double-count.

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Cochlea — type I spiral ganglion | per ear | ~31,500 | **0** (fan-in exactly 1) | **0** |
| Cochlea — type II spiral ganglion | per ear | ~2,500 | 4 (fan-in ~12) | ~1.2 kB |
| Cochlea — hair cells | per ear | ~15,500 | not a threshold gate | to derive |
| Cochlear nucleus | per hemisphere | ~0.5M | ≤ 16; **1** for the spherical bushy cell | ≤ 1.00 MB |
| Superior olive — medial superior olive | per side | ~15,500 | ≤ 16 | ≤ 0.031 MB |
| Superior olive — lateral superior olive | per side | ~5,600 | ≤ 16 | ≤ 0.011 MB |
| Superior olive — trapezoid body, periolivary | per side | to derive | **0** for the calyx target | to derive |
| Inferior colliculus | per side | ~0.6M (central nucleus ~420,000) | ≤ 16 | ≤ 1.20 MB |
| Medial geniculate nucleus | per hemisphere | ~1.8–2.3M | ≤ 16 | ≤ 4.10 MB |
| Primary auditory cortex | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB |
| Auditory belt | per hemisphere | ~25M | ≤ 16 | ≤ 50.00 MB |
| Auditory parabelt | per hemisphere | ~56M | ≤ 16 | ≤ 112.00 MB |
| Anterior superior temporal | per hemisphere | ~48M | ≤ 16 | ≤ 96.00 MB |
| Posterior superior temporal + hinge | per hemisphere | ~40M | ≤ 16 | ≤ 80.00 MB |
| Right prosodic homologues | right side, both | ~50M | ≤ 16 | ≤ 100.00 MB |
| **stated total** | mixed | | | **~484 MB** |

**The whole subcortical auditory pathway costs ~6.3 MB and the cortex ~478 MB**, a ratio of about 76:1,
and every localisation computation in the section happens in the cheap end. **The two structures that
compute azimuth together hold ~21,000 neurons and ~0.042 MB.**

**Three fan-ins in this section are known exactly, and two of them cost nothing.** A type I spiral
ganglion neuron contacts exactly one inner hair cell, and the medial nucleus of the trapezoid body's
principal cell receives one calyx of Held: **log₂(1) = 0, because a neuron with a single input has no
count to threshold.** The spherical bushy cell's one-or-two endbulbs cost 1 bit. **The pathway's
most timing-critical stages are its cheapest in parameter memory, and for the same reason they are
precise** — a low fan-in is what buys timing fidelity. That inverts the expectation that a
high-precision stage is an expensive one.

**A source-internal cross-check that closes.** The temporal-lobe anchor gives ~145M neurons per
hemisphere for the lateral association superior temporal cortex spanning parabelt, anterior and
posterior superior temporal. Recomputed: **56 + 48 + 40 = 144M**, in exactly the stated 7:6:5
proportions. That closes.

**A source-internal cross-check that does not close, and it is recorded here rather than repaired.**
The right prosodic homologues are given **~50M for both**, while the two structures they are the
counterparts of are given **~48M and ~40M per hemisphere — 88M for the same two areas.** Either those
two figures are left-hemisphere values labelled per-hemisphere, in which case the right side is
**1.76× smaller** and the anchor above cannot hold for both hemispheres; or they are true
per-hemisphere values, in which case the right homologues' 50M **double-counts** structure already
included. **The two readings differ by ~88 MB of parameter memory** in the table above. This is a
finding about the description and the repair belongs at that rung.

**The per-hemisphere convention does not survive this section, and the parabelt is where it stops.**
Below that tier the two sides are counterparts and one count serves both. Above it the source describes
**left** endpoints for segmental content and gives the **right** endpoints a separate entry with its own
count and its own payload — so from the parabelt upward there is no symmetric description to count once
and double. **The totals above are mixed-basis for that reason and are not a whole-brain figure.**

**The total is a floor.** Hair-cell storage is to derive, the trapezoid body and periolivary groups are
uncounted, eight belt fields share one count and two parabelt divisions share another, every cortical
fan-in sits at the 16-bit ceiling rather than at a measured value, and **state memory and edge storage
are not in this table at all.** Edge storage is the one that would bite hardest here: a pathway
resolving tens of microseconds implies a very short update interval, and edge storage scales with its
reciprocal. **That figure cannot be computed until the scheduling discipline is set, and it is not.**

**Memory is not a binding constraint and none of these figures is to be reduced.**
