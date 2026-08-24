# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-15
---

---

# FILE 13 OF 20 — NEUROMODULATORY SYSTEMS

**What is in this file.** The four diffuse neuromodulatory sources: ventral tegmental area (dopamine), locus coeruleus (noradrenaline), raphe (serotonin), and the basal forebrain cholinergic system. These project almost everywhere, so their edges cross into every other file.

**Size:** 546 lines, ~13.1k tokens / ~51 kB (estimated from bytes, not tokenised; kB = 1024 bytes, truncated). **Entries:** 4. **Edge lines:** 45 — 20 in, 25 out. *(No edge added or removed 2026-08-15; **one endpoint renamed**, which changes no count and changes which file the edge crosses into.)* **Internal structure slots:** 4 of 4. **Pass stamps:** 4 of 4. **Reference keys:** 9, over 12 mentions — 3 of them shared with file 12. *(Before the 2026-07-24 pass: 88 lines, ~10 prose class-lines standing in for edges across three entries, 0 internal-structure slots, 1 partial pass on the basal forebrain — which had already typed its outputs.)*

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**A note on this pass, 2026-07-24.** Before it, three of the four entries carried their Inputs and Outputs as **prose class-lists** — the locus coeruleus Outputs slot was the whole of "brain-wide — the entire cortex, thalamus, hippocampus, cerebellum, and spinal cord." A class-list makes no checkable claim and cannot fail a two-ended diff, which is why this file accumulated a large owed docket while reading as complete: **eight other files had already recorded edits owed at this file**, each naming one of these four nuclei, declaring the payload at its own end, and recording that this end carried it as a class or not at all. The conversion did not discover most of what is marked owed below; it made it visible. **All four entries lacked the Internal-structure slot** that §3 requires of every entry.

