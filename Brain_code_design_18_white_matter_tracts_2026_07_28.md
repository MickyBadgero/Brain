# Brain code design — 18 white matter tracts

**Date:** 2026-07-28
**Derived from:** `Brain_architecture_18_white_matter_tracts_2026_07_28.md` — five entries, in its
order: the corpus callosum, the internal capsule, the fornix, the arcuate / superior longitudinal
fasciculus, and the medial longitudinal fasciculus.
**Rung spec:** `Brain_code_design_spec_2026_07_28.md`.
**Implements:** `Brain_18_white_matter_tracts.py`.

**No history in this document.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live. The same rule binds the code file's header, and a comment
is updated in the same edit as the code it describes.

**Standalone, not a companion.** Every contract field below is carried verbatim from the architecture
entry. At coding time this file is loaded and the architecture file is not.

**The verbatim diff does not certify this pair.** The architecture file and this one were produced in
the same session, so §3's character-for-character check agrees by construction and must not be
reported as a check. It becomes one the next time either file is regenerated alone.

---

## 1. Section preamble — the whole file is one class

**All five entries are transmission-only.** This is the first section in which §5a's transmission-only
class is not an exception inside a section but the section itself, and the consequences run through
every field.

### 1a. What a transmission-only entry does to the entry template

| field | at a grey-matter entry | here |
|---|---|---|
| Transform | a named operation over arrays | **a routing statement** |
| Arrays | `threshold` and `active` | **neither exists** — a routing index instead, and it is not an activity array |
| Parameters | thresholds at ⌈log₂(fan-in)⌉ bits | **none** — no neuron, no threshold |
| Update equation | count of active inputs against a threshold | **`out(t) = in(t − latency)`**, and nothing else |
| State | values carried between updates | **none held by the structure**; the delay line is edge storage |
| Edge storage | a side quantity beside parameter memory | **the structure's entire runtime memory** |
| Adaptation | a learning rule, or a statement that none is set | **not applicable** — there is no stored parameter to change |

**Two of those are worth stating as findings rather than as table rows.**

**The update equation is complete.** `out(t) = in(t − latency)` requires no further choice about its
*form*: a tract applies a delay and nothing else, there is no arithmetic to specify, and no
sign-convention question arises because nothing is compared against anything. **This is the opposite
of the failure the last section carried**, where the operation could not be named at all. Here the
operation is fully named and the term it needs is missing.

**Edge storage stops being a side quantity.** At a grey-matter entry the values in flight are a third
memory class beside the parameter store. **At a tract they are the whole of it** — parameter memory is
zero, no state is held, and everything the structure occupies at run time is either the routing index
that says where each line goes or the values sitting in the delay. So **the figure the architecture
rung declared unsizable is, for this section, the only figure there is.**

### 1b. Edges and their granularity

**34 routed-edge declarations — 15 in, 19 out — and zero internal edges.** The zero is a positive
statement in every entry: no synapse occurs in a tract, so its sub-elements are parallel channels and
not a circuit.

**No declaration is a duplicate.** A tract's Inputs name its producers and its Outputs name its
consumers, and no tract in this file routes an edge to another tract in this file, so **34 declarations
are 34 distinct routed edges.** *(Checked against the entries; the section has no in-file
producer–consumer pair.)*

**The line count is ambiguous by three orders of magnitude and the ambiguity is not this rung's to
resolve.** A routed edge is a region-to-region relation; a line is an axon. The corpus callosum
carries **7 routed edges** and **200–300 million axons**, and which granularity the routing index and
the delay line are built at is downstream of the inter-structure connection topology, which is unset
and is on the surface-before-touching list. **Both bounds are carried on every entry and neither is
chosen.**

### 1c. Representation at a tract, which is a different field from Representation anywhere else

**A tract does not read or write the values it carries.** Units, numeric range and coordinate frame are
declared by the producing region and consumed by the receiving region; the tract's own contribution to
the representation is **exactly the timing**, and nothing else. So for every line in this section:

- **units** — **not applicable at this structure.** Typed at the region ends; the tract passes them
  through unchanged. This is a positive statement and not an unfilled slot: a claim that the tract
  alters units would be a claim that it computes.
