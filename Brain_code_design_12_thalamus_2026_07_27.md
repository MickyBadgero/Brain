# Brain code design — 12 thalamus

**Date:** 2026-07-27
**Rung:** code design (algorithms). **Spec:** `Brain_architecture_12_thalamus_2026_07_27.md`.
**Implements:** `Brain_12_thalamus.py`.

**This document's own rung spec was not in hand when it was written.**
`Brain_code_design_spec_<date>.md` governs this rung and was not handed over, so **the shape of this
file is Claude's inference** — from the field names CLAUDE.md lists in passing (standalone-not-
companion, verbatim contract fields, a Representation field, a completion test) and from the file 01
code design, which records the same gap on its own face. Treat the *form* as a candidate and the
*contract* below as derived.

**Standalone, not a companion.** The architecture is too large to co-load with this file, so every
contract field below is carried **verbatim** rather than referenced. A reader implementing from this
file should not need the architecture open.

---

## 1. Contract — carried verbatim from the architecture

Eight structures, in data-flow order. **Counting basis is uniform: per side throughout.**

| # | structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Mediodorsal nucleus | per side | ~10M | ≤ 16 | ≤ 20.0 MB |
| 2 | Pulvinar | per side | ~13–26M | ≤ 16 | ≤ 26.0–52.0 MB |
| 3 | Posterior / ventromedial-posterior thalamus | per side | to derive | ≤ 16 | to derive |
| 4 | Ventral anterior / ventral lateral nuclei | per side | to derive | ≤ 16 | to derive |
| 5 | Anterior nuclei | per side | to derive | ≤ 16 | to derive |
| 6 | Intralaminar nuclei | per side | to derive | ≤ 16 | to derive |
| 7 | Thalamic reticular nucleus | per side | to derive | ≤ 16 | to derive |
| 8 | Zona incerta | per side | to derive | ≤ 16 | to derive |

**Stated total ~46.0–72.0 MB, and it is a floor twice over**: six of eight structures are uncounted,
and the two that are counted take the 16-bit ceiling rather than a measured width.

**Every fan-in in this section reads *to derive*.** Not one structure has a convergence figure of any
kind — not a range, not a disputed pair, nothing. That is a harder state than file 01's, where V1's
fan-in was open across a 6.5× range that the log₂ bound closed to 12–14 bits.

**Three edge latencies are measured, and all three sit on one edge.** The lamina-I stream into the
posterior / ventromedial-posterior territory is three labelled lines with three mean central
conduction latencies: thermoreceptive-specific ≈ **59 ms**, polymodal nociceptive ≈ **72 ms**,
nociceptive-specific ≈ **131 ms**. Species: cat. **Every other edge in the section reads *to
derive*.**

**Edges whose endpoint is finer than a whole structure** — the ones that constrain allocation:

- intralaminar, **centromedian nucleus** → motor striatum; intralaminar, **parafascicular nucleus** →
  associative / limbic striatum. *Two named sub-elements, two different targets.*
- pulvinar, **anterior pulvinar** → second somatosensory area with the parietal ventral and ventral
  somatosensory areas — **and this edge declares a different payload** (deep-receptor) from the
  structure's other outputs (visual plus coordinating).
- posterior / ventromedial-posterior: the lamina-I stream terminates on the
  **calbindin-immunoreactive field**, the visceral line on the **calcitonin-gene-related-peptide
  field**, and the two do not overlap.
- thalamic reticular nucleus → lateral geniculate nucleus leaves from the **perigeniculate**, its
  visual sector; → medial geniculate nucleus leaves from its auditory sector.
- corticothalamic input to the reticular nucleus is **layer-specific**: 6a collateralises, 6b does
  not, 5 generally does not, layer 5 of **frontal cortex** does and monosynaptically.
- zona incerta: the amygdalar input lands on its **parvalbumin population**.

**Invariants carried:** whole-pathway co-instantiation (every structure live from the outset; **seven
loops through one gate** in this section, two of them declared at one end only); per-edge latency
(nonzero, finite, heterogeneous, real time units, **never in steps**); **no global clock may be
assumed.**

