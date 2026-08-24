# Brain code design — 07 anterior temporal lobe

**Date:** 2026-08-22
**Derived from:** `Brain_architecture_07_anterior_temporal_lobe_2026_08_22.md`,
`Brain_code_design_spec`, and CLAUDE.md.
**No other content source.**
**Implements:** `Brain_07_anterior_temporal_lobe.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly," no commented-out prior version.

**How to read the entry.** It carries a **Contract** block, then **Representation**, then
**Algorithm**. The contract block is **copied from the architecture character for character** — read
off the architecture file mechanically and written out unchanged — so a diff of that block against the
architecture entry is a check on the copy, and a stem count is a check that no edge was dropped.
**Representation and Algorithm are this rung's own writing**, and that is where anything unfaithful
would live.

**The contract block is the whole architecture entry.** `Brain_code_design_spec` §3 names eight
fields — Function → structure, Inputs, Outputs, Sizing, Shape, Edge latency, Invariant conformance,
Justification (biological) — and **there is no field this rung re-derives rather than copies.** The
boundary between copy and writing falls at the block edge and nowhere inside it.

**Provenance.** The contract block is verbatim copy. Unmarked sentences in Representation and
Algorithm are derivation from the architecture entry above them. Readings placed on it are marked
**(Claude's reading)**. Every number was recomputed with `python3`.

**Standalone, not a companion.**

---

## Element class, and the shape of this section

**One structure, one element class, and none of the four exceptional classes appears.** Every neuron
in the temporal pole is a **threshold gate**. There is no transmission-only structure here, no
transducer, no graded non-spiking element, and no sign-inverting stage. **That is a positive statement
about the section and not an absence of information**, and it is why the ordinary entry shape fits.

**Every edge in this section leaves it.** Twelve edges, and not one is internal to the file — so this
rung has no intra-file wiring to write and no intra-file payload to reconcile. What it has instead is
twelve far ends, **ten of which sit in files the architecture checks against itself**
(`01_visual_pathway`, `02_auditory_pathway`, `06_posterior_parietal`, `08_medial_temporal_lobe`,
`11_frontal_lobe`, `17_insula_claustrum_habenula`), and two in regions with no entry in any file at
all.

## The forward operation, and the four things it cannot be run with

The specified part of the computation is writable for every neuron in this section:

```
count[j]  = Σ_{i ∈ fan_in(j)} sign(i, j) · active_source[i]
active[j] = count[j] ≥ threshold[j]
```

Integer-only, no multiply, no gradient, and — unlike sections carrying transducers or graded elements
— **it covers every neuron here without exception.** Four of its terms are unset:

- **`fan_in(j)` — inter-structure connection topology is not set at any rung**, and this section is in
  a worse state than one where a topography is described in prose and merely needs turning into a
  function. **No topography of any kind is recorded for this structure** — no map, no gradient of
  convergence, no ordering principle on any axis, and fan-in reads *to derive* on all twelve edges.
  **The distinction matters because the two states call for different work**: a stated pattern needs
  transcribing, an unstated one needs measuring. **(Claude's reading.)**
- **`sign(i, j)` — sign arithmetic is not set anywhere.** The expression carries the term rather than
  writing a bare sum, because a bare sum silently asserts that every input is excitatory. Here the
  term is doubly open: the standard laminar block that would have supplied at least one sign
  relationship **is not available in this section at all** (below), so there is not even an internal
  edge whose sign could be named.
- **`threshold[j]` — no rule writes it.** Adaptation is Micky's and is not set.
- **the update order — the scheduling discipline is not set**, and two closed loops run through this
  structure.

**What is not unset is the operation itself.** Every neuron is a threshold gate and none is described
as doing anything else, so the arithmetic needs no decision once those terms arrive.

## The laminar block is unavailable here, and that is a claim rather than a gap

Sections built on granular isocortex inherit a standard eight-sub-element block — 1, 2, 3, 4, 5a, 5b,
6a, 6b, with **4 → 2/3**, **2/3 → 5a** and **5b**, **6a → 4** and **6a → 5a** at opposite signs,
**6b → 6a** arousal-gated. **This structure cannot take it**, and the module must not transcribe it
from a neighbouring section. The region is **agranular medially and dysgranular dorsolaterally, on a
gradient**, so layer 4 is absent at one end and thin at the other — and **three of the block's edges
route through layer 4.** Transcribing the block would assert a circuit the description denies over
part of the region.

**So the module carries no laminar edge set at all**, and the laminar axis reads **owed, per
subdivision** — which is downstream of a subdivision count that is itself contested, making the axis
**doubly blocked**. What *is* recorded is a partial pattern for the temporopolar cortex proper only —
thin layer II, a size gradient of pyramids through layer III, a thin layer IV, large dark pyramids in
layer V, layer VI spreading into the underlying white matter — **and a partial pattern for part of the
entry is not a laminar set for the entry.** The module holds it as description and allocates nothing
from it.

## Two closed loops, and a register would break both

**The temporal pole ↔ insular cortex and temporal pole ↔ amygdala loops both run in and out of this
structure**, on four limbs, with real, different and unmeasured delays. A loop with heterogeneous real
delays settles by its own dynamics; the same loop broken by registers becomes an iterated map whose
trajectory depends on the update rate. **Those are two different systems computing two different
things.**

A uniform one-step delay is a legitimate thing this rung may decide to adopt — set every latency equal
and choose a step short enough to carry the finest. **The finest is not known here**, and this section
has nothing at all to go on: **not one timing statement of any kind, qualitative or quantitative,
appears anywhere in it.** What it has instead is the substrate — four named association tracts, no
lengths, no diameters, no g-ratios, and a tract-to-edge assignment for one of them.

**The module therefore contains no loop, no step counter and no `for t in range(...)`.** Where the
scheduler would go, it raises. Writing an iteration would invent a clock the system does not have.

## Four axes, open in four different states

**"To derive" is an honest answer only for a quantity the source has not supplied**, and writing it
over any of the states below would make a claim the architecture did not make. The shape is
**(lamina, subdivision, H, W)** and **none of the four axes has an extent**:

| axis | state | why it is not plain *to derive* |
|---|---|---|
| lamina | **owed, per subdivision** | the eight-layer block is **positively wrong** over part of the region, a partial pattern is recorded for part of the entry, and it is known what research would close it |
| subdivision | **contested — extent 2, 3, 3 or 4** | four schemes, not reducible to one another; **four groups have looked and disagree**, so this needs adjudication and not a measurement |
| H | **to derive** | tangential sub-elements unknown, no pitch measured |
| W | **to derive** | as H |

**A single *to derive* across all four would have hidden that**, and the four states call for four
different kinds of work.

**The contested axis is not blocked in the way the other unset items are.** Everything else this rung
waits on — topology, sparsity, buffer shapes, the scheduling discipline, the learning rule — waits on
**a decision, and Micky is the decision-maker**. The subdivision extent waits on **an adjudication
between published results**, and no decision-maker on this project can supply one. **Writing
`n_divisions = 3` would take a side in a literature dispute and then propagate into every buffer shape
downstream.** The module declares the four schemes as data and raises where an extent is required.
**(Claude's reading, that a decision and an adjudication are different states needing different work.)**

## The payload boundary, and where it sits in this section

**Not one of the twelve payloads has units, a range or a coordinate frame.** Sorting them by how far
the description gets:

| payload state | edges |
|---|---|
| named, not typed | 3 |
| one component named, the rest owed | 2 |
| wholly owed | 7 |
| **typed** | **0** |

**Zero of twelve, and the zero is a finding rather than a coverage gap.** The architecture's own
justification says why: this is where the payload stops being modal. Every stage below this one on the
ventral line carries something with a frame — retinotopic position, orientation, disparity, hue, a
talker-invariant word — and **what leaves here is defined by what it has lost.** The one checkable
property in hand on the six outputs is a negative: **the concept has lost its modality.**

**A consequence for this rung specifically.** Representation exists to catch the failure where two
structures each read a shared line correctly and disagree about what its numbers mean. **On twelve of
twelve lines there are no numbers to disagree about**, so the guard has nothing to hold and the check
it would provide is unavailable anywhere in this section.

---

## Temporal pole
### Contract — copied from the architecture, character for character

*All eight fields of the architecture entry, in the order the architecture writes them. Nothing
below this heading is this file's writing.*

- **Function → structure.** The convergence apex of the ventral "what" streams and a semantic hub:
  highly processed visual object and face identity from the inferotemporal cortex and highly
  processed auditory word and sound-object identity from the rostral superior temporal gyrus are
  bound into **amodal concepts** — the anterior-temporal hub of the hub-and-spoke semantic model.
  Also social and emotional evaluation, and naming.
  Structurally it is **paralimbic and graded, not a field.** Its architecture changes progressively
  from **medial agranular limbic cortex** toward **more dorsolateral dysgranular paralimbic cortex**,
  so layer 4 is absent at one end of the region and thin at the other and **there is no single
  laminar set true of the whole entry**. The standard eight-layer cortical block — 1, 2, 3, 4, 5a,
  5b, 6a, 6b, with three of its edges routed through layer 4 — **is a claim about granular isocortex
  and this structure cannot take it.** Laminar sub-elements are **owed, per subdivision.**
  What is recorded of the laminar pattern, for the temporopolar cortex proper: **thin layer II**, a
  **size gradient of pyramids through layer III**, a **thin layer IV**, and **large dark pyramids in
  layer V** fusing with a **layer VI that spreads out into the underlying white matter**.
  **Divisional sub-elements are contested and the contest is between four incompatible schemes** —
  two fields (a lateral temporopolar and a medial-and-ventral one); three by cytoarchitecture
  (dorsal, ventrolateral, ventromedial); three by anatomical connectivity (dorsal, lateral, medial);
  and four by functional and anatomical network (dorsal, ventromedial, medial, anterolateral, whose
  authors explicitly declined to draw a hard parcellation). **The gradient is not in dispute; the
  number of cuts through it is.**
  **The subdivisions sort this entry's edges, which is what makes them load-bearing rather than
  descriptive.** Across the schemes the connectional assignments agree even where the boundaries do
  not: the **dorsal / dorsolateral** subdivision takes the auditory input and emits to the entorhinal,
  rostral perirhinal and posterior parahippocampal cortices, and is the subdivision reported strongly
  connected with parietal cortex; the **ventrolateral / anterolateral** subdivision is the
  default-semantic network node; the **ventromedial / medial** subdivision carries the limbic and
  paralimbic connections — amygdala, hippocampus, entorhinal and parahippocampal cortex,
  orbitofrontal cortex — largely via the uncinate fasciculus. **Every edge below belongs to a
  subdivision and none of them says which: the assignment is owed at the source.**
  **Tangential sub-elements: unknown.** No columnar, stripe or patch organisation is recorded, and no
  tangential pitch is measured.
  **Internal edges: owed, all of them.** No edge between any two subdivisions is recorded in either
  direction under any scheme.

- **Inputs.**
  - **← rostral superior temporal gyrus** — talker-invariant word and sound-object identity, the
    auditory "what" endpoint. **This is the principal input to the dorsolateral subdivision.**
    Fan-in: to derive. **Two-ended** (`02_auditory_pathway`): that file's anterior
    superior temporal gyrus entry declares `→ temporal pole and middle temporal gyrus → ventrolateral
    prefrontal cortex — the same identity code, toward amodal concept and controlled retrieval`. **So
    the edge is two-ended and the producer already names where this region sends it next**, which
    matches this entry's own ventrolateral prefrontal output. **The producer writes it as a chained
    compound** — two targets and an onward hop on one line — so the arity is owed there.
  - **← anterior inferotemporal cortex / ventral temporal** — view-invariant object and face
    identity. Fan-in: to derive. **Two-ended, and both endpoints are structures**
    (`01_visual_pathway`): that entry writes this region as the named consumer and the distributed
    conceptual / semantic system as what lies beyond it, rather than carrying this region as a
    waypoint inside a class endpoint. **The payloads agree** — that end carries identity, this end
    receives view-invariant object and face identity.
  - **← orbitofrontal cortex** (`11_frontal_lobe`) — **value**, and nothing else typed: the rest of the
    payload is owed. Fan-in: to derive.
    That file's orbitofrontal / ventromedial prefrontal entry declares `→ the temporal pole` by
    name, so **the edge is two-ended**. **Neither end types the payload beyond *value*, so the payload
    is owed at both.**
  - **← insular cortex** — **interoceptive context**, and the rest of the payload owed. Fan-in: to
    derive. **Two-ended** (`17_insula_claustrum_habenula`): that
    file's insula entry declares `→ the temporal pole`, typed **interoceptive context** with the rest
    owed, and names this region among its own inputs on a line marked reciprocal. **Both limbs of the
    reciprocity it asserts are written at that end.**
  - **← angular gyrus** (`06_posterior_parietal`) — payload **owed at both ends**. Fan-in: to derive.
    **Two-ended, and written from the producer's side**: that file's angular gyrus entry declares an
    output to "the distributed conceptual / semantic system via the temporal pole, the hippocampal
    formation, ventrolateral prefrontal cortex and the default-mode partners," names this structure
    explicitly among the four targets, and records the edge as owed as a cross-file edit at this
    section's source. **The producer's line is a compound of four targets and one network endpoint
    and is owed a split there**, so the arity at that end may change; the limb naming this structure
    will not.
  - **← amygdala** (`08_medial_temporal_lobe`) — the **valence tag**: a gain on perception, attention
    and memory encoding, **carrying no identity information of its own**. Fan-in: to derive.
    That entry declares `→ temporal pole` **on its own line, attributed to the basal / accessory
    basal nuclei and typed the valence tag** — this region is the named consumer, not a member of a
    "widespread cortex" class. **The edge is two-ended and the payloads agree in the same words.**
    Fan-out is to derive at that end as fan-in is here, so **the edge is typed at both ends and
    quantified at neither.**

- **Outputs.** All six carry the **amodal concept**, and that is a phrase rather than a type. It has
  **no units, no range, no coordinate frame and no declared channel structure**, and the one thing
  known about it is a negative: **it has lost its modality.** Every payload below is therefore
  **owed**, and the modality-loss is the only checkable property currently in hand.
  - **→ entorhinal cortex** (toward the hippocampal formation) (`08_medial_temporal_lobe`) — the
    amodal concept. Fan-out: to derive. The hippocampal formation entry declares
    `← temporal pole, onto entorhinal cortex` **on its own line, naming the sub-element this line
    names**, typed an amodal concept and marked *payload owed at the producer, where modality-loss is
    the only checkable property in hand* — **which is this file's own sentence about its own payload,
    arriving from the other side.** **The edge is two-ended and the sub-element agrees.** That entry's
    inferotemporal edge is a separate edge and is not this one.
  - **→ rostral perirhinal cortex** — the same amodal concept. Fan-out: to derive. **No entry in any
    file checked against this one**, and the inferotemporal entry in `01_visual_pathway` points at the
    same region,
    naming perirhinal cortex explicitly as the step by which the ventral stream reaches the
    hippocampal formation. **So two files' edges dangle on it. Inherited gap; not patched here.**
  - **→ posterior parahippocampal cortex** — the same amodal concept. Fan-out: to derive. **No entry
    in any file checked against this one. Inherited gap; not patched here.** *(These two were one
    compound source line naming two structures. Split here because an edge names its target
    structure; the arity is the source's and is not invented.)*
  - **→ ventrolateral prefrontal cortex** (`11_frontal_lobe`) — the amodal concept, for controlled
    retrieval and selection. Fan-out: to derive. **Two-ended and typed at both:** that far end declares
    `← the temporal pole` on its own line, typed **an amodal concept**, with the payload owed there
    as here. Fan-in is to derive at that end as fan-out is here, so **the edge is typed at both ends
    and quantified at neither.**
    **A separate claim in that file about this entry holds.** Its frontopolar
    cortex entry records that it takes auditory and temporal input including the temporal pole, and
    that **the temporal-pole limb was checked and this producer does not declare it.** **It does not:
    the six outputs above contain no frontopolar target.** So that edge is declared at the consumer
    and at no producer, and the repair is owed at this section's source — **either declare it here or
    it is withdrawn there.**
  - **→ amygdala** (`08_medial_temporal_lobe`) — the amodal concept, for affective evaluation.
    Fan-out: to derive. That entry declares `← temporal pole` **on its own line, typed an amodal
    concept, for affective evaluation** — this end's payload, in this end's words, and it marks the
    payload owed for the same reason this file does. **The edge is two-ended.** **This is the return
    limb of the loop above**, and the loop closes at both ends.
  - **→ insular cortex** (`17_insula_claustrum_habenula`) — payload owed at both ends. Fan-out: to
    derive. **Two-ended:** that file's insula entry declares `← the temporal pole`, carrying
    "emotional, evaluative and social context," and marks that its own largest gap — context being a
    function word rather than a type with a range and a frame. **The two ends agree that the payload
    is not writable, in the same terms.**
  

- **Sizing.** Basis: **per hemisphere.**
  - **~103M neurons.** Fan-in: unknown — synapses are unrecorded for this structure — so bounded at
    the log₂ ceiling, **≤ 16 bits → ≤ 206 MB.**
  - **The count is the sensitive term and there is no fan-in dispute to absorb here at all.** The
    fan-in is not disputed across a range as V1's is; it is simply absent, so the 16-bit ceiling is
    doing all the work and the figure is a bound rather than an estimate.
  - **Density cross-check, recomputed rather than carried.** Grey-matter volume is ~5.04 ± 0.96 cm³
    per hemisphere. 103M neurons over that range is **17,167 to 25,245 neurons/mm³**, centre
    **~20,437**, which closes against the source's ~20,000 figure and places this structure at
    ordinary association-cortex packing — **about a third of V1's ~60,000/mm³.** The count is the
    same order as the ~145M of Brodmann area 22 / area TA, the neighbouring superior temporal gyrus
    association cortex, at a ratio of 1.41.
  - **No per-subdivision partition exists, and one cannot be constructed.** The source records no
    per-subdivision count, and **the number of subdivisions is itself contested**, so there is no
    denominator to divide 103M by. An even split is not offered: it would invent both the arity and
    the uniformity.

- **Shape.** **Sheet**, rank 4: **(lamina, subdivision, H, W)** — and **three of the four axes are
  open in three different states, none of which is plain *to derive*.**
  - **lamina — owed, per subdivision.** Not unknown and not to-derive: the eight-layer block is
    positively wrong here over part of the region, the partial pattern that is recorded (thin II,
    graded III, thin IV, large V, VI spreading into white matter) is for the temporopolar cortex
    proper rather than for the whole entry, and it is known what research would close it.
  - **subdivision — contested, extent 2, 3, 3 or 4.** Four schemes, not reducible to one another,
    with the connectional assignments agreeing where the boundaries do not. **Writing *to derive*
    here would assert that nobody has looked, when the problem is that four groups have looked and
    disagree** — and the two states call for different work: one needs a measurement, this needs
    adjudication. *(That a contested extent is written as contested rather than as to-derive is
    Claude's reading; the design file forbids the substitution and does not say what to write
    instead.)*
  - **H, W — to derive.** Tangential sub-elements are unknown and no tangential pitch is measured.
  - **The tile calculation cannot be started, and it is short two terms rather than one.** Surface
    density needs volumetric density × cortical thickness: **the density is in hand (~20,400/mm³) and
    the thickness is not recorded**, and the surface area is not recorded either.
    `01_visual_pathway`'s V1 carries
    both and closes 312M against its headline independently; here there is no second route to the
    count. **The 103M is single-sourced.**

- **Edge latency.** All twelve edges: **to derive.** No timing figure of any kind is recorded for
  this structure. The four named association tracts are the substrate a derivation would start from,
  and only the uncinate fasciculus is assigned to particular edges.

- **Invariant conformance.** **Co-instantiation: satisfied at the region level and unstatable at the
  sub-element level.** The two reciprocal loops — with the insular cortex and with the amygdala —
  are both written here and neither can be staged. Below that level the invariant cannot be checked
  at all, because the sub-elements the edges attach to have **no edges between them**, and the
  binding the function claims is exactly such an edge. **Per-edge latency: satisfied in form, all
  twelve to derive**; no edge is zero, none is uniform with another, and none has a number.

- **Justification (biological).** This is where the payload stops being modal. Every stage below it
  on the ventral line carries something with a frame — retinotopic position, orientation, disparity,
  hue, a talker-invariant word — and what leaves here is defined by what it has lost. **The lesion
  evidence is what makes that a structural claim rather than a description**: degeneration of this
  region is the lesion of semantic dementia, a progressive loss of word *and* object meaning with
  anterior-temporal atrophy — one lesion taking out two modalities' meaning together, which is the
  behavioural signature of a shared amodal representation rather than of two modal ones side by side.
  The structural consequence is that **no units can be stated on any output edge above**, and that is
  a finding about the region rather than a gap in the record.
  The second justification is architectural and is the reason the contested subdivision count
  matters: **the region's own architecture is a gradient.** Agranular medially, dysgranular
  dorsolaterally, changing progressively. A gradient is what different instruments cut differently,
  which is why four parcellation schemes coexist without any of them being wrong — the same object
  the source records at the insula. **A structure whose sub-element count depends on the instrument
  is a structure whose array rank is not settled by measurement alone.**

---

### Representation — declared here for the six lines this entry produces

| line | units | range and normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| → entorhinal cortex (`08_medial_temporal_lobe`) | **none — the amodal concept has no units** | none | event-driven | **none, and the absence is the content** |
| → rostral perirhinal cortex | **none** | none | event-driven | none |
| → posterior parahippocampal cortex | **none** | none | event-driven | none |
| → ventrolateral prefrontal cortex (`11_frontal_lobe`) | **none** | none | event-driven | none |
| → amygdala (`08_medial_temporal_lobe`) | **none** | none | event-driven | none |
| → insular cortex | **none** | none | event-driven | none |

**All six carry the amodal concept, and that is a phrase rather than a type.** It has no units, no
range, no coordinate frame and no declared channel structure. **The module records the six as carrying
a named-but-untyped value** rather than as typed, and does not treat the shared name as evidence that
the six lines carry the same thing.

**The one checkable property is a negative, and it is a finding rather than a hole.** What is known
about the payload is that **it has lost its modality** — and the architecture's justification makes
that structural rather than descriptive: degeneration of this region is the lesion of semantic
dementia, a progressive loss of word *and* object meaning together. **One lesion taking out two
modalities' meaning at once is the behavioural signature of a shared amodal representation** rather
than of two modal ones side by side. So *no units can be stated on any output line above* is a
statement about the region, not a gap in the record, and **this rung must not repair it by inventing
an encoding.**

**Update timing is event-driven on all twelve lines, and that is a statement rather than a
placeholder.** This structure is not a sensor and has no rate of its own; it is driven by its inputs
and emits when they change. There is no system clock to borrow a rate from, and borrowing one would
invent what the per-edge-latency invariant forbids.

**Inherited representation on the input side, and none of the six is typed either.** The auditory
identity from the rostral superior temporal gyrus and the visual identity from the anterior
inferotemporal cortex are **named without units**; the orbitofrontal input names **value** and owes the
rest; the insular input names **interoceptive context** and owes the rest; the amygdala input names the
**valence tag** and adds one checkable property — **it carries no identity information of its own**,
which is a constraint on what the gate may do with it rather than a type; the angular gyrus input is
**wholly owed at both ends**.

**Two of the six output lines have no far end to inherit from or agree with.** Rostral perirhinal and
posterior parahippocampal cortex **have no entry in any file at all**, so their payloads
have nobody to be diffed against. The module records that as a distinct state from *owed at both ends*:
**a payload owed at two ends can be closed by research at either; a payload with one end missing cannot
be checked at all.**

### Algorithm

- **Transform.** **The threshold gate, and nothing else — and the entry's declared operation has no
  substrate.** The writable operation is the gate over every neuron in the structure. **The transform
  the entry exists for is binding across modalities**, and under §5 the absence of a standard name is
  recorded as a finding rather than filled in: visual identity arrives, auditory identity arrives, an
  amodal concept leaves, **and the edge on which the combination would happen is not declared in either
  direction under any of the four subdivision schemes.** The connectional assignment puts the auditory
  input on the **dorsal** subdivision and the semantic output on the **ventrolateral** one, so the step
  is not merely unnamed — **its two ends are known to sit on different subdivisions with nothing
  written between them.** **Repaired at the source rung, against the literature. It may not be filled
  here**: a supplied inter-subdivision edge would read exactly like a derived one and would supply the
  region's headline function out of nothing.
- **Arrays.**
  - `active` — shape **(lamina = owed, subdivision = contested, H = to derive, W = to derive)**, dtype
    **bool** (1 bit per neuron), range **{0, 1}**, unitless. At the stated count: **12.875 MB.**
  - `threshold` — shape as `active`, dtype **uint16**, range **to derive**, unit **input count**. **16
    bits is a ceiling, not a derived width**: the width a threshold needs is set by the fan-in it
    counts against, and **fan-in is absent rather than ranged** for this structure. At the ceiling:
    **206.0 MB.**
  - `count` — shape as `active`, dtype **uint16**, range **0 … fan_in**, unit **input count**.
    Intermediate, not state.
  - **A note on the realisation gap, which is zero here and must not be read as a good fit.** The
    derived width **is** 16 bits, so `uint16` is exact and no bits are wasted at the container. **That
    is the signature of an absent measurement, not of a well-fitted one** — the moment a synapse count
    arrives the gap opens, and at a fan-in of 4,000 the derived width is 12 bits against a realised 16,
    a **33%** gap. **(Claude's reading.)**
  - **A consequence worth stating positively.** Because 16 bits is a ceiling rather than a measurement,
    **the allocated array is correct at every fan-in the biology could turn out to have**, and
    oversized at all but the largest. Allocating to the ceiling is the only choice available and **it
    cannot be wrong; it can only be wasteful**, and by how much is unknown until a synapse count
    exists. That is a compute-versus-memory trade at the container, not an architectural one.
  - **Input arrays: six lines.** **Output arrays: six lines.** **No array may be allocated on any
    sub-element axis**, and the three refusals are for three different reasons — see **Open**.
- **Parameters.** `threshold[j]` — unit input count, value **not set**, origin **chosen by no one
  yet**: no rule at any rung writes an initial threshold and the learning rule is Micky's. `fan_in(j)`
  — **not set**, origin connection topology, which requires explicit agreement before it is touched,
  **and which has no recorded topography to be derived from here.** `sign(i, j)` — **not set
  anywhere.** **No lamina set is a parameter of this entry**, and that is the difference from every
  granular section: there is no eight-member tuple to hold.
- **Update equation.** `count[j] = Σ_{i ∈ fan_in(j)} sign(i, j) · active_source[i]`, then
  `active[j] = count[j] ≥ threshold[j]`, over every neuron in the structure without exception. **The
  equation is complete in form and unrunnable in fact**, on the terms named in the preamble. **No
  internal edge set is written**, because none is recorded: no laminar block is available here and no
  inter-subdivision edge exists in any scheme. **No update order is written**, because two loops close
  through this structure and ordering them would choose the scheduling discipline.
- **State carried between updates.** `active` — shape and dtype as above, initial value **all zero**,
  written at the end of the update. **State memory is not parameter memory and the two are never
  summed.** `threshold` is a parameter and is not state. **Note that `active` is state here for a
  different reason than in a section with laminar recurrence**: there are no internal edges reading it
  at all, so it is state only because the two external loops return through this structure.
- **Edge storage.** `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`.
  **Every term is unavailable on every edge of this entry.** `line_count` — fan-in and fan-out both
  read *to derive* and no axon count is stated for any of the four named tracts. `latency` — *to
  derive*, on all twelve. `update_interval` — unset, and Micky's. `bytes_per_value` — **unavailable on
  all twelve, since no payload in the section is typed.** **The specification anticipates one unset
  term and this entry has four**, which is recorded rather than estimated: a figure computed from
  assumed terms would enter the file looking exactly like a derived one.
- **Adaptation.** **No parameter in this entry changes, because no rule says one does.** The learning
  rules are Micky's and are not set. **The entry records that the rule is not set; it does not assume
  one.** `threshold` is therefore a read-only buffer and its cost is a construction cost.
- **Open.**
  1. **The inter-subdivision edge**, in both directions, under all four schemes — **the substrate of
     the region's declared function.** Source rung, against the literature. **This is the entry's
     headline gap and the module cannot state its signature**, because neither the payload leaving nor
     the payload arriving is typed.
  2. **How many subdivisions there are: 2, 3, 3 or 4.** **Not a measurement question — an adjudication
     between four published schemes that do not reduce to one another.** `allocate()` refuses a
     sub-element request on this axis with **contested** as its stated reason, distinct from *unsized*.
  3. **A laminar set true of the whole entry.** **Owed, per subdivision**, and therefore downstream of
     item 2 — **doubly blocked.** The standard eight-layer block is **positively wrong** over part of
     the region and may not be transcribed from a granular section. Source rung.
  4. **Tangential organisation: unknown**, no columnar, stripe or patch structure recorded and no pitch
     measured. Source rung.
  5. **Which subdivision each edge attaches to.** The connectional assignment agrees across the schemes
     even where the boundaries do not — dorsal takes the auditory input and emits to the entorhinal,
     rostral perirhinal and posterior parahippocampal cortices; ventrolateral is the default-semantic
     node; ventromedial carries the limbic traffic via the uncinate fasciculus — **but every edge
     belongs to a subdivision and no edge declares which.** Source rung.
    6. **Rostral perirhinal and posterior parahippocampal cortex have no entry in any file at all**, and
     **three files' edges point at the first of them.** Source rung. **A stub would
     supply the consumer and destroy the payload check**, which is the only thing making the edge
     verifiable.
    7. **Both insular edges are two-ended.** That file declares the input limb on a line marked
     reciprocal and the output limb by name, typed *interoceptive context* with the rest owed — so the
     reciprocity it asserts is written at both ends, and the payloads are owed on both limbs at both
     ends.
    8. **The angular gyrus edge is written and its producer's line is owed a split.** That file's angular
     gyrus entry names this structure explicitly among four targets of one compound output line, one of
     which is a network endpoint. **The limb naming this structure will survive the split; the arity at
     that end will not.** Source rung, at `06_posterior_parietal`.
  9. **A frontopolar edge is declared at its consumer and at no producer.** `11_frontal_lobe`'s
     frontopolar entry records taking temporal input including the temporal pole, and **the six outputs
     above contain no frontopolar target.** Owed at this section's source — **either declare it here or
     it is withdrawn there.**
  10. **No timing figure of any kind exists in this section**, qualitative or quantitative. The four
     named association tracts are the substrate a derivation would start from, and **only the uncinate
     fasciculus is assigned to particular edges**, with no length, diameter or g-ratio for any of the
     four. Source rung.

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory | activity bitmap |
|---|---|---|---|---|---|
| Temporal pole | per hemisphere | ~103M, **single-sourced** | ≤ 16 | ≤ **206.0 MB** | **12.875 MB** |
| **stated total** | per hemisphere | **~103M** | | **≤ 206.0 MB** | **12.875 MB** |

Recomputed with `python3`. **The total is a ceiling, not a floor**, and that inverts the usual
caveat: the fan-in is **absent rather than ranged**, so 16 bits is the log₂ cap doing all the work and
the true figure is at or below 206.0 MB. **What would move it is a synapse count** — at a fan-in of
4,000 the store is 12 bits and **154.5 MB**; at 256 it is 8 bits and **103.0 MB**.

**Density cross-check, recomputed across the full volume range rather than at its centre.**
Grey-matter volume ~5.04 ± 0.96 cm³ per hemisphere gives **4.08 to 6.00 cm³**, and 103M neurons over
that range is **17,167 to 25,245 neurons/mm³**, centre **~20,437** — ordinary association-cortex
packing, **0.34 of V1's ~60,000/mm³**, and the same order as the ~145M of the neighbouring superior
temporal gyrus association cortex at a ratio of **1.41**.

**The count has no second route.** Neither cortical thickness nor surface area is recorded, so the
surface-density calculation that would confirm a headline count independently **cannot be started, and
it is short two terms rather than one**: the volumetric density is the one term in hand and it needs
both of the others to be useful.

**State memory and edge storage are not in this total and are never summed with it.**

**Memory is a derived requirement and not a limit to design against.** Nothing here is reduced, capped
or simplified because a figure looks large.

## What blocks the implementation, specifically

| needed for | item | state | rung that repairs it |
|---|---|---|---|
| `fan_in(j)` | inter-structure connection topology | not set, **and no topography is recorded to derive one from** | this rung, Micky's — explicit agreement first |
| `sign(i, j)` | sign arithmetic | not set anywhere, **and no internal edge exists whose sign could be named** | this rung, Micky's |
| the update loop | the scheduling discipline | not set, **and two closed loops would be broken by a register** | this rung, Micky's |
| any threshold ever being written | the learning rule | not set | this rung, Micky's |
| whether `active` is dense or sparse | sparsity | not set | this rung, Micky's — explicit agreement first |
| every `register_buffer()` | buffer shapes | not set, **and blocked by a contested extent rather than a missing number** | **adjudication between published results** |
| any tangential partition | tile geometry | not set, **and no pitch is measured here to set it from** | source rung, literature |
| the subdivision axis | how many subdivisions there are | **contested: 2, 3, 3 or 4** | **adjudication, not measurement** |
| the laminar axis | a laminar set true of the whole entry | **owed, per subdivision — and the standard block is positively wrong here** | source rung, literature |
| **the region's declared function** | **an edge between any two subdivisions** | **owed, in both directions, under all four schemes** | source rung, literature |

**The learning rule's absence is the least blocking of these.** A threshold that is never written is a
**construction cost, not a memory**: `threshold` is a read-only buffer and the module does not learn.
It is the one item where *not set* still yields a runnable artifact.

**The last row is the one that changes what this rung can promise**, and it is different in kind from
every row above it. Those are things the module lacks. **That one is a stated function with no declared
substrate.**

## Completion test

**A design entry is finished when the code can be written from it without making a single further
choice.** **This entry is not finished, and it fails in a way worth naming precisely.**

| | state |
|---|---|
| forward operation | **writable, and it covers every neuron in the section** |
| parameter array size | **computable**, at a ceiling |
| density cross-check | **computable**, and re-derived here |
| payload | **0 of 12 typed** |
| sub-element arrays | **no axis of four has an extent** |
| connectivity | **no topography recorded at all** |
| scheduling | **no timing statement of any kind in the section** |
| **the region's own computation** | **runs across an edge nothing declares** |

**The forward operation is writable for every neuron here and the arrays would run over signals the
description cannot name.** More than that: **a module implementing the threshold gate over every
neuron in this structure implements the region's neurons correctly and does not implement what the
region does.** The Function claims that visual and auditory identity are bound into amodal concepts;
the connectional evidence puts the auditory input on the **dorsal** subdivision and the semantic output
on the **ventrolateral** one; **and no edge between any two subdivisions is recorded, in either
direction, under any of the four schemes.** The binding runs on an edge that is not written anywhere.

**That gap is worse than a region with no entry.** A missing region is a missing node, and it is
visible as one — the two outputs to rostral perirhinal and posterior parahippocampal cortex are exactly
that, and they announce themselves. **This is a missing edge inside the one entry the file has**, and
nothing in the entry's own shape makes it visible. **It cannot be repaired at this rung**, and a module
that supplied it would supply the region's headline function out of nothing.

## What the module implements

One structure with its populations, axes and twelve edges as data; the threshold-gate forward operation
with `fan_in`, `sign` and `threshold` unset and visibly so; parameter allocation at the 16-bit ceiling
**with the ceiling flagged as a ceiling** and the fan-in sensitivity curve computed rather than quoted;
an independent recomputation of the density cross-check **across the full ±0.96 cm³ range** rather than
at its centre; the four contested subdivision schemes as data, with `allocate()` raising against a
**contested** extent in different terms from an unsized one; a **payload report** showing 0 of 12 typed
and sorting the twelve by how far the description gets; a **far-end report** distinguishing the six
files checked against the architecture from the two endpoints with no entry anywhere; a
**dangling-requirement report** naming the missing inter-subdivision edge as a stated
function with no declared substrate; and the **measurement cautions** — the 206 MB is a ceiling, the
103M is single-sourced, and the packing density is one term of a calculation that needs two more.
