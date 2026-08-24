# Brain architecture — 03 other senses

**Date:** 2026-08-22
**Derived from:** `human_brain_03_other_senses` — olfaction from the epithelium to
piriform cortex, taste from the taste buds to the insula, and the vestibular apparatus with its
central nuclei. **One source file, and no other content source.**

**Counting basis is declared per structure, and for most of this section there is nothing to count.**
**Per side** at the olfactory epithelium and bulb, **per ear** at the vestibular transducers,
**per hemisphere** where a cortical figure exists — and **six of the seven structures carry no
neuron count at all.** That is the section's defining fact and it is not a formatting problem: the
olfactory bulb is the only structure here with verified human numbers, and everything else reads
*soft* or *unknown* in the description.

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed below.

- `14_brainstem_midbrain_hypothalamus`, `16_spinal_cord`. **Eleven shared edges diffed and stemmed.
  Three two-ended; and this file holds, inside one bundled entry, a thalamic structure that two other
  files independently record as having no entry anywhere.**
- `10_cerebellum`. **Five shared edges diffed and stemmed. Four two-ended, and this file's three
  outputs to the cerebellum are the split that file's single bundled afferent line owes. One edge is
  declared only at the far end: the deep cerebellar nuclei's fastigial projection onto the vestibular
  nuclei, which this file does not carry.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number**, where the
far file is checked against this one. An endpoint with no stem is unchecked, and that is not a claim
that none exists.

**These three senses break the template the first two sections were built on.** Olfaction reaches
cortex **with no thalamic relay and therefore no thalamic gate** — the only sense that does.
Taste relays through the thalamus but lands in the insula and frontal operculum rather than on a
neocortical strip. Vestibular sensation has **no dedicated primary cortex at all**, and it is **two
senses on two transducers**, neither of whose payload can be interpreted without the other.

---

## Structural invariants

**Whole-pathway co-instantiation, and here it takes its strongest form in the map.** Elsewhere the
argument is that staging leaves loops open. In the vestibular line it is stronger than that:
**neither transducer's payload is defined without its sibling.** A semicircular canal carries
rotation rate and is blind to gravity, tilt and attitude; an otolith organ carries the
gravito-inertial sum and cannot separate a steady tilt from a steady acceleration, because the two
produce the same shear on the same hair cells. The description states the consequence flatly:
neither organ is capable of providing unambiguous information about head motion and orientation, and
the resolution is the **specific convergence of canal and otolith signals onto central vestibular
neurons**. So a build that instantiated one line first would not have a partial system — it would
have a line whose output means nothing. **Attitude is computed, never transduced, and there is no
attitude receptor.**

The olfactory line closes its own loops the ordinary way: piriform projects back to the bulb, and
centrifugal neuromodulation from basal forebrain, raphe and locus coeruleus arrives at the bulb;
whether the brain modulates the **epithelium** the way the olive modulates the cochlea is recorded as
**owed** rather than denied. **The gain loop onto the chemical front end is the one this section
cannot confirm exists.**

**Per-edge latency: every edge in this section reads *to derive*, and yet this is the first section
in the map that states time constants at all.**

- The canal afferent's velocity signal **decays with a time constant of 3–5 seconds**.
- The central percept, the nuclei's activity, and the nystagmus following a step change in head
  velocity all have a time constant of **at least 15–25 seconds**, produced by the **velocity storage
  integrator** — a **3× to 8.3× lengthening**, recomputed from those two ranges.
- **The velocity-storage stage's declared transformation is purely temporal**: the content is still
  angular velocity, and only its persistence changes. The description notes it has no other edge of
  that form.

**These are state time constants and not edge latencies, and the distinction is the whole point.**
An edge latency says when a signal arrives; a time constant says how long a stage holds what it
received. **The invariant is about the first and this section only supplies the second.**

**And the two sections together bracket the system's dynamic range.** File 02 states a computation
working at **tens of microseconds**; this file states state that must persist **15–25 seconds**.
Recomputed, 25 s against 10 µs is a ratio of **2.5 × 10⁶ — about 6.4 orders of magnitude, ~21 bits of
time.** **No single update interval is comfortable across that span**, and this is a constraint on the
scheduling discipline that neither section produces alone.

**Two new classes of non-neural edge, bringing the map's total to four.** After light at the retina
and sound at the cochlea:

- **Chemical arrival** — odorant molecules dissolved in the olfactory mucus, and tastants at the taste
  buds. Fan-in **not applicable**.
- **Mechanical arrival, twice and by two different mechanisms** — head rotation reaching the cupula
  through the inertial lag of the endolymph, and head linear acceleration reaching the hair bundles
  through the weight and inertia of the **otoconial mass**. Fan-in **not applicable**.

**A fifth class of internal transfer, which is not an edge and must not be written as one.** In the
olfactory epithelium the basal stem cells produce new sensory neurons throughout life. The
description marks the basal-cell → sensory-neuron line as **a developmental transfer carrying no
signal**, recorded only because the slot would otherwise imply a fixed population. **A structure that
continuously rebuilds its own front end has no representation in an architecture of fixed arrays**,
and that is a finding rather than an omission.

---

## Olfactory epithelium

