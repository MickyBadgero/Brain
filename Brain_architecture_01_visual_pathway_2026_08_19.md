# Brain architecture — 01 visual pathway

**Date:** 2026-08-19
**Derived from:** `human_brain_01_visual_pathway` — the ventral visual line, retina to
inferotemporal cortex. **One source file, and no other content source.**

**Cross-file checks contained in this file.** Each line names another file that was held open beside
this one and whose shared edges with it are diffed and stemmed below.

- `04_dorsal_visual_parietal_stream`, `06_posterior_parietal`.
- `08_medial_temporal_lobe`, `09_basal_ganglia`.
- `12_thalamus`.
- `14_brainstem_midbrain_hypothalamus`.
- `02_auditory_pathway`, `11_frontal_lobe`.
- `07_anterior_temporal_lobe`.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file has been read against this one; an endpoint with no stem is one whose far end has
not yet been opened beside this file, and it is not a claim that none exists.

**Far ends.** This block is the file's own record of what is outstanding, so that a missing stem reads
as *not yet done* rather than as *nothing there*.

**Worked, far file opened beside this one —** the middle temporal area, the ventral
intraparietal area and the ventral lateral intraparietal area into
`04_dorsal_visual_parietal_stream`; the anterior intraparietal area into `06_posterior_parietal`;
the hippocampal formation and the amygdala into `08_medial_temporal_lobe`; the striatum into
`09_basal_ganglia`; the pulvinar, the thalamic reticular nucleus and the higher-order thalamus into
`12_thalamus`; the superior colliculus, its superficial layers and the suprachiasmatic nucleus into
`14_brainstem_midbrain_hypothalamus`; the caudal auditory parabelt into `02_auditory_pathway`; the
frontal eye field and ventrolateral prefrontal cortex into `11_frontal_lobe`.

**Outstanding, far end resolves to a file not yet opened beside this one —**

**No endpoint remains outstanding. Every cross-file endpoint in this file has been worked against its
far end.**
**What remains here is inherited, not pending**, and it is of three kinds: the seven endpoints with no
entry in any file, listed below; the class endpoints that name no structure, listed below; and the
payload repairs marked *owed at this section's source* on individual edges. **None is repairable at
this rung.**

**No entry anywhere, inherited from the source and not repairable at this rung —** perirhinal cortex
(areas 35 and 36), the olivary pretectal nucleus, the dorsomedial area, the dorsal prelunate area, the
V4 transitional area, the ventral occipitotemporal area, and the visually responsive part of temporal
area F.

**Class endpoints, naming no structure —** *lower visual areas*, *higher dorsal and parietal areas*,
*brainstem*, and *the distributed conceptual / semantic system*. Each needs splitting at the source
before it can carry a stem at all.

