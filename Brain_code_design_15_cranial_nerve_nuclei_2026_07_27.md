# Brain code design — 15 cranial nerve nuclei

**Rung:** code design (algorithms). **Spec:** `Brain_architecture_15_cranial_nerve_nuclei_2026_07_27.md`.
**Implements:** `Brain_15_cranial_nerve_nuclei.py`.

**This document's own rung spec was not in hand when it was written.**
`Brain_code_design_spec_<date>.md` governs this rung and was not available, so the shape of this file
is Claude's inference from the field names CLAUDE.md lists in passing and from the file-01, file-13
and file-14 code designs. Treat the *form* as a candidate and the *contract* below as derived.

**Standalone, not a companion.** Every contract field below is carried **verbatim**. A reader
implementing from this file should not need the architecture open.

---

## 1. Contract — carried verbatim from the architecture

Four entries, **all four of them bundles**. **Counting basis: per side** throughout, following the
source's convention for this section, with one sub-element (the spinal accessory nucleus) lying in
upper cervical cord and gathered here for its nerve.

| # | structure / sub-element group | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Ocular motor nuclei — all four sub-elements | per side | soft, order 10³–10⁴ | ≤ 16 | to derive |
| 2 | Branchiomotor / visceromotor — **facial nucleus** | per side | **~10,000** | ≤ 16 | **≤ 0.02 MB** |
| 2 | Branchiomotor / visceromotor — the other seven pools | per side | soft, order 10³–10⁴ | ≤ 16 | to derive |
| 3 | Trigeminal sensory — mesencephalic nucleus | per side | soft, order 10³ | **0 (transducer)** | to derive |
| 3 | Trigeminal sensory — principal and spinal nuclei | per side | soft | ≤ 16 | to derive |
| 4 | Pretectum — olivary pretectal nucleus | per side | unknown, **bordered and countable** | ≤ 16 | to derive |
| 4 | Gaze integrators — prepositus hypoglossi, interstitial nucleus of Cajal | per side | unknown | ≤ 16 | to derive |
| | **stated total** | per side | **~10,000 counted** | | **≤ 0.02 MB per side** |

**Every fan-in and fan-out reads *unknown*, and every edge latency reads *to derive*.** No conduction
time and no synaptic delay appears anywhere in the section.

**Twenty-four edges — 13 in, 10 out, 1 internal.** The internal edge is the only one in the section
and **the only edge that crosses the midline**: abducens internuclear neurons → the contralateral
oculomotor medial-rectus pool, carrying **a copy of the abducens's own lateral-rectus drive and no
independent command**.

**Six endpoints are peripheral and are termini, not owed edges:** extraocular striated muscle, the
ciliary ganglion, orofacial striated muscle, the cranial parasympathetic ganglia, the trigeminal
ganglion (a source), and the jaw-muscle spindles and periodontal receptors (also a source).

**Edges whose endpoint is finer than a whole structure:**

- burst generators → **abducens** (horizontal) and → **oculomotor / trochlear** (vertical)
- gaze integrators → the ocular motor nuclei; pretectum → **Edinger-Westphal nucleus, preganglionic
  subdivision, bilaterally**, onto a **distinct pupillary subpopulation** and not the
  lens-accommodation cells sharing the nucleus
- corticobulbar → **facial pool**, with upper-face motoneurons receiving **bilateral** input and
  lower-face **contralateral only**
- solitary nucleus → **dorsal motor nucleus of the vagus**; pattern generators → the rhythmic pools
- trigeminal ganglion → **principal** (discriminative touch) and **spinal** (pain and temperature)
- **mesencephalic** → trigeminal motor nucleus (jaw-jerk); **principal** and **spinal** → ventral
  posteromedial thalamus; **spinal** → the branchiomotor pools

**Two bullets name several endpoints**: four producers onto the integrators and burst generators, and
four consumers of the olivary pretectal nucleus's ascending and descending outputs.

**Invariants carried:** whole-pathway co-instantiation — **the oculomotor loop closes onto muscle
here**, with one joint still open because file 14 names these nuclei only as a class; per-edge
latency, nonzero, finite, heterogeneous, in real time units, **never in steps**; **no global clock**.
**Two edges carry a timing requirement with no number**: the vestibulo-ocular reflex is the fastest
gaze-stabilising reflex, and the jaw-jerk is monosynaptic.

## 2. Representation

**The two arrays as everywhere else** — `threshold`, one unsigned integer per neuron at
`ceil(log2(fan_in))` bits, and `active`, one bit per neuron of state.

