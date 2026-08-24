# Brain code design — 13 neuromodulatory systems

**Rung:** code design (algorithms). **Spec:** `Brain_architecture_13_neuromodulatory_systems_2026_07_27.md`.
**Implements:** `Brain_13_neuromodulatory_systems.py`.

**This document's own rung spec was not in hand when it was written.**
`brain_code_design_spec_<date>.md` governs this rung and was not available, so **the shape of this
file is Claude's inference** from the field names CLAUDE.md lists in passing — standalone-not-
companion, verbatim contract fields, a Representation field, a completion test — and from the file-01
code design, which was written under the same limitation. Treat the *form* as a candidate and the
*contract* below as derived.

**Standalone, not a companion.** Every contract field below is carried **verbatim** rather than
referenced. A reader implementing from this file should not need the architecture open.

---

## 1. Contract — carried verbatim from the architecture

Four structures. **Counting basis is not uniform and two of the four declare no basis at all** — the
source states no basis for the ventral tegmental area or the basal forebrain, so their basis reads
*to derive* and a factor of two sits between the two readings.

| # | structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Ventral tegmental area — all cell classes | to derive | order 10⁵ | ≤ 16 | ≤ 0.20 MB |
| 1 | — dopaminergic ~65% | to derive | ~65,000 | ≤ 16 | ≤ 0.13 MB |
| 1 | — GABAergic ~30% | to derive | ~30,000 | ≤ 16 | ≤ 0.06 MB |
| 1 | — glutamatergic ~5% | to derive | ~5,000 | ≤ 16 | ≤ 0.01 MB |
| 2 | Locus coeruleus | per side | ~50,000 | ≤ 16 | ≤ 0.10 MB |
| 3 | Raphe — dorsal raphe only | whole (midline) | ~235,000 | ≤ 16 | ≤ 0.47 MB |
| 3 | Raphe — median and caudal | whole (midline) | to derive | ≤ 16 | to derive |
| 4 | Basal forebrain — cholinergic only | to derive | order 10⁵ | ≤ 16 | ≤ 0.20 MB |
| 4 | Basal forebrain — GABAergic and glutamatergic | to derive | to derive | ≤ 16 | to derive |
| | **stated total** | mixed | ~485,000 | | **≤ 0.97 MB** |

**Every fan-in and every fan-out in this section reads *unknown* at the source**, so every bits/neuron
figure above is the 16-bit log₂ ceiling and not a measured width. **Every edge latency reads *to
derive*.** The section records no conduction time and no synaptic delay anywhere.

**Forty-five edges, twenty in and twenty-five out, and not one has both ends inside this file.** The
four structures do not connect to each other. Far ends live in files 8, 9, 10, 11, 12, 14, 16 and 17.

**Edges whose endpoint is finer than a whole structure** — the ones that constrain allocation:

- lateral habenula → **rostromedial tegmental nucleus** → ventral tegmental area — an inverting relay
  that is a structure on the edge and has no entry in this section
- ventral pallidum → the ventral tegmental area's **local GABAergic population** (disinhibition)
- basal forebrain **medial septum, cholinergic cells** → hippocampus, via the fornix pre-commissural
  limb — **by volume transmission**
- basal forebrain **medial septum, parvalbumin GABAergic cells** → **hippocampal inhibitory
  interneurons**, via the fornix — the theta phase reference
- basal forebrain **medial septum, glutamatergic cells** → hippocampus, via the fornix — a tonic gate
- basal forebrain **parvalbumin GABAergic** → cortical inhibitory interneurons; and → thalamic
  reticular nucleus
- basal forebrain **cholinergic** → thalamic reticular nucleus — **opposite in sign** to the line above
- basal forebrain **nucleus basalis of Meynert** → the entire cerebral cortex
- raphe, **caudal division** → spinal dorsal horn and intermediolateral cell column

**Fourteen endpoints name a class rather than a structure** — counted mechanically from the edge
table, not eyeballed — and all fourteen are inherited from the source, which marks each owed:
prefrontal cortex three times, as an input to three different structures; the entire cerebral cortex
three times, as an output of three of them; thalamus; striatum; the limbic system; limbic and
prefrontal cortex; brainstem; and three "further targets beyond those named" remainders. **That is
just under a third of the section's forty-five edges**, and the cortical ones are the load-bearing
cases: an edge to "the entire cerebral cortex" is one line standing in for every cortical entry in
the map.

**Invariants carried:** whole-pathway co-instantiation — **and no loop in this section closes inside
it**; per-edge latency, nonzero, finite, heterogeneous, in real time units, **never in steps**; **no
global clock may be assumed.**

**One edge is not conduction plus synaptic transmission.** The medial septum's cholinergic edge to the
hippocampus is delivered largely by **volume transmission** — about 93% of cholinergic varicosities in
the hippocampus form no classic synapse, so the transmitter reaches its targets by **diffusion**
through the extracellular space.