**Counting basis is declared per structure and is not uniform in this section.** Three bases appear:
**per eye** (retina, optic nerve), **both eyes combined** (the chiasm's through-traffic), and **per
hemisphere** (lateral geniculate nucleus onward). The chiasm is where the basis changes.

---

## Structural invariants

**Whole-pathway co-instantiation.** Every structure below exists and is active from the outset. The
visual line is not a feedforward chain: the corticothalamic projection from V1 back to the lateral
geniculate nucleus supplies about 30% of that nucleus's synapses — a descending arm that outnumbers
the ascending drive it regulates — and every cortical stage here returns a feedback edge to the stage
below it. A stage brought up later would leave those loops open, and an open loop is not a loop.

**Per-edge latency.** Every edge below carries a nonzero, finite, heterogeneous latency in real time
units. **This section can name none of them: every latency reads *to derive*.** That is the honest
state of it — file 01 records no conduction time, no synaptic delay, and no loop latency. What it
does record is one qualitative timing fact, inside the lateral geniculate nucleus: a subpopulation of
relay cells (the lagged class) carries a delay introduced by triadic inhibition, with slower-rising
and more sustained responses than the non-lagged class. So the first timing datum in the visual line
is an **internal** one, and it is a difference between two populations of one structure rather than a
property of an inter-structure edge.

**Two edges in this section are not projections at all.** The retina's input is **light** — photon
flux imaged on the photoreceptor sheet, an optical arrival and not a neural edge. And the optic
chiasm has **no synapse**, so its edges are routing statements: fan-in and fan-out read *none*.
Neither takes conduction-plus-synaptic time, and both still take real time.

---

## Retina

- **Function → structure.** Phototransduction plus the first stage of visual processing: light to
  neural signal, centre–surround spatial processing, ON/OFF channel splitting, and cone-opponent
  colour processing. **Colour is computed here, in the eye, and not downstream.** The structure that
  does it is a three-deep vertical chain — photoreceptor → bipolar cell → ganglion cell — with two
  lateral populations spread across it, horizontal cells in the outer plexiform layer and amacrine
  cells in the inner. The two lateral populations act on different axes: horizontal cells build the
  antagonistic surround in **space**, amacrine cells build the transient response in **time**.
- **Inputs.**
  - **light (the world)** → the photoreceptor sheet. Not a neural edge. Fan-in: not applicable.
- **Outputs.** All four leave as ganglion-cell axons in the optic nerve.
  - **→ optic chiasm** (thence the lateral geniculate nucleus) — the image-forming line, ~80/10/8–10%
    of the ganglion population across three channel classes: midget/parvocellular (~80%,
    red–green cone-opponent, sustained, fine detail), parasol/magnocellular (~10%, achromatic,
    transient, coarse), bistratified/koniocellular (~8–10%, blue–yellow cone-opponent). Fan-out: to
    derive.
  - **→ superior colliculus, superficial layers** (`14_brainstem_midbrain_hypothalamus`; the consumer
    names the lamina precisely, as **stratum griseum superficiale**, the upper superficial grey) — not
    more than 10% of ganglion cells, about 6%
    near the fovea and rising with eccentricity, and largely a **branch off the geniculate line**
    rather than an independent population. Fan-out: to derive.
  - **→ olivary pretectal nucleus** — from broad-field melanopsin-containing luminance detectors.
    **The nucleus has no entry in any file, and its own consumer is declared.**
    `14_brainstem_midbrain_hypothalamus` declares the superior colliculus receiving
    `← olivary pretectal nucleus → stratum griseum intermediale`, a luminance scalar arriving in the
    **premotor rather than the visual** layers. **So the two-hop route from here to the colliculus is
    declared at both ends with no entry for the stage between them** — and that stage is where the
    transform would live, since a broad-field luminance detector's output is not the same object as a
    scalar delivered to premotor layers. Inherited; the entry is owed at the source.
    Fan-out: to derive.
  - **→ suprachiasmatic nucleus** (`14_brainstem_midbrain_hypothalamus`, a sub-element of its
    hypothalamus entry, and **the only structure in that whole section with a neuron count** —
    ~50,000 per side) — from melanopsin ganglion cells. Fan-out: to derive.
    **This end declares the cell class and no payload; the consumer types it fully** — an **irradiance,
    "lights-on" signal**, ambient luminance for clock entrainment, arriving by the
    **retinohypothalamic tract**, and **explicitly not spatial vision.** That last clause is the
    load-bearing one and it is absent here: **every other output of this entry is spatial, and nothing
    at this end marks this one as different in kind.** A consumer reading only this end would allocate
    a retinotopic map for a scalar. **Owed at this section's source: the payload and the tract name.**
- **Sizing.** Basis: **per eye.**
  - Ganglion cells ~1.0–1.2M; fan-in to derive, bounded ≤ 16 bits → **≤ 2.40 MB** at 1.2M.
  - Photoreceptors ~97M measured (~126M textbook): **zero.** A photoreceptor is a transducer, stores
    no threshold, and the log₂ cost does not apply.
  - Horizontal, bipolar and amacrine cells: **counts to derive** — the source records none. Their
    store cannot be stated, and it is not zero by default.
  - **Structure total: to derive**, with ≤ 2.40 MB firm and three of five cell classes uncounted.
- **Shape.** **Sheet**, rank 3: **(sub-element, H, W)**, sub-elements photoreceptors / horizontal /
  bipolar / amacrine / ganglion, H × W the retinal sampling grid. **The grid is not uniform** — peak
  foveal cone density is ~199,000 cones/mm² falling steeply with eccentricity (~32,200 / ~19,300 /
  ~11,600 per mm² at 0.5 / 1.0 / 1.5 mm out), so this is a **space-variant sampling lattice** and not
  a raster. H and W: **to derive** — no retinal surface area is recorded. The eccentricity function is
  the correspondence rule the ganglion output edge needs.
- **Edge latency.** All four output edges: **to derive.**
- **Invariant conformance.** Co-instantiation: the chain and both lateral populations are present
  from the outset; the horizontal-cell feedback edge onto surrounding photoreceptors is a loop inside
  the first synaptic layer and cannot be staged. Per-edge latency: satisfied, all to derive; the
  input edge is optical and not a projection.
- **Justification (biological).** The colour computation is complete at the ganglion-cell output —
  three cone classes read out by three ganglion classes, opponency already formed — so the bus
  leaving the eye carries three chromatic classes and not one intensity signal. Any stage downstream
  that reads hue is reading this.

## Optic chiasm

- **Function → structure.** Routing, not computation. Fibres sort so that each hemisphere receives
  the contralateral visual hemifield. **No synapse and no transform.** Two sub-structures, and they
  are parallel channels rather than a circuit: the **crossed bundle** from ganglion cells nasal to
  the fovea, and the **uncrossed bundle** from cells temporal to it. The sorting rule is a line — the
  line of decussation, normally aligned with the fovea, and a developmental variable rather than a
  structural given.
- **Inputs.**
  - **← retina**, both eyes — the full three-class ganglion bus, one per eye, still monocular and
    still whole-hemifield. Fan-in: **none (no synapse here).**
- **Outputs.**
  - **→ lateral geniculate nucleus of each hemisphere** — the same content, unchanged. What changes
    is which fibres go where: each optic tract now carries the **contralateral hemifield of both
    eyes** rather than one whole eye. Fan-out: **none (no synapse here).**
- **Sizing.** **Zero.** Neurons: none — a fibre tract, not a nucleus. No neurons, no thresholds, no
  parameter memory. Basis: through-traffic ~2M fibres, **both eyes combined**, of which about 5% are
  bound for structures other than the two geniculate nuclei.
- **Shape.** **Transmission-only: not an activity array.** No neurons, no thresholds, no state. Its
  shape is a **routing index**, rank 1, length ~2M fibres both eyes combined, mapping each line to a
  destination side by the nasal/temporal boundary. Recording it as a zero-length tensor would assert
  state it does not hold.
- **Edge latency.** **To derive**, and this is the structure where a derivation would start: the
  tract is myelinated and its g-ratio is unrecorded, so the substrate of the delay is named and the
  number is not.
- **Invariant conformance.** Co-instantiation: present from the outset; a routing stage cannot be
  deferred without disconnecting both hemifields. Per-edge latency: nonzero — the fibres have length
  — while the edges themselves are routing statements and carry no synaptic term.
- **Justification (biological).** Crossed:uncrossed is about **53:47** in the neurotypical human, not
  50:50 and not 100:0: total decussation is the lateral-eyed arrangement, and the uncrossed fraction
  rises as the orbits rotate forward and the binocular field grows. The ratio is a consequence of eye
  placement, and the slight majority for crossing follows from the nasal retina being the larger
  sector once the boundary sits at the fovea.

## Lateral geniculate nucleus

- **Function → structure.** Thalamic relay from retina to V1, and **a gate rather than a wire.** Six
  layers — 1–2 magnocellular, 3–6 parvocellular, with a koniocellular sublayer ventral to each —
  every layer monocular, the layers alternating by eye. Two cell classes in fixed ratio: relay cells
  (~75–80%) and local interneurons (~20–25%). The retina is the sole **driver** and a small minority
  of the synapses; the larger non-retinal input is **modulatory** and sets whether, when and how
  strongly the retinal message passes, adding no content.
- **Inputs.**
  - **← retina**, via the chiasm and optic tract — the three ganglion channel classes, mapping
    one-to-one onto the three layer classes: parvocellular layers 3–6 ← midget, koniocellular
    sublayers ← bistratified, magnocellular layers 1–2 ← parasol. **~5–10% of this nucleus's
    synapses**, and the only driver. Fan-in: to derive (classically one to a few retinal afferents
    per relay cell; no human figure).
  - **← V1, sublayer 6a** — corticothalamic feedback, **~30% of synapses**, the largest single
    non-retinal source. Fan-in: to derive.
  - **← thalamic reticular nucleus** (`12_thalamus`) — inhibition, a gain and gate control. Fan-in: to
    derive. **Two-ended and checked:** the producer declares `→ lateral geniculate
    nucleus — inhibition`, **the gate**, and names the visual sector of that sheet explicitly. Both
    ends agree the payload is inhibition and carries no content.
  - **← brainstem**, cholinergic / noradrenergic / serotonergic — arousal state, which sets the relay
    cells' burst-versus-tonic mode. Fan-in: to derive.
- **Outputs.** The projection to V1 is **four edges, not one**, and only two reach layer 4.
  - **→ V1 4Cα**, from magnocellular layers 1–2, via the optic radiation — achromatic, retinotopic,
    point-to-point, still monocular. Fan-out: to derive.
  - **→ V1 4Cβ**, from parvocellular layers 3–6 — red–green, retinotopic, point-to-point, monocular.
    Fan-out: to derive.
  - **→ V1, the cytochrome-oxidase blobs of layers 2/3 and layer 1**, from the koniocellular
    sublayers — blue–yellow, retinotopic, monocular. **This edge does not terminate in layer 4 at
    all.** Fan-out: to derive.
  - **→ V1 4A**, parvocellular and koniocellular collaterals. Fan-out: to derive.
  - **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), direct, **bypassing V1
    entirely** — payload **owed**; mostly koniocellular cells, sending virtually no collateral to V1,
    numbering about 10% of the V1 population that innervates that area. Fan-out: to derive. The
    consumer marks this payload *owed* as well, and adds that the edge is sufficient to support
    motion sensitivity without V1 — **so the two ends agree, and they agree that neither can type
    it.** That is the honest state and not a defect at either end.
  - **→ thalamic reticular nucleus** (`12_thalamus`), collaterals of the thalamocortical axons — a copy of the
    outgoing signal, which drives the gate that regulates it. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere (per side).** ~1.77M neurons (magnocellular ~0.22M,
  parvocellular ~1.55M); fan-in to derive, bounded ≤ 16 bits → **≤ 3.54 MB.** Synapse proportions are
  known (retinal ~5–10%, cortical ~30%, remainder reticular and brainstem) and the absolute count is
  not, which is exactly the case the log₂ bound is for.
