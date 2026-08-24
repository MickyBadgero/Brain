# Brain architecture — 04 dorsal visual / parietal stream

**Date:** 2026-08-23
**Derived from:** `human_brain_04_dorsal_visual_parietal_stream` — the middle temporal
area, the medial superior temporal area, and the ventral and lateral intraparietal areas. **One
source file, and no other content source.**

**Cross-file checks contained in this file.** Each line names another file that was held open beside
this one and whose shared edges with it are diffed and stemmed below.

- `01_visual_pathway`, `06_posterior_parietal`.
- `11_frontal_lobe`, `14_brainstem_midbrain_hypothalamus`. **Sixteen shared edges
  diffed and stemmed. Four marks in this file discharged, three of them one repeated claim that the
  frontal file names no pursuit area — it names one, as a sub-element, on two output lines. One
  reciprocal pair found to be two-ended in both directions with entirely different payloads on the
  two limbs.**
- `10_cerebellum`. **Checked and closed as carrying no edge between the two files.** The Purkinje
  cells of the cerebellar nodulus and uvula, named at the medial superior temporal entry as where the
  tilt-versus-translation ambiguity is resolved, are **an upstream stage and not an endpoint of this
  section**: the edge declared here is `← vestibular nuclei by way of the thalamus`, and the
  cerebellar stage sits behind it. **That route runs through `03_other_senses`, which declares the
  flocculonodular limb**, so the upstream naming owed at that entry resolves through a file already
  checked rather than by adding a far end in `10_cerebellum`.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file has been read against this one; an endpoint with no stem is one whose far end has
not yet been opened beside this file, and it is not a claim that none exists.

**Counting basis is uniform for the first time in the map: per hemisphere, all four structures.**
Four isocortical areas, each with the same eight laminar sub-elements, each with a stated neuron
count. Chunk 02's basis changed four times within one section and broke down entirely above the
parabelt; chunk 03 could not count eleven of twelve populations. **Here every row is priced and the
basis never moves.**

**And that is the inversion this section is for. The counts are the firmest in the map and the
payloads are the least settled.** The source records 52 edge lines, 29 in and 23 out, audited from
both ends — and what the audit found was disagreement: payloads owed at one end and typed at the
other, a direction attribute the two ends dispute, a route marked contested, a false attribution
pointer removed. **A section can be well counted and badly typed, and this one is.**

**Where visual information stops being about recognition.** These four areas re-express visual
information in coordinate frames for action. The characteristic operation is therefore a
**coordinate transform**, and the source states its mechanism: **gain fields — a sensory receptive
field multiplicatively modulated by eye and head position.**

---

## Structural invariants

**Whole-pathway co-instantiation.** The loops here close inside the section and outside it in equal
measure: the middle temporal area and the medial superior temporal area are reciprocal; the medial
superior temporal area and the ventral intraparietal area are both reciprocally connected with a
**frontal pursuit area that has no entry anywhere in the source**; the middle temporal area sends
feedback to V1 and V2 in file 01. **Three edges in this section terminate on a structure the
description does not describe**, which is the same class of defect the auditory section found at the
nuclei of the lateral lemniscus, and here it is three edges rather than one.

**Per-edge latency: every edge reads *to derive*, and this section makes that fail in two new
ways.**

1. **A pair of edges whose payloads are identical and whose latencies are not.** The direct route
   from V1 layer 4B carries direction and disparity on a **fast few-hop route** — fewer stages, so
   it arrives earlier — and the source states plainly that **the payload is the same as the indirect
   routes carry and the latency is not.** So the only thing distinguishing the direct route from the
   route through V2 and V3 is the field that reads *to derive*. **This is the medial superior
   olive's problem in a new place:** set the latencies equal and the direct route stops being a
   different edge.
2. **A payload with a deadline against an external event.** The corollary discharge reaching the
   lateral intraparietal area says *the eye is about to move, by this vector*, and it drives
   **predictive remapping** — cells shift receptive fields toward the post-saccadic location
   **before** the movement. The source states the constraint directly: this payload is only useful
   if it arrives before the eye moves. **Arrival order is part of correctness here, not of
   performance**, and it is ordered against an event outside the section rather than against another
   edge. **The map has had no payload of that form before.**

**Two new classes of thing the shape slot cannot address, and neither is a gap in the description.**

- **Two maps superimposed on one sheet.** The middle temporal area carries **direction columns** and
  **disparity columns** at once, plus a **speed clustering that is explicitly not columnar.** The
  source draws the consequence: a position in this area has *both* a direction preference and a
  disparity preference, and **an edge terminating on it terminates on both.** Two superimposed maps
  is a different object from one compartmentation, and one sub-element name is insufficient for it.
