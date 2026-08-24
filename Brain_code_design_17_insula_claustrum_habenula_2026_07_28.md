# Brain code design — 17 insula, claustrum, habenula, cingulate remainder

**Date:** 2026-07-28
**Derived from:** `Brain_architecture_17_insula_claustrum_habenula_2026_07_28.md` — six entries, in its
order: insula, claustrum, habenula, midcingulate cortex, posterior cingulate cortex, retrosplenial
cortex.
**Rung spec:** `brain_code_design_spec_2026_07_28.md`.
**Implements:** `Brain_17_insula_claustrum_habenula.py`.

**No history in this document.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live. The same rule binds the code file's header, and a comment
is updated in the same edit as the code it describes.

**Standalone, not a companion.** Every contract field below is carried verbatim from the architecture
entry. At coding time this file is loaded and the architecture file is not.

**Far ends were not read.** Edges leave into files 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 13 and 14. Each edge
carries the file its far end sits in and the state of that far end's declaration, as the architecture
records it. No far end's content is written from memory.

---

## 1. Section preamble — what is true across all six entries

Carried here rather than repeated six times. Nothing in this section is a design entry; the entries
begin at §2.

### 1a. Counting basis, and three count states that are three different repairs

Basis is **per hemisphere** for five structures and **per side** for the habenula, a bilateral midline
nucleus. **No structure in the section carries a neuron count.** Nine sub-element groupings, no count
anywhere, so **the section sizes zero of nine**.

The architecture separates three states beneath the single word the source uses. The source's own slot
reads *soft / unknown* in all six cases; the three-way separation is a **reading placed on it, not a
copy of it**, and both are carried so the refinement cannot absorb the original:

| structure | source slot | state | volume | cross-check |
|---|---|---|---|---|
| insula | soft / unknown | uncounted tissue class | sizeable, no verified figure | none runnable |
| claustrum | soft / unknown | segmentation-limited | thin sheet, soft, segmentation-dependent | none runnable |
| habenula | soft / unknown | measured, not as a control absolute | **30–36 mm³ per side** | none runnable — no density |
| midcingulate cortex | soft / unknown | uncounted tissue class | unknown | none runnable |
| posterior cingulate cortex | soft / unknown | uncounted tissue class | unknown | none runnable |
| retrosplenial cortex | soft / unknown | uncounted tissue class | unknown | none runnable |

*Uncounted tissue class* says nobody counts this kind of tissue this way in human — **one repair covers
four structures**, and it reaches past this section to prefrontal and inferior-parietal association
cortex. *Segmentation-limited* says the boundary cannot be drawn: a method question, not a measurement
one. *Measured but not as a control absolute* says the measurement was taken and reported as something
else — **the cheapest repair in the section**, and it is the structure whose output closes a loop into
files 9, 13 and 14. *(The three-state separation is Claude's reading, offered to be checked. The slot
contents are Class 1 from the source.)*

### 1b. Edges — declarations against distinct edges, and the count the code needs

**76 edge declarations: 74 inter-region and 2 internal.** Three tract-routing bullets — *← the
cingulum*, at the midcingulate, posterior cingulate and retrosplenial entries — are **not edges**; the
cingulum has an entry in file 18 as transmission without processing, so its traffic belongs to the
cingulate edges themselves. The reconciliation is **44 in-bullets + 33 out-bullets − 3 routing = 74**,
and the per-entry totals sum to 76.

