# Brain code design — 05 sensorimotor loop

**Date:** 2026-08-19
**Derived from:** `Brain_architecture_05_sensorimotor_loop`, `Brain_code_design_spec`,
and CLAUDE.md. **No other content source.**
**Implements:** `Brain_05_sensorimotor_loop.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
character for character, so that at coding time only this file is loaded. **One deviation from that
copy, and it is declared here so that anything else is a defect.** Where the architecture says an
agreement between two ends **certifies nothing** because one end was transcribed from the other,
that **is** copied: it is contract rather than commentary, a statement about how much weight a
reader may put on the pair. The architecture's **internal
cross-references** — *the disputed topology recorded above*, *the same driver/modulator gate declared
at the lateral geniculate nucleus*, *the parietal class below* — are not copied, because they point
at fields this rung does not have; their content is carried at the entry it belongs to.

**Six entries, one per architecture entry, same names, same order.**

**Two entries are bundles and both stay bundles.** The **dorsal column nuclei and trigeminal relay**
carries **three nuclei plus a trigeminal relay** in one slot set; the **second somatosensory area**
carries **three fields** — the second somatosensory area proper, the parietal ventral area, and the
ventral somatosensory area. Per spec §1 the design entry is a bundle where the architecture entry is,
and **the split is owed at the source.** Splitting here invents the arity two rungs below where the
arity is known.

---

## What is open for every entry in this file, stated once

Repeating these six times would make the file longer without making it truer. Each entry names only
what is open **beyond** this list.

- **Emission — graded or binary, and the unit's expressiveness.** Micky's, and unresolved.
- **The scheduling discipline.** Micky's, and the largest open item at this rung. No entry contains a
  loop, a step counter, or a `for t in range(...)`. **No global clock may be assumed**, and no latency
  in this section is stated in steps.
- **The learning rules.** Micky's. Every Adaptation field reads *none set* — **and in this section
  that costs more than it has anywhere before**, for two reasons named under the next two headings.
- **Inter-structure connection topology.** Fan-in is **underived on every edge in this section**, at
  every structure. The code needs it as a **map** — which source lines converge on which unit — and a
  convergence count is not a convergence pattern. Surface-before-touching.
- **Tile geometry and sparsity.** Both surface-before-touching, both unset, and every array extent
  below that is not one of the four somatosensory areas is therefore symbolic.
- **Every edge latency in this section reads *to derive*, and no time constant and no ordering
  constraint is stated anywhere** — the first section since chunk 01 of which that is true.
  **What this section constrains instead is the graph**, which is where its findings land.
- **Edge storage cannot be closed anywhere in this file.**
  `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`. Latency is *to
  derive* on every edge, the update interval waits on the scheduling discipline, and bytes per value
  waits on the emission question. Each entry records its **edge count** and its **line count status**.
  **Never summed with parameter memory or state.**

### The loop does not close inside the map, and that is this section's largest fact

Primary motor cortex drives **muscles**; the muscles, the skeleton and their dynamics **have no entry
anywhere**; and the return path runs **through the world** — the movement's consequence read back
through proprioception. **The loop closes through the body, not inside the brain.**

**Co-instantiation therefore takes its strongest form here and it points outside the map.** In the
auditory section a staged bring-up left a gain loop open; in the other-senses section neither
vestibular transducer's payload was defined without its sibling. **Here the pathway does not close at
all without a body.** A sensorimotor loop instantiated without one is not a degraded loop — **the
return edge has no producer.** The architecture calls this **the map's largest open boundary on the
output side, the mirror image of the retina's input edge.**

**At this rung it has three exact consequences, and none of them is repairable here.**

1. **The corticospinal output edge has a payload and no consumer.** It can be typed, allocated and
   emitted, and nothing in the code can receive it. An `Endpoint` for it names a structure with **no
   entry in any file**, which is a different state from a far end whose file has not been opened.
2. **The return line has no producer.** Every other input line in this file names a structure that
   exists somewhere. This one names *the world*, and what it delivers is the **consequence** of a
   command whose effect nothing in the code computes.
3. **So the sensorimotor loop cannot be closed by any amount of work at this rung**, and a design that
   quietly closed it — by feeding the motor command back as its own consequence, which is the obvious
   thing a coder reaches for — **would have built a system with no body and no world, and it would run.**
   That is the failure mode this heading exists to name. *(The out-of-map boundary is the
   architecture's; that a self-fed loop would run and pass every other check here is Claude's reading.)*

**And this is the first sensory section in the map with no transducer entry.** The mechanoreceptors
and proprioceptors are the transducers of this pathway and **they arrive from a body that has no
entry.** Chunks 01, 02 and 03 each began with a transducer that the file itself described. **Here the
transducer is outside the map at the input end and the effector is outside it at the output end**, so
§5a's transducer class is inapplicable throughout — a positive statement about the section rather
than an omission.

### The topology is contested, so the graph has more edges than the anatomy may

Chunk 04 found contested payloads, one contested route and one contested frame. **This section finds a
dispute about whether the four primary somatosensory areas form a chain or four partly independent
lines.** All four receive direct thalamic input, which is not disputed; what is disputed is whether
the later areas can work without the earlier.

- **Ablation** in macaque and marmoset abolishes cutaneous responsiveness in area 1 and the second
  somatosensory cortex when area 3b is removed, which reads **serial**.
- **Reversible lidocaine inactivation** in cat, rabbit and marmoset leaves second-somatosensory
  responses substantially intact, which reads **parallel**, and parallel thalamic activation is
  reported in prosimian primates and tree shrews.
- **Irreversible ablation and reversible inactivation are not measuring the same thing**, and **the
  entry keeps both the intracortical and the direct thalamic edges rather than choosing.**

**The design-rung consequence is exact and it is unusual: the edge set below is knowingly larger than
the biology may be.** Every other kind of open item in this project makes the code *smaller* than the
biology — an unwritten payload, an underived extent. This one makes it **larger**: two edge sets are
declared where the anatomy may support one. **Nothing is deleted**, because deleting either would be
adjudicating a contest at the rung furthest from the evidence. Per §5b this reads **contested** and
not *to derive*: it is measured, and yielding readings that disagree, so it needs adjudication between
existing results rather than a new measurement.

### The standard laminar block is a claim and not a default, and its scope is stated here

The architecture assigns this: **stating the block's scope is owed at the design file.** It is stated
below, and it is stated as a **scope**, not as arithmetic — the block's edges are not transcribed into
any update equation in this file.

**The block.** Laminae **1, 2, 3, 4, 5a, 5b, 6a, 6b**, with **4 → 2/3**, **2/3 → 5a and 5b**,
**6a → 4**, **6a → 5a**, **6b → 6a**, and within-sub-element recurrence. **It is Class 3 throughout —
the general cortical pattern, not a measurement made at any entry that carries it** — and this file
marks it so wherever it appears.

**Its scope: granular isocortex, and nothing else.** Three of its six edges route through **layer 4**,
so an entry whose own Function denies layer 4 cannot take the block without asserting a circuit that
entry denies.

**Nine entries across five files cannot take it, and they fail in four different ways:**

| failure mode | entries |
|---|---|
| uniformly agranular | **primary motor cortex** (this file), and frontal-lobe entries |
| agranular across a gradient | frontal-lobe entries |
| agranular across an internal border | frontal-lobe entries |
| not isocortex at all | the **hippocampal formation**, the **cerebellar cortex** |
| (also named) | the **temporal pole** |

**So a single exception clause would not cover them**, which is why the scope is a table and not a
sentence. **In this file the block applies to primary somatosensory cortex, the second somatosensory
area and superior parietal area 5, and is withheld at primary motor cortex**, whose laminae are
**seven, not eight**. The dorsal column nuclei and the ventral posterior thalamus are **not cortex**
and the question does not arise there.

**What the scope statement does not do is license the block's arithmetic.** Naming which entries may
carry a Class-3 laminar claim is not the same as deriving an update equation from it, and **no entry
below writes one.** The block tells a reader which internal edges exist; it does not say what they
compute, and nothing above supplies that.

### Two arithmetic cautions the architecture carries down explicitly, and this rung is where they bite

1. **The 87% convergence figure is not a fan-in measurement.** In anaesthetised macaque, **87% of 317
   recorded cuneate and external-cuneate cells responded to stimulation of two or more peripheral
   nerves** — **276 cells**. It counts **cells responding to two or more nerve territories**, not
   **contacts per neuron**, and the architecture says the two are different measurements.
2. **The ~10% nociceptive figure at the thalamus is carried forward unverified**, flagged at the
   architecture as a candidate for removal or sourcing.

**Neither may be promoted into a width or a fraction at a lower rung**, and neither is. `fan_in` for
the dorsal column nuclei reads **None**, not 2 and not 276; there is no `nociceptive_fraction`
parameter anywhere below. **The temptation is specific and worth naming: 87% and 10% are the only two
percentages in the section, and both would slot into a parameter table without looking wrong.**

### Proprioception is delivered twice, and the two copies write different kinds of memory

Proprioception leaves the first relay on **two edges carrying one payload to destinations of different
kinds**: the **cerebellum**, by the cuneocerebellar tract from the external cuneate nucleus, and the
**thalamus** onward to cortical area 3a. **This is unlike the other senses, whose branches carry
different content** — the retina sends orienting transients to the colliculus and a luminance scalar
to the pretectum, not two copies of the image.

**The two copies differ in what kind of memory they write, not in whether they are used:** the
cortical copy becomes **reportable**, and the cerebellar copy writes **procedural** change, motor
learning being cerebellum-dependent. **A learning channel that operates without perceptual access is
an architectural fact, not an absence of one** — and a build that folded the cerebellar branch into
the motor loop and dropped the sense would still pass a consistency check on that entry unless the
duplication is stated.

**At this rung: the two edges carry the same `Representation` and must not be deduplicated.** They are
identical in units, range, timing and frame, and a pass that noticed that and merged them would delete
the architectural fact. **And the Adaptation field's cost is highest here**: the destination of the
procedural copy is a structure this section does not describe, so the one edge in this file whose
purpose is learning terminates in a file whose learning rule is also unset.

### Element classes, and the counting basis

Every population in this file is a **threshold gate** or an **inhibitory interneuron modelled as one**.
**No transducer** — the transducers are outside the map. **No transmission-only structure**, **no
graded non-spiking element**, and **no sign-inverting stage.** §5a's four exceptions are all
inapplicable, for the second time in the map.

**Counting basis: per hemisphere throughout, and one structure is unpriced.** Five of six rows carry a
count; the second somatosensory area carries none.

**Cross-file endpoints carry the far file's stem.** Four far files are reached from this section:
`06_posterior_parietal`, `11_frontal_lobe`, `17_insula_claustrum_habenula`,
`04_dorsal_visual_parietal_stream`. Every other named far end arrives **without a stem**, which means
its file has not been opened beside this one — not that no far end exists.

---

# 1. Dorsal column nuclei and trigeminal relay

**A bundle, and it stays one.** Three nuclei plus a trigeminal relay in one slot set. The split is
owed at the source.

## Contract

**Inputs.**
- **← mechanoreceptor and proprioceptor afferents** — **two distinct payloads on one relay**:
  **cutaneous** (touch, pressure, vibration — intensity per skin location, somatotopic) and
  **proprioceptive** (muscle spindle length and rate, Golgi tendon force, joint angle — **the
  body's configuration, not the world's**). **Fan-in: no contacts-per-neuron figure found.** A
  **convergence** figure exists **and is not the same measurement**: in anaesthetised macaque,
  **87% of 317 recorded cuneate and external-cuneate cells responded to stimulation of two or more
  peripheral nerves** — 276 cells, recomputed — so a single relay cell reads from more than one
  nerve territory.
- **← primary sensorimotor cortex**, corticocuneate, from the hand regions of areas 3b, 3a and 1/2
  and the forelimb region of primary motor cortex, **bilateral** — **no new stimulus content; a
  movement-contingent gain signal.** Somatosensory transmission through the cuneate is
  **attenuated** during voluntary hand movement, by an amount **comparable to that seen in cerebral
  cortex and larger than in the spinal cord.** **And it is not a scalar gain:** the cortical fibres
  produce **a central zone of facilitation surrounded by a peripheral zone of inhibition**, which
  is **a spatial sharpening operation.**

**Outputs.**
- **→ ventral posterior thalamus**, by the medial lemniscus and trigeminothalamic tract — both
  payloads, somatotopic, **with the cutaneous and deep submodalities kept separate.**
- **→ cerebellum**, by the cuneocerebellar tract **from the external cuneate nucleus** —
  **proprioception only, body configuration, unconscious.**
- **→ dorsal cochlear nucleus** — the head, face and neck configuration copy **used to cancel
  self-generated sound**. **Contested at the receiving end**: the granule-cell domain carrying this
  copy is decreased or absent in primates, **so what receives this edge in a human is owed.**

**Sizing.** Basis: **per hemisphere.** **~0.5M neurons**, soft, no clean human count, and **no
separate count for the external cuneate nucleus** — the sub-element the cerebellar edge leaves
from. Fan-in **to derive**. At the 16-bit ceiling: **1.00 MB.**

**Shape.** Rank 3: **(nucleus, territory, somatotopic position)** — three nuclei, two territories,
and a somatotopic axis that is **punctate in the cluster region and overlapping in the reticular
one**, so the axis means different things in the two territories.

**Edge latency.** All edges **to derive.**

## Representation — declared once per line, inherited by every consumer

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← mechanoreceptor afferents (cutaneous) | intensity per skin location | to derive | **event-driven** — the producer is outside the map and has no stated rate | **somatotopic — the skin surface** |
| ← proprioceptor afferents | muscle spindle length and rate, Golgi tendon force, joint angle | to derive | event-driven | **the body's configuration, not the world's** |
| ← primary sensorimotor cortex (corticocuneate) | **no new stimulus content; a movement-contingent gain** | to derive; **attenuating, comparable to cerebral cortex and larger than spinal cord** | event-driven | **somatotopic, and organised centre–surround: facilitation centrally, inhibition peripherally** |
| → ventral posterior thalamus | both payloads, **submodalities kept separate** | to derive | event-driven | somatotopic |
| → cerebellum (cuneocerebellar, from the external cuneate nucleus) | **proprioception only, body configuration, unconscious** | to derive | event-driven | body configuration |
| → dorsal cochlear nucleus | the head, face and neck configuration copy, **to cancel self-generated sound** | to derive | event-driven | head/face/neck configuration |

**Row 3 is a gain and not content, and it is the strongest instance of that distinction in the file**,
because it is spatially structured. A modulatory line that carried one scalar could be applied by
multiplication at the structure; **this one has a centre and a surround**, so applying it needs the
somatotopic index of the line it modulates. **A design that reduced it to a scalar would delete the
sharpening**, which is the operation the edge exists to perform.

**Rows 4 and 5 carry proprioception twice and are identical in every column.** They must not be
deduplicated: the two copies write different kinds of memory, and merging them deletes an
architectural fact rather than a redundancy.

## Algorithm

- **Transform.** **Not a passive relay.** The current literature describes it as a **sensorimotor
  integration and distribution hub**: descending input from sensorimotor cortex, intrinsic inhibitory
  interneurons and recurrent collaterals, and **the signal that leaves is not the signal that
  arrived.** **No standard operation name is given for what it computes**, and per §5 that is a finding
  about the structure rather than a gap to fill. What *is* named is one operation on one line —
  **centre–surround spatial sharpening**, driven by the descending edge — and **the centre–surround
  question is §10's and is Micky's**, so it is named and no arithmetic is written for it.
- **The internal division is the entry's central structural fact, and it makes the somatotopic axis
  mean two different things.** Each of the gracile and cuneate nuclei splits into two territories with
  different input regimes:
  - a **cluster region** — the middle third, **pars rotunda** in the primate cuneate — of tightly
    packed cells in **cytochrome-oxidase-dense patches separated by cell-poor, oxidase-light septa**,
    receiving afferents from **glabrous skin of the digits and pads**, punctate and high-acuity, **one
    body part per cluster**;
  - a **reticular region** rostral and caudal to it, of small and large **multipolar** cells receiving
    diffuse terminations with **intersegmental overlap** rather than somatotopic lamination.

  **The design consequence is that the position axis is not one axis.** In the cluster region an index
  addresses one body part; in the reticular region an index addresses a region of overlap whose extent
  is not stated. **An array indexed uniformly along that axis asserts a uniform meaning the structure
  does not have**, and no rung above supplies the mapping for either territory. Recorded.
  *(The two territories are the architecture's; that a uniform index over-claims is Claude's reading.)*
- **Four internal edges converge on the same projection cells with different payloads**, and this is
  where the entry's computation lives:
  1. the **cluster region** delivering the punctate high-acuity cutaneous payload;
  2. the **reticular region** delivering the convergent multi-territory payload the 87% figure
     measures;
  3. **intrinsic inhibitory interneurons** delivering inhibition with **no content** — **the substrate
     of the centre–surround sharpening the corticocuneate edge drives**;
  4. **recurrent projection-cell collaterals** between cells with overlapping receptive fields,
     carrying **synchronisation, no new content.**

  **Two of the four carry no content and they must not be summed with the two that do.** Edges 3 and 4
  are typed as inhibition-without-content and synchronisation-without-content; an update that summed
  all four alike would read a gain and a timing signal as evidence.
  **Species note carried, and it constrains what may be built on this list:** the cluster/reticular
  division is **primate and rodent**; the internal edges are typed from **cat physiology.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `relay_active` | (N, T, P) | open — emission question | to derive | to derive |
  | `relay_threshold` | (N, T, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `interneuron_state` | (N, T, P) | open | to derive | inhibition, no content |
  | `cortical_gain` | (N, T, P) | open | to derive | **centre–surround, not a scalar** |

  **N = 3 nuclei** — gracile, cuneate, external cuneate — **and the count does not divide among them.**
  ~0.5M is one figure for the complex, and **there is no separate count for the external cuneate
  nucleus**, which is **the sub-element the cerebellar edge leaves from**. **So the one edge in this
  entry whose source is a named sub-element cannot be sized.** That is not a general shortfall: it is
  one specific edge whose line count is unobtainable while every other term is available.
  **T = 2 territories**, cluster and reticular, and the count does not divide among them either.
  **P is the somatotopic axis and it has no extent and two meanings** — see above.
  **The trigeminal relay is in the entry's name and has no axis.** The bundle names four things and the
  shape names three; **where the trigeminal relay sits in `(N, T, P)` is not stated**, and it is not
  guessed here. Recorded, and it is one more reason the split is owed at the source.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~500,000**, soft, **no clean human count** | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling, fan-in being underived | architecture Sizing |
  | `parameter_memory` | bytes | **1.00 MB** at 0.5M × 16 bits | recomputed from the two above |
  | `nucleus_count` N | nuclei | **3** — gracile, cuneate, external cuneate | architecture Function |
  | `territory_count` T | territories | **2** — cluster, reticular | architecture Function |
  | `external_cuneate_count` | neurons | **no separate count** | architecture Sizing |
  | `fan_in` | contacts per neuron | **no contacts-per-neuron figure found** | architecture Inputs |

  **There is no `convergence` parameter and there must not be.** The 87% / 276-cell figure counts cells
  responding to two or more nerve territories and is **not a contacts-per-neuron measurement**; writing
  it as a fan-in, a fan-in floor, or a fraction would promote a different measurement into this slot.
  **`fan_in` reads None.**
- **Update equation.** **Waiting on the emission question and on the centre–surround question**, and on
  a third thing: **what the structure computes is not named at any rung above.** *A sensorimotor
  integration and distribution hub* describes a role, not an operation over arrays, and **a picture of
  an operation is not an operation.** What is fixed regardless of all three: **the two payloads leave
  separate** — the output line declares the cutaneous and deep submodalities kept separate — so **no
  equation here may merge them**, and the separation is carried through the structure rather than
  re-established at the far end.
- **State carried between updates.** `relay_active`, `interneuron_state`, and whatever the recurrent
  collateral synchronisation holds. **No time constant is stated for any of them**, in this section or
  anywhere in it. Initial values: to derive. **State memory is not parameter memory and the two are
  never summed.**
- **Edge storage.** 2 input edges, 3 output edges. Line counts: all to derive — **and one of them is
  unobtainable rather than merely underived**, the cerebellar line, whose source sub-element has no
  count. Latency to derive. Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Invariant note carried from the architecture.** Co-instantiation: **the descending gain edge closes
  a loop from cortex on to the first relay**, and it is the one every comparable first relay in the map
  already declares. Per-edge latency: satisfied.
- **Open, beyond the standing list.**
  - **What the structure computes**, unnamed at every rung above.
  - **The centre–surround arithmetic** of the descending gain edge. Micky's.
  - **P has no extent and two meanings**, punctate in one territory and overlapping in the other, with
    no mapping supplied for either.
  - **No count for the external cuneate nucleus**, so the cerebellar edge's line count is unobtainable.
  - **Where the trigeminal relay sits in the shape.** Not stated; the bundle's split is owed.
  - **A possible third payload, and it would make the entry's two-payload claim incomplete for human.**
    The human cuneate contains discrete subregions, present from prenatal life to old age, whose
    neurochemistry closely resembles **the superficial layers of the caudal spinal trigeminal nucleus,
    a nociceptive relay.** The authors state the arrangement **has never been formalised in the human
    brain and has not been described in another species.** **If it relays nociception, the entry's
    two-payload claim is incomplete for human, and the payload of any such third line is owed.**
    Per §5b this is **contested for human** and recorded rather than smoothed.
  - **What receives the dorsal cochlear nucleus edge in a human**, the granule-cell domain carrying it
    being decreased or absent in primates. **Owed.**

---

# 2. Ventral posterior thalamus

## Contract

**Inputs.** **← dorsal column nuclei and trigeminal relay** — the driver, and **as at the lateral
and medial geniculate nuclei a minority of the synapses**; it **terminates in the parvalbumin
core**, and its terminals form **triadic synapses with GABAergic presynaptic dendrites — an
arrangement the spinothalamic input does not have.** **← spinal cord grey matter** (spinothalamic,
from laminae I and IV–VIII) and the **spinal trigeminal nucleus** — pain, temperature and crude
touch, **terminating diffusely and preferentially in the calbindin matrix**; about **10% of ventral
posterior lateral neurons are nociceptive**, of wide-dynamic-range type, **and that figure is
carried forward unverified and is a candidate for removal or sourcing.** **Contested:** whether the
lamina-I pain and temperature stream relays here at all is disputed — one account concentrates
lamina-I terminations in a separate posterior ventral medial nucleus, the other routes
spinothalamic input into this complex's matrix. **The two accounts are not reconciled.**
**← primary somatosensory cortex** and **← thalamic reticular nucleus** — no stimulus content; **the
same driver/modulator gate.**

**Outputs.** **→ primary somatosensory cortex, onto layers 3B and 4, from the parvalbumin core** —
the somatotopic payload, **gated, not transformed**, and **sorted onto its cortical targets by
submodality: proprioception → area 3a, cutaneous → area 3b. This is the edge that carries the
map.** **→ primary somatosensory cortex and adjacent cortex, onto layer 1, from the calbindin
matrix** — **not topographic and not confined to one cortical area**, and the matrix cells can also
be labelled from motor cortex; **its payload is owed** — what a non-topographic thalamic broadcast
to layer 1 delivers, as a type with a range and a frame, is not established. **→ second
somatosensory and parietal ventral areas**, from the ventral posterior inferior nucleus and the
ventral posterior superior territory — **deep-receptor signals from muscles and joints, little if
any cutaneous content.**

**Sizing.** Basis: **per hemisphere.** **~2.5M neurons**, soft — **the largest primary sensory
relay, above the lateral and medial geniculate nuclei at ~1.8–2.3M**, about **1.2× the geniculate
midpoint**, recomputed, **its body-surface and proprioceptive afferent load exceeding the retina's
or cochlea's.** **No separate core-versus-matrix count was found.** At the 16-bit ceiling:
**5.00 MB.**

**Shape.** Rank 3: **(subnucleus, compartment, somatotopic position)** — **and the compartment axis
does not fit inside this structure.** The matrix **runs uninterrupted** from the ventral posterior
medial and lateral nuclei into the ventral posterior inferior and basal ventral medial nuclei, and
on into **the anterior pulvinar, posterior and ventral lateral nuclei.** **A compartment that
crosses region boundaries cannot be expressed by per-region edges, and that is a finding about the
description's representation and not only about the thalamus.**

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← dorsal column nuclei and trigeminal relay | both payloads, submodalities separate | to derive; **a minority of the synapses** | **event-driven** | somatotopic |
| ← spinal cord grey matter (spinothalamic) and spinal trigeminal nucleus | pain, temperature and crude touch | to derive | event-driven | **diffuse — terminating preferentially in the matrix, not point-to-point** |
| ← primary somatosensory cortex; ← thalamic reticular nucleus | **no stimulus content — the gate** | to derive | event-driven | **none — a gate over the relay, not a content map** |
| → primary somatosensory cortex, layers 3B and 4, from the **parvalbumin core** | the somatotopic payload, **gated, not transformed** | to derive | event-driven | **somatotopic, point-to-point, and sorted by submodality: proprioception → 3a, cutaneous → 3b** |
| → primary somatosensory cortex and adjacent cortex, layer 1, from the **calbindin matrix** | **owed** | owed | event-driven | **not topographic and not confined to one cortical area** |
| → second somatosensory and parietal ventral areas | **deep-receptor signals from muscles and joints, little if any cutaneous content** | to derive | event-driven | to derive |

**Rows 4 and 5 are one structure's output to one cortical area and they are two different transfers.**
The core line is topographic, point-to-point, submodality-sorted and lands on layers 3B and 4; the
matrix line is non-topographic, spreads beyond the target area, and lands on layer 1 with its **payload
owed**. **A single edge from this complex to the cortex describes two different transfers**, and the
architecture says so. **A consumer that inherited one representation for "thalamic input" would be
right about one line and wrong about the other.**

**Row 5 is the untyped one and its consumer's entry marks it owed too**, so the line is **owed at both
ends** — no reading anywhere establishes what a non-topographic thalamic broadcast to layer 1
delivers as a type with a range and a frame.

## Algorithm

- **Transform.** **Gated, not transformed.** The architecture states this on the core output line and it
  is the strongest statement of a transform in this entry: **the payload that leaves is the payload that
  arrived, with a gate applied.** So the operation is **modulation of throughput**, and its arithmetic is
  the emission question wearing a thalamic name. **No re-expression, no change of frame, no reduction.**
- **The two compartments are the entry's central structural fact and they take different afferents and
  project to different layers.** A **core** of large and medium **parvalbumin-positive** relay cells
  staining densely for cytochrome oxidase, and a **matrix** of smaller **calbindin-positive** cells
  staining weakly. **They take different afferents and project to different cortical layers, so a single
  edge from this complex to the cortex describes two different transfers.**
- **The compartment axis does not fit inside the structure, and this is a finding about the
  representation and not about the thalamus.** The matrix **runs uninterrupted** out of this complex
  into **the anterior pulvinar and the posterior and ventral lateral nuclei.** **Per-region edges cannot
  express a population that crosses region boundaries.**
  **At this rung that has a precise cost:** `matrix` is an axis of *this* structure's array and the
  population it names is not confined to this structure. **Allocating it here asserts a boundary the
  biology does not have**, and allocating it in each region separately asserts several populations where
  there is one. **Neither is written**, and the architecture's own finding is carried rather than
  resolved. *(The uninterrupted matrix is the architecture's; that both allocations over-claim is
  Claude's reading of the array vocabulary.)*
- **Three internal edges, and the difference between the first two is synaptic rather than
  topological.**
  1. **medial lemniscal terminals → core relay cells**, by **triadic synapses with GABAergic
     presynaptic dendrites**, so **the transfer is locally inhibition-shaped rather than a simple
     relay**;
  2. **spinothalamic terminals → matrix relay cells**, **no triads**;
  3. **local GABAergic interneurons → relay cells**, inhibition with no content.

  **Two edges that differ only in their synaptic arrangement have no distinct representation in an
  array model**, where an edge is a source, a target and a payload. **The triad is the difference and
  the vocabulary has no field for it.** Recorded. *(The triadic arrangement is the architecture's; that
  the shared edge type cannot express it is Claude's reading — and it is the second instance in the map,
  after the reciprocal dendrodendritic apposition in the olfactory bulb.)*
  **Species note, and it is load-bearing:** interneuron density differs sharply — **the rat complex has
  very few, primates have many — so a rodent-derived internal circuit does not transfer here.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `relay_active` | (S, C, P) | open — emission question | to derive | to derive |
  | `relay_threshold` | (S, C, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `interneuron_state` | (S, C, P) | open | to derive | inhibition, no content |
  | `gate` | (S, C, P) | open | to derive | **no stimulus content** |

  **S = 4 subnuclei** — ventral posterior lateral (body), ventral posterior medial (face), ventral
  posterior inferior, basal ventral medial — **and the count does not divide among them.**
  **C = 2 compartments**, core and matrix, **no core-versus-matrix count was found**, and **the axis
  does not fit inside the structure** — see above.
  **P has no extent.**
  **And the subnucleus axis is itself contested in its naming.** The four-subnucleus scheme used here
  and a parallel literature's **ventroposterior / ventroposterior superior / ventroposterior inferior**
  scheme **are not a relabelling of each other: they cut the proprioceptive relay out as a separate
  nucleus.** **The edges carry the function either way**, so no edge below depends on the choice — but
  **S = 4 is one scheme's count and the other scheme does not have four.**
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~2,500,000**, soft | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling | architecture Sizing |
  | `parameter_memory` | bytes | **5.00 MB** at 2.5M × 16 bits | recomputed |
  | `subnucleus_count` S | subnuclei | **4**, on the scheme used | architecture Function |
  | `compartment_count` C | compartments | **2**, core and matrix, **no count for either** | architecture Function |
  | `geniculate_comparison` | ratio | **~1.2×** the geniculate midpoint of ~2.05M | recomputed from ~2.5M against ~1.8–2.3M |

  **There is no `nociceptive_fraction` parameter and there must not be.** The ~10% figure is **carried
  forward unverified** and flagged at the architecture as a candidate for removal or sourcing; writing
  it into a parameter table would give an unverified figure the same standing as a measured one.
- **Update equation.** **Waiting on the emission question.** What is fixed regardless: **the payload is
  gated and not transformed**, so the output equals the input under a gate, and **the submodality sort
  is a routing of the output onto two different cortical targets rather than a computation** —
  proprioception to area 3a, cutaneous to area 3b. **An equation that mixed the submodalities before the
  sort would have made the sort impossible**, and the sort is what makes the map arrive.
- **State carried between updates.** `relay_active`, `interneuron_state`, `gate`. No time constant is
  stated. Initial values: to derive.
- **Edge storage.** 4 input edges, 3 output edges. Line counts: all to derive. Latency to derive.
  Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Invariant note carried from the architecture.** Co-instantiation: **the corticothalamic gate closes
  here.** Per-edge latency: satisfied.
- **Open, beyond the standing list.**
  - **The matrix line's payload**, **owed at both ends** — what a non-topographic thalamic broadcast to
    layer 1 delivers, as a type with a range and a frame, is not established anywhere.
  - **The compartment axis does not fit inside the structure**, and neither available allocation is
    honest.
  - **No core-versus-matrix count**, so neither compartment can be sized.
  - **Whether the lamina-I pain and temperature stream relays here at all.** **Contested**, and the two
    accounts are not reconciled. Per §5b this is contested rather than underived.
  - **The subnucleus scheme is contested** and the two schemes do not have the same arity.
  - **The triadic synapse has no representation** in the shared edge type.
  - **The ~10% nociceptive figure is unverified** and is a candidate for removal or sourcing at the
    source rung.

---

# 3. Primary somatosensory cortex

**This is the one entry in the map that can be allocated sub-element by sub-element**, and the rest of
this file is written against that contrast.

## Contract

**Inputs.** **← ventral posterior thalamus, onto layers 3B and 4, from the parvalbumin core** —
cutaneous intensity to areas 3b and 1, proprioceptive configuration to areas 3a and 2, topographic
and point-to-point. **← the same complex, onto layer 1, from the calbindin matrix** —
non-topographic, **payload owed at both ends**, terminating on **apical tuft dendrites belonging to
cells whose somata sit in layers 2/3 and 5**, with **no second internal edge written for the
propagation to those somata.**

**Outputs.** **→ second somatosensory area and the parietal junction** along the intracortical
chain **3b → 1 → 2** — a rising code: point pressure and adaptation rate, then texture and motion
*across* the skin, then size, shape and stereognosis with cutaneous and deep input **combined,
which is the first place the payload describes an object rather than the skin.** **The modality
split is preserved along the way**, cutaneous by areas 3b and 1 and deep by 3a and 2, **as parallel
channels rather than one merged stream.** **→ primary motor and premotor cortex, from area 3a**
(the premotor consumer in `11_frontal_lobe`) — limb and joint configuration, **the feedback signal that closes the sensorimotor loop**, and **a
payload type rather than a label**: single-unit recording distinguishes **single-digit
position-scaled, multi-digit position-scaled, and posture-selective** cells, so what leaves is **a
graded position variable per digit plus a categorical posture signal, not an undifferentiated
proprioception.** **→ superior parietal area 5**, principally from area 2 with area 3a — limb
configuration and tactile object properties **in a skin / joint frame, the frame that is
re-expressed downstream.** **This payload also leaves the section**: the medial intraparietal entry
in `06_posterior_parietal` declares a primary somatosensory source of its own, on the four-source
line noted under the parietal class below. **→ the insula** from area 3a and **→ posterior parietal cortex** from
areas 1 and 2 — **owed.** **The parietal class has one named consumer** in `06_posterior_parietal`: the medial intraparietal area declares
`← the primary somatosensory cortex` on a four-source line. **No other entry in that file declares a
primary somatosensory source** — the angular gyrus declares only a *somatosensory association
cortex* class, which is itself unresolved. **So the class narrows to one named member and one class
facing a class**; naming the medial intraparietal area here is owed. **The insular endpoint was not
tested** — that far end is in `17_insula_claustrum_habenula`. **→ ventral posterior thalamus** — the gate, no content. **→ dorsal
column nuclei**, corticocuneate, bilateral — the movement-contingent gain signal with its
**centre–surround** organisation.

**Sizing.** Basis: **per hemisphere. Four counts, not one: area 3a ~15M, area 3b ~25M, area 1
~20M, area 2 ~20M**, summing to **80M**, recomputed. At the 16-bit ceiling: **30.00, 50.00, 40.00
and 40.00 MB, total 160.00 MB.** **This is the first structure in the map that can be allocated
sub-element by sub-element.**

**Shape.** Rank 3: **(area, lamina, somatotopic position)**, with a fourth level inside areas 3b
and 1 — **digit modules** — and **the somatotopic axis is plastic**, reorganising after input
change. **An extent that moves with experience is not the same kind of extent as one that does
not.**

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← ventral posterior thalamus, layers 3B and 4, from the **parvalbumin core** | cutaneous intensity to 3b and 1; proprioceptive configuration to 3a and 2 | to derive | **event-driven** | **topographic and point-to-point — somatotopic** |
| ← ventral posterior thalamus, layer 1, from the **calbindin matrix** | **owed at both ends** | owed | event-driven | **non-topographic** |
| → 3b → 1 (intracortical) | point pressure and adaptation rate, elaborating toward **texture and motion across the skin** | to derive | event-driven | somatotopic — the skin |
| → 1 → 2 (intracortical) | toward **size and shape** | to derive | event-driven | somatotopic |
| → 3a → 2 (intracortical) | the **deep** payload converging with the cutaneous stream | to derive | event-driven | **skin / joint** |
| → second somatosensory area and the parietal junction | **size, shape and stereognosis, cutaneous and deep combined — the first place the payload describes an object rather than the skin** | to derive | event-driven | **object, not skin** |
| → primary motor and premotor cortex, from area 3a | **a graded position variable per digit plus a categorical posture signal** | to derive | event-driven | **limb and joint configuration** |
| → superior parietal area 5, principally from area 2 with 3a | limb configuration and tactile object properties | to derive | event-driven | **skin / joint — the frame that is re-expressed downstream** |
| → the insula (from 3a); → posterior parietal cortex (from 1 and 2) | **owed** | owed | event-driven | owed |
| → ventral posterior thalamus | **the gate, no content** | to derive | event-driven | **none** |
| → dorsal column nuclei (corticocuneate, bilateral) | **the movement-contingent gain signal** | to derive | event-driven | **somatotopic, centre–surround** |

**Row 6 is where the payload changes kind, and it is the only such change in this file.** Everything
upstream describes the **skin**; from here on the payload describes an **object**. **The frame column
carries that**, and a consumer inheriting *somatotopic* from the structure rather than from the line
would be reading an object code as a skin map.

**Row 7 is a payload type rather than a label, and this rung has to build two arrays for it.**
*Proprioception* would be one array; what the architecture states is **single-digit position-scaled,
multi-digit position-scaled, and posture-selective** cells — so **a graded position variable per digit
plus a categorical posture signal**, which is a continuous vector and a discrete class travelling
together. **Not an undifferentiated proprioception.** A single array cannot carry both.

**Rows 3, 4 and 5 exist only under one reading of a contested topology** — see the Algorithm field.

## Algorithm

- **Transform.** **A rising code along an intracortical chain, and each step has a stated payload
  change rather than a named operation.** **Area 3a** — proprioceptive core, at the border with primary
  motor cortex, receiving group Ia muscle-spindle afferents. **Area 3b** — cutaneous core, **the true
  primary, with the finest somatotopic map.** **Area 1** — cutaneous secondary, texture and motion
  across the skin. **Area 2** — cutaneous-and-deep tertiary, size, shape and stereognosis, **where
  cutaneous and deep inputs converge.**
  **Three payload changes are named and none of their arithmetic is:** point pressure → texture and
  motion across the skin; texture and motion → size and shape; and **deep converging with cutaneous to
  make stereognosis possible.** Each is a description of what the output is about, not an operation
  over arrays, and **no update equation is written for any of them.**
- **The modality split is preserved along the chain and that is a constraint on any eventual
  equation.** Cutaneous by areas 3b and 1, deep by 3a and 2, **as parallel channels rather than one
  merged stream** — so the chain is **not** a single pipeline, and an equation that merged the two
  streams at any step before area 2 would have destroyed the convergence that makes stereognosis the
  entry's stated function.
- **Four internal edges implement the rising code, and whether they are a chain or four parallel lines
  is contested.** **3b → 1** (elaborating toward texture and motion), **1 → 2** (toward size and
  shape), **3a → 2** carrying the deep payload that converges with the cutaneous stream — **the
  transfer that makes stereognosis possible** — and **3b → 2** direct. **The entry keeps both
  readings**, so **the four intracortical edges and the four direct thalamic edges are both declared.**
  **The design consequence, stated once here and referred to from the second somatosensory entry:** the
  code declares a superset. Under the serial reading the thalamic edges to areas 1 and 2 are not
  load-bearing; under the parallel reading the intracortical chain is not. **Both are written and
  neither is marked preferred**, and a build that pruned either would be adjudicating a contest
  between two methods that are not measuring the same thing.
- **Thalamic input is a minority of long-range input — ~32% of layer-1 long-range input — and most
  input is intracortical.** **At this rung that is a statement about where the fan-in comes from and
  not about the payload**, and it constrains the connection topology rather than the equation: a
  topology built by wiring the declared inter-structure edges alone would supply a minority of the
  convergence this structure has. **The intracortical majority is not enumerated at any rung**, so it
  cannot be built; it is recorded so that a fan-in map built later is not mistaken for complete.
- **The layer-1 matrix line has no second internal edge and that is a stated gap, not an omission.**
  It terminates on **apical tuft dendrites belonging to cells whose somata sit in layers 2/3 and 5**,
  with **no second internal edge written for the propagation to those somata.** So the line arrives at
  a place, and **nothing carries it from that place to the cells it belongs to.** **This is the same
  same-dendrite geometry the map has recorded before**, and the same unresolved question — a
  single-compartment unit cannot express an input that arrives at a tuft and must reach a soma two
  layers away. **Whether a unit has compartments is §10's and is Micky's.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `s1_active_3a` | (L, P₃ₐ) | open — emission question | to derive | to derive |
  | `s1_active_3b` | (L, P₃ᵦ, M) | open | to derive | to derive |
  | `s1_active_1` | (L, P₁, M) | open | to derive | to derive |
  | `s1_active_2` | (L, P₂) | open | to derive | to derive |
  | `s1_threshold_*` | as each above | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `digit_position` | per digit, in the area-3a output | open | to derive | **graded position variable** |
  | `posture_class` | in the area-3a output | open — **categorical** | to derive | **a discrete class, not a scalar** |

  **Four separate arrays and not one, because the counts are four and not one.** **Area 3a ~15M, area
  3b ~25M, area 1 ~20M, area 2 ~20M**, summing to **80M** — and the architecture gives **no total**, so
  **the total is what is derived and the partition is what is stated.** This inverts every previous
  section: chunks 01 through 04 all failed allocation at the same place, a stated total with no
  partition across the sub-elements the edges terminate on. **Here `allocate` closes at the sub-element
  level for the first time, for four sub-elements.**
  **L = 8 laminae**, the granular isocortical set, and **the four counts do not divide among the
  laminae** — so allocation closes one level down from the total and not two.
  **M = digit modules, inside areas 3b and 1 only**, **discrete representations of individual digits**,
  resolvable in imaging and separately affected by deafferentation. **No module count is given**, and
  **areas 3a and 2 have no such axis**, so the four arrays are not the same rank.
  **P is plastic, and that is a different kind of open than an underived extent.** The somatotopic axis
  **reorganises after input change**, and **an extent that moves with experience is not the same kind of
  extent as one that does not.** An underived extent is a number nobody has supplied; **this is an
  extent that has no single true value at any time.** **A fixed-extent array asserts a stability the
  structure does not have**, and what a re-organising axis is in code is **not settled at any rung.**
  *(The plasticity is the architecture's; that it makes the extent a different kind of quantity from an
  underived one is Claude's reading.)*
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `count_3a` | neurons per hemisphere | **~15,000,000** | architecture Sizing |
  | `count_3b` | neurons per hemisphere | **~25,000,000** | architecture Sizing |
  | `count_1` | neurons per hemisphere | **~20,000,000** | architecture Sizing |
  | `count_2` | neurons per hemisphere | **~20,000,000** | architecture Sizing |
  | `structure_total` | neurons | **80,000,000** — **derived, not stated** | recomputed from the four |
  | `parameter_memory` | bytes | **30.00 / 50.00 / 40.00 / 40.00 MB**, total **160.00 MB** | recomputed at 16 bits |
  | `lamina_count` L | laminae | **8** — granular isocortex, the block applies here | architecture Shape |
  | `digit_module_count` M | modules | **to derive**, and **only in areas 3b and 1** | architecture Function |
  | `thalamic_share_layer1` | fraction | **~32%** of layer-1 long-range input | architecture Function |

- **Update equation.** **Waiting on the emission question**, and on the arithmetic of the three payload
  changes, none of which is named above. What is fixed regardless: **the two streams stay parallel to
  area 2**, and **the area-3a output is two objects and not one** — a graded per-digit position vector
  and a categorical posture signal. **An equation emitting a single proprioceptive scalar would have
  collapsed a distinction the architecture draws from single-unit recording.**
- **State carried between updates.** The four activity arrays. **And the somatotopic map itself is
  state under any learning rule** — it is **self-organising and highly plastic** — so this is the one
  structure in the file where the extent and the state are the same object. No time constant is stated.
  Initial values: to derive.
- **Edge storage.** 2 input edges, 8 output edges declared, plus 4 internal edges under the serial
  reading. Line counts: all to derive — **the counts are known and the fan-ins are not**, so the
  structure that can be allocated still cannot have its edges sized. Latency to derive. Interval unset.
  **Not summable.**
- **Adaptation.** **None set** — **and this is the entry where that costs the most in the file.** The
  map is **self-organising and highly plastic, reorganising after input change**; that is a stated
  property of the structure, not an aside, and **no rule for it exists at any rung.** An entry whose
  Shape field says the extent moves and whose Adaptation field says nothing changes it is internally
  incomplete, and it is incomplete **at the rung above this one.**
- **Invariant note carried from the architecture.** Co-instantiation: **the corticothalamic gate and
  the corticocuneate gain edge both close here, and the return limb of the motor loop arrives from the
  world.** Per-edge latency: satisfied.
- **Open, beyond the standing list.**
  - **The rule that reorganises the map.** Micky's, and the structure's stated function depends on it.
  - **The arithmetic of the three payload changes** along the chain, none of it named above.
  - **The chain-versus-parallel contest**, which leaves the declared edge set a superset.
  - **M has no count**, and only two of the four areas have the axis.
  - **P is plastic**, which is not an underived extent but an extent with no single true value.
  - **The layer-1 matrix line's payload**, **owed at both ends**, and **no internal edge from tuft to
    soma.**
  - **Whether a unit has compartments**, without which that line cannot be delivered. Micky's.
  - **The intracortical majority of the fan-in is not enumerated anywhere**, so a topology built from
    the declared edges is a minority of the real convergence.
  - **Naming the medial intraparietal area** on the parietal class line is owed at the source; **the
    insular endpoint is unchecked**, its far end being in `17_insula_claustrum_habenula`.

---

# 4. Second somatosensory area

**A bundle, and it stays one.** Three fields in one slot set — the second somatosensory area proper,
the parietal ventral area, and the ventral somatosensory area. The split is owed at the source.

## Contract

**Inputs.** **← primary somatosensory cortex** — cutaneous by areas 3b and 1, deep by areas 3a and
2, **two parallel channels, not one merged stream**; **whether this edge is necessary for the
region to respond is the disputed topology.** **← ventral posterior thalamus** and **← the
anterior pulvinar** — **deep-receptor signals, not cutaneous. This is the entry's correction:**
these fields receive **little if any cutaneous input from the thalamus**, so their cutaneous
payload must arrive through the cortical edge, **and an account that treats this region as a second
cutaneous relay fed from the thalamus has the modality backwards.** **The anterior-pulvinar limb is
declared at this end only** and the pulvinar entry names no somatosensory target, **so it is owed
or withdrawn — and it is a second endpoint on a shared line, so splitting the line is owed too.**
**← the contralateral second somatosensory area, area 3b and area 7b**, callosal — **the opposite
side's tactile payload, which is what makes the bilateral receptive field.** **The parietal ventral
area's callosal connections are restricted to its own homologue and the second somatosensory
area's are not**, so the two fields **differ in how much of the other hemisphere they see.**

**Outputs.** **→ area 7b**, **→ the anterior intraparietal area** (`06_posterior_parietal`),
**→ posterior parietal cortex** (a class, **owed**), **→ premotor cortex** from the parietal ventral
area (`11_frontal_lobe`), **→ the parietal rostroventral area** (**owed**, far end unchecked), **→ the insula** from
the ventral somatosensory area (**owed**), and **→ primary somatosensory cortex** reciprocally
(feedback, no new stimulus content).

**Sizing.** Basis: per hemisphere. **Neurons: unknown — the only unpriced structure in this
section.** Everything else in its slot list is unknown too. **Structure total: to derive.**

**Shape.** Rank 3: **(field, map position, lamina)** — three fields, and **the map axis reverses at
the seam**, since the second somatosensory and parietal ventral areas are mirror-symmetric maps
joined at the hand, foot and face.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← primary somatosensory cortex | **cutaneous by 3b and 1, deep by 3a and 2 — two parallel channels, not one merged stream** | to derive | **event-driven** | somatotopic on arrival; **and this line carries the cutaneous payload, because the thalamic lines do not** |
| ← ventral posterior thalamus; ← the anterior pulvinar | **deep-receptor signals, not cutaneous** | to derive; **little if any cutaneous content** | event-driven | to derive |
| ← contralateral second somatosensory area, area 3b and area 7b (callosal) | **the opposite side's tactile payload** | to derive | event-driven | **the other hemisphere's body map — and this is what makes the receptive field bilateral** |
| → area 7b; → the anterior intraparietal area; → posterior parietal cortex (a class); → premotor cortex; → the parietal rostroventral area; → the insula | **owed** on the class and on three named limbs | owed | event-driven | owed |
| → primary somatosensory cortex (reciprocal) | **feedback, no new stimulus content** | to derive | event-driven | somatotopic |

**Row 1 against row 2 is the entry's correction and it inverts the intuitive wiring.** These fields
receive **little if any cutaneous input from the thalamus**, so **the cutaneous payload must arrive
through the cortical edge.** **An account that treats this region as a second cutaneous relay fed from
the thalamus has the modality backwards** — and that account is exactly what a coder builds by analogy
with the first relay. **The Representation table is where the inversion is visible**, because the two
rows differ in modality and not in strength.

**Row 3 is the first line in this pathway carrying the other body side.** Receptive fields here are
large and frequently bilateral — spanning multiple digits, the whole hand, or **both hands** — and
**this is the first place in the pathway where the two body sides converge.** **The callosal line is
what makes that true**, so an implementation without it does not have a degraded receptive field; it
has a unilateral one.

## Algorithm

- **Transform.** **Tactile object identity and stereognosis — texture, shape, material, invariant to
  the exact contact point.** **The invariance is the operation and its arithmetic is not stated.**
  *Invariant to the exact contact point* names what the output does not depend on, which is a
  well-formed specification of an invariance and not an operation over arrays — and **no rung above
  says how the invariance is obtained.** Per §5 that is a finding about the structure.
- **The name covers more than one field, and the fields are not interchangeable.** The parietal
  operculum holds at least three: the **second somatosensory area** caudally, the **parietal ventral
  area** rostral to it, and the **ventral somatosensory area** deeper in the sulcus, its inner edge
  adjoining insular cortex. **The first two are mirror-symmetric body maps joined at the hand, foot and
  face representations.** In human they occupy parts of **Brodmann areas 40 and 43.**
- **The map axis reverses at the seam, and no other axis in the map does this.** Two mirror-symmetric
  maps joined at the hand, foot and face means **the position axis runs one way in one field and the
  other way in the other**, meeting at shared representations. **A single monotonic index across the
  field axis is wrong at the seam**, and the seam is not located by any number given above. **The three
  fields also differ in how much of the other hemisphere they see** — the parietal ventral area's
  callosal connections are restricted to its own homologue and the second somatosensory area's are not
  — so **the field axis carries a connectivity difference as well as a position reversal.** Recorded.
  *(The mirror symmetry and the callosal difference are the architecture's; that a monotonic index
  fails at the seam is Claude's reading.)*
- **Neurons here are less modality-specific than in primary somatosensory cortex**, which is a stated
  property of the population and constrains the arrays: **the parallel cutaneous and deep channels that
  the previous structure preserved are not preserved here**, and nothing above says what replaces them.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `s2_active` | (F, P, L) | open — emission question | to derive | to derive |
  | `s2_threshold` | (F, P, L) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |

  **F = 3 fields**, and **every extent in this entry is unknown.** **Neurons: unknown — the only
  unpriced structure in this section — and everything else in its slot list is unknown too.**
  **P reverses at the seam** and its extent is not given. **L = 8 laminae**, the granular isocortical
  set. **So this is the one structure in the file that can be described and not allocated at all**,
  which is the exact inverse of entry 3.
  Per §5b **unknown** is the right state and not *to derive*: it exists and has not been measured, which
  is an experiment to run rather than a reading to look up.
- **Parameters.** **None has a value.** `neuron_count` — **unknown**; `field_count` F = **3**;
  `fan_in` — to derive, bounded ≤ 16 bits; `seam_position` — not given. **Structure total: to derive.**
- **Update equation.** **Not written**, and blocked beyond the standing list by the invariance
  arithmetic, which no rung supplies. What is fixed regardless: **the cutaneous payload arrives on the
  cortical line and not the thalamic one**, so an equation drawing cutaneous content from the thalamic
  input has the modality backwards.
- **State carried between updates.** `s2_active`. No time constant is stated. Initial values: to derive.
- **Edge storage.** 4 input edges, 7 output edges. Line counts: **all unobtainable**, since the neuron
  count itself is unknown. Latency to derive. Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Invariant note carried from the architecture.** Co-instantiation: **the reciprocal edge to primary
  somatosensory cortex closes here.** Per-edge latency: satisfied.
- **Open, beyond the standing list.**
  - **Every extent.** The count is **unknown**, the field extents are unknown, the seam is unlocated.
  - **The invariance arithmetic**, which is the entry's stated function.
  - **What replaces the parallel cutaneous and deep channels** in a less modality-specific population.
  - **The anterior-pulvinar limb is declared at this end only** and the pulvinar entry names no
    somatosensory target — **owed or withdrawn**, and **splitting the shared line is owed too.**
  - **The bundle's split into three fields.** Owed at the source.
  - **A finding that cuts against the description's own stream model, and it is carried rather than
    resolved.** The authors of the connection study conclude that these patterns suggest the
    somatosensory system **may not be segregated into two separate streams** in the way hypothesised
    for vision — the fields' cortical and thalamic connections **overlap rather than sorting into a
    "what" and a "where."** **The map carries an explicit dorsal/ventral split for vision, and whether
    the same split is imported into touch is a claim this entry does not support.** **Nothing at this
    rung is built on the split**, and it is recorded because a design that named a dorsal and a ventral
    somatosensory stream would be importing an unsupported claim from another section.

---

# 5. Superior parietal area 5

## Contract

**Inputs.** **← primary somatosensory cortex** (principally area 2, with 3a) — limb configuration
and tactile object properties in a **skin / joint** frame. **← the medial bank of the
intraparietal sulcus, the parietal opercular areas PGop and PFop, and the retroinsular area** —
(the medial-bank limb in
`06_posterior_parietal`) — **payload owed**, and **this line names four sources at once, so
splitting it is owed.** That entry declares `→ superior parietal area 5, onto the
medial bank (area PEa)`, naming the medial bank and area PEa in the same terms this line uses, and
marks its own payload owed. **So the limb is two-ended and untyped at both ends**, which is a
different state from having no producer. **The other three sources on this line were not tested** —
PGop, PFop and the retroinsular area have far ends outside the two files opened here, so they are
unchecked rather than absent, and the split this line owes is now between one two-ended limb and
three unchecked ones. **← the precuneus** (`06_posterior_parietal`), from its anterior
sensorimotor sector — reach and body-configuration signals, body-centred; **that entry calls it the
one edge out of itself whose payload can be written.** That entry records that this end was transcribed from it, **so the agreement between the two ends
certifies nothing about the payload** — it is one statement written twice, not two readings that
matched. **← primary motor cortex, the supplementary
motor area and caudal dorsal premotor cortex** (the two frontal limbs in `11_frontal_lobe`) —
**payload owed; the studies establish the projection, not its content.** **The three sources are in three different states, which is why splitting this line is owed.** The
supplementary motor area and caudal dorsal premotor cortex are one structure in that file, and it
declares `→ superior parietal area 5` — **two-ended, untyped there as here.** **The primary motor
limb has no producer end, and the producer is in this file**: that entry's Outputs slot declares
muscles, the return through the world to primary somatosensory cortex, the ventral anterior /
ventral lateral thalamus and the dorsal column nuclei, **and no parietal target of any kind.**
**An in-file edge declared at one end only is a weaker state than a cross-file one**, because
nothing about file boundaries explains it. **Owed at the source: declare it at primary motor
cortex, or withdraw it here.** **← the posterior cingulate area PEci and cingulate areas 23 and
24** — owed, and for **PEc** substantial: **about 15% of its labelled afferent neurons lie in PEci
and a further 10% elsewhere on the medial surface — 25% in total**, recomputed. **← gaze-position
signals**, reaching PEc and PEa — eye position, and for PEc **the interaction of gaze with hand
position rather than either alone.**

**Outputs.** **→ dorsal premotor cortex** — limb position and the reach specification; **the
payload change across this region is the frame, not the content.** **→ primary motor cortex**
(reciprocal with area PE), **→ the medial, anterior, ventral and lateral intraparietal areas**, **→
the supramarginal gyrus** (`06_posterior_parietal`), **→ the precuneus**
(`06_posterior_parietal`) — the same limb state.
Four of the six named limbs are declared at their far ends in `06_posterior_parietal`: the anterior
intraparietal area (`← superior parietal area 5`, principally area PE), the medial intraparietal
area (on its four-source arm-configuration line), the supramarginal gyrus (`← superior parietal area
5`, body configuration) and the precuneus (`← superior parietal area 5`, body configuration and
spatial layout). **The ventral and lateral intraparietal limbs are unchecked** — their far ends are
in `04_dorsal_visual_parietal_stream` — **and the dorsal premotor limb
above is two-ended** with `11_frontal_lobe`.
**Two of the four discharged ends warn that they certify nothing.** The supramarginal and precuneus
entries both record that their end was transcribed from this one, **so those two are one statement
written twice.** The two intraparietal ends were written independently. **Replacing a false absence
with a true declaration is not the same as replacing it with agreement**, and only two of the four
are agreement.
**Splitting the intraparietal line is owed and now has a reason**: it names four areas in two files
and three states.

**Sizing.** Basis: **per hemisphere. ~25M neurons**, soft, **no per-subdivision count found** —
so this structure has the sub-elements and not the partition, the ordinary case. At the 16-bit
ceiling: **50.00 MB.**

**Shape.** Rank 2: **(subdivision, position)** — three subdivisions forming an
**anterior-to-caudal functional gradient**: **PE** most sensitive to limb proprioception and
encoding arm position with **the most independence from gaze**; **PEa** proprioceptive and
kinematic, **the reach-planning end**; **PEc** sensitive to **proprioception and gaze together**,
linked to lower-limb motor representations, vestibular cortex and optic-flow areas, with a proposed
role in **locomotion and limb coordination in the environment, not reaching alone.**

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← primary somatosensory cortex (principally area 2, with 3a) | limb configuration and tactile object properties | to derive | **event-driven** | **skin / joint** |
| ← the medial bank, PGop, PFop, the retroinsular area | **payload owed** | owed | event-driven | owed — **and the line names four sources at once** |
| ← the precuneus, anterior sensorimotor sector | reach and body-configuration signals | to derive | event-driven | **body-centred — and the two ends agreeing certifies nothing, one having been transcribed from the other** |
| ← primary motor cortex, the supplementary motor area and caudal dorsal premotor cortex | **payload owed; the studies establish the projection, not its content** | owed | event-driven | owed |
| ← posterior cingulate area PEci and cingulate areas 23 and 24 | **owed** — and for PEc **25% of labelled afferents** | owed | event-driven | owed |
| ← gaze-position signals | eye position; **for PEc the interaction of gaze with hand position rather than either alone** | to derive | event-driven | eye |
| → dorsal premotor cortex | limb position and the reach specification | to derive | event-driven | **contested — see below. The payload change across this region is the frame, not the content** |
| → primary motor cortex; → the medial, anterior, ventral and lateral intraparietal areas; → the supramarginal gyrus; → the precuneus | **the same limb state** | to derive | event-driven | **contested at this end, body-centred at two far ends** |

**The frame is contested and on this project's payload rule that makes the payload unsettled.** The
reported frames are **body-, shoulder- and hand-centred across different studies**, and in area PE
specifically a memorised target's distance is encoded **relative to the initial hand position rather
than to the body.** **This matters more than a nomenclature dispute would, because on this
description's payload rule the coordinate frame is part of the payload, so an unsettled frame is an
unsettled payload.**

**And the far ends have not withdrawn.** The medial intraparietal area and the precuneus both **type
the frame as body-centred**, so **the two ends disagree about the frame, which is a payload
disagreement and not a wording one.** Per §5b this reads **contested**: measured, and yielding readings
that disagree.

**Row 6 is the one input line whose payload is a modulator of another line's meaning.** For **PEc** the
signal is **the interaction of gaze with hand position rather than either alone** — so gaze is not an
independent content channel there but a term the limb payload is expressed against. **That is the
fourth structure in the map to have gaze modulate a non-visual payload**, and the arithmetic is again
the open unit-expressiveness question.

## Algorithm

- **Transform.** **The payload change across this region is the frame, not the content.** The
  architecture states it directly, and it is the entry's clearest specification: **limb position and
  the reach specification go in and come out re-expressed**, with cardinality and content preserved.
  **And the frame they come out in is contested**, so the transform's output type is unsettled —
  **the one operation this entry states is the one its own Justification field says is disputed.**
- **It is not a purely sensory area, and that changes what the update equation is allowed to depend
  on.** Movement-related activity **persists in the absence of sensory stimulation**, so it is
  **internally generated rather than driven**, and the area is active in movement **preparation**.
  **At this rung: an equation that computed the output as a function of the input arrays alone would
  produce a structure that goes silent when the inputs do**, and the architecture says this one does
  not. **What generates the persistent activity is not stated at any rung**, so no equation is written
  — but the constraint on any eventual one is recorded, because it is checkable against the finished
  code.
- **The three subdivisions form an anterior-to-caudal functional gradient and they are not
  interchangeable.** **PE** on the gyral convexity, most sensitive to limb proprioception, encoding arm
  position with **the most independence from gaze**; **PEa** on the medial bank of the intraparietal
  sulcus, proprioceptive and kinematic, **the reach-planning end**; **PEc** caudally, sensitive to
  **proprioception and gaze together**, linked to lower-limb motor representations, vestibular cortex
  and optic-flow areas, with a proposed role in **locomotion and limb coordination in the environment,
  not reaching alone.** **Human area 5 overlaps all three**, and is distinguished by **a dense
  concentration of SMI-32-immunoreactive pyramidal neurons in layers III and V.**
  **A gradient is not a partition, and the array has to be one or the other.** Three named subdivisions
  along a continuum, with **no per-subdivision count**, means an index into the subdivision axis names a
  position on a gradient rather than a member of a set. **Which of the two the axis is is not stated**,
  and the difference matters: gaze-dependence varies along it, so an edge terminating on "area 5" lands
  on cells whose gaze sensitivity depends on where along the gradient they sit.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `a5_active` | (D, P) | open — emission question | to derive | to derive |
  | `a5_threshold` | (D, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `persistent_state` | (D, P) | open | to derive | **internally generated, not driven** |

  **D = 3 subdivisions**, **no per-subdivision count found** — **so this structure has the
  sub-elements and not the partition, the ordinary case**, and it is the direct contrast with entry 3.
  **P has no extent.**
  **`persistent_state` is an array the architecture requires and does not describe.** Movement-related
  activity persists without sensory stimulation, so something is held; **its shape, its initial value
  and what writes it are all unstated.**
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~25,000,000**, soft | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling | architecture Sizing |
  | `parameter_memory` | bytes | **50.00 MB** at 25M × 16 bits | recomputed |
  | `subdivision_count` D | subdivisions | **3** — PE, PEa, PEc, **no per-subdivision count** | architecture Shape |
  | `pec_cingulate_afferent_share` | fraction | **25%** — 15% in PEci plus 10% elsewhere on the medial surface | recomputed from the architecture's two figures |
  | `output_frame` | — | **contested: body-, shoulder- and hand-centred** | architecture Justification |

- **Update equation.** **Not written**, and blocked beyond the standing list by three things: the output
  frame is contested, so the transform's output type is unsettled; the persistent activity's generator
  is unstated; and the gaze interaction at PEc is a modulation whose arithmetic is the open unit
  question. What is fixed regardless: **cardinality and content are preserved and only the frame
  changes.**
- **State carried between updates.** `a5_active` and `persistent_state`. **The second is required by
  the architecture's own Function field and described nowhere.** No time constant is stated. Initial
  values: to derive.
- **Edge storage.** 6 input edges, 8 output edges across the named limbs. Line counts: all to derive.
  Latency to derive. Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Invariant note carried from the architecture.** Co-instantiation: **reciprocal with primary motor
  cortex and with the intraparietal areas.** Per-edge latency: satisfied.
- **Open, beyond the standing list.**
  - **The output frame is contested**, and on the payload rule that makes the payload unsettled — with
    **the two ends disagreeing**, which is a payload disagreement and not a wording one.
  - **What generates the persistent activity.** Required by the Function field, described nowhere.
  - **Whether the subdivision axis is a partition or a gradient.**
  - **No per-subdivision count.**
  - **Two lines name four sources each** and both splits are owed at the source.
  - **The primary motor limb has no producer end and the producer is in this file** — a weaker state
    than a cross-file one-ended edge, because nothing about file boundaries explains it. **Owed at the
    source: declare it at primary motor cortex, or withdraw it here.** **Not repaired here**, because
    writing it at the producer would assert a connection this rung has read nothing for.
  - **Two of the four discharged output ends certify nothing**, having been transcribed from this one.

---

# 6. Primary motor cortex

**This is the structure whose output loop does not close inside the map**, and it is the one entry in
this file where the standard laminar block is withheld.

## Contract

**Inputs.** **← primary somatosensory cortex, area 3a** — proprioceptive and cutaneous feedback,
**the consequence of the last command.** **← premotor cortex** (`11_frontal_lobe`) — **the planned action, already
sequenced and shaped, not yet a muscle command**; the far end declares it and is **untyped**.
**← superior parietal area 5** (reciprocal with area PE) — limb position and the reach
specification **in a contested frame.** **← thalamus, ventral anterior / ventral lateral** — **the
basal-ganglia selection (which action is released) and the cerebellar correction (how it is
shaped), combined on one relay**; the far end names this area but is **untyped**.
**Two inbound edges are declared at producers in `11_frontal_lobe` and are not declared here.** Broca's area declares `→ premotor cortex and primary motor cortex, for
articulation`, and the right inferior frontal gyrus declares the homologous edge for affective
prosody. **That file already records that its own premotor structure declares neither, and marks
both as inherited gaps owed at the source. This end is the second consumer on both, and it does
not declare them either** — so each edge is producer-only at **both** of its two named targets
rather than at one. **They are not written in above**,
because writing an edge whose only support is the far end's declaration would assert a
connection this file has read nothing for. **Owed at the source: accept both here, or narrow the
producers' endpoint to premotor cortex alone.**

**Outputs.** **→ muscles**, by the corticospinal tract — the motor command. **The consumer at the
far end is not in this map**: the muscles, the skeleton and their dynamics have no entry, **so this
edge's payload is declared with no one to receive it.** **→ (returning through the world) →
primary somatosensory cortex** — the movement's **consequence**, read back through proprioception;
**fan-out not applicable.** **→ thalamus, ventral anterior / ventral lateral**, corticothalamic and
reciprocal — **owed at both ends.** **→ dorsal column nuclei**, corticocuneate from the forelimb
region — the same movement-contingent gain signal primary somatosensory cortex declares, **arriving
on the same target**, and **its distinctness from the somatosensory limb is owed**: the retrograde
study labelled both and whether they carry the same content is not established.

**Sizing.** Basis: **per hemisphere. ~30M neurons**, soft. At the 16-bit ceiling: **60.00 MB.**

**Shape.** Rank 2: **(lamina, somatotopic position)** — seven laminae, and **tangential
sub-elements owed**: whether the somatotopic motor map and the movement primitives are a
compartmentation an edge could terminate on, or a continuous map, **is not established.**

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← primary somatosensory cortex, area 3a | **the consequence of the last command** — proprioceptive and cutaneous feedback | to derive | **event-driven** | limb and joint configuration |
| ← premotor cortex | **the planned action, already sequenced and shaped, not yet a muscle command** | to derive | event-driven | to derive; **the far end is untyped, so this end carries the payload** |
| ← superior parietal area 5 (reciprocal with PE) | limb position and the reach specification | to derive | event-driven | **contested — body-, shoulder- or hand-centred** |
| ← thalamus, ventral anterior / ventral lateral | **the basal-ganglia selection (which action is released) and the cerebellar correction (how it is shaped), combined on one relay** | to derive | event-driven | to derive; the far end names this area and is **untyped** |
| → muscles (corticospinal) | **the motor command** | to derive | event-driven | **the body — and the consumer is not in this map** |
| → (returning through the world) → primary somatosensory cortex | **the movement's consequence, read back through proprioception** | to derive | **event-driven, and the event is outside the map** | **the world.** Fan-out: **not applicable** |
| → thalamus, ventral anterior / ventral lateral (corticothalamic, reciprocal) | **owed at both ends** | owed | event-driven | owed |
| → dorsal column nuclei (corticocuneate, forelimb region) | **the movement-contingent gain signal** | to derive | event-driven | somatotopic, centre–surround; **its distinctness from the somatosensory limb is owed** |

**Row 4 carries two payloads on one line and the architecture says so.** **Which action is released**
comes from the basal ganglia and **how it is shaped** from the cerebellum, **combined on one relay** —
so this is a single line whose content is two decisions of different kinds, and **splitting it would
require the relay to be split, which is another file's decision.**

**Rows 5 and 6 are the pair that does not close.** Row 5 has a payload and **no consumer in the map**;
row 6 has a producer **outside** it. **They are the same physical loop and neither end of it is
represented**, so the two rows cannot be checked against each other the way every other producer /
consumer pair in this file can.

**Row 8 duplicates a line declared by another structure in this file.** Primary somatosensory cortex
declares the same movement-contingent gain signal onto the same target, and **its distinctness from
this limb is owed** — the retrograde study labelled both and **whether they carry the same content is
not established.** **So the code declares two edges where there may be one payload**, which is the
second place in this file where the graph is knowingly a superset.

## Algorithm

- **Transform.** **Corticospinal drive to muscles; a somatotopic motor map and movement primitives.**
  **No standard operation name is given and per §5 that is a finding.** *Movement primitives* names a
  vocabulary of outputs rather than an operation producing them, and **what a primitive is, as an
  object with a shape and a range, is not stated at any rung.**
- **Agranular cortex, and this is the entry's structural fact.** **Thin or absent layer 4, layer-5
  pyramidal and Betz-cell heavy — because it is output-dominated.** **Laminar sub-elements: seven, not
  eight — 1, 2, 3, 5a, 5b, 6a, 6b.**
- **The standard laminar block is withheld here and the withholding is the finding.** Three of its
  edges terminate on or leave from **layer 4**, which this entry says is thin or absent, **so
  transcribing it would assert a circuit the entry's own Function denies.** **The internal edges
  therefore read owed.** **A laminar set copied across entries is a Class-3 claim that has to be
  checked against each entry's own laminar description, and here it fails** — with eight further
  entries across four other files failing it in three more ways.
  **At this rung the cost is that this structure has no internal edges at all.** Every other cortical
  entry in this file carries either the block or its own named internal edges; this one carries
  neither, and **the gap is stated rather than filled.** The scope table in the standing list is where
  the withholding is made general.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `m1_active` | (L, P) | open — emission question | to derive | to derive |
  | `m1_threshold` | (L, P) | width `ceil(log₂(fan_in))`, **fan_in to derive**, bounded 16 | 0 … fan_in | count of active inputs |
  | `motor_command` | to derive | open | to derive | **the corticospinal output — no consumer in the map** |

  **L = 7 laminae, not 8**, and **no laminar count**, so the ~30M does not divide among them.
  **P is the somatotopic motor map and its status is owed**: whether the map and the movement
  primitives are **a compartmentation an edge could terminate on, or a continuous map, is not
  established.** **That is a question about whether the axis is indexable at all**, which is a
  different open state from an axis with no extent — and this entry has both.
  **`motor_command`'s shape is not derivable, because its consumer is not in the map.** Every other
  output array in this file gets its shape from what receives it; **there is nothing to receive this
  one**, and the muscles, the skeleton and their dynamics have no entry anywhere.
- **Parameters.**

  | parameter | unit | value / range | origin |
  |---|---|---|---|
  | `neuron_count` | neurons per hemisphere | **~30,000,000**, soft | architecture Sizing |
  | `threshold_bits` | bits | **16**, the ceiling | architecture Sizing |
  | `parameter_memory` | bytes | **60.00 MB** at 30M × 16 bits | recomputed |
  | `lamina_count` L | laminae | **7, not 8** — 1, 2, 3, 5a, 5b, 6a, 6b | architecture Function |
  | tangential sub-elements | — | **owed** — compartmentation or continuous map, not established | architecture Shape |

- **Update equation.** **Not written**, and blocked beyond the standing list by three things: the
  transform is unnamed, the internal edges are owed because the block is withheld, and **the output
  has no consumer to be typed against.** What is fixed regardless: **the input from area 3a is the
  consequence of the last command and not a new stimulus**, so **an equation treating it as sensory
  drive would have deleted the loop's meaning** — it is feedback about what this structure just did.
- **State carried between updates.** `m1_active`, and whatever a movement primitive holds while it
  unfolds — **which is not described.** No time constant is stated. Initial values: to derive.
- **Edge storage.** 4 input edges declared here (**plus 2 more declared only at producers in another
  file and deliberately not written in**), 4 output edges. Line counts: all to derive, and **the
  corticospinal line's is unobtainable**, having no far end to count against. Latency to derive.
  Interval unset. **Not summable.**
- **Adaptation.** **None set.**
- **Invariant note carried from the architecture.** Co-instantiation: **this is the structure whose
  output loop does not close inside the map.** Per-edge latency: satisfied.
- **Open, beyond the standing list.**
  - **The output edge has no consumer**, and the return line has no producer. **Not repairable at any
    rung below the source**, and not closable by any work here.
  - **What a movement primitive is**, as an object with a shape and a range.
  - **The internal edges**, owed because the laminar block is withheld.
  - **Whether P is indexable at all** — compartmentation or continuous map, not established.
  - **No laminar count**, so the seven laminae have no partition.
  - **The corticocuneate limb's distinctness** from the somatosensory one, **owed**.
  - **The two edges declared at producers in `11_frontal_lobe` and not here** — Broca's area and the
    right inferior frontal gyrus. **Each is producer-only at both of its named targets.** **Owed at
    the source: accept both here, or narrow the producers' endpoint to premotor cortex alone.** **Not
    written in**, because writing an edge whose only support is the far end's declaration would assert
    a connection this file has read nothing for.

---

## Section totals

Copied from the architecture, with one column added at this rung: **the realised store, which here
equals the derived store because every width is already at a container boundary.**

| # | structure | basis | neurons | bits/neuron | parameter memory | realised at 16 bits |
|---|---|---|---|---|---|---|
| 1 | Dorsal column nuclei and trigeminal relay | per hemisphere | ~0.5M | ≤ 16 | ≤ 1.00 MB | 1.00 MB |
| 2 | Ventral posterior thalamus | per hemisphere | ~2.5M | ≤ 16 | ≤ 5.00 MB | 5.00 MB |
| 3 | Primary somatosensory cortex — area 3a | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB | 30.00 MB |
| 3 | Primary somatosensory cortex — area 3b | per hemisphere | ~25M | ≤ 16 | ≤ 50.00 MB | 50.00 MB |
| 3 | Primary somatosensory cortex — area 1 | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB | 40.00 MB |
| 3 | Primary somatosensory cortex — area 2 | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB | 40.00 MB |
| 4 | Second somatosensory area | per hemisphere | **unknown** | ≤ 16 | **to derive** | **to derive** |
| 5 | Superior parietal area 5 | per hemisphere | ~25M | ≤ 16 | ≤ 50.00 MB | 50.00 MB |
| 6 | Primary motor cortex | per hemisphere | ~30M | ≤ 16 | ≤ 60.00 MB | 60.00 MB |
| | **stated total** | per hemisphere | **~138M** | | **276.00 MB**, one row unpriced | **276.00 MB** |

Recomputed here: **138M neurons and 276.00 MB**, with the four somatosensory areas summing to **80M
and 160.00 MB.** All reproduce. Against the earlier sections: **2.2× chunk 04, 0.57× chunk 02.**

**The realisation gap is zero, for the same reason it was zero in chunk 04 and it is still not good
news.** Every width here is the **16-bit ceiling**, which is a container boundary by construction, so
nothing is lost to padding. **No fan-in in this section is known** — every edge reads *to derive* at
every structure — so every neuron sits at the cap and nothing is derived below it. **A zero gap and an
unmeasured fan-in are the same fact stated twice.**

**The first partition in the map, and it is worth saying exactly what makes it one.** Every previous
section stated a total for a structure and named sub-elements the edges terminate on, with nothing
connecting them — eight belt fields sharing one count, two parabelt divisions sharing another, a
lateral intraparietal subdivision border established by two independent stains with no count split
across it. **Here primary somatosensory cortex is given no total at all: it is given four counts, one
per area, and the total is what has to be derived.** So `allocate` closes at the sub-element level for
the first time, for four sub-elements.

**And the partition stops there.** The dorsal column nuclei have three nuclei, two territories and
**no separate count for the external cuneate nucleus** — which is the sub-element the cerebellar edge
leaves from, so **the one edge whose source is a named sub-element cannot be sized.** The thalamus has
core and matrix and **no core-versus-matrix count.** Area 5 has three subdivisions and **no
per-subdivision count.** Primary motor cortex has seven laminae and no laminar count. **One structure
in six partitions; the other five are the ordinary case.**

**At this rung the partition buys exactly one thing, and it is worth being precise about how little.**
Four arrays can be allocated where an unpartitioned count could not be. **It does not buy an edge**: every fan-in
in the section is underived, so the structure that can be allocated still cannot have its edges sized.
**Allocation and connection are separate closures and this section closes the first for one structure
and the second for none.**

**Three findings about representation, and none of them is a gap in the description.**

1. **A compartment that is not contained in a structure.** The calbindin matrix runs uninterrupted out
   of the ventral posterior complex into the anterior pulvinar and the posterior and ventral lateral
   nuclei. **Per-region edges cannot express a population that crosses region boundaries**, and the
   description says so. At this rung neither available allocation is honest — one asserts a boundary
   the biology does not have, the other asserts several populations where there is one.
2. **A topology that is contested rather than a payload.** Whether the four somatosensory areas are
   serial or parallel is disputed by two methods that are not measuring the same thing, and the
   description **keeps both edge sets rather than choosing** — so **the graph has more edges than the
   anatomy may.** This is the one open state in the project that makes the code **larger** than the
   biology rather than smaller.
3. **A laminar template that is a claim, not a default.** Nine entries across five files cannot take
   the standard block, failing in four distinct ways, **so a single exception clause would not cover
   them.** **Stating the block's scope was owed at this rung and is discharged in the standing list
   above**, as a scope table rather than a sentence — and stating the scope does not license the
   block's arithmetic, which no entry below writes.

**Two arithmetic cautions carried from the description, and both are honoured below rather than
restated.** The **87% convergence figure is not a fan-in measurement** — it counts cells responding to
two or more nerve territories, not contacts per neuron. And the **~10% nociceptive figure at the
thalamus is carried forward unverified**, flagged as a candidate for removal or sourcing. **Neither
may be promoted into a width or a fraction at a lower rung**, and neither appears in any parameter
table in this file: `fan_in` at the dorsal column nuclei reads None, and there is no
`nociceptive_fraction` anywhere.

**The section's largest fact is not in the table.** The motor output edge has no consumer in the map,
the return path runs through the world, and proprioception is delivered twice — once as a reportable
percept and once as procedural change in a cerebellum this section does not describe. **Memory is not
a binding constraint and none of these figures is to be reduced; state memory and edge storage are not
in the total.**

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
| 1 Dorsal column nuclei and trigeminal relay | **what the structure computes**, unnamed above; the centre–surround arithmetic; **P has no extent and two meanings**; no count for the external cuneate nucleus, so one edge's line count is unobtainable; where the trigeminal relay sits in the shape; a possible third payload, **contested for human** |
| 2 Ventral posterior thalamus | the matrix line's payload, **owed at both ends**; **a compartment axis that does not fit inside the structure**; no core-versus-matrix count; **contested** lamina-I routing; a contested subnucleus scheme with a different arity; the triad, which the edge type cannot express |
| 3 Primary somatosensory cortex | **the rule that reorganises the map** — its stated function; the arithmetic of three payload changes; **the chain-versus-parallel contest**; M has no count; **P is plastic**; no internal edge from tuft to soma; whether a unit has compartments |
| 4 Second somatosensory area | **every extent** — the count is **unknown**; the invariance arithmetic; what replaces the parallel channels; **the seam is unlocated**; the anterior-pulvinar limb, owed or withdrawn |
| 5 Superior parietal area 5 | **the output frame is contested and the two ends disagree**; what generates the persistent activity; partition or gradient; no per-subdivision count; **an in-file edge declared at one end only** |
| 6 Primary motor cortex | **an output edge with no consumer and a return line with no producer**; what a movement primitive is; internal edges owed because the block is withheld; **whether P is indexable at all**; two producer-only edges from another file |

**Three of these reach past this file rather than waiting inside it**, and they are named separately
because they are not gaps to be filled by more reading:

- **The loop does not close inside the map.** No work at any rung below the source closes it, and a
  design that closed it by feeding the motor command back as its own consequence would run and would
  be wrong.
- **Whether a unit has compartments**, without which the layer-1 matrix line arrives at a tuft and
  cannot reach the soma it belongs to. **Micky's**, and the same question this rung raised at piriform
  cortex.
- **The map is self-organising and highly plastic and no learning rule exists for it.** The one
  structure in the map that can be allocated sub-element by sub-element is also the one whose extent
  is stated to move with experience — **so the section's best-specified structure and its least
  runnable one are the same structure.**

**All three are Micky's or the source's, all three are asked out loud rather than parked, and nothing
below this rung is built on a guess at any of them.**
