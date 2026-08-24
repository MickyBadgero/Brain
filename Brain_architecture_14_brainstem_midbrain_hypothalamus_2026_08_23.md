# Brain architecture — 14 brainstem midbrain hypothalamus

**Date:** 2026-08-23
**Derived from:** `human_brain_14_brainstem_midbrain_hypothalamus_2026_07_24.md` — ten structures of
the subcortical core. **One source file, and no other content source.**

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed.

- `01_visual_pathway`.
- `02_auditory_pathway`, `15_cranial_nerve_nuclei`. **Nine shared edges diffed and
  stemmed. Four two-ended; and **the relay this file records as having no entry anywhere found to be
  described in `15_cranial_nerve_nuclei`**, inside a bundled entry under a heading that does not name
  it — the second such case found today.**
- `03_other_senses`, `16_spinal_cord`. **Eleven shared edges diffed and stemmed.
  Eight two-ended with this file's spinal edges confirmed at both ends; one cross-file check the cord
  file asked for run and closed as a negative — this file's reticular formation declares no locomotor
  start/speed payload on its spinal edge; both structures this file records as having no entry
  anywhere confirmed absent from the other side; and **the thalamic relay this file twice records as
  missing found to exist, as a bundled stage inside `03_other_senses`'s gustatory entry**.**
- `04_dorsal_visual_parietal_stream`, `11_frontal_lobe`. **Six shared edges diffed
  and stemmed; four two-ended with the sub-element agreeing at both ends on three of them, one
  consumer-only edge confirmed absent here, and this file found to be the third of three declaring a
  route through a thalamic relay that the named nucleus does not carry.**
- `12_thalamus`, `13_neuromodulatory_systems`. **Thirteen shared edges diffed and
  stemmed; six two-ended, one two-ended claim in this file corrected to a class-with-a-member, one
  class closed as a negative against `12_thalamus`, and one endpoint of this file's found to name a
  thalamic structure that has no entry there.**
- `08_medial_temporal_lobe`. **Eleven shared edges diffed; seven two-ended, four
  edges confirmed to have no producer end here, two stale marks discharged at the far end, and two
  structures found to be crossing between the files without an edge — one hidden inside this file's
  *extended amygdala* class endpoint, one inside its hypothalamus bundle.**
- `09_basal_ganglia`. **Six shared endpoints diffed. This file's rostromedial tegmental nucleus is
  the inverting relay that section's pallidohabenular loop runs through, and it is typed here as
  precisely that stage — the GABAergic relay converting the habenula's glutamatergic bad-outcome
  signal into inhibition of dopamine.** **Two class endpoints of that file check as negatives here:
  no entry declares an input from the basal ganglia as a class, so *the brainstem* and *reticular and
  extrapyramidal motor systems* have no far end here and are owed a named target or a withdrawal
  there.** **And one named edge is written at neither end there**: this file's rostromedial tegmental
  entry declares `← substantia nigra` as a lesser input with the payload owed, and that far end
  declares no matching output.
