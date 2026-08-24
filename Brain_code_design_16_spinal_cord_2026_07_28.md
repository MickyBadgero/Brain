# brain_code_design_16_spinal_cord

**Rung:** code design (algorithms). **Spec:** `Brain_architecture_16_spinal_cord_2026_07_28.md`.
**Implements:** `Brain_16_spinal_cord.py`.

**This document's own rung spec was not in hand when it was written.** `brain_code_design_spec_<date>.md`
governs this rung and was not available. The **form** below is taken from the one existing file at this
rung, `brain_code_design_01_visual_pathway`, which was itself written without the spec and says so. So
the shape is a precedent and not a derivation; **the contract in §1 is derived and the form around it
is not.**

**Standalone, not a companion.** Every contract field below is carried **verbatim** from the
architecture rather than referenced. A reader implementing from this file should not need the
architecture open.

---

## 1. Contract — carried verbatim from the architecture

Three structures, in data-flow order. Counting basis is **whole cord, both sides** throughout — a
fourth basis in the set, after per eye, both eyes combined, and per hemisphere.

| # | structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Spinal cord grey matter | whole (both sides) | ~200M (197–222M) | ≤ 16 | ≤ 400 MB (394–444) |
| 1 | — of which lumbosacral motor neurons | whole (both sides) | ~52–62k | ≤ 16 | included above |
| 1 | — per-lamina / per-segment partition | whole (both sides) | to derive | ≤ 16 | to derive |
| 2 | Spinal cord white matter | whole (both sides) | none | — | 0 |
| 3 | Reflex arcs and central pattern generators | — | none (no new tissue) | — | 0, **not additive** |

**Not one fan-in in this file is known** — incoming, outgoing or internal. Every bit-width above is
the 16-bit log₂ cap, not a measured value. Where V1 could at least be bracketed at 12–14 bits from a
disputed synapse count, this section offers nothing to bracket with.

**Three edge latencies are measured, and that is what makes this file different from file 01.** The
lamina-I edge to the posterior / ventromedial-posterior thalamus carries three labelled lines with
central conduction latencies of roughly **131 ms** (nociceptive-specific), **59 ms**
(thermoreceptive-specific) and **72 ms** (polymodal nociceptive). **Three latencies on one anatomical
edge, the slowest 2.2× the fastest.** Every other edge in the section reads *to derive*.

**Shape, verbatim.** Grey matter is rank 4: **(lamina, side, rostrocaudal segment, mediolateral
position)** = **10 × 2 × 31 × to derive**. Three of four extents are known — the only structure in the
map so far whose shape is mostly closed. White matter is **transmission-only**: a routing index, rank
1, length to derive, with the corticospinal tract at order ~1M axons per side the sole fibre count.
The reflex entry has **no array of its own.**

**Edges, with sub-element endpoints** — the ones whose endpoint is finer than a whole structure:

- primary sensory afferents → **laminae I and II** (nociceptive, thermoreceptive) and → **laminae
  III–VI** (low-threshold mechanoreceptive) — *the same bus sorted onto different laminae by modality*
- periaqueductal gray and rostral ventromedial medulla → **lamina II** (the analgesic gate)
- raphe nuclei and hypothalamus → **dorsal horn** and → **intermediolateral cell column**
- rostral ventrolateral medulla → **intermediolateral cell column**
- **lamina I** → thalamus (crossed), lateral parabrachial nucleus, caudal ventrolateral medulla,
  periaqueductal gray — *four edges, largely one population with collaterals, not four populations*
- **laminae III/IV neurokinin-1-receptor-expressing neurons with long dorsal dendrites** → caudal
  thalamus — *a second, separate ascending population*
- **Clarke's column** → cerebellum; **intermediolateral cell column** → sympathetic chain ganglia;
  **motor-neuron pools** → skeletal muscle

**Invariants carried:** whole-structure co-instantiation (three loops close inside the cord — pain
gate, gamma loop, Renshaw); per-edge latency (nonzero, finite, heterogeneous, real time units,
**never in steps**); **no global clock may be assumed.**

