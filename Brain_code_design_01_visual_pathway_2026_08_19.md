# Brain code design — 01 visual pathway

**Date:** 2026-08-19
**Derived from:** `Brain_architecture_01_visual_pathway`, `Brain_code_design_spec`,
and CLAUDE.md. **No other content source.**
**Implements:** `Brain_01_visual_pathway.py`.

**This file carries no history.** No versions, no provenance, no "changed since," no reference to
sessions or prior files, no changelog, no "formerly." A file that carries its own past gives a reader
two truths and no way to tell which is live.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
character for character, so that at coding time only this file is loaded. **One deviation from that
copy, and it is declared here so that anything else is a defect.** The architecture's **internal
cross-references** — *see Justification*, *see below*, *see that entry's output line below*
— are not copied, because they point at fields this rung does not have. Their content is carried, at
the entry it belongs to.

**Eight entries, one per architecture entry, same names, same order.**

---

## What is open for every entry in this file, stated once

Repeating these eight times would make the file longer without making it truer. Each entry names only
what is open **beyond** this list.

- **Emission — graded or binary, and the unit's expressiveness.** This is the centre–surround /
  threshold-gate question and it is **Micky's**. The architecture's sizing model charges each neuron
  `log₂(fan-in)` bits, which is what a threshold over equal-weight inputs would store — *(that reading
  is Claude's inference from the Sizing fields, constrained by them and not stated in them)*. Until
  Micky sets it, **no entry below writes an update equation as though the answer were given.** Every
  Update equation field says what it is waiting on.
- **The scheduling discipline.** Micky's, and the largest open item at this rung. No entry contains a
  loop, a step counter, or a `for t in range(...)`.
- **The learning rules.** Micky's. Every Adaptation field reads *none set*. A threshold that is never
  written is a construction cost and not a memory, which is why the entries are still coherent.
- **Inter-structure connection topology.** Fan-in is given above as a **scalar per structure**; the
  code needs it as a **map** — which source lines converge on which neuron. A convergence count is not
  a convergence pattern, and no field above carries the pattern. Surface-before-touching.
- **Tile geometry and sparsity.** Both surface-before-touching, both unset, and every array extent
  below is therefore symbolic.
- **Every edge latency in this section reads *to derive*.** The architecture states this positively:
  this file records no conduction time, no synaptic delay and no loop latency. One qualitative timing
  fact exists and is internal, not an edge: the lagged relay-cell class of the lateral geniculate
  nucleus is delayed by triadic inhibition.
- **Edge storage cannot be closed anywhere in this file.**
  `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`. Latency is *to
  derive* on every edge here, the update interval waits on the scheduling discipline, and bytes per
  value waits on the emission question. Each entry records its **edge count** and its **line count
  status**, which is the term this rung can supply. **Never summed with parameter memory or state.**

**Counting basis is not uniform in this section.** Per eye at the retina and optic nerve, both eyes
combined for the chiasm's through-traffic, per hemisphere from the lateral geniculate nucleus onward.
The chiasm is where the basis changes.

**Cross-file endpoints carry the far file's stem.** Nine far files are reached from this section:
`02_auditory_pathway`, `04_dorsal_visual_parietal_stream`, `06_posterior_parietal`,
`07_anterior_temporal_lobe`, `08_medial_temporal_lobe`, `09_basal_ganglia`, `11_frontal_lobe`,
`12_thalamus`, `14_brainstem_midbrain_hypothalamus`.

---

# 1. Retina

## Contract

**Inputs.**
- **light (the world)** → the photoreceptor sheet. Not a neural edge. Fan-in: not applicable.

**Outputs.** All four leave as ganglion-cell axons in the optic nerve.
- **→ optic chiasm** (thence the lateral geniculate nucleus) — the image-forming line, ~80/10/8–10%
  of the ganglion population across three channel classes: midget/parvocellular (~80%, red–green
  cone-opponent, sustained, fine detail), parasol/magnocellular (~10%, achromatic, transient, coarse),
  bistratified/koniocellular (~8–10%, blue–yellow cone-opponent). Fan-out: to derive.
- **→ superior colliculus, superficial layers** (`14_brainstem_midbrain_hypothalamus`; the consumer
  names the lamina precisely, as **stratum griseum superficiale**, the upper superficial grey) — not
  more than 10% of ganglion cells, about 6% near the fovea and rising with eccentricity, and largely a
  **branch off the geniculate line** rather than an independent population. Fan-out: to derive.
- **→ olivary pretectal nucleus** — from broad-field melanopsin-containing luminance detectors. **The
  nucleus has no entry in any file, and its own consumer is declared.**
  `14_brainstem_midbrain_hypothalamus` declares the superior colliculus receiving
  `← olivary pretectal nucleus → stratum griseum intermediale`, a luminance scalar arriving in the
  **premotor rather than the visual** layers. **So the two-hop route from here to the colliculus is
  declared at both ends with no entry for the stage between them** — and that stage is where the
  transform would live, since a broad-field luminance detector's output is not the same object as a
  scalar delivered to premotor layers. Inherited; the entry is owed at the source. Fan-out: to derive.
- **→ suprachiasmatic nucleus** (`14_brainstem_midbrain_hypothalamus`, a sub-element of its
  hypothalamus entry, and **the only structure in that whole section with a neuron count** — ~50,000
  per side) — from melanopsin ganglion cells. Fan-out: to derive.
  **This end declares the cell class and no payload; the consumer types it fully** — an **irradiance,
  "lights-on" signal**, ambient luminance for clock entrainment, arriving by the
  **retinohypothalamic tract**, and **explicitly not spatial vision.** That last clause is the
  load-bearing one and it is absent here: **every other output of this entry is spatial, and nothing
  at this end marks this one as different in kind.** A consumer reading only this end would allocate
  a retinotopic map for a scalar. **Owed at this section's source: the payload and the tract name.**

**Sizing.** Basis: **per eye.**
- Ganglion cells ~1.0–1.2M; fan-in to derive, bounded ≤ 16 bits → **≤ 2.40 MB** at 1.2M.
- Photoreceptors ~97M measured (~126M textbook): **zero.** A photoreceptor is a transducer, stores no
  threshold, and the log₂ cost does not apply.
- Horizontal, bipolar and amacrine cells: **counts to derive** — the source records none. Their store
  cannot be stated, and it is not zero by default.
- **Structure total: to derive**, with ≤ 2.40 MB firm and three of five cell classes uncounted.

**Shape.** **Sheet**, rank 3: **(sub-element, H, W)**, sub-elements photoreceptors / horizontal /
bipolar / amacrine / ganglion, H × W the retinal sampling grid. **The grid is not uniform** — peak
foveal cone density is ~199,000 cones/mm² falling steeply with eccentricity (~32,200 / ~19,300 /
~11,600 per mm² at 0.5 / 1.0 / 1.5 mm out), so this is a **space-variant sampling lattice** and not a
raster. H and W: **to derive** — no retinal surface area is recorded. The eccentricity function is the
correspondence rule the ganglion output edge needs.

**Edge latency.** All four output edges: **to derive.**

## Representation — declared once per line, inherited by every consumer

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| light → photoreceptor sheet | photon flux (radiometric) | to derive | **event-driven** — an optical arrival, and the sheet has no sampling rate of its own recorded | retinal image plane, space-variant |
| → optic chiasm (3 channel classes) | to derive | to derive | event-driven | retinotopic, space-variant lattice |
| → superior colliculus, superficial | to derive | to derive | event-driven | retinotopic |
| → olivary pretectal nucleus | to derive | to derive | event-driven | broad-field; **not retinotopic** — the producer is a broad-field detector |
| → suprachiasmatic nucleus | irradiance | to derive | event-driven | **none — this is a scalar, explicitly not spatial vision** |

**The last row is the load-bearing one and it is why this field exists.** Every other output of this
structure is spatial. A consumer reading only the edge line would allocate a retinotopic map for a
scalar. The typing comes from the consumer, and the architecture records that it is **owed at this
section's source** at this end.

## Algorithm

- **Transform.** Four distinct operations, and **only the third has a standard name licensed from
  above**:
  1. **Phototransduction** — physical stimulus to neural signal, at the photoreceptors. A
     **transducer**, per spec §5a: not a threshold gate, stores no threshold, and its input edge is not
     a projection. **What it computes is not specified at any rung above.** Recorded as a finding, not
     invented here.
  2. **Antagonistic surround formation in space**, by the horizontal cells in the outer plexiform
     layer; **transient response formation in time**, by the amacrine cells in the inner. The two
     lateral populations act on different axes. Both are **graded, non-spiking elements** per §5a.
     **No standard operation is named above for either, and this is a finding about the structure.**
     A centre–surround difference-of-fields is the obvious candidate and **it is not written here**,
     because the centre–surround question is on §10's list and is Micky's.
  3. **ON/OFF channel splitting.** That is the whole of what the rung above says about it, and it is
     a name rather than an operation. **A gap, and it is not this rung's to fill.** The mechanism —
     which synapse, and by what — is in this section's source and did not survive into the
     architecture entry, so the design cannot carry it without skipping a rung. **Repaired at the
     architecture rung**, by restoring the mechanism into its Function field; recorded here because a
     gap that is neither patched nor recorded reads on the next pass exactly like a subject with
     nothing to say about it.
  4. **Cone-opponent colour processing**, complete at the ganglion-cell output: three cone classes read
     out by three ganglion classes, opponency already formed. **The architecture gives channel
     fractions and no equations.** No opponency arithmetic is written here.
- **Sign is inverted at the front of this structure and an update equation must carry it.**
  Photoreceptors **hyperpolarise to light** and release more transmitter in the dark, and because these
  cells do not spike, hyperpolarising is not inhibiting: **hyperpolarisation is the excitatory
  response.** An equation reading depolarisation as activation has the stage exactly backwards. This is
  a constraint on the arithmetic, not on the structure.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `photoreceptor_state` | (H, W) | open — emission question | to derive | to derive |
  | `horizontal_state` | (H, W) | open | to derive | to derive |
  | `bipolar_state` | (H, W) | open | to derive | to derive |
  | `amacrine_state` | (H, W) | open | to derive | to derive |
  | `ganglion_active` | (H, W) | open | to derive | to derive |
  | `ganglion_threshold` | (H, W) | width `ceil(log₂(fan_in))`, fan_in to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **H and W are to derive** and are not a raster: the sampling lattice is space-variant, and the
  eccentricity function above is the correspondence rule. **Allocating a uniform H × W grid would
  assert a raster the structure does not have.**
  **Only `ganglion_threshold` has a licensed width.** The other four sub-elements are transducers or
  graded elements; §5a forbids defaulting their store to zero or to `log₂(fan-in)`.
- **Parameters.** `ganglion_fan_in` — **to derive**, bounded ≤ 16 bits, origin: the architecture's
  Sizing field. No other parameter has a value or an origin above.
- **Update equation.** **Waiting on the emission question (§10).** What is fixed regardless of the
  answer: the sign inversion at the photoreceptor, and that colour is complete at the ganglion output
  so nothing downstream recomputes it.
- **State carried between updates.** The five arrays above, all of them. The horizontal-cell feedback
  onto surrounding photoreceptors is a **loop inside the first synaptic layer** and cannot be staged,
  so photoreceptor state is read after horizontal state is written within one update — **the ordering
  is fixed by that loop and not by a clock.** Initial values: to derive.
- **Edge storage.** 4 output edges, 1 input edge. Line count = ganglion count × fan-out, both terms to
  derive. Latency to derive on all four. Interval unset. **Not summable.**
- **Adaptation.** **None set.** `ganglion_threshold` is a read-only construction constant.
- **Open, beyond the standing list.** The ON/OFF mechanism, dropped between the source and the
  architecture and **owed at the architecture rung**; what a transducer computes; what a graded
  non-spiking element stores; the counts of horizontal, bipolar and amacrine cells; the retinal surface area, and with it H
  and W; the payload and tract name on the suprachiasmatic edge, owed at the source; the olivary
  pretectal nucleus, which has no entry anywhere.

---

# 2. Optic chiasm

## Contract

**Inputs.**
- **← retina**, both eyes — the full three-class ganglion bus, one per eye, still monocular and still
  whole-hemifield. Fan-in: **none (no synapse here).**

**Outputs.**
- **→ lateral geniculate nucleus of each hemisphere** — the same content, unchanged. What changes is
  which fibres go where: each optic tract now carries the **contralateral hemifield of both eyes**
  rather than one whole eye. Fan-out: **none (no synapse here).**

**Sizing.** **Zero.** Neurons: none — a fibre tract, not a nucleus. No neurons, no thresholds, no
parameter memory. Basis: through-traffic ~2M fibres, **both eyes combined**, of which about 5% are
bound for structures other than the two geniculate nuclei.

**Shape.** **Transmission-only: not an activity array.** No neurons, no thresholds, no state. Its shape
is a **routing index**, rank 1, length ~2M fibres both eyes combined, mapping each line to a
destination side by the nasal/temporal boundary. Recording it as a zero-length tensor would assert
state it does not hold.

**Edge latency.** **To derive**, and this is the structure where a derivation would start: the tract is
myelinated and its g-ratio is unrecorded, so the substrate of the delay is named and the number is not.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← retina, both eyes | inherited from the retina's ganglion output, unchanged | unchanged | event-driven | monocular retinotopic, whole hemifield, one frame per eye |
| → lateral geniculate nucleus, each side | **identical to the input** — no synapse, no transform | unchanged | event-driven | **hemifield-of-both-eyes, per side** — the frame changes here and the content does not |

**The frame change is the whole of what this structure does**, and it is the only row in this file
where a representation changes without a transform.

## Algorithm

- **Transform.** **A routing statement, and nothing else.** Per spec §5a this is a
  **transmission-only** structure: no synapse, no computation, no update equation, **no state.**
  Fibres sort so that each hemisphere receives the contralateral visual hemifield. The sorting rule is
  a line — the **line of decussation**, normally aligned with the fovea, and a **developmental
  variable rather than a structural given**. Two sub-structures, and they are **parallel channels
  rather than a circuit**: the crossed bundle from ganglion cells nasal to the fovea, the uncrossed
  bundle from cells temporal to it.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `routing_index` | (~2M,) rank 1 | integer, destination side | {crossed, uncrossed} | — |

  **This is the only array**, and it is an index, not activity. **Writing a zero-length activity array
  here asserts state the structure does not hold**, which is the specific error §5a names.
- **Parameters.** The **line of decussation** — the nasal/temporal boundary that fixes each fibre's
  destination. **Origin: developmental, and a variable rather than a given.** No value above. The
  crossed:uncrossed ratio it produces is **~53:47** in the neurotypical human, which is a consequence
  of the boundary sitting at the fovea and of the nasal retina being the larger sector.
- **Update equation.** **None, and this is not an omission.** A structure with no synapse has nothing
  to update.
- **State carried between updates.** **None.**
- **Edge storage.** 1 input edge, 1 output edge, ~2M lines in flight both eyes combined. Latency to
  derive; the **substrate is named** — a myelinated tract with an unrecorded g-ratio — which is more
  than any other edge in this file has. **This entry is load-bearing for exactly that reason: a tract
  is where the physical substrate of a latency lives**, and a derived conduction time is derived from
  it. Interval unset.
- **Adaptation.** **None**, and here it is a positive statement rather than an unset one: there is no
  stored parameter to change. The line of decussation is developmental, not learned.
- **Open, beyond the standing list.** The g-ratio, without which the one derivable latency in this file
  stays underived. The ~5% of through-traffic bound for structures other than the two geniculate
  nuclei — this entry declares one output and the retina declares four, so **three of the retina's
  outputs pass through a stage that does not declare them.**

---

# 3. Lateral geniculate nucleus

## Contract

**Inputs.**
- **← retina**, via the chiasm and optic tract — the three ganglion channel classes, mapping
  one-to-one onto the three layer classes: parvocellular layers 3–6 ← midget, koniocellular sublayers ←
  bistratified, magnocellular layers 1–2 ← parasol. **~5–10% of this nucleus's synapses**, and the only
  driver. Fan-in: to derive (classically one to a few retinal afferents per relay cell; no human
  figure).
- **← V1, sublayer 6a** — corticothalamic feedback, **~30% of synapses**, the largest single
  non-retinal source. Fan-in: to derive.
- **← thalamic reticular nucleus** (`12_thalamus`) — inhibition, a gain and gate control. Fan-in: to
  derive. The producer declares `→ lateral geniculate nucleus — inhibition`, **the gate**, and names
  the visual sector of that sheet explicitly. Both ends agree the payload is inhibition and **carries
  no content**.
- **← brainstem**, cholinergic / noradrenergic / serotonergic — arousal state, which sets the relay
  cells' burst-versus-tonic mode. Fan-in: to derive.

**Outputs.** The projection to V1 is **four edges, not one**, and only two reach layer 4.
- **→ V1 4Cα**, from magnocellular layers 1–2, via the optic radiation — achromatic, retinotopic,
  point-to-point, still monocular. Fan-out: to derive.
- **→ V1 4Cβ**, from parvocellular layers 3–6 — red–green, retinotopic, point-to-point, monocular.
  Fan-out: to derive.
- **→ V1, the cytochrome-oxidase blobs of layers 2/3 and layer 1**, from the koniocellular sublayers —
  blue–yellow, retinotopic, monocular. **This edge does not terminate in layer 4 at all.** Fan-out: to
  derive.
- **→ V1 4A**, parvocellular and koniocellular collaterals. Fan-out: to derive.
- **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), direct, **bypassing V1 entirely** —
  payload **owed**; mostly koniocellular cells, sending virtually no collateral to V1, numbering about
  10% of the V1 population that innervates that area. Fan-out: to derive. The consumer marks this
  payload *owed* as well, and adds that the edge is sufficient to support motion sensitivity without
  V1 — **so the two ends agree, and they agree that neither can type it.** That is the honest state and
  not a defect at either end.