- **Function → structure.** Turns airborne molecules into a neural signal. A patch of
  pseudostratified neuroepithelium in the **olfactory cleft**, covered by mucus into which the
  receptor cells project cilia. **Unlike every other sensory front end in the map, the transducer is
  itself a neuron whose own axon enters the brain** — no separate primary afferent, no ganglion, and
  no relay before the first central synapse. Its unmyelinated axons bundle into the **fila
  olfactoria**, cross the **cribriform plate**, and terminate in the bulb: **the shortest path from
  the outside world to the brain anywhere in the body.** Three cell classes — **olfactory sensory
  neurons**, **sustentacular cells**, and the **basal stem cells** that replace the first class for
  life.
  **The one-neuron-one-receptor rule is the central structural fact.** Each sensory neuron expresses
  **exactly one** olfactory receptor gene, chosen stochastically and then held; every neuron
  expressing a given receptor — **scattered across a broad zone rather than clustered** — sends its
  axon to **the same one or two glomeruli**, and **the receptor protein itself steers the axon there.**
  So the sorting that builds the bulb's chemotopic map **is done by the receptor molecule, not by a
  topographic projection.**
- **Inputs.**
  - **← airborne odorant molecules dissolved in the mucus** — chemical identity and concentration.
    **A chemical arrival, not a neural edge.** Fan-in: not applicable.
  - **← centrifugal modulation of the epithelium** — **payload owed**; whether this edge exists at all
    is what the description declines to assert.
- **Outputs.**
  - **→ olfactory bulb**, by the olfactory nerve, onto the **glomeruli** — one component of a
    **combinatorial chemical code**: a single neuron reports how strongly its one receptor type is
    occupied, and the odour's identity exists only in the pattern across types. **Not a scalar, not a
    map of space, and not frequency-analysed the way the cochlear output is — there is no ordering of
    the chemical dimension corresponding to the tonotopic axis.** Fan-out: **one or two glomeruli**
    per axon.
- **Sizing.** Basis: **per side.** **~40 million sensory neurons**, and the description flags the
  figure as **inherited from the bulb entry, not independently sourced, with human estimates varying
  widely.** **Store: zero, and for a reason the model already contains.** The cell has **no neural
  input**, so there is no count of active inputs to compare against a threshold, exactly as for a
  fan-in of one. **The caveat is that the model's count has no referent here at all**: what this cell
  thresholds is receptor occupancy, and occupancy is not an input line. **Structure total: 0, with
  that caveat.**
- **Shape.** **Sheet**, rank 2: **(receptor type, position in the epithelium)** — and **the position
  axis carries no information.** The description is explicit: the signal is not spatial, there is no
  receptor sheet mapping the world, and position in the epithelium says nothing about where the
  odorant came from. **This is the first axis in the map that exists physically and indexes nothing.**
  Receptor-type extent: **contested** — 350–400 intact types on one reading, 100–200 on another, a
  disagreement the description records without taking a side.
- **Edge latency.** All edges **to derive.** One qualitative fact: the olfactory nerve is
  **unmyelinated**, which is part of why olfactory conduction is slow — the opposite of the auditory
  brainstem's heavy myelination, and stated for the same kind of reason.
- **Invariant conformance.** Co-instantiation: the only descending edge onto this structure is the one
  recorded as owed, so **the front-end gain loop that closes in the auditory section cannot be
  confirmed to close here.** Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The transduction cascade is **biochemical amplification private to
  each cell** — odorant binds, a G-protein cascade raises cyclic adenosine monophosphate, a
  cyclic-nucleotide-gated channel opens, a calcium-activated chloride current amplifies — where the
  cochlear amplifier is mechanical and shared across cells. **Lifelong regeneration is an
  architectural fact, not a maintenance detail**: whatever holds the map stable cannot be the
  individual cells, because they are replaced.

## Olfactory bulb

- **Function → structure.** The first olfactory processing stage. Sensory-neuron axons expressing one
  receptor type converge onto **glomeruli**; **mitral and tufted cells** read the glomerular pattern
  and, shaped by **granule- and periglomerular-cell inhibition**, send it on. **Laminar sub-elements:
  six, and they are not cortical layers** — olfactory nerve, glomerular, external plexiform, mitral
  cell, internal plexiform, granule cell.
  **What it computes is named as four operations rather than as a transform:** gain control, contrast
  enhancement, spatial decorrelation, temporal synchronisation. **What is not in that list matters as
  much:** no change of reference frame, no binding, no categorisation. **The payload leaves in the
  format it arrived in — a pattern over glomerular channels — cleaned up.** This is the clearest case
  in the map of a stage whose payload change is a **normalisation rather than a re-expression**, the
  same class of operation the auditory callosal edge performs.
- **Inputs.**
  - **← olfactory epithelium** — the combinatorial chemical code, as a **pattern across ~5,500
    glomeruli**. **Fan-in: ~800 : 1** receptor-to-mitral convergence. **There is no topography of the
    world here: the map is chemotopic, and adjacency means chemical similarity.**
  - **← piriform cortex** (feedback) and **← basal forebrain / raphe / locus coeruleus** (centrifugal
    neuromodulation) — gain and state, no chemical content. Payload otherwise **owed**.
- **Outputs.**
  - **→ piriform and the rest of primary olfactory cortex**, by the **lateral olfactory tract**, and
    also to anterior olfactory nucleus, olfactory tubercle, cortical amygdala and rostral entorhinal
    cortex — the **decorrelated glomerular pattern**, sharpened by inhibition, chiefly ipsilateral,
    and **straight to cortex with no thalamic relay and therefore no thalamic gate.** Fan-out: to
    derive.