**The diffuse-projection problem, stated once here because it governs all four entries.** These nuclei genuinely project brain-wide, so their Outputs slots are the hardest case in the source for the named-region rule (§3: an edge names a region with an entry of its own, never a class). "Brain-wide" is true and is not a typed edge. This pass resolves the output side **to the consumers that declare an input from each nucleus** — those are checkable, two-ended edges — and records the unresolved remainder explicitly as a class endpoint marked **owed**, rather than leaving the whole slot as one prose class-line. The remainder is not deleted, because the brain-wide reach is a real property; it is marked as the research it names. *(File 12's reticular nucleus raised whether a genuinely universal projection can stand as a class endpoint; research on 2026-07-24 found the universal claim there was false and the class had to resolve. No universal claim is relied on here either — every output class carries an explicit owed mark.)*

**A note on the abbreviation pass, 2026-07-27, and it changed no content.** Every abbreviation in the file now carries its full name at the entry that owns it, per §3, and none stands as the only label for anything: **γ-aminobutyric acid (GABA)**, the **hyperpolarisation-activated cyclic-nucleotide-gated (HCN) channel** current, **serotonin (5-hydroxytryptamine, 5-HT)**, the catecholamine cell-group designations **A10** and **A6**, the **C1 adrenergic cell group**, and the **PubMed Central** accession prefix on the citations. No edge, count, payload or owed mark was touched. **One further naming defect of the same class was found and resolved by research, 2026-07-27.** The file wrote the locus coeruleus transmitter as both **norepinephrine** (in the entry heading and Function) and **noradrenaline** (on three output edges), and two strings for one substance defeat a diff exactly as an abbreviation does. There is no chemical or functional distinction between them — they name one molecule, and the split is regional: norepinephrine is the recommended international nonproprietary name and the United States standard, noradrenaline the British approved name and the common international usage. **The tie is broken by the derived vocabulary, which is *not* split.** Both nomenclatures form the adjective as **noradrenergic** and the receptors as **adrenergic** / **adrenoceptors**; there is no "norepinephrinergic", and the A6 cell group's own name in the anatomical nomenclature is a **noradrenergic cell group**. Choosing norepinephrine for the noun therefore leaves the file with two roots for one substance no matter what, because the file already carries *noradrenergic axons*, *noradrenergic input*, *descending noradrenergic analgesia* and the *C1 adrenergic cell group*. **The file now uses noradrenaline, with norepinephrine given once in parentheses at the entry that owns the name**, per §3.

**Entries in this file, with the date each was last worked:**

- **Ventral tegmental area (VTA; catecholamine cell group A10) — mesolimbic / mesocortical dopamine** — pass 2026-08-15 — the `← the amygdala` input **renamed to the bed nucleus of the stria terminalis**: this entry's provenance note named file 8's central nucleus as producer, that entry declares no such output, and the payload quoted here is the bed nucleus entry's own; the edge researched and confirmed in primate with a subdivision topography neither end carries, and a second limb to the substantia nigra pars compacta recorded as owed at file 9 *(prior pass 2026-07-24 — prose Inputs and Outputs converted to typed edges; outputs resolved to five named consumers (files 8, 9, 11) with the input side reconciled against three files that declare edges this entry did not carry; missing Internal structure slot added)*
- **Locus coeruleus (LC; catecholamine cell group A6) — noradrenaline / arousal** — pass 2026-07-24 — the brain-wide Outputs class resolved to five named consumers (files 8, 10) plus a recorded class remainder; the amygdalar input typed from its producer; missing Internal structure slot added
- **Raphe nuclei — serotonin (5-hydroxytryptamine, 5-HT)** — pass 2026-07-24 — the brain-wide Outputs class resolved to named consumers (files 8, 16, 17) plus a recorded class remainder; the internal dorsal/median/caudal division named as sub-elements; missing Internal structure slot added
- **Basal forebrain / nucleus basalis of Meynert — acetylcholine** — pass 2026-07-24 — the medial-septum → hippocampus edge, a two-ended-diff failure against file 8 (acetylcholine vs theta pacing), resolved by research into three transmitter-split outputs (cholinergic tonic-gain by volume transmission; GABAergic parvalbumin theta timing carried by an intrinsic membrane oscillation of the hyperpolarisation-activated cyclic-nucleotide-gated channel current; glutamatergic tonic gate); the amygdalar and hypothalamic inputs typed from their producers; the two thalamic-reticular outputs confirmed two-ended against file 12; missing Internal structure slot added

**Files read beside this one in the 2026-08-15 pass and not modified:** 8 (medial temporal lobe). **Two marks that made a data claim wait on a person's reading were removed** and replaced with the state each line is in; verification of data runs to the literature and stops there.

**Files read for reference in the 2026-07-24 pass and not modified:** 8 (medial temporal lobe), 9 (basal ganglia), 10 (cerebellum), 11 (frontal lobe), 12 (thalamus), 14 (brainstem / midbrain / hypothalamus), 16 (spinal cord), 17 (insula / claustrum / habenula), 18 (white-matter tracts), 20 (loop structure). **Not read, so unchecked:** 1, 2, 3, 4, 5, 6, 7, 15, 19 — several of which (1, 2, 3) name a brainstem neuromodulatory input as a class and hold un-resolved far ends of this file's output edges.

---

# NEUROMODULATORY SYSTEMS (brainstem + basal forebrain)

*Small nuclei, brain-wide reach. Each is a compact cell group whose axons project diffusely
across cortex and subcortex, releasing a single modulator that sets gain, arousal, or a
learning signal rather than relaying specific content — small size, outsized influence (the
"value/arousal wall"). The nigrostriatal dopamine source, the **substantia nigra pars compacta**
(~400–500k dopaminergic neurons per side), is described in the BASAL GANGLIA section; the two
dopamine systems split as pars compacta = motor loop, ventral tegmental area = reward / limbic
loop. Counts here are order-of-magnitude except the locus coeruleus, which has a firm human figure.*

## Ventral tegmental area (VTA; catecholamine cell group A10) — mesolimbic / mesocortical dopamine

- **Function:** the reward and motivation dopamine source — the mesolimbic projection
  (→ nucleus accumbens / ventral striatum) and mesocortical projection (→ prefrontal cortex);
  carries reward-prediction-error signals alongside the substantia nigra pars compacta. Central
  to motivation, reinforcement, and addiction. The payload on its dopamine edges is a
  **reward-prediction error** — a scalar teaching signal, the difference between reward received
  and reward expected — not a content signal; a consumer that reads identity or category off this
  wire has misread it.
- **Inputs:**
  - **← the nucleus accumbens / ventral striatum** — **carries:** payload **owed. Fan-in:**
    unknown. **The far end is the basal-ganglia entry** (file 9); whether it declares this specific
    return edge with a payload was not confirmed this pass. **Owed as a cross-file check at file 9.**
  - **← the ventral pallidum** — **carries:** disinhibition of dopamine — the ventral-pallidum →
    ventral-tegmental-area → accumbens motivational limb. **Fan-in:** unknown. **The producer
    declares it** (file 9) and recorded it **owed at this file** because this entry's Inputs named
    the accumbens, prefrontal cortex, the lateral hypothalamus, the brainstem laterodorsal and
    pedunculopontine tegmental nuclei, and the lateral habenula — **not the ventral pallidum.
    Written now** from the producer's declaration, discharging that owed edit.
  - **← the prefrontal cortex** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint
    names a class.** The five prefrontal entries in file 11 are the candidate producers; none was
    confirmed to declare this return edge this pass. **Owed: resolve to named producers in file 11,
    or withdraw.**
  - **← the lateral hypothalamus** — **carries:** payload **owed. Fan-in:** unknown. **The far end
    is in file 14** (hypothalamus); whether it declares this edge was not confirmed this pass.
    **Owed as a cross-file check at file 14.**
  - **← the brainstem laterodorsal and pedunculopontine tegmental nuclei** — **carries:** payload
    **owed**; a cholinergic and glutamatergic drive onto the dopamine cells. **Fan-in:** unknown.
    **The far end is in file 14**; not confirmed this pass. **Owed as a cross-file check at file 14.**
  - **← the lateral habenula**, via the **rostromedial tegmental nucleus** — **carries:** a
    **negative / aversive value signal** — a negative reward-prediction error, the opponent brake
    on this nucleus's dopamine output; the rostromedial tegmental nucleus is the GABAergic
    (γ-aminobutyric acid, GABA) inverting relay that turns the habenula's "bad-outcome" signal
    into inhibition here. **Fan-in:** unknown. **The producer declares it** (file 17), naming the
    lateral habenula → rostromedial tegmental nucleus → ventral tegmental area /
    substantia nigra pars compacta dopamine-inhibition
    limb, and file 20 names the same limb as the opponent to the mesolimbic loop. **Two-ended.**
    *(The rostromedial tegmental nucleus itself has no entry in any file read — it is named as a
    relay at both file 17 and file 9 and owns no slot. Recorded: this is a §9a "named region with
    no entry" and belongs on that list.)*
  - **← the bed nucleus of the stria terminalis** (extended amygdala) — **carries:** a **sustained
    threat / defence state** — a persistent aversive-state signal, **not a discrete stimulus**.
    **Payload otherwise owed. Fan-in:** unknown. **The producer declares it** (file 8), whose bed
    nucleus entry names this nucleus and carries this payload in these words. **Two-ended.**
    ***The endpoint was renamed on 2026-08-15, and the reason is a false provenance note rather than
    a synonym.*** *This line read* **← the amygdala** *and stated that the edge was written from
    "that file's central-nucleus / defence output". **File 8's amygdala entry declares no output to
    this nucleus.** Its central nucleus declares six — hypothalamus, periaqueductal gray, locus
    coeruleus, lateral parabrachial nucleus, basal forebrain, zona incerta — and this nucleus is not
    among them. **The only entry in file 8 that declares it is the bed nucleus of the stria
    terminalis**, whose payload is the one quoted above, word for word. **So this entry took an edge
    and its payload from one structure and attributed them to a neighbouring one**, and the
    misattribution read back to file 8 as its own far end declaring nothing — that file recorded the
    edge as undeclared here until 2026-08-15.*
    ***Why that is worth more than the correction.*** *This is not two files disagreeing, which the
    two-ended diff catches. **It is one file naming the wrong producer while quoting the right
    payload**, and the diff cannot catch that at all: both ends carry the same words, so they agree.
    **The payload was the evidence, not the name** — *sustained*, *persistent*, *not a discrete
    stimulus* is precisely the distinction the bed nucleus exists to carry and that the central
    amygdala's phasic arm does not. **A provenance note is a claim about another file and is
    checkable against it; nothing in this source was checking them.**
    ***Researched 2026-08-15, and the edge holds in primate with sub-element structure neither end
    carries.*** *(Class 1 — **Fudge & Haber 2001**, *Bed nucleus of the stria terminalis and extended
    amygdala inputs to dopamine subpopulations in primates*, PubMed 11440812. **Primate. Verified
    against the PubMed record, 2026-08-15**; abstract read, full text not opened. The projection is
    topographic and divides by subdivision: the **medial** bed nucleus and its medial sublenticular
    extension send their densest inputs medially among the dopamine cells; the **lateral** bed nucleus
    and its continuation into the sublenticular extended amygdala project across the whole
    mediolateral extent; within the lateral division the **central core** has restricted inputs while
    the **dorsolateral, capsular and juxtacapsular** subdivisions project strongly to the **dorsal
    tier** dopamine neurons, and the **posterior** subdivision together with the central sublenticular
    extended amygdala reaches both the dorsal tier and the **densocellular** group. **Owed at file 8:
    that entry names no subdivisions of the bed nucleus, and this edge leaves from a specific set of
    them.**)*
    ***And the far end is wider than this entry.*** **The study's target is the primate dopamine cell
    population, which spans this nucleus *and* the substantia nigra pars compacta** — the dorsal-tier
    and densocellular groups are not confined here. **The substantia nigra pars compacta is described
    in file 9, and no entry in this source declares a bed-nucleus input to it.** **Owed: write that
    limb at file 9, or establish that the projection is confined to this nucleus.** *(This file's own
    preamble records that the two dopamine systems are split across two files; **a producer that
    reaches both therefore owes two edges, and file 8 currently declares one.**)*
- **Outputs:**
  - **→ the nucleus accumbens / ventral striatum** (the mesolimbic projection) — **carries:**
    dopamine carrying a **reward-prediction error**, alongside the substantia nigra pars compacta.
    **Payload otherwise owed. Fan-out:** unknown. **The consumer declares it and names this
    structure** (file 9). **Two-ended.**
  - **→ the striatum's dopamine-modulated projection neurons**, the reinforcement-learning teaching
    signal onto the direct and indirect pathways — **carries:** the same reward-prediction error, as
    a **three-factor plasticity signal** gating cortico-striatal synaptic change. **Fan-out:**
    unknown. **The consumer declares it** (file 9), which reads "prediction error" on the edge but
    recorded that **this entry declared no such edge** — this nucleus's Outputs named the accumbens,
    prefrontal cortex, the amygdala and the hippocampus, and this second striatal target was not
    among them. **Written now**, discharging file 9's owed cross-file edit. *(Whether this and the
    mesolimbic edge above are one projection described at two grains or two distinct targets is
    owed — file 9 holds both far ends.)*
  - **→ the prefrontal cortex** (the mesocortical projection) — **carries:** payload **owed**;
    dopamine, setting the gain on prefrontal working-memory and rule representations. **Fan-out:**
    unknown. **The consumer declares it** (file 11), which recorded that it had carried this edge
    only as the adjective "dopaminergic modulation" until it named this nucleus as the producer,
    noting this is one of the source's few genuinely famous edges. **Two-ended**, the consumer being
    the dorsolateral prefrontal entry. *(Which of the five prefrontal entries receive this
    projection is owed: file 11's dorsolateral entry declares it; the others were not confirmed.)*
  - **→ the amygdala** — **carries:** payload **owed. Fan-out:** unknown. **The consumer declares
    it** (file 8), written there from this entry's own output declaration. **Two-ended.**
  - **→ the hippocampus** — **carries:** payload **owed**; dopamine, in this entry's terms — a
    novelty / salience signal gating what is encoded. **Fan-out:** unknown. **The consumer declares
    it** (file 8), written there from this entry's output declaration. **Two-ended.**
- **Internal structure and internal data flow:** described but not typed — **owed.** The nucleus is
  a mixed population: **~65% dopaminergic, ~30% GABAergic, ~5% glutamatergic** (Sesack & Grace
  2010). These are sub-elements in the §3 sense — the local GABAergic cells inhibit the dopamine
  cells and are the target of the disinhibitory ventral-pallidum input, so an internal edge
  (GABAergic interneuron → dopaminergic projection neuron, carrying inhibition) exists and is not
  written. **Owed: type the internal inhibitory edge and say whether the glutamatergic cells
  project locally or out.** The dopamine / GABA / glutamate split also means some of this nucleus's
  *outputs* are not dopaminergic — a mesolimbic GABAergic projection to the accumbens is reported —
  which the output edges above do not distinguish. **Owed there too.**
- **Neurons:** composition ~65% dopaminergic, ~30% GABAergic, ~5% glutamatergic (Sesack & Grace
  2010); human absolute count soft — smaller than the substantia nigra pars compacta, order 10⁵
  (stereology exists in rat and macaque, not cleanly in human).
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown — largely unmyelinated, thin dopaminergic axons (a property this system
  shares with the other diffuse modulators), but no g-ratio or white-fraction figure is recorded.
- **Pass:** 2026-08-15 — the amygdalar input endpoint renamed to the bed nucleus of the stria terminalis, on the evidence that file 8's amygdala entry declares no output here while its bed nucleus entry declares this one with this payload; the edge researched in primate and its subdivision topography recorded as owed at file 8; the projection's substantia-nigra-pars-compacta limb recorded as owed at file 9
- **Pass:** 2026-07-24 — prose Inputs and Outputs converted to typed edges; three input edges (ventral pallidum, amygdala) and one output edge (the striatal teaching signal) written from producers/consumers that had recorded them owed at this file; the mesocortical and mesolimbic outputs confirmed two-ended; the rostromedial tegmental nucleus flagged as a named region with no entry; missing Internal structure slot added

## Locus coeruleus (LC; catecholamine cell group A6) — noradrenaline / arousal

- **Function:** the sole source of cortical noradrenaline (norepinephrine) — arousal, vigilance,
  attention,
  and the sleep–wake cycle; sets global gain and signals salience / surprise. A tiny nucleus
  with among the widest projections in the brain. The payload on its edges is **not stimulus
  content**: it is a global gain / arousal signal, a scalar that multiplies the effective strength
  of whatever other edges are active, plus a phasic salience / surprise transient. A consumer
  reading identity off this wire has misread it.
- **Inputs:**
  - **← the nucleus paragigantocellularis of the medulla** — **carries:** payload **owed**; the
    principal excitatory drive setting this nucleus's firing mode. **Fan-in:** unknown. **The far
    end is in file 14** (medullary reticular formation); not confirmed this pass. **Owed as a
    cross-file check at file 14.**
  - **← the prefrontal cortex** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint
    names a class**; the descending cortical control of this nucleus is attributed to prefrontal
    cortex without a named entry. **Owed: resolve to a named producer in file 11, or withdraw.**
  - **← the hypothalamus** — **carries:** payload **owed. Fan-in:** unknown. **The far end is in
    file 14**, whose C1 adrenergic cell group / autonomic outputs name the locus coeruleus and
    raphe together;
    not fully confirmed this pass. **Owed as a cross-file check at file 14.**
  - **← the amygdala**, from the **central nucleus** — **carries:** a threat / salience signal —
    the amygdala recruiting global arousal in proportion to detected threat. **Payload otherwise
    owed. Fan-in:** unknown. **The producer declares it and names this structure** (file 8), and
    recorded it **owed at this file. Written now**, discharging that edit; the pair is reciprocal,
    this nucleus also projecting back to the amygdala (below).
  - **← the ventrolateral periaqueductal gray** — **carries:** payload **owed**; the periaqueductal
    limb of descending noradrenergic analgesia. **Fan-in:** unknown. **The producer names this
    structure** (file 14, naming a ventrolateral-periaqueductal-gray → locus-coeruleus limb).
    **Owed as a cross-file check at file 14 to type it.**
- **Outputs:**
  - **→ the entire cerebral cortex** — **carries:** the global gain / arousal signal and the phasic
    salience transient; no stimulus content. **Fan-out:** unknown. **This endpoint names a class**,
    and the cortex is not one entry — the class covers every cortical entry in the source.
    **Owed: this is the load-bearing class in the entry.** File 1's visual-pathway entries name a
    brainstem noradrenergic input as a class (their end also un-resolved), so the far ends exist but
    are themselves un-typed. **Owed: resolve to named cortical consumers as those files are worked.**
  - **→ the hippocampus** — **carries:** noradrenaline, setting global gain and signalling salience
    or surprise. **Payload otherwise owed. Fan-out:** unknown. **The consumer declares it** (file
    8), which noted this nucleus declares its target as a class that names the hippocampus inside
    it. **Two-ended** now that the consumer's edge is matched here.
  - **→ the amygdala** — **carries:** the same gain / salience signal. **Payload otherwise owed.
    Fan-out:** unknown. **The consumer declares it** (file 8), reciprocal with the central-nucleus
    input above. **Two-ended.**
  - **→ the cerebellar cortex** — **carries:** noradrenaline, setting global gain. **Payload
    otherwise owed. Fan-out:** unknown. **The consumer declares it** (file 10), which recorded that
    it had previously declared only its two afferent systems and that a diffuse modulator arriving
    on the cortex was missing until written from this nucleus's class. **Two-ended.**
  - **→ the thalamus** — **carries:** the gain / arousal signal; no content. **Fan-out:** unknown.
    **This endpoint names a class**; file 12's nuclei were not checked for a declared noradrenergic
    input this pass. **Owed: resolve to named thalamic consumers in file 12.**
  - **→ the spinal cord** — **carries:** noradrenaline; part of descending modulation of the dorsal
    horn. **Payload otherwise owed. Fan-out:** unknown. **The far end is in file 16**, whose dorsal
    horn declares raphe / hypothalamic descending modulation but was not confirmed to name this
    nucleus specifically. **Owed as a cross-file check at file 16.**
  - **→ further subcortical targets beyond those named** — **carries:** the gain / arousal signal.
    **Fan-out:** unknown. **This endpoint names a class** and is the recorded remainder of the
    brain-wide reach. **Owed: resolve or confirm exhausted as files are worked.**
- **Internal structure and internal data flow:** **unknown.** The nucleus has a described
  topographic organisation — dorsal and ventral tiers with partly different projection targets, and
  a modular output architecture reported in rodent — but no sub-element set and no internal edges
  are described in the material read for this entry. **Owed** where the modular organisation has
  been described; **unknown** for the rest.
- **Neurons:** **~50,000 per side** (Benarroch 2018; reported human range ~22,000–51,000 per side,
  pigmented neurons) — one of the smallest yet most widely-projecting nuclei; pigmented
  (neuromelanin), like the substantia nigra pars compacta.
- **Synapses:** unknown.
- **Axons:** unknown — a single neuron's axon branches to reach multiple non-adjacent cortical and
  subcortical territories, the anatomical basis of the diffuse projection, but no branch count is
  recorded.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown — thin, largely unmyelinated noradrenergic axons; no g-ratio recorded.
- **Pass:** 2026-07-24 — the brain-wide Outputs class resolved to five named consumers (hippocampus, amygdala, cerebellar cortex in files 8 and 10, plus cortex and thalamus recorded as owed classes); the central-nucleus amygdalar input typed from its producer; two class remainders recorded rather than left as one prose line; missing Internal structure slot added

## Raphe nuclei — serotonin (5-hydroxytryptamine, 5-HT)

- **Function:** the brainstem serotonin source (dorsal and median raphe most prominent) —
  mood, arousal state, patience / time horizon, and broad modulation of sensory and limbic
  processing. Dorsal / median raphe → forebrain; caudal raphe → spinal cord. The payload is a
  slow modulatory state signal, not stimulus content; the "patience / time horizon" reading is a
  candidate functional interpretation, not a decoded format, and is marked as such.
- **Inputs:**
  - **← the prefrontal cortex** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint
    names a class**; descending cortical control attributed to prefrontal cortex without a named
    entry. **Owed: resolve to a named producer in file 11, or withdraw.**
  - **← the hypothalamus** — **carries:** payload **owed. Fan-in:** unknown. **The far end is in
    file 14**; the C1 adrenergic cell group's autonomic output there names the raphe among its
    targets. **Owed as a
    cross-file check at file 14.**
  - **← the lateral habenula** — **carries:** a **negative / aversive value signal** — the same
    "bad-outcome" habenular output that brakes dopamine, here modulating serotonin. **Payload
    otherwise owed. Fan-in:** unknown. **The producer declares it** (file 17), naming a lateral
    habenula → raphe (serotonin) limb alongside the dopamine-inhibition limb. **Two-ended.**
  - **← the amygdala** — **carries:** payload **owed. Fan-in:** unknown. **The producer declares
    it** (file 8), whose central-nucleus / defence output names the raphe. **Two-ended**, and file 8
    recorded its end owed for the payload.
- **Outputs:**
  - **→ the cerebral cortex** — **carries:** the serotonergic modulatory state signal; no stimulus
    content. **Fan-out:** unknown. **This endpoint names a class** covering every cortical entry.
    File 1 and file 4 name a serotonergic input among their modulatory afferents, their ends also
    un-resolved. **Owed: resolve to named cortical consumers as those files are worked.**
  - **→ the striatum** — **carries:** the same modulatory signal. **Fan-out:** unknown. **This
    endpoint names a class**; file 9 was not confirmed to declare a raphe input this pass. **Owed as
    a cross-file check at file 9.**
  - **→ the limbic system** — **carries:** the modulatory signal. **Fan-out:** unknown. **This
    endpoint names a class** and does not resolve. **Owed: name the limbic consumers** — file 8's
    entries name the raphe as an input, so some far ends exist.
  - **→ the spinal dorsal horn and the intermediolateral cell column** (the caudal raphe) —
    **carries:** neuromodulatory state, no stimulus content — part of descending pain modulation
    (the analgesia limb). **Payload otherwise owed. Fan-out:** unknown. **The consumer declares it**
    (file 16), naming "raphe nuclei and hypothalamus" as modulatory onto the dorsal horn and the
    intermediolateral cell column. **Two-ended.**
  - **→ further forebrain and limbic targets beyond those named** — **carries:** the modulatory
    signal. **Fan-out:** unknown. **This endpoint names a class** and is the recorded remainder of
    the brain-wide reach. **Owed.**
- **Internal structure and internal data flow:** described but not typed — **owed.** The raphe is
  not one nucleus: the **dorsal raphe**, the **median raphe** and the **caudal raphe** are distinct
  sub-elements with **different projection targets** — dorsal and median to the forebrain, caudal to
  the spinal cord — which is exactly the §3 test for sub-element status (different targets). They
  are named in this entry's own Function and output edges and are load-bearing, because the
  forebrain outputs leave from the rostral pair and the spinal output from the caudal one. **No
  internal edge between them is described**, and it is not clear one exists (they may be parallel
  sources rather than a chain). **Owed: name the sub-elements formally and assign each output edge
  to one; state whether any internal edge exists or mark it not applicable.**
- **Neurons:** the **dorsal raphe** (the largest raphe nucleus) holds **~235,000 neurons,
  ~165,000 serotonergic** (Baker et al. 1990 / 1991) — about a third of the brain's serotonergic
  neurons (Hornung); the median and caudal raphe add the rest, the whole serotonergic system order
  ~10⁵–10⁶. *(This count is for one sub-element, the dorsal raphe — the per-sub-element figure the
  Internal-structure slot above calls for, recorded here until that slot is typed.)*
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown — thin, largely unmyelinated serotonergic axons; no g-ratio recorded.
- **Pass:** 2026-07-24 — the brain-wide Outputs class resolved to the spinal-cord consumer (file 16) and habenular/amygdalar inputs (files 17, 8) as two-ended edges, plus cortex/striatum/limbic remainders recorded as owed classes; the dorsal/median/caudal division named as sub-elements with the dorsal-raphe count reattributed to its sub-element; missing Internal structure slot added

## Basal forebrain / nucleus basalis of Meynert — acetylcholine

- **Function:** the main source of cortical acetylcholine — attention, arousal, cortical
  plasticity / learning gain, and memory encoding; its degeneration is a hallmark of
  Alzheimer's disease. The medial septum (part of the basal forebrain) drives hippocampal theta.

  **This entry's title and framing are narrower than the structure.** The region also contains
  **GABAergic** and **glutamatergic** projection neurons, and the GABAergic and glutamatergic
  populations together are reported to make up **the majority of its projections** — the cholinergic
  population, which the entry is named for, is not the bulk of the output. The parvalbumin-expressing
  GABAergic subpopulation has its own targets and its own signature effect (cortical gamma-band
  activity), distinct from the cholinergic one. **Re-titling this entry, or splitting it by
  transmitter, is owed.** *(Class 1 — PubMed Central PMC4463930; PMC4371918; PMC11785998; rodent.
  **Unverified: the key reads owed in the reference section — not searched.**)*
- **Inputs:**
  - **← limbic and prefrontal cortex** — **carries:** payload **owed. Fan-in:** unknown. **This
    endpoint names a class** — descending cortical control, not resolved to named entries. **Owed:
    resolve to named producers in files 8, 11 and 17, or narrow.** File 8's amygdalar central
    nucleus declares an output here (below), which is one member of what this class was standing in
    for.
  - **← the amygdala**, from the **central nucleus** — **carries:** payload **owed. Fan-in:**
    unknown. **The producer declares it and names this structure** (file 8), and recorded that
    **this entry declared its sources only as the class "limbic and prefrontal cortex,"** which
    covers this structure without naming it, with the edit **owed at this file. Written now**,
    discharging that owed edit.
  - **← the hypothalamus** — **carries:** payload **owed. Fan-in:** unknown. **The producer declares
    it** (file 14), naming a hypothalamic / brainstem projection to the basal forebrain and the
    substantia innominata. **Two-ended.**
  - **← the brainstem** — **carries:** payload **owed. Fan-in:** unknown. **This endpoint names a
    class**; the ascending brainstem arousal drive is attributed to "brainstem" without a named
    entry. **Owed: resolve to named producers in file 14, or narrow.**
- **Outputs:**
  - **→ the entire cerebral cortex**, from the **nucleus basalis of Meynert** — **carries:**
    acetylcholine, as the entry's Function describes — a cortical plasticity / learning-gain and
    attention signal, not stimulus content. **Fan-out:** unknown. **This endpoint names a class**
    covering every cortical entry, and is the load-bearing class in the entry. File 1 and file 3
    name a cholinergic / basal-forebrain input among their modulatory afferents, their ends
    un-resolved. **Owed: resolve to named cortical consumers as those files are worked.**
  - **→ the hippocampus, from the medial septum, cholinergic cells**, via the fornix (pre-commissural
    limb) — **carries:** a **tonic gain / arousal-state signal**, delivered largely by **volume
    transmission** (≈93% of cholinergic varicosities in the hippocampus form no classic synapse); it
    biases hippocampal state and theta amplitude and gates the theta-vs-ripple regime, but does
    **not** pace theta — optogenetically activating it barely moves theta frequency. **Fan-out:**
    unknown. **The consumer declares it** (file 8, the cholinergic limb). **Two-ended.** *(This is the
    edge this entry formerly declared as the whole "→ hippocampus (medial septum) — acetylcholine"
    line; research on 2026-07-24 established that acetylcholine is only one of three transmitter
    limbs and carries the gain envelope, not the clock.)*
  - **→ hippocampal inhibitory interneurons, from the medial septum, parvalbumin-expressing
    GABAergic pacemaker cells**, via the fornix — **carries:** the **theta timing reference** — the
    phase of a 4–12 Hz clock whose tick is an **intrinsic membrane oscillation carried by the
    hyperpolarisation-activated cyclic-nucleotide-gated (HCN) channel current** in these cells
    (not made by GABA; GABA is the wire and the synchronizing coupling). **Fan-out:** unknown.
    **The consumer declares it** (file 8). **Two-ended.** *(This limb belongs to the basal-forebrain
    GABAergic population this entry's Function already flags as the bulk of its output; it is one of
    the concrete edges that population owes.)*
  - **→ the hippocampus, from the medial septum, glutamatergic cells**, via the fornix —
    **carries:** a **tonic excitatory gate** — the depolarizing drive that toggles the pacemakers
    between theta and non-theta states; not content and not a per-cycle signal. **Fan-out:** unknown.
    **The consumer declares it** (file 8). **Two-ended.**
    *(These three lines replace one that read "→ hippocampus (medial septum) — acetylcholine" and was
    a genuine two-ended-diff failure against file 8's "theta pacing." Resolved by research 2026-07-24:
    the septo-hippocampal projection is three transmitter limbs with three payloads, and each end had
    named one and mistaken it for the whole. Rodent throughout; candidate. This resolution is the
    concrete instance of the transmitter split the entry's Internal-structure slot calls for.)*
  - **→ cortical inhibitory interneurons**, from the **parvalbumin-expressing GABAergic**
    population — **carries:** an inhibitory signal onto inhibitory targets, whose net cortical
    effect is **activation**: it drives and entrains cortical gamma-band oscillations, probably by
    synchronising cortical inhibitory neurons. Targets include both parvalbumin- and
    somatostatin-expressing cortical interneurons. **Fan-out:** unknown. *(Class 1 — PMC4371918,
    mouse.)*
  - **→ the thalamic reticular nucleus**, from the same parvalbumin GABAergic population —
    **carries:** inhibition of the thalamic gate, and therefore disinhibition of the relay nuclei
    behind it. **Fan-out:** unknown. **Declared at both ends** and confirmed against file 12 this
    pass — that entry's reticular-nucleus Inputs declare "basal forebrain, parvalbumin-expressing
    GABAergic neurons," carrying the double-negative logic (a tonic inhibitory hold on the relay
    nuclei, transiently released). **Two-ended.** *(Class 1 — PMC4371918, mouse. Not yet verified
    for the source. One negative result recorded at the consumer: driving these fibres within the
    reticular nucleus enhanced cortical power at ~10 Hz, spindle frequency, not gamma — so this
    edge is not the carrier of the gamma effect; the direct cortical projection above is.)*
  - **→ the thalamic reticular nucleus**, from the **cholinergic** population — **carries:** payload
    **owed**; driving it promotes sleep, opposite in sign to the edge above. **Fan-out:** unknown.
    **Declared at both ends** and confirmed against file 12 this pass — two projections from one
    source region to one target with opposite behavioural consequences. **Two-ended.** *(Class 1 —
    PMC4764559, rodent.)*
  - **→ further subcortical targets beyond the thalamic reticular nucleus** — **carries:** the
    relevant population's signal. **Fan-out:** unknown. **This endpoint names a class** and is the
    recorded remainder. **Owed.**
- **Internal structure and internal data flow:** described but not typed — **owed**, and it is the
  most load-bearing internal-structure slot in the file. This "entry" is really **three
  co-located projection systems** distinguished by transmitter — **cholinergic**, **parvalbumin-
  expressing GABAergic**, and **glutamatergic** — plus a topographic division into the **medial
  septum** (→ hippocampus), the **diagonal band**, and the **nucleus basalis of Meynert**
  (→ neocortex). Both divisions are sub-elements in the §3 sense, because the output edges above
  already leave from different ones: the gamma-driving and reticular-inhibiting edges from the
  parvalbumin GABAergic cells, the cortical and hippocampal acetylcholine edges from the
  cholinergic cells, the sleep-promoting reticular edge from a cholinergic subset. **The internal
  edges — if the transmitter populations interact locally — are not described, and may not exist
  (they may be parallel systems). Owed: name the transmitter and topographic sub-elements formally,
  assign every output edge to one, and state whether internal edges exist.** The transmitter split
  is why the medial-septum → hippocampus edge failed its diff against file 8: it was one edge line
  for what research on 2026-07-24 showed to be three transmitter limbs — cholinergic, GABAergic
  parvalbumin, glutamatergic — now split into three output edges above.
- **Neurons:** order 10⁵ cholinergic (soft, to firm). *(This is the cholinergic sub-element only;
  the GABAergic and glutamatergic populations — reported to be the majority of projections — have
  no count recorded, which the Internal-structure slot's split makes a visible gap rather than a
  silent one.)*
- **Synapses:** unknown.
- **Axons:** unknown.
- **Grey-matter volume:** unknown.
- **White-matter volume:** unknown.
- **Myelination:** unknown.
- **Pass:** 2026-07-24 — the medial-septum → hippocampus edge resolved from a two-ended-diff failure into three transmitter-split outputs (cholinergic tonic-gain by volume transmission; GABAergic parvalbumin theta timing carried by an intrinsic membrane oscillation of the hyperpolarisation-activated cyclic-nucleotide-gated channel current; glutamatergic tonic gate), matched two-ended against file 8; the two typed reticular-nucleus outputs confirmed two-ended against file 12; the amygdalar and hypothalamic inputs typed from their producers (files 8, 14); missing Internal structure slot added, carrying the transmitter and topographic sub-elements

---

## References

*(Section added 2026-08-12 under source design §2a; **statuses corrected 2026-08-15** — a key read
off a publisher, journal or PubMed record **is verified against that record**, per §2a's rule that
searching *is* the verification, and verification of data does not run to a person at all. Each full
reference given here was obtained by
a web search run in this pass against publisher, journal or PubMed records — no reference is
written from recall. Keys reading **owed** were not searched in this pass, and keys reading
**partial** were resolved only far enough to name the work, which the line says.)*

**8 distinct keys, 11 mentions. 2 searched to a full reference; 1 partial; 5 owed.**

**Three of the eight keys also appear in file 12, and that is the finding this section was
written to expose.** *PMC4371918*, *PMC4463930* and *PMC4764559* are cited in both files, as bare
accession numbers with no author, title or year in either. They support the **same two edges seen
from both ends** — the basal forebrain's parvalbumin and cholinergic projections to the thalamic
reticular nucleus, declared as outputs here and as inputs there. **This is what an edge sweep
leaves behind:** the accession travelled with the edge to the far file, and the bibliography did
not travel with it. Neither file can identify these papers on its own, and both depend on them.

**Resolving one of the three answers an open question left in file 12's reference section.**
That section recorded *Proceedings of the National Academy of Sciences* (file 12, line 629) as a
key naming no volume, page, year or author, and marked it as identifying nothing on its own.
**It is the journal of PMC4371918** — Kim et al. 2015 — which the file 12 line already sits
beside. **That key is not a separate source and should be folded into the accession's reference.**

**Two of the three searched works are reviews, and both are labelled Class 1 in the files.**
*PMC4463930* is an ascending-GABAergic-arousal review, and *Sesack & Grace 2010* is a
*Neuropsychopharmacology Reviews* article. Line 284 here and line 643 of file 12 both mark
*PMC4463930* **Class 1**, which in this source means primary measurement. **Owed at three citing
lines: reclassify, or name the primary papers the reviews are standing in for.**

**One number in this file falls outside the range its own cited source gives**, and it appears
twice. See the *Sesack & Grace 2010* entry: the file's ~5% glutamatergic against the review's
~2–3%.

**One searched reference carries a published correction**, recorded in its entry so that nobody
has to check twice. It is an acknowledgments change, not a scientific one.

**Species composition of what has been searched: all three are rodent** — *PMC4371918* mouse,
*PMC4463930* a rodent-based review, *Sesack & Grace 2010* a review drawing chiefly on rat with
some primate work. **The file's only human material is in the five owed keys** — the locus
coeruleus and dorsal raphe counts at lines 198 and 261 rest on *Benarroch 2018*, *Baker et al.
1990 / 1991* and *Hornung*, none of them searched. **So the searched half of this file is entirely
non-human and the unsearched half is where the human numbers live**, which is the reverse of a
useful order and is worth fixing on the next pass.


- **Baker et al. 1990 / 1991** — **owed**: not searched in this pass. **The key hedges between two
  years**, which is either two papers or an unresolved citation, and the file does not say which.
  It carries the dorsal raphe's ~235,000 neurons and ~165,000 serotonergic — **the only firm
  per-sub-element count in the file**, and one the Internal-structure slot at lines 251–259
  explicitly depends on. *(Line 261.)*
- **Benarroch 2018** — **owed**: not searched in this pass. Carries the locus coeruleus figure of
  ~50,000 neurons per side and the reported human range of ~22,000–51,000, which the file's own
  preamble at line 41 calls the one firm human figure among these four nuclei. **Highest-value owed
  key in the file.** *(Line 198.)*
- **Fudge & Haber 2001 (PubMed 11440812)** — Fudge, J.L. & Haber, S.N. (2001). Bed nucleus of the stria terminalis and extended amygdala inputs to dopamine subpopulations in primates. **Primate.** Anterograde/retrograde tracing with a subdivision-level analysis of the bed nucleus and sublenticular extended amygdala against the dorsal-tier and densocellular dopamine groups. *(PubMed record; abstract read, **full text not opened**; searched 2026-08-15.)* **Verified as a reference; the abstract is the extent of what was read, so any claim beyond the topography summarised on the citing edge is not supported by this pass.** **Two things it establishes that no entry in this source carries:** the projection divides by **bed-nucleus subdivision** — medial, lateral, and within the lateral the central core, dorsolateral, capsular, juxtacapsular and posterior — and its target spans **both** the ventral tegmental area and the substantia nigra pars compacta, which live in two different files. *(Ventral tegmental area entry, Inputs.)*
- **Hornung** — **owed**: not searched in this pass; **the key carries no year and no title.** It
  supports the claim that the dorsal raphe holds about a third of the brain's serotonergic neurons.
  *(Line 262.)*
- **PMC11785998** — **owed**: not searched in this pass. **A bare accession**, and unlike the other
  three it appears in this file only. It is one of three cited together at line 284 for the claim
  that the GABAergic and glutamatergic populations together make up the majority of the basal
  forebrain's projections — **the claim that makes re-titling this entry owed**, so it is
  load-bearing for a structural change rather than for a number. *(Line 284.)*
- **PMC4371918** — Kim, T., Thankachan, S., McKenna, J.T., McNally, J.M., Yang, C., Choi, J.H.,
  Chen, L., Kocsis, B., Deisseroth, K., Strecker, R.E., Basheer, R., Brown, R.E. & McCarley, R.W.
  (2015). Cortically projecting basal forebrain parvalbumin neurons regulate cortical gamma band
  oscillations. *Proceedings of the National Academy of Sciences* 112(11): 3535–3540; doi
  10.1073/pnas.1413625112; PubMed 25733878; PMC4371918. **Mouse.** Viral transduction of basal
  forebrain parvalbumin neurons with optogenetic stimulation and cortical recording. **Correction:
  *Proceedings of the National Academy of Sciences* 112(21): E2848; doi 10.1073/pnas.1507465112;
  PubMed 25918414 — an addition to the acknowledgments naming funding support, with no change to
  any result.** *(National Academy of Sciences publisher record, PubMed and PubMed Central.)*
  **Both this file's uses of the paper check out, and so does file 12's.** The paper found the
  transduced fibres densely innervating the thalamic reticular nucleus, which is the edge at line
  342; it found the cortical fibres apposed to cortical parvalbumin interneurons and concluded that
  the direct cortical projection is the parsimonious explanation of the gamma effect, which is the
  edge at line 336; and it reports that stimulating the reticular nucleus's own parvalbumin neurons
  **preferentially enhanced cortical power at 10 Hz**, consistent with spindle activity, **and not
  gamma** — which is the negative result recorded at lines 348–350 here and at lines 684–689 of
  file 12. **The two files state it independently and agree.** **This accession is also what file
  12's orphan *Proceedings of the National Academy of Sciences* key names.** *(searched 2026-08-12;
  candidate. Lines 284, 340, 347.)*
- **PMC4463930** — **partial.** A review titled *Turning a Negative into a Positive: Ascending
  GABAergic Control of Cortical Activation and Arousal*; PMC4463930. **Rodent-based review.**
  *(**Author list, journal, volume, pages and year were not obtained from a publisher record this
  pass** — only the title and the accession. §2a requires saying so.)* **Two findings, and the
  second is for file 12 rather than this one.** **First, it is a review and both files call it
  Class 1** — see the note above the list. **Second, and this bears on an ambiguity file 12
  declares as owed:** file 12's reticular-nucleus entry cites this accession at line 643 for a
  pallidal and nigral input to the reticular nucleus, and records at lines 640–643 that whether
  those fibres terminate on the reticular nucleus or directly on the relay nuclei is not
  distinguished at either end. **The passage of this review surfaced by the search states that the
  substantia nigra pars reticulata's output tonically inhibits the motor thalamus and the
  centromedian–parafascicular nucleus** — relay nuclei, not the reticular sheet — **which leans
  toward the second horn of that ambiguity.** **This is one retrieved passage and not a reading of
  the paper; it is a candidate for opening the review, not a resolution.** *(searched 2026-08-12;
  candidate, partial. Line 284.)*
- **PMC4764559** — **owed**: not searched in this pass. **A bare accession, and shared with file
  12** (line 636 there). It carries the cholinergic sleep-promoting result — the edge whose sign is
  opposite to the parvalbumin edge from the same source region to the same target, which both files
  flag as the surprise. **Of the five owed keys this is the one whose resolution would settle a
  claim rather than confirm a number.** *(Line 355.)*
- **Sesack & Grace 2010** — Sesack, S.R. & Grace, A.A. (2010). Cortico-basal ganglia reward
  network: microcircuitry. *Neuropsychopharmacology* 35(1): 27–47; doi 10.1038/npp.2009.93; PubMed
  19675534. **A review**, in that journal's Reviews series, drawing chiefly on **rat** work with
  some primate. *(Nature Publishing Group publisher record and PubMed.)* **The composition figures
  this file takes from it do not all match it.** The file gives **~65% dopaminergic, ~30%
  GABAergic, ~5% glutamatergic** at lines 116 and 124. The review states that non-dopaminergic
  ventral midbrain neurons are primarily GABAergic and make up approximately **30–35%** of ventral
  tegmental area cells, and that the glutamate population comprises approximately **2–3%** —
  attributing both to a primary paper, **Nair-Roberts et al. 2008, which this file does not cite.**
  **So the GABAergic figure sits at the bottom edge of the review's range with the range dropped,
  and the glutamatergic figure is roughly double the review's upper bound.** **The three numbers as
  written also sum to exactly 100**, which the review's ranges do not, and which is the signature of
  a set rounded to close rather than reported. **Owed at both citing lines: carry the ranges, cite
  the primary paper the review names, and say the figures are rodent** — the file attaches no
  species to them, and they sit in a Neurons slot whose other entries are human. *(searched
  2026-08-12; candidate. Lines 116, 124.)*
