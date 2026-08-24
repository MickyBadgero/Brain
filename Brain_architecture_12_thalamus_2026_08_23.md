# Brain architecture — 12 thalamus

**Date:** 2026-08-23
**Derived from:** `human_brain_12_thalamus_2026_07_27.md` — the thalamic nuclei that are not sensory
relays, plus the adjacent zona incerta. **One source file, and no other content source.**

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed.

- `01_visual_pathway`.
- `08_medial_temporal_lobe`, `11_frontal_lobe`. **Twenty-one shared edges diffed and
  stemmed. Three marks in this file confirmed to hold, including the section's load-bearing gap; six
  wrong claims about this file's mediodorsal entry discharged at the far end; and the corticothalamic
  return limbs this file declares as two class endpoints found to be declared at no cortical consumer
  at all.** **`11_frontal_lobe`'s five prefrontal consumers name this file's mediodorsal entry by the
  heading it carries here**, so the two ends agree on the endpoint string and not only on the edge.
- `09_basal_ganglia`. **Two shared edges diffed. The mediodorsal entry's limbic limb is distinguished
  at both ends: this file declares it reaching the mediodorsal nucleus via the ventral pallidum,
  beside the dorsal basal-ganglia line rather than inside it, and the far end declares value as
  computed at the ventral pallidum rather than relayed.** **The two sources do not carry the same
  payload** — tonic inhibition alone from the dorsal nuclei, inhibition plus a computed relative value
  from the ventral pallidum — **so keeping the two lines apart here is load-bearing and not a
  labelling preference.** **The far end names this nucleus *mediodorsal thalamus* where this file's
  heading is *Mediodorsal nucleus*; the endpoint strings do not match and the edge cannot pair.**
- `10_cerebellum`, `16_spinal_cord`. **Nine shared edges diffed and stemmed. Five
  two-ended, two of them carrying the same measured figures at both ends; one stale mark discharged at
  `10_cerebellum`; this section's load-bearing gap traced to the exact clause in the producer that
  creates it; one endpoint of `16_spinal_cord`'s found to name no entry here; and the zona incerta's
  producer-only count raised from three to four.**
- `13_neuromodulatory_systems`, `14_brainstem_midbrain_hypothalamus`. **Fourteen
  shared edges diffed and stemmed. Seven two-ended; two ascending class endpoints declared at their
  producers close as negatives against every entry here; three of the zona incerta's outputs found to
  have no consumer end at either far file; one input here found to have no producer end; and one
  thalamic relay the far file depends on twice confirmed absent from this section's eight entries.**
  **Neither far end is derived from this file, nor this file from them**,
  which is what makes the agreements below a check rather than a copy.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file has been read against this one; an endpoint with no stem is one whose far end has
not yet been opened beside this file, and it is not a claim that none exists.

**Counting basis is uniform in this section, and that is itself worth stating**, because the section
before it was not: every structure here is counted **per side**. The three first-order sensory relays
are described in their own pathway files; the fourth, the posterior / ventromedial-posterior
interoceptive relay, is here because its cortical target is described later.

**Far-end dependencies, and which have now been read.** Edges in this section reach files 1, 4, 5, 8,
9, 10, 11, 13, 14, 16 and 17. **Files 1, 8, 11, 13 and 14 have been held open beside this one** and
their shared edges carry a stem and a mark. **Files 4, 5, 9, 10, 16 and 17 have not**, and every far
end reaching them below is recorded as the source states it and is unchecked at the other end — the
second of the two permitted responses, and the one still taken for those six.

---

## Structural invariants

**Whole-pathway co-instantiation.** This section is not a chain with loops hung off it; it is a set
of **nested loops sharing one gate.** The thalamic reticular nucleus receives a collateral copy of
the outgoing traffic of each relay nucleus and returns inhibition to it, so each relay closes a loop
through the gate — **seven such loops are named here**, and the gate **has no cortical output at
all.** A structure whose only projections are back into the structures that drive it cannot be
brought up later, because it has no function outside the loops it closes. Two of the seven loops are
declared at the producer's end only: the reticular nucleus claims outputs to the anterior nuclei and
the intralaminar nuclei, and neither of those entries declares the input.

The second loop family is corticothalamic and closes outside this section. The mediodorsal nucleus
takes a layer-5 driver and a layer-6 modulator from prefrontal cortex and returns amplification to
five prefrontal consumers; the pulvinar takes the same pair from visual cortex and returns to four
named cortical areas; the ventral anterior / ventral lateral group is reciprocal with primary motor
cortex; the posterior / ventromedial-posterior territory is reciprocal with the insula; the anterior
nuclei's return arm from retrosplenial cortex is declared at the consumer and **missing from this
end** — a loop with one limb recorded.

**Per-edge latency. This section names three, and they are the first measured edge latencies to
appear in the architecture.** The lamina-I stream into the posterior / ventromedial-posterior
territory is not one edge with one delay but **three labelled lines with three measured mean central
conduction latencies**: thermoreceptive-specific ≈ **59 ms**, polymodal nociceptive ≈ **72 ms**,
nociceptive-specific ≈ **131 ms**. Recomputed: the spread is **2.22×** and the cold signal precedes
the nociceptive one by **72 ms**.

**That is the per-edge-latency invariant's strongest support anywhere in the map so far, and the
reason is the granularity.** The invariant says no two edges need the same latency. Here the
heterogeneity is *inside a single anatomical projection* — one origin, one target, three cell
morphologies, three delays — so a uniform delay would not merely be coarse, it would **merge three
lines the biology keeps separate** and destroy the arrival order that is the finding. Every other
edge in this section reads **to derive**.

