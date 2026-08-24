# Brain architecture — 13 neuromodulatory systems

**Date:** 2026-08-22
**Derived from:** `human_brain_13_neuromodulatory_systems_2026_07_24.md` — the four diffuse
neuromodulatory sources. **One source file, and no other content source.**

**Cross-file passes contained in this file.** Each line records a pass in which another file was held
open beside this one and their shared edges were diffed and stemmed. **A copy of this file missing a
line below is an older copy, whatever its filename says.**

- **2026-08-14** — `09_basal_ganglia`, `11_frontal_lobe`. **Sixteen shared edges diffed and stemmed.
  Two stale marks discharged at `09_basal_ganglia` and none here; one consumer-only edge of this file's
  confirmed absent at its far end and one producer-only edge of that file's confirmed absent here; and
  **four class endpoints in this file naming prefrontal cortex as a source found to have no producer
  in `11_frontal_lobe` at all** — one negative covering every ascending limb this section declares.
- **2026-08-14** — `12_thalamus`, `14_brainstem_midbrain_hypothalamus`. **Twelve shared edges diffed
  and stemmed; five two-ended, one class closed as a negative against `12_thalamus`, one endpoint's
  missing relay found to have an entry after all, and one endpoint resolved to a sub-element rather
  than to nothing.**
- **2026-08-13** — `08_medial_temporal_lobe`. **Thirteen shared edges diffed; four marks corrected at
  the far end, one endpoint here found to be misnamed, and one class endpoint confirmed outstanding.**
- `10_cerebellum`. **One shared edge diffed and stemmed. Two-ended, and a mark at the far end
  discharged: it had recorded this file's cerebellar output as reaching it inside the brain-wide
  cortical class, where it is a named edge here — the same correction this file already made for its
  hippocampal consumer.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number.** Stems below
are written only where the far file is checked against this one; an endpoint with no stem is
unchecked, and that is not a claim that none exists.

**Counting basis is declared per structure and is not uniform in this section, and two of the four
declare no basis at all.** The locus coeruleus is counted **per side**. The raphe is a **midline**
structure and its one count is reported **whole**. The ventral tegmental area and the basal
forebrain carry order-of-magnitude counts with **no basis stated at the source**, so their basis
reads **to derive** — and that is not a formality, because a factor of two sits between the two
readings.

**Every edge in this section leaves the section.** Forty-five edges, twenty in and twenty-five out,
and **not one of them has both ends inside this file**. **Thirteen of the forty-five reach
`08_medial_temporal_lobe`, which is the heaviest far-end dependency in the section and the first one
read beside this file — on 2026-08-13.** All thirteen were declared at both ends once one misnamed
endpoint was resolved; see the ventral tegmental area's amygdalar input. The four structures do not
connect to each
other. That is the section's defining structural property and it is why the far ends live in files
8, 9, 10, 11, 12, 14, 16 and 17. This file records the far-end dependency and does not write an edge
whose far end it did not read; where the source itself marks an end owed or unconfirmed, that mark is
carried here rather than repaired here.

**Fourteen of the forty-five endpoints name a class rather than a structure** — counted, not
estimated — which is just under a third of the section. Every one of them is inherited from the
source, which marks each owed, so §2 forbids repairing them here. They are: prefrontal cortex three
times, as an input to three different structures; the entire cerebral cortex three times, as an
output of three of them; thalamus; striatum; the limbic system; limbic and prefrontal cortex;
brainstem; and three "further targets beyond those named" remainders. **The design file's rule that
an edge names its target structure and not its class is therefore unsatisfiable for a third of this
section at the rung below the source** — and that is not a local defect, it is what a brain-wide
diffuse projection looks like when it meets a named-endpoint discipline.

**A synonym pair was carried in from the source and is resolved rather than flagged.** The source
wrote the locus coeruleus transmitter as both **norepinephrine** and **noradrenaline**, and two
strings for one substance is the same defect an abbreviation is — the dangling-edge diff cannot tell
that they match. They name one molecule and the split is regional, not chemical. **The derived
vocabulary is what settles it, because that part is not split**: both nomenclatures form the
adjective as **noradrenergic** and the receptors as **adrenergic**, there is no
"norepinephrinergic", and the A6 cell group's own anatomical name is a **noradrenergic cell group**.
A document using *norepinephrine* for the noun therefore holds two roots for one substance
regardless. **Noradrenaline throughout, with the synonym given once at the entry that owns the
name.**

---

## Structural invariants

**Whole-pathway co-instantiation.** All four structures exist and are active from the outset, and
this section is where the invariant is at its least optional. A neuromodulator sets the **gain** at
which other structures run. A structure brought up later does not merely leave a loop open; it
leaves every structure it modulates running at an undefined gain until it arrives, so the whole
pathway computes something different before and after. The loops themselves are also present and
closed across file boundaries: the ventral tegmental area sits in a nucleus-accumbens / ventral-
pallidum limb that returns to it, the locus coeruleus and the amygdala are reciprocal, and the
lateral habenula reaches both the ventral tegmental area and the raphe. **None of those loops closes
inside this file**, so co-instantiation for this section is a claim about the whole map and cannot be
checked within it.

**Per-edge latency.** Every edge below carries a nonzero, finite, heterogeneous latency in real time
units. **This section can name none of them: every latency reads *to derive*.** The source records
no conduction time and no synaptic delay anywhere in file 13. Two timing facts appear and neither is
an edge latency: the theta reference carried on the septo-hippocampal γ-aminobutyric-acid (GABA)
edge is a **4–12 Hz** membrane oscillation intrinsic to the pacemaker cells, and the whole section is
described as slow modulation against fast relay — a qualitative ordering with no figure.