**Distinct edges are 73, not 76, and this is the figure the edge-storage arithmetic runs on.** Three
inter-region edges carry **two declarations each**, because both of their endpoints are entries in this
file: insula → midcingulate cortex, insula → lateral habenula, and midcingulate → posterior cingulate
cortex. **74 declarations − 3 duplicates = 71 distinct inter-region edges, plus 2 internal = 73.**
Sizing in-flight values on 76 would double-count three lines. *(Computed from the source's own edge
bullets; the duplicate identification is Claude's and is checkable line by line.)*

**33 of the distinct edges are produced inside the section** and are sized at their producer's entry
below. One more — posterior cingulate → midcingulate — is produced in-section and declared only at its
consumer (§1c). The remainder arrive from outside and are sized at their producers, in other files.

**Payload states: 49 of the 74 declarations are fully owed** — the slot reads *payload unknown — owed*
and nothing else. Within the 25 that carry content, four shapes are kept apart because they are four
different distances from a type:

- **a name only** — *the salience signal*, *a bad-outcome expectation*, *interoceptive state*.
- **a partial type** — *taste quality and intensity*; *head rotation rate and gravito-inertial
  acceleration*; *the body's physiological condition, somatotopically ordered*.
- **a stated absence** — *no stimulus content; the driver / modulator gate*. What makes it checkable is
  what it does **not** carry.
- **a property in place of a type** — the **completed episode**, *addressable by any fragment of
  itself*. No units, no frame; content-addressability is what makes it checkable.

### 1c. Endpoint kinds, and the class families

| kind | count |
|---|---|
| named region with an entry | 59 |
| named region with **no entry anywhere** | 3 |
| a **class** | 11 |
| a **network** | 1 |
| *(tract routing — not an edge)* | *3* |

**The three entry-less regions are not scattered.** The **septal nuclei** and the **interpeduncular
nucleus** are the medial habenula's only input and only output; neither has an entry in any of the
twenty files, and the string *interpeduncular nucleus* appears nowhere else in the source. The third is
**parahippocampal cortex**, which is also the stage the Papez return arm runs through.

**The eleven class endpoints resolve to seven decisions, not eleven problems**, and **three of the
seven are repeated families covering seven of the eleven endpoints** — which is where the saving is:
one decision, several edges. *the posterior parietal cortex* three times with the same candidate
producers in file 6; *the cerebral cortex, near all-to-all* twice, in and out of the claustrum; *the
cingulate cortex* twice, likewise; and four singletons — *neuromodulatory afferents*, *the basal
ganglia*, *brainstem autonomic targets*, *visual areas*. **Three families plus four singletons is
seven**, and the count is derived in the module rather than carried.

**Four far ends inside this file do not declare the edge pointed at them** — the posterior cingulate at
the midcingulate's input, and the three in-file cingulate entries at the claustrum's two cingulate
class endpoints. **This is the cheapest repair in the section and it is not done**; no other file needs
opening.

**Of 24 declarations marked two-ended, five state in the same breath that both ends were written in one
pass** and therefore certify nothing. The agreements that do certify something cross a file boundary
and a date: the amygdala's valence tag from file 8, the anterior cingulate's scalar reward value from
file 11, the completed episode from file 8, the rostromedial tegmental and raphe limbs from files 14
and 13.

### 1d. Tracts

Four are named; **two have entries and two do not.** The **cingulum** has one in file 18 and is used
correctly as routing. The **stria medullaris** (all habenular input) and the **fasciculus retroflexus**
(all habenular output) have none — **so the entire habenular traffic, both divisions, both directions,
rides on tracts the source does not describe**, and a tract is where the physical substrate of a
latency lives. The **external and extreme capsules** are named as the claustrum's myelination context,
not as carriers.

### 1e. Two findings against the model, and both are narrower than a section-wide one

**A non-directed coupling, which an `Edge` cannot represent.** The claustrum's internal organisation
includes a **gap-junction-coupled GABAergic interneuron network**, which the source records as an
electrical coupling among interneurons rather than a directed synapse, and for which it has **no
convention**. An `Edge` has a source and a target; a gap junction has neither, or both symmetrically
and simultaneously. Writing it as two directed edges asserts two transfers where there is one coupling
and gives it a latency in each direction where the physical claim is that there is effectively none.
**Recorded, not worked around**: the module carries a `Coupling` record that is deliberately not an
`Edge`, so it cannot be counted as one or scheduled as one.

**A payload that may be purely temporal, which the slot has no shape for.** Every one of the
claustrum's four candidate functions — binding, synchronisation, network switching, slow-oscillation
control — is a claim about **when** distributed activity is aligned, not about **what** is on the line.
A payload slot asks for a property, its units or quality, and its coordinate frame; **a signal whose
entire content is a time of arrival has none of the three and is not thereby empty.** The payload is
owed, so nobody knows that it is purely temporal; what is known is that all four hypotheses would make
it so. The module records the hypotheses as four claims about one untyped edge and reports the count.
*(Class 2 — Claude's reading of the source's Function slot. No source was opened for it.)*

### 1f. What is unset above this rung, and what that blocks here

| needed for | item | state |
|---|---|---|
| sizing anything at all | neuron counts | zero of six, in three states — §1a |
| converting the one volume | a packing density | absent; a factor of twelve rides on it — §4 |
| `fan_in(j)` | inter-structure connection topology | not set, **and it is the claustrum's defining quantity** — §3 |
| whether `active` is dense or sparse | sparsity | not set |
| any cortical layer axis | tile geometry | not set, **and inadmissible for three of four cortical structures anyway** |
| the update interval in every edge-storage figure | the scheduling discipline | not set, and Micky's |
| whether `threshold` is ever written | the learning rule | not set, and Micky's |
| the claustrum's interneuron network | a representation for a non-directed coupling | not a listed item; the source has no convention — §1e |
| the section's three convergence steps | the internal edges that would perform them | owed at the source |
| 49 of 74 edge declarations | the payloads | owed at the source — **this is the section's binding constraint** |

**The bottom two rows are not deferred decisions.** Six of the items are choices Micky has not made and
would unblock other sections too. **The payloads and the internal edges are research the source has not
done**, and no decision at any rung substitutes for them.

**The section contains exactly one number with a time in it and it is not an edge latency**: the
claustrum's **~0.5–4 Hz** cortical oscillations, a period of **250 ms to 2 s**. A structure that
regulates an oscillation must close its loop fast relative to that period, so the claustro-cortical
round trip has an **upper bound of order the period** — and the axons carrying it are described as
exceptionally far-reaching, which is what makes the bound non-trivial rather than automatic. **It is
the only quantitative constraint on any latency in the section and it constrains the one edge whose
payload cannot be written.** *(Class 2 — a control argument, not a measurement.)*

---

## 2. Insula — interoceptive / salience / emotional core

### Contract — copied verbatim from the architecture

- **Inputs.** Ten edges.
  - **← posterior / ventromedial-posterior thalamus** (ventromedial posterior nucleus, posterior
    nuclear group), onto the **dorsal posterior insula** — the body's physiological condition, the
    lamina-I interoceptive stream, **somatotopically ordered**. Fan-in: to derive. *(File 12,
    two-ended and in the same terms. **Whether the three labelled lines the spinal entry types —
    nociceptive-specific, thermoreceptive-specific, polymodal — stay separate on this edge or are
    merged is owed at both ends.** That is an arity question.)*
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
  - **← amygdala** — the **valence tag**: a gain on perception, attention and memory encoding,
    carrying **no identity information** — what arrives is the significance, not the thing. Fan-in: to
    derive. *(File 8; typed from the producer. **Two-ended across a file boundary.**)*
  - **← temporal pole** — payload owed. Fan-in: to derive. *(File 7; two-ended, owed at both.)*
  - **← orbitofrontal / ventromedial prefrontal cortex** — payload owed. Fan-in: to derive. *(File 11;
    two-ended, owed at both.)*
  - **← anterior cingulate cortex** — payload owed. Fan-in: to derive. **The producer declares no such
    edge**, though its Inputs do declare the reciprocal limb from here. *(Owed at file 11.)*

  **Dangling requirement — "context" was never a payload, and three quarters of it still is not.** The
  Function slot consumes *emotional, cognitive and social context*, bound at the anterior pole into
  subjective feeling. Four incoming limbs were meant to supply it; **one now carries a typed payload
  (the amygdala's valence tag) and three are owed at both ends.**

- **Outputs.** Eleven edges.
  - **→ anterior cingulate cortex** (salience → control) — the **salience signal**: *this event is
    behaviourally relevant now*. **Whether what leaves is a scalar, a pointer, or a switching command
    is not established.** Fan-out: to derive. *(File 11; two-ended.)*
  - **→ right inferior frontal gyrus** — the same salience signal; payload otherwise owed. Fan-out: to
    derive. *(File 11.)*
  - **→ orbitofrontal / ventromedial prefrontal cortex** — the salience signal and, reciprocally, the
    **interoceptive state**; payload otherwise owed. Fan-out: to derive. *(File 11.)*
  - **→ temporal pole** — **interoceptive context**; payload otherwise owed. Fan-out: to derive.
    *(File 7.)*
  - **→ midcingulate cortex** — the **salience / affect signal**, in the consumer's terms; payload
    otherwise owed. Fan-out: to derive. *(In this file. **Both ends written in one pass.**)*
  - **→ amygdala** — payload owed at both ends. Fan-out: to derive. *(File 8; two-ended.)*
  - **→ bed nucleus of the stria terminalis**, from the **anterior insula** — **interoceptive state**;
    payload otherwise owed. Fan-out: to derive. *(File 8.)*
  - **→ hypothalamus** (autonomic / affect) — payload owed. Fan-out: to derive. *(File 14, not
    confirmed.)*
  - **→ basal ganglia**, onto the **ventral striatum** — payload owed at both ends. Fan-out: to derive.
    *(File 9; two-ended across a file boundary and across a date.)*
  - **→ habenula**, onto the **lateral habenula** — a **bad-outcome expectation**: an affective /
    evaluative signal that an outcome is worse than wanted. Payload otherwise owed. Fan-out: to derive.
    *(In this file; both ends confirmed in one pass.)*
  - **→ posterior / ventromedial-posterior thalamus** (corticothalamic feedback) — **no stimulus
    content; the driver / modulator gate.** Fan-out: to derive. *(File 12, two-ended and in the same
    terms.)*

  **The cortical output class is not fully resolved.** The dorsolateral prefrontal cortex is not among
  the consumers that declare an insular input, so whether the class covered it is unchecked.

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, no clean human per-region count;
  association / paralimbic cortex, uncounted per-region in human. **Parameter memory: to derive.**
  Synapses, axons, white-matter volume, myelination: unknown. **Grey-matter volume:** a sizeable
  territory, no single verified human figure. **No cross-check of any kind can be run.**

- **Shape.** **Laminated cortex whose laminar axis is not uniform across its own extent.** Granular
  postero-dorsally, agranular antero-ventrally, so **there is no single layer axis for the structure**.
  The tangential axis is **contested in extent** — 2, 3 or 16 areas depending on the parcellation:
  not unknown, not owed, but contested. Somatotopy in the dorsal posterior sector gives one sector a
  metric axis and the rest none. **The tile calculation cannot start: no thickness, no surface area, no
  pitch.**

- **Edge latency.** All 23 edges **to derive.**

### Representation

Declared per line, inherited by every consumer. **Latency is not re-declared here; it is the copied
Edge latency field above.**

| line | units | range / normalization | update timing | coordinate frame |
|---|---|---|---|---|
| ← thalamus, lamina-I stream | owed | owed | event-driven | **somatotopic** — stated, extent not given |
| ← gustatory pathway | owed | owed | event-driven | quality × intensity, axes unnamed |
| ← vestibular pathway | rate; acceleration | owed | event-driven | head-centred, stated by the producer |
| ← amygdala, valence tag | owed | owed | event-driven | **none — explicitly carries no identity** |
| → thalamus, driver/modulator gate | **not applicable — no stimulus content** | not applicable | event-driven | not applicable |
| all remaining 18 lines | owed | owed | event-driven | owed |

**Event-driven is the honest answer for every line here**, not a rate borrowed from elsewhere: no
producer in or out of this entry has a sampling rate of its own, and there is no system clock to borrow
one from.

### Transform

**Three operations in sequence along the granularity gradient**, and the third is not writable.

1. **Posterior (granular) sector** — reception of the lamina-I interoceptive stream into primary
   interoceptive cortex, somatotopically ordered. Standard operation: **threshold gate over a
   topographically ordered input array**.
2. **Posterior → mid (dysgranular)** — *re-representation and integration*. **No standard name fits**,
   and that is a finding about the structure and is recorded as one: the source says what the edge
   carries and does not say what operation produces it.
3. **Mid → anterior (agranular)** — binding of the re-represented image with emotional, cognitive and
   social context into *subjective feeling*. **No standard name fits and the output type does not
   exist.** `bind()` raises: **a written edge with an unwritable payload.**

**The direction is the claim.** Both internal edges run toward decreasing granularity — the tissue
loses layer 4, the input layer, exactly where it stops receiving from outside and starts receiving from
itself.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `threshold` | (sector, N) — sector extent **contested (2 / 3 / 16)**, N **to derive** | uint, `ceil(log2(fan_in))` bits | 0 … fan_in | count of active inputs |
| `active` | (sector, N) — same | 1 bit | {0, 1} | dimensionless |

**Neither is allocatable.** The sector axis has no settled extent and N has no value on any axis.

### Parameters

- **`threshold[j]`** — unit: count of active inputs. Value: **to derive**. Origin: **would be derived
  from the architecture's fan-in**, which reads *to derive* on all 23 edges. Not chosen.
- **`bits_per_threshold`** — unit: bits. Value: **≤ 16**, the log₂ ceiling. Origin: **derived** from the
  architecture's sizing method. It is a **cap, not a measurement**, and here it multiplies nothing.

### Update equation

```
count[j]  = Σ_{i ∈ fan_in(j)} active_source[i]
active[j] = count[j] ≥ threshold[j]
```

Integer comparison only; equal weights reduce the dot product to a count. **`fan_in(j)` is
unimplementable** — every fan slot in the entry reads *to derive*, and inter-structure connection
topology is unset and is Micky's.

### State carried between updates

**None declared.** No value in this entry is described as persisting between updates. The gradient's
re-representation could require one and the source does not say so; **inventing one would assert a
mechanism the description does not make.** State memory is not summed with parameter memory.

### Edge storage

`edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`

- **`line_count` = 13** — 11 outputs plus 2 internal edges, the lines this entry produces. Arriving
  lines are sized at their producers.
- **`latency`** — to derive, all 23 edges.
- **`update_interval`** — **unset.** The scheduling discipline is Micky's.
- **`bytes_per_value`** — to derive; gated on graded-versus-binary emission, which is on the
  surface-before-touching list.

**Three of four terms unset, so the figure is not computable and is not estimated.**

### Adaptation

**No rule changes any stored parameter in this entry, and none is assumed.** Nothing here is described
as changing as a result of what it computes. The learning rule is unset and is Micky's.

### Open

- The layer axis, which the standard laminar block cannot supply across a granularity gradient.
- Whether the three labelled lines from the spinal entry stay separate on the thalamic edge or merge —
  an arity question owed at both ends.
- The output type of the mid → anterior edge. **Open and unasked at the source rung**, where it sits.

---

## 3. Claustrum — the most-connected hub

### Contract — copied verbatim from the architecture

- **Inputs.** Five edges, **all payloads owed.**
  - **← cerebral cortex**, near **"all-to-all"** — payload owed. Fan-in: to derive. **The hardest class
    endpoint in the file**, and the one the source says it has no convention for.
  - **← amygdala**, onto the **ventral claustrum** — payload owed. Fan-in: to derive. **The producer
    declares no such edge**, though its Inputs declare the reciprocal limb from here. *(Owed at file
    8.)*
  - **← cingulate cortex** — payload owed. Fan-in: to derive. **A class, and three of its four
    candidate producers are entries in this same file. None of the four declares it.**
  - **← hippocampus / subiculum** — payload owed. Fan-in: to derive. *(File 8, which declares no
    claustral edge in either direction.)*
  - **← neuromodulatory afferents** — payload owed. Fan-in: to derive. **A class.** *(Owed at file 13:
    name the nuclei, or record that the brain-wide class is the whole claim.)*

- **Outputs.** Four edges, **all payloads owed.**
  - **→ cerebral cortex**, near all-to-all and reciprocal, on **exceptionally far-reaching
    claustro-cortical axons** — payload owed. Fan-out: to derive. **This is the edge the entry's
    Function slot depends on.** Binding, synchronisation, network switching, slow-oscillation control —
    **every one of the four hypotheses is a claim about what travels on this edge, and none of them
    types it.**
  - **→ amygdala** — payload owed. Fan-out: to derive. *(File 8; two-ended.)*
  - **→ hippocampus / subiculum** — payload owed. Fan-out: to derive. *(File 8, which declares no such
    edge.)*
  - **→ cingulate cortex** — payload owed. Fan-out: to derive. **Same class problem and same four
    unconfirmed far ends as the input limb.**

- **Sizing.** Basis: per hemisphere. **Neurons: to derive**, and the reason differs from the cortical
  entries': **a thin, hard-to-segment sheet.** **Grey-matter volume: no verified human figure, soft and
  segmentation-dependent.** Synapses, axons, white matter: unknown. Myelination: flanked by the extreme
  and external capsules, g-ratio unknown. **No cross-check can be run.**

- **Shape.** **Non-laminated sheet.** A **two-dimensional sheet with a thickness**, and none of the
  three extents is given. The cell-class axis has **three named members** whose status as sub-elements
  is unestablished; the dorsal / ventral axis has two members whose status is **owed**. **No extent on
  any axis.**

- **Edge latency.** All 9 edges **to derive.**

### Representation

| line | units | range / normalization | update timing | coordinate frame |
|---|---|---|---|---|
| → cerebral cortex (all-to-all) | **owed, and possibly not applicable** — see §1e | owed | **event-driven, bounded**: the loop it serves runs at 0.5–4 Hz, so a round trip of order 250 ms – 2 s | owed |
| all remaining 8 lines | owed | owed | event-driven | owed |

**The one bound in the section sits on the one line that cannot be typed.** It is recorded on the line
rather than applied, because a bound on a round trip is not a latency on an edge.

### Transform

**Unknown, and this is the completion test's clearest failure in the source.** The entry has four
candidate functions; each is a claim about the single all-to-all output edge; that edge's payload is
owed. **So the four hypotheses are not four competing descriptions of a known signal — they are four
guesses at an unknown one**, and choosing among them is not a modelling decision deferrable to a lower
rung, because there is nothing to defer.

**No standard name fits, and that is a finding about the structure.** The module records the four
hypotheses as four claims about one untyped edge and reports the count; it does not pick one.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `threshold` | (cell class, N) — cell-class extent 3, **status as sub-elements unestablished**; N to derive | uint, `ceil(log2(fan_in))` bits | 0 … fan_in | count of active inputs |
| `active` | (cell class, N) — same | 1 bit | {0, 1} | dimensionless |

**Not allocatable, and the axis itself is not established.** Three cell classes are named and the
source's own test for a sub-element — different targets or different payloads — has not been met by
any of them. A dorsal / ventral division is used by the entry's edges and its sub-element status is
owed.

**And one relation in this structure is not an array or an edge.** The `Coupling` record for the
gap-junction network has `members` rather than `source` and `target`, is excluded from the edge count,
and cannot be given a latency (§1e).

### Parameters

- **`threshold[j]`** — unit: count of active inputs. Value: **to derive**. Origin: would be derived
  from fan-in; **every fan slot in the entry reads unknown.**
- **`bits_per_threshold`** — **≤ 16**, the log₂ ceiling. Derived. A cap; it multiplies nothing.

**The structure's defining quantitative fact is a parameter this rung cannot use.** *Most-connected per
unit volume* is a statement about **connection density**, and connection topology is precisely what is
unset. **So the one thing known quantitatively about this structure is known about the one axis the
model has no values on.** `fan_in_map()` raises with that named.

### Update equation

The forward operation above applies unchanged in form. **It cannot be run**: no counts, no topology,
and the operation's output would be a value on an edge whose payload is owed.

**And there is a prior question the equation cannot answer.** If the claustral output carries no
content at all but only a **time**, then a count of active inputs crossing a threshold is not the wrong
arithmetic, it is arithmetic on the wrong quantity. **Recorded as a candidate, not a verdict.**

### State carried between updates

**None declared.** A structure regulating a 0.5–4 Hz oscillation would need a phase or a timer, and
**no such value appears in the description.** Inventing one would supply the mechanism the section is
missing.

### Edge storage

- **`line_count` = 4** — the outputs this entry produces. No internal edges.
- **`latency`** — to derive, all 9 edges.
- **`update_interval`** — unset.
- **`bytes_per_value`** — to derive.

**Not computable. But this is the one structure in the project so far where edge storage would
plausibly dominate the parameter store** — a near-all-to-all cortical projection on exceptionally
far-reaching axons — and it is the one whose topology is furthest from being stateable. **Recorded as
where the figure will be large, which is what can be said.**

### Adaptation

**None declared, and none assumed.**

### Open

- A representation for a non-directed coupling. **The source has no convention and this entry is where
  it is first needed.**
- Whether the payload is purely temporal, which the payload slot has no shape for.
- Whether dorsal and ventral project to different targets — the test for a sub-element.

---

## 4. Habenula — the value brake

### Contract — copied verbatim from the architecture

- **Inputs.** Eight edges, all over the **stria medullaris**.
  - **← septal nuclei**, onto the **medial habenula** — payload owed. Fan-in: to derive. **This
    producer has no entry in any of the twenty files.**
  - **← internal globus pallidus**, onto the **lateral habenula** — the basal-ganglia **"no-reward"
    signal**; payload otherwise owed. Fan-in: to derive. *(File 9, which wrote its end specifically to
    close this diff. Two-ended.)*
  - **← ventral pallidum**, onto the **lateral habenula** — payload owed. Fan-in: to derive. *(File 9;
    written here and the owed edit discharged. **File 9 still records it as owed.**)*
  - **← lateral hypothalamus** and the lateral septo-hypothalamic continuum, onto the **lateral
    habenula** — payload owed. Fan-in: to derive. *(File 14, not confirmed.)*
  - **← suprachiasmatic nucleus**, onto the **lateral habenula** — payload owed. Fan-in: to derive.
    *(File 14, where it is a named sub-element that does not declare this edge. Owed there.)*
  - **← anterior cingulate cortex**, onto the **lateral habenula** — a **bad-outcome expectation**;
    payload otherwise owed. Fan-in: to derive. **The producer declares no such edge.** *(Owed at file
    11.)*
  - **← anterior insula**, onto the **lateral habenula** — a **bad-outcome expectation**; payload
    otherwise owed. Fan-in: to derive. *(In this file; both ends in one pass.)*
  - **← ventromedial prefrontal cortex**, onto the **lateral habenula** — a **bad-outcome
    expectation**; payload otherwise owed. Fan-in: to derive. **The producer declares no such edge.**
    *(Owed at file 11.)*

  **Three edges carry the same payload name and two of the three have no producer end.**

- **Outputs.** Four edges, all over the **fasciculus retroflexus**.
  - **→ interpeduncular nucleus**, from the **medial habenula** — payload owed. Fan-out: to derive.
    **This consumer has no entry in any of the twenty files.**
  - **→ rostromedial tegmental nucleus**, from the **lateral habenula** — a **negative / aversive value
    signal**: a **glutamatergic excitatory drive encoding a worse-than-expected outcome, which that
    nucleus inverts in sign into inhibition of the dopamine cells.** Fan-out: to derive. *(File 14.
    Two-ended.)* **This is the best-typed edge in the section.**
  - **→ raphe nuclei**, from the **lateral habenula** — the same signal, modulating serotonin rather
    than dopamine; payload otherwise owed. Fan-out: to derive. *(File 13; two-ended.)*
  - **→ pineal gland**, from the **medial habenula** — payload owed. Fan-out: to derive. **The consumer
    declares no such edge.** **The link is stated in the Function slot as prose and that is not an
    edge.** *(Owed here first, then at file 14.)*

  **No direct dopamine edge is written**, deliberately: the suppression is *chiefly indirect*. A sparse
  direct habenula → ventral-tegmental-area projection is reported in the literature and is **not**
  written, because it was not confirmed at either end.

- **Sizing.** Basis: **per side**, and this is the only entry in the section with a firm number of any
  kind. **Neurons: to derive** — **human stereology exists and reports volumes and disease-related
  changes rather than a control absolute.** **Grey-matter volume: ~30–36 mm³ per side** — post-mortem
  ~31 mm³ left and ~33 mm³ right, uncorrected for shrinkage; high-resolution magnetic resonance imaging
  ~29–36 mm³. A slight **right > left** asymmetry. **White-matter volume:** unknown. **Myelination:**
  the fasciculus retroflexus is a compact myelinated tract, g-ratio unknown.

- **Shape.** **Non-laminated nucleus, rank 2: (division, N)**, with the division axis at **extent 2**
  and both members named — the only fully-populated shape axis in the section. **The next axis down is
  owed.** N is to derive. **Cell-class axis: not applicable at the structure level and unknown below
  it.**

- **Edge latency.** All 12 edges **to derive.** **Both carrying tracts have no entry.**

### Representation

| line | units | range / normalization | update timing | coordinate frame |
|---|---|---|---|---|
| ← internal globus pallidus, "no-reward" | owed | owed | event-driven | owed |
| ← anterior cingulate / insula / ventromedial prefrontal, bad-outcome expectation | owed | owed | event-driven | owed — **and the same name on three lines is not evidence of the same frame** |
| → rostromedial tegmental nucleus | owed | **signed in effect, not in the payload**: excitatory drive, inverted downstream | event-driven | owed |
| all remaining 8 lines | owed | owed | event-driven | owed |

### Transform

**Two divisions, two transforms, and only one of them has both ends.**

- **Lateral habenula** — computes a **negative reward-prediction error**: excitation by aversive
  events, pain, loss, and the **omission of expected reward**. The named operation is a **comparison of
  an expected against a received value, emitting on the negative residual**. It is the mirror of the
  midbrain dopamine computation and is a separate line with its own tract, relay and transmitter.
- **Medial habenula** — cholinergic / substance-P. **No transform is writable**: its only input and its
  only output are regions with no entry anywhere, so there is nothing at either end to transform
  between.

`value_brake()` raises, and its blocker is the **model**, not the description: the payload is typed,
the sign is stated, the inversion is attributed to the correct stage — and **a count of active inputs
crossing a threshold has no term for either the excitation's magnitude or the downstream inversion.**

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `threshold` | **(division, N)**, division extent **2**, both members named; N to derive | uint, `ceil(log2(fan_in))` bits | 0 … fan_in | count of active inputs |
| `active` | (division, N) — same | 1 bit | {0, 1} | dimensionless |

**The only fully-populated shape axis in the section**, and the only one that would be allocatable if
N existed.

### Parameters

- **`threshold[j]`** — count of active inputs. **To derive.**
- **`bits_per_threshold`** — **≤ 16**, the log₂ ceiling. Derived; a cap.
- **`packing_density`** — neurons per mm³. **Absent from the section, and it is the one parameter that
  would convert this entry's firm volume into a count.** Not chosen. Across a bracketing span — and
  these four values are **Claude's construction, chosen to span, and none is a candidate figure for
  this tissue**:

| density | neurons per side | store at 16 bits |
|---|---|---|
| 10,000 /mm³ | 300,000 – 360,000 | 0.60 – 0.72 MB |
| 20,000 /mm³ | 600,000 – 720,000 | 1.20 – 1.44 MB |
| 50,000 /mm³ | 1.50M – 1.80M | 3.00 – 3.60 MB |
| 100,000 /mm³ | 3.00M – 3.60M | 6.00 – 7.20 MB |

  **Factor of twelve end to end, and it decomposes: the density span contributes ×10 and the volume's
  own range ×1.2.** The table is here to show that the firm number buys nothing on its own, **not to
  propose a figure**. The volume is Class 1; the arithmetic is computed in the module, not carried.

### Update equation

The forward operation above, unchanged in form and unrunnable for want of N and fan-in. **And it is
the wrong shape for what this structure does**: the lateral habenula's computation is a residual
between an expectation and an outcome, which the count-and-threshold form cannot express.

### State carried between updates

**None declared — and the entry's own function implies one.** A *negative reward-prediction error*
requires an **expected** value to compare a received one against, and **no expectation is declared as
stored anywhere in the entry**. Whether the expectation is held here or arrives on the pallidal or
cortical lines is **not stated**. Recorded as a gap in the description, not filled.

### Edge storage

- **`line_count` = 4** — the outputs this entry produces.
- **`latency`** — to derive, all 12 edges. **Both carrying tracts have no entry**, and a tract is where
  the physical substrate of a latency lives, so the derivation has no starting point either.
- **`update_interval`** — unset.
- **`bytes_per_value`** — to derive.

### Adaptation

**None declared here, and the section produces a teaching signal it does not consume.** The lateral
habenula's negative reward-prediction error **leaves** this section — to the rostromedial tegmental
nucleus in file 14 and the raphe in file 13 — and nothing here is described as changing as a result.

*(Worth recording for whenever a rule is set: **the two halves of the reward-prediction error are
computed in different files by different structures with different transmitters.** Positive is
dopaminergic; negative is glutamatergic, from the lateral habenula, and is inverted to inhibition one
stage downstream. **A rule that treats the error as one signed scalar will be asserting a merge the
description does not make.** Class 2 — Claude's reading.)*

### Open

- Whether the two divisions communicate at all. **Not established**, and they share nothing on the wire
  in this description.
- Where the expectation term of the prediction error is held.
- The subnuclei of each division — described in the literature, not named here.

---

## 5. Midcingulate cortex — the action–outcome / cingulate-motor hub

### Contract — copied verbatim from the architecture

- **Inputs.** Seven edges.
  - **← anterior cingulate cortex** (reward / outcome) — a **scalar reward-value signal**: expected
    reward magnitude, and a response to the mismatch between expected and received reward — firing to
    unexpected reward and to expected-but-omitted reward. **It has a coordinate frame — a scalar value
    axis — whose zero and slope are set by bodily and motivational state, so the frame is
    body-relative.** Fan-in: to derive. *(File 11. Two-ended, with the producer's caution carried: the
    two ends are copies.)*
  - **← amygdala** — the **valence tag**, carrying no identity information. Fan-in: to derive. *(File
    8; two-ended across a file boundary.)*
  - **← anterior insula** — the **salience / affect signal**; payload otherwise owed. Fan-in: to
    derive. *(In this file; both ends in one pass.)*
  - **← posterior parietal cortex** — payload owed. Fan-in: to derive. **A class**, with candidate
    producers in file 6 and none confirmed.
  - **← posterior cingulate cortex** (action / spatial) — payload owed. Fan-in: to derive. **The
    producer is an entry in this same file and does not declare it.**
  - **← midline and intralaminar thalamus** — payload owed. Fan-in: to derive. **The producer declares
    its cortical target as a class** — *striatum (major) and cortex (diffuse)*. *(Owed at file 12.)*
  - **← mediodorsal thalamus** — payload owed. Fan-in: to derive. *(File 12, not confirmed.)*

  **← the cingulum** is **routing, not an edge**, and is not counted.

- **Outputs.** Six edges.
  - **→ supplementary and pre-supplementary motor areas and premotor cortex**, via the **cingulate
    motor areas** — payload owed; at this end it is *the convergence of reward or non-reward outcome
    with action and spatial information, turned into a motor plan*. Fan-out: to derive. *(File 11.
    Two-ended.)*
  - **→ primary motor cortex**, via the **cingulate motor areas** — payload owed. Fan-out: to derive.
    *(File 5, not confirmed.)*
  - **→ anterior cingulate cortex**, reciprocally, via the **cingulum** — payload owed. Fan-out: to
    derive. *(File 11; two-ended, owed at both.)*
  - **→ posterior cingulate cortex**, reciprocally — payload owed. Fan-out: to derive. *(In this file;
    both ends in one pass.)*
  - **→ basal ganglia** — payload owed. Fan-out: to derive. **A class**: the striatal target is likely
    and is not stated. *(File 9; the far end confirms the edge exists and inherits the same unresolved
    target. Naming the nucleus is owed here first.)*
  - **→ brainstem autonomic targets** — payload owed. Fan-out: to derive. **A class**; file 14 holds
    the candidates and none was confirmed.

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, paralimbic association cortex,
  uncounted per-region in human. **Grey-matter volume, white-matter volume, synapses, axons,
  myelination: all unknown.** **Not one figure in the entry, and no cross-check runnable.**

- **Shape.** **Agranular-to-dysgranular cortex: a laminar axis that exists and is not the standard one,
  and is not written.** The block is inadmissible and no replacement is given, so **the layer axis is
  owed rather than unknown.** The tangential axis has **four named members** — 24′, 32′, and the rostral
  and caudal cingulate motor areas — plus 24′'s three subdivisions a′, b′, c′. **No extent, no
  boundaries, no pitch.**

- **Edge latency.** All 13 edges **to derive.**

### Representation

| line | units | range / normalization | update timing | coordinate frame |
|---|---|---|---|---|
| ← anterior cingulate, scalar reward value | owed | **a scalar value axis**; zero and slope set by bodily and motivational state | event-driven | **body-relative** — the only stated frame in the section |
| ← amygdala, valence tag | owed | owed | event-driven | **none — explicitly carries no identity** |
| ← anterior insula, salience / affect | owed | owed | event-driven | owed |
| → motor fields, motor plan | owed | owed | event-driven | **body-centred, implied by *motor plan* and not stated** |
| all remaining 9 lines | owed | owed | event-driven | owed |

**The one stated frame and the one implied frame are not the same frame**, and that is the entry's
whole operation — see below.

### Transform

**A change of frame, from value to action.** A scalar value axis with a body-relative zero, a valence
gain, and a salience flag arrive; a motor plan leaves. **So the operation is not a combination within a
frame — it is a frame conversion**, and that is precisely what the action–outcome reading claims the
structure is for.

**No standard name fits, and the edge that would carry it is not written.** *Convergence turned into a
motor plan* is a transfer from the fields that receive outcome and action onto the motor areas that
emit; **that internal edge is owed**, so the structure's whole claim is the step the slot does not
contain. `converge()` raises: **an unwritten internal edge.**

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `threshold` | (field, N) — field extent 4 named, with a partially-populated second level (24′ → a′, b′, c′); N to derive | uint, `ceil(log2(fan_in))` bits | 0 … fan_in | count of active inputs |
| `active` | (field, N) — same | 1 bit | {0, 1} | dimensionless |

**No layer axis**, because the standard block is inadmissible for agranular-to-dysgranular tissue and
no replacement is given. That axis reads **owed**, not unknown.

### Parameters

- **`threshold[j]`** — count of active inputs. **To derive.**
- **`bits_per_threshold`** — **≤ 16**. Derived; a cap.

### Update equation

The forward operation above. **Unrunnable**, and additionally the wrong shape: a frame conversion is
not expressible as a count of active inputs crossing a threshold, whatever the counts turn out to be.

### State carried between updates

**None declared.** *Expected* reward magnitude arrives already computed on the anterior cingulate line;
nothing in this entry is described as holding it.

### Edge storage

- **`line_count` = 6** — the outputs this entry produces. One further edge it produces, → posterior
  cingulate cortex at that entry's input side, is the same line as its own output and is not counted
  twice (§1b).
- **`latency`** — to derive, all 13 edges.
- **`update_interval`** — unset.
- **`bytes_per_value`** — to derive.

### Adaptation

**None declared, and none assumed** — although the entry's stated function is *action–outcome
learning*, which is a learning claim with no rule attached to it anywhere in the section.

### Open

- The internal edge from the receiving fields to the cingulate motor areas. **This is the entry's
  stated function.**
- The layer axis for agranular-to-dysgranular tissue.
- Naming the striatal target, before the file-9 far end can be checked.

---

## 6. Posterior cingulate cortex — default-mode hub

### Contract — copied verbatim from the architecture

- **Inputs.** Six edges.
  - **← hippocampal formation** — the **completed episode**: the bound, retrievable pattern,
    **addressable by any fragment of itself**. **Payload only partly writable — owed:** an episode has
    no units and no frame, and what makes it checkable is a **property** rather than a type. Fan-in: to
    derive. *(File 8, typed from the producer's declaration.)*
  - **← anterior cingulate cortex** — payload owed. Fan-in: to derive. **The producer declares no such
    edge.** *(Owed at file 11.)*
  - **← midcingulate cortex** — payload owed. Fan-in: to derive. *(In this file; both ends in one
    pass.)*
  - **← precuneus** — payload owed. Fan-in: to derive. *(File 6, which declares an input from here but
    was not confirmed to declare the return limb.)*
  - **← posterior parietal cortex** (action / spatial) — payload owed. Fan-in: to derive. **A class.**
  - **← anterior thalamus** — payload owed. Fan-in: to derive. **The producer declares no such edge**:
    its anterior nuclei name the retrosplenial and anterior cingulate cortices, not this region.
    *(Owed at file 12.)*

  **← the cingulum** is **routing, not an edge.**

- **Outputs.** Five edges, **all payloads owed.**
  - **→ hippocampal formation** — payload owed at both ends. Fan-out: to derive. *(File 8; **written by
    name now, the class it was hidden in gone, and the payload still owed.**)*
  - **→ precuneus** — payload owed at both ends. Fan-out: to derive. *(File 6; two-ended by name.)*
  - **→ angular gyrus** — payload owed. Fan-out: to derive. *(File 6, not confirmed.)*
  - **→ orbitofrontal / ventromedial prefrontal cortex**, the medial-prefrontal default-mode partner —
    payload owed. Fan-out: to derive. *(File 11, not confirmed.)*
  - **→ cognitive-control network**, via the **dorsal posterior cingulate cortex** — payload owed.
    Fan-out: to derive. **A network endpoint, and the source states it is not repairable by naming the
    members.**

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, association cortex, uncounted
  per-region in human. **Everything else unknown. No cross-check runnable.**

- **Shape.** **Granular isocortex — the only structure in the section whose laminar axis could be
  written from the standard block, and it is not written.** Layer axis therefore **owed, not unknown**.
  Tangential axis: **two named sectors** (dorsal: 23d, 31; ventral: 23a, 23b), each resolving to named
  areas — **the best-populated tangential axis in the section**. **No extents, no boundaries, no
  pitch.**

- **Edge latency.** All 11 edges **to derive.**

### Representation

| line | units | range / normalization | update timing | coordinate frame |
|---|---|---|---|---|
| ← hippocampal formation, completed episode | **not applicable — an episode has no units** | **not applicable**; what makes it checkable is **content-addressability**, a property | event-driven | **not applicable — no frame** |
| all remaining 10 lines | owed | owed | event-driven | owed |

**The structure's own distinctive fact has no line to sit on.** It **deactivates** as externally-focused
task demand rises — a statement about a **baseline** from which the structure is driven **down**. That
is a property of the structure, not of an edge, so **there is nowhere in this template to write it.**
It is the third payload in the project whose informative event is a decrease, alongside the insula's
content-free corticothalamic gate and the basal ganglia's tonic inhibition, **and the activity bit's
polarity convention is not this rung's to set.**

### Transform

**A switch between two regimes, and the edge that would perform it is owed.** The ventral sector is
tied to the default-mode network and the medial temporal lobe; the dorsal sector additionally to the
fronto-parietal control network, and helps modulate the switch between internal and external focus.
**Whether the dorsal and ventral sectors are connected to each other is owed** — and that connection is
exactly what a switch requires.

**A second gap sits on the input side.** The sector division is written on the outputs and **not one of
the six incoming edges says which sector it lands on**, while three of five outgoing edges are
attributed by sector. **A structure whose function is switching between two regimes needs to know which
regime an input belongs to**, and the description assigns sectors only on the way out.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `threshold` | (sector, N) — sector extent 2, each resolving to named areas; N to derive | uint, `ceil(log2(fan_in))` bits | 0 … fan_in | count of active inputs |
| `active` | (sector, N) — same | 1 bit | {0, 1} | dimensionless |

**The layer axis is admissible here and is absent**, because the check against the entry's own laminar
description has not been run. That is the correct order and it leaves the axis **owed**.

### Parameters

- **`threshold[j]`** — count of active inputs. **To derive.**
- **`bits_per_threshold`** — **≤ 16**. Derived; a cap.
- **`baseline`** — the resting level the structure is driven down from. **Named by the description,
  with no value, no units, and no slot in this template.** Not chosen and not defaulted.

### Update equation

The forward operation above, unrunnable. **And it cannot express a deactivation**: `active[j] =
count[j] ≥ threshold[j]` has no resting state to fall below.

### State carried between updates

**A baseline is implied and not declared.** A structure that deactivates from rest holds a rest level
between updates; the description states the behaviour and not the quantity. **Recorded as implied, not
written as state**, because writing it would fix a value the description does not give.

### Edge storage

- **`line_count` = 5** — the outputs this entry produces, one of which (→ midcingulate cortex) is
  declared only at its consumer.
- **`latency`** — to derive, all 11 edges.
- **`update_interval`** — unset.
- **`bytes_per_value`** — to derive.

### Adaptation

**None declared, and none assumed.**

### Open

- Whether the dorsal and ventral sectors are connected. **The stated function requires it.**
- Which sector each incoming edge lands on.
- How the description writes an edge to a network, or whether it refuses to.

---

## 7. Retrosplenial cortex — the spatial / Papez node

### Contract — copied verbatim from the architecture

- **Inputs.** Five edges.
  - **← hippocampal formation**, from the **subiculum** — the **completed episode**, addressable by any
    fragment of itself; payload only partly writable — owed. Fan-in: to derive. *(File 8, typed from
    the producer.)*
  - **← anterior thalamic nuclei** — payload owed. Fan-in: to derive. *(File 12. Two-ended, owed at
    both.)* **A specific gap sits under this edge and it is the entry's headline input.** The
    **head-direction** signal the Function slot depends on is classically carried by **one division**
    of the anterior nuclei rather than by the group, and that entry records its own divisions as
    unnamed and owed. **Until they are named, the entry's headline input cannot be written as an edge
    from the division that carries it.**
  - **← parahippocampal cortex** — payload owed. Fan-in: to derive. **This producer has no entry in any
    of the twenty files**, and is named as a producer by three other files as well.
  - **← posterior parietal cortex** — payload owed. Fan-in: to derive. **A class.**
  - **← visual areas** — payload owed. Fan-in: to derive. **A class**, and it is the edge that would
    supply **half of what the region is said to fuse**.

  **← the cingulum** is **routing, not an edge.**

  **Dangling requirement — the self-motion half of the fusion, and it is the largest gap in the
  entry.** The Function slot fuses **internal self-motion cues (vestibular, proprioceptive, motor
  efference)** with external visual landmarks, and **no incoming edge declares any of the three.**
  **Both halves of the fusion the entry exists to perform are undeclared at their sources** — the
  visual half by a class endpoint, the self-motion half by nothing at all.

- **Outputs.** Three edges.
  - **→ hippocampal formation**, via **parahippocampal and entorhinal cortex** — the **return arm of
    the spatial-memory loop**: heading and landmark information **after the egocentric-to-allocentric
    translation this region performs.** Payload otherwise owed. Fan-out: to derive. *(File 8;
    two-ended. **The route runs through a region with no entry.**)*
  - **→ anterior thalamic nuclei** — payload owed. Fan-out: to derive. **The consumer records this edge
    as one it does not carry.** **Two-ended in intent only.**
  - **→ precuneus** — the **return arm of the spatial-memory loop**, in the same terms. Payload
    otherwise owed. Fan-out: to derive. *(File 6; two-ended.)*

- **Sizing.** Basis: per hemisphere. **Neurons: to derive** — soft, a small granular / dysgranular
  peri-allocortical strip, no clean human per-region count. **Everything else unknown. No cross-check
  runnable.**

- **Shape.** **Cortex spanning a granular / dysgranular border: two layer sets, one structure.** The
  layer axis is **not one axis** and the block cannot be written across it. Tangential axis: **two named
  members**, area 29 and area 30, **whose status as sub-elements is itself owed.** **No extents, no
  pitch.**

- **Edge latency.** All 8 edges **to derive.**

### Representation

| line | units | range / normalization | update timing | coordinate frame |
|---|---|---|---|---|
| ← anterior thalamic nuclei | owed | owed | event-driven | **egocentric, required by the function and not stated on the edge** |
| ← hippocampal formation, completed episode | **not applicable** | **not applicable**; content-addressable | event-driven | **not applicable** |
| → hippocampal formation / precuneus, return arm | owed | owed | event-driven | **allocentric, declared by reference to an operation rather than stated** |
| all remaining 5 lines | owed | owed | event-driven | owed |

**This is the entry where the missing Representation field costs most.** The structure's whole function
is a **coordinate-frame conversion**, and a coordinate frame is one of the four things this field
carries. The frames are named at the structure level and **absent from every edge.**

### Transform

**A coordinate-frame conversion: egocentric in, allocentric out.** That is a stated transformation with
named input and output frames, and it is worth more than the payloads the entry carries — it is
**a transform, not a selection or a gain**, which constrains the owed internal edges more tightly than
any other entry in the section constrains its own.

**And it is undercut at the input.** A frame conversion needs the self-motion signal to define the
transform, and **no edge declares one.** `fuse()` raises: **an undeclared input**, which is a different
blocker from the insula's unwritable payload and the midcingulate's unwritten edge.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `threshold` | (area, N) — area extent 2 (29, 30), **status as sub-elements owed**; N to derive | uint, `ceil(log2(fan_in))` bits | 0 … fan_in | count of active inputs |
| `active` | (area, N) — same | 1 bit | {0, 1} | dimensionless |

**No single layer axis**, because the entry spans a granular / dysgranular border and one block would
assert a layer-4 circuit across tissue that has layer 4 on one side only.

**And the transform implies an array this list does not have.** Holding the same content in two frames
requires two representations and a mapping between them; **the description names both frames and
declares neither array.** Not written, because writing it would invent the arity.

### Parameters

- **`threshold[j]`** — count of active inputs. **To derive.**
- **`bits_per_threshold`** — **≤ 16**. Derived; a cap.
- **`heading`** — the quantity the frame conversion runs on. **Required by the stated function, declared
  by no incoming edge.** Not chosen.

### Update equation

The forward operation above, unrunnable — and, as at the midcingulate, the wrong shape: a frame
conversion is not a count of active inputs crossing a threshold.

### State carried between updates

**A current heading is implied and not declared.** *Keeping heading current* requires a value that
persists between updates; the description states the function and declares no such value. Recorded as
implied, not written.

### Edge storage

- **`line_count` = 3** — the outputs this entry produces.
- **`latency`** — to derive, all 8 edges.
- **`update_interval`** — unset.
- **`bytes_per_value`** — to derive.

### Adaptation

**None declared, and none assumed.**

### Open

- Whether areas 29 and 30 project to different targets — the prior question to their being
  sub-elements at all.
- The producer of the self-motion signal. **This entry's largest gap.**
- Naming the anterior thalamic division that carries head-direction, which will split the input edge
  from the far end.

---

## 8. Completion test

**An entry is finished when the code can be written from it without making a single further choice.**

| entry | finished | what a further choice would be |
|---|---|---|
| Insula | **no** | the output type of the mid → anterior edge; the layer axis; N on every axis |
| Claustrum | **no** | the transform itself — four hypotheses, one untyped edge; a representation for the coupling |
| Habenula | **no** | where the expectation term lives; a packing density; N |
| Midcingulate cortex | **no** | the internal edge that is the entry's stated function; the layer axis; N |
| Posterior cingulate cortex | **no** | the dorsal–ventral connection; the baseline value; the input sector attributions; N |
| Retrosplenial cortex | **no** | the self-motion producer; the two-frame array structure; N |

**None of the six is finished, and the section cannot be finished at this rung.** The forward operation
is writable and there is almost nothing to run it on: no counts, no topology, no latencies, and
two-thirds of the payloads owed.

**The blockers are of three kinds and only one of them is a decision.** Six items in §1f are choices
Micky has not made, and making them would unblock other sections too. **The payloads and the internal
edges are research the source has not done**, and no decision at any rung substitutes for them. **One —
the non-directed coupling — is a property of the biology the edge model has no slot for**, and it is
one relation inside one structure rather than the mechanism of a section.

**What the module implements**, given all of that:

- six structures and nine sub-element groupings as data, each carrying its source slot state **and**
  the three-way count state, so four structures blocked by one repair are not reported as four
  problems;
- **76 edge declarations resolving to 73 distinct edges**, each carrying the file its far end lives in,
  that far end's declaration state, which of four payload shapes it is in, and whether the endpoint is
  a region, an entry-less region, a class or a network;
- a `Coupling` record for the gap-junction network that is **deliberately not an `Edge`**, so it cannot
  be counted or scheduled as one;
- an **endpoint-kind census** and a **class-family report** collapsing eleven class endpoints into
  seven decisions, three of which are repeated families covering seven of the eleven;
- an **intra-file diff** — the four far ends that are entries in this same file and do not declare the
  edge;
- a **same-pass certification report** — the declarations marked two-ended that say in the same breath
  that both ends were written in one pass;
- an **edge-count reconciliation**, 44 + 33 − 3 = 74 inter-region and 2 internal, **with the
  declaration-to-distinct-edge collapse shown**, and the recorded disagreement with the source design's
  figure of 62 left unsmoothed;
- a **laminar-admissibility check** over the four cortical structures, separating *inadmissible* from
  *admissible and unchecked*;
- the habenula volume-to-count arithmetic across a bracketing density range, **presented as a
  demonstration that the number is absent rather than as an estimate**;
- `bind()`, `converge()`, `fuse()` and `value_brake()` raising with four different reasons, and
  `step()` raising with the claustral bound recorded rather than applied.