- **→ thalamic reticular nucleus** (`12_thalamus`), collaterals of the thalamocortical axons — a copy
  of the outgoing signal, which drives the gate that regulates it. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere (per side).** ~1.77M neurons (magnocellular ~0.22M, parvocellular
~1.55M); fan-in to derive, bounded ≤ 16 bits → **≤ 3.54 MB.** Synapse proportions are known (retinal
~5–10%, cortical ~30%, remainder reticular and brainstem) and the absolute count is not, which is
exactly the case the log₂ bound is for.

**Shape.** **Laminated nucleus**, rank 3: **(lamina, H, W)** — six laminae plus a koniocellular
sublayer ventral to each, every lamina a retinotopic map and every lamina monocular. **This is the one
structure in this section whose count partitions to its sub-elements**, and it closes: magnocellular
~0.22M over laminae 1–2 is **~110,000 per lamina**; parvocellular ~1.55M over 3–6 is **~387,500 per
lamina**; the two sum to ~1.77M against the headline exactly. Volumetric density ~104 mm³ over ~1.77M
is **~17,019 neurons/mm³**. H and W: **to derive** — no retinotopic pitch is recorded. **The eye
assignment per lamina is owed**, so the lamina axis is ordered and not yet labelled.

**Edge latency.** All edges **to derive.** One internal timing fact is recorded and is not an edge
latency: the lagged relay-cell class is delayed by triadic inhibition.

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← retina (3 classes) | inherited from the retina's ganglion output | unchanged | event-driven | retinotopic, monocular, per side |
| ← V1 6a | to derive | to derive | event-driven | retinotopic, in register with the relay it gates |
| ← thalamic reticular nucleus | **inhibition — carries no content** | to derive | event-driven | visual sector of the reticular sheet |
| ← brainstem (ACh / NA / 5-HT) | **arousal state — a mode, not a message** | to derive | event-driven | **none — not a mapped signal** |
| → V1 4Cα | achromatic | to derive | event-driven | retinotopic, point-to-point, monocular |
| → V1 4Cβ | red–green | to derive | event-driven | retinotopic, point-to-point, monocular |
| → V1 blobs 2/3 and layer 1 | blue–yellow | to derive | event-driven | retinotopic, monocular |
| → V1 4A | parvo + konio collateral | to derive | event-driven | retinotopic, monocular |
| → middle temporal area (`04_...`) | **owed at both ends** | to derive | event-driven | to derive |
| → thalamic reticular nucleus (`12_thalamus`) | a copy of the outgoing signal | unchanged from the output it copies | event-driven | retinotopic |