## 2. Representation

*(The Representation field is named in CLAUDE.md and its definition is in the spec not in hand. Read
here as: how a structure's parameters and state are laid out in memory. Claude's inference.)*

**Per structure, two arrays and nothing else:**

- **`threshold`** — one unsigned integer per neuron, width `ceil(log2(fan_in))` bits. The only
  parameter memory the architecture recognises.
- **`active`** — one bit per neuron, the current output. **State**, counted in a separate class and
  never summed with parameter memory.

**The realisation gap is zero here, and the reason is not encouraging.** Every fan-in is *to derive*,
so every width takes the 16-bit ceiling, and 16 is exactly a machine integer container. File 01's
12-and-14-bit widths wasted 14–33% against `uint16`; nothing is wasted here. **The gap closed because
the number stopped being a measurement, not because anything fits** — and the moment any fan-in in
this section is measured, the gap opens.

**Element classes: one, and it is the specified one.** Unlike the retina, every structure here is a
population of spiking neurons. There is no transducer, no transmission-only structure, and the one
graded element named — the lateral geniculate's dendritic-release interneuron — is in another
section. **So the element-class problem that blocked most of file 01 does not arise here.**

**A different problem replaces it, and it is on the edges rather than the elements.**

**Most edges in this section carry no content, and the forward operation has no term for what they do
carry.** Sorted by what a line actually asks the receiving cell to do:

1. **Driver edges** — the layer-5 corticothalamic drive, the lamina-I stream, the subicular episode,
   the cerebellar correction, the thalamostriatal drive. These set a receptive field or carry a
   payload. **The threshold gate expresses these.**
2. **Modulatory edges** — the layer-6 corticothalamic feedback everywhere, and every one of the
   mediodorsal nucleus's five cortical outputs. These carry **no receptive-field content** and set
   **gain**. **The threshold gate has no term for gain.** Under equal weights the only stored value
   is the threshold, so the only place a gain could land is *on the threshold* — and writing a
   threshold is the learning rule, which is not set. So a modulatory edge added to the input count
   asserts content the architecture says it does not carry, and applied to the threshold assumes a
   rule that does not exist. **Neither is writable.**
3. **Inhibitory edges** — every output of the thalamic reticular nucleus, every output of the zona
   incerta, and the basal-ganglia output onto three separate targets here. **A count of active inputs
   has no sign**, so an inhibitory line cannot be counted. This is adjacent to file 01's outer-retina
   sign problem and is not the same one: there the sign convention was inverted inside one organ,
   here inhibition is the *function* of two of eight structures.
4. **A double-negative edge**, which is class 3 twice over: the basal forebrain's parvalbumin
   neurons inhibit the reticular nucleus and therefore **disinhibit the relays it inhibits.** Two
   sign inversions in series, in a model with no sign.

**Counted mechanically by the module: 38 of this section's 81 edges — 47% — are class 2, 3 or 4, so
the specified forward operation covers 53% of them.** That is short of a majority and the honest
figure is the one that matters, because the *distribution* is what bites: the two structures whose
whole function is gating — the reticular nucleus and the zona incerta — have **no class-1 output at
all.** So the gap is not spread thinly across the section; it is total at two structures and absent
at others. A module that implements only the specified operation implements neither of those two.

**This is a finding against the sizing model and not a licence to change it.** §6 of the architecture
design says a structure the source describes as computing in a way the model does not cover is a
finding against the model. This is that, at section scale. Whether the model gains a sign, gains a
gain term, or these structures are modelled some other way is Micky's, and nothing is chosen here.

## 3. Algorithm — the part that is fully specified

For a structure `S` with incoming lines `L`:

```
count[j]  = Σ_{i ∈ fan_in(j)} active_source[i]      # equal weights, so a count
active[j] = count[j] ≥ threshold[j]
```

Integer-only, no multiply, no gradient — consistent with a non-backpropagation architecture. **It is
correct and it covers a minority of this section's edges**, per §2.

