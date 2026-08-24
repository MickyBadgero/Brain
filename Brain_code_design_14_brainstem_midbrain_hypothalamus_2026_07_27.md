# Brain code design — 14 brainstem midbrain hypothalamus

**Rung:** code design (algorithms). **Spec:** `Brain_architecture_14_brainstem_midbrain_hypothalamus_2026_07_27.md`.
**Implements:** `Brain_14_brainstem_midbrain_hypothalamus.py`.

**This document's own rung spec was not in hand when it was written.**
`Brain_code_design_spec_<date>.md` governs this rung and was not available, so **the shape of this
file is Claude's inference** from the field names CLAUDE.md lists in passing — standalone-not-
companion, verbatim contract fields, a Representation field, a completion test — and from the file-01
and file-13 code designs, written under the same limitation. Treat the *form* as a candidate and the
*contract* below as derived.

**Standalone, not a companion.** Every contract field below is carried **verbatim** rather than
referenced. A reader implementing from this file should not need the architecture open.

---

## 1. Contract — carried verbatim from the architecture

Ten structures. **Counting basis is not uniform**: paired nuclei per side, midline structures whole,
and one structure changes basis along its own length.

| # | structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Superior colliculus | per side | soft, no clean human total | ≤ 16 | to derive |
| 2 | Lateral parabrachial nucleus | per side | unknown | ≤ 16 | to derive |
| 3 | Caudal ventrolateral medulla | per side | unknown | ≤ 16 | to derive |
| 4 | Nucleus of the solitary tract | per side rostrally / whole caudally | unknown | ≤ 16 | to derive |
| 5 | Rostral ventrolateral medulla | per side | unknown | ≤ 16 | to derive |
| 6 | Periaqueductal grey | whole (midline) | soft, no clean count | ≤ 16 | to derive |
| 7 | Hypothalamus — suprachiasmatic nucleus | per side | ~50,000 | ≤ 16 | ≤ 0.10 MB |
| 7 | Hypothalamus — the other ten sub-nuclei | mixed | unknown | ≤ 16 | to derive |
| 8 | Pineal gland | whole (midline) | **none** | — | **0** |
| 9 | Reticular formation | whole (both sides) | soft, no countable border | ≤ 16 | to derive |
| 10 | Rostromedial tegmental nucleus | per side | soft, no clean count | ≤ 16 | to derive |
| | **stated total** | mixed | **~50,000 counted** | | **≤ 0.10 MB per side** |

**Every fan-in and every fan-out in this section reads *unknown*, and every edge latency reads *to
derive*.** No conduction time and no synaptic delay appears anywhere in the section.

**Eighty edges. Not one structure here can be sized except one sub-element of one entry.** The
pineal's zero is the only figure in the table that is not a gap: the gland has no neurons, so it
stores no thresholds, and no measurement will change that.

**Edges whose endpoint is finer than a whole structure**, because those constrain allocation:

- retina → **superior colliculus, stratum griseum superficiale**; V1 layer 5b → **the superficial
  layers**; ventral lateral intraparietal area and frontal eye field → **the intermediate layers**;
  olivary pretectal nucleus → **stratum griseum intermediale**
- superior colliculus **intermediate and deep layers** → the saccade burst generators, which are
  themselves **sub-elements of the reticular formation entry**
- superior colliculus **deep layers** → cervical spinal cord via the tectospinal tract
- caudal ventrolateral medulla → **rostral ventrolateral medulla, presympathetic neurons**
- rostral ventrolateral medulla, **non-bulbospinal C1 group** → hypothalamus, paraventricular nucleus
- periaqueductal grey **ventrolateral column** → rostral ventromedial medulla, and → locus coeruleus
- hypothalamus **magnocellular supraoptic and paraventricular neurons** → posterior pituitary;
  **parvocellular** neurons → anterior pituitary; **mammillary bodies** → anterior thalamic nuclei
- retina → **hypothalamus, suprachiasmatic nucleus** — the only edge in the section terminating on a
  sub-element that has a count
- lateral parabrachial nucleus → **five named hypothalamic sub-nuclei** of an entry that is itself a
  bundle

**Seven edges are not projections**, in four classes: **chemical sensing from blood** (solitary
nucleus, hypothalamus — fan-in *not applicable*, no producer region); **hormonal output into blood**
(posterior pituitary, anterior pituitary, melatonin to the general circulation); **a hormonal edge
with a receptor-bearing consumer** (melatonin → suprachiasmatic nucleus, a real two-ended edge); and
**an edge with no consumer at all** (melatonin into circulation and cerebrospinal fluid — a producer,
a payload, a real physical effect, and no target region).