- **A sub-element that is not a place.** In the medial superior temporal area's dorsal division,
  heading-tuned cells divide into **congruent** and **opposite** cells by the *relation* between
  their visual and vestibular tunings. They are interleaved, with no spatial segregation found.
  **Every other sub-element anywhere in this section is a place, and an edge terminates on a place** —
  so **what it would mean for an edge to terminate on the congruent cells and not the opposite ones
  is owed**, and the source records that it may not be answerable in the slot's present form.

**No global clock may be assumed**, and no latency in this section is stated in steps.

---

## Middle temporal area

- **Function → structure.** Motion processing: direction selectivity, speed tuning, **motion
  integration** — local components resolved into global pattern motion, solving the aperture
  problem — motion-in-depth and disparity, and motion opponency with antagonistic surrounds
  yielding figure–ground from motion. **Laminar sub-elements: eight** — 1, 2, 3, 4, 5a, 5b, 6a, 6b,
  layer 4 undivided. **A myelin-dense grey-matter patch**, which is the basis of its architectonic
  delineation.
- **Inputs.**
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
    owed at the V2 entry in `01_visual_pathway`. **That entry has now been read against this one, and
    what it declares is narrower than assumed here: it declares no payload on this edge at all.**
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
    **This edge is not declared at this end only.** That entry declares `→ the middle temporal area, terminating in all cortical layers` **on its own
    output line, with the same lamination.** **Two-ended, and this end is the typed one** — the
    producer carries no payload for it.
    **The same phrasing is claimed by a third structure in a fourth file, and that is the finding.**
    The frontal entry records that `01_visual_pathway`'s V4 declares
    `← frontal eye field, terminating in all cortical layers — the spatial attentional gain` **with no
    matching output anywhere in the frontal file**, and notes that the nearest thing that does exist
    is the edge to this area — *the same lamination and the same phrasing, to a different consumer in
    a different file.* **With both consumers read, the pair separates cleanly**: this edge is
    two-ended and V4's is producer-less. **So the shared wording is not evidence that the two
    are one edge mis-copied**; it is evidence that one general description — a laminar-nonspecific
    frontal attentional projection to extrastriate cortex — was instantiated at two consumers and
    declared back at only one. **Owed at the source: establish the V4 limb at the producer, or
    withdraw it there.**
  - **← the medial superior temporal area** and **← posterior parietal areas** (feedback), onto
    **layer 1** — payloads **owed**. The second endpoint **is a class and does not resolve**: none
    of the posterior parietal file's five entries declares an output here, and the supramarginal
    gyrus declares traffic in the opposite direction only.
- **Outputs.**
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
- **Sizing.** Basis: **per hemisphere.** **~15M neurons**, high variance, though the area is fairly
  well bounded by a myeloarchitectonic border and its motion selectivity. Fan-in: **to derive on
  every edge.** At the 16-bit ceiling: **30.00 MB.**
- **Shape.** **Sheet**, rank 4: **(lamina, direction column, disparity domain, position)** — and the
  third axis is not a refinement of the second. **Direction columns** of smoothly varying preference
  run beside a matching set preferring the locally opposite direction, forming **pinwheels** where
  the area lies on the surface rather than in a sulcus. **Disparity columns** form a topographic map
  in millimetre-sized interleaved domains, and **some regions contain neurons with poor disparity
  tuning, so that map does not tile the area uniformly.** **Speed preference is clustered and
  explicitly not columnar.**
  **A coverage mismatch recorded rather than smoothed.** Imaging finds only **3–4 segregated motion
  domains**, each **2–3 mm²**, spaced **2–3 mm**, occupying roughly **15%** of the surface — while
  about **85%** of the area's neurons are directionally selective, a **5.7-fold** discrepancy,
  recomputed. **Either the domains are not where most direction selectivity lives, or the imaging
  measures something narrower than direction selectivity. Unresolved.**
- **Edge latency.** All edges **to derive** — and this is the structure where that costs the most,
  because **the direct and indirect routes carry the same payload and differ only in arrival time.**
- **Invariant conformance.** Co-instantiation: feedback loops close into file 01 and into the medial
  superior temporal area. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The stated function demands an internal edge that is recorded
  nowhere.** Integrating local component motions into one pattern motion **requires signal to cross
  direction columns**, since the components and the resolved pattern have different directions by
  construction. **So an internal edge crossing the direction map is demanded by the stated function
  and is not recorded** — the sharpest dangling requirement in the visual line.

