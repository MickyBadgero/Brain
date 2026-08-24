# Brain architecture — 11 frontal lobe

**Date:** 2026-08-23
**Derived from:** `human_brain_11_frontal_lobe_2026_08_23.md` — file 11 of 20, the frontal lobe.

**Structures:** 9. **Edges:** 106 declarations — 63 in, 43 out, every one of them a live edge.
**Eleven of those edges have both ends in this file and seven of the eleven are declared at both
ends, so the 106 declarations are 99 distinct edges.** **One recorded negative** — an edge checked
and found not to exist — is carried at structure 1 and is not one of the 43. **Four further outputs
are recorded as owed rather than written** and are listed at the entries they belong to; they are
not counted in the 43 either.

**Files whose shared edges with this one are stemmed below, and what stands between them.**

- `01_visual_pathway`, `02_auditory_pathway`, `07_anterior_temporal_lobe`.
- `17_insula_claustrum_habenula`. **Twelve shared edges; eight two-ended, one internal
  contradiction, and four outputs the far end declares and this file does not — every one of them
  leaving the medial wall.**
- `04_dorsal_visual_parietal_stream`, `14_brainstem_midbrain_hypothalamus`. **Sixteen shared edges;
  one producer-only edge at this end, and a sub-element this file names on two lines carries a
  far-end payload it has nowhere to put.**
- `08_medial_temporal_lobe`, `12_thalamus`. **Twenty-one shared edges, and the thalamic return
  limbs are absent from every structure in this file.** **Five edges from
  `08_medial_temporal_lobe` stand at the source and are carried above** — three amygdalar limbs to
  the premotor, dorsolateral and ventrolateral structures, and the two hippocampal limbs to the
  orbitofrontal / ventromedial and anterior cingulate structures.
- `09_basal_ganglia`, `13_neuromodulatory_systems`. **Sixteen shared edges. This file's four
  cortico-striatal producers stand against three at the far end's inventory; the mesocortical
  dopamine limb is two-ended at one entry and absent at the other four; and **every ascending limb
  `13_neuromodulatory_systems` declares from prefrontal cortex has no producer in this file** — no
  structure here declares an output to any neuromodulatory nucleus.**
- `05_sensorimotor_loop`, `06_posterior_parietal`. **Twenty-three endpoints in this file carry a
  stem. Fifteen edges two-ended; two producer-only edges absent at their `05_sensorimotor_loop`
  consumer; two class endpoints, one closed as a negative against both files and one facing an
  unresolved class at the far end.**

**No structure in this file declares an output to any thalamic nucleus, and that is a
whole-file absence rather than six separate ones.** Seven structures here declare a
thalamic **input** — the premotor areas from the ventral anterior / ventral lateral nuclei, the
frontal eye fields and the four granular prefrontal structures from the mediodorsal nucleus, the
anterior cingulate cortex from the midline / intralaminar group. **Not one declares a limb back.**
`12_thalamus` declares the return traffic as two class endpoints on its mediodorsal entry —
`← prefrontal cortex, layer 6, reciprocal — the modulator` and `← prefrontal cortex, layer 5 — the
driver` — and states that **whether all five of its named prefrontal consumers send the layer-6 limb
is not stated at either end.** **It is not stated at this end because this end declares neither
limb.**

**This is load-bearing rather than bookkeeping, and it is load-bearing in that file's terms.** The
layer-5 driver is what makes that nucleus a higher-order, cortically-driven relay rather than a
first-order sensory one — the drive originates here. That file lists the prefrontal
layer-5-driver / amplification / layer-6-modulator loop as one of the two loops that close on it and
marks it as one that **would be open in a staged bring-up.** **It is open now, at every one of its
cortical ends, and the openness is on this side.** **Owed at the source**: declare the corticothalamic
limbs at the structures that send them, or establish that they are not separable per structure. **The
absence is recorded and not repaired here** — writing six edges whose only warrant is the far end's
class would invent the per-structure arity that is precisely what is unknown.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file is checked against this one; an endpoint with no stem is unchecked, and that is
not a claim that none exists.

---

## Findings this file records against `17_insula_claustrum_habenula`

**Twelve edges cross between the two files. Eight are declared at both ends and four are declared only
at the far end — and the four are not scattered.** Every one of them leaves a **medial-wall** structure
here: three from the **anterior cingulate cortex** (structure 8) and one from the **ventromedial**
half of structure 7.

| edge, as the far end declares it | producer here | state |
|---|---|---|
| insula `← anterior cingulate cortex` | structure 8, Outputs | **owed here** |
| lateral habenula `← anterior cingulate cortex` — *bad-outcome expectation* | structure 8, Outputs | **owed here** |
| posterior cingulate cortex `← anterior cingulate cortex` | structure 8, Outputs | **owed here** |
| lateral habenula `← ventromedial prefrontal cortex` — *bad-outcome expectation* | structure 7, Outputs | **owed here** |

**Structure 8 is a named producer to three of that file's six entries and declares an output to none
of the three**, while carrying four outputs in total. **That is not four scattered omissions; it is
one structure's output slot being three edges short**, and the shortfall is invisible from inside this
file because each missing edge is a far end.

**The habenular pair is the load-bearing one.** That file's value-brake path types a *bad-outcome
expectation* arriving on the lateral habenula from three cortical producers — the anterior cingulate
cortex, the anterior insula and the ventromedial prefrontal cortex. **Only the insular limb is declared
at its producer, and that producer sits inside file 17 itself.** Both cortical producers outside it are
in this file and **neither declares the edge**. The far end carries the pair as *unconfirmed at two of
three producers*; **the state here is stronger than unconfirmed — both edges are absent at both
producers.**

**That file names both of its cortical targets on their own lines**, having split the compound
`→ anterior cingulate cortex and prefrontal cortex` into separate named edges, so neither reaches a
structure here as an unnamed class. Carried at the entries they belong to, below.

**One line at the far end does not hold:** it carries its posterior-cingulate output to structure 7
as *not confirmed*. **This file declares it.** Owed at `17_insula_claustrum_habenula`.

**One open question at the far end is closed as a negative.** That file asked whether its split-out
cortical output class had covered the **dorsolateral prefrontal cortex** and left it unchecked.
**Structure 5's Inputs declare no insular input of any kind** — so the
class either did not cover it or the consumer does not carry it. **A recorded negative, not an absence
of evidence.**

**And one numbering question stands open in both files.** Structure 8 holds Brodmann areas
**24 and 32**; that file's midcingulate entry holds **24′ and 32′**. **Neither file states the
relationship between the two numberings.**

---

## Findings this file records against `13_neuromodulatory_systems`

**No structure in this file declares an output to any neuromodulatory nucleus, and it is a negative
covering four of that file's endpoints at once.** Its ventral tegmental area, locus coeruleus and raphe nuclei each declare
`← prefrontal cortex`, and its basal forebrain declares `← limbic and prefrontal cortex`. **The nine
Outputs slots in this file** reach cortex, the basal ganglia, the thalamus, the
amygdala, the bed nucleus of the stria terminalis, the hypothalamus, the temporal pole, the insula and
the corticospinal tract. **No neuromodulatory nucleus is named as a target anywhere in this file.**

**The descending direction is declared and the ascending one is not**, which is what makes this one
finding rather than four. That file's mesocortical dopamine limb is written at the dorsolateral entry
below; its cortex-wide noradrenergic, serotonergic and cholinergic limbs are classes that cover every
entry here and are declared at neither end. **So this file receives four brain-wide modulatory
projections and declares one of them, and sends four ascending control limbs and declares none.**

**In that file's terms the missing arm is what triggers release**, and the release is what each of its
four structures is for. **Not written in here**, because writing an output on the far end's
declaration alone would assert a projection this file has read nothing for. **Owed at the source.**

---

## Findings this file records — developmental evidence bearing on co-instantiation

**This changes no edge, count or payload here, and the literature it rests on is
recorded at the source** — `human_brain_11_frontal_lobe`, its developmental-timing section, where
every claim is marked Class 2 and awaiting verification. **Repeated here only where it bears on an
invariant this rung asserts**, and the reading below is Claude's, offered to be checked.

**Whole-pathway co-instantiation gets support from an unexpected direction: development.** The
invariant says every structure and edge must be live from the outset because a partially-staged loop
computes something different rather than something incomplete, and it has until now been argued from
the loops themselves. **The developmental record runs the same way.** The long-range association
tracts reaching this section are present before birth and unmyelinated; **axon addition to the
callosum occurs exclusively before birth with none postnatally**, the count *overshoots* the adult
figure by about 3.5× in monkey, and the excess is removed by selective axonal elimination while the
neurons survive. **So the wiring is not grown in stages and then run — it is laid down complete,
over-complete in fact, and then reduced.** A staged bring-up is not an approximation of that; it is
the reverse of it.

**But the support is for the edge set only, and the second half of the record cuts the other way for
sizing.** Synaptic spine density on the **layer IIIC cortico-cortical** cells of dorsolateral
prefrontal cortex — the cells of origin of this section's long-range edges — runs **two- to threefold
above adult values and is not pruned to adult level until the third decade.** **So the edge set is
early and uniform while the parameter memory on those edges is late and prefrontally exceptional**,
and the two cannot be given one developmental story.

**What it does not settle, stated so it is not over-read.** Nothing found bears on **fan-in**, which
is *to derive* on every input in this file and is the term the sizing rests on. A spine count is not
a fan-in: it is a density on one cell's dendrite at one age, and it peaks at a value the adult
structure does not keep. **The source of the finding frames the protraction as plasticity rather than
capacity**, and reading an unpruned spine excess as storage would assert exactly the payload claim the
measurement declines to make. **Not used in any sizing line here.**

---

## Structural invariants

Both bind every structure and every edge below. Conformance is noted per structure.

### Whole-pathway co-instantiation

Every structural unit exists and is active from the outset. No sequential bring-up, no unit that
comes online later, no enable flag holding a unit off until it is needed. A feedback loop with a
missing stage in it is not a loop.

