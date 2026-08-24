# Brain code design — 06 posterior parietal

**Date:** 2026-08-21
**Derived from:** `Brain_architecture_06_posterior_parietal`, `Brain_code_design_spec`, and CLAUDE.md.
**No other content source.**
**Implements:** `Brain_06_posterior_parietal.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly," no commented-out prior version.

**How to read an entry.** Each entry carries a **Contract** block, then **Representation**, then
**Algorithm**. The contract block is **copied from the architecture character for character** and is
not this file's writing; it is read off the architecture file mechanically and written out unchanged,
so a diff of those blocks against the architecture entry is a check on the copy. **Representation and
Algorithm are this rung's own writing**, and that is where anything unfaithful would live.

**The contract block is the whole architecture entry.** `Brain_code_design_spec` §3 names eight
fields — Function → structure, Inputs, Outputs, Sizing, Shape, Edge latency, Invariant conformance,
Justification (biological) — and **there is no field this rung re-derives rather than copies.** So the
boundary between copy and writing falls at the block edge and nowhere inside it: everything above
**Representation** in each entry is the architecture's text, and everything from **Representation**
down is this file's.

**Provenance.** Contract blocks are verbatim copy. Unmarked sentences in Representation and Algorithm
are derivation from the architecture entry above them. Readings placed on it are marked **(Claude's
reading)**. Every number was recomputed with `python3`.

**Standalone, not a companion.**

---

## Element classes, and the template all five entries take

**One element class, and none of the four exceptional classes appears in this section.** Every
population in all five structures is a **threshold gate**. There is no transmission-only structure
here — every entry computes; no transducer — no entry converts a physical stimulus; no graded,
non-spiking element — no entry describes a cell responding without an action potential; and no
sign-inverting stage — no entry describes hyperpolarisation as the excitatory response. **That is a
positive statement about this section and not an absence of information**, and it is the reason the
ordinary entry shape fits all five.

**The laminar template is uniform across the five and stays a per-structure field.** All five are
granular association isocortex taking the standard eight sub-elements — **1, 2, 3, 4, 5a, 5b, 6a,
6b**, layer 4 undivided — with the standard internal block: **4 → 2/3**; **2/3 → 5a** and
**2/3 → 5b**, with reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**, **opposite signs**;
**6b → 6a**, arousal-gated; and within-sub-element recurrence in **4** and **2/3**. **A field that
happens to hold one value across five instances is still a field**, and the module holds the lamina
set per structure rather than as a module constant, because the value is not uniform across the map.

**One laminar feature is not a population and must not be allocated as one.** The medial intraparietal
area carries **two distinct bands of Baillarger**. The architecture is explicit that this belongs to
the **fibre plexus in layers 4 and 5b** rather than to a cell population, so it is a property of the
lamina axis. Allocating an array for it would create a population the architecture does not describe.

## The forward operation, and the three things it cannot be run with

The specified part of the computation is writable for every population in this section:

```
count[j]  = Σ_{i ∈ fan_in(j)} sign(i, j) · active_source[i]
active[j] = count[j] ≥ threshold[j]
```

and **three of the four terms in it are unset**:

- **`fan_in(j)` — inter-structure connection topology is not set at any rung**, here as in every
  section. It is one of the items requiring explicit agreement before it is touched.
- **`sign(i, j)` — sign arithmetic is not set anywhere.** The internal block requires it: **6a → 4**
  and **6a → 5a** are stated to carry **opposite signs**, so at least one internal edge is
  subtractive, and how an inhibitory contribution combines with an excitatory one in the sum above
  is not stated at any rung. The expression carries `sign(i, j)` to keep the requirement visible
  rather than writing a bare sum that would silently assume every input is excitatory.
- **`threshold[j]` — no rule writes it.** Adaptation is Micky's and is not set; see each entry.

**What is not unset is the operation itself.** Every population in this section is a threshold gate
and no population is described as doing anything else, so the arithmetic above needs no decision once
those three terms arrive.

## The recurrence reads a value, and which value is the scheduling discipline

Two of the internal edges are **within-sub-element recurrence, in layer 4 and in layer 2/3**, and the
reciprocal **5a → 2/3** closes a second loop. Each of these reads `active` from a population that the
same update writes. **Whether the read takes the value this update produced or the one before it is
the scheduling discipline**, which is not set and is **Micky's**. It may not be resolved here, and no
update equation in this file may be written as though a uniform one-step delay had been chosen. The
module therefore carries the recurrent edges as edges and **refuses to order them**, rather than
emitting a loop that would embody a choice nobody made.

## Update timing is event-driven throughout, and that is the honest answer

**No structure in this section has a rate of its own.** None is a sensor and none is described as
emitting on a schedule; every one of the five is driven by its inputs and emits when its inputs
change. **Event-driven** is therefore what every Representation block below declares under update
timing, and it is a statement rather than a placeholder: there is no system clock to borrow a rate
from, and borrowing one would invent the thing the architecture's second invariant forbids.

## The payload boundary, which is what Representation can and cannot declare here

**Representation pins units, range, update timing and coordinate frame once, at the line.** In this
section **the line usually has nothing to pin.** Of **55 edge lines, 18 carry a payload that can be
written and 37 do not** — **32.7%**. Sorting the 55 by what they carry:

| content class | typed | untyped |
|---|---|---|
| sensorimotor | 9 | 9 |
| perceptual | 9 | 4 |
| association / default-mode | 0 | 24 |
| **total** | **18** | **37** |

**(Claude's reading, offered to be checked, and it is the weaker of the two readings the counts
allow.)** Association
coupling is **sufficient** for an untypable payload and is **not necessary** for one: no association
payload in this section is typed, and thirteen sensorimotor and perceptual payloads are untyped as
well. The stronger converse does not hold. The module **computes this split rather than restating
it**, and reports it **by content class rather than as a single percentage**, because a rate
distributed at random would be a coverage problem — more research, evenly spread — while a boundary
with a location is a claim about where the description stops, and the untyped edges will not be closed
by the same kind of work that typed the others.

**A consequence for this rung specifically.** Representation exists to catch the failure where two
neighbouring structures each read a shared line correctly and disagree about what its numbers mean.
**On 37 of 55 lines there are no numbers to disagree about**, so the guard has nothing to hold and
the check it would provide is unavailable. That is recorded per line below, at the entry that
produces it.

## Four states this section needs that are not "to derive"

**"To derive" is an honest answer only for a quantity the source has not yet supplied**, and writing
it over any of the states below would make a claim the architecture did not make. The module carries
each separately and refuses to normalise them:

- **contested** — measured repeatedly, the measurements disagreeing. The arm-configuration input to
  the medial intraparietal area is contested and **not owed**: the reported frames are body-,
  shoulder- and hand-centred across studies. It points at a reconciliation between existing results,
  not at an experiment to run, and the same dispute reaches the precuneus, whose area-5 input types
  the frame as body-centred while the producer holds it unsettled. **So those two ends disagree about
  the payload, not about wording.**
- **contested scheme** — two or three incompatible parcellations of one tissue, held side by side.
  The medial intraparietal area (a receptor border against a connectivity gradient), the supramarginal
  gyrus (five architectonic areas against a dorsal/ventral junction split against a left/right
  asymmetry, none aligning), and the precuneus (three functional sectors against the architectonic
  pair 7Am / 7Pm).
- **gradient, not partition** — an axis whose **existence as an axis** is unsettled. PGa and PGp in
  the angular gyrus sit on a stated rostro-caudal gradient, and a gradient is not a border.
  **(Claude's reading, and it is a data-model finding.)** Every unknown extent in the sections before
  this one was an unmeasured *size* — the axis existed and its length was open. **Here a count would
  not close the question**, because whether an edge can terminate on PGa is a question about whether
  PGa is a place. The module carries this as an extent kind distinct from *to derive*, and
  `allocate()` refuses a sub-element request against such an axis **for a different stated reason**
  than it refuses an unsized one.
- **count is an analogy** — a figure obtained by comparison rather than by measurement. Both priced
  rows in this section are analogies. **(Claude's reading.)** A count and an analogy occupy the same
  field and behave identically in arithmetic, so **the only place the difference can live is a flag
  set at the moment the number is written**; it cannot be recovered afterwards. `allocate()` returns
  the array size and the flag together, so a caller cannot obtain the size without the caveat.

## Two endpoint kinds the module cannot resolve, and must not resolve

- **A target that is not a node.** Two edges terminate on **networks** — the ventral-attention
  frontoparietal network, and default-mode partners. A network is a set of regions defined by
  correlated activity, not by a projection. **Naming its members turns one edge into several and
  asserts that each member receives the same payload**, which is not what the network claim says. The
  module marks the edge and leaves it unresolved, **so the arity stays visibly unknown rather than
  silently multiplied.**
- **An edge that exists because the other end declared it.** Two output edges to the lateral
  intraparietal area were written at this end **so that the edge would have two ends**, both Class 2,
  both carrying the note that nothing read establishes the projection exists. **(Claude's reading.)**
  An edge written to make a two-ended diff pass has evidence on neither side, and **the diff it passes
  is the very check that would have caught it.** A surplus edge runs and produces output, which is
  what makes this class of defect harder to find than a missing one. The module marks both, counts
  them, and **refuses to build a graph containing them without a decision**, naming the two edges
  rather than reporting a count. **Five further payloads in this section were transcribed from a far
  end**, and the architecture states twice that such agreement certifies nothing; those five are
  marked at the lines that carry them.

## Far-end dependencies recorded rather than opened

This session holds `Brain_architecture_06_posterior_parietal` and no other architecture file, so
**every far end below is recorded as a dependency and none was read here.** Naming the file and
structure is the permitted response; writing an algorithm whose far end was never read is not.

- **`04_dorsal_visual_parietal_stream`** — the lateral and ventral intraparietal areas: the two counts
  this section's sizing is an analogy to, and the producer of the priority map.
- **`05_sensorimotor_loop`** — the secondary somatosensory cortex, superior parietal area 5, primary
  motor cortex and the medial motor fields.
- **`01_visual_pathway`** — the inferotemporal cortex entry, for object identity.
- **`11_frontal_lobe`** — prefrontal areas 46 and 12, the ventrolateral entry, the premotor entry,
  and the orbitofrontal / ventromedial entry.
- **`17_insula_claustrum_habenula`** — the posterior cingulate and retrosplenial cortices, and the
  structure this file names as **cingulate area 23**, which is that file's posterior cingulate cortex
  written as a Brodmann number.

**Some endpoints in this file carry no stem, and that is a state rather than a gap.** A stem is
written only where the far file is checked against this one, so an unstemmed endpoint is
**unchecked** and **not a claim that no far end exists.** The architecture leaves several endpoints
unstemmed whose file it did read for other edges — ventral premotor area F5, the ventrolateral
prefrontal / Broca and premotor target, and both edges to the lateral intraparietal area — and **this
rung does not supply them.** Writing a stem here would be an independent sweep, which derives
connectivity at the wrong rung: the endpoint would resolve and nothing would have checked that it
resolves right.

**Four endpoints have no entry in any of the files the architecture's own pass read**, and they
are not far-end dependencies but missing
producers: **V6**, **the dorsal subdivision of V6A**, **the ventral subdivision of V6A**, and **the
caudal intraparietal area**. The repair is a **source-rung** one — a structure with no entry anywhere
cannot be supplied at this rung, and stubbing it here would supply the signal while destroying the
two-ended payload check that is the only thing making the edge verifiable.

---

## Anterior intraparietal area
### Contract — copied from the architecture, character for character

*All eight fields of the architecture entry, in the order the architecture writes them. Nothing
below this heading is this file's writing.*

- **Function → structure.** The parietal node of the visuomotor grasping circuit — it **transforms
  an object's 3-D physical properties (size, shape, orientation) into a hand configuration for
  grasp.** Neurons are selective for object shape, size and orientation and for **grip type,
  precision against whole-hand.** Object attributes are encoded as a **gradient** running from this
  area through ventral premotor area F5 to primary motor cortex — **object first in visual terms,
  then as an appropriate grip.**
  **Divisional sub-elements: none, and it is established rather than absent.** Receptor-architectonic
  mapping of the whole intraparietal sulcus divides its neighbours — the ventral area into medial and
  lateral parts, the lateral into dorsal and ventral, the medial into dorsal and ventral — and leaves
  **this area undivided.** **That is a negative result from a study that would have found a division**,
  and the description records it as such rather than as unknown. **It is the only structure in this
  section whose divisional axis is closed.**

- **Inputs.** **← caudal intraparietal area** — **3-D surface shape from disparity and texture: the
  object's geometry, not its identity**; **the far end has no entry anywhere.** **← the rostral part
  of the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`) — the **priority map**,
  which object is the current target; two-ended, **and the two ends agree in the same words, which
  certifies less than a diff of two independently written ends.** **← lower-bank superior temporal
  sulcus / middle temporal gyrus** (`01_visual_pathway`, the inferotemporal cortex entry) (ventral
  stream) — **object identity**, so the transformation here draws on ventral-stream identity as well
  as dorsal-stream geometry.
  **The producer declares this edge, typed as object identity in the same words this entry uses, so
  the edge is two-ended and typed at both ends.**
  **What survives from the old note is the verification state, not the absence.** The producer marks
  this edge Class 1 from a macaque retrograde-tracer study located by web search, with **the abstract
  only read and no full paper opened**, awaiting verification under the verified-only rule. **So the
  edge is declared at both ends and verified at neither.**
  **← the secondary somatosensory cortex** (`05_sensorimotor_loop`) — tactile object identity and
  contact state. **Two-ended, confirmed**; the producer declares `→ the anterior intraparietal area`
  by name and carries no type for it, so the payload above is this end's alone.
  **← the ventral intraparietal area** (`04_dorsal_visual_parietal_stream`) — object location and
  motion in head- and body-centred coordinates. **The producer declares this edge and types it in the
  same words**, and adds what this end does not: that it is **the one edge out of that entry whose
  two ends agree.** **← superior parietal area 5** (`05_sensorimotor_loop`, principally area PE) —
  **limb state, the arm and
  hand configuration against which the object's geometry has to be expressed**; payload otherwise
  owed. **← prefrontal areas 46 and 12** (`11_frontal_lobe`) — goal / task context, owed.
  **Both producers declare this edge by name.** The dorsolateral entry
  declares `→ the anterior intraparietal area` **on its own line, by name and not as a class**, and
  records this entry's own two-area phrasing as its reason. The ventrolateral entry declares
  `→ the anterior intraparietal area, from area 12` — **by name, and attributed to the sub-element
  this line names.** **So the edge is two-ended at both producers, and the pair of them supplies the
  area-46 / area-12 split this line asserts from one side.** **Payload remains owed at all three
  ends**: goal / task context is a function and not a payload, and neither producer types it either.
  **What is gone is the absence, not the owed payload** — and the two producers agreeing on the
  sub-element division is the stronger half of the result.