**A fourth non-projection edge class appears here, and it is volume transmission.** The design file
already records three edges that are not conduction-plus-synaptic-transmission — optical, endocrine
or blood-borne, and mechanical. This section adds one. The medial septum's cholinergic edge to the
hippocampus is delivered **largely by volume transmission**: about **93% of cholinergic varicosities
in the hippocampus form no classic synapse**, so the transmitter is released into the extracellular
space and reaches its targets by **diffusion**. The invariant's requirement holds — the edge takes
real, finite time — while its biological justification does not, because there is no synapse to
charge a synaptic delay to and no single postsynaptic target to conduct to. A diffusion time and a
conduction time are not the same quantity and do not scale the same way with distance. **The
architecture states the edge's latency as *to derive* and does not claim the conduction-plus-synapse
justification for it.** *(That volume transmission is a fourth class of the kind §4 already
enumerates is Claude's reading. The 93% figure and the volume-transmission mechanism are Class 1 from
the source.)*

**There is no global clock, and one of this section's payloads is a clock.** The septo-hippocampal
parvalbumin edge carries a **theta timing reference — the phase of a 4–12 Hz oscillation** — and the
source is explicit that the tick is an **intrinsic hyperpolarisation-activated cyclic-nucleotide-gated
channel current** in those cells, not something GABA generates; GABA is the wire and the
synchronising coupling. **This is a local, biological oscillator on one edge between two named
structures. It is not a global clock and must not be read as one**, and nothing in this section
licenses a step, a cycle, a frame or a tick anywhere else. That a real oscillator exists in the
biology is precisely what makes the confusion available, which is why it is stated here.

---

## Ventral tegmental area

- **Function → structure.** The reward and motivation dopamine source. Two projections define it —
  the **mesolimbic** limb to the nucleus accumbens and ventral striatum, and the **mesocortical** limb
  to the prefrontal cortex — and it shares the reward-prediction-error signal with the substantia
  nigra pars compacta, the two dopamine systems splitting as **pars compacta = motor loop, ventral
  tegmental area = reward and limbic loop**. Structurally it is a **mixed population, not a
  dopaminergic one**: ~65% dopaminergic, ~30% γ-aminobutyric-acid (GABA) ergic, ~5% glutamatergic. The
  three are sub-elements in the source's sense, because the local GABAergic cells inhibit the dopamine
  cells and are the target of the disinhibitory ventral-pallidum input — so **an internal inhibitory
  edge exists inside this structure and the source records it as described but not typed.**
- **Inputs.**
  - **← nucleus accumbens / ventral striatum** (`09_basal_ganglia`) — payload **owed** at the source.
    Fan-in: to derive. **Consumer-only, confirmed 2026-08-14 by reading that file directly.** The
    accumbens is a **sub-element** of its bundled basal-ganglia entry, **whose every output leaves from
    the internal globus pallidus or the substantia nigra pars reticulata**, and no line there sends the
    accumbens anywhere. **The absence is structural rather than accidental**: while that entry's
    Outputs slot is stated at the level of the bundle's two output nuclei, a sub-element output edge
    has nowhere to be written. **That is the bundling question that file records in its own head,
    arriving on a specific wire.** **Owed at the source, and at that file.**
  - **← ventral pallidum** (`09_basal_ganglia`) — **disinhibition of the dopamine cells**, the
    ventral-pallidum → ventral-tegmental-area → accumbens motivational limb, terminating on the local
    GABAergic population. Fan-in: to derive. **Two-ended and confirmed 2026-08-14, and this end
    discharged a mark there**: that line read *the consumer declares no such edge*. **It does**, and it
    is this one. **This end is also the more specific of the two** — the producer names no termination,
    and the local GABAergic population named here is a sub-element of this structure, **so the word
    *disinhibition* is checkable at this end and not at that one.**
  - **← prefrontal cortex** (`11_frontal_lobe`) — payload **owed**. Fan-in: to derive.
    **Checked 2026-08-14 and it closes as a negative: no structure in that file declares an output to
    this one, or to any structure in this section, under any name.** Its nine entries were read for it.
    **See the section-level block below**, which records the same negative for the three other ascending
    class endpoints here and states it once. **This endpoint names a class and
    not a structure** — five prefrontal entries in file 11 are candidate producers and none is
    confirmed. Inherited from the source, which marks it owed; not repaired here.
  - **← lateral hypothalamus** (`14_brainstem_midbrain_hypothalamus`) — payload **owed**. Fan-in: to
    derive. **Checked 2026-08-14 and neither end names the other precisely.** That file declares
    `→ brainstem tegmentum` as a class and names this entry among the far ends that exist; **this line
    names a hypothalamic sub-element and that entry is itself a bundle of eleven sub-nuclei.** **So a
    sub-element endpoint faces a class endpoint** and the edge is neither dangling nor two-ended.
    **Owed at the source at both ends.**
  - **← brainstem laterodorsal and pedunculopontine tegmental nuclei** — a **cholinergic and
    glutamatergic drive** onto the dopamine cells; payload otherwise **owed**. Fan-in: to derive.
    **Checked 2026-08-14 and the far end exists as a sub-element, not as an entry.**
    `14_brainstem_midbrain_hypothalamus` has no entry under either name; **both are named inside its
    reticular formation entry**, which lists them among the sub-elements that **do** have real borders
    and gives them rank 2, `(cell class, N)`. **So this is a sub-element endpoint and not a dangling
    one** — the distinction the edge index warns about, arriving in a real case. **The producer end is
    still undeclared**: that entry's Outputs name the intralaminar thalamus, cortex, spinal cord and
    the cranial-nerve motor nuclei, **and no dopaminergic target.** **Owed at the source**, and the
    repair is at the sub-element rather than at the structure.
  - **← lateral habenula, via the rostromedial tegmental nucleus** — a **negative / aversive value
    signal**: a negative reward-prediction error, the opponent brake on this structure's dopamine
    output. The rostromedial tegmental nucleus is the **GABAergic inverting relay** that turns the
    habenula's bad-outcome signal into inhibition here. Fan-in: to derive. Declared at file 17 and
    named again at file 20. **The relay is a structure on this edge and it has no entry in this file**;
    the source's own inventory records that it gained one in `14_brainstem_midbrain_hypothalamus`.
    **That file was read beside this one on 2026-08-14 and the entry is there.** It declares
    `→ ventral tegmental area, synapsing on its dopamine neurons` — **inhibition, a GABAergic brake,
    the sign-inverted image of the habenular input, no content** — and marks it two-ended against this
    file. **So this edge is two-ended and the relay on it is a described structure with a count basis,
    a shape and its own inputs**, not an unrepresented waypoint. **What remains owed is unchanged**:
    the relay is still not an entry *here*, and whether this file should carry one or defer to that
    one is a source decision. **The payload agrees at both ends and neither end derives the fan-in.**
  - **← amygdala** — a **sustained threat / defence state**, a persistent aversive-state signal and
    not a discrete stimulus; payload otherwise **owed**. Fan-in: to derive.
    **This endpoint is misnamed, found 2026-08-13 by holding `08_medial_temporal_lobe` open beside
    this file.** That file's **amygdala** entry declares sixteen outputs and this structure is not
    among them. Its **bed nucleus of the stria terminalis** entry declares `→ ventral tegmental area`
    — and had marked it *the consumer declares no such edge, owed at file 13*. **Each file recorded
    the other as missing the edge. Both were wrong, and the cause is that they named the producer
    differently.** **A name mismatch produces a false negative at both ends at once and neither end
    can see it alone**; this is the first instance the map has found.
    **This entry's own payload is what identifies the producer.** *Sustained*, *persistent* and *not a
    discrete stimulus* is the distinction that separates the bed nucleus from the central amygdala in
    the far file, where the bed nucleus is the sustained arm and the central nucleus the phasic one.
    **The payload was derived here from this file's source and it describes that structure, not the
    one this line names.**
    **Owed at the source: rename this endpoint to the bed nucleus of the stria terminalis**, or state
    that the projection arises from both and that this line is one edge at a coarse grain. **Not
    repaired here** — the endpoint name is inherited and the repair is the source's.