**Six structures are named on this section's edges and have no entry anywhere:** the rostral
ventromedial medulla, the pontine nuclei, the red nucleus, the lateral septum, the two pituitaries
(recorded as endocrine terminals), and the superior cervical ganglion (peripheral, outside scope by
rule).

**Invariants carried:** whole-pathway co-instantiation — **and the cerebro-cerebellar loop cannot
satisfy it**, because the pontine nuclei and red nucleus are computing stages inside a closed loop
with no slot; per-edge latency, nonzero, finite, heterogeneous, in real time units, **never in
steps**; **no global clock may be assumed**, and this section contains a **twenty-four-hour**
biological oscillator that is not one.

## 2. Representation

*(The Representation field is named in CLAUDE.md and its definition is in the spec not in hand. Read
here as: how a structure's parameters and state are laid out in memory. Claude's inference.)*

**The two arrays are the same as everywhere else on the ladder:**

- **`threshold`** — one unsigned integer per neuron, width `ceil(log2(fan_in))` bits, the only
  parameter memory the architecture recognises.
- **`active`** — one bit per neuron, the current output; **state**, counted separately and never
  summed with parameter memory.

**And for nine of ten structures neither array can be allocated, because there is no `N`.** This is
the difference from the two code designs before it, and it is worth stating precisely because the
three files fail in three different places:

- **File 01** had counts for six of eight structures and was blocked on **connectivity** — it knew
  how big the arrays were and not what wired them.
- **File 13** had counts for all four structures and was blocked on **operations** — it could
  allocate and could not express what the structures emit.
- **File 14 is blocked one rung earlier than either, on *extent*.** `N` is unknown for nine of ten.
  An array whose length is unknown is not a partially specified array; it is not an array.

**This is not on the surface-before-touching list, and that is correct rather than an omission.** The
six items on that list are **decisions** — tile geometry, sparsity, topology, scheduling, learning
rules, buffer shapes — things Micky sets and Claude must not. A neuron count is not a decision. It is
a **measurement**, and it is missing from the literature rather than from the project. Nothing in the
conversation can unblock it. **The module therefore records the counts as absent rather than raising
on them as unset**, and the distinction matters because raising suggests something is waiting on a
person.

**Three structures may not be measurable in the form the array wants.** The periaqueductal grey is
defined by function and column, the reticular formation by connectivity and transmitter, and the
caudal ventrolateral medulla's boundary is contested between two parcellations. **A count needs a
border.** For these three, *to derive* promises that an experiment would settle it, and that promise
may not be keepable — so the module marks them **borderless** rather than merely uncounted, and the
two states are distinct in the data.

**One structure needs no activity array at all, and it is not the usual zero.** The pineal has **no
neurons**. It is not a tract (zero because it is fibres) and not a transducer (neurons that store no
threshold): it is a load-bearing loop stage made of secretory cells. What it holds is **a single
scalar concentration varying in time**, plus the state of the gate that drives it. **Nothing in the
`threshold` / `active` vocabulary holds a concentration**, and representing it as a one-neuron
activity bit would assert a spike where there is a slow hormonal ramp. **Recorded as an open
representation case.**

**The one width question the section does raise is trivial and worth saying so.** With every fan-in
unknown and bounded at 16 bits, the derived width *is* the container width — `uint16`, no padding gap
and no bit-packing decision, and at ~50,000 neurons the whole allocatable part of the section is
0.10 MB. **The container question that mattered for V1 does not arise here**, because nothing here is
large enough for it to matter.

## 3. Algorithm — what is writable, and the one thing that would unlock the rest

For a structure `S` with incoming lines `L`:

```
count[j]  = Σ_{i ∈ fan_in(j)} active_source[i]      # equal weights, so a count
active[j] = count[j] ≥ threshold[j]
```

Integer-only, no multiply, no gradient. **Correct for every neuron in this section** — no transducer
and no graded non-spiking population is described among the ten, so `ceil(log2(fan_in))` applies to
every neuron that has a count, which is one sub-element of one entry.

**The section names four operations the model has no term for, and one of them is nearly in reach.**