- **numeric range and normalization** — **not applicable at this structure**, for the same reason.
- **coordinate frame** — **not applicable at this structure**, for the same reason.
- **update timing** — **event-driven**, and this one *is* the tract's own. A tract emits when its
  producer emits, displaced by the conduction delay. There is no clock to borrow a rate from and the
  tract has no rate of its own.

**So the Representation field collapses to one populated row per line, and that row is the delay.**
*(That units, range and frame read "not applicable at this structure" rather than "owed" is Claude's
reading of the transmission-only convention, offered to be checked. That the payload is typed at the
region ends is Class 1 from the source.)*

### 1d. What the section could have supplied and does not

A tract is where a conduction time is derived from, and a conduction time is a **length** divided by a
**velocity**, with velocity derived from **fibre calibre** and **myelination**. Across five entries the
architecture carries one calibre figure — 3–5 µm, for the corpus callosum's fast minority — **no
g-ratio anywhere**, and **no length anywhere.**

**All 34 latencies therefore read *to derive*, and so does every `update_interval` term below.** The
missing measurement is small and specific: **a length and a g-ratio per tract.**

### 1e. Two entries are bundles and are not split here

The corpus callosum entry is **four tracts** — the callosum with the anterior, hippocampal and
posterior commissures. The arcuate entry is **five** — the superior longitudinal system with the
inferior longitudinal, inferior fronto-occipital, uncinate and cingulum fasciculi. **Five entries cover
twelve tracts.** The split is owed at the source and is not made here: splitting invents the arity, and
it would invent it two rungs below where the arity is known.

**The bundling has a visible cost the module reports**: three of the twelve — the anterior commissure,
the posterior commissure and the inferior fronto-occipital fasciculus — **have a stated function and no
declared traffic at either end**, which is the mirror of a dangling endpoint and fails more silently,
because the entry reads as complete on its own.

---

## 2. Corpus callosum — the great interhemispheric commissure

### Contract — copied verbatim from the architecture

- **Inputs.** Three routed edges. *(Routing statements, not payload transfers. Fan-in reads **none**
  throughout, because no synapse occurs here.)*
  - **← the cerebral cortex of either hemisphere**, from callosal projection neurons in **layers 3
    and 5** — routing only. Fan-in: none. **A class endpoint, and intrinsic to the structure.**
  - **← the primary auditory cortex**, contralateral, through the **central body, posterior body and
    dorsal splenium** — routing only; the payload at the region ends is the same frequency band's
    activity from the other hemisphere, **which sharpens rather than adds**. Fan-in: none. *(File 2,
    both region ends. Two-ended, and the sector attribution is declared there and matched here.)*
  - **← the inferior frontal gyrus**, contralateral — routing only; payload owed at the region ends.
    Fan-in: none. *(File 11; two-ended.)*
- **Outputs.** Four routed edges.
  - **→ the homotopic cortex of the opposite hemisphere**, terminating throughout **layers 2–6**,
    densest in 2 and 3, **sparsest in layer 4** — routing only. Fan-out: none. **Same class endpoint
    as the input limb and the same reason.**
  - **→ heterotopic cortex of the opposite hemisphere** — routing only. Fan-out: none. **A separate
    limb, not a variant**: sensory association cortices carry proportionally more of this traffic than
    primary sensory cortices, so the two limbs have different origins and different densities. **A
    class endpoint, and no entry in the source declares a heterotopic callosal edge.** *(Owed at the
    source.)*
  - **→ the contralateral temporal lobe, olfactory structures and amygdala**, via the **anterior
    commissure** — routing only. Fan-out: none. **No entry in the source declares an edge routed
    through the anterior commissure.** *(Owed at both ends.)*
  - **→ the contralateral hippocampal formation** via the **hippocampal commissure**, and **→ the
    contralateral pretectal and vertical-gaze structures** via the **posterior commissure** — routing
    only. Fan-out: none. **Neither string appears anywhere in the source outside this entry.** *(Owed
    at both ends.)*
- **Sizing.** Basis: **whole**, a midline commissure. **Neurons: none. Synapses: none. Parameter
  memory: zero** — and zero because there are no neurons to hold a threshold, not because a threshold
  was struck. **Axons: about 200 million**, range 200–300 million, by electron microscopy in human
  material. Cross-sectional area about **500–700 mm²**. **Grey-matter volume: not applicable.
  White-matter volume:** the single largest white-matter structure in the brain; **no figure
  recorded.**