## 2. Representation

*(The Representation field is named in CLAUDE.md and its definition is in the spec not in hand. Read
here as: how a structure's parameters and state are laid out in memory. Claude's inference.)*

**Per structure, the same two arrays as everywhere else on the ladder:**

- **`threshold`** — one unsigned integer per neuron, width `ceil(log2(fan_in))` bits. The only
  parameter memory the architecture recognises.
- **`active`** — one bit per neuron, the current output. **State**, counted in a separate class and
  never summed with parameter memory.

**And in this section that is provably not enough, which is the difference from file 01.** File 01's
representation was blocked on missing *numbers* — a partition, a pitch, a topology. This one is
blocked on a missing *operation*. Three of the four structures emit a payload for which no array
above holds anything and no operation in §3 does anything.

**Every element here is a threshold gate, and that is the one thing that is simple.** There are no
transducers in this section and no graded non-spiking populations are described; the dopaminergic,
GABAergic, glutamatergic, noradrenergic, serotonergic and cholinergic populations all spike. So the
three-code-path problem of file 01 does not recur, and `ceil(log2(fan_in))` applies to every neuron
counted. **All of the difficulty has moved from the elements to the edges.**

**The widths are small enough that the container question inverts.** With every fan-in unknown and
bounded at 16 bits, the derived width **is** the container width: `uint16` with no padding gap and no
bit-packing decision to make. The whole section fits in **under one megabyte** of `threshold` array —
which is the point at which a realisation note stops being about memory and starts being about
whether the arrays are worth allocating separately from their consumers at all. **That is a compute
and layout question and it belongs at this rung**, and it cannot be answered until the connection
topology is set, because a structure that projects brain-wide may be cheaper to hold beside each
consumer than to hold once and route from.

## 3. Algorithm — the part that is fully specified, and the part that is not

For a structure `S` with incoming lines `L`:

```
count[j]  = Σ_{i ∈ fan_in(j)} active_source[i]      # equal weights, so a count
active[j] = count[j] ≥ threshold[j]
```

That is the whole forward operation and it is a faithful reading of the architecture's sizing model.
Integer-only, no multiply, no gradient.

**It runs for the four structures' own neurons, and it does not express what any of them sends.**
This is the central finding of this file and it is not the same finding as file 01's.

The architecture carries four payload descriptions from the source, and each names an operation:

1. **A scalar that multiplies the effective strength of whatever other edges are active** — the locus
   coeruleus's global gain. `count[j] = Σ active_source[i]` has **no multiplicand**. A gain edge is
   not one more active input; if it were modelled as one, doubling the arousal signal would move the
   count by one and the sum would saturate, which is not what a gain does. Writing
   `count[j] = g · Σ active_source[i]` is a different model — it reintroduces a multiply, and with it
   a graded value the threshold-gate model was adopted to remove.
2. **A reward-prediction error used as a three-factor plasticity signal gating cortico-striatal
   synaptic change** — the ventral tegmental area's striatal edge. This does not change `active` at
   all. It changes what the receiving structure **stores**, which is `threshold`, and **nothing writes
   `threshold`, because no learning rule is set.**
3. **A tonic gain delivered by volume transmission** — the medial septum's cholinergic hippocampal
   edge. Not point-to-point: the transmitter reaches a **volume**, not a fan-in list, so there is no
   `fan_in(j)` to write for it even in principle. It is the one edge in the section whose connectivity
   is not a missing map but a **wrong data structure**.
4. **A phase reference from a 4–12 Hz intrinsic membrane oscillation** — the septo-hippocampal
   parvalbumin edge. A time, not an amount. Nothing in `active` or `threshold` holds a phase.

**So the forward operation is writable and the section's function is not.** A module that implements
only §3 implements the four structures as ordinary threshold-gate populations whose outputs do
nothing distinctive, which is a faithful implementation of the arrays and an unfaithful
implementation of the biology. **The module therefore raises where each of the four operations would
go**, rather than choosing one, and the four are listed in §4 as what they are: a modelling decision
above this rung.

**`fan_in(j)` is unwritable here for the same reason as in file 01, and for one more.** The
architecture gives fan-in as *unknown* on every edge — not a scalar to be turned into a map, but no
scalar at all. And where file 01 at least had the pattern stated in prose (retinotopy, a
space-variant compression ratio), this section has **the opposite of a pattern**: brain-wide diffuse
projection with a single axon branching to multiple non-adjacent territories, and **fourteen
endpoints that name a class rather than a structure**. There is no geometry to write down and no
target list to write it against.

## 4. What blocks the implementation, specifically

CLAUDE.md lists six things that must be surfaced to Micky before being touched, each triggering a
fresh start. **Five of the six are required to write this module and none is set** — one more than
file 01, and the extra one is the learning rule.