## Medial superior temporal area

- **Function → structure.** Global optic-flow structure over large receptive fields —
  expansion/contraction, rotation, deformation, translation — **heading** as the focus of expansion,
  **self- versus object-motion disambiguation**, and smooth-pursuit signals. **First dorsal stage
  that is not purely visual.** **Divisional sub-elements: two** — a **dorsal division** (optic flow,
  heading, self-motion; large receptive fields) and a **lateral division** (object motion, smooth
  pursuit; smaller fields); **splitting them into separate entries is owed.** **Laminar
  sub-elements: eight.**
  **Visual and vestibular heading cues are carried by the same single neurons**, not by two
  populations that meet later: individual dorsal-division cells are tuned to both and combine them
  **linearly with subadditive weights.** Most cells prefer lateral headings and are broadly tuned,
  **which makes the population most discriminating around straight ahead.**
- **Inputs.**
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
    not simply downstream.** **The frontal lobe file does name a pursuit area, so this edge does not
    lack a far end.** That file's frontal eye fields entry declares
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
- **Outputs.** **→ the ventral intraparietal area** — global optic-flow structure plus **heading**
  and the self/object attribution. **→ the medial intraparietal area** (`06_posterior_parietal`), **→ the supramarginal
  gyrus** (`06_posterior_parietal`), **→ the lateral intraparietal area** — payloads **owed** here, and two of the three
  **→ the pursuit area of the frontal eye
  field** (`11_frontal_lobe`), reciprocally — pursuit and gaze-target velocity. **Two-ended and
  confirmed**; the producer's reciprocal limb is declared there from the same sub-element,
  and is untyped, **so this end carries the payload for both directions.** **→ the middle temporal area**
  (feedback), onto layer 1 — **owed.**
- **Sizing.** Basis: **per hemisphere.** **~15M neurons**, and **softer than the middle temporal
  area's**: no comparable myeloarchitectonic signature and retinotopy crude to absent, **so both its
  borders and its count are loose.** At the 16-bit ceiling: **30.00 MB.**
- **Shape.** Rank 3: **(lamina, division, position)** — eight laminae, two divisions, and
  **tangential sub-elements unknown**: no columnar or compartmental map was found here, unlike the
  area immediately upstream, which has two. **Whether that reflects the anatomy or the reading is not
  established.**
  **And a third division that is not spatial at all** — the congruent and opposite cells above.
  Under cue combination the two behave in **opposite directions**: congruent cells become **more**
  sensitive, paralleling the animal's behavioural improvement, and opposite cells become **less**
  sensitive.
- **Edge latency.** All edges **to derive** — and latency is the evidence the contested vestibular
  route turns on, so **the field that would settle the route is the field the section cannot state.**
- **Invariant conformance.** Co-instantiation: three of this structure's edges point at a frontal
  pursuit area with no entry. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **What the opposite cells are proposed to be for is separating
  self-motion from object motion.** A cell whose visual and vestibular heading preferences are
  inverted reports the **disagreement** between the two cues, and a disagreement between optic flow
  and inertial motion **is the signature of something in the world moving independently of the
  observer.** A mixed population is proposed as the substrate for that causal-inference problem, and
  a linear decode of it approximates marginalising self-motion out. **Recorded as a candidate
  mechanism rather than a finding:** peer review noted that the analyses did not isolate the opposite
  cells and test performance with and without them, so the contribution attributed to them is
  inferred from the population result rather than demonstrated on that subpopulation.
  **One causal asymmetry that complicates the entry's own account.** Microstimulation here **biased
  heading judgements made from optic flow** but **did not** significantly affect vestibular heading
  judgements — even though single cells carry both cues. **The two payloads are not symmetrically
  read out downstream**, and the stage should not be taken to contribute to both equally.

## Ventral intraparietal area

- **Function → structure.** **Reference-frame transformation** — coding of motion and location in
  frames other than the retinal one, **implemented by gain fields: a sensory receptive field
  multiplicatively modulated by eye and head position.** Multimodal: visual motion and optic flow,
  vestibular, tactile and auditory, and **strongly bimodal visual-plus-tactile with facial and head
  tactile receptive fields aligned to visual ones** — peripersonal and defensive space. **Divisional
  sub-elements: two**, medial and lateral, **their separate payloads owed. Laminar sub-elements:
  eight. Tangential sub-elements: unknown.**