- **Sizing.** Basis: **per side.** **Glomeruli ~5,568 ± 830 per bulb** (range ~3,000–9,300, verified
  human); **mitral cells ~50,000 per bulb** (verified human). **Fan-in ~800 gives ceil(log₂ 800) = 10
  bits**, recomputed — **so this is the second exactly-derived width in the map, after the auditory
  zero-cost fan-ins, and the first that is neither zero nor one.** Mitral-cell store: **50,000 × 10
  bits = 62,500 bytes = 0.063 MB.**
  **Interneurons vastly outnumber the projection neurons**, so the bulb's total is
  **interneuron-dominated and soft** — recorded as *to derive*, and it is the larger term.
  **Structure total: ~0.063 MB firm, plus an interneuron store that is to derive and is the majority
  of it.**
- **Shape.** Rank 3: **(lamina, glomerulus, cell class)** — six laminae, ~5,568 glomeruli, and cell
  classes the description does not fully partition. **The glomerular axis is the one indexable axis in
  this section, and its index is chemical identity rather than space.**
  **Two extent problems, and both are real numbers rather than gaps.** First, the glomerular count
  ranges **3,000–9,300 across individuals — a 3.1× spread**, recomputed, so the axis length is not a
  property of the species. Second, **the convergence ratio the description states depends on the
  contested receptor count**: recomputed, 5,568 glomeruli over 350–400 types is **13.9 : 1 to 15.9 :
  1**, but over 100–200 types it is **27.8 : 1 to 55.7 : 1**. **The same measurement supports a
  four-fold range of glomerulus-per-receptor-type convergence**, and that consequence follows from the
  contest the epithelium entry records without being stated there.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the piriform feedback loop and the neuromodulatory
  loops close here. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **One synaptic arrangement here has no other instance in the map and
  breaks an assumption a lower rung would make.** The **mitral / tufted lateral dendrite ↔ granule
  cell spine** synapse is **dendrodendritic and reciprocal** — **one synaptic apposition carrying
  signal in both directions**, not two edges. **An architecture that assumes edges are directed must
  special-case it.**
  **A second one: lateral inhibition over a non-spatial neighbourhood.** Short-axon cells inhibit
  between glomeruli, and because glomerular adjacency is chemotopic, **"lateral" here means lateral in
  chemical similarity.** Every other instance of lateral inhibition in the map operates over a map of
  the world.
  **And the project-relevant divergence.** In rodents the bulb is a lifelong neurogenic region,
  ~95% of added cells becoming inhibitory granule cells, and is **the canonical example of a circuit
  holding stable representations while its own components are replaced.** **In humans it appears not
  to happen**: carbon-14 dating found adult bulbar neurogenesis extremely limited, migration reported
  only up to about 18 months, with human neuroblasts migrating toward the **striatum** instead — a
  different destination, not a reduced one. **If that holds, the most-cited mammalian instance of
  continuous structural learning is not a human mechanism.** The caveats are real and recorded: the
  cohort was forensic material weighted toward neuropsychiatric disease, and **a negative in that
  sample is not a negative in the species.** Also recorded: in rodent, reducing granule cells impairs
  odour **discrimination** while leaving **detection thresholds** and short-term olfactory memory
  intact, so **the link from neurogenesis to learning is real but neither simple nor monotonic.**

## Piriform and primary olfactory cortex

- **Function → structure.** The largest primary olfactory area: **three-layered allocortex** that
  forms and stores odour objects by **associative, content-addressable recurrent processing** — a
  cortical autoassociator supporting identification, **pattern completion**, and rapid olfactory
  learning. Anterior piriform is weighted to identity, posterior to category and association.
  **Laminar sub-elements: three layers, two of which subdivide, on piriform's own scheme — Ia, Ib,
  IIa, IIb, III** — and the description states explicitly that "layer" here does not mean what it
  means in the isocortical entries.
  **The afferent / associational segregation is strict and it sorts the cell classes.** Afferent
  fibres from the lateral olfactory tract land in **Ia**; associational fibres in **Ib through III**.
  **Semilunar cells** (IIa) are afferent-dominated and carry large spines in Ia but not in Ib;
  **superficial pyramidal cells** (IIb) take weaker afferent and stronger associational drive; **deep
  pyramidal cells** (III) are mostly driven by the recurrent circuit and receive the strongest
  recurrent inhibition. **So "sensory-driven" and "self-driven" are not two states of this network but
  two populations in it, ordered by depth.** **Semilunar cells send no feedback to the bulb** while
  the pyramidal cells do — **the afferent-dominated class is the one that does not talk back.**
  **Inhibition is split the same way:** layer I horizontal and neurogliaform interneurons take direct
  tract input and synapse on apical dendrites, scoped to the afferent stream; layer II/III bitufted
  regular-spiking interneurons take little tract input and synapse on somata and basal dendrites,
  scoped to the associational stream. **One structure, two inhibitory systems, each guarding its own
  input class.**
- **Inputs.**
  - **← olfactory bulb**, lateral olfactory tract, **monosynaptic**, onto **layer Ia** — the sparse
    glomerular odour pattern. Fan-in: to derive.
  - **← its own recurrent associational fibres**, onto **layer Ib and III** — the network's own state;
    the feedback that completes a partial pattern. Fan-in: to derive.
  - **← orbitofrontal and entorhinal cortex, amygdala, neuromodulatory nuclei** — context, value and
    state. Payload otherwise **owed**.
- **Outputs.**
  - **→ orbitofrontal cortex**, directly and by the mediodorsal thalamus — the **odour object**: a
    completed, content-addressed identity rather than a receptor pattern. **As at the inferotemporal
    cortex, the payload has become a category — "which smell", not "how much of what chemical."**
    Fan-out: to derive.
  - **→ amygdala** — the odour object, for hedonic and emotional evaluation.
  - **→ entorhinal cortex → hippocampal formation** — the odour object as an element of an episode.
  - **→ hypothalamus**, and **→ olfactory bulb** (reciprocal feedback) — payload **owed**.