**One array in the section can be allocated: the facial motor nucleus's**, at ~10,000 neurons per
side and ≤ 0.02 MB at the 16-bit bound. Everything else has no count.

**But the extent gap here is repairable in a way file 14's was not, and the module records the
difference.** File 14 held three structures defined without a countable border, where a count may not
be well posed. **Every structure in this section has a border — they are nuclei defined by a nerve** —
and two have a named route to a figure: the olivary pretectal nucleus has definite borders in macaque
with its projection cells already labelled and no human figure yet looked up, and **every motor pool
here can be cross-checked against the myelinated-axon count of its own nerve**, which is how the
facial figure was corroborated. So the module marks these **countable-but-uncounted**, a third state
alongside file 14's *uncounted* and *borderless*.

**Three representation cases the two arrays do not cover.**

1. **A value held against decay.** The gaze integrators' whole function is to hold **eye position** —
   the time integral of a velocity command — between saccades. `active` is one bit; `threshold` is a
   parameter nothing writes. **Neither is a value stored and read back.** This is the first structure
   in the map whose declared function is to store something, and the source records the internal
   mechanism as unknown and names it as work for a lower rung.
2. **A transducer that projects.** The mesencephalic nucleus's cells are **primary sensory neurons
   with somata inside the central nervous system, the only ones in the body.** Under §6 a transducer
   stores no threshold — but these transducers also project monosynaptically onto the trigeminal motor
   nucleus, which the retina's photoreceptors do not. **The element-class vocabulary assigns the cell
   to one class while its edges require another**, and the module carries a flag rather than choosing.
3. **A peripheral interface.** Six endpoints lie outside the scope boundary with **definite named
   targets** — the lateral rectus, the ciliary ganglion, the trigeminal ganglion. This differs from
   file 14's endocrine terminal, which had no target region at all. **An edge to nowhere has no
   consumer to write; an edge to a named out-of-scope effector has an interface a later rung must
   supply**, and the module records which is which so the two are not conflated.

**The width question is trivial here, as in file 14.** Fan-in unknown and bounded at 16 bits means the
derived width is the container width, `uint16`, and at ~10,000 neurons nothing is large enough for
bit-packing to matter.

## 3. Algorithm — and for the first time, something fits

```
count[j]  = Σ_{i ∈ fan_in(j)} active_source[i]      # equal weights, so a count
active[j] = count[j] ≥ threshold[j]
```

**The olivary pretectal nucleus's described computation is this operation and not an approximation of
it.** The nucleus converges a very wide retinal field — receptive fields averaging about **31°**, with
retinal terminals concentrating inside its borders and the projection cells' dendrites branching
heavily through that core — and emits **a scalar: how much light.** A count of active inputs over a
large fan-in, compared against a threshold, *is* spatial integration to a scalar. **The ~31° figure is
a statement about the size of the fan-in.**

**The module implements it, and that is the first working demonstration on this ladder.** Three
consecutive code designs have listed what the model cannot express; a model that only ever fails is
not being tested. What the demonstration needs and does not have is the actual fan-in and the actual
threshold, so it runs on a stated fan-in and reports that the parameters are illustrative — but the
*operation* is the contract's, unmodified.

**Three things do not fit.**

1. **Hold a value against decay** — the gaze integrators. Nothing in `active` or `threshold` persists
   and is read back. **Blocked.**
2. **Sign inversion** — implicit here rather than stated as a named inhibitory edge, but the
   pupillary-motoneuron asymmetry (pupillary cells receive **more inhibitory input** than the lens
   cells beside them) is a quantitative claim about inhibition that the model cannot record, because
   it has no inhibitory term to be more or less of. **Blocked, and it is the same gap as everywhere.**
3. **A payload that is a copy, not a command** — the yoking edge. This is expressible and the module
   expresses it, but it carries a build constraint worth writing down: **the medial-rectus pool must
   not be given an independent input that could disagree with the lateral-rectus drive**, because the
   whole point of the edge is that the two cannot disagree.

**And the section names a candidate that would close two gaps at once.** Recurrence plus delay plus a
sign gives an oscillator at one parity and a **latch** at the other. File 14's intrinsic pacemaker and
this file's integrator may therefore want **one** addition to the model rather than two, and it is the
inverting term the sign gap has been asking for since the outer retina. **This is generative — offered
to be checked, not asserted** — and what would test it is whether a held eye position degrades
gracefully or not at all, which the source does not say.