- **Inputs.** **← the middle temporal area** — motion in **eye-centred** coordinates, **and it stays
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
  candidate is recorded. Fan-in: to derive. **← somatosensory (facial / head tactile)** — touch location in a **skin-surface**
  frame.
- **Outputs.** **→ premotor area F4** — object location and motion in **head- and body-centred
  coordinates**, peripersonal and defensive space. **The payload change at this stage is the
  coordinate frame and nothing else**: the same objects go in and come out, re-expressed in a frame
  the body can act in. **That is what the gain fields buy, and it is the reason the entry exists.**
  **The far end does declare this edge and does name F4** (`11_frontal_lobe`). That file's premotor
  entry declares
  `← the ventral intraparietal area, terminating on F4` — **the edge and the sub-element both, and it
  is one of three parietal inputs there written by terminating sub-element**, alongside the anterior
  intraparietal area on F5 and the medial intraparietal area on F2. **So the F-numbering this line
  asked for is the convention in use at the far end.** **That end is untyped**, and the coordinate
  frame this line makes its whole justification exists only here. **→ the lateral intraparietal area** — body-centred locations for
  prioritisation, and **the two ends disagree by one frame.** **→ the medial intraparietal area** (`06_posterior_parietal`) —
  body-centred locations for reach; **the consumer's declaration is the vaguer.** **→ the anterior
  intraparietal area** (`06_posterior_parietal`) — head- and body-centred location and motion for grasp: **the one edge out of
  this entry whose two ends agree, in the same words.** **→ the pursuit area of the frontal eye
  field** (`11_frontal_lobe`), reciprocally — heading in some frame, **owed**. **The far end is not missing here either** — that entry declares
  `→ the ventral intraparietal area, reciprocally, from the pursuit area`, and the qualification
  recorded at the medial superior temporal entry above applies here identically: **the sub-element is
  named there and not described there.**
- **Sizing.** Basis: **per hemisphere.** **~12M neurons**, **very high variance — the softest count
  in the map**: the area sits in the fundus of the intraparietal sulcus, lightly myelinated, with no
  clean architectonic border, and **the macaque area has expanded into several human parietal
  areas.** At the 16-bit ceiling: **24.00 MB.**
- **Shape.** Rank 3: **(lamina, division, position)**, tangential organisation unknown.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the gain-field mechanism requires the eye- and
  head-position signal to reach the same cells that carry the sensory receptive field, and **the edge
  carrying it is owed at its source** — so **the mechanism the entry rests on has no declared
  input.** Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The transformation is not applied to everything that arrives.**
  Vestibular heading is **body-centred**, transformed out of the head-centred frame it arrives in;
  visual heading from optic flow is **approximately eye-centred and not transformed** — tested
  directly as a hypothesis and refused, with **no neuron found with head-centred visual heading
  tuning** and only a small proportion intermediate. **So the intuitive engineering solution — bring
  both cues into a common frame, then combine — is not what happens.** Across this area and the
  medial superior temporal area the visual signal stays mainly eye-centred and the vestibular signal
  is head- or body-centred, **and single neurons nevertheless combine them. Whatever reconciles the
  frames is not a change of frame before combination.**
  **The vestibular frame is further hybrid and gaze-dependent:** this area shows **either** a
  body-centred or a world-centred frame **depending on gaze direction** — a flexible switch between
  two frames, not a fixed one.
  **And the frame may be a property of the measurement rather than of the area.** Visual receptive
  fields mapped with **moving bars** are reported **head-centred in a substantial proportion** of
  neurons, while visual heading from **large-field optic flow** is eye-centred with no head-centred
  cells found. **The same modality in the same area gives different answers, and the difference
  tracks the stimulus and the property measured rather than the cells. Unresolved** — and for a
  description whose purpose is to state what is on a wire, the warning is that **the frame of a
  payload here may not be well defined independently of what is being asked of it.**
  **The disagreement is not symmetric, and two facts about it are now settled.** Head position
  relative to the body was **not manipulated** in the moving-bar studies, so head- and
  body-centred frames were not separable there — one side of the disagreement rests on a design
  that could distinguish the frames and the other on designs that could not. And **a shift of a
  tuning curve is hard to distinguish from a change in response gain** in this area, because most
  of its neurons prefer lateral motion and are therefore monotonically tuned around straight
  ahead, **unless the complete tuning function is measured** — so a frame claim and a gain claim
  are separable only under that condition. **What remains unresolved is named rather than open:**
  optic-flow tuning and receptive-field shift have not been tested in the same neurons, and that
  is the experiment the resolution requires. **Owed at the source, with the research specified.**
  **And the frame table for this structure is four rows, not two.** Vestibular heading is
  **body-centred**; visual heading from optic flow is **eye-centred**, with 52% of classifiable
  neurons significantly eye-centred and **none** head- or body-centred; facial **tactile**
  receptive fields are **head-centred**; **auditory** receptive fields lie on a **continuum
  between eye- and head-centred.** **Four modalities arrive at one structure in four different
  frames**, and a subset of neurons was tested with two of the protocols, so **the disparity holds
  within single multisensory cells and is not a difference between two populations.**