*(The three figures are Class 1 from the source, cat, antidromically identified spinothalamic
neurons. The reading placed on them — that intra-edge heterogeneity is a stronger case for the
invariant than inter-edge heterogeneity — is Claude's, offered to be checked.)*

**No global clock, and this section is where the cost of assuming one would be visible.** The gate
above sits inside seven loops that also carry the corticothalamic loops inside them. A loop with
real heterogeneous delays settles by its own dynamics; the same loop broken by registers becomes an
iterated map whose trajectory depends on the update rate. With loops nested three deep here, uniform
delay is a substitution and not an approximation.

---

## The payload in this section is a gain, and the sizing model has no term for one

**Recorded up front because it bears on every entry below, and marked as what it is: Claude's
reading of the source, offered to be checked. The source's descriptions are Class 1 and Class 2 as
each entry marks them; the consequence drawn here for §6's model is not the source's claim.**

The threshold-gate model of §6 is a **count of active inputs against a stored threshold**, with
equal weights. It has no sign and no scaling term. Four of this section's eight structures carry
payloads it cannot express:

- **The mediodorsal nucleus does not relay categorical content.** Silencing it does not stop
  prefrontal cortex receiving task information; it stops that cortex *holding* it. What leaves is
  **amplification of the consumer's own recurrent connectivity** — a gain applied to a cortical
  loop, not a message on a wire. All five of its cortical output edges carry this and nothing else.
- **The pulvinar's output is two things on one wire**: content that largely *reflects* its cortical
  driver rather than adding a representation, plus **attentional gain and cross-areal synchrony**.
  The second is the part that is its own, and it is a coordinating payload, not a content one.
- **The thalamic reticular nucleus carries inhibition and no content**, to seven or eight thalamic
  consumers, and projects nowhere else.
- **The zona incerta carries inhibition and no content** on its signature thalamic edge and on its
  edge to the reticular nucleus.

**Two separate gaps, and they are not the same gap.**

1. **Inhibition has no term.** A count of active inputs has no sign, so an inhibitory edge cannot be
   counted. This is adjacent to the finding already recorded against the outer retina — where
   hyperpolarisation *is* the excitatory response — but it is a different failure: there the sign
   convention is inverted, here there is no sign at all, and inhibition is the *function* of two of
   these structures rather than a stage inside one.
2. **Gain has no term either, and this one is worse.** A modulatory edge does not add to the
   consumer's input count; it changes the consumer's **transfer function**. Under equal weights the
   only quantity a neuron holds is its threshold, so the only place a gain could land is on the
   threshold — and writing a threshold is the **learning rule, which is not set.** So a modulatory
   edge has nowhere to go at all: expressed as an ordinary input it asserts content the edge
   explicitly does not carry, and expressed as a threshold change it assumes a rule that does not
   exist.

**What this is not.** It is not an argument for changing the model, and it is not a licence to
simplify a structure to fit it. It is the same class of finding §6 already invites: a structure the
source describes as computing in a way the model does not cover is a finding against the model. The
first such finding was the retina's graded, non-spiking cells. **This is the second, it is larger,
and it is the dominant mode of the thalamus rather than an exception inside one organ.** Whether the
model is extended, or these structures are modelled some other way, is Micky's.

---

## Two ascending inputs are asserted at their producers and declared at no entry here

**Both close as negatives, checked from both sides on 2026-08-14, and neither is written in.** Each is
a class endpoint at its producer — an edge aimed at "the thalamus" rather than at a nucleus — and the
class has no member here to land on.

- **The locus coeruleus declares `→ thalamus`** (`13_neuromodulatory_systems`), the noradrenergic gain
  and arousal signal. **No entry in this section declares a noradrenergic or locus-coeruleus input
  under any name.** All eight were read for it. **The only neuromodulatory inputs anywhere in this
  file are the two basal-forebrain limbs at the thalamic reticular nucleus**, and they are cholinergic
  and parvalbumin-GABAergic, not noradrenergic. The sole source of thalamic noradrenaline therefore has
  a producer and no consumer.
- **The periaqueductal grey declares `→ thalamus`, ascending** (`14_brainstem_midbrain_hypothalamus`)
  — the affective pain projection. **No entry here declares a periaqueductal input under any name.**
  The two plausible consumers were read from that end and are marked below.

**This is a different state from an unresolved class with candidate members**, which is what the
cortical and afferent-field classes elsewhere in this file are. Here the members were enumerated and
none of them declares the edge. **The repair is at the source and it is bidirectional**: accept the
input at the nucleus that receives it, or establish that the description does not carry it. **Not
written in here**, because writing an edge on the far end's declaration alone would assert a
projection this section has read nothing for — the same rule already applied to the amygdalar edge at
the posterior / ventromedial-posterior entry.

---

## Mediodorsal nucleus

- **Function → structure.** The higher-order relay for prefrontal cortex, reciprocal with the whole
  of it — dorsolateral, ventrolateral and orbitofrontal — supporting working memory, executive
  control, and value / limbic processing. **A cognitive gateway and not a sensory relay, and not a
  relay in the payload sense at all:** it does not relay categorical content to the cortex, and what
  it supplies is amplification of the cortex's own recurrent dynamics. Structurally, the
  magnocellular, parvocellular and densocellular divisions are named in the literature this
  structure's counts draw on, but **no sub-element set and no internal edges are described**, so the
  structure has a count and no internal circuit.
- **Inputs.**
  - **← internal globus pallidus** and **← substantia nigra pars reticulata** — the associative and
    limbic basal-ganglia output. **Tonic inhibition, selectively released**: a gate on which
    prefrontal loops may proceed, not a positive content signal. Fan-in: to derive.
  - **← amygdala** (`08_medial_temporal_lobe`) — limbic value / significance context; payload
    otherwise owed at the source. Fan-in: to derive. **Two-ended and confirmed 2026-08-14.** That
    entry declares `→ mediodorsal thalamus` and types it *limbic value / significance context, payload
    otherwise owed* — **the same words at both ends, and both owing the same remainder.** Neither end
    names the amygdalar nucleus of origin, which the far file does name on its other limbs.
  - **← olfactory / limbic cortex** — limbic value / significance context. **This endpoint names a
    class rather than a structure with an entry**, is unresolved at the source, and is recorded here
    unresolved. Fan-in: to derive.
  - **← prefrontal cortex, layer 6, reciprocal — the modulator.** No receptive-field content;
    corticothalamic feedback. **Class endpoint.** Whether all five of the prefrontal consumers named
    below also send the layer-6 limb is not stated at either end. Fan-in: to derive.
    **Checked 2026-08-14, and it is not stated at the far end because the far end declares no
    corticothalamic limb at all.** **No structure in `11_frontal_lobe` declares an output to any
    thalamic nucleus** — seven declare a thalamic input and none declares one back. **So this class
    has no consumer-end declaration to be split against**, and the arity question below cannot be
    answered from that file as written.
  - **← prefrontal cortex, layer 5 — the driver.** The cortical drive that makes this a
    higher-order, cortically-driven nucleus rather than a first-order sensory relay. **A subset of
    its relay cells instead have subcortical drivers.** Class endpoint. Fan-in: to derive.
    **Undeclared at every one of its named sources, checked 2026-08-14** — see the layer-6 limb above.
    **This is the more consequential of the two absences**: the property that makes this structure
    higher-order rather than first-order rests on a drive whose origin declares nothing, so **the
    classification is asserted here and unsupported at the only end that could support it.**

    **Searched 2026-08-14, and the literature does not simply confirm the line. Class 2 — this bears
    on a content claim, not on citation form. All of the following are candidates awaiting
    verification; none is written into the payload above.**
    - **The distinction itself is standard and its criterion is exactly the one this line uses.**
      First-order relays take their driver from an ascending subcortical source; higher-order relays
      take it from cortical layer 5. **All thalamic nuclei receive a layer-6 cortical input; only
      higher-order nuclei additionally receive layer 5.** *(Sherman & Guillery, and the reviews
      descending from them — Sherman, *The thalamus is more than just a relay*, Curr Opin Neurobiol
      2007, PubMed 17707635; Sherman & Guillery, Neuron 2002, 33:163–175. Species: cat and monkey,
      tract-tracing and intracellular recording.)*
    - **The rodent literature supports the line as written.** The mediodorsal nucleus is described as
      a higher-order relay of prefrontal cortex **on the grounds of dual layer-5 driver and layer-6
      modulator input from that cortex** — the same two limbs this entry declares. *(Mitchell, Neurosci
      Biobehav Rev 2015, PubMed 25757689; Miller et al., eNeuro 2017, 4(5), rat, tetrode recording.)*
    - **A primate review reverses the attribution, and this is the finding.** In macaque, **most
      corticothalamic projections from prefrontal areas to this nucleus originate in layer VI**, while
      projections from **supplementary motor cortex** originate in **both layers V and VI** — from
      which the review draws that prefrontal input here **may be primarily modulatory** and the
      supplementary-motor input **may be the driver.** *(Review of primate mediodorsal and motor
      thalamic connections, arXiv 2409.02065, citing Xiao et al. 2009. Species: macaque,
      retrograde tracing with laminar counts.)*
    - **If that holds for human, the consequence lands on this section and not only on the far file.**
      This entry names its five cortical consumers and they are all prefrontal; **the supplementary
      motor areas are not among them, and this nucleus declares no edge to or from them.** So the
      structure that the primate result nominates as the driver source has **no relationship with this
      nucleus written anywhere in either file** — while the structures that do have one may be sending
      the modulator and not the driver. **The absence recorded above would then be an absence of the
      wrong limb at the wrong end.**
    - **A subdivision-specific split is described in the literature and it falls on the axis this
      entry marks *to derive*.** Only **some** subdivisions are reported to receive the layer-5 input;
      a review distinguishes **lateral** portions, described as passing sensory information and
      related actions onward, from **magnocellular, parvocellular and densocellular** portions,
      described as receiving a layer-5 **efference copy** and transmitting it by a transthalamic
      route. *(Frontiers in Neuroscience 2018, 12:33.)* **These are the three divisions the Shape
      field below names and does not use.** **The axis this entry calls load-bearing has labels in the
      literature its counts come from.**
    - **The layer-5 driver is described as a branch rather than a dedicated projection** — a
      collateral of a corticofugal axon whose other branch reaches a motor target. *(Guillery &
      Sherman, Brain Res Rev 2011, 66:205–219; and the Frontiers review above.)* **If that is right,
      the driver edge and some motor edge are one axon**, which is a fan-out fact this section has no
      slot for and which the far file would have to declare at the same structure.

    **What this changes here: nothing yet, and that is deliberate.** The classification stands as the
    description's, the payload is unaltered, and no citation above has been verified. **What it
    changes is the shape of the owed repair** — the question is no longer only *which prefrontal
    structures declare the return limb* but **whether the driver is prefrontal at all in primate, and
    which subdivision receives it.**
- **Outputs.** All five cortical edges carry the same thing, and it is not content.
  - **→ frontal eye fields** — no categorical content; modulatory amplification, raising the gain of
    the consumer's local recurrent connectivity. Fan-out: to derive.
  - **→ dorsolateral prefrontal cortex** — the same. Fan-out: to derive.
  - **→ ventrolateral prefrontal cortex** — the same. Fan-out: to derive.
  - **→ orbitofrontal / ventromedial prefrontal cortex** — the same. The consumer also declares a
    separate limbic limb reaching it via the ventral pallidum and this nucleus. Fan-out: to derive.
  - **→ frontopolar cortex** — the same. Fan-out: to derive.
  - **→ thalamic reticular nucleus**, collaterals of the thalamocortical axons — a copy of this
    nucleus's outgoing traffic, which drives the gate that regulates it. Fan-out: to derive.
  - **All five consumers are in `11_frontal_lobe` and all five declare this edge, checked 2026-08-14
    — and all five described it wrongly until this pass.** Each carried the note *declared there as a
    class covering all prefrontal divisions*, and the frontal eye fields entry additionally read *the
    mediodorsal entry names prefrontal cortex only.* **This entry names all six of them individually,
    on six separate lines**, and the sixth is the frontal eye fields. **The class this entry does
    declare is on its Inputs above, on the layer-5 and layer-6 return limbs** — the far end read the
    input-side class as describing the output side, and the reading propagated to every consumer.
    **All six are corrected there; no edge here changed.**
  - **Whether the five consumers receive the same amplification or differently-tuned ones is not
    stated at either end**, and it is the question that decides whether five edges or one is the
    right arity. **The far end could not have raised it while it believed itself inside a class**, and
    now can. **It remains unstated at both ends**, and the cell-class axis below is where an answer
    would land.
- **Sizing.** Basis: **per side.** ~10M neurons, an order estimate from volume × low thalamic
  density rather than a stereological count; fan-in to derive, bounded ≤ 16 bits → **≤ 20.0 MB.**
  **An independent route closes on it:** grey-matter volume ~680–990 mm³ at the thalamic packing of
  ~1.0–1.8 × 10⁴ /mm³ gives **6.8M to 17.8M**, which brackets the ~10M headline. Human control
  stereology exists but counts vary substantially study to study, so no single figure is pinned.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)**. N ~10M. **The cell-class axis is
  to derive** — three divisions are named in the literature the counts come from and none is written
  into the description, so the axis has a length and no labels. **The partition is load-bearing
  rather than cosmetic**: the five output edges leave for five different consumers, and whether each
  division reaches a different one is exactly the open question.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: two loops close here and both would be open in a
  staged bring-up — the prefrontal layer-5-driver / amplification / layer-6-modulator loop, and the
  reticular collateral loop. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The defining property is negative and it is what makes this a
  structure rather than a wire: **silencing it does not stop the prefrontal cortex from receiving
  task information; it stops that cortex from holding it.** A structure described only as a relay
  would make that unstatable, and it is the fact that sets what a learning rule here would be about
  — not content and not passage, but the amplification's setting.