- **Sizing.** Basis: **per hemisphere.** **Soft / unknown — no clean human per-area count.** Fan-in to
  derive. **Structure total: to derive**, and this is a large allocortical area, so the absence is not
  a small term.
- **Shape.** **Sheet**, rank 3: **(lamina, cell class, position)** — five laminar sub-elements, three
  principal cell classes, **and a position axis that is not indexable.** The bulb→piriform projection
  is **famously non-topographic**: a glomerulus's output is distributed broadly across the sheet
  rather than to a matched location, **so the chemotopy present in the bulb is discarded at this
  synapse.** The association fibres are non-topographic too, so nothing restores it, and **there is no
  spatial mapping of odour-evoked activity anywhere in this structure.**
  **One possible exception, and it would be a kind of map the map has no other instance of:** a spatial
  organisation by **efferent target** rather than by input — tissue ordered by where its cells project
  rather than by what they receive. **Owed.**
- **Edge latency.** All edges **to derive.** One structural fact stands in for one: **it is two
  synapses from the outside world**, receptor → bulb → here, with **no thalamic relay and therefore no
  gate that can be closed** — and every other primary sensory cortex in the map sits behind one.
- **Invariant conformance.** Co-instantiation: the bulb feedback loop closes here, and **the recurrent
  associational edge is the map's only declared intra-regional recurrent edge that is load-bearing for
  the entry's stated function** rather than noted in passing. **A staged bring-up that omitted it would
  not have a degraded autoassociator; it would have no autoassociator.** Per-edge latency: satisfied,
  all to derive.
- **Justification (biological).** **The discarding of chemotopy is what makes the autoassociator
  possible** — a content-addressable network cannot use an input map — and the description notes this
  payload change is not currently stated in the entry's own edge fields.
  **The same-dendrite, different-depth geometry recurs here for the fourth time in the map**: sensory
  input and network feedback arriving on one apical dendrite at different depths, as at the cortical
  layer-1 tuft, the dorsal cochlear nucleus's fusiform cell, and the medial superior olive's bipolar
  cell. **At four instances across four unrelated structures this is a pattern rather than a
  coincidence, and it is specific: the two streams are separated by distance along a dendrite rather
  than by different cells.**
  **One challenge to the laminar account, recorded not smoothed:** a single Golgi study reports
  afferent fibres penetrating beyond layer I into layer II, which would make the segregation strict
  only to first order.
  **And a chemical pathway the description does not carry as one.** Nasal irritants are transduced by
  **nociceptive free endings of the trigeminal nerve** and ride the somatosensory route to cortex, with
  two edges connecting them to olfaction proper — trigeminal collaterals to the epithelium and bulb,
  and carbon dioxide evoking piriform responses. **The protective-warning reading of that channel is
  wrong and the correction matters:** trigeminal thresholds are about **100 times higher** than
  olfactory ones, so **the irritant channel fires later and at higher dose, not earlier**; what it
  supplies is **damage-limitation reflexes** that reduce further intake after intake has occurred.
  **Detection in these modalities never precedes exposure — the molecule must already be inside.**

## Gustatory pathway

- **Function → structure.** Taste. Receptor cells in the taste buds are read out through **three
  cranial nerves** — VII, IX and X — into the rostral **nucleus of the solitary tract**, relayed by
  the **ventral posteromedial parvocellular thalamic nucleus** to the **primary gustatory cortex**,
  the **anterior insula and frontal operculum**, where quality and intensity are represented
  **independently of hunger — sensory, not yet reward.** **In primates this line skips the pontine
  parabrachial relay that rodents use.** The **orbitofrontal cortex** is the secondary taste cortex,
  where taste combines by learning with smell and vision into **flavour** and acquires reward value
  and hunger-dependent, sensory-specific satiety.
- **Inputs.**
  - **← taste buds**, by cranial nerves VII, IX and X → rostral **nucleus of the solitary tract**
    (`14_brainstem_midbrain_hypothalamus`) — taste **quality** and **intensity**, plus **oral
    somatosensation** (temperature, texture, viscosity, fat, capsaicin): a five-ish-dimensional quality
    vector with an intensity scalar, **no spatial map of the world, only a crude map of the tongue.**
    Fan-in: to derive.
    **The relay stage of this line has its own entry in another file, and that entry defers the
    payload to this one. Two-ended and confirmed.** That entry declares `→ the gustatory
    pathway, via the parvicellular ventral posteromedial thalamus to insular taste cortex — taste
    quality and intensity, typed at the gustatory entry`, **naming this entry as the place the payload
    lives.** **So the two files agree on the route and on which end types it**, and this end does.
    **The far end carries a partition this end does not**: its solitary-tract entry names seven
    subnuclei, one of them **parvicellular**, and a rostrocaudal gradient. **Owed here: say which
    subnucleus the gustatory line leaves from**, since the far end already has the axis.
  - **← the ventral posteromedial parvocellular thalamic nucleus** → anterior insula and frontal
    operculum — the same vector, relayed, chiefly ipsilateral. Fan-in: to derive.
- **Outputs.**
  - **→ orbitofrontal cortex** — quality and intensity, **independent of hunger.** **The payload
    changes at the next stage, not this one**, and that is the load-bearing fact: **the primary cortex
    declares what is in the mouth; the secondary declares what it is worth.** Fan-out: to derive.
  - **→ amygdala** and **→ hypothalamus** (feeding), reciprocal — payload otherwise **owed**.
