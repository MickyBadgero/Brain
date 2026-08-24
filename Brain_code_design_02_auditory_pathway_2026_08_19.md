# Brain code design — 02 auditory pathway

**Date:** 2026-08-19
**Derived from:** `Brain_architecture_02_auditory_pathway`, `Brain_code_design_spec`, and CLAUDE.md.
**No other content source.**
**Implements:** `Brain_02_auditory_pathway.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
character for character, so that at coding time only this file is loaded. **One deviation from that
copy, and it is declared here so that anything else is a defect.** The architecture's **internal
cross-references** — *see Justification*, *see below*, *see the section totals*, *(below)* — are not
copied, because they point at fields this rung does not have. Their content is carried, at the entry
it belongs to.

**Eleven entries, one per architecture entry, same names, same order.**

**All eleven entries are written.**

---

## What is open for every entry in this file, stated once

Each entry names only what is open **beyond** this list.

- **Emission — graded or binary, and the unit's expressiveness.** Micky's, and unset. Until it is set,
  **no entry below writes an update equation as though the answer were given.** This section presses on
  the question harder than the visual line does: the cochlea's hair cells **produce graded receptor
  potentials with no action potentials at all**, and they are neither transducers in the sense that
  exempts a photoreceptor nor threshold gates.
- **The scheduling discipline.** Micky's, and the largest open item at this rung. **And this section is
  the strongest case in the map against a uniform interval**: three structures compute on arrival-time
  differences at the tens-of-microseconds scale, so setting every edge equal does not approximate the
  medial superior olive — it deletes what the medial superior olive computes.
- **The learning rules.** Micky's. Every Adaptation field reads *none set*.
- **Inter-structure connection topology.** Fan-in is a scalar per structure and the code needs a map.
  **This section supplies two exact fan-ins where the visual line supplied none** — one onto the type I
  spiral ganglion neuron, one or two onto the spherical bushy cell — and an exact fan-in is still not a
  pattern.
- **Tile geometry and sparsity.** Both surface-before-touching, both unset.
- **No numerical edge latency is stated anywhere in this section, so every edge reads *to derive*.**
  Four qualitative timing facts are recorded and each is a structural claim rather than a performance
  note: the interaural time difference computation works at **tens of microseconds**; **phase locking**
  at low frequencies makes waveform timing *part of the payload* on the auditory nerve rather than the
  schedule it arrives on; the **endbulb of Held** buys timing fidelity by morphology, its terminal
  large enough to generate an extracellular prepotential before the receiving cell's own spike, with
  exceptionally low jitter between the two; and the **octopus cell** detects coincidence across the
  tonotopic array at the highest temporal precision in the brain.
- **Edge storage cannot be closed anywhere in this file**, for the same three missing terms as
  elsewhere: latency, update interval, bytes per value. Each entry records its edge count. **Never
  summed with parameter memory or state.**

**Counting basis is not uniform.** **Per ear** at the cochlea, **per side** through the brainstem and
thalamus, **per hemisphere** in cortex — and **above the parabelt the per-hemisphere convention breaks
down**, because the two hemispheres stop being counterparts and the architecture gives the right-side
endpoints an entry of their own.

**The tonotopic map is inherited, not computed.** Position along the cochlear tube maps to frequency,
base to apex, high to low, by the mechanics of the basilar membrane's graded stiffness and mass. What
leaves the ear is already sorted, and **every downstream structure inherits that map rather than
computing it.** No entry below writes a frequency analysis.

**One structural difference from the visual line governs every array in this file.** The cochlear sheet
is **one-dimensional**: position *is* frequency and there is no second axis to index, where a
retinotopic sheet has two. An array shaped like a visual sheet would give this pathway a dimension the
organ does not have.

---

# 1. Cochlea

## Contract

**Inputs.**
- **← sound-pressure vibration, via the middle ear** — mechanical, not a neural edge. Fan-in: not
  applicable.
- **← superior olivary complex**, medial olivocochlear efferents, onto the **outer hair cells** — a
  gain command, no stimulus content. Fan-in: to derive.
- **← branchiomotor / visceromotor nuclei** (`15_cranial_nerve_nuclei`), indirectly via the stapedius
  muscle — the acoustic reflex's attenuation. The effector is a middle-ear muscle, outside scope, so
  this is an influence on the input above rather than an edge onto neural structure.
  The named producer has an entry and it declares the muscle, not this loop. That entry's facial
  nucleus drives **stapedius** and its output line to orofacial striated muscle carries it — **so the
  efferent half of this reflex is written at both ends. The afferent half is written at neither**: that
  entry declares no auditory input of any kind, and the drive onto it is declared only at this file's
  superior olivary complex, where the endpoint names an arc rather than a nucleus.

**Outputs.**
- **→ cochlear nucleus**, via the auditory nerve, from the **inner hair cells** through the **type I
  spiral ganglion neurons** (~30,000 fibres) — energy in one narrow frequency band as a function of
  time, tonotopically ordered, with waveform timing preserved by phase locking at low frequencies.
  **Fan-out: 5–30** type I neurons per inner hair cell; **fan-in exactly one** — each type I neuron
  contacts one inner hair cell. **A pure divergence with no convergence at all.**
- **→ cochlear nucleus**, from the **outer hair cells** through the **type II spiral ganglion neurons**
  (~5–10% of the ganglion, unmyelinated) — **not sound.** These fibres are not required for hearing;
  the current reading is a **damage signal from the organ of Corti**. Fan-out: each type II neuron
  branches onto roughly a dozen outer hair cells; **fan-in ~12**, the opposite arity to the line above.

**Sizing.** Basis: **per ear.**
- **Type I spiral ganglion, ~31,500: zero.** Fan-in is exactly one, and log₂(1) = 0 — **a neuron with a
  single input stores no threshold, because there is no count to compare against.** This is the first
  structure in the map where a *known* fan-in drives the cost to zero rather than an unknown one
  leaving it open.
- **Type II spiral ganglion, ~2,500** at fan-in ~12 → 4 bits → **~1.2 kB.**
- **Hair cells, ~15,500 inner and outer: to derive, and not zero.** They are **not neurons** — they are
  sensory epithelial cells — and they **produce graded receptor potentials with no action potentials at
  all.** Neither the transducer exception nor the threshold-gate model reaches them.
- **Structure total: ~1.2 kB firm, plus the hair-cell store to derive.**

**Shape.** **Sheet, and it is one-dimensional**, which is the structural difference between this
section and the visual one. Rank 2: **(cell class, position along the tube)** — position *is* frequency,
base to apex, high to low. Extents are measured: **~3,500 inner hair cells** and **~12,000 outer** in
one row and three rows over a **~35 mm** tube, **~30,000–35,000** spiral ganglion neurons. **The
tonotopic axis is the only map axis**; there is no second dimension to index, where a retinotopic sheet
has two.

**Edge latency.** All edges **to derive.**

## Representation — declared once per line, inherited by every consumer

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← sound-pressure vibration, via the middle ear | sound pressure | to derive | **event-driven** — an acoustic arrival; the organ has no sampling rate of its own recorded | **none — a pressure waveform at a point**, not yet a map |
| ← superior olivary complex → outer hair cells | **gain command — no stimulus content** | to derive | event-driven | tonotopic position |
| ← branchiomotor / visceromotor (`15_cranial_nerve_nuclei`) via stapedius | **attenuation — mechanical, and not an edge onto neural structure** | to derive | event-driven | **none** |
| → cochlear nucleus, type I | **energy in one narrow band as a function of time** | to derive | event-driven | **tonotopic, rank 1** — position is frequency |
| → cochlear nucleus, type II | **not sound — a damage signal from the organ of Corti** | to derive | event-driven | tonotopic position |
| cochlear amplifier (outer hair cell ↔ basilar membrane) | **force**, added back into the travelling wave | to derive | **continuous, mechanical** | tonotopic position |

**Two rows here carry no sound and one carries no neural signal at all.** The type II line is the sharp
one: it runs on the same nerve, in the same tonotopic order, to the same target, and **it is not
audition.** A consumer that reads the auditory nerve as one bus of ~30,000 sound-carrying fibres has
absorbed ~2,500 damage-signal fibres into the spectrum.

**The input row has no coordinate frame and the output rows do**, and the structure between them
supplies the frame mechanically. That is the one place in this file where a frame is created rather
than inherited or transformed.

## Algorithm

- **Transform.** Two operations, and **the first is not neural**:
  1. **Mechanical frequency analysis, before any neural processing happens.** The decomposition is done
     by the mechanics of the basilar membrane's graded stiffness and mass. **This is a property of the
     organ and not a computation any neural stage performs**, and it is why no entry in this file
     computes a spectrum. **No standard operation is named above**; a filterbank is the obvious
     candidate and **it is not written here**, because a bank of filters is a design decision about how
     to model a mechanical structure and nothing above licenses its order, spacing or response.
  2. **Transduction**, at the inner hair cells: vibration to graded receptor potential. A **transducer**
     whose input edge is not a projection — fan-in reads *not applicable* rather than underived.
- **The organ runs on a battery it supplies itself.** The middle fluid compartment is held at a standing
  positive voltage, the **endocochlear potential**, **supplied by the structure and not by the
  stimulus.** It is what the transduction current runs on and the reason the organ responds to
  vibrations of atomic dimension. **An update equation that draws all its energy from the stimulus has
  the wrong power source**, and this is a constraint on the arithmetic in the same way the retina's sign
  inversion is.
- **The amplifier is a mechanical feedback loop inside the sensory organ.** Outer hair cells add force
  back into the basilar-membrane travelling wave through **prestin**, a voltage-driven membrane protein
  that changes cell length directly. **Fan-in and fan-out read *not applicable* — the transfer is
  mechanical.** With light at the retina and the endocrine limbs elsewhere in the map, this is the third
  class of edge that takes real time and is not conduction plus synaptic transmission.
  **This loop cannot be staged and is not a refinement:** an unamplified cochlea is **40–60 dB less
  sensitive**, roughly a hundredfold, which is not a degraded version of the same structure. The loop's
  output is observable from outside the head as otoacoustic emissions.
- **A sensor with a servo built into it**, and the servo's set point comes from the brain: the medial
  olivocochlear efferents land on the outer hair cells, so **the brain sets the gain of its own front
  end before transduction.** Without that limb the front end has no set point.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `inner_hair_cell_state` | (~3,500,) rank 1 | **open, and not defaultable** — graded receptor potential, no action potential | to derive | to derive |
  | `outer_hair_cell_state` | (~12,000,) rank 1 | **open, and not defaultable** | to derive | to derive |
  | `type_I_active` | (~31,500,) rank 1 | open — emission question | to derive | to derive |
  | `type_I_threshold` | — | **absent by derivation, not by omission** | — | — |
  | `type_II_active` | (~2,500,) rank 1 | open — emission question | to derive | to derive |
  | `type_II_threshold` | (~2,500,) | 4 bits = `ceil(log₂(12))` | 0 … 12 | count of active inputs |

  **Rank 1 throughout, and this is the finding the shape field forces.** Position along the tube *is*
  frequency; there is no second axis. **Every extent here is measured**, which makes this the only
  structure in either of the first two sections whose arrays can be sized today — and they still cannot
  be allocated, because tile geometry and sparsity are unset.
  **`type_I_threshold` does not exist**, and the entry says so positively rather than leaving the row
  out. A fan-in of exactly one gives log₂(1) = 0 bits: there is no count to compare against a threshold,
  so the array is absent by derivation. **Allocating a zero-length array would assert a store the
  structure does not have; omitting the row silently would read as an oversight.**
  **The hair cells are neither transducer-exempt nor threshold gates.** They are not neurons, they are
  sensory epithelial cells, and they produce graded potentials with no action potentials at all.
  §5a forbids defaulting their store to zero or to `log₂(fan-in)`. **This is the widest such gap in
  either section: ~15,500 cells whose store cannot be written at all.**
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `type_I_fan_in` | inputs per neuron | **exactly 1** | the architecture's Sizing field — measured, not bounded |
  | `type_I_fan_out` | neurons per inner hair cell | **5–30** | the Outputs field |
  | `type_II_fan_in` | outer hair cells per neuron | **~12** | the Outputs field |
  | `type_II_fan_out` | — | branches onto roughly a dozen | the Outputs field |
  | `tube_length` | mm | **~35** | the Shape field |
  | `inner_hair_cells` | count | **~3,500** | the Shape field |
  | `outer_hair_cells` | count | **~12,000** | the Shape field |
  | `spiral_ganglion` | count | **~30,000–35,000** | the Shape field |
  | `amplifier_gain` | dB | **40–60**, as the loss when it is abolished | the Justification field |
  | `endocochlear_potential` | volts | **to derive** — named as a standing positive voltage, no figure | the Function field |

  **This is the densest parameter set in either of the first two sections**, and the reason is that the
  organ is peripheral and measurable in a way cortex is not.
- **Update equation.** **Waiting on the emission question (§10)**, and on a second thing this entry
  raises alone: **how a graded receptor potential with no spike is expressed at all.** Three of this
  structure's five cell populations are in that class.
- **State carried between updates.** The four state arrays above. **The mechanical amplifier loop
  closes inside the structure and cannot be staged**, so outer-hair-cell force is read back into the
  travelling wave within one update — an ordering fixed by the loop and not by a clock. The
  olivocochlear gain command is written before the transduction it sets, for the same reason. Initial
  values: to derive, **except that the endocochlear potential is standing rather than initialised to
  rest** — it is supplied by the structure whether or not a stimulus is present.
- **Edge storage.** 3 input edges, 2 output edges, plus 1 internal mechanical loop that is not a
  projection. Line count on the type I output is **~30,000 fibres, measured**, which makes it one of
  the few line counts in either section that is a number rather than a placeholder. Latency to derive on
  all. Interval unset.
- **Adaptation.** **None set.** Note that **olivocochlear gain is not adaptation** — it changes the
  response and not a stored parameter, and folding it into a learning rule would be a category error.
  The same holds for the acoustic reflex's attenuation.
- **Open, beyond the standing list.** What a hair cell stores, across ~15,500 cells; the endocochlear
  potential's value; how the mechanical frequency analysis is modelled at all; the afferent half of the
  acoustic reflex, **written at neither end** — this entry's producer names an arc rather than a
  nucleus, and `15_cranial_nerve_nuclei` declares no auditory input of any kind. **That gap is
  inherited and is repaired at the source, not here.**

---

# 2. Cochlear nucleus

## Contract

**Inputs.**
- **← cochlea**, auditory nerve, ~30,000 fibres, tonotopic — **one edge terminating in three places.**
  Fan-in: **one or two** onto the spherical bushy cell, by axosomatic endbulb of Held, and little else;
  unknown for the other classes.
- **← dorsal column nuclei and trigeminal relay** → the dorsal division, by way of the granule cells —
  somatosensory state of head, face, neck and pinna, for cancelling self-generated sound. Fan-in: to
  derive.
- **← semicircular canals, otolith organs and vestibular nuclei** → the dorsal division, same
  granule-cell route — head rotation rate and gravito-inertial acceleration. Fan-in: to derive.
- **← primary auditory cortex and inferior colliculus** (descending) — gain and expectation, no new
  stimulus content. Fan-in: to derive.
- **← superior olivary complex**, glycinergic — inhibition, no content. Fan-in: to derive.

**Outputs.**
- **→ superior olivary complex**, from **bushy cells** — the spectral vector with sub-millisecond
  arrival timing preserved, monaural, one per ear. **Not itself a localisation signal**: it is what the
  differences are computed *from*. Three destinations differing in side and sign, not content —
  spherical bushy cells to the medial superior olive bilaterally and the lateral superior olive
  ipsilaterally, globular bushy cells to the medial nucleus of the trapezoid body contralaterally.
  Fan-out: to derive.
- **→ inferior colliculus**, from **T-stellate cells** — the spectrum, rate-coded per band, timing not
  preserved. Fan-out: to derive.
- **→ inferior colliculus**, from **octopus cells** — broadband onset, a coincidence event marking a
  transient. Fan-out: to derive.
- **→ inferior colliculus**, from **fusiform cells** — monaural spectral-notch cues for elevation, with
  the self-motion signal already subtracted. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~0.5M neurons, soft — no clean human count, and the source notes
this is a gap in what has been *counted* rather than in what has been sectioned. Fan-in to derive for
most classes, bounded ≤ 16 bits → **≤ 1.00 MB.**
**The spherical bushy cell is the exception and it costs 1 bit**: a fan-in of one or two gives log₂(2)
= 1. **The structure's most timing-critical cell is its cheapest.**

**Shape.** **Rank 3: (division, cell class, position along the tonotopic axis)** — three divisions,
**each holding a complete tonotopic map, so three maps of frequency per side rather than one.** The
cell-class axis is the labelled-line structure: spherical and globular bushy, T- and D-stellate,
octopus, fusiform, plus the dorsal interneurons. Extents: ~0.5M neurons total, **partition across
divisions and classes to derive.** **And the division axis may not be indexable in a human** — the
ventral cell classes lie intermixed within the cochlear nerve branches, so the boundary that defines the
sub-elements may not be drawable.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← cochlea, auditory nerve | energy per narrow band as a function of time; **waveform timing is part of the payload** at low frequencies | to derive | event-driven | tonotopic, rank 1, monaural |
| ← dorsal column nuclei and trigeminal relay → dorsal division | **somatosensory state of head, face, neck and pinna** | to derive | event-driven | **somatotopic — not tonotopic**; the correspondence to the tonotopic axis is unstated |
| ← semicircular canals, otolith organs, vestibular nuclei → dorsal division | **head rotation rate and gravito-inertial acceleration** | to derive | event-driven | **head-centred / gravito-inertial — not tonotopic**; correspondence unstated |
| ← primary auditory cortex and inferior colliculus (descending) | **gain and expectation — no new stimulus content** | to derive | event-driven | tonotopic, in register |
| ← superior olivary complex, glycinergic | **inhibition — no content** | to derive | event-driven | tonotopic |
| → superior olivary complex, from bushy cells | the spectral vector with **sub-millisecond arrival timing preserved**, monaural | to derive | event-driven | tonotopic, monaural, **one per ear** |
| → inferior colliculus, from T-stellate | the spectrum, **rate-coded per band, timing not preserved** | to derive | event-driven | tonotopic |
| → inferior colliculus, from octopus | **broadband onset — a coincidence event marking a transient** | to derive | event-driven | **broadband: across the tonotopic array rather than at a position on it** |
| → inferior colliculus, from fusiform | **monaural spectral-notch cues for elevation**, self-motion already subtracted | to derive | event-driven | tonotopic, **and it encodes elevation** |

**Two input rows arrive in a frame the structure does not use, and neither end supplies a
correspondence.** Somatosensory and vestibular signals land on the dorsal division by the granule-cell
route, and the axis they are indexed on is not the tonotopic one. **This is the same class of gap as the
auditory-parabelt edge into secondary visual cortex in `01_visual_pathway`, and it is owed at the
source for the same reason:** a signal cannot be subtracted from another signal until the two are on one
axis, and self-motion cancellation is exactly a subtraction.

**The octopus row does not have a tonotopic position and every other auditory row does.** Its payload is
coincidence *across* the array, so its output is indexed by time rather than by place. **An array laid
out on the tonotopic axis has nowhere to put it.**

**Timing is preserved on one output and discarded on another, from the same input.** The bushy line
carries sub-millisecond arrival timing; the T-stellate line is rate-coded with timing not preserved.
**So the representation differs between two readings of one signal**, which is what a labelled line
means at this rung.

## Algorithm

- **Transform.** **Parallel labelled lines — each cell class a different message on a different wire.
  And the lines are not parallel processing of different inputs; they are different readings of the
  same input.** Every auditory nerve fibre bifurcates on entry and reaches **all three divisions**, so
  what differs between the lines is the **terminal type and the receiving cell's intrinsic properties**,
  not the source.
  **This is the structural claim the code must not lose.** An implementation that routes different
  inputs to different cell classes has built a demultiplexer, and the structure is not one: it is one
  input read several ways at once. **No standard operation is named above for any of the readings**, and
  none is invented here.
- **The readings, named:** spherical and globular **bushy** cells — timing; **T-stellate** — spectrum;
  **octopus** — broadband onset by coincidence; **fusiform** — monaural spectral-notch elevation cues;
  plus inhibitory **D-stellate** and the dorsal interneurons.
- **Timing fidelity is bought by synapse morphology rather than by circuitry**, and the arithmetic must
  not substitute the one for the other. The **endbulb of Held** is axosomatic and gives the spherical
  bushy cell a fan-in of **one or two and little else**; **a stage that averaged many afferents could
  not do it.** The terminal is large enough to generate an extracellular prepotential before the
  receiving cell's own spike, and the jitter between the two is exceptionally low. **A model that
  reaches the same timing by averaging more inputs has inverted the mechanism.**
- **The octopus cell detects coincidence across the tonotopic array at the highest temporal precision
  in the brain**, which makes **the spread across its afferents the computation** rather than a
  property of it. This is the per-edge-latency invariant instantiated: with every afferent latency set
  equal, the spread is zero and the cell computes nothing.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (division=3, cell_class, tonotopic position) rank 3 | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive per class, bounded 16 | 0 … fan_in | count of active inputs |
  | `spherical_bushy_threshold` | (position,) | **1 bit** = `ceil(log₂(2))` | 0 … 2 | count of active inputs |

  **The division axis may not be indexable in a human**, and this is a defect in the addressing scheme
  rather than in the array. The ventral cell classes lie **intermixed within the cochlear nerve
  branches**, so the boundary defining the sub-elements may not be drawable — which makes "onto the
  anteroventral division" a checkable endpoint in a cat and possibly not in us. **Recorded, not
  resolved: an array indexed on a boundary that cannot be drawn asserts a partition the tissue may not
  have.**
  **Three complete tonotopic maps per side, not one.** Each division holds a full map, so the tonotopic
  extent is repeated three times rather than divided three ways.
  **The ~0.5M count partitions across neither divisions nor classes**, both to derive, so no per-class
  array can be sized — including the 1-bit one, whose *width* is known and whose *length* is not.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `spherical_bushy_fan_in` | inputs per cell | **1–2**, by axosomatic endbulb of Held | the Inputs field — measured |
  | `auditory_nerve_fibres` | count | **~30,000** | the Inputs field |
  | `divisions` | count | **3**, each with a complete tonotopic map | the Shape field |
  | `neurons` | count | **~0.5M, soft** — no clean human count | the Sizing field |
  | fan-in, all other classes | — | **unknown** | the Sizing field |

  **`unknown` above is not `to derive`.** The architecture says the count is a gap in what has been
  *counted* rather than in what has been sectioned — the structure has been looked at and the number has
  not been taken. Copying that state rather than translating it is the difference between an experiment
  to run and a derivation to perform.
- **Update equation.** **Waiting on the emission question (§10)**, and on a second thing: **how
  coincidence detection is expressed.** The octopus cell's computation is over the *spread* of arrival
  times across its afferents, and a count of active inputs over a threshold has no term for spread.
- **State carried between updates.** `active` at (3, cell_class, position). The descending edges from
  cortex, colliculus and olive **all close loops through structures present in this section**, so none
  can be staged. Initial values: to derive.
- **Edge storage.** 5 input edges, 4 output edges — **and the first input edge terminates in three
  places**, so the edge count under-reports the line count. Line count = ~30,000 fibres × 3 divisions on
  the afferent side, and to derive elsewhere. Latency to derive on all nine. Interval unset.
- **Adaptation.** **None set.** Note that **self-generated sound cancellation is not adaptation** if it
  is a subtraction of a concurrent signal; whether anything here stores a changing parameter is not
  stated above.
- **Open, beyond the standing list.** The partition of ~0.5M across three divisions and seven-plus cell
  classes; whether the division axis is indexable in a human at all; the frame correspondence the
  somatosensory and vestibular inputs need before a subtraction can be written; how coincidence over
  arrival-time spread is expressed.
  **And a species caution the architecture insists on, which lands on the arrays above rather than on
  the prose.** The two-domain fusiform cell and the cerebellum-like granule / parallel-fibre / cartwheel
  circuit carrying the self-motion cancellation are **cat and rodent anatomy that human material has not
  confirmed and in part contradicts**: the granule domain is decreased or absent in primates, human
  dorsal division shows **two layers rather than three** with no inhibitory interneurons labelled, and
  fusiform cells are reported as clustered or absent. **The somatosensory and vestibular inputs are
  independently attested, so something receives them; what, in a human, is to derive.** An array with a
  fusiform class and a three-layer dorsal division would encode the non-human reading. **Inherited, and
  repaired at the source rather than here.**

---

# 3. Superior olivary complex

## Contract

**Inputs.**
- **← cochlear nucleus, spherical bushy cells, bilaterally** → **medial superior olive** — the
  phase-locked spectral vector from **both** ears. **This edge's payload is a pair and the pairing is
  the point**: neither copy carries azimuth, and the difference is not taken until it arrives. Fan-in:
  to derive.
- **← cochlear nucleus, globular bushy cells, contralateral** → **medial nucleus of the trapezoid
  body** — the same vector, which that nucleus then sign-inverts. **Fan-in: one** — the calyx of Held
  is a one-to-one giant terminal.
- **← cochlear nucleus, spherical bushy cells, ipsilateral** → **lateral superior olive** — the same
  monaural vector as excitation, uninverted; the positive term of the subtraction. Fan-in: to derive.
- **← primary auditory cortex and inferior colliculus** (descending). Fan-in: to derive.

**Outputs.**
- **→ inferior colliculus**, lateral lemniscus, bilaterally — **horizontal sound location (azimuth).**
  **This is the edge where timing stops being the payload and azimuth starts being it.** Elevation is
  not on it. **What form azimuth takes on this wire is contested, and the architecture must not assume
  a place code.** Fan-out: to derive.
- **→ cochlea**, medial olivocochlear efferents onto the outer hair cells — a gain command. Fan-out: to
  derive.
- **→ cochlear nucleus**, glycinergic, descending — inhibition. Fan-out: to derive.
- **→ the acoustic-reflex arc** (stapedius) — a loudness-triggered attenuation command; the effector is
  outside scope. Fan-out: to derive.
  **This endpoint names a circuit and not a structure, and the structure it should name has an entry.**
  The arc runs through the **facial motor nucleus**, a named sub-element of `15_cranial_nerve_nuclei`'s
  branchiomotor and visceromotor entry — **the one structure in that section with a firm human count,
  ~10,000 per side, corroborated against the myelinated-axon count of its own nerve.** That entry
  declares the efferent limb to stapedius and **declares no auditory input at all**, so this edge has a
  producer here and no consumer there.
  **The failure is in the endpoint's kind rather than in its spelling.** *The acoustic-reflex arc* is a
  route; a route cannot declare an input back, so no diff at either end can pair this edge, and it
  reads as terminating outside scope when in fact its next stage is a counted nucleus two files away.
  **An endpoint naming a loop hides a structure the same way a class endpoint hides a member**, and it
  is worse in one respect: a class is visibly unresolved, while an arc reads as a complete description.
  **Owed at the source: retype this endpoint to the facial motor nucleus**, keeping stapedius as the
  terminus beyond it — or establish that the drive reaches the muscle by a route that does not pass
  through that pool. **Not retyped here**, because changing an endpoint at this rung re-terminates an
  edge the source still carries as written.

**Sizing.** Basis: **per side.** **Medial superior olive ~15,500 and lateral superior olive ~5,600** —
firm human unbiased stereology, among the few in the auditory brainstem. Fan-in to derive, bounded ≤ 16
bits → **~0.031 MB and ~0.011 MB.**
- **The medial nucleus of the trapezoid body carries no count**, because its existence in human is
  disputed, and its principal cell's **fan-in is one, which costs zero bits** — so even a firm count
  would add nothing to the parameter store.
- Periolivary groups: uncounted. **Structure total: ~0.042 MB stated, and the two structures doing the
  localisation arithmetic are together smaller than a rounding error against any cortical area in this
  section.**

**Shape.** **Rank 2 per nucleus: (nucleus, position along the tonotopic axis)**, and the medial superior
olive's own geometry is explicit — its somata lie in **a thin sagittal sheet** with the two dendrites
extending in opposite directions, so the structure is a sheet one cell thick with the binaural
comparison across its thickness. Extents measured: **~15,500** medial superior olive and **~5,600**
lateral superior olive per side. Trapezoid body and periolivary groups: **to derive**, and for the
medial nucleus of the trapezoid body the count is disputed rather than merely absent.

**Edge latency.** All edges **to derive** — and this is the structure where that is most costly.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← cochlear nucleus, spherical bushy, **bilaterally** → medial superior olive | the phase-locked spectral vector from **both** ears; **the payload is a pair** | to derive | event-driven | tonotopic, **one copy per ear, and neither carries azimuth** |
| ← cochlear nucleus, globular bushy, contralateral → medial nucleus of the trapezoid body | the same vector, **to be sign-inverted** | to derive | event-driven | tonotopic, monaural |
| ← cochlear nucleus, spherical bushy, ipsilateral → lateral superior olive | the same monaural vector **as excitation, uninverted** | to derive | event-driven | tonotopic, monaural |
| ← primary auditory cortex and inferior colliculus (descending) | to derive | to derive | event-driven | tonotopic, in register |
| → inferior colliculus, lateral lemniscus, bilaterally | **horizontal sound location (azimuth). Elevation is not on it** | **contested — see Parameters** | event-driven | **azimuth, and the form is decoded and disputed** |
| → cochlea, medial olivocochlear → outer hair cells | **gain command — no stimulus content** | to derive | event-driven | tonotopic position |
| → cochlear nucleus, glycinergic, descending | **inhibition — no content** | to derive | event-driven | tonotopic |
| → the acoustic-reflex arc (stapedius) | **a loudness-triggered attenuation command** | to derive | event-driven | **none — a scalar** |

**Three input rows carry the same payload and differ only in side and sign, and that is the whole
computation.** The architecture says it directly at the cochlear nucleus: the bushy output is **not
itself a localisation signal — it is what the differences are computed from.** So a consumer that reads
the three rows as three signals has lost the structure; they are one signal delivered three ways.

**The output row is the one place in either section where the representation is *contested* rather than
*to derive*.** It has been measured and the readings disagree. Every other open row in these two files
is open because nobody has supplied it.

## Algorithm

- **Transform.** Two arithmetic operations, on two nuclei, and **only the second has a name that
  survives contact with the architecture**:
  1. **Interaural time difference, by coincidence detection**, in the medial superior olive — on a
     **bipolar cell whose two dendrites point in opposite directions**, ipsilateral excitation on one,
     contralateral on the other, **so one cell's two inputs are segregated by compartment and the
     geometry is the computation.**
  2. **Interaural level difference, as a subtraction**, in the lateral superior olive: ipsilateral
     excitation against contralateral inhibition, sign-inverted through the medial nucleus of the
     trapezoid body, whose cells are driven by the giant **calyx of Held.**
- **The geometry is the computation, and an array cannot hold it.** A bipolar cell with two dendrites
  pointing opposite ways is a **two-compartment** cell whose compartments are separately addressed by
  separate afferents. **A single scalar activation per cell erases the compartment distinction and
  with it the mechanism** — the two inputs would sum before the comparison rather than being compared.
  This is the sharpest case in either section of a structural fact that the ordinary array shape cannot
  express, and it is recorded rather than worked around.
- **The coincidence detector's tuning is manufactured by timed glycinergic inhibition, not by a
  difference in axonal path length.** Blocking the inhibition shifts a cell's best interaural time
  difference toward zero. **That inverts the classical delay-line account**, and it means **the
  inhibitory internal edges are functional, not modulatory** — an implementation that treats inhibition
  here as a gain term has deleted the thing that sets the tuning.
- **Fan-in of one, twice, and both times it is load-bearing.** The calyx of Held is a **one-to-one giant
  terminal**, so the trapezoid body's principal cell stores **zero bits** — the same derivation as the
  type I spiral ganglion neuron in entry 1. **A giant one-to-one terminal is how a sign inversion is
  bought without adding jitter**, and averaging afferents to reach the same inversion would invert the
  mechanism.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `mso_active` | (~15,500,) rank 1 along the tonotopic axis | open — emission question | to derive | to derive |
  | `mso_threshold` | (~15,500,) | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |
  | `mso_dendrite_ipsi` / `mso_dendrite_contra` | **required by the mechanism and not writable** | — | — | — |
  | `lso_active` | (~5,600,) rank 1 | open | to derive | to derive |
  | `lso_threshold` | (~5,600,) | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |
  | `mntb_active` | **extent to derive, and disputed rather than absent** | open | to derive | to derive |
  | `mntb_threshold` | — | **absent by derivation** — fan-in is one, log₂(1) = 0 | — | — |
  | periolivary groups | **uncounted** | — | — | — |

  **Two extents here are measured**, which with entry 1 makes three structures in this file whose arrays
  could be sized today. **Rank 2 per nucleus and rank 1 within one** — position along the tonotopic
  axis, as everywhere in this section.
  **The medial superior olive is a sheet one cell thick with the binaural comparison across its
  thickness.** Its somata lie in a thin sagittal sheet with the two dendrites extending in opposite
  directions. **So the thickness is not an extent to allocate; it is where the comparison happens**, and
  an array with a thickness axis of length one has described the geometry without capturing it.
  **`mntb_threshold` is absent by derivation, and `mntb_active`'s extent is disputed rather than
  underived.** Those are two different open states on one nucleus and they do not collapse.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `mso_neurons` | count per side | **~15,500** — firm human unbiased stereology | the Sizing field |
  | `lso_neurons` | count per side | **~5,600** — firm, same source class | the Sizing field |
  | `mntb_fan_in` | inputs per principal cell | **exactly 1**, the calyx of Held | the Inputs field |
  | `mntb_neurons` | count | **disputed** — the nucleus's existence in human is disputed | the Sizing field |
  | `periolivary_neurons` | count | **uncounted** | the Sizing field |
  | `itd_scale` | seconds | **tens of microseconds** — qualitative, no figure | the structural invariants |
  | azimuth output format | — | **contested, three live readings** | the Justification field |

  **The output format is decoded and disputed, and that state is neither *to derive* nor settled.** Three
  readings are live: a **place code in a map of interaural delay** (verified in birds, and mammals
  evolved the computation independently); a **hemispheric opponent population rate code** read out by the
  slope of the response-azimuth function; and a **chinchilla result finding best delays clustered near
  zero and inside the physiological range.** **The architecture must not assume a place code** and this
  entry does not: no array above is indexed by azimuth. **Choosing among the three is a source decision
  and it is not made here.**
- **Update equation.** **Waiting on the emission question (§10)**, and on two things this entry raises
  alone. **How a two-compartment cell is expressed** — the medial superior olive's mechanism is
  compartmental segregation and nothing above names an operation over compartments. And **how a
  subtraction with a sign-inverting intermediate is expressed** when the intermediate's substrate is
  disputed in humans.
- **State carried between updates.** `mso_active`, `lso_active`, `mntb_active`. **Two descending loops
  close here** — the olivocochlear loop back to the cochlea and the glycinergic loop back to the
  cochlear nucleus — and both far ends are in this section, so neither can be staged. **The
  olivocochlear limb closes on the transducer itself**, which is the map's most complete descending
  loop: the brain sets the gain of its own front end before transduction. Initial values: to derive.
- **Edge storage.** 4 input edges, 4 output edges — **and the first input edge is bilateral**, so it is
  two lines rather than one and the edge count under-reports it. **The two bilateral lines are the same
  payload distinguished only by arrival time**, so an implementation that gave them equal latency would
  **delete the function rather than approximate it.** Line count to derive. Latency to derive on all
  eight. Interval unset.
- **Adaptation.** **None set.** **Olivocochlear gain and the acoustic reflex are not adaptation** — both
  change a response and not a stored parameter.
- **Open, beyond the standing list.** How a two-compartment cell is expressed at all; the azimuth output
  format, contested with three live readings; the acoustic-reflex endpoint's kind, **owed at the
  source** and not retyped here.
  **And a species caution wider than any other in this section, which lands on which arrays exist rather
  than on their contents.** This is the **least species-transferable structure in the pathway**, and the
  disagreement is **about which nuclei exist**: the medial superior olive is present in every human study
  examined; the lateral superior olive is called prominent by one group and **not consistently
  identifiable** by another; the medial nucleus of the trapezoid body is reported as well established by
  one line of work and as **vestigial or absent by four others.** **Every inhibitory internal edge in
  this structure originates there** — so if the human nucleus is absent, the sign-inverting term of the
  level computation and the timed inhibition that sets time-difference tuning arrive from somewhere else
  or work differently in us. **The edges are kept because the function is attested in human
  psychophysics; the substrate is recorded as disputed.** Inherited, and repaired at the source.

---

# 4. Inferior colliculus

## Contract

**Inputs.**
- **← cochlear nucleus** (T-stellate, octopus and fusiform cells, lateral lemniscus) → central nucleus —
  spectrum, broadband onset, and monaural elevation cues. Fan-in: to derive.
- **← superior olivary complex**, bilateral → central nucleus — azimuth. **A consumer of this edge must
  not assume a map.** Fan-in: to derive.
- **← nuclei of the lateral lemniscus**, bilaterally → central nucleus. **These have no entry anywhere
  in the source, so this edge terminates at a structure the description does not describe** —
  inherited, and not repaired at this rung. Fan-in: to derive.
- **← primary auditory cortex** (heavy descending), terminating **mainly in the dorsal and external
  cortices, not the central nucleus** — gain and expectation. Fan-in: to derive.
- **← contralateral inferior colliculus** (commissural). Fan-in: to derive.

**Outputs.**
- **→ medial geniculate nucleus, ventral division** (brachium), from the central nucleus — the assembled
  auditory scene: tonotopic spectrum, periodicity and duration tuning, and the binaural cues bound with
  the monaural elevation cue. **A named majority source class**: cholecystokinin disc-shaped neurons,
  ~63% of the excitatory population, projecting exclusively to that division. Fan-out: to derive.
- **→ medial geniculate nucleus, dorsal and medial divisions**, from the dorsal and external cortices —
  the non-lemniscal, broadly tuned signal. Fan-out: to derive.
- **→ contralateral inferior colliculus** (commissural). Fan-out: to derive.
- **→ superior colliculus** — auditory azimuth and elevation in a frame the orienting map can register
  against the visual one. Fan-out: to derive.
- **→ superior olivary complex and cochlear nucleus** (descending). Fan-out: to derive.

**Sizing.** Basis: **per side.** **Central nucleus ~420,000 neurons in ~22.4 mm³** — verified human
primary measurement, one of the firmest figures in the section. Whole colliculus with the dorsal and
external cortices ~0.6M. Fan-in to derive, bounded ≤ 16 bits → **≤ 1.20 MB.**
**Density cross-check, recomputed: ~420,000 / 22.4 mm³ ≈ 18,750 neurons/mm³** — consistent with the
loose packing of subcortical relays and far below cortical density.

**Shape.** **Laminated nucleus**, rank 3: **(division, lamina, position within lamina)** — three
divisions, and the central nucleus built of **10–12 fibrodendritic laminae each an isofrequency plane**,
so **the tonotopic axis runs across the laminae** and each lamina is one frequency band. **This
structure's partition is derivable and closes**: ~420,000 central-nucleus neurons over 10–12 laminae is
**~35,000 to ~42,000 per lamina**, in ~22.4 mm³ at **~18,750 neurons/mm³**. **The lamina axis is the
frequency axis** — which is what makes the shape and the map the same thing here.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← cochlear nucleus (T-stellate, octopus, fusiform) → central nucleus | spectrum, broadband onset, **monaural elevation cues** | to derive | event-driven | tonotopic — **and the octopus limb is broadband, indexed by time not place** |
| ← superior olivary complex, bilateral → central nucleus | **azimuth** | **contested at the producer** | event-driven | **azimuth. A consumer of this edge must not assume a map** |
| ← nuclei of the lateral lemniscus, bilaterally → central nucleus | to derive | to derive | event-driven | to derive |
| ← primary auditory cortex (heavy descending) → **dorsal and external cortices** | **gain and expectation — no new stimulus content** | to derive | event-driven | tonotopic, in register |
| ← contralateral inferior colliculus (commissural) | to derive | to derive | event-driven | tonotopic, **the far side's** |
| → medial geniculate, ventral division | the assembled auditory scene: tonotopic spectrum, periodicity and duration tuning, **binaural cues bound with the monaural elevation cue** | to derive | event-driven | tonotopic |
| → medial geniculate, dorsal and medial divisions | the non-lemniscal, **broadly tuned** signal | to derive | event-driven | **non-tonotopic** |
| → superior colliculus | **auditory azimuth and elevation in a frame the orienting map can register against the visual one** | to derive | event-driven | **an orienting frame, registrable against a retinotopic one** |
| → contralateral inferior colliculus (commissural) | to derive | to derive | event-driven | tonotopic |
| → superior olivary complex and cochlear nucleus (descending) | to derive | to derive | event-driven | tonotopic |

**The superior colliculus row is the one line in this section that is explicitly built to be registered
against another modality's frame**, and it names the requirement without supplying the correspondence.
The visual side of that registration is in `01_visual_pathway`, whose collicular edges arrive
retinotopically. **Neither end states the transform between an auditory azimuth-and-elevation frame and
a retinotopic one.**

**Azimuth arrives here in a format its producer records as contested**, and the instruction travels with
it: *a consumer of this edge must not assume a map.* **No array below is indexed by azimuth.**

## Algorithm

- **Transform.** **The obligatory hub — every ascending auditory line passes through it.** And the
  architecture draws a distinction here that governs what may be built: **obligatory is right; summed is
  not established.** Terminals from the different ascending pathways are **interleaved in different
  sublaminae and remain functionally segregated at this level**, so the lines all arrive and arrive in a
  shared tonotopic frame — **whether they are combined here or merely brought into register is not
  settled by the anatomy.**
  **So the parallel structure the cochlear nucleus creates may survive this stage**, and an
  implementation that sums the ascending lines on arrival has chosen the unsettled reading. **No
  combination is written here.**
- **Morphology does not predict sign**, which is unlike the rest of this section. Cell classes by
  dendrite: **disc-shaped**, confined to one lamina, and **stellate**, crossing two or more — and
  **both classes can be glutamatergic or glycinergic/GABAergic.** An implementation that assigns sign
  by cell class has imported a rule this structure breaks.
- **Across frequency bands the only stated route is the translaminar stellate cell**, so **any
  across-frequency integration here must take it.** That is a positive constraint on the topology rather
  than an absence: the lamina axis is the frequency axis, disc-shaped cells stay within a lamina, and the
  stellate cell is the only declared crossing.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `central_active` | (lamina=10–12, position within lamina) rank 2 | open — emission question | to derive | to derive |
  | `central_threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |
  | `dorsal_active` / `external_active` | extents **to derive** | open | to derive | to derive |

  **This structure's partition is derivable and closes**, which makes it the second in this file after
  the geniculate laminae of `01_visual_pathway` of which that is true: ~420,000 over 10–12 laminae is
  **~35,000 to ~42,000 per lamina**, and ~420,000 in ~22.4 mm³ recomputes to **~18,750 neurons/mm³.**
  **The lamina axis is the frequency axis.** The shape and the map are the same object here, so unlike
  every cortical entry in these two files, **the tonotopic index does not need a separate correspondence
  rule** — it is the array index.
  **The whole-colliculus figure of ~0.6M against the central nucleus's ~420,000 leaves ~180,000 across
  the dorsal and external cortices**, and the architecture does not divide that between them, so those
  two arrays cannot be sized separately.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `central_neurons` | count per side | **~420,000** — verified human primary measurement | the Sizing field |
  | `central_volume` | mm³ | **~22.4** — verified | the Sizing field |
  | `central_density` | neurons/mm³ | **~18,750** — recomputed and consistent | derived, and closing |
  | `laminae` | count | **10–12**, each an isofrequency plane | the Shape field |
  | `per_lamina` | count | **~35,000–42,000** | derived from the two above |
  | `whole_colliculus` | count per side | **~0.6M** | the Sizing field |
  | `cck_disc_fraction` | fraction of the excitatory population | **~63%**, projecting **exclusively** to the geniculate ventral division | the Outputs field |

  **The cholecystokinin disc-shaped fraction is the only named majority source class on any edge in
  either of these two files**, and it is a fact about the topology rather than about the store: it says
  which cells carry one output edge, not what any cell holds.