- **Outputs.** **→ ventral premotor area F5** → primary motor cortex hand representation — **a hand
  configuration**: grip type and the wrist and finger posture the object affords. **This is the
  payload change that is a translation between ontologies** — an object's physical properties go in
  and **a posture of the body** comes out. **→ the medial intraparietal area** — grasp-related object
  geometry into the reach channel, **where the two parieto-frontal channels actually meet**; payload
  owed at both ends. **→ the dorsal subdivision of V6A** — the same geometry, **and the far end has
  no entry.**

- **Sizing.** Basis: **per hemisphere. ~15M neurons**, soft — **by analogy to the neighbouring
  measured intraparietal areas**, the lateral at ~20M and the ventral at ~12M, **whose counts are in
  `04_dorsal_visual_parietal_stream` and are right as quoted there.** No clean human count. Fan-in
  **to derive** on every edge. At the
  16-bit ceiling: **30.00 MB.**

- **Shape.** Rank 2: **(lamina, position)** — eight laminae, layer 4 undivided, and a position axis
  **to derive**. **No divisional axis, and that is a result rather than a gap.** **Tangential
  sub-elements: owed** — the Function asserts selectivity for grip type, a categorical property that
  is columnar elsewhere in this section, and **whether grip types cluster spatially was not
  established.**

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: **two of this entry's edges have far ends with no
  entry anywhere** — the caudal intraparietal area on the input side and the dorsal subdivision of
  V6A on the output side, so **the entry is open at both ends of the geometry channel.** Per-edge
  latency: satisfied.

- **Justification (biological).** **The internal edges are the standard laminar block and nothing
  else, and the omission is the entry.** Object geometry arrives on one set of edges and a hand
  posture leaves on another, and **nothing at any level this description records says what happens in
  between.** The description calls this the completion test biting: **the payloads at both ends are
  writable and the step that converts one to the other is not described.** That is the strongest form
  the detector can take — **not an untyped payload, but two typed payloads with no stated transform
  between them.**

### Representation — declared here for the three lines this entry produces

| line | units | range and normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| → ventral premotor area F5 — **unstemmed** | **grip type: a category label, not a number. Wrist and finger posture: owed** | owed | event-driven | **owed** — a posture of the body, and the description does not say in what frame |
| → the medial intraparietal area | **owed at both ends** | owed | event-driven | owed |
| → the dorsal subdivision of V6A | **owed — and the far end has no entry** | owed | event-driven | owed |

**The first line is named and not typed, and the distinction is load-bearing here.** *Grip type,
precision against whole-hand* is a category with two stated members and no stated encoding; *the
wrist and finger posture the object affords* has no units, no range and no frame. **A payload that
can be described in a sentence is not thereby a payload that can be put on a wire**, and the module
records the line as carrying a named-but-untyped value rather than as typed.

**Inherited representation on the input side.** Seven input lines are declared at their producers
and inherited here; **none of those producers is restated**, so the module records the inheritance
only. The one input whose type is fully written at this end is the
priority map from the rostral lateral intraparietal area — **one scalar per retinotopic location**,
and the architecture records that the two ends agree in the same words, **which certifies less than a
diff of two independently written ends.**

### Algorithm

- **Transform.** **The laminar block, and nothing else — and that is the entry.** The writable
  operation is the standard internal block over eight laminae with the threshold gate at every
  population. **The transform the entry exists for has no standard name and no description**, and
  under §5 that is recorded as a finding about the structure rather than filled in: object geometry
  arrives typed, a hand configuration leaves named, **and nothing at any rung says what happens
  between them.** This is the strongest form the completion test's detector takes — **not an untyped
  payload, but two payloads and no stated transform between them.** **The gap is exactly one function
  wide and its signature is known**, which is what distinguishes it from the supramarginal case.
  **Repaired at the source rung, against the literature. It may not be filled here**; an invented
  coordinate-change operation would read exactly like a derived one.