- **A structure this entry holds as a stage is recorded as missing by two other files.**
  This entry names the **ventral posteromedial parvocellular thalamic nucleus** twice — in its
  Function field and on an input line — and carries it as its own row in the section totals below.
  **`14_brainstem_midbrain_hypothalamus` names the same structure twice**, at its lateral parabrachial
  nucleus (`→ intralaminar nuclei and the ventroposterior parvicellular thalamus`) and at its nucleus
  of the solitary tract (`→ the gustatory pathway, via the parvicellular ventral posteromedial
  thalamus to insular taste cortex`), and **records against both that it has no entry in
  `12_thalamus` under any name.** **`12_thalamus` confirms that absence from its own side**, having
  read its eight entries for it.
  **All three statements are true and the conclusion drawn from them was wrong.** The structure is
  absent from the thalamus section and **it is not absent from the architecture** — it is here, as one
  of three stages inside this bundled entry. **So a structure was reported missing because the file it
  belongs in by subject matter does not carry it, while the file that does carry it holds it below the
  level a search for entries can see.**
  **Two things make it invisible to the edge index as well.** The name differs in two places at once —
  *ventroposterior parvicellular* and *ventral posteromedial parvocellular* are the same nucleus
  written with a different word order and a different vowel — and **this entry is a bundle**, so the
  stage has no heading of its own to be matched against. **A bundled stage with a spelling variant is
  invisible from both directions**, which is the same failure the basal-ganglia file records for one
  structure carried at two levels of the hierarchy, arriving here through the spelling.
  **Owed at the source, and it is a decision rather than a repair:** either this stage becomes an
  entry in `12_thalamus` and this entry cites it, or `12_thalamus` records that the nucleus is
  described here. **Not moved here** — moving a stage between files at this rung would re-terminate
  three files' edges on a structure whose owner has not been decided.
- **Sizing.** Basis: **per hemisphere.** **Soft / unknown at all three stages** — the nucleus of the
  solitary tract (`14_brainstem_midbrain_hypothalamus`), the thalamic nucleus and the insular cortex —
  **no clean human counts.** Fan-in to derive. **Structure total: to derive, and this is three
  structures priced as none.** **And the first of the three has a full entry of its own in another
  file** — see above — **so this entry prices as none a structure that is counted, or fails to be
  counted, elsewhere.**
- **Shape.** **Rank and axes to derive.** **Sub-elements are owed throughout**: no laminar or
  divisional partition of any of the three stages was established. **The rostral/caudal gradient of
  the disputed hot spots is the only tangential organisation anyone has proposed, and it did not
  replicate.**
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the amygdala and hypothalamic edges are declared
  reciprocal, so loops close outside this section. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The five-quality alphabet is real at the receptor and does not
  survive the ascent.** Receptor proteins are expressed in **non-overlapping sets of cells**, which is
  what makes a discrete alphabet available and is the main evidence for **labelled-line** coding — but
  taste buds hold both narrowly and broadly tuned cells, and **as the signal proceeds to the hindbrain
  and higher, coding becomes more distributed and temporal patterns become important.** **So the
  quality vector is progressively re-encoded into an ensemble pattern as it ascends, and the same
  payload description must not be carried at every stage.**
  **Three coding models are live, not two:** labelled line; across-fibre / ensemble; and **temporal**,
  with quality embedded in the **cadence** of impulses rather than in which cells fire or how fast.
  **The map has no other payload of that form anywhere**, and it is the one a lower rung would find
  hardest to implement, since it makes spike timing the message rather than its carrier.
  **The gustotopic map is claimed and then contradicted.** Two-photon imaging in anaesthetised mouse
  reported quality-specific hot spots — sweet rostral, bitter caudal — with broadly tuned cells
  virtually absent; **a later study with a more sensitive calcium indicator, under the same
  anaesthesia, found the opposite**, and attributed the discrepancy to indicator sensitivity, so **the
  earlier study's narrow tuning may have been a detection threshold rather than a property of the
  tissue.** Imaging in **alert** mice found taste-responsive cells narrowly *or* broadly tuned and
  **sparsely scattered.** In human, high-resolution imaging with multivariate analysis finds distinct
  qualities in **distributed spatial patterns** rather than distinct topographic areas. **Recorded
  verdict: no map; a spatial population code.**
  **The convergence with olfaction is the finding worth carrying.** Taste quality is encoded in
  insular cortex **like odour in piriform cortex** — dispersed ensembles, no topography. **Both
  chemical senses arrive at cortex as distributed population patterns over a non-spatial quality
  space, and neither builds a map at any stage.** Against vision and hearing, where map claims were
  repeatedly over-stated but the underlying topography is real, **the chemical senses are the case
  where there was never a map to over-state — they are the control condition, and they behave like
  one.**
  **A confound specific to this cortex:** the insula is **inherently multisensory**, carrying
  somatosensory and thermal responses alongside taste, and the entry's own inputs declare oral
  somatosensation arriving on the same edges as taste.

## Semicircular canals

- **Function → structure.** Transduction of head **rotation**, and nothing else. **Three fluid-filled
  canals per ear** — horizontal, anterior, posterior — each ending in an **ampulla** whose **crista**
  carries hair cells with their bundles embedded in a gelatinous **cupula** spanning the duct. Head
  rotation makes the endolymph lag by inertia and deflect the cupula, shearing the bundles. The two
  ears' canals work as **coplanar pairs in push-pull**: a rotation exciting one member inhibits its
  partner.
- **Inputs.**
  - **← head angular motion** — mechanical rotation onto the hair cells of the three cristae. **Not a
    neural edge.** Fan-in: not applicable.