- **Update equation.** **Waiting on the emission question (§10)**, and on the combined-versus-register
  question above, which is not this rung's to settle.
- **State carried between updates.** `central_active`, `dorsal_active`, `external_active`.
  **Co-instantiation is obligatory by construction here** — no ascending auditory line reaches the
  thalamus without this structure, so it cannot be a later addition. The commissural edge closes a loop
  with the contralateral copy of this same structure, which the per-side basis makes a second instance
  rather than a far structure. Initial values: to derive.
- **Edge storage.** 5 input edges, 5 output edges — **two of them bilateral and one commissural**, so the
  line count exceeds the edge count. Line count to derive. Latency to derive on all ten. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** Whether the ascending lines are combined here or only brought into
  register; the division of ~180,000 between the dorsal and external cortices; the frame correspondence
  the superior colliculus edge needs against a retinotopic map.
  **Two inherited gaps, neither repairable here.** The **nuclei of the lateral lemniscus have no entry
  anywhere in the source**, so an input edge terminates at a structure the description does not describe.
  And the **auditory space map attributed to this structure is barn-owl anatomy**, in the owl's
  *external* nucleus, with a single mammalian report in guinea pig and none in human — **recorded as
  contested and mis-sited rather than carried.** No array here is indexed by auditory space.

---

