# Brain architecture — 07 anterior temporal lobe

**Date:** 2026-08-22
**Derived from:** `human_brain_07_anterior_temporal_lobe_2026_08_22.md` — one entry, the temporal
pole. **One source file, and no other content source.**

**Counting basis is uniform in this section: per hemisphere.** One structure, one basis. The
three-basis change that runs through `01_visual_pathway` does not arise here.

**Cross-file checks contained in this file.** One line per far file whose shared edges with this
one are diffed and stemmed.

- `01_visual_pathway`
- `02_auditory_pathway`
- `06_posterior_parietal`
- `08_medial_temporal_lobe`
- `11_frontal_lobe`
- `17_insula_claustrum_habenula`
- `18_white_matter_tracts`

**Every edge in this section leaves it.** All twelve terminate in other files —
`01_visual_pathway`, `02_auditory_pathway`, `06_posterior_parietal`, `08_medial_temporal_lobe`,
`11_frontal_lobe`, `17_insula_claustrum_habenula` — or in a region with no entry anywhere. **All six
now carry a check above**, so every edge below records a diffed far end rather than a dependency.

**A far-end status this file records against an unchecked file is unverified, never settled.** Where
a far file carries no check line above, the response taken is the second of the two permitted ones:
**the far-end dependency is recorded here, naming the file by stem and naming the structure, and no
far end's content is written from memory.** No edge below is in that state.

**Twelve edges here against the source's eleven edge lines, and the difference is recorded rather
than silent.** One source output line names **two** structures — rostral perirhinal cortex and
posterior parahippocampal cortex — and the rule at this rung is that an edge names its target
structure. The arity is explicit in the source, so splitting the line invents nothing; splitting it
without saying so would still have been wrong.

---

## Structural invariants

**Whole-pathway co-instantiation.** This structure is present and active from the outset, and it must
be, because **two loops close through it**:

- **temporal pole ↔ insular cortex** — the insular input carries interoceptive context inward and
  the output limb leaves for the insula. Both limbs are written here.
- **temporal pole ↔ amygdala** — the amygdala's valence tag arrives, the amodal concept leaves for
  affective evaluation. Both limbs are written here.

**The two loops are in different states at their far ends.** The amygdala entry
(`08_medial_temporal_lobe`) declares **both** limbs by name — `← temporal pole`, an amodal concept for
affective evaluation, and `→ temporal pole`, from the **basal / accessory basal** nuclei, the valence
tag — **and the nucleus attribution and both payloads are the ones this file carries.** **So the
temporal pole ↔ amygdala loop is closed at both ends and verifiable from either**, and
co-instantiation for it is satisfied rather than satisfiable-from-this-end-only. The insula entry
(`17_insula_claustrum_habenula`) declares **both** limbs as well — this region among its own inputs
on a line marked reciprocal, and `→ the temporal pole`, interoceptive context, payload otherwise
owed. **So both loops are closed at both ends**, and the two files agree on the payload in each
direction.
*(Both loops are Class 1 — both limbs of each are written in the source's Inputs and Outputs.)*

**Co-instantiation fails one level down, and that is this section's structural finding.** The
region's declared function is binding — visual identity from the inferotemporal cortex and auditory
identity from the rostral superior temporal gyrus, combined into an amodal concept. The connectional
evidence puts the auditory input on the **dorsal** subdivision and the semantic output on the
**ventrolateral** one. **No edge between any two subdivisions is recorded, in either direction, under
any of the four subdivision schemes.** So the loop the function requires runs through a stage the
source does not describe — the same shape the design file records for the cerebro-cerebellar and
hippocampal loops, and it is worse here in one respect: the missing stage is not a region with no
entry, it is an **edge inside the one entry this file has**. **The repair is the source's, not this
document's.**

**Per-edge latency.** Every edge below carries a nonzero, finite, heterogeneous latency in real time
units. **This section can name none of them: all twelve read *to derive*.** The source records no
conduction time, no synaptic delay, and no loop latency — and, unlike `01_visual_pathway`, not even
a qualitative
timing fact anywhere in the section.

**What it does record is the substrate, and it is more than `01_visual_pathway` carries.** Four
association pathways are named as supplying this region's structural connectivity — the **uncinate
fasciculus**, the **inferior longitudinal fasciculus**, the **middle longitudinal fasciculus** and
the **arcuate fasciculus**. Their counts are unknown, and **which pathway carries which edge is
recorded only for the uncinate**, which carries the ventromedial subdivision's limbic and
orbitofrontal traffic. So **one edge class of twelve has a named physical carrier** to derive a
conduction time from, the rest do not, and no length, diameter or g-ratio is recorded for any of the
four tracts. **Three of the four have entries in `18_white_matter_tracts`, and that file declares
this structure
by name** on two routing-only edges, payload owed at the region ends. **The middle longitudinal
fasciculus has no entry there or anywhere**, which that file records as an owed correction at this
section's source.

**No edge in this section is anything other than a projection.** There is no optical arrival, no
endocrine or blood-borne edge, no mechanical transfer, and no transmission-only structure. The
invariant's biological justification — conduction plus synaptic transmission — covers all twelve
edges without exception.

---

## Temporal pole

**Name.** The source's entry heading is *Temporal pole (BA38 / area TG — anterior temporal,
paralimbic)*. The structure is written here as **temporal pole**, with **Brodmann area 38** spelled
out; **area TG** is carried as the area label it is and is not expanded, because no expansion for it
is in the source. **The heading names one cytoarchitectonic field and the source records that as
contested** — the region is a gradient, not a field, and the literature does not agree on how many
areas to cut it into.

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

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Temporal pole | per hemisphere | ~103M | ≤ 16 | ≤ 206 MB |
| **stated total** | per hemisphere | ~103M | | **≤ 206 MB** |

**The total is a ceiling here, not a floor, and that inverts `01_visual_pathway`'s caveat.** One
structure, one
count, and a fan-in that is absent rather than ranged — so 16 bits is the log₂ cap and not a measured
width, and the true figure is at or below 206 MB. What would move it is a synapse count: at a fan-in
of 4,000 the store is 12 bits and **154.5 MB**; at 256 it is 8 bits and **103 MB**. **The neuron
count is single-sourced and has no independent second route**, unlike V1's, because neither cortical
thickness nor surface area is recorded.

**State memory and edge storage are not in this table**, as at every other section: edge storage
cannot be sized until the scheduling discipline is set, and it is not.

**Memory is not a binding constraint here and the figure is not to be reduced.** It is a derived
requirement recorded as found.