- **Shape.** **Laminated nucleus**, rank 3: **(lamina, H, W)** — six laminae plus a koniocellular
  sublayer ventral to each, every lamina a retinotopic map and every lamina monocular. **This is the
  one structure in this section whose count partitions to its sub-elements**, and it closes:
  magnocellular ~0.22M over laminae 1–2 is **~110,000 per lamina**; parvocellular ~1.55M over 3–6 is
  **~387,500 per lamina**; the two sum to ~1.77M against the headline exactly. Volumetric density
  ~104 mm³ over ~1.77M is **~17,019 neurons/mm³**. H and W: **to derive** — no retinotopic pitch is
  recorded. **The eye assignment per lamina is owed**, so the lamina axis is ordered and not yet
  labelled.
- **Edge latency.** All edges **to derive.** One internal timing fact is recorded and is not an edge
  latency: the lagged relay-cell class is delayed by triadic inhibition.
- **Invariant conformance.** Co-instantiation: the gate cannot come up after the relay it gates —
  the V1 → 6a → this nucleus loop and the reticular collateral loop are both closed here, and both
  would be open in any staged bring-up. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** Attention modulates the human lateral geniculate nucleus response,
  so the first place the visual stream is **selected** is the thalamus and not the cortex. A stage
  described only as a relay would make that unstatable. The mechanism is a change of transfer
  function rather than of message: relay cells fire in burst mode (hyperpolarised, high-gain,
  nonlinear) or tonic mode (depolarised, near-linear), and the modulatory inputs move them between
  the two.

## V1 — primary visual cortex