- **Outputs.**
  - **→ vestibular nuclei**, chiefly superior and medial, by the **superior division** of the
    vestibular ganglion and cranial nerve VIII — **head angular velocity, three-axis, head-fixed,
    band-limited with no direct-current term, one triplet per ear.** **Does not carry:** linear
    acceleration, gravity, tilt or attitude. Fan-out: to derive.
    - **→ cerebellum** (flocculonodular lobe) (`10_cerebellum`), on a branch that **bypasses the
    nuclei** — the same rotation-rate signal, unrelayed. **Two-ended, and this end is the specific
    one:** that file carries this limb inside a single afferent line naming the canals, the otolith
    organs and the vestibular nuclei together, with one payload clause across all three. **The split
    is owed there and every term it needs is here.**
- **Sizing.** Basis: **per ear.** **Soft / unknown — no hair-cell or ganglion-cell count is recorded.**
  Hair cells are **not neurons** and are the same class as the cochlear hair cells: their store is
  **to derive and not zero.** **Structure total: to derive.**
- **Shape.** **Rank 1: (canal).** **Extent exactly three per ear** — and this is **the only extent in
  the map that is exact, small, and physical.** Every hair cell in a crista is aligned along that
  canal's axis with kinocilia in the same direction, so **an entire crista has one directional
  sensitivity**: the organ is **not a map and not a population code but one scalar per canal**, and
  **the three canals' anatomical orientations are the three basis vectors.** **The payload is an
  angular-velocity 3-vector expressed in a basis fixed to the skull** — **the one payload in the map
  that can be stated exactly.**
  **And the basis is oblique.** X-ray computed tomography across **39 mammal species** found
  substantial deviations from orthogonality, angle symmetry and coplanarity to be **the rule**, and
  the degree of deviation is **negatively correlated with estimated vestibular sensitivity** — so the
  departures are **functional, not noise**, and orthogonality is called a **misleading descriptor.**
  **A consumer of this edge cannot assume an orthonormal triad and read components off directly**; it
  needs the actual inter-canal angles, which are a per-species and possibly per-individual parameter.
  **Owed: the human angles.** **So the map's one exact payload has an unknown parameter inside it.**
- **Edge latency.** All edges **to derive.** The transducer's own dynamics are stated: **the velocity
  signal decays with a time constant of 3–5 seconds**, and afferents discriminate head-velocity
  differences of about **2 deg/s** while remaining sensitive to hundreds of deg/s.
- **Invariant conformance.** Co-instantiation: **this structure's output is uninterpretable without
  the otolith line** — see the section invariant. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **A payload change happens before the first synapse, performed by
  fluid mechanics.** The canal is a heavily damped **torsion pendulum**: viscous drag dominates
  inertia, so across the band of natural head movement the mechanics **integrate** the angular
  acceleration that drives them and the afferent's firing is proportional to **velocity**, peaking at
  peak velocity rather than peak acceleration. **The map has no other instance of a transform executed
  outside the nervous system.** The integration is imperfect — hence the 3–5 second decay, and hence a
  **steady rotation is not held**, which the central stage partially repairs.

## Otolith organs

- **Function → structure.** Transduction of **linear acceleration, gravity included and inseparable
  from it.** **Two maculae per ear** set close to orthogonal — the **utricle** roughly horizontal, the
  **saccule** roughly vertical — with hair bundles loaded by an **otoconial mass** of calcium-carbonate
  crystals in a gel, whose **inertia** shears them under acceleration and whose **weight** shears them
  under tilt.
- **Inputs.**
  - **← head linear acceleration and gravity** — mechanical shear by way of the otoconial mass. **Not
    a neural edge.** Fan-in: not applicable.
- **Outputs.**
  - **→ vestibular nuclei**, chiefly lateral and inferior, by the **inferior division** of the
    vestibular ganglion and cranial nerve VIII — the **gravito-inertial acceleration vector**,
    head-fixed, **with a direct-current term**: a maintained tilt produces a maintained signal.
    **Does not carry:** rotation rate, and — the load-bearing negative — **not tilt or attitude
    separately from translation. The two leave the ear summed, and the sum is the signal.**
    Fan-out: to derive.
    - **→ cerebellum** (flocculonodular lobe, nodulus and uvula) (`10_cerebellum`), on the direct
    branch — the same vector, unrelayed. **Two-ended, and this end names the destination
    sub-element** — nodulus and uvula — **where the far end's bundled line names the flocculonodular
    lobe entire.**
- **Sizing.** Basis: **per ear.** **Soft / unknown — no hair-cell or ganglion-cell count is recorded.**
  Same element class and same *to derive, not zero* store as the canal and cochlear hair cells.
  **Structure total: to derive.**
- **Shape.** Rank 2: **(macula, preferred direction).** **Two maculae per ear**, and **the direction
  axis is a distributed code rather than a basis.** In a crista every hair cell shares one directional
  sensitivity; in a **macula** the hair cells are aligned in a **multitude of directions**, with
  polarity reversing across the **striola**. **So the otolith organs do not supply basis vectors; they
  supply a distributed directional code across a population, from which the acceleration direction
  must be decoded rather than read off.** **One sense, two payload formats, and they must not be
  described alike.**
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: as with the canals, **the payload is only interpretable
  in combination with the sibling line**, and the description calls this the clearest such case in the
  source. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The ambiguity is a consequence of physics, not a limitation of the
  organ, and it is total.** Gravity and linear acceleration are indistinguishable to any accelerometer
  — the equivalence principle — so the output is a gravito-inertial vector with **no decomposition**,
  and **neither vestibular organ can provide unambiguous information about head motion and
  orientation.** Resolution requires central convergence, and is declared at the nuclei's end.