## Lateral intraparietal area

- **Function → structure.** A **priority (salience) map**: a retinotopic map ranking locations by
  behavioural priority — bottom-up salience plus top-down attention plus reward — **the peak
  selecting the next saccade target**, with selection as **competition among locations through
  lateral inhibition.** **Supramodal**: visual and, in eye-centred coordinates, auditory saccade
  targets. **Predictive remapping**: just before a saccade, cells shift receptive fields toward the
  post-saccadic location, driven by **corollary discharge.** Eye-position gain modulation.
  **Laminar sub-elements: eight. Tangential sub-elements: none reported.**
  **Divisional sub-elements: two, and they are architectonically defined before they are functionally
  defined.** The **ventral subdivision** is **densely myelinated**; the **dorsal subdivision** is
  **lightly myelinated**; and receptor mapping separates them again on a different measure —
  N-methyl-D-aspartate, α1-adrenergic and 5-HT1A receptor densities are all **higher in the dorsal**
  subdivision. **Two independent stains agreeing on one border is a stronger basis than either
  alone**, and it is firmer footing than the tangential compartments recorded at V4 and the middle
  temporal area, which rest on function and connection.
- **Inputs.** **← the middle temporal area** — visual motion, retinotopic, **reaching the ventral
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
- **Outputs.** **→ the superior colliculus** (`14_brainstem_midbrain_hypothalamus`), from the
  **ventral** subdivision onto its intermediate and deep layers — the priority map: **one scalar per
  retinotopic location**, peak specifying the next saccade target. **The payload is a scalar field over space and it is deliberately
  modality-free: what it has thrown away — colour, identity, pitch — is as important as what it
  keeps.** **The ventral subdivision carries this edge and the dorsal one does not**, so a consumer
  reading "the lateral intraparietal area projects to the colliculus" **is reading half the area.**
  **→ frontal eye field** (`11_frontal_lobe`), **→ prefrontal area 46** (`11_frontal_lobe`),
  **→ the anterior intraparietal area** (`06_posterior_parietal`), **→ the angular gyrus**
  (`06_posterior_parietal`), **→ parahippocampal temporal area TF** — the same priority map; two far
  ends agree and are untyped, one declares nothing, one is unchecked.
  **The two frontal limbs are confirmed and both are two-ended in both directions.** The
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
- **Sizing.** Basis: **per hemisphere.** **~20M neurons**, high variance but **firmer-bordered than
  the ventral intraparietal area** — in the lateral bank of the intraparietal sulcus with two
  myeloarchitectonic zones. At the 16-bit ceiling: **40.00 MB.**
- **Shape.** Rank 3: **(lamina, subdivision, retinotopic position)** — and **the subdivision axis
  carries a signed payload difference.** The ventral subdivision holds a **single topographic map of
  the contralateral hemifield** with a foveal representation rostrally, connects strongly with the
  frontal eye field and the deep collicular layers, and a GABA-A agonist injected into it **sharply
  reduces express saccades** while the same injection dorsally does not. Along the dorsal-to-ventral
  axis the population shifts from cells driven by **visual** events to cells driven by **visual and
  saccadic** events together. **So the map is not uniform and an edge terminating "on the lateral
  intraparietal area" is under-specified.**
- **Edge latency.** All edges **to derive** — and **one of them has a deadline**: the corollary
  discharge is only useful if it arrives before the eye moves.
- **Invariant conformance.** Co-instantiation: the priority map's consumers are mostly outside this
  section. Per-edge latency: satisfied, all to derive — **and unsatisfiable in spirit for the
  corollary discharge, whose correctness is an ordering constraint.**