*Biological why:* the pathway forms and runs as one active loop, not as a chain switched on stage by
stage. Every structure in this file sits on at least one loop that closes back on itself, and in
every case the loop leaves the frontal lobe and returns — the sensorimotor loop through parietal
cortex, thalamus, basal ganglia and cerebellum; the oculomotor loop through the lateral
intraparietal area and the superior colliculus; the audiomotor language loop through the posterior
superior temporal gyrus and the supramarginal gyrus; the limbic value loop through the ventral
striatum, the ventral pallidum and the mediodorsal thalamus; and the mediodorsal-thalamic loop that
touches every prefrontal division here. **No structure in this file is a terminus.**

**Where co-instantiation cannot be checked at this rung, and it is inherited.** Eleven of this
file's edges terminate on an endpoint the source names as a *class* rather than a structure —
brainstem saccade generators, autonomic centres, sensory cortex, temporal cortex, temporoparietal
cortex, other prefrontal cortex, other frontal cortex, other association cortex. A class endpoint
has no unit to co-instantiate. Each is carried on the edge that has it, below.

**One edge leaves the map by rule rather than by omission.** The premotor corticospinal projection
terminates at muscle, which is outside the source's scope on the body side. The edge terminates at
the scope boundary; it does not close, and that is correct rather than defective.

### Per-edge latency

No edge has zero latency, and no two edges need the same latency. Every projection takes a nonzero,
finite time to carry a signal. That time is a property of the edge, is stated in real time units,
and is heterogeneous. An edge with a latency of zero does not exist.

*Biological why:* conduction and synaptic transmission take real time, and those times differ across
the map. **Every edge in this file is a neural projection** — cortico-cortical, cortico-subcortical,
callosal, or the ascending dopaminergic projection from the ventral tegmental area, which is axonal.
None is optical, endocrine, blood-borne or mechanical. So the invariant's justification covers every
edge here without exception, which is a positive statement about this file and not true of the map
as a whole.

**Every one of the 106 edges in this file reads *to derive*.** The source carries **no timing figure
of any kind** — no conduction time, no synaptic delay, no loop latency, and no myelination figure
from which one could be derived; the Myelination slot reads *unknown* at all nine structures. This
is the shape of the ignorance for this file: **timing is not partially known here, it is absent**,
and every edge below must be timed before code can be written against it.

**No global clock is assumed anywhere in this file, and none may be.** What makes the re-entrant
loops above well-defined is the physical delay on each edge, not a shared beat. The scheduling
discipline is not set, and no latency below is stated in steps, frames, cycles or ticks.

---

## Sizing basis for this file

**Counts are per hemisphere.** Every structure here is cortex and none is midline, so no whole-brain
or per-organ basis arises. The frontal lobe is the part of the map where per-hemisphere counting
matters most: Broca's area and its right-hemisphere homologue are separate structures with separate
entries below, doing different jobs, and a single number covering both would assert a symmetry that
the source explicitly denies.

**Not one structure in this file has a neuron count, and not one edge has a fan-in.** All 63 fan-ins
and all 43 fan-outs read *unknown* in the source. Under §6's threshold-gate model — parameter memory
= neurons × log₂(fan-in) / 8 bytes — **both terms are open at every structure**, so every Sizing
field below reads *to derive*. That is not nine independent gaps; it is one gap with nine instances.

**One aggregate is nevertheless closed, and it bounds most of the file.** The source gives the
granular frontal cortex anterior to the corpus callosum as **~640M neurons per hemisphere**, and
records the fraction as constant across primates rather than human-expanded. Four structures below
declare themselves part of that budget — dorsolateral prefrontal, ventrolateral prefrontal,
orbitofrontal / ventromedial prefrontal, and frontopolar cortex — and the frontal eye fields and
Brodmann area 45 are granular frontal as well. Under the threshold-gate model the log₂ term caps
hard: any fan-in up to ~65,000 costs at most 16 bits.

    prefrontal parameter memory ≤ 640,000,000 × 16 / 8 = 1.28 GB per hemisphere
    at 12 bits (fan-in ~4,100)                          = 0.96 GB per hemisphere

**So the whole granular prefrontal parameter store sits between ~0.96 and ~1.28 GB per hemisphere
across the entire plausible fan-in range — a spread of 1.33×.** The consequence for research effort
is the same one §6 draws for the visual file, and it is sharper here: **pinning a fan-in anywhere in
prefrontal cortex would move this figure by at most a third, while the per-area partition of the
640M is what every individual Sizing field below is waiting on.** The aggregate is nearly closed and
the partition is entirely open.

**This ceiling is a sum over structures, not a figure to enter on any one of them.** It is stated
once, here, for that reason. It is parameter memory only; state memory and edge storage are not
counted anywhere and are never summed with it. *(The 640M and the constant-fraction finding are the
source's. The bound and the 1.33× spread are computed here from the source's figure and §6's log₂
cap.)*