- **Outputs.**
  - **→ nucleus accumbens / ventral striatum** (the mesolimbic limb) — dopamine carrying a
    **reward-prediction error**, alongside the substantia nigra pars compacta; payload otherwise
    **owed**. Fan-out: to derive. **Two-ended and confirmed 2026-08-14** (`09_basal_ganglia`), payload
    owed at both ends, and both ends record the same split of the two dopamine systems by loop — pars
    compacta to the motor loop, this structure to the reward / limbic one.
  - **→ the striatum's dopamine-modulated projection neurons** (`09_basal_ganglia`) — the same
    reward-prediction error as a **three-factor plasticity signal**, gating cortico-striatal synaptic
    change on the direct and indirect pathways. Fan-out: to derive. **Producer-only, checked
    2026-08-14: that file declares no second dopaminergic limb from this structure.** **But the far end
    already carries the partition this line terminates on** — the direct and indirect pathways are
    internal edges there and the **D1- and D2-expressing medium spiny neurons are named sub-elements**
    that project to different targets. **So this is an edge with a landing site and no declaration**,
    which is a different state from an endpoint with no far end. **Owed at the source, and the far end
    has recorded the debt from its side.** **Whether this and the mesolimbic edge above are one
    projection at two grains or two distinct targets is owed at the source**, and the far end cannot
    settle it either: its own nigrostriatal line makes the same claim for the pars compacta and marks
    the opposite signs on the two cell classes owed.
  - **→ prefrontal cortex** (`11_frontal_lobe`) (the mesocortical limb) — dopamine **setting the
    gain** on prefrontal working-memory and rule representations; payload otherwise **owed**. Fan-out:
    to derive. **Two-ended at one member and confirmed 2026-08-14**, the dorsolateral entry declaring
    `← the ventral tegmental area, the mesocortical projection` — **untyped there, so this end carries
    the payload alone.**
    **The *which of the five* question is now answered in the negative and stays open in the
    positive.** All nine entries of that file were read: **the dorsolateral entry is the only one that
    declares this input.** The ventrolateral, orbitofrontal / ventromedial, cingulate and frontopolar
    entries declare no dopaminergic input under any name. **So either the class has exactly one member
    and should be renamed, or four consumers are missing the limb** — and the far end's own gain claim
    bears on it, since that file types the mediodorsal thalamic input to several of those entries as
    modulatory amplification and would have a second gain source here if the limb were accepted.
    **Owed at the source.**
  - **→ amygdala** (`08_medial_temporal_lobe`) — payload **owed**. Fan-out: to derive. **Two-ended
    and confirmed 2026-08-13; payload owed at both ends.**
  - **→ hippocampus** (`08_medial_temporal_lobe`) — dopamine as a **novelty / salience signal gating
    what is encoded**; payload otherwise **owed**. Fan-out: to derive. **Two-ended and confirmed
    2026-08-13, and this end is the typed one** — the consumer carried the edge untyped and has taken
    this wording.
  - **Not distinguished on any edge above:** some of this structure's outputs are **not
    dopaminergic** — a mesolimbic GABAergic projection to the accumbens is reported at the source and
    no output edge separates it. Owed at the source.
- **Sizing.** Basis: **not declared at the source — to derive.** Neurons **order 10⁵**, human absolute
  count soft (stereology in rat and macaque, not cleanly in human), and smaller than the substantia
  nigra pars compacta's ~400–500k per side. Every fan-in on every edge reads unknown at the source, so
  the store is bounded rather than computed: **≤ 16 bits per neuron → ≤ 0.20 MB at 10⁵ neurons.**
  All three cell classes are spiking neurons and all three are threshold gates, so the whole count
  carries a threshold; none of the §6 exemptions applies here.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)**, cell classes **dopaminergic /
  GABAergic / glutamatergic**. **This is one of the few structures whose count partitions to its
  sub-elements**, because the source gives the partition as fractions rather than leaving it open: at
  10⁵ neurons the axis is ~65,000 / ~30,000 / ~5,000. The partition is a proportion applied to an
  order-of-magnitude total, so it is exact in shape and soft in extent. No map axis is recorded, so
  there is no H × W and none is invented.
- **Edge latency.** All twelve edges **to derive.**
- **Invariant conformance.** Co-instantiation: the structure is inside at least two loops, both
  closing outside this file — accumbens and ventral pallidum return to it (file 9), and the habenular
  brake reaches it through a relay (files 17, 14). Neither can be checked here. Per-edge latency:
  satisfied, all to derive; every edge is a conventional projection and none is in the volume-
  transmission, optical, endocrine or mechanical classes.
