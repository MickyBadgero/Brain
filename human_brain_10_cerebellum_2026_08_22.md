# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-22
---

---

# FILE 10 OF 20 — CEREBELLUM

**What is in this file.** The cerebellum: cortex, deep nuclei, and the inferior olive that supplies the climbing-fibre error signal.

**Size:** 581 lines, ~12.2k tokens (estimated from bytes, not tokenised). **Entries:** 3. **Edge lines:** 21 — 12 in, 9 out.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Cerebellar cortex — the repeating microcircuit (three-layered)**
- **Deep cerebellar nuclei — the sole output stage**
- **Inferior olive — the climbing-fibre source (medulla)**

**Which cross-file claims here are checked, and which are not.** Claims made about files 3 (other
senses), 5 (sensorimotor loop), 7 (anterior temporal lobe), 8 (medial temporal lobe), 9 (basal
ganglia), 11 (frontal lobe), 12 (thalamus), 13 (neuromodulatory systems), 14 (brainstem / midbrain /
hypothalamus), 16 (spinal cord), 17 (insula / claustrum / habenula / cingulate remainder) and 18
(white-matter tracts) are checked against those files. **Claims about files 1 (visual pathway), 2
(auditory), 4 (dorsal visual / parietal stream), 6 (posterior parietal), 15, 19 and 20 are
unchecked.**

---

# CEREBELLUM

*The cerebellum holds ~80% of all the brain's neurons (~69B — the single largest neuron pool) in
~10% of its volume, yet it is built from **one microcircuit repeated on a massive scale** — the most
stereotyped, crystalline architecture in the brain. Because that architecture is so uniform, the
cerebellum is also the **best-counted** part of the brain (the isotropic-fractionator and the Danish
stereology lineages both converge here), so — unlike almost everything else in this document — it
enters with **hard numbers rather than soft ones**. The same circuit is applied across a
**functional topography**: an anterior sensorimotor cerebellum and a posterior cognitive / limbic
cerebellum, each wired to the matching cerebral areas through crossed **cerebro-cerebellar loops**
(cortex → pontine nuclei → cerebellar cortex → deep nuclei → thalamus → cortex). Schmahmann's
unifying reading — that the cerebellum performs one computation, so "dysmetria of thought" mirrors
dysmetria of movement — is the current organizing hypothesis. **Number convention:** cerebellar
counts are usually reported for the **whole cerebellum (both sides)**; whole-cerebellum figures are
tagged as such with the per-hemisphere value alongside (≈ half), following the basal-ganglia
treatment.*

***Two regions on that loop have no entry anywhere, and they belong to this section and to the
brainstem section together.*** *The **pontine nuclei** and the **red nucleus** are named on five
edges below — the mossy-fibre input to the cortex, both of the deep nuclei's rubral outputs, and the
descending limb of the dentato-rubro-olivary loop — and neither has an entry in this file or in any
file checked against it. **Naming a region on an edge is not describing it**, and the brainstem
file's preamble states that the pontine nuclei, red nucleus and inferior olive are described **in
this section**. Only the third is.*

***Neither section owns them alone, and that is a fact about the loop rather than an unmade
decision.*** *Anatomically they are brainstem — the pontine nuclei fill the ventral two-thirds of
the pons, the red nucleus sits in the ventral midbrain. Functionally they are stations on the
cerebro-cerebellar and dentato-rubro-olivary loops described here. **The source's sections are split
by data flow, and this loop runs through two of them.** **Owed: write both entries, and decide which
file physically carries each — the other must then reference it and must not treat the endpoint as
missing.** The researched payloads are recorded on the edges below, so writing them is transcription
rather than new research.*

***And the corticopontine relay is the load-bearing case.*** *It is the route by which cortical
activity reaches the cerebellum at all, and it is a processing stage rather than a relay — see the
first input edge below. **A region that transforms
the payload cannot be left as a name on an edge.***

## Cerebellar cortex — the repeating microcircuit (three-layered)

- **Function:** a single canonical circuit tiled across the whole structure, and the circuit itself
  is now written under Internal structure rather than here. In outline: two afferent systems drive
  it — **mossy fibres**, carrying sensorimotor and cortical information, and **climbing fibres**,
  one per Purkinje cell, carrying an instructive error signal. **Purkinje cells are the sole output
  of the cortex**, and their projection is inhibitory onto the deep nuclei.
- **Functional topography (one circuit, many jobs):** the **anterior lobe (lobules I–V) plus lobule
  VIII** is the sensorimotor cerebellum (two somatotopic maps, looped with cerebral sensorimotor
  cortex); the **posterior lobe (lobules VI–VII)** is the cognitive / limbic cerebellum (looped with
  prefrontal, posterior-parietal, superior-temporal, and cingulate / retrosplenial association
  cortex — language lateralises to the right cerebellar hemisphere, spatial cognition to the left);
  the **flocculonodular lobe (lobule X) plus vermis** is the vestibulocerebellum. The three matching
  lesion syndromes are the cerebellar **motor** syndrome (anterior), the **cerebellar
  cognitive-affective / Schmahmann** syndrome (posterior — executive, visuospatial, linguistic and
  affective deficits), and the **vestibulo-cerebellar** syndrome (flocculonodular) (Stoodley &
  Schmahmann meta-analyses 2009/2012; Schmahmann & Sherman 1998).