- **Arrays.**
  - `active` — shape **(lamina = 8, position = to derive)**, dtype **bool** (1 bit per neuron),
    range **{0, 1}**, unitless. At the stated count: **1.875 MB.**
  - `threshold` — shape as `active`, dtype **uint16**, range **to derive**, unit **input count**.
    **16 bits is a ceiling, not a derived width**: the width a threshold needs is set by the fan-in
    it counts against, and **every fan-in in this entry reads *to derive*.** At the ceiling:
    **30.00 MB.**
  - `count` — shape as `active`, dtype **uint16**, range **0 … fan_in**, unit **input count**.
    Intermediate, not state.
  - **Input arrays: seven lines**, each an `active` slice of a producer in another file, of a shape
    that file holds. **Output arrays: three lines.** No array may be allocated for the divisional
    axis: **there is none, and its absence is a negative result from a study that would have found a
    division**, not a gap.
- **Parameters.** `threshold[j]` — unit input count, value **not set**, origin **chosen by no one
  yet**: no rule at any rung writes an initial threshold, and the learning rule that would move it is
  Micky's. `fan_in(j)` — **not set**, origin connection topology, which requires explicit agreement
  before it is touched. `sign(i, j)` — **not set anywhere.** The lamina set **{1, 2, 3, 4, 5a, 5b,
  6a, 6b}** — origin **the architecture's own field**, held per structure.
- **Update equation.** `count[j] = Σ_{i ∈ fan_in(j)} sign(i, j) · active_source[i]`, then
  `active[j] = count[j] ≥ threshold[j]`, over the internal block **4 → 2/3**, **2/3 → 5a**,
  **2/3 → 5b**, **5a → 2/3**, **6a → 4** and **6a → 5a** at opposite signs, **6b → 6a** arousal-gated,
  with recurrence within **4** and within **2/3**. **The equation is complete in form and unrunnable
  in fact**, on the three unset terms named in the preamble. **No update order is written**, because
  the recurrent edges and the 5a ↔ 2/3 loop each read a value the same update writes, and choosing
  which value that is would be choosing the scheduling discipline.
- **State carried between updates.** `active` — shape and dtype as above, initial value **all zero**,
  written at the end of the update. **It is the only state this entry holds**, and it is state solely
  because the recurrent and reciprocal edges read it. **State memory is not parameter memory and the
  two are never summed.** `threshold` is a parameter and is not state.
- **Edge storage.** `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`.
  **Every term is unavailable on every edge of this entry.** `line_count` — fan-in is *to derive* and
  no axon count is stated. `latency` — *to derive*, on all edges. `update_interval` — unset, and
  Micky's. `bytes_per_value` — available on no line here, since the one fully typed payload is an
  inherited input rather than a line this entry produces. **The specification anticipates one unset
  term and this entry has four**, which is recorded rather than estimated: a figure computed from
  assumed terms would enter the file looking exactly like a derived one.
- **Adaptation.** **No parameter in this entry changes, because no rule says one does.** The learning
  rules are Micky's and are not set. **The entry records that the rule is not set; it does not assume
  one.** Nothing here may write `threshold` at run time until that decision exists.
- **Open.**
  1. **The transform itself** — the entry's whole subject. Source rung.
  2. **The caudal intraparietal area has no entry anywhere**, so the geometry input has no producer.
     Source rung. **A stub would supply the signal and destroy the payload check**, which is the only
     thing that makes the edge verifiable.
  3. **The dorsal subdivision of V6A has no entry anywhere**, so the entry is open at both ends of
     the geometry channel. Source rung.
  4. **Whether grip types cluster spatially** — the Function asserts selectivity for a categorical
     property that is columnar elsewhere in this section, and the tangential sub-element slot reads
     **owed.** Until it is answered the position axis carries no compartments and no edge may
     terminate below the region level. Source rung.
  5. **The object-identity input is declared at both ends and verified at neither** — Class 1 from a
     macaque retrograde-tracer study with the abstract only read. **Species and method travel with
     the edge**; the module does not promote it.

---

## Medial intraparietal area / parietal reach region
### Contract — copied from the architecture, character for character

*All eight fields of the architecture entry, in the order the architecture writes them. Nothing
below this heading is this file's writing.*

- **Function → structure.** The parietal node of the reach channel — it encodes **the direction, and
  more weakly the amplitude, of an intended reach**, in a **mixture of gaze-centred, hand-centred and
  intermediate reference frames**, and is **effector-specific**, more active before contralateral-arm
  than eye movements.
  **"Parietal reach region" is a functional label over more than one area, and the areas differ.**
  Myeloarchitecture and retrograde tracing divide the medial bank into **three**: the dorsal
  subdivision of V6A, this area, and the intraparietal subdivision of area PE. Against V6A this area
  takes **denser input from somatosensory areas, primary motor cortex and the medial motor fields**
  while V6A takes the stronger visual input; the intraparietal subdivision of PE emphasises anterior
  parietal and ventral premotor connections and, **unlike this area, projects to the spinal cord.**
  **So the three are ordered by how close to movement they sit, and treating the reach region as one
  thing loses that ordering.** **Two of the three have no entry in the source.**

- **Inputs.** **← V6, and the ventral subdivision of V6A** — target location in the visual field,
  retinotopic; **neither far end has an entry, and this is the edge that supplies the visual half of
  the frame mixture**, so its absence is not bookkeeping. **← the primary somatosensory cortex,
  superior parietal area 5, the primary motor cortex and the medial motor fields**
  (`05_sensorimotor_loop`) — current arm
  configuration, **the edge that makes the frame mixture possible**; **the frame is contested at the
  producer rather than body-centred**, the reported frames being **body-,
  shoulder- and hand-centred across studies**, and in area PE a memorised target's distance encoded
  **relative to the initial hand position**. **On the payload rule the frame is part of the payload,
  so this line is payload contested rather than owed** — measured repeatedly, and the measurements
  disagree. **The line names four sources and splitting it is owed.** **← the anterior intraparietal
  area** — grasp-related object geometry, owed. **← the ventral intraparietal area** — **body-centred
  locations, for reach**, per the producer, whose end is more specific than this one was.
  **← the medial superior temporal area** — owed at both ends. **← superior parietal area PEc** —
  spatial context and self-motion, owed, **and whether this and the area-5 output are one edge or two
  is owed.** **← the angular gyrus** and **← the precuneus** — owed, **both producers in this section
  and both declaring the output edge only at this end.**
  **← temporo-parieto-occipital cortex** — **a class that does not resolve to a named region.**
  **← cingulate area 23, dorsocaudal premotor area F2, and ventral premotor areas F4 and F5**
  (`11_frontal_lobe` for the premotor pair) — owed, **a return limb from the very areas the output
  edge targets.** **Two of the three far ends declare it.** The premotor entry in that file declares
  `→ the medial intraparietal area, from F2` and `→ the medial intraparietal area, from F4 and F5` as
  **two separate bullets, split precisely because they leave from different sub-elements** — which are
  the sub-elements this line names. **The cingulate limb crosses to `17_insula_claustrum_habenula`
  under a name that file does not use** — area 23 is the posterior cingulate cortex there, and that
  entry declares no intraparietal target, so this limb's mark holds and the repair is owed at that
  end. **Splitting this line is owed for a reason beyond tidiness** — two of its three
  sources are two-ended and one is unchecked, and one line cannot carry three states.

- **Outputs.** **→ dorsal premotor cortex (area F2)** → primary motor cortex — **a reach vector**:
  direction and, more weakly, amplitude, **in a mixture of gaze-centred, hand-centred and
  intermediate frames**, effector-specific. **The mixed frame is not sloppiness in the description —
  the code genuinely is intermediate, and a consumer that assumes one pure frame will be wrong.**
  **The far end declares it by name and names F2** (`11_frontal_lobe`): the premotor entry declares
  `← the medial intraparietal area, terminating on F2` — **the sub-element named, on its own line, not
  as a class.** **The two ends name the same sub-element from both sides.** Payload owed at the far
  end still; it carries no type for this edge. **→ superior parietal area 5**,
  onto the medial bank (area PEa) (`05_sensorimotor_loop`) — payload owed. **Two-ended**: that
  entry's Inputs slot carries a four-source line — the medial bank of
  the intraparietal sulcus, the parietal opercular areas PGop and PFop, and the retroinsular area —
  including the medial intraparietal limb. **This is that producer end**, and it names the medial
  bank and area PEa in the same terms the consumer uses. The other three sources on that line are
  untested here. **The reciprocal pair is closed and its two limbs are not symmetric:** the
  descending limb carries limb state in a contested frame, **this limb has no typed payload at all**,
  and the description says the asymmetry is the finding — **the reach literature reads the
  parietal-to-frontal direction and has not read this one.**

- **Sizing.** Basis: **per hemisphere. ~15M neurons**, soft, **by the same intraparietal-neighbour
  analogy as the grasp entry**, no clean human count. At the 16-bit ceiling: **30.00 MB.**
  **No per-division count under either parcellation.**

- **Shape.** Rank 3: **(division, lamina, position)** — **and the division axis has two incompatible
  versions.** Receptor architecture gives **a dorsal and a ventral part**, separated in the same
  mapping that divides the lateral and ventral intraparietal areas, **their separate payloads owed
  and the reach literature not using the division at all** — recorded as **a division the physiology
  has not caught up with.** Tracer plus tractography gives instead **an anterior and a posterior
  sector**, on gradient-like connectivity profiles rather than on a border. **A gradient with sectors
  and a receptor border with two parts are not the same claim about the same tissue**, and this
  description has no basis for choosing. The lamina axis carries **eight laminae with two bands of
  Baillarger**. Tangential: **unknown.**

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: **the reach channel's visual producer does not exist**,
  so this entry cannot be instantiated with its stated input. Per-edge latency: satisfied.