# 5. Medial geniculate nucleus

## Contract

**Inputs.**
- **← inferior colliculus** (brachium) → principally the ventral division — the assembled auditory
  scene; the **driver**, and a minority of the synapses. **Roughly 20% of that collicular input is
  GABAergic** to the ventral and medial divisions, ~11% to the dorsal — **so the edge that sets what the
  message is also carries a substantial inhibitory component**, and a stage modelling it as pure
  excitatory drive would be wrong about a fifth of it. Itself **three parallel pathways** — lemniscal,
  polysensory, diffuse — terminating preferentially in the ventral, medial and dorsal divisions. Fan-in:
  to derive.
- **← primary auditory cortex, layer 6** (small terminals), reaching **all three divisions** —
  modulatory, no new content. Fan-in: to derive.
- **← primary auditory cortex, layer 5** (giant terminals) → **dorsal and medial divisions** —
  **cortical content, as a driver.** Giant terminals are the signature of a driver, and this is what
  makes those two divisions higher-order. Fan-in: to derive.
- **← thalamic reticular nucleus** — inhibition, the gate; and that nucleus's auditory sector is itself
  layered by relay class, **so the gate is applied separately to the first-order and higher-order
  relays.** Fan-in: to derive.

**Outputs.**
- **→ primary auditory cortex**, from the **ventral division** — the lemniscal payload, sharply
  tonotopic, relayed and **gated, not transformed.** Fan-out: to derive.