1. **Sign inversion.** The caudal ventrolateral medulla's output is explicitly sign-inverting:
   excitation there becomes suppression of sympathetic drive at the rostral ventrolateral medulla.
   `count = Σ active_source` has no negative term. **This is the same gap the design file records from
   the outer retina, arriving here on an ordinary spiking edge between two ordinary nuclei** — which
   makes it the cheapest place in the map to fix, because no graded, non-spiking, receptor-level
   mechanism is involved. An inhibitory edge here is a whole population of spiking cells whose effect
   on the target is to reduce its count.

2. **A standing output with no input.** The rostral ventrolateral medulla's presympathetic cells are
   intrinsic pacemakers, so the baroreflex is **a subtraction from a drive that exists without input**
   rather than a signal path. **A stateless threshold gate cannot do this; a threshold gate in a
   delayed feedback loop is an ordinary relaxation oscillator**, and the per-edge-latency invariant
   already supplies the delay. **So this is not a separate missing operation — it is item 1 again**:
   given an inverting term, free-running activity falls out of connectivity and delay with no new
   mechanism. Whether the biology generates it in the membrane or in the circuit is not decidable from
   the source and is owed there.

3. **A gain applied at another structure's first synapse.** The periaqueductal grey's descending
   analgesic output carries **no nociceptive content**; its effect is to change how much of the spinal
   dorsal horn's content gets through. This is file 13's multiplicative-gain problem **on a single
   named edge with a single named target**, which is the tractable instance — it can be written and
   tested without deciding what a brain-wide diffuse modulator does.

4. **A hormonal concentration and a gate.** The pineal's melatonin arm has no fan-in list, no target
   region on one limb, a receptor-bearing consumer on the other, and a latency made of synthesis,
   secretion, circulation and receptor binding. **Nothing in §3 touches any part of it.**

**So the shape of this file's algorithmic gap is different from file 13's.** There, four independent
operations were missing. Here, **two of the four collapse into one** — a sign — and that one is
cheaper to supply than anywhere else on the map. **The module raises on all four and records which
two would close together**, because that is a fact about the work remaining and not a decision.

**`fan_in(j)` is unwritable, and for this section it is not even the binding constraint.** Every
fan-in reads unknown on all eighty edges. But a connectivity map is indexed by neuron, and **for nine
of ten structures there are no neurons to index.** Connectivity is blocked behind extent here, which
inverts the usual order.

## 4. What blocks the implementation, specifically

CLAUDE.md lists six things that must be surfaced to Micky before being touched. **Five are needed here
and none is set** — and a sixth blocker is not on the list and does not belong on it.

| needed for | item | state |
|---|---|---|
| `fan_in(j)`, every structure | **inter-structure connection topology** | not set; and blocked behind extent for nine of ten |
| allocation of every array | **tile geometry** | not set; no map axis is recorded for any structure except the superior colliculus, whose extents are unrecorded |
| whether `active` is dense or sparse | **sparsity** | not set |
| every `register_buffer()` in the module | **buffer shapes** | not set, downstream of the three above |
| the update loop | **the scheduling discipline** | not set, and Micky's — §6 below |
| whether `threshold` is ever written | **the learning rule** | not set |
| **any array at all, for nine of ten structures** | **the neuron counts** | **absent — and this is a measurement, not a decision** |

**The last row is why this file is different.** Every other blocker on the ladder has been a decision
withheld or a rung not yet written. This one is a hole in the literature: the source states, for the
superior colliculus, that it has historically been counted only in single midbrain sections and never
as an unbiased whole-structure stereological figure; for the reticular formation, that it is defined
by connectivity and transmitter rather than by a countable border. **No conversation and no rung
resolves that.** The module records it as absent, does not raise on it as though someone were being
asked, and does not substitute an order-of-magnitude guess.

## 5. Allocation, and the section's one allocatable array

**One array in this section can be sized: the suprachiasmatic nucleus's, at ~50,000 neurons per side,
0.10 MB of `threshold` at the 16-bit bound.** It is a sub-element of the hypothalamus entry, and the
hypothalamus entry cannot be allocated because the other ten sub-nuclei have no counts.

**The granularity mismatch of file 01 recurs and is worse.** There, sizing was stated per structure
and edges terminated on sub-elements, so a partition was missing. Here **the totals themselves are
missing**, so there is nothing to partition — and the edges still terminate on sub-elements: four
separate edges land on named layers of the superior colliculus, two leave the periaqueductal grey's
ventrolateral column specifically, three leave named hypothalamic populations, and one lands on the
saccade burst generators, which are sub-elements of a structure whose sub-elements are **partly
uncountable in principle**.