- **Shape.** **Transmission-only: a routing index, rank 1** — not an activity array. Extent: **7** at
  routed-edge granularity, **200–300 million** at line granularity, and the choice between them is not
  this rung's. **The per-sector partition is unknown.**
- **Edge latency.** All 7 routed edges **to derive** — this is the one entry with a fibre calibre, and
  it has neither a g-ratio figure nor a length.

### Representation

All seven lines: **units, range and coordinate frame — not applicable at this structure**, typed at the
region ends and passed through unchanged. **Update timing — event-driven**, displaced by a conduction
delay that reads *to derive*.

**One line carries a representation claim the tract cannot honour and the region ends can.** The
auditory limb's payload sharpens rather than adds, which is a statement about how the receiving
representation combines two sources — **a normalization claim living at the consumer**, not here.

### Transform

**Routing.** Deliver each line from its origin sector to its termination, unchanged, after a delay.
**No standard operation name applies because no operation occurs**, and that is a positive statement,
not a missing name.

**The sector structure is the transform's only internal detail**: five parallel channels — rostrum,
genu, body, isthmus, splenium — carrying different traffic at different fibre calibres, hence at
different delays. **A single delay for the whole tract would erase the calibre gradient**, which the
architecture records as heterogeneity inside one structure.

### Arrays

**No activity array and no threshold array.** One structure:

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `routing_index` | rank 1, extent **7** (edge granularity) or **200–300M** (line granularity) | uint, ⌈log₂(destinations)⌉ bits | 0 … destinations−1 | dimensionless index |

**Not allocatable**, and not for the usual reason: the extent is known at both bounds and the *choice*
between them is unset. **This is a different blocker from a missing count** — nothing needs measuring,
something needs deciding.

### Parameters

- **`latency_per_sector`** — unit: seconds. Value: **to derive**, per sector. Origin: **would be
  derived** from fibre calibre, g-ratio and tract length; the entry carries a calibre for the fast
  minority and neither of the other two. Not chosen.
- **No threshold parameter exists.** There is no neuron here.

### Update equation

```
out[line](t) = in[line](t − latency[sector(line)])
```

**Complete in form and unrunnable in fact.** Nothing further about the arithmetic needs deciding; the
delay term is *to derive* and `sector(line)` needs the per-sector partition of the axon count, which is
unknown.

### State carried between updates

**None held by the structure.** A tract stores nothing across updates; the values in transit are edge
storage and are counted there, never summed with parameter memory.

### Edge storage

`edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`

- **`line_count`** — **7** at edge granularity, **200–300 million** at line granularity.
- **`latency`** — to derive, all 7 edges.
- **`update_interval`** — **unset.** The scheduling discipline is Micky's.
- **`bytes_per_value`** — to derive; gated on graded versus binary emission.

**This is the entry where the figure will be largest in the section, and possibly in the project.** Two
hundred million lines each holding values in flight for the duration of a delay is the section's whole
runtime cost, and it scales with the reciprocal of the update interval. **Recorded as where it will be
large, which is what can be said.**

### Adaptation

**Not applicable.** There is no stored parameter to change. This is not "no rule is set" — it is that
the structure holds nothing a rule could act on.

### Open

- The granularity at which the routing index and the delay line are built. **A decision, not a
  measurement.**
- The per-sector partition of the axon count, which the sector-dependent delay needs.
- Whether the three bundled commissures become their own entries.

---

## 3. Internal capsule — the great projection tract

### Contract — copied verbatim from the architecture

- **Inputs.** Two routed edges. *(Routing statements; fan-in reads **none** throughout.)*
  - **← the cerebral cortex**, corticofugal fibres from every lobe — routing only. Fan-in: none.
    **A class endpoint, intrinsic to the structure.** The named corticofugal edges other entries
    declare as routed through this tract are the **corticospinal tract from the primary motor
    cortex** *(files 5 and 16)* and the corticothalamic return traffic below.
  - **← the thalamus**, thalamocortical fibres from every relay nucleus — routing only. Fan-in: none.
    **A class endpoint.** The named thalamocortical edges declared as routed here are the **optic
    radiation** *(file 12 to file 1)*, the **auditory radiation** *(to file 2)*, the **superior
    thalamic radiation** *(file 5)*, and the **anterior thalamic radiation** *(file 12 to file 11)*.