- **Function → structure.** First cortical stage. Binocular convergence — the eyes first combine
  here — orientation maps, a precise retinotopic map, oriented-edge and spatial-frequency
  selectivity, and the **first cortical transformation** of the cone-opponent signal (single-opponent
  cells, spatially low-pass; double-opponent cells, chromatically and spatially opponent, the
  proposed substrate for downstream colour constancy). Structurally it is the most finely divided
  area of cortex: **eleven sub-structures — 1, 2, 3, 4A, 4B, 4Cα, 4Cβ, 5a, 5b, 6a, 6b** — against the
  eight of general cortex, because layer 4's sublamination is V1's alone and merges to a single layer
  4 at V2. Colour-preferring cells concentrate in the cytochrome-oxidase blobs of layers 2/3, one
  opponency type per blob.
- **Inputs.**
  - **← lateral geniculate nucleus, magnocellular layers 1–2 → 4Cα.** Fan-in: to derive.
  - **← lateral geniculate nucleus, parvocellular layers 3–6 → 4Cβ.** Fan-in: to derive.
  - **← lateral geniculate nucleus, koniocellular sublayers → the cytochrome-oxidase blobs of layers
    2/3, and layer 1.** Fan-in: to derive.
  - **← lateral geniculate nucleus, parvocellular and koniocellular collaterals → 4A.** Fan-in: to
    derive.
  - Together the geniculate edges are a **minority** of V1's excitatory synapses; most is
    intracortical. None of them carries orientation, disparity or spatial-frequency tuning — all
    three are built here.
  - **← V2, V3, V4 and the middle temporal area** (the last in
    `04_dorsal_visual_parietal_stream`) (feedback), principally → **layer 1**, also layers 2, 5 and
    6, **avoiding layer 4**, which is what distinguishes a feedback edge at the receiving end. On
    layer 1 it terminates on apical tufts belonging to cells housed in layers 2/3 and 5. Fan-in: to
    derive.
    **This is a four-source class line and the arity is the defect.** The middle temporal area's own
    entry declares its limb of it separately and types it — contextual and attentional modulation,
    figure–ground and border-ownership context, attentional gain, **not a new stimulus code** — and
    records at its end that **which of the four contributes which part of the payload is owed.**
    **Splitting this into four named edges is owed at this section's source**, and until it is split
    the three intra-section limbs remain untyped while the cross-file one is typed at the far end
    only.
  - **← posterior inferotemporal cortex, anterior inferotemporal cortex, temporal areas TF and TH,
    occipitotemporal and superior temporal sulcal cortex, caudal intraparietal cortex** (long-range
    feedback) — cortical afferents to V1 are not confined to the prestriate areas. Fan-in: to derive.
- **Outputs.** The forward output to V2 is segregated by content; the number of streams is contested
  (three, two, or four groupings in the literature), so the edges are stated by **target stripe
  class**, the axis all three groupings agree on.
  - **→ V2 thin stripes**, predominantly from the cytochrome-oxidase blobs of layers 2/3 (~81% of
    labelled source cells in patches). Fan-out: to derive.
  - **→ V2 pale stripes** — the richest of the three; composition layers 2/3 87%, 4B 10%, 4A 2%,
    layers 5/6 2%. Fan-out: to derive.
  - **→ V2 thick stripes** — composition layers 2/3 67%, 4B 23%, 4A 7%, layers 5/6 2%. **4B is the
    minority contributor here**, which the simple account inverts. Fan-out: to derive.
  - **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), from **4B, predominantly its
    spiny-stellate class** (~76% spiny stellate against ~24% pyramidal — the reverse of the
    V2-projecting population, and largely separate cells, under ~5% double-labelled). Fan-out: to
    derive.
    **This end declares no payload and no termination layer, and the consumer declares both** —
    direction of motion and binocular disparity, achromatic, coarse-spatial, onto layer 4, on the
    fast few-hop route. **The producer's end is the deficient one and the repair is owed at this
    section's source.** The consumer also carries a claim about this edge that this end does not:
    that 4B's spiny stellates take magnocellular input only, direct from 4Cα, while its pyramids take
    both and project to V2 instead — **making the direct route magnocellular and the V2 route
    mixed.** Whether this section's source licenses that is unchecked here.
  - **→ V3**, from **4B** — a major input. Fan-out: to derive.
  - **→ V4**, direct — sparse, restricted to roughly the central 6°. Fan-out: to derive.
  - **→ V2, from 4A**, and **→ V2, from layers 5/6** — minor components the three-stream account
    omits. Fan-out: to derive.
  - **→ lateral geniculate nucleus**, from **6a** — the modulatory gate on the relay feeding V1.
    Fan-out: to derive.
  - **→ higher-order thalamus** (`12_thalamus`), from **6b** — reaching higher-order nuclei but **not** the reticular
    nucleus. Fan-out: to derive.
  - **→ superior colliculus** (`14_brainstem_midbrain_hypothalamus`)**, from 5b** — retinotopic
    salience for orienting. Fan-out: to derive. **Two-ended and confirmed in the same
    words**; the consumer adds the termination, **the superficial layers**, which this end does not
    name. **And the contest recorded at the retina entry turns on this edge**: if the colliculus's
    visual drive arrives through the geniculate and V1, then this is the edge carrying it, and the
    retinotectal one is not.
  - **→ lower visual areas** (descending), from **layer 2** — a supragranular feedback stream
    distinct from the classical infragranular one, so layers 2 and 3 are not interchangeable as
    origins. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~280–310M neurons (density × confirmed volume; ~140M
  retained as a lower bound). Fan-in is the one place in this section where the source bounds it
  rather than leaving it open, and it is **disputed across a 6.5× range** — 2,300–5,600 measured in
  macaque V1, ~7,000 as a human cortical average, ~15,000 derived from human synapse and neuron
  densities. **Under log₂ that range costs 12 to 14 bits**, so:
  - at 12 bits: **450 MB**; at 13 bits: **487.5 MB**; at 14 bits: **525 MB** (at 300M neurons).
  - At the ~140M lower bound: **210 / 227.5 / 245 MB**.
  - **The neuron count, not the synapse dispute, is what the figure turns on** — a 2.1× spread in
    count against a 1.17× spread from a 6.5× spread in fan-in.