- **Justification (biological).** **The frame mixture has no declared internal mechanism, and the
  hole is worse than a missing edge.** The output payload is stated to be a mixture of gaze-centred
  and hand-centred frames; two incoming edges supply the two frames — the visual one from V6 and
  V6A, the postural one from the somatosensory and motor areas; **and no internal edge says where
  they meet.** **Divisional internal edges are owed under either parcellation.** The description
  names the shape directly: the same hole sits at the ventral intraparietal gain field and at the
  anterior intraparietal transform, **three neighbouring entries whose stated function is a
  coordinate change and none of which can say where the change happens** — and here **the mixture
  lacks both a mechanism and one of its two inputs.**

### Representation — declared here for the two lines this entry produces

| line | units | range and normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| → dorsal premotor cortex, area F2 (`11_frontal_lobe`) | **direction, and more weakly amplitude, of an intended reach**; units owed | owed | event-driven | **a mixture of gaze-centred, hand-centred and intermediate frames** |
| → superior parietal area 5, area PEa (`05_sensorimotor_loop`) | **owed** | owed | event-driven | owed |

**The mixed frame is the declared frame, not a missing one, and the module must carry it as a
value.** The architecture is explicit that the code genuinely is intermediate and that **a consumer
assuming one pure frame will be wrong.** Writing *frame: unknown* here would translate a stated
property into an absence; writing *gaze-centred* would pick one of three. The module carries **mixed**
as a frame value distinct from both, and a consumer that cannot handle a mixed frame **fails loudly
rather than reading the line as though it were pure.**

**The reciprocal pair is closed and its two limbs are not symmetric.** The descending limb into this
entry carries limb state in a **contested** frame; **this outgoing limb to area 5 has no typed payload
at all.** The architecture records the asymmetry as the finding — the reach literature reads the
parietal-to-frontal direction and has not read this one — so the module carries the pair as **closed
and asymmetric**, which is a different state from either limb being absent.

**Inherited representation on the input side, and one input is contested rather than owed.** The arm
configuration arriving from the primary somatosensory cortex, superior parietal area 5, the primary
motor cortex and the medial motor fields reads **payload contested — not owed**: body-, shoulder- and
hand-centred frames are reported across studies, and in area PE a memorised target's distance is
encoded relative to the initial hand position. **Measured repeatedly, and the measurements disagree.**
The module holds *contested* and *owed* as separate states and refuses to normalise them: **an owed
payload points at an experiment to run, a contested one at a reconciliation**, and collapsing them
discards a real result in one direction and manufactures one in the other.

### Algorithm

- **Transform.** **The laminar block, and the frame mixture is not described.** The output is stated
  to be a reach vector in a mixture of frames; two incoming edges supply the two frames — the visual
  one from V6 and the ventral subdivision of V6A, the postural one from the somatosensory and motor
  areas — **and no edge says where they meet.** No standard name is available for the missing step,
  and it is recorded as a finding. **This is worse than the grasp entry's version of the same hole**,
  because **one of the mixture's two inputs has no producer anywhere**, so the mechanism is missing
  *and* an operand is missing. Source rung, against the literature.
- **Arrays.**
  - `active` — shape **(division = refused, lamina = 8, position = to derive)**, dtype **bool**,
    range **{0, 1}**, unitless. At the stated count: **1.875 MB.**
  - `threshold` — shape as `active`, dtype **uint16**, unit input count, range **to derive**; 16 bits
    is the ceiling for the reason given at the previous entry. At the ceiling: **30.00 MB.**
  - `count` — shape as `active`, dtype **uint16**, intermediate.
  - **The division axis cannot be allocated, and the reason is not that it is unsized.** Two
    incompatible parcellations are held side by side: **dorsal / ventral** by receptor architecture,
    and **anterior / posterior sectors** on gradient-like connectivity. **A border and a gradient are
    not the same claim about the same tissue**, and there is **no per-division count under either.**
    `allocate()` refuses a sub-element request here with **contested scheme** as its stated reason,
    which is distinct from the *unsized* refusal.
  - **No array for the bands of Baillarger.** They are a property of the lamina axis — the fibre
    plexus in layers 4 and 5b — and not a cell population.
- **Parameters.** As the previous entry: `threshold[j]` unset with no rule to write it, `fan_in(j)`
  unset, `sign(i, j)` unset. The lamina set is the architecture's own field, **eight laminae, with
  two bands of Baillarger recorded on the axis and not as a population.**
- **Update equation.** As the previous entry, over the same internal block. **Divisional internal
  edges are owed under either parcellation**, so the module has no internal graph below the lamina
  level to write, in either scheme.
- **State carried between updates.** `active`, all zero at start, written at the end of the update;
  state only because of the recurrent and reciprocal edges. Not summed with parameter memory.
- **Edge storage.** `line_count` unknown, `latency` *to derive*, `update_interval` unset,
  `bytes_per_value` unknown on both produced lines. **Four terms, none available.**
- **Adaptation.** No parameter changes; no rule is set; the rule is Micky's. Not assumed.
- **Open.**
  1. **V6 and the ventral subdivision of V6A have no entry anywhere**, and this is the edge that
     supplies **the visual half of the frame mixture** — so the absence is not bookkeeping. Source
     rung. The architecture names V6A as the origin of the whole reach channel, which means **the
     reach channel is described from its second stage onward.**
  2. **The frame mixture has no mechanism.** Source rung.
  3. **Two input lines carry more than one state each and splitting is owed.** The arm-configuration
     line names **four sources**; the return-limb line names **three**, of which two far ends declare
     the edge and one is unchecked. **One line cannot carry three states**, and the module cannot give
     per-source arity while they are merged. Architecture rung for the split, source rung for the
     arity.
  4. **`cingulate area 23` is `17_insula_claustrum_habenula`'s posterior cingulate cortex**, written
     here as a Brodmann number while every other reference in this file uses the region name. **The
     endpoint is a cross-file edge that was invisible as one.** Architecture rung.
  5. **Whether the area-5 output and the PEc input are one edge or two** — owed. Source rung.
  6. **Two of the three areas the "parietal reach region" label covers have no entry** — the dorsal
     subdivision of V6A and the intraparietal subdivision of area PE. **The three are ordered by how
     close to movement they sit**, and one of the two missing ones projects to the spinal cord while
     this one does not, **so treating the reach region as one thing loses that ordering.** Source rung.

---

## Supramarginal gyrus
### Contract — copied from the architecture, character for character

*All eight fields of the architecture entry, in the order the architecture writes them. Nothing
below this heading is this file's writing.*

- **Function → structure.** Polymodal somato-motor association at the anterior inferior parietal
  lobule — **tactile and proprioceptive integration, praxis and tool use, and, left-lateralised,
  phonological processing.** The frontoparietal mirror and action-observation system runs through
  PF/PFG. Its ventral part, with the posterior superior temporal sulcus, forms the **right-dominant
  temporoparietal junction** of the ventral-attention network — **stimulus-driven reorienting to
  behaviourally relevant events outside the current focus.** The left gyrus anchors the
  temporoparietal phonological route of language via the arcuate fasciculus.
  **Cytoarchitectonically it is five areas, not one: PFop, PFt, PF, PFcm, PFm.**

- **Inputs.** **← the secondary somatosensory cortex** (`05_sensorimotor_loop`) — **the object-level
tactile payload: texture,
  shape and material, contact-point invariant.** **The producer declares this edge only inside its
  `→ posterior parietal cortex` class and not by name** — so this consumer is a located candidate
  for that class, and naming it is owed there. **← superior parietal area 5**
  (`05_sensorimotor_loop`) — body configuration;
  **the far end was transcribed from this one, so the agreement certifies nothing.**
  **← posterior superior temporal gyrus / Spt** — **the auditory-to-motor mapping and phonological
  form**; **far end in the auditory file, not read, status unchecked.** **← the medial superior
  temporal area** — owed at both ends. **← the lateral intraparietal area** — **the priority
  (salience) map**, one scalar per retinotopic location ranking it by behavioural priority.
  **← the middle temporal area** — motion, owed, **and the producer declares nothing.**
  **← ventrolateral prefrontal cortex (Brodmann areas 44 and 45)** (`11_frontal_lobe`), reciprocal via
  the arcuate fasciculus and superior longitudinal fasciculus III — task and articulatory context,
  owed. **The two prefrontal producers are in different states and must not be carried as one
  judgement.** The ventrolateral entry declares
  `→ the supramarginal gyrus, reciprocally, via the arcuate fasciculus and superior longitudinal
  fasciculus III` — **by name, naming both tracts this line names.** Broca's entry declares
  `→ temporoparietal cortex, reciprocally` as a **class**, and resolves this gyrus as its one named
  member — **still a class, and still the weaker state.** **The two prefrontal producers this line
  compresses into one endpoint are in different states**: Brodmann areas 44 and 45 are split across
  two structures in
  that file, and this line addresses them as one.