- **Justification (biological).** The payload on the dopamine edges is a **reward-prediction error** —
  a scalar teaching signal, the difference between reward received and reward expected — and
  explicitly **not a content signal**: a consumer that reads identity or category off this wire has
  misread it. That is a structural claim and not a functional gloss, because it says what the edge
  cannot be used for. The opponent input from the habenula is the same quantity with the sign
  inverted, which is why the inversion has a **dedicated relay structure** rather than being done at
  the receiving cell.

## Locus coeruleus

- **Function → structure.** The **sole source of cortical noradrenaline (norepinephrine)** — arousal,
  vigilance, attention and the sleep–wake cycle. A tiny nucleus with among the widest projections in
  the brain, and pigmented with neuromelanin as the substantia nigra pars compacta is. Its internal
  organisation is **described and not resolved**: dorsal and ventral tiers with partly different
  projection targets, and a modular output architecture reported in rodent, with **no sub-element set
  and no internal edges** stated. A single neuron's axon **branches to reach multiple non-adjacent
  cortical and subcortical territories**, which is the anatomical basis of the diffuse projection and
  which no branch count is recorded for.
- **Inputs.**
  - **← nucleus paragigantocellularis of the medulla** — the **principal excitatory drive setting
    this structure's firing mode**; payload otherwise **owed**. Fan-in: to derive.
    **Checked 2026-08-14 and no entry or sub-element in `14_brainstem_midbrain_hypothalamus` carries
    this name.** **A candidate producer is there and is not asserted to be the same structure**: its
    rostral ventrolateral medulla entry declares `→ locus coeruleus, raphe nuclei` and the dorsal vagal
    complex, and adds that **the bulbospinal neurons have brainstem collaterals, so these are not
    necessarily separate populations.** **The two names sit in the same medullary territory and the
    identification would be a content claim, so it is not made here.** **Owed at the source: establish
    whether this nucleus is that entry, a sub-element of it, or a third thing** — and note that if it
    is the same structure, the far end reaches this nucleus **and** the raphe on one line while this
    file's two entries name different sources.
  - **← prefrontal cortex** — payload **owed**. Fan-in: to derive. **This endpoint names a class**;
    the descending cortical control is attributed to prefrontal cortex with no named entry. Inherited.
  - **← hypothalamus** (`14_brainstem_midbrain_hypothalamus`) — payload **owed**. Fan-in: to derive.
    **Checked 2026-08-14 and there are two candidate producers there, not one.** Its hypothalamus entry
    declares `→ brainstem tegmentum`, a class naming this entry among its existing far ends; its
    rostral ventrolateral medulla entry separately declares `→ locus coeruleus, raphe nuclei` **by
    name**, which is the C1 adrenergic limb this line was pointing at. **The named one is not the
    hypothalamus**, so this line's endpoint and the edge that actually reaches it by name are two
    different sources. **Owed at the source: split this line, or establish that the hypothalamic limb
    is the same projection under a different origin.**
  - **← amygdala, central nucleus** (`08_medial_temporal_lobe`) — a **threat / salience signal**, the
    amygdala recruiting global arousal in proportion to detected threat; payload otherwise **owed**.
    Fan-in: to derive. Reciprocal with the output to the amygdala below. **Two-ended and confirmed
    2026-08-13, and this end discharged a mark there**: the producer's line read *untyped there*, and
    this line types it and names the producing sub-element, which the producer's own line does not.
  - **← ventrolateral periaqueductal grey** (`14_brainstem_midbrain_hypothalamus`) — the
    periaqueductal limb of **descending noradrenergic analgesia**; payload otherwise **owed**. Fan-in:
    to derive. **Two-ended and confirmed 2026-08-14**, and **both ends name the ventrolateral column**
    rather than the structure as a whole — that file gives the periaqueductal grey a four-column shape
    axis, so the attribution is to a sub-element it carries. **Payload owed at both ends.**
- **Outputs.**
  - **→ the entire cerebral cortex** — the **global gain / arousal signal and a phasic salience
    transient; no stimulus content**. Fan-out: to derive. **This endpoint names a class and the cortex
    is not one structure** — the class covers every cortical entry in the map. It is **the
    load-bearing class in this entry** and it is inherited: file 1's visual entries name a brainstem
    noradrenergic input as a class from their side too, so both ends are untyped.
  - **→ hippocampus** (`08_medial_temporal_lobe`) — the gain and salience signal; payload otherwise
    **owed**. Fan-out: to derive. **Two-ended and confirmed 2026-08-13, and this line discharged a
    mark there**: the consumer had recorded this edge as reaching it *inside the producer's brain-wide
    class*. **It is a named edge here, declared separately from the cortical class above it**, and the
    distinction matters because the class is unresolved and this edge is not.
  - **→ amygdala** (`08_medial_temporal_lobe`) — the same gain and salience signal; payload otherwise
    **owed**. Fan-out: to derive. Reciprocal with the central-nucleus input above. **Two-ended and
    confirmed 2026-08-13, and this pair discharged a mark there**: the consumer read *reciprocal, one
    limb written there*. **Both limbs are written here.** **The pair is complete at both ends**, which
    of the thirteen edges shared with that file is true of this one and its partner alone.
    - **→ cerebellar cortex** (`10_cerebellum`) — noradrenaline setting global gain; payload otherwise
    **owed**. Fan-out: to derive. **Two-ended**, and this line discharged a mark there: **that entry
    had recorded this edge as arriving inside the `→ the entire cerebral cortex` class above**, where
    it is a named edge here, declared separately. **That is the second consumer of which this was
    true** — the hippocampal edge two lines up carried the same misreading — **so the pattern is the
    class endpoint's, not either consumer's**: a structure named on its own line beside a brain-wide
    class is read at the far end as a member of the class.
  - **→ thalamus** (`12_thalamus`) — the gain and arousal signal, no content. Fan-out: to derive.
    **This endpoint names a class.** **Checked 2026-08-14 and it closes as a negative: not one entry in
    that section declares a noradrenergic or locus-coeruleus input under any name.** Its eight
    structures were read for it — mediodorsal, pulvinar, posterior / ventromedial-posterior, ventral
    anterior / ventral lateral, anterior, intralaminar and reticular nuclei, and the zona incerta — and
    **the only neuromodulatory inputs written anywhere in that file are two basal-forebrain limbs at
    the reticular nucleus.** **So this class has no consumer end at all**, which is a different state
    from an unresolved class with candidate members. **Owed at the source, and at that file rather than
    here**: accept the input at the nuclei that receive it, or establish that the description does not
    carry it. The far end now records the same negative from its side.
  - **→ spinal cord** — noradrenaline, part of **descending modulation of the dorsal horn**; payload
    otherwise **owed**. Fan-out: to derive. Far end in file 16, which declares raphe and hypothalamic
    descending modulation and was not confirmed to name this structure.
  - **→ further subcortical targets beyond those named** — the gain and arousal signal. Fan-out: to
    derive. **This endpoint names a class** and is the recorded remainder of the brain-wide reach.
