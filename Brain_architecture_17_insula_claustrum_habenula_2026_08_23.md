# Brain architecture — 17 insula, claustrum, habenula, cingulate remainder

**Date:** 2026-08-23
**Derived from:** `human_brain_17_insula_claustrum_habenula_2026_07_25.md` — six entries: the insula,
the claustrum, the habenula, and the midcingulate, posterior cingulate and retrosplenial cortices.
**One source file for content.** One other source file was held on 2026-07-28 and is used only where a
far end sits in it: `human_brain_09_basal_ganglia_2026_07_27.md`.

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed.

- `06_posterior_parietal`. **Five named edges two-ended, two of this file's own marks
  withdrawn, and the three-instance posterior-parietal class endpoint checked against the file its
  candidates were located in and found to have no producer there.**
- `07_anterior_temporal_lobe`. **Both temporal-pole limbs of the insula entry two-ended: this file
  declares `← temporal pole` and `→ temporal pole`, the far end declares each back by name, and the
  two agree on the payload in both directions — *interoceptive context* outbound with the rest owed,
  and owed at both ends inbound.**
- `09_basal_ganglia`. **Four shared endpoints diffed against the file in hand. The internal globus
  pallidus's habenular output is confirmed two-ended and agrees at both ends; the ventral pallidum's
  habenular output is written here on its own line beside the dorsal pallidal source, which discharges
  the cross-file edit that file's ventral-pallidum entry asks for.** **That far end still records the
  edit as owed** — its ground is a quotation taken from a copy of this file that predates the line it
  quotes. See §1b.
- `08_medial_temporal_lobe`. **Twelve shared edges diffed; all twelve declared at both
  ends; three stale marks discharged at the far end and one imprecision corrected here.**
- `11_frontal_lobe`. **Twelve shared edges diffed; eight two-ended, two stale
  class-marks discharged at the far end, one mark of this file's own withdrawn, and four edges
  confirmed to have no producer end — three of them from one structure.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file has been read against this one; an endpoint with no stem is one whose far end has
not yet been opened beside this file, and it is not a claim that none exists.

**The rung spec was not in hand.** `Brain_architecture_design_<date>.md` governs this rung and was
not among the files handed over. The shape below follows
`Brain_architecture_09_basal_ganglia_2026_07_27.md`, which was handed over as the example. **Treat the
*form* as a candidate and the *content* as derived.** In particular the shape-class vocabulary
(*non-laminated nucleus, rank 2: (cell class, N)*) is taken from that file rather than from the spec,
so a shape written below may use a name the spec does not have.

**Counting basis: per hemisphere, and it does not matter, because there are no counts.** Five of the
six structures are cortex or paralimbic cortex; the habenula is a bilateral midline nucleus whose one
firm figure is a **per-side volume**. No entry in the section carries a neuron count of any kind.

**Far ends were mostly not read, and the response taken is to record the dependency rather than fetch
it — with two exceptions now.** Edges leave into files 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13 and 14,
twelve of the nineteen other files. **`09_basal_ganglia`, `06_posterior_parietal`, `07_anterior_temporal_lobe`,
`08_medial_temporal_lobe` and `11_frontal_lobe` are held — five of the twelve.** Weighted by edge mentions the dependency is concentrated:
**files 8 and 11 carry fourteen far ends each**, file 12 eight, file 6 seven, file 14 five, file 9
four. Each edge below names the file its far end sits in and the state of that far end's declaration
as the source records it; **no far end's content is written from memory.**

**The file-8 pass is the first in this file where the far end was read rather than recorded, and its
result is unlike what the rest of this file's marks would predict.** Twelve edges cross between the
two files and **all twelve are declared at both ends. Not one dangles in either direction** — against
a file in which 49 of 74 edges carry a fully owed payload and four far ends inside this very file fail
to declare each other (§3b). **The dependency this file recorded on file 8 was heavier than the debt
turned out to be.** What the diff found instead was three marks in *file 8* asserting a state of this
file that is not this file's state — all three discharged there — and three claustral edges this file
declares that file 8 does not. **The counts of fourteen far ends per file above are edge mentions, not
outstanding items, and the file-8 pass is the evidence that the two are not the same quantity.**

---

## 0. What this section is, and it is the opposite of the last one

**File 09 was a good description the model could not express. This one is a description that does not
say what is on the wires, and the model is not the binding constraint.**

- **74 inter-region edges and 2 internal edges. 49 of the 74 carry a payload that is fully owed** —
  the slot reads *payload unknown — owed* and nothing else. That is **66%.**
- **Six structures, zero neuron counts.** Not one entry in the section carries a count. Nine
  sub-element slots' worth of arrays, and none of them can be sized.
- **Two internal edges in the whole section, both in the insula.** The other five entries read
  *Internal edges: owed* — sub-elements named, no edge between them typed.
- **The completion test fails outright at the claustrum**, and the source says so: *what leaves the
  claustrum on a wire cannot be said.* It fails again at the insula's anterior pole, where the
  payload is *a subjective feeling* — a phrase, not a type.

**So the architecture's job here is mostly to say what is missing in a way that separates the
repairs**, because nothing in the section can be sized, wired or scheduled.

**One thing is not missing, and it is worth naming first because it is the section's real content.**
The **value-brake path is typed end to end**: the internal globus pallidus's *no-reward* signal
arrives on the lateral habenula, and what leaves is a **negative / aversive value signal — a
glutamatergic excitatory drive encoding a worse-than-expected outcome, which the rostromedial
tegmental nucleus inverts in sign into inhibition of the dopamine cells.** That is a payload with a
sign, a content, a stated inversion downstream, and a consumer that declares it. It is the best-typed
edge in the section and one of the better ones in the project.

---

## 1. A correction to the file-09 architecture, from the two files held together

**This is a stop-and-challenge and the evidence is in the two files in hand, so it is checkable
without opening anything else.** It is raised because it changes an invariant conformance verdict at
the previous rung, not because a defect was hunted for.

### 1a. The pallidohabenular loop is satisfiable, and file 09 says it is not

`Brain_architecture_09_basal_ganglia_2026_07_27.md` records, under Structural invariants:

> the whole loop is inside this entry except for one region in file 17 and one that has no entry
> anywhere: the rostromedial tegmental nucleus

and concludes **co-instantiation cannot be satisfied for this loop.** Its source file
(`human_brain_09_..._2026_07_27.md`) carries the same claim, qualified as *no entry in any file read
this pass* — and that pass was 2026-07-23.

**Three independent records in hand say the region now has an entry.** File 17's habenula output edge
reads: *the consumer declares it (file 14), where it is named the major input and the one that defines
the nucleus. Two-ended.* — and adds parenthetically that *this consumer had no entry when this file
was last worked and now has one; the relay is no longer a name on an edge.* The source design file's
§9a records the same, dated **2026-07-24**, with the anatomical owner given as file 14.

**So the sequence is: file 09 checked on 07-23 and found nothing; file 14 gained the entry on 07-24;
file 17 confirmed it two-ended on 07-25; file 09's 07-27 pass expanded abbreviations and did not
re-check.** The claim is not wrong-headed, it is **stale by four days**, and the staleness survived a
regeneration because that regeneration was not a content pass.

**What it changes:** every stage of the loop — internal globus pallidus → lateral habenula →
rostromedial tegmental nucleus → substantia nigra pars compacta → striatum → internal globus pallidus
— now has an entry somewhere, so **co-instantiation for that loop is satisfiable**, and the file-09
architecture's verdict of *not satisfiable* should be reversed when that file is next worked.

**What this does not establish.** File 14 was not read this session. **Three files assert the entry
exists; none of them is file 14.** That is a stronger position than file 09's — its claim rests on one
check that has since been superseded — but it is not verification, and this section does not treat it
as one. *(The quotations and dates are Class 1, from the four documents in hand. The conclusion that
the invariant verdict reverses is Class 2 — Claude's reading, offered to be checked, and it is
contingent on file 14 actually holding the entry.)*

### 1b. A discharged edit still recorded as owed, and the quotation shows why

File 09's ventral-pallidum entry records its lateral-habenula output as **owed as a cross-file edit at
file 17**, on the ground that file 17 *attributes the whole pallidal input to the dorsal structure.*
**File 17 wrote that edge on 2026-07-25** — *← the ventral pallidum, onto the lateral habenula …
Written now, and that owed edit is discharged* — naming file 9 as the producer and quoting file 9's own
owed-edit line back at it.

**The quotation in file 09 is the tell.** It renders file 17's line as *"the **globus pallidus
internus** (the basal-ganglia 'no-reward' signal; entopeduncular nucleus in rodents)"*. File 17 now
reads *← the internal globus pallidus … notes the rodent homologue is the entopeduncular nucleus.*
**The quoted string is from a copy of file 17 that predates its 07-25 abbreviation pass.** The
quotation discipline is not at fault — file 09's 07-27 pass deliberately kept quotations verbatim — but
the *conclusion drawn from it* is stale in the same way §1a is.

**Two staleness findings, one shape.** In both cases file 09 asserts a state of another file that was
true when it looked and is not true now. This is the cross-file version of the failure the source
design records for the superseded copy of file 11: **a record that passes every check that can be run
on it alone.** *(Class 1 — both texts are in hand. The generalisation is Class 2.)*

**Not repaired here.** Editing another section's architecture or source without an explicit request is
outside what this pass may do. **Recorded so the repair is found by reading the work.**

---

## 2. Endpoint kinds — this section exercises all four, and two have no convention

The source's rule is that an endpoint is a **named region with an entry of its own**. This section's
74 edges land on four different kinds of thing, and the count is mechanical:

| kind | count | state |
|---|---|---|
| named region with an entry | 59 | fine |
| named region with **no entry anywhere** | 3 | a gap with a named repair |
| a **class** | 11 | no convention for one sub-kind; see below |
| a **network** | 1 | **explicitly not repairable by naming** |
| *(tract routing, not an edge)* | *3* | *a positive statement; not counted as an edge* |