## Vestibular nuclei and the central vestibular pathway

- **Function → structure.** The central stage that reads **both** vestibular lines, drives the fast
  reflexes directly, and **computes what neither transducer can sense.** **Four nuclei** — superior,
  medial, lateral, inferior — at the pontomedullary junction. **Attitude is a computed quantity, not a
  sensed one:** the otolith line arrives carrying gravity and acceleration summed, the canal line
  arrives carrying rotation rate, which says how the head has turned relative to gravity, and the
  central neurons combine the two as **an internal model of the physical laws of motion rather than a
  measurement.** Vision and proprioception are combined with them, **which is why the estimate
  survives when one line is degraded and why it can be fooled when vision and the labyrinth
  disagree.**
  **No dedicated primary cortex — the one sense without one.** The cortical representation is
  distributed and inherently multisensory: the **parieto-insular vestibular cortex** (posterior insula
  / parietal operculum / retroinsular, human homologue debated), plus **area 2v**, **area 3a**, and
  the **medial superior temporal** and **ventral intraparietal** areas described elsewhere in the map.
- **Inputs.**
  - **← semicircular canals** (cranial nerve VIII) — head angular velocity, three-axis, head-fixed,
    **no direct-current**. Fan-in: to derive.
  - **← otolith organs** (cranial nerve VIII) — the gravito-inertial vector, **with direct-current,
    tilt and translation unresolved.** Fan-in: to derive.
    - **← cerebellum** (flocculonodular lobe, nodulus and uvula) (`10_cerebellum`) — the return arm of
    the computation, the internal model's correction. Payload otherwise **owed**. **Two-ended**, and
    that file records this as **the one exception to its rule that the cerebellar cortex projects
    nowhere but the deep nuclei.** **This end names the finer origin**, nodulus and uvula against that
    end's flocculonodular lobe.
  - **← the deep cerebellar nuclei**, from the **fastigial** nucleus (`10_cerebellum`) — axial
    posture, balance and eye-movement corrections; payload otherwise **owed**. Fan-in: to derive.
    **Declared at the producer's end only and written here from it.** **This is a second and
    separate cerebellar source**: the line above arrives from the cerebellar *cortex* directly, this
    one from the *output nuclei*, and the two are different structures with different payloads.
    **The far end also bundles this limb with a reticular one and owes that split.**
    - **← vision and proprioception**, by the cortical vestibular areas and the cerebellum — optic flow
    and body configuration, **as the second and third estimates of the same quantity.** Fan-in: to
    derive. **The cerebellar half is consumer-only**: `10_cerebellum` declares no output carrying
    vision or proprioception to this structure, and its two outputs that reach here carry graded
    inhibition and postural correction instead. **Owed: name which cerebellar structure carries this,
    or withdraw the cerebellar half of the route.**
- **Outputs.**
  - **→ oculomotor nuclei (III / IV / VI)** by the medial longitudinal fasciculus — the
    **vestibulo-ocular reflex** command, an eye-velocity signal equal and opposite to head rotation,
    driven chiefly by the canal line.
  - **→ spinal cord** (`16_spinal_cord`) (vestibulospinal tracts) — an antigravity postural command,
    **two-ended and confirmed, and this end is the typed one.** That file carries the
    vestibulospinal limb inside a **five-tract descending bundle** whose payload it marks owed and
    declines to split, because splitting would invent the arity of the five payloads. **This entry's
    line is one of the five and it is typed here**, so the far end's *owed* is accurate for the bundle
    and not for this member. Driven chiefly by the otolith line by way of the lateral nucleus.
    - **→ cerebellum** (`10_cerebellum`) — both lines plus the current estimate. **Two-ended**, and
    **this is the limb that carries a computed quantity rather than a transducer signal**, which the
    far end's bundled afferent line types correctly but cannot attribute, since it names three sources
    under one payload clause.
  - **→ thalamus** (ventroposterior / ventral lateral / intralaminar) **→ parieto-insular vestibular
    cortex, area 2v, area 3a**, and on to the hippocampal formation — **the computed estimate: head
    attitude and self-motion, with gravity separated from linear acceleration. This is not the
    transducer signal, and that distinction is the whole reason the structure exists: what ascends is
    a result, not a measurement.** Fan-out: to derive.
  - **→ the cortical vestibular areas onward** — parieto-insular vestibular cortex → ventral
    intraparietal area → medial superior temporal area, **carrying the same computed estimate in a
    frame that changes at each step**: intermediate between head- and body-centred at the
    parieto-insular cortex, **body-centred** at the ventral intraparietal area, approximately
    **head-centred** at the medial superior temporal area.
- **Sizing.** Basis: **per side** for the nuclei, **per hemisphere** for the cortical areas. **Soft /
  unknown throughout — no clean human counts recorded for the four nuclei or for the parieto-insular
  cortex.** Fan-in to derive. **Structure total: to derive.**
- **Shape.** Rank 2: **(nucleus, cell class)** — four nuclei, and **the cell-class axis is partly
  named by response rather than by place**: type II **vestibular-only** neurons increase firing with
  rotation toward the **contralateral** canal, so the population is distinguished by what it responds
  to and which side drives it, not by where it sits. **Further partition is owed.**
- **Edge latency.** All edges **to derive** — and this is the structure whose **state** time constants
  are stated instead: **velocity storage lengthens the canal line's 3–5 second constant to at least
  15–25 seconds**, a 3× to 8.3× lengthening, recomputed.