## 2. Representation

*(The Representation field is named in CLAUDE.md and its definition is in the spec I do not have. Read
here as: how a structure's parameters and state are laid out in memory. Claude's inference.)*

**Per structure, two arrays and nothing else:**

- **`threshold`** — one unsigned integer per neuron, width `ceil(log2(fan_in))` bits. Under equal
  weights this is the whole of what a neuron stores.
- **`active`** — one bit per neuron, the current output. **State**, counted in a separate class and
  never summed with parameter memory.

**The container question resolves differently here than in file 01, and it resolves cleanly.** Every
threshold in this file is at the 16-bit cap because no fan-in is known, and **16 bits is a machine
integer width.** So `uint16` is exact and there is no bit-packing trade to make: 200M × 2 bytes =
**400 MB derived and 400 MB realised, gap zero.** File 01's 14–33% padding gap came from V1's derived
12–14 bits falling between containers; nothing here falls between containers, because nothing here is
derived at all. **The gap closes for the wrong reason** — not because the widths are known but because
they are all at the ceiling — and it re-opens the moment a single fan-in is measured.

**Element classes present, and the count is higher than file 01's three.**

1. **Threshold gates** — the motor neurons, projection neurons and most interneurons. Specified.
2. **Graded / non-spiking elements** — not typed as such in this file, unlike the retina's. The source
   does not say which spinal interneurons spike. Reads *to derive* and must not default to zero.
3. **Pacemakers.** The rostral ventrolateral medulla's drive onto the intermediolateral cell column is
   **generated by intrinsically pacemaking cells rather than relayed**. **A threshold gate with no
   active inputs never fires**, so a cell that fires from nothing is not a threshold gate under any
   fan-in. That source lies at the far end (file 14) and its *output* is this file's input, so the
   class has to be representable here whether or not it is instantiated here.
4. **Gain edges.** The descending analgesic gate carries **no stimulus content — a gain applied to
   another edge's payload.** This is not an input to a neuron at all; it is a modulation of a
   different edge's transfer function. `count[j] = Σ active_source[i]` has no place to put it. Adding
   it as an ordinary input would make an analgesic signal *excite* the pain line, which is backwards.

**And the sign problem, which in this file is not an exception but the subject.** In file 01 the sign
problem was confined to the outer retina, where hyperpolarisation is the excitatory response. Here
**inhibition is what the cord computes with**, and the source types it explicitly, by name and by
transmitter:

| circuit | what it is | sign |
|---|---|---|
| lamina II inhibitory interneurons → lamina I projection neurons | the substrate of the pain gate | inhibitory |
| Ia inhibitory interneuron → antagonist alpha motor neuron | reciprocal inhibition | inhibitory |
| Ib Golgi-tendon → interneuron → homonymous alpha motor neuron | autogenic inhibition | inhibitory |
| alpha collateral → Renshaw cell → the same and neighbouring motor neurons | recurrent inhibition | inhibitory |
| dorsal-horn interneuron classes | gamma-aminobutyric acid and/or glycine | inhibitory by transmitter |

**Four of the eleven internal edges the source types are inhibitory, and they are the ones the entries
are named for.** Reciprocal inhibition, autogenic inhibition and recurrent inhibition are not
side-channels around the reflexes — they *are* three of the six reflex arcs. **A count of active
inputs compared against a threshold has no term for a negative contribution**, so the forward
operation as specified cannot express the majority of this file's characteristic computations.

**This is a finding about the model and not about the tissue, and it is not this rung's to fix.** The
architecture records the sign problem for the outer retina and says it is a constraint on the model.
File 16 widens it: the constraint is general, and the spinal cord is where it stops being a corner
case. **Whether the threshold-gate model gains a signed term, or these elements are modelled some
other way, is Micky's** — it is a change to the sizing model, which would change the parameter-memory
derivation for every structure in the map, so it belongs above this rung and not in it.