- **Outputs.** Four routed edges.
  - **→ the brainstem and spinal cord**, through the **posterior limb** and **genu** — routing only;
    the corticospinal and corticobulbar motor commands, typed at their cortical origins and at the
    ventral horn and cranial-nerve nuclei that consume them. Fan-out: none. *(File 16 declares this
    tract by name. Two-ended.)*
  - **→ the thalamic reticular nucleus**, from corticothalamic fibres traversing this tract — routing
    only; the collateral copy of the cortex's outgoing traffic that the reticular nucleus gates on.
    Fan-out: none. *(File 12, which records that only about three quarters of the corticothalamic
    fibres passing through gave visible collaterals there. Two-ended, **and that quarter is a finding
    about this tract rather than about the nucleus.**)*
  - **→ the red nucleus**, corticorubral fibres through the **posterior limb** — routing only.
    Fan-out: none. **This consumer has no entry in any of the twenty files.**
  - **→ the pontine nuclei**, frontopontine fibres through the **anterior limb** — routing only.
    Fan-out: none. **This consumer has no entry in any of the twenty files**, and it is **the
    load-bearing half**, because the corticopontine stage is recorded elsewhere as transforming the
    payload rather than relaying it.
- **Sizing.** Basis: **per side.** **Neurons: none. Synapses: none. Parameter memory: zero.**
  **Axons:** carries the **corticospinal tract at about 1 million axons per side** — a classic order
  estimate, with about **1.1 million pyramidal-tract fibres above the decussation** — plus the
  thalamocortical radiations, counts unknown. **The per-limb split of that total is unknown.**
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**
- **Shape.** **Routing index, rank 1.** Extent: **6** at routed-edge granularity; at line granularity
  the corticospinal component alone is **~1–1.1 million** and the radiations are unknown, so the full
  line count is **to derive**. **The per-limb partition is unknown.**
- **Edge latency.** All 6 routed edges **to derive.** No fibre calibre, no g-ratio and no length are
  recorded.

### Representation

All six lines: **units, range and coordinate frame — not applicable at this structure. Update timing —
event-driven**, displaced by a delay that reads *to derive*.

**One line's representation is explicitly partial at the source, and the module carries the figure.**
Only about three quarters of the corticothalamic fibres crossing this tract collateralise into the
reticular nucleus, **so the copy on that line is a sample of the cortex's outgoing traffic and not all
of it** — a completeness property of the line, which no field in the template holds.

### Transform

**Routing, through five parallel limbs**, each carrying a different fibre system to a different target:
anterior limb, genu, posterior limb, retrolenticular part, sublenticular part. Every routed edge is
attributed to one of them.

**No operation occurs.** The one place this entry approaches a transform is the corticothalamic
collateral, and even there the tract does not make the copy — the fibres branch.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `routing_index` | rank 1, extent **6** (edge granularity) or **to derive** (line granularity) | uint, ⌈log₂(destinations)⌉ bits | 0 … destinations−1 | dimensionless index |

**Not allocatable at line granularity**, and here the reason *is* a missing measurement: the
thalamocortical radiations have no counts, so only the corticospinal component can be sized.

### Parameters

- **`latency_per_limb`** — unit: seconds. Value: **to derive**, per limb. Origin: would be derived from
  calibre, g-ratio and length; the entry carries none of the three. Not chosen.
- **`collateral_fraction`** — unit: dimensionless. Value: **≈ 0.75** of corticothalamic fibres giving a
  visible collateral to the thalamic reticular nucleus. Origin: **computed from the source**, declared
  at the far end in file 12. **This is the only numeric parameter in the entire section that is neither
  a count nor to-derive.**

### Update equation

```
out[line](t) = in[line](t − latency[limb(line)])
```

Complete in form. `limb(line)` needs the per-limb partition, which is unknown.

### State carried between updates

**None held by the structure.**

### Edge storage

- **`line_count`** — **6** at edge granularity; at line granularity **~1–1.1 million** for the
  corticospinal component and **to derive** overall.
- **`latency`** — to derive, all 6 edges. **`update_interval`** — unset. **`bytes_per_value`** — to
  derive.

### Adaptation

**Not applicable** — no stored parameter.

### Open

- The per-limb partition of the axon count.
- Whether the un-collateralised quarter is modelled as a property of the line or as a separate line.

---

## 4. Fornix — the hippocampal output tract

