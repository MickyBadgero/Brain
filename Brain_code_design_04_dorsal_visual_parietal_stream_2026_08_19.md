# Brain code design — 04 dorsal visual / parietal stream

**Date:** 2026-08-19
**Derived from:** `Brain_architecture_04_dorsal_visual_parietal_stream`,
`Brain_code_design_spec`, and CLAUDE.md. **No other content source.**
**Implements:** `Brain_04_dorsal_visual_parietal_stream.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
character for character, so that at coding time only this file is loaded. **One deviation from that
copy, and it is declared here so that anything else is a defect.** The architecture's
**internal cross-references** — *see the section invariant*, *the qualification recorded at the entry
above*, *same shape of hole as* — are not copied, because they point at fields this rung does not
have; their content is carried at the entry it belongs to.

**Four entries, one per architecture entry, same names, same order.**

**One entry is a bundle in a sense the spec's §1 does not quite name, and it stays one.** The medial
superior temporal area carries **two divisions** — dorsal and lateral — whose separate payloads the
architecture does not give, and it says on its own face that **splitting them into separate entries is
owed**. The ventral intraparietal area carries a medial and a lateral division on the same terms. **The
design entries stay undivided**, because splitting invents the arity two rungs below where the arity
is known.

---

## What is open for every entry in this file, stated once

Repeating these four times would make the file longer without making it truer. Each entry names only
what is open **beyond** this list.

- **Emission — graded or binary, and the unit's expressiveness.** Micky's. **And in this section it is
  not one open item among several: it is the item the section's characteristic operation runs into.**
  See the next heading, which is why this list has one.
- **The scheduling discipline.** Micky's, and the largest open item at this rung. No entry contains a
  loop, a step counter, or a `for t in range(...)`. **No global clock may be assumed**, and no latency
  in this section is stated in steps.
- **The learning rules.** Micky's. Every Adaptation field reads *none set*. A threshold that is never
  written is a construction cost and not a memory, which is why the entries are still coherent without
  one.
- **Inter-structure connection topology.** Fan-in is a **scalar per structure** above and **underived
  on every edge in this section**; the code needs it as a **map** — which source lines converge on
  which unit. A convergence count is not a convergence pattern. Surface-before-touching.
- **Tile geometry and sparsity.** Both surface-before-touching, both unset, and every array extent
  below is therefore symbolic.
- **Every edge latency in this section reads *to derive*** — and this section makes that fail in two
  new ways, both of which land here rather than above. See the second heading below.
- **Edge storage cannot be closed anywhere in this file.**
  `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`. Latency is *to
  derive* on every edge here, the update interval waits on the scheduling discipline, and bytes per
  value waits on the emission question. Each entry records its **edge count** and its **line count
  status**, which is the term this rung can supply. **Never summed with parameter memory or state.**

### The section's characteristic operation is the one arithmetic the unit model excludes

These four areas re-express visual information in coordinate frames for action. **The characteristic
operation is therefore a coordinate transform, and the architecture states its mechanism: gain fields
— a sensory receptive field multiplicatively modulated by eye and head position.**

**The transform is stated as multiplicative. The threshold-gate model has equal weights and no
multiply, by construction, which is what makes the stored value a single threshold.** The architecture
draws that conclusion itself and adds that **it is not a gap in the description.**

**At this rung it has an exact cost, and it is larger than any other open item in the file.** Three of
the four entries below rest on a multiplication:

- the **ventral intraparietal area**, whose whole reason for existing is the gain-field transform;
- the **lateral intraparietal area**, which carries eye-position gain modulation on its own face;
- the **medial superior temporal area**, whose dorsal cells combine visual and vestibular heading
  **linearly with subadditive weights** — which is not a gain field, and is still not a sum of
  equal-weight inputs.

**No update equation in this file may be written under the current unit model, and none is.** A unit
that sums equal-weight inputs and compares the total to one threshold cannot express a receptive field
scaled by a position signal, and writing one that appeared to would be inventing the unit. **This is
§10's unit-expressiveness item, it is Micky's, and it is asked in the conversation rather than parked
here.** *(The multiplicative statement and the equal-weight model are both the architecture's; that
the three entries are therefore uncodeable under the present unit is Claude's reading, constrained by
them.)*

### Per-edge latency fails here in two new ways, and both are design-rung problems

**1. A pair of edges whose payloads are identical and whose latencies are not.** The direct route from
V1 layer 4B carries direction and disparity on a **fast few-hop route** — fewer stages, so it arrives
earlier — and **the payload is the same as the indirect routes carry and the latency is not.** So the
only thing distinguishing the direct route from the route through V2 and V3 is the field that reads
*to derive*. **Set the latencies equal and the direct route stops being a different edge.**
**The design consequence is exact:** a scheduling discipline that assigns one uniform interval to
every edge does not merely approximate this section — **it deletes one of its structures' inputs**, by
making two declared edges indistinguishable in every field the code carries. That is a constraint on
Micky's discipline decision, produced by this section and by no other.

**2. A payload with a deadline against an external event.** The corollary discharge reaching the
lateral intraparietal area says *the eye is about to move, by this vector*, and it drives **predictive
remapping** — cells shift receptive fields toward the post-saccadic location **before** the movement.
**This payload is only useful if it arrives before the eye moves. Arrival order is part of correctness
here, not of performance**, and it is ordered against an event outside the section rather than against
another edge. **The map has had no payload of that form before.**
**The design consequence:** every other timing quantity in this file is a number waiting to be
supplied; this one is a **predicate over two events**, and the shared edge vocabulary has no field for
a predicate. An `Edge` carries a latency in seconds and cannot carry *before the eye moves*. **Recorded
as a finding, not patched**, and it is a second thing the scheduling decision has to accommodate.

### Two classes of thing the Shape slot cannot address, and neither is a gap in the description

- **Two maps superimposed on one sheet.** The middle temporal area carries **direction columns** and
  **disparity columns** at once, plus a **speed clustering that is explicitly not columnar.** A
  position in this area has *both* a direction preference and a disparity preference, and **an edge
  terminating on it terminates on both.** Two superimposed maps is a different object from one
  compartmentation, and one sub-element name is insufficient for it. **The arrays below carry both as
  separate axes**, which is the only representation available and is not the same claim as the
  biology's.
- **A sub-element that is not a place.** In the medial superior temporal area's dorsal division,
  heading-tuned cells divide into **congruent** and **opposite** cells by the *relation* between their
  visual and vestibular tunings. They are interleaved, with no spatial segregation found. **Every
  other sub-element anywhere in this section is a place, and an edge terminates on a place** — so
  **what it would mean for an edge to terminate on the congruent cells and not the opposite ones is
  owed**, and the architecture records that it may not be answerable in the slot's present form.
  **At this rung that is an indexing problem with no index:** a boolean mask over the population is the
  representation available, and a mask is not a sub-element, because nothing can terminate on it.

### Three stated functions in this section have no declared substrate, and it is the same shape three times

1. **Motion integration across direction columns** — demanded by the middle temporal area's stated
   function, recorded nowhere.
2. **The gain-field multiplication** — the ventral intraparietal area's whole reason for existing, and
   the edge delivering eye and head position to those cells is **owed at its source.**
3. **Lateral inhibition across the priority map** — what the lateral intraparietal area's selection
   rests on, with no within-map inhibitory edge recorded.

**In each case the Function field names a mechanism and the Internal-structure field cannot show it.
That is a different defect from a missing payload: the edge is not merely untyped, it is absent while
being required.** **Three of the four entries below therefore have a Transform field describing an
operation with no internal edge to carry it**, and each says so in place rather than supplying one.

### The element class is uniform here, for the first time in the map

All four structures are **isocortical areas** and every population in them is a **threshold gate**.
**No transducer, no graded non-spiking element, no transmission-only structure, and no sign-inverting
stage appears in this section** — so §5a's four exceptions are all inapplicable, which is a positive
statement about the section and not an omission. The earlier sections needed all four.

**Counting basis is uniform for the first time in the map: per hemisphere, all four structures.** Four
isocortical areas, each with the same eight laminar sub-elements, each with a stated neuron count.
**Here every row is priced and the basis never moves.**

**Cross-file endpoints carry the far file's stem.** Five far files are reached from this section:
`01_visual_pathway`, `06_posterior_parietal`, `11_frontal_lobe`, `12_thalamus`,
`14_brainstem_midbrain_hypothalamus`. Every other named far end arrives **without a stem**, which means
its file has not been opened beside this one — not that no far end exists.

---

# 1. Middle temporal area

## Contract

**Inputs.**
- **← V1 layer 4B, predominantly its spiny-stellate class** (`01_visual_pathway`), onto **layer 4** — direction of
  motion and binocular disparity, achromatic, coarse-spatial, **on the fast few-hop route.**
  **The magnocellular annotation on this edge is settled and no longer contested:** 4B's two
  output classes are separate populations with separate inputs — spiny stellates take
  magnocellular input only, from 4Cα directly, and **these are the cells that project here**;
  pyramids take both and **project to V2 instead.** So **the direct route to this area is
  magnocellular and the route through V2 is mixed.**
  **The producer declares neither this payload nor the termination layer** — its 4B output line
  carries the cell-class composition and a fan-out and nothing about what is on the wire. **This is
  the only typed end and the producer's is the deficient one.** The composition is **76% spiny stellate**
  (range 67–93%) for the cells labelled from this area, against **80% pyramidal** for the
  V2-projecting population — the reverse figure for the other target — with **fewer than about 5%
  double-labelled** under dual-tracer injection. The cells projecting here are distributed
  **indiscriminately with respect to the cytochrome-oxidase compartment.**
- **← V2 thick stripes** (`01_visual_pathway`), from layers 2/3, onto **layer 4** — binocular disparity, high-speed
  sensitivity, and the surround suppression underlying motion opponency; achromatic, retinotopic.
  **The two ends disagree about direction and the disagreement is substantive:** the producer
  declares this edge as carrying motion direction and disparity; this end declares direction as
  arriving on the direct V1 route instead, on the strength of reversible inactivation — cooling V2
  and V3 degrades **disparity** tuning disproportionately relative to **direction** tuning. **A
  causal inactivation result outranks an unqualified connectivity statement**, and the repair is
  owed at the V2 entry in `01_visual_pathway`. **What that entry declares is narrower than assumed
  here: it declares no payload on this edge at all.**
  So the disagreement is not between two typed architecture ends — it is between this end and the
  *source's* V2 declaration, which the producer's architecture did not carry forward. **The repair
  therefore starts at the source, and the producer now records the disagreement on its own face.**
- **← V3** (`01_visual_pathway`), onto **layer 4** — the same class of contribution as the V2 route, plus **dynamic
  form**: contour bound to direction of motion.
- **← lateral geniculate nucleus** (`01_visual_pathway`)**, direct, bypassing V1** — payload **owed**; sufficient to support
  motion sensitivity without V1. Mostly **koniocellular**, sending virtually no collaterals to V1,
  numbering about **10%** of the V1 population that innervates this area. **This is a thalamic
  input to a non-primary cortical area**, and it contradicts the framing that a relay funnels
  everything into a primary area which then redistributes it. **The leading account of blindsight's
  residual motion sensitivity.**
- **← superior colliculus, di-synaptically by way of the pulvinar** — payload **owed**; the relay
  reaches **this area and V3 selectively**, a subcortical route into the motion areas that does not
  pass through V1. **Written as one line where the pulvinar has an entry of its own that declares
  both legs — the split is owed at that entry.**
- **← pulvinar** — **two things on the same wire**: a visual signal that largely **reflects its
  cortical driver's content** — selective for orientation, direction and motion, but not a
  representation the cortex lacks — and a **coordinating payload**, attentional gain and
  cross-areal synchrony. **Fan-out at the producer: each pulvinar cell reaches the input layers of
  ~2–3 cortical areas.** A second candidate subcortical route past V1; **this edge and the
  geniculate one are competing or complementary explanations of the same residual capacity, not
  established alternatives.**
- **← frontal eye field** (`11_frontal_lobe`), terminating in **all cortical layers** — the spatial
  attentional gain signal: an enhancement or suppression **by location, not a stimulus code.**
  That entry declares `→ the middle temporal area, terminating in all cortical layers` **on its own
  output line, with the same lamination.** **Two-ended, and this end is the typed one** — the
  producer carries no payload for it.
  **The same phrasing is claimed by a third structure in a fourth file, and that is the finding.**
  The frontal entry already records that `01_visual_pathway`'s V4 declares
  `← frontal eye field, terminating in all cortical layers — the spatial attentional gain` **with no
  matching output anywhere in the frontal file**, and notes that the nearest thing that does exist
  is the edge to this area — *the same lamination and the same phrasing, to a different consumer in
  a different file.* **With both consumers read, the pair separates cleanly**: this
  edge is two-ended and V4's is producer-less. **So the shared wording is not evidence that the two
  are one edge mis-copied**; it is evidence that one general description — a laminar-nonspecific
  frontal attentional projection to extrastriate cortex — was instantiated at two consumers and
  declared back at only one. **Owed at the source: establish the V4 limb at the producer, or
  withdraw it there.**
- **← the medial superior temporal area** and **← posterior parietal areas** (feedback), onto
  **layer 1** — payloads **owed**. The second endpoint **is a class and does not resolve**: none
  of the posterior parietal file's five entries declares an output here, and the supramarginal
  gyrus declares traffic in the opposite direction only.

**Outputs.**
- **→ the medial superior temporal area** — **integrated global motion**: local component motions
  resolved into a single pattern-motion direction, speed, motion-in-depth, and figure–ground from
  motion opponency. **The transformation is local vectors in, one vector per region out.**
- **→ smooth-pursuit oculomotor circuitry** — target velocity as a pursuit command. **This
  endpoint is a class and names no region**, and the frontal lobe file contains no pursuit entry at
  all.
- **→ the ventral intraparietal area** and **→ the lateral intraparietal area** — payload **owed
  at this end** and typed at both consumers'. **The two ends disagree: one owed, one typed, and
  neither cites a source for the payload.**
- **→ V1** (`01_visual_pathway`) (feedback), principally onto **layer 1** and also 2, 5 and 6 — contextual and
  attentional modulation, figure–ground and border-ownership context, attentional gain; **not a new
  stimulus code.** **Descending input avoids layer 4, which is what distinguishes a feedback edge
  from a forward one at the receiving end.** On layer 1 it terminates on apical tufts belonging to
  cells housed in layers 2/3 and 5, mainly on **spines**. Declared inside a four-source class, so
  **which of the four contributes which part of the payload is owed.**
- **→ V2** (`01_visual_pathway`) (feedback), onto layer 1 — **owed at both ends**, and the consumer's end confirms it: its V2 entry declares the edge inside a three-source feedback class line and types no limb of it.

**Sizing.** Basis: **per hemisphere.** **~15M neurons**, high variance, though the area is fairly
well bounded by a myeloarchitectonic border and its motion selectivity. Fan-in: **to derive on
every edge.** At the 16-bit ceiling: **30.00 MB.**

**Shape.** **Sheet**, rank 4: **(lamina, direction column, disparity domain, position)** — and the
third axis is not a refinement of the second. **Direction columns** of smoothly varying preference
run beside a matching set preferring the locally opposite direction, forming **pinwheels** where
the area lies on the surface rather than in a sulcus. **Disparity columns** form a topographic map
in millimetre-sized interleaved domains, and **some regions contain neurons with poor disparity
tuning, so that map does not tile the area uniformly.** **Speed preference is clustered and
explicitly not columnar.**
**A coverage mismatch recorded rather than smoothed.** Imaging finds only **3–4 segregated motion
domains**, each **2–3 mm²**, spaced **2–3 mm**, occupying roughly **15%** of the surface — while
about **85%** of the area's neurons are directionally selective, a **5.7-fold** discrepancy.
**Either the domains are not where most direction selectivity lives, or the imaging
measures something narrower than direction selectivity. Unresolved.**

**Edge latency.** All edges **to derive** — and this is the structure where that costs the most,
because **the direct and indirect routes carry the same payload and differ only in arrival time.**

## Representation — declared once per line, inherited by every consumer

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← V1 layer 4B, spiny stellates, onto layer 4 | direction of motion; binocular disparity | to derive | **event-driven** | **retinotopic**, achromatic, coarse-spatial |
| ← V2 thick stripes, onto layer 4 | binocular disparity; high-speed sensitivity; surround suppression | to derive | event-driven | **retinotopic**, achromatic |
| ← V3, onto layer 4 | as the V2 route, plus dynamic form: contour bound to direction | to derive | event-driven | retinotopic |
| ← lateral geniculate nucleus, direct | **owed** | owed | event-driven | owed |
| ← superior colliculus, di-synaptic via pulvinar | **owed** | owed | event-driven | owed |
| ← pulvinar | **two things on one wire**: a driver-reflecting visual signal, and attentional gain plus cross-areal synchrony | to derive | event-driven | to derive |
| ← frontal eye field, all cortical layers | **enhancement or suppression by location — not a stimulus code** | to derive | event-driven | **spatial, and the payload is a gain over locations rather than a content map** |
| ← medial superior temporal area; ← posterior parietal areas, onto layer 1 | **owed** | owed | event-driven | owed |
| → medial superior temporal area | **integrated global motion**: one pattern-motion direction, speed, motion-in-depth, figure–ground | to derive | event-driven | retinotopic |
| → smooth-pursuit oculomotor circuitry | target velocity as a pursuit command | to derive | event-driven | to derive |
| → ventral intraparietal area; → lateral intraparietal area | **owed at this end**, typed at both consumers | owed here | event-driven | **owed here; the consumers say eye-centred / retinotopic** |
| → V1 (feedback), layer 1 and 2, 5, 6 | contextual and attentional modulation, figure–ground and border-ownership context, attentional gain — **not a new stimulus code** | to derive | event-driven | retinotopic |
| → V2 (feedback), layer 1 | **owed at both ends** | owed | event-driven | owed |

**Two rows are the reason this field exists in this section.** The **frontal eye field** row carries a
gain over locations and not a content map, so a consumer summing it with the stimulus lines would be
reading an attentional weight as evidence. And the **outbound intraparietal** rows are *owed here and
typed there* — **the producer does not know what it is sending.** A representation declared once per
line cannot be declared at all when the only end that types it is the receiving one, and **that is a
finding about the pair rather than about either entry.**

**The first three input rows are the section's first latency failure in the Representation field.**
Rows 1, 2 and 3 differ in payload only partially — row 1 and rows 2–3 overlap on direction and
disparity — and **row 1's distinguishing property is that it arrives earlier.** There is no column in
this table for that, because latency is an architecture field copied under §3 and not restated here,
and it reads *to derive*. **So the table cannot express the difference between the direct and indirect
routes**, and neither can the code.

## Algorithm

- **Transform.** **Four operations, and only two have a standard name that the architecture licenses.**
  1. **Direction selectivity** and **speed tuning** — a tuned response over a motion parameter. **No
     arithmetic is stated above**, and the obvious candidate is a spatiotemporal oriented filter, which
     **is not written here**: nothing in the architecture names a filter, and a well-formed invented
     one reads exactly like a derived one.
  2. **Motion integration** — local components resolved into **global pattern motion, solving the
     aperture problem.** **The transformation is local vectors in, one vector per region out**, which
     the architecture states directly and which is the closest thing to an operation in this entry.
     **It is a many-to-one reduction over a spatial neighbourhood with a constraint-satisfaction
     character**, and the constraint is the aperture problem — but **which reduction is not stated**
     and is not invented here.
  3. **Motion-in-depth and disparity** — a second tuned response over a second parameter, on the same
     cells. See Arrays.
  4. **Motion opponency with antagonistic surrounds**, yielding **figure–ground from motion.** A
     centre–surround difference over the direction map is the candidate and **it is not written**,
     because the centre–surround question is §10's and is Micky's.
- **The stated function demands an internal edge that is recorded nowhere, and it blocks the one
  operation this entry could otherwise carry.** Integrating local component motions into one pattern
  motion **requires signal to cross direction columns**, since the components and the resolved pattern
  have different directions by construction. **So an internal edge crossing the direction map is
  demanded by the stated function and is not recorded** — the sharpest dangling requirement in the
  visual line.
  **The design consequence is exact:** `Transform` item 2 above is the entry's headline operation, and
  **there is no edge in the array vocabulary along which it could run.** The direction axis exists;
  nothing connects positions along it. Recorded, not patched.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `mt_active` | (L, D, Z, P) | open — emission question | to derive | to derive |
  | `mt_threshold` | (L, D, Z, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `direction_preference` | (D,) | to derive | 0 … 2π | radians of motion direction |
  | `disparity_preference` | (Z,) | to derive | to derive | binocular disparity |

  **L = 8 laminae**, and the count does not divide among them: ~15M is one figure for the area and no
  per-lamina number exists, so **an array for layer 4 cannot be sized however precisely the edges name
  it** — and five of this entry's input edges name layer 4 or layer 1 as their termination.
  **D and Z are two superimposed maps and the array carries them as two axes, which is the only
  representation available and is a stronger claim than the biology makes.** A position has both a
  direction preference and a disparity preference, and **an edge terminating on it terminates on
  both**. Writing `(D, Z, P)` as a product asserts that every direction-column value co-occurs with
  every disparity-domain value at every position, and **the architecture says the disparity map does
  not tile the area uniformly** — some regions contain neurons with poor disparity tuning. **So the
  product form over-allocates and the amount is not derivable.** Recorded.
  **Speed has no axis at all.** Speed preference is **clustered and explicitly not columnar**, so it is
  neither a map nor a per-unit scalar that any stated organisation indexes. **A third tuned property
  with no place to live in a rank-4 sheet** — carried as a per-unit value with no axis, and what that
  means for allocation is owed.
  **P is not sized.** The architecture gives surface figures — motion domains **2–3 mm²**, spaced
  **2–3 mm** — and no total area, so P cannot be derived from them.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~15,000,000**, high variance | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling, because fan-in is underived on every edge | architecture Sizing |
  | `parameter_memory` | bytes | **30.00 MB** at 15M × 16 bits | recomputed from the two above |
  | `lamina_count` L | laminae | **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided | architecture Function |
  | `direction_column_count` D | columns | to derive | not supplied above |
  | `disparity_domain_count` Z | domains | to derive | not supplied above |
  | `motion_domain_count` | domains | **3–4**, each **2–3 mm²**, spaced **2–3 mm**, ~**15%** of surface | architecture Shape |
  | `direction_selective_fraction` | fraction | ~**85%** of neurons | architecture Shape |

  **The last two parameters disagree by 5.7-fold and the architecture records the disagreement rather
  than resolving it.** 85% of neurons are directionally selective while the imaged domains occupy 15%
  of the surface. **Either the domains are not where most direction selectivity lives, or the imaging
  measures something narrower than direction selectivity. Unresolved.** **At this rung the consequence
  is that D cannot be derived from the domain count**, because it is not established that the domains
  are the columns.
- **Update equation.** **Waiting on the emission question**, and on three things this entry has beyond
  it: the arithmetic of direction and speed tuning, the reduction that performs motion integration, and
  **the internal edge that reduction would have to run along.** What is fixed regardless of all four:
  **local vectors in, one vector per region out** — so any equation here **reduces cardinality along
  the spatial axis** and does not merely re-weight it. That is a real constraint and it is the one this
  entry can state exactly.
- **State carried between updates.** `mt_active`, and whatever the motion-integration reduction holds
  while it settles. **The integration is a resolution of competing local measurements and the
  architecture does not say whether it is iterative**, so whether there is state at all in that step is
  **to derive**. Initial values: to derive. **State memory is not parameter memory and the two are
  never summed.**
- **Edge storage.** 8 input edges, 6 output edges. Line counts: all to derive — no fan-in or fan-out
  is supplied on any edge in this entry. Latency to derive. Interval unset. **Not summable.**
  **And this is the entry where the interval choice is not merely unknown but constrained:** two of its
  input edges are distinguished only by latency, so an interval coarse enough to make them equal
  **merges them.**
- **Adaptation.** **None set.**
- **Open, beyond the standing list.**
  - **The internal edge crossing the direction map**, demanded by the stated function and recorded
    nowhere. Architecture rung, and the entry's headline operation cannot run without it.
  - **The arithmetic of direction and speed tuning**, and of the integration reduction.
  - **D and Z**, neither of which is supplied, and **D is not derivable from the motion-domain count**
    while the 5.7-fold coverage mismatch stands **unresolved**.
  - **Speed, which is a tuned property with no axis** in a rank-4 sheet.
  - **P**, with no total surface area to derive it from.
  - **The per-lamina partition of the count**, without which five edges terminate on places that
    cannot be sized.
  - **The product form of (D, Z)** over-allocates by an amount that is not derivable.
  - **Two payloads owed at this end and typed at the consumers'** — the intraparietal outputs — so this
    producer does not know what it sends.
  - **One endpoint that is a class and names no region**: smooth-pursuit oculomotor circuitry.
  - **One endpoint that is a class and does not resolve**: posterior parietal areas, whose file's five
    entries declare no output here.

---

# 2. Medial superior temporal area

## Contract

**Inputs.**
- **← the middle temporal area** — integrated motion vectors, retinotopic.
- **← vestibular nuclei by way of the thalamus** — the **computed** self-motion estimate, not the
  raw transducer lines. **The first cortical edge in the file on which a non-visual payload arrives
  into a visual area, and the whole function of the stage depends on it:** without it, optic flow
  cannot be attributed to self-motion rather than to the world. Three properties constrain it: it
  has **velocity-like temporal dynamics**, the form that combines with visual motion rather than
  with acceleration; it modulates **during self-motion and not with changes of orientation relative
  to gravity**, so **it is not an attitude signal**; and the tilt-versus-translation ambiguity is
  **already resolved before this edge**, by combining otolith and canal signals, described in the
  Purkinje cells of the cerebellar nodulus and uvula. **Naming the upstream stages is owed.**
  **The route is contested and the evidence runs against it.** There is reported to be a lack of
  anatomical evidence for a vestibular projection here through the thalamus, and latency orders the
  three areas **parieto-insular vestibular cortex → ventral intraparietal area → this area**, with
  this area showing **the longest latencies** — the opposite of what a direct thalamic input
  predicts. **The thalamic file carries no relay for the route**, and **the cortical alternative
  requires a ventral intraparietal → this area edge that neither entry declares.**
- **← the pursuit area of the frontal eye field** (`11_frontal_lobe`), reciprocally — payload
  **owed**. **That area carries visual, vestibular and combined heading tuning of its own, so it is
  not simply downstream.** That file's frontal eye fields entry declares
  `→ the medial superior temporal area, reciprocally, from the pursuit area` **and**
  `→ the ventral intraparietal area, reciprocally, from the pursuit area` — **two output lines, both
  attributing the edge to a pursuit sub-element, both naming this file's structures.**
  **What is true is narrower and still worth carrying.** The pursuit area is **not a heading and
  not an entry** there: it appears only as a sub-element attribution on those two lines, it has no
  count, no shape and no inputs of its own, and that file's structure list carries a single frontal
  eye fields entry. **So the far end names the sub-element without describing it**, which is a
  different failure from not naming it at all — and the heading tuning this line attributes to the
  area has nowhere to live at the producer. **Owed at the source: give the pursuit area an entry,
  or state that the frontal eye fields entry covers it and carry the tuning there.**
- **← extraretinal eye-movement / efference copy** — the eye's own velocity command, **what the
  system did, so that the flow it caused can be subtracted.** **Source region still not named.**

**Outputs.** **→ the ventral intraparietal area** — global optic-flow structure plus **heading**
and the self/object attribution. **→ the medial intraparietal area** (`06_posterior_parietal`), **→ the supramarginal
gyrus** (`06_posterior_parietal`), **→ the lateral intraparietal area** — payloads **owed** here, and two of the three
existed only at the consumer's end. **→ the pursuit area of the frontal eye
field** (`11_frontal_lobe`), reciprocally — pursuit and gaze-target velocity;
the producer's reciprocal limb is declared there from the same sub-element,
and is untyped, **so this end carries the payload for both directions.** **→ the middle temporal area**
(feedback), onto layer 1 — **owed.**

**Sizing.** Basis: **per hemisphere.** **~15M neurons**, and **softer than the middle temporal
area's**: no comparable myeloarchitectonic signature and retinotopy crude to absent, **so both its
borders and its count are loose.** At the 16-bit ceiling: **30.00 MB.**

**Shape.** Rank 3: **(lamina, division, position)** — eight laminae, two divisions, and
**tangential sub-elements unknown**: no columnar or compartmental map was found here, unlike the
area immediately upstream, which has two. **Whether that reflects the anatomy or the reading is not
established.**
**And a third division that is not spatial at all** — the congruent and opposite cells above.
Under cue combination the two behave in **opposite directions**: congruent cells become **more**
sensitive, paralleling the animal's behavioural improvement, and opposite cells become **less**
sensitive.

**Edge latency.** All edges **to derive** — and latency is the evidence the contested vestibular
route turns on, so **the field that would settle the route is the field the section cannot state.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← middle temporal area | integrated motion vectors | to derive | **event-driven** | **retinotopic** |
| ← vestibular nuclei by way of the thalamus | the **computed** self-motion estimate — **not the raw transducer lines** | to derive; **velocity-like temporal dynamics**, the form that combines with visual motion rather than with acceleration | event-driven | **head- or body-centred** — and explicitly **not an attitude signal**, modulating during self-motion and not with orientation relative to gravity |
| ← pursuit area of the frontal eye field, reciprocally | **owed** | owed | event-driven | owed |
| ← extraretinal eye-movement / efference copy | the eye's own **velocity** command | to derive | event-driven | eye; **source region not named** |
| → ventral intraparietal area | global optic-flow structure plus **heading** and the self/object attribution | to derive | event-driven | **mainly eye-centred for the visual heading** |
| → medial intraparietal area; → supramarginal gyrus; → lateral intraparietal area | **owed** | owed | event-driven | owed |
| → pursuit area of the frontal eye field, reciprocally | pursuit and gaze-target velocity | to derive | event-driven | to derive — **this end carries the payload for both directions** |
| → middle temporal area (feedback), layer 1 | **owed** | owed | event-driven | owed |

**Row 2 is the row the whole entry depends on and it is the row whose route is contested.** The
architecture types the payload in three independent ways — dynamics, what it does not vary with, and
what has already been resolved before it arrives — **and states that the anatomical route delivering it
may not exist.** The alternative route **requires a ventral intraparietal → this area edge that neither
entry declares.** So the line has a well-typed payload and no established producer.

**Rows 1 and 2 arrive in different frames and single neurons combine them anyway.** Row 1 is
retinotopic; row 2 is head- or body-centred. The architecture states, at the entry below, that **the
visual signal stays mainly eye-centred and the vestibular signal is head- or body-centred, and single
neurons nevertheless combine them** — so **whatever reconciles the frames is not a change of frame
before combination.** **A design that inserted a transform to bring them into register would be
building the intuitive engineering solution the architecture explicitly refuses.**

## Algorithm

- **Transform.** **Optic-flow structure over large receptive fields** — expansion/contraction,
  rotation, deformation, translation — **heading as the focus of expansion**, **self- versus
  object-motion disambiguation**, and smooth-pursuit signals. **First dorsal stage that is not purely
  visual.**
  **One arithmetic statement is licensed here and it is the only one in this file:** individual
  dorsal-division cells are tuned to **both** visual and vestibular heading and combine them
  **linearly with subadditive weights.** **That is a named form — a weighted linear combination whose
  weights sum to less than one — and it is stated at the rung above.**
  **It is still not writable under the current unit model.** A threshold gate sums **equal-weight**
  inputs; *subadditive weights* means unequal, and specifically means two weights whose sum is under
  unity. **So the one entry in this section with a stated arithmetic is blocked by the same item as
  the three that have none**, and the weights themselves are not given. *(The linear-subadditive
  statement is the architecture's; that the equal-weight unit cannot carry it is Claude's reading.)*
- **Heading is the focus of expansion, which is a named geometric operation and is recorded as one.**
  Locating the singular point of a flow field is standard, and **the architecture names the quantity
  and not the method**, so the operation is named here and no method is written.
- **Most cells prefer lateral headings and are broadly tuned, which makes the population most
  discriminating around straight ahead.** **This is a property of the population's tuning-curve
  distribution and it constrains any eventual decode**: the sharpest discrimination sits where the
  fewest cells have their peaks. Carried as a parameter constraint rather than as an equation.
- **The congruent / opposite division is a sub-element that is not a place, and at this rung it has no
  index.** Heading-tuned cells divide into **congruent** and **opposite** cells **by the relation
  between their visual and vestibular tunings**; they are **interleaved, with no spatial segregation
  found**. **What it would mean for an edge to terminate on the congruent cells and not the opposite
  ones is owed**, and the architecture records that it may not be answerable in the slot's present
  form.
  **The representation available is a boolean mask over the population, and a mask is not a
  sub-element**, because nothing can terminate on it: an `Endpoint` names a structure or a
  sub-element, and there is no name here for a set defined by a relation between two tuning curves.
  Recorded. *(The interleaving is the architecture's; that a mask cannot serve as an endpoint is
  Claude's reading of the shared vocabulary.)*
- **What the opposite cells are proposed to be for, carried as a candidate and not as a finding.** A
  cell whose visual and vestibular heading preferences are **inverted** reports the **disagreement**
  between the two cues, and a disagreement between optic flow and inertial motion **is the signature of
  something in the world moving independently of the observer.** A mixed population is proposed as the
  substrate for that causal-inference problem, and a linear decode of it approximates marginalising
  self-motion out. **Recorded as a candidate mechanism rather than a finding:** peer review noted that
  the analyses did not isolate the opposite cells and test performance with and without them, so the
  contribution attributed to them is inferred from the population result rather than demonstrated on
  that subpopulation. **Nothing is designed from it.**
- **One causal asymmetry that complicates the entry's own account, and it constrains the output
  lines.** Microstimulation here **biased heading judgements made from optic flow** but **did not**
  significantly affect vestibular heading judgements — **even though single cells carry both cues.**
  **The two payloads are not symmetrically read out downstream**, and the stage should not be taken to
  contribute to both equally. **So an output array carrying "heading" as one quantity would be
  asserting a symmetry the evidence refuses.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `mst_active` | (L, V, P) | open — emission question | to derive | to derive |
  | `mst_threshold` | (L, V, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `visual_heading_preference` | (L, V, P) | to derive | to derive | heading direction |
  | `vestibular_heading_preference` | (L, V, P) | to derive | to derive | heading direction |
  | `congruence_mask` | (L, V, P) | boolean | congruent / opposite | **not a sub-element; no edge can terminate on it** |

  **L = 8 laminae, V = 2 divisions**, and the count divides among neither: ~15M is one figure and no
  per-lamina or per-division number exists. **The two divisions differ in receptive-field size and in
  function** — dorsal for optic flow, heading and self-motion with large fields; lateral for object
  motion and smooth pursuit with smaller fields — **and splitting them into separate entries is owed**,
  so the array carries them as an axis over a structure the architecture says should be two.
  **Tangential sub-elements are unknown**, so P has no internal organisation and no extent.
  **The last three arrays are per-unit properties and not axes**, which is what a sub-element that is
  not a place forces. `congruence_mask` is derived from the relation between the two preference arrays
  and **the architecture does not say what relation** — inverted is stated for the opposite cells and
  no threshold on the relation is given.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~15,000,000**, **softer than the middle temporal area's** — no comparable myeloarchitectonic signature, retinotopy crude to absent, **so both its borders and its count are loose** | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling | architecture Sizing |
  | `parameter_memory` | bytes | **30.00 MB** at 15M × 16 bits | recomputed |
  | `lamina_count` L | laminae | **8** | architecture Shape |
  | `division_count` V | divisions | **2** — dorsal and lateral | architecture Function |
  | `cue_weights` | — | **linear, subadditive** — the sum is under unity and **the values are not given** | architecture Function |

- **Update equation.** **Waiting on the unit's expressiveness**, which here is not the multiply but the
  **unequal weight**. What is fixed regardless: **the two cues are combined on single cells and not by
  two populations meeting later**, so any equation reads both input lines into one unit; and **the
  combination is subadditive**, so an equation that summed them at full weight would over-count the
  agreement case, which is precisely where the behavioural improvement lives.
- **State carried between updates.** `mst_active`, and the preference arrays, which are construction
  constants rather than state under the current adaptation answer. Initial values: to derive.
- **Edge storage.** 4 input edges, 7 output edges across five named targets. Line counts: all to
  derive. Latency to derive — **and on one edge the latency is the evidence the route turns on**, so
  the field the code cannot supply is the field that would settle whether the edge exists. Interval
  unset. **Not summable.**
- **Adaptation.** **None set** — and the architecture records a behavioural change this entry's cells
  undergo, which is not a rule and must not be filed as one: under cue combination **congruent cells
  become more sensitive, paralleling the animal's behavioural improvement, and opposite cells become
  less sensitive.** **That is a described change in the two subpopulations' sensitivity with no rule
  attached**, and adopting any rule that produced it would be choosing a learning rule.
- **Open, beyond the standing list.**
  - **The vestibular route is contested**, the thalamic file carries no relay, and the cortical
    alternative **requires an edge that neither entry declares.** Per §5b this reads **contested** and
    not *to derive*. Source rung.
  - **The upstream stages of the vestibular line**, owed — the payload is well typed and its producers
    are not named.
  - **The source region of the efference copy**, not named.
  - **The pursuit area has no entry**, only a sub-element attribution at the far end, and the heading
    tuning this entry attributes to it has nowhere to live there. Source rung.
  - **The congruent / opposite division has no index**, and a mask cannot be an endpoint.
  - **The relation defining congruence** is not given as a rule.
  - **The cue weights** are stated as subadditive and not given.
  - **The division split into two entries**, owed at the source.
  - **P has no extent and no internal organisation**, tangential sub-elements being unknown.
  - **Three output payloads owed at this end**, to the medial intraparietal area, the supramarginal
    gyrus and the lateral intraparietal area.

---

# 3. Ventral intraparietal area

## Contract

**Inputs.** **← the middle temporal area** — motion in **eye-centred** coordinates, **and it stays
eye-centred here**, so this edge's frame is not changed by the stage receiving it; the producer
declares the payload owed, **so the two ends disagree and neither cites a source.**
**← V3** — dynamic form, contour bound to direction of motion. **← the medial superior temporal
area** — global optic-flow structure plus heading and the self/object attribution.
**← parieto-insular vestibular cortex** — the computed self-motion estimate **in a frame
intermediate between head- and body-centred, which this stage completes to body-centred.**
**← eye-position / efference copy** — **current eye position (eye-in-head): one of the two
variables the gain field multiplies by. Source region not named — owed.**
**← head-position (head-on-body) — no line is declared here and one is required.** The Function
field names **eye and head position** as the multiplicands and this field supplies only the
first. **Head-on-body is a separately measured variable in this area and not a loose synonym
for gaze**: tuning has been measured against it as its own axis, with the head free to rotate
and its angular position tracked, independently of eye-in-head. Payload: head position relative
to the body. **Producer not named anywhere — owed at the source**, where a neck-proprioceptive
candidate is recorded. Fan-in: to derive.
**← somatosensory (facial / head tactile)** — touch location in a **skin-surface**
frame.

**Outputs.** **→ premotor area F4** — object location and motion in **head- and body-centred
coordinates**, peripersonal and defensive space. **The payload change at this stage is the
coordinate frame and nothing else**: the same objects go in and come out, re-expressed in a frame
the body can act in. **That is what the gain fields buy, and it is the reason the entry exists.**
(`11_frontal_lobe`.) That file's premotor entry declares
`← the ventral intraparietal area, terminating on F4` — **the edge and the sub-element both, and it
is one of three parietal inputs there written by terminating sub-element**, alongside the anterior
intraparietal area on F5 and the medial intraparietal area on F2. **So the F-numbering this line
asked for is the convention in use at the far end.** **That end is untyped**, and the coordinate
frame this line makes its whole justification exists only here. **→ the lateral intraparietal area** — body-centred locations for
prioritisation, and **the two ends disagree by one frame.** **→ the medial intraparietal area** (`06_posterior_parietal`) —
body-centred locations for reach; **the consumer's declaration is the vaguer.** **→ the anterior
intraparietal area** (`06_posterior_parietal`) — head- and body-centred location and motion for grasp: **the one edge out of
this entry whose two ends agree, in the same words.** **→ the pursuit area of the frontal eye
field** (`11_frontal_lobe`), reciprocally — heading in some frame, **owed**. That entry declares
`→ the ventral intraparietal area, reciprocally, from the pursuit area`: **the sub-element is
named there and not described there.**

**Sizing.** Basis: **per hemisphere.** **~12M neurons**, **very high variance — the softest count
in the map**: the area sits in the fundus of the intraparietal sulcus, lightly myelinated, with no
clean architectonic border, and **the macaque area has expanded into several human parietal
areas.** At the 16-bit ceiling: **24.00 MB.**

**Shape.** Rank 3: **(lamina, division, position)**, tangential organisation unknown.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← middle temporal area | motion | to derive | **event-driven** | **eye-centred, and it stays eye-centred here** — the frame is not changed by this stage. **The producer declares the payload owed, so the two ends disagree and neither cites a source** |
| ← V3 | dynamic form: contour bound to direction of motion | to derive | event-driven | retinotopic |
| ← medial superior temporal area | global optic-flow structure plus heading and the self/object attribution | to derive | event-driven | **mainly eye-centred** for the visual heading |
| ← parieto-insular vestibular cortex | the computed self-motion estimate | to derive | event-driven | **intermediate between head- and body-centred, which this stage completes to body-centred** |
| ← eye-position / efference copy | **current eye position** | to derive | event-driven | **eye-in-head. Source region not named — owed** |
| ← head-position (head-on-body) | **head position relative to the body** | to derive | event-driven | **body. No line is declared and one is required — producer not named anywhere** |
| ← somatosensory (facial / head tactile) | touch location | to derive | event-driven | **skin-surface** |
| → premotor area F4 | object location and motion, peripersonal and defensive space | to derive | event-driven | **head- and body-centred.** The far end is untyped, **so this frame exists only here** |
| → lateral intraparietal area | locations for prioritisation | to derive | event-driven | **body-centred at this end; the consumer declares body- and head-centred — the two ends disagree by one frame** |
| → medial intraparietal area | locations for reach | to derive | event-driven | **body-centred; the consumer's declaration is the vaguer** |
| → anterior intraparietal area | location and motion for grasp | to derive | event-driven | **head- and body-centred — the one edge out of this entry whose two ends agree, in the same words** |
| → pursuit area of the frontal eye field, reciprocally | heading | **owed** | event-driven | **owed — "in some frame"** |

**Seven input lines arrive in six different frames — and one of the seven does not exist yet.** This is the densest frame table in the file and it is the reason the field is declared at the
line: eye-centred, retinotopic, intermediate head/body, eye-in-head, and skin-surface, all landing on
one structure. **A consumer inheriting a single frame from the structure would be wrong five times out
of six.**

**Rows 5 and 6 are the load-bearing ones and neither has a producer.** *Eye-in-head position* is one of
the two variables the gain field multiplies by, and its **source region is not named**;
*head-on-body position* is the other, and **no line for it is declared at all.** **So the mechanism
the entry rests on has no declared input on either multiplicand**, which is a stronger statement
than a payload being untyped.
**And head-on-body is not a loose synonym for gaze**, which is the reading that would make the
single eye-position line sufficient. Tuning in this area has been measured against head-on-body as
its own axis, with the head free to rotate and its angular position tracked, independently of
eye-in-head. **A structure whose tuning is measured against an axis needs an input carrying that
axis.**

## Algorithm

- **Transform.** **Reference-frame transformation — coding of motion and location in frames other than
  the retinal one, implemented by gain fields: a sensory receptive field multiplicatively modulated by
  eye and head position.** **This is a named operation and the architecture names it.**
  **It is the one operation in the file with a stated arithmetic form, and it is the one arithmetic the
  unit model excludes.** A gain field is a product: a sensory response scaled by a position signal.
  **The threshold-gate model has equal weights and no multiply, by construction**, which is what makes
  the stored value a single threshold. **So no update equation is written for this entry, and the
  reason is not that the architecture is silent — it is that the architecture is explicit and the unit
  cannot express what it says.** §10's unit-expressiveness item, and Micky's.
- **The payload change at this stage is the coordinate frame and nothing else.** **The same objects go
  in and come out, re-expressed in a frame the body can act in.** **That is a strong constraint on any
  eventual equation and this entry can state it exactly:** the output arrays have the **same cardinality
  and the same contents** as the input arrays, and differ only in the frame the positions are expressed
  in. **An equation here that added, removed or merged objects would have exceeded the stated
  transform.**
- **The transformation is not applied to everything that arrives, and this is where an engineer's
  instinct is wrong.** Vestibular heading is **body-centred, transformed out of the head-centred frame
  it arrives in**; visual heading from optic flow is **approximately eye-centred and not transformed** —
  **tested directly as a hypothesis and refused, with no neuron found with head-centred visual heading
  tuning** and only a small proportion intermediate. **So the intuitive engineering solution — bring
  both cues into a common frame, then combine — is not what happens.** Across this area and the medial
  superior temporal area **the visual signal stays mainly eye-centred and the vestibular signal is head-
  or body-centred, and single neurons nevertheless combine them. Whatever reconciles the frames is not
  a change of frame before combination.**
  **The design consequence, and it is the sharpest instruction in this file:** the transform is applied
  **per line, not per structure.** A design that ran every input through one frame conversion before
  combining would be building the refused hypothesis, and it would look entirely reasonable.
- **The vestibular frame is further hybrid and gaze-dependent:** this area shows **either** a
  body-centred or a world-centred frame **depending on gaze direction** — **a flexible switch between
  two frames, not a fixed one.** **So the frame on that line is not a constant and the Representation
  row above cannot hold it as one.** A frame that is a function of another input's value has no
  representation in the shared vocabulary, where `Representation.frame` is a string. Recorded.
  *(The gaze-dependence is the architecture's; that the vocabulary cannot hold a frame-valued function
  is Claude's reading.)*
- **And the frame may be a property of the measurement rather than of the area.** Visual receptive
  fields mapped with **moving bars** are reported **head-centred in a substantial proportion** of
  neurons, while visual heading from **large-field optic flow** is eye-centred with no head-centred
  cells found. **The same modality in the same area gives different answers, and the difference tracks
  the stimulus and the property measured rather than the cells. Unresolved** — and for a description
  whose purpose is to state what is on a wire, the warning is that **the frame of a payload here may
  not be well defined independently of what is being asked of it.** **Nothing is designed from either
  reading**, and per §5b this stands **unresolved** rather than *to derive*.
  **Two things about the disagreement are settled, and they matter at this rung.** The moving-bar
  studies **did not manipulate head position relative to the body**, so head- and body-centred frames
  were not separable there: the disagreement is asymmetric, one side resting on a design that could
  distinguish the frames and the other on designs that could not. And in this area **a shift of a
  tuning curve is hard to distinguish from a change in response gain**, because most of its neurons
  prefer lateral motion and are therefore monotonically tuned around straight ahead, **unless the
  complete tuning function is measured.** **That is a design-rung fact and not only a methodological
  one:** a shift and a gain are two different operations over an array — a re-index and a scaling —
  and the evidence separating them exists only under a measurement condition. **What remains open is
  named:** optic-flow tuning and receptive-field shift have not been tested in the same neurons.
- **The frame table for this structure is four rows, not two, and every modality differs.**
  Vestibular heading is **body-centred**; visual heading from optic flow is **eye-centred**, with 52%
  of classifiable neurons significantly eye-centred and **none** head- or body-centred; facial
  **tactile** receptive fields are **head-centred**; **auditory** receptive fields lie on a
  **continuum between eye- and head-centred.** A subset of neurons was tested with two of the
  protocols, so **the disparity holds within single multisensory cells and is not a difference
  between two populations.** **At this rung that forbids one array per structure carrying a frame:**
  the frame belongs to the line, and the same cell holds several.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `vip_active` | (L, V, P) | open — emission question | to derive | to derive |
  | `vip_threshold` | (L, V, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `receptive_field_response` | (L, V, P) | open | to derive | sensory response, per line |
  | `eye_position` | to derive | open | to derive | **eye-in-head position — the gain-field multiplicand, with no declared producer** |
  | `head_position` | to derive | open | to derive | head position — **named in the transform and on no input line at all** |

  **L = 8 laminae, V = 2 divisions — medial and lateral, their separate payloads owed** — and the
  count divides among neither. **Tangential sub-elements are unknown**, so P has no internal
  organisation and no extent.
  **`eye_position` and `head_position` are the two arrays the entry's function requires and neither has
  a shape.** The transform is stated as modulation by **eye and head position**; the Inputs field
  declares an eye-position line whose **source region is not named**, and a head-position line that
  **is required and not declared.** **So one multiplicand arrives from an unnamed producer and the
  other does not arrive at all.** Recorded, not patched, and the gap is now two lines wide rather
  than one.
  **`receptive_field_response` is per line and not per structure**, because the transform is applied to
  some lines and not others — see the Transform field. **A single response array over the structure
  would have merged the transformed and untransformed lines**, which is exactly the refused hypothesis.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~12,000,000**, **very high variance — the softest count in the map** | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling | architecture Sizing |
  | `parameter_memory` | bytes | **24.00 MB** at 12M × 16 bits | recomputed |
  | `lamina_count` L | laminae | **8** | architecture Function |
  | `division_count` V | divisions | **2** — medial and lateral, **separate payloads owed** | architecture Function |
  | `gain_field_weights` | — | **not given, and not expressible under the current unit** | architecture Function |

  **The count is the softest in the map and the architecture says why in a way that matters to the
  code:** the area is **lightly myelinated with no clean architectonic border**, and **the macaque area
  has expanded into several human parietal areas.** **A count whose region has split between species is
  not the same kind of number as one whose region has a stain** — so 12M is not merely uncertain, it may
  be a count of a thing that is one structure in one species and several in another.
- **Update equation.** **Not written, and this entry is the reason the file's standing list opens with
  the unit's expressiveness.** The operation is named, its form is stated, and the unit cannot perform
  it. Beyond that: one multiplicand has no producer and the other has no line. What is fixed regardless
  of all three: **cardinality and contents are preserved and only the frame changes**, and **the change
  is per line rather than per structure.**
- **State carried between updates.** `vip_active`, and `eye_position` / `head_position` if they are held
  rather than read fresh — **which the architecture does not say**, and the difference matters, because
  a gain field reading a stale position produces a systematically wrong frame. Initial values: to
  derive.
- **Edge storage.** 6 input edges, 5 output edges. Line counts: all to derive. Latency to derive.
  Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Open, beyond the standing list.**
  - **The gain-field multiply**, which the unit model excludes by construction. **Micky's**, and it is
    this entry's whole reason for existing.
  - **The eye-position line has no named producer**, and **the head-position line is required and not
    declared**, so the mechanism the entry rests on has no declared input on either multiplicand.
    Source rung, and the research is specified rather than open-ended.
  - **The frame on the vestibular line is gaze-dependent** — a switch between body-centred and
    world-centred — and the shared vocabulary holds a frame as a string.
  - **The frame may be a property of the measurement**, moving bars and optic flow giving different
    answers in the same area. **Unresolved.**
  - **The two divisions' separate payloads**, owed.
  - **P has no extent**, tangential organisation being unknown.
  - **One outbound edge disagrees with its consumer by one frame** — the lateral intraparietal line.
  - **The count may be counting a structure that is several in this species.**

---

# 4. Lateral intraparietal area

## Contract

**Inputs.** **← the middle temporal area** — visual motion, retinotopic, **reaching the ventral
subdivision and not the dorsal one.** **← the medial superior temporal area** — optic flow,
retinotopic; the same ventral selectivity is asserted, **but the 1990 tracer result is not
separated between the two sources, so which of the two it was shown for is owed.**
**← pulvinar** — the two-part pulvinar payload; **which subdivision it reaches is unknown, and
given that every other visual input here is subdivision-specific, that is owed.**
**← ventral-stream visual areas**, onto the **dorsal** subdivision — payload **owed**, **and the
endpoint is a class the visual file does not resolve**: none of the four ventral-stream entries
declares an output here, and the one candidate found runs the other way on the subdivision.
**← frontal eye field** (`11_frontal_lobe`) — corollary discharge of the saccade command, relayed
from the superior colliculus through the thalamus: ***the eye is about to move, by this vector.***
**The thalamic relay is still unnamed and the thalamus file does not supply it.**
**The gap is located precisely, at three files at once.** The frontal
entry declares `→ the lateral intraparietal area, carrying the corollary discharge of the saccade
command` and states the path runs through the **mediodorsal** thalamus.
`14_brainstem_midbrain_hypothalamus`'s superior colliculus declares
`→ frontal eye field and lateral intraparietal area, reciprocally via the thalamus` and types it in
**this line's own words** — *the eye is about to move, by this vector* — adding that its usefulness
**depends on arriving before the movement, a latency requirement stated without a latency.**
**And `12_thalamus`'s mediodorsal entry names the frontal eye fields among its five cortical
outputs and declares no intraparietal target of any kind.** **So three files declare a route
through a relay, the relay is named by one of them, and the nucleus named declares only the first
leg.** **The gap is the second leg and it is at the nucleus**, not at either cortical end. Owed at
the source, in `12_thalamus`.
**← prefrontal area 46** — top-down goal relevance, **a weighting, not a stimulus.**
**← auditory saccade-target signals** — sound location **converted into eye-centred coordinates**,
a supramodal target, **which is why this map can rank a sound against a sight**; **the converting
stage is not named anywhere, and it is the interesting part of the edge.**
**← the ventral intraparietal area** — body- and head-centred locations, **disagreeing with the
producer by one frame.** **← the angular gyrus** and **← the supramarginal gyrus** — payloads
**owed**, and **the producers declare nothing; the supramarginal entry declares the opposite
direction instead.**

**Outputs.** **→ the superior colliculus** (`14_brainstem_midbrain_hypothalamus`), from the
**ventral** subdivision onto its intermediate and deep layers — the priority map: **one scalar per
retinotopic location**, peak specifying the next saccade target. **The payload is a scalar field over space and it is deliberately
modality-free: what it has thrown away — colour, identity, pitch — is as important as what it
keeps.** **The ventral subdivision carries this edge and the dorsal one does not**, so a consumer
reading "the lateral intraparietal area projects to the colliculus" **is reading half the area.**
**→ frontal eye field** (`11_frontal_lobe`), **→ prefrontal area 46** (`11_frontal_lobe`),
**→ the anterior intraparietal area** (`06_posterior_parietal`), **→ the angular gyrus**
(`06_posterior_parietal`), **→ parahippocampal temporal area TF** — the same priority map; two far
ends agree and are untyped, one declares nothing, one is unchecked.
**The two frontal limbs are two-ended in both directions.** The
frontal eye fields declare `← the lateral intraparietal area`, marked there *two-ended and
agreeing*; the dorsolateral prefrontal entry declares `← the lateral intraparietal area, which
names area 46` and `→ the lateral intraparietal area, which names area 46` — **naming the
sub-element this line names, from its own side, in both directions.**
**And the frontal-eye-field pair is the clearest case in this section of a reciprocal edge whose
two limbs are not the same edge.** Outbound from here is the **priority map**: a scalar field over
retinotopic space, deliberately modality-free, what it has thrown away as important as what it
keeps. Inbound is the **corollary discharge**: a single impending eye-movement vector, arriving by
a two-hop subcortical route with a latency requirement. **Different payloads, different arities,
different routes, and one of the two limbs is direct while the other is relayed.** **Recording the
pair as *reciprocal* or as *two-ended* says nothing about any of that**, and the two limbs are
written separately here for that reason.

**Sizing.** Basis: **per hemisphere.** **~20M neurons**, high variance but **firmer-bordered than
the ventral intraparietal area** — in the lateral bank of the intraparietal sulcus with two
myeloarchitectonic zones. At the 16-bit ceiling: **40.00 MB.**

**Shape.** Rank 3: **(lamina, subdivision, retinotopic position)** — and **the subdivision axis
carries a signed payload difference.** The ventral subdivision holds a **single topographic map of
the contralateral hemifield** with a foveal representation rostrally, connects strongly with the
frontal eye field and the deep collicular layers, and a GABA-A agonist injected into it **sharply
reduces express saccades** while the same injection dorsally does not. Along the dorsal-to-ventral
axis the population shifts from cells driven by **visual** events to cells driven by **visual and
saccadic** events together. **So the map is not uniform and an edge terminating "on the lateral
intraparietal area" is under-specified.**

**Edge latency.** All edges **to derive** — and **one of them has a deadline**: the corollary
discharge is only useful if it arrives before the eye moves.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← middle temporal area → **ventral** subdivision | visual motion | to derive | **event-driven** | **retinotopic** |
| ← medial superior temporal area → **ventral** subdivision (asserted) | optic flow | to derive | event-driven | retinotopic |
| ← pulvinar | the two-part pulvinar payload | to derive | event-driven | to derive — **which subdivision it reaches is unknown, and every other visual input here is subdivision-specific, so that is owed** |
| ← ventral-stream visual areas → **dorsal** subdivision | **owed** | owed | event-driven | owed — **and the endpoint is a class the visual file does not resolve** |
| ← frontal eye field (corollary discharge) | **a single impending eye-movement vector** — *the eye is about to move, by this vector* | to derive | **event-driven, and the event is a saccade about to happen** | **eye-movement vector.** **Its usefulness depends on arriving before the movement — an ordering constraint against an external event, and there is no field for it** |
| ← prefrontal area 46 | **top-down goal relevance — a weighting, not a stimulus** | to derive | event-driven | **none — a weight over locations, not a content map** |
| ← auditory saccade-target signals | sound location, **converted into eye-centred coordinates** | to derive | event-driven | **eye-centred — and the converting stage is not named anywhere** |
| ← ventral intraparietal area | locations | to derive | event-driven | **body- and head-centred, disagreeing with the producer by one frame** |
| ← angular gyrus; ← supramarginal gyrus | **owed** | owed | event-driven | owed — **the producers declare nothing** |
| → superior colliculus, from the **ventral** subdivision, onto intermediate and deep layers | **the priority map: one scalar per retinotopic location**, peak specifying the next saccade target | to derive | event-driven | **retinotopic, and deliberately modality-free** |
| → frontal eye field; → prefrontal area 46; → anterior intraparietal area; → angular gyrus; → parahippocampal temporal area TF | the same priority map | to derive | event-driven | retinotopic |

**Row 5 is the payload the shared vocabulary cannot hold.** Its correctness condition is *before the
eye moves* — a predicate over two events — and `Edge.latency_s` is a number of seconds. **The
requirement is stated at three files and the field that would carry it exists at none.**

**Row 6 sets a weight and rows 1–4 supply content, and the map sums them.** *Top-down goal relevance*
is explicitly **a weighting, not a stimulus**, so an update that treated it as another content line
would rank locations by how much attention they already had. **The role belongs on the line.**

**Row 10 is the file's cleanest payload and the cleanest statement of what a payload is.** **One
scalar per retinotopic location**, and **what it has thrown away — colour, identity, pitch — is as
important as what it keeps.** A design that carried modality tags alongside the scalar would have
undone the structure's function, which is to make a sound and a sight comparable.

## Algorithm

- **Transform.** **A priority (salience) map: a retinotopic map ranking locations by behavioural
  priority — bottom-up salience plus top-down attention plus reward — the peak selecting the next
  saccade target, with selection as competition among locations through lateral inhibition.**
  **Three named operations, and the arithmetic of none of them is given.**
  1. **Ranking** — many typed input lines reduced to **one scalar per location**. **A many-to-one
     reduction over modality and source, and the combining rule is not stated.** The output's whole
     value is that it is modality-free, so the reduction is the entry's core operation and it has no
     equation above it.
  2. **Selection by competition through lateral inhibition** — see the next item, which is why this one
     cannot be written.
  3. **Predictive remapping** — see below.
- **The mechanism the Function field rests on has no declared substrate.** Selection is stated to be
  **competition among locations through lateral inhibition, which requires within-map inhibitory edges
  between separated locations, and no such edge is recorded** — the divisional edges are between
  subdivisions, not across the map.
  **The design consequence is the same shape as the middle temporal area's:** the retinotopic axis
  exists, and **nothing connects positions along it**, so the operation the Function field names has no
  path in the array vocabulary. Recorded, not patched.
- **Predictive remapping is a payload change driven by an input whose correctness is an ordering
  constraint.** Just before a saccade, **cells shift receptive fields toward the post-saccadic
  location, driven by corollary discharge.** **This is a re-indexing of the map by a vector delivered
  on an input line**, which is a named operation — a shift, or a gather along the position axis by an
  offset — **and the architecture supplies the vector's meaning and not the shift's arithmetic**, so
  the operation is named and the equation is not written.
  **What is fixed regardless: the shift precedes the movement.** **Arrival order is part of
  correctness here, not of performance.** An implementation that applied the remap after the eye moved
  would produce a structure that satisfies every field in this file and does the opposite of what the
  entry describes. **The scheduling discipline has to be able to express that, and it is Micky's.**
- **Eye-position gain modulation appears here too**, on the entry's own face, and it is the same
  multiply the ventral intraparietal entry rests on. **Not written, for the same reason.**
- **The subdivision axis carries a signed payload difference, and this is the strongest statement in
  the file that an axis is not a formality.** The **ventral** subdivision holds a **single topographic
  map of the contralateral hemifield** with a foveal representation rostrally, connects strongly with
  the frontal eye field and the deep collicular layers, and a GABA-A agonist injected into it **sharply
  reduces express saccades** while the same injection dorsally does not. Along the dorsal-to-ventral
  axis the population shifts from cells driven by **visual** events to cells driven by **visual and
  saccadic** events together. **So the map is not uniform and an edge terminating "on the lateral
  intraparietal area" is under-specified** — three of this entry's input edges and one of its output
  edges name a subdivision, and the rest do not.
  **The two subdivisions are architectonically defined before they are functionally defined**, on two
  independent measures: the ventral is **densely myelinated** and the dorsal **lightly myelinated**,
  and receptor mapping separates them again — N-methyl-D-aspartate, α1-adrenergic and 5-HT1A receptor
  densities are all **higher in the dorsal** subdivision. **Two independent stains agreeing on one
  border is a stronger basis than either alone**, and it is firmer footing than the tangential
  compartments recorded at V4 and the middle temporal area, which rest on function and connection.
- **The intrinsic loop is asymmetric and the asymmetry is the finding, and at this rung it is two
  different operations rather than one bidirectional link.** Retrograde tracing found
  **ventral → dorsal point-to-point**, described as sensory-like, one location talking to its
  counterpart; and **dorsal → ventral widespread**, not point-to-point, one location talking to many.
  **A topographic forward limb and a divergent return limb are the anatomy of a map being read out
  against a broadcast, not of two copies of one map.** It is offered as the intrinsic circuit
  underlying the observation that a cell's **motor** response field is spatially distinct from its
  **sensory** receptive field — **a payload change inside one entry, and the first the file has had to
  record at that scale.**
  **So the two internal edges below are an identity map and a broadcast, and they must not be written
  as one reciprocal link.** One is a per-position pairing and the other is a one-to-many fan; they have
  different arities and different shapes.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `lip_active` | (L, S, P) | open — emission question | to derive | to derive |
  | `lip_threshold` | (L, S, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `priority_map` | (P,) | open | to derive | **one scalar per retinotopic location, modality-free** |
  | `sensory_receptive_field` | (L, S, P) | open | to derive | position |
  | `motor_response_field` | (L, S, P) | open | to derive | position — **spatially distinct from the sensory field on the same cell** |
  | `remap_offset` | eye-movement vector | open | to derive | **applied before the movement** |

  **L = 8 laminae, S = 2 subdivisions**, and the count divides among neither: ~20M is one figure and no
  per-lamina or per-subdivision number exists. **Tangential sub-elements: none reported**, so P's
  internal organisation is a single topographic map of the contralateral hemifield **in the ventral
  subdivision only** — the architecture states that map for the ventral and does not state one for the
  dorsal. **So `priority_map` is a ventral object and the array indexes it under a structure whose
  other half may not carry it.**
  **`sensory_receptive_field` and `motor_response_field` are two position arrays over the same cells
  and they differ.** That is the payload change inside one entry, and it means **a single position
  index per unit is insufficient**.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~20,000,000**, high variance but **firmer-bordered than the ventral intraparietal area** | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling | architecture Sizing |
  | `parameter_memory` | bytes | **40.00 MB** at 20M × 16 bits | recomputed |
  | `lamina_count` L | laminae | **8** | architecture Function |
  | `subdivision_count` S | subdivisions | **2** — ventral densely myelinated, dorsal lightly myelinated | architecture Function |
  | `remap_deadline` | — | **before the eye moves — a predicate, not a duration** | architecture Function and Edge latency |

- **Update equation.** **Not written**, and blocked by four things beyond the standing list: the
  ranking rule that reduces many typed lines to one scalar; the within-map inhibitory edge that
  selection requires and that is recorded nowhere; the shift arithmetic of predictive remapping; and
  the eye-position gain multiply. What is fixed regardless: **the output is one scalar per location and
  is modality-free**, so **no equation may carry a modality tag through to the priority map** — the
  discarding is the function.
- **State carried between updates.** `priority_map`, `sensory_receptive_field` and
  `motor_response_field`, and `remap_offset` for the interval between the corollary discharge arriving
  and the movement occurring. **That last one is state whose lifetime is defined by an external event**,
  and nothing at any rung gives its duration. Initial values: to derive.
- **Edge storage.** 9 input edges, 6 output edges, plus 2 internal edges between subdivisions. Line
  counts: all to derive. Latency to derive. Interval unset. **Not summable.** **And one edge's storage
  is not a quantity of the ordinary kind:** the corollary discharge's values-in-flight figure is
  bounded by an event rather than by a latency.
- **Adaptation.** **None set.** Reward contributes to priority on the entry's own face — **bottom-up
  salience plus top-down attention plus reward** — and **no rule is given for how reward enters the
  ranking.** That is a learning rule and it is Micky's.
- **Open, beyond the standing list.**
  - **The within-map lateral inhibition**, on which selection rests, recorded nowhere. Architecture
    rung.
  - **The ranking rule** that reduces many typed lines to one modality-free scalar.
  - **The second leg of the corollary-discharge route**, at `12_thalamus`'s mediodorsal nucleus, which
    names the frontal eye fields and declares no intraparietal target. Source rung.
  - **The ordering constraint has no field**: *before the eye moves* is a predicate and the vocabulary
    carries seconds.
  - **How reward enters the ranking**, which is a learning rule.
  - **Which subdivision the pulvinar reaches**, owed, when every other visual input here is
    subdivision-specific.
  - **Which of two sources the ventral selectivity was shown for**, owed.
  - **The converting stage** that puts sound location into eye-centred coordinates, named nowhere, and
    **it is the interesting part of the edge.**
  - **One endpoint that is a class the visual file does not resolve**: ventral-stream visual areas.
  - **Two producers that declare nothing** — the angular and supramarginal gyri — and one that declares
    the opposite direction.
  - **The per-lamina and per-subdivision partition of the count.**

---

## Section totals

Copied from the architecture, with one column added at this rung: **the realised store, which here
equals the derived store because every width is already at a container boundary.**

| # | structure | basis | neurons | bits/neuron | parameter memory | realised at 16 bits |
|---|---|---|---|---|---|---|
| 1 | Middle temporal area | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB | 30.00 MB |
| 2 | Medial superior temporal area | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB | 30.00 MB |
| 3 | Ventral intraparietal area | per hemisphere | ~12M | ≤ 16 | ≤ 24.00 MB | 24.00 MB |
| 4 | Lateral intraparietal area | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB | 40.00 MB |
| | **stated total** | per hemisphere | **~62M** | | **124.00 MB** | **124.00 MB** |

**The realisation gap is zero for the first time in the map, and the reason is not good news.** Every
width here is the **16-bit ceiling**, which is a container boundary by construction, so nothing is
lost to padding. In the olfactory section a derived width of 10 bits cost a 60% gap; here **no width is
derived at all.** **A zero gap and an unmeasured fan-in are the same fact stated twice.**

**No row reads *to derive* and no basis changes within the section — the first time in the map.**
Recomputed from the counts and the 16-bit ceiling: **124.00 MB** and **62M neurons.**

**That is the section's first finding and it is a negative one about the other sections rather than a
positive one about this.** Chunk 02's basis moved from per ear to per hemisphere to per side and then
broke down; chunk 03 could price one population out of twelve. **Here all four rows price, and the
total is exact given the ceiling.** What makes it exact is that **no fan-in in this section is known**
— every edge reads *to derive* — so every neuron sits at the 16-bit cap and nothing is derived below
it. **The total is clean because nothing was measured, not because everything was.**

**The counts themselves are soft and they say so, in a graded way worth carrying.** The middle
temporal area is "fairly well bounded" by a myeloarchitectonic border; the medial superior temporal
area is "softer, with no comparable signature and retinotopy crude to absent, so both its borders and
its count are loose"; the lateral intraparietal area is "firmer-bordered" with two myeloarchitectonic
zones; and the ventral intraparietal area is **the softest count in the map**, lightly myelinated with
no clean border, **and the macaque area has expanded into several human parietal areas.**
**A count whose region has split between species is not the same kind of number as one whose region
has a stain.**

**The counts are the firmest in the map and the payloads are the least settled, and that inversion is
what this section is for.** Of the 52 edge lines the source records: a direction attribute the two ends
dispute, with the inactivation result outranking the connectivity statement; four payloads owed at one
end and typed at the other; **one edge whose consumer attributed its typing to a producer that declares
nothing**, now removed; two frames disagreeing by one step; a route marked contested with **no declared
substrate at either end**; and **exactly one edge whose two ends agree in the same words.** **A section
whose counts all close and whose payloads mostly do not is the inverse of chunk 03, and the two
together say the sizing arithmetic and the payload description fail independently.**

**At this rung the inversion has a precise consequence, and it is worth stating because it is
counter-intuitive.** Sizing is the thing this section does best, and **sizing is the least of what the
code needs.** Every array below has a known element count and an unknown shape: **the extent of every
tangential axis in this section is to derive or unknown**, at all four structures. **A count sizes a
population; it does not size an array**, and none of the four Shape fields closes.

**One note on the stem count, so it is not read as a dropped edge.** The architecture names **five**
far files and `Brain_04_dorsal_visual_parietal_stream.py` reports **four files reached**. The fifth,
`12_thalamus`, is named as the location of a gap rather than as the far end of a line: the
corollary-discharge route runs frontal eye field → mediodorsal thalamus → lateral intraparietal area
and is declared as **one edge from the cortical producer**, so the nucleus is where the route's second
leg is missing and not where a line terminates. **The stem is carried, on that edge, and no endpoint
resolves to it.**

**Memory is not a binding constraint and none of these figures is to be reduced.** The total here is
about a quarter of the auditory section's and about a tenth of the visual section's; **state memory and
edge storage are not in it.**

---

## Completion test

Spec §5's test is mechanical: **an entry is finished when the code can be written from it without
making a single further choice.** **No entry in this file passes**, and the file says so rather than
reading as though it did.

**Every entry is blocked by the standing list** — emission, scheduling, learning rules, connection
topology, tile geometry and sparsity. That is common to the rung and is not this section's finding.

**What is additional here, per entry:**

| entry | additionally blocked by |
|---|---|
| 1 Middle temporal area | **the internal edge crossing the direction map**, demanded by the stated function and recorded nowhere; the tuning and integration arithmetic; D and Z; speed, which has no axis; P; the per-lamina partition; the over-allocating (D, Z) product |
| 2 Medial superior temporal area | **unequal, subadditive weights**, which the equal-weight unit cannot carry; the **contested** vestibular route, whose alternative requires an edge neither entry declares; the congruent/opposite division, which has **no index**; the cue weights; the division split, owed |
| 3 Ventral intraparietal area | **the gain-field multiply, which the unit model excludes by construction**; an eye-position line with **no named producer** and a **head-position line that is required and undeclared**; a **gaze-dependent frame** the vocabulary holds as a string; the shift-against-gain confound, separable only when the complete tuning function is measured; four modalities in four frames on single cells |
| 4 Lateral intraparietal area | **the within-map lateral inhibition**, recorded nowhere; the ranking rule; **an ordering constraint with no field to carry it**; how reward enters; the second leg of the corollary-discharge route, at `12_thalamus` |

**Three of these reach past this file rather than waiting inside it**, and they are named separately
because they are not gaps to be filled by more reading:

- **The unit cannot multiply, and this section's characteristic operation is a multiplication.** Three
  of the four entries rest on it. **This is the largest single blocker in the file and it is not
  local to any entry.**
- **The shared vocabulary carries a latency in seconds and cannot carry an ordering constraint against
  an external event**, which the corollary discharge requires and which three files declare.
- **A uniform update interval would merge two of the middle temporal area's input edges**, which are
  distinguished by latency alone. **The scheduling decision therefore has a correctness consequence in
  this section**, not only a performance one.

**All three are Micky's, all three are asked out loud rather than parked, and nothing below this rung
is built on a guess at any of them.**