- **→ auditory belt and parabelt**, from the **dorsal division** — the non-tonotopic, broadly tuned
  signal, **and on the higher-order limb, cortical content returning from layer 5.** Fan-out: to derive.
- **→ wide cortical targets and the amygdala**, from the **medial division** — a coarse, broadly tuned
  multisensory alarm signal: enough to say *something loud and sudden happened, roughly there*, and not
  enough to identify it. **The payload is impoverished by design, and that is what makes it fast.**
  Fan-out: to derive.
- **→ inferior colliculus** (descending), from the **medial division** and associated nuclei — with a
  specific negative alongside: **the ventral and dorsal divisions send no return projection to the
  colliculus**, so the descending limb does not mirror the ascending one. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~1.8–2.3M neurons, soft — no direct human count; bracketed by
comparability with the lateral geniculate nucleus's firm ~1.8M and by a volume cross-check at that
nucleus's ~17,000 neurons/mm³ against this one's verified ~134 mm³, which gives ~2.3M. Fan-in to derive,
bounded ≤ 16 bits → **≤ 4.10 MB** at 2.05M.
**A partition is available in principle and changes the output count, not the store:** if the primate
interneuron proportion holds, roughly a quarter of the total are local inhibitory cells that project
nowhere outside the nucleus and are therefore not part of the thalamocortical output.

**Shape.** **Laminated nucleus**, rank 3: **(division, lamina, position)** — three divisions, and the
ventral division's principal cells sitting in **rows about 50–100 µm wide** whose bi-tufted dendritic
fields form fibrodendritic laminae. **Row width is a measured pitch**, one of the few in the map. Neuron
count ~1.8–2.3M with the **division partition to derive**; the medial division admits **no further
subdivision at all**, so that axis is rank-1 by the description rather than by omission. **A quarter of
the total may be local interneurons that project nowhere**, which changes the output extent without
changing the array.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← inferior colliculus (brachium) → ventral division | the assembled auditory scene; **the driver, and ~20% of it GABAergic** | to derive | event-driven | tonotopic |
| ← primary auditory cortex, layer 6, small terminals → all three divisions | **modulatory — no new content** | to derive | event-driven | tonotopic, in register |
| ← primary auditory cortex, layer 5, giant terminals → dorsal and medial | **cortical content, as a driver** | to derive | event-driven | cortical, **not the ascending frame** |
| ← thalamic reticular nucleus | **inhibition — the gate, no content**, applied separately to first- and higher-order relays | to derive | event-driven | auditory sector of the reticular sheet |
| → primary auditory cortex, from ventral | the lemniscal payload, **relayed and gated, not transformed** | to derive | event-driven | **sharply tonotopic** |
| → auditory belt and parabelt, from dorsal | the broadly tuned signal, **and cortical content returning from layer 5** | to derive | event-driven | **non-tonotopic** |
| → wide cortical targets and the amygdala, from medial | **a coarse multisensory alarm: something loud and sudden happened, roughly there** | to derive | event-driven | **coarse and roughly spatial — not tonotopic** |
| → inferior colliculus (descending), from medial and associated nuclei | to derive | to derive | event-driven | to derive |

**One input edge is a driver and carries a fifth of itself as inhibition**, which no other driver row in
either file does. **Roughly 20% GABAergic to the ventral and medial divisions, ~11% to the dorsal** — so
a stage that models the collicular input as pure excitatory drive is wrong about a fifth of it. **The
sign is not a property of the edge; it is a mixture within the edge.**

**The medial division's row is impoverished on purpose and the representation must not enrich it.**
Enough to say something loud and sudden happened, roughly there, and not enough to identify it — **and
that is what makes it fast.** A consumer that reads it as a degraded copy of the ventral payload has
mistaken a design for a deficiency.

## Algorithm

- **Transform.** **Three divisions that differ in what drives them, not in flavour.** The **ventral
  division** is a **first-order** relay — driving input subcortical, from the inferior colliculus,
  **exactly as the lateral geniculate nucleus is driven by the retina** — tonotopic, sharply tuned, to
  the core. The **dorsal** and **medial** divisions are substantially **higher-order** relays: their
  driving input is **layer 5 of auditory cortex**, so they carry cortical output back into the thalamus
  and out to another cortical area — **a transthalamic route between cortical areas rather than a stage
  on the way up from the ear.**
  **This is the structural claim the code must not lose.** An implementation that treats all three
  divisions as stages on the ascending path has built a relay where two-thirds of the structure is a
  cortico-cortical bypass.
- **Giant terminals are the signature of a driver**, and the distinction is carried on the edge rather
  than inferred: layer 6 arrives by small terminals and is modulatory, layer 5 by giant terminals and is
  a driver. **Two edges from one structure, opposite in kind, distinguished by terminal morphology.**
- **The relay is gated, not transformed** on the lemniscal limb — the same claim the lateral geniculate
  nucleus carries in `01_visual_pathway`, and the same consequence: the transfer function changes and
  the message does not.
