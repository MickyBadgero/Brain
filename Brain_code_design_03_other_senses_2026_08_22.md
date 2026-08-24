# Brain code design — 03 other senses

**Date:** 2026-08-22
**Derived from:** `Brain_architecture_03_other_senses`, `Brain_code_design_spec`,
and CLAUDE.md. **No other content source.**
**Implements:** `Brain_03_other_senses.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
character for character, so that at coding time only this file is loaded. **One deviation from that
copy, and it is declared here so that anything else is a defect.** The architecture's **internal
cross-references** — *see above*, *see the section invariant*, *declared at the nuclei's end* — are
not copied, because they point at fields this rung does not have; their content is carried at the
entry it belongs to.

**Seven entries, one per architecture entry, same names, same order.**

**One of the seven is a bundle and stays one.** The gustatory entry carries **three stages** — the
nucleus of the solitary tract, the ventral posteromedial parvocellular thalamic nucleus, and the
anterior insula with the frontal operculum — inside one slot set. Per spec §1 the design entry is a
bundle too, and **the split is owed at the source.** Splitting it here would invent the arity two
rungs below where the arity is known.

---

## What is open for every entry in this file, stated once

Repeating these seven times would make the file longer without making it truer. Each entry names only
what is open **beyond** this list.

- **Emission — graded or binary, and the unit's expressiveness.** The centre–surround / threshold-gate
  question, and it is **Micky's**. The architecture's sizing model charges each neuron `log₂(fan-in)`
  bits, which is what a threshold over equal-weight inputs would store — *(that reading is Claude's
  inference from the Sizing fields, constrained by them and not stated in them)*. Until Micky sets it,
  **no entry below writes an update equation as though the answer were given.**
- **The scheduling discipline.** Micky's, and the largest open item at this rung. No entry contains a
  loop, a step counter, or a `for t in range(...)`.
- **The learning rules.** Micky's. Every Adaptation field reads *none set*. A threshold that is never
  written is a construction cost and not a memory, which is why the entries are still coherent without
  one.
- **Inter-structure connection topology.** Fan-in is given above as a **scalar per structure**; the
  code needs it as a **map** — which source lines converge on which unit. A convergence count is not a
  convergence pattern. Surface-before-touching.
- **Tile geometry and sparsity.** Both surface-before-touching, both unset, and every array extent
  below is therefore symbolic.
- **Every edge latency in this section reads *to derive*.** The architecture states this positively,
  and this section is nonetheless the first in the map that states time constants at all — **which are
  not edge latencies.** See the next item, because it is the discipline this whole section turns on.
- **Edge storage cannot be closed anywhere in this file.**
  `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`. Latency is *to
  derive* on every edge here, the update interval waits on the scheduling discipline, and bytes per
  value waits on the emission question. Each entry records its **edge count** and its **line count
  status**, which is the term this rung can supply. **Never summed with parameter memory or state.**

### A time constant is not an edge latency, and this section is where the two would be confused

The architecture states it flatly and it is repeated here because it governs three of the seven
entries: **an edge latency says when a signal arrives; a time constant says how long a stage holds
what it received.** The per-edge-latency invariant is about the first, and this section supplies only
the second.

- The canal afferent's velocity signal **decays with a time constant of 3–5 seconds**.
- The central percept, the nuclei's activity, and the nystagmus following a step change in head
  velocity all have a time constant of **at least 15–25 seconds**, produced by the **velocity storage
  integrator** — a **3× to 8.3× lengthening**.

Both belong in the **State carried between updates** field, never in **Edge latency**, and the entries
below put them there. A design that wrote 3–5 s into an edge latency field would have manufactured the
only stated timing in the section out of the only fields that have none.

**And the constraint the two sections together place on the scheduling decision.** File 02 states a
computation working at **tens of microseconds**; this file states state that must persist **15–25
seconds**. 25 s against 10 µs is a ratio of **2.5 × 10⁶ — about 6.4 orders of magnitude, ~21 bits of
time.** **No single update interval is comfortable across that span.** That figure cannot be turned
into a number until the discipline is set, and it is not; it is recorded here because it is a
constraint on Micky's decision that neither section produces alone.

### Element classes in this section, because four of the seven entries are not threshold gates

- **Transducers** — the olfactory sensory neuron, the taste receptor cell, the canal crista, the
  otolith macula. Not threshold gates, store no threshold, and the log₂ cost does not apply. Their
  input edges are **chemical** and **mechanical arrivals**, not projections, and fan-in reads *not
  applicable* rather than underived.
- **Graded, non-spiking elements** — the vestibular hair cells, which are **not neurons** and are the
  same class as the cochlear hair cells. Their store is **to derive and not zero.** Zero would assert
  they hold nothing; `log₂(fan-in)` would assert a threshold they do not have.
- **A fifth class of internal transfer, which is not an edge and must not be written as one.** In the
  olfactory epithelium the basal stem cells produce new sensory neurons throughout life; that line is
  **a developmental transfer carrying no signal.** Writing it as an edge would put a signal path in the
  code that does not exist. **A structure that continuously rebuilds its own front end has no
  representation in an architecture of fixed arrays**, and that is a finding rather than an omission.

**Two new classes of non-neural arrival, bringing the map's total to four.** After light at the retina
and sound at the cochlea: **chemical arrival** — odorant molecules dissolved in the olfactory mucus,
and tastants at the taste buds; and **mechanical arrival, twice and by two different mechanisms** —
head rotation reaching the cupula through the inertial lag of the endolymph, and head linear
acceleration reaching the hair bundles through the weight and inertia of the otoconial mass. Fan-in on
all of them: **not applicable.**

**Counting basis is not uniform in this section.** Per side at the olfactory epithelium and bulb, per
ear at the vestibular transducers, per hemisphere where a cortical figure exists. **Six of the seven
structures carry no neuron count at all.**

**Cross-file endpoints carry the far file's stem.** Two far files are reached from this section with a
stem: `14_brainstem_midbrain_hypothalamus` and `16_spinal_cord`. Every other named far end in this
section arrives **without a stem**, which means its file has not been opened beside this one — not that
no far end exists.

---

# 1. Olfactory epithelium

## Contract

**Inputs.**
- **← airborne odorant molecules dissolved in the mucus** — chemical identity and concentration.
  **A chemical arrival, not a neural edge.** Fan-in: not applicable.
- **← centrifugal modulation of the epithelium** — **payload owed**; whether this edge exists at all
  is what the description declines to assert.

**Outputs.**
- **→ olfactory bulb**, by the olfactory nerve, onto the **glomeruli** — one component of a
  **combinatorial chemical code**: a single neuron reports how strongly its one receptor type is
  occupied, and the odour's identity exists only in the pattern across types. **Not a scalar, not a
  map of space, and not frequency-analysed the way the cochlear output is — there is no ordering of
  the chemical dimension corresponding to the tonotopic axis.** Fan-out: **one or two glomeruli**
  per axon.

**Sizing.** Basis: **per side.** **~40 million sensory neurons**, and the description flags the
figure as **inherited from the bulb entry, not independently sourced, with human estimates varying
widely.** **Store: zero, and for a reason the model already contains.** The cell has **no neural
input**, so there is no count of active inputs to compare against a threshold, exactly as for a
fan-in of one. **The caveat is that the model's count has no referent here at all**: what this cell
thresholds is receptor occupancy, and occupancy is not an input line. **Structure total: 0, with
that caveat.**

**Shape.** **Sheet**, rank 2: **(receptor type, position in the epithelium)** — and **the position
axis carries no information.** The description is explicit: the signal is not spatial, there is no
receptor sheet mapping the world, and position in the epithelium says nothing about where the
odorant came from. **This is the first axis in the map that exists physically and indexes nothing.**
Receptor-type extent: **contested** — 350–400 intact types on one reading, 100–200 on another, a
disagreement the description records without taking a side.

**Edge latency.** All edges **to derive.** One qualitative fact: the olfactory nerve is
**unmyelinated**, which is part of why olfactory conduction is slow — the opposite of the auditory
brainstem's heavy myelination, and stated for the same kind of reason.

## Representation — declared once per line, inherited by every consumer

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| odorant molecules → cilia | chemical identity and concentration | to derive | **event-driven** — a chemical arrival; the sheet has no sampling rate of its own recorded | **none** — chemical identity is not a coordinate |
| → olfactory bulb, onto glomeruli | receptor occupancy, per receptor type | to derive | event-driven | **none — a combinatorial code over receptor types.** Not a scalar, not spatial, and **not ordered**: there is no chemical axis corresponding to the tonotopic one |
| ← centrifugal modulation | **owed** | owed | owed | owed — **and whether the line exists at all is what the description declines to assert** |

**The frame column is the load-bearing one here and it is why the field exists.** Every sensory line
in the first two sections of the map arrives with a coordinate frame — retinotopic, tonotopic. This
one has none, and the absence is a positive statement rather than a gap: **a consumer that allocated an
ordered axis for the chemical dimension would be asserting a neighbourhood relation the biology does
not have.** The bulb's entry is where a neighbourhood does appear, and it is chemical rather than
spatial.

## Algorithm

- **Transform.** **Chemical transduction**, and **no standard engineering or computer-science name
  fits it — which spec §5 says is a finding about the structure, and it is recorded as one.** What the
  architecture supplies is a **mechanism**, not an operation over arrays: odorant binds, a G-protein
  cascade raises cyclic adenosine monophosphate, a cyclic-nucleotide-gated channel opens, and a
  calcium-activated chloride current amplifies. **The amplification is biochemical and private to each
  cell**, where the cochlear amplifier is mechanical and shared across cells. **A picture of an
  operation is not an operation**, and this rung does not turn the cascade into arithmetic.
- **The one-neuron-one-receptor rule is the structural fact the arrays are built on.** Each sensory
  neuron expresses **exactly one** olfactory receptor gene, chosen stochastically and then held. Every
  neuron expressing a given receptor is **scattered across a broad zone rather than clustered**, and
  sends its axon to **the same one or two glomeruli** — **and the receptor protein itself steers the
  axon there.** So the sorting that builds the bulb's chemotopic map is **done by the receptor
  molecule, not by a topographic projection.**
  **The consequence for the code is exact and it is the reason the position axis can be carried at
  all**: the mapping from `(receptor_type, position)` to glomerulus **does not depend on position.**
  A projection built by sampling a neighbourhood in the position axis would be building the wrong
  thing. *(The architecture states the receptor-steered sorting; that a position-indexed projection is
  therefore the wrong construction is Claude's reading, constrained by it.)*
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `receptor_occupancy` | (R, P) | open — emission question | to derive | fractional occupancy |
  | `sensory_neuron_output` | (R, P) | open — emission question | to derive | to derive |
  | `receptor_type_of_neuron` | (R, P) → glomerulus index | integer index | 0 … G−1 | one or two
  glomeruli per axon |

  **R is contested and P is to derive.** R — the receptor-type extent — is **350–400 on one reading and
  100–200 on another**, and spec §5b forbids writing *to derive* over a **contested** state: contested
  means measured and yielding several readings that disagree, and needs adjudication between existing
  results rather than a new measurement. **The array cannot be allocated until R is adjudicated**, and
  that adjudication belongs at the source rung, not here.
  **P — position in the epithelium — is an axis that exists physically and indexes nothing.** It has
  to be carried, because the neurons occupy positions and the count is over them; it must not be
  indexed by any consumer, because position says nothing about where the odorant came from.
  **There is no threshold array**, because the store is zero.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `sensory_neuron_count` | cells per side | ~40,000,000 | architecture Sizing — **flagged there as
  inherited from the bulb entry, not independently sourced, human estimates varying widely** |
  | `receptor_type_count` R | types | **contested: 350–400 or 100–200** | architecture Shape |
  | `glomeruli_per_axon` | glomeruli | 1–2 | architecture Outputs, fan-out |
  | `position_extent` P | cells | to derive | not supplied above |

- **Update equation.** **Waiting on the emission question, and on a second thing this entry has that
  no other in the file has: what a transducer computes is not specified at any rung above.** The
  cascade is a mechanism and not arithmetic. What is fixed regardless of both answers: **one neuron
  reports occupancy of one receptor type**, and identity exists only across types — so **no equation
  at this stage may combine across the R axis.** Combination is the bulb's, and it is inhibitory.
- **State carried between updates.** **To derive.** The cascade plainly has state — a second-messenger
  concentration is state by construction — and **the architecture states no time constant, no
  adaptation rule and no initial value for it.** Recorded as owed at the architecture rung rather than
  supplied here. **State memory is not parameter memory and the two are never summed.**
- **Edge storage.** 1 chemical arrival, 1 output edge, 1 input edge whose existence is owed. Line count
  = `sensory_neuron_count × glomeruli_per_axon`, so **40M × 1–2** — the one line count in this section
  that is nearly closed, needing only the fan-out to be pinned within its stated 1–2. Latency to
  derive. Interval unset. Bytes per value unset. **Not summable.**
- **Adaptation.** **None set** as a learning rule. **And this entry carries a structural fact that is
  not a learning rule and must not be filed as one:** the basal stem cells replace the sensory neurons
  for life. The architecture types that line as **a developmental transfer carrying no signal**, and it
  is not an edge. **Lifelong regeneration is an architectural fact, not a maintenance detail: whatever
  holds the map stable cannot be the individual cells, because they are replaced.**
  **The design consequence, stated as the finding it is:** the arrays above are fixed-extent, and the
  population they describe is not. **Nothing at any rung says what a turning-over population is in
  code.** Not patched here; recorded.
- **Open, beyond the standing list.**
  - **R is contested** and the array cannot be allocated until it is adjudicated. Source rung.
  - **P is to derive** — no epithelial extent is supplied.
  - **Whether the centrifugal edge onto the epithelium exists at all.** The architecture declines to
    assert it, and marks its payload owed. **This is the gain loop onto the chemical front end that the
    section cannot confirm exists** — the auditory equivalent closes, and here co-instantiation cannot
    be shown to be satisfied for that loop, because there may be no loop.
  - **What a transducer computes**, unspecified at every rung above.
  - **State: the cascade's time constant, adaptation and initial value.** Owed at the architecture rung.
  - **A turning-over population has no representation in fixed arrays.**

---

# 2. Olfactory bulb

## Contract

**Inputs.**
- **← olfactory epithelium** — the combinatorial chemical code, as a **pattern across ~5,500
  glomeruli**. **Fan-in: ~800 : 1** receptor-to-mitral convergence. **There is no topography of the
  world here: the map is chemotopic, and adjacency means chemical similarity.**
- **← piriform cortex** (feedback) and **← basal forebrain / raphe / locus coeruleus** (centrifugal
  neuromodulation) — gain and state, no chemical content. Payload otherwise **owed**.

**Outputs.**
- **→ piriform and the rest of primary olfactory cortex**, by the **lateral olfactory tract**, and
  also to anterior olfactory nucleus, olfactory tubercle, cortical amygdala and rostral entorhinal
  cortex — the **decorrelated glomerular pattern**, sharpened by inhibition, chiefly ipsilateral,
  and **straight to cortex with no thalamic relay and therefore no thalamic gate.** Fan-out: to
  derive.

**Sizing.** Basis: **per side.** **Glomeruli ~5,568 ± 830 per bulb** (range ~3,000–9,300, verified
human); **mitral cells ~50,000 per bulb** (verified human). **Fan-in ~800 gives ceil(log₂ 800) = 10
bits** — **so this is the second exactly-derived width in the map, after the auditory zero-cost
fan-ins, and the first that is neither zero nor one.** Mitral-cell store: **50,000 × 10 bits = 62,500
bytes = 0.063 MB.**
**Interneurons vastly outnumber the projection neurons**, so the bulb's total is
**interneuron-dominated and soft** — recorded as *to derive*, and it is the larger term.
**Structure total: ~0.063 MB firm, plus an interneuron store that is to derive and is the majority
of it.**

**Shape.** Rank 3: **(lamina, glomerulus, cell class)** — six laminae, ~5,568 glomeruli, and cell
classes the description does not fully partition. **The glomerular axis is the one indexable axis in
this section, and its index is chemical identity rather than space.**
**Two extent problems, and both are real numbers rather than gaps.** First, the glomerular count
ranges **3,000–9,300 across individuals — a 3.1× spread**, so the axis length is not a
property of the species. Second, **the convergence ratio the description states depends on the
contested receptor count**: 5,568 glomeruli over 350–400 types is **13.9 : 1 to 15.9 :
1**, but over 100–200 types it is **27.8 : 1 to 55.7 : 1**. **The same measurement supports a
four-fold range of glomerulus-per-receptor-type convergence**, and that consequence follows from the
contest the epithelium entry records without being stated there.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← olfactory epithelium | receptor occupancy per type | to derive | event-driven | **chemotopic** — adjacency in the glomerular axis means **chemical similarity**, not spatial proximity |
| ← piriform cortex (feedback) | **gain and state, no chemical content** | owed | event-driven | owed |
| ← basal forebrain / raphe / locus coeruleus | **gain and state, no chemical content** | owed | event-driven | owed |
| → piriform and the rest of primary olfactory cortex | the **decorrelated** glomerular pattern | to derive — **normalised, and that is the payload change** | event-driven | **chemotopic leaving here, and discarded at the far end.** The consumer's own entry records that the projection is non-topographic |

**Three of the four lines carry no content and set gain.** The feedback and the two neuromodulatory
lines are declared with **no chemical content**, so a forward operation that summed all inputs alike
would be reading a gain as evidence. **The role belongs on the line, not inferred at the consumer.**

**The last row is where two entries' representations must be read together.** The pattern leaves here
chemotopic and the consumer discards the chemotopy at the synapse. **That payload change is real, it
is the thing that makes the consumer's function possible, and the architecture records that it is not
stated in the consumer entry's own edge fields.** A design that inherited the frame from this line and
allocated a chemotopic array at the far end would be right at the producer and wrong at the consumer.

## Algorithm

- **Transform.** **Named as four operations rather than as one transform, and the architecture says so
  explicitly:** gain control, contrast enhancement, spatial decorrelation, temporal synchronisation.
  **What is not in that list matters as much:** no change of reference frame, no binding, no
  categorisation. **The payload leaves in the format it arrived in — a pattern over glomerular channels
  — cleaned up.** This is the clearest case in the map of a stage whose payload change is a
  **normalisation rather than a re-expression.**
  **Three of the four names are functional and not operational, and that is a finding rather than a
  gap to fill.** *Gain control* and *contrast enhancement* each have obvious standard candidates —
  divisive normalisation, a difference-of-fields — and **neither is written here**, because the
  architecture supplies the name and not the arithmetic, and the candidate that suggests itself is the
  centre–surround question on §10's list. *Temporal synchronisation* has no candidate at all while the
  scheduling discipline is unset: **synchronisation of what, against what clock, is the discipline
  question wearing a biological name.**
- **Lateral inhibition here operates over a non-spatial neighbourhood, and this is the item most
  likely to be got wrong in code.** Short-axon cells inhibit between glomeruli, and because glomerular
  adjacency is **chemotopic**, *lateral* means **lateral in chemical similarity.** Every other instance
  of lateral inhibition in the map operates over a map of the world.
  **The design consequence:** a neighbourhood operator over the glomerular axis needs a **chemical
  similarity metric**, and **no rung above supplies one.** A convolution over adjacent glomerular
  indices is the thing a coder would reach for and it would be asserting that index adjacency equals
  chemical similarity — which is what the chemotopic claim says qualitatively and does not quantify.
  **Recorded as owed at the architecture rung**, not filled here. *(The architecture states the
  chemotopy and the inhibition; that an index-adjacency convolution would over-claim is Claude's
  reading.)*
- **The dendrodendritic reciprocal synapse has no representation in a directed-edge model.** The
  **mitral / tufted lateral dendrite ↔ granule cell spine** synapse is **reciprocal** — **one synaptic
  apposition carrying signal in both directions, not two edges.** **An architecture that assumes edges
  are directed must special-case it.**
  **The consequence at this rung is concrete and it lands on the shared vocabulary:** an `Edge` with a
  source and a target is directed by construction, so writing this as two edges asserts two synapses
  where there is one, and writing it as one asserts a direction it does not have. **The code declares
  it once and marks it**, and what a reciprocal apposition *is* in code is **owed and is Micky's**,
  because it is a change to the shared edge type. *(The single-apposition physiology is from the
  architecture; that the directed `Edge` type cannot express it is Claude's reading.)*
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `glomerular_pattern` | (G,) | open — emission question | to derive | receptor occupancy, pooled |
  | `mitral_active` | (G, C_mitral) | open — emission question | to derive | to derive |
  | `mitral_threshold` | (G, C_mitral) | **width 10 bits derived**, realised 16 | 0 … 800 | count of
  active inputs |
  | `granule_state` | (L, G, C_granule) | open | to derive | to derive |
  | `periglomerular_state` | (L, G, C_pg) | open | to derive | to derive |

  **G ≈ 5,568 and is not a species constant.** The range across individuals is **3,000–9,300, a 3.1×
  spread**, so **the axis length is a per-individual parameter and not a fixed extent.** Allocating
  5,568 asserts a species value the measurement does not support. **This is the first array extent in
  the map whose correct value is a distribution rather than a number**, and what the code does about
  that is owed. *(The spread is the architecture's; that it makes the extent a parameter rather than a
  constant is Claude's reading.)*
  **The cell-class axes C are not partitioned.** The architecture says the description does not fully
  partition the cell classes, and the six laminae are named while the counts do not divide among them.
  **An array for one lamina cannot be sized however well the lamina is described.**
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `glomerulus_count` G | glomeruli per bulb | **~5,568 ± 830, range 3,000–9,300** | architecture
  Sizing, verified human |
  | `mitral_count` | cells per bulb | ~50,000 | architecture Sizing, verified human |
  | `mitral_fan_in` | contacts per mitral cell | ~800 | architecture Inputs |
  | `mitral_threshold_bits` | bits | **10**, from `ceil(log₂ 800)` | derived from the two above |
  | `lamina_count` | laminae | 6 | architecture Shape |
  | interneuron counts | cells | to derive, **and the majority of the store** | not supplied above |

- **Update equation.** **Waiting on the emission question**, and on the chemical-similarity metric the
  lateral inhibition needs. What is fixed regardless of both answers: **the output format equals the
  input format.** Whatever the four operations are, they do not change the axis, the frame or the
  dimensionality — **content in, content out, normalised.** An equation that emitted a different kind
  of object here would be wrong on the architecture's own terms.
- **State carried between updates.** The granule and periglomerular arrays, and whatever the four
  operations hold. Time constants and initial values: **to derive at every one.** **State memory is not
  parameter memory and the two are never summed.**
- **Edge storage.** 1 input edge, 3 modulatory or feedback input edges, 1 output edge to a named set of
  six targets. Line count into the bulb = **G × mitral_fan_in ≈ 5,568 × 800**, which is the one input
  line count in this section that closes; the output line count needs a fan-out that is to derive.
  Latency to derive on all of them. Interval unset. **Not summable.**
- **Adaptation.** **None set.**
  **And this entry carries the project's own most-cited counter-example, which is why it is recorded
  and not acted on.** In rodents the bulb is a lifelong neurogenic region, ~95% of added cells becoming
  inhibitory granule cells, and is **the canonical example of a circuit holding stable representations
  while its own components are replaced.** **In humans it appears not to happen**: carbon-14 dating
  found adult bulbar neurogenesis extremely limited, migration reported only up to about 18 months,
  with human neuroblasts migrating toward the **striatum** instead — a different destination, not a
  reduced one. **If that holds, the most-cited mammalian instance of continuous structural learning is
  not a human mechanism.** The caveats are in the architecture and are carried with the claim: the
  cohort was forensic material weighted toward neuropsychiatric disease, and **a negative in that
  sample is not a negative in the species.** Also carried: in rodent, reducing granule cells impairs
  odour **discrimination** while leaving **detection thresholds** and short-term olfactory memory
  intact, so **the link from neurogenesis to learning is real but neither simple nor monotonic.**
  **Nothing is designed from this either way.** It bears on a learning rule, learning rules are Micky's,
  and a design that quietly adopted the rodent finding would be choosing one.
- **Open, beyond the standing list.**
  - **The chemical similarity metric** the lateral inhibition operates over. Architecture rung.
  - **What a reciprocal dendrodendritic apposition is in code.** Micky's — it changes the shared edge
    type.
  - **G is a distribution, not a constant**, and what the code allocates against is owed.
  - **The interneuron counts**, which are the majority of the store.
  - **The cell-class partition**, which the description does not supply.
  - **The four operations' arithmetic**, none of which is licensed from above.
  - **The output fan-out**, to derive, which blocks the output line count.

---

# 3. Piriform and primary olfactory cortex

## Contract

**Inputs.**
- **← olfactory bulb**, lateral olfactory tract, **monosynaptic**, onto **layer Ia** — the sparse
  glomerular odour pattern. Fan-in: to derive.
- **← its own recurrent associational fibres**, onto **layer Ib and III** — the network's own state;
  the feedback that completes a partial pattern. Fan-in: to derive.
- **← orbitofrontal and entorhinal cortex, amygdala, neuromodulatory nuclei** — context, value and
  state. Payload otherwise **owed**.

**Outputs.**
- **→ orbitofrontal cortex**, directly and by the mediodorsal thalamus — the **odour object**: a
  completed, content-addressed identity rather than a receptor pattern. **As at the inferotemporal
  cortex, the payload has become a category — "which smell", not "how much of what chemical."**
  Fan-out: to derive.
- **→ amygdala** — the odour object, for hedonic and emotional evaluation.
- **→ entorhinal cortex → hippocampal formation** — the odour object as an element of an episode.
- **→ hypothalamus**, and **→ olfactory bulb** (reciprocal feedback) — payload **owed**.

**Sizing.** Basis: **per hemisphere.** **Soft / unknown — no clean human per-area count.** Fan-in to
derive. **Structure total: to derive**, and this is a large allocortical area, so the absence is not
a small term.

**Shape.** **Sheet**, rank 3: **(lamina, cell class, position)** — five laminar sub-elements, three
principal cell classes, **and a position axis that is not indexable.** The bulb→piriform projection
is **famously non-topographic**: a glomerulus's output is distributed broadly across the sheet
rather than to a matched location, **so the chemotopy present in the bulb is discarded at this
synapse.** The association fibres are non-topographic too, so nothing restores it, and **there is no
spatial mapping of odour-evoked activity anywhere in this structure.**
**One possible exception, and it would be a kind of map the map has no other instance of:** a spatial
organisation by **efferent target** rather than by input — tissue ordered by where its cells project
rather than by what they receive. **Owed.**

**Edge latency.** All edges **to derive.** One structural fact stands in for one: **it is two
synapses from the outside world**, receptor → bulb → here, with **no thalamic relay and therefore no
gate that can be closed** — and every other primary sensory cortex in the map sits behind one.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← olfactory bulb, onto layer Ia | the sparse glomerular odour pattern | to derive | event-driven | **arrives chemotopic and is discarded at this synapse.** The projection is non-topographic: **no frame on this side** |
| ← own recurrent associational fibres, onto Ib and III | **the network's own state** | to derive | event-driven | **none** — non-topographic, and nothing restores the bulb's chemotopy |
| ← orbitofrontal / entorhinal / amygdala / neuromodulatory | context, value and state | **owed** | event-driven | owed |
| → orbitofrontal cortex | **the odour object — a category** | to derive | event-driven | **none — a category has no coordinate frame** |
| → amygdala | the odour object | to derive | event-driven | none |
| → entorhinal cortex → hippocampal formation | the odour object, as an element of an episode | to derive | event-driven | none |
| → hypothalamus; → olfactory bulb (reciprocal) | **owed** | owed | event-driven | owed |

**The payload changes kind at this structure and the frame column is where that shows.** The input is
*how much of what chemical*; the output is *which smell*. **That change is the entry's whole function
and the architecture records that it is not stated in the entry's own edge fields** — it is written
into the Outputs payload and nowhere typed as a transformation. Carried here at the line, which is
where a consumer will read it.

## Algorithm

- **Transform.** **A content-addressable autoassociator**, and **this is the one entry in the section
  where a standard name does fit** — the architecture names it directly: associative,
  content-addressable recurrent processing, supporting identification, **pattern completion**, and
  rapid olfactory learning. Anterior piriform is weighted to identity, posterior to category and
  association.
  **The name is licensed and the arithmetic is not, and the gap between those two is the whole of this
  field.** An autoassociator implies a storage rule and a recall dynamics, and **both are learning
  rules, which are Micky's.** Writing an energy function, a Hebbian outer-product store, or a recall
  iteration here would be choosing the learning rule at the rung below the one that owns it — and it
  would read exactly like a derived equation, which is the defect class that is hardest to catch.
  **No update equation is written. The name is recorded; the rule is asked for.**
- **The afferent / associational segregation is strict and it sorts the cell classes — so the
  populations are not interchangeable and an array per lamina is not enough.** Afferent fibres from the
  lateral olfactory tract land in **Ia**; associational fibres in **Ib through III**. **Semilunar
  cells** (IIa) are afferent-dominated and carry large spines in Ia but not in Ib; **superficial
  pyramidal cells** (IIb) take weaker afferent and stronger associational drive; **deep pyramidal
  cells** (III) are mostly driven by the recurrent circuit and receive the strongest recurrent
  inhibition. **So "sensory-driven" and "self-driven" are not two states of this network but two
  populations in it, ordered by depth.** **Semilunar cells send no feedback to the bulb** while the
  pyramidal cells do — **the afferent-dominated class is the one that does not talk back.**
  **The code consequence:** the recurrent input array and the afferent input array **address different
  cell classes with different weights**, and the bulb-feedback output array **is not addressed by the
  semilunar population at all.**
- **Two inhibitory systems, each scoped to one input class.** Layer I horizontal and neurogliaform
  interneurons take direct tract input and synapse on apical dendrites, scoped to the **afferent**
  stream; layer II/III bitufted regular-spiking interneurons take little tract input and synapse on
  somata and basal dendrites, scoped to the **associational** stream. **One structure, two inhibitory
  systems, each guarding its own input class.** **A single inhibition array over the structure would
  merge two systems the architecture separates.**
- **The same-dendrite, different-depth geometry recurs here for the fourth time in the map**: sensory
  input and network feedback arriving on one apical dendrite at different depths, as at the cortical
  layer-1 tuft, the dorsal cochlear nucleus's fusiform cell, and the medial superior olive's bipolar
  cell. **At four instances across four unrelated structures this is a pattern rather than a
  coincidence, and it is specific: the two streams are separated by distance along a dendrite rather
  than by different cells.**
  **The design consequence is the sharpest in this file:** a **single-compartment unit cannot express
  it.** One unit summing both streams has merged exactly what the geometry separates, and the
  separation is not a detail of the biology — it is what lets the same cell treat afferent drive and
  network feedback differently. **Whether a unit has compartments is a change to the unit's
  expressiveness, which is §10's list and is Micky's.** Recorded and not chosen. *(The four instances
  and the geometry are the architecture's; that a single-compartment unit cannot carry it is Claude's
  reading.)*
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `semilunar_active` | (P,) | open — emission question | to derive | to derive |
  | `superficial_pyramidal_active` | (P,) | open | to derive | to derive |
  | `deep_pyramidal_active` | (P,) | open | to derive | to derive |
  | `afferent_inhibition_state` | (P,) | open | to derive | layer I horizontal / neurogliaform |
  | `associational_inhibition_state` | (P,) | open | to derive | layer II/III bitufted |
  | `*_threshold` per principal class | (P,) | width `ceil(log₂(fan_in))`, **fan_in to derive**,
  bounded 16 | 0 … fan_in | count of active inputs |

  **P is not indexable and it is also not sized.** The position axis has no spatial meaning — the
  projection into it is non-topographic and nothing restores the bulb's chemotopy — **and no count
  exists to give it an extent.** Both are true at once and they are different problems: an axis that
  indexes nothing can still be allocated once its length is known, and this one's length is not.
  **Three principal cell classes and five laminar sub-elements**, with no partition of any count among
  them, because there is no count.
- **Parameters.** **None has a value.** `piriform_neuron_count` — **soft / unknown, no clean human
  per-area count**, origin: architecture Sizing. `afferent_fan_in`, `associational_fan_in` — to derive,
  bounded ≤ 16 bits. **This is a large allocortical area and the absence is not a small term.**
- **Update equation.** **Waiting on the learning rule and on the emission question.** What is fixed
  regardless of both: **the recurrent edge is load-bearing rather than incidental**, so any equation
  must read the network's own state on the same update in which it reads the afferent drive; and the
  two must arrive **separably**, because the cell classes and the two inhibitory systems distinguish
  them.
- **State carried between updates.** The network's own state — **which here is not an implementation
  detail but the payload of a declared input edge.** The recurrent associational fibres are an input
  line carrying *the network's own state*, so this structure's state is **typed at an edge** and not
  only held in an array. Shapes as above; initial values to derive; the point in the update at which
  it is written is fixed by the recurrence and not by a clock.
- **Edge storage.** 3 input edges (one of them the recurrent line, whose two ends are both here), 5
  output edges. Line counts: all to derive, since neither the population count nor any fan-in or
  fan-out is supplied. Latency to derive. Interval unset. **Not summable.**
- **Adaptation.** **None set** — and this is the entry where that costs the most, because **the
  structure's stated function is rapid olfactory learning.** An autoassociator with no storage rule can
  be allocated and cannot be run. **The entry is honest about that rather than filling it.**
- **Invariant note carried from the architecture, because it constrains the code directly.** The
  recurrent associational edge is **the map's only declared intra-regional recurrent edge that is
  load-bearing for the entry's stated function** rather than noted in passing. **A staged bring-up that
  omitted it would not have a degraded autoassociator; it would have no autoassociator.** So this
  structure and its own recurrence come up together or not at all.
- **Open, beyond the standing list.**
  - **The storage and recall rules** of the autoassociator. Micky's, and the entry cannot run without
    them.
  - **Whether a unit has compartments**, without which the same-dendrite different-depth geometry
    cannot be expressed. Micky's.
  - **P — no count, no extent, and no spatial meaning.**
  - **The possible organisation by efferent target**, owed at the architecture rung, and it would be a
    kind of map the map has no other instance of.
  - **A challenge to the laminar account, recorded not smoothed:** a single Golgi study reports
    afferent fibres penetrating beyond layer I into layer II, which would make the segregation strict
    only to first order. **The arrays above assume the strict version**, because that is what the
    architecture states; if the challenge holds, `afferent_inhibition_state`'s scoping is wrong.
  - **A chemical pathway the description does not carry as one, and it is not an edge in this entry.**
    Nasal irritants are transduced by **nociceptive free endings of the trigeminal nerve** and ride the
    somatosensory route to cortex, with two edges connecting them to olfaction proper — trigeminal
    collaterals to the epithelium and bulb, and carbon dioxide evoking piriform responses. **The
    protective-warning reading of that channel is wrong and the correction matters:** trigeminal
    thresholds are about **100 times higher** than olfactory ones, so **the irritant channel fires
    later and at higher dose, not earlier**; what it supplies is **damage-limitation reflexes** that
    reduce further intake after intake has occurred. **Detection in these modalities never precedes
    exposure — the molecule must already be inside.** No array or edge is written for it here, because
    the architecture does not carry it as a pathway.

---

# 4. Gustatory pathway

**This entry is a bundle and stays one.** It carries **three stages** — the nucleus of the solitary
tract, the ventral posteromedial parvocellular thalamic nucleus, and the anterior insula with the
frontal operculum. Per spec §1, **the design entry is a bundle too, and the split is owed at the
source.** Splitting it here would invent the arity two rungs below where the arity is known, and it
would do it to a stage whose file ownership is itself unresolved — see Open.

## Contract

**Inputs.**
- **← taste buds**, by cranial nerves VII, IX and X → rostral **nucleus of the solitary tract**
  (`14_brainstem_midbrain_hypothalamus`) — taste **quality** and **intensity**, plus **oral
  somatosensation** (temperature, texture, viscosity, fat, capsaicin): a five-ish-dimensional quality
  vector with an intensity scalar, **no spatial map of the world, only a crude map of the tongue.**
  Fan-in: to derive.
  **The relay stage of this line has its own entry in another file, and that entry defers the
  payload to this one.** That entry declares `→ the gustatory pathway, via the parvicellular ventral
  posteromedial thalamus to insular taste cortex — taste quality and intensity, typed at the gustatory
  entry`, **naming this entry as the place the payload lives.** **So the two files agree on the route
  and on which end types it**, and this end does. **The far end carries a partition this end does
  not**: its solitary-tract entry names seven subnuclei, one of them **parvicellular**, and a
  rostrocaudal gradient. **Owed here: say which subnucleus the gustatory line leaves from**, since the
  far end already has the axis.
- **← the ventral posteromedial parvocellular thalamic nucleus** → anterior insula and frontal
  operculum — the same vector, relayed, chiefly ipsilateral. Fan-in: to derive.

**Outputs.**
- **→ orbitofrontal cortex** — quality and intensity, **independent of hunger.** **The payload
  changes at the next stage, not this one**, and that is the load-bearing fact: **the primary cortex
  declares what is in the mouth; the secondary declares what it is worth.** Fan-out: to derive.
- **→ amygdala** and **→ hypothalamus** (feeding), reciprocal — payload otherwise **owed**.

**Sizing.** Basis: **per hemisphere.** **Soft / unknown at all three stages** — the nucleus of the
solitary tract (`14_brainstem_midbrain_hypothalamus`), the thalamic nucleus and the insular cortex —
**no clean human counts.** Fan-in to derive. **Structure total: to derive, and this is three
structures priced as none.** **And the first of the three has a full entry of its own in another
file** — **so this entry prices as none a structure that is counted, or fails to be counted,
elsewhere.**

**Shape.** **Rank and axes to derive.** **Sub-elements are owed throughout**: no laminar or
divisional partition of any of the three stages was established. **The rostral/caudal gradient of
the disputed hot spots is the only tangential organisation anyone has proposed, and it did not
replicate.**

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← taste buds, by cranial nerves VII / IX / X | **a five-ish-dimensional quality vector with an intensity scalar**, plus oral somatosensation (temperature, texture, viscosity, fat, capsaicin) | to derive | **event-driven** — a chemical arrival at the receptor cells; no sampling rate is recorded | **no spatial map of the world, only a crude map of the tongue** |
| ← ventral posteromedial parvocellular thalamic nucleus → anterior insula and frontal operculum | **the same vector, relayed** | to derive | event-driven | **chiefly ipsilateral**; crude tongue map only |
| → orbitofrontal cortex | quality and intensity, **independent of hunger** | to derive | event-driven | none |
| → amygdala; → hypothalamus (reciprocal) | **owed** | owed | event-driven | owed |

**The representation is not constant along this line and that is the entry's central design problem.**
The receptor alphabet is discrete; the cortical code is a distributed ensemble; and the architecture
says so directly — **as the signal proceeds to the hindbrain and higher, coding becomes more
distributed and temporal patterns become important**, so **the quality vector is progressively
re-encoded into an ensemble pattern as it ascends, and the same payload description must not be
carried at every stage.**
**Which means the table above is right at row 1, right at row 3, and cannot be right at row 2 as
written** — row 2 says *the same vector, relayed*, and the architecture's own Justification says the
vector is being re-encoded across exactly that span. **The re-encoding is real, it is stated, and the
architecture's Inputs field carries the pre-re-encoding description on the relayed line.** Recorded as
a finding against the architecture entry, **not smoothed here**: the copied field says *the same
vector, relayed*, and the copy is faithful.

## Algorithm

- **Transform.** **Three coding models are live, not two**, and the architecture declines to choose:
  1. **Labelled line.** Receptor proteins are expressed in **non-overlapping sets of cells**, which is
     what makes a discrete alphabet available and is the main evidence for it.
  2. **Across-fibre / ensemble.** Taste buds hold both narrowly and broadly tuned cells, and the code
     becomes more distributed as it ascends.
  3. **Temporal**, with quality embedded in the **cadence** of impulses rather than in which cells fire
     or how fast.
  **No transform is written, because the three models require three different arrays**, and choosing
  one here would settle at the design rung a question the architecture records as open. **The five-
  quality alphabet is real at the receptor and does not survive the ascent** — so whatever is written
  must change format along the line, and what it changes into is exactly what the three models
  disagree about.
- **The temporal model is the one that would break the array vocabulary, and it is worth stating
  before anything is allocated.** **The map has no other payload of that form anywhere, and it is the
  one a lower rung would find hardest to implement, since it makes spike timing the message rather
  than its carrier.** **An array of rates cannot carry a cadence code at all** — not badly, not
  approximately: the quantity the code is in has been discarded before the array is written.
  **So this is not a parameter waiting on a value; it is a representation question that reaches the
  shared vocabulary**, and it reaches it in the same place the scheduling discipline does. **Micky's,
  and surfaced rather than chosen.** *(The three models and the cadence claim are the architecture's;
  that a rate array cannot express the third is Claude's reading.)*
- **There is no map here, and the negative is a result rather than a gap.** **The gustotopic map is
  claimed and then contradicted.** Two-photon imaging in anaesthetised mouse reported quality-specific
  hot spots — sweet rostral, bitter caudal — with broadly tuned cells virtually absent; **a later study
  with a more sensitive calcium indicator, under the same anaesthesia, found the opposite**, and
  attributed the discrepancy to indicator sensitivity, so **the earlier study's narrow tuning may have
  been a detection threshold rather than a property of the tissue.** Imaging in **alert** mice found
  taste-responsive cells narrowly *or* broadly tuned and **sparsely scattered.** In human,
  high-resolution imaging with multivariate analysis finds distinct qualities in **distributed spatial
  patterns** rather than distinct topographic areas. **Recorded verdict: no map; a spatial population
  code.**
  **The design consequence:** the cortical array has **no indexable tangential axis**, and an
  allocation that gave it one — rostral for sweet, caudal for bitter — would be encoding a result that
  did not replicate.
- **A confound specific to this cortex, and it lands on the arrays.** The insula is **inherently
  multisensory**, carrying somatosensory and thermal responses alongside taste, and **the entry's own
  inputs declare oral somatosensation arriving on the same edges as taste.** **So the input array is
  not a taste array**, and nothing above says how the two are separated, or whether they are.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `receptor_quality_vector` | (Q, T) | open — emission question | to derive | quality channels
  over tongue positions |
  | `solitary_tract_state` | **rank and axes to derive** | open | to derive | to derive |
  | `thalamic_relay_state` | **rank and axes to derive** | open | to derive | to derive |
  | `insular_state` | **rank and axes to derive**, and **no indexable tangential axis** | open | to
  derive | to derive |
  | `*_threshold` per stage | as above | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded
  16 | 0 … fan_in | count of active inputs |

  **Q is "five-ish" and that is the architecture's word, not a hedge added here.** The five-quality
  alphabet is real at the receptor; the *-ish* is doing work, because oral somatosensation arrives on
  the same edges and is not one of the five.
  **T is a crude map of the tongue and is the only spatial axis in the entry**, and it does not
  survive to cortex.
  **Every rank below the receptor is to derive.** The architecture says so in the Shape field, and
  **sub-elements are owed throughout** — no laminar or divisional partition of any of the three stages.
- **Parameters.** **None has a value.** Three neuron counts, all **soft / unknown**; three fan-ins, all
  to derive, all bounded ≤ 16 bits. **Three structures priced as none**, and **the first of them has a
  full entry of its own in another file**, so the same structure is priced here at nothing and
  priced — or not priced — there.
- **Update equation.** **Not written, and blocked by more than the standing list.** Beyond emission and
  the learning rules: **the coding model is not chosen**, and the three models do not share an update
  equation. What is fixed regardless: **the payload changes at the next stage, not this one** — the
  primary cortex declares what is in the mouth and the secondary declares what it is worth — so **no
  equation in this entry may make the output depend on hunger, satiety or value.** That is a real
  constraint and it is the one this entry can state exactly.
- **State carried between updates.** To derive at all three stages. **If the temporal model is the
  right one, the state is a history and not a value**, and its extent is set by the cadence window,
  which is not stated. Recorded.
- **Edge storage.** 2 input edges, 3 output edges. Line counts: all to derive. Latency to derive.
  Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Open, beyond the standing list.**
  - **Which of the three coding models**, and it reaches the shared vocabulary rather than this file.
    Micky's.
  - **Which subnucleus of the solitary tract the gustatory line leaves from.** The far end names seven
    subnuclei, one of them parvicellular, and a rostrocaudal gradient; **this end has no axis and the
    far end already has one.** Owed at this section's source.
  - **The bundle's split into three entries.** Owed at the source. **Not done here.**
  - **A structure this entry holds as a stage is recorded as missing by two other files**, and the
    architecture records the finding rather than repairing it. This entry names the **ventral
    posteromedial parvocellular thalamic nucleus** in its Function field and on an input line and
    carries it as its own row in the section totals; **`14_brainstem_midbrain_hypothalamus` names the
    same structure twice** and **records against both that it has no entry in `12_thalamus` under any
    name**, and **`12_thalamus` confirms that absence from its own side.** **All three statements are
    true and the conclusion drawn from them was wrong.** The structure is absent from the thalamus
    section and **it is not absent from the architecture** — it is here, as one of three stages inside
    this bundled entry. **So a structure was reported missing because the file it belongs in by subject
    matter does not carry it, while the file that does carry it holds it below the level a search for
    entries can see.**
    **Two things make it invisible to an index as well.** The name differs in two places at once —
    *ventroposterior parvicellular* and *ventral posteromedial parvocellular* are the same nucleus
    written with a different word order and a different vowel — and **this entry is a bundle**, so the
    stage has no heading of its own to be matched against. **A bundled stage with a spelling variant is
    invisible from both directions.**
    **Owed at the source, and it is a decision rather than a repair:** either this stage becomes an
    entry in `12_thalamus` and this entry cites it, or `12_thalamus` records that the nucleus is
    described here. **Not moved here** — moving a stage between files at this rung would re-terminate
    three files' edges on a structure whose owner has not been decided.
    **The design-rung consequence, which is the part this file owns:** the code cannot give this stage
    a module of its own, because it has no entry to be derived from, and it cannot leave it out,
    because it is a declared stage on a declared route. **It is written inside this file's gustatory
    structure and marked**, which is the same treatment the architecture gives it.
  - **How taste and oral somatosensation are separated**, when they arrive on the same edges into an
    inherently multisensory cortex. Not stated above.
  - **The rank and axes of all three stages**, and the sub-element partition, owed throughout.

---

# 5. Semicircular canals

## Contract

**Inputs.**
- **← head angular motion** — mechanical rotation onto the hair cells of the three cristae. **Not a
  neural edge.** Fan-in: not applicable.

**Outputs.**
- **→ vestibular nuclei**, chiefly superior and medial, by the **superior division** of the
  vestibular ganglion and cranial nerve VIII — **head angular velocity, three-axis, head-fixed,
  band-limited with no direct-current term, one triplet per ear.** **Does not carry:** linear
  acceleration, gravity, tilt or attitude. Fan-out: to derive.
- **→ cerebellum** (flocculonodular lobe) (`10_cerebellum`), on a branch that **bypasses the
  nuclei** — the same rotation-rate signal, unrelayed. **Two-ended, and this end is the specific
  one:** that file carries this limb inside a single afferent line naming the canals, the otolith
  organs and the vestibular nuclei together, with one payload clause across all three. **The split
  is owed there and every term it needs is here.**

**Sizing.** Basis: **per ear.** **Soft / unknown — no hair-cell or ganglion-cell count is recorded.**
Hair cells are **not neurons** and are the same class as the cochlear hair cells: their store is
**to derive and not zero.** **Structure total: to derive.**

**Shape.** **Rank 1: (canal).** **Extent exactly three per ear** — and this is **the only extent in
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

**Edge latency.** All edges **to derive.** The transducer's own dynamics are stated: **the velocity
signal decays with a time constant of 3–5 seconds**, and afferents discriminate head-velocity
differences of about **2 deg/s** while remaining sensitive to hundreds of deg/s.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← head angular motion | angular velocity of the head | to derive | **event-driven** — a mechanical arrival by the inertial lag of the endolymph; no sampling rate | world |
| → vestibular nuclei (superior division, CN VIII) | **deg/s** — head angular velocity, three-axis | **~2 deg/s discriminable, sensitive to hundreds of deg/s**; **band-limited with no direct-current term** | event-driven | **head-fixed, three canal axes — and the basis is oblique, not orthonormal. The angles are owed.** |
| → cerebellum (flocculonodular lobe) (`10_cerebellum`), bypassing the nuclei | **the same rotation-rate signal, unrelayed** | as above | event-driven | as above |

**This is the one line in the whole file whose units, range and frame are all stated**, and it is
still not closed, because the frame is a basis whose vectors have no numbers. **The range column is
also the only one in the section with two real figures**, and the width they imply is derivable the
moment an upper bound is pinned: `ceil(log₂(2 × ω_max ÷ 2 deg/s))`. **ω_max reads "hundreds of deg/s"
and is not a number**, so the width is written as that expression and not evaluated. **Evaluating it
against a guessed 500 deg/s would put an invented figure into the one representation this section can
almost state.**

**The second row and the third carry the same payload and must not be allocated twice.** The
cerebellar branch bypasses the nuclei; it is a branch of the same signal, not a second signal.

## Algorithm

- **Transform.** **A payload change happens before the first synapse, performed by fluid mechanics —
  and the map has no other instance of a transform executed outside the nervous system.** The canal is
  a heavily damped **torsion pendulum**: viscous drag dominates inertia, so across the band of natural
  head movement the mechanics **integrate** the angular acceleration that drives them, and the
  afferent's firing is proportional to **velocity**, peaking at peak velocity rather than peak
  acceleration.
  **The standard name is available and the transfer function is not.** A damped torsion pendulum is a
  second-order linear mechanical system, and what the architecture supplies is its qualitative
  behaviour across one band plus **one** time constant. **The equation is not written**: writing a
  transfer function here would require the pendulum's two other parameters, which no rung supplies,
  and the result would read exactly like a derived one. **Named, not evaluated.**
  **The integration is imperfect — hence the 3–5 second decay, and hence a steady rotation is not
  held**, which the central stage partially repairs.
- **Transducer class, and the hair cells are a second class inside it.** The crista is a **transducer**:
  not a threshold gate, storing no threshold, and the log₂ cost does not apply, with its input a
  **mechanical arrival** rather than a projection. The **hair cells** within it are **not neurons** and
  are the same class as the cochlear hair cells — **graded, and their store is to derive and not
  zero.** Zero would assert they hold nothing; `log₂(fan-in)` would assert a threshold they do not
  have. **Two element classes in one structure, and they must not be collapsed.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `canal_rate` | **(3,)** per ear | open — emission question | ~2 deg/s resolution, ω_max to
  derive | **deg/s** |
  | `cupula_state` | (3,) | open | to derive | cupula deflection |
  | `hair_cell_state` | (3, H) | open — **graded, not a threshold gate** | to derive | to derive |

  **`canal_rate` is the only array in this file whose extent is a number rather than a symbol**, and
  the number is **3**. Every hair cell in a crista shares one directional sensitivity, so a crista
  emits **one scalar**, not a population pattern.
  **H — hair cells per crista — is to derive**, no count being recorded, and their store is not zero.
  **There is no threshold array**, because neither element class in this structure is a threshold gate.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `canal_count` | canals per ear | **3, exact** | architecture Shape |
  | `canal_basis` | 3 × 3 direction cosines | **owed — the human inter-canal angles** | architecture
  Shape; **deviations from orthogonality are the rule and are functional** |
  | `velocity_decay_tau` | **seconds** | **3–5** | architecture Edge latency — **a state time
  constant, not an edge latency** |
  | `velocity_resolution` | deg/s | ~2 | architecture Edge latency |
  | `velocity_max` | deg/s | **"hundreds", to derive** | architecture Edge latency |
  | `hair_cells_per_crista` H | cells | to derive | not supplied above |

  **`canal_basis` is the parameter that matters most and it has no value.** **A consumer cannot assume
  an orthonormal triad and read components off directly.** An identity matrix here is not a
  placeholder — it is the specific assumption the architecture calls a **misleading descriptor**, and
  the deviations it would erase are **negatively correlated with vestibular sensitivity**, meaning the
  obliqueness is doing work. **Initialising it to the identity would be building the less sensitive
  organ on purpose.**
- **Update equation.** **Waiting on the emission question**, and on the pendulum's remaining
  parameters. What is fixed regardless: the transform from head motion to afferent rate is an
  **integration with leak**, and its output is a **velocity**, not an acceleration — so **any equation
  whose output tracks acceleration has the stage backwards**, in the same way that reading
  depolarisation as activation has the outer retina backwards.
- **State carried between updates.** **`cupula_state`, and this is where the 3–5 second time constant
  lives.** It is a **state time constant and not an edge latency**: it says how long the stage holds
  what it received, not when the signal arrives. Written into this field and **not** into Edge latency,
  which reads *to derive* on every edge of this entry. Initial value: to derive. **State memory is not
  parameter memory and the two are never summed.**
- **Edge storage.** 1 mechanical arrival, 2 output edges carrying **the same payload**. Line count = 3
  per ear on each output — **the one line count in this file that is exactly known.** Latency to
  derive. Interval unset. Bytes per value unset. **Not summable** — but this is the edge whose storage
  will close first once the discipline is set, because two of the four terms are already numbers.
- **Adaptation.** **None set.** The canal stores no threshold, so there is nothing here for a learning
  rule to write even when one exists.
- **Invariant note carried from the architecture, because it forbids a staged bring-up.** **This
  structure's output is uninterpretable without the otolith line.** A canal carries rotation rate and
  is blind to gravity, tilt and attitude. **A build that instantiated this line first would not have a
  partial system — it would have a line whose output means nothing.**
- **Open, beyond the standing list.**
  - **The human inter-canal angles.** Owed. **The map's one exactly-stateable payload has an unknown
    parameter inside it**, and the obvious default is the one the architecture rules out.
  - **ω_max**, without which the value range is an expression rather than a width.
  - **The torsion pendulum's remaining parameters**, without which the mechanics are named and not
    computed.
  - **H, and what a graded hair cell stores** — to derive and not zero, at both vestibular transducers.

---

# 6. Otolith organs

## Contract

**Inputs.**
- **← head linear acceleration and gravity** — mechanical shear by way of the otoconial mass. **Not
  a neural edge.** Fan-in: not applicable.

**Outputs.**
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

**Sizing.** Basis: **per ear.** **Soft / unknown — no hair-cell or ganglion-cell count is recorded.**
Same element class and same *to derive, not zero* store as the canal and cochlear hair cells.
**Structure total: to derive.**

**Shape.** Rank 2: **(macula, preferred direction).** **Two maculae per ear**, and **the direction
axis is a distributed code rather than a basis.** In a crista every hair cell shares one directional
sensitivity; in a **macula** the hair cells are aligned in a **multitude of directions**, with
polarity reversing across the **striola**. **So the otolith organs do not supply basis vectors; they
supply a distributed directional code across a population, from which the acceleration direction
must be decoded rather than read off.** **One sense, two payload formats, and they must not be
described alike.**

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← head linear acceleration and gravity | acceleration, **gravity included and inseparable** | to derive | **event-driven** — a mechanical arrival through the weight and inertia of the otoconial mass | world |
| → vestibular nuclei (inferior division, CN VIII) | **the gravito-inertial acceleration vector** | to derive; **with a direct-current term — a maintained tilt produces a maintained signal** | event-driven | **head-fixed, and a distributed directional code rather than a basis.** Must be **decoded**, not read off |
| → cerebellum (flocculonodular lobe, nodulus and uvula) (`10_cerebellum`), direct branch | **the same vector, unrelayed** | as above | event-driven | as above |

**The direct-current term is the representational difference from the canal line and it is not
cosmetic.** The canal output is **band-limited with no direct-current term** — a steady rotation is
not held. The otolith output **has** one — a steady tilt is held indefinitely. **Two lines into the
same consumer, one of which loses steady state by construction and one of which does not.** A
consumer normalising both the same way would destroy the only signal that survives a constant
stimulus.

## Algorithm

- **Transform.** **Mechanical shear, by two mechanisms in one organ:** the **otoconial mass** of
  calcium-carbonate crystals in a gel, whose **inertia** shears the hair bundles under acceleration and
  whose **weight** shears them under tilt. **Two maculae per ear** set close to orthogonal — the
  **utricle** roughly horizontal, the **saccule** roughly vertical.
  **No standard operation name is written, because the operation is the ambiguity itself.** **The
  ambiguity is a consequence of physics, not a limitation of the organ, and it is total.** Gravity and
  linear acceleration are indistinguishable to any accelerometer — the equivalence principle — so the
  output is a gravito-inertial vector with **no decomposition.**
  **The design consequence, stated so it cannot be quietly repaired:** an update equation that emitted
  tilt and translation as separate quantities would be computing something the organ does not produce,
  and the separation is not this structure's to perform. **Neither vestibular organ can provide
  unambiguous information about head motion and orientation.** Resolution requires central convergence.
- **The two vestibular transducers have two different payload formats and one of them needs a decoder
  that no rung supplies.** In a **crista** every hair cell shares one directional sensitivity, so the
  organ emits one scalar per canal and the three canal axes are the basis. In a **macula** the hair
  cells are aligned in a **multitude of directions**, with polarity reversing across the **striola**,
  so the organ emits a **population pattern from which the direction must be decoded.**
  **One sense, two payload formats, and they must not be described alike.** **The decoding operation
  is not named at any rung above**, and this rung does not invent one: a population-vector readout is
  the obvious candidate and writing it would be choosing a decoder the architecture does not state.
  **Recorded as owed at the architecture rung.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `macula_population` | **(2, D)** per ear | open — emission question | to derive | to derive |
  | `otoconial_shear_state` | (2, D) | open | to derive | shear |
  | `hair_cell_state` | (2, D) | open — **graded, not a threshold gate** | to derive | to derive |

  **The first axis is exactly 2 — utricle and saccule — and the second is not a basis.** D is the
  population of preferred directions and its extent is **to derive**; **it must not be set to 2 or 3
  as though it were a coordinate count**, because that is precisely the canal's arrangement and not
  this one. **The polarity reversal across the striola means D is signed and not merely directional**,
  and where the reversal falls is not partitioned above.
  **There is no threshold array**, for the same reason as at the canals.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `macula_count` | maculae per ear | **2, exact** | architecture Shape |
  | `macula_orientation` | — | **utricle roughly horizontal, saccule roughly vertical, close to
  orthogonal** — **no angles given** | architecture Function |
  | `preferred_direction_count` D | directions | to derive | not supplied above |
  | `striola_partition` | — | **owed** — where polarity reverses is not partitioned | architecture Shape |
  | `hair_cells_per_macula` | cells | to derive | not supplied above |

  **`macula_orientation` is stated in words and not in numbers**, exactly as the canal basis is, and it
  fails in the same way: *roughly horizontal*, *roughly vertical*, *close to orthogonal*. **Two
  structures in this section carry a geometry the code needs and the literature has not been asked
  for.**
- **Update equation.** **Waiting on the emission question and on the decoder.** What is fixed
  regardless: **the output is a sum and the sum is the signal.** **Tilt and translation leave the ear
  summed**, so no equation in this entry separates them, and any equation that does has moved the
  central computation into the transducer.
- **State carried between updates.** `otoconial_shear_state`. **No time constant is stated for it**,
  in contrast to the canal, and the difference is real rather than an omission: the canal's constant
  exists because its integration leaks, and **this organ holds a maintained signal.** Initial value: to
  derive.
- **Edge storage.** 1 mechanical arrival, 2 output edges carrying **the same vector**. Line count = D
  per macula, D to derive. Latency to derive. Interval unset. **Not summable.**
- **Adaptation.** **None set.** No threshold is stored here either.
- **Invariant note carried from the architecture.** **The payload is only interpretable in combination
  with the sibling line**, and the architecture calls this the clearest such case in the source.
  **Neither transducer's payload is defined without its sibling.** Co-instantiation is not a
  convenience here: a semicircular canal carries rotation rate and is blind to gravity, tilt and
  attitude; an otolith organ carries the gravito-inertial sum and cannot separate a steady tilt from a
  steady acceleration, because the two produce the same shear on the same hair cells. **Attitude is
  computed, never transduced, and there is no attitude receptor.**
- **Open, beyond the standing list.**
  - **The decoder** that turns the distributed directional code into a direction. Owed at the
    architecture rung.
  - **D, and the striola partition** that makes it signed.
  - **The macula orientations as numbers.**
  - **What a graded hair cell stores** — to derive and not zero.

---

# 7. Vestibular nuclei and the central vestibular pathway

## Contract

**Inputs.**
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

**Outputs.**
- **→ oculomotor nuclei (III / IV / VI)** by the medial longitudinal fasciculus — the
  **vestibulo-ocular reflex** command, an eye-velocity signal equal and opposite to head rotation,
  driven chiefly by the canal line.
- **→ spinal cord** (`16_spinal_cord`) (vestibulospinal tracts) — an antigravity postural command,
  **two-ended and confirmed, and this end is the typed one.** That file carries the
  vestibulospinal limb inside a **five-tract descending bundle** whose payload
  it marks owed and declines to split, because splitting would invent the arity of the five payloads.
  **This entry's line is one of the five and it is typed here**, so the far end's *owed* is accurate
  for the bundle and not for this member. Driven chiefly by the otolith line by way of the lateral
  nucleus.
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

**Sizing.** Basis: **per side** for the nuclei, **per hemisphere** for the cortical areas. **Soft /
unknown throughout — no clean human counts recorded for the four nuclei or for the parieto-insular
cortex.** Fan-in to derive. **Structure total: to derive.**

**Shape.** Rank 2: **(nucleus, cell class)** — four nuclei, and **the cell-class axis is partly
named by response rather than by place**: type II **vestibular-only** neurons increase firing with
rotation toward the **contralateral** canal, so the population is distinguished by what it responds
to and which side drives it, not by where it sits. **Further partition is owed.**

**Edge latency.** All edges **to derive** — and this is the structure whose **state** time constants
are stated instead: **velocity storage lengthens the canal line's 3–5 second constant to at least
15–25 seconds**, a 3× to 8.3× lengthening.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← semicircular canals (CN VIII) | deg/s, three-axis | **no direct-current** | event-driven | **head-fixed, oblique canal basis** |
| ← otolith organs (CN VIII) | gravito-inertial acceleration | **with direct-current; tilt and translation unresolved** | event-driven | head-fixed, distributed directional code |
| ← cerebellum (flocculonodular lobe, nodulus, uvula) (`10_cerebellum`) | the internal model's correction | **owed** | event-driven | owed |
| ← deep cerebellar nuclei, fastigial (`10_cerebellum`) | **axial posture, balance and eye-movement corrections** | **owed** | event-driven | owed |
| ← vision and proprioception | optic flow and body configuration | to derive | event-driven | **to derive — and these are the second and third estimates of the same quantity**, so the frames must be commensurable and no rung says they are. **The cerebellar half of this route is consumer-only** — `10_cerebellum` declares no output carrying vision or proprioception here |
| → oculomotor nuclei (III / IV / VI), by the medial longitudinal fasciculus | **eye velocity, equal and opposite to head rotation** | to derive | event-driven | eye, driven chiefly by the canal line |
| → spinal cord (`16_spinal_cord`), vestibulospinal tracts | **an antigravity postural command** | to derive | event-driven | body, driven chiefly by the otolith line by way of the lateral nucleus |
| → cerebellum (`10_cerebellum`) | **both lines plus the current estimate** | to derive | event-driven | as the constituents |
| → thalamus → parieto-insular vestibular cortex, area 2v, area 3a → hippocampal formation | **the computed estimate: head attitude and self-motion, with gravity separated from linear acceleration** | to derive | event-driven | **head; and this is a result, not a measurement** |
| → cortical vestibular areas onward | the same computed estimate | to derive | event-driven | **the frame changes at each step**: intermediate head/body at parieto-insular, **body-centred** at ventral intraparietal, approximately **head-centred** at medial superior temporal |

**The last row is the one a consumer will get wrong, and it is why the frame is declared at the line
rather than at the structure.** The same payload travels three hops and **is in a different frame at
each**, and one of the changes is not monotonic — head, then body, then head again. **A consumer that
inherited the frame from the producing structure would be right once and wrong twice.** This is
precisely the failure the Representation field exists to make mechanical: every structure satisfying
its own contract, and the composition still not running, because two neighbours read one shared line
correctly and disagree about what its numbers mean.

**And the fourth input row is a second instance of the same hazard.** Vision and proprioception arrive
as **the second and third estimates of the same quantity** — so they are not additional content, they
are the same content in other frames, and combining them requires a common frame that no rung
supplies.

**The two cerebellar input rows are two structures and not one, and a consumer that merged them would
be merging a cortex with a nucleus.** The first arrives from the cerebellar **cortex** directly, from
the flocculonodular lobe, carrying the internal model's correction; the second from the **deep
cerebellar nuclei**, from the fastigial, carrying axial posture, balance and eye-movement corrections.
**Both payloads are owed, which is exactly the condition under which two rows look interchangeable
and are not** — and the second row exists because the far file was read end to end rather than
searched, since a search for *cerebellum* at this end matches the first row and stops.

## Algorithm

- **Transform.** **The structure computes what neither transducer can sense, and the architecture names
  the mechanism rather than an operation: an internal model of the physical laws of motion rather than
  a measurement.** The otolith line arrives carrying gravity and acceleration summed, the canal line
  arrives carrying rotation rate — which says how the head has turned relative to gravity — and the
  central neurons combine the two. **Attitude is a computed quantity, not a sensed one.**
  **An internal model of the physical laws of motion is a description of what the computation
  achieves, not a named operation over arrays**, and spec §5 says a picture of an operation is not an
  operation. **This is a finding about the structure and is recorded as one.** What the architecture
  does supply, and what constrains any eventual equation:
  - the two inputs and what each carries and does not carry;
  - that the combination is **the specific convergence of canal and otolith signals onto central
    vestibular neurons**;
  - that vision and proprioception are combined with them, **which is why the estimate survives when
    one line is degraded and why it can be fooled when vision and the labyrinth disagree.**
- **The convergence that resolves the ambiguity is declared as a fact and not as an edge, and that is
  the largest single gap in this entry.** Neither transducer alone can disambiguate tilt from
  translation; the resolution is the specific convergence of canal and otolith signals onto central
  vestibular neurons. **The entry declares both inputs and does not declare the meeting** — so **the
  convergence edge, and which cells carry it, is owed**, and it is the internal edge that matters most
  here.
  **At this rung that has an exact cost:** the entry's central function has **no internal edge to
  transcribe.** Two input arrays arrive, one output array is described, and **the line between them is
  not written at any rung.** No update equation can be produced from an entry in that state, and
  producing one would be inventing the structure's whole purpose. **Recorded, not patched.**
- **Velocity storage is a named, measured payload change and it is a repair rather than a
  re-expression** — content unchanged, persistence altered. **The map has no other edge whose declared
  transformation is purely temporal**, and it is a useful category: a stage that neither adds nor
  removes dimensions but extends the life of what it receives. **The mechanism is owed** — nothing in
  the description says what implements the integrator.
  **So the arithmetic is a lengthening whose factor is stated and whose implementation is not:** the
  canal line's **3–5 second** constant becomes **at least 15–25 seconds**, a **3× to 8.3×**
  lengthening. **The content is still angular velocity and only its persistence changes.** An
  integrator with a longer leak is the obvious candidate and **it is not written**, because the
  architecture marks the mechanism owed and a well-formed invented integrator reads exactly like a
  derived one.
- **Both time constants in this entry are state, not latency, and the field they go in is fixed.** The
  entry's Edge latency reads *to derive* on every edge; the 15–25 seconds is how long this stage holds
  what it received. **Writing it into an edge latency would convert the section's only stated timing
  into the section's only invented latency.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `canal_input` | (3,) per side | open — emission question | as the canal line | deg/s |
  | `otolith_input` | (2, D) per side | open | as the otolith line | to derive |
  | `nucleus_state` | **(4, C)** | open | to derive | to derive |
  | `nucleus_threshold` | (4, C) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0
  … fan_in | count of active inputs |
  | `velocity_storage_state` | to derive | open | to derive | angular velocity, **persisted** |
  | `attitude_estimate` | to derive | open | to derive | **head attitude and self-motion, gravity
  separated from linear acceleration** |

  **The first axis of `nucleus_state` is exactly 4** — superior, medial, lateral, inferior. **The
  second is not a partition of a count**: the cell-class axis is **partly named by response rather
  than by place**, type II vestibular-only neurons being distinguished by what they respond to and
  which side drives them rather than by where they sit, and **further partition is owed.** So C names
  a set the architecture has not closed and no count divides among it.
  **`attitude_estimate` is the structure's product and its shape is to derive.** The payload is stated
  exactly — head attitude and self-motion with gravity separated — and **no rung says what shape that
  object has.**
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `nucleus_count` | nuclei per side | **4, exact** | architecture Function and Shape |
  | `velocity_storage_tau` | **seconds** | **at least 15–25** | architecture Edge latency — **a
  state time constant** |
  | `storage_lengthening` | ratio | **3× to 8.3×**, from 15/5 and 25/3 | derived from the canal
  constant and this one |
  | nucleus and cortical counts | cells | **soft / unknown throughout** | architecture Sizing |
  | fan-ins, all four input lines | contacts | to derive, bounded ≤ 16 bits | architecture Inputs |

- **Update equation.** **Not written, and blocked by more than the standing list.** The convergence
  edge is owed, the velocity-storage mechanism is owed, and the frames of the vision and
  proprioception lines are not commensurable on the page. What is fixed regardless of all three:
  **what ascends is a result, not a measurement**, so **no output line of this entry may carry the
  transducer signal unchanged** — the thalamic and cortical lines carry the computed estimate, and an
  equation that passed either input through would have deleted the reason the structure exists.
- **State carried between updates.** `velocity_storage_state`, holding at least **15–25 seconds** of
  persistence, and `attitude_estimate`, which is by construction carried between updates because it is
  an estimate rather than a reading. **This is the longest-lived state anywhere in the map so far**, and
  it is the far end of the span the standing list records: **tens of microseconds in file 02 against
  15–25 seconds here, about 6.4 orders of magnitude.** Initial values: to derive. **State memory is not
  parameter memory and the two are never summed.**
- **Edge storage.** 4 input edges, 5 output edges. Line counts: all to derive except the canal input at
  3 per ear. Latency to derive. Interval unset. **Not summable.** **And this is the entry where the
  interval decision bites hardest in both directions**: the same structure holds 15–25 second state and
  drives the vestibulo-ocular reflex, whose command must track head rotation closely enough to
  stabilise gaze.
- **Adaptation.** **None set.** The architecture notes the estimate **can be fooled when vision and the
  labyrinth disagree**, which is a statement about the combination and not a rule for changing it.
- **Invariant note carried from the architecture.** **The two ascending transducer lines must both be
  live for the structure's declared function to exist at all**, and the cerebellar loop and the
  cortical loop both close here. Co-instantiation is therefore not satisfiable one line at a time in
  this entry, and it is the strongest form the requirement takes anywhere in the map.
- **Open, beyond the standing list.**
  - **The convergence edge**, and which cells carry it. Owed at the architecture rung, and **the entry
    cannot be coded without it.**
  - **The velocity-storage mechanism.** Owed. The factor is stated; nothing implements it.
  - **C — the cell-class partition**, owed, and partly named by response rather than by place.
  - **The shape of `attitude_estimate`**, the structure's own product.
  - **A common frame for vision and proprioception**, which arrive as the second and third estimates of
    the same quantity.
  - **The medial superior temporal and ventral intraparietal areas are not direct thalamic targets on
    this line, and the route to them is contested.** There is reported to be **a lack of anatomical
    evidence for a thalamic vestibular projection to the medial superior temporal area**, and response
    dynamics and latency order the three areas **parieto-insular vestibular cortex → ventral
    intraparietal area → medial superior temporal area**, which is what a **cortico-cortical** route
    predicts and not what a shared thalamic input predicts. **Re-deriving the route is owed.** Per
    spec §5b this reads **contested** and not
    *to derive*: it is measured, and yielding readings that disagree, so it needs adjudication between
    existing results rather than a new measurement.
  - **No dedicated primary cortex — the one sense without one.** The cortical representation is
    distributed and inherently multisensory: the **parieto-insular vestibular cortex** (posterior
    insula / parietal operculum / retroinsular, human homologue debated), plus **area 2v**, **area
    3a**, and the **medial superior temporal** and **ventral intraparietal** areas described elsewhere
    in the map. **So the cortical end of this entry is a set of areas owned by other files**, and none
    of those files has been opened beside this one — the endpoints below carry no stem, which means the
    reading has not been done, not that no far end exists.

---

## Section totals

Copied from the architecture, with one column added at this rung: **what the derived width costs when
a machine integer holds it.** The added column is this rung's own and is not in the architecture.

| structure | basis | neurons | bits/neuron | parameter memory | realised at 8/16 bits |
|---|---|---|---|---|---|
| Olfactory epithelium — sensory neurons | per side | ~40M (flagged, not independently sourced) | **0** (no neural input, so no count) | **0** | **0** |
| Olfactory epithelium — sustentacular, basal | per side | to derive | not a threshold gate | to derive | to derive |
| Olfactory bulb — mitral cells | per side | ~50,000 | **10** (fan-in ~800) | **0.063 MB** | **0.100 MB** |
| Olfactory bulb — granule, periglomerular | per side | to derive, and the majority | ≤ 16 | to derive | to derive |
| Piriform and primary olfactory cortex | per hemisphere | to derive | ≤ 16 | to derive | to derive |
| Gustatory — nucleus of the solitary tract | per side | to derive | ≤ 16 | to derive | to derive |
| Gustatory — ventral posteromedial parvocellular nucleus | per hemisphere | to derive | ≤ 16 | to derive | to derive |
| Gustatory — anterior insula and frontal operculum | per hemisphere | to derive | ≤ 16 | to derive | to derive |
| Semicircular canals — hair cells | per ear | to derive | not a threshold gate | to derive | to derive |
| Otolith organs — hair cells | per ear | to derive | not a threshold gate | to derive | to derive |
| Vestibular nuclei | per side | to derive | ≤ 16 | to derive | to derive |
| Parieto-insular vestibular cortex | per hemisphere | to derive | ≤ 16 | to derive | to derive |
| **stated total** | mixed | | | **~0.063 MB** | **~0.100 MB** |

**The stated total is 0.063 MB and it is not a small section — it is an uncounted one.** Eleven of the
twelve rows read *to derive*, and the one that does not is 50,000 cells. **Piriform cortex is a large
allocortical area and the insula is a large cortical one; neither is priced, and the reason is that no
clean human count exists, not that the structures are small.** Against ~1.3 GB for the visual section
and ~484 MB for the auditory, **this section's figure is not comparable to either and must not be
summed with them as though it were.**

**The one derived width in this section is 10 bits, and it is the map's first that is neither zero nor
one.** A receptor-to-mitral convergence of ~800 gives `ceil(log₂ 800) = 10`. **Realised in a machine
integer that becomes 16 bits — 62,500 bytes derived against 100,000 realised, a 60% gap** — the widest
realisation gap in the map so far, because **10 bits is the furthest any derived width has sat from a
container boundary.**
**The trade the gap names, and it is a trade and not a problem to fix.** No integer type is 10 bits
wide. Bit-packing closes the gap and costs unpacking on every read; padding spends the memory instead.
That is a compute-against-memory trade, it is this rung's to record, and **it is never a reason to
shrink anything.** Memory is a derived requirement, not a limit to design against.

**Three facts about extent that the arrays above had to be built around.**

1. **An axis that exists physically and indexes nothing** — position in the olfactory epithelium. It is
   allocated and never indexed.
2. **An extent that is exact, small, and physical** — three canals per ear, whose orientations *are*
   the basis vectors of the payload. **And that basis is oblique, with the human angles owed**, so the
   map's one exactly-stateable payload still has an unknown parameter inside it. **The default a coder
   would reach for — an identity matrix — is the one the architecture rules out by name.**
3. **An extent that varies 3.1× between individuals** — 3,000 to 9,300 glomeruli per bulb. **The axis
   length is not a property of the species**, so the correct value of that extent is a distribution and
   not a number, and what the code allocates against is owed.

**A consequence the description does not draw, carried down because it lands on an array extent.** The
glomerulus-per-receptor-type convergence depends on a receptor count the source records as contested:
**13.9 : 1 to 15.9 : 1** if there are 350–400 intact types, **27.8 : 1 to 55.7 : 1** if there are
100–200. **The same measured glomerular count supports a four-fold range of convergence**, and the
contest therefore propagates into the shape rather than staying in the epithelium's prose.

**This section is the map's control condition on maps, and it behaves like one.** There was never a
topographic map here to over-state: chemotopy in the bulb is a map of chemical similarity and is
**discarded** at the next synapse; gustotopy was claimed and contradicted, with the verdict **no map, a
spatial population code**; and vestibular sensation has no map and no dedicated primary cortex. **Both
chemical senses arrive at cortex as distributed population patterns over a non-spatial quality space.**
**At this rung that shows up as an absence of indexable axes**, and it is the reason so many arrays
above carry a position axis that is allocated and never read.

**The total is a floor, and more so than in either previous section.** Every structure but one is
unpriced, the hair-cell store is *to derive and not zero* as it was in the auditory section, the
epithelium's own count is flagged as un-sourced, and **state memory and edge storage are not in the
table at all.** Edge storage would bite differently here than in the auditory section: **this section's
constraint is not a short interval but a long horizon** — state that must persist 15–25 seconds — and
**the two constraints together span about 6.4 orders of magnitude, which no single update interval
serves comfortably.** That figure cannot be turned into a number until the scheduling discipline is
set, and it is not.

**One difference between this table and the code below it, recorded so it is not read as a
discrepancy.** `Brain_03_other_senses.py` declares **seventeen populations** where this table has
**twelve rows**. The difference is granularity, not content: the table pools piriform's five cell
classes into one row and gives the taste receptor cells no row at all, while the entries above name
all six, and the code follows the entries. **No figure moves** — every added population is uncounted,
so the stated total is the same **0.063 MB**, and only the count of unstated stores rises, from
**eleven to fifteen**. **That is the same gap read at a finer grain and is not a new one**, which is
worth saying, because fifteen against eleven would otherwise look like four stores had gone missing.

**Memory is not a binding constraint and none of these figures is to be reduced.**

---

## Completion test

Spec §5's test is mechanical: **an entry is finished when the code can be written from it without
making a single further choice.** **No entry in this file passes**, and the file says so rather than
reading as though it did.

**Every entry is blocked by the standing list** — emission, scheduling, learning rules, connection
topology, tile geometry and sparsity. That is common to the rung and is not this section's finding.

**What is additional here, per entry, and it is what a session working this file should read first:**

| entry | additionally blocked by |
|---|---|
| 1 Olfactory epithelium | R **contested**; P not supplied; what a transducer computes; the cascade's state; **whether the centrifugal edge exists at all**; a turning-over population in fixed arrays |
| 2 Olfactory bulb | the **chemical similarity metric**; what a **reciprocal dendrodendritic apposition** is in code; G a distribution not a constant; interneuron counts; the cell-class partition; the four operations' arithmetic; output fan-out |
| 3 Piriform | **the storage and recall rules** — the entry's stated function is learning and it cannot run without them; **whether a unit has compartments**; P has no count, no extent and no meaning; organisation by efferent target |
| 4 Gustatory (bundle) | **which of three coding models**, one of which a rate array cannot express at all; the bundle's split, owed at the source; which solitary-tract subnucleus; how taste and oral somatosensation separate; rank and axes at all three stages |
| 5 Semicircular canals | **the human inter-canal angles**; ω_max; the pendulum's remaining parameters; H, and what a graded hair cell stores |
| 6 Otolith organs | **the decoder** from distributed directional code to direction; D and the striola partition; the macula orientations as numbers |
| 7 Vestibular nuclei | **the convergence edge, without which the entry's central function has nothing to transcribe**; the velocity-storage mechanism; C; the shape of the estimate; a common frame for vision and proprioception; the contested cortical route |

**Three of these reach past this file rather than waiting inside it**, and they are named separately
because they are not gaps to be filled by more reading:

- **What a reciprocal dendrodendritic apposition is in code** changes the shared edge type, which every
  module imports.
- **Whether a unit has compartments** is the unit's expressiveness, which is §10's list.
- **Whether a rate array can carry a cadence code** is the same question the scheduling discipline
  asks, arriving from the gustatory line instead of from the timing one.

**All three are Micky's, all three are asked here rather than parked, and nothing below this rung is
built on a guess at any of them.**