- **Outputs.** **→ ventrolateral prefrontal / Broca and premotor cortex** — **two things this
  description can name and not type**: a **praxis / action-sequence code**, the learned structure of
  a skilled act, and, on the left, a **phonological code**, the sound-form of words for the
  articulatory route. **Payload only partly writable — owed:** *the plan of a skilled action* has no
  units and no frame, **and calling it a code does not make it one.** The description marks this as
  the first entry where the slot cannot be filled honestly, **and the detector working rather than
  failing.** **Splitting is owed** — the two codes go to different places and only one is
  left-lateralised. **→ the ventral-attention frontoparietal network** — **a reorienting signal:
  something behaviourally relevant just happened outside the current focus. A one-bit interrupt with
  a location attached**, as far as this description can determine. **The endpoint is a network and
  does not resolve.**
  **Its frontal candidate exists and the endpoint still does not resolve, which is the finding.**
  `11_frontal_lobe`'s right inferior frontal gyrus is the frontal node the network name
  implies, and **that entry declares `→ right temporoparietal cortex, reciprocally` as a class of its
  own**, marked there as unchecked with its far end placed in the auditory file. **This entry's own
  Function names the right-dominant temporoparietal junction, so the candidate that file is reaching
  for is here.** **But neither end names the other structure: this line declares a network and that
  line declares a cortical class, and the two descriptions overlap without either resolving.**
  **Two unresolved classes that point at each other are not an edge**, and treating the overlap as
  confirmation would build a two-ended edge out of two absences. **What is established is where the
  repair belongs** — one of the two ends must name a structure, and both ends are now known to be
  waiting on the other. **Also checked: that file's right inferior frontal entry declares no parietal
  input of any kind**, so the reciprocal limb this line implies has no consumer end there either.
  **→ the lateral intraparietal area** — owed, **asserted at the consumer's end
  with no independent support here**, and marked: **nothing read establishes that this projection
  exists.**

- **Sizing.** Basis: per hemisphere. **Neurons: unknown.** No clean human per-area count, as for
  prefrontal association cortex; what is stated instead is **association-cortex packing of order
  20,000 neurons/mm³**, with the human inferior parietal lobule **greatly enlarged over the
  macaque.** **A packing density is not a count and cannot be promoted into one without a volume,
  and the grey-matter volume slot reads unknown.** **Structure total: to derive.** Axons: the arcuate
  fasciculus and superior longitudinal fasciculus III, counts unknown.

- **Shape.** Rank 3: **(area, lamina, position)** — **five areas, and two further divisions that
  cross-cut them.** The five are **cytoarchitectonic before they are functional**, their separate
  payloads owed, and **every edge above terminates on the whole gyrus.** The Function asserts **at
  least three functionally distinct jobs**, so an edge terminating "on the supramarginal gyrus" is
  under-specified in the same way an edge terminating on the undivided lateral intraparietal area
  was; **splitting is owed and the basis for it already exists.** The second division is the
  **dorsal / ventral** temporoparietal-junction split and the third is the **left / right** functional
  asymmetry, **and neither maps cleanly onto the five architectonic areas.** Tangential: **unknown**,
  no columnar or compartmental repeat found.

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: **one output edge terminates on a network that does
  not resolve to nodes**, and the nearest candidate found — the insula (`17_insula_claustrum_habenula`)
  — **declares no parietal source**, so if the edge reaches it that end is undeclared too.
  **The claim holds**: that entry declares ten inputs and not one is parietal.
  *(One near-miss, recorded so a later keyword pass does not overturn this wrongly: that entry's
  vestibular input terminates on the **parieto-insular vestibular cortex**, which carries "parietal"
  in its name and is insular territory rather than a parietal producer.)*
  Per-edge latency: satisfied.

- **Justification (biological).** **This entry fails the completion test at both ends, and it is the
  only one in the section that does.** The internal edges are the laminar block; **no edge between
  any two of the five areas is recorded anywhere, in either direction**; and the somato-to-praxis
  conversion is owed. Object-level tactile payload and body configuration arrive, a praxis code
  leaves, **and unlike the grasp entry the output payload is not writable either.** So where the
  anterior intraparietal area has two typed ends and no stated transform, **this entry has one typed
  end, no transform, and an output that cannot be typed** — a strictly weaker position, on a region
  whose count is also unknown.

### Representation — declared here for the three lines this entry produces

| line | units | range and normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| → ventrolateral prefrontal / Broca and premotor cortex — **unstemmed** | **praxis / action-sequence code: none. Phonological code: none** | owed | event-driven | **none stated** |
| → the ventral-attention frontoparietal network | **one bit**, plus a location | interrupt: {0, 1}; location owed | event-driven | **the location's frame is owed** |
| → the lateral intraparietal area — **unstemmed** | **owed** | owed | event-driven | owed |

**The first line is the one the architecture marks as the first place the slot cannot be filled
honestly, and the module records it that way.** *The plan of a skilled action* has no units and no
frame, and **calling it a code does not make it one.** The line also carries **two** codes to
**different** places, only one of them left-lateralised, so **splitting is owed** and the module
cannot give either half its own representation while they share a line.

**The second line is the section's one partly-typed output, and the typed part is a single bit.**
*Something behaviourally relevant just happened outside the current focus* is a one-bit interrupt;
the location attached to it has no stated frame. **The module carries one bit as one bit** rather
than promoting the line to typed on the strength of it, because the location is the part a consumer
would have to agree about.

**The third line exists because the far end declared it.** It is Class 2, **nothing read establishes
that the projection exists**, and it is one of the two edges the module refuses to build a graph
around without a decision.

**Inherited representation on the input side, and two inputs are typed.** The object-level tactile
payload from the secondary somatosensory cortex — **texture, shape and material, contact-point
invariant** — and the priority map from the lateral intraparietal area — **one scalar per retinotopic
location** — are the two. The body-configuration input from superior parietal area 5 is **transcribed
from this end at the far end, so its agreement certifies nothing**, and the module marks it rather
than counting it as a two-ended confirmation.

### Algorithm

- **Transform.** **The laminar block, and the somato-to-praxis conversion is absent.** No standard
  name is available and none is invented. **(Claude's reading, and it separates two things the same
  mark covers.)** This entry's version of the missing transform is **strictly worse than the grasp
  entry's**: there the gap is one function wide with a known signature, because both ends are typed.
  **Here the output is not typed either, so the gap has no signature** — a module could not even state
  what the missing operation would have to return. **The entry fails the completion test at both the
  transform and the output**, on a structure whose count is also unknown. Source rung, against the
  literature.
- **Arrays.**
  - `active` — shape **(area = 5, lamina = 8, position = to derive)**, dtype **bool**, range
    **{0, 1}**, unitless. **Size cannot be computed: the neuron count is unknown.**
  - `threshold` — shape as `active`, dtype **uint16**, unit input count, range **to derive**.
    **Size cannot be computed.**
  - `count` — shape as `active`, dtype **uint16**, intermediate.
  - **The area axis has five named members and no counts.** PFop, PFt, PF, PFcm and PFm are
    **cytoarchitectonic before they are functional**, their separate payloads owed, and **every edge
    in the contract terminates on the whole gyrus.** `allocate()` refuses a sub-element request with
    **unsized** as its reason — distinct from the medial intraparietal area's *contested scheme* and
    from the angular gyrus's *gradient, not partition*.
  - **Two further divisions cross-cut the five and neither maps cleanly onto them**: the
    **dorsal / ventral** temporoparietal-junction split, and the **left / right** functional
    asymmetry. The module holds all three schemes and chooses none.
- **Parameters.** `threshold[j]`, `fan_in(j)` and `sign(i, j)` unset as elsewhere. **The axon counts
  are unknown too** — the arcuate fasciculus and superior longitudinal fasciculus III are named and
  not counted — so no line count is available for any edge leaving on them.
- **Update equation.** As the other entries, over the same internal block. **No edge between any two
  of the five areas is recorded anywhere, in either direction**, so even with the five allocated the
  internal graph above the lamina level would be empty. **That is a recorded absence and not an
  omission here.**
- **State carried between updates.** `active`, all zero at start, written at the end of the update.
  **Shape unknown, so the state figure is unknown**, and it is not summed with parameter memory.
- **Edge storage.** Four terms, none available: `line_count` unknown and the axon counts stated
  unknown, `latency` *to derive*, `update_interval` unset, `bytes_per_value` available on no
  produced line except the one-bit component of the reorienting interrupt, whose location component
  is untyped.