- **Sizing.** Basis: **per side.** **~50,000 neurons per side** — the one firm human figure in this
  section — with a reported human range of ~22,000–51,000 pigmented neurons per side. Every fan-in
  reads unknown, so **≤ 16 bits per neuron → ≤ 0.10 MB per side**, and **≤ 0.044–0.102 MB** across the
  reported range. **This is the smallest parameter store of any computing structure anywhere in the
  architecture so far**, and it is the sole source of cortical noradrenaline.
- **Shape.** **Non-laminated nucleus**, rank 2: **(cell class, N)** with **N ≈ 50,000** and the **cell
  class axis to derive** — the dorsal and ventral tiers are described as having partly different
  targets, which is the source's own test for sub-element status, but no set is named and no partition
  of the count exists. So this structure's extent is known and its first axis is not, which is the
  reverse of the usual case in the map. Recording it as rank 1 would assert that the tiers are not
  sub-elements, which the description contradicts.
- **Edge latency.** All twelve edges **to derive.**
- **Invariant conformance.** Co-instantiation: the amygdalar pair is reciprocal and closes in file 8;
  the descending cortical control closes through an unnamed prefrontal producer and therefore cannot
  be closed at all until that class resolves. Per-edge latency: satisfied, all to derive. **An
  arousal source that came up late would leave every structure it gains running at an undefined gain,
  which is the strongest form of the co-instantiation argument in the map.**
- **Justification (biological).** The payload is stated at the source as **a scalar that multiplies
  the effective strength of whatever other edges are active**, plus a phasic salience transient, and
  explicitly not stimulus content. **Multiplication of another edge's strength is not a count of
  active inputs crossing a threshold**, so this is a described computation the §6 sizing model has no
  term for — the same shape of finding as the outer retina's sign inversion, and it is recorded, not
  flattened. *(The multiplicative reading is the source's own wording and is Class 1; that it falls
  outside the threshold-gate model is Claude's reading and is the finding at §6's own invitation.)*

## Raphe nuclei

- **Function → structure.** The brainstem **serotonin (5-hydroxytryptamine)** source — mood, arousal
  state, patience or time horizon, and broad modulation of sensory and limbic processing. Structurally
  it is **not one nucleus**: the **dorsal raphe**, the **median raphe** and the **caudal raphe** are
  distinct sub-elements with **different projection targets** — dorsal and median to the forebrain,
  caudal to the spinal cord — which is the source's own test for sub-element status. **No internal
  edge between them is described and it is not clear one exists**; they may be parallel sources rather
  than a chain.
- **Inputs.**
  - **← prefrontal cortex** — payload **owed**. Fan-in: to derive. **This endpoint names a class.**
    Inherited.
  - **← hypothalamus** (`14_brainstem_midbrain_hypothalamus`) — payload **owed**. Fan-in: to derive.
    **Checked 2026-08-14.** That file's hypothalamus entry declares `→ brainstem tegmentum` and marks
    it a class, **naming this file's locus coeruleus, raphe and ventral tegmental entries as the far
    ends that exist** — so **the class is resolvable and unresolved, and this entry is one of the three
    members it stands for.** **Neither end names the other structure**: this line names a bundle and
    that line names a class. **Owed at the source: name the members there, or name the hypothalamic
    sub-element here.** The rostral ventrolateral medulla entry in that file separately declares
    `→ locus coeruleus, raphe nuclei`, which is a **different and named** producer for this input.
  - **← lateral habenula** — a **negative / aversive value signal**, the same bad-outcome habenular
    output that brakes dopamine, here modulating serotonin; payload otherwise **owed**. Fan-in: to
    derive. Declared at file 17.
  - **← amygdala** (`08_medial_temporal_lobe`) — payload **owed**. Fan-in: to derive. **Two-ended and
    confirmed 2026-08-13**, the producer declaring `→ raphe nuclei` from the central nucleus. **Payload
    owed at both ends**, so what the two ends agree on is that neither can say what is on the wire.
- **Outputs.**
  - **→ the cerebral cortex** — the serotonergic modulatory state signal, no stimulus content.
    Fan-out: to derive. **This endpoint names a class** covering every cortical entry; files 1 and 4
    name a serotonergic input from their side and their ends are unresolved too. Inherited.
  - **→ striatum** — the same modulatory signal. Fan-out: to derive. **This endpoint names a class**;
    file 9 was not confirmed to declare a raphe input. Inherited.
  - **→ the limbic system** (`08_medial_temporal_lobe` in part) — the modulatory signal. Fan-out: to
    derive. **This endpoint names a class and does not resolve.** Inherited. **Checked 2026-08-13 and
    the class is confirmed to have at least one real far end**: that file's hippocampal formation
    declares `← raphe nuclei`, and marks it *the producer's class covers this structure without naming
    it — owed there*. **Both ends agree the debt is here, and both agree it is inherited**, so neither
    rung may repair it: §2 forbids repairing an inherited class here, and the far end declines to
    write a name this end has not given. **Owed at the source, and it is now a debt two files have
    independently recorded rather than one.**
  - **→ spinal dorsal horn and intermediolateral cell column**, from the **caudal raphe** —
    neuromodulatory state, no stimulus content; part of **descending pain modulation**, the analgesia
    limb. Fan-out: to derive. Declared at file 16. **This is the one output edge in the entry that
    leaves from a named sub-element**, and the sub-element it leaves from is the one the forebrain
    outputs do not use.
  - **→ further forebrain and limbic targets beyond those named** — the modulatory signal. Fan-out: to
    derive. **This endpoint names a class** and is the recorded remainder of the brain-wide reach.