- **Third occurrence of one geometry in this section.** The medial superior olive's bipolar cell, the
  colliculus's disc-shaped cell, and this nucleus's **bi-tufted** principal cell **all build isofrequency
  sheets from cells whose dendrites lie in the plane of the sheet.** Three structures, one solution.
  **This is a fact about how tonotopy is physically realised**, and an array indexed on a tonotopic axis
  expresses the result without expressing the mechanism.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `ventral_active` | (lamina, position) — rows **50–100 µm** wide | open — emission question | to derive | to derive |
  | `dorsal_active` | (lamina, position) | open | to derive | to derive |
  | `medial_active` | (position,) — **rank 1 by description** | open | to derive | to derive |
  | `threshold` per division | matching | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |
  | `interneuron_state` | **extent to derive; ~25% of the total if the primate proportion holds** | **open, and not defaultable** | to derive | to derive |

  **The medial division admits no further subdivision at all**, so its axis is **rank 1 by the
  description rather than by omission** — the same positive statement as the absent threshold arrays in
  entries 1 and 3, and it must not be read as a gap.
  **Row width is a measured pitch, one of the few in the map**: 50–100 µm. **It is a pitch and not an
  extent** — it gives the spacing of the rows and not how many there are, so it constrains the lamina
  axis without sizing it.
  **A quarter of the total may be local interneurons that project nowhere outside the nucleus**, which
  **changes the output extent without changing the array.** Parameter store is unaffected; the count of
  lines leaving is not.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count per hemisphere | **~1.8–2.3M, soft** — no direct human count | the Sizing field |
  | `volume` | mm³ | **~134**, verified | the Sizing field |
  | `density_basis` | neurons/mm³ | **~17,000**, borrowed from the lateral geniculate nucleus | the Sizing field |
  | `row_width` | µm | **50–100**, measured | the Shape field |
  | `collicular_gabaergic` | fraction of the driving edge | **~20%** ventral and medial, **~11%** dorsal | the Inputs field |
  | `interneuron_fraction` | fraction of the total | **~25%** if the primate proportion holds — **and see below** | the Sizing field |

  **The count is derived by two independent brackets that agree**, which is worth carrying: comparability
  with the lateral geniculate nucleus's firm ~1.8M, and a volume cross-check at ~17,000 neurons/mm³
  against ~134 mm³ giving ~2.3M. **Neither is a direct human count and the entry does not present them
  as one.**
- **Update equation.** **Waiting on the emission question (§10)**, and on **how an edge carrying a fixed
  proportion of inhibition within itself is expressed** — the collicular driver is not sign-uniform, and
  a count of active inputs has no term for a mixture.
- **State carried between updates.** The three divisional arrays and the interneuron state. **The
  layer-6 modulatory loop and the layer-5 driver loop both pass through cortex present in this section,
  and the reticular gate is a third. The higher-order divisions cannot function at all without their
  cortical driver**, so for them **co-instantiation is not a discipline but a precondition** — the dorsal
  and medial arrays have no input at all until auditory cortex is live. Initial values: to derive.
- **Edge storage.** 4 input edges, 4 output edges. **The first input edge is itself three parallel
  pathways** — lemniscal, polysensory, diffuse — terminating preferentially in the ventral, medial and
  dorsal divisions, so the edge count under-reports the line count by three. Line count to derive.
  Latency to derive on all eight. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The division partition of ~1.8–2.3M; how a mixed-sign driver edge
  is expressed; **internal edges are to derive throughout** — including whether this nucleus builds the
  **triadic glomerulus** its visual counterpart does, which the interneuron figures make answerable in
  primates and unanswerable in rodents.
  **And the sharpest species-transfer hazard in the pathway sits here, on a number the arrays above
  use.** The GABAergic local interneuron proportion runs from **under 1% in bat and rat — some divisions
  with none at all — to 25% or more in cat and monkey**, with primate thalamus generally 25–30%. **This
  is specific to the auditory thalamus**: the lateral geniculate nucleus holds about the same proportion
  across species, and so do the colliculus and auditory cortex. **Only this nucleus swings that way.** In
  rodent it has essentially no interneurons and its inhibition comes from the reticular nucleus alone; in
  cat, monkey and by extension human there are **two independent inhibitory systems.** **A circuit for
  this structure taken from mouse would be missing an entire population that is present in us.**
  Inherited, and repaired at the source.

---

# 6. Primary auditory cortex

## Contract

**Inputs.**
- **← medial geniculate nucleus, ventral division**, point-to-point → **layer 4** — the tonotopic
  spectrum with periodicity and duration tuning and the binaural cues bound with elevation. **A minority
  driver: ~20% of this area's excitatory input is thalamic, ~80% intracortical.** Fan-in: to derive.
- **← auditory belt** (descending), principally → **layer 1.** Fan-in: to derive.
- **← contralateral primary auditory cortex** (callosal), from **layers 3 and 5**, terminating
  throughout layers 2–6, densest in 2 and 3 and **sparsest in layer 4.** Fan-in: to derive.

**Outputs.**
- **→ auditory belt** — the spectrotemporal receptive-field code on a tonotopic map. **Left and right
  differ as a bias from here on** — left favouring finer temporal resolution, right finer spectral —
  **so the two hemispheres' payloads are no longer identical.** Fan-out: to derive.
- **→ auditory parabelt** — **weak but not absent**: injections confined to the parabelt label only few
  neurons here against large numbers in the belt. Recorded because *few is not none*, which matters for
  anything treating the three tiers as strictly serial. Fan-out: to derive, and small.
- **→ medial geniculate nucleus, from layer 6** (all three divisions), **and inferior colliculus**
  (mainly its dorsal and external cortices) — modulatory, no new content. Fan-out: to derive.
- **→ medial geniculate nucleus, dorsal and medial divisions, from layer 5** (giant terminals) —
  **cortical content as a driver.** The two corticofugal limbs leave from different layers and do
  different jobs. Fan-out: to derive.
- **→ contralateral primary auditory cortex** (callosal), from **layers 3 and 5.** Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~20M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 40.00
MB.** **The variability is not measurement noise** — Heschl's gyrus differs markedly between individuals
and between the two hemispheres of one brain, including in the number of transverse gyri present, with
a left>right volume asymmetry.

**Shape.** **Sheet**, rank 3: **(lamina, areal field, position along the tonotopic axis)** — eight
laminae, three human areal sub-elements in a medial-to-lateral sequence, ~20M neurons per hemisphere
with the partition **to derive**.
**The map axis cannot be labelled, and that blocks the shape rather than decorating it.** Four proposals
for the tonotopic gradient's orientation are on record — parallel to the gyrus, perpendicular, circular,
and high-low-high with an inverted V. **An axis whose direction is unknown cannot be indexed**, so this
structure has a rank and no orientation for its principal axis. The areal count is unsettled too: the
human core may be three fields or **one**.

**Edge latency.** All edges **to derive.** One gradient is recorded and is not a latency figure: response
latency **increases from posteromedial to anterolateral** along the gyrus, for tones and for isolated
syllables.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← medial geniculate, ventral, point-to-point → layer 4 | the tonotopic spectrum with periodicity and duration tuning and the binaural cues bound with elevation | to derive | event-driven | tonotopic — **and the axis orientation is disputed at this end** |
| ← auditory belt (descending) → layer 1 | to derive | to derive | event-driven | tonotopic, in register |
| ← contralateral primary auditory cortex (callosal), layers 3 and 5 → layers 2–6, sparsest in 4 | **a normalisation, not a message** | to derive | event-driven | **matched frequency bands, principally homotopic — not a seam** |
| → auditory belt | the spectrotemporal receptive-field code on a tonotopic map | to derive | event-driven | tonotopic, **and left/right payloads now differ as a bias** |
| → auditory parabelt | **weak but not absent** | to derive | event-driven | tonotopic |
| → medial geniculate, layer 6, all three divisions; → inferior colliculus, dorsal and external cortices | **modulatory — no new content** | to derive | event-driven | tonotopic, in register |
| → medial geniculate, dorsal and medial, layer 5, giant terminals | **cortical content as a driver** | to derive | event-driven | cortical, not the ascending frame |
| → contralateral primary auditory cortex (callosal), layers 3 and 5 | a normalisation | to derive | event-driven | matched frequency bands |

**This is where the two hemispheres stop carrying the same payload**, and the representation table is
where that has to be recorded, because nothing in the array shape shows it. **Left favours finer temporal
resolution, right finer spectral.** Every row above this one is hemisphere-symmetric; no row below it is.

**The callosal rows carry a normalisation and not a message, and this is stated once for the whole
auditory cortex.** Audition has **no representational midline to stitch**, unlike vision's vertical
meridian and somatosensation's proximal body, so its callosal connections are **widespread across the
entire tonotopic map rather than restricted to a seam — treating the auditory callosum as a seam would
be a category error.** It connects matched frequency bands, principally homotopically; it **avoids the
layer the thalamic driver targets**; it lands preferentially on the patchy **binaural columns** and not
on monaural regions; **every fibre is excitatory**, so its net inhibitory effect is feedforward through
local interneurons; and its measured consequences are **sharpened tuning and enforced signal-to-noise
ratio. A consumer treating it as a second copy of the other hemisphere's percept would be wrong about
what it does.**

## Algorithm

- **Transform.** **Spectrotemporal receptive fields**: frequency tuning, onset and offset,
  frequency-modulated sweep rate and direction, bandwidth, intensity, temporal modulation. **This is the
  auditory counterpart of V1's oriented-edge code — local features, not objects.** **No standard
  operation is named above**, and none is invented here; the parallel to V1 is a statement about the
  tier's role and not a licence to write V1's arithmetic in an auditory frame.
- **A minority driver, and the proportion is the finding.** ~20% of this area's excitatory input is
  thalamic and ~80% intracortical — the same shape as V1's, where the four geniculate edges are together
  a minority. **An implementation that drives this structure from the thalamic edge alone has built the
  fifth of it that arrives from below.**
- **The two corticofugal limbs leave from different layers and do different jobs.** Layer 6 to all three
  geniculate divisions and to the colliculus is **modulatory**; layer 5, by giant terminals, to the
  dorsal and medial divisions is **a driver carrying cortical content**. Same source structure, opposite
  kind, distinguished by lamina of origin and terminal morphology.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, areal_field=3, position along the tonotopic axis) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **The principal axis has a rank and no orientation, and that blocks the array rather than decorating
  it.** Four proposals for the tonotopic gradient's direction are on record — parallel to the gyrus,
  perpendicular, circular, high-low-high with an inverted V. **An axis whose direction is unknown cannot
  be indexed.** This is a different open state from every extent in entries 1–5: those are lengths not
  yet supplied, this is an axis that cannot be laid down at all. **A map is a spatial claim, and if the
  axis is unknown then "tonotopic" says frequency is ordered somehow, not what is where — which is less
  than a build needs.**
  **The areal_field extent of 3 is itself unsettled: the human core may be three fields or one.** So the
  second axis has a disputed length and the third has a disputed direction, and the ~20M count
  partitions across neither.
  **The variability is not measurement noise and it is not averageable.** Heschl's gyrus differs markedly
  between individuals and between the two hemispheres of one brain, **including in the number of
  transverse gyri present.** An array whose second axis is a count of gyri has assumed a number that
  varies within a single subject.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count per hemisphere | **~20M** | the Sizing field |
  | `thalamic_fraction` | fraction of excitatory input | **~20%**, against ~80% intracortical | the Inputs field |
  | `areal_fields` | count | **3 in the human parcellation, and possibly 1** | the Shape field |
  | `laminae` | count | **8**, layer 4 undivided but koniocortical | the Function field |
  | tonotopic axis orientation | — | **to derive — four proposals on record** | the Shape field |
  | latency gradient | — | **increases posteromedial → anterolateral**, qualitative | the Edge latency field |

  **The latency gradient is recorded and is not a latency figure**, and it must not be promoted into
  one. It says the order of arrival across the gyrus, for tones and for isolated syllables, and gives no
  interval.
- **Update equation.** **Waiting on the emission question (§10)**, and unwritable in any case while the
  principal axis has no orientation: a spectrotemporal receptive field is defined over frequency and
  time, and the frequency axis here cannot be laid down.
- **State carried between updates.** `active` at (8, 3, position). **Three loops close through this
  structure** — to the geniculate on two separate limbs, to the colliculus, and across the callosum —
  and all three far ends are in this section. **The callosal loop is what holds the hemispheric asymmetry
  in place:** callosotomy raises the right pole's activity and abolishes the left–right difference, **so
  lateralisation is a dynamic equilibrium maintained by an edge rather than a static division of
  labour.** An implementation that hard-codes the left/right bias as a property of each side, rather than
  letting it emerge from the callosal edge, has built the wrong mechanism. Initial values: to derive.
- **Edge storage.** 3 input edges, 5 output edges — **and two output lines each name multiple targets**,
  so the line count exceeds the edge count. Line count to derive. Latency to derive on all eight.
  Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The orientation of the tonotopic axis; the areal count, three or
  one; the partition of ~20M; the number of transverse gyri, which varies within a subject.
  **Two structural claims here are weaker than the tier's role suggests, and both bear on what can be
  built.** The **correspondence to the macaque core is not established**: human cytoarchitecture is
  consistent with three primary-like fields, functional imaging mostly finds two, and one reading treats
  Te1.1 and Te1.2 as medial junction and lateral belt rather than primary fields at all — which would
  make the human core **one** area. And the **tonotopic map's axis in human is disputed**, above.
  Inherited, and repaired at the source.

---

# 7. Auditory belt

## Contract

**Inputs.**
- **← primary auditory cortex** — the spectrotemporal feature code, tonotopic. Fan-in: to derive.
- **← medial geniculate nucleus, dorsal division** — the belt's **preferential** thalamic source, and the
  same division that is substantially higher-order, **so part of what arrives here is cortical output
  returning through the thalamus rather than a fresh ascending signal.** Fan-in: to derive.
- **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. **Denser here than at the
  core and less strictly area-to-area**, because association fields are more heavily callosally connected
  and carry proportionally more heterotopic traffic. Fan-in / fan-out: to derive.

**Outputs.**
- **→ auditory parabelt, rostral division**, from the **anterolateral** field — call and **identity**
  features; no location. Fan-out: to derive.
- **→ auditory parabelt, caudal division**, from the **caudolateral** field — **sound-source location
  (azimuth)**; not identity, and **not a map.** Fan-out: to derive.