- **Invariant conformance.** Co-instantiation: the cerebellar loop and the cortical loop both close
  here, and **the two ascending transducer lines must both be live for the structure's declared
  function to exist at all.** Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **Velocity storage is a named, measured payload change and it is a
  repair rather than a re-expression** — content unchanged, persistence altered. **The map has no
  other edge whose declared transformation is purely temporal**, and it is a useful category: a stage
  that neither adds nor removes dimensions but extends the life of what it receives. **The mechanism
  is owed** — nothing in the description says what implements the integrator.
  **The convergence that resolves the ambiguity is declared as a fact and not as an edge.** Neither
  transducer alone can disambiguate tilt from translation; the resolution is the specific convergence
  of canal and otolith signals onto central vestibular neurons. **The entry declares both inputs and
  does not declare the meeting** — so **the convergence edge, and which cells carry it, is owed**, and
  it is the internal edge that matters most here.
  **The medial superior temporal and ventral intraparietal areas are not direct thalamic targets on
  this line, and the route to them is contested.** There is reported to be **a lack of anatomical
  evidence for a thalamic vestibular projection to the medial superior temporal area**, and response
  dynamics and latency order the three areas **parieto-insular vestibular cortex → ventral
  intraparietal area → medial superior temporal area**, which is what a **cortico-cortical** route
  predicts and not what a shared thalamic input predicts. **Re-deriving the route is owed.**

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Olfactory epithelium — sensory neurons | per side | ~40M (flagged, not independently sourced) | **0** (no neural input, so no count) | **0** |
| Olfactory epithelium — sustentacular, basal | per side | to derive | not a threshold gate | to derive |
| Olfactory bulb — mitral cells | per side | ~50,000 | **10** (fan-in ~800) | **0.063 MB** |
| Olfactory bulb — granule, periglomerular | per side | to derive, and the majority | ≤ 16 | to derive |
| Piriform and primary olfactory cortex | per hemisphere | to derive | ≤ 16 | to derive |
| Gustatory — nucleus of the solitary tract | per side | to derive | ≤ 16 | to derive |
| Gustatory — ventral posteromedial parvocellular nucleus | per hemisphere | to derive | ≤ 16 | to derive |
| Gustatory — anterior insula and frontal operculum | per hemisphere | to derive | ≤ 16 | to derive |
| Semicircular canals — hair cells | per ear | to derive | not a threshold gate | to derive |
| Otolith organs — hair cells | per ear | to derive | not a threshold gate | to derive |
| Vestibular nuclei | per side | to derive | ≤ 16 | to derive |
| Parieto-insular vestibular cortex | per hemisphere | to derive | ≤ 16 | to derive |
| **stated total** | mixed | | | **~0.063 MB** |

**The stated total is 0.063 MB and it is not a small section — it is an uncounted one.** Eleven of the
twelve rows above read *to derive*, and the one that does not is 50,000 cells. Piriform cortex is a
large allocortical area and the insula is a large cortical one; **neither is priced, and the reason is
that no clean human count exists, not that the structures are small.** Against ~1.3 GB for the visual
section and ~484 MB for the auditory, **this section's figure is not comparable to either and must not
be summed with them as though it were.**

**The one derived width in this section is 10 bits, and it is the map's first that is neither zero nor
one.** A receptor-to-mitral convergence of ~800 gives ceil(log₂ 800) = 10, recomputed. **Realised in a
machine integer that becomes 16 bits — 62,500 bytes derived against 100,000 realised, a 60% gap** —
the widest realisation gap in the map so far, because 10 bits is the furthest any derived width has
sat from a container boundary.

**Three facts about extent that are unlike anything in the first two sections.**

1. **An axis that exists physically and indexes nothing** — position in the olfactory epithelium.
2. **An extent that is exact, small, and physical** — three canals per ear, whose orientations *are*
   the basis vectors of the payload. **And that basis is oblique, with the human angles owed**, so the
   map's one exactly-stateable payload still has an unknown parameter inside it.
3. **An extent that varies 3.1× between individuals** — 3,000 to 9,300 glomeruli per bulb, recomputed
   from the stated range. **The axis length is not a property of the species.**

**A consequence the description does not draw.** The glomerulus-per-receptor-type convergence depends
on a receptor count the source records as contested. Recomputed: **13.9 : 1 to 15.9 : 1** if there are
350–400 intact types, **27.8 : 1 to 55.7 : 1** if there are 100–200. **The same measured glomerular
count supports a four-fold range of convergence**, and the contest therefore propagates into the shape
rather than staying in the epithelium's prose.

**This section is the map's control condition on maps, and it behaves like one.** There was never a
topographic map here to over-state: chemotopy in the bulb is a map of chemical similarity and is
**discarded** at the next synapse; gustotopy was claimed and contradicted, with the verdict **no map, a
spatial population code**; and vestibular sensation has no map and no dedicated primary cortex.
**Both chemical senses arrive at cortex as distributed population patterns over a non-spatial quality
space.**

**The total is a floor, and more so than in either previous section.** Every structure but one is
unpriced, the hair-cell store is *to derive and not zero* as it was in the auditory section, the
epithelium's own count is flagged as un-sourced, and **state memory and edge storage are not in the
table at all.** Edge storage would bite differently here than in the auditory section: **this section's
constraint is not a short interval but a long horizon** — state that must persist 15–25 seconds — and
**the two constraints together span about 6.4 orders of magnitude, which no single update interval
serves comfortably.** That figure cannot be turned into a number until the scheduling discipline is
set, and it is not.

**Memory is not a binding constraint and none of these figures is to be reduced.**