- **Sizing.** Basis: **whole (midline).** The one count is for a **sub-element and not the
  structure**: the **dorsal raphe**, the largest of the three, holds **~235,000 neurons of which
  ~165,000 are serotonergic**. The median and caudal raphe add the rest and the whole serotonergic
  system is order **10⁵–10⁶**. Every fan-in reads unknown, so **≤ 16 bits per neuron → ≤ 0.47 MB for
  the dorsal raphe**, of which **≤ 0.33 MB** is its serotonergic population. **Structure total: to
  derive**, two of three sub-elements uncounted.
  **A cross-check the source supports and which closes.** The dorsal raphe's serotonergic population
  is recorded as about a third of the brain's serotonergic neurons, giving ~495,000 for the whole
  serotonergic system — which sits inside the stated order of 10⁵–10⁶ and is **≤ 0.99 MB** at the
  16-bit bound. Two independently recorded statements about the same quantity agree.
  **A per-side figure is not derivable.** This is a midline structure reported whole, and halving it
  would assert a symmetry the source does not state.
- **Shape.** **Non-laminated nucleus**, and it needs **rank 3: (division, cell class, N)** — divisions
  **dorsal / median / caudal**, cell classes **serotonergic** and **non-serotonergic** (the dorsal
  raphe's ~235,000 against ~165,000 leaves ~70,000 that are not serotonergic and are not otherwise
  described). **The design file's shape class 3 is rank 2 and does not hold this**, because the
  topographic division and the transmitter division are different axes that both carry edges. Extents:
  dorsal ~235,000, median and caudal **to derive**. No map axis is recorded. *(The rank-3 extension of
  a non-laminated nucleus is Claude's reading, offered to be checked. The three divisions and their
  differing targets are Class 1 from the source.)*
- **Edge latency.** All nine edges **to derive.**
- **Invariant conformance.** Co-instantiation: the habenular and amygdalar inputs close in files 17
  and 8; three of the five outputs terminate on classes and therefore close nowhere, so conformance
  cannot be asserted for them. Per-edge latency: satisfied, all to derive.
- **Justification (biological).** The functional reading — **patience, or time horizon** — is marked at
  the source as **a candidate interpretation and not a decoded format**, and the architecture carries
  that mark rather than promoting it. The structural fact that does carry is the division of labour by
  sub-element: the forebrain outputs leave from the rostral pair and the spinal output from the caudal
  one, so **the divisions are not a finer description of one source, they are three sources with three
  destinations**, and an architecture that collapsed them would put the analgesia limb and the cortical
  modulation on the same wire.

## Basal forebrain

- **Function → structure.** The main source of **cortical acetylcholine** — attention, arousal,
  cortical plasticity and learning gain, and memory encoding — with the **medial septum** driving
  hippocampal theta. **The name is narrower than the structure, and the source says so.** It is
  really **three co-located projection systems distinguished by transmitter** — **cholinergic**,
  **parvalbumin-expressing GABAergic**, and **glutamatergic** — crossed with a **topographic division**
  into the **medial septum** (to the hippocampus), the **diagonal band**, and the **nucleus basalis of
  Meynert** (to the neocortex). **Both divisions are sub-elements**, because the output edges below
  already leave from different ones. The GABAergic and glutamatergic populations together are reported
  to be **the majority of the projections**, so the population the structure is named for is not the
  bulk of its output. **Whether internal edges exist between the three transmitter systems is not
  described and they may be parallel systems.**
- **Inputs.**
  - **← limbic and prefrontal cortex** — payload **owed**. Fan-in: to derive. **This endpoint names a
    class** — descending cortical control, unresolved across files 8, 11 and 17. Inherited.
    **Checked against `08_medial_temporal_lobe` on 2026-08-13, and the class is carrying a specific
    named edge that this entry does not declare.** That file's hippocampal formation declares
    `→ basal forebrain` **and** `→ septum`, via the **pre-commissural fornix**, and names it **the
    return limb of the theta loop** — the path back for the pacing signal this entry sends out on
    three edges. **This entry declares no input from it.**
    **So the theta loop is closed at the far end and open here**, and the septal half is the worse of
    the two: **the medial septum is a named division of this structure, it is the origin of all three
    outgoing septo-hippocampal edges, and it declares no input at all.** A structure that paces
    another and declares nothing coming back is not a loop at this rung. **Owed at the source: resolve
    the class, or write the return limb by name.**
  - **← amygdala, central nucleus** (`08_medial_temporal_lobe`) — payload **owed**. Fan-in: to derive.
    One named member of what the class above was standing in for. **Two-ended and confirmed
    2026-08-13, and this line discharged a mark there**: the consumer read *class covers it without
    naming it — owed there*. **This entry carries both the class and the named edge**, and the
    producer saw only the class. **Payload owed at both ends and nothing else is.**
  - **← hypothalamus** — payload **owed**. Fan-in: to derive. Declared at file 14, naming a
    hypothalamic and brainstem projection to the basal forebrain and the substantia innominata.
  - **← brainstem** — payload **owed**. Fan-in: to derive. **This endpoint names a class**; the
    ascending brainstem arousal drive is attributed to "brainstem" with no named entry. Inherited.
    **One named member was located 2026-08-14 and the class is narrowed, not closed.**
    `14_brainstem_midbrain_hypothalamus`'s lateral parabrachial entry declares
    `→ basal forebrain / nucleus basalis of Meynert, to the substantia innominata` **by name**, and
    records it as *two-ended against file 13, whose basal forebrain entry declares a brainstem input.*
    **That reading is generous and is corrected here rather than there**: this end declares a class
    that covers that producer without naming it, which is **a class with a located member** and not a
    two-ended edge. **The two states are not the same and this file has been careful to keep them
    apart elsewhere.** **Owed at the source: name the lateral parabrachial nucleus on this line.**