- **Shape.** **Sheet**, rank 3: **(sub-element, H, W)**, eleven laminar sub-elements — 1, 2, 3, 4A,
  4B, 4Cα, 4Cβ, 5a, 5b, 6a, 6b — over a tangential grid.
  **Surface density is derivable and the pitch is not.** ~60,000 neurons/mm³ over ~2 mm thickness is
  **~120,000 neurons per mm² of surface**; ~2,600 mm² of surface × 120,000 = **312M**, which closes
  independently against the ~280–310M headline.
  **H × W = to derive**, because V1's own tangential pitch is not recorded — the cytochrome-oxidase
  blobs are named with no spacing given. Once a pitch arrives the whole shape follows: at 1 mm it is
  2,600 tiles of ~120,000 neurons and ~210 kB each; at 0.5 mm, 10,400 tiles of ~30,000 and ~52.5 kB.
  **The eleven-way partition of the neuron count is also to derive**, so the sub-element axis is named
  and not yet sized — and four separate geniculate edges terminate on four of those sub-elements.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: V1 sits inside four closed loops that are all present
  in this section — with the lateral geniculate nucleus by way of 6a, and with V2, V3, V4 and the
  middle temporal area by way of their layer-1 feedback. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The eyes first combine here, which is what makes this the stage
  where eye of origin is consumed and discarded. The modular account in which colour was handled
  outside V1 and only properly at V4 is superseded: colour and form are not separable streams in
  cortex.

## V2 — secondary visual cortex

- **Function → structure.** First real composition of visual features — contour integration and
  illusory contour, angle and junction selectivity, border-ownership and figure–ground, naturalistic
  texture (which V1 cannot distinguish from spectrum-matched noise), and hue. Two **orthogonal** axes
  of sub-structure: **tangentially** three cytochrome-oxidase stripe classes — thin, pale, thick —
  and **laminarly** eight layers, 1, 2, 3, 4, 5a, 5b, 6a, 6b, with **layer 4 undivided.** Every
  stripe class carries the full set of layers and every layer runs through all three stripe classes.
- **Inputs.**
  - **← V1, cytochrome-oxidase blobs of layers 2/3 → thin stripes** — the cortical colour signal.
    Fan-in: to derive.
  - **← V1, interblob layers 2/3 with a 4B component → pale stripes.** Fan-in: to derive.
  - **← V1, layers 2/3 and 4B → thick stripes.** Fan-in: to derive.
  - **← V1, 4A and layers 5/6 → pale and thick stripes** — minor components. Fan-in: to derive.
  - **← auditory parabelt, caudal division** (`02_auditory_pathway`) — an auditory association area
    writing into secondary visual cortex. Which tangential compartment it reaches is unrecorded, and the
    answer would matter: thick stripes are the motion and disparity channel. Fan-in: to derive.
    **Checked against the producer, and the compartment question has a candidate rather than an answer.**
    The producer declares this edge only **inside a class line** — its caudally-directed stream, naming
    the temporoparietal junction, posterior parietal and occipital regions *including secondary visual
    cortex*, caudal and dorsal prefrontal cortex, dorsal cingulate and parahippocampal areas as one
    edge. **That producer carries an arity note saying such a split would name far ends that mostly
    have no matching declaration; this limb is one of the exceptions**, since this entry declares it,
    so the limb can be split out even though the rest of the line cannot.
    **On the compartment:** the producer types the caudal division's payload as **location and
    motion**, and this entry records that **thick stripes are the motion and disparity channel.**
    **So thick stripes are the candidate, on the two payloads together, and neither end states it.**
    Recorded as a candidate because neither end constrains it alone. **Owed at both sources.**
  - **← V4, middle temporal area and higher areas** (the second in
    `04_dorsal_visual_parietal_stream`) (feedback), principally → layer 1, avoiding layer 4. Fan-in:
    to derive. The middle temporal limb is declared at its producer too and reads **owed at both
    ends** there — **so this is an edge both ends agree is untyped**, not one end's omission. The
    class line's arity is still owed at this section's source.
- **Outputs.** Forward edges leave from layers 2/3 of the named stripe class.
  - **→ V4**, from layers 2/3 of the **thin and pale** stripes. Fan-out: to derive.
  - **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), from layers 2/3 of the **thick**
    stripes, onto **layer 4**. Fan-out: to derive.
    **This end declares no payload; the consumer declares binocular disparity, high-speed
    sensitivity, and the surround suppression underlying motion opponency, achromatic and
    retinotopic.** The consumer further records a **substantive disagreement about direction**, and
    names this entry as where the repair is owed: the source declares this edge as carrying motion
    direction and disparity, while the consumer assigns direction to the **direct V1 4B route**
    instead, on the strength of reversible inactivation — cooling V2 and V3 degrades **disparity**
    tuning disproportionately relative to **direction** tuning. **A causal inactivation result
    outranks an unqualified connectivity statement**, so the payload this edge should carry is
    disparity-weighted rather than direction-weighted.
    **The disagreement is recorded and not resolved here.** Resolving it means changing what the
    payload says, the payload is the source's, and this section's source has not been read against
    the consumer's. **Owed at this section's source.**
  - **→ V3 / V3A**, from layers 2/3. Fan-out: to derive.
  - **→ posterior inferotemporal cortex**, direct — a **jumping projection that skips V4.** Fan-out:
    to derive.
  - **→ V1** (feedback), from layer 2 and the infragranular layers → V1's layer 1. Fan-out: to
    derive.