**Two entries are bundles and are not split here.** The hypothalamus is at least eleven sub-nuclei,
each effectively its own region, recorded as a bundle whose split is owed at the source. The
reticular formation is a set of bordered nuclei plus a borderless mesh. **Splitting either at this
rung would invent the arity**, and the module holds both as single structures carrying a sub-element
list.

## 6. The scheduler, and why the sanctioned shortcut is worst here

Two facts collide as in every section:

1. **Every edge latency reads *to derive*.** There are no numbers to schedule with.
2. **The scheduling discipline is not set and is Micky's.**

**But this section makes the uniform-step shortcut quantitatively bad, and the arithmetic is worth
having.** The sanctioned shortcut is to set every latency equal and choose a step short enough to
carry the finest one. The finest latency in this section is unknown; the auditory section works at
tens of microseconds, which is a floor for *that* section. **The slowest loop in this section has a
twenty-four-hour period.** Taking a step even as coarse as one millisecond:

- 1 ms step → **86,400,000 steps** per circadian period
- 100 µs step → **864,000,000 steps**
- 50 µs step → **1,728,000,000 steps**

**That is the cost of one turn of one loop**, and the module recomputes it rather than quoting it.
The point is not that the number is large; it is that **a single uniform step must simultaneously
resolve a synaptic delay and span a day**, and those differ by eight to nine orders of magnitude
*within this one section*. The design file argues the per-edge-latency invariant from exactly this
spread. Here it is arithmetic.

**And the hazard of file 13 recurs at a slower period.** The suprachiasmatic nucleus is a named
master clock with a twenty-four-hour rhythm sitting in the contract. **It is a biological oscillator
inside the system, not a clock for the system.** A twenty-four-hour period is the sort of number that
invites being treated as a frame boundary; it paces the circadian loop and nothing else. The module
contains no loop, no step counter and no `for t in range(...)`, and where the scheduler would go it
raises, naming the circadian period explicitly so the next reader does not have to rediscover why it
was not used.

## 7. Completion test

*(Inferred, since the rung spec is not in hand: the architecture's completion test for an entry is
that you can say what leaves it on a wire; the analogue at this rung.)*

**A code design entry is finished when the module can be written from it without opening the
architecture and without making an unauthorised decision.**

By that test **this document is not finished, and it fails earlier than either of its predecessors.**
File 01 could size six of eight structures and write their forward operation, blocked on connectivity,
allocation and scheduling. File 13 could size all four and write theirs, blocked additionally on the
operations its payloads name. **This file can size one sub-element of one entry.** Nine of ten
structures have no array to write a forward operation into, and for three of them the missing number
may not be obtainable in the form the array wants.

**What the module does implement, and it is not nothing:**

- the structure, sub-element and edge declarations as data, with every unknown count, every
  borderless structure, every class endpoint, every non-projection edge class and every
  entry-less endpoint marked as such rather than filled;
- the threshold-gate forward operation, correct for every neuron in the section;
- an independent recomputation of the architecture's sizing table, which **re-derives the result that
  one of eleven rows has a number in it** rather than trusting the claim;
- **the transcription cross-check, run mechanically — and it resolves.** The source's header states
  80 edge lines, 39 in and 41 out; the architecture transcribed 40 in and 41 out and attributed the
  extra line to a compound bullet. **Counting the module's own table gives 39 in, 41 out, 80 total —
  the source's figures exactly.** The architecture's extra incoming line was the lateral parabrachial
  entry's **collateral bullet**, which names no producer: it is a qualification on the arity of the
  whole ascending nociceptive system, not an edge. The module carries it as a named note rather than
  dropping it, and prints all three counts side by side on every run. **Two things had to be right for
  this to close**: that an edge with both ends inside the section is written twice in the source, once
  under each entry, so "in" and "out" are positions in a document and not properties of an edge; and
  that a bullet naming no producer is not an edge. Getting either wrong gives a different number,
  which is why the check is worth running rather than reasoning about;
- the uniform-step arithmetic above, computed rather than quoted;
- and a report of the four payload operations with no term in the model, **recording which two of
  them close together given a sign** — which is the one piece of actionable information this file
  produces about the work remaining.