### Contract — copied verbatim from the architecture

- **Inputs.** Four routed edges. **This is the best-declared tract in the section** — six of its routed
  edges are written at both region ends, in four different files, by passes that did not consult each
  other. *(Fan-in reads **none** throughout.)*
  - **← the hippocampal formation**, from the **subiculum**, into the **fimbria** — routing only; the
    payload at the region ends is the **completed episode**, the bound retrievable pattern addressable
    by any fragment of itself, and **only partly writable there**, since an episode has no units and
    no frame. Fan-in: none. *(File 8. Two-ended, and the far end already uses this convention.)*
  - **← the medial septum, cholinergic cells** — routing only; the payload at the region ends is a
    cholinergic modulatory signal. Fan-in: none. *(Files 13 and 8. Two-ended.)*
  - **← the medial septum, parvalbumin-expressing GABAergic pacemaker cells** — routing only; the
    payload at the region ends is the **theta timing reference**. Fan-in: none. *(Files 13 and 8.
    Two-ended.)*
  - **← the medial septum, glutamatergic cells** — routing only; the payload at the region ends is a
    **tonic drive**. Fan-in: none. *(Files 13 and 8. Two-ended.)*
- **Outputs.** Three routed edges.
  - **→ the mammillary bodies and the anterior thalamic nuclei**, through the **post-commissural
    limb** — routing only; the completed episode. Fan-out: none. *(Files 8, 12 and 14. Two-ended.)*
    **This is the Papez limb**, and the **mammillothalamic tract** carrying its next leg has no entry.
  - **→ the hypothalamus** — routing only; payload owed at both region ends. Fan-out: none. *(Files 8
    and 14. Two-ended, owed at both.)*
  - **→ the septum and basal forebrain**, through the **pre-commissural limb** — routing only; payload
    owed at the region ends. Fan-out: none. **The consumer is split:** the basal forebrain has an entry
    in file 13 and **the septal nuclei have no entry in any of the twenty files.**
- **Sizing.** Basis: **per side.** **Neurons: none. Synapses: none. Parameter memory: zero.**
  **Axons:** soft, no clean human count pinned; classic order about **1 million**. **The per-limb split
  is unknown**, and the pre-commissural limb's share is what would size the septo-hippocampal return.
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**
- **Shape.** **Routing index, rank 1.** Extent: **7** at routed-edge granularity, **~1 million** at
  line granularity on a soft order estimate. **The per-limb partition is unknown.**
- **Edge latency.** All 7 routed edges **to derive.** Myelination reads *myelinated tract* with no
  g-ratio; no calibre and no length are recorded. **One payload in this entry is itself a timing
  signal**, which makes the missing latency load-bearing: the parvalbumin-expressing septal limb
  carries a **theta timing reference**, and a timing reference delivered over a cable of unknown delay
  is a reference to an unknown phase.

### Representation

All seven lines: **units, range and coordinate frame — not applicable at this structure. Update
timing — event-driven**, displaced by a delay that reads *to derive*.

**And one line is the exception that proves the field matters.** The theta timing reference is a line
whose entire content **is** the timing, so for that one line the tract's own contribution — the delay —
is not a modifier of the payload but a corruption of it. **A delay on a data line shifts when a value
arrives; a delay on a timing reference changes what the value means.** *(Claude's reading, offered to
be checked. That the payload is a theta timing reference is Class 1 from files 13 and 8.)*

### Transform

**Routing, through two limbs running in opposite functional directions** — the post-commissural limb
carrying the completed episode out to the Papez circuit, the pre-commissural limb carrying the septal
return in. **The fimbria, crus, body and columns are segments of one course, not parallel channels**,
so they do not enter the routing map as alternatives.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `routing_index` | rank 1, extent **7** (edge granularity) or **~1M** (line granularity, soft) | uint, ⌈log₂(destinations)⌉ bits | 0 … destinations−1 | dimensionless index |

### Parameters

- **`latency_per_limb`** — unit: seconds. Value: **to derive**. Origin: would be derived from calibre,
  g-ratio and length; none is recorded. Not chosen.

### Update equation

```
out[line](t) = in[line](t − latency[limb(line)])
```

Complete in form; the delay is to derive and the per-limb partition is unknown.

### State carried between updates

**None held by the structure.**

### Edge storage