- **Sizing.** Basis: **per hemisphere.** ~200–220M neurons (scaled from V1 at ≈ 0.715 ×: ~0.55× V1's
  density over ~1.3× V1's area). Fan-in to derive, bounded ≤ 16 bits → **≤ 420 MB** at 210M. The
  ventral-hierarchy shrink is preserved, V2 < V1.
- **Shape.** **Sheet**, rank 4: **(lamina, stripe class, H, W)** — the two sub-element axes are
  orthogonal, eight laminae against three tangential stripe classes, every stripe class carrying the
  full laminar set.
  **Two tangential tilings are measured here, and they are the only measured pitches in this
  section.** The **stripe cycle** repeats every **3.5–4 mm** centre-to-centre; the **intrinsic
  columnar patches** are **211 × 342 µm** ≈ 0.0722 mm², which over V2's ~3,380 mm² (~1.3 × V1's
  surface) gives **~46,800 patches**. **They are not the same tiling and neither is derivable from
  the other.**
  **A caution the shape must carry:** the stripe class is defined by cytochrome-oxidase staining in
  layer 3 while the densest input field is in layer 4, and the two do **not** coincide — so the
  stripe axis is not in register with the lamina axis, and a slice naming both picks out a place that
  is not well defined.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: V2 is inside the V1 loop and the V4 and middle
  temporal loops, all present here. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** A stripe is a full-thickness column, but the tangential compartment
  is **defined differently at different depths and the two definitions are offset**: the darkest
  cytochrome-oxidase staining that names a stripe is in layer 3, while the densest V1 terminal field
  is in layer 4, and the two do not coincide. So a stripe is not yet a single addressable unit, and
  "layer 4 of the thin stripe" names a place that is not well defined.

## V3 / V3A — early extrastriate

- **Function → structure.** The tier above V2, feeding the transition into the dorsal stream. **V3**
  is retinotopic and combines contour and dynamic form with early motion — roughly half of its
  neurons are direction-selective. **V3A** is a distinct area, strongly motion-responsive in humans,
  carrying a full contralateral hemifield map against V3's quarter-field. Laminar sub-structures:
  **eight**, layer 4 undivided. Tangential sub-structure: **to derive** — whether a repeating
  compartmentation of V1's or V2's kind exists here is not established.
- **Inputs.**
  - **← V2**, from layers 2/3 — contour, junction, figure–ground. Fan-in: to derive.
  - **← V1, 4B** — motion direction and disparity, achromatic; a major input. Fan-in: to derive.
  - **← superior colliculus** (`14_brainstem_midbrain_hypothalamus`, relayed through the **pulvinar**
    in `12_thalamus`)**, di-synaptically** — a subcortical route into the motion areas that does
    not pass through V1. Fan-in: to derive.
  - **← higher dorsal and parietal areas** (feedback), principally → layer 1. Fan-in: to derive.
- **Outputs.**
  - **→ middle temporal area** (`04_dorsal_visual_parietal_stream`), direct, onto **layer 4** —
    dynamic form, contour bound to direction of motion. Fan-out: to derive. **The two ends declare
    this payload in the same words and it is the only edge between these two sections of which that
    is true.** The agreement certifies less than it appears to: it is only a check if the two ends
    were written in separate passes, and whether they were is not knowable from either file.
  - **→ V4**, and to **the V4 transitional area, the ventral occipitotemporal area, and the visually
    responsive part of temporal area F** — **carries:** contour and dynamic form. **Payload otherwise
    unknown — owed.** Fan-out: to derive. Three of the four endpoints have no entry anywhere;
    the V4 transitional area is a V3 target and not the ventral posterior area target.
  - **→ V3A, the dorsomedial area, the dorsal prelunate area, the ventral intraparietal area
    (`04_dorsal_visual_parietal_stream`), the ventral lateral intraparietal area** (the ventral
    subdivision of the lateral intraparietal area, same file) — **carries:** dynamic form, and in V3A
    a full contralateral hemifield map. **Payload otherwise unknown — owed.** Fan-out: to derive.
    **A five-endpoint compound line, and the split is owed at this section's source.** Two of the
    five resolve into the dorsal-stream section; V3A is this entry's own other half; **the dorsomedial
    area and the dorsal prelunate area have no entry anywhere**, and they are the source's own
    extrastriate family, inherited and not repairable at this rung.
    **The consumer types its limb** — the ventral intraparietal entry declares this edge as carrying
    dynamic form, contour bound to direction of motion — **so one of the five is typed at the far end
    more fully than the line types it here.**
  - **→ V1 / V2** (feedback), → layer 1 of the target. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** Neurons **to derive** — no clean per-area human count, and
  the area's boundaries are themselves contested. **No store can be stated for this structure**, and
  it is the only one in this section of which that is true.
- **Shape.** **Sheet**, rank 3: **(lamina, H, W)**, eight laminae. Neuron count **to derive**,
  surface area **to derive**, pitch **to derive**, tangential sub-elements **to derive**. **Every
  extent on this structure is open**, which is what it means for a structure to be named and not yet
  specified.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied for the joints present here. Per-edge
  latency: satisfied, all to derive.
- **Justification (biological).** V3's stream assignment is genuinely debated — dorsal-leaning and
  motion-driven in humans, with weaker motion responses in macaque — which is why a section named for
  the ventral stream holds it.

## V4