**`fan_in(j)` is unwritable**, as everywhere: every fan-in on all twenty-four edges reads unknown. One
of them is qualified — the retinal input to the olivary pretectal nucleus is **high by construction**,
which is a direction and not a number.

## 4. What blocks the implementation

| needed for | item | state |
|---|---|---|
| `fan_in(j)`, every structure | **inter-structure connection topology** | not set |
| allocation of every array | **tile geometry** | not set; no map axis is recorded, though a motor pool plausibly has one since muscles are discrete |
| whether `active` is dense or sparse | **sparsity** | not set |
| every `register_buffer()` | **buffer shapes** | not set, downstream of the above |
| the update loop | **the scheduling discipline** | not set, and Micky's |
| whether `threshold` is ever written | **the learning rule** | not set |
| **any array for six of seven sub-element groups** | **the neuron counts** | absent — a measurement, and here a **repairable** one |

**And one blocker that is genuinely new at this rung: the state model itself.** The integrator needs a
held value, which is neither a parameter nor an activity bit. **Adding one is a decision about what a
structure stores**, which is closer to the learning-rule item than to anything else on the list — and
it is not on the list. The module raises rather than choosing, and flags that the item may belong on
the surface-before-touching list. **That is a question for Micky and is asked in the conversation, not
parked here.**

## 5. Allocation

**One array: the facial motor nucleus's.** Every other sub-element group has no count.

**All four entries are bundles and none is split here.** Four sub-elements gathered by function rather
than neighbourhood, with the trochlear and abducens at different brainstem levels; **eight** motor
pools from pons to upper cervical cord; three trigeminal nuclei with the spinal one subdividing into
pars oralis, interpolaris and caudalis; and **two structures that share no edge with each other.**
Splitting any of them here would invent the arity.

**The sub-elements are load-bearing everywhere and the edges prove it** — the burst-generator and
integrator inputs segregate by axis, the light reflex goes specifically to a distinct pupillary
subpopulation, the corticobulbar rule attaches to the facial pool, and every trigeminal output leaves
from a named nucleus. **So allocation needs the partition in all four entries and has it in none.**

## 6. The scheduler

Every latency reads *to derive*; the scheduling discipline is not set and is Micky's. The sanctioned
uniform-step shortcut has no parameter, because the finest latency is unknown.

**This section states two timing requirements without numbers**, and they are the kind a scheduler
would be sized against: the vestibulo-ocular reflex is **the fastest gaze-stabilising reflex**, which
is a claim that its total loop delay must beat the head movement it corrects; and the jaw-jerk is
**monosynaptic**, which sets a floor as anatomy rather than as a figure. **A section that names the
tightest timing constraint in the map and supplies no time is exactly the case the per-edge-latency
invariant is written for.**

The module contains no loop, no step counter and no `for t in range(...)`. Where the scheduler would
go, it raises.

## 7. Completion test

**A code design entry is finished when the module can be written from it without opening the
architecture and without making an unauthorised decision.**

By that test **this document is not finished** — six of seven sub-element groups have no array to
write a forward operation into, no connectivity can be built, and no updates can be scheduled.

**But it fails less completely than the three before it, and in a different direction.** File 01 was
blocked on connectivity, file 13 on operations, file 14 on extent with three structures possibly
unmeasurable. **Here every structure has a border, two have a named route to a count, and one
described computation is implementable today.**

**What the module implements:**

- the structure, sub-element and edge declarations as data, with peripheral termini, recorded
  non-edges, transducer-class cells, countable-but-uncounted structures and bundles all marked;
- the threshold-gate forward operation;
- **a working spatial integrator** — the olivary pretectal nucleus's luminance computation, run on an
  illustrative fan-in, demonstrating that the contract's operation produces the contract's payload;
- an independent recomputation of the sizing table, re-deriving that one of seven rows has a number;
- **the edge-count cross-check**, which must handle a subtlety this file shares with file 14: **one of
  the thirteen incoming bullets is explicitly not an edge.** The ocular-motor entry lists the superior
  colliculus and frontal eye fields among its inputs and states in the same bullet that there is **no
  direct edge**. Counting bullets gives 13; counting edges gives 12. **Both numbers are printed and
  the difference is named**, because two files running have now produced a one-line drift from exactly
  this shape;
- and a report of what the model cannot express, **with the latch-and-oscillator candidate recorded as
  generative** rather than as a finding.