**One structure is a single transcription away from a count.** Brodmann areas 44 and 45 are among
the few frontal areas with human stereology, and the source names a study reporting **volume and
total neuron number, left and right**, without transcribing the neuron figure — it carries only the
grey-matter volumes, Brodmann area 44 at ~3.8 cm³ left against ~2.5 cm³ right, a ~1.52× leftward
asymmetry. **So Broca's Sizing field closes by reading a paper the source already cites, not by new
measurement**, which is the cheapest open number in this file. *(That the figure is one transcription
away is inferred from the source's own description of the study, not stated by it.)*

**No tile pitch is measured anywhere in this file.** There is no figure in millimetres or
micrometres at any structure. Every tangential extent below therefore reads *to derive*, and the
pitch is a single measurement per structure that would convert the whole Shape from open to
computed.

---

## 1. Premotor cortex and the supplementary motor areas (Brodmann area 6)

- **Function → structure.** Motor planning and sequencing — the stage between association cortex and
  primary motor cortex. Lateral premotor cortex maps sensory-guided reach and grasp; the
  supplementary and pre-supplementary motor areas handle internally-generated action sequences and
  initiation. The structural form is an agranular-to-dysgranular frontal sheet in posterior frontal
  cortex, carrying **at least five divisional sub-elements**: dorsal premotor cortex (**F2**),
  ventral premotor cortex (**F4** and **F5**), the **supplementary motor area**, and the
  **pre-supplementary motor area**. The split is load-bearing rather than descriptive: the
  sensory-guided payloads arrive from parietal cortex and the internally-generated ones from
  cingulate cortex, and they arrive on different sub-elements.

- **Inputs.**
  - ← **superior parietal area 5**, principally area PE (`05_sensorimotor_loop`).
  - ← **the anterior intraparietal area**, terminating on **F5** (`06_posterior_parietal`).
  - ← **the medial intraparietal area**, terminating on **F2** (`06_posterior_parietal`).
  - ← **the ventral intraparietal area**, terminating on **F4**
  (`04_dorsal_visual_parietal_stream`). *(Written by full name;
    the source file's own heading for this structure is a bare abbreviation.)*
  - ← **the supramarginal gyrus** (`06_posterior_parietal`).
  - ← **the precuneus**, from its anterior sensorimotor sector (`06_posterior_parietal`).
  - ← **the primary somatosensory cortex**, from **area 3a** (`05_sensorimotor_loop`).
  - ← **the secondary somatosensory cortex**, principally from the **parietal ventral area**
  (`05_sensorimotor_loop`).
  - ← **the ventral anterior / ventral lateral thalamus** (`12_thalamus`).
  - ← **the midcingulate cortex**, via the **cingulate motor areas**
    (`17_insula_claustrum_habenula`). **Two-ended and confirmed**: the producer declares
    `→ supplementary and pre-supplementary motor areas and premotor cortex`, names the cingulate motor
    areas as the route in the same words, and types it at its own end as *the convergence of reward or
    non-reward outcome with action and spatial information, turned into a motor plan*. **Payload owed
    at that end and untyped at this one**, so the type above is the producer's and is carried, not
    asserted here.
  - ← **the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus**
    (`08_medial_temporal_lobe`) — the **valence tag**: a gain on perception, attention and memory
    encoding, carrying no identity of its own; payload otherwise owed. Terminations in **ventral
    area 6**, continuous with the area 45 label at the Broca and ventrolateral entries, and lighter
    in **dorsal area 6**; **ipsilateral only**, in deep layer I, layer II and layer VI. **Two-ended.**
    **Which sub-element receives it is owed**: this structure names **F2**, **F4** and **F5**, F4 and
    F5 sit in ventral area 6 where the denser half terminates, and the producing study divides area 6
    dorsally and ventrally rather than by those names.
  - ← **the anterior cingulate cortex** (structure 8 below).
  - ← **the dorsolateral prefrontal cortex** (structure 5 below). **The ventrolateral prefrontal
    cortex is named alongside it at the source and does not declare the output** (structure 6 below);
    that half of the edge is an inherited gap and is not repaired here.

  **Two further inbound edges are declared only at their producers, both inside this file** —
  Broca's area → premotor and primary motor cortex, and the right inferior frontal gyrus → premotor
  and primary motor cortex. **The source records both as owed at this structure and this rung does
  not patch them**; they are carried on the producers' Outputs below.

  **Owed at the source: assign each of these inputs to one of the five divisional sub-elements.**
  Six of them are already assignable because their producers name the target.

- **Outputs.**
  - → **primary motor cortex** (`05_sensorimotor_loop`).
  - → **the corticospinal tract**, from a minority of cells. **The tract's consumer is muscle, which
    is outside the map's scope on the body side**; this edge terminates at the scope boundary.
  - → **the basal ganglia**, to the **motor striatum** (`09_basal_ganglia`). The consumer declares its
    cortical source as a class covering all of cortex, so this edge is two-ended only in one direction.
    **Confirmed and the note holds.** **The sector this line names is load-bearing at the far
    end and unusable there:** that entry marks its striatal **motor / associative / limbic** partition
    as a tangential axis that is *named and unbounded*, with no internal edges between sectors — **so
    this edge terminates on a partition the consumer has named and cannot allocate against.** Three of
    this file's four striatal producers name a sector; see the frontopolar entry's note for the count.
  - → **superior parietal area 5** (`05_sensorimotor_loop`).
  - → **the medial intraparietal area**, from **F2** (`06_posterior_parietal`).
  - → **the medial intraparietal area**, from **F4** and **F5** (`06_posterior_parietal`).

  **The two preceding edges are one bullet at the source, split here because they leave from
  different sub-elements.** Six edges stand against five source bullets for that reason; collapsing
  them would lose which sub-element each departs from.

  **And the split is what answers a line at the far end.** That entry's Inputs slot carries one line
  reading *← cingulate area 23, dorsocaudal premotor area F2, and ventral premotor areas F4 and F5*,
  marked **owed, and none of the three far ends declares it.** **Two of those three are this
  structure, and it declares both** — F2 on one bullet, F4 and F5 on the other, named at the
  sub-element the far end names. **So that line does not hold for the premotor limbs**, and it is
  untested for the cingulate one, whose far end is in `17_insula_claustrum_habenula` and is
  unchecked. Owed at `06_posterior_parietal`. **The far end writes the three sources on one line and
  this file writes the premotor pair on two, so a diff by line rather than by endpoint sees no
  match** — which is why the two can disagree unnoticed.

  **Recorded negative:** there is **no** edge from this structure to the middle temporal area. The
  middle temporal entry (`04_dorsal_visual_parietal_stream`) declares its frontal input from the
  frontal eye fields instead.

- **Sizing.** **To derive**, both terms. Neuron count unknown; this structure is **outside the ~640M
  granular prefrontal budget** — it is posterior frontal and agranular-to-dysgranular, with lower
  density than granular prefrontal cortex, and the source says so explicitly. Fan-in unknown on all
  thirteen inputs. Basis: per hemisphere. Synapses, axon counts, grey- and white-matter volumes all
  unknown; the corticospinal contribution is unquantified here.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated **once per divisional
  sub-element**, so five arrays at minimum, not one.
  - Laminar axis: **to derive per divisional sub-element.** Eight laminar sub-elements are named
    (1, 2, 3, 4, 5a, 5b, 6a, 6b), but the sheet is agranular-to-dysgranular and layer 4 is thin or
    absent over part of its extent, so the extent is not uniform across the tangential axes and the
    source declines to assert the standard block here.
  - Tangential axes **H, W: to derive.** No pitch measured. Whether the sheet carries a somatotopic
    map at all is open at the source — the Function field's reach-and-grasp mapping implies a body
    map and does not establish one.

- **Edge latency.** **To derive** on all nineteen edges. No timing figure at the source, and
  myelination unknown, so no conduction time is derivable either.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied. This structure is a stage in the sensorimotor loop — out to
    primary motor cortex and the basal ganglia, back through the ventral anterior / ventral lateral
    thalamus carrying the basal-ganglia selection and the cerebellar correction on one relay — and in
    reciprocal parietal loops with files 4, 5 and 6. Every arm closes outside this file. The
    corticospinal arm terminates at the scope boundary and is not required to close.
  - *Per-edge latency:* satisfied in form. Every edge is a neural projection, none is zero, none is
    assumed equal to another; values open.

- **Justification (biological).** The structure is a distinct stage because the payloads entering it
  are not muscle commands and the payload leaving it toward primary motor cortex is a sequenced,
  shaped movement that is still not a muscle command. Five sub-elements rather than one because the
  afferents segregate by sub-element in the biology — grasp affordances onto F5, reach vectors onto
  F2, peripersonal space onto F4 — and because the supplementary and pre-supplementary areas take
  internally-generated rather than sensory-guided drive. The agranular-to-dysgranular architecture is
  the reason the laminar extent cannot be asserted uniformly: layer 4 is the granular layer, and this
  sheet does not have one throughout.

---

## 2. Frontal eye fields (Brodmann area 8)

- **Function → structure.** Voluntary saccade generation and endogenous control of gaze and
  attention — the frontal node of the oculomotor loop, closing the lateral intraparietal area →
  frontal eye field → superior colliculus circuit. Granular frontal isocortex, unlike the premotor
  sheet above. **Two divisional sub-elements: the saccade area and the pursuit area.** The source's
  Function statement covers the saccade area only; the pursuit area has no function statement and is
  owed one at the source.

- **Inputs.**
  - ← **the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`). Two-ended and agreeing.
  - **A consumer declares an output from this structure that this entry does not declare, found.** `01_visual_pathway`'s V4 entry declares `← frontal eye field, terminating in all
    cortical layers — the spatial attentional gain`. **No output to V4 appears below.** The nearest
    thing that does is `→ the middle temporal area, terminating in all cortical layers` — **the same
    lamination and the same phrasing, to a different consumer in a different file.** So either this
    structure has two all-layer visual outputs and one is missing here, or one edge has been recorded
    against the wrong consumer at one of the two ends. **Owed at the source, and the two candidate
    repairs are not equivalent** — adding an edge and re-terminating an edge have different
    consequences for V4's fan-in.
  - ← **posterior parietal cortex**, beyond the lateral intraparietal area. **Class endpoint, and it
    resolves nowhere**: the parietal files were read at the source and no other parietal structure
    declares an output here. Owed at the source: name the structure, or withdraw the edge.
  - ← **the dorsolateral prefrontal cortex** (structure 5 below).
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **This edge is not declared there as a class covering all prefrontal divisions**, a reading the
    producer's input-side class invites and which is wrong. That entry declares **five
    separate named outputs**, one per consumer, this structure among them, each on its own line and
    each typed in the words above. **The class it does declare is on the return limbs, not this
    one**: its Inputs carry `← prefrontal cortex, layer 6, reciprocal — the modulator` and
    `← prefrontal cortex, layer 5 — the driver`, both marked class endpoints. **Reading the
    producer's input-side class as describing its output side is the available error here**, and it
    is available at all six entries in this file that declare this input.
    **What that opens is a further question.** The producer
    marks its own cell-class axis *to derive* — magnocellular, parvocellular and densocellular are
    named in its literature and none is written in — and states that **whether the five consumers
    receive the same amplification or differently-tuned ones is not stated at either end, and that
    this is what decides whether five edges or one is the right arity.** **A consumer that believes
    it sits inside a class has no reason to ask which division reaches it.** The belief suppressed
    the question at six sites at once. **Owed at the source: which division, and whether the
    amplification is tuned per consumer.**
  - ← **the caudal auditory belt**, directly (`02_auditory_pathway`). **Confirmed two-ended:** that file's auditory belt declares `→ prefrontal cortex, directly` with the **caudal**
    belt reaching the caudal principal sulcus and **this structure by name**, and states what the
    payload is for — **moving the eyes to the sound**, the "where" stream's motor purpose. **The
    producer writes all three of its prefrontal targets on one line**, so the arity is owed there and
    not here.

- **Outputs.**
  - → **the superior colliculus** (`14_brainstem_midbrain_hypothalamus`). **Discharged:**
    that file's superior colliculus entry declares `← frontal eye field → the intermediate layers` and
    types the payload as **a saccade goal, the cortically selected target location in eye-centred
    coordinates**, payload otherwise owed. **So this end is the untyped one**, and the termination layer
    — the intermediate layers, not the superficial visual ones — exists only at the consumer.
  - → **brainstem saccade generators**. **Class endpoint**, and unchecked — the cranial-nerve-nuclei
    file was not read at the source.
  - → **the lateral intraparietal area**, carrying the corollary discharge of the saccade command
    (`04_dorsal_visual_parietal_stream`). **The relay nucleus on this path is unnamed**: the path is
    stated as running through the
    mediodorsal thalamus. **That entry's **first** named output is
    `→ frontal eye fields`, this structure, typed as modulatory amplification. **So the relay names
    this structure; what it does not name is the onward parietal limb**, and its output list contains
    no intraparietal target of any kind. **The gap sits on the second leg of the path, not the
    first.** Owed at the source, in `12_thalamus` or here: state whether the
    corollary discharge leaves that nucleus for parietal cortex, or route it elsewhere.
  - → **the middle temporal area**, terminating in **all cortical layers**
    (`04_dorsal_visual_parietal_stream`). **Two-ended and confirmed**, declared
    at both ends with the same lamination. **That end is the typed one** — it carries the payload as
    *the spatial attentional gain signal: an enhancement or suppression by location, not a stimulus
    code*, and this line carries none.
    **This sharpens the V4 question recorded above rather than answering it.** The two consumers
    separate: **this edge is two-ended and V4's is producer-less.** So the shared wording is **not**
    evidence that one edge was mis-copied into two files — it is evidence that a single general
    description was instantiated at two consumers and declared back at one. **The repair is
    unambiguous: establish the V4 limb here, or withdraw it there.**
  - → **the medial superior temporal area**, reciprocally, **from the pursuit area**
    (`04_dorsal_visual_parietal_stream`). **Two-ended and confirmed**, typed at the far end
    as pursuit and gaze-target velocity and untyped here.
  - → **the ventral intraparietal area**, reciprocally, **from the pursuit area**
    (`04_dorsal_visual_parietal_stream`). **Two-ended and confirmed**, the far end owing
    the payload as this end does.

  **These two lines answer three lines in that file and create a problem here.** Its medial superior
  temporal and ventral intraparietal entries each state that **the frontal lobe file names no pursuit
  area and no pursuit function anywhere** — stated three times across the two entries, and not true:
  **this file names one, on the two lines above.** Owed at `04_dorsal_visual_parietal_stream`.
  **But it names it and does not describe it.** The pursuit area appears here only as a sub-element attribution on two
  outputs: **it has no heading, no count, no shape axis and no inputs**, and this structure's Sizing
  reads *to derive* on both terms with no partition of any kind.
  **What that costs is a payload with nowhere to live.** The far end states that the pursuit area
  **carries visual, vestibular and combined heading tuning of its own, so it is not simply
  downstream** — a claim about this structure, made in another file, about a sub-element this file
  mentions twice and never characterises. **Vestibular tuning in the frontal eye fields has no slot
  here at all.** **Owed at the source: give the pursuit area an entry, or state that this entry
  covers it and carry the far end's tuning claim into it.**

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown; the source does not attribute
  this structure to the ~640M granular prefrontal budget, though it is granular frontal isocortex.
  Fan-in unknown on all five inputs. Basis: per hemisphere. Synapses, axons, volumes and myelination
  all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated **twice**, once for
  the saccade area and once for the pursuit area.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular frontal isocortex.
  - Tangential axes **H, W: to derive.** No pitch measured. A saccade area generating movements to
    retinotopic targets implies a motor map of saccade vectors, but whether that map is a
    compartmentation an edge could terminate on is not established at the source.

- **Edge latency.** **To derive** on all eleven edges.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the oculomotor loop — lateral intraparietal area in, superior
    colliculus out, corollary discharge back to the lateral intraparietal area, closing through file
    4 and file 14. **Not checkable for two arms**: the brainstem saccade generators are a class with
    no structure, and the corollary-discharge relay nucleus is unnamed. Both are inherited.
  - *Per-edge latency:* satisfied in form; values open. **This is the structure where the absence
    hurts most in this file** — a saccade command, its corollary discharge, and the remapping the
    consumer performs across the movement are all timing-defined operations, and not one of the three
    edges has a time on it.

- **Justification (biological).** The frontal node of a loop whose other nodes are parietal and
  collicular; it is granular where the premotor sheet is not, which is why the standard laminar
  extent holds here and not there. Two sub-elements because saccades and smooth pursuit are different
  movement classes with different parietal partners — the pursuit area's partners are the medial
  superior temporal and ventral intraparietal areas, and the source records those edges terminating
  on it by name. **The internal edge between the two areas is not recorded and the biology requires
  one**: a pursuit movement is interrupted by saccades, so the two classes are coordinated somewhere.

---

## 3. Broca's area — inferior frontal gyrus (Brodmann area 44, pars opercularis; Brodmann area 45,
pars triangularis)

- **Function → structure.** Speech production and syntax; the frontal terminus of the auditory dorsal
  (audiomotor) stream. Strongly left-lateralised. **Two divisional sub-elements with different jobs
  and different architecture** — **Brodmann area 44**, agranular and premotor-adjacent, doing
  phonological and articulatory sequencing and hierarchical structure; **Brodmann area 45**,
  granular, doing controlled semantic retrieval and selection. **Each subdivides further**: receptor
  architecture splits area 44 into **44d** and **44v** and area 45 into **45a** and **45p**, and a
  cytoarchitectonic lineage splits area 45 into a rostral **45A** and a caudal **45B**. Whether
  45A/45B and 45a/45p are one border under two names is not established at the source.

- **Inputs.**
  - ← **the posterior superior temporal gyrus and area Spt**, via the **arcuate fasciculus**
    (file 2; the tract has an entry in file 18). Far end unchecked at the source.
  - ← **the supramarginal gyrus**, via the **arcuate fasciculus** and **superior longitudinal
    fasciculus III** (`06_posterior_parietal`).
  - ← **the ventrolateral prefrontal cortex** (structure 6 below). **This edge crosses a boundary
    whose location is not agreed** — see Shape.
  - ← **premotor cortex** (structure 1 above). **The producer does not declare it**; inherited gap,
    not repaired here.

- **Outputs.**
  - → **premotor cortex and primary motor cortex**, for articulation (structure 1 above;
  `05_sensorimotor_loop`).
    **The premotor consumer in this file does not declare this edge.** Inherited; owed at the source.
    **The primary motor consumer does not declare it either, checked.** That entry's Inputs
    slot names four sources — area 3a, premotor cortex, superior parietal area 5, and the ventral
    anterior / ventral lateral thalamus — **and no inferior-frontal source of any kind.** So this edge
    is producer-only at **both** of its two named targets, not just the in-file one, and the owed
    repair is two edges at two files rather than one.
  - → **temporoparietal cortex**, reciprocally. **Class endpoint.** One member resolves — the
    supramarginal gyrus, which declares the reciprocal input (`06_posterior_parietal`). The others
    are unnamed. Owed at
    the source: name them, or narrow the endpoint.

- **Sizing.** **To derive**, both terms — but **this is the cheapest open figure in the file.** The
  source names a human stereological study reporting volume and total neuron number for areas 44 and
  45, left and right, and reports a significant left-greater-than-right neuron-number asymmetry in
  area 44, without transcribing the count. What it does carry is grey-matter volume: **area 44 ~3.8
  cm³ left, ~2.5 cm³ right**, a ~1.52× leftward asymmetry. Fan-in unknown on all four inputs. Basis:
  per hemisphere, and the asymmetry is why that basis matters here.
  - **One fan-like figure exists and must not be entered as a fan-in.** The arcuate trunk carries a
    median of about 6,200 axons between areas within a hemisphere, and direct posterior-temporal to
    inferior-frontal connections are under ~5% of it. That counts a tract's inter-areal axons, not
    contacts per cell, so it does not enter log₂(fan-in). Reconciling the two measures is owed at the
    source.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated **once per divisional
  sub-element**, and **the two do not have the same rank-3 extent**:
  - **Brodmann area 45: laminar axis = 8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b. Granular, with a
    well-developed layer 4. The source records a specific laminar signature here: layer III holds
    small-to-medium pyramidal cells above and **clusters of large, deeply stained, densely packed
    pyramidal neurons** in its deeper part; layer Va holds medium pyramidal cells and layer Vb is
    cell-sparse, so layer VI separates clearly from Va. **The combination of the deep-layer-III
    clusters with a well-developed layer 4 is what distinguishes this area from all its neighbours**
    — the sharpest laminar signature anywhere in this file, and a sub-element-level measurement rather
    than a generic block.
  - **Brodmann area 44: laminar axis = 7** — 1, 2, 3, 5a, 5b, 6a, 6b. Agranular; layer 4 thin or
    absent.
  - **So a single laminar extent is wrong within one structure.** This is the case that forces the
    laminar axis to be a property of the divisional sub-element rather than of the structure.
  - Tangential axes **H, W: to derive.** No pitch measured. **And the tangential boundary itself is
    not reliably placeable**: the area 44 / area 45 border is conventionally taken at the ascending
    ramus of the lateral sulcus, but the ascending and horizontal rami are highly variable and the
    sulcus diagonalis is present in only about half of hemispheres. **That is not a naming dispute
    and cannot be fixed by renaming** — it is a statement that the two sub-elements' tangential
    extents are individually variable.
  - **Brodmann area 45 is claimed by this structure and by the ventrolateral prefrontal cortex below,
    and both claims are real** — Broca's area is classically 44 plus 45, the ventrolateral structure
    is 45 plus 47, and 45 is the member the two conventional groupings share. The source proposes
    assigning **45B / 45p** here and **45A / 45a** to the ventrolateral structure, and records the
    proposal as unadopted. **Until it is adopted the two structures overlap and their Shapes cannot
    both be allocated.**

- **Edge latency.** **To derive** on all six edges. The arcuate fasciculus has an entry in file 18
  and is where a conduction time for two of them would be derived from; myelination is unknown there
  as it is here.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the audiomotor loop — posterior superior temporal gyrus and
    supramarginal gyrus in via the arcuate fasciculus, temporoparietal cortex back out reciprocally —
    which closes through files 2 and 6. **Not checkable for the temporoparietal arm**, which is a
    class.
  - *Per-edge latency:* satisfied in form; values open.
  - **Not conformant on Shape**, and the defect is inherited: a structure whose tangential extent
    overlaps another structure's cannot be allocated, and this one does until the area 45 assignment
    is settled at the source.

- **Justification (biological).** The two sub-elements differ in cytoarchitecture, not only in job:
  one is agranular and one granular, which is the same structural distinction that separates premotor
  from prefrontal cortex above, occurring here **inside one structure**. Left lateralisation is
  structural rather than functional shorthand — it appears as a volume and neuron-number asymmetry —
  which is why the right homologue is a separate structure below rather than a mirrored copy of this
  one. **The internal edge from area 45 to area 44 is required by the Function statement** — a
  pipeline from semantic selection to articulatory sequencing needs one — **and is not recorded at the
  source.**

---

## 4. Right inferior frontal gyrus — affective-prosody production (right Brodmann area 44 / 45 homologue)

- **Function → structure.** The production node for affective (emotional) prosody — the
  right-hemisphere homologue of Broca's area, and the frontal complement to the right perceptual
  prosodic homologues in the auditory file. A right anterior frontal lesion produces motor
  (expressive) aprosodia: speech gone flat and monotone, unable to impose emotional intonation,
  mirroring Broca's aphasia on the left. **The lateralisation is a bias, not a dichotomy** —
  producing emotional prosody activates the inferior frontal gyrus bilaterally with a larger
  right-hemisphere extent — so this is the right-dominant end of a bilateral network. Isocortex.
  **Two divisional sub-elements by homology: right Brodmann area 44 and right Brodmann area 45.**

- **Inputs.**
  - ← **the right auditory prosodic stream** — the right superior temporal gyrus and sulcus
    homologues (file 2). Far end unchecked at the source.
  - ← **the amygdala**, from the **basal** and **accessory basal** nuclei (`08_medial_temporal_lobe`).
  - ← **the anterior insula** (`17_insula_claustrum_habenula`) — the **salience signal**: *this event
    is behaviourally relevant now*; payload otherwise owed. **Two-ended and confirmed.**
    **The producer declares `→ right inferior frontal gyrus` on its own line**, having split that
    line out of a compound naming one region and one class, so it reaches this structure by name and
    not inside a class.
  - ← **the orbitofrontal cortex** (structure 7 below). **The producer does not declare it**;
    inherited gap.
  - ← **premotor cortex** (structure 1 above). **The producer does not declare it**; inherited gap.
  - ← **the contralateral inferior frontal gyrus**, via the **corpus callosum** (file 18).
    **The laminar termination is specified and is load-bearing**: callosal origin is layers 3 and 5,
    termination is throughout layers 2–6, densest in 2 and 3 and **sparsest in layer 4** — so this
    input **avoids the layer a thalamic driver targets**. All callosal fibres are excitatory; the
    inhibitory effects are feedforward through local interneurons.

- **Outputs.**
  - → **premotor cortex and primary motor cortex** (structure 1 above; `05_sensorimotor_loop`).
  **The premotor
    consumer in this file does not declare it**; inherited gap. **The primary motor consumer does not
    declare it either, checked** — the same result as the homologous edge at Broca's area,
    and from the same reading of that entry's four-source Inputs slot.
  - → **right temporoparietal cortex**, reciprocally. **Class endpoint**, and it was marked unchecked
    with the far end placed in the auditory file. **Checked against `06_posterior_parietal`,
    and the placement was too narrow.** That file's supramarginal gyrus entry states that its ventral
    part, together with the posterior superior temporal sulcus, **forms the right-dominant
    temporoparietal junction of the ventral-attention network** — so a candidate for this class sits in
    the parietal file and not only in the auditory one.
    **What was found there is not a resolution but a second class facing this one.** That entry's own
    Outputs slot declares an output to the **ventral-attention frontoparietal network**, typed there
    as a reorienting
    signal — *a one-bit interrupt with a location attached* — and marked there as an endpoint that
    **does not resolve to nodes.** **So each end declares a class whose description names the other
    end's network, and neither declares the other structure by name.** Two unresolved classes pointing
    at each other are not a two-ended edge, and reading one as confirming the other would manufacture
    an edge from two absences. **Owed at the source: name the node at one end or the other.**
- **Sizing.** **To derive**, both terms. No clean per-area count. **It is bounded above by the left
  side**: this is the smaller side of the documented left-greater-than-right area 44 asymmetry, so
  once Broca's count is firmed this structure's is bounded below it. Grey-matter volume unknown here,
  **but bounded above by the ~2.5 cm³ right-side figure recorded at Broca's entry, which is the same
  measurement recorded from the other side.** Reconciling the two records is owed at the source.
  Fan-in unknown on all six inputs. Basis: per hemisphere — right.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element.
  - Laminar axis: **contested for this side.** By homology it would be 8 in area 45 and 7 in area 44,
    as on the left. Whether the agranular/granular difference holds on the right is not established,
    and it is exactly the kind of property the documented left-right asymmetry might not preserve.
    **To derive.**
  - Tangential axes **H, W: to derive.** No pitch measured.
  - **The Function statement extends this structure past its own boundary.**
    Producing emotional prosody activates areas 44, 45 **and 47**, extending into **anterior insula**
    — area 47 belongs to the ventrolateral structure below and the anterior insula to
    `17_insula_claustrum_habenula`. **An edge connects to one of them**: this entry's Inputs slot declares `← the anterior insula`,
    and the producer declares it back by name. **A claim that no edge connects to either would
    contradict this entry's own Inputs slot, and no cross-file read is needed to see that** — only
    reading the entry whole. **The area 47 half stands**: the ventrolateral structure below declares no output here.
    **Owed at the source: write the area 47 edge, or state that that half is co-activation rather than
    connection.**

- **Edge latency.** **To derive** on all eight edges. The callosal edge is the one whose physical
  substrate is described — the corpus callosum has an entry in file 18 — and its myelination is
  unknown there.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the prosodic loop through the auditory file, and for the
    callosal loop with the contralateral structure. **Not checkable for the temporoparietal arm**
    (class) and for three arms whose producers do not declare them.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** A separate structure from Broca's area rather than a mirrored copy,
  because the two sides are not identical: the volume and neuron-number asymmetry is measured, and
  the jobs differ — propositional language on the left, affective components on the right. The
  clinical evidence is symmetric in weight: aprosodia after right-hemisphere stroke is about as
  common as aphasia after left-hemisphere stroke. **The callosal input's laminar profile is a
  structural claim, not a detail** — an input that avoids layer 4 is not arriving as a driver, and
  that distinction is what makes the two hemispheres one network rather than two.

---

## 5. Dorsolateral prefrontal cortex (Brodmann areas 9 and 46)

- **Function → structure.** Working memory, executive control, goal maintenance and top-down
  attention — holding and manipulating information across delays and biasing posterior cortex toward
  goals. The action-control, "where" apex of prefrontal cortex. Granular prefrontal isocortex, thick
  but low-density. **Two divisional sub-elements are named — Brodmann area 9 and Brodmann area 46 —
  and no edge uses either**, although other files address this structure as *area 46* specifically,
  so the finer name is already in use outside it. **A third location is named by an edge and not by
  the heading**: the **caudal principal sulcus**, which is a location within area 46 rather than
  either named area. Whether it is a sub-element of area 46 or a separate one is owed at the source.

- **Inputs.**
  - ← **the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`), which names **area
  46**. Two-ended and agreeing.
  - ← **the angular gyrus** (macaque area 7a) (`06_posterior_parietal`). **The producer declares an
    output to the ventrolateral prefrontal cortex and not to this structure**, so this edge has no
    producer end. Owed at the source: establish it, or withdraw it.
    That entry's Outputs slot carries three lines — a four-member default-mode class naming the
    ventrolateral prefrontal cortex explicitly, and two intraparietal edges — **and no dorsolateral
    target under any name.** The distinction is the producer's own: it separates the two prefrontal
    divisions and names only the ventral one.
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.** **This is the edge the structure's headline function
    depends on** — see Justification.
  - ← **the ventral tegmental area**, the mesocortical projection (`13_neuromodulatory_systems`).
    **Two-ended and confirmed, and this end is the untyped one.** The producer types it as
    dopamine **setting the gain** on prefrontal working-memory and rule representations, payload
    otherwise owed, and this line takes that wording. **This structure is the only entry in this file
    that declares the limb** — the ventrolateral, orbitofrontal / ventromedial, cingulate and
    frontopolar entries declare no dopaminergic input under any name, and the producer marks *which of
    the five prefrontal entries receive it* as owed. **So the class has exactly one member here.**
    **That bears on this structure's own gain story**: it already takes modulatory amplification from
    the mediodorsal thalamus, so **two different gain sources are declared onto one structure and
    neither entry says how they differ.** **Owed at the source.**
  - ← **other prefrontal cortex.** **Class endpoint**, unresolved. Of the four in-file candidates,
    the anterior cingulate cortex declares an output here and the frontopolar cortex declares one to
    a class that covers it; the ventrolateral and orbitofrontal structures declare nothing. Owed at
    the source: name the others, or withdraw.
  - ← **the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus**
    (`08_medial_temporal_lobe`) — the **valence tag**, as at the other prefrontal consumers; payload
    otherwise owed. Terminations in **Brodmann area 9** medially and laterally and **patchily in area
    46**, in the lower bank of the principal sulcus; **ipsilateral only**, in deep layer I, layer II
    and layer VI. **Two-ended.** **The lightest and least consistent of the producer's four lateral
    edges** — the area 46 label was present in one hemisphere and absent in the other of the same
    animal, and absent altogether in a second case. **The area 46 limb lands on this structure's own
    unused divisional sub-elements**, which the Internal structure slot records as named in the
    heading and used by no edge; the producer names both areas, so this is the first edge here that
    could be assigned. **Owed: assign it.**
  - ← **the anterior cingulate cortex** (structure 8 below).
  - ← **the caudal auditory belt**, directly, onto the **caudal principal sulcus** (file 2).
    Unchecked at the source.
  - **Recorded negative: there is no insular input to this structure.**
    `17_insula_claustrum_habenula` split a compound cortical output into named lines and left open
    *whether the class had covered the dorsolateral prefrontal cortex*. **This Inputs slot was read
    against that question and declares no insular source of any kind.** So either the class never
    covered this structure, or it did and the consumer does not carry it. **The question is closed as
    a negative rather than left unchecked**, which is the stronger of the two states.

- **Outputs.**
  - → **the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`), which names **area 46**.
  - → **the anterior intraparietal area** (`06_posterior_parietal`), which declares an input from
  prefrontal areas 46
    and 12.
  - → **sensory cortex**, top-down bias. **Class endpoint**, remaining after the two parietal members
    above are split out, and unchecked at the source — the visual and auditory files were not read there.
    **Checked against `05_sensorimotor_loop` and closed as a negative for that file.**
    Neither somatosensory entry admits a frontal source of any kind: primary somatosensory cortex
    declares two inputs, both from the ventral posterior thalamus, one onto the core and one onto the
    matrix; the second somatosensory area declares the thalamus, the anterior pulvinar, primary
    somatosensory cortex and its callosal partners. **So either this class never covered somatosensory
    cortex, or it did and neither consumer carries it.** The visual and auditory members remain
    unchecked — this closes one file, not the class.
  - → **the frontal eye fields** (structure 2 above).
  - → **premotor cortex** (structure 1 above).
  - → **the basal ganglia**, to the **associative striatum** (`09_basal_ganglia`). The consumer
    declares its cortical source as a class. **Confirmed**, and the same sector caveat
    applies as at premotor cortex above.
  - → **the anterior cingulate cortex** (structure 8 below).

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere** — see the sizing basis above; this structure's share of that
  budget is the open quantity, not the budget. Fan-in unknown on all eight inputs. Basis: per
  hemisphere. Synapses, axons, volumes and myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, so at least two arrays.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular prefrontal
    isocortex.
  - Tangential axes **H, W: to derive.** No pitch measured. **And the tangential organisation is
    load-bearing here in a way it is not elsewhere in this file**: working memory across delays is
    standardly attributed to recurrent local connectivity, so the extent over which recurrence runs
    is the structure's stated function. Owed at the source.

- **Edge latency.** **To derive** on all fifteen edges. **The absence is load-bearing at this
  structure**: a delay period is a duration, and the structure whose job is to hold information
  across delays has no time on any edge into or out of it.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the parietal loop (file 4, reciprocal), the thalamic loop (file
    12), the cortico-striatal loop (file 9), and the cingulate loop (structure 8, reciprocal). **Not
    checkable for two arms** — "other prefrontal cortex" and "sensory cortex" are classes — and one
    inbound arm, from the angular gyrus, has no producer at all. All inherited.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The thalamic input is what makes this a distinct stage rather than
  a region of cortex that happens to be persistently active: it carries **no categorical content**
  and amplifies the cortex's own recurrent connectivity, sustaining rule and working-memory
  representations that are generated in and belong to the cortex. **The thalamus is a temporal
  scaffold, not a source.** That has a direct structural consequence for the build: **the content
  this structure holds lives on an internal recurrent edge, and no such edge is recorded at the
  source.** The external evidence points at the missing edge more specifically here than anywhere
  else in this file — the function is a claim about internal connectivity, and the thalamic edge is
  typed as amplifying exactly that. Naming the dopaminergic producer matters for the same reason: the
  mesocortical projection to this structure is one of the map's best-known edges and had been carried
  as an adjective rather than a source.

---

## 6. Ventrolateral prefrontal cortex (Brodmann areas 45 and 47)

- **Function → structure.** Controlled retrieval and selection — of words, semantic knowledge and
  responses; the "what" / semantic-control counterpart to the dorsolateral structure above. Granular
  prefrontal isocortex. **Two divisional sub-elements: Brodmann area 45 and Brodmann area 47.**
  **Area 47 is macaque area 12** — Brodmann's own area 47 incorporates the region he identified as
  area 12 in the monkey, which is why the literature writes the area as 47/12. Two other files
  terminate edges on "area 12", so the correspondence is load-bearing: without it those edges land on
  a name this structure does not use. Owed at the source: put the correspondence in the heading.

- **Inputs.**
  - ← **the temporal pole** (`07_anterior_temporal_lobe`). **Two-ended, confirmed**, and
    the producer types it where this end does not: **the amodal concept, for controlled retrieval and
    selection.** That producer records this end as declaring the edge and naming the region and
    **typing nothing — no payload line and no fan-in — and marks it owed here.** It is.
  - ← **the inferotemporal cortex** (`01_visual_pathway`). **Confirmed at the producer itself and
    not through a third file**: its inferotemporal entry declares `→ prefrontal cortex, ventrolateral
    — identity, for controlled retrieval and selection`. **Two-ended, and the producer types the payload where this end does
    not**, naming both the content (identity) and the use (controlled retrieval and selection).
    *(Written by full name; the source file's own heading for this structure is a bare abbreviation.)*
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.**
  - ← **the anterior auditory belt**, directly, onto **areas 12 and 45** (file 2). Unchecked at the
    source. This is the auditory "what" stream reaching prefrontal cortex without waiting for the
    temporal endpoints.
  - ← **the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus**
    (`08_medial_temporal_lobe`) — the **valence tag**, as at the other prefrontal consumers; payload
    otherwise owed. **The densest of the producer's four lateral edges**: terminations across **area
    12**, which this structure's Internal structure slot resolves to **Brodmann area 47**, in deep
    layer I, layer II and layer VI, continuing dorsally into much of **Brodmann area 45**;
    **ipsilateral only**. **Two-ended.** **This is a second external edge assigning itself to areas 12
    and 45 specifically, arriving from a different file and a different modality than the anterior
    auditory belt above.** **Two independent external demands on one unmade division is a different
    state from one**, and the divisional internal edges below stay owed on stronger grounds than a single
    demand would give.
  - ← **the supramarginal gyrus** (`06_posterior_parietal`).
  - ← **the angular gyrus** (`06_posterior_parietal`).

- **Outputs.**
  - → **Broca's area** (structure 3 above). **The two structures share Brodmann area 45**, so this
    edge crosses a boundary whose location is not agreed — see Shape.
  - → **temporal cortex**, retrieval bias. **Class endpoint**, and it resolves nowhere: the temporal
    pole (file 7) does not declare an input from this structure, and the auditory and visual files
    were not read at the source. Owed: name the target.
  - → **the basal ganglia** (`09_basal_ganglia`). The consumer declares its cortical source as a
    class. **Confirmed. This is the one of this file's four striatal producers that names
    no sector**, where premotor, dorsolateral and orbitofrontal / ventromedial each name one.
    **Owed here: name the sector, or establish that this projection is not sectored.**
  - → **the supramarginal gyrus**, reciprocally, via the **arcuate fasciculus** and **superior
    longitudinal fasciculus III** (`06_posterior_parietal`).
  - → **the anterior intraparietal area**, from **area 12** (`06_posterior_parietal`).

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere**. Fan-in unknown on all seven inputs. Basis: per hemisphere.
  Synapses, axons, volumes and myelination all unknown. **The area 45 overlap with Broca's area makes
  even the partition ill-posed until it is settled**: a neuron count for area 45 cannot be assigned to
  one structure or the other while both claim it undivided.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular prefrontal
    isocortex. **Consistent with Broca's record of area 45 as granular**, which is worth holding
    because the same area is described at two structures.
  - Tangential axes **H, W: to derive.** No pitch measured.
  - **The tangential extent overlaps structure 3's and the overlap is real, not a bookkeeping
    error.** Broca's area is classically areas 44 plus 45; this structure is areas 45 plus 47; area
    45 is the member the two conventional groupings genuinely share. Area 45 is not indivisible — a
    cytoarchitectonic lineage splits it into rostral **45A** and caudal **45B**, and receptor
    architecture splits the same territory into anterior **45a** and posterior **45p** — but whether
    those are one border under two names is not established. **The source proposes 45A / 45a here,
    rostral and continuous with area 47, and 45B / 45p to Broca's area, caudal and abutting area 44,
    and records the proposal as unadopted.** Until it is adopted, neither structure can be allocated.
  - **The overlap is wider than area 45.** Functional imaging routinely includes pars orbitalis
    (area 47) and the ventral part of Brodmann area 6 in what is called "Broca's region", which would
    put this structure's other sub-element and part of structure 1 inside structure 3's functional
    territory. Recorded, unresolved at the source.

- **Edge latency.** **To derive** on all twelve edges. Two of them run in the arcuate fasciculus and
  superior longitudinal fasciculus III, which have entries in file 18 and are where their conduction
  times would be derived from.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the parietal loop (file 6, reciprocal), the thalamic loop (file
    12), the cortico-striatal loop (file 9), and the in-file link to Broca's area. **Not checkable for
    the temporal-cortex arm**, which is a class.
  - *Per-edge latency:* satisfied in form; values open.
  - **Not conformant on Shape**, for the same inherited reason as structure 3: two structures claim
    one undivided area, and neither can be allocated until the claim is divided.

- **Justification (biological).** The "what" counterpart to the dorsolateral structure: its afferents
  are the identity-bearing ones — the temporal pole's amodal concepts, inferotemporal object and face
  identity, the auditory *what* stream's call and identity features — where the dorsolateral
  structure's are spatial and attentional. That the auditory *what* stream arrives here directly,
  onto areas 12 and 45, rather than by way of the temporal endpoints, is a structural claim about
  where the stream terminates and is the reason the area-12 correspondence has to be carried.

---

## 7. Orbitofrontal / ventromedial prefrontal cortex (orbitofrontal cortex: Brodmann areas 11 and
13; ventromedial prefrontal cortex: Brodmann areas 14, 25 and 32)

- **Function → structure.** Value, reward and outcome-based decision-making; emotion regulation and
  social or affective evaluation. Assigns and updates the expected value of options. **Five divisional
  sub-elements are named and no edge uses any of them** — areas 11 and 13 orbitally, areas 14, 25 and
  32 medially. **This is the largest named-but-unused sub-element set in the file**, and other files
  are already treating the structure as two: file 9 names **infralimbic cortex**, which is area 25,
  and files 6 and 17 address it as **medial prefrontal cortex**, which is the ventromedial half and
  not the orbital half.
  **The edges sort into two systems and the Function statement covers both in one sentence.** Value,
  reward and outcome-based decision-making is orbital business; the default-mode inputs from the
  precuneus, angular gyrus and posterior cingulate cortex are medial and have nothing to do with
  taste or object value. Owed at the source: split the structure, or assign every edge to a
  sub-element. *(That the edges sort into two systems is inferred here from the edge list, not stated
  at the source as a split.)*

- **Inputs.**
  - ← **the hippocampal formation**, from the **subiculum** (with the adjacent **prosubiculum** and
    distal **CA1**), via the **fornix** (`08_medial_temporal_lobe`) — the **completed episode**;
    payload otherwise owed at both ends, the producer recording the same limit on its parietal and
    cingulate limbs. Terminating principally in **layer III** of Brodmann areas **11**, **13**, **14**
    and **25**; **ipsilateral only**. **Two-ended.** ***This edge uses four of this structure's five
    named-but-unused divisional sub-elements, and it is the first edge in the file with a claim on any
    of them*** — the producer's evidence names the termination areas individually, so the assignment
    arrives with the edge rather than being owed after it. ***And the route is load-bearing rather
    than descriptive***: the projection travels by the **fornix and by no other route**, so the tract
    is a condition on the edge and not a description of it.
  - ← **the amygdala**, from the **basal** and **accessory basal** nuclei
  (`08_medial_temporal_lobe`). Orbital.
  - ← **the gustatory pathway** and ← **olfactory cortex** (file 3). Orbital. Unchecked at the source,
    and **splitting the line is owed**: two modalities are not one source.
  - ← **the inferotemporal and temporal cortex** (`01_visual_pathway`). Orbital. **Checked, and the producer does not declare it.** That file's inferotemporal entry declares one
    prefrontal output only — `→ prefrontal cortex, ventrolateral` — and this structure is a **separate
    entry** in this file from the ventrolateral one, so the ventrolateral declaration does not cover
    it. **This edge is declared at the consumer and at no producer.** The endpoint is also compound —
    *inferotemporal* and *temporal cortex* are not one source — so the split is owed as well as the
    producer end. **Owed at the source: declare it at the producer, or withdraw it.**
  - ← **the basal ganglia**, via the **ventral pallidum → mediodorsal thalamus** limb of the limbic
    loop (`09_basal_ganglia`). **An ambiguity is inherited on this edge**: the mediodorsal entry
    attributes its basal-ganglia input to the dorsal pallidum rather than the ventral one, and that
    file marks it unresolved. **Checked, and the ambiguity is worse than inherited — it is
    a three-file contradiction and this entry is one of the three ends.** **This line believes the limb
    leaves the ventral pallidum**; `12_thalamus`'s mediodorsal entry declares its basal-ganglia input
    from the **internal globus pallidus and substantia nigra pars reticulata** and names no ventral
    source; and `09_basal_ganglia` cannot say which, because **the ventral pallidum is an entry there
    while the dorsal nuclei are sub-elements of a different entry** — one functional stage carried at
    two levels of the hierarchy. **The payloads differ and that is what puts it on the wire**: tonic
    inhibition alone from the dorsal nuclei, **inhibition plus a computed relative value** from the
    ventral pallidum, which that file records as computing value rather than relaying it. **So what
    arrives at this structure on this edge is not settled**, and this structure's value story is what
    depends on it. **Owed at the source, at the boundary question rather than per-edge.**
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.**
  - ← **the posterior cingulate cortex** (`17_insula_claustrum_habenula`). Medial. **Two-ended and confirmed.**
    **The producer's line carries the edge as *not confirmed* and that does not hold — this file
    declares it.** Owed at `17_insula_claustrum_habenula`. The producer names it *the medial-prefrontal
    default-mode partner*, which is the medial half of this structure and not the orbital half — **so
    the far end is already treating this structure as two, as file 9 and file 6 are.** Payload owed at
    both ends.
  - ← **the precuneus** (`06_posterior_parietal`). Medial. **Two-ended and confirmed.**
    **The producer's line carries a compound naming this structure and the medial temporal lobe as
    *neither far end declares it*, and that does not hold for this half — this structure declares
    it.** Owed at `06_posterior_parietal`. The medial temporal half of that compound is unchecked.
  - ← **the angular gyrus** (`06_posterior_parietal`). Medial. **Checked and it is not
    two-ended by name.** That entry's Outputs slot names the ventrolateral prefrontal cortex and not
    this structure; the only line that could carry this edge is its four-member **default-mode
    partners** class, which it marks as unresolved. **So this input is a located candidate for that
    class rather than a declared edge** — the class has a consumer here that declares the input by
    name, which narrows it by one member without closing it. Owed at the source: name the member, or
    withdraw this input.

  **Both parietal inputs above are one-way at this structure, and the direction is the same one.**
  This entry declares no output to the precuneus and none to the angular gyrus, and the far file
  records both absences from its own side — its precuneus entry marks its medial-prefrontal input
  *owed, one producer declares nothing*, and its angular gyrus entry marks the same input owed.
  **Both marks hold.** The Outputs slot below leaves for the amygdala, the bed
  nucleus, the hypothalamus, the ventral striatum and pallidum, the temporal pole, the insula, the
  right inferior frontal gyrus, the periaqueductal gray and a class of autonomic centres — **nothing
  medial-parietal.** So the medial wall's parietal traffic reaches this structure and does not return,
  which is the same shape the habenular finding below records in the opposite direction.
  - ← **the insula** (`17_insula_claustrum_habenula`), reciprocally — the **salience signal** and the
    **interoceptive state**; payload otherwise owed. **Two-ended and confirmed.**
    **The producer declares `→ orbitofrontal / ventromedial prefrontal cortex` by name and types
    it**, naming the interoceptive state as the reciprocal limb, so the edge arrives named and not
    inside a cortical class.

- **Outputs.**
  - → **the amygdala** (`08_medial_temporal_lobe`).
  - → **the bed nucleus of the stria terminalis** (`08_medial_temporal_lobe`).
  - → **the hypothalamus** (`14_brainstem_midbrain_hypothalamus`). **Checked and it is
    producer-only**: that entry's Inputs declare no prefrontal or orbitofrontal source under any
    name. **Owed at the source: accept it there, or withdraw it here.**
  - → **the ventral striatum** (`09_basal_ganglia`). **Two-ended and confirmed, and this
    end is the untyped one.** That entry writes the edge as its own line rather than inside its
    cortical class, precisely because this producer names the ventral sector, and types the payload as
    **value — the expected value of the options.** **This line takes no payload and the far end records
    that it does not.** **Owed here: type it, or take the producer's wording.**
  - → **the ventral pallidum** (`09_basal_ganglia`). The consumer's line also names **infralimbic
    cortex**, which is area 25 and therefore a sub-element of this structure that the heading names and
    no edge uses. **Two-ended and confirmed.** **That entry carries the edge as *the
    producer declares no such edge*, with the repair owed at this file, and that does not hold — it
    is declared, on this line.** Owed at `09_basal_ganglia`. **Both ends record the same
    sub-element debt from opposite sides** — the far end names infralimbic cortex on its endpoint, this
    end names area 25 in its heading, and **neither end has an edge that uses it.** **Payload owed
    here**, the far end typing it as **value** as it does for the striatal limb above.
  - → **the temporal pole** (`07_anterior_temporal_lobe`). **Two-ended, confirmed.** That entry
    declares `← orbitofrontal cortex — value`, and also states that **this file declares no temporal
    target at all.** **That is false — this line is the target.** Owed at
    `07_anterior_temporal_lobe`. **Payload is owed at both ends beyond *value*.**
  - → **the insula** (`17_insula_claustrum_habenula`). **Two-ended and confirmed; payload
    owed at both ends**, which the producer's line marks in the same words.
  - → **the right inferior frontal gyrus** (structure 4 above).
  - → **the periaqueductal gray** (file 14).
  - → **autonomic centres**, remainder. **Class endpoint** after the periaqueductal gray is split out,
    and it resolves nowhere. Owed at the source: name them.

  **One output the far end declares and this entry does not, found and not written as an
  edge.** `17_insula_claustrum_habenula`'s habenula entry declares `← ventromedial prefrontal cortex`,
  onto the **lateral habenula**, typed a **bad-outcome expectation**, and marks the producer as
  declaring no such edge. **It is correct: nothing below leaves for the habenula.** **Owed at the
  source.**
  **The endpoint it names is the medial half of this structure, not the whole**, which is the same
  split the posterior-cingulate input above already forces — so if the split is adopted, this edge and
  that one leave and arrive on the ventromedial sub-elements and neither belongs to the orbital ones.
  **Together with structure 8's habenular limb, two of the three cortical producers of that file's
  value brake are in this file and neither declares its edge.**

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere** — with the caveat that the budget is defined over *granular*
  frontal cortex and area 25 is agranular, so the five sub-elements are not all inside it on the same
  footing. Fan-in unknown on all ten inputs. Basis: per hemisphere. Synapses, axons, volumes and
  myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, so **five arrays**.
  - Laminar axis: **to derive, per sub-element, and it differs across them.** Areas 11 and 13 are
    orbital granular-to-dysgranular; area 25 (infralimbic) is **agranular**; area 32 is transitional.
    A single laminar extent is wrong across this structure, as it is across Broca's area, and the
    source declines to assert one. *(That the standard block does not hold across all five is the
    source's reading of the named areas' architecture, offered there to be checked.)*
  - Tangential axes **H, W: to derive.** No pitch measured. **And the tangential organisation is
    itself in question**: the value axis this structure computes on is **body-relative** — its zero
    and slope are set by motivational state, because there are no receptors for reward — and whether
    that axis is a spatial organisation here or a population code is not established at the source.

- **Edge latency.** **To derive** on all twenty edges. This is the widest edge fan in the file and
  not one of the twenty carries a time.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the limbic value loop — out to the ventral striatum and ventral
    pallidum, back via the ventral pallidum → mediodorsal thalamus limb — which closes through files 9
    and 12; and for the reciprocal amygdalar, insular and default-mode loops. **Not checkable for the
    autonomic-centres arm**, which is a class on this side of the scope boundary. Inherited.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The structure is where identity becomes value: object and face
  identity, taste and odour quality, a valence tag from the amygdala and an interoceptive state from
  the insula all arrive, and an expected value leaves toward the ventral striatum. **The step that
  performs that conversion has no edge at the source** — this is the structure in this file whose
  stated job most explicitly names an operation with no declared internal substrate. The value axis
  being body-relative is the reason the conversion cannot be a fixed function of the inputs: the same
  food's value falls once sated, so the mapping is modulated by a state the structure does not itself
  compute.

---

## 8. Anterior cingulate cortex (Brodmann areas 24 and 32)

- **Function → structure.** Conflict and error monitoring, effort and outcome valuation, and
  motivation — the medial-wall control and salience node that signals when more control is needed.
  **Agranular-to-dysgranular cingulate cortex.** **Two divisional sub-elements are named and no edge
  uses either** — Brodmann areas 24 and 32. The midcingulate structure in file 17 uses the prime
  notation 24′ / 32′ for its own territory, which implies this structure holds the unprimed pair;
  the relationship between the two numberings is stated in neither and is owed at the source.
  **A cell-class sub-element is also present: von Economo (spindle) neurons**, a large projection cell
  type concentrated in this structure and in the insula. Whether it has its own targets — and so
  whether it is a sub-element an edge could terminate on — is not stated at the source.

- **Inputs.**
  - ← **the insula** (`17_insula_claustrum_habenula`) — the **salience signal**: *this event is
    behaviourally relevant now*. **Whether what leaves is a scalar, a pointer, or a switching command
    is not established at the producer**, and that non-establishment is stated there rather than
    glossed. Fan-in: to derive. **Two-ended and confirmed**, the producer marking it
    *salience → control*. **This end is the untyped one and takes the producer's type above.**
  - ← **the hippocampal formation**, from the **subiculum**, via the **fornix**
    (`08_medial_temporal_lobe`) — the **completed episode**; payload otherwise owed at both ends.
    Terminating in **layer III of Brodmann area 24a only**; **ipsilateral only**. **Two-ended.**
    ***The sub-element restriction is finer than this structure's own headings and it cannot
    currently receive it***: the Internal structure slot names Brodmann areas **24** and **32** as
    divisional sub-elements that no edge uses, and this edge terminates in **24a and not 24b or
    24c**. **Owed: divide Brodmann area 24, or record that this edge carries a sub-element claim the
    structure cannot yet receive.** **This is the second such demand in the file** — the
    ventrolateral structure has two on its own unmade division — and all three arrive from the same
    producer and the same study.
  - ← **the amygdala** (`08_medial_temporal_lobe`).
  - ← **the dorsolateral prefrontal cortex** (structure 5 above).
  - ← **the midline / intralaminar thalamus** (`12_thalamus`). **The producer does not declare its cortical
    target as a class covering this structure without naming it.** That entry declares
    `→ anterior cingulate cortex` **on its own line**, and marks the class beside it —
    `→ further cortex, diffusely, beyond the anterior cingulate` — explicitly as **the residue of the
    line the named edge came out of.** **The split is made there and this structure is the named
    member.** Payload owed at both ends.
    **A second thalamic edge reaches this structure and is not declared here.** That file's anterior
    nuclei entry declares `→ anterior cingulate cortex` and marks it *declared at one end only*,
    observing that this consumer names the midline / intralaminar thalamus and not that nucleus.
    **That mark is exact.** This line names one thalamic source and there are two.
    **Owed at the source: accept the anterior-nuclei limb here, or withdraw it there** — it is the
    cingulate half of the classical Papez target and it is unconfirmed at its consumer.
  - ← **the midcingulate cortex**, reciprocally, via the **cingulum**
    (`17_insula_claustrum_habenula`). **Two-ended and confirmed; payload owed at both
    ends**, and the producer names the same route. **The reciprocal pair with that structure is the
    only relationship in this entry that is complete at both ends in both directions** — the outgoing
    limb below is its partner.

- **Outputs.**
  - → **the dorsolateral prefrontal cortex** (structure 5 above), recruiting control.
  - → **the midcingulate cortex** (`17_insula_claustrum_habenula`) — a **scalar reward-value signal**:
    expected reward magnitude, and a response to the mismatch between expected and received reward,
    firing to unexpected reward and to expected-but-omitted reward. **Its coordinate frame is
    body-relative**, zero and slope set by bodily and motivational state. Fan-out: to derive.
    **Two-ended and confirmed.** The consumer carries this payload verbatim and records it
    as *the only edge in that section with a stated coordinate frame*. **The consumer also carries this
    end's caution — that the body-relative reading is Class 2, the source's own inference offered to be
    checked — so the two ends are copies and their agreement certifies transmission, not corroboration.**

  **Three outputs the far end declares and this entry does not, found and not written as
  edges.** `17_insula_claustrum_habenula` names this structure as the producer of an edge to **three
  of its six entries**, and this Outputs slot declares none of them:
  - **→ insula** — the far end's insula declares `← anterior cingulate cortex`, payload owed, and
    records that **the return arm of a relationship it calls reciprocal is unconfirmed at its
    producer.** This entry declares the inbound limb above and not this one.
  - **→ lateral habenula** — the far end types it a **bad-outcome expectation**, one of three cortical
    limbs of the value brake.
  - **→ posterior cingulate cortex** — payload owed at the far end.
  **All three are owed at the source, not written here from the far end's declaration.** **This is not three separate omissions but one shortfall**: this entry carries four
  outputs, and a structure that the adjacent file names as a producer three times over should not have
  a four-line Outputs slot. **The shortfall is invisible from inside this file, because every one of
  the three missing edges is a far end.**
  - → **premotor cortex and the supplementary motor areas** (structure 1 above).
  - → **autonomic centres.** **The far side of these centres — the visceral effectors they drive —
    is outside the map's scope, so this edge terminates at the scope boundary on its output side.**
    **It is nonetheless a Class endpoint on this side of the boundary**: the brainstem autonomic
    nuclei that would receive it have entries, and none was checked at the source. Naming them is a
    different question from the scope boundary and is owed.

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown. **This structure is not
  attributed to the ~640M budget** and should not be counted inside it without a decision: the budget
  is defined over granular frontal cortex anterior to the corpus callosum, and this cortex is
  agranular-to-dysgranular. Fan-in unknown on all six inputs. Basis: per hemisphere. Synapses, axons,
  volumes and myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, plus an open question about the cell-class sub-element, which is not a sheet axis and
  would not be one.
  - Laminar axis: **7, not 8** — layer 4 thin or absent, as this is agranular-to-dysgranular cortex.
    The source declines to assert the standard eight-layer block here and marks the laminar sets per
    sub-element as owed. **To derive per sub-element**, bounded at 7.
  - Tangential axes **H, W: to derive.** No pitch measured.

- **Edge latency.** **To derive** on all ten edges.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied — reciprocal with the dorsolateral prefrontal cortex, reciprocal
    with the midcingulate cortex via the cingulum, and closing the salience pair with the insula.
    **Not checkable for the autonomic-centres arm**, which is a class up to the scope boundary.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The control signal this structure sends the dorsolateral prefrontal
  cortex is **not a conflict signal carrying its own frame**. Human single-unit recording during an
  interference conflict task, analysed with a method that tested explicitly for a conflict-coding
  axis, did not find one; what the signal does instead is raise the gain on the already-framed coding
  of the correct sensorimotor response, so that under conflict the population activity shifts along
  the response-coding directions. **That absence was decoded rather than merely unmeasured**, which
  is a different and stronger state than "not yet known", and it is the sharpest such result in this
  file. The reward output has the opposite character: a scalar value axis, coding expected reward
  magnitude and the mismatch between expected and received reward, whose zero and slope are
  body-relative in the same way the orbital value axis is. **So this structure's outputs are
  characterised and the operation that produces them is not** — nothing at the source says where
  conflict is detected inside it, and the internal edges, including area 24 ↔ area 32, are unrecorded.
  *(The gain-on-a-framed-signal reading and the body-relative reading of the reward axis are the
  source's own inferences, marked there as offered to be checked.)*

---

## 9. Frontopolar cortex (Brodmann area 10)

- **Function → structure.** The most anterior and largest granular prefrontal area — metacognition,
  prospective memory, and cognitive branching, the management of multiple goals and subgoals. Widely
  regarded as the least-understood cortical area, and relatively neuron-rich in humans. **Two
  divisional sub-elements, defined by where the afferents come from**: the **lateral** part, whose
  afferents are more than 90% from other frontal areas, and the **medial / midline** part, which takes
  substantial temporal-lobe input including clear auditory connections. **The two parts therefore sit
  at different distances from the sensory periphery inside one structure**, and an edge terminating
  "on frontopolar cortex" is under-specified. Splitting is owed at the source, and unusually the basis
  for it is already quantitative.

- **Inputs.**
  - ← **other association / prefrontal cortex**, supramodal, onto the **lateral** part. **Class
    endpoint**, unresolved: **none of the four other prefrontal structures in this file declares an
    output here.** Owed at the source as cross-file edits within file 11, or withdraw.
  - ← **auditory association cortex** — the **anterior belt**, the **parabelt**, the **rostral
    superior temporal gyrus** and the **temporal pole** — directly and densely, onto the **medial**
    part (files 2 and 7). **The producer does not declare the temporal-pole limb**
    (`07_anterior_temporal_lobe`): that file's six outputs contain no frontopolar target, so this limb is declared here and at no producer.
    Owed at that section's source: declare it there, or withdraw it here. **The belt and parabelt limbs
    are confirmed** — see structure 2 and structure 6, and `02_auditory_pathway`'s belt entry declares
    the frontal pole among its direct prefrontal targets by name.
  - ← **other sensory modalities** — **parietal**, **inferior temporal** and **occipital** cortex —
    present but of lower density. **Class endpoint**, and a threefold one: each of the three names a
    lobe rather than a structure. **The parietal limb was checked at the source and no structure in
    file 4 or file 6 declares an output here.** Owed: repair at those files, or withdraw the limb.
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.**

- **Outputs.**
  - → **other frontal / prefrontal cortex**, from the structure as a whole; whether the signal leaves
    from one part is not stated. **Class endpoint**, unresolved: **none of the four other prefrontal
    structures in this file declares an input from here.** Owed at the source as cross-file edits
    within file 11.

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere**, and **this structure takes the largest share of it** — the
  source records Brodmann area 10 as the largest single prefrontal subdivision, and separately as
  relatively neuron-rich in humans. **That is an ordering constraint on the partition, not a count**:
  it says this structure's share exceeds every other prefrontal structure's, and it is the only
  partition constraint the file supplies. Fan-in unknown on all four inputs. Basis: per hemisphere.
  Synapses, axons, volumes and myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, so two arrays: medial and lateral.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular prefrontal
    isocortex.
  - Tangential axes **H, W: to derive.** No pitch measured. **The medial/lateral division is the one
    tangential boundary in this file with a quantitative basis** — the afferent-origin fractions above
    — and it is still not a pitch.
  - **A species caution attaches to the division and to the arrays it implies.** The pattern is very
    similar in Cebus and macaque despite more than 40 million years of separation, which is
    reassuring; but the **marmoset** differs, its labelled neurons extending ventrally into inferior
    temporal visual association cortex, which the other two do not show. **So a direct visual input to
    the frontal pole exists in at least one primate and not in others**, and which pattern the human
    follows is not established at the source.

- **Edge latency.** **To derive** on all five edges.

- **Invariant conformance.**
  - *Co-instantiation:* **not checkable, and this is the weakest case in the file.** Both of this
    structure's cortical arms — the supramodal input and the sole output — are classes that resolve
    nowhere, and the two structures that would close them are unnamed at both ends. The auditory arm
    reaches file 2, whose far end is unchecked, and the one limb that was checked, the temporal pole,
    does not declare it. Only the mediodorsal arm closes. All inherited; none repaired here.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The structure's premise in the literature — supramodal, with little
  direct sensory input — **is true of the lateral part and false of the medial part**, and the
  correction is quantitative rather than a hedge: retrograde tracer injections in lateral area 10 find
  more than 90% of afferents arising from other frontal areas, while injections on the midline surface
  receive substantial temporal-lobe projections including clear auditory ones. **Among all prefrontal
  areas this one has the densest interconnections with auditory association cortex**, spanning a large
  antero-posterior extent of the superior temporal gyrus from the temporal pole back to parabelt and
  belt; auditory pathways make up the largest single component of its extrinsic connections, and it is
  described as the main frontal auditory field. **So audition is not one sensory exception to a
  supramodal rule here; it is this structure's principal external connection**, and the other
  modalities are present at lower density rather than absent. That inverts the premise the heading
  carries, and it is the reason the medial/lateral split is a structural fact rather than a
  refinement. **The internal edge between the two parts is required and not recorded**: if the medial
  part receives the acoustic input and the lateral part is the frontally-connected one, the two must
  communicate for the input to bear on the output at all.