- **Inputs:** **two afferent systems, and their payloads are different in kind — this is the
  structural fact of the whole cerebellum.**
  - **← the pontine nuclei** (mossy fibres, via the middle cerebellar peduncle; the corticopontine
    relay, crossed) — **carries:** an **integrated mixture of cortical activity** — intention, plan
    and context, drawn from many cortical areas at once and **not** a copy of any one of them.
    **Fan-in:** each granule cell has only **3–7 dendrites (~4 in human), one mossy input each** —
    the lowest fan-in in the map, and the reason the granule layer can expand rather than average.
    **The producer has no entry in any file checked against this one** — see the note at the head of
    this section — **and the payload is not a copy of cortical activity, in three specific ways.**
    - **It is not a copy: the relay diverges and then reconverges.** The corticopontine projection
      is markedly **divergent** and the pontocerebellar projection markedly **convergent**, and
      together they produce considerable **integration** of cerebrocortical information before it
      reaches this structure. Each small spot of this cortex receives afferents from **many widely
      separated pontine cell clusters**. So a granule cell's single mossy input is a mixture of
      spatially separated cortical sources, which is a payload transform and not a relay.
    - **It is not nearly the whole cortex.** In monkey the most notable exception is an **almost
      total lack of projections from large parts of prefrontal and temporal cortices**. The input
      arises from **layer 5**, and subcortical sources contribute only a few percent of the total.
    - **The map is reweighted in transit.** Within the corticopontine projections from visual and
      somatosensory areas there is a **de-emphasis of central vision and of the distal parts of the
      extremities**, compared with those same areas' other connections. **That is a payload change
      with a direction**: the relay discards precisely the parts of the map the cortical areas
      themselves magnify.
    **Taken together these say the corticopontine relay is a processing stage**, and the cerebellum
    therefore does not receive cortex's state — it receives a reweighted, integrated projection of
    part of it. **Owed: give the pontine nuclei an entry and type what leaves them**; the entry
    would also need to record that the structure comprises the **basal pontine nuclei** and the
    **reticulotegmental nucleus**, and that the corticopontine terminal fields are arranged in
    lamellar, onion-like patches with anterior cortex projecting medially and posterior cortex
    laterally.
    *(Class 1 — divergence / convergence and the widely-separated-clusters finding: the ScienceDirect pontine nuclei
    overview, primate and rodent tracing. Cortical
    exceptions, the central-vision and distal-extremity de-emphasis, and the few-percent subcortical
    share: "Organization of the pontine nuclei," PubMed 1374872, 1992, monkey. Layer-5 origin and
    the basal / reticulotegmental composition: bioRxiv 637447, 2019, mouse. Subarea topography:
    PMC10070096, 2023, mouse bidirectional tracing. Lamellar patch organisation in human: Scientific
    Reports s41598-025-00886-7, 2025, human in-vivo and post-mortem diffusion tractography. Located
    by web search 2026-07-23; **abstracts and search excerpts only, no full paper opened.**
    Candidates — awaiting Micky's verification.)*
  - **← the spinocerebellar tracts** (mossy fibres, via the inferior peduncle, ipsilateral) —
    **carries:** body proprioception — the actual configuration, unconscious. **Fan-in:** as above.
    **Two-ended:** `16_spinal_cord` declares `→ Cerebellum`, from **Clarke's column / nucleus
    dorsalis** (≈ C8–L2/3) via the **dorsal spinocerebellar tract**, carrying unconscious
    proprioception — body configuration. **The two ends agree on the payload**, and that end names
    the sub-element this one does not.
  - **← the external cuneate nucleus** (the cuneocerebellar tract, mossy fibres, via the inferior
    peduncle) — **carries:** proprioception only — body configuration, unconscious. **Fan-in:** as
    above. **Declared at the producer's end as well as here**: the dorsal
    column nuclei entry (file 5) declares "→ cerebellum (cuneocerebellar tract, **from the external
    cuneate nucleus**)" and records that the external cuneate nucleus is a third nucleus of that
    complex, added precisely so the sub-element this edge leaves from has a name.
    That entry also records that this edge and its thalamocortical sibling carry **the same payload
    to two destinations of different kinds**, one becoming a reportable percept and one writing
    procedural change — a claim about this structure made at the other end. *(Transcribed from the dorsal column nuclei entry, file 5. Candidate — awaiting
    Micky's verification.)*
  - **← the semicircular canals, the otolith organs, and the vestibular nuclei** (mossy fibres, to
    the flocculonodular lobe) — **carries:** rotation rate and gravito-inertial acceleration, and the
    nuclei's computed estimate. **Fan-in:** as above. **Two-ended:** `03_other_senses` declares `→ cerebellum`
    (flocculonodular lobe) from the semicircular canals and the otolith organs **on a branch that
    bypasses the nuclei**, and `→ cerebellum` (flocculus / nodulus / vermis) from the vestibular
    nuclei carrying their computed estimate — **so that end already distinguishes the direct
    transducer branch from the nuclear one, which is the split this line owes.** Splitting it is
    **owed** — two transducers and a computing nucleus are not one source, and the line's own payload
    clause already distinguishes their contributions.
  - **← the inferior olive** (climbing fibres, via the inferior peduncle, crossed) — **carries:** the
    **instructive error signal** — one all-or-none complex spike saying *that was wrong*. **One
    climbing fibre per Purkinje cell**, and the payload is **one bit with a timestamp**: it must
    arrive while the error is still present or it teaches nothing. **Fan-in: exactly one** — the
    other known fan-in in this file, and the sharpest contrast in it: ~335,000 parallel-fibre inputs
    against **one** climbing fibre, and the one wins. **The producer is in this file and declares
    it.**
  - **← the locus coeruleus** — **carries:** payload **owed**; noradrenaline, setting global gain,
    in the producer's terms. **Fan-in:** unknown. **The producer declares its targets as a class**
    that names this structure — "brain-wide — the entire cortex, thalamus, hippocampus, cerebellum,
    and spinal cord" (file 13). **A diffuse modulator arriving on a circuit whose whole
    account is two afferent systems is worth having visible**, which is why it is written as an edge
    rather than left inside the producer's class.
- **Outputs:**
  - **→ the deep cerebellar nuclei**, from the **Purkinje cells** — **carries:** **inhibition**,
    graded — the Purkinje sheet's summed verdict on the expansion-recoded input. **The cortex
    projects nowhere else** except the line below. **Fan-out:** unknown. **The consumer is in this
    file and declares it.**
  - **→ the vestibular nuclei**, from the **flocculonodular lobe**, directly — **carries:** graded
    inhibition, as above. **Fan-out:** unknown. **Two-ended:** `03_other_senses` declares `← cerebellum`
    (flocculonodular lobe, nodulus / uvula) as the return arm. *(A separate line rather than a
    parenthesis on the line above: it is the one exception to "the cortex projects nowhere else,"
    and a rule's exception cannot be carried inside the clause that asserts the rule.)*
- **Internal structure and internal data flow:** *(**This is the case the design file names**: a
  microcircuit that would otherwise sit as prose inside **Function**, with its payload change filed
  under **Outputs** as a bullet with no target region. Both belong here, typed.)*

  **Laminar sub-elements: three** — the **molecular layer**, the **Purkinje cell layer**, and the
  **granular layer**. Three-layered, as the entry's heading says; the file's eight-layer isocortical
  block does not apply and is not written. *(Class 3 — general cerebellar anatomy.)*

  **The scope of this exception, recorded identically in five files.**
  The source's standard Class-3 laminar block — **1, 2, 3, 4, 5a, 5b, 6a, 6b** with **4 → 2/3**,
  **2/3 → 5a and 5b**, **6a → 4**, **6a → 5a**, **6b → 6a** and within-sub-element recurrence — is
  **not a default. It is a claim about granular isocortex**, and three of its edges route through
  layer 4. **Nine entries across five files cannot take it**: primary motor cortex (file 5,
  agranular throughout); the temporal pole (file 7, agranular medially on a gradient); the
  hippocampal formation (file 8, three-layered allocortex); this entry (three-layered and not
  isocortex at all); and five entries in the frontal lobe (file 11) — premotor cortex, Broca's area,
  the right inferior frontal gyrus, the orbitofrontal / ventromedial entry and the anterior
  cingulate. **They fail it in four different ways** — uniformly agranular, agranular across a
  gradient, agranular across an internal border, and not isocortex — **so a single exception clause
  would not cover them.** **This entry is the furthest from the block of the nine**, being the only
  one whose tissue is not cerebral cortex. **Owed at the design file: state where the block is
  defined that it applies to granular isocortex only.**


  **Cell-class sub-elements: five, and they are sub-elements rather than properties** — **granule
  cells**, **Purkinje cells**, **Golgi cells**, **stellate cells** and **basket cells**. Taken from
  this entry's own Function field. Each meets the floor-of-the-hierarchy test by having its own
  targets: the granule cell's axon becomes the parallel fibre, the Purkinje cell is the sole
  output, the Golgi cell projects back onto granule cells, and the stellate and basket cells project
  onto Purkinje cells. *(Class 3, as stated in the entry's own Function.)*

  **Tangential sub-elements: the parallel fibre is the tangential organisation, and it is
  geometric rather than compartmental.** Granule axons ascend and bifurcate to run **~5–6 mm along
  the length of the folium**, crossing the flat dendritic fans of many Purkinje cells at right
  angles. **An edge cannot terminate on a compartment here** — the organisation is a lattice, not a
  parcellation — which is a different case from the divisional sub-elements above and from the
  continuous feature maps recorded elsewhere in the source.

  **Internal edges:**
  - **mossy-fibre terminals → granule cells** — **carries:** the afferent payload, whichever of the
    four mossy systems it arrived on. **Fan-in: 3–7 dendrites per granule cell (~4 in human), one
    mossy input each. Fan-out:** a single mossy fibre contacts **~500 granule cells** *(rat figure;
    Ito 1984, 2006)*.
  - **granule cells → Purkinje cells**, via the **parallel fibres** — **carries:** the
    **expansion-recoded** afferent payload: the same information in a different code, spread into an
    enormous, sparsely-active population so that patterns which arrived similar leave **separable**.
    **This is the entry's payload change and the point of the structure.** **Fan-in: ~335,000 parallel-fibre synapses per
    Purkinje cell. Fan-out:** through the parallel fibres a single mossy fibre reaches **~150,000
    Purkinje cells** *(rat figure)*; per granule cell, the derived cross-check below gives **~148
    parallel-fibre–Purkinje contacts**.
  - **granule cells → Golgi cells**, via the parallel fibres, and **Golgi cells → granule cells** —
    **carries:** feedback inhibition onto the expansion stage; no content. **This is the loop that
    keeps the granule population sparse**, which the expansion recoding depends on, and the entry
    asserts the sparseness without it. **Fan-in / fan-out:** unknown.
  - **granule cells → stellate and basket cells**, via the parallel fibres, and **stellate and
    basket cells → Purkinje cells** — **carries:** feedforward inhibition onto the output stage; no
    content. The basket cell's terminal is on the Purkinje soma and initial segment, the stellate
    cell's on the dendrites. **Fan-in / fan-out:** unknown.
  - **climbing fibre → Purkinje cell** — **this is an inter-region edge terminating on a
    sub-element, not an internal edge**, and it is written in Inputs above. It is noted here because
    the plasticity it drives is internal: the complex spike depresses the **parallel-fibre–Purkinje**
    synapse named two edges up, so the instructive signal from one region modifies an internal edge
    of this one. **The source has no way to express that** — a payload on an inter-region edge whose
    effect is a change to an internal edge's transfer — and it is recorded here as a limit of the
    representation rather than a gap in the anatomy. *(Class 3 for the long-term depression, which is
    in the entry's Function. **Class 2** — the observation that the file cannot express a
    cross-region effect on an internal edge is Claude's, offered to be checked.)*

  **What the sheet computes with the verdict is not written.** Expansion-recoded input arrives on
  ~335,000 parallel fibres per Purkinje cell; graded inhibition leaves. **The operation between them
  — a weighted sum, a threshold, a temporal pattern — is not stated**, and the entry's own phrase,
  the sheet's "summed verdict," is the only description of it. This is the **eighth** entry in the
  source where the stated function has no declared internal substrate. **It is also the mildest of
  the eight**: here the sub-elements, their edges and two of the fan figures *are* written, so what
  is missing is the transfer function rather than the circuit. Recorded so the eight are not read as
  one severity.
- **Neurons:** **~69B total, whole cerebellum (~34–35B per hemisphere)** — ~80% of all brain neurons
  (Azevedo et al. 2009, isotropic fractionator; Herculano-Houzel lineage). **Granule cells** are
  essentially the entire count (the most abundant neuron in the central nervous system); **Purkinje
  cells ~30.5M whole cerebellum (~15.3M per hemisphere)** (Korbo & Andersen 1995; Andersen, Korbo &
  Pakkenberg 1992), a granule-to-Purkinje convergence of **~2,000–3,000 : 1**. **Honest method
  tension:** the older Danish stereology counts **granule cells alone at ~101–109B** (Andersen,
  Korbo & Pakkenberg 1992; Andersen et al. 2003) — ~1.46× the fractionator's *total*-neuron figure
  of 69B. Both are primary, unbiased methods; the discrepancy is method-dependent (like V1's, but in
  the opposite direction — here stereology runs high and the fractionator low) and is recorded, not
  resolved.
- **Synapses:** **each human Purkinje cell carries ~300,000–500,000 dendritic spines, headline
  ~360,000** — from direct morphological reconstruction of human tissue (Busch & Hansel 2025; Masoli
  et al. 2024; reviewed in Masoli, Rizza, Moccia & D'Angelo 2025), with **~93% carrying a
  presynaptic partner** (Loschky et al. 2022) — so **~335,000 actual parallel-fibre synapses per
  human Purkinje cell**, plus the single climbing fibre. Its dendritic fan is a two-dimensional
  matrix of >10⁵ near-independent inputs. Each granule cell, by contrast, has only **3–7 short
  dendrites (~4 in human), one mossy-fibre input each** — the sparse front end. A single mossy fibre
  contacts ~500 granule cells and, through the parallel fibres, ~150,000 Purkinje cells (both rat
  figures; Ito 1984, 2006).
- **Superseded figures (recorded, because both are widely cited and both are wrong).**
  **(1) The ~175,000 parallel-fibre synapses per Purkinje cell** (Napper & Harvey 1988) is **not a
  spine count and not a human figure**: it is a *rat estimate* obtained by multiplying a
  spine-volume-density equation (17.2 spines/µm) by an average dendritic length (9,941.5 µm). It
  does not match the majority of experimental recordings and, even in the best cases, runs **six to
  seven times larger than reality** (Masoli et al. 2025); direct rodent counts give ~35,000. The
  figure is **retired here**, not merely flagged as cross-species.
  **(2) The ~10¹⁴ whole-cerebellum parallel-fibre–Purkinje contact total** (Huang et al. 2014)
  descends from the assumption that human Purkinje cells reach ~10⁶ spines — a value **recently
  disproven** by direct human reconstruction (Busch & Hansel 2025). It is **retired here** too.
- **Parallel-fibre–Purkinje contact total (human, whole cerebellum): ~1 × 10¹³**, derived from the
  two firm human counts this document already carries — ~30.5M Purkinje cells × ~335,000 synapses
  each ≈ 1.02 × 10¹³. **Cross-check:** that implies ~148 parallel-fibre–Purkinje contacts per
  granule cell (1.02 × 10¹³ ÷ 69B), which is consistent with a parallel fibre crossing many Purkinje
  dendritic trees and synapsing with only about half of them (Nguyen et al. 2023; Park et al. 2023).
  The retired ~10¹⁴ figure admits no such reconciliation — it would demand ~1,480 contacts per
  granule cell. This is the document's one derived-and-cross-checked synapse total, and it is **~10×
  below the retired ~10¹⁴ figure**.
- **Axons:** parallel fibres ~5–6 mm long; the three peduncles carry the afferents and efferents
  (counts unknown beyond the ~200M input-fibre order). **None of the three peduncles has an entry in
  the white-matter-tracts file**, whose four entries are the corpus callosum, the internal capsule,
  the fornix and the arcuate / superior longitudinal fasciculus — and that file records the same from its own side,
  correcting an earlier wording of its preamble which had implied otherwise. **The three peduncles
  have an entry nowhere.**
- **Grey-matter volume:** whole cerebellum **~130–150 cm³ in vivo (~10% of brain volume)**; fixed
  ~70 cm³ (shrinkage; Andersen / Pakkenberg lineage). The cortex is a thin, tightly-folded sheet
  whose **unfolded surface area ~1,590 cm² ≈ 78% of the neocortex** (Sereno et al. 2020) — roughly a
  1 m × 10 cm strip, ~85% of it buried in fissures.
- **White-matter volume:** the arbor vitae (absolute value unknown). **Myelination:** unknown.

## Deep cerebellar nuclei — the sole output stage

- **Function:** the **only output of the cerebellum**. Inhibition from the Purkinje sheet sculpts the
  firing of these tonically-active excitatory nuclei, whose output *is* the cerebellar contribution
  to movement and cognition. Three (four) paired nuclei, matched to the cortical zones above:
  **dentate** (lateral, the largest — reads the cognitive and association hemispheres); **interposed**
  (globose plus emboliform; paravermal — limb coordination); **fastigial** (medial;
  vermal / flocculonodular — axial posture, balance and eye movements).
- **Inputs:**
  - **← the Purkinje cells of the cerebellar cortex** (gamma-aminobutyric-acid-releasing
    (GABAergic), the dominant input) — **carries:**
    graded inhibition — the cortex's verdict. **Fan-in:** unknown. **The producer is in this file and
    declares it.**
  - **← collaterals of the mossy and climbing afferents** — **carries:** the raw input, excitatory,
    arriving alongside the verdict on it. **Fan-in:** unknown. **The climbing-fibre limb has a
    producer in this file** — the inferior olive declares collaterals to these nuclei. **The
    mossy-fibre limb does not resolve**: its four sources are the pontine nuclei (no entry), the
    spinocerebellar tracts (file 16, unchecked), the external cuneate nucleus (file 5, which declares
    only the cortical target), and the vestibular system (file 3, unchecked). **Owed: split this line
    by source, and check each.**
- **Outputs:**
  - **→ the contralateral red nucleus** (via the superior cerebellar peduncle, decussating), from
    the **interposed** nuclei — **carries:** a **correction** — the difference between what cortex
    intended and what the cerebellum predicts will actually happen. The nuclei are tonically active
    and the Purkinje sheet **sculpts** that firing, so the payload is a *modulation of an ongoing
    signal*, not a command issued from rest. **Fan-out:** unknown. **The consumer has no entry in
    any file checked against this one** — see the note at the head of this section. It is also one vertex of
    the dentato-rubro-olivary loop the inferior olive entry describes, so **two of that loop's three
    vertices are in this file and the third is nowhere.** **Owed: give the red nucleus an entry.**
    **The research splits this edge in two and makes the human case the opposite of the textbook
    one.** The red nucleus has two cytoarchitectonic subdivisions with
    different afferents and different targets: the caudal **magnocellular** part, which receives
    from the **interposed** nuclei and gives rise to the rubrospinal tract, and the rostral
    **parvocellular** part, which receives from the **dentate** nucleus and cortex and projects to
    the **inferior olivary complex** via the central tegmental tract. **In the human the
    magnocellular part is markedly reduced and the rubrospinal tract is vestigial** — few large
    fibres, and those not traceable below the upper cervical segments — while the parvocellular part
    **occupies most of the nucleus's volume** and its rubro-olivary fibres are very numerous.
    **So the edge written here is the one that barely exists in a human, and the one that does the
    work is missing.** *(Class 1 — subdivision, afferents and targets: Scientific Reports
    s41598-019-48164-7, 2019, human Human-Connectome-Project tractography, 100 subjects; Frontiers
    in Neuroanatomy 18:1331305, 2024, cytoarchitecture across 20 primate species. Vestigial
    rubrospinal tract and the very large rubro-olivary fibre population: "The rubrospinal and
    central tegmental tracts in man," PubMed 7082990, human. Located by web search 2026-07-23;
    abstracts only. Candidates — awaiting Micky's verification.)*
  - **→ the parvocellular red nucleus**, from the **dentate** nucleus — **carries:** payload
    **owed**; the descending limb of the dentato-rubro-olivary loop, which returns to this structure
    through the inferior olive. **Fan-out:** unknown. **The dentate limb is the larger of the two in human**, and
    attributing the whole red-nucleus output to the limb-coordination pathway would drop it. **The
    consumer has no entry in any file checked against this one.** *(Class 1 — same sources as above.
    Candidate.)*
  - **→ the ventral anterior / ventral lateral thalamus** (via the superior cerebellar peduncle,
    decussating) → motor, premotor and prefrontal cortex, chiefly from the **dentate** — **carries:**
    the same correction. **Fan-out:** the cerebellar-cortex to output-nucleus areal ratio is
    **~85 : 1** — a massive convergence, and one of the few fan figures this file actually carries.
    **Two-ended and typed at both**: that entry (file 12) declares `← the deep cerebellar nuclei,
    chiefly the dentate`, via the superior cerebellar peduncle, decussating, and types it as the
    cerebellar **correction** — the forward-model error correction — carrying this end's ~85 : 1
    convergence figure across with it. *(A separate line from the red-nucleus outputs: their far
    ends have different statuses — one has no entry, one declares the edge — and they leave from
    different nuclei.)*
    **Because both the corticopontine input and this output cross, each cerebellar hemisphere serves
    the contralateral cortex and the ipsilateral body.**
  - **→ the intralaminar nuclei of the thalamus** — **carries:** payload **owed. Fan-out:** unknown.
    **Declared at the consumer's end as well as here**: that entry's Inputs (file 12) name the deep
    cerebellar nuclei among its sources.
  - **→ the vestibular nuclei** and **→ the reticular formation** (fastigial, via the inferior
    peduncle) — **carries:** axial posture, balance, and eye-movement corrections. **Fan-out:**
    unknown. **The reticular-formation end declares it on its own line and names the source nucleus** —
    `← the cerebellum, from the fastigial nucleus` (file 14) — with the payload owed at that end.
    **The vestibular end is declared too**: `03_other_senses` names the cerebellum among the
    sources of its vestibular nuclei. **Both far ends are two-ended now, and splitting this line is
    owed** — the two carry different payloads and neither end can say which of the three terms goes
    to which target.
  - **→ the inferior olive** (inhibitory feedback) — **carries:** suppression of the error signal
    once the error is learned — the loop that turns the teacher off. **Fan-out:** unknown. **The
    consumer is in this file and declares it.**
- **Internal structure and internal data flow:** *(The sub-elements below come from the entry's own Function
  field, which names each and assigns it a zone and a target.)*

  **Divisional sub-elements: three, or four depending on how one is counted** — the **dentate**
  nucleus, the **interposed** nuclei (the **globose** and **emboliform** nuclei, counted as one or
  two), and the **fastigial** nucleus. Taken from this entry's own Function field, which already
  states the ambiguity in the phrase "three (four) paired nuclei." **Recorded as it stands rather
  than resolved by preference**, which is the same treatment the source gives the layer number of
  V1's 4B and the subdivision count of the insula and the temporal pole.

  **The sub-elements sort this entry's output edges, and the Function field already does the
  sorting** — dentate to the thalamus and the association loop, interposed to the red nucleus,
  fastigial to the vestibular and reticular nuclei. **Each output edge above names the nucleus it
  leaves from**, which is what this slot requires: a compound output line attributing the
  red-nucleus and thalamic targets jointly to the whole structure would lose the sorting the
  Function field states.

  **Laminar sub-elements: not applicable.** Nuclei, not cortex.

  **Tangential sub-elements: the zonal correspondence with the cortex is the organisation, and it is
  owed.** The Function field says the nuclei are "matched to the cortical zones above," and the
  cortex entry's functional topography names those zones — anterior sensorimotor, posterior
  cognitive, flocculonodular vestibular. **Which Purkinje zone projects to which nucleus is stated
  only as that matching**, and the parasagittal zonal organisation the matching rests on is not
  described in either entry.

  **Internal edges: owed, all of them.** No edge between any two of the three nuclei is recorded, in
  either direction.

  **The transfer this entry performs is stated and not typed.** Tonic excitatory firing is
  **sculpted** by graded Purkinje inhibition, and what leaves is a correction. **What sculpting is,
  on a wire — subtraction, division, a change in timing — is not stated**, and the entry's claim
  that the payload is a *modulation of an ongoing signal rather than a command from rest* is a claim
  about exactly that operation.
- **Neurons:** **dentate ~5.0M whole cerebellum** (Andersen, Korbo & Pakkenberg 1992); interposed
  and fastigial smaller (soft). The cerebellar-cortex-to-output-nucleus areal ratio is ~85 : 1 — a
  massive convergence onto the output stage.
- **Synapses:** unknown. **Axons:** the superior cerebellar peduncle (count unknown).
  **Grey-matter volume:** dentate surface ~18.6 cm² (Sereno et al. 2020); absolute volume unknown.
  **White-matter volume / Myelination:** unknown.

## Inferior olive — the climbing-fibre source (medulla)

- **Function:** the **sole source of climbing fibres**, the cerebellum's instructive input.
  Electrotonically (gap-junction) coupled olivary neurons with intrinsic subthreshold oscillations
  fire in near-synchronous bursts; each drives its target Purkinje cell to an all-or-none **complex
  spike** that signals movement error and gates plasticity at the parallel-fibre synapse.
  Anatomically it sits at the apex of the **dentato-rubro-olivary loop** (the Guillain–Mollaret
  triangle: dentate nucleus → contralateral red nucleus → ipsilateral inferior olive →
  contralateral cerebellum).
- **Inputs:**
  - **← the spinal cord grey matter** — **carries:** somatosensory **error** — the actual
    consequence, against which the prediction failed. **Fan-in:** unknown. **Two-ended:** `16_spinal_cord` declares `→ Inferior
    olive`, typing it in the same words — the actual consequence against which a prediction failed.
  - **← the dorsal column nuclei** — **carries:** the same somatosensory error. **Fan-in:** unknown.
    **The producer declares no such edge.** That entry's Outputs (file 5) name the ventral posterior
    thalamus, the cerebellum by the cuneocerebellar tract from the external cuneate nucleus, and the
    dorsal cochlear nucleus — **no olivary target**. **Owed as a cross-file edit at that entry
    (file 5), or withdraw the limb.** *(A separate line from the spinal-cord input above: the two
    limbs have different statuses.)*
  - **← the red nucleus and the mesodiencephalic junction** — **carries:** the descending limb of the
    dentato-rubro-olivary loop. **Payload otherwise unknown — owed. Fan-in:** unknown. **The red
    nucleus has no entry in any file checked against this one** — see the note at the head of this
    section.
    The mesodiencephalic junction is a region name that resolves to no entry either. **Owed: give
    the red nucleus an entry, and name what the mesodiencephalic junction refers to.**
  - **← the deep cerebellar nuclei** (inhibitory) — **carries:** suppression — *this error is
    already accounted for*. **Fan-in:** unknown. **The producer is in this file and declares it.**
- **Outputs:**
  - **→ every Purkinje cell of the cerebellar cortex** (climbing fibres, crossing, one-to-one), with
    **collaterals to the deep cerebellar nuclei** — **carries:** the **instructive signal**: a single
    all-or-none complex spike per event, timed to the error. Not a magnitude and not a direction — a
    **when**. The gap-junction coupling means these fire in near-synchronous **bursts across a
    population**, so the payload is also *which population*, which is the only addressing it has.
    **Fan-out:** one climbing fibre per Purkinje cell, and the whole map's sharpest asymmetry against
    the parallel-fibre fan-in. **Both consumers are in this file and declare it.**
    **Splitting this line is owed**: the Purkinje target and the deep-nuclei collateral are two
    edges, they terminate on different entries, and only the first is one-to-one.
- **Internal structure and internal data flow:** *(Unusually for this file, the entry's own Function field
  describes an internal mechanism without naming any sub-element to hang it on.)*

  **Divisional sub-elements: owed.** The olivary complex is conventionally divided into a principal
  olive and medial and dorsal accessory olives, whose projections address different cerebellar
  zones — **but no subdivision is named in this entry, and none is established here.** This is *owed* rather than *unknown*: the sub-elements are known to exist and to have been
  described; they have not been written here. It matters because the entry's own output payload
  says the addressing is *which population*, and a population with no named parts cannot be
  addressed in this file.

  **Cell-class sub-elements: unknown.**

  **Tangential sub-elements: the gap-junction coupling is the organisation, and it is not a
  parcellation.** The Function field makes near-synchronous bursting across an electrotonically
  coupled population the mechanism by which the payload acquires its *which population* component.
  **A coupled cluster is a dynamic grouping rather than an anatomical compartment**, so it is
  recorded here as tangential structure of a kind the slot has not met before — closer to the
  parallel-fibre lattice than to a set of areas. **Whether the clusters have fixed boundaries an
  edge could terminate on is owed.**

  **Internal edges: one, and it is not a synapse.**
  - **olivary neuron ↔ olivary neuron**, via **gap junctions** — **carries:** electrotonic coupling
    of subthreshold oscillations, producing the near-synchronous burst. **This is a non-synaptic
    internal edge**, and the source has met only two comparable cases — the retina's photon flux and
    the solitary nucleus's blood-borne chemical input, both of which are non-axonal *inputs* rather
    than internal transfers. **Recorded as its own kind.** **Fan-in / fan-out:** unknown; the entry's
    Myelination slot already records that these neurons are among the most densely
    gap-junction-coupled in the brain, which is a statement about this edge and was filed under
    myelination for want of anywhere else to put it.
- **Neurons:** soft / unknown (no clean human count recorded here).
- **Synapses:** unknown. **Axons:** the climbing fibres, via the inferior cerebellar peduncle
  (counts unknown). **Grey-matter volume:** unknown. **White-matter volume:** unknown.
- **Myelination:** unknown.

**The cerebellum is described:** the repeating cortical microcircuit (granule and parallel fibre →
Purkinje, with mossy and inferior-olivary climbing-fibre inputs and Golgi, stellate and basket
interneurons), its motor, cognitive and vestibular functional topography, the deep cerebellar nuclei
as the sole output (dentate, interposed and fastigial → superior peduncle → contralateral red
nucleus and ventral lateral / ventral anterior thalamus → cortex), and the inferior olive as the
climbing-fibre source. It carries the **firmest neuron counts in the document** (~69B total, ~80% of
all brain neurons) and a rare non-unknown synapse slot (~300–500k spines per human Purkinje cell,
~360k headline, ~93% synapsed — direct human reconstruction; ~1 × 10¹³ parallel-fibre–Purkinje
contacts across the cerebellum, derived and cross-checked). The long-quoted ~175,000-per-Purkinje
and ~10¹⁴-total figures are **retired**: the first is a rat estimate running 6–7× above measured
reality, the second descends from a now-disproven ~10⁶-spine human assumption.

**What this file does not bring into the map.** The **pontine nuclei** and the **red nucleus** are
named on five edges here and have an entry neither here nor in any file checked against this one,
and the brainstem file's preamble claims both are described here. **Naming a region on an edge is
not describing it.** The two belong to
this section and to the brainstem section together, because the loop they sit on crosses the
boundary; see the note at the head of this section for what is owed.

---

---

## References

*(Under source design §2a. Every line below is a **candidate** awaiting Micky's verification; none is
verified. Each full reference given here was obtained by a web search against publisher or journal
records — no reference is written from recall. Keys reading **owed** were not searched. **No line
here carries a line number**: a pointer into the file goes stale on the next edit and fails silently,
so the section is joined to the entries by the key alone.)*

**28 distinct keys, 33 mentions. 4 searched; 24 owed.**

**This file is the opposite of file 09.** That file carried six keys and six sourceless numbers; this
one carries 28 keys across three entries, and nearly every number in it names one. That is consistent
with the file's own claim to be the best-counted part of the brain, and it is worth stating because
the two files were built to the same standard and the citation density differs by an order of
magnitude.

**Two keys are bare surnames or lineages with no paper.** *Schmahmann*, attached to the unifying
"dysmetria of thought" reading, and *Herculano-Houzel lineage*, attached beside Azevedo et al. to the
~69B figure. A third, *Andersen / Pakkenberg lineage*, names a body of work and supports the
fixed-volume figure. None can be searched as written.

**One key names two papers.** *Stoodley & Schmahmann meta-analyses 2009/2012* is one key spanning two
years and needs splitting before either can be checked. *Ito 1984, 2006* has the same shape and
carries both rat fan figures — ~500 granule cells per mossy fibre and ~150,000 Purkinje cells through
the parallel fibres.

**Three keys support figures the file has deliberately retired**, and they are listed like any other
because a retirement rests on evidence as much as a claim does: *Napper & Harvey 1988*, for the
~175,000 parallel-fibre synapse estimate, and *Huang et al. 2014*, for the ~10¹⁴ whole-cerebellum
total, together with *Busch & Hansel 2025*, which is cited both for the replacement human spine count
and as the disproof of the assumption under Huang.

**A disagreement between two of this file's own keys.** *Andersen, Korbo & Pakkenberg 1992* gives the
human cerebellar surface area as **1,160 cm²**; *Sereno et al. 2020*, cited three number slots later,
gives the unfolded cortical surface as **~1,590 cm²**. The file uses the second and does not record
the first. Both keys are already in the file; neither citing line mentions the other. See both
reference lines below.

**The pontine and rubral research blocks carry five keys between them**, and the file records that all
were reached by web search at abstract level with **no full paper opened**. That standing is recorded
at the citing lines and is not repeated on every reference line below.

- **Andersen / Pakkenberg lineage** — **owed**: not searched.
- **Andersen et al. 2003** — Andersen, B.B., Gundersen, H.J.G. & Pakkenberg, B. (2003). Aging of the human cerebellum: a stereological study. *Journal of Comparative Neurology* 466(3): 356–365; doi 10.1002/cne.10884. **Human**, cerebellum divided into anterior lobe, posterior lobe, vermis and flocculonodular lobe. *(Wiley publisher record.)* Total granule cells **109 × 10⁹**, which is the upper end of's ~101–109B range. **Sample: 19 normal Caucasian males, aged 19–84.** Note that this paper also gives total Purkinje cells as **28 × 10⁶**, against the 1992 paper's 30.5 × 10⁶ — the file takes 30.5M as its headline and does not record the second figure. It further reports **no global Purkinje or granule loss with age** but a selective **40% loss of both in the anterior lobe**, which bears on the entry's functional topography and is not recorded there. *(searched 2026-08-11; candidate.)*
- **Andersen, Korbo & Pakkenberg 1992** — Andersen, B.B., Korbo, L. & Pakkenberg, B. (1992). A quantitative study of the human cerebellum with unbiased stereological techniques. *Journal of Comparative Neurology* 326(4): 549–560; doi 10.1002/cne.903260405. **Human**, optical disector and Cavalieri. *(Wiley publisher record.)* All three figures the file draws from it match the paper exactly: granule cells **101,000 × 10⁶**, Purkinje cells **30.5 × 10⁶**, dentate nucleus **5.01 × 10⁶**. **Sample: five elderly men.** **And the paper carries a fourth number the file does not use, which disagrees with one the file does** — see the *Sereno et al. 2020* line. *(searched 2026-08-11; candidate.)*
- **Azevedo et al. 2009** — Azevedo, F.A.C., Carvalho, L.R.B., Grinberg, L.T., Farfel, J.M., Ferretti, R.E.L., Leite, R.E.P., Jacob Filho, W., Lent, R. & Herculano-Houzel, S. (2009). Equal numbers of neuronal and nonneuronal cells make the human brain an isometrically scaled-up primate brain. *Journal of Comparative Neurology* 513(5): 532–541; doi 10.1002/cne.21974. **Human, isotropic fractionator.** *(Wiley publisher record.)* The whole-brain figure is **86.1 ± 8.1 billion** neurons, with the cerebellum at ~69 billion and the cerebral cortex ~16 billion (~19%), which is what supports. **Sample note the entry does not carry: the brains are adult *male*.** Herculano-Houzel is the last author, which is presumably what the adjacent *Herculano-Houzel lineage* key at the same line points at. *(searched 2026-08-11; candidate.)*
- **bioRxiv 637447, 2019** — **owed**: not searched.
- **Busch & Hansel 2025** — **owed**: not searched.
- **Frontiers in Neuroanatomy 18:1331305, 2024** — **owed**: not searched.
- **Herculano-Houzel lineage** — **owed**: not searched.
- **Huang et al. 2014** — **owed**: not searched.
- **Ito 1984, 2006** — **owed**: not searched.
- **Korbo & Andersen 1995** — **owed**: not searched.
- **Loschky et al. 2022** — **owed**: not searched.
- **Masoli et al. 2024** — **owed**: not searched.
- **Masoli et al. 2025** — **owed**: not searched.
- **Masoli, Rizza, Moccia & D'Angelo 2025** — **owed**: not searched.
- **Napper & Harvey 1988** — **owed**: not searched.
- **Nguyen et al. 2023** — **owed**: not searched.
- **Park et al. 2023** — **owed**: not searched.
- **PMC10070096, 2023** — **owed**: not searched.
- **PubMed 1374872, 1992** — **owed**: not searched.
- **PubMed 7082990** — **owed**: not searched.
- **Schmahmann** — **owed**: not searched.
- **Schmahmann & Sherman 1998** — **owed**: not searched.
- **ScienceDirect pontine nuclei overview** — **owed**: not searched.
- **Scientific Reports s41598-019-48164-7, 2019** — **owed**: not searched.
- **Scientific Reports s41598-025-00886-7, 2025** — **owed**: not searched.
- **Sereno et al. 2020** — **Not searched, but named here because another key contradicts it.** The file takes the cerebellar cortical surface area as **~1,590 cm²** (≈78% of the neocortex) from this keyand the dentate surface as ~18.6 cm². **Andersen, Korbo & Pakkenberg 1992 — a key of this same file, three slots earlier — gives the average human cerebellar surface area as 1,160 cm².** That is a ~27% disagreement between two sources the entry cites in adjacent number slots, and the file records neither the second figure nor the disagreement. Whether the two measure the same surface (unfolded cortical sheet versus something else) was not established here. **Owed at the citing line: reconcile, or record as contested** — the treatment this file already gives the granule-count method tension. *(searched 2026-08-11; candidate.)*
- **Stoodley & Schmahmann meta-analyses 2009/2012** — **owed**: not searched.