**Two input rows carry no content and this is the field's whole point.** Reticular inhibition and
brainstem arousal both change the transfer function rather than the message. A consumer that reads them
as content is reading a gain as data.

## Algorithm

- **Transform.** **A gate, not a wire.** The mechanism is a **change of transfer function rather than
  of message**: relay cells fire in **burst mode** (hyperpolarised, high-gain, nonlinear) or **tonic
  mode** (depolarised, near-linear), and the modulatory inputs move them between the two. The retina is
  the sole **driver** and a small minority of the synapses; the larger non-retinal input is
  **modulatory** and sets whether, when and how strongly the retinal message passes, **adding no
  content.**
  **No standard operation is named above for the burst/tonic switch**, and one is not invented here.
  Its selector is the arousal line; its effect is on gain and linearity, not on the payload.
- **Two cell classes in fixed ratio**, and they are not one population: **relay cells ~75–80%**,
  **local interneurons ~20–25%.** The interneuron **releases transmitter from dendrites without an
  action potential** and is therefore a **graded, non-spiking element** under §5a — **its store must
  not default to zero or to `log₂(fan-in)`.** The architecture's ~1.77M count and ≤ 3.54 MB bound do
  not distinguish the two classes, so the bound covers a population of which a fifth to a quarter is
  **not a threshold gate.**
- **A lagged relay-cell subpopulation exists and is delayed by triadic inhibition.** This is the only
  timing datum in the file and it is **internal** — a difference between two populations of one
  structure, not a property of an inter-structure edge. **An implementation that treats all relay cells
  as one timing class deletes it.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `relay_active` | (lamina=6 + 6 konio sublayers, H, W) | open — emission question | to derive | to derive |
  | `relay_threshold` | same | width `ceil(log₂(fan_in))`, fan_in to derive, bounded 16 | 0 … fan_in | count of active inputs |
  | `relay_mode` | same | open — a two-state selector, burst or tonic | {burst, tonic} | — |
  | `interneuron_state` | to derive | **open, and not defaultable** — graded, non-spiking | to derive | to derive |

  **The lamina axis is ordered and not labelled**, because the eye assignment per lamina is owed. **An
  implementation that labels it invents the assignment.** H and W to derive; no retinotopic pitch is
  recorded.
- **Parameters.** `relay_fan_in` — to derive, bounded ≤ 16 bits, origin: the Sizing field.
  Class proportions, origin: the architecture's Function field — relay ~75–80%, interneuron ~20–25%;
  magnocellular ~0.22M over laminae 1–2, parvocellular ~1.55M over 3–6.
- **Update equation.** **Waiting on the emission question (§10)**, and on a second thing this entry
  raises alone: **how a two-mode transfer function is expressed at all.** Burst and tonic are not two
  values of a gain term; they differ in linearity. Nothing above names an operation for it.
- **State carried between updates.** `relay_active`, `relay_mode`, `interneuron_state`. `relay_mode` is
  written by the arousal line and read by the relay update, so **it is written before the relay it
  governs within one update** — an ordering fixed by the gate relation, not by a clock. Initial values:
  to derive.
- **Edge storage.** 4 input edges, 6 output edges. Line count = per-lamina counts (which **do**
  partition here, uniquely in this file) × fan-out, fan-out to derive. Latency to derive on all ten.
  Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** What the interneuron stores; how burst/tonic is expressed; the
  eye assignment per lamina; the retinotopic pitch, and with it H and W; the payload on the direct
  middle-temporal edge, owed at both ends; the brainstem class endpoint, which names no structure.

---

# 4. V1 — primary visual cortex

## Contract

**Inputs.**
- **← lateral geniculate nucleus, magnocellular layers 1–2 → 4Cα.** Fan-in: to derive.
- **← lateral geniculate nucleus, parvocellular layers 3–6 → 4Cβ.** Fan-in: to derive.
- **← lateral geniculate nucleus, koniocellular sublayers → the cytochrome-oxidase blobs of layers 2/3,
  and layer 1.** Fan-in: to derive.
- **← lateral geniculate nucleus, parvocellular and koniocellular collaterals → 4A.** Fan-in: to
  derive.
- Together the geniculate edges are a **minority** of V1's excitatory synapses; most is intracortical.
  None of them carries orientation, disparity or spatial-frequency tuning — **all three are built
  here.**
- **← V2, V3, V4 and the middle temporal area** (the last in `04_dorsal_visual_parietal_stream`)
  (feedback), principally → **layer 1**, also layers 2, 5 and 6, **avoiding layer 4**, which is what
  distinguishes a feedback edge at the receiving end. On layer 1 it terminates on apical tufts
  belonging to cells housed in layers 2/3 and 5. Fan-in: to derive.
  **This is a four-source class line and the arity is the defect.** The middle temporal area's own
  entry declares its limb of it separately and types it — contextual and attentional modulation,
  figure–ground and border-ownership context, attentional gain, **not a new stimulus code** — and
  records at its end that **which of the four contributes which part of the payload is owed.**
  **Splitting this into four named edges is owed at this section's source**, and until it is split the
  three intra-section limbs remain untyped while the cross-file one is typed at the far end only.
- **← posterior inferotemporal cortex, anterior inferotemporal cortex, temporal areas TF and TH,
  occipitotemporal and superior temporal sulcal cortex, caudal intraparietal cortex** (long-range
  feedback) — cortical afferents to V1 are not confined to the prestriate areas. Fan-in: to derive.

**Outputs.** The forward output to V2 is segregated by content; the number of streams is contested
(three, two, or four groupings in the literature), so the edges are stated by **target stripe class**,
the axis all three groupings agree on.
- **→ V2 thin stripes**, predominantly from the cytochrome-oxidase blobs of layers 2/3 (~81% of
  labelled source cells in patches). Fan-out: to derive.