- **`line_count`** — **7** at edge granularity, **~1 million** at line granularity.
- **`latency`** — to derive. **`update_interval`** — unset. **`bytes_per_value`** — to derive.

### Adaptation

**Not applicable** — no stored parameter.

### Open

- Whether the lateral / medial division, which carries anterior against posterior hippocampus, is
  preserved as far as the targets.
- The per-limb partition, which is what would size the septo-hippocampal return.

---

## 5. Arcuate fasciculus / superior longitudinal fasciculus — the dorsal language tract

### Contract — copied verbatim from the architecture

- **Inputs.** Three routed edges. *(Fan-in reads **none** throughout.)*
  - **← the supramarginal gyrus** — routing only; the payload at the region ends is a **praxis /
    action-sequence code** and, on the left, a **phonological code** — the sound-form of words for the
    articulatory route, only partly writable there. Fan-in: none. *(Files 6 and 11, both naming this
    tract and **branch III** specifically. Two-ended.)*
  - **← the posterior superior temporal gyrus and the sylvian parieto-temporal area** — routing only;
    payload owed at the region ends. Fan-in: none. *(File 11; file 2 names this tract as carrying the
    stream forward. Two-ended.)*
  - **← the temporal pole**, over the **uncinate fasciculus**, the **inferior longitudinal
    fasciculus**, the **middle longitudinal fasciculus** and this tract — routing only; payload owed.
    Fan-in: none. *(File 7 declares all four by name; which pathway carries which of its edges is
    established only for the uncinate. **That entry also states these tracts have their own entries
    here, which is wrong for the middle longitudinal fasciculus.** Owed as a cross-file edit at file
    7.)*
- **Outputs.** Five routed edges.
  - **→ Broca's area and premotor cortex** — routing only. Fan-out: none. *(Files 6 and 11. Two-ended.)*
  - **→ the orbitofrontal and ventrolateral prefrontal cortex**, over the **uncinate fasciculus** —
    routing only; payload owed at the region ends. Fan-out: none. *(File 7. Two-ended.)*
  - **→ the cingulate midline nodes**, over the **cingulum** — routing only. Fan-out: none. **Four
    entries declare this tract by name** — file 11 and the three cingulate entries in file 17, the
    last three recording it as routing rather than as an edge. Two-ended.
  - **→ occipito-temporal cortex**, over the **inferior longitudinal fasciculus** — routing only.
    Fan-out: none. **Named at one far end only** *(file 7)*. *(Owed at both ends.)*
  - **→ the ventral semantic stream**, over the **inferior fronto-occipital fasciculus** — routing
    only. Fan-out: none. **This string appears nowhere in the source outside this entry.** **A tract
    with a stated function and no traffic.** *(Owed: attribute an edge to it, or withdraw it.)*
- **Sizing.** Basis: **per hemisphere**, and this is the one entry in the section where the basis
  carries a functional claim rather than a convention: the tract is **left-dominant for language**.
  **Neurons: none. Synapses: none. Parameter memory: zero.**
  **Axons:** counts largely unknown, **and one rare absolute estimate exists and does not fit the
  slots.** Direct connections between the posterior and anterior language regions are **under about 5%
  of the axons in the arcuate / superior longitudinal trunk**, with a median of about **6,200 axons
  between areas within a hemisphere** and about **1,300 interhemispherically.** **That figure counts
  inter-areal axons rather than contacts per cell, so it fits neither fan slot**, and the far end
  records the same mismatch and marks it owed.
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**
- **Shape.** **Routing index, rank 1.** Extent: **8** at routed-edge granularity; at line granularity
  **to derive**. **The per-branch partition across I, II and III is unknown.**
- **Edge latency.** All 8 routed edges **to derive.** No calibre, no g-ratio, no length.

### Representation

All eight lines: **units, range and coordinate frame — not applicable at this structure. Update
timing — event-driven**, displaced by a delay that reads *to derive*.