- **Adaptation.** No parameter changes; no rule is set; the rule is Micky's.
- **Open.**
  1. **The somato-to-praxis conversion**, and **the output payload**. Both source rung. **This is the
     only entry in the section failing at both.**
  2. **The neuron count is unknown, and this row is one measurement short of a count.**
     Association-cortex packing of order **20,000 neurons/mm³** is stated and the grey-matter volume
     reads unknown. **A density is one factor of a count and may not be promoted into one**, so
     `allocate()` refuses and **says which measurement is missing** rather than refusing generically.
     Source rung.
  3. **The ventral-attention network endpoint does not resolve, and its frontal candidate exists.**
     `11_frontal_lobe`'s right inferior frontal gyrus declares `→ right temporoparietal cortex,
     reciprocally` as a class of its own, and this entry's Function names the right-dominant
     temporoparietal junction — **so each end is an unresolved class pointing at the other.** **Two
     unresolved classes that point at each other are not an edge**, and the module must not treat the
     overlap as confirmation. **What is established is where the repair belongs**: one of the two ends
     must name a structure. Architecture rung for the naming, source rung for whether the projection
     exists.
  4. **The nearest resolved candidate declares no parietal source.** The insula entry in
     `17_insula_claustrum_habenula` declares ten inputs and not one is parietal, **so if the edge
     reaches it that end is undeclared too.**
  5. **The output line to the lateral intraparietal area is Class 2 with no primary source.**
  6. **Splitting the praxis and phonological codes is owed**, and **the two prefrontal producers this
     file compresses into one endpoint are in different states** — one declares by name and names both
     tracts, the other declares a class. **One endpoint cannot carry two states.** Architecture rung.

---

## Angular gyrus
### Contract — copied from the architecture, character for character

*All eight fields of the architecture entry, in the order the architecture writes them. Nothing
below this heading is this file's writing.*

- **Function → structure.** A high-level cross-modal integration and semantic hub at the
  temporo-parieto-occipital junction — **binds information across modalities and over time into
  concepts and events.** Central to semantic processing, reading, and number and arithmetic, and to
  the vivid re-experiencing of episodic memory; **a core node of the default-mode network.** The left
  gyrus is a semantic-integration hub complementing the anterior-temporal hub at the temporal pole;
  the right contributes to spatial, attentional and social cognition. **A rostro-caudal gradient runs
  from ventrolateral-prefrontal-coupled and more attentional (PGa) to hippocampal and
  default-mode-coupled and more mnemonic (PGp).**

- **Inputs.** **← occipitotemporal cortex** — **object and face identity**, and the description notes
  what has already been discarded upstream: **no hue**; **the producer declares nothing and nothing
  searched established the edge**, so it is **open at both ends.** **← superior temporal sulcus** —
  word and sound identity; **far end unchecked.** **← somatosensory association cortex** — tactile
  object identity; **both producers declare only a class.** **← the lateral intraparietal area**
  (`04_dorsal_visual_parietal_stream`) —
  the **priority (salience) map**, one scalar per retinotopic location, **modality-free**; **this is
  the one input whose payload is fully typed.** **The producer declares this edge and types it in the
  same words**, and adds what this end does not: the map leaves from the **ventral subdivision** and
  not the dorsal one, so reading it as coming from the whole area **is reading half the area.** **←
  the hippocampal formation** — **a completed
  episode**, the bound retrievable pattern, **addressable by any fragment of itself**; payload only
  partly writable, **and the one checkable property in hand is that it is content-addressable, which
  the identity codes on the other inputs are not.** **← the posterior cingulate cortex**
  (`17_insula_claustrum_habenula`), **← the precuneus**, **← medial prefrontal cortex**
  (`11_frontal_lobe`) — all owed. **The medial prefrontal limb is owed as an absence at the
  producer**: that file's orbitofrontal / ventromedial entry declares
  ten outputs and **not one is medial-parietal** — no angular gyrus, no precuneus, nothing on the
  medial wall behind the cingulate. **The traffic between that structure and this one runs one way**,
  parietal to prefrontal, on the two inputs it declares from this section.
  **The cingulate limb is two-ended and confirmed.** The producer sorts
  this edge with the precuneus and the medial prefrontal cortex into the same default-mode group this
  line lists it in — **two files grouping the same three edges the same way, from their own sides.**

- **Outputs.** **→ default-mode partners, the hippocampal formation, ventrolateral prefrontal
  cortex, lateral temporal semantic cortex** — **PAYLOAD UNKNOWN — OWED, AND THIS IS THE LOUD ONE.**
  The Function says this region binds across modalities and over time into concepts and events;
  **that sentence reads as complete right up until you try to say what leaves it on a wire, and then
  it fails** — a concept and an event have **no units, no range, no coordinate frame and no channel
  structure.** **The four far ends are in three states: one member two-ended, two untested, one a
  class that does not resolve.** `11_frontal_lobe`'s ventrolateral prefrontal entry declares
  `← the angular gyrus` **by name**, so that far end is two-ended and untyped rather than silent. The
  hippocampal and lateral-temporal members are untested, and the fourth is a network.
  **And a fifth consumer exists that this line does not name.** That file's orbitofrontal /
  ventromedial entry declares `← the angular gyrus`, marked **Medial** — a medial-prefrontal
  default-mode node that this line's *default-mode partners* would cover if the class were named out.
  **It declares an input this entry does not declare as an output under any specific name**, so the
  class has a consumer waiting on it. **Splitting is owed** — four targets, a fifth consumer declaring
  itself from the far side, and one non-payload. **→ the lateral intraparietal area** —
  owed, **asserted at the consumer's end, Class 2, no primary source names it.** **→ the medial
  intraparietal area** — owed, asserted at the consumer's end, **but this one does carry a primary
  source there.**

- **Sizing.** Basis: per hemisphere. **Neurons: unknown**, and **less recoverable here than
  anywhere else in the section**: the macaque has no angular gyrus in the strict sense, so **even a
  homology-based estimate is loose** — the analogy route that priced the two intraparietal areas is
  closed for this one. **Structure total: to derive.**

- **Shape.** Rank 3: **(division, lamina, position)** — **and the division axis is not known to be a
  partition.** **PGa** rostral and **PGp** caudal sit on a stated gradient, and **a gradient is not a
  border**: whether they are compartments an edge can terminate on, or two ends of a continuum with
  no boundary, **is not established** — the same limit the inferotemporal entry records for its
  continuous feature map, where a position is a coordinate and not a compartment. **The gradient
  sorts this entry's inputs if it is a partition** — prefrontal and priority-map inputs to PGa,
  hippocampal and default-mode inputs to PGp — **and assigning them would change the arity of six
  edges at once**, which is why the question is not idle. The **left / right asymmetry is not a
  sub-element** and is covered by the per-hemisphere convention, **but whether the gradient is the
  same on both sides is unknown.** Tangential: **unknown.**

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: **this entry's output cannot be instantiated at all**,
  since the payload is unwritable and three of its four targets do not declare the edge. Per-edge
  latency: satisfied.

- **Justification (biological).** **The load-bearing internal edge is the one that is missing.** The
  laminar block is present; **no PGa ↔ PGp edge is recorded in either direction.** The Function's
  claim is that this region *binds* across modalities and over time; the attentional and mnemonic
  streams arrive on **different divisions** by the gradient account; **so the binding, if it happens
  here, happens on an edge between the two divisions, and that edge is not written.**
  **And the location of the hole is precisely established, which is the entry's most useful
  property.** Every typed input arrives with a frame or an explicit absence of one — the priority map
  modality-free, the identity codes, the completed episode content-addressable. **The output has
  neither.** So the untypable step is **inside this entry, not inherited from a vague input** — the
  same shape as the temporal pole's amodal concept and the anterior insula's subjective feeling, and
  the three together are **the description's clearest statement of where it stops.**

### Representation — declared here for the three lines this entry produces

| line | units | range and normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| → default-mode partners, the hippocampal formation, ventrolateral prefrontal cortex, lateral temporal semantic cortex (`11_frontal_lobe` for the third) | **none — unknown, owed, and the architecture marks this the loud one** | none | event-driven | **none** |
| → the lateral intraparietal area — **unstemmed** | **owed** | owed | event-driven | owed |
| → the medial intraparietal area | **owed** | owed | event-driven | owed |

**Nothing typed leaves this entry, and that is the section's sharpest finding rather than a hole in
the table.** The Function says the region binds across modalities and over time into concepts and
events; **that sentence reads as complete right up until you try to say what leaves it on a wire.** A
concept and an event have **no units, no range, no coordinate frame and no channel structure** — four
absences, which is the entire Representation field.

**The location of the hole is precisely established, and that is what the module can use.** Every
typed input arrives **with a frame or with an explicit absence of one**: the priority map is
**modality-free**, the identity codes carry their modality, and the completed episode from the
hippocampal formation is **content-addressable, which the identity codes are not.** **The output has
neither a frame nor a stated absence of one.** So the untypable step is **inside this entry and not
inherited from a vague input**, and the module reports it as an internal gap rather than as
propagation.

**The first line carries four targets, one non-payload, and a fifth consumer declaring itself from
the far side.** `11_frontal_lobe`'s orbitofrontal / ventromedial entry declares `← the angular gyrus`,
marked Medial — **a consumer this line does not name, waiting on a class that has not been named
out.** **Splitting is owed**, and until it happens the module cannot give any target its own
representation.

**The second line exists because the far end declared it** — Class 2, no primary source names it, and
it is the second of the two edges the module refuses to build a graph around. **The third does carry a
primary source at the consumer's end**, so the two are not in the same state and are not marked the
same way.

**Inherited representation on the input side: three of nine typed, and the priority map's producer
is more specific than this end.** The lateral intraparietal area's map leaves from the **ventral
subdivision**, not the whole area, **so reading this input as coming from the whole area is reading
half the area.** The module carries the producer's narrower endpoint.

### Algorithm

- **Transform.** **The laminar block, and the binding operation is absent — and it cannot even be
  stated as a gap in the ordinary way.** The Function claims binding across modalities and over time.
  The attentional and mnemonic streams **arrive on different divisions** by the gradient account, so
  **the binding, if it happens here, happens on an edge between the two divisions, and that edge is
  not written.** **(Claude's reading.)** At the grasp entry the missing transform has a known
  signature; at the supramarginal gyrus it has none; **here the substrate the transform would run on
  is a division that is not known to exist.** The module cannot write the operation, cannot state its
  signature, and cannot allocate the place it would run. Source rung, against the literature.
- **Arrays.**
  - `active` — shape **(division = refused, lamina = 8, position = to derive)**, dtype **bool**,
    range **{0, 1}**, unitless. **Size cannot be computed: the neuron count is unknown.**
  - `threshold` — shape as `active`, dtype **uint16**, unit input count, range **to derive**.
    **Size cannot be computed.**
  - `count` — shape as `active`, dtype **uint16**, intermediate.
  - **The division axis is refused for a reason no measurement would remove.** PGa rostral and PGp
    caudal sit on a stated rostro-caudal gradient, and **a gradient is not a border**: whether they
    are compartments an edge can terminate on, or two ends of a continuum with no boundary, **is not
    established.** `allocate()` refuses with **gradient, not partition** as its stated reason —
    **distinct from *unsized* and distinct from *contested scheme***, and the module keeps the three
    reasons separate because they call for three different repairs.
  - **The refusal is not cheap.** If the gradient is a partition it **sorts six of this entry's input
    edges** — prefrontal and priority-map to PGa, hippocampal and default-mode to PGp — so resolving
    it **would change the arity of six edges at once.** The module records the six as arity-pending
    rather than assigning them.
  - **The left / right asymmetry is not a sub-element** and is covered by the per-hemisphere
    convention. **Whether the gradient is the same on both sides is unknown**, so the per-hemisphere
    convention is carrying an assumption it has not been checked against.
- **Parameters.** `threshold[j]`, `fan_in(j)` and `sign(i, j)` unset as elsewhere.
- **Update equation.** As the other entries, over the same internal block. **No PGa ↔ PGp edge is
  recorded in either direction**, and it is **the load-bearing internal edge** — the one the Function
  needs. Its absence is recorded and not repaired here.
- **State carried between updates.** `active`, all zero at start, written at the end of the update.
  **Shape unknown, so the state figure is unknown.**
- **Edge storage.** Four terms, none available on any line.
- **Adaptation.** No parameter changes; no rule is set; the rule is Micky's.
- **Open.**
  1. **Whether PGa / PGp is a partition at all.** **Not a size question**, and no count would answer
     it. Source rung. **Six edges' arity waits on it.**
  2. **The neuron count is unknown and this section's own pricing method is closed here.** The macaque
     has no angular gyrus in the strict sense, **so even a homology-based estimate is loose** — the
     analogy that priced the two intraparietal areas is unavailable **precisely where the payload is
     least writable.** Those are independent facts landing on one entry, and the module does not treat
     one as explaining the other. Source rung.
  3. **The output payload, on every one of the five output lines.** Source rung.
  4. **Splitting the four-target line is owed**, and **a fifth consumer declares the edge from the far
     side.** Architecture rung.
  5. **The occipitotemporal input is open at both ends** — the producer declares nothing and nothing
     searched established the edge.
  6. **The binding edge cannot be recorded as a dangling requirement in the same way as the other
     four**, because the divisions it would run between are not known to be divisions.

---

## Precuneus
### Contract — copied from the architecture, character for character

*All eight fields of the architecture entry, in the order the architecture writes them. Nothing
below this heading is this file's writing.*

- **Function → structure.** A medial-wall association hub and **default-mode network core**, with
  the posterior cingulate and medial prefrontal cortex — self-referential processing, first-person
  perspective and sense of agency, episodic-memory retrieval, and **visuospatial mental imagery and
  scene construction.** **Functionally graded into three sectors:** an **anterior sensorimotor**
  sector (reach, area-5 coupled), a **central cognitive / default-mode** sector, and a **posterior
  visual** sector (occipital-coupled). One of the most metabolically active cortical regions at rest
  and a highly connected hub.

- **Inputs.** **← superior parietal area 5** (`05_sensorimotor_loop`) — body configuration and
spatial layout, **body-centred
  here and contested at the producer**, which holds the frame unsettled across body-, shoulder- and
  hand-centred readings; **so the two ends disagree about the payload, not about wording.**
  **← dorsal-stream visual areas** — spatial layout, **a class that does not resolve**, and none of
  the four dorsal-stream entries declares an output here. **← the posterior cingulate cortex**
  (`17_insula_claustrum_habenula`) — owed, declared and untyped at the producer. **Two-ended and
  confirmed; payload owed at both ends**, the producer marking it *two-ended by name* in the
  same terms. **← the retrosplenial cortex** (`17_insula_claustrum_habenula`) — **the return
  arm of the spatial-memory loop: egocentric-to-allocentric translated heading and landmark
  information**; payload otherwise owed.
  **This edge matters more than an added line usually does** — the entry's headline function is scene
  construction, and the retrosplenial entry is **where the frame translation those depend on lives.**
  **Two-ended and confirmed, and it is not untyped at both ends.** **Both ends carry the same
  partial type** — the return arm, with
  heading and landmark information after the egocentric-to-allocentric translation — and each marks
  the remainder owed. **What is owed is the rest of the payload, not the whole of it.** The producer
  independently records this entry as the one consumer whose headline function the edge could supply,
  **which is this line's own claim arriving from the other side.** **← the angular gyrus** — owed,
  **and the producer marks its output payload the
  loudest owed in the file.** **← medial prefrontal cortex** (`11_frontal_lobe`) and **← the medial
  temporal lobe** —
  owed; one producer declares nothing, the other declares a class. **For the prefrontal half
  *declares nothing* is exact**: that file's orbitofrontal / ventromedial entry carries
  no output to this structure under any name, while declaring an input from it. **The reciprocal pair
  is open in one direction and the open direction is the return one.**

- **Outputs.** **→ the posterior cingulate cortex** (`17_insula_claustrum_habenula`) — **payload
  unknown — owed**. **Two-ended and confirmed, and this is the return limb** the consumer's own
  entry names. **The reciprocal pair is closed and both limbs are
  untyped**, which is a different state from the pair being open. *Self-referential
  processing*, *first-person perspective* and *scene construction* **are functions, not payloads.**
  **→ the angular gyrus** — unknown, owed, consumer in this section. **→ the medial intraparietal
  area** — owed, asserted at the consumer's end with a primary source there. **→ medial prefrontal
  cortex** (`11_frontal_lobe`) **and the medial temporal lobe** — unknown, owed, splitting owed.
  **The prefrontal half is declared at its far end.** That file's orbitofrontal / ventromedial entry
  declares `← the precuneus`, marked **Medial** — the ventromedial half of a structure whose two
  halves that file treats separately. **The medial temporal half is untested**, its far end
  unchecked. **So the splitting this line owes is forced**: one target declares the
  edge and the other is unchecked, and no single judgement describes both. **→ superior parietal
  area 5** (`05_sensorimotor_loop`) **and premotor cortex**
  (`11_frontal_lobe`), from the anterior sensorimotor sector —
  **reach and body-configuration signals, body-centred: the one edge out of this entry whose payload
  can be written**, and the one coupled to area 5 rather than to the default-mode network. **The
  area-5 end was transcribed from this one and certifies nothing.** **The premotor end does declare
  it.** That file's premotor entry declares
  `← the precuneus, from its anterior sensorimotor sector` — **naming the sector, in this line's own
  words.** **That end is untyped**, so what the far end supplies is the declaration and not the
  payload; this remains the only edge in the entry whose payload is written, and it is written here
  only. **Splitting this line is owed**: its two targets are in different files and in different
  states.

- **Sizing.** Basis: per hemisphere. **Neurons: soft / unknown** — no clean human per-area count, **a
  large medial-parietal association territory** and nothing more precise. **Structure total: to
  derive.**

- **Shape.** Rank 3: **(sector, lamina, position)** — three functional sectors against **an
  anterior / posterior architectonic pair, 7Am and 7Pm**, and **whether they are the same division
  under two names or a cross-cutting one is owed.** Tangential: **unknown.** **No per-sector count.**

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: **four of this entry's five outputs are untyped**, and
  the typed one is the sensorimotor limb. Per-edge latency: satisfied.

- **Justification (biological).** **The sectors sort this entry's edges, and that is what makes them
  load-bearing rather than descriptive.** The Outputs slot assigns one edge to a sector by name — the
  area-5 and premotor edge leaving from the anterior sensorimotor sector — **and it is the only edge
  in the entry whose payload can be written.** The description states the correlation plainly:
  **the one sector with a sensorimotor coupling is the one sector whose payload is typed, and the
  default-mode sectors account for every owed payload in the entry.** **Which sector each remaining
  edge reaches or leaves from is owed.** And **no edge between any two of the three sectors is
  recorded, in either direction** — while the Function claims scene construction and visuospatial
  imagery, **which would have to combine the posterior visual sector's content with the central
  sector's retrieved episodic content.** *(The sector-sorting reading is marked Class 2 in the
  description — its author's reading of the entry's own Function and Outputs, offered to be checked.)*

---

### Representation — declared here for the five lines this entry produces

| line | units | range and normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| → superior parietal area 5 (`05_sensorimotor_loop`) and premotor cortex (`11_frontal_lobe`), from the anterior sensorimotor sector | **reach and body-configuration signals**; units owed | owed | event-driven | **body-centred** |
| → the posterior cingulate cortex (`17_insula_claustrum_habenula`) | **unknown — owed** | owed | event-driven | none |
| → the angular gyrus | **unknown — owed** | owed | event-driven | none |
| → the medial intraparietal area | **owed** | owed | event-driven | none |
| → medial prefrontal cortex (`11_frontal_lobe`) and the medial temporal lobe | **unknown — owed** | owed | event-driven | none |

**One of five outputs is typed, and it is the one coupled to a sector rather than to the network.**
The architecture states the correlation directly: **the one sector with a sensorimotor coupling is the
one sector whose payload is typed, and the default-mode sectors account for every owed payload in the
entry.** The module records the sector on the line rather than as commentary, **because the sector is
what sorts the entry's edges** — that is what makes the three sectors load-bearing rather than
descriptive.

**And the typed line's payload is written at this end only.** The area-5 end **was transcribed from
this one and certifies nothing**; the premotor end **declares the edge, naming the anterior
sensorimotor sector in this line's own words, and carries no type.** So the far ends supply the
declaration and not the payload. **The module holds the payload as single-ended**, which is a
different state from two ends agreeing.

**Splitting is owed on two of the five lines**, and on both it is forced rather than tidiness: the
first line's two targets are **in different files and in different states**, and so are the last
line's — **one target declares the edge and the other is unchecked**, and no single judgement
describes both.

**Inherited representation on the input side, and two facts about it are unusual.** First, **one
input is partly typed at both ends**: the retrosplenial return arm carries **egocentric-to-allocentric
translated heading and landmark information**, and each end marks the remainder owed — **so what is
owed is the rest of the payload, not the whole of it.** That edge **matters more than an added line
usually does**, because this entry's headline function is scene construction and the retrosplenial
entry is where the frame translation it depends on lives. Second, **one input disagrees with its
producer about the payload rather than about wording**: superior parietal area 5's body configuration
is typed **body-centred here** while the producer holds the frame **contested** across body-,
shoulder- and hand-centred readings. **The module records the disagreement at the line and does not
resolve it in favour of this end.**

### Algorithm

- **Transform.** **The laminar block, and the inter-sector edge that scene construction requires is
  absent.** The Function claims **visuospatial mental imagery and scene construction**, which would
  have to combine **the posterior visual sector's content with the central sector's retrieved
  episodic content** — and **no edge between any two of the three sectors is recorded, in either
  direction.** No standard name is available for the combining operation and none is invented. Source
  rung, against the literature.
- **Arrays.**
  - `active` — shape **(sector = refused, lamina = 8, position = to derive)**, dtype **bool**, range
    **{0, 1}**, unitless. **Size cannot be computed: the neuron count is unknown.**
  - `threshold` — shape as `active`, dtype **uint16**, unit input count, range **to derive**.
    **Size cannot be computed.**
  - `count` — shape as `active`, dtype **uint16**, intermediate.
  - **The sector axis is refused for two reasons at once, and the module states both.** There is **no
    per-sector count**, and the three functional sectors stand against the architectonic pair **7Am /
    7Pm** with **alignment owed** — so the axis is **unsized** *and* **contested scheme**. This is the
    only entry in the section where the two refusals coincide, and reporting one would hide the other.
  - **The sectors are named and are the only divisional axis in this section that sorts an edge.**
    One output line is assigned to the anterior sensorimotor sector by name. **Which sector each
    remaining edge reaches or leaves from is owed**, so the module cannot place the other nine lines
    on the axis even in the scheme it has.
- **Parameters.** `threshold[j]`, `fan_in(j)` and `sign(i, j)` unset as elsewhere.
- **Update equation.** As the other entries, over the same internal block. **No inter-sector edge
  exists to write**, and writing one would invent the substrate of the entry's headline function.
- **State carried between updates.** `active`, all zero at start, written at the end of the update.
  **Shape unknown, so the state figure is unknown.**
- **Edge storage.** Four terms, none available. `bytes_per_value` is unavailable even on the one typed
  line, since its units are owed.
- **Adaptation.** No parameter changes; no rule is set; the rule is Micky's.
- **Open.**
  1. **The inter-sector edge**, demanded by the stated function and recorded nowhere. Source rung.
  2. **The neuron count is unknown and this entry has neither factor of one** — no density and no
     volume, only *a large medial-parietal association territory*. **The refusal here is the barest of
     the three unpriced entries**, and the module says so rather than refusing in the same words as
     the supramarginal gyrus, which is one measurement short. Source rung.
  3. **Whether the three sectors and 7Am / 7Pm are the same division under two names or a
     cross-cutting one.** Source rung.
  4. **Four of five outputs untyped**, and the typed one written at one end only.
  5. **The dorsal-stream visual input is a class that does not resolve**, and **none of the four
     dorsal-stream entries declares an output here.**
  6. **The medial prefrontal pair is open in the return direction**, and the open direction is the
     one this entry needs: that producer declares an input from this structure and no output to it
     under any name.
  7. **The sector-sorting reading is Class 2 in the architecture** — its author's reading of the
     entry's own Function and Outputs, offered to be checked. The module carries it as a reading and
     not as a fact.

---

## Section totals

| # | structure | basis | neurons | bits/neuron | parameter memory | activity bitmap |
|---|---|---|---|---|---|---|
| 1 | Anterior intraparietal area | per hemisphere | ~15M, soft, **analogy** | ≤ 16 | ≤ 30.00 MB | 1.875 MB |
| 2 | Medial intraparietal area | per hemisphere | ~15M, soft, **analogy** | ≤ 16 | ≤ 30.00 MB | 1.875 MB |
| 3 | Supramarginal gyrus | per hemisphere | **unknown** | ≤ 16 | **to derive** | **to derive** |
| 4 | Angular gyrus | per hemisphere | **unknown** | ≤ 16 | **to derive** | **to derive** |
| 5 | Precuneus | per hemisphere | **unknown** | ≤ 16 | **to derive** | **to derive** |
| | **stated total** | per hemisphere | **~30M** | | **60.00 MB**, three rows unpriced | 3.75 MB |

Recomputed with `python3`: **30M neurons, 60.00 MB parameter memory, 1.875 MB per priced activity
bitmap.** **Every fan-in in this section reads *to derive*, so every width sits at the 16-bit ceiling
and no width is derived here.** **State memory and edge storage are not in this total and are never
summed with it.**

**The 60.00 MB is a placeholder and the module carries it as one.** Both priced rows are analogies to
the lateral (~20M) and ventral (~12M) intraparietal areas, whose counts live in
`04_dorsal_visual_parietal_stream`. **The two structures the figure sizes are not the same size as
each other for any biological reason**, and the packing figure of order 20,000 neurons/mm³ at the
supramarginal gyrus **is not a count and may not be promoted into an array size here**, because the
volume it would need is unknown.

**Memory is a derived requirement and not a limit to design against.** Nothing in this section is
reduced, capped or simplified because a figure looks large; the figures above are findings.

## What blocks the implementation, specifically

| needed for | item | state | rung that repairs it |
|---|---|---|---|
| `fan_in(j)` | inter-structure connection topology | not set | this rung, Micky's — explicit agreement first |
| `sign(i, j)` | sign arithmetic, inhibitory against excitatory | not set anywhere | this rung, Micky's |
| the update order | the scheduling discipline | not set | this rung, Micky's |
| any threshold ever being written | the learning rule | not set | this rung, Micky's |
| whether `active` is dense or sparse | sparsity | not set | this rung, Micky's — explicit agreement first |
| every `register_buffer()` | buffer shapes | not set | this rung, Micky's — explicit agreement first |
| allocation for three of five structures | neuron counts | **not stated** | source rung, literature |
| trusting the two counts that exist | a measurement rather than an analogy | **both are analogies to counts measured in another file** | source rung, literature |
| allocating below the region level in the angular gyrus | whether PGa / PGp is a partition at all | **not a size question** | source rung, literature |
| resolving two edges' targets | what a network endpoint resolves to | **open and unanswered at the source** | source rung |
| placing an operation between two typed arrays | the coordinate-change transform | **absent in three adjacent entries at once** | source rung, literature |
| driving the reach channel at all | V6, both subdivisions of V6A, the caudal intraparietal area | **no entry anywhere** | source rung |
| **37 of 55 edges** | **a payload** | **unwritable, and the boundary has a location** | source rung, literature |

**The last row is the one that changes what this rung can promise.** Every blocked item above it is
something the module lacks. **That one is something the description lacks, on two thirds of its own
graph** — and it is not repaired at this rung. Patching it here would create an added edge, and an
added edge reads exactly like a derived one.

## Completion test

**A design entry is finished when the code can be written from it without making a single further
choice.** **No entry in this section is finished, and they fail differently:**

| entry | forward operation | payload | count | transform |
|---|---|---|---|---|
| Anterior intraparietal area | writable | **both ends typed** | analogy | **absent** |
| Medial intraparietal area | writable | one input contested, one producer missing | analogy | **absent** |
| Supramarginal gyrus | writable | **output untypable** | **unknown** | **absent** |
| Angular gyrus | writable | **no output typed at all** | **unknown, and the method is closed** | **absent** |
| Precuneus | writable | one output typed of five | **unknown** | **absent** |

**The forward operation is writable for every population in this section and the arrays would run
over signals the description cannot name.** That is this section's characteristic failure, and it is
not the same as any earlier one: the gates can be built, and on 37 of 55 edges there is nothing to
send along them.

**Five stated functions have no declared substrate**, and the module reports them as **one problem
plus two**, not as five: the anterior intraparietal transform, the medial intraparietal frame mixture
and the ventral intraparietal gain field in `04_dorsal_visual_parietal_stream` are **three
neighbouring entries whose stated function is a coordinate change, and none can say where the change
happens** — one problem in three places. The supramarginal somato-to-praxis conversion and the
precuneus inter-sector edge are the other two. **The angular gyrus's PGa ↔ PGp binding edge is a
sixth requirement that cannot even be stated as a gap**, because the division it would run between is
not known to be a division.

## What the module implements

Five structures with per-structure laminar sets, populations, shapes and edges as data; the
threshold-gate forward operation with `fan_in`, `sign` and `threshold` unset and visibly so;
allocation for the two priced structures **with the analogy flag returned together with the figure**,
and three distinct refusals for the three unpriced ones; a **payload report** splitting the 55 edges
into typed and untyped **by content class**; an **axis-status report** naming PGa / PGp as an axis
whose existence is unsettled and the three entries holding incompatible parcellations; a
**network-endpoint report** for the two edges whose target is not a node; a **single-ended-origin
report** naming the two edges written to satisfy the two-ended diff and the five payloads transcribed
from a far end; a **dangling-requirement report** for the five stated functions with no declared
substrate, **grouping the three that are one problem**; a **missing-producer report** for V6, the two
subdivisions of V6A and the caudal intraparietal area; and the two **measurement cautions** — the
packing figure is not a count, and the ~15M figures are analogies — **neither of which may be promoted
into a width or an array size here.**