- **→ V2 pale stripes** — the richest of the three; composition layers 2/3 87%, 4B 10%, 4A 2%, layers
  5/6 2%. Fan-out: to derive.
- **→ V2 thick stripes** — composition layers 2/3 67%, 4B 23%, 4A 7%, layers 5/6 2%. **4B is the
  minority contributor here**, which the simple account inverts. Fan-out: to derive.
- **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), from **4B, predominantly its
  spiny-stellate class** (~76% spiny stellate against ~24% pyramidal — the reverse of the
  V2-projecting population, and largely separate cells, under ~5% double-labelled). Fan-out: to derive.
  **This end declares no payload and no termination layer, and the consumer declares both** —
  direction of motion and binocular disparity, achromatic, coarse-spatial, onto layer 4, on the fast
  few-hop route. **The producer's end is the deficient one and the repair is owed at this section's
  source.** The consumer also carries a claim about this edge that this end does not: that 4B's spiny
  stellates take magnocellular input only, direct from 4Cα, while its pyramids take both and project to
  V2 instead — **making the direct route magnocellular and the V2 route mixed.** Whether this section's
  source licenses that is unchecked here.
- **→ V3**, from **4B** — a major input. Fan-out: to derive.
- **→ V4**, direct — sparse, restricted to roughly the central 6°. Fan-out: to derive.
- **→ V2, from 4A**, and **→ V2, from layers 5/6** — minor components the three-stream account omits.
  Fan-out: to derive.
- **→ lateral geniculate nucleus**, from **6a** — the modulatory gate on the relay feeding V1. Fan-out:
  to derive.
- **→ higher-order thalamus** (`12_thalamus`), from **6b** — reaching higher-order nuclei but **not**
  the reticular nucleus. Fan-out: to derive.
- **→ superior colliculus** (`14_brainstem_midbrain_hypothalamus`)**, from 5b** — retinotopic salience
  for orienting. Fan-out: to derive. The consumer adds the termination, **the superficial layers**,
  which this end does not name. **And the contest recorded at the retina entry turns on this edge**: if
  the colliculus's visual drive arrives through the geniculate and V1, then this is the edge carrying
  it, and the retinotectal one is not.
- **→ lower visual areas** (descending), from **layer 2** — a supragranular feedback stream distinct
  from the classical infragranular one, so layers 2 and 3 are not interchangeable as origins. Fan-out:
  to derive.

**Sizing.** Basis: **per hemisphere.** ~280–310M neurons (density × confirmed volume; ~140M retained as
a lower bound). Fan-in is the one place in this section where the source bounds it rather than leaving
it open, and it is **disputed across a 6.5× range** — 2,300–5,600 measured in macaque V1, ~7,000 as a
human cortical average, ~15,000 derived from human synapse and neuron densities. **Under log₂ that
range costs 12 to 14 bits**, so:
- at 12 bits: **450 MB**; at 13 bits: **487.5 MB**; at 14 bits: **525 MB** (at 300M neurons).
- At the ~140M lower bound: **210 / 227.5 / 245 MB**.
- **The neuron count, not the synapse dispute, is what the figure turns on** — a 2.1× spread in count
  against a 1.17× spread from a 6.5× spread in fan-in.

**Shape.** **Sheet**, rank 3: **(sub-element, H, W)**, eleven laminar sub-elements — 1, 2, 3, 4A, 4B,
4Cα, 4Cβ, 5a, 5b, 6a, 6b — over a tangential grid.
**Surface density is derivable and the pitch is not.** ~60,000 neurons/mm³ over ~2 mm thickness is
**~120,000 neurons per mm² of surface**; ~2,600 mm² of surface × 120,000 = **312M**, which closes
independently against the ~280–310M headline.
**H × W = to derive**, because V1's own tangential pitch is not recorded — the cytochrome-oxidase blobs
are named with no spacing given. Once a pitch arrives the whole shape follows: at 1 mm it is 2,600
tiles of ~120,000 neurons and ~210 kB each; at 0.5 mm, 10,400 tiles of ~30,000 and ~52.5 kB.
**The eleven-way partition of the neuron count is also to derive**, so the sub-element axis is named
and not yet sized — and four separate geniculate edges terminate on four of those sub-elements.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← LGN magno → 4Cα | achromatic | to derive | event-driven | retinotopic, monocular |
| ← LGN parvo → 4Cβ | red–green | to derive | event-driven | retinotopic, monocular |
| ← LGN konio → blobs 2/3, layer 1 | blue–yellow | to derive | event-driven | retinotopic, monocular |
| ← LGN collaterals → 4A | parvo + konio | to derive | event-driven | retinotopic, monocular |
| ← V2/V3/V4/MT feedback → layer 1 | **contextual and attentional modulation — not a new stimulus code** (typed at the MT end only) | to derive | event-driven | retinotopic, in register |
| ← long-range temporal and parietal feedback → layer 1 | to derive | to derive | event-driven | to derive |
| → V2 thin stripes | cortical colour, single- and double-opponent | to derive | event-driven | retinotopic, **binocular from here on** |
| → V2 pale stripes | oriented edge, contour, spatial frequency | to derive | event-driven | retinotopic, binocular |
| → V2 thick stripes | to derive | to derive | event-driven | retinotopic, binocular |
| → V2 from 4A; → V2 from layers 5/6 | to derive | to derive | event-driven | retinotopic, binocular |
| → middle temporal area (`04_...`) | **owed here; the consumer types it** — direction of motion, binocular disparity, achromatic, coarse-spatial | to derive | event-driven | retinotopic |
| → V3 from 4B | motion direction and disparity, achromatic | to derive | event-driven | retinotopic |
| → V4 direct | to derive | to derive | event-driven | retinotopic, **central ~6° only** |
| → LGN from 6a | **modulatory — carries no content** | to derive | event-driven | retinotopic, in register with the relay |
| → higher-order thalamus (`12_thalamus`) from 6b | to derive | to derive | event-driven | to derive |
| → superior colliculus (`14_...`) from 5b | **retinotopic salience** — for orienting, not a stimulus code | to derive | event-driven | retinotopic |
| → lower visual areas from layer 2 | to derive | to derive | event-driven | retinotopic |

**Eye of origin is consumed here and does not appear on any output row.** Every input row above is
monocular and every output row is binocular. **That transition has no array and no equation above it**,
and it is the one representational change in this entry that the contract states in prose only.

## Algorithm

- **Transform.** Four operations are named, and **the fourth is the one with a licensed standard
  name**:
  1. **Binocular convergence** — the eyes first combine here. **No operation is named above**, and this
     is a finding: the contract states the fact and not the arithmetic.
  2. **Orientation and spatial-frequency selectivity**, built here and **carried by none of the four
     geniculate inputs**. A two-dimensional oriented bandpass response is the obvious candidate and
     **it is not written here** — the architecture gives no filter, no bank, and no kernel, and an
     invented one is the added-edge defect class.
  3. **The first cortical transformation of the cone-opponent signal** — single-opponent cells
     (spatially low-pass) and double-opponent cells (chromatically and spatially opponent, the proposed
     substrate for downstream colour constancy). **The architecture gives channel fractions and no
     equations.** No opponency arithmetic is written here.
  4. **Retinotopic mapping** — a precise map of the visual field, which is a **correspondence rule and
     not a computation**, and it is the same object `fan_in(j)` needs.
- **Eleven laminar sub-elements, against the eight of general cortex.** Layer 4's sublamination is
  V1's alone and merges to a single layer 4 at V2. **Colour-preferring cells concentrate in the
  cytochrome-oxidase blobs of layers 2/3, one opponency type per blob.**