- **Outputs.**
  - **→ the entire cerebral cortex**, from the **nucleus basalis of Meynert** — acetylcholine as a
    **cortical plasticity / learning-gain and attention signal, not stimulus content**. Fan-out: to
    derive. **This endpoint names a class** covering every cortical entry and is the load-bearing
    class in the entry; files 1 and 3 name a cholinergic input from their side, unresolved. Inherited.
  - **→ hippocampus** (`08_medial_temporal_lobe`), from the **medial septum, cholinergic cells**, via
    the **fornix, pre-commissural limb** — a **tonic gain / arousal-state signal**, delivered largely
    by **volume transmission**. It biases hippocampal state and theta amplitude and gates the
    theta-versus-ripple
    regime, and it **does not pace theta**. Fan-out: to derive. **Two-ended and confirmed 2026-08-13**,
    the consumer carrying the same 93% varicosity figure, the same volume-transmission mechanism and
    the same negative — that it gates the theta-versus-ripple regime and does not set theta frequency.
    **This is the
    volume-transmission edge of the invariants section above.**
  - **→ hippocampal inhibitory interneurons**, from the **medial septum, parvalbumin-expressing
    GABAergic pacemaker cells**, via the **fornix** — the **theta timing reference**, the phase of a
    **4–12 Hz** oscillation whose tick is an **intrinsic hyperpolarisation-activated
    cyclic-nucleotide-gated channel current** in those cells. GABA is the wire and the synchronising
    coupling, not the oscillator. Fan-out: to derive. **Two-ended and confirmed 2026-08-13**
    (`08_medial_temporal_lobe`), which names the same sub-element, the same interneuron target — in
    CA1, CA3 and the dentate gyrus, finer than this end — and the same payload, and which records the
    rhythm's period as **83 to 250 ms**, a figure this entry does not carry.
    **The three septo-hippocampal edges disagree with the far end about which fornix limb carries
    which, and neither end noticed.** This entry routes the **cholinergic** edge via the
    **pre-commissural limb** and leaves this one and the glutamatergic one on the fornix unqualified;
    that file routes the **parvalbumin** edge via the **pre-commissural** fornix and leaves the other
    two unqualified. **Each end asserts the finer route on one edge, and they are different edges.**
    Not a contradiction — all three may run the same limb — but **no edge carries the finer route at
    both ends**. **Owed at the source: which limb carries which.**
  - **→ hippocampus** (`08_medial_temporal_lobe`), from the **medial septum, glutamatergic cells**,
    via the **fornix** — a **tonic excitatory gate**, the depolarising drive that toggles the
    pacemakers between theta and non-theta states; **not content and not a per-cycle signal**.
    Fan-out: to derive. **Two-ended and confirmed 2026-08-13**, both ends typed and in agreement.
  - **→ cortical inhibitory interneurons**, from the **parvalbumin-expressing GABAergic** population —
    an inhibitory signal onto inhibitory targets whose **net cortical effect is activation**: it
    drives and entrains cortical **gamma-band** oscillations, probably by synchronising cortical
    inhibitory neurons, targeting both parvalbumin- and somatostatin-expressing cortical interneurons.
    Fan-out: to derive.
  - **→ thalamic reticular nucleus**, from the same **parvalbumin GABAergic** population — inhibition
    of the thalamic gate and therefore **disinhibition of the relay nuclei behind it**, a tonic
    inhibitory hold transiently released. Fan-out: to derive. **Two-ended and confirmed 2026-08-14**
    (`12_thalamus`), **and it is the
    strongest agreement either file records.** Both ends declare the edge from this named population,
    both type it in the same double-negative terms, **and both independently carry the same
    disconfirming experiment.** **A negative result is recorded at the consumer and is carried:**
    driving these fibres inside the reticular nucleus
    enhanced cortical power at ~10 Hz, spindle frequency, not gamma — so **this edge is not the
    carrier of the gamma effect** and the direct cortical edge above is.
  - **→ thalamic reticular nucleus** (`12_thalamus`), from the **cholinergic** population — payload
    **owed**; driving it **promotes sleep, opposite in sign** to the edge above. Fan-out: to derive.
    **Two-ended and confirmed 2026-08-14**, the consumer recording the same opposite sign from the
    same named population and reaching the same conclusion about the transmitter axis independently.
    **Two edges from one structure to one target with opposite behavioural consequences**, separated
    only by which transmitter population they leave from — which is what makes the transmitter axis
    load-bearing rather than descriptive.
  - **→ further subcortical targets beyond the thalamic reticular nucleus** — the relevant
    population's signal. Fan-out: to derive. **This endpoint names a class** and is the recorded
    remainder.
- **Sizing.** Basis: **not declared at the source — to derive.** Neurons **order 10⁵ cholinergic**,
  and that figure is **the cholinergic sub-element only**. The GABAergic and glutamatergic
  populations — reported to be the **majority** of the projections — **have no count at all**. Every
  fan-in reads unknown, so **≤ 16 bits per neuron → ≤ 0.20 MB for the cholinergic population**.
  **Structure total: to derive, and the uncounted part is the larger part.** This is the one place in
  the section where the missing count is known to exceed the recorded one.
- **Shape.** **Non-laminated nucleus**, **rank 3: (topographic division, cell class, N)** — divisions
  **medial septum / diagonal band / nucleus basalis of Meynert**, cell classes **cholinergic /
  parvalbumin-expressing GABAergic / glutamatergic**, both axes named by the source and **neither
  partitioned**. Extents: cholinergic order 10⁵ across all divisions, everything else **to derive**.
  **The two axes are crossed and not nested, and the edges prove it**: three edges leave the medial
  septum on three different transmitters, and two edges leave the parvalbumin population for two
  different targets. A rank-2 shape on either axis alone cannot address the eight output edges above.
  *(The rank-3 crossed shape is Claude's reading; that both divisions are sub-elements and that the
  edges leave from different ones is Class 1 from the source.)*
- **Edge latency.** All twelve edges **to derive**, and **the cholinergic hippocampal edge is not a
  conduction-plus-synapse latency** — see the invariants above.