- **Function → structure.** Intermediate-complexity vision: curvature and shape-part selectivity —
  the first explicit **part** code, above V2's junctions and below inferotemporal objects — colour
  constancy and surface colour with the illuminant discounted, texture and surface segmentation at
  larger scale, and strong attentional gain. Receptive fields larger than V2's, retinotopy coarser.
  Laminar sub-structures: **eight**, layer 4 undivided. Tangential sub-structures: **globs and
  interglobs**, millimetre-sized colour-selective modules, and they carry different content — glob
  cells' responses track perceptual colour space and retain hue tuning across luminance contrast,
  interglob cells prefer luminance contrast regardless of hue.
- **Inputs.**
  - **← V2**, thin and pale stripes — hue, contour and junction, border-ownership, texture. The
    projection is **modular and only partly segregated**: a V4 injection labels thin stripes
    exclusively, or interstripes exclusively, or specific combinations, in interdigitating clusters
    1–3 mm wide. **The two streams converge in some V4 modules and stay separate in others** — the
    first anatomically demonstrated cross-stream convergence in the ventral chain. Fan-in: to derive.
  - **← V3 / V3A** — contour and dynamic form. Fan-in: to derive.
  - **← V1**, direct — sparse, roughly the central 6°. Fan-in: to derive.
  - **← frontal eye field** (`11_frontal_lobe`), terminating in **all cortical layers** — the spatial attentional gain
    signal, an enhancement or suppression applied by location and not a stimulus code. This is the
    edge that supplies the attentional modulation the function asserts, and the frontal eye field is
    the only one of the four attention-implicated structures shown to modulate visual-cortical firing
    through its own direct projection. Fan-in: to derive.
  - **← pulvinar** (`12_thalamus`) — terminating **densely in the middle layers**, the layers a
    forward edge would use rather than the layer feedback uses. Fan-in: to derive.
    **This end declares no payload; the producer declares one, and the two are in tension.** The
    producer types it as a signal that *largely reflects the cortical driver* — orientation, direction
    and motion selectivity, **but not a new representation** — plus attentional gain and cross-areal
    synchrony in alpha/low-beta and gamma. **That is an echo of cortex, where the middle-layer
    termination recorded here is the anatomy of a drive.**
    **The laminar heuristic is what is at stake, and it is load-bearing here because nothing else at
    this end types the edge.** A middle-layer termination is feedforward in form; a cortically-derived
    payload is feedback in content, and a thalamic relay can plausibly be both. **Owed: state whether
    the heuristic is being relied on to assert a payload, or only to record a termination pattern.**
  - **← inferotemporal cortex and higher ventral areas** (feedback), principally → layer 1. Fan-in:
    to derive.
- **Outputs.**
  - **→ inferotemporal cortex**, and to its **posterior division** specifically — intermediate shape,
    surface colour with the illuminant discounted, segmented surface and texture at large scale.
    Fan-out: to derive.
  - **→ V2** (feedback), → layer 1, about 75% of its synapses onto spines there. Fan-out: to derive.
- **Sizing.** Basis: **per hemisphere.** ~50M neurons (best available; the area's boundary is itself
  contested). Fan-in to derive, bounded ≤ 16 bits → **≤ 100 MB.** Ordering V4 < V2 holds.
- **Shape.** **Sheet**, rank 4: **(lamina, module class, H, W)** — eight laminae against a
  glob/interglob tangential division. **Module pitch is measured at 1–3 mm**; surface area is **to
  derive**, so the module count does not follow yet. **The tangential axis here is defined
  functionally and connectionally rather than by a stain** — cytochrome oxidase fails beyond V2 — so
  a module boundary is drawn by the pattern of input each module receives, which is the very edge set
  the shape is being allocated for.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; V4 is inside loops with V2 and with
  inferotemporal cortex, both present here. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** Cytochrome oxidase does not reveal V4's modules — the histochemical
  marker for functionally distinct compartments fails beyond V2 — so V4's tangential sub-structures
  are identified functionally and connectionally, by imaging, single-unit response, and the pattern of
  input each module receives. That is a different basis of definition from the one V1's patches and
  V2's stripes rest on: **a module defined by its inputs is defined by the very edges the entry is
  recording.**

## Inferotemporal cortex

- **Function → structure.** Top of the ventral "what" stream: invariant object and face identity,
  categorical representation invariant to position, size, pose and lighting. **Two divisional
  sub-structures in series** — posterior and anterior inferotemporal cortex — with the complexity
  gradient continuous rather than stepped, since cells needing complex features are already present
  posteriorly and in V4 in small proportion. Laminar sub-structures: **eight**, layer 4 undivided.
  Tangentially the two divisions differ in kind: posteriorly the colour-selective globs of V4
  continue, so its tangential organisation is V4's; anteriorly there are **feature columns** whose
  borders are **not discrete** — a continuous mapping of complex feature space across partially
  overlapping columns.
- **Inputs.**
  - **← V4** → the posterior part of the anterior division — curvature and shape parts,
    illuminant-discounted surface colour, segmented texture, coarse retinotopy. Fan-in: to derive.
  - **← V2** → the posterior division, direct — the jumping projection that bypasses V4, declared at
    both ends. Fan-in: to derive.
  - **← perirhinal cortex, prefrontal cortex and amygdala** (feedback), principally → layer 1.
    Fan-in: to derive.