- **4B is two cell classes projecting to different targets**, and they are largely separate cells
  (under ~5% double-labelled): spiny stellates ~76% to the middle temporal area, pyramids ~24% to V2.
  **A single 4B array with one output edge deletes that split.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (sub_element=11, H, W) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))` = **12–14 bits, disputed** | 0 … fan_in | count of active inputs |

  **`threshold` cannot be allocated per sub-element.** The Shape field names eleven sub-elements and
  the Sizing field carries one count for all of them; **the eleven-way partition is to derive.** Four
  geniculate edges terminate on 4Cα, 4Cβ, the blobs of 2/3, and 4A, so **four edges land on
  sub-elements whose extent is unknown.** This is the granularity mismatch, and it blocks allocation
  rather than description.
  **A realisation note this rung owns, because this is where a container is chosen.** The derived width
  is 12 to 14 bits and **no machine integer type is 12 or 14 bits wide.** In `uint16` the array
  realises at 600 MB against 450 MB derived at 12 bits (a 33.3% gap) and 525 MB at 14 bits (14.3%).
  Bit-packing closes the gap and costs unpacking on every read. **This does not license reducing
  anything** — memory is a derived requirement and never a limit to design against.
- **Parameters.** `fan_in` — **12–14 bits under log₂, from a disputed 6.5× range**; origin: the Sizing
  field, which bounds it here and nowhere else in this section. **Choosing a single value within the
  range is a choice, and it is not made here**; the entry carries the range. Surface density ~120,000
  neurons per mm² of surface, origin: derived in the Shape field and closing independently against the
  headline count.
- **Update equation.** **Waiting on the emission question (§10).**
- **State carried between updates.** `active`, at (11, H, W). **V1 sits inside four closed loops all
  present in this section** — with the lateral geniculate nucleus by way of 6a, and with V2, V3, V4 and
  the middle temporal area by way of their layer-1 feedback. **A staged bring-up would leave all four
  open, and an open loop is not a loop.** Initial values: to derive.
- **Edge storage.** 6 input edges, 11 output edges — the largest edge count in this file. Line count =
  per-sub-element counts × fan-out, and **the per-sub-element counts do not exist**. Latency to derive
  on all seventeen. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The eleven-way partition of the neuron count; the tangential
  pitch, and with it H and W; the four-source feedback class line's arity, owed at the source; the
  payload and termination layer on the middle-temporal edge, owed at the source; whether the source
  licenses the spiny-stellate/pyramid claim the consumer carries; the *lower visual areas* class
  endpoint; how binocular convergence is expressed.

---

# 5. V2 — secondary visual cortex

## Contract

**Inputs.**
- **← V1, cytochrome-oxidase blobs of layers 2/3 → thin stripes** — the cortical colour signal. Fan-in:
  to derive.
- **← V1, interblob layers 2/3 with a 4B component → pale stripes.** Fan-in: to derive.
- **← V1, layers 2/3 and 4B → thick stripes.** Fan-in: to derive.
- **← V1, 4A and layers 5/6 → pale and thick stripes** — minor components. Fan-in: to derive.
- **← auditory parabelt, caudal division** (`02_auditory_pathway`) — an auditory association area
  writing into secondary visual cortex. Which tangential compartment it reaches is unrecorded, and the
  answer would matter: thick stripes are the motion and disparity channel. Fan-in: to derive.
  The producer declares this edge only **inside a class line** — its caudally-directed stream, naming
  the temporoparietal junction, posterior parietal and occipital regions *including secondary visual
  cortex*, caudal and dorsal prefrontal cortex, dorsal cingulate and parahippocampal areas as one edge.
  **That producer carries an arity note saying such a split would name far ends that mostly have no
  matching declaration; this limb is one of the exceptions**, since this entry declares it, so the limb
  can be split out even though the rest of the line cannot.
  **On the compartment:** the producer types the caudal division's payload as **location and motion**,
  and this entry records that **thick stripes are the motion and disparity channel.** **So thick
  stripes are the candidate, on the two payloads together, and neither end states it.** Recorded as a
  candidate because neither end constrains it alone. **Owed at both sources.**
- **← V4, middle temporal area and higher areas** (the second in `04_dorsal_visual_parietal_stream`)
  (feedback), principally → layer 1, avoiding layer 4. Fan-in: to derive. The middle temporal limb is
  declared at its producer too and reads **owed at both ends** there — **so this is an edge both ends
  agree is untyped**, not one end's omission. The class line's arity is still owed at this section's
  source.

**Outputs.** Forward edges leave from layers 2/3 of the named stripe class.
- **→ V4**, from layers 2/3 of the **thin and pale** stripes. Fan-out: to derive.
- **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), from layers 2/3 of the **thick**
  stripes, onto **layer 4**. Fan-out: to derive.
  **This end declares no payload; the consumer declares binocular disparity, high-speed sensitivity,
  and the surround suppression underlying motion opponency, achromatic and retinotopic.** The consumer
  further records a **substantive disagreement about direction**, and names this entry as where the
  repair is owed: the source declares this edge as carrying motion direction and disparity, while the
  consumer assigns direction to the **direct V1 4B route** instead, on the strength of reversible
  inactivation — cooling V2 and V3 degrades **disparity** tuning disproportionately relative to
  **direction** tuning. **A causal inactivation result outranks an unqualified connectivity
  statement**, so the payload this edge should carry is disparity-weighted rather than
  direction-weighted.
  **The disagreement is recorded and not resolved here.** Resolving it means changing what the payload
  says, the payload is the source's, and this section's source has not been read against the
  consumer's. **Owed at this section's source.**
- **→ V3 / V3A**, from layers 2/3. Fan-out: to derive.
- **→ posterior inferotemporal cortex**, direct — a **jumping projection that skips V4.** Fan-out: to
  derive.
- **→ V1** (feedback), from layer 2 and the infragranular layers → V1's layer 1. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~200–220M neurons (scaled from V1 at ≈ 0.715 ×: ~0.55× V1's
density over ~1.3× V1's area). Fan-in to derive, bounded ≤ 16 bits → **≤ 420 MB** at 210M. The
ventral-hierarchy shrink is preserved, V2 < V1.

**Shape.** **Sheet**, rank 4: **(lamina, stripe class, H, W)** — the two sub-element axes are
orthogonal, eight laminae against three tangential stripe classes, every stripe class carrying the full
laminar set.
**Two tangential tilings are measured here, and they are the only measured pitches in this section.**
The **stripe cycle** repeats every **3.5–4 mm** centre-to-centre; the **intrinsic columnar patches**
are **211 × 342 µm** ≈ 0.0722 mm², which over V2's ~3,380 mm² (~1.3 × V1's surface) gives **~46,800
patches**. **They are not the same tiling and neither is derivable from the other.**
**A caution the shape must carry:** the stripe class is defined by cytochrome-oxidase staining in layer
3 while the densest input field is in layer 4, and the two do **not** coincide — so the stripe axis is
not in register with the lamina axis, and a slice naming both picks out a place that is not well
defined.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← V1 blobs 2/3 → thin stripes | cortical colour | to derive | event-driven | retinotopic, binocular |
| ← V1 interblob 2/3 + 4B → pale stripes | contour, oriented edge | to derive | event-driven | retinotopic, binocular |
| ← V1 2/3 + 4B → thick stripes | to derive | to derive | event-driven | retinotopic, binocular |
| ← V1 4A and 5/6 → pale, thick | to derive | to derive | event-driven | retinotopic, binocular |
| ← auditory parabelt caudal (`02_...`) | **location and motion** (typed at the producer) | to derive | event-driven | **auditory — not retinotopic**; the frame change is unstated at both ends |
| ← V4/MT/higher feedback → layer 1 | **owed at both ends** | to derive | event-driven | retinotopic |
| → V4 from thin and pale 2/3 | hue, contour, junction, border-ownership, texture | to derive | event-driven | retinotopic |
| → middle temporal area (`04_...`) from thick 2/3 → layer 4 | **contested** — the producer's source says direction and disparity, the consumer says disparity-weighted on causal grounds | to derive | event-driven | retinotopic |
| → V3 / V3A from 2/3 | contour, junction, figure–ground | to derive | event-driven | retinotopic |
| → posterior inferotemporal, direct | to derive | to derive | event-driven | retinotopic, coarsening |
| → V1 feedback → layer 1 | figure–ground and border-ownership context | to derive | event-driven | retinotopic, in register |

**The auditory row is the one cross-modal line in this file and it changes frame without a stated
rule.** A signal in an auditory frame arriving in a retinotopic sheet needs a correspondence, and
neither end supplies one. **Owed at both sources**, and recorded here because this rung is where the
absence stops being describable and starts being unwritable.

## Algorithm

- **Transform.** **First real composition of visual features.** Named: contour integration and
  illusory contour, angle and junction selectivity, border-ownership and figure–ground, naturalistic
  texture (**which V1 cannot distinguish from spectrum-matched noise**), and hue. **No standard
  operation is named above for any of the five**, and none is invented here. That V1 fails on
  spectrum-matched noise while V2 succeeds is a **discriminative constraint on whatever operation is
  eventually written** — it must separate texture statistics from a power spectrum — and it is the only
  such constraint this file supplies for any transform.
- **Two orthogonal sub-structure axes**, and they are not a hierarchy: **tangentially** three
  cytochrome-oxidase stripe classes (thin, pale, thick); **laminarly** eight layers (1, 2, 3, 4, 5a,
  5b, 6a, 6b, layer 4 undivided). **Every stripe class carries the full set of layers and every layer
  runs through all three stripe classes.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, stripe_class=3, H, W) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, fan_in to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **Rank 4, and the two sub-element axes are not in register.** The stripe class is defined by staining
  in **layer 3**; the densest input field is in **layer 4**. So the index pair (lamina=4,
  stripe_class=thin) **names a place that is not well defined**, and an allocation that treats the two
  axes as an orthogonal grid asserts a registration the biology does not have. **This is a defect in
  the addressing scheme and not in the array**, and it is recorded rather than resolved.
  **The 24-way partition (8 laminae × 3 stripes) of ~210M neurons is to derive.**
  **Two measured pitches and neither gives H × W.** The stripe cycle is 3.5–4 mm; the intrinsic
  columnar patches are 211 × 342 µm ≈ 0.0722 mm², giving ~46,800 patches over ~3,380 mm². **Choosing
  either as the tangential grid is a tile-geometry decision and it is surface-before-touching.**
- **Parameters.** `fan_in` — to derive, bounded ≤ 16 bits, origin: the Sizing field. Neuron count
  ~200–220M, origin: **scaled from V1 at ≈ 0.715×** — ~0.55× V1's density over ~1.3× V1's area — which
  makes it a **derived** figure and not a measured one, and the entry carries that.
- **Update equation.** **Waiting on the emission question (§10).**
- **State carried between updates.** `active`, at (8, 3, H, W). V2 is inside the V1 loop and the V4 and
  middle temporal loops, all present in this section. Initial values: to derive.
- **Edge storage.** 6 input edges, 5 output edges. Line count = per-compartment counts × fan-out, and
  the 24-way partition does not exist. Latency to derive on all eleven. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** The 24-way partition; which of the two measured pitches is the
  tangential grid; the stripe/lamina registration defect; which compartment the auditory parabelt edge
  reaches, and the frame correspondence it needs — owed at both sources; the direction-versus-disparity
  contest on the middle-temporal edge, owed at this section's source; the feedback class line's arity.

---

# 6. V3 / V3A — early extrastriate

## Contract

**Inputs.**
- **← V2**, from layers 2/3 — contour, junction, figure–ground. Fan-in: to derive.
- **← V1, 4B** — motion direction and disparity, achromatic; a major input. Fan-in: to derive.
- **← superior colliculus** (`14_brainstem_midbrain_hypothalamus`, relayed through the **pulvinar** in
  `12_thalamus`)**, di-synaptically** — a subcortical route into the motion areas that does not pass
  through V1. Fan-in: to derive.
- **← higher dorsal and parietal areas** (feedback), principally → layer 1. Fan-in: to derive.

**Outputs.**
- **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), direct, onto **layer 4** — dynamic
  form, contour bound to direction of motion. Fan-out: to derive. **The two ends declare this payload
  in the same words and it is the only edge between these two sections of which that is true.** The
  agreement certifies less than it appears to: it is only a check if the two ends were written in
  separate passes, and whether they were is not knowable from either file.
- **→ V4**, and to **the V4 transitional area, the ventral occipitotemporal area, and the visually
  responsive part of temporal area F** — **carries:** contour and dynamic form. **Payload otherwise
  unknown — owed.** Fan-out: to derive. Three of the four endpoints have no entry anywhere; the V4
  transitional area is a V3 target and not the ventral posterior area target.
- **→ V3A, the dorsomedial area, the dorsal prelunate area, the ventral intraparietal area
  (`04_dorsal_visual_parietal_stream`), the ventral lateral intraparietal area** (the ventral
  subdivision of the lateral intraparietal area, same file) — **carries:** dynamic form, and in V3A a
  full contralateral hemifield map. **Payload otherwise unknown — owed.** Fan-out: to derive.
  **A five-endpoint compound line, and the split is owed at this section's source.** Two of the five
  resolve into the dorsal-stream section; V3A is this entry's own other half; **the dorsomedial area
  and the dorsal prelunate area have no entry anywhere**, and they are the source's own extrastriate
  family, inherited and not repairable at this rung.
  **The consumer types its limb** — the ventral intraparietal entry declares this edge as carrying
  dynamic form, contour bound to direction of motion — **so one of the five is typed at the far end
  more fully than the line types it here.**
- **→ V1 / V2** (feedback), → layer 1 of the target. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** Neurons **to derive** — no clean per-area human count, and the
area's boundaries are themselves contested. **No store can be stated for this structure**, and it is
the only one in this section of which that is true.

**Shape.** **Sheet**, rank 3: **(lamina, H, W)**, eight laminae. Neuron count **to derive**, surface
area **to derive**, pitch **to derive**, tangential sub-elements **to derive**. **Every extent on this
structure is open**, which is what it means for a structure to be named and not yet specified.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← V2 from 2/3 | contour, junction, figure–ground | to derive | event-driven | retinotopic |
| ← V1 4B | motion direction and disparity, achromatic | to derive | event-driven | retinotopic |
| ← superior colliculus via pulvinar, di-synaptic | to derive | to derive | event-driven | retinotopic — **and it does not pass through V1**, so it is not in register with the two rows above by construction |
| ← higher dorsal and parietal feedback → layer 1 | to derive | to derive | event-driven | to derive |
| → middle temporal area (`04_...`) → layer 4 | dynamic form, contour bound to direction of motion | to derive | event-driven | retinotopic |
| → V4 and three unentered areas | contour and dynamic form; **otherwise owed** | to derive | event-driven | retinotopic |
| → V3A / dorsomedial / dorsal prelunate / VIP / VLIP | dynamic form; in V3A a **full contralateral hemifield map**; otherwise owed | to derive | event-driven | retinotopic — **V3A's field is full-hemifield against V3's quarter-field** |
| → V1 / V2 feedback → layer 1 | to derive | to derive | event-driven | retinotopic |

**V3 and V3A do not share a coordinate frame and the contract carries them as one entry.** V3 carries a
quarter-field, V3A a full contralateral hemifield. **Two different extents cannot be one array**, and
the entry is a bundle at the architecture rung, so the split is owed at the source and **is not
performed here** — splitting invents the arity two rungs below where it is known.

## Algorithm

- **Transform.** **V3** is retinotopic and combines contour and dynamic form with early motion —
  **roughly half of its neurons are direction-selective. V3A** is a distinct area, strongly
  motion-responsive in humans, carrying a full contralateral hemifield map against V3's quarter-field.
  **No standard operation is named above for either**, and none is invented here.
- **Arrays.** **None can be written.** Neuron count to derive, surface area to derive, pitch to derive,
  tangential sub-elements to derive. **Every extent on this structure is open** — the lamina axis has a
  length (eight) and nothing else does. Recording an array with a symbolic H and W here would be no
  worse than elsewhere in this file; recording one with a symbolic *count* as well means the array has
  no dimension that is known. **The honest form is that the shape is (lamina=8, H, W) and that is all.**
- **Parameters.** **None with a value or a range above.** `fan_in` is to derive and, uniquely in this
  file, so is the count it would bound, so **not even the ≤ 16-bit ceiling yields a store figure.**
- **Update equation.** **Waiting on the emission question (§10)**, and it would be unwritable anyway:
  there is no array to write it over.
- **State carried between updates.** Shape (8, H, W), extents open.
- **Edge storage.** 4 input edges, 4 output edges — but **two of the output edges name multiple
  endpoints** (four and five respectively), so the edge count under-reports the line count by an
  unknown factor. Line count: to derive. Latency to derive on all. Interval unset.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** Everything the Shape field lists as to derive, which is all of it;
  whether V3 and V3A are one structure or two, owed at the source; the five-endpoint compound line's
  split, owed at the source; the four-endpoint line to V4 and three unentered areas; the *higher dorsal
  and parietal areas* class endpoint; the dorsomedial and dorsal prelunate areas, which have no entry
  anywhere.

---

# 7. V4

## Contract

**Inputs.**
- **← V2**, thin and pale stripes — hue, contour and junction, border-ownership, texture. The
  projection is **modular and only partly segregated**: a V4 injection labels thin stripes exclusively,
  or interstripes exclusively, or specific combinations, in interdigitating clusters 1–3 mm wide. **The
  two streams converge in some V4 modules and stay separate in others** — the first anatomically
  demonstrated cross-stream convergence in the ventral chain. Fan-in: to derive.
- **← V3 / V3A** — contour and dynamic form. Fan-in: to derive.
- **← V1**, direct — sparse, roughly the central 6°. Fan-in: to derive.
- **← frontal eye field** (`11_frontal_lobe`), terminating in **all cortical layers** — the spatial
  attentional gain signal, an enhancement or suppression applied by location and not a stimulus code.
  This is the edge that supplies the attentional modulation the function asserts, and the frontal eye
  field is the only one of the four attention-implicated structures shown to modulate visual-cortical
  firing through its own direct projection. Fan-in: to derive.
- **← pulvinar** (`12_thalamus`) — terminating **densely in the middle layers**, the layers a forward
  edge would use rather than the layer feedback uses. Fan-in: to derive.
  **This end declares no payload; the producer declares one, and the two are in tension.** The producer
  types it as a signal that *largely reflects the cortical driver* — orientation, direction and motion
  selectivity, **but not a new representation** — plus attentional gain and cross-areal synchrony in
  alpha/low-beta and gamma. **That is an echo of cortex, where the middle-layer termination recorded
  here is the anatomy of a drive.**
  **The laminar heuristic is what is at stake, and it is load-bearing here because nothing else at this
  end types the edge.** A middle-layer termination is feedforward in form; a cortically-derived payload
  is feedback in content, and a thalamic relay can plausibly be both. **Owed: state whether the
  heuristic is being relied on to assert a payload, or only to record a termination pattern.**
- **← inferotemporal cortex and higher ventral areas** (feedback), principally → layer 1. Fan-in: to
  derive.

**Outputs.**
- **→ inferotemporal cortex**, and to its **posterior division** specifically — intermediate shape,
  surface colour with the illuminant discounted, segmented surface and texture at large scale. Fan-out:
  to derive.
- **→ V2** (feedback), → layer 1, about 75% of its synapses onto spines there. Fan-out: to derive.

**Sizing.** Basis: **per hemisphere.** ~50M neurons (best available; the area's boundary is itself
contested). Fan-in to derive, bounded ≤ 16 bits → **≤ 100 MB.** Ordering V4 < V2 holds.

**Shape.** **Sheet**, rank 4: **(lamina, module class, H, W)** — eight laminae against a
glob/interglob tangential division. **Module pitch is measured at 1–3 mm**; surface area is **to
derive**, so the module count does not follow yet. **The tangential axis here is defined functionally
and connectionally rather than by a stain** — cytochrome oxidase fails beyond V2 — so a module boundary
is drawn by the pattern of input each module receives, which is the very edge set the shape is being
allocated for.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← V2 thin and pale stripes | hue, contour, junction, border-ownership, texture | to derive | event-driven | retinotopic, **coarser than V2's** |
| ← V3 / V3A | contour and dynamic form | to derive | event-driven | retinotopic |
| ← V1 direct | to derive | to derive | event-driven | retinotopic, **central ~6° only** |
| ← frontal eye field (`11_frontal_lobe`), all layers | **spatial attentional gain — an enhancement or suppression by location, not a stimulus code** | to derive | event-driven | **spatial, by location** — not a feature code |
| ← pulvinar (`12_thalamus`), middle layers | **in tension** — the producer types it as an echo of the cortical driver, the termination pattern here is that of a drive | to derive | event-driven | retinotopic |
| ← inferotemporal and higher ventral feedback → layer 1 | to derive | to derive | event-driven | retinotopic, in register |
| → inferotemporal, posterior division | intermediate shape, **illuminant-discounted** surface colour, segmented surface and texture at large scale | to derive | event-driven | retinotopic, coarse |
| → V2 feedback → layer 1 | **owed** | to derive | event-driven | retinotopic, in register |

**The frontal eye field row is a gain and not content, and the arithmetic must not read it as content.**
Two of this entry's six input rows carry modulation rather than a stimulus code — the frontal eye field
certainly, the pulvinar contestedly — and **a threshold gate summing all six inputs alike treats a gain
as evidence.**

## Algorithm

- **Transform.** Four operations named, and **none has a standard name licensed from above**:
  curvature and shape-part selectivity — **the first explicit *part* code**, above V2's junctions and
  below inferotemporal objects; **colour constancy and surface colour with the illuminant discounted**;
  texture and surface segmentation at larger scale; and **strong attentional gain**. Receptive fields
  larger than V2's, retinotopy coarser. The illuminant-discounting is the sharpest of the four —
  **discounting an illuminant is a named problem with no operation named for it here**, and the
  single- and double-opponent cells of V1 are recorded above as its *proposed substrate*, which is a
  hypothesis about mechanism and not a specification of one.
- **Tangential sub-structures carry different content**, so they are not a tiling of one population:
  **glob** cells' responses track perceptual colour space and retain hue tuning across luminance
  contrast; **interglob** cells prefer luminance contrast regardless of hue.
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `active` | (lamina=8, module_class=2, H, W) | open — emission question | to derive | to derive |
  | `threshold` | same | width `ceil(log₂(fan_in))`, fan_in to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **The module axis is defined by the edges the array is being allocated for**, and this is circular in
  a way no other entry in this file is. Cytochrome oxidase fails beyond V2, so a V4 module boundary is
  drawn by **the pattern of input each module receives** — the same connectivity map `fan_in(j)` needs
  and does not have. **So the tangential extent cannot be fixed before the topology is set, and the
  topology is surface-before-touching.**
  Module pitch is measured at **1–3 mm**; surface area is to derive, **so the module count does not
  follow.** The 16-way partition (8 laminae × 2 module classes) of ~50M neurons is to derive.
- **Parameters.** `fan_in` — to derive, bounded ≤ 16 bits, origin: the Sizing field. Module pitch 1–3
  mm, origin: measured, carried in the Shape field. The **V2 → V4 convergence pattern** — exclusive
  thin, exclusive interstripe, or specific combinations, in interdigitating clusters 1–3 mm wide — is
  **structure in the topology and not a scalar**, and it is the one place in this file where the
  architecture describes a convergence *pattern* rather than a convergence *count*. **It is still not a
  function**, and writing one is topology.
- **Update equation.** **Waiting on the emission question (§10)**, and on a second thing: **how a gain
  input is combined with a content input.** Two of six inputs here are modulatory. A count of active
  inputs over a threshold has no term that distinguishes them.
- **State carried between updates.** `active`, at (8, 2, H, W). V4 is inside loops with V2 and with
  inferotemporal cortex, both present in this section. Initial values: to derive.
- **Edge storage.** 6 input edges, 2 output edges. Line count = per-compartment counts × fan-out, and
  the 16-way partition does not exist. Latency to derive on all eight. Interval unset.
- **Adaptation.** **None set.** Note that **attentional gain is not adaptation** — it changes the
  response and not a stored parameter, and folding it into a learning rule would be a category error.
- **Open, beyond the standing list.** The 16-way partition; the surface area, and with it the module
  count and H × W; the circularity in the module definition; how a modulatory input combines with a
  content input; whether the pulvinar edge's payload rests on the laminar heuristic or only records a
  termination — owed at the producer.

---

# 8. Inferotemporal cortex

## Contract

**Inputs.**
- **← V4** → the posterior part of the anterior division — curvature and shape parts,
  illuminant-discounted surface colour, segmented texture, coarse retinotopy. Fan-in: to derive.
- **← V2** → the posterior division, direct — the jumping projection that bypasses V4, declared at both
  ends. Fan-in: to derive.
- **← perirhinal cortex, prefrontal cortex and amygdala** (feedback), principally → layer 1. Fan-in: to
  derive.

**Outputs.** All of these are more numerous from the anterior division than from earlier stages, so
**the outward fan of the ventral stream is concentrated at its last sub-structure** rather than spread
along it.
- **→ perirhinal cortex (areas 35 and 36)** — the identity code, and the anatomical step by which the
  ventral stream reaches the hippocampal formation. Fan-out: to derive.
- **→ hippocampal formation** — the identity code as one element of an episode. Fan-out: to derive.
- **→ prefrontal cortex, ventrolateral** (`11_frontal_lobe`) — identity, for controlled retrieval and
  selection. **The consumer types no payload**, so this end is the only typed one.
  **This entry declares no orbitofrontal output, and the consumer's orbitofrontal entry declares an
  input from here.** That entry reads `← the inferotemporal and temporal cortex, orbital`, and it is a
  separate structure in that file from the ventrolateral one, so the line above does not cover it.
  **That edge is declared at the consumer and at no producer. Owed at this section's source: declare it
  here, or it is withdrawn there.** Fan-out: to derive.
- **→ amygdala** — identity, for affective evaluation. Fan-out: to derive.
- **→ striatum** — putting the ventral stream's output into the action-selection loop and not only into
  memory and evaluation. Fan-out: to derive.
- **→ anterior intraparietal area** (`06_posterior_parietal`), from **the lower bank of the superior
  temporal sulcus and the middle temporal gyrus** — **carries:** object **identity**, the same
  categorical code the edges above carry, invariant to position, size, pose and lighting, delivered
  into the grasp channel. **This is the only projection out of the ventral stream and into the parietal
  lobe in this section.** Fan-out: to derive.
  **The consumer's entry asserts that the producer declares nothing on this edge, and that assertion
  is false: this entry declares it, above.** **The repair
  is owed at the consumer, not here** — it is the class of defect where a file asserts what another
  file contains without opening it, and the consumer's own front matter records that it did not open
  the neighbouring files.
  **The edge itself is a candidate and this end should not read as settled.** The source marks it Class
  1 from a macaque retrograde-tracer study located by web search, with **the abstract only read and no
  full paper opened**, awaiting verification under the verified-only rule.
- **→ the distributed conceptual / semantic system** (via the temporal pole,
  `07_anterior_temporal_lobe`) — the identity code, view-invariant object and face identity.
  Fan-out: to derive.
  **This endpoint names a system and not a structure, and it is inherited in that form**, so the
  architecture records it as a class endpoint owed a split at the source. The temporal pole is a named
  region with an entry and the consumer declares `← anterior inferotemporal cortex / ventral temporal —
  view-invariant object and face identity`, so a direct edge has a far end that already declares it —
  but writing one here would add a claim the source does not make. **Recorded, owed at the source.**
  **What lies beyond the temporal pole is not this entry's to name.** That consumer's six outputs carry
  the amodal concept onward, and it records that *amodal concept* is a phrase and not a type — no
  units, no range, no coordinate frame — so the system this edge ultimately serves is **untyped at the
  only end that can type it.**

**Sizing.** Basis: **per hemisphere.** ~120M neurons, order-of-magnitude — no clean primary human count
exists. Fan-in to derive, bounded ≤ 16 bits → **≤ 240 MB.** V1's density-derived figure does not carry
here: V1 is the ~60,000/mm³ packing outlier, while this is ordinary
association cortex at ~20–40,000/mm³.

**Shape.** **Sheet**, rank 4 posteriorly and **rank 3 anteriorly**, and the change is the finding:
**(lamina, division, H, W)** where the posterior division continues V4's glob tangential organisation,
but the anterior division's feature columns have **no discrete boundaries** — a continuous mapping of
feature space across partially overlapping columns. **A continuous map has no compartment axis to
index**, so anteriorly the tangential axis is a coordinate rather than a sub-element list, and what an
edge terminating "on a column" selects is **to derive**. Extents: **to derive** throughout.

**Edge latency.** All edges **to derive.**

## Representation

| line | units | range / normalisation | update timing | coordinate frame |
|---|---|---|---|---|
| ← V4 → posterior part of anterior division | curvature and shape parts, illuminant-discounted surface colour, segmented texture | to derive | event-driven | **coarse retinotopy** — the last row in this file with one |
| ← V2 → posterior division, direct | to derive | to derive | event-driven | retinotopic |
| ← perirhinal / prefrontal / amygdala feedback → layer 1 | to derive | to derive | event-driven | to derive |
| → perirhinal cortex (35, 36) | identity code | **none — a phrase, not a type** | event-driven | **none** |
| → hippocampal formation | identity code, as one element of an episode | none | event-driven | none |
| → prefrontal cortex, ventrolateral (`11_frontal_lobe`) | identity, for controlled retrieval and selection | none | event-driven | none |
| → amygdala | identity, for affective evaluation | none | event-driven | none |
| → striatum | identity, into the action-selection loop | none | event-driven | none |
| → anterior intraparietal area (`06_posterior_parietal`) | object identity, invariant to position, size, pose and lighting, into the grasp channel | none | event-driven | none |
| → the distributed conceptual / semantic system, via the temporal pole (`07_anterior_temporal_lobe`) | view-invariant object and face identity | none | event-driven | none |

**Every output row above has no units, no range and no coordinate frame, and that is a finding rather
than an omission.** This is where the payload stops being a signal and becomes a category: *the
identity of the thing*, with no coordinate frame, **is a phrase and not a type**, and this is the first
stage in the visual line of which that is true. **The structural consequence is that no units can be
stated on any output edge**, so seven of this file's cross-file edges leave untyped — and the untyping
is licensed at the architecture rung, not introduced here.
**This is the representational wall of the file.** Everything upstream has a frame; nothing downstream
of here does.

## Algorithm

- **Transform.** **Top of the ventral "what" stream**: invariant object and face identity, categorical
  representation invariant to position, size, pose and lighting. **No standard operation is named
  above**, and invariance to four transformation groups at once is not a named operation in any case.
  Recorded as a finding.
- **Two divisional sub-structures in series** — posterior and anterior inferotemporal cortex — **with
  the complexity gradient continuous rather than stepped**, since cells needing complex features are
  already present posteriorly and in V4 in small proportion. **So the division axis is not a pipeline
  boundary**, and an implementation that computes posteriorly then anteriorly asserts a step the
  architecture denies.
- **The two divisions differ in kind tangentially, and the rank changes between them.** Posteriorly the
  colour-selective globs of V4 continue, so the tangential organisation is V4's — **rank 4.**
  Anteriorly there are **feature columns whose borders are not discrete**, a continuous mapping of
  complex feature space across partially overlapping columns — **rank 3**, because **a continuous map
  has no compartment axis to index.**
- **Arrays.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `posterior_active` | (lamina=8, module_class, H, W) — rank 4 | open — emission question | to derive | to derive |
  | `anterior_active` | (lamina=8, H, W) — **rank 3** | open | to derive | to derive |
  | `posterior_threshold` / `anterior_threshold` | matching | width `ceil(log₂(fan_in))`, to derive, bounded 16 | 0 … fan_in | count of active inputs |

  **This is the only structure in the file whose two halves have different rank**, and it is why they
  are two arrays rather than one array with a division axis. **A single (lamina, division, H, W) tensor
  would give the anterior division a compartment axis it does not have.**
  **What an edge terminating "on a column" selects anteriorly is to derive**, because there is no
  column to select — the tangential axis is a coordinate. Extents to derive throughout.
- **Parameters.** `fan_in` — to derive, bounded ≤ 16 bits, origin: the Sizing field. Neuron count ~120M
  is **order-of-magnitude**, origin: the Sizing field, which states that no clean primary human count
  exists — **the widest-tolerance count in the file, and the entry carries the tolerance rather than
  the number alone.**
- **Update equation.** **Waiting on the emission question (§10).**
- **State carried between updates.** `posterior_active` and `anterior_active`. The return limbs from
  perirhinal cortex, prefrontal cortex and amygdala **close loops whose far ends are outside this
  section**, so co-instantiation for this entry is satisfied only for the joints present here.
  Initial values: to derive.
- **Edge storage.** 3 input edges, 7 output edges — **and seven of the ten cross a file boundary or
  reach a structure with no entry anywhere.** Line count to derive. Latency to derive on all ten.
  Interval unset. **The outward fan is concentrated at the anterior division**, so line count is not
  distributed evenly across the division axis, and the split is to derive.
- **Adaptation.** **None set.**
- **Open, beyond the standing list.** Every extent; what an edge terminating on an anterior column
  selects; the orbitofrontal output declared at the consumer and at no producer, owed at this section's
  source; the anterior intraparietal edge's verification, which is a candidate on an abstract only;
  perirhinal cortex, which has no entry in any file.

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Retina — ganglion cells | per eye | ~1.0–1.2M | ≤ 16 | ≤ 2.40 MB |
| Retina — photoreceptors | per eye | ~97M | 0 | 0 |
| Retina — horizontal / bipolar / amacrine | per eye | to derive | to derive | to derive |
| Optic chiasm | both eyes | none | — | 0 |
| Lateral geniculate nucleus | per side | ~1.77M | ≤ 16 | ≤ 3.54 MB |
| V1 | per hemisphere | ~280–310M | 12–14 | 450–525 MB |
| V2 | per hemisphere | ~200–220M | ≤ 16 | ≤ 420 MB |
| V3 / V3A | per hemisphere | to derive | ≤ 16 | to derive |
| V4 | per hemisphere | ~50M | ≤ 16 | ≤ 100 MB |
| Inferotemporal cortex | per hemisphere | ~120M | ≤ 16 | ≤ 240 MB |
| **stated total** | mixed | | | **~1.22–1.29 GB** |

**The total is a floor, not a requirement.** Two structures are uncounted, every fan-in but V1's is at
the 16-bit ceiling rather than at a measured value, and **state memory and edge storage are not in this
table at all** — edge storage cannot be sized until the scheduling discipline is set, and it is not.

**Memory is not a binding constraint here and the figure is not to be reduced.** It is a derived
requirement recorded as found.

**One row differs from the architecture's own table and the difference is deliberate.** The
architecture gives the retina's horizontal / bipolar / amacrine row as `≤ 16` bits per neuron. Under
spec §5a those are **graded, non-spiking elements**, whose store **must not be defaulted to zero or to
`log₂(fan-in)`** — and `≤ 16` is the log₂ ceiling. The row reads **to derive** here for that reason.
**This is a defect found at the architecture rung and it is repaired there, not here**; it is recorded
in this file because the design entry cannot carry a store it is forbidden to assume.

## Completion test

**An entry is finished when the code can be written from it without making a single further choice.**

**By that test no entry in this file is finished, and none can be finished at this rung.** The
blocking items are the six on the standing list above, and four of them — the emission question,
the scheduling discipline, the connection topology, and tile geometry and sparsity — are on the
surface-before-touching list and are Micky's.

**What the entries do carry, and it is not nothing:** the contract for every structure, the
representation of every line including the frame changes at the chiasm and the untyping at
inferotemporal cortex, the array shapes and their open extents, the parameters that have an origin, the
state and the loops that fix its ordering, the edge count per structure, and — at every point where an
operation would have to be invented — a recorded finding that none is named above.