- `10_cerebellum`. **One shared edge diffed — the fastigial limb into the reticular formation,
  two-ended, and the far end types the payload this end marks owed. Three findings land here, and
  all three are owed at this file rather than at that one: this entry names its producer
  *cerebellum*, which matches no entry heading there; the pontine nuclei and the red nucleus are
  listed in the front matter below as named on this section's edges and are named on none of them,
  being named on five of that file's; and the inferior olive, which is medullary tissue, has its
  entry there.** *(This line carries no date, per the current convention; the dated lines above
  predate it and their retrofit is Micky's.)*

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** The number
fixes data-flow position and the section names the structure; either alone is ambiguous, and a bare
number goes silently wrong the moment a file is split or renumbered. Stems below are written only
where the far file has been read against this one; an endpoint with no stem is one whose far end has
not yet been opened beside this file, and it is not a claim that none exists.

**Counting basis follows the source's own convention for this section:** paired nuclei **per side**,
midline structures **whole (both sides)**, each tagged. The convention is almost inert here, because
nine of the ten structures have no count to attach a basis to.

**Nine of ten structures cannot be sized, and that is this file's principal result.** The one neuron
count in the section belongs to a **sub-element of one entry** — the suprachiasmatic nucleus at
~50,000 per side. Every other structure reads *soft*, *unknown*, or *none*. File 01 could size six of
eight structures; file 13 could size all four in part; **this file can size one sub-element of one
entry.** The oldest part of the brain is the part the architecture can say least about, and the
reason is stated at the source and is structural rather than accidental: these are small,
ill-bordered, or many-nucleus structures, several of them defined by connectivity and transmitter
rather than by a countable border.

**Eighty edges. Seven of them are not projections**, which is the largest concentration of
non-projection edges anywhere in the map: two chemical inputs sensed directly from blood, three
hormonal outputs, one hormonal edge that has a receptor-bearing consumer and is therefore a real
edge, and one input arriving from a peripheral ganglion that lies outside the scope boundary.

*A transcription cross-check, run mechanically and closed.* The source's header states **80 edge
lines — 39 in, 41 out**, and the edge table of `Brain_14_brainstem_midbrain_hypothalamus.py`
counts **39 in, 41 out, 80 total** — the source's figures exactly.

**An earlier pass of this file reported 40 in, and that figure was wrong.** It counted the lateral
parabrachial entry's **collateral bullet** as an edge. That bullet names **no producer**: it records
that a large fraction of ascending fibres reaching other targets send axon collaterals to this
nucleus, which is a qualification on the **arity of the whole ascending nociceptive system** and not
an edge with two ends. It is carried in the module as a named note rather than dropped.

**Two things had to be right for the count to close, and both are worth stating because either one
alone gives a different number.** An edge with both ends inside this section is written **twice** in
the source, once under the producer's Outputs and once under the consumer's Inputs — so *in* and
*out* are positions in a document, not properties of an edge, and seventeen edges here appear twice.
And a bullet naming no producer is not an edge. **The one-line drift was real and is the reason the
check is worth running rather than reasoning about.**

**Six structures are named on this section's edges and have no entry anywhere:** the **rostral
ventromedial medulla** (the relay of the descending analgesic gate, named at the periaqueductal grey
here and at the spinal cord in file 16); the **lateral septum**; the **posterior** and **anterior
pituitary** (endocrine release sites, recorded as terminals rather than regions); and the **superior
cervical ganglion** (peripheral, outside the scope boundary by rule).
All are inherited from the source, which marks each; §2 forbids repairing any of them here.

**Two further structures belong to this section anatomically, have no entry anywhere, and are named
on no edge in this file:** the **pontine nuclei** and the **red nucleus**. **They are named on five
edges in `10_cerebellum`** — the mossy-fibre input to the cerebellar cortex, the mossy limb of the
deep nuclei's collateral input, both of the deep nuclei's rubral outputs, and the descending limb of
the dentato-rubro-olivary loop — **and on none here, as an endpoint or as a route.** The correction
matters because it aims the repair: a reader deciding what a pontine-nuclei entry must satisfy needs
the edges, and the edges are all in that file. **This was introduced in derivation and not inherited**
— the source carries the same correction in its own preamble, states that **naming a region on an edge
is not describing it**, and attributes these edges to the cerebellum file. **Owed as new entries
belonging jointly to this section and the cerebellum**, with the source recording the open decision as
**which file physically carries each**; the loop they sit in is the invariants section's
cerebro-cerebellar case below.

**The noradrenaline convention set at file 13 applies and is not re-derived.** This section's C1
adrenergic cell group, its A1 noradrenergic cells, and its locus coeruleus and raphe endpoints all
use it; the pineal's sympathetic input carries the transmitter as **noradrenaline (norepinephrine)**,
the synonym given once.

---

## Structural invariants

**Whole-pathway co-instantiation.** All ten structures exist and are active from the outset. Two
observations specific to this section, and they pull in opposite directions.

The first is that **this file closes loops that were open elsewhere**. The mammillary bodies to the
anterior thalamic nuclei — the Papez return arm — is two-ended here and at file 12. The habenular
brake reaches dopamine through the rostromedial tegmental nucleus, whose entry exists here and whose
two outputs are two-ended against files 9 and 13; that closes a limb that four files had been
pointing at. The circadian loop's stations are here.

The second is that **two loops still cannot be closed, and this file is where the missing stages
belong.** The cerebro-cerebellar loop runs through the pontine nuclei and the red nucleus; both are
anatomically in this section, neither has an entry, and the source records that they are owed and
that the corticopontine stage *transforms* rather than relays — a computing stage inside a closed
loop with no slot. **Co-instantiation therefore cannot be satisfied for that loop at this rung**, and
the repair is the source's.

**And the split that puts those two stages in no file puts a third structure in an unexpected one.**
The **inferior olive** is medullary tissue and **its entry is in `10_cerebellum`**, whose other two
entries are the cerebellar cortex and the deep cerebellar nuclei. **It appears nowhere in this file**,
as an entry or as a sub-element, and an endpoint here addressed to it is **mis-addressed rather than
dangling** — `16_spinal_cord` records having made and corrected exactly that error. **So the source's
data-flow split produces both cases at this boundary**: a structure in no file in one direction, a
structure in the unexpected file in the other. **The difference is that the olive has a heading**, so
any check that reads headings finds it, which is not true of the other two. **Recorded so a search of
this file does not report it missing.** *(That the three cases are one consequence of the split is
Claude's reading; the split is Class 1 from the source.)*
**A name hazard travels with it:** this file's *superior olivary complex* reference belongs to
`02_auditory_pathway` and its *olivary pretectal nucleus* to `15_cranial_nerve_nuclei`, and neither is
the inferior olive — the same exposure this file records for the rostral ventrolateral and
ventromedial medulla, arriving from outside.

**The circadian loop turns out to be less outside the boundary than it was recorded as being.** The
design file treats it as closed in the body and outside scope by rule, on the ground that its closing
limb is melatonin in the bloodstream and one of its forward joints is a peripheral ganglion. This
file's pineal entry types that closing limb as **melatonin acting on receptors at the suprachiasmatic
nucleus** — a hormonal action on a receptor-bearing target inside the map, declared at both ends. So
the closing limb has a named consumer in scope, and **only the superior cervical ganglion joint is
outside.** The loop is not wholly outside the boundary; it has one joint outside. *(Both statements
are Class 1 from the source. That they refine the design file's reading of the loop is Claude's.)*

**Per-edge latency.** Every edge carries a nonzero, finite, heterogeneous latency in real time units,
and **this section can name none of them: every latency reads *to derive*.** No conduction time and
no synaptic delay appears anywhere in file 14.

**But this is the section where the enormous spread is visible without any figure at all.** One
structure's outputs span the whole range on their own: the hypothalamus drives autonomic
preganglionic neurons through the periaqueductal grey and the spinal cord on ordinary projections,
and it drives the anterior pituitary through **portal blood**, whose transit and hormone action are
minutes to hours; the circadian loop it sits in closes over **twenty-four hours**. Three regimes on
one entry's Outputs field. The design file's per-edge-latency invariant is argued from exactly this,
and here it is not an argument but a list.

**Four non-projection edge classes appear, and one of them is new to the enumeration.**

1. **Chemical sensing from blood.** The nucleus of the solitary tract senses glucose, leptin and
   angiotensin II directly; the hypothalamus senses leptin, ghrelin, glucose, osmolality and
   temperature at the circumventricular organs where the blood–brain barrier is open. **Fan-in is
   not applicable** because there is no producer region and the transfer is diffusion.
2. **Hormonal output into blood.** The posterior pituitary arm (oxytocin and vasopressin from
   magnocellular axons), the anterior pituitary arm (releasing and inhibiting hormones through the
   hypophyseal portal circulation), and the pineal's melatonin into the general circulation.
3. **A hormonal edge with a receptor-bearing consumer** — the pineal's melatonin feedback onto the
   suprachiasmatic nucleus. This is a real edge with two ends, and it is what distinguishes case 3
   from case 2: the same substance in the same bloodstream, but one arm terminates on a named
   consumer and the other does not.
4. **An edge with no consumer at all** — melatonin into the general circulation and cerebrospinal
   fluid. It has a producer, a payload and a real physical effect, and **no target region**, because
   its targets are brain-wide and peripheral. The design file has no shape for an edge that
   terminates in the body rather than at a structure. **Recorded, not resolved.** *(That this is a
   distinct case rather than an untyped one is Claude's reading; the source's treatment of it as an
   endocrine terminal is Class 1.)*

**There is no global clock, and this section contains the slowest oscillator in the map.** The
circadian loop has a twenty-four-hour period and a named master clock in the suprachiasmatic
nucleus. **It is a biological oscillator inside the system, not a clock for the system**, exactly as
the theta rhythm in file 13 is not. The same guard applies with more force here, because a
twenty-four-hour period is the sort of number that invites being treated as a frame boundary. It
paces the circadian loop and nothing else.

**And one structure generates activity with no input at all.** The rostral ventrolateral medulla's
presympathetic neurons show **intrinsic pacemaker activity** in slice: the sympathetic tone it
supplies is *generated*, not relayed, and the inhibition arriving from the caudal ventrolateral
medulla acts on a drive that exists without input.

**What this does and does not cost the sizing model, stated carefully.** A *stateless* threshold gate
with no feedback path cannot fire at zero input, and that much is true of the forward operation as
written. **It is not true of a threshold gate inside this architecture**, because the per-edge-latency
invariant already puts a nonzero delay on every edge and the map is full of loops: a threshold element
in a delayed feedback path is a **relaxation oscillator**, the same construction a Schmitt trigger
with a resistor–capacitor feedback path is, and a ring of an odd number of inverting stages
oscillates for the same
reason. **Free-running activity is therefore available to the model as a property of connectivity plus
delay, and is not a missing operation.**

**What it does need is a sign.** `count[j] = Σ active_source[i]` has no inverting term, and every
construction above requires one. That gap is already on the books — the design file records it from
the outer retina, where hyperpolarisation is the excitatory response — and **this section records it
again in a place where it is much easier to see**: the caudal ventrolateral medulla's output is
explicitly sign-inverting, excitation there becoming suppression here. **So this is a further
consequence of the sign gap, not a second independent finding against the model**, and it is recorded
as the smaller thing it is.

**What the source does not settle, and it decides which of the two readings applies.** The recordings
are from tissue slices and the activity is called *intrinsic*, but the source does not say whether
synaptic transmission was blocked. If the pacemaking is cell-intrinsic — pacemaker conductances in
the membrane — it is a property of the element and needs an element-level mechanism. If it survives
in slice because local recurrence survives with it, it is a property of the circuit and falls out of
connectivity and delay with no new mechanism at all. **Owed, and it is a question about the biology
rather than about the model.** *(The pacemaker physiology is Class 1 from the source. The oscillator
constructions and the reading that this reduces to the sign gap are Claude's.)*

---

## Superior colliculus

- **Function → structure.** The layered midbrain hub for **orienting gaze and attention**, in two
  functional tiers over **seven laminae** — stratum zonale, stratum griseum superficiale, stratum
  opticum, stratum griseum intermediale, stratum album intermediale, stratum griseum profundum,
  stratum album profundum, alternating grey and fibre. **These are not cortical layers and nothing
  here reads against the six-layer scheme**: the colliculus is tectum and its laminae are a different
  object sharing the word. Superficial layers carry a retinotopic **visual** map; intermediate and
  deep layers carry **auditory and somatosensory maps spatially aligned with it** and a **motor map**
  of saccade vectors aligned with all three. **Alignment is the structure** — a location in the
  tissue means the same direction in the world at every depth. The **rostral pole is functionally
  distinct**, a fixation zone whose cells fire continuously during fixation. Functionally the whole is
  a retinotopic **priority / salience map** whose active locus specifies the next gaze target.
- **Inputs.**
  - **← retina** (`01_visual_pathway`) **→ stratum griseum superficiale** (the retinotectal
    projection) — retinotopic luminance transients for orienting; payload otherwise **owed and
    contested** (below). Not more than 10% of ganglion cells, ~6% near the fovea, and **largely a
    branch of axons that also reach the lateral geniculate nucleus** rather than a separate population.
    Terminates in the **upper** superficial grey and is segregated by eye into alternating columns and
    strata though cells here are binocular. Fan-in: to derive.
    **Checked against the producer on 2026-07-29, and the two ends are asymmetric in three ways.**
    The producer declares the edge and the ganglion-cell fraction and **types no payload at all**, so
    the *contested* state recorded here exists at this end only — **the producer's retina entry gives no
    hint that the edge's content is disputed.** The producer names *superficial layers*, one level
    coarser than the *stratum griseum superficiale* named here. And the producer does **not** carry the
    branching fact, which is the one with a build consequence: it lists the chiasmal and collicular
    outputs as separate bullets with separate percentages, **so its ~80% image-forming figure and its
    ≤10% collicular figure are not additive if the collicular axons are largely branches of the
    geniculate-bound ones.** **Owed at the producer: the contest, the lamina, and whether its retinal
    output percentages partition the ganglion-cell population or overlap it.**
  - **← V1** (`01_visual_pathway`)**, from 5b → the superficial layers** — retinotopic salience for
    orienting; payload otherwise **owed**. Fan-in: to derive. **Two-ended and confirmed on
    2026-07-29: the producer declares `→ superior colliculus, from 5b — retinotopic salience for
    orienting`, in the same words.** This end adds the termination layer, which the producer does not
    name. **And this edge is the one the contest below turns on** — if the colliculus's visual drive
    arrives through the geniculate and V1 rather than from the retina directly, then this edge, and not
    the retinotectal one, is carrying the visual payload into the superficial layers.
  - **← extrastriate and parietal cortex, specifically the ventral lateral intraparietal area → the
    intermediate layers** (`04_dorsal_visual_parietal_stream`) — the **priority (salience)
    map**: one scalar per retinotopic location ranking it by behavioural priority, **modality-free**.
    The ventral subdivision projects strongly to the deep layers here and the dorsal does not. Fan-in:
    to derive. **Two-ended and confirmed 2026-08-14, and the sub-element agrees at both ends**: that
    entry declares the output **from the ventral subdivision onto the intermediate and deep layers**
    and warns that **the ventral subdivision carries this edge and the dorsal one does not**, so a
    consumer reading *the lateral intraparietal area projects to the colliculus* is reading half the
    area. **This entry does not read it that way.** **Both ends type the payload the same way — one
    scalar per retinotopic location, modality-free — and both owe the fan term.** **The extrastriate
    remainder of this line is still a class** and was not resolved in this pass.
  - **← frontal eye field → the intermediate layers** (`11_frontal_lobe`) — a **saccade goal**,
    the cortically selected target location in eye-centred coordinates; payload otherwise **owed**.
    Fan-in: to derive. **Two-ended, discharged on 2026-07-29 and re-confirmed 2026-08-14**; that end
    is untyped and carries no termination layer, so **both the payload and the lamination exist only
    here.**
  - **← inferior colliculus** — auditory **azimuth and elevation**, azimuth from interaural cues in
    the superior olivary complex and elevation from the dorsal cochlear nucleus's spectral notches, in
    a frame this structure's map can register against the visual one. **Not a map: the map is built
    here, not relayed into it** — and a topographic auditory space map does exist in the mammalian
    superior colliculus, the only mammalian subcortical structure in which one has been found.
    Fan-in: to derive.
  - **← somatosensory afferents** — body-surface location of touch, somatotopic; payload otherwise
    **owed**. Fan-in: to derive.
  - **← olivary pretectal nucleus → stratum griseum intermediale** — payload **owed**: a luminance
    scalar arriving in the **premotor rather than the visual** layers, by a route that is not the
    retinotectal one. Fan-in: to derive.
    **Both ends of the missing stage are declared. The producer's** retina entry
    (`01_visual_pathway`) declares `→ olivary pretectal nucleus — from broad-field
    melanopsin-containing luminance detectors`, and this entry declares the nucleus's output into the
    intermediate layers. **So a two-hop route retina → olivary pretectal nucleus → superior colliculus
    is declared at its origin and at its destination** — and the relay is where the transform would
    live, since a broad-field luminance detector's output arriving as a scalar in premotor layers is
    not the same object that left the retina.
    **The claim that the relay has no entry anywhere is wrong and is withdrawn, checked 2026-08-14.**
    **The olivary pretectal nucleus is described in `15_cranial_nerve_nuclei`**, inside its *pretectum
    and gaze-integrator tegmental cell groups* entry, **and the description is exactly the transform
    this line says is missing**: a spatially resolved retinal signal arrives on broad-field
    melanopsin-containing ganglion cells, the projection cells are tonic on-centre luminance neurons
    with receptive fields averaging about **31°**, their somata form a shell around a neuropil core
    where the retinal terminals concentrate, and **a single number leaves.** That entry also declares
    this edge outward — `→ intermediate grey layer of the superior colliculus` — **so the limb is
    two-ended and was two-ended all along.**
    **Why it read as missing.** It is one of **two structures inside one bundled entry named for
    neither of them**, in a file whose subject is cranial-nerve nuclei — **so the structure has a full
    description, no heading, and lives in the file no one would search.** That entry records the
    bundle's split as owed and notes that its two structures share no edge with each other.
    **This is the second instance found today**, after the thalamic relay this file twice recorded as
    absent, which is a bundled stage in `03_other_senses`. **Both were reported missing on the same
    evidence — a search for a structure name returning nothing — and in both the structure was
    described below a heading.** **A structure without a heading is invisible to every check this rung
    has**, and that is a finding about the checks rather than about either file.
    **Owed at the source: give the olivary pretectal nucleus an entry**, which the far file's own text
    already argues for, **or record here that the relay is described there.** Not repaired at this
    rung.
  - **← substantia nigra pars reticulata** — **tonic inhibition and its release, no content
    whatever.** The saccade is not commanded by this edge, it is **permitted** by a pause in the tonic
    firing, so what is on the wire is a gate and **its informative event is a cessation**. Fan-in: to
    derive.
- **Outputs.**
  - **→ the brainstem saccade burst generators**, from the intermediate and deep layers — the
    **paramedian pontine reticular formation** (horizontal) and the **rostral interstitial nucleus of
    the medial longitudinal fasciculus** (vertical) — a **saccade displacement vector as a place
    code**. The vector is specified by *where* the active population sits: amplitude rostral-to-caudal,
    direction medial-to-lateral, a two-dimensional activity hill whose locus is the message. **The
    payload change here is spatial-to-temporal** — a location on a map in, a timed burst out. **This
    is the one place in the visual line where a payload is a position in tissue rather than a value on
    a line**, and a consumer reading firing rate alone would recover nothing. Fan-out: to derive.
    **Contested and carried:** whether the *rate* on top of the place code is itself payload is
    disputed — one line reads saccade kinematics out of a rostral-to-caudal gradient of peak rate and
    burst duration, another reports the motor burst does not dictate kinematics. The place code is not
    in dispute; what the rate adds to it is.
  - **→ cervical spinal cord**, via the **tectospinal tract**, from the deep layers — a head and body
    orienting command in the same map's coordinates; payload otherwise **owed**. Fan-out: to derive.
  - **→ pulvinar** (`12_thalamus`) **and other thalamus → cortex**, from the intermediate and deep
    layers — payload **owed**. The colliculo-pulvinar-cortical route running parallel to the
    geniculostriate one, and a **candidate** carrier for residual vision after V1 damage. Fan-out: to
    derive. **The pulvinar limb is two-ended and confirmed 2026-08-14**, and **both ends name the
    intermediate and deep layers** — that entry writes the input as subdivision-specific and from those
    layers, so the attribution agrees on both sides. **The *other thalamus* remainder is a class** and
    stays one: no further entry in that section declares a collicular input.
  - **→ V3** (`01_visual_pathway`) **and the middle temporal area**
    (`04_dorsal_visual_parietal_stream`)**, di-synaptically via the pulvinar** (`12_thalamus`) —
    payload **owed**; the relay reaches those two areas **selectively**. Fan-out: to derive.
    **Two-ended against the V3 end and checked on 2026-07-29**, which declares `← superior colliculus,
    di-synaptically — a subcortical route into the motion areas`. **One edge crossing four files**, and
    the intermediate stage is a structure with its own entry elsewhere rather than a bundle
    sub-element — so this is a two-hop route written as one edge at both ends, and neither end names
    the relay's payload.
  - **→ frontal eye field and lateral intraparietal area** (`11_frontal_lobe`,
    `04_dorsal_visual_parietal_stream`), reciprocally via the thalamus — **corollary discharge of
    the saccade command**: *the eye is about to move, by this vector*. Its usefulness **depends on
    arriving before the movement**, which is a latency requirement stated without a latency. Fan-out:
    to derive.
    **Checked 2026-08-14, and this is the third of three files declaring this route while the relay
    on it declares only its first leg.** The parietal end declares
    `← frontal eye field — corollary discharge of the saccade command, relayed from the superior
    colliculus through the thalamus` **in this line's own words**, and marks that **the thalamic relay
    is still unnamed and the thalamus file does not supply it.** The frontal end declares
    `→ the lateral intraparietal area, carrying the corollary discharge` and **names the relay as the
    mediodorsal thalamus.** **`12_thalamus`'s mediodorsal entry names the frontal eye fields among
    its five cortical outputs and declares no intraparietal target of any kind.**
    **So the first leg is two-ended and named, and the second leg is declared by three files and by
    no nucleus.** **The latency requirement this line states without a latency sits on the leg that
    does not exist**, which is why it could not be given one. Owed at the source, in `12_thalamus`:
    state whether the corollary discharge leaves that nucleus for parietal cortex, or name a
    different relay.
- **Sizing.** Basis: **per side.** **Soft, and there is no clean human total** — the structure has
  historically been counted only in single midbrain sections, never as an unbiased whole-structure
  stereological figure. Layered like cortex but with subcortical packing. Fan-in unknown on every
  edge, so the width is the 16-bit bound and **the store is to derive for want of a count, not for
  want of a width.**
- **Shape.** **Sheet**, and the interesting part is that **one H × W serves every lamina**: rank 3,
  **(lamina, H, W)** with seven laminae, and the visual, auditory, somatosensory and motor maps in
  register across depth. Registration is not a convenience here, it is the structural claim — the
  tangential axes are shared, which is what makes "see it, look at it" a local operation. Extents **to
  derive**: no pitch and no surface area is recorded.
  **A cell-class axis exists and does not partition spatially, which the shape cannot express.** The
  intermediate layers hold **burst** neurons (locked to saccade execution) and **buildup** neurons
  (firing continuously from target onset until the saccade begins) — **two payloads on one map, not
  separated spatially.** What it would mean for an edge to terminate on the buildup cells and not the
  burst cells is recorded as owed at the source. A rank-4 shape **(lamina, cell class, H, W)** would
  assert a separation the tissue does not have; leaving it out drops a real distinction. **Recorded
  as an open shape question, not resolved.**
- **Edge latency.** All thirteen edges **to derive**, and one of them carries a stated ordering
  requirement with no number: the corollary discharge must arrive **before** the movement it
  predicts.
- **Invariant conformance.** Co-instantiation: satisfied for the joints present here; the gaze loop
  through the frontal eye field and lateral intraparietal area closes outside this file, and the
  saccade burst generators are sub-elements of the reticular formation entry below, so that one
  closes **within** the file. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The output payload is **a position in tissue**, and that is a
  structural claim with a build consequence: the receiving stage must read *where* the active
  population is, not how hard it fires, so an implementation that carries only activity levels per
  line loses the message entirely. The input from the substantia nigra pars reticulata is the mirror
  case — a wire whose informative event is a **stop**, which an implementation reading presence of
  activity as signal would read exactly backwards.
  **And the entry contains a result that contradicts its own Function field, carried unsmoothed.**
  Reversibly inactivating the lateral geniculate nucleus in awake macaque abolished visually evoked
  spiking here — a 98% mean reduction, significant in 115 of 115 neurons — while leaving
  saccade-related bursts unchanged, with the loss extending into the retinorecipient superficial
  layers themselves and the retinotectal axons confirmed structurally intact. The reading drawn is
  that the visual drive arrives **through the geniculate and V1** rather than from the retina
  directly. It is a preprint, in two animals, acute and passive-viewing, and it runs against an
  earlier anaesthetised result. **The architectural consequence is specific and is carried: the
  retina → superior colliculus edge's payload is *contested*, not merely *owed*** — the state the
  design file records as being in use and unnamed — and the "subcortical arm of vision" is a claim
  about the chronically lesioned brain rather than the intact one.

## Lateral parabrachial nucleus

- **Function → structure.** The pontine relay carrying body-state and nociceptive signals to
  **limbic** targets rather than to sensory cortex. It is the destination of the great majority of
  the spinal cord's superficial-dorsal-horn output, and its projection to the central nucleus of the
  amygdala is held to carry the **affective** dimension of pain — the unpleasantness, as distinct
  from the location and intensity the thalamocortical line carries. Sub-elements with separately
  described output: the **subparabrachial nucleus (Kölliker–Fuse)** and the **lateral crescent**,
  both projecting to the solitary nucleus, the ventrolateral medulla and the spinal cord onto
  respiratory and autonomic cell groups. **No internal edge between subnuclei is typed.**
- **Inputs.**
  - **← spinal cord grey matter, lamina I**, and **← the caudal spinal trigeminal nucleus** — the
    nociceptive, thermoreceptive and pruritic payload typed at the spinal entry. **The dominant
    destination of that output**, with the proportion disputed in detail and agreed in kind: ~85% of
    rat lumbar lamina-I projection cells labelled from here or the caudal ventrolateral medulla in one
    quantitative study, ~95% of ascending lamina-I neurons targeting this nucleus in a review of the
    same literature. Fan-in: to derive.
  - **A structural qualification that changes the arity of the whole ascending system.** A large
    fraction of the ascending fibres reaching *other* targets send **axon collaterals** here, so this
    nucleus receives what has been described as a **carbon copy** of most nociceptive information the
    cord sends anywhere. **An architecture that treats the spinothalamic and spinoparabrachial lines
    as independent channels would double-count the source population.** *(The double-counting
    consequence is marked at the source as Claude's reading; the collateral anatomy is Class 1.)*
  - **← nucleus of the solitary tract** — visceral and gustatory; payload **owed**. Fan-in: to derive.
    Two-ended within this file.
  - **Two forebrain inputs are declared at their producers and not here. Checked 2026-08-13.**
    `08_medial_temporal_lobe` declares `→ lateral parabrachial nucleus` at **both** its amygdala entry
    and its bed-nucleus entry, and records both as undeclared at this end. **They are: this entry
    declares three inputs and no forebrain source of any kind.** **The amygdalar one is the return
    limb of this entry's own affective-pain output**, so a reciprocal pair is declared at one end
    only. **Owed at `human_brain_14_...`: write both limbs, or state that the descending projection
    does not exist.**
- **Outputs.**
  - **→ amygdala, central nucleus** (`08_medial_temporal_lobe`) — the affective nociceptive payload,
    monosynaptic and excitatory with feed-forward inhibition in the target. **Payload beyond "aversive
    value" is owed, and the source records that the completion test is not passed:** *unpleasantness*
    is a phrase, not a type with a range and a frame. Fan-out: to derive. **Two-ended and confirmed
    2026-08-13**, the consumer naming the same sub-element, carrying the same payload and the same
    contest, and marking the payload owed at both ends.
  - **→ bed nucleus of the stria terminalis** (`08_medial_temporal_lobe`) — payload **owed**. Fan-out:
    to derive. **Two-ended and confirmed 2026-08-13.**
    **These two lines are the same nucleus supplying both arms of the extended amygdala, and only one
    of them is typed.** The consumer records the consequence this end does not: the phasic and
    sustained arms **share a producer**, so whatever distinguishes them — duration, cue-binding — **is
    not a difference in this source.** **Owed here: type the second line, or state that the two arms
    receive the same signal and differ downstream.**
  - **→ hypothalamus** — lateral, ventromedial, dorsomedial and arcuate nuclei, and median and
    lateral preoptic — body-state signals driving autonomic and ingestive responses; payload
    otherwise **owed**. Fan-out: to derive. **This edge names five sub-nuclei of an entry that is
    itself a bundle** — see the hypothalamus entry.
  - **→ intralaminar nuclei** (`12_thalamus`) **and the ventroposterior parvicellular thalamus** —
    payload **owed**. Fan-out: to derive. **The intralaminar limb is two-ended and confirmed
    2026-08-14**, payload owed at both ends. **The second limb names a thalamic structure that has no
    entry in `12_thalamus` under any name**, and this file names it a second time — the gustatory
    pathway line below routes through the parvicellular ventral posteromedial thalamus to insular
    cortex. **So a thalamic relay this file depends on twice is absent from the thalamus section's
    eight entries.** **Splitting this line is owed**, and the far end has recorded the missing entry
    from its side.
    **The relay is not missing from the architecture, found 2026-08-14. It is described in
    `03_other_senses`**, inside that file's **gustatory pathway** entry, which names it the **ventral
    posteromedial parvocellular thalamic nucleus**, carries it as one of three bundled stages, and
    gives it a row of its own in that file's section totals. **The claim that it has no entry in
    `12_thalamus` stands; the inference that it has no entry anywhere does not, and is withdrawn.**
    **Two things hid it.** The name differs in word order and in one vowel — *ventroposterior
    parvicellular* here, *ventral posteromedial parvocellular* there — **and it is a stage inside a
    bundled entry rather than a heading**, so it is invisible to a search for structure names from
    either direction. **Owed at the source, and it is a decision: give the nucleus an entry in
    `12_thalamus`, or record there that it is described in `03_other_senses`.** **Not moved here.**
  - **→ insula and infralimbic cortex** — payload **owed**. Fan-out: to derive.
  - **→ basal forebrain / nucleus basalis of Meynert** (`13_neuromodulatory_systems`), to the
    substantia innominata — payload **owed**. Fan-out: to derive. **This line read *two-ended against
    file 13, whose basal forebrain entry declares a brainstem input*, and that is too strong. Corrected
    2026-08-14.** That entry's input is `← brainstem`, **marked there as a class endpoint with no named
    member**, and it covers this producer without naming it. **A class that covers a producer is not a
    two-ended edge**, and the far file keeps the two states apart carefully elsewhere. **What is true
    is the narrower claim**: this structure is a **located named member** of that class, and naming it
    there is owed at the source. **The correction is recorded at both ends.**
- **Sizing.** Basis: **per side.** **No count — unknown**, no human figure found. Every fan-in and
  fan-out unknown. **Zero derivable parameter memory, and it is a gap and not a zero:** unlike a
  tract or a transducer, this structure has neurons and computes.
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-element, N)**, sub-elements the
  subparabrachial nucleus, the lateral crescent, and the remaining unnamed subnuclei. **N to derive**
  and the sub-element list itself incomplete — the source says "several subnuclei are distinguished"
  and names two. No map axis is recorded.
- **Edge latency.** All eight edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; the solitary-nucleus input closes within
  this file, the amygdalar and basal-forebrain outputs close in files 8 and 13. Per-edge latency:
  satisfied, all to derive.
- **Justification (biological).** **Contested and carried:** one report holds that this nucleus
  channels spinal nociceptive signals to the intralaminar thalamic nuclei **but not** to the
  amygdala, against the mainstream spino-parabrachio-amygdaloid account the edges above record. The
  edges are kept because human tractography and rodent circuit mapping both support them, and the
  dispute is recorded rather than resolved. The human evidence is recent: the trigeminal nerve →
  lateral parabrachial → central amygdala circuit was delineated in vivo in humans for the first time
  by diffusion tractography, with the right-side circuit stronger in males than females — **an
  asymmetry recorded on a structure counted per side.**

## Caudal ventrolateral medulla

- **Function → structure.** **Two functions in one territory, described by two literatures that
  rarely cite each other, and the source records the doubling as itself the finding.** In
  cardiovascular physiology it is the **inhibitory link of the arterial baroreflex**: glutamatergic
  drive from the solitary nucleus excites **GABAergic** (γ-aminobutyric acid, GABA) neurons here,
  which
  tonically inhibit the presympathetic neurons of the rostral ventrolateral medulla, and that
  inhibition is what converts a rise in arterial pressure into withdrawal of sympathetic vasomotor
  drive. In pain anatomy the same region is **one of the two dominant supraspinal targets of lamina
  I**. **Whether the lamina-I input and the baroreflex neurons are the same cells is not
  established** — which is a question about whether this is one structure or two sharing a location.
- **Inputs.**
  - **← spinal cord grey matter, lamina I** — the nociceptive and thermoreceptive payload typed at
    the spinal entry. Fan-in: to derive.
  - **← nucleus of the solitary tract**, carrying arterial baroreceptor afferents — **arterial
    pressure**, as a tonic excitatory (likely glutamatergic) drive **proportional to baroreceptor
    firing**. Fan-in: to derive. Two-ended within this file.
- **Outputs.**
  - **→ rostral ventrolateral medulla**, presympathetic neurons — **inhibition, and it is tonic, not
    phasic.** A **sign-inverting edge**: excitation here becomes suppression of sympathetic vasomotor
    drive there. Its magnitude is measured — lesioning these neurons in baroreceptor-denervated rats
    raises arterial pressure by about **40 mmHg** and splanchnic sympathetic nerve activity by about
    **200%**, so the inhibition is load-bearing even with the baroreflex removed. Fan-out: to derive.
    Two-ended within this file.
- **Sizing.** Basis: **per side.** **No count — unknown.** Zero derivable parameter memory, a gap.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)**, cell classes **GABAergic
  baro-activated** neurons (identified by glutamic-acid-decarboxylase-67 messenger ribonucleic
  acid) and
  **cholinergic cardiovagal motor** neurons, with **A1 noradrenergic** cells named by the competing
  parcellation below. N **to derive**, and **the sub-element list is contested rather than merely
  incomplete**.
- **Edge latency.** All three edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied and wholly within this file — every edge on
  this structure has its far end in file 14. **It is the only structure in the section of which that
  is true.** Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The structure's own boundary is contested and the file does not
  pick a side.** A more recent parcellation from the same laboratory lineage divides the lower
  ventrolateral medulla into three segments and places the bulk of the baroreflex GABAergic neurons,
  with the cardiovagal motor neurons, in an **intermediate ventrolateral medulla** between the
  rostral and caudal territories — reserving this entry's name for the region of A1 noradrenergic
  cells. **The data flow is not in dispute; where the middle term is drawn on a map is.** For the
  architecture that is the worse of the two disputes to have: a shape is allocated against a
  boundary, and an edge is not.
  **A name collision is recorded because the file is exposed to it.** The target of the output above
  is the rostral ventro**lateral** medulla, the sympathetic vasomotor source, which has its own entry.
  Other entries in this file name the rostral ventro**medial** medulla, the descending-analgesia
  source acting on the spinal dorsal horn, which has **no entry anywhere**. Two different structures,
  near-identical names, and the literature uses the same three-letter abbreviation for both — which is
  precisely the failure mode §3's write-names-out rule exists to prevent, arriving from the outside.

## Nucleus of the solitary tract

- **Function → structure.** The first central relay for **everything the body reports about itself** —
  cardiovascular, respiratory, gastrointestinal, gustatory and orotactile afferents on the facial,
  glossopharyngeal and vagus nerves. It runs from the pyramidal decussation rostrally to the caudal
  dorsal cochlear nucleus, **spanning the midline caudally as the commissural subnucleus and
  splitting into left and right halves rostral to the area postrema** — so its counting basis changes
  along its own length. Functionally it divides **rostral (gustatory)** and **caudal (visceral)**.
  Named subnuclei: **interstitial** (longest, most rostral, gustatory in monkey and human),
  **central**, **dorsomedial**, **medial**, **parvicellular**, **ventrolateral**, **commissural**.
- **Inputs.**
  - **← taste afferents on the facial, glossopharyngeal and vagus nerves** — taste quality and
    intensity, **topographically ordered by oral location**: anterior oral cavity most rostrally,
    posterior more caudally, pharynx and larynx more caudally still. Fan-in: to derive. **The
    receptors lie outside the scope boundary.**
  - **← vagal and glossopharyngeal visceral afferents** — arterial pressure from baroreceptors, blood
    chemistry from chemoreceptors, lung inflation, gastrointestinal distension; glutamatergic onto
    second-order cells. Fan-in: to derive.
  - **← the bloodstream, directly** — glucose, leptin and angiotensin II concentrations. **A chemical
    input and not a neural edge**, the second such case in the map after the retina's photon flux.
    **Fan-in: not applicable.**
  - **← insula, hypothalamus and amygdala** (descending) — payload **owed**. Fan-in: to derive.
    **This bullet names three producers**; the hypothalamic one is two-ended within this file.
    **The amygdalar third is two-ended against `08_medial_temporal_lobe`, confirmed 2026-08-13**,
    where it is a line of its own marked *payload owed at both ends*. **So one edge is a whole bullet
    at one end and a third of a bullet at the other**, and the split is owed here.
- **Outputs.**
  - **→ lateral parabrachial nucleus** — the visceral and gustatory payload for relay to limbic
    forebrain. Fan-out: to derive. Two-ended within this file.
  - **→ caudal ventrolateral medulla** — **arterial pressure**, as the excitatory glutamatergic drive
    that makes the baroreflex's inhibitory limb work. Fan-out: to derive. Two-ended within this file.
  - **→ the gustatory pathway** (`03_other_senses`), via the parvicellular ventral posteromedial
    thalamus to insular taste cortex — taste quality and intensity, typed at the gustatory entry.
    Fan-out: to derive. **Two-ended and confirmed 2026-08-14, and the deferral this line makes is
    honoured at the far end**: that entry types the payload as a five-ish-dimensional quality vector
    with an intensity scalar plus oral somatosensation, and records that **the quality alphabet is
    progressively re-encoded into an ensemble pattern as it ascends**, so the same payload description
    must not be carried at every stage. **This line carries the earliest stage of that payload and the
    far end carries the later ones.**
    **This entry holds a partition the far end lacks**: its seven named subnuclei, one of them
    **parvicellular**, and its rostrocaudal gradient. **The far end has recorded, from its side, that
    which subnucleus the gustatory line leaves from is owed** — and this entry is where the axis to
    answer it already exists. **Owed here: assign this edge to a subnucleus.**
    **The thalamic relay this line routes through is described in that same far file** — see the
    lateral parabrachial entry above — **so this line's intermediate stage and its consumer are both
    in `03_other_senses`, and neither is in `12_thalamus`.**
  - **→ branchiomotor and visceromotor nuclei**, to the dorsal motor nucleus of the vagus — the
    afferent limb of vagal reflexes; payload otherwise **owed**. Fan-out: to derive.
  - **→ hypothalamus** — payload **owed**. Fan-out: to derive. Two-ended within this file.
- **Sizing.** Basis: **per side rostrally, whole caudally** — the structure changes basis along its
  own length at the area postrema, which no other entry in the map does. **No count — unknown.** The
  one extent recorded is **more than 4 mm rostrocaudally in rat**, and it is a rat figure, not human.
  Zero derivable parameter memory, a gap.
- **Shape.** **Non-laminated nucleus**, rank 2: **(subnucleus, N)** with seven named subnuclei —
  **and a rostrocaudal coordinate that is a gradient rather than an index.** The classical claim that
  the nucleus is **viscerotopic**, each organ system terminating in its own subnucleus, is qualified
  by organ-specific viral tracing: vagal afferents from the gastrointestinal, cardiovascular and
  respiratory systems are **distributed broadly across multiple subnuclei rather than confined to
  organ-exclusive subregions**. **The gradient is real; exclusive organ compartments are not.**
  This is the same shape problem the anterior inferotemporal cortex raises in file 01 — a continuous
  map has no compartment axis to index — arriving here from a completely different tissue, which is
  weak evidence that it is a general case rather than a cortical curiosity. **What an edge terminating
  "on the gastrointestinal subnucleus" selects is to derive.** N to derive throughout.
- **Edge latency.** All nine edges **to derive**, and one of them has no conduction term at all: the
  blood-borne chemical input.
- **Invariant conformance.** Co-instantiation: satisfied; four of its nine edges close within this
  file, which is the densest within-file connectivity in the section. Per-edge latency: satisfied,
  all to derive; the chemical input takes real, finite, wildly different time and does not claim the
  conduction-plus-synapse justification.
- **Justification (biological).** This is the structure at which the map's data flow **starts from
  inside the body**, and the architecture consequence is that its input side is not an axon bundle.
  Two of its four input bullets do not name a producing region: the taste and visceral afferents
  begin at receptors outside the scope boundary, and the blood-borne input has no producer by design.
  An implementation that assumes every input edge has a source structure would leave this entry with
  half an input side and not notice.

## Rostral ventrolateral medulla

- **Function → structure.** The source of the **tonic excitatory drive to the sympathetic nervous
  system**, and therefore of resting arterial pressure. Defined over forty years ago as the territory
  of the **C1 adrenergic cell group**. Its **presympathetic bulbospinal** neurons are glutamatergic,
  some also adrenergic, are **barosensitive**, and project directly onto the sympathetic preganglionic
  neurons of the spinal intermediolateral cell column controlling heart, kidney, resistance vessels
  and adrenal medulla. **Not all presympathetic neurons here are C1 cells, and presympathetic neurons
  are also found elsewhere** — spinal cord, raphe, ventromedial medulla, pons and hypothalamus — so
  this is the principal source, not the only one.
- **Inputs.**
  - **← caudal ventrolateral medulla** — **GABAergic inhibition, tonic**; the baroreflex's sign
    inversion. Fan-in: to derive. Two-ended within this file.
  - **← nucleus of the solitary tract**, direct, alongside the indirect route above — payload
    **owed**. Fan-in: to derive.
  - **← hypothalamus** and **← periaqueductal grey** — payload **owed**. Fan-in: to derive. Both
    producers are in this file.
- **Outputs.**
  - **→ spinal cord grey matter, intermediolateral cell column** (`16_spinal_cord`) — the
    **excitatory presympathetic drive** setting vasomotor tone and cardiac sympathetic output.
    Fan-out: to derive. **Two-ended and confirmed 2026-08-14**, typed in the same words at both ends.
    **The far end carries one fact about this edge that this end does not**: that the drive is
    **generated by intrinsically pacemaking cells rather than relayed**, which it records as the one
    edge in its section that is not a projection, its timing being a property of the source cells
    rather than of the wire. **Those source cells are this structure's.** **Owed here: take the
    pacemaking attribution, since it is a property of this entry and is currently recorded only at the
    consumer.**
  - **→ hypothalamus, paraventricular nucleus**, from the **non-bulbospinal C1 group** — a signal
    regulating vasopressin and adrenocorticotropic hormone release and sodium intake; payload
    otherwise **owed**. Fan-out: to derive.
  - **→ locus coeruleus, raphe nuclei** (`13_neuromodulatory_systems`) and the dorsal vagal complex —
    payload **owed**. Fan-out: to derive. **Checked 2026-08-14 and neither far end names this
    structure.** Both declare `← hypothalamus`, and the locus coeruleus additionally declares
    `← nucleus paragigantocellularis of the medulla` as **its principal excitatory drive** — **a name
    that appears nowhere in this file, as an entry or as a sub-element.** **The two names sit in the
    same medullary territory and the identification would be a content claim, so it is not made
    here.** **Owed at the source: establish whether that nucleus is this entry, a sub-element of it,
    or a third thing.** If it is this entry, then this line reaches both nuclei together while that
    file's two entries name different sources — **an arity disagreement as well as a naming one.**
    **The bulbospinal neurons have brainstem collaterals, so these are not necessarily separate
    populations** — the same arity warning the parabrachial entry raises, in a different system.
- **Sizing.** Basis: **per side.** **No count — unknown.** Zero derivable parameter memory, a gap.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)** with three functionally distinct
  C1 groups — **bulbospinal presympathetic**, **hypothalamus-projecting**, and one **regulating
  parasympathetic efferents**. The three are sub-elements by the source's own test because the output
  edges above already leave from different ones, and **the collateral warning means the partition may
  not be a partition** — a bulbospinal cell with a brainstem collateral belongs to two groups at once.
  N to derive. No map axis recorded.
- **Edge latency.** All seven edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; the baroreflex loop through the solitary
  nucleus and the caudal ventrolateral medulla is closed entirely within this file, which makes it
  the one loop in the section that can be checked here. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **Its cells beat on their own.** In tissue slices these neurons show
  **intrinsic pacemaker activity**, upregulated by slow transmitters such as angiotensin II, so the
  sympathetic tone this region supplies is **generated, not relayed**, and the inhibition arriving
  from the caudal ventrolateral medulla acts on a drive that exists without input. This is the
  invariants section's finding in its home entry, in the narrowed form recorded there: a *stateless*
  threshold gate cannot fire at zero input, while a threshold gate in a delayed feedback loop is an
  ordinary relaxation oscillator — so what the standing output needs from the model is an **inverting
  term**, not a new mechanism. The baroreflex is then not a signal path but a **subtraction from a
  standing output**, which is a different computational shape from anything the visual line contains,
  and whether the biology generates it in the membrane or in the circuit is not settled by the
  source.

## Periaqueductal grey

- **Function → structure.** The midbrain grey surrounding the cerebral aqueduct — the integrating hub
  for **defensive behaviour, autonomic reaction, innate vocalisation, and descending pain
  modulation** — organised as **four longitudinal columns with distinct jobs**. The **dorsolateral**
  and **lateral** columns drive **active defence** (fight-or-flight, sympathetic and hypertensive
  response, non-opioid analgesia); the **ventrolateral** column drives **passive coping** (freezing
  and quiescence, hypotensive response, opioid analgesia) and is the origin of the descending
  analgesia circuit; a **dorsomedial** column completes the set. **No internal edge between columns is
  described and it is not established that one exists** — they may be parallel effectors selected by
  input.
- **Inputs.**
  - **← amygdala, central nucleus** (`08_medial_temporal_lobe`) — a **valence and urgency signal**,
    *this is bad, act now*, here driving the defensive response; **no identity information**. Fan-in:
    to derive. **Two-ended and confirmed 2026-08-13, and this line discharged a mark there**: the
    producer's line read *untyped there*. **This end types it and names the producing sub-element**,
    which the producer's own line does not.
  - **← hypothalamus** — payload **owed**; defensive and autonomic drive. Fan-in: to derive. Producer
    in this file.
  - **← ventromedial and orbital prefrontal cortex** — payload **owed**; top-down control of defence
    and analgesia. Fan-in: to derive. Two-ended against file 11.
  - **One forebrain input is declared at its producer and not here. Checked 2026-08-13.**
    `08_medial_temporal_lobe`'s bed-nucleus entry declares `→ periaqueductal gray` and records it as
    undeclared at this end. **It is.** **The bed nucleus is the sustained arm of the extended amygdala
    and the central nucleus above is the phasic arm**, so this entry declares one arm and not the
    other. **Owed at `human_brain_14_...`.**
  - **← spinal cord, lamina I**, via the **spinomesencephalic tract** — payload **owed**; ascending
    nociceptive input. About **120 lamina-I cells per side** (rat L4) project here and **over 90% are
    collaterals** of cells also projecting to the caudal ventrolateral medulla and lateral
    parabrachial area — **a branching axon, not an independent population.** Fan-in: to derive.
    **Two-ended and confirmed 2026-08-14** (`16_spinal_cord`), which declares the same edge from
    lamina I, carries the same ~120-cells-per-side figure and the same **over-90% collateral** finding,
    **and reaches it independently at its own end.** **This is the third entry in the section to record
    the same collateral warning**, which makes it a property of the ascending nociceptive system rather
    than of any one target — **and the far end records it as a property of its own output slot, that
    five of nine outputs are one population with collaterals rather than five populations.** **Both
    files therefore forbid summing these edges as independent populations**, which is the same
    constraint written twice from opposite ends.
- **Outputs.**
  - **→ rostral ventromedial medulla**, from the **ventrolateral column** — the **descending
    analgesic command**, the drive that gates nociception at the spinal first synapse; no stimulus
    content. Fan-out: to derive. **The rostral ventromedial medulla has no entry in any file** — named
    as a relay here and as a producer at file 16, owning no slot. Inherited; not repaired here.
  - **→ spinal dorsal horn** (`16_spinal_cord`), laminae I and II, directly and via the medullary
    relay — the **analgesic gate**: **a gain applied to incoming nociception at the first synapse, no
    content.** Fan-out: to derive. **Two-ended and confirmed 2026-08-14, and both ends type it in the
    same words.** **This end names the sub-element the command leaves from — the ventrolateral column
    — and the far end does not**; that has been recorded there as owed. **The far end's routing entry
    carries only the relayed limb and not the direct one**, which this line declares, and that is
    recorded there too.
  - **→ locus coeruleus** (`13_neuromodulatory_systems`), from the **ventrolateral column** — payload
    **owed**; the noradrenergic limb of descending analgesia. Fan-out: to derive. **Two-ended and
    confirmed 2026-08-14, and both ends name the ventrolateral column** — the consumer writes
    `← ventrolateral periaqueductal grey`, attributing it to the sub-element this entry's column axis
    carries. **Payload owed at both ends.** **This is the cleanest edge in the pass**: two-ended, both
    ends naming the same sub-element of the producer, and both owing the same thing.
  - **→ vocal and autonomic premotor targets** in the reticular formation and lower brainstem —
    payload **owed**; the innate vocalisation and freezing motor pattern. Fan-out: to derive. **This
    endpoint names a class**, and the reticular formation entry is in this file and does declare a
    periaqueductal input, so the class is partly resolvable within the file and is not resolved here.
  - **→ thalamus** (`12_thalamus`), ascending — payload **owed**; the affective pain projection.
    Fan-out: to derive. **This endpoint names a class**, and **it closes as a negative, checked
    2026-08-14: no entry in that section declares a periaqueductal input under any name.** The two
    plausible consumers were read directly — its intralaminar nuclei declare the reticular formation,
    the deep cerebellar nuclei, the lateral parabrachial nucleus, the pallidum and nigra, and a
    cortical class; its posterior / ventromedial-posterior entry declares the anterolateral system,
    the visceral line, the insula, the reticular nucleus and the zona incerta. **Neither names this
    structure.** **So the affective pain limb has a producer and no consumer**, which is a different
    state from a class with unresolved members. **Owed at the source, and at that file**: accept it at
    the nucleus that receives it, or establish that the description does not carry it.
- **Sizing.** Basis: **whole (midline)** — a sleeve of grey around the aqueduct. **Soft / no clean
  human count**, and the source states why in structural terms: it is **defined by function and
  column, not by a countable border.** Zero derivable parameter memory, a gap.
- **Shape.** **Non-laminated nucleus**, rank 2: **(column, N)**, four columns — dorsomedial,
  dorsolateral, lateral, ventrolateral — running longitudinally around the aqueduct. **The columns are
  load-bearing endpoints, not descriptive divisions**: two of the five output edges leave specifically
  from the ventrolateral column. N **to derive**, and no partition of any total to the four columns
  exists because no total exists. **A rank-3 shape (column, position along the aqueduct, N) is
  arguable** — the columns are longitudinal, so there is a rostrocaudal coordinate — but no map, pitch
  or extent along that axis is recorded, and adding the axis would assert an ordering the source does
  not use. **Rank 2, with the longitudinal coordinate noted and not indexed.**
- **Edge latency.** All nine edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied for the joints present; the descending
  analgesia limb runs through a structure with no entry, so **that path cannot be traced end to end at
  this rung** even though both its ends are described. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The analgesic output is **a gain applied at another structure's
  first synapse**, and the architecture has to say so rather than treat it as a signal: nothing on
  that wire is nociceptive content, and its effect is to change how much of somebody else's content
  gets through. **That is the same operation file 13's locus coeruleus performs on the whole cortex,
  arriving here on a single named edge with a single named target** — which makes it the most
  tractable instance of the multiplicative-gain problem anywhere in the map, and the place a solution
  would be easiest to test.

## Hypothalamus

- **Function → structure.** The master regulator of **homeostasis and the basic drives** —
  temperature, feeding, thirst, sleep and wake, circadian timing, stress, reproduction, defence —
  acting through **two output arms**. **Neuroendocrine:** magnocellular neurons of the supraoptic and
  paraventricular nuclei send oxytocin and vasopressin down their axons to the **posterior pituitary**
  for direct release into blood; parvocellular neurons release releasing and inhibiting hormones into
  the **hypophyseal portal** blood to command the **anterior pituitary**, including the
  corticotropin-releasing hormone → adrenocorticotropic hormone → cortisol stress axis.
  **Autonomic and behavioural:** descending control of autonomic preganglionic neurons through the
  periaqueductal grey, brainstem and spinal cord.
  **Structurally this is not one structure.** It is **at least eleven sub-nuclei**, each with a
  distinct payload and its own edges: **suprachiasmatic** (the circadian master clock, entrained by a
  direct retinal input), **arcuate** (metabolic sensing and the feeding balance, reading blood leptin
  and ghrelin at the leaky median eminence), **lateral hypothalamus** (orexin/hypocretin for
  wakefulness and feeding), **ventromedial** (satiety and defensive rage), **medial preoptic**
  (thermoregulation and sexual behaviour), **ventrolateral preoptic** (the sleep switch),
  **paraventricular** and **supraoptic** (magnocellular and parvocellular neuroendocrine), and the
  **mammillary bodies** (the Papez relay). **Internal edges among them are described in the
  literature — suprachiasmatic → paraventricular, arcuate → paraventricular, preoptic → the defensive
  and thermoregulatory effectors — and none is typed at the source.**
- **This entry is a bundle, and it is recorded as one rather than split here.** The design file's
  §6 rule is explicit: sizing runs per structure and the dangling-edge diff needs one unique name per
  structure, so a bundled source entry either becomes several entries at this rung or is **recorded as
  a bundle whose split is owed at the source** — and **it is not silently split here, because
  splitting invents the arity.** The source itself says each sub-nucleus is effectively its own
  region and marks this the heaviest internal conversion remaining in the file. **So the split is
  owed at the source and this entry stays one.**
- **Inputs.**
  - **← amygdala, central nucleus** (`08_medial_temporal_lobe`), via the **stria terminalis** and the
    **ventral amygdalofugal pathway** — a **valence and urgency signal**, *this is bad or good, act
    now*, driving autonomic, endocrine and freezing responses; **no identity information**. Fan-in: to
    derive. **Both named tracts lack entries anywhere.** **Two-ended and confirmed 2026-08-13, and this
    line discharged a mark there**: the producer's line read *untyped there*. **This end types it in
    the producer's own words and names both tracts**, which the producer names too — **so the two ends
    agree on the payload and only this one records that the tracts have no entries.**
  - **← hippocampal formation**, via the **fornix** (`08_medial_temporal_lobe`) — payload **owed**.
    Fan-in: to derive. **Two-ended and confirmed 2026-08-13 — and this single line may be standing for
    two edges.**
    **The producer declares two outputs that land in this entry, not one.** It declares
    `→ hypothalamus, via the fornix` and, separately, `→ mammillary bodies`, via the
    **post-commissural** fornix, as the Papez limb. **The mammillary bodies are a sub-element of this
    entry**, so both of the producer's lines terminate here while this slot declares one hippocampal
    input. **Neither end is wrong**: the producer separates the two because they leave by different
    fornix divisions, and this entry cannot separate them because it is a bundle. **The arity mismatch
    is a consequence of the bundle recorded above and resolves when the bundle splits.** **Owed at
    `human_brain_14_...`, with the split.**
  - **One further forebrain input is declared at its producer and not here. Checked 2026-08-13.**
    `08_medial_temporal_lobe`'s bed-nucleus entry declares `→ hypothalamus`, to the **paraventricular
    nucleus** and the feeding and autonomic nuclei, and records it as undeclared at this end. **It is.**
    **Owed at `human_brain_14_...`** — and note the producer names a sub-element this entry holds,
    so the edge arrives at a named part of the bundle rather than at the whole.
  - **← the septum** — payload **owed**. Fan-in: to derive. **This endpoint names a class**; the
    lateral septum has no entry anywhere. Inherited.
  - **← nucleus of the solitary tract** — payload **owed**; visceral and cardiovascular state.
    Fan-in: to derive. Two-ended within this file.
  - **← retina** (`01_visual_pathway`) **→ the suprachiasmatic nucleus**, via the
    **retinohypothalamic tract** — an **irradiance, "lights-on" signal**: ambient luminance for clock
    entrainment from melanopsin-expressing ganglion cells, **not spatial vision**. Fan-in: to derive.
    **The only edge in the section terminating on a sub-element that has a count.**
    **Two-ended and checked on 2026-07-29, and this end is much the fuller.** The producer declares
    `→ suprachiasmatic nucleus — from melanopsin ganglion cells` and stops: it gives the cell class and
    **no payload, no tract, and no statement that the signal is not spatial.** The *not spatial vision*
    clause is the load-bearing one, because the producer's other retinal outputs are all spatial and
    nothing at its end marks this one as different in kind. **Owed at the producer: the payload and the
    tract name.**
  - **← blood-borne signals** — leptin, ghrelin, glucose, osmolality, temperature — **sensed directly**
    at the circumventricular organs (median eminence, organum vasculosum of the lamina terminalis,
    subfornical organ) where the blood–brain barrier is open. Metabolic and osmotic state as
    **chemical concentration rather than a neural code**. **Fan-in: not applicable** — no producer
    region, and the edge is diffusion from blood. **An input with no source region by design, not an
    owed edge.**
  - **An edge is asserted against this structure from `11_frontal_lobe` and is not written here.**
    Its orbitofrontal / ventromedial prefrontal entry declares `→ the hypothalamus`, marked there as
    unchecked at the source. **Checked 2026-08-14: no input above names a prefrontal or orbitofrontal
    source under any name.** **The edge is not written in**, because writing it on the far end's
    declaration alone would assert a projection this section has read nothing for. **Owed at the
    source: establish it here, or withdraw it there.** The far end now carries the same finding from
    its side.
- **Outputs.**
  - **→ posterior pituitary**, from the **magnocellular supraoptic and paraventricular neurons** —
    **oxytocin and vasopressin released directly into blood**, a hormonal output and not a neural
    code. Fan-out: to derive. **An endocrine terminal, not an owed edge**: the posterior pituitary is
    a release site, not a processing region, and has no entry.
  - **→ anterior pituitary**, from **parvocellular** neurons, via the **hypophyseal portal blood** —
    releasing and inhibiting hormones into a private portal circulation. Fan-out: to derive. **An
    endocrine terminal.**
  - **→ periaqueductal grey, brainstem and spinal cord** (autonomic preganglionic control) — payload
    **owed**; descending autonomic and defensive drive. Fan-out: to derive. Two-ended for the
    periaqueductal grey (this file) and the spinal cord (`16_spinal_cord`); **the "brainstem"
    remainder names a class.**
  - **→ mammillary bodies → anterior thalamic nuclei**, via the **mammillothalamic tract** — payload
    **owed**; the Papez memory relay. Fan-out: to derive. Two-ended against file 12. **The mammillary
    bodies are a sub-element of this entry and the tract has an entry in file 18** — so one edge here
    crosses three files and a bundle boundary.
  - **→ brainstem tegmentum** — payload **owed**. Fan-out: to derive. **This endpoint names a class**;
    file 13's locus coeruleus, raphe and ventral tegmental entries each declare a hypothalamic input,
    so several far ends exist and the class is resolvable and not resolved.
  - **→ pineal gland**, functionally, via the **paraventricular nucleus → intermediolateral cell
    column → superior cervical ganglion** chain — the circadian **"it is night" disinhibition** that
    drives melatonin. Fan-out: to derive. Two-ended within this file. **A multi-synaptic functional
    route, not a direct axon** — the payload rides the chain, and one joint of the chain is outside
    the scope boundary.
  - **→ widespread limbic and cortical targets shaping motivated behaviour** — payload **owed**.
    Fan-out: to derive. **This endpoint names a class and does not resolve.**
- **Sizing.** Basis: **mixed within one entry.** The **suprachiasmatic nucleus is ~50,000 neurons per
  side** (human) — one of the smallest nuclei with a defined mapped function, and **the only firm
  neuron count in this entire section.** At the 16-bit fan-in bound that is **≤ 0.10 MB per side**,
  **≤ 0.20 MB both sides.** Every other hypothalamic nucleus is **soft or uncounted in human**.
  Whole-hypothalamus grey matter is **~4 g / ~4 cm³ both sides**, a soft secondary compilation figure.
  **Structure total: to derive**, ten of eleven sub-nuclei uncounted.
  **A density cross-check is available and is refused, and the refusal is the source's.** The
  suprachiasmatic nucleus is sub-cubic-millimetre and its ~50,000 count against that volume implies an
  implausibly high packing, so the two do not reconcile. The source states this and asserts no
  density; **this file does not compute one either.** The count is the honest anchor and the volume is
  soft. *(This is the case §9's cross-check procedure is for, and here the cross-check fails rather
  than closes — which is a finding about the source's numbers, recorded and not smoothed.)*
- **Shape.** **Non-laminated nucleus**, rank 2: **(sub-nucleus, N)** with at least eleven named
  sub-nuclei. **Extents: ~50,000 for the suprachiasmatic nucleus per side, to derive for the other
  ten.** No map axis is recorded for any of them. **The shape is the bundle problem in its allocation
  form**: an array indexed by sub-nucleus is allocatable only where the sub-nucleus has a count, so
  one slot of eleven can be sized and the entry cannot.
- **Edge latency.** All thirteen edges **to derive**, and **three of them are not conduction plus
  synaptic transmission**: the blood-borne input and the two pituitary arms. **This entry's Outputs
  field spans the map's whole latency range on its own** — millisecond projections, minutes-to-hours
  hormonal arms, and a joint of a twenty-four-hour loop.
- **Invariant conformance.** Co-instantiation: satisfied and heavily cross-file — five of its
  thirteen edges are two-ended against files 1, 8, 12 and 16, and two close within file 14. The
  circadian loop closes through the pineal entry below with one joint outside the boundary.
  Per-edge latency: satisfied, all to derive, with three edges in classes the invariant's biological
  justification does not cover.
- **Justification (biological).** This is the structure at which **the map stops being a nervous
  system**. Two of its output arms terminate in blood rather than at a synapse, one of its input arms
  begins in blood, and the whole neuroendocrine half of its function is a chemical control loop whose
  latencies are minutes to hours. The design file's scope boundary excludes the non-neuronal layer
  and everything past the transducer on the body side — **and this entry's function is defined by
  traffic across exactly that boundary.** An architecture that carried only the projections would keep
  the structure and lose what it is for.

## Pineal gland

- **Function → structure.** The **neuroendocrine output arm of the circadian system**: a small
  midline epithalamic gland that converts the suprachiasmatic clock's neural signal into a hormonal
  one, secreting **melatonin** into blood and cerebrospinal fluid at night. Darkness raises melatonin
  and light suppresses it; melatonin is the body's principal **"it is night" signal**, entraining
  peripheral clocks and timing sleep. **Its pinealocytes — about 95% of its cells — are secretory
  endocrine cells, not neurons.** The gland **transduces; it does not compute.**
- **Inputs.**
  - **← superior cervical ganglion** (sympathetic fibres onto pinealocytes), terminating the
    **multisynaptic circadian efferent chain**: retina, melanopsin ganglion cells →
    retinohypothalamic tract → suprachiasmatic nucleus → paraventricular nucleus →
    intermediolateral cell column → superior cervical ganglion → here. **Carries noradrenaline
    (norepinephrine), gated by the clock** — darkness disinhibits the paraventricular nucleus, the
    ganglion releases noradrenaline, and through β-adrenergic signalling this drives the rate-limiting
    melatonin enzyme; light re-imposes suprachiasmatic inhibition and shuts synthesis off. **The
    payload is a "darkness / night" permission signal, not content.** Fan-in: to derive. **The
    superior cervical ganglion is a peripheral autonomic ganglion, outside the scope boundary, and has
    no entry**; the chain's upstream stations are in this file and file 16, and file 20 declares the
    chain.
- **Outputs.**
  - **→ the general circulation and cerebrospinal fluid** — **melatonin, an endocrine and not a
    synaptic output**, reaching targets brain-wide and peripherally. Fan-out: to derive. **An
    endocrine terminal with no target region and no consumer** — the fourth non-projection class in
    the invariants above.
  - **→ suprachiasmatic nucleus** (melatonin feedback, via melatonin receptors) — melatonin as a
    **phase-feedback signal closing the circadian loop**. Fan-out: to derive. Two-ended within this
    file and declared at file 20. **This limb is a hormonal action on a receptor-bearing target, so it
    is a real edge with a consumer, unlike the diffuse output above** — and it is what puts the
    circadian loop's closing limb inside the map.
- **Sizing.** Basis: **whole (midline).** **Neurons: none.** Pinealocytes are secretory endocrine
  cells; the gland is *innervated by* sympathetic fibres and contains no projection neurons.
  **Parameter memory: zero**, and it is a **positive zero** of a third kind — not a tract's zero (no
  neurons because it is fibres) and not a transducer's zero (neurons that store no threshold), but a
  structure with **no neurons at all that is nonetheless a load-bearing loop stage.** Its one firm
  physical number is a **volume: ~90–210 mm³ across human imaging cohorts**, with a soft-tissue
  parenchyma fraction and an age-increasing calcified fraction; gland weight ~100–150 mg. **A rare
  verified physical figure for a structure this small, and it is a volume where every other structure
  in the section is missing a count.**
- **Shape.** **None of the design file's four shape classes fits.** It is not a sheet, not a
  laminated or non-laminated nucleus, and not transmission-only — a tract's shape is a routing index
  from source line to destination, and this gland has no lines to route. **What it holds is a single
  scalar concentration varying in time**, so its rank is arguably **0** with a time axis, and
  recording it as any activity array would assert state it does not have in the form it does not have
  it. **Recorded as a new shape case, marked open, and not forced into an existing class.** *(Claude's
  reading. The tissue facts are Class 1 from the source.)*
- **Edge latency.** All three edges **to derive**, and **none of them is an ordinary projection
  latency**: the input is the terminal limb of a six-station multisynaptic chain, and both outputs are
  hormonal. The melatonin feedback edge's latency is a **synthesis, secretion, circulation and
  receptor-binding time**, which shares no term with a conduction delay.
- **Invariant conformance.** Co-instantiation: **the gland cannot be brought up late without leaving
  the circadian loop open**, and unlike the cerebro-cerebellar case that loop's stages all exist —
  one of them simply lies outside the scope boundary. Per-edge latency: satisfied in requirement,
  unsupported in justification, on all three edges.
- **Justification (biological).** **Internal data flow is *not applicable*, as a positive statement
  about the tissue.** There is no intra-glandular projection circuit; the one transduction step —
  noradrenaline to second messenger to enzyme to melatonin — is **intracellular biochemistry within
  pinealocytes, not an inter-cellular edge.** This matters for the architecture because it is the
  cleanest case in the map of a stage that is load-bearing in a loop and has **no computation to
  represent at all**: an implementation of this structure is a gated scalar, and everything about it
  that is interesting is in the timing of the gate.

## Reticular formation

- **Function → structure.** The diffuse, phylogenetically old **core of the brainstem tegmentum** —
  **not one nucleus but a mesh of ill-bordered cell groups** running from medulla to midbrain, with
  two roles. **Ascending, the arousal engine:** the ascending reticular activating system sets
  arousal, wakefulness and consciousness, driving the **intralaminar thalamus** and, diffusely, the
  cortex; its transmitter arms are the cholinergic **pedunculopontine** and **laterodorsal tegmental**
  nuclei plus the monoaminergic systems of file 13 and the histaminergic **tuberomammillary nucleus**.
  **Descending, pattern generation and premotor control:** reticulospinal control of postural tone and
  locomotion; the **central pattern generators** for breathing (the **pre-Bötzinger complex**) and
  cardiovascular tone (the rostral ventrolateral medulla, which has its own entry above); and the
  **premotor coordinators** sequencing the cranial-nerve motor nuclei — the saccade **burst
  generators** (**paramedian pontine reticular formation** and **rostral interstitial nucleus of the
  medial longitudinal fasciculus**) and the chewing, swallowing and facial/laryngeal patterns.
- **Inputs.**
  - **← collaterals of the ascending sensory systems** — payload **owed**; the non-specific sensory
    drive that maintains arousal. Fan-in: to derive. **This endpoint names a class**, and the source
    notes the class may be close to the real claim and is not exempt.
  - **← cerebellum, from the fastigial nucleus** — payload **owed**. Fan-in: to derive. Two-ended
    against file 10.
    **Diffed end to end against `10_cerebellum`, and three things follow.**
    **The producer is the deep cerebellar nuclei entry**, whose fastigial nucleus is a sub-element of
    it — **not the cerebellum**, which is a region with no entry there: that file's three entries are
    the cerebellar cortex, the deep cerebellar nuclei and the inferior olive. **This endpoint names a
    class with exactly one resolvable member**, and it is **inherited** — the source writes
    `← the cerebellum, from the fastigial nucleus` in these words — **so §2 forbids renaming it here.**
    **The mechanical consequence is worth stating because it is the reason the repair matters:** the
    endpoint resolves to nothing from that side, so **the edge index pairs neither end** — it reports
    producer-only at file 10 and an unresolved endpoint here, one edge wearing two different failures,
    and *cerebellum* is the single most repeated unresolved endpoint in the whole map. **A pass that
    runs the index over this file will not see this pair until the source names the entry.**
    **Owed at the source: name the producing entry**, which is the deep cerebellar nuclei; the
    sub-element is already there and correct.
    **The producer types the payload and this end does not**: it carries *axial posture, balance, and
    eye-movement corrections*, written on one line that also names the vestibular nuclei as a target.
    **This entry declares the reticular limb alone**, which supplies the split that file records as
    owed for this target. **Owed here: take the payload from the producer.**
    **Neither end names where in this structure the limb arrives**, which is not obviously repairable:
    the Shape field below records that only some of this entry's sub-elements have borders at all.
    **And a fourth file's bullet may land on the same joint.** `15_cranial_nerve_nuclei`'s
    pretectum-and-gaze-integrator entry names *cerebellum* among four producers reaching **the
    integrators and burst generators**, and **the burst generators are sub-elements of this entry** —
    as that file already establishes for the collicular term of the same bullet. **So a cerebellar
    drive onto them would be this edge at a finer grain rather than a second edge**, and the finer
    grain is one this end cannot state until its sub-element question is settled. *(Claude's reading;
    the bullet and the sub-element attribution are Class 1 from that file and this entry.)*
  - **← periaqueductal grey** — payload **owed**; the vocal and freezing motor patterns. Fan-in: to
    derive. Two-ended within this file.
  - **← hypothalamus** — payload **owed**; descending autonomic and arousal drive. Fan-in: to derive.
    The producer is in this file and names this structure only inside its "brainstem tegmentum" class.
  - **← cerebral cortex** — payload **owed**; top-down control of arousal and of the premotor pattern
    generators, the frontal eye field onto the saccade burst generators being the sharpest case.
    Fan-in: to derive. **This endpoint names a class.**
- **Outputs.**
  - **→ intralaminar thalamus** (ascending arousal) — payload **owed**; the arousal drive. Fan-out:
    to derive. Two-ended against file 12.
  - **→ cerebral cortex** (diffuse ascending arousal) — the arousal and gain signal, **no content**.
    Fan-out: to derive. **This endpoint names a class covering every cortical entry** — and the source
    adds a qualification that matters structurally: **much of the diffuse cortical arousal is
    delivered by the monoaminergic and cholinergic nuclei of file 13 rather than by reticular cells
    directly**, so the direct reticulo-cortical limb and the neuromodulator-relayed one are not
    distinguished and need to be.
  - **→ spinal cord** (`16_spinal_cord`) (reticulospinal, postural and autonomic) — payload **owed**.
    Fan-out: to derive. **Two-ended and confirmed 2026-08-14**, the far end carrying this limb inside
    a five-tract descending bundle whose payload it also marks owed. **Payload owed at both ends.**
    **And a cross-file check the far end asked for closes as a negative here.** That file's
    central-pattern-generator entry declares one input crossing a structure boundary — `← mesencephalic
    locomotor region (reticular formation)`, typed as **a start / speed command for locomotion**, not
    the pattern itself — and records that whether this entry types that edge was owed and unrun.
    **It is not typed here.** This entry declares one spinal output and it is the line above;
    **locomotion appears in this entry's Function field and on no edge**, and **the mesencephalic
    locomotor region is not named as a sub-element** of this structure. **So the consumer types a
    payload the producer does not declare, on an edge the producer does declare.** **Owed at the
    source: type the locomotor limb here, or establish that it is a separate edge from the postural
    one.** Not written in.
  - **→ cranial-nerve motor nuclei** (`15_cranial_nerve_nuclei`) — payload **owed**; the premotor
    sequencing signal for saccade bursts, chewing, swallowing and facial/laryngeal patterns. Fan-out:
    to derive. **This endpoint names a class**; the individual nuclei are described in file 15.
    **Two-ended and confirmed 2026-08-14, payload owed at both ends.** That file declares two inputs
    against this one — its branchiomotor pools take `← the reticular premotor pattern generators` for
    chewing, swallowing, respiration and vocalisation, and its ocular motor nuclei take
    `← the brainstem saccade burst generators`, **naming the paramedian pontine reticular formation
    and the rostral interstitial nucleus of the medial longitudinal fasciculus by name** — the same two
    sub-elements this entry names.
    **So the class can be split from the far end and cannot be split from here.** That file assigns the
    generators by axis — **horizontal to the abducens, vertical to the oculomotor and trochlear
    nuclei** — and assigns the pattern generators to the rhythmic pools. **Owed here: split this class
    to the pools each sub-element drives**, using the assignment the consumer already carries. **Not
    split here**, per §6.
- **Sizing.** Basis: **whole (both sides).** **Soft / unknown**, and the source gives the structural
  reason: it is **a distributed, ill-bordered network defined by connectivity and transmitter, not a
  countable nucleus.** Zero derivable parameter memory, and this is the entry where that is least
  repairable — a count needs a border.
- **Shape.** **This structure does not have one shape, and the honest record is two.** Some
  sub-elements have real borders and are ordinary non-laminated nuclei — the **pre-Bötzinger complex**,
  the **paramedian pontine reticular formation**, the **rostral interstitial nucleus of the medial
  longitudinal fasciculus**, the **pedunculopontine** and **laterodorsal tegmental** nuclei — each
  rank 2, **(cell class, N)**, N to derive. **The remainder is a network without countable
  sub-elements**, and the source is explicit that the boundaries are **genuinely indistinct rather
  than merely unwritten.**
  **That distinction is load-bearing at this rung and the design file's vocabulary does not carry it.**
  Writing the remainder's sub-element axis as *to derive* would assert that a partition exists and
  has not been measured, and the source says the opposite. It is nearer to **not applicable** — the
  positive statement — but *not applicable* is used for a property the tissue lacks, and this is a
  partition the tissue lacks while the neurons plainly exist. **Recorded as: discrete sub-elements
  where borders exist, and no sub-element axis for the remainder, which is not the same as an
  unmeasured one.** *(Claude's reading; the mesh description is Class 1 from the source.)*
- **Edge latency.** All nine edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied; two of its nine edges close within this
  file and two more against files 10 and 12. **The saccade burst generators are sub-elements of this
  entry and are named as targets by the superior colliculus above**, so one of the section's few
  fully within-file edges terminates on a sub-element of a structure whose sub-elements are partly
  uncountable. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The entry is the clearest case in the map of a structure that is
  **real, load-bearing, and not a unit.** Its discrete parts are genuine nuclei with their own edges;
  its diffuse remainder is a mesh; and an architecture must allocate against both. Treating the whole
  as one array asserts a homogeneity the tissue denies, and splitting it into the named nuclei alone
  discards the arousal engine, which is the part with no borders. **The source's own instruction —
  name the sub-nuclei that have borders and mark the remainder a network without countable
  sub-elements — is the correct architectural record and is carried unchanged.**

## Rostromedial tegmental nucleus

- **Function → structure.** The **GABAergic inverting relay** that converts the lateral habenula's
  "bad-outcome" signal into inhibition of midbrain dopamine neurons. It is the structure that lets a
  *negative* reward-prediction error suppress dopamine: the habenula fires to worse-than-expected
  outcomes and **excites** this nucleus, which **inhibits** the dopamine cells, so their firing dips
  below baseline. **Without it there is no route from the habenula's glutamatergic output to a
  decrease in dopamine — the sign inversion happens here.** It encodes aversive events and reward
  omission, inhibits motor responding to them, and is a µ-opioid-receptor-rich site. Also called the
  **tail of the ventral tegmental area**, and recently defined. **About 72% of its projection neurons
  are GABAergic**; a **core / periphery** distinction is reported, the core more strongly
  shock-cue-responsive. **No internal edge is described.**
- **Inputs.**
  - **← lateral habenula** — a **negative / aversive value signal**: a glutamatergic excitatory drive
    encoding worse-than-expected outcome, **the major input and the one that defines the nucleus**.
    Fan-in: to derive. Two-ended against file 17.
  - **← laterodorsal and pedunculopontine tegmental nuclei** — payload **owed**; a cholinergic input.
    Fan-in: to derive. **The far end is the reticular formation entry in this file**, which names
    those nuclei as its cholinergic arm and does not yet type an edge here — **an owed edit inside
    this file**, and the only one in the section.
  - **← extended amygdala** (`08_medial_temporal_lobe`)**, lateral septum, and periaqueductal grey** —
    payload **owed**; aversion-related and defensive-state inputs. Fan-in: to derive. **The lateral
    septum has no entry anywhere**; the periaqueductal grey is in this file and does not declare this
    edge.
    **The amygdalar third is a class endpoint, and holding `08_medial_temporal_lobe` open beside this
    file on 2026-08-13 showed it pointing at a class endpoint coming the other way.**
    ***Extended amygdala* names two entries in that file** — the amygdala and the bed nucleus of the
    stria terminalis, which that file describes as the phasic and sustained arms of one system.
    **Neither declares an output to this nucleus.** What that file's bed-nucleus entry does declare is
    an unwritten output to **"brainstem autonomic and neuromodulatory centres"**, a class it records as
    resolving to no named structure, with **name them** owed.
    **This nucleus is a member of that class, and that structure is a member of this one.** **Each
    endpoint is the other's missing far end**, and neither file could see it: on both sides the far end
    is inside a class name rather than absent, so both ends read as unresolved rather than as two
    halves of one edge.
    **Owed at both sources, and the two repairs are one question**: whether the aversive drive to this
    nucleus arises from the central amygdala, from the bed nucleus, or from both. **Answering it splits
    this endpoint and names a member of that one in the same stroke.** Not repaired here — both
    endpoints are inherited and §2 forbids it.
  - **← substantia nigra** (`09_basal_ganglia`) — payload **owed**; a lesser input. Fan-in: to derive.
- **Outputs.**
  - **→ ventral tegmental area**, synapsing on its **dopamine neurons** — **inhibition**: a GABAergic
    brake, the sign-inverted image of the habenular input; **no content, a negative gain on the
    dopamine cells' firing**. Fan-out: to derive. **Two-ended and confirmed 2026-08-14, and this end
    discharged a mark in `13_neuromodulatory_systems`.** That file's ventral tegmental entry writes the
    edge as `← lateral habenula, via the rostromedial tegmental nucleus` and noted that **the relay is
    a structure on the edge with no entry in its own file**, recording that the source inventory said
    it had gained one here **which that file had not read.** **It had. This is it.** **So the waypoint
    on that edge is a described structure with a count basis, a shape axis and its own inputs**, and
    the payload agrees at both ends. **What stays owed there is unchanged** — whether that file should
    carry an entry of its own or defer to this one is a source decision, not a missing edge.
  - **→ substantia nigra pars compacta** (`09_basal_ganglia`), on its dopamine neurons — the same
    GABAergic inhibition; **stimulation suppresses ~90% of pars-compacta dopamine cells.** Fan-out:
    to derive. **Two-ended.**
  - **→ hypothalamus and other targets beyond the dopamine midbrain** — payload **owed**. Fan-out: to
    derive. **This endpoint names a class**, and whether the dopamine midbrain is the whole story is
    owed.
- **Sizing.** Basis: **per side.** **Soft / no clean human absolute count** — a small, recently
  defined nucleus. Human anatomical mapping now exists and reports **location rather than an unbiased
  count.** Zero derivable parameter memory, a gap.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)**, cell classes **GABAergic (~72% of
  projection neurons)** and non-GABAergic, with a **core / periphery** division reported. **The
  72% is a fraction of an uncounted total**, so unlike the ventral tegmental area in file 13 — whose
  ~65/30/5 split partitions an order-of-magnitude count into three usable extents — this partition has
  nothing to partition. **A ratio without a total sizes nothing**, and the two entries make the point
  side by side.
- **Edge latency.** All seven edges **to derive.**
- **Invariant conformance.** Co-instantiation: satisfied, and this entry is why — **it is the stage
  that four other files were pointing at with no slot**, and its creation closes the habenula →
  dopamine limb end to end across files 9, 13, 17 and 20. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** **The sign inversion has a dedicated structure, and that is the
  architectural claim.** The design file records that a sign-inverting stage is not expressible as a
  count of active inputs crossing a threshold, and records it from the outer retina where the
  inversion happens at a receptor on a non-spiking cell. **Here the same operation is performed by a
  whole nucleus of ordinary spiking threshold gates**, and that is the tractable version: an
  excitatory input, an inhibitory output, and a population in between. So the map contains **two
  physically different implementations of one logical operation**, and only one of them is a problem
  for the sizing model. *(That the two are the same operation implemented differently is Claude's
  reading; both mechanisms are Class 1 from the source.)*

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Superior colliculus | per side | soft, no clean human total | ≤ 16 | to derive |
| Lateral parabrachial nucleus | per side | unknown | ≤ 16 | to derive |
| Caudal ventrolateral medulla | per side | unknown | ≤ 16 | to derive |
| Nucleus of the solitary tract | per side / whole caudally | unknown | ≤ 16 | to derive |
| Rostral ventrolateral medulla | per side | unknown | ≤ 16 | to derive |
| Periaqueductal grey | whole (midline) | soft, no clean count | ≤ 16 | to derive |
| Hypothalamus — suprachiasmatic nucleus | per side | ~50,000 | ≤ 16 | ≤ 0.10 MB |
| Hypothalamus — the other ten sub-nuclei | mixed | unknown | ≤ 16 | to derive |
| Pineal gland | whole (midline) | **none** | — | **0** |
| Reticular formation | whole (both sides) | soft, no countable border | ≤ 16 | to derive |
| Rostromedial tegmental nucleus | per side | soft, no clean count | ≤ 16 | to derive |
| **stated total** | mixed | **~50,000 counted** | | **≤ 0.10 MB per side** |

**Ten structures, and the table has one number in it.** The section's entire derivable parameter
memory is the suprachiasmatic nucleus at **≤ 0.10 MB per side**, ≤ 0.20 MB both sides. V1 alone at
the middle of its fan-in range is **525 MB**, about **5,250 times** the whole of what this section can
be shown to require. **That ratio is not a fact about the brainstem; it is a fact about the
measurements**, and stating it the other way round would be the error. Nine structures are missing a
count, not known to be small.

**The pineal's zero is the only figure in the table that is not a gap.** It is a positive statement:
the gland has no neurons, so it stores no thresholds, and no measurement will change that.

**What the section needs before it can be sized, in the order it would help.** A neuron count for the
superior colliculus, which is the one structure here with a defined border, a laminar organisation
and a measurable surface — it is the section's most tractable count and the only one where a shape
would follow from it. Then counts for the discrete reticular sub-nuclei, which are bordered even
though their parent is not. The periaqueductal grey and the reticular remainder are last, and may
never be countable in the form this table wants, **because a count needs a border and those two are
defined without one.**

## Three findings this file records and does not repair

**The baroreflex is a subtraction from a standing output, and the standing output needs a sign
rather than a new mechanism.** The rostral ventrolateral medulla's presympathetic cells are described
as intrinsic pacemakers, so the sympathetic tone they supply is generated rather than relayed, and the
inhibition arriving from the caudal ventrolateral medulla acts on a drive that exists without input.
**A stateless threshold gate cannot produce that; a threshold gate in a delayed feedback loop can** —
the per-edge-latency invariant supplies the delay, and the construction is the ordinary relaxation
oscillator. What is missing is the **inverting term**, which the design file already records from the
outer retina and which this section shows again on a plain spiking edge at the caudal ventrolateral
medulla. **So this is not a second independent finding against the §6 model; it is the sign gap
turning up in a place where it costs a whole structure's behaviour rather than one synapse's.**
Whether the biological pacemaking is cell-intrinsic or circuit-generated is not decidable from the
source and is owed. *(Physiology Class 1; the reduction to the sign gap is Claude's reading.)*

**A count needs a border, and three structures here are defined without one.** The periaqueductal grey
is defined by function and column, the reticular formation by connectivity and transmitter, and the
caudal ventrolateral medulla's boundary is actively contested between two parcellations. The design
file's shape machinery assumes a structure whose extent can in principle be measured and simply has
not been. **These are structures for which the measurement may not be well posed**, and the difference
matters because *to derive* promises that an experiment would settle it. Recorded, because writing *to
derive* over all three would overstate what is missing by one category. *(Claude's reading; the three
definitional statements are Class 1 from the source.)*

**The map's data flow crosses out of the nervous system at this section, in both directions, and the
scope boundary was drawn before that was visible.** Two inputs arrive as chemical concentration from
blood, three outputs leave as hormone into blood, one of those three has a receptor-bearing consumer
inside the map and is a real edge, one has no consumer at all, and one input arrives through a
peripheral ganglion that is out of scope by rule. **Seven of eighty edges, concentrated in three
entries.** The design file's non-projection enumeration — optical, endocrine or blood-borne,
mechanical — covers most of this by name and does not cover an edge with **no target region**, and
nothing on the ladder gives a shape for a structure that holds a hormone concentration rather than an
activity array. **The scope boundary is the source's and is inherited, not re-decided here**; what
this file records is that the boundary is crossed more often, and more load-bearingly, in this
section than anywhere else in the map.