## Pulvinar

- **Function → structure.** The largest thalamic nucleus: higher-order visual and attentional
  processing, and transthalamic routing among visual, parietal and temporal cortex. **It sits
  between a first-order relay and a content-transformer and is neither.** Unlike the lateral
  geniculate nucleus it has cortex-like selective units of its own — orientation, direction, motion,
  measured directly in primate. Unlike a cortical area, its output content largely **reflects its
  cortical driver** rather than building a representation the cortex lacks. What it adds on top is
  **coordination**: attentional gain and cross-areal synchrony. An **anterior pulvinar** is named,
  and the medial, lateral and inferior divisions are standard in the literature the counts draw on,
  but no sub-element set and no internal edges are written.
- **Inputs.**
  - **← visual cortex, layer 5 — the driver.** A feedforward cortical visual signal, the driver that
    sets the receptive field. **Class endpoint** — "V1 and higher visual areas" — unresolved at the
    source. Fan-in: to derive.
    **Checked against `01_visual_pathway` on 2026-07-29, and this edge has no producer end there.**
    That file declares **one** thalamic output from any visual area — V1's `→ higher-order thalamus,
    from 6b` — and **no layer-5 output to any thalamic nucleus anywhere in its eight structures.** Its
    only layer-5 efferent is V1 5b to the superior colliculus. V2, V3, V4 and inferotemporal cortex
    declare no thalamic output at all.
    **So the driver input this entry depends on is declared here and nowhere else**, and the class
    endpoint is what conceals it: had the class been split to "V1", the missing producer would have
    been a dangling edge the diff could see. **Owed at `01_visual_pathway`'s source, and it is the
    driver — the edge that sets the receptive field — not a modulatory afterthought.**
  - **← superior colliculus** (`14_brainstem_midbrain_hypothalamus`), subdivision-specific, from its
    intermediate and deep layers — a collicular visual signal, retinotopic salience and motion, on the
    colliculo-pulvinar-cortical route parallel to the geniculostriate one. Fan-in: to derive.
    **Two-ended and confirmed 2026-08-14, and the sub-element attribution agrees at both ends** — that
    entry writes the edge from its intermediate and deep layers, as this one does. **Payload owed
    there and typed here**, so this end carries the content and that end carries the layers.
    **The producer's line also carries a remainder this end cannot corroborate**: it reads
    `→ pulvinar and other thalamus → cortex`, and **no other entry in this section declares a
    collicular input**, so the remainder stays a class with no member here.
  - **A second collicular line names this structure as a relay rather than as an endpoint, and it is
    not written here as an edge.** That entry declares `→ V3 and the middle temporal area,
    di-synaptically via the pulvinar` — **one edge crossing four files with this nucleus as the
    intermediate stage.** This entry declares an output to the middle temporal area and none to V3,
    and **types neither as carrying a collicular signal**. **Owed at the source: either the transit is
    a property of the two outputs below and belongs in their payloads, or the di-synaptic line is a
    route description and not an edge.** Not resolved here.
  - **← visual cortex, layer 6 — the modulator.** No receptive-field content; sets response gain and
    frequency. Same class endpoint. Fan-in: to derive.
    **This one does have a producer end** (`01_visual_pathway`): V1's `→ higher-order thalamus, from
    **6b**`, typed there as reaching higher-order nuclei **but not** the reticular nucleus. **The
    layer numbering reconciles rather than conflicts** — that file gives V1 eleven laminar
    sub-elements against the standard six, splitting 5 into 5a/5b and 6 into 6a/6b, so its *6b* is a
    sublayer of this entry's *layer 6* and not a peer of layer 5. **Its 6a goes to the lateral
    geniculate nucleus and its 6b here, so the two sublayers of layer 6 have different thalamic
    targets** — a distinction this end cannot express while its endpoint is a class.
  - **← thalamic reticular nucleus** — inhibitory gating of specific transthalamic pathways; no
    content. Fan-in: to derive.
  - **← long-range inhibitory sources other than the thalamic reticular nucleus** — inhibition, no
    content. **Class endpoint.** The zona incerta is a candidate and whether it reaches this nucleus
    is not stated at either end. Fan-in: to derive.
- **Outputs.** The first four carry the same two-part payload: reflected content plus coordination.
  - **→ V4** (`01_visual_pathway`) — a visual signal that largely reflects the cortical driver,
    selective for orientation, direction and motion but not a new representation; plus attentional
    gain and cross-areal synchrony in alpha / low-beta and gamma. Fan-out: to derive.
    **Checked on 2026-07-29, and the disagreement is real but is about direction, not payload.** The
    consumer declares no payload at all. What it declares instead is a **termination pattern**:
    the edge terminates *densely in the middle layers, the layers a forward edge would use rather than
    the layer feedback uses* — **an anatomical claim that this is a driving input.** This end declares
    the opposite functional role: a signal that *largely reflects the cortical driver* and is *not a
    new representation*, which is an echo rather than a drive.
    **Both ends may be right and the reconciliation is the finding.** A middle-layer termination is
    feedforward in form; a payload that reflects cortex is feedback in content. **The pulvinar can
    deliver a cortically-derived signal through a feedforward-patterned synapse**, and if so the
    laminar-termination heuristic does not license inferring the payload. **Owed: state whether the
    heuristic is being relied on at the consumer's end, since nothing else there types this edge.**
  - **→ middle temporal area** — the same two-part payload. Fan-out: to derive.
  - **→ lateral intraparietal area** — the same. Fan-out: to derive.
  - **→ second somatosensory area, with the parietal ventral and ventral somatosensory areas**, from
    the **anterior pulvinar** — the consumer declares **deep-receptor** signals here, which is **not**
    the visual / coordinating payload this structure declares for its other targets. **A payload
    disagreement, recorded and not resolved**: this is a visual / associative nucleus and the
    anterior pulvinar is a non-visual subdivision, so both declarations may be right about different
    sub-elements. Fan-out: to derive.
  - **→ further visual, parietal and temporal cortical areas beyond the four named** — the same
    two-part payload. **Class endpoint**, the residue of the line the four named edges came out of.
    **Fan-out: each pulvinar cell reaches the input layers of ~2–3 cortical areas.**
  - **→ thalamic reticular nucleus**, collaterals of the thalamocortical axons. Fan-out: to derive.
- **Sizing.** Basis: **per side.** ~13–26M neurons, density-derived and soft; fan-in to derive,
  bounded ≤ 16 bits → **26.0–52.0 MB.** The independent route closes here too: grey-matter volume
  ~840–1640 mm³ at ~1.0–1.8 × 10⁴ /mm³ gives **8.4M to 29.5M** against the stated ~13–26M.
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-element, N)**, N ~13–26M. **The sub-element
  axis is to derive and its absence blocks allocation rather than description**, because two output
  edges declare *different payloads* and the most likely reconciliation is that they leave from
  different subdivisions. An array for the anterior pulvinar cannot be sized. Whether a map axis
  belongs here is open: the collicular input arrives **retinotopic**, and no retinotopic organisation
  of this nucleus is recorded, so a payload with a coordinate frame arrives at a structure with no
  recorded map. *(That the arriving frame implies a map axis is Claude's reading; the source records
  the payload and no map.)*
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the cortical driver / modulator loop and the
  reticular collateral loop both close here. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** Silencing this nucleus leaves cortical receptive fields intact but
  removes the attentional gain, the gamma synchrony and the inter-areal coherence. That result is
  what separates it from both neighbours in the taxonomy: a structure that carried content would
  take the receptive fields with it, and a structure that only gated passage would not have coherence
  to remove.

## Posterior / ventromedial-posterior thalamus

- **Function → structure.** The thalamic relay for the body's **physiological condition** — the
  fourth first-order sensory relay, carrying the **lamina-I spinothalamic and trigeminothalamic**
  stream (pain, temperature, itch, visceral and cardiorespiratory sensation, air hunger, sensual
  touch, muscle and vasomotor state) to the dorsal posterior insula, which is primary interoceptive
  cortex. **It is distinct from the ventral posterior relay and the two streams stay separate at the
  thalamus**: the discriminative dorsal-column stream relays through the ventral posterior complex
  onto primary somatosensory cortex, this one relays onto insular cortex, and **their topographies
  run on different axes** — this territory antero-posterior, head-to-foot, with trigeminal input
  anterior and lumbar posterior; the ventral posterior complex medio-lateral. Two **non-overlapping
  termination fields** are its sub-elements: a **calbindin-immunoreactive** field of small-to-medium
  round and oval cells clustered between cell-sparse zones, receiving the lamina-I stream, and a
  **calcitonin-gene-related-peptide** field intercalated between those clusters, receiving the
  visceral line. **No internal edge between them is typed**, and their near-non-overlap is a reason
  to expect none.
- **Contested, and carried as contested.** Whether this territory is a *distinct nucleus* is
  genuinely disputed — one lineage holds it is a cytoarchitectonically separate ventromedial-posterior
  nucleus that is the near-exclusive lamina-I target, another that classical anatomy already assigned
  the territory to the posterior nuclear group and that lamina-I fibres also terminate in the ventral
  posterior lateral and inferior nuclei and in the mediodorsal and intralaminar nuclei. **The data
  flow is not in dispute.** This is not *to derive*: it is a measured question yielding several
  answers, and the work it calls for is adjudication rather than experiment.
- **Inputs.**
  - **← spinal cord grey matter, lamina I** (`16_spinal_cord`) (crossed anterolateral /
    spinothalamic) and **← caudal spinal trigeminal nucleus** (trigeminothalamic, for the face) — **not one payload but three
    labelled lines**, distinguishable by cell morphology, response class and conduction velocity:
    **nociceptive-specific** (fusiform cells, pinch and/or heat), **thermoreceptive-specific**
    (pyramidal cells, innocuous cooling), **polymodal nociceptive** (multipolar cells, heat, pinch
    and cold). A pruriceptive population is reported within the nociceptive group. The
    morphology–physiology correspondence is near-total. **The three lines do not all go to the same
    place**: nearly all thermoreceptive cells reach the dorsomedial part of the ventral posterior
    medial nucleus and almost no nociceptive cells do. Fan-in: to derive. **The crossing is
    load-bearing** — the anterolateral system is crossed, so this territory serves the contralateral
    body.
    **Two-ended and confirmed 2026-08-14, and it is the strongest agreement either file records.**
    That entry declares the same edge from lamina I, names the same three lines with the same cell
    morphologies, **carries the same three measured central conduction latencies — 59, 72 and 131 ms —
    and records the crossing as load-bearing**, reaching all of it independently and eleven days
    earlier. **One edge's three latencies written twice, in two files, identically.**
    **The far end carries two facts this end does not.** Its lamina-I output is **five edges that are
    largely one population with collaterals rather than five populations**, so this edge may not be
    summed as an independent projection; and the **thalamic share is not a constant of the cord** — 
    spinothalamic cells are ~5% of ~400 lamina-I projection neurons per side per segment in the lumbar
    enlargement and ~42% of ~215 in the cervical. **So the fan-in on this line varies eightfold along
    the producer**, which this end's single *to derive* cannot express. **Owed here: record the
    segmental dependence**, since it is a property of what arrives.
  - **← vagal / solitary / parabrachial visceral line** (`14_brainstem_midbrain_hypothalamus`) —
    visceral and cardiorespiratory state, onto the second termination field rather than convergent
    onto the same cells. Payload otherwise owed. Fan-in: to derive.
    **Consumer-only, checked 2026-08-14: neither named producer declares an output to this territory.**
    The nucleus of the solitary tract declares the lateral parabrachial nucleus, the caudal
    ventrolateral medulla, the gustatory pathway, the vagal motor nuclei and the hypothalamus; the
    lateral parabrachial nucleus declares the amygdala, the bed nucleus, the hypothalamus, the
    intralaminar nuclei and the ventroposterior parvicellular thalamus, and the insula. **This
    territory is named by neither, under any of its names.**
    **One candidate identification exists and is not asserted:** the parabrachial line's second limb,
    the **ventroposterior parvicellular thalamus**, is a visceral thalamic target with no entry in
    this section, and whether it names this territory or a further structure is exactly what is
    unresolved below. **Owed at the source: establish the producer end, or establish that the two
    names denote one structure.**
  - **← insula**, corticothalamic feedback — no stimulus content; the driver / modulator gate.
    Fan-in: to derive.
  - **← thalamic reticular nucleus** — inhibition, a gain and gate control, no content. Fan-in: to
    derive.
  - **← zona incerta**, the incerto-thalamic projection whose signature target is precisely this
    territory — inhibition, no content. Fan-in: to derive.
- **Outputs.**
  - **→ dorsal posterior insula** — the body's physiological condition, **somatotopically ordered**
    on the antero-posterior axis. **Whether the three labelled lines stay separate on this edge or
    are merged here is owed**, and it is the question that decides the edge's arity. Fan-out: to
    derive.
  - **→ area 3a**, a reported lesser projection — payload owed. Fan-out: to derive.
  - **An edge is asserted against this structure from `08_medial_temporal_lobe` and is not written
    here.** That file's amygdala entry declares `← posterior thalamus` and already records that this
    entry declares no such edge. **Confirmed 2026-08-14 and its mark is exact**: the outputs above are
    the dorsal posterior insula, area 3a and the reticular collaterals, **and no amygdala target under
    any name.** **The edge is not written in here**, because writing it on the far end's declaration
    alone would assert a projection this section has read nothing for. **Owed at the source: establish
    it here, or withdraw it there.**
  - **→ thalamic reticular nucleus**, collaterals. Fan-out: to derive.
- **Sizing.** Basis: **per side. To derive** — no clean human count, and the contested and indistinct
  borders make an unbiased whole-structure figure unavailable. No grey-matter volume is recorded
  either, so the density route has no input here. Thalamic packing ~1.0–1.8 × 10⁴ /mm³ applies if a
  volume is ever pinned. **Structure total: to derive.**
- **Shape.** **Laminated nucleus** in the §6a sense — rank 3, **(termination field, body axis,
  to derive)** — where the field axis has **two** members and the map axis is the **1-D**
  head-to-foot somatotopy. **The map's dimensionality falls out of the description and is not
  imposed**: two in vision, one in audition, and one again here along the body. Extents: to derive.
- **Edge latency.** **Three measured, and they are on one edge.** Mean central conduction latency by
  line: thermoreceptive-specific ≈ **59 ms** (standard deviation 25, n = 136), polymodal nociceptive
  ≈ **72 ms** (standard deviation 28, n = 128), nociceptive-specific ≈ **131 ms** (standard deviation
  56, n = 100). Species: cat. Every other edge here reads **to derive.**
- **Invariant conformance.** Co-instantiation: the insular corticothalamic loop and the reticular
  collateral loop close here, as does the incerto-thalamic gate. Per-edge latency: **satisfied and
  partly measured** — the only structure in this section of which that is true.
- **Justification (biological).** The separation is the finding: temperature and pain do not travel
  as one "pain and temperature" payload but separate **at the thalamus**, by cell morphology, by
  target and by arrival time. An edge declaring them as a single stream is under-specified, and the
  72 ms gap between the cold signal and the nociceptive one is a structural consequence of the
  conduction velocities that carry them.

## Ventral anterior / ventral lateral nuclei

- **Function → structure.** The motor relay: it carries basal-ganglia and cerebellar output up to
  motor, premotor and supplementary motor cortex, **closing the two great motor loops.** Two
  sub-elements are named — the **ventral lateral** nucleus is the cerebellar-recipient, the **ventral
  anterior** the pallidal-recipient — **"with overlap," and the overlap is the contested part.** No
  internal edges are written, and the inputs and outputs are typed at the level of the combined
  nucleus rather than assigned to one division.
- **Inputs.**
  - **← internal globus pallidus** and **← substantia nigra pars reticulata** — **tonic inhibition,
    selectively released.** The payload is a *negative*: the output nuclei fire constantly and the
    selected action is the one whose inhibition **pauses**. Nothing here carries the action itself.
    **A consumer that expects a positive command on this edge has misread the structure.** Fan-in: to
    derive.
  - **← deep cerebellar nuclei, chiefly the dentate** (`10_cerebellum`), via the superior cerebellar
    peduncle, **decussating** — the cerebellar **correction**, the forward-model error correction that
    shapes an action already selected. Fan-in: to derive. **Fan-out at the producer: the
    cerebellar-cortex to output-nucleus areal ratio is ~85 : 1**, a massive convergence.
    **Two-ended and confirmed 2026-08-14, and this end discharged a mark there**: that line read *the
    consumer names these nuclei, untyped there.* **This end types it**, in the words above, and the
    producer's mark is withdrawn. **Both ends agree on the source sub-element, the peduncle and the
    decussation**, and **both carry the 85 : 1 figure** — the producer's only fan figure, and the one
    number in that file with a second written record here.
  - **← primary motor cortex**, corticothalamic and reciprocal — payload owed at both ends. Fan-in:
    to derive.
  - **← thalamic reticular nucleus** — inhibition, a gain and gate control, no content. Fan-in: to
    derive.
- **Outputs.**
  - **→ primary motor cortex** — the basal-ganglia **selection** (which action is released) and the
    cerebellar **correction** (how it is shaped), **combined on one relay.** Fan-out: to derive.
  - **→ premotor cortex and the supplementary motor areas** (`11_frontal_lobe`) — the same combined
    payload. Fan-out: to derive. **Two-ended and confirmed 2026-08-14**, and it is **the only
    two-ended cortical edge this nucleus has in that file** — the consumer declares
    `← the ventral anterior / ventral lateral thalamus` and is untyped, so this end carries the
    payload alone.
  - **→ prefrontal cortex** — payload owed, **class endpoint**, and **this is the section's
    load-bearing gap.** The cerebellar limb of this relay is declared as reaching "motor, premotor
    and prefrontal cortex" by its producer, and **no prefrontal entry declares this nucleus as an
    input** — the five that declare a thalamic input name the mediodorsal nucleus instead. **So
    either this limb is missing at its consumers or it does not exist, and which it is decides
    whether the cerebellar loop reaches prefrontal cortex at all.** Fan-out: to derive.
    **The origin of this gap is now located, 2026-08-14, and it is a clause in the producer.**
    `10_cerebellum`'s deep-nuclei entry writes its thalamic output as reaching this nucleus *onward to
    motor, premotor and prefrontal cortex* — **and that onward-clause is the whole basis for the
    prefrontal limb.** The producer names no prefrontal structure, declares no edge to one, and the
    clause describes a destination two synapses away through this section. **So the claim originates as
    a subordinate phrase in a file that cannot check it, is inherited here as a class endpoint, and is
    declared by no consumer.** **Owed at the source, and at `10_cerebellum` as well as here**:
    establish which cortical areas the dentate limb reaches through this relay, or narrow the clause.
    **The producer has been given the finding from this side.**
    **Confirmed 2026-08-14 by reading `11_frontal_lobe` directly, and the mark holds exactly as
    written.** Seven structures there declare a thalamic input. **One names this nucleus** — the
    premotor and supplementary motor areas, which is the named edge above and not this class. **The
    four granular prefrontal structures and the frontal eye fields all name the mediodorsal nucleus;
    the anterior cingulate cortex names the midline / intralaminar group. None names this one.** So
    the count is exact and the gap is not a matter of a synonym or an unread far end. **It stays a
    class, and the decision it forces is unchanged.**
  - **→ thalamic reticular nucleus**, collaterals. Fan-out: to derive.
- **Sizing.** Basis: **per side. To derive** — no clean human per-nucleus count and no grey-matter
  volume, so neither the direct nor the density route has an input. **Structure total: to derive.**
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-element, N)**, sub-elements **ventral
  lateral** and **ventral anterior**, N to derive. **The partition is what decides the payload
  question and not just the anatomy**: the output edges declare selection and correction *combined
  on one relay*, and whether the combining happens by convergence onto shared cells or by two
  segregated channels leaving side by side is exactly what a sub-element assignment would settle.
  The literature's "with overlap" is the contested part and is carried as contested.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the primary-motor reciprocal loop and the reticular
  collateral loop close here; the basal-ganglia and cerebellar loops close outside this section.
  Per-edge latency: satisfied, all to derive.
- **Justification (biological). Both crossings on the cerebellar limb are load-bearing and neither
  may be dropped.** The corticopontine input crosses and this output crosses, so **each cerebellar
  hemisphere serves the contralateral cortex and the ipsilateral body.** A double crossing is the
  case §5 names as easiest to lose, because both endpoints see a same-side connection and neither
  end can re-derive the route.

## Anterior nuclei

- **Function → structure.** The memory relay of the Papez circuit — mammillary bodies → this nucleus
  → cingulate and retrosplenial cortex — supporting episodic memory and spatial orientation. The
  anterodorsal, anteroventral and anteromedial nuclei are the standard divisions and **are not named
  in the description**, and no internal edges are described.
- **Inputs.**
  - **← mammillary bodies** (`14_brainstem_midbrain_hypothalamus`), via the **mammillothalamic
    tract** — payload owed. Fan-in: to derive. **Two-ended and confirmed 2026-08-14, payload owed at
    both ends.** **The far end declares it from inside its hypothalamus entry, of which the mammillary
    bodies are a sub-element**, and the tract has its own entry in `18_white_matter_tracts` — **so this
    one edge crosses three files and terminates on a sub-element of a bundled entry at its producer.**
    The Papez limb is intact here; what is missing from this structure is the retrosplenial return
    arm below, not this one.
  - **← subiculum**, via the **post-commissural fornix** — a **completed episode**: the bound,
    retrievable pattern, **addressable by any fragment of itself.** The payload is only partly
    writable and is owed, because "an episode" has no units and no coordinate frame; what makes it
    checkable is a property rather than a type — it is **content-addressable**, which the upstream
    identity codes are not. Fan-in: to derive.
  - **← retrosplenial cortex**, reciprocally — **declared at the consumer's end only and missing
    here.** A reciprocal loop needs this limb and this structure's Inputs carry no cortical line at
    all. Recorded, not invented: the edge is written because the far end declares it, and the gap is
    the source's.
- **Outputs.**
  - **→ retrosplenial cortex** — payload owed. Fan-out: to derive.
  - **→ anterior cingulate cortex** (`11_frontal_lobe`) — payload owed, **and declared at one end
    only.** The consumer declares a thalamic input from the midline / intralaminar thalamus and
    **not** from this nucleus, so the cingulate half of the classical Papez target is unconfirmed at
    its consumer. Fan-out: to derive. **Confirmed 2026-08-14 and the mark is exact**: that entry names
    one thalamic source and this nucleus is not it. **The far end has been given the mark from this
    side**, and the repair — accept the limb there or withdraw it here — is owed at the source.
  - **→ thalamic reticular nucleus**, collaterals. **The reticular nucleus declares an output to this
    structure and this structure does not declare the input** — one of the two loops asserted at one
    end only. Fan-out: to derive.
- **Sizing.** Basis: **per side. To derive** — counts have been consistently normal across
  schizophrenia stereology but no control figure is pinned, and no grey-matter volume is recorded.
  **Structure total: to derive.** Axons: the mammillothalamic tract and the fornix limb reaching this
  nucleus, counts to derive.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)**, both **to derive**. **The
  cell-class axis is not decoration here**: the head-direction signal the retrosplenial consumer
  describes is classically carried by one of the three divisions rather than by the group, so naming
  them is what would let that be written as an edge at all.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: **the Papez loop cannot be shown closed from this
  end.** Its return arm through parahippocampal cortex has no entry anywhere in the source, and the
  retrosplenial reciprocal limb is missing from this structure's Inputs. **A missing stage inside a
  closed loop breaks traceability rather than leaving a visible dangling end**, and the repair is the
  source's. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** What arrives on the subicular edge is not a code for a thing but a
  **retrieval property**: an episode addressable by any fragment of itself. That is the first payload
  in this section whose defining feature is how it is *accessed* rather than what it represents, and
  it is why the payload cannot be finished by naming units.

## Intralaminar nuclei

- **Function → structure.** The "nonspecific" nuclei: arousal and alertness, plus a major **direct
  excitatory input to the striatum**, a thalamostriatal drive running parallel to the cortical one.
  Two sub-elements are named and **they are already load-bearing**, because the two striatal output
  edges leave from different ones and reach different striatal sectors: the **centromedian** nucleus
  → motor striatum, the **parafascicular** nucleus → associative and limbic striatum. **No internal
  edge between them is described**, and the wider intralaminar group — central lateral, paracentral,
  central medial — is named neither in the description nor in the material behind it.
- **Inputs.**
  - **← reticular formation** (`14_brainstem_midbrain_hypothalamus`) — payload owed; the arousal
    drive the function names. Fan-in: to derive. **Two-ended and confirmed 2026-08-14**, that entry
    declaring `→ intralaminar thalamus (ascending arousal)`, **payload owed at both ends.**
    **The producer records a structural qualification this end does not**: much of the diffuse cortical
    arousal it is credited with is delivered by the monoaminergic and cholinergic nuclei of
    `13_neuromodulatory_systems` rather than by reticular cells directly. That bears on its cortical
    class and not on this edge, **and it is the reason the negative recorded above matters** — the
    relay it names has no declared input here either.
  - **← deep cerebellar nuclei** (`10_cerebellum`) — payload owed at both ends. Fan-in: to derive.
    **Two-ended and confirmed 2026-08-14, payload owed at both ends** as this line already recorded.
    **Neither end names the nucleus of origin**, where the sibling edge at the ventral anterior /
    ventral lateral group names the dentate at both ends. **The producer's divisional axis exists and
    sorts its other outputs**, so the far end can answer it; the debt has been recorded there.
  - **← lateral parabrachial nucleus** (`14_brainstem_midbrain_hypothalamus`) — payload owed.
    Fan-in: to derive. **Two-ended and confirmed 2026-08-14, payload owed at both ends.**
    **The producer's line is compound and its second limb has no entry here.** It reads
    `→ intralaminar nuclei and the ventroposterior parvicellular thalamus`, and **that second
    structure has no entry in this section under any name** — while the same file names it again at
    its nucleus of the solitary tract, routing taste through it to insular cortex. **So a thalamic
    relay another section depends on twice is absent from this section's eight entries.** Confirmed
    from this end 2026-08-14. **Owed at the source: give it an entry here, or establish which entry
    already covers it** — and see the visceral line at the posterior / ventromedial-posterior entry,
    which is the candidate.
  - **← periaqueductal grey — asserted at the producer and not written here.** See the section-level
    block above: that file read this entry directly and found no periaqueductal input, and this end
    confirms it. **The edge is not written in.**
  - **← internal globus pallidus** and **← substantia nigra pars reticulata** — payload owed, **and
    the edge is unconfirmed at its producer**, whose declared thalamic targets are the ventral
    anterior / ventral lateral group, the mediodorsal nucleus and the reticular nucleus. Recorded as
    the source records it: confirm or delete. Fan-in: to derive.
  - **← cerebral cortex** — payload owed. **Class endpoint**, unresolved. Fan-in: to derive.
- **Outputs.**
  - **→ motor striatum**, from the **centromedian nucleus** — arousal and a thalamostriatal drive
    parallel to cortex; payload otherwise owed. Fan-out: to derive.
  - **→ associative / limbic striatum**, from the **parafascicular nucleus** — the same drive.
    Fan-out: to derive.
  - **→ anterior cingulate cortex** (`11_frontal_lobe`) — payload owed. Fan-out: to derive.
    **Two-ended and confirmed 2026-08-14, and this end discharged a mark there**: that line read *the
    producer declares its cortical target as a class — striatum major, cortex diffuse — which covers
    this structure without naming it.* **The split it asked for had already been made here**, and this
    is the named member. Payload owed at both ends.
  - **→ further cortex, diffusely, beyond the anterior cingulate** — payload owed. **Class
    endpoint**, the residue of the line the named edge came out of. Fan-out: to derive.
  - **→ thalamic reticular nucleus**, collaterals. **The reticular nucleus declares an output to this
    group and this group does not declare the input** — the second of the two one-ended loops.
    Fan-out: to derive.
- **Sizing.** Basis: **per side. To derive** — no clean human per-nucleus count, no volume.
  **Structure total: to derive.**
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-element, N)**, sub-elements **centromedian**
  and **parafascicular**, N to derive. **This is the section's clearest case of an edge terminating
  below the level the count is stated at**: the two striatal edges leave from named sub-elements, and
  a count exists for neither the group nor either member, so the arrays those edges would read from
  cannot be sized in either direction.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the striatal drive puts this group inside the
  basal-ganglia loop, which closes outside this section; the reticular loop is asserted at one end.
  Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The sector split is what makes this a structure with parts rather
  than a diffuse projection: two named sub-elements reaching two functionally distinct striatal
  sectors is a topographic claim, and it is the claim the striatal end of the map does not carry.

## Thalamic reticular nucleus

- **Function → structure.** The gamma-aminobutyric-acid-releasing inhibitory **shell** around the
  thalamus, and **the one thalamic structure that does not project to cortex.** It inhibits the other
  thalamic nuclei, gating thalamocortical traffic and implementing attentional selection. **Most, but
  not all**, cortico-thalamic and thalamo-cortical axons passing through give it collaterals — and
  the exceptions are specific, measured, and the reason the qualifier matters, **because a sheet that
  monitors most traffic is a different gate from one that monitors all of it.** It is **sectored by
  modality**, and the sectors are load-bearing because the output edges leave from different ones:
  the **perigeniculate nucleus** is the visual sector, an auditory sector is named at the medial
  geniculate entry, and the somatosensory and motor sectors are implied by the remaining outputs.
  **No sector is given as a named sub-element and no internal edge between sectors is described** —
  which matters, because intra-reticular connectivity is what would let the searchlight select one
  modality *against* another rather than gating each independently.
- **Inputs.**
  - **← collaterals of cortico-thalamic and thalamo-cortical axons** — a copy of the traffic in both
    directions, which is what lets this sheet gate what it monitors. **A class endpoint that is not
    exempt, because the universal claim that would have exempted it is false.** The exceptions, and
    **they are the only measured connectivity fractions in this section**:
    - **corticothalamic layer 6a** collateralises here — the canonical top-down input.
    - **corticothalamic layer 5** generally does **not**; the layer-5 driver axons reach the
      higher-order nuclei without the feed-forward inhibition the layer-6 route carries. **One
      region-specific exception:** layer 5 pyramidal cells of **frontal cortex**, and not of other
      cortical regions, make **monosynaptic** connections here — a direct connection rather than a
      passing collateral, morphologically and physiologically distinct from the layer-6 route.
    - **corticothalamic layer 6b** targets higher-order thalamus and sends **no** collaterals here.
    - **thalamocortical** collaterals arise from *virtually* all thalamic nuclei, not all: in the one
      nucleus where the fraction was counted, **76% of ventrobasal relay axons gave visible
      collaterals here**, so roughly a quarter did not. A paraventricular projection to this sheet
      has not been described though the reverse has.

    Fan-in: to derive. **The cortical half is owed a split by producer and layer.**
  - **← basal forebrain, parvalbumin-expressing inhibitory neurons** (`13_neuromodulatory_systems`) —
    inhibition of this nucleus and therefore **disinhibition of the relay nuclei it inhibits.** The
    logic is double-negative: a tonic inhibitory hold on the relays is transiently released when
    attention or arousal demands it. Fan-in: to derive.
    **Two-ended and confirmed 2026-08-14, and it is the strongest agreement either file records.**
    Both ends declare the edge **from that named population**, both type it in the same
    double-negative terms, **and both independently carry the same disconfirming experiment** — the
    ~10 Hz spindle result in this entry's Justification field below, which each file wrote without the
    other in hand. **An agreement reached twice from the same source is not a check; this one was
    reached from two files on two dates and is.**
  - **← basal forebrain, cholinergic neurons** (`13_neuromodulatory_systems`) — payload owed,
    **and the sign is the surprise**:
    driving these fibres optically within this nucleus **promotes sleep**, opposite to
    acetylcholine's general arousal role and opposite to the parvalbumin edge above. **Two
    projections from one source region to one target with opposite behavioural consequences.**
    Fan-in: to derive. **Two-ended and confirmed 2026-08-14**, the producer recording the same
    opposite sign from the same named population and reaching the same conclusion independently:
    **the transmitter axis is load-bearing rather than descriptive**, because it is the only thing
    separating two edges that share a producer, a target and a sign convention and differ in outcome.
    **Payload owed at both ends.**
  - **← internal globus pallidus** and **← substantia nigra pars reticulata** — inhibition, payload
    owed. **Whether these terminate here or directly on the relay nuclei is not distinguished at
    either end**, and the consequence is stated plainly at the producer: if they terminate on the
    relays directly, this edge and the two thalamic edges are the same projection described twice.
    Fan-in: to derive.
  - **← zona incerta** — inhibition, payload owed. **The same terminate-here-or-on-the-relay
    ambiguity applies.** Fan-in: to derive.
- **Outputs.** All carry inhibition and no content, and **none leaves the thalamus.**
  - **→ mediodorsal nucleus** — inhibition, a gain and gate control. Fan-out: to derive.
  - **→ pulvinar** — inhibitory gating of specific transthalamic pathways. Fan-out: to derive.
  - **→ posterior / ventromedial-posterior thalamus** — inhibition. Fan-out: to derive.
  - **→ ventral anterior / ventral lateral thalamus** — inhibition. Fan-out: to derive.
  - **→ lateral geniculate nucleus** — inhibition. **The visual sector of this sheet is the
    perigeniculate nucleus, and the two are one structure described at two scales.** Recorded as a
    naming collision rather than resolved by preference: both names are in common use and the edges
    carry the function either way. Fan-out: to derive.
  - **→ medial geniculate nucleus** — inhibition; the gate. Fan-out: to derive.
  - **→ ventral posterior nuclear complex** — inhibition. Fan-out: to derive.
  - **→ anterior nuclei and intralaminar nuclei** — inhibition. **Neither consumer declares this
    input**, though the function claims this nucleus inhibits the other thalamic nuclei generally.
    Fan-out: to derive.
- **Sizing.** Basis: **per side. To derive** — a thin sheet with no clean human count and no volume.
  **Structure total: to derive.** White-matter volume: **not applicable** — a thin grey sheet lying
  within the internal capsule's fibre path rather than a nucleus with its own white-matter
  compartment.
- **Shape.** **A sheet, and it does not fit the four shape classes cleanly.** It has a real tangential
  extent and a sector organisation, so it is not the rank-2 non-laminated case; but **§6a's sheet
  class specifies a *laminar* sub-element axis and this sheet has no laminae** — its sub-element axis
  is a **modality sector.** Written here as rank 3, **(sector, H, W)**, all three extents **to
  derive**, with the class question recorded rather than resolved: either the sheet class generalises
  from laminar to any sub-element axis, or a fifth class is wanted for an unlaminated sheet. *(The
  anatomy is Class 1 from the source; the observation that it falls between the shape classes is
  Claude's reading, offered to be checked. The zona incerta below is the second instance.)*
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: **this structure is the reason the section cannot be
  staged at all.** It sits inside seven loops, it has no output outside them, and every relay nucleus
  here is gated by it from the outset. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** One negative result constrains the payload and is carried for that
  reason: the basal forebrain's parvalbumin neurons drive cortical gamma, and this projection was
  tested as the route. Stimulating the parvalbumin neurons **of this nucleus** instead enhanced
  cortical power at about **10 Hz** — spindle frequency — and **not** gamma. **So this edge is not
  the carrier of that effect**, and an architecture that assumed the obvious route would have wired a
  projection that does not do the job attributed to it.

## Zona incerta

- **Function → structure.** A largely inhibitory cell **sheet of the subthalamus** — ventral
  diencephalon, lying dorsal to the subthalamic nucleus. **It is not thalamus**, and it is here
  because its signature projection is the **incerto-thalamic** inhibitory input to the higher-order
  thalamus, gating thalamocortical and thalamostriatal transmission: **an extrathalamic gate that
  complements the intrinsic one above.** An integrative inhibitory hub with an unusually wide
  afferent field, whose precise role is still debated. **Different sectors** have been tied to
  arousal and attention, posture and locomotion, feeding, defensive behaviour, sleep, visceral
  activity and pain gating, and a **parvalbumin population** is named as the target of the amygdalar
  input — **so sub-elements are described, none is named, and no internal edge is written.**
- **Inputs.**
  - **← central nucleus of the amygdala** (`08_medial_temporal_lobe`), onto this structure's
    **parvalbumin neurons** — payload owed; the producer's role in the pair is given as fear. Fan-in:
    to derive. **Two-ended and confirmed 2026-08-14**, and both ends name the parvalbumin target.
    **The two ends differ on the source sub-element and this end is the more specific one**: the
    producer writes the edge from the amygdala as a whole and names no nucleus, while this line names
    the central nucleus. **Owed at the source: name the nucleus at the producer, or establish that
    this end's attribution is narrower than the evidence.**
  - **← a near-whole-brain afferent field** — cerebral cortex, basal ganglia, thalamus, hypothalamus,
    brainstem, cerebellum and spinal cord. Payload owed. **Seven class endpoints, none checkable as
    written, and the largest single block of them in the section.** The wide afferent field is an
    explanation for the shape of the line and not a resolution of it. Fan-in: to derive.
- **Outputs.** Eight edges to eight targets, and **the functional list implies they do not all leave
  from the same sector.**
  - **→ posterior / ventromedial-posterior thalamus**, the incerto-thalamic projection — inhibition,
    no content; the signature target. Fan-out: to derive.
  - **→ thalamic reticular nucleus** — inhibition, payload owed, with the
    terminate-here-or-on-the-relay ambiguity owed at both ends. Fan-out: to derive.
  - **→ hypothalamus** (`14_brainstem_midbrain_hypothalamus`) — payload owed. Fan-out: to derive.
    **Producer-only, checked 2026-08-14: that entry declares no incertal input.**
  - **→ periaqueductal gray** (`14_brainstem_midbrain_hypothalamus`), defensive behaviour — payload
    owed. Fan-out: to derive. **Producer-only, checked 2026-08-14**, and that entry's Inputs are fully
    enumerated — the amygdala's central nucleus, the hypothalamus, ventromedial and orbital prefrontal
    cortex, and spinal lamina I — **with no incertal line among them.**
  - **→ ventral tegmental area** (`13_neuromodulatory_systems`), feeding drive — payload owed.
    Fan-out: to derive. **Producer-only, checked 2026-08-14**: that entry declares the ventral
    pallidum, prefrontal cortex, the lateral hypothalamus, the brainstem tegmental nuclei and the
    lateral habenula, **and no incertal input.**
  - **These are one finding and not several, and there are now four of them.** **This structure's name appears nowhere in either
    far file except inside the two paragraphs recording the negatives above** — it is named as a
    structure that was read past, never as an endpoint. **So the zona incerta projects into two
    sections that do not know it projects to them.** It is the mirror of the two ascending negatives
    at the head of this file: there, two producers aim at a class with no member here; here, one
    producer aims at three named structures none of which declares the edge. **The direction of the
    repair is opposite and the state is the same** — an edge sound at one end and absent at the other,
    which each end reads as complete on its own.
  - **→ rostral ventromedial medulla**, descending pain control — payload owed. Fan-out: to derive.
    **Resolved 2026-08-14, and it is the dangling case rather than the cross-file one.** The
    conditional above is discharged: `14_brainstem_midbrain_hypothalamus` states flatly that **the
    rostral ventromedial medulla has no entry in any file**, and declares an edge to it from its own
    periaqueductal grey; `16_spinal_cord` names it a third time, in the descending analgesic gate onto
    lamina II, and records the same absence. **Three files declare edges to a structure that has no
    entry anywhere.** **Owed at the source, and it is not this section's to repair** — the same shape
    as the septal nuclei and the red nucleus.
  - **→ cerebral cortex** — payload owed. **Class endpoint.** Fan-out: to derive.
  - **→ spinal cord** (`16_spinal_cord`) — payload owed. Fan-out: to derive. **Producer-only, checked
    2026-08-14: no entry in that file declares an incertal input under any name.** Its descending
    inputs are the primary afferents, the five-tract motor bundle, the periaqueductal and medullary
    analgesic gate, the raphe and hypothalamic modulatory line, and the presympathetic drive.
    **This is the fourth of this structure's outputs found producer-only**, after the hypothalamus, the
    periaqueductal grey and the ventral tegmental area — **so the finding recorded there stands and
    grows: the zona incerta projects into four sections and is declared at none of them.**
- **Sizing.** Basis: **per side. To derive** — a diffuse, ill-bordered subthalamic sheet with no
  clean human count and no volume. **Structure total: to derive.** Axons: the incerto-thalamic and
  descending incertal projections, counts to derive.
- **Shape.** **A sheet, and the second instance of the class question above.** Rank 3, **(sector, H,
  W)**, all extents **to derive**, with the sector axis functional rather than laminar. The rostral /
  caudal division is already in use in the description, so at least one axis label exists. **The
  partition blocks allocation**: eight output edges leave for eight targets and none is assigned to a
  sector.
- **Edge latency.** All edges **to derive.**
- **Invariant conformance.** Co-instantiation: the incerto-thalamic gate closes a loop with the
  posterior / ventromedial-posterior territory inside this section; the remaining seven edges close
  outside it. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** This is the second gate on the same traffic, and it is outside the
  structure it gates. The intrinsic shell above is built from the thalamus's own collaterals and
  therefore only knows what the thalamus is already sending; this one is driven by a near-whole-brain
  afferent field and can gate the same relays on information the thalamus does not carry. **Two gates
  on one relay, differing in what each is allowed to know**, is a structural claim and not a
  redundancy.

---

## Findings this file records against `13_neuromodulatory_systems` and `14_brainstem_midbrain_hypothalamus`

**No edge in this file was added, deleted or re-typed.** Fourteen shared edges were diffed; **seven
are two-ended and were confirmed as written**, and the payload agreed at both ends on every one of
them. What changed is the **state recorded against six endpoints** — three producer-only, one
consumer-only, and two ascending classes closing as negatives — and the addition of stems where the
far file has now been read.

**The section's relationship to the two files is asymmetric, and the asymmetry is the finding.**
Everything this section *receives* from them arrives on **class endpoints aimed at "the thalamus"**,
and two of the three close as negatives against all eight entries. Everything it *sends* them leaves
from **one structure** — the zona incerta — on **named** edges, and three of those have no consumer
end. **So the traffic between this section and the subcortical core is declared at one end almost
everywhere it is declared at all**, in both directions, and the two directions fail differently: the
inbound ones fail by naming a class too coarse to land, the outbound ones by naming a structure
exactly and not being heard.

**One count that is not a defect.** The seven two-ended edges are concentrated at three entries —
the reticular nucleus's two basal-forebrain limbs, the intralaminar group's two ascending arousal
limbs, the pulvinar's collicular input, the anterior nuclei's mammillary input. **Every one of them
is an edge whose producer is a small, named nucleus.** The failures are at endpoints naming a
territory. That is the same pattern §9b of the source design records, arriving here from the far side.

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Mediodorsal nucleus | per side | ~10M | ≤ 16 | ≤ 20.0 MB |
| Pulvinar | per side | ~13–26M | ≤ 16 | ≤ 26.0–52.0 MB |
| Posterior / ventromedial-posterior thalamus | per side | to derive | ≤ 16 | to derive |
| Ventral anterior / ventral lateral nuclei | per side | to derive | ≤ 16 | to derive |
| Anterior nuclei | per side | to derive | ≤ 16 | to derive |
| Intralaminar nuclei | per side | to derive | ≤ 16 | to derive |
| Thalamic reticular nucleus | per side | to derive | ≤ 16 | to derive |
| Zona incerta | per side | to derive | ≤ 16 | to derive |
| **stated total** | per side | **~23–36M** | | **~46.0–72.0 MB** |

**Six of the eight structures have no neuron count, and the total is built from the other two.** That
is a different state from the visual section, where six of eight were counted, and it is not a
defect in this document: **the counts are not in the description because they have not been
measured.** Five of the six have no grey-matter volume either, so **the density × volume route that
independently confirms both counted structures has no input for any of them.**

**The two counted structures both close against that second route**, which is worth recording because
it is the only mechanical check available at this rung:

- mediodorsal, ~680–990 mm³ at ~1.0–1.8 × 10⁴ /mm³ → **6.8M–17.8M**, against a stated ~10M.
- pulvinar, ~840–1640 mm³ at the same packing → **8.4M–29.5M**, against a stated ~13–26M.

**Every fan-in in this section is *to derive*, so every bits-per-neuron figure above is the 16-bit
ceiling and not a measured width.** Unlike the visual section, where V1's fan-in dispute could be
bounded at 12–14 bits, nothing here has a fan-in at all.

**The total is a floor twice over.** It omits six structures, it takes the ceiling on the two it
includes, and **state memory and edge storage are not in it** — edge storage in particular cannot be
sized until the scheduling discipline is set, and it is not.

**Memory is not a binding constraint here and this figure is not to be reduced.** It is a derived
requirement recorded as found, and it is small only because most of the section is uncounted.