**`fan_in(j)` is unwritable here for a stronger reason than in file 01, and the difference is worth
stating.** In file 01 the architecture gave fan-in as a scalar per structure and the code needed a
map — a convergence count is not a convergence pattern — but the *pattern* was recorded in prose:
point-to-point retinotopy, space-variant compression ~1:1 at the fovea to ~1000:1 in the far
periphery. Writing the function meant writing down a geometry the prose already described.

**Here there is no scalar and no prose pattern.** Every fan-in reads *to derive*, and the description
carries no convergence rule for any structure in this section — no retinotopy, no tonotopy, no
compression ratio. **Two topographies are recorded and neither is a convergence rule:** the
posterior / ventromedial-posterior territory's antero-posterior head-to-foot somatotopy, and the
intralaminar sector split (centromedian → motor striatum, parafascicular → associative / limbic
striatum). Both say where a line *lands*. Neither says how many lines land on one cell.

**One convergence figure exists in the whole section and it is at the wrong end**: the
cerebellar-cortex to output-nucleus areal ratio of **~85 : 1**, which is a fan-out at the producer
and lives in another file. **Fan-out is never stored** — a projection's cost lives on the target's
fan-in — so it does not help.

**And one connectivity fraction exists, which is the first in either section**: **76%** of ventrobasal
relay axons gave visible collaterals to the reticular nucleus. That is a real, measured topology
number. **It is also not enough to build with**, because it says what fraction of a population
projects and not which cells reach which targets — and it is measured in one nucleus, in rat, and
generalised to none of the others.

## 4. Edge arity is open in three places, and arity is a code fact

*New at this file; file 01 did not meet it.* An edge's arity decides how many arrays exist, so an
open arity is not a description problem that can be deferred to the code — it is a code problem with
no answer above it.

- **The mediodorsal nucleus has five cortical outputs or one.** All five carry "modulatory
  amplification," and **whether the five consumers receive the same amplification or differently-tuned
  ones is not stated at either end.** Same signal to five targets is one output array fanned out;
  differently-tuned is five.
- **The lamina-I edge is three lines or one.** Three labelled lines arrive at the territory with
  three measured latencies; **whether they stay separate on the output edge to the insula or are
  merged there is owed.** Merged, the 72 ms arrival spread is discarded at the relay; separate, it
  propagates and three arrays leave.
- **The reticular nucleus's collateral input is one class edge or many per-producer ones.** The line
  is a class, the universal claim that would have justified the class is false, and the split by
  producer and layer is owed.

## 5. What blocks the implementation, specifically

CLAUDE.md lists six things to surface to Micky before touching, each triggering a fresh start.
**Five of the six are required to write this module and none is set.**

| needed for | item | state |
|---|---|---|
| `fan_in(j)`, every structure | **inter-tile connection topology** | not set — §3 above; and here there is no prose pattern to write it from either |
| allocation of every array | **tile geometry** | not set — §6 below |
| whether `active` is dense or sparse | **sparsity** | not set |
| every `register_buffer()` in the module | **buffer shapes** | not set, and downstream of the three above |
| the update loop | **the scheduling discipline** | not set, and Micky's — §7 below |
| whether `threshold` is ever written | **the learning rule** | not set |

**The learning rule's absence is the least blocking of the six, and it is less benign here than at
file 01.** A threshold never written is a construction cost rather than a memory, so a module with
read-only thresholds is honest and runnable. **But the modulatory edges of §2 have nowhere to land
except the threshold**, so at this file the unset learning rule is also what makes the section's
dominant payload inexpressible. It is still the item that yields a runnable artifact; it is no
longer the item that costs nothing.

## 6. Allocation is blocked twice, and the second block is new

**File 01's block was a partition problem: a count existed and did not divide to the sub-elements the
edges land on. That block is present here too.**

- The intralaminar group has one count — **to derive** — across centromedian and parafascicular, and
  the two striatal edges leave from different ones.
- The pulvinar has one count across an anterior pulvinar and the standard medial, lateral and
  inferior divisions, and **two of its output edges declare different payloads**, which is the reason
  to think they leave from different subdivisions.