- **→ auditory parabelt, both divisions**, from the **rostromedial** field of the medial belt — **a
  source that ignores the caudorostral split** the lateral belt observes, which makes it a different kind
  of input from one that honours it. Payload to derive. Fan-out: to derive.
- **→ prefrontal cortex, directly** (`11_frontal_lobe`), split by origin and kept split at the
  destination — the **anterior** belt to the frontal pole, rostral principal sulcus and ventral
  prefrontal areas; the **caudal** belt to the caudal principal sulcus and the **frontal eye field.**
  **The caudal target being the frontal eye field says plainly what the "where" payload is for: moving
  the eyes to the sound.** Fan-out: to derive.
  All three named prefrontal targets declare this edge at their end. Its frontopolar entry
  declares `← auditory association cortex — the anterior belt` onto its **medial** part; its
  ventrolateral prefrontal entry declares `← the anterior auditory belt, directly, onto areas 12 and
  45`; and its frontal eye field entry declares `← the caudal auditory belt, directly`.
  **The arity mismatch is at this end.** This is written as **one** output line naming three destinations
  in two groups, while the consumer writes **three separate inputs at three separate entries.** So the
  edge count differs across the boundary by two, and **the split is owed here rather than there — the
  consumer has already done it.**
  **One consumer-end fact this line does not carry, and it bears on the payload.** The frontopolar target
  is its **medial** part specifically, and that file records audition as **the principal external
  connection of that part** — more than 90% of the *lateral* part's afferents are frontal, while the
  medial surface takes substantial temporal input. **So this edge does not reach a supramodal area
  incidentally; it is the main input to the part it reaches.**
- **→ primary auditory cortex, medial geniculate nucleus and inferior colliculus** (corticofugal).
  Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~25M neurons for the belt as a whole. Fan-in to derive, bounded ≤
16 bits → **≤ 50.00 MB.** **No per-field partition exists**, and with eight fields named that is a
visible gap rather than an implicit one — **eight sub-structures sharing one count.**

**Shape.** **Sheet**, rank 3: **(lamina, field, position)** — eight laminae against **eight areal
fields**, four lateral and four medial, arranged as a ring around the core. **The field axis is not a
sequence**: each lateral field sits beside a core field and each medial field beside the same core field
on the other side, so the axis is indexed by relation to the core rather than by order. ~25M neurons with
**no per-field partition — eight sub-elements sharing one count.** Field borders are drawn at **tonotopic
reversals**, which means the map axis reverses at each boundary rather than running monotonically across
the structure.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← primary auditory cortex | the spectrotemporal feature code | to derive | event-driven | tonotopic, **reversing at each field border** |
| ← medial geniculate, dorsal division | **part of it is cortical output returning through the thalamus, not a fresh ascending signal** | to derive | event-driven | **non-tonotopic** |
| ↔ contralateral counterpart (callosal, reciprocal) | a normalisation, **denser than at the core and less strictly area-to-area** | to derive | event-driven | matched bands, **more heterotopic traffic than the core's** |
| → parabelt rostral, from anterolateral | **call and identity features; no location** | to derive | event-driven | **none — an identity class** |
| → parabelt caudal, from caudolateral | **sound-source location (azimuth)** | **the region of steepest change in the response-azimuth function — not the peak** | event-driven | **an opponent hemifield population rate code, and NOT a map** |
| → parabelt both, from rostromedial | to derive | to derive | event-driven | **ignores the caudorostral split the lateral belt observes** |
| → prefrontal cortex, directly (`11_frontal_lobe`), split anterior / caudal | identity features / location, **the caudal limb for moving the eyes to the sound** | to derive | event-driven | none / opponent rate code |
| → primary auditory cortex, medial geniculate, inferior colliculus (corticofugal) | to derive | to derive | event-driven | tonotopic |

**The location row is the strongest of this section's three map withdrawals and it binds every consumer
downstream.** The auditory cortex has been searched for a topographic map of auditory space and **none
has been found.** What is there is an **opponent hemifield population rate code**: two broadly tuned
populations, one preferring each hemifield, with location read from the **balance** between them. Two
properties bind a consumer: **location is carried by the region of steepest change in the
response-azimuth function, not by the peak** — a downstream stage looking for a maximum finds nothing
useful — and **it is robust to sound level, precisely because it is a slope code and not a peak code.**
Resolution is correspondingly coarse: reliable left-versus-right with confusion *within* a hemifield.

**The identity payload is neither "sound" nor "meaning" but a third thing**: the complex, call-like
spectrotemporal **class**, abstracted well above tones and noise and not yet organised by referent —
prefrontal responses cluster by acoustics rather than by referent, while pure tones scarcely drive those
cells at all.

## Algorithm

- **Transform.** **Nonlinear spectral and temporal integration** — tuning to noise bandwidth, to
  frequency-modulated sweep rate and direction, and to a limited set of species-specific vocalisations;
  broader tuning than the core, and **responding better to broad spectral stimuli than to pure tones.**
  **No standard operation is named above**, and none is invented here.
- **Tonotopy survives and only shows itself with the right probe**: with narrowband noise the best centre
  frequency varies systematically, **with reversals at the field borders, and those reversals are how the
  borders are drawn.** So the map axis and the field axis are not independent — **the field boundary is
  defined by a feature of the map**, which means an implementation cannot lay down the fields first and
  the map within them.
- **The field axis is not a sequence.** Each lateral field sits beside a core field and each medial field
  beside the same core field on the other side, **so the ring is organised by its relation to the core
  rather than as a sequence of its own.** An array whose field axis is ordered 0…7 has imposed an order
  the structure does not have; the index is a relation to a core field, and the core's own areal count is
  disputed at entry 6.
- **Layer 4 is present but less granular than the core's** — the signature of a field one step off the
  thalamic driver. The laminar axis is the same eight as the core's and the granularity differs.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, field=8, position) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **Eight sub-structures sharing one count**, and the architecture calls that a **visible gap rather than
  an implicit one.** ~25M over eight fields with no partition: no field can be sized, and the fields are
  not equal — the lateral and medial halves differ in what they carry.
  **The map axis reverses at each field boundary rather than running monotonically.** A single monotonic
  position index across the structure would be wrong at seven boundaries. **The position axis is
  per-field and the reversal is the boundary**, which is the same entanglement as above seen from the
  array side.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count per hemisphere | **~25M**, belt as a whole | the Sizing field |
  | `fields` | count | **8** — four lateral, four medial | the Shape field |
  | `field_partition` | — | **none exists** | the Sizing field |
  | azimuth code | — | **opponent hemifield population rate code; read at the slope, not the peak** | the Justification field |

- **Update equation.** **Waiting on the emission question (§10)**, and on how an **opponent population
  rate code read at its slope** is expressed — a count of active inputs over a threshold has no term for
  a balance between two populations, and none for a derivative.
- **State carried between updates.** `active` at (8, 8, position). Corticofugal loops to the core,
  thalamus and colliculus, plus the callosal loop; all far ends in this section. Initial values: to
  derive.
- **Edge storage.** 3 input edges, 5 output edges — **and the prefrontal line names three destinations
  while the consumer declares three separate inputs**, so the line count is three where the edge count is
  one, and the boundary disagrees by two. Line count otherwise to derive. Latency to derive on all eight.
  Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The per-field partition of ~25M; how a slope-read opponent code is
  expressed; the prefrontal line's arity, **owed here and already done at the consumer.**
  **And the eight fields are a macaque parcellation applied to human**: the human belt's internal
  boundaries are drawn by **extending the borders between adjacent core fields laterally**, inherited
  from the monkey model rather than measured, **while a large expanse of human lateral superior temporal
  cortex may have no clear monkey homologue at all.** The **medial belt** is poorly characterised in the
  literature and shows broad **spatial** tuning, so the "where" function may be distributed around the
  medial half of the ring — **to derive.** **The what/where split is supported and graded rather than
  clean**: belt-to-parabelt projections overlap, and the temporal-field connections of the two streams
  overlap more than the frontal ones do, **so the streams separate progressively rather than at a
  border.** An array with a clean two-stream partition would encode a border the anatomy denies.
  Inherited, and repaired at the source.

---

# 8. Auditory parabelt

## Contract

**Inputs.**
- **← anterolateral belt** → **rostral** division — call and identity features. Fan-in: to derive.
- **← caudolateral belt** → **caudal** division — location, as an opponent rate code. **The
  belt-to-parabelt connections are topographic in the caudorostral dimension**, which is what makes the
  two divisions two streams rather than two samples of one. Fan-in: to derive.
- **← rostromedial belt** → **both** divisions. Payload to derive. Fan-in: to derive.
- **← primary auditory cortex** — weak rather than absent. Fan-in: to derive, and small.
- **← medial geniculate nucleus, dorsal division** — the non-tonotopic thalamic signal, and **it cannot
  be what imposes a frequency map here**, since that division is not tonotopically organised. Fan-in: to
  derive.
- **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation, denser than at the core.
  Fan-in / fan-out: to derive.

**Outputs.**
- **→ anterior superior temporal gyrus and sulcus**, from the **rostral** division — sound-object
  identity, invariance-building. Fan-out: to derive.
- **→ posterior superior temporal gyrus and the Sylvian parieto-temporal area**, from the **caudal**
  division — location and motion. Fan-out: to derive.
- **→ the rostrally-directed stream** — temporal pole, ventral/rostral/medial prefrontal cortex, rostral
  cingulate, parahippocampal areas, and the **amygdala**. The amygdala target is the one worth naming: **a
  cortical identity signal reaching the amygdala directly is a second route to affective evaluation
  alongside the fast subcortical one**, and unlike that one this route has already done the invariance
  work. Fan-out: to derive.