- **Invariant conformance.** Co-instantiation: the septo-hippocampal triple and the two reticular
  edges close in files 8 and 12; the cortical class endpoint closes nowhere. Per-edge latency:
  satisfied, all to derive, with one edge in a class the invariant's justification does not cover.
- **Justification (biological).** The three septo-hippocampal edges are the section's clearest
  demonstration that **a transmitter is not a label on a projection, it is what distinguishes one
  projection from another**. One anatomical route — the medial septum through the fornix to the
  hippocampus — carries **three different payloads**: a gain envelope by diffusion, a phase reference
  from an intrinsic membrane oscillation, and a tonic gate that switches the oscillator's regime. The
  source records that each end of that route had previously named one limb and mistaken it for the
  whole. **Collapsing them would put a clock, a gain and a switch on one wire.**

---

## Every ascending input this section declares from prefrontal cortex has no producer there

**Four class endpoints, one negative, checked 2026-08-14 by reading all nine entries of
`11_frontal_lobe`.** The ventral tegmental area declares `← prefrontal cortex`; the locus coeruleus
declares `← prefrontal cortex`; the raphe nuclei declare `← prefrontal cortex`; the basal forebrain
declares `← limbic and prefrontal cortex`. **Not one structure in that file declares an output to any
structure in this section.** Its nine entries' Outputs slots reach cortex, the basal ganglia, the
thalamus, the amygdala, the bed nucleus, the hypothalamus, the temporal pole, the insula and the
corticospinal tract. **No neuromodulatory nucleus is named as a target anywhere in it.**

**The reciprocal direction is not symmetric, and that is what makes this a finding rather than a
tally.** This section's *descending* limbs into that file are declared there: the mesocortical
projection is written at its dorsolateral entry. **So the traffic between the two files is declared at
both ends going down and at one end coming up** — the top-down control arm of every neuromodulatory
loop this section describes exists here and nowhere else.

**That control arm is load-bearing in this section's own terms.** Three of the four structures are
described as receiving cortical drive that selects *when* the modulatory signal is released, and the
release is what each entry's function is about. **A gain signal whose trigger has no declared producer
is a structure with a described function and no described cause.**

**Not written in at the far end, and not withdrawn here.** **Owed at the source**, and the shape of the
repair is the same for all four: **name the prefrontal structures that project here, or establish that
the descriptions do not carry the ascending limb.** *(Class 1 that the endpoints are classes and Class
1 that the far entries declare nothing; the reading that the four constitute one finding rather than
four is Claude's, offered to be checked.)*

---

## Section totals

| structure | basis | neurons | bits/neuron | parameter memory |
|---|---|---|---|---|
| Ventral tegmental area — all cell classes | to derive | order 10⁵ | ≤ 16 | ≤ 0.20 MB |
| — dopaminergic ~65% | to derive | ~65,000 | ≤ 16 | ≤ 0.13 MB |
| — GABAergic ~30% | to derive | ~30,000 | ≤ 16 | ≤ 0.06 MB |
| — glutamatergic ~5% | to derive | ~5,000 | ≤ 16 | ≤ 0.01 MB |
| Locus coeruleus | per side | ~50,000 | ≤ 16 | ≤ 0.10 MB |
| Raphe — dorsal raphe only | whole (midline) | ~235,000 | ≤ 16 | ≤ 0.47 MB |
| Raphe — median and caudal | whole (midline) | to derive | ≤ 16 | to derive |
| Basal forebrain — cholinergic only | to derive | order 10⁵ | ≤ 16 | ≤ 0.20 MB |
| Basal forebrain — GABAergic and glutamatergic | to derive | to derive | ≤ 16 | to derive |
| **stated total** | **mixed** | **~485,000** | | **≤ 0.97 MB** |

**The total is a floor and a loose one.** Three of the four structures are counted only in part, the
uncounted part of the basal forebrain is reported to be the larger part, **every** fan-in in the
section sits at the 16-bit ceiling rather than at a measured value, and state memory and edge storage
are not in this table at all.

**The figure is small, and how small is the finding.** The whole neuromodulatory section, as counted,
requires **under one megabyte** of parameter memory — against **450–525 MB for V1 alone**, a ratio of
about **540 to 1**. The source's own framing of these nuclei is *small size, outsized influence*, and
under the threshold-gate model that phrase comes out as an arithmetic result rather than a
characterisation. **This is a derived requirement recorded as found, and it is not an argument for
anything.** A structure that is cheap to store is not thereby cheap to build, to time, or to connect:
the connection cost of this section is where the size actually lives, because these four structures
project brain-wide and **fan-out is never stored** in this model.

## Two findings this file records and does not repair

**The threshold-gate model has no term for what all four of these structures emit.** The section's
payloads are, in the source's own words, a scalar that **multiplies** the effective strength of other
active edges; a **reward-prediction error** used as a **three-factor plasticity signal** gating
synaptic change; a **tonic gain** delivered by diffusion; and a **phase reference**. A threshold gate
fires when the count of active inputs crosses a stored threshold, and none of those four is a count of
active inputs. Two of them are not even signals in the same sense: a plasticity signal changes what
the receiving structure stores, and a phase reference is a time and not an amount. The design file
already states that the model is answerable to the description and that a structure described as
computing with graded weights is **a finding against the model rather than a structure to flatten**.
**This is that finding, at four structures at once, and it is the whole content of this section.**
*(The payload descriptions are Class 1 from the source. That they fall outside the threshold-gate
model is Claude's reading.)*

**And the reward-prediction-error edges want a learning rule that is not set anywhere on the ladder.**
The design file's memory classes record that a threshold which is never written is a construction cost
and not a memory, and that whether any threshold is ever written is the learning rule, which is not
set. Everywhere else on the map that has been an acceptable deferral. **Here it is not a deferral, it
is the function**: the ventral tegmental area's declared job on its striatal edge is to carry the
teaching signal that gates synaptic change, so a structure whose output has no consumer rule has no
described effect. **The architecture records that the rule is not set. It does not assume one**, and
choosing one is on the list that is surfaced before it is touched.