| needed for | item | state |
|---|---|---|
| `fan_in(j)`, every structure | **inter-structure connection topology** | not set — and §3 above, with no prose pattern to fall back on |
| allocation of every array | **tile geometry** | not set; and no map axis is recorded for any structure here, so the usual tile question may not even be the right one |
| whether `active` is dense or sparse | **sparsity** | not set — and see below, because this section is where the answer probably matters most |
| every `register_buffer()` in the module | **buffer shapes** | not set, downstream of the three above |
| the update loop | **the scheduling discipline** | not set, and Micky's — §6 below |
| **the reward-prediction-error edge to have any effect at all** | **the learning rule** | not set — and here it is not a deferral, §5 below |

**Sparsity is worth naming as different here.** The architecture records that these are tiny
populations with brain-wide reach — ~50,000 locus coeruleus neurons addressing the entire cortex. A
dense `active` array for the source costs nothing at that size; the fan-out **map** is where the
storage goes, and fan-out is never stored in the sizing model. So this is the section where the
sizing model's silence about fan-out and the unset sparsity decision meet, and the module cannot say
what it costs to connect what it can cheaply hold. **Recorded, not resolved, and not this rung's to
resolve.**

## 5. The learning rule stops being the harmless one

File 01's code design recorded the learning rule as **the least blocking of the six**, on the
architecture's own ground that a threshold which is never written is a construction cost and not a
memory, so a module with `threshold` as a read-only buffer is honest and simply does not learn.

**That argument does not survive this file.** The ventral tegmental area's declared function on its
striatal edge is to carry the teaching signal that gates cortico-striatal synaptic change. With no
learning rule, that edge has no consumer and the structure has **no described effect at all** — not a
reduced one. The module can still be written, and it is still honest, but what it is honest about has
changed: it is no longer "this runs open-loop", it is "**this structure's entire output is a no-op**."

**The module therefore raises on the plasticity edge rather than silently dropping it**, which is the
difference between a module that does not learn and a module that quietly pretends the edge was never
there. **Choosing the rule is on the surface-before-touching list and is not taken here.**

## 6. The scheduler cannot be written, and this section adds a specific hazard

Two facts collide, exactly as in file 01:

1. **Every edge latency in this section reads *to derive*.** There are no numbers to schedule with.
2. **The scheduling discipline is not set and is Micky's**, explicitly not the architecture's and
   explicitly not Claude's.

The sanctioned shortcut — set every latency equal and choose a step short enough to carry the finest
one — has no parameter here either, because the finest one is not known.

**And there is a live temptation in this file that is not in file 01.** This section contains a real
oscillator: the septo-hippocampal parvalbumin edge carries the phase of a **4–12 Hz** rhythm whose
tick is an intrinsic membrane current. It is a number, it has units of time, it is periodic, and it is
sitting in the contract. **It is not a clock for this module and must not become one.** It is a
payload on one edge between two named structures, one of which is not in this file; it paces the
hippocampus and nothing else; and adopting it as an update rate would do exactly what the
no-global-clock argument forbids — convert a set of loops with heterogeneous delays into an iterated
map whose trajectory depends on the rate. **The fact that the biology contains an oscillator is not
the fact that the system contains a clock.**

The module therefore contains no loop, no step counter, and no `for t in range(...)`. Where the
scheduler would go, it raises, and the raise names the theta rhythm explicitly so that the next reader
does not have to rediscover why it was not used.

## 7. Completion test

*(Inferred, since the rung spec is not in hand: the architecture's completion test for an entry is
that you can say what leaves it on a wire; the analogue at this rung.)*

**A code design entry is finished when the module can be written from it without opening the
architecture and without making an unauthorised decision.**

By that test **this document is not finished and cannot be finished at this rung** — and it fails
differently from file 01. File 01 could size six of eight structures and write their forward
operation, and was blocked on connectivity, allocation and scheduling. This file can size all four
structures' recorded populations and write their forward operation, and is blocked on all of the same
things **plus the operations the payloads name**. The gap is not that the module cannot be wired; it
is that **three of the four structures would still not do their jobs if it were.**

**What the module does implement, and it is not nothing:**

- the structure, population and edge declarations as data, with every class endpoint and every unknown
  fan-in marked as such rather than filled;
- the threshold-gate forward operation, which is correct for every neuron in the section, since no
  transducer and no graded non-spiking population is described here;
- an independent recomputation of the architecture's sizing table from counts and fan-in bounds —
  re-deriving the ≤ 0.97 MB rather than trusting it;
- the source's own internal cross-check, run as code: the dorsal raphe's ~165,000 serotonergic neurons
  as about a third of the brain's serotonergic population gives ~495,000, which is inside the stated
  order of 10⁵–10⁶. **Two independently recorded statements about one quantity, checked mechanically.**
- and a report of the four payload operations the model has no term for, so that the gap is visible
  when the module is run rather than only when this document is read.