- **Justification (biological).** **The intrinsic loop is asymmetric and the asymmetry is the
  finding.** Retrograde tracing found **ventral → dorsal point-to-point**, described as sensory-like,
  one location talking to its counterpart; and **dorsal → ventral widespread**, not point-to-point,
  one location talking to many. **A topographic forward limb and a divergent return limb are the
  anatomy of a map being read out against a broadcast, not of two copies of one map.** It is offered
  as the intrinsic circuit underlying the observation that a cell's **motor** response field is
  spatially distinct from its **sensory** receptive field — **a payload change inside one entry, and
  the first the file has had to record at that scale.**
  **And the mechanism the Function field rests on has no declared substrate.** Selection is stated to
  be competition among locations through lateral inhibition, which requires within-map inhibitory
  edges between separated locations, **and no such edge is recorded** — the divisional edges above
  are between subdivisions, not across the map. **Same shape of hole as the gain-field edge owed at
  the ventral intraparietal area.**

---

## Section totals

| # | structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|---|
| 1 | Middle temporal area | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB |
| 2 | Medial superior temporal area | per hemisphere | ~15M | ≤ 16 | ≤ 30.00 MB |
| 3 | Ventral intraparietal area | per hemisphere | ~12M | ≤ 16 | ≤ 24.00 MB |
| 4 | Lateral intraparietal area | per hemisphere | ~20M | ≤ 16 | ≤ 40.00 MB |
| | **stated total** | per hemisphere | **~62M** | | **124.00 MB** |

Recomputed from the counts and the 16-bit ceiling: **124.00 MB**, **62M neurons**, and — for the
first time in the map — **no row reads *to derive* and no basis changes within the section.**

**That is the section's first finding and it is a negative one about the other sections rather than a
positive one about this.** Chunk 02's basis moved from per ear to per hemisphere to per side and then
broke down; chunk 03 could price one population out of twelve. **Here all four rows price, and the
total is exact given the ceiling.** What makes it exact is that **no fan-in in this section is
known** — every edge reads *to derive* — so every neuron sits at the 16-bit cap and nothing is
derived below it. **The total is clean because nothing was measured, not because everything was.**

**The counts themselves are soft and they say so, in a graded way worth carrying.** The middle
temporal area is "fairly well bounded" by a myeloarchitectonic border; the medial superior temporal
area is "softer, with no comparable signature and retinotopy crude to absent, so both its borders and
its count are loose"; the lateral intraparietal area is "firmer-bordered" with two myeloarchitectonic
zones; and the ventral intraparietal area is **the softest count in the map**, lightly myelinated
with no clean border, **and the macaque area has expanded into several human parietal areas.**
**A count whose region has split between species is not the same kind of number as one whose region
has a stain.**

**Three stated functions in this section have no declared substrate, and it is the same shape three
times.**

1. **Motion integration across direction columns** — demanded by the middle temporal area's stated
   function, recorded nowhere.
2. **The gain-field multiplication** — the ventral intraparietal area's whole reason for existing,
   and the edge delivering eye and head position to those cells is **owed at its source.** **The
   gap is two lines wide, not one:** the entry declares an eye-in-head line whose producer is
   unnamed, and **no head-on-body line at all**, while head-on-body is a separately measured
   variable in that area rather than a loose synonym for gaze.
3. **Lateral inhibition across the priority map** — what the lateral intraparietal area's selection
   rests on, with no within-map inhibitory edge recorded.

**In each case the Function field names a mechanism and the Internal-structure field cannot show it.
That is a different defect from a missing payload: the edge is not merely untyped, it is absent while
being required.**

**And the mechanism in the middle of that list is one the model cannot express even if the edge were
declared.** The transform is stated as **multiplicative** — a receptive field modulated by eye and
head position. **The threshold-gate model has equal weights and no multiply**, by construction, which
is what makes the stored value a single threshold. **So this section's characteristic operation is
the one arithmetic the sizing model excludes**, and that is not a gap in the description.

**The two-ended audit is this section's method and its result is disagreement.** Of the 52 edge lines
the source records, the last pass found: a direction attribute the two ends dispute, with the
inactivation result outranking the connectivity statement; four payloads owed at one end and typed at
the other; **one edge whose consumer attributed its typing to a producer that declares nothing**, now
removed; two frames disagreeing by one step; a route marked contested with **no declared substrate at
either end**; and **exactly one edge whose two ends agree in the same words.** **A section whose
counts all close and whose payloads mostly do not is the inverse of chunk 03, and the two together
say the sizing arithmetic and the payload description fail independently.**

**Memory is not a binding constraint and none of these figures is to be reduced.** The total here is
about a quarter of the auditory section's and about a tenth of the visual section's; **state memory
and edge storage are not in it.**