**The three regions with no entry anywhere are not evenly distributed. Two of them are the medial
habenula's only input and only output.** The **septal nuclei** produce onto the medial habenula; the
**interpeduncular nucleus** consumes from it; **neither has an entry in any of the twenty files**, and
the string *interpeduncular nucleus* appears nowhere in the source outside that one edge. The third is
**parahippocampal cortex**, producing onto the retrosplenial cortex and named by three other files as
well.

**So one of this section's two habenular divisions is described as a relay between two blanks.** The
medial-habenular limb — the cholinergic / substance-P arm, nicotine aversion and withdrawal — has an
origin and nothing at either end of it. **Co-instantiation is not merely unsatisfiable for a loop
here; an entire limb has no instantiable neighbours.** That is a different and worse state than the
missing-stage-inside-a-loop case, because there is no loop to break: there is one described structure
with two undescribed sides.

**The eleven class endpoints cluster, and the clustering is the finding — one repair, not eleven.**

- **"the posterior parietal cortex" appears three times** — at the midcingulate, posterior cingulate
  and retrosplenial entries — with **the same candidate producers in `06_posterior_parietal`** named at
  all three. This was recorded as *one file, one decision, three edges*.
  **Checked against that file on 2026-08-13, and the decision is not the one expected.** All five of
  its entries were read. **Only one of them declares any output into this file at all — the precuneus,
  to the posterior cingulate cortex — and that edge is already declared by name at both ends,
  separately from the class.** The angular gyrus, the supramarginal gyrus and the two intraparietal
  entries declare no output to any entry here. **So the class does not resolve into that file's
  structures; it resolves to nothing there beyond an edge already written.**
  **That is a stronger state than an unresolved class, not a weaker one.** An unresolved class is a
  question with an assumed location for its answer. **This one has had its assumed location checked
  and emptied**, so the repair is no longer a decision inside that file but a search for producers
  neither file has named. **One repair still, but not the repair described** — and the three instances
  remain one repair only because they will now all resolve, or fail to, in the same place.
- **"the cerebral cortex, near all-to-all"** appears twice, in and out of the claustrum, and the
  source states plainly that **it has no convention for an all-to-all endpoint and this entry is where
  it is first needed.** This is *not* the file-09 case. There the source held *nearly all of cortex*
  open as a question about whether a list is expressible. Here the reason is stronger and is about the
  data: **the connectivity is described as diffuse rather than precisely mapped, so resolving it into
  named producers would assert a specificity the literature does not report.** Splitting is not merely
  awkward, it would manufacture a claim.
- **"the cingulate cortex"** appears twice, in and out of the claustrum, and **three of its four
  candidate far ends are entries in this same file** — see §3b.
- The remainder are singletons: *neuromodulatory afferents*, *the basal ganglia*, *brainstem autonomic
  targets*, *visual areas*.

**The one network endpoint is a different kind of object and the source refuses to repair it.** The
posterior cingulate's output to **the cognitive-control network**, via the dorsal posterior cingulate,
names a set of regions defined by correlated activity rather than by a projection. Listing the members
would turn one edge into several and assert that each receives the same payload, which is not what the
claim says. **How the source writes an edge to a network, or whether it refuses to, is open and
unasked.** *(Class 1 — the source states this. The observation that the section exercises all four
endpoint kinds is Class 2.)*

---

## 3. Structural invariants

### 3a. Whole-pathway co-instantiation

Every structure here is present and active from the outset. Four statements about whether that is
satisfiable:

- **The value-brake path is satisfiable**, subject to §1a. Internal globus pallidus → lateral habenula
  → rostromedial tegmental nucleus → ventral tegmental area and substantia nigra pars compacta, with
  the raphe limb alongside. Every stage has an entry; three of the four edges are two-ended; the
  payload is typed. **This is the one path in the section that could be instantiated if it had
  numbers.**
- **The medial-habenular limb is not satisfiable at all**, and not because of a loop — because
  **both** of its neighbours are regions the source does not describe (§2).
- **The Papez return arm is not satisfiable**, and it fails in a file the section does not own. The
  retrosplenial output to the hippocampal formation runs **via parahippocampal and entorhinal cortex**,
  and parahippocampal cortex has no entry. The source design already records this loop as blocked by
  that family; **this section is a second file declaring an edge through it.**
- **Co-instantiation below the structure level is unstatable for five of six.** Only the insula has
  internal edges. The habenula's two divisions are stated to have different transmitters, inputs and
  targets and **whether they communicate with each other at all is not established**; the claustrum's
  three cell classes have no edge between them; the three cingulate entries name sub-elements and type
  nothing between them.

### 3b. A two-ended diff failure inside one file, in one pass

**Four far ends that this section's edges point at are entries in this same file, and they do not
declare the edge.**

- **← the posterior cingulate cortex**, at the midcingulate entry. The posterior cingulate entry's
  Outputs name the hippocampal formation, the precuneus, the angular gyrus, the orbitofrontal /
  ventromedial prefrontal cortex, and the cognitive-control network. **Not the midcingulate cortex.**
  The midcingulate entry's line says *the producer is in this file and declares the reciprocal
  relationship* — and that is the mechanism of the miss. **Reciprocity is a relationship; an edge is
  not.** A reciprocal pair is two edges and each needs its own declaration at both of its own ends.
  Eleven edges in this section use the word *reciprocal*; this is the one where it stood in for a
  declaration that is absent.
- **← and → the cingulate cortex**, at the claustrum, whose candidate producers are the anterior
  cingulate entry in file 11 and **the midcingulate, posterior cingulate and retrosplenial entries in
  this file. None of the four declares it**, and the source records it as owed at all four.

**This is the cheapest repair in the section and it is the one not done.** No other file needs to be
opened, no far end needs to be fetched, and the whole diff runs inside the one file that one pass had
open at once — 649 non-blank lines as this section was written, 952 now (§11). *(That the four ends are undeclared is Class 1 — the source states it. The reading that
*reciprocal* is what let the midcingulate case through is Class 2.)*

**And the two-ended agreements this section does have are mostly worth less than they look.** Of 24
edges marked *two-ended*, **five say in the same breath that both ends were written in this same pass**
— insula ↔ midcingulate, insula ↔ habenula, midcingulate ↔ posterior cingulate. The source's own
caution applies: two ends written in one pass from one sentence agree by construction and certify
nothing. **The agreements that do certify something are the ones across a file boundary and across a
date** — the amygdala's valence tag from file 8, the anterior cingulate's scalar reward value from
file 11, the completed episode from file 8, the rostromedial tegmental and raphe limbs from files 14
and 13.

### 3c. Per-edge latency

Every edge carries a nonzero, finite, heterogeneous latency in real time units. **All 76 read *to
derive*.**

**The section contains exactly one number with a time in it, and it is not an edge latency.** The
claustrum is described as regulating **slow (~0.5–4 Hz) cortical oscillations** during mental-state
transitions. That is a period of **250 ms to 2 s**.

**It is nevertheless the only quantitative constraint on any latency in the section, and it constrains
the one edge that cannot be typed.** A structure that regulates an oscillation must close its loop
fast relative to the oscillation's period — so the claustro-cortical round trip has an upper bound of
order the period, and the axons carrying it are described as **exceptionally far-reaching**, which is
the property that makes the bound non-trivial rather than automatic. **The architecture can state that
a bound exists and cannot state the number**, and the edge it bounds is the same edge whose payload
cannot be written. *(The frequency and the axon description are Class 1. The inference that it bounds
the loop delay is Class 2 — Claude's reading, offered to be checked; it is a control argument, not a
measurement, and no source was opened for it.)*

**A second timing claim with no number, and it is a function rather than a property.** The anterior
insula and dorsal anterior cingulate cortex are said to **switch** between the default-mode and
central-executive networks. A switch has a latency and the section gives none. The posterior cingulate
is likewise said to **modulate the switch between internal and external focus**. **Two structures in
this section are defined by a transition whose duration is nowhere.**

### 3d. Tracts

Four tracts are named as carrying this section's edges. **Two have entries and two do not.**

- **the cingulum** — has an entry in file 18, and this section uses it correctly: three entries record
  it as **routing rather than as an edge**, which is the convention the source settled for tracts. Those
  three bullets are not counted as edges above.
- **the stria medullaris** (all habenular input) and **the fasciculus retroflexus** (all habenular
  output) — **neither has an entry anywhere.** Both are on the source design's list of tracts named on
  other files' edges with no entry.
- **the external and extreme capsules**, which flank the claustrum, are named as its myelination
  context rather than as carriers.

**So the entire habenular traffic — in and out, both divisions — rides on two tracts the source does
not describe**, and a tract is where the physical substrate of a latency lives.

---

## 4. Insula — interoceptive / salience / emotional core

- **Function → structure.** The brain's **interoceptive** cortex, and at its anterior pole a core hub
  of the **salience network**, with a **posterior → anterior gradient** from objective body state to
  subjective feeling. Posterior insula is primary interoceptive cortex, receiving the lamina-I
  spinothalamic stream by way of the posterior / ventromedial-posterior thalamus. Mid-insula
  re-represents and integrates. Anterior insula binds that image with emotional, cognitive and social
  context into **subjective feelings**, and with the dorsal anterior cingulate cortex anchors the
  salience network — detecting behaviourally relevant events and switching between the default-mode
  and central-executive networks. Contains **von Economo (spindle) neurons**, large fast projection
  cells.

  **Sub-elements: a gradient, not blocks, and this is a shape claim before it is an anatomy claim.**
  Fully **granular** six-layered cortex postero-dorsally, **dysgranular** through the middle and dorsal
  anterior territory, **agranular** with undifferentiated layers II/III antero-ventrally. Quantitative
  human postmortem mapping names granular areas **Ig1, Ig2, Ig3**, dysgranular areas **Id1** through
  **Id6**, and agranular area **Ia1**. Intracortical myelin and parvalbumin neuropil follow the same
  decreasing gradient, so it is chemical and myeloarchitectonic as well as laminar. Somatotopy is
  reported in the dorsal posterior sector.

  **The standard laminar block is not transcribed**, and correctly: three of its edges route through
  layer 4, which the agranular and dysgranular sectors do not have.

  **How many subdivisions there are is contested, and the contest is over the boundaries, not the
  gradient.** Published human parcellations run from a two-part anterior-agranular / posterior-granular
  split, through the three-belt scheme, to schemes naming sixteen granular areas. The source records
  it as contested and places its edges on the gradient's poles rather than on any one parcellation.

  **Von Economo neurons cross the architectonic boundary rather than marking it** — the field extends
  from the anterior agranular insula into the anterior dysgranular insula.