**Two lines carry a laterality qualifier that no field holds.** The supramarginal input carries a
phonological code **on the left** and a praxis code on both sides, so the same anatomical line has
different content by hemisphere. **A per-line representation declared once and inherited by every
consumer cannot express a payload that differs by side**, and the tract is where that would have to be
recorded because the tract is what is paired. *(Claude's reading. The left-dominance is Class 1.)*

### Transform

**Routing, through three numbered branches** of the superior longitudinal system — I, II and III, which
connect different cortical territories, with branch III already named on the supramarginal edge by both
region ends. **Whether the arcuate is a branch of that system or a tract adjacent to it is contested**
and is carried as contested, not resolved by preference.

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `routing_index` | rank 1, extent **8** (edge granularity) or **to derive** (line granularity) | uint, ⌈log₂(destinations)⌉ bits | 0 … destinations−1 | dimensionless index |

### Parameters

- **`latency_per_branch`** — unit: seconds. Value: **to derive**. Not chosen.
- **`interareal_axons`** — unit: axons. Value: **~6,200** median within a hemisphere, **~1,300**
  interhemispherically. Origin: **computed from the source**. **It is carried as a recorded figure and
  not used**, because it is a fan measure that fits neither fan slot and its reconciliation is owed at
  both ends.

### Update equation

```
out[line](t) = in[line](t − latency[branch(line)])
```

Complete in form; the delay is to derive and the per-branch partition is unknown.

### State carried between updates

**None held by the structure.**

### Edge storage

- **`line_count`** — **8** at edge granularity, **to derive** at line granularity.
- **`latency`** — to derive. **`update_interval`** — unset. **`bytes_per_value`** — to derive.

### Adaptation

**Not applicable** — no stored parameter.

### Open

- How a per-line representation expresses a payload that differs by hemisphere.
- Whether the four bundled association fasciculi become their own entries.
- Reconciling the inter-areal axon estimate with the fan slots.

---

## 6. Medial longitudinal fasciculus — the gaze-yoking brainstem tract

### Contract — copied verbatim from the architecture

- **Inputs.** Three routed edges. *(Fan-in reads **none** throughout.)*
  - **← the vestibular nuclei** — routing only; the payload at the region ends is the
    **vestibulo-ocular reflex command**, an eye-velocity signal **equal and opposite to head
    rotation**, driven chiefly by the semicircular-canal line, and the fastest gaze-stabilising
    reflex. Fan-in: none. *(Files 3 and 15. Two-ended.)*
  - **← the abducens nucleus**, from its **internuclear neurons** — routing only; the payload at the
    region end is the yoking signal that makes the two eyes move together in horizontal gaze. Fan-in:
    none. *(File 15 records the edge as one that should be typed as an internal edge, marking it
    owed.)*
  - **← the gaze neural integrators** — the **nucleus prepositus hypoglossi** with the medial
    vestibular nucleus for horizontal, and the **interstitial nucleus of Cajal** for vertical —
    routing only; the payload at the region ends is **eye position**, the integrated signal that holds
    the eye where the burst put it. Fan-in: none. **Neither far end names this tract.** *(Owed at both
    ends.)*
- **Outputs.** Three routed edges.
  - **→ the ocular motor nuclei** — the **oculomotor**, **trochlear** and **abducens** nuclei —
    routing only. Fan-out: none. *(Files 3 and 15. Two-ended.)* **This is the edge that makes the entry
    worth writing.**
  - **→ the contralateral oculomotor medial-rectus pool**, from the abducens internuclear neurons —
    routing only. Fan-out: none. *(Owed at file 15.)* **This limb crosses the midline and no other limb
    of this tract does, and that crossing is what conjugate horizontal gaze consists of.**
  - **→ the cervical spinal cord**, as the **medial vestibulospinal** fibres — routing only; the
    payload at the region ends is a head- and neck-stabilising postural command. Fan-out: none.
    **Neither far end names this tract**, and **neither separates the medial vestibulospinal tract from
    the lateral one.** *(Owed at both ends.)*
- **Sizing.** Basis: **per side** — the tract is paired. **Neurons: none. Synapses: none. Parameter
  memory: zero.** **Axons: unknown, at either limb. The per-limb split is unknown.**
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**
- **Shape.** **Routing index, rank 1.** Extent: **6** at routed-edge granularity; at line granularity
  **to derive**. **The per-limb partition is unknown.**
- **Edge latency.** All 6 routed edges **to derive** — **and this is the entry where that reads worst.**
  Myelination is recorded as **heavily myelinated and among the earliest tracts in the brain to
  myelinate**; the **g-ratio is explicitly unknown**, no calibre is recorded, and no length is
  recorded. **So the description says this cable is built for speed and supplies no term of the
  velocity.**

### Representation

All six lines: **units, range and coordinate frame — not applicable at this structure. Update timing —
event-driven**, displaced by a delay that reads *to derive*.

**One line's crossing is a representation fact and the field has nowhere to put it.** The abducens
internuclear limb **crosses the midline** and no other limb does. Laterality is not units, not range,
not frame and not timing — **it is which side the value is about**, and losing it turns conjugate gaze
into two independent eyes. The architecture rung holds crossings as load-bearing; this rung has no slot
for one.

### Transform

**Routing, through an ascending and a descending limb** — the ascending carrying vestibulo-ocular and
yoking traffic rostrally to the ocular motor nuclei, the descending carrying medial vestibulospinal
fibres caudally to the cervical cord. **One limb crosses the midline.**

### Arrays

| array | shape | dtype | range | units |
|---|---|---|---|---|
| `routing_index` | rank 1, extent **6** (edge granularity) or **to derive** (line granularity) | uint, ⌈log₂(destinations)⌉ bits | 0 … destinations−1 | dimensionless index |

**A second field is required and the template has no column for it**: each index entry must carry
**which side the destination is on**, because one of six limbs crosses. Recorded, not added.

### Parameters

- **`latency_per_limb`** — unit: seconds. Value: **to derive**. **The entry's function is a speed claim
  and none of the three terms of a velocity is recorded.** Not chosen.

### Update equation

```
out[line](t) = in[line](t − latency[limb(line)])
```

Complete in form. **And for this entry the delay is not a detail**: the vestibulo-ocular reflex is
described as the fastest gaze-stabilising reflex, so an unstated latency on this line is an unstated
value of the quantity the structure exists to minimise.

### State carried between updates

**None held by the structure.**

### Edge storage

- **`line_count`** — **6** at edge granularity, **to derive** at line granularity.
- **`latency`** — to derive. **`update_interval`** — unset. **`bytes_per_value`** — to derive.

### Adaptation

**Not applicable** — no stored parameter.

### Open

- Splitting the vestibulospinal endpoint into medial and lateral limbs, which is owed at both far ends.
- How the routing index carries laterality for the one crossing limb.

---

## 7. Completion test

**An entry is finished when the code can be written from it without making a single further choice.**

| entry | finished | what a further choice would be |
|---|---|---|
| Corpus callosum | **no** | the routing granularity; the per-sector partition; every delay |
| Internal capsule | **no** | the per-limb partition; the radiations' line counts; every delay |
| Fornix | **no** | the per-limb partition; every delay — and one payload *is* a timing reference |
| Arcuate / superior longitudinal fasciculus | **no** | the per-branch partition; every delay; how laterality is expressed |
| Medial longitudinal fasciculus | **no** | the per-limb partition; every delay; how the crossing is carried |

**None is finished, and the shape of the failure is different from the last section's.** There, the
operation could not be named. **Here every operation is named, the update equation is complete in form
at all five entries, and what is missing is a single quantity — the delay — plus one decision about
granularity.**

**That makes this section the cheapest of the three worked so far to finish**, and it names its own
price: **a length and a g-ratio per tract, and a ruling on routing granularity.** Neither is a payload
question and neither needs the connection topology.

**What the module implements:**

- five structures as data, each carrying its bundle count, its basis, its axon count and its
  transmission-only class;
- **34 routed-edge declarations**, each with the file its far end lives in, that far end's declaration
  state, and whether the endpoint is a region, an entry-less region, a class or a stream;
- an **endpoint-kind census**, with the class endpoints separated into those **intrinsic to a tract**
  and those marked owed at the source, because a class endpoint at a commissure is not the same defect
  it is at a grey-matter entry;
- a **traffic-less tract report** — the three tracts with a stated function and no declared edge at
  either end, which is the mirror of a dangling endpoint and fails more silently;
- a **bundle report** — five entries covering twelve tracts, with the split owed at the source;
- the **routing-index arithmetic** at both granularities, presented as a bound in two directions rather
  than as a figure, and reporting that the corpus callosum's index exceeds the largest parameter store
  in the map;
- a **latency-substrate report** — calibre, g-ratio and length per entry against what a conduction time
  needs, which is the section's own diagnosis;
- `route()` returning the delay expression and raising on evaluation, `allocate()` raising on the
  granularity decision, and `step()` raising with the scheduling discipline unset.