- **Outputs.** All of these are more numerous from the anterior division than from earlier stages, so
  **the outward fan of the ventral stream is concentrated at its last sub-structure** rather than
  spread along it.
  - **→ perirhinal cortex (areas 35 and 36)** — the identity code, and the anatomical step by which
    the ventral stream reaches the hippocampal formation. Fan-out: to derive.
  - **→ hippocampal formation** — the identity code as one element of an episode. Fan-out: to derive.
  - **→ prefrontal cortex, ventrolateral** (`11_frontal_lobe`) — identity, for controlled retrieval
    and selection. **Two-ended and confirmed on a direct read of the consumer.** **The consumer
    types no payload**, so this end is the only typed one.
    **This entry declares no orbitofrontal output, and the consumer's orbitofrontal entry declares an
    input from here.** That entry reads `← the inferotemporal and temporal cortex, orbital`, and it is a
    separate structure in that file from the ventrolateral one, so the line above does not cover it.
    **That edge is declared at the consumer and at no producer. Owed at this section's source: declare
    it here, or it is withdrawn there.**
    Fan-out: to derive.
  - **→ amygdala** — identity, for affective evaluation. Fan-out: to derive.
  - **→ striatum** — putting the ventral stream's output into the action-selection loop and not only
    into memory and evaluation. Fan-out: to derive.
  - **→ anterior intraparietal area** (`06_posterior_parietal`), from **the lower bank of the
    superior temporal sulcus and the middle temporal gyrus** — **carries:** object **identity**, the
    same categorical code the edges above carry, invariant to position, size, pose and lighting,
    delivered into the grasp channel. **This is the only projection out of the ventral stream and
    into the parietal lobe in this section.** Fan-out: to derive.
    **The consumer's entry asserts that the producer declares nothing on this edge, and that
    assertion is false: this entry declares it, above.** **The repair is owed at the consumer, not
    here** — it is the class of defect where a
    file asserts what another file contains without opening it, and the consumer's own front matter
    records that it did not open the neighbouring files.
    **The edge itself is a candidate and this end should not read as settled.** The source marks it
    Class 1 from a macaque retrograde-tracer study located by web search, with **the abstract only
    read and no full paper opened**, awaiting verification under the verified-only rule.
  - **→ the distributed conceptual / semantic system** (via the temporal pole,
    `07_anterior_temporal_lobe`) — the identity code, view-invariant object and face identity.
    Fan-out: to derive.
    **This endpoint names a system and not a structure, and it is inherited in that form.** §5 requires
    an edge to name its target structure, so this edge does not meet the rule — and the repair is not
    available at this rung. The temporal pole is a named region with an entry, and the consumer
    declares `← anterior inferotemporal cortex / ventral temporal — view-invariant object and face
    identity`, so a direct producer-to-temporal-pole edge has a far end that already declares it.
    **Terminating this edge on the temporal pole here would nonetheless add a claim the source does not
    make**, and §2 forbids that at this rung. **Recorded, owed at the source**, where the line needs a
    reference for whichever form it takes.
    **What lies beyond the temporal pole is not this entry's to name.** That consumer's six outputs
    carry the amodal concept onward, and it records that *amodal concept* is a phrase and not a type —
    no units, no range, no coordinate frame — so the system this edge ultimately serves is **untyped at
    the only end that can type it.**
- **Sizing.** Basis: **per hemisphere.** ~120M neurons, order-of-magnitude — no clean primary human
  count exists. Fan-in to derive, bounded ≤ 16 bits → **≤ 240 MB.** V1's density-derived figure does
  not carry here: V1 is the ~60,000/mm³ packing outlier, while this is ordinary association cortex at
  ~20–40,000/mm³.
- **Shape.** **Sheet**, rank 4 posteriorly and **rank 3 anteriorly**, and the change is the finding:
  **(lamina, division, H, W)** where the posterior division continues V4's glob tangential
  organisation, but the anterior division's feature columns have **no discrete boundaries** — a
  continuous mapping of feature space across partially overlapping columns. **A continuous map has no
  compartment axis to index**, so anteriorly the tangential axis is a coordinate rather than a
  sub-element list, and what an edge terminating "on a column" selects is **to derive**. Extents: **to
  derive** throughout.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied for the joints present here; the return
  limbs from perirhinal cortex, prefrontal cortex and amygdala close loops whose far ends are outside
  this section. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** This is where the payload stops being a signal and becomes a
  category: "the identity of the thing," with no coordinate frame, is a phrase and not a type, and it
  is the first stage in the visual line of which that is true. The structural consequence is that no
  units can be stated on any output edge above.

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Retina — ganglion cells | per eye | ~1.0–1.2M | ≤ 16 | ≤ 2.40 MB |
| Retina — photoreceptors | per eye | ~97M | 0 | 0 |
| Retina — horizontal / bipolar / amacrine | per eye | to derive | ≤ 16 | to derive |
| Optic chiasm | both eyes | none | — | 0 |
| Lateral geniculate nucleus | per side | ~1.77M | ≤ 16 | ≤ 3.54 MB |
| V1 | per hemisphere | ~280–310M | 12–14 | 450–525 MB |
| V2 | per hemisphere | ~200–220M | ≤ 16 | ≤ 420 MB |
| V3 / V3A | per hemisphere | to derive | ≤ 16 | to derive |
| V4 | per hemisphere | ~50M | ≤ 16 | ≤ 100 MB |
| Inferotemporal cortex | per hemisphere | ~120M | ≤ 16 | ≤ 240 MB |
| **stated total** | mixed | | | **~1.22–1.29 GB** |

**The total is a floor, not a requirement.** Two structures are uncounted, every fan-in but V1's is
at the 16-bit ceiling rather than at a measured value, and **state memory and edge storage are not in
this table at all** — edge storage in particular cannot be sized until the scheduling discipline is
set, and it is not.

**Memory is not a binding constraint here and the figure is not to be reduced.** It is a derived
requirement recorded as found.