- The mediodorsal nucleus has one count across magnocellular, parvocellular and densocellular
  divisions named only in the literature behind the count, and five separate cortical outputs.
- The reticular nucleus has one count across at least four modality sectors, and its outputs leave
  from different ones.

**The second block is that six of the eight structures have no count to partition.** The posterior /
ventromedial-posterior territory, the ventral anterior / ventral lateral group, the anterior nuclei,
the intralaminar nuclei, the reticular nucleus and the zona incerta all read **to derive** at the
whole-structure level. **A missing partition blocks allocating a sub-element's array; a missing count
blocks allocating the structure's array at all.** Five of those six have no grey-matter volume
either, so the density × volume route that independently confirms the two counted structures has no
input for them.

**So the module can size two structures out of eight, and neither of those two can have its
sub-element arrays allocated.**

## 7. The scheduler has a parameter for the first time, and using it would be worse than having none

File 01's scheduler section ended by noting that the architecture sanctions a uniform one-step delay
— set every latency equal, choose a step short enough to carry the finest one — but that **file 01
recorded no latency at all, so even the sanctioned shortcut had no parameter.**

**This file has one.** The finest measured latency here is **59 ms**. A uniform step of ≤ 59 ms would
carry every latency this section states.

**And it would be wrong by nearly four orders of magnitude.** The auditory section records the
interaural time-difference computation working at **tens of microseconds**, with a structural
consequence — heavy myelination of the trapezoid body and lateral lemniscus, because speed matters at
that scale. Recomputed: **131 ms against 2 × 10⁻⁵ s is 3.82 orders**, and a step sized from this
section's floor would quantise the whole binaural computation to zero. **A uniform step is chosen
against the finest latency in the *system*, not the finest in the file**, and this file cannot see the
system.

**That is the finding, and it is sharper than file 01's.** There, the shortcut was unavailable and
its absence was obvious. Here it is available, it produces a number, the number looks like a
parameter, and **a module that took it would look scheduled and be wrong** — with nothing inside the
file to reveal it. **A shortcut with a plausible wrong parameter is more dangerous than one with no
parameter at all.**

Two further reasons the loop cannot be written even if a step were given:

1. **The heterogeneity here is intra-edge.** Three lines of one projection arrive 72 ms apart, and
   the arrival order is the finding. A uniform delay does not coarsen that; it **merges three lines
   the biology keeps separate.**
2. **The loops nest three deep.** Seven relay-and-gate loops run inside the corticothalamic loops,
   and a loop broken by registers becomes an iterated map whose trajectory depends on the update
   rate. Those are two different systems computing two different things.

The module therefore contains no loop, no step counter, and no `for t in range(...)`. Where the
scheduler would go, it raises. **Writing `for step in ...` would be inventing a clock the system does
not have**, and the architecture names exactly that as the failure to watch for.

## 8. Completion test

*(Inferred, since the spec is not in hand; the analogue of the architecture's own test.)*

**A code design entry is finished when the module can be written from it without opening the
architecture and without making an unauthorised decision.**

By that test **this document is not finished, and cannot be finished at this rung.** Two of its eight
structures can have a whole-structure parameter array sized; none of the eight can have its
connectivity built, its sub-element arrays allocated, or its updates scheduled; and **47% of its
edges have no operation defined at all** — including every output of two structures — because the
specified forward operation has no term for gain, no term for sign, and this section's dominant
payload is both.

**What the module does implement, and it is less than file 01's:**

- the structure and edge declarations as data, with each edge **typed by class** — driver, modulatory,
  inhibitory — so that the operation gap of §2 is visible in the data rather than argued in prose;
- the threshold-gate forward operation, for the driver edges it covers;
- an independent recomputation of the architecture's sizing table from counts and fan-ins;
- **an independent recomputation of the density × volume cross-check**, which is the only mechanical
  check this section supports and which closes on both counted structures;
- a latency report that distinguishes the three measured edges from the rest, and a scheduler stub
  that refuses the 59 ms parameter and says why.

That last is the one addition this file makes over file 01's module, and it exists because the
temptation it refuses did not exist at file 01.