**A fifth class the code will meet and this rung cannot resolve: the plant.** The **gamma loop** runs
gamma motor neuron → intrafusal spindle fibre → Ia afferent → alpha motor neuron, and the intrafusal
fibre is **muscle** — outside the scope boundary by rule at every rung. The same is true of the
stretch reflex, whose input is muscle length. **So the two loops the cord is most famous for cannot be
closed inside the map**, not because a stage is missing from the source but because the missing stage
is declared out of scope on purpose. The architecture states this generally — what moves is not
specified anywhere on the ladder. **Here it is a concrete blocker rather than a note**, because the
loop is short, closed in one segment, and unrunnable without a plant model that no rung provides.

## 3. Algorithm — the part that is fully specified, and how little of this file it covers

For a structure `S` with incoming lines `L`:

```
count[j]  = Σ_{i ∈ fan_in(j)} active_source[i]      # equal weights, so a count
active[j] = count[j] ≥ threshold[j]
```

Integer-only, no multiply, no gradient — consistent with a non-backpropagation architecture, and a
faithful reading of the sizing model.

**In file 01 this covered the forward operation of six of eight structures. Here it covers the
excitatory edges of one structure and no complete circuit.** The stretch reflex needs a muscle; the
other five reflex arcs and the pain gate need a sign; the pattern generator needs both a sign and a
period. **What remains fully writable is the monosynaptic excitatory edge, and it terminates in a
plant that does not exist.**

**`fan_in(j)` is unwritable here for a reason file 01 did not have.** In file 01 the topography was in
the biology and recorded as prose — retinotopy, a space-variant compression ratio — so the function
existed and only its authorisation was missing. Here **the pattern is not in the source at all.**
Which Ia line reaches which alpha motor neuron *is* the somatotopic map; the source records the map
qualitatively (medial axial, lateral distal limb; flexor dorsal, extensor ventral) and gives **no
correspondence rule, no pitch, and no fan-in anywhere in the file.** Writing `fan_in(j)` would mean
inventing the somatotopy, not merely formalising it — and it is the inter-structure connection
topology, which is a surface-before-touching item.

## 4. What blocks the implementation, specifically

CLAUDE.md lists six things that must be surfaced to Micky before being touched, each triggering a
fresh start. **Four of the six are required to write this module and none is set** — the same four as
file 01, plus two blockers that are this file's own and are not on that list.

| needed for | item | state |
|---|---|---|
| `fan_in(j)`, every edge | **inter-structure connection topology** | not set — §3 |
| the mediolateral axis, and per-segment counts | **tile geometry** | not set — §5 |
| whether `active` is dense or sparse | **sparsity** | not set |
| every `register_buffer()` in the module | **buffer shapes** | not set, downstream of the three above |
| the update loop | **the scheduling discipline** | not set, and Micky's — §6 |
| whether `threshold` is ever written | **the learning rule** | not set |
| **the forward operation itself** | **a signed term in the threshold-gate model** | **not set, and above this rung — §2** |
| **closing the gamma and stretch loops** | **a plant model for muscle** | **out of scope at every rung — §2** |

**The learning rule's absence is again the least blocking.** A threshold that is never written is a
construction cost rather than a memory; the module holds `threshold` as read-only and is honest about
not learning.

**The sign gap is the most blocking, and it is new at this file.** Every other item on the list blocks
*building* the module. This one blocks *stating what the module computes*, because a forward operation
that drops the inhibitory edges does not approximate the spinal cord — it produces a cord in which
antagonist muscles co-contract, motor output has no gain control, and analgesia is excitatory.

## 5. Allocation — three of four axes close, and the fourth is not the blocker

**This is the first file at this rung whose shape mostly resolves.** The grey matter's array is
**(lamina, side, rostrocaudal segment, mediolateral position)** and three extents are stated outright:
**10** Rexed laminae, **2** sides, **31** segments (8 cervical, 12 thoracic, 5 lumbar, 5 sacral, 1
coccygeal). Only the mediolateral extent reads *to derive*, and there is no measured tile pitch
anywhere in the file to close it with.