- **→ the caudally-directed stream** — temporoparietal junction, posterior parietal and occipital regions
  **including secondary visual cortex** (`01_visual_pathway`), caudal and dorsal prefrontal cortex, dorsal
  cingulate, parahippocampal areas. **An auditory area writing into visual cortex runs opposite to the
  direction this section otherwise records.** Fan-out: to derive.
  **The secondary-visual-cortex limb has a matching declaration**, which qualifies the arity note below:
  that note says splitting these lines would name far ends that *mostly have no matching declaration*,
  and **this limb is one of the exceptions.** The visual file's V2 entry declares `← auditory parabelt,
  caudal division — an auditory association area writing into secondary visual cortex`, and asks a
  question this end can nearly answer: **which tangential compartment it reaches.** That end notes its
  **thick stripes are the motion and disparity channel**, and this end types the caudal division's
  payload as **location and motion**. **So thick stripes are the candidate compartment, on the payloads
  alone, and neither end states it.** A candidate, not a resolution — recorded because the two ends
  together constrain it and neither does alone. **This limb can be split out now; the rest of the line
  still cannot.**
- **→ upper bank of the superior temporal sulcus**, and **the insula and retroinsular areas** — two
  further output streams beyond the rostral/caudal pair. Payload to derive. Fan-out: to derive.
- **Arity note carried from the source:** the three stream edges above are each written as **one edge
  naming many targets**, which is not one edge. Splitting them names far ends that mostly have no
  matching declaration, so the split is **owed at the source** and is not performed here — performing it
  would invent the arity.

**Sizing.** Basis: **per hemisphere.** ~56M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 112.00
MB.** **No per-division partition exists** for a structure the source now describes as two divisions
with a possible hierarchy between them.

**Shape.** **Sheet**, rank 3: **(lamina, division, position)** — eight laminae against **two divisions,
"at least"**, the hedge being the description's own, so the division axis has an extent that is a lower
bound rather than a count. ~56M neurons, partition **to derive**. **The map axis is weakly ordered here
and that is a positive finding**: frequency is ordered enough to locate the border between the two
divisions and not ordered enough to index as a map.

**Edge latency.** All edges **to derive**, and one internal gradient is recorded qualitatively: response
latencies rise from the caudal to the rostral division.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← anterolateral belt → rostral | call and identity features | to derive | event-driven | **none — an identity class** |
| ← caudolateral belt → caudal | location, **as an opponent rate code** | **read at the slope, not the peak** | event-driven | **opponent hemifield rate code — not a map** |
| ← rostromedial belt → both | to derive | to derive | event-driven | **ignores the caudorostral split** |
| ← primary auditory cortex | **weak rather than absent** | to derive | event-driven | tonotopic |
| ← medial geniculate, dorsal division | the non-tonotopic thalamic signal | to derive | event-driven | **non-tonotopic — and it cannot be what imposes a frequency map here** |
| ↔ contralateral counterpart (callosal) | a normalisation, denser than at the core | to derive | event-driven | matched bands |
| → anterior superior temporal, from rostral | **sound-object identity, invariance-building** | to derive | event-driven | none |
| → posterior superior temporal and the hinge, from caudal | location and motion | slope, not peak | event-driven | opponent rate code |
| → the rostrally-directed stream (incl. **amygdala**) | identity, **already invariance-worked** | to derive | event-driven | none |
| → the caudally-directed stream (incl. **secondary visual cortex**, `01_visual_pathway`) | location and motion | slope, not peak | event-driven | **auditory — and the far end is retinotopic** |
| → upper bank of the superior temporal sulcus; the insula and retroinsular areas | to derive | to derive | event-driven | to derive |

**One row here writes into another modality's sheet, and it runs opposite to the direction this section
otherwise records.** The frame change from an opponent auditory rate code to a retinotopic compartment
has no correspondence at either end. **The candidate compartment is the thick stripes**, on the two
payloads together — location and motion at this end, motion and disparity at that one — **and neither end
states it.**

**The amygdala row is a second route to affective evaluation alongside the fast subcortical one** from
entry 5's medial geniculate division, and the two differ in kind: **this route has already done the
invariance work and that one is impoverished by design.** A consumer that merges them has collapsed a
fast coarse alarm and a slow worked identity into one input.

## Algorithm

- **Transform.** **Complex sound-objects and sequences with invariance building** — identity invariant to
  talker, pitch and level ("what"), and location and motion ("where"). And the architecture states the
  transformation as a gradient rather than an operation: up the core → belt → parabelt hierarchy,
  **tuning bandwidth, latency and stimulus specificity rise while temporal precision falls, and that
  gradient *is* the payload transformation.** **No standard operation is named above**, and none is
  invented here.
- **The staining agrees with the connectional hierarchy rather than merely accompanying it** —
  parvalbumin, acetylcholinesterase and cytochrome-oxidase fall off in steps, heaviest in the core,
  moderate in the belt, lightest here. **Three independent measures ordering the same three tiers the
  same way**, which is a corroboration of the tier structure and not a further fact about this one.
- **Laminar sub-structures: eight**, layer 4 **thinner and less granular than the belt's**, with enlarged
  pyramidal populations in **3c** and **5** — the feedforward and driver-output layers, **consistent with
  a stage whose job is to project widely.** The laminar profile and the output fan agree.
- **Whether this is one stage or two is unsettled, and it matters structurally.** The caudal-to-rostral
  latency gradient plus activation beginning in **layer 4** of the rostral division admits two readings:
  the parabelt inherits the gradient already present in the belt, or **there is an additional
  hierarchical step inside it. Under the second, this structure is two stages in series and the "what"
  and "where" divisions are not siblings** — which contradicts the parallel-streams picture. **An
  implementation that runs the two divisions in parallel has chosen the first reading; one that runs them
  in series has chosen the second. Neither is written here.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, division≥2, position) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **The division axis has an extent that is a lower bound rather than a count** — two, "at least", the
  hedge being the description's own. **An array dimension cannot be a lower bound**, so this axis cannot
  be allocated at all, which is a third distinct blocking state: entries 1–5 lack lengths, entry 6 lacks
  an axis direction, and this one has an axis whose length is open above rather than unknown.
  **The map axis is weakly ordered and that is a positive finding**: frequency is ordered enough to
  locate the border between the two divisions and **not ordered enough to index as a map.** So the
  position axis exists to separate the divisions and cannot be used to address within them.
  **~56M with no per-division partition**, for a structure the architecture describes as two divisions
  with a possible hierarchy between them.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count per hemisphere | **~56M** | the Sizing field |
  | `divisions` | count | **≥ 2** — a lower bound, not a count | the Shape field |
  | `laminae` | count | **8**, layer 4 thinner than the belt's; enlarged pyramids in 3c and 5 | the Function field |
  | latency gradient | — | **rises caudal → rostral**, qualitative; **and human evidence contradicts it** | the Edge latency and Justification fields |

- **Update equation.** **Waiting on the emission question (§10)**, and on whether the two divisions are
  siblings or stages, which changes what reads what.
- **State carried between updates.** `active` at (8, ≥2, position). The callosal loop closes here; the
  belt and core loops close through structures in this section. Initial values: to derive.
- **Edge storage.** 6 input edges, 5 output edges — **and three of the outputs are each one edge naming
  many targets**, so the line count exceeds the edge count by an amount the architecture declines to fix.
  Line count to derive. Latency to derive on all eleven. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The per-division partition of ~56M; the division axis's true
  extent; whether this is one stage or two; the three compound output lines' arity, **owed at the
  source**; the compartment the secondary-visual-cortex limb reaches, a candidate at both ends and stated
  at neither.
  **And the human evidence contradicts the macaque arrangement**: human electrocorticography finds the
  shortest latencies to clicks and vowels in the **middle** of the superior temporal gyrus, not at the
  caudal end where the macaque gradient starts, **so the internal edge may run the wrong way or from the
  wrong place in a human brain.** The remaining third of the superior temporal gyrus responds to sound
  and has not been shown to receive significant thalamic input, so it is **neither core, belt nor
  parabelt — to derive.** Inherited, and repaired at the source.

---

# 9. Anterior superior temporal gyrus and sulcus

## Contract

**Inputs.**
- **← auditory parabelt, rostral division** → the **mid** superior temporal gyrus — talker-invariant
  sound-object identity. The edge terminates at the mid gyrus and the rest of the chain is internal.
  Fan-in: to derive.
- **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. Fan-in / fan-out: to
  derive.

**Outputs.**
- **→ the distributed semantic system** (lexical access) — **invariant phonetic form**: phonemes composed
  into words and phrases, plus voice identity. **This is the auditory line's inferotemporal cortex, and
  the payload hardens the same way** — "the word that was said" and "who said it" are **phrases, not
  types**: no units, no frame. Fan-out: to derive.
- **→ temporal pole** (`07_anterior_temporal_lobe`) **and middle temporal gyrus → ventrolateral
  prefrontal cortex** (`11_frontal_lobe`) — the same identity code, toward amodal concept and controlled
  retrieval. Fan-out: to derive.
  That consumer declares `← rostral superior temporal gyrus — talker-invariant word and sound-object
  identity, the auditory "what" endpoint`, records it as **the principal input to its dorsolateral
  subdivision.**
  **This line is a chained compound and the arity is owed here.** It names two targets and an onward hop
  on one edge: the temporal pole and the middle temporal gyrus are separate destinations, and the
  ventrolateral prefrontal cortex is reached *through* them rather than by this edge. **The consumer
  declares its own onward output to ventrolateral prefrontal cortex separately**, so the hop is a second
  edge at a second producer, not part of this one.
- **→ amygdala and inferior prefrontal cortex**, on the **voice-identity** payload specifically — speaker
  identity and vocal affect. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~48M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 96.00 MB.**

**Shape.** **Sheet**, rank 3, and **two sub-element systems compete for the same axis** — a three-stage
speech hierarchy running posterior to anterior on **integration-window length**, and three **voice
patches** on the same axis that are not the same three things. **The shape must carry both or it will
assert they are one.** ~48M neurons, partition **to derive**.
**And the tangential extent is not shared across individuals**: the voice patches are highly reproducible
within one brain and highly variable between brains in location. **A per-structure count is meaningful
and a per-coordinate index is not**, which is a constraint on what any allocation can claim to address.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← parabelt rostral → mid superior temporal gyrus | talker-invariant sound-object identity | to derive | event-driven | none |
| ↔ contralateral counterpart (callosal) | a normalisation | to derive | event-driven | matched |
| → the distributed semantic system | **invariant phonetic form**: phonemes composed into words and phrases, plus voice identity | **none — a phrase, not a type** | event-driven | **none** |
| → temporal pole (`07_anterior_temporal_lobe`) and middle temporal gyrus | the same identity code, toward amodal concept and controlled retrieval | none | event-driven | none |
| → amygdala and inferior prefrontal cortex | **voice identity specifically** — speaker identity and vocal affect | none | event-driven | none |

**This is the auditory line's inferotemporal cortex and the payload hardens the same way.** *The word
that was said* and *who said it* are **phrases, not types**: no units, no range, no coordinate frame.
Every output row above is untyped for that reason, and the untyping is licensed at the architecture rung
rather than introduced here — the same wall `01_visual_pathway` hits at inferotemporal cortex.

**Two payloads leave this structure on different edges to different targets**, and they must be separated
somewhere inside it. **Internal edges between the speech hierarchy and the voice patches are to derive**,
and that is the interesting gap: the two systems occupy the same territory on the same axis.

## Algorithm

- **Transform.** **Top of the auditory ventral stream.** Three stages on a **timescale hierarchy** —
  phoneme-length processing in the **mid** superior temporal gyrus, word-length in the **anterior
  gyrus**, phrase-length beginning in the **anterior sulcus**. **The organising variable is the length of
  the pattern being integrated, which makes this a hierarchy of temporal receptive windows rather than of
  feature complexity.** **No standard operation is named above**, and none is invented here — but the
  organising variable is named, and it is a **duration**, which no array axis in this file carries.
- **Two sub-structure systems occupy the same structure on the same axis and are not the same three
  things.** Three speech stages posterior-to-anterior on integration-window length; three **voice
  patches** per hemisphere — posterior, mid, anterior — densest in the right posterior sulcus. **The
  shape must carry both or it will assert they are one.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, speech_stage=3, voice_patch=3, position) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **Rank 4, and the two sub-element axes lie on the same physical axis.** This is not the orthogonal
  case of V2's stripes against laminae in `01_visual_pathway`: there the two axes were genuinely
  independent and merely out of register. Here **both sub-element systems run posterior to anterior on
  the same tissue**, so the index pair (speech_stage, voice_patch) does not address a product space —
  most of the product is empty and the architecture does not say which part. **Collapsing them to one
  axis of three would assert they are the same three things, which the architecture denies in as many
  words. Carrying both as written asserts a product that does not exist.** Recorded, and not resolved.
  **A per-structure count is meaningful and a per-coordinate index is not.** The voice patches are highly
  reproducible **within** one brain and highly variable **between** brains in anatomical location, so the
  position axis addresses nothing stable across individuals. **This constrains what any allocation can
  claim to address**, and it is a different limitation from an unknown extent: the extent could be
  supplied and the index would still not mean the same thing in two brains.
  **~48M with no partition** across three speech stages, three voice patches, or eight laminae.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count per hemisphere | **~48M** | the Sizing field |
  | `speech_stages` | count | **3**, on integration-window length | the Function field |
  | `voice_patches` | count | **3** per hemisphere, densest in the right posterior sulcus | the Function field |
  | `laminae` | count | **8**, homotypical association cortex, layer 4 present and thin | the Function field |
  | integration windows | duration | **phoneme / word / phrase length — named, no figures** | the Function field |

  **The integration windows are the organising variable of the whole structure and no figure is given for
  any of the three.** They are durations, and durations are the one quantity this rung cannot supply
  itself: they would come from the scheduling discipline, which is unset.
- **Update equation.** **Waiting on the emission question (§10)**, and on the integration windows, which
  are durations with no figures and no interval to express them in.
- **State carried between updates.** `active`. **The internal three-stage chain is a series, not a
  loop**, so it does not impose an ordering constraint of the kind the retina's or the olive's loops do;
  the callosal loop closes here. Initial values: to derive.
- **Edge storage.** 2 input edges, 3 output edges — **and one output is a chained compound naming two
  targets plus an onward hop**, so its line count is two and not three: the onward hop is a second edge
  at a second producer. Line count otherwise to derive. Latency to derive on all five. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The partition of ~48M; the integration-window durations; the
  internal edges between the speech hierarchy and the voice patches; the chained compound's arity, **owed
  here**.
  **And lateralisation here is contested, so the architecture must not carry a single label — nor may
  this file.** For **speech content** the literature is divided: one meta-analytic model is explicitly
  left-biased, while the dual-stream account holds the ventral stream **largely bilateral** with
  computational differences rather than a division of labour, and word deafness most commonly follows
  **bilateral** superior temporal damage. For **voice identity** the direction is the other one —
  right-biased on both accounts. **So a single "left-lateralised" label is wrong regardless of how the
  speech dispute resolves**, because it would be applied to one structure carrying two payloads that
  lateralise oppositely. **And voice selectivity is contested about which structure is selective**:
  damage to the posterior sulcus does not impair voice recognition, so of the three voice patches **the
  most active may not be the one doing the recognising** — which means the voice_patch axis above may be
  ordered by the wrong criterion. Inherited, and repaired at the source.

---

# 10. Posterior superior temporal gyrus and the Sylvian parieto-temporal area

## Contract

**Inputs.**
- **← auditory parabelt, caudal division** → the **posterior gyrus** — location and motion as an opponent
  rate code, and the auditory form of speech. The edge terminates at the posterior gyrus; the rest of the
  chain is internal. Fan-in: to derive.
- **← visual and somatosensory cortex** — payload to derive. Recorded because the hinge responds to
  **silent lip-reading** and to **reading written words**, neither of which can arrive on an auditory
  edge. Fan-in: to derive.
- **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. Fan-in / fan-out: to
  derive.

**Outputs.**
- **→ inferior parietal lobule (supramarginal gyrus), and onward to premotor and inferior frontal
  cortex** — the **auditory-to-motor mapping**: a sound target expressed in terms the motor system can act
  on, plus phonological working memory. Strongly left-dominant. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~40M neurons. Fan-in to derive, bounded ≤ 16 bits → **≤ 80.00
MB.** **No partition across the three sub-structures exists**, and for the hinge one may not be
constructible in the usual way.

**Shape.** **Sheet**, rank 3: **(lamina, sub-element, position)**, three sub-elements in series. **The
last of the three has no extent that can be stated**: the hinge is defined by response profile — the
region responding to both auditory perception and silent vocal-tract gestures — so **its borders move with
the task used to find it**, and an axis bounded by a criterion rather than by a boundary cannot be given a
length. Tangentially it is a **patchy sensory/motor mosaic**, two interdigitated populations in one
territory, and an edge that should reach the motor-weighted patches and not the sensory-weighted ones has
no index to say so. ~40M neurons, partition **to derive**.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← parabelt caudal → posterior gyrus | location and motion **as an opponent rate code**, and the auditory form of speech | slope, not peak | event-driven | opponent rate code — not a map |
| ← visual and somatosensory cortex | to derive | to derive | event-driven | **visual / somatosensory — neither is the auditory frame** |
| ↔ contralateral counterpart (callosal) | a normalisation | to derive | event-driven | matched |
| → inferior parietal lobule (supramarginal gyrus), onward to premotor and inferior frontal cortex | **the auditory-to-motor mapping**: a sound target expressed in terms the motor system can act on, plus phonological working memory | to derive | event-driven | **a motor frame — and the transform into it is the open question below** |

**The second input row exists because of what the structure does and not because a producer declared
it.** The hinge responds to **silent lip-reading** and to **reading written words**, **neither of which
can arrive on an auditory edge** — so the edge is inferred from function. It is the only row in either of
these two files reached that way, and its payload is to derive at both ends.

**The output row names a frame change that may not be a transform at all** — see the algorithm.

## Algorithm

- **Transform.** **Auditory space and motion, and the sensorimotor interface for sound.** And here the
  architecture records something no other entry in either file does: **the central question has a named
  alternative answer of "nothing."** The literature distinguishes an area that acts as an **interface**
  between two tasks — a shared level of processing both draw on — from one that **integrates** one level
  into another. **Under the first reading there is no transform at this stage at all**, only a common
  representation the sensory and motor systems each read and write. **This is the one place in this
  section where the payload change may be null**, and it is recorded as unsettled rather than resolved in
  favour of a transform. **Writing any operation here would resolve it by assertion.**
- **The patchy mosaic is compatible with either reading and arguably favours the shared-representation
  one**, since a converter would not obviously need two segregated populations.
- **It is not speech-specific.** Sensorimotor responses are equally robust for a tonal melody with covert
  humming as for speech, and it activates for silent lip-reading, for reading, and in musicians for
  covert playing. **So the function is auditory-to-vocal-tract guidance in general**, and an
  implementation specialised to phonemes has narrowed it.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, sub_element=3, position) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **The third sub-element has no extent that can be stated, and this is a fourth distinct blocking
  state.** The hinge is **defined by response profile** — the region responding to both auditory
  perception and silent vocal-tract gestures — so **its borders move with the task used to find it.** An
  axis bounded by a criterion rather than by a boundary **cannot be given a length at all**, which is not
  the same as a length not yet supplied. **A structure so defined has no border independent of the task
  used to elicit it**, so an edge terminating "on the Sylvian parieto-temporal area" is anchored to a
  response profile and not to a bounded structure — unlike, say, the medial superior olive. **Every other
  structure in this section would still be there if nobody ran an experiment.**
  **Tangentially the hinge is a patchy sensory/motor mosaic** — two interdigitated populations in one
  territory, attributed to different neuronal subpopulations, with distinct spatial activation patterns
  for the sensory and motor phases of one task. **So the hinge is not a homogeneous converter**, and **an
  edge that should terminate on the motor-weighted patches and not the sensory-weighted ones has no index
  to say so.** The array above has no axis for it.
  **~40M with no partition across the three sub-structures**, and for the hinge one may not be
  constructible in the usual way.
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count per hemisphere | **~40M** | the Sizing field |
  | `sub_elements` | count | **3 in series** — posterior gyrus, posterior sulcus, the hinge | the Shape field |
  | `laminae` | count | **8**, homotypical association cortex | the Function field |
  | hinge extent | — | **not statable** — borders move with the task | the Shape field |
  | mosaic index | — | **none exists** | the Function field |

- **Update equation.** **Waiting on the emission question (§10)**, and **on whether there is a transform
  here at all.** No other entry in either file has that second condition.
- **State carried between updates.** `active`. The callosal loop closes here; the internal three-stage
  chain is a series. Initial values: to derive.
- **Edge storage.** 3 input edges, 1 output edge — **the smallest output fan of any cortical structure in
  either file**, and the one output is itself chained onward to premotor and inferior frontal cortex.
  Line count to derive. Latency to derive on all four. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** Whether there is a transform here at all; the hinge's extent, which
  may not be statable; an index for the sensory/motor mosaic; the payload on the visual and somatosensory
  input, inferred from function at both ends.

---

# 11. Right-hemisphere prosodic homologues

## Contract

**Inputs.**
- **← right auditory parabelt** → the right superior temporal gyrus and sulcus — the same acoustic feature
  stream as the left, read with a **finer spectral and coarser temporal** bias: the primary auditory
  cortex asymmetry compounded up the hierarchy. Fan-in: to derive.
- **↔ the contralateral counterpart** (callosal, reciprocal) — a normalisation. Fan-in / fan-out: to
  derive.

**Outputs.**
- **→ semantic and limbic targets**, and for production the right inferior frontal gyrus — **prosodic and
  affective identity**: the contour of pitch, loudness, timing and stress and the emotional category it
  signals; **not** segmental content. Fan-out: to derive.

**Sizing.** Basis: **the right side, both sub-structures combined.** ~50M neurons. Fan-in to derive,
bounded ≤ 16 bits → **≤ 100.00 MB.** **This figure does not reconcile with the per-hemisphere figures of
the two structures it is the counterpart of.**

**Shape.** **Sheet**, rank 3, two sub-elements — and **this structure's shape is where the per-hemisphere
convention visibly fails.** These are the right-side counterparts of two structures that have their own
entries and their own per-hemisphere counts, so the same array is described twice under two conventions.
~50M for both against ~88M for the same two areas counted per hemisphere: **the extents cannot both be
right.** **No cytoarchitectural difference between the two hemispheres' versions is established**, so the
shapes are identical and only the extents disagree.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← right auditory parabelt | the same acoustic feature stream as the left, **finer spectral and coarser temporal** | to derive | event-driven | as the left, read with the opposite bias |
| ↔ contralateral counterpart (callosal, reciprocal) | a normalisation | to derive | event-driven | matched |
| → semantic and limbic targets; right inferior frontal gyrus for production | **prosodic and affective identity**: the contour of pitch, loudness, timing and stress and the emotional category it signals; **not segmental content** | **none — a phrase, not a type** | event-driven | **none** |

**The input row is the primary auditory cortex asymmetry compounded up the hierarchy**, not a new
divergence — which bears directly on whether this structure needs a separate existence at all.

## Algorithm

- **Transform.** **The right counterparts of the two temporal endpoints above, weighted toward prosody
  and affect rather than segmental content.** **No standard operation is named above**, and none is
  invented here.
- **The packaging is a decision rather than a finding.** Two sub-structures — the right anterior superior
  temporal gyrus and sulcus (affective-voice and prosodic-contour identity), and the right posterior
  superior temporal gyrus (prosodic-spatial). **They are the right-side counterparts of two structures
  that have their own entries, and the source gives them one entry between them — the split is owed at
  the source.**
- **No cytoarchitectural difference between the two hemispheres' versions of these areas is
  established**, which is itself worth recording: **the claimed functional divergence has no declared
  structural correlate.** So the arrays here are shaped identically to entries 9 and 10 and differ only in
  extent — and the extents disagree.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, sub_element=2, position) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **These arrays may be the same arrays as entries 9 and 10's, described twice under two conventions.**
  ~50M for both against ~88M for the same two areas counted per hemisphere. **The extents cannot both be
  right**, and allocating both as written either double-counts ~50M of tissue or asserts a right side
  1.76× smaller than the left. **This is the one place in either of these two files where two entries may
  describe one piece of brain.**
- **Parameters.**

  | parameter | unit | value or range | origin |
  |---|---|---|---|
  | `neurons` | count, **right side, both sub-structures combined** | **~50M** — and see the reconciliation below | the Sizing field |
  | `sub_elements` | count | **2** | the Function field |
  | `laminae` | count | **8**, homotypical association cortex | the Function field |
  | cytoarchitectural difference from the left | — | **none established** | the Function field |

- **Update equation.** **Waiting on the emission question (§10)**, and on whether this structure is
  distinct from entries 9 and 10 at all.
- **State carried between updates.** `active`. **The callosal edge is load-bearing here in a way it is
  not elsewhere**: if lateralisation is an equilibrium held by interhemispheric inhibition, **the edge is
  not an addition to these structures but a condition of their differing at all.** Initial values: to
  derive.
- **Edge storage.** 2 input edges, 1 output edge. Line count to derive. Latency to derive on all three.
  Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** Whether these are two structures or the right halves of entries 9
  and 10; the ~50M against ~88M reconciliation; the split into two entries, **owed at the source**.
  **Three competing accounts of why prosody lateralises, and none may be adopted silently.** The
  **biological** account makes affective prosody right-lateralised as hemispheric specialisation. The
  **functional** account makes lateralisation follow communicative function — emotional prosody right,
  linguistic prosody left — with the right operating on larger units and the left on smaller. The
  **acoustic** account makes it follow the cue: left for timing, right for pitch and spectral structure.
  **The aggregate evidence is bilateral with a right lean at best.**
  **Part of the reported lateralisation is an artefact of paradigm**, which tells a builder how much to
  trust the rest: valence effects are strongly right-lateralised under blocked presentation and bilateral
  or left-accented in event-related designs, and explicit attention to prosody gives left lateralisation
  while implicit perception gives none. **The same structure lateralises differently depending on how it
  is asked.**
  **And the acoustic account is deflationary for this structure's status.** Its claim — left for
  temporal, right for spectral — **is the same asymmetry already declared at the primary auditory cortex
  as a bias and a trade-off.** If prosodic lateralisation is that bias working on longer stimuli, then
  this is **not a new divergence between the hemispheres but a downstream consequence of one recorded
  three stages earlier, and treating it as new would double-count.** Inherited, and repaired at the
  source.

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
and **every localisation computation in the section happens in the cheap end. The two structures that
compute azimuth together hold ~21,000 neurons and ~0.042 MB.**

**Three fan-ins in this section are known exactly, and two of them cost nothing.** A type I spiral
ganglion neuron contacts exactly one inner hair cell, and the medial nucleus of the trapezoid body's
principal cell receives one calyx of Held: **log₂(1) = 0, because a neuron with a single input has no
count to threshold.** The spherical bushy cell's one-or-two endbulbs cost 1 bit. **The pathway's most
timing-critical stages are its cheapest in parameter memory, and for the same reason they are precise** —
a low fan-in is what buys timing fidelity. **That inverts the expectation that a high-precision stage is
an expensive one**, and it is the sharpest single finding this rung inherits from the section.

**A source-internal cross-check that closes.** The temporal-lobe anchor gives ~145M neurons per
hemisphere for the lateral association superior temporal cortex spanning parabelt, anterior and posterior
superior temporal. Recomputed: **56 + 48 + 40 = 144M**, in exactly the stated 7:6:5 proportions. That
closes.

**A source-internal cross-check that does not close, and it is recorded here rather than repaired.** The
right prosodic homologues are given **~50M for both**, while the two structures they are the counterparts
of are given **~48M and ~40M per hemisphere — 88M for the same two areas.** Either those two figures are
left-hemisphere values labelled per-hemisphere, in which case the right side is **1.76× smaller** and the
anchor above cannot hold for both hemispheres; or they are true per-hemisphere values, in which case the
right homologues' 50M **double-counts** structure already included. **The two readings differ by ~88 MB
of parameter memory** in the table above. **This is a finding about the description and the repair
belongs at that rung.**

**The per-hemisphere convention does not survive this section, and the parabelt is where it stops.**
Below that tier the two sides are counterparts and one count serves both. Above it the source describes
**left** endpoints for segmental content and gives the **right** endpoints a separate entry with its own
count and its own payload — **so from the parabelt upward there is no symmetric description to count once
and double.** The totals above are mixed-basis for that reason and are not a whole-brain figure.

**The total is a floor.** Hair-cell storage is to derive, the trapezoid body and periolivary groups are
uncounted, eight belt fields share one count and two parabelt divisions share another, every cortical
fan-in sits at the 16-bit ceiling rather than at a measured value, and **state memory and edge storage
are not in this table at all.** **Edge storage is the one that would bite hardest here**: a pathway
resolving tens of microseconds implies a very short update interval, and edge storage scales with its
reciprocal. **That figure cannot be computed until the scheduling discipline is set, and it is not.**

**Memory is not a binding constraint and none of these figures is to be reduced.** It is a derived
requirement recorded as found.

## Completion test

**An entry is finished when the code can be written from it without making a single further choice.**

**By that test no entry in this file is finished, and none can be finished at this rung.** The blocking
items are the six on the standing list, and four of them are on the surface-before-touching list and are
Micky's.

**This section adds four blocking states the visual line did not have**, and they are distinct from one
another and from a missing length:
1. **An axis whose direction is unknown** — the primary auditory cortex's tonotopic gradient, four
   orientations on record. An axis that cannot be laid down cannot be indexed.
2. **An axis whose extent is a lower bound** — the parabelt's "two divisions, at least." An array
   dimension cannot be a lower bound.
3. **An axis bounded by a criterion rather than by a boundary** — the Sylvian parieto-temporal hinge,
   whose borders move with the task used to find it. It cannot be given a length at all.
4. **Two sub-element systems on one physical axis** — the anterior superior temporal gyrus's speech
   stages against its voice patches, which are explicitly not the same three things.

**And one transform may be null.** The hinge may be an interface rather than an integrator, in which case
there is no payload change at that stage. **No other entry in either of the first two sections has that
possibility**, and writing an operation there would settle it by assertion.