- **Inputs.** Ten edges.
  - **← posterior / ventromedial-posterior thalamus** (ventromedial posterior nucleus, posterior
    nuclear group), onto the **dorsal posterior insula** — the body's physiological condition, the
    lamina-I interoceptive stream, **somatotopically ordered**. Fan-in: to derive. *(File 12,
    two-ended and in the same terms. **Whether the three labelled lines the spinal entry types —
    nociceptive-specific, thermoreceptive-specific, polymodal — stay separate on this edge or are
    merged is owed at both ends.** That is an arity question, and it is the same class as the layer-4
    split the source design warns changes an edge's arity from the far end.)*
  - **← primary somatosensory cortex**, from **area 3a** — payload owed. Fan-in: to derive. *(File 5;
    two-ended, owed at both.)*
  - **← secondary somatosensory cortex**, from the **ventral somatosensory area**, whose inner edge
    adjoins the insula — payload owed. Fan-in: to derive. *(File 5; two-ended, owed at both.)*
  - **← the gustatory pathway**, onto the **anterior insula / frontal operculum** — **taste quality
    and intensity**, in the producer's terms. Fan-in: to derive. *(File 3.)*
  - **← vestibular nuclei and the central vestibular pathway**, onto the **parieto-insular vestibular
    cortex** — **head rotation rate and gravito-inertial acceleration**, in the producer's terms.
    Fan-in: to derive. *(File 3.)*
  - **← auditory parabelt** — payload owed. Fan-in: to derive. *(File 2; the producer's line is a
    compound naming several destinations and marks its own arity unresolved, so this edge is
    **declared but not individually typed at either end.**)*
  - **← amygdala** (`08_medial_temporal_lobe`) — the **valence tag**: a gain on perception, attention
    and memory encoding, carrying **no identity information** — what arrives is the significance, not
    the thing. Fan-in: to derive. *(Typed from the producer.* **Two-ended across a file boundary — one
    of the agreements that certifies something —** *and confirmed by reading the producer on
    2026-08-13: its amygdala entry declares this target inside a five-edge compound carrying the same
    valence tag, of which this file holds two ends and file 11 the other three.)*
  - **← temporal pole** — payload owed. Fan-in: to derive. *(`07_anterior_temporal_lobe`; two-ended, owed at both.)*
  - **← orbitofrontal / ventromedial prefrontal cortex** (`11_frontal_lobe`) — payload owed. Fan-in:
    to derive. **Two-ended and confirmed 2026-08-13; owed at both ends**, in the same words at each.
  - **← anterior cingulate cortex** (`11_frontal_lobe`) — payload owed. Fan-in: to derive. **The
    producer declares no such edge**, though its Inputs do declare the reciprocal limb from here.
    **Checked 2026-08-13 and the mark is confirmed, not merely carried**: that structure's Outputs slot
    holds four edges and none is to this one. **So the return arm of a relationship this entry calls
    reciprocal is absent at its producer, and *unconfirmed* was the weaker word.** **Owed at
    `human_brain_11_...`, and it is one of three edges that file's anterior cingulate entry owes this
    section** — see the habenula and posterior cingulate entries below.

  **Dangling requirement — "context" was never a payload, and three quarters of it still is not.** The
  Function slot consumes *emotional, cognitive and social context*, bound at the anterior pole into
  subjective feeling. Four incoming limbs were meant to supply it; **one now carries a typed payload
  (the amygdala's valence tag) and three are owed at both ends.** **The requirement stands at
  three-quarters size.**

- **Outputs.** Eleven edges.
  - **→ anterior cingulate cortex** (`11_frontal_lobe`) (salience → control) — the **salience
    signal**: *this event is behaviourally relevant now*. **Whether what leaves is a scalar, a pointer,
    or a switching command is not established.** Fan-out: to derive. **Two-ended and confirmed
    2026-08-13, and this end is the typed one** — the consumer carried the edge untyped and has taken
    this wording, including the non-establishment.
  - **→ right inferior frontal gyrus** (`11_frontal_lobe`) — the same salience signal; payload
    otherwise owed. Fan-out: to derive. **Two-ended and confirmed 2026-08-13, and this line discharged
    a mark there.** The consumer read *the producer declares its cortical target as a class that covers
    this structure without naming it*. **It is a named line here and has been since the split below.**
  - **→ orbitofrontal / ventromedial prefrontal cortex** (`11_frontal_lobe`) — the salience signal and,
    reciprocally, the **interoceptive state**; payload otherwise owed. Fan-out: to derive. **Two-ended
    and confirmed 2026-08-13, and this line discharged a mark there** in the same terms: the consumer
    read *the producer declares its cortical output as a class covering this structure; writing the
    limb by name is owed at file 17*. **The named limb it asked for is this line.**
  - **→ temporal pole** — **interoceptive context**; payload otherwise owed. Fan-out: to derive.
    *(File 7.)*
  - **→ midcingulate cortex** — the **salience / affect signal**, in the consumer's terms; payload
    otherwise owed. Fan-out: to derive. *(In this file. **Both ends written in one pass; the agreement
    certifies nothing.**)*
  - **→ amygdala** (`08_medial_temporal_lobe`) — payload owed at both ends. Fan-out: to derive.
    **Two-ended and confirmed on 2026-08-13**: the consumer declares `← insula` and marks it *payload
    owed at both ends* in the same words. **Both ends agree, and what they agree on is that neither
    can say what is on the wire.**
  - **→ bed nucleus of the stria terminalis** (`08_medial_temporal_lobe`), from the **anterior
    insula** — **interoceptive state**; payload otherwise owed. Fan-out: to derive.
    **Two-ended and confirmed on 2026-08-13, and this edge discharged a debt at the far end.** The
    consumer's line read *the producer declares no such edge — owed at file 17*. **This file declares
    it, attributes it to the same sub-element the consumer names, and types it in the same two
    words.** The mark was written on 2026-07-26, before this file existed; **it was never a finding
    about this file, and the pass is what turned it into one that could be discharged.**
  - **→ hypothalamus** (autonomic / affect) — payload owed. Fan-out: to derive. *(File 14, not
    confirmed.)*
  - **→ basal ganglia**, onto the **ventral striatum** — payload owed at both ends. Fan-out: to derive.
    *(`09_basal_ganglia`. **Checked against the file in hand and it agrees**: that entry declares
    the insular input onto the ventral striatum with the payload owed at both ends. Two-ended, across a
    file boundary and across a date.)*
  - **→ habenula**, onto the **lateral habenula** — a **bad-outcome expectation**: an affective /
    evaluative signal that an outcome is worse than wanted. Payload otherwise owed. Fan-out: to derive.
    *(In this file; both ends confirmed in one pass.)*
  - **→ posterior / ventromedial-posterior thalamus** (corticothalamic feedback) — **no stimulus
    content; the driver / modulator gate.** Fan-out: to derive. *(File 12, two-ended and in the same
    terms.)*
    **This is a payload stated as an absence**, and it is the same shape as the basal ganglia's *tonic
    inhibition, selectively released*: what makes it checkable is what it does **not** carry. **The
    section has two of these** — this and the salience signal's stated non-establishment — and a
    stated negative is worth more than a name.

  **The cortical output class is resolved as far as it can be, and the residue is now a negative.**
  Three of the lines above were split out of *→ anterior cingulate cortex and prefrontal cortex*, which
  named one region and one class. **Two of the three split-out lines discharged stale marks at their
  consumers on 2026-08-13**, which is what a split is for: the consumers had been carrying the
  pre-split state.
  **The open question about the dorsolateral prefrontal cortex is now closed as a negative.** That
  structure's Inputs slot in `11_frontal_lobe` was read on 2026-08-13 and **declares no insular source
  of any kind**. So either the class never covered it, or it did and the consumer does not carry it.
  **Either way this file writes no fourth line**, and the question moves from *unchecked* to
  *checked and absent* — the stronger of the two states, and the one a later pass cannot mistake for
  work not yet done.

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, no clean human per-region count;
  association / paralimbic cortex, uncounted per-region in human as with prefrontal and
  inferior-parietal association areas. **Parameter memory: to derive.** Synapses, axons, white-matter
  volume, myelination: unknown. **Grey-matter volume:** a sizeable territory, no single verified human
  figure. **No cross-check of any kind can be run.**

  **The one countable feature named is the von Economo neuron population**, and it is *a small
  specialised fraction of the total* — a count of a fraction of an uncounted whole, which constrains
  nothing until the whole is counted.

- **Shape.** **Laminated cortex whose laminar axis is not uniform across its own extent.** The layer
  set is granular postero-dorsally and agranular antero-ventrally, so **there is no single layer axis
  for the structure** and the standard block cannot supply one.
  The tangential axis is **contested in extent** — 2, 3 or 16 areas depending on the parcellation.
  That is a state the count ladder has a name for and the shape ladder does not: **not unknown (the
  tissue has been mapped repeatedly), not owed (no further literature is being pointed at), but
  contested — measured several ways, needing adjudication.** *(That *contested* is the right state for
  a shape axis rather than only for a count is Class 2 — Claude's reading.)*
  Somatotopy is reported in the dorsal posterior sector, giving one sector a metric axis and the rest
  none. **The tile calculation cannot start: no thickness, no surface area, no pitch.**

- **Edge latency.** All 23 edges **to derive.**

- **Invariant conformance.** Co-instantiation: **the only entry in the section with internal edges**,
  two of them, posterior → mid and mid → anterior, which is the gradient's own data flow. Satisfied in
  form at the structure level; **the second internal edge terminates on a payload that fails the
  completion test.** Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** **The gradient is the computation, and the architecture can say so
  precisely because the source refused to draw boundaries across it.** Three sectors, three
  cytoarchitectures, and one directed chain through them: an objective body-state image enters the
  granular pole, is re-represented in the dysgranular middle, and is bound with limbic context at the
  agranular pole. **What makes it a claim rather than a description is that the two internal edges run
  in the direction of decreasing granularity** — the tissue loses layer 4, which is the input layer,
  exactly where it stops receiving from outside and starts receiving from itself.
  **And that is where the payload stops being writable.** *A subjective feeling* is the terminus of the
  chain and it is a phrase. The source names the same failure at the temporal pole and the prefrontal
  cortex, and the source design records where such cases cluster: **the convergence nodes whose claim
  is that modality-specific formats become modality-independent.** A payload is a statement about
  format, so the place where format is said to dissolve is the place where the payload cannot be
  stated. **The insula's anterior pole is that place, reached by a two-edge walk that is fully
  described.** The description gets you to the door.

---

## 5. Claustrum — the most-connected hub

- **Function → structure.** A thin sheet of grey matter in the basolateral forebrain, lateral to the
  putamen across the external capsule and medial to the insula across the extreme capsule — and **per
  unit volume the most densely connected structure in the brain**, reciprocal with almost the entire
  neocortex plus the amygdala, hippocampus / subiculum and cingulate cortex. **Its function is
  unresolved.** Four hypotheses are on the table: cortical **synchronisation / binding** (the
  "conductor of the cortical orchestra"), **multisensory integration**, **salience / attentional
  control and network switching**, and regulation of **slow (~0.5–4 Hz) cortical oscillations** during
  mental-state transitions. A single human stimulation case near the claustrum produced a reversible
  loss of consciousness. It densely expresses serotonin-2A receptors.

  **Sub-elements: three cell classes and a division, none of which is established as a sub-element by
  the source's own test.** **Pyramidal-like projection neurons**, **fusiform cells**, **circular
  cells**, and a **gap-junction-coupled GABAergic interneuron network**. A **dorsal / ventral**
  division is used by the entry's own edges — the ventral claustrum carries the amygdala and cingulate
  connections. **Whether dorsal and ventral project to different targets, which is the test, is owed.**

  **No cortical-style lamination**, and that is a **positive statement**, not a gap: it is why the
  standard laminar block cannot be written here.

  **Internal edges: owed — and one of them may not be an edge at all.** The gap-junction coupling among
  interneurons is an **electrical coupling, not a directed synapse**, and **the source has no
  convention for a non-directed coupling.** This is a finding against the edge model rather than a gap
  in the description: an edge has a source and a target, and a gap junction has neither, or both at
  once. **Recorded, not repaired — the convention is not this rung's to set.**

  **All four of this entry's non-cortical cross-edges rest on one sentence and one citation, and the
  citation cannot carry them. Found 2026-08-13.** The amygdalar and hippocampal limbs, in and out,
  derive from the source's Function statement that this structure is *reciprocally connected* with the
  amygdala and hippocampus / subiculum, cited to a single **diffusion-tractography** study. **Diffusion
  tractography is undirected** — it cannot distinguish an afferent from an efferent connection — so the
  citation supports **that a connection exists** and supports **no direction on any of the four.** The
  2026-07-25 pass split that one undirected prose claim into four directed edges; **nothing was
  invented at the split, and four directions now stand where none was warranted.**
  **Owed at `human_brain_17_...`: a directional warrant for each limb, or the four edges collapse to
  two undirected connections the edge model has no form for** — which is the same gap this entry
  already records for the gap-junction coupling below. **The §2a entry for that citation already
  records that its "connectivity" is streamline count rather than counted projections; this is the
  consequence that entry does not draw.**
  *(Class 1: the citation, the method and the split are all in the two files. That the primate
  tract-tracing literature describes the amygdala and hippocampus as projecting **to** the claustrum
  rather than reciprocally with it is Class 3 — from a search run 2026-08-13, offered as a candidate,
  and not written into any edge.)*

- **Inputs.** Five edges, **all payloads owed.**
  - **← cerebral cortex**, near **"all-to-all"** — payload owed. Fan-in: to derive. **The hardest class
    endpoint in the file**, and the one the source says it has no convention for (§2).
  - **← amygdala** (`08_medial_temporal_lobe`), onto the **ventral claustrum** — payload owed. Fan-in:
    to derive. **The producer declares no such edge**, though its Inputs declare the reciprocal limb
    from here. **Confirmed outstanding on 2026-08-13 by reading the producer**: its amygdala Outputs
    slot lists sixteen targets and the claustrum is not among them, while its Inputs slot carries
    `← claustrum`. **But the repair is not at that file.** This edge's warrant is one sentence in
    `human_brain_17_...`'s Function slot above, carrying one citation — **a diffusion-tractography
    study, which is undirected and cannot establish that the connection runs this way rather than the
    other.** **Owed at `human_brain_17_...`: the direction, not the far end's declaration.**
  - **← cingulate cortex** — payload owed. Fan-in: to derive. **A class, and three of its four
    candidate producers are entries in this same file. None of the four declares it.** *(§3b.)*
  - **← hippocampus / subiculum** (`08_medial_temporal_lobe`) — payload owed. Fan-in: to derive.
    **Confirmed outstanding on 2026-08-13: that file's hippocampal formation entry declares no
    claustral edge in either direction.**
    **A correction to this line, from reading the far end.** It previously read *file 8, which declares
    no claustral edge in either direction*. **That is true of the hippocampal formation entry and
    false of the file** — file 8's **amygdala** entry declares `← claustrum`. The scope of the claim
    was the file and the evidence was one entry. **The generalisation was one entry too wide, and a
    far-end claim about a whole file is the shape that goes wrong quietly**, because the entry it was
    checked against still supports it.
  - **← neuromodulatory afferents** — payload owed. Fan-in: to derive. **A class.** The four
    neuromodulatory entries each declare a brain-wide cortical class that would cover this structure
    without naming it. *(Owed at file 13: name the nuclei, or record that the brain-wide class is the
    whole claim.)*

- **Outputs.** Four edges, **all payloads owed.**
  - **→ cerebral cortex**, near all-to-all and reciprocal, on **exceptionally far-reaching
    claustro-cortical axons** — payload owed. Fan-out: to derive.
    **This is the edge the entry's Function slot depends on.** Binding, synchronisation, network
    switching, slow-oscillation control — **every one of the four hypotheses is a claim about what
    travels on this edge, and none of them types it.**
  - **→ amygdala** (`08_medial_temporal_lobe`) — payload owed. Fan-out: to derive. **Two-ended and
    confirmed on 2026-08-13, and this edge discharged a debt at the far end.** The consumer's line
    read *declared in prose rather than as a typed edge — owed there*. **It is a typed edge line here,
    with a payload slot and a fan-out slot, and has been since this file was written.** *(The
    consumer's mark was written against the source rung on 2026-07-26, before this file existed;
    whether it still holds of `human_brain_17_...` was not checked, because that file was not held.)*
    **This is the only one of the four claustral cross-edges that is declared at both ends.**
  - **→ hippocampus / subiculum** (`08_medial_temporal_lobe`) — payload owed. Fan-out: to derive.
    **Confirmed outstanding on 2026-08-13**: that file's hippocampal formation Inputs slot declares no
    claustral source. **The repair is not at that file** — this limb and its inbound partner share the
    single undirected citation described in the Function slot above. **Owed at `human_brain_17_...`.**
  - **→ cingulate cortex** — payload owed. Fan-out: to derive. **Same class problem and same four
    unconfirmed far ends as the input limb.**

- **Sizing.** Basis: per hemisphere. **Neurons: to derive**, and the reason is different from the
  cortical entries' reason: **a thin, hard-to-segment sheet.** **Grey-matter volume: no verified human
  figure, soft and segmentation-dependent.** Synapses, axons, white matter: unknown. Myelination:
  flanked by the extreme and external capsules, g-ratio unknown. **No cross-check can be run.**

  **The structure's defining quantitative fact is a quantity the architecture cannot use.**
  *Most-connected per unit volume* is a statement about **connection density** — and connection
  topology is precisely what is not set, and every fan-in and fan-out slot in the entry reads unknown.
  **So the one thing that is known quantitatively about this structure is known about the one axis the
  model has no values on.**

- **Shape.** **Non-laminated sheet.** Rank is not the nucleus rank-2 of the file-09 entries and not
  laminated cortex either: it is a **two-dimensional sheet with a thickness**, and none of the three
  extents is given. The cell-class axis has **three named members** whose status as sub-elements is
  unestablished; the dorsal / ventral axis has two members whose status is **owed**. **No extent on any
  axis.**

- **Edge latency.** All 9 edges **to derive** — and see §3c: this is the entry whose function supplies
  the section's only temporal constraint, on the one edge whose payload cannot be written.

- **Invariant conformance.** Co-instantiation: **internally unstatable** — no internal edge is
  described, and one candidate internal relation is not a directed edge at all. At the structure level
  the near-all-to-all cortical coupling means **co-instantiation of this structure is co-instantiation
  of the cortex**, which is either the invariant working as intended or the invariant becoming
  vacuous; **the section cannot tell which, because the edge is untyped.** Per-edge latency: satisfied
  in form, all to derive.

- **Justification (biological).** **This entry is the completion test's clearest failure in the source,
  and its structure is worth stating exactly.** The entry has four candidate functions. Each is a claim
  about one output edge. That edge's payload is owed. **So the four hypotheses are not four competing
  descriptions of a known signal — they are four guesses at an unknown one**, and choosing among them
  is not a modelling decision that can be deferred to a lower rung, because there is nothing to defer.
  **An entry whose payload cannot be written is an entry whose function is not understood, and the
  source says as much on its face.**
  **The architecture's contribution is to say what would settle it, and one thing would.** Every
  hypothesis is a claim about *timing* rather than about content: binding, synchronisation, switching
  and slow-oscillation control are all statements about **when** distributed activity is aligned, not
  about **what** is on the line. **A payload that is purely temporal is a payload this project has not
  met yet** — everywhere else the slot asks what property, in what units, in what frame. **If the
  claustral output turns out to carry no content at all but only a time, that is a finding about the
  source's payload slot and not only about the claustrum.** *(Class 2 throughout this paragraph —
  Claude's reading of the four hypotheses in the source's Function slot. Offered to be checked; no
  source was opened for it.)*

---

## 6. Habenula — the value brake

- **Function → structure.** A small **epithalamic** hub that converts *things are going badly* into a
  brake on the brain's value chemistry — the anatomical counterweight to the dopamine reward system.
  **Two divisions.** The **lateral habenula** is the negative-value node: excited by aversive events,
  pain, loss, and the **omission of expected reward** — a **negative reward-prediction error**, the
  mirror image of midbrain dopamine neurons. It suppresses dopamine chiefly **indirectly**, driving the
  GABAergic **rostromedial tegmental nucleus**, which inhibits dopamine cells in the ventral tegmental
  area and the substantia nigra pars compacta; and it is reciprocally tied to raphe **serotonin**.
  Sustained lateral-habenular overactivity is a leading circuit account of depression / learned
  helplessness. The **medial habenula** is a cholinergic / substance-P system projecting to the
  **interpeduncular nucleus**, tied to nicotine aversion and withdrawal, anxiety and sleep-state
  modulation.

  **Sub-elements: two, and they meet the test on the strongest possible ground.** Medial and lateral
  habenula have **different transmitters, different inputs and entirely different targets**, and every
  edge in the entry is already attributed to one or the other. Each has several subnuclei that are not
  named here, so **the level below the division is owed.**

  **Internal edges: owed, and the specific gap is stated — whether the two divisions communicate at
  all is not established.** That is a real question rather than a formality: they are adjacent, they
  are named as one structure, and they share nothing on the wire in this description.

- **Inputs.** Eight edges, all over the **stria medullaris**, from limbic and basal-ganglia forebrain.
  - **← septal nuclei**, onto the **medial habenula** — payload owed. Fan-in: to derive. **This
    producer has no entry in any of the twenty files.** *(§2. A third file naming a septal producer
    with no slot; the source records that which file owns them is not obvious.)*
  - **← internal globus pallidus**, onto the **lateral habenula** — the basal-ganglia **"no-reward"
    signal**; payload otherwise owed. Fan-in: to derive. *(`09_basal_ganglia`, which wrote its end specifically to
    close this diff. **Confirmed against the file in hand this session: it agrees.** Two-ended.)*
  - **← ventral pallidum**, onto the **lateral habenula** — payload owed. Fan-in: to derive. *(`09_basal_ganglia`;
    written here and the owed edit discharged. **File 9 still records it as owed — see §1b.**)*
  - **← lateral hypothalamus** and the lateral septo-hypothalamic continuum, onto the **lateral
    habenula** — payload owed. Fan-in: to derive. *(File 14, not confirmed.)*
  - **← suprachiasmatic nucleus**, onto the **lateral habenula** — payload owed. Fan-in: to derive.
    *(File 14, where it is a named sub-element — the circadian master clock — that does not declare
    this edge. Owed there.)*
  - **← anterior cingulate cortex** (`11_frontal_lobe`), onto the **lateral habenula** — a
    **bad-outcome expectation**; payload otherwise owed. Fan-in: to derive. **The producer declares no
    such edge. Checked 2026-08-13 and confirmed absent**, not merely unconfirmed: that structure's
    Outputs slot holds four edges and none reaches this section. **Owed at `human_brain_11_...`.**
  - **← anterior insula**, onto the **lateral habenula** — a **bad-outcome expectation**; payload
    otherwise owed. Fan-in: to derive. *(In this file; both ends in one pass.)*
  - **← ventromedial prefrontal cortex** (`11_frontal_lobe`), onto the **lateral habenula** — a
    **bad-outcome expectation**; payload otherwise owed. Fan-in: to derive. **The producer declares no
    such edge. Checked 2026-08-13 and confirmed absent**: that structure's Outputs slot holds ten edges
    and none reaches this section. **Owed at `human_brain_11_...`.**
    **The endpoint names the ventromedial half of a structure the far file has not split**, whose
    heading covers orbital and medial areas together and whose own entry records that its edges sort
    into two systems. **So this edge asks for a producer sub-element that does not yet exist as a
    unit**, which is a second debt behind the first.

  **Three edges carry the same payload name and two of the three have no producer end.** *Bad-outcome
  expectation* arrives from the anterior cingulate cortex, the anterior insula and the ventromedial
  prefrontal cortex; only the insular limb is declared at its source, and that one is in this file.
  **Checked 2026-08-13 against `11_frontal_lobe`, which holds both outstanding producers: both were
  read and both edges are absent.** **So the cortical half of the value brake is asserted at the
  consumer and *absent* at two of three producers** — the word was *unconfirmed*, and the pass has
  replaced a state that could have resolved either way with one that can only resolve by writing the
  edges at the source. **This entry is the whole cortical evidence for a path this section describes
  as the brake on the reward system.**

- **Outputs.** Four edges, all over the **fasciculus retroflexus**.
  - **→ interpeduncular nucleus**, from the **medial habenula** — payload owed. Fan-out: to derive.
    **This consumer has no entry in any of the twenty files** and the string appears nowhere else in
    the source. *(§2.)*
  - **→ rostromedial tegmental nucleus**, from the **lateral habenula** — a **negative / aversive value
    signal**: a **glutamatergic excitatory drive encoding a worse-than-expected outcome, which that
    nucleus inverts in sign into inhibition of the dopamine cells.** Fan-out: to derive. *(File 14,
    where it is named the major input and the one that defines the nucleus. Two-ended.)*
    **This is the best-typed edge in the section** — sign, content, and a stated downstream inversion.
  - **→ raphe nuclei**, from the **lateral habenula** — the same signal, modulating serotonin rather
    than dopamine; payload otherwise owed. Fan-out: to derive. *(File 13; two-ended.)*
  - **→ pineal gland**, from the **medial habenula** — payload owed. Fan-out: to derive. **The consumer
    declares no such edge**, and types its own input as a sympathetic efferent chain gated by the
    circadian clock. **The link is stated in the Function slot as prose — "links to the pineal" — and
    that is not an edge**: neither its direction nor its content is established at this end either.
    *(Owed here first, then at file 14.)*

  **No direct dopamine edge is written**, deliberately: the suppression is *chiefly indirect* and the
  source records the relay as the edge. A sparse direct habenula → ventral-tegmental-area projection is
  reported in the literature and is **not** written, because it was not confirmed at either end.
  **Owed: confirm or refuse it.** **This is the right handling and it is worth naming as such** — a
  reported edge left out with the reason recorded costs nothing and can be checked; a reported edge
  written in from recall cannot.

- **Sizing.** Basis: **per side**, and this is the only entry in the section with a firm number of any
  kind.
  **Neurons: to derive**, and the state is different again from the other five: **human stereology
  exists and reports volumes and disease-related changes rather than a control absolute.**
  **Grey-matter volume: ~30–36 mm³ per side** — post-mortem ~31 mm³ left and ~33 mm³ right,
  uncorrected for shrinkage; high-resolution magnetic resonance imaging ~29–36 mm³. A slight **right >
  left** asymmetry with a soft functional lateralisation. **White-matter volume:** unknown.
  **Myelination:** the fasciculus retroflexus is a compact myelinated tract, g-ratio unknown.

  **What the volume does and does not buy, computed rather than asserted.** A volume converts to a
  count only through a density, and **no density is given anywhere in this section.** Across a span of
  packing densities chosen to bracket rather than to estimate:

  | density | neurons per side | store at 16 bits/neuron |
  |---|---|---|
  | 10,000 /mm³ | 300,000 – 360,000 | 0.60 – 0.72 MB |
  | 20,000 /mm³ | 600,000 – 720,000 | 1.20 – 1.44 MB |
  | 50,000 /mm³ | 1.50M – 1.80M | 3.00 – 3.60 MB |
  | 100,000 /mm³ | 3.00M – 3.60M | 6.00 – 7.20 MB |

  **Factor of twelve across the table, and eleven of it comes from the density, not the volume.** So
  the firm number is firm and buys nothing on its own. **The table is here to show that, not to
  propose a figure**; the four densities are Claude's, chosen to span, and none of them is a claim
  about this tissue. *(The volume is Class 1. The arithmetic is computed. The densities are Class 2 —
  Claude's construction, and explicitly not candidates.)*

  **The volume is about the size of a single functional magnetic-resonance-imaging voxel** — 30–36 mm³
  against a 3 mm isotropic voxel's 27 mm³, so **1.1 to 1.3 voxels.** The structure that closes the
  value-brake loop sits at the resolution limit of the instrument that would image it in a living
  subject.

- **Shape.** **Non-laminated nucleus, rank 2: (division, N)**, with the division axis at **extent 2**
  and both members named — the only fully-populated shape axis in the section. Below it, the subnuclei
  of each division are described in the literature and not named here, so **the next axis down is
  owed**. N is to derive.
  **Cell-class axis: not applicable at the structure level and unknown below it** — the transmitters
  are named per division (cholinergic / substance-P; glutamatergic) rather than per cell class, so the
  division axis is carrying the transmitter distinction.

- **Edge latency.** All 12 edges **to derive.** **Both carrying tracts have no entry** (§3d).

- **Invariant conformance.** Co-instantiation: **satisfiable for the lateral limb** and its onward path
  through the rostromedial tegmental nucleus, subject to §1a; **not satisfiable for the medial limb**,
  whose only input and only output are regions with no entry anywhere. Below the structure level,
  **unstatable** — no internal edge, and whether the two divisions communicate is unestablished.
  Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** **The section's headline structure is 30 mm³ and it is a
  sign-inverter for the whole reward system.** The arithmetic that matters is not memory, it is
  leverage: a structure of order one imaging voxel sits astride the input to a dopamine population
  that file 9 puts at 400,000–500,000 cells per side, and its output is *excitatory* onto a relay whose
  job is to **invert the sign**. **The habenula does not brake dopamine; it excites something that
  does** — and that indirection is the mechanism, stated positively, with the inversion attributed to
  the correct stage.
  **This is the one place in the section where the payload's sign is load-bearing and stated**, and it
  is the same finding file 09 made against the forward model, arriving from the other side: there,
  inhibition was the mechanism and the model had no term for it; here, an **excitation that becomes an
  inhibition one stage later** is the mechanism, and a count of active inputs cannot represent either
  half.
  The second justification is about what the structure is for. **A negative reward-prediction error is
  not the negation of a positive one — it is a separate line with its own anatomy**, its own tract, its
  own relay and its own transmitter. The description could have made worse-than-expected a sign on the
  dopamine wire and did not. **That is an architectural claim about representation: the brain spends a
  nucleus, two tracts and a relay to keep the bad news on its own line.**

---

## 7. Midcingulate cortex — the action–outcome / cingulate-motor hub

- **Function → structure.** The dorsal-cingulate "doing" zone between the emotional anterior cingulate
  and the mnemonic posterior cingulate — the hub linking **reinforcement outcomes to action**. Its
  anterior part is where **negative affect, pain and cognitive control overlap**: effortful,
  feedback-mediated decision-making, conflict, and the drive to adjust behaviour. It houses the
  **cingulate motor areas**, projecting onto supplementary and premotor fields and the primary motor
  cortex, **so this structure is output-capable, not just a monitor.** On the action–outcome reading,
  the anterior cingulate supplies reward / non-reward outcome, the posterior cingulate supplies action
  / spatial information, and the **midcingulate motor area turns their convergence into a motor plan.**

  **Sub-elements: the "prime" midcingulate fields plus two motor areas.** **Area 24′** (with a′, b′ and
  c′ divisions) and **area 32′**, together with the **rostral cingulate motor area** and the **caudal
  cingulate motor area**, which are the output-capable sectors and are already named on the motor
  edges. An **anterior / posterior midcingulate** division is used by the Function slot.

  **The standard laminar block is not transcribed**, and correctly: this tissue is **agranular to
  dysgranular** across its extent.

  **Internal edges: owed** — the sub-elements are named and no edge between them is typed. **And the
  entry's stated function is exactly an internal edge.** *Convergence turned into a motor plan* is a
  transfer from the fields that receive outcome and action onto the motor areas that emit, and **that
  transfer is not written.** The structure's whole claim is the step the slot does not contain.

- **Inputs.** Seven edges.
  - **← anterior cingulate cortex** (`11_frontal_lobe`) (reward / outcome) — a **scalar reward-value
    signal**: expected
    reward magnitude, and a response to the mismatch between expected and received reward — firing to
    unexpected reward and to expected-but-omitted reward. **It has a coordinate frame — a scalar value
    axis — whose zero and slope are set by bodily and motivational state, so the frame is
    body-relative.** Fan-in: to derive. **Two-ended and confirmed 2026-08-13.** *(The payload is
    verified for the source at the producer and the body-relative reading is marked Class 2 there;
    the caution is carried here. **The two ends are copies, so their agreement certifies that the
    payload crossed the file boundary intact, not that two derivations met.**)*
    **This is the only edge in the section with a stated coordinate frame**, which is one of the three
    things a payload is supposed to carry.
  - **← amygdala** (`08_medial_temporal_lobe`) — the **valence tag**, carrying no identity
    information. Fan-in: to derive. **Two-ended across a file boundary, and confirmed on 2026-08-13**:
    the producer declares this target inside the same five-edge compound that carries the insular
    limb, and types it identically. *(Two of that compound's five consumers are entries in this file
    and both now declare it; the other three are in file 11 and are unchecked.)*
  - **← anterior insula** — the **salience / affect signal**; payload otherwise owed. Fan-in: to
    derive. *(In this file; both ends in one pass.)*
  - **← posterior parietal cortex** (`06_posterior_parietal`) — payload owed. Fan-in: to derive.
    **A class. Checked 2026-08-13 and no producer was found**: all five entries in that file were read
    and none declares an output to this one. *(One of three identical class endpoints in this section —
    §2, where the consequence is recorded: the file the candidates were located in has been checked and
    is empty of them.)*
  - **← posterior cingulate cortex** (action / spatial) — payload owed. Fan-in: to derive. **The
    producer is an entry in this same file and does not declare it** (§3b).
  - **← midline and intralaminar thalamus** — payload owed. Fan-in: to derive. **The producer declares
    its cortical target as a class** — *striatum (major) and cortex (diffuse)* — covering this region
    without naming it. *(Owed at file 12.)*
  - **← mediodorsal thalamus** — payload owed. Fan-in: to derive. *(File 12, not confirmed.)*

  **← the cingulum** is recorded as **routing, not an edge**, and is not counted.

- **Outputs.** Six edges.
  - **→ supplementary and pre-supplementary motor areas and premotor cortex** (`11_frontal_lobe`), via
    the **cingulate motor areas** — payload owed; at this end it is *the convergence of reward or
    non-reward outcome with action and spatial information, turned into a motor plan*. Fan-out: to
    derive. **Two-ended and confirmed 2026-08-13**: the consumer names the same route in the same
    words and **carries the edge untyped**, so the payload above exists at this end only.
  - **→ primary motor cortex**, via the **cingulate motor areas** — payload owed. Fan-out: to derive.
    *(File 5, not confirmed.)*
  - **→ anterior cingulate cortex** (`11_frontal_lobe`), reciprocally, via the **cingulum** — payload
    owed. Fan-out: to derive. **Two-ended and confirmed 2026-08-13; owed at both ends**, and the
    consumer names the same route. **With the inbound reward edge above, this is the only relationship
    between the two files that is complete at both ends in both directions.**
  - **→ posterior cingulate cortex**, reciprocally — payload owed. Fan-out: to derive. *(In this file;
    both ends in one pass.)*
  - **→ basal ganglia** — payload owed. Fan-out: to derive. **A class**: the striatal target is likely
    and is not stated. *(`09_basal_ganglia`. **Checked against the file in hand**: that file's cortical
    input line names the midcingulate cortex among the five cortical entries declaring an output to it,
    quoting *"basal-ganglia and brainstem autonomic targets"* — **which is this entry's own compound
    line, so the far end confirms the edge exists and inherits the same unresolved target.** Naming the
    nucleus is owed here first.)*
  - **→ brainstem autonomic targets** — payload owed. Fan-out: to derive. **A class**; file 14 holds
    the candidates — periaqueductal gray, solitary nucleus, rostral and caudal ventrolateral medulla —
    and none was confirmed.

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, paralimbic association cortex,
  uncounted per-region in human. **Grey-matter volume, white-matter volume, synapses, axons,
  myelination: all unknown.** **Not one figure in the entry, and no cross-check runnable.**

- **Shape.** **Agranular-to-dysgranular cortex: a laminar axis that exists and is not the standard
  one, and is not written.** The block is inadmissible and no replacement is given, so **the layer axis
  is owed rather than unknown** — the tissue's lamination is described qualitatively (agranular to
  dysgranular) and its sub-elements are named, and only the edges between them are missing.
  The tangential axis has **four named members** — 24′, 32′, and the rostral and caudal cingulate motor
  areas — plus 24′'s three subdivisions a′, b′, c′, giving a partially-populated second level. **No
  extent, no boundaries, no pitch.**

- **Edge latency.** All 13 edges **to derive.**

- **Invariant conformance.** Co-instantiation: satisfied in form at the structure level; **internally
  unstatable, and the unstatable part is the entry's stated function.** One input's producer is an
  entry in this same file and does not declare the edge (§3b). Per-edge latency: satisfied in form, all
  to derive.

- **Justification (biological).** **This entry is the section's convergence node and it is the one
  whose inputs are best typed** — a scalar reward value with a body-relative frame from the anterior
  cingulate, a valence tag from the amygdala, a salience signal from the insula. **Three typed inputs,
  a stated computation, and an untyped output**, which is the reverse of the claustrum's shape and is
  the more tractable failure: the ingredients are named, so what leaves is a question about the
  operation rather than about the whole structure.
  **The architecture's contribution is to name what the operation must do to the frames.** A scalar
  value axis, a valence gain, and a salience flag arrive; a motor plan leaves. **A motor plan has a
  body-centred frame and the value signal has a body-relative scalar one, so the operation is not a
  combination within a frame — it is a change of frame from value to action**, and that is precisely
  what the action–outcome reading claims the structure is for. **The edge that would carry it is the
  internal one that is owed.** *(Class 1 for the payloads and the reading of the structure's function;
  Class 2 for the frame-change formulation, which is Claude's and is offered to be checked.)*

---

## 8. Posterior cingulate cortex — default-mode hub

- **Function → structure.** A core hub of the **default-mode network** and part of the brain's
  structural connectivity core — internally-directed cognition, self-reference, autobiographical
  memory, and regulation of the balance between internal and external attention. **It is not
  homogeneous.** The **ventral** sector is tied into the default-mode network proper and the medial
  temporal lobe / hippocampus; the **dorsal** sector connects additionally to the fronto-parietal
  cognitive-control and attention networks and helps modulate the switch between internal and external
  focus. Its neurons track decision variables and exploratory choice. **It usually deactivates as
  externally-focused task demand rises** — the signature default-mode response.

  **Sub-elements: two, and they meet the test.** **Dorsal posterior cingulate cortex** (area 23d and
  area 31) and **ventral posterior cingulate cortex** (areas 23a and 23b). They **project to different
  targets** — ventral to the default-mode partners and the medial temporal lobe, dorsal additionally to
  the fronto-parietal control network — and the entry's Function slot and output edges are already
  written on the division.

  **This is granular isocortex, so the standard laminar block is admissible here — and it is still not
  transcribed**, because the entry's own laminar description has not been read against it. **That is
  the correct order.** The block is a claim, and checking it against the entry is part of writing the
  slot, not an optional refinement. **Of the four cortical structures in this section, this is the only
  one that could take the block, and none of the four has it.**

  **Internal edges: owed — including, specifically, whether the dorsal and ventral sectors are
  connected to each other, which is what a switch between internal and external focus would need.**

- **Inputs.** Six edges.
  - **← hippocampal formation** (`08_medial_temporal_lobe`) — the **completed episode**: the bound,
    retrievable pattern, **addressable by any fragment of itself**. **Payload only partly writable —
    owed:** an episode has no units and no frame, and what makes it checkable is a **property** rather
    than a type, namely content-addressability. Fan-in: to derive. *(Typed from the producer's
    declaration.* **Two-ended and confirmed on 2026-08-13**, *and the confirmation discharged a mark
    at the far end: the producer's output line read* both untyped there, *which this line and the
    retrosplenial one below make false. The producer declares no sub-element on its side of this edge,
    so nothing here says which hippocampal field it leaves from.)*
    **This is a fourth payload shape the section carries**: not a name, not a partial type, not a
    stated absence, but **a property in place of a type.**
  - **← anterior cingulate cortex** (`11_frontal_lobe`) — payload owed. Fan-in: to derive. **The
    producer declares no such edge. Checked 2026-08-13 and confirmed absent.** **This is the third of
    three edges that structure owes this section**, alongside the insula's return arm and the
    habenula's cortical brake limb. **One structure is a named producer to three of this file's six
    entries and declares an output to none of them**, while carrying four outputs in total — **so what
    looked like three unrelated gaps is one Outputs slot three edges short**, and no single entry here
    could have seen that. **Owed at `human_brain_11_...`.**
  - **← midcingulate cortex** — payload owed. Fan-in: to derive. *(In this file; both ends in one
    pass.)*
  - **← precuneus** (`06_posterior_parietal`) — payload owed. Fan-in: to derive. **Two-ended and
    confirmed 2026-08-13, and this file's own mark is withdrawn**: it read *not confirmed to declare
    the return limb*. **The producer declares it**, as `→ the posterior cingulate cortex`, payload
    unknown and owed. **The reciprocal pair with that structure is closed and both limbs are untyped**
    — a different state from the pair being open, and one no amount of further reading will improve.
  - **← posterior parietal cortex** (`06_posterior_parietal`) (action / spatial) — payload owed.
    Fan-in: to derive. **A class, checked 2026-08-13 and no producer found** — see §2. **This entry is
    the one of the three where the check is least empty**, because that file's precuneus does declare
    an output here; **but it is declared by name above and is not what the class was standing in
    for.**
  - **← anterior thalamus** — payload owed. Fan-in: to derive. **The producer declares no such edge**:
    its anterior nuclei name the retrosplenial cortex and the anterior cingulate cortex as their
    cortical targets, not this region. **So the posterior-cingulate limb of the classical limbic
    thalamic projection is unconfirmed at its producer.** *(Owed at file 12.)*

  **← the cingulum** is **routing, not an edge.**

- **Outputs.** Five edges, **all payloads owed.**
  - **→ hippocampal formation** (`08_medial_temporal_lobe`) — payload owed at both ends. Fan-out: to
    derive. ***Written by name now, the class it was hidden in gone, and the payload still owed —
    naming the consumer is not typing the edge.*** **Two-ended and confirmed on 2026-08-13**: the
    consumer declares `← posterior cingulate cortex` and marks it *untyped there*, **which is accurate
    — this line is the untyped one.** *(The only far-end mark in that file pointing here that survived
    the diff unchanged.)*
  - **→ precuneus** (`06_posterior_parietal`) — payload owed at both ends. Fan-out: to derive.
    **Two-ended and confirmed 2026-08-13**, the consumer marking it *declared and untyped at the
    producer*, which is accurate.
  - **→ angular gyrus** (`06_posterior_parietal`) — payload owed. Fan-out: to derive. **Two-ended and
    confirmed 2026-08-13, and this file's own mark is withdrawn**: it read *not confirmed*. **The
    consumer declares it**, and lists it beside its inputs from the precuneus and medial prefrontal
    cortex — **the same three-edge default-mode grouping this entry's own output slot makes, arrived
    at from the other side.**
  - **→ orbitofrontal / ventromedial prefrontal cortex** (`11_frontal_lobe`), the medial-prefrontal
    default-mode partner — payload owed. Fan-out: to derive. **Two-ended and confirmed 2026-08-13, and
    this file's own mark is withdrawn**: it read *not confirmed*. **The consumer declares it**, marks it
    *medial*, and sorts it with the precuneus and angular gyrus into a default-mode group it
    distinguishes from that structure's orbital business. **So this end's *medial-prefrontal* qualifier
    and that end's *medial* sorting are two independent arrivals at the same split**, in a structure
    whose own file records the split as owed and unadopted. **That is the one agreement in this pair
    that is not a copy.**
  - **→ cognitive-control network**, via the **dorsal posterior cingulate cortex** — payload owed.
    Fan-out: to derive. **A network endpoint, and the source states it is not repairable by naming the
    members.** *(§2.)*

  **The first four were split out of a single network endpoint that also listed four members**, and the
  split was defensible only because two of the far ends had already declared the edge from their own
  side. **The residual network endpoint was not split, because no far end declares it and naming
  members would manufacture the arity.** So this entry carries **both** halves of the network question,
  worked and refused, in one Outputs slot.

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, association cortex, uncounted
  per-region in human. **Everything else unknown. No cross-check runnable.**

- **Shape.** **Granular isocortex — the only structure in the section whose laminar axis could be
  written from the standard block, and it is not written.** Layer axis therefore **owed, not
  unknown**: the block exists and the check that would license it has not been run.
  Tangential axis: **two named sectors** (dorsal: 23d, 31; ventral: 23a, 23b), each resolving to named
  areas, so this is the **best-populated tangential axis in the section** — two levels, all members
  named. **No extents, no boundaries, no pitch.**

- **Edge latency.** All 11 edges **to derive.** **And the entry's function is a switch** whose duration
  is not given (§3c).

- **Invariant conformance.** Co-instantiation: satisfied in form at the structure level; **internally
  unstatable, and the missing internal edge is the one the stated function requires** — a switch
  between internal and external focus needs the dorsal and ventral sectors connected, and whether they
  are is owed. One input's producer is an entry in this same file and does not declare the edge (§3b).
  Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** **This entry's distinctive fact is a negative and it is not on any
  edge.** The structure *deactivates* as externally-focused task demand rises. That is a statement
  about a **baseline** — the structure has a resting level from which it is driven **down**, which is
  the same representational shape as the basal ganglia's tonic inhibition and the insula's
  content-free corticothalamic gate. **Three structures in two sections now carry a payload whose
  informative event is a decrease, and none of the three has a way to say so in the slot.**
  The second point is about the two sectors. **The division is written on the outputs and the input
  side does not use it**: not one of the six incoming edges says which sector it lands on, while three
  of five outgoing edges are attributed by sector. **A structure whose function is switching between
  two regimes needs to know which regime the input belongs to**, and the description assigns sectors
  only on the way out. *(Class 1 for the deactivation and the sector attributions; the reading that the
  input side does not use the division is a count over the entry, and the significance placed on it is
  Class 2.)*

---

## 9. Retrosplenial cortex — the spatial / Papez node

- **Function → structure.** A small cortical strip behind the splenium of the corpus callosum, central
  to **spatial navigation and memory** — translating between **egocentric (viewpoint) and allocentric
  (world / map) reference frames**, anchoring **head-direction** and landmark information, and
  supporting **scene construction** and the spatial-contextual side of episodic and autobiographical
  memory. **It fuses internal self-motion cues — vestibular, proprioceptive, motor efference — with
  external visual landmarks** to keep heading current. Its connectional signature, reciprocal with the
  hippocampal formation, parahippocampal region, anterior limbic thalamus and parietal cortex, is
  conserved across mammals. **One of the first regions to show Alzheimer pathology.**

  **Sub-elements: two, and the division is architectonic and is in the entry's own heading.** **Area
  29**, granular, and **area 30**, dysgranular.

  **The standard laminar block is not transcribed**, and correctly: the entry **spans a granular /
  dysgranular internal border**, so one block would assert a layer-4 circuit across tissue that has
  layer 4 on one side and not the other.

  **Internal edges: owed — and so is the prior question of whether areas 29 and 30 project to different
  targets**, which is the test for a sub-element as against a property. **This is the only entry in the
  section whose sub-element division is not yet established as one.**

- **Inputs.** Five edges.
  - **← hippocampal formation** (`08_medial_temporal_lobe`), from the **subiculum** — the **completed
    episode**, addressable by any fragment of itself; payload only partly writable — owed. Fan-in: to
    derive. *(Typed from the producer.* **Two-ended and confirmed on 2026-08-13**, *and it discharged
    the same* both untyped there *mark as the posterior-cingulate limb above.)*
    **An arity asymmetry sits on this edge and the producer does not carry it.** This end names the
    **subiculum**; the producer's line attributes the output to the hippocampal formation whole and
    bundles this edge with the posterior-cingulate one in a single bullet. **So the sub-element
    endpoint exists at this end only**, and whether both edges leave the subiculum or only this one is
    **owed at the producer**. This is the design file's finer-at-one-end case, arriving here in the
    direction the far file's own inferotemporal-to-lateral-nucleus edge already met from the other
    side.
  - **← anterior thalamic nuclei** — payload owed. Fan-in: to derive. *(File 12, which names this
    region as the anterior-thalamus limb of the Papez circuit. Two-ended, owed at both.)*
    **A specific gap sits under this edge and it is the entry's headline input.** The **head-direction**
    signal the Function slot depends on is classically carried by **one division** of the anterior
    nuclei rather than by the group, and that entry records its own divisions as unnamed and owed.
    **Until they are named, the entry's headline input cannot be written as an edge from the division
    that carries it.** This is the arity problem the source design describes, arriving from the far
    end: naming the producer's sub-elements will split this edge.
  - **← parahippocampal cortex** — payload owed. Fan-in: to derive. **This producer has no entry in any
    of the twenty files**, and is named as a producer by three other files as well. *(§2, and it is the
    stage the Papez return arm runs through — §3a.)*
  - **← posterior parietal cortex** (`06_posterior_parietal`) — payload owed. Fan-in: to derive.
    **A class, checked 2026-08-13 and no producer found** — see §2.
    **The check bears on this entry's dangling requirement below.** The parietal class was one of three
    places the self-motion half of the fusion might have arrived from. **It is now excluded**, leaving
    the anterior thalamic head-direction signal — whose producing division is itself unnamed — or a
    producer no file has named. **The gap is unchanged in size and better located.**
  - **← visual areas** — payload owed. Fan-in: to derive. **A class**, and it is the edge that would
    supply **half of what the region is said to fuse**. The medial parieto-occipital candidates that
    would most plausibly supply it are themselves regions the source names on edges and does not
    describe.

  **← the cingulum** is **routing, not an edge.**

  **Dangling requirement — the self-motion half of the fusion, and it is the largest gap in the
  entry.** The Function slot fuses **internal self-motion cues (vestibular, proprioceptive, motor
  efference)** with **external visual landmarks**, and **no incoming edge declares any of the three
  self-motion cues.** Whether they arrive by way of the anterior thalamic head-direction signal, the
  parietal class endpoint, or a producer not yet named is not stated. **Both halves of the fusion the
  entry exists to perform are undeclared at their sources** — the visual half by a class endpoint, the
  self-motion half by nothing at all.

- **Outputs.** Three edges.
  - **→ hippocampal formation** (`08_medial_temporal_lobe`), via **parahippocampal and entorhinal
    cortex** — the **return arm of the spatial-memory loop**: heading and landmark information
    **after the egocentric-to-allocentric translation this region performs.** Payload otherwise owed.
    Fan-out: to derive. **Two-ended and confirmed on 2026-08-13, and it is the strongest agreement in
    the pair**: the consumer declares it in near-identical terms, names the same two-stage route, and
    was written from its own side rather than copied from this one. **The route runs through a region
    with no entry** — §3a — **and both ends say so independently**, which makes the gap a finding of
    two files rather than a note in one.
  - **→ anterior thalamic nuclei** — payload owed. Fan-out: to derive. **The consumer records this edge
    as one it does not carry**: its Inputs slot has no cortical line at all, and it marks the reciprocal
    limb owed at that end. **Two-ended in intent only.**
  - **→ precuneus** (`06_posterior_parietal`) — the **return arm of the spatial-memory loop**, in the
    same terms. Payload otherwise owed. Fan-out: to derive. **Two-ended and confirmed 2026-08-13**, and
    the consumer records this as the one incoming edge that could supply its headline
    visuospatial-imagery function. **That consumer had described the edge as untyped at both ends and
    it is not** — both ends carry the same partial type and both mark the remainder owed; the
    description was corrected there. **This is the second of this entry's two outputs to be confirmed
    two-ended, and both are limbs of the same spatial-memory loop**, to the hippocampal formation and
    to here.

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, a small granular / dysgranular
  peri-allocortical strip, no clean human per-region count. **Everything else unknown. No cross-check
  runnable.**

- **Shape.** **Cortex spanning a granular / dysgranular border: two layer sets, one structure.** The
  layer axis is **not one axis** and the block cannot be written across it — the same state as the
  insula's, arriving by a border rather than by a gradient.
  Tangential axis: **two named members**, area 29 and area 30, **whose status as sub-elements is
  itself owed.** **No extents, no pitch.**

- **Edge latency.** All 8 edges **to derive.**

- **Invariant conformance.** Co-instantiation: **not satisfiable for the Papez return arm**, which runs
  through parahippocampal cortex; **internally unstatable**, and the sub-element division is not
  established. Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** **This is the one entry in the section whose function is a stated
  transformation with named input and output frames**, and it is worth more than the payloads it
  carries. Egocentric in, allocentric out. **That is a coordinate-frame conversion — the property a
  payload is supposed to declare — named at the structure level and absent from every edge.** The
  output edges say *after the egocentric-to-allocentric translation this region performs*, which
  declares the frame of what leaves by reference to an operation rather than by stating it.
  **So the architecture can say what this structure's shape must be even though none of its numbers
  exist**: it must hold two representations of the same content in two frames, and the operation
  between them is a transform, not a selection or a gain. **That constrains the internal edges that are
  owed more tightly than any other entry in the section constrains its own.**
  **And it is undercut by the input side.** A frame conversion needs the self-motion signal to define
  the transform, and **no edge declares one.** The entry states the output frame precisely and does not
  declare the quantity the conversion runs on. *(Class 1 for the frames and the fusion claim; the
  reading that this constrains the owed internal edges is Class 2 — Claude's, offered to be checked.)*

---

## 10. Section totals

**Every cell that would carry a number is *to derive*, and that is the total.**

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Insula | per hemisphere | to derive | ≤ 16 | to derive |
| Claustrum | per hemisphere | to derive | ≤ 16 | to derive |
| Habenula | per side | to derive (volume 30–36 mm³) | ≤ 16 | to derive |
| Midcingulate cortex | per hemisphere | to derive | ≤ 16 | to derive |
| Posterior cingulate cortex | per hemisphere | to derive | ≤ 16 | to derive |
| Retrosplenial cortex | per hemisphere | to derive | ≤ 16 | to derive |
| **stated total** | **per hemisphere** | **to derive — six of six** | ≤ 16 | **to derive** |

**16 bits is the log₂ ceiling and it is doing all the work**, as it did in file 09: fan-in is unknown
on all 76 edges, so the width is a cap rather than a measurement. **Unlike file 09 there is nothing for
the cap to multiply.**

**Three different count states, three different repairs, and separating them is the useful output of
this table.**

| state | structures | what the repair is | cost |
|---|---|---|---|
| **uncounted tissue class** — association / paralimbic cortex, uncounted per-region in human | insula, midcingulate, posterior cingulate, retrosplenial | a per-region human stereology programme for association cortex, which does not exist for any of them | **one repair, four structures** — and it reaches beyond this section, to prefrontal and inferior-parietal cortex, which the source names in the same breath |
| **segmentation-limited** | claustrum | a segmentation method for a thin sheet; the volume is soft for the same reason the count is | one repair, one structure, and it is a method question rather than a measurement one |
| **measured, but not as a control absolute** | habenula | human stereology exists and reports volumes and disease-related changes; the repair is to obtain or convert a control absolute | **the cheapest repair in the section**, and probably a matter of reading a table that exists |

**The three states are not degrees of the same thing.** *Uncounted tissue class* says nobody counts
this kind of tissue this way; *segmentation-limited* says the boundary cannot be drawn; *measured but
not as an absolute* says the measurement was taken and reported as something else. **Only the third is
close to money**, and it is the structure whose output closes a loop into three other files.

**No density cross-check can be run anywhere in the section** — the arithmetic file 09 ran on the
striatum needs a count and a volume, and no structure here has both. **The habenula has the volume and
not the count**, which is why the table in §6 runs the arithmetic backwards and shows only how much
the missing density is worth.

**State memory and edge storage are not in this table**, and edge storage cannot be sized until the
scheduling discipline is set, which it is not. **The claustrum is the one structure in the project so
far where edge storage would plausibly dominate the parameter store** — a near-all-to-all cortical
projection on exceptionally far-reaching axons — and it is the one whose topology is furthest from
being stateable.

**Memory is not a binding constraint here and no figure is to be reduced.** There are no figures.

---

## 11. A measurement of the file itself, and it disagrees with two records

Run because the source design assigns the size column the job of a **checksum**, and a checksum is
only worth having if it is read.

**Re-run on 2026-08-13, after the `08_medial_temporal_lobe` pass. The figures below are the current
ones; the 2026-07-28 figures are kept beside them because the comparison is what the section is for.**

| quantity | 2026-07-28 | after `08` | after `11` | after `06` |
|---|---|---|---|---|
| bytes | 62,454 | 85,837 | 90,620 | 94,260 |
| non-blank lines | 649 | 985 | 1032 | 1069 |
| tokens, at bytes ÷ 4 | 15.6k | 21.5k | 22.7k | 23.6k |
| kB at ÷1024 | 60.99 | 83.83 | 88.50 | 92.05 |
| kB at ÷1000 | 62.45 | 85.84 | 90.62 | 94.26 |

**The measurement is a fixed point, and that is worth stating because it is not obvious.** Writing the
byte count into the file changes the byte count, so the figures above were iterated until re-measuring
reproduced them — two rounds. **A file that measures itself has to converge or it lies**, and the
2026-07-28 run did not say which it had done.

**A cross-file pass costs a third of the file's size in prose, and that number was not predicted
anywhere.** Twelve edges were diffed and not one was added or removed; the growth is entirely the
record of what the diff found. **Whether that is the right price is Micky's to judge**, and it is
recorded here rather than argued because §11 exists to measure the file, not to defend it.

- **The 2026-07-28 unit finding still stands and is worth keeping**: the file header said 62 kB and the
  map row said 60 kB, and both were right on different units — 62,454 ÷ 1024 = **60.99** against
  62,454 ÷ 1000 = **62.45**. **The ratio is 1.024**, the 2.4% one-directional discrepancy the source
  design predicts by name for exactly this cause, and the map's unit is the declared one.
- **The source design's map row for this file is now stale by construction**, since the file grew.
  **Owed: regenerate the map row, or record that the map is regenerated on its own schedule.**
- **Edge lines: 74 inter-region, 2 internal, plus 3 tract-routing statements that are not edges.**
  **The file's header gives no edge count**, unlike file 9's, which gives *27 — 16 in, 11 out.* The
  source design's own §9 records this file's conversion as producing **62 typed edges**, against **74**
  measured here. **Neither the five-converted-entries subtotal (53) nor the whole-file total (74) is
  62**, so the two figures do not reconcile by any grouping tried.

**Not repaired, and the disagreement is the point.** A second independently-derived record of the same
quantity is the mechanism that caught the superseded copy of file 11, and smoothing to the nearer
number would destroy the signal. **Recorded as measured; which figure is right is the source's to
settle.** *(All figures Class 1 — computed from the file in hand. The reading that the kB gap is a unit
mismatch rather than an error is Class 2, though the arithmetic is exact.)*