**But the array is ragged, and that blocks allocation harder than the open axis does.** Three of
lamina VII's named cell groups exist over sub-ranges of the segment axis:

- **Clarke's column / nucleus dorsalis** ≈ **C8–L2/3**
- **intermediolateral cell column** ≈ **T1–L2/3**
- **sacral parasympathetic nucleus** — **S2–S4**

A dense `10 × 2 × 31 × M` allocation **asserts tissue at levels where the source says there is none.**
The two enlargements are the same fact on the same axis from the other direction: the cervical and
lumbosacral segments carry limb motor pools and the thoracic segments do not.

**So the partition, not the geometry, is what stops the allocator.** Dividing 200M evenly across the
620 lamina-side-segment cells gives ~322,600 each, and that number is an invention: it asserts a
uniform cord against a source that describes two enlargements and three level-restricted nuclei. The
only counted subpopulation is the lumbosacral motor pool at ~52–62k, which is **0.026–0.031%** of the
total and constrains almost nothing about the other 99.97%.

**This is the same granularity mismatch file 01 found, arriving from the opposite direction.** There,
sizing was per structure and edges terminated on sub-elements that had no counts. Here the sub-element
*axes* are known and the counts along them are not. **Knowing the shape of an array does not size it**,
and this file is the clean demonstration.

## 6. The scheduler — and here the clock question is observable in the output

File 01 could not write a scheduler because it had no latencies to schedule with. **This file has
three**, and it still cannot, for a different and sharper reason.

Two facts:

1. **Three latencies are measured** — 131, 59 and 72 ms on one edge. So the sanctioned shortcut
   *does* have a parameter here: setting every latency equal and choosing a step short enough to
   carry the finest one has a finest one to point at, at least on that edge.
2. **The scheduling discipline is not set and is Micky's** — explicitly not the architecture's and
   explicitly not this rung's.

**And the locomotor central pattern generator is why the shortcut would be wrong anyway.** It
generates the alternating flexor / extensor and left / right pattern **without descending command and
without sensory feedback** — a network that manufactures a temporal pattern out of a tonic input. Its
period is set by the delays and time constants inside it. Break those with a uniform update step and
**the walking rate becomes a property of the step size.** The architecture's claim — that a loop with
real heterogeneous delays and the same loop broken by registers are two different systems computing
two different things — is usually an argument about correctness that cannot be checked. **Here it can
be: the difference shows up as a number in the output.**

So the module contains no loop, no step counter, and no `for t in range(...)`. Where the scheduler
would go, it raises.

**What the module can do that file 01's could not: state edge storage as a function.**
`edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value` has two of three terms
available on the thalamic edge — real latencies, and `bytes_per_value` = 1 bit for a binary `active`.
The module exposes this as a function taking `update_interval` and `line_count` as arguments and
**refuses to supply a default for either**. Supplying one would be choosing the scheduling discipline
in a helper.

## 7. Completion test

*(Inferred, since the spec is not in hand: the architecture's completion test for an entry is that you
can say what leaves it on a wire; the analogue at this rung.)*

**A code design entry is finished when the module can be written from it without opening the
architecture and without making an unauthorised decision.**

By that test **this document is not finished, and cannot be finished at this rung** — and it is
further from finished than file 01's was. There, the forward operation was writable and only the
connectivity, allocation and scheduling were blocked. Here the **forward operation itself is not
writable for the majority of the file's circuits**, because the model has no term for inhibition and
the source's own naming makes inhibition the subject.

**What the module does implement, and it is not nothing:** the structure, edge and internal-edge
declarations as data, with signs carried where the source types them; the threshold-gate forward
operation for the excitatory case; the three measured latencies in real seconds; the edge-storage
formula as a function of an unset update interval; the ragged-array check that reports which
(lamina, segment) cells the source denies; and an independent recomputation of the architecture's
sizing table from counts and fan-ins. That last re-derives the numbers rather than trusting them,
which the fidelity procedure asks for and which no prose pass can do.
