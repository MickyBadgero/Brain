# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-22
---

---

# FILE 7 OF 20 — ANTERIOR TEMPORAL LOBE

**What is in this file.** The temporal pole. One entry, and the source's clearest example of a payload that fails the completion test — what it carries is named but not typed.

**Size:** 310 lines, ~7.2k tokens (estimated from bytes, not tokenised). **Entries:** 1. **Edge lines:** 11 — 6 in, 5 out.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Temporal pole (Brodmann area 38 / area TG — anterior temporal, paralimbic)**

**Cross-file endpoints carry the far file's stem where that file is checked against this one.**
An endpoint carrying no stem is unchecked, and that is not a claim that no far end exists.

---

# ANTERIOR TEMPORAL LOBE

## Temporal pole (Brodmann area 38 / area TG — anterior temporal, paralimbic)

- **Function:** the convergence apex of the ventral "what" streams and a semantic hub —
  where highly processed visual (from the inferotemporal cortex) and auditory (from the
  rostral superior temporal gyrus) object/word
  representations are bound into amodal concepts (the anterior-temporal "hub" of the
  hub-and-spoke semantic model). Also social/emotional evaluation and naming; its
  degeneration is the lesion of semantic dementia (progressive loss of word and object
  meaning with anterior-temporal atrophy).
  **The heading's "Brodmann area 38 / area TG" names one cytoarchitectonic field, and that is contested** —
  see Internal structure. The region is a **gradient**, not a field, and the literature does not
  agree on how many areas to cut it into.
- **Inputs:**
  - **← rostral superior temporal gyrus** (auditory "what") — **carries:** talker-invariant word and
    sound-object identity. **Fan-in:** unknown. **The producer declares this edge, under another name and inside a chain**: what this line calls
    the rostral superior temporal gyrus is the *anterior superior temporal gyrus and sulcus* entry
    (`02_auditory_pathway`), whose Outputs read "→ temporal pole and middle temporal gyrus →
    ventrolateral prefrontal cortex," carrying the same identity code toward amodal concept and
    controlled retrieval. **That is two edges written as one**, with this region a waypoint rather
    than a terminus, and it carries no fan-out. The parabelt entry there names this region again
    inside a seven-member compound endpoint, "→ the rostrally-directed stream." **Owed as a
    cross-file edit at `02_auditory_pathway`: give this region its own output line, at the entry
    that ends the auditory "what" stream.** **This is the principal input to the dorsolateral subdivision** — the
    quantitative connectional work on that subdivision reports its main input as arising in the
    auditory processing areas of the rostral superior temporal gyrus. *(Class 1 — Muñoz-López et al. 2015
    as reported in Córcoles-Parada et al. 2019, macaque/primate; web search 2026-07-23, abstract only.
    Candidate — awaiting Micky's verification.)*
  - **← anterior inferotemporal cortex / ventral temporal** — **carries:** view-invariant object and
    face identity. **Fan-in:** unknown. **The producer declares this region, but as a waypoint
    inside a class endpoint rather than as a target**: the inferotemporal entry's Outputs read
    "→ the distributed conceptual / semantic system (via temporal pole) — carries: object and face
    identity, invariant to position, size, pose, and lighting." The payloads agree. **Owed as a
    cross-file edit at the inferotemporal entry (`01_visual_pathway`): make this region a named target with its
    own line, rather than a parenthesis on the route to somewhere else.**
  - **← orbitofrontal cortex** — **carries:** value. **Payload otherwise unknown — owed.**
    **Fan-in:** unknown. **Declared at the producer's end as well as here**: the orbitofrontal /
    ventromedial prefrontal entry (`11_frontal_lobe`) declares "→ the temporal pole — carries:
    value," with its own payload otherwise owed. **The two ends agree on the payload and both mark
    the remainder owed.**
  - **← insular cortex** — **carries:** interoceptive context. **Payload otherwise unknown — owed.**
    **Fan-in:** unknown. **Declared at the producer's end as well as here**: the insula entry
    (`17_insula_claustrum_habenula`) declares "→ the temporal pole — carries: interoceptive
    context," payload otherwise owed, and names this region among its own Inputs as well. **Both
    limbs of the reciprocal pair it asserts are now written at that end.**
  - **← amygdala** — **carries:** the **valence tag** — a gain on perception, attention and memory
    encoding, carrying no identity information of its own, per the producer's declaration.
    **Fan-in:** unknown. **Declared at the producer's end as well as here**: the amygdala entry
    (`08_medial_temporal_lobe`) declares "→ the temporal pole, from the basal / accessory basal
    nuclei" — named, and **attributed to a sub-element this end has no counterpart for**. *(Payload transcribed from that entry, `08_medial_temporal_lobe`. **The orbitofrontal,
    insular and amygdala inputs are three separate lines because they carry three different
    payloads** — value, interoceptive context, and the valence tag — and all three producers now
    declare the edge by name, each marking its own remainder owed.)*
  - **← angular gyrus** (`06_posterior_parietal`) — **carries:** payload **owed** at both ends.
    **Fan-in:** unknown. **Written here from the producer's declaration**: the angular gyrus entry
    declares an output to "the distributed conceptual / semantic system via the temporal pole, the
    hippocampal formation, ventrolateral prefrontal cortex and the default-mode partners," names
    this region explicitly among its four targets, marks the payload owed, and records the edge as
    owed as a cross-file edit here. **The producer's line is a compound of four targets and one
    network and is owed a split**, so the arity at that end may change; the limb naming this region
    will not. *(Transcribed from the angular gyrus entry, `06_posterior_parietal`. Candidate —
    awaiting Micky's verification.)*

- **Outputs:**
  - **→ entorhinal cortex** (toward the hippocampal formation) — **carries:** an **amodal concept**
    — a representation of the thing that is no longer visual or auditory or tactile. **This is a
    phrase, not a type:** the payload has no units,
    no range, no frame, and no declared channel structure, and the one thing that *is* known about
    it is a negative — it has lost its modality. **Payload unknown — owed.** Recorded loudly,
    because the modality-loss is the only checkable property currently in hand. **Fan-out:**
    unknown.
    **Declared at the consumer's end as well as here**: the hippocampal formation entry
    (`08_medial_temporal_lobe`) declares "← the temporal pole, onto entorhinal cortex," carrying an
    amodal concept, **named on its own line rather than covered by the class endpoint beside it**,
    and marks the same payload owed. Entorhinal cortex is a sub-element of that entry, so this edge
    terminates on a sub-element and the line says which.
  - **→ rostral perirhinal cortex and posterior parahippocampal cortex** — **carries:** the same
    amodal concept; **payload unknown — owed. Fan-out:** unknown.
    **Neither far end has an entry in any file checked against this one.** The medial temporal lobe file holds
    three entries — hippocampal formation, amygdala, bed nucleus of the stria terminalis — and
    neither perirhinal nor parahippocampal cortex is among them. **This is corroborated from two
    further directions:** the inferotemporal entry (`01_visual_pathway`) declares an output "→
    perirhinal cortex (areas 35 and 36)" and names it explicitly as the anatomical step by which the
    ventral stream reaches the hippocampal formation, and the medial temporal lobe file records the
    same gap from its own side. **Three files' edges point at a region no file owns.**
    **Owed: give perirhinal and parahippocampal cortex entries, and decide which file owns them.**
    *(The dorsolateral subdivision's outputs are reported as reaching the entorhinal, rostral
    perirhinal and posterior parahippocampal cortices, which is what splits this line from the
    entorhinal one above. Class 1 — Muñoz-López et al. 2015 as reported in Córcoles-Parada et al. 2019;
    web search 2026-07-23, abstract only. Candidate.)*
  - **→ ventrolateral prefrontal cortex** — **carries:** the amodal concept, for controlled
    retrieval and selection. **Payload unknown — owed. Fan-out:** unknown. **Declared and typed at the
    consumer's end**: the ventrolateral prefrontal entry (`11_frontal_lobe`) declares "← the
    temporal pole — carries: an amodal concept," on its own line rather than inside the prose that
    named this region beside the inferotemporal cortex. **The payload is owed at both ends, and the
    two ends agree on what it is not.**
  - **→ amygdala** — **carries:** the amodal concept, for affective evaluation. **Payload unknown —
    owed. Fan-out:** unknown. **Declared at the consumer's end as well as here**: the amygdala entry
    (`08_medial_temporal_lobe`) declares "← the temporal pole — carries: an amodal concept, for
    affective evaluation," payload owed there as here. **The two sensory-cortex endpoints it names
    beside this one are this region's own sources**, so the amygdala receives the same content twice
    — once modality-bound and once amodal — and neither end says whether that is redundancy or two
    different signals. *(**The entorhinal, perirhinal/parahippocampal, ventrolateral-prefrontal and amygdala
    outputs are four separate lines because their far ends are in two different states** — three
    declared and typed at the consumer, and one with no entry in any file at all.)*
  - **→ the insula** — **carries:** payload **owed**. **Fan-out:** unknown. **Declared at the consumer's end
    as well as here**: the insula entry (`17_insula_claustrum_habenula`) names this
    region among its inputs, carrying "emotional, evaluative and social context," and marks that
    payload **owed** and "the entry's largest gap: 'context' is a function word, not a type with a
    range and a frame." Owed at both ends. *(Transcribed from the insula entry,
    `17_insula_claustrum_habenula`. Candidate — awaiting Micky's verification.)*

  
- **Internal structure and internal data flow:** *(From web search; abstracts and search excerpts
  only, **no full paper opened**. **Nothing here is verified for the source.**)*

  **Laminar sub-elements: the standard eight-layer block does not apply here, and it is not
  written.** This region is **paralimbic**, and its architecture changes **progressively from
  medial agranular limbic cortex toward more dorsolateral dysgranular paralimbic cortex** — so
  layer 4 is absent at one end of the region and thin at the other, and there is no single laminar
  set true of the whole entry. Transcribing the file's usual Class-3 block — which routes three
  edges through layer 4 — would assert a circuit this description denies over part of the region.
  **This is the second entry in the source where the boilerplate fails**, after primary motor cortex, and it fails for
  the same reason and a different one: primary motor cortex is agranular throughout, this region is agranular *in
  part*, so the block is wrong here in a place-dependent way rather than uniformly. **Laminar
  sub-elements: owed, per subdivision.**
  What is recorded of the laminar pattern, for the temporopolar cortex proper: **thin layer II**, a
  **size gradient of pyramids through layer III**, a **thin layer IV**, and **large dark pyramids in
  layer V** which fuse with a **layer VI that spreads out into the underlying white matter** —
  confirming the classical Brodmann and von Economo & Koskinas descriptions. *(Class 1 — Blaizot et al. 2010, human. Candidate.)*

  **The scope of this exception, recorded identically in five files.**
  The file's standard Class-3 laminar block — **1, 2, 3, 4, 5a, 5b, 6a, 6b** with **4 → 2/3**,
  **2/3 → 5a and 5b**, **6a → 4**, **6a → 5a**, **6b → 6a** and within-sub-element recurrence — is
  **not a default. It is a claim about granular isocortex**, and three of its edges route through
  layer 4. **Nine entries across five files cannot take it**: primary motor cortex (`05_sensorimotor_loop`,
  agranular throughout); the temporal pole (`07_anterior_temporal_lobe`, agranular medially on a gradient); the
  hippocampal formation (`08_medial_temporal_lobe`, three-layered allocortex); the cerebellar cortex (`10_cerebellum`,
  three-layered and not isocortex at all); and five entries in the frontal lobe (`11_frontal_lobe`) — premotor
  cortex, Broca's area, the right inferior frontal gyrus, the orbitofrontal / ventromedial entry and
  the anterior cingulate. **They fail it in four different ways** — uniformly agranular, agranular
  across a gradient, agranular across an internal border, and not isocortex — **so a single
  exception clause would not cover them.** **Owed at the design file: state where the block is
  defined that it applies to granular isocortex only**, rather than leaving each entry to discover
  the incompatibility on its own.


  **Divisional sub-elements: contested — how many there are is not agreed, and the gradient is not
  in dispute.** Four schemes are in the literature and they do not reduce to one another:
  - **Two** — a **lateral** temporopolar field and a **medial-and-ventral** one, the division
    reported for the first time in human in the study above and argued to have a counterpart in
    macaque and baboon. *(Class 1 — Blaizot et al. 2010, human.)*
  - **Three, by cytoarchitecture** — **dorsal**, **ventrolateral**, and **ventromedial**.
    *(Class 1 — Frontiers in Neuroanatomy 17:1240545, 2023, human.)*
  - **Three, by anatomical connectivity** — a **dorsal**, a **lateral** and a **medial** cluster.
    *(Class 1 — Fan et al. 2013, human, as reported in Neuroscience and Biobehavioral Reviews
    115:134, 2020.)*
  - **Four, by functional and anatomical network** — **dorsal**, **ventromedial**, **medial** and
    **anterolateral**, and the authors explicitly declined to draw a hard parcellation.
    *(Class 1 — Pascual et al. 2015, human, as reported in the same review.)*

  **Recorded as contested, not resolved by preference**, the same treatment the source gives 4B's
  layer number and the insula's subdivision count — and it is the same *kind* of object as the
  insula: a graded sheet that different instruments cut differently. **The region's edges carry the
  function either way**, and the next line is why that is not merely a formula here.

  **The subdivisions sort this entry's edges, and that is what makes the division load-bearing
  rather than descriptive.** Across the schemes the connectional assignments agree even where the
  boundaries do not:
  - **Dorsal / dorsolateral** — takes the **auditory** input from the rostral superior temporal
    gyrus, and emits to the **entorhinal, rostral perirhinal and posterior parahippocampal**
    cortices. Also reported as the subdivision strongly connected with **parietal** cortex.
  - **Ventrolateral / anterolateral** — the **default-semantic network** node.
  - **Ventromedial / medial** — connected with the **limbic and paralimbic** structures: amygdala,
    hippocampus, entorhinal and parahippocampal cortex, and orbitofrontal cortex, largely via the
    **uncinate fasciculus**.

  **So every edge in this entry belongs to a subdivision, and none of them says which.** The
  auditory input is dorsal, the amygdala and orbitofrontal inputs are ventromedial, the
  semantic outputs are ventrolateral. **Owed: assign each edge to a subdivision**, which would
  change the arity of the compound lines that remain and would also settle whether the visual input
  from the inferotemporal cortex arrives on the same subdivision as the auditory one — **the
  question the entry's Function turns on**, since the claimed operation is binding the two.
  *(Class 1 for the connectional assignments — Frontiers in Neuroanatomy 17:1240545, 2023;
  Córcoles-Parada et al. 2019; Fan et al. 2013 and Pascual et al. 2015 as reported in Neuroscience
  and Biobehavioral Reviews 115:134, 2020. Class 2 — the reading that these assignments sort this entry's existing edges is
  Claude's, offered to be checked. Web search 2026-07-23, abstracts only. Candidates.)*

  **Tangential sub-elements: unknown.**

  **Internal edges: owed, all of them.** No edge between any two subdivisions is recorded, in either
  direction, under any of the four schemes.

  **And the missing internal edge is the entry's whole claim.** The Function field says visual and
  auditory object representations are **bound into amodal concepts** here. The connectional evidence
  above puts the auditory input on the dorsal subdivision and the semantic output on the
  ventrolateral one. **So the binding, if it happens here, happens on an edge between subdivisions,
  and no such edge is written anywhere.** This is a **dangling requirement** in the payload rule's
  sense — a stated function with no declared substrate — and it stands alongside the same hole at
  the anterior intraparietal area's transform, the medial intraparietal area's frame mixture, the
  angular gyrus's binding, and the anterior insula's subjective feeling. **In every one of those
  cases the region whose payload cannot be typed is also the region whose internal mechanism is not
  written**, which is a pattern about the source's coverage and not a coincidence about five
  regions.
- **Neurons:** ~103M per hemisphere (Bothwell et al. 2001, in typical cases; via
  Wu & Amaral 2015 — verified human stereology). Same order as the Brodmann area 22 /
  area TA total (~145M), the neighbouring superior temporal gyrus association cortex.
  **No per-subdivision count is recorded**, and given that the subdivision count is itself
  contested, one could not currently be apportioned. **Owed.**
- **Synapses:** unknown.
- **Axons:** the **uncinate fasciculus** (to and from orbitofrontal cortex and the limbic
  structures), the **inferior longitudinal fasciculus**, the **middle longitudinal fasciculus**,
  and the **arcuate fasciculus** — the four major association pathways reported to supply this
  region's structural connectivity. **Counts unknown**, and which pathway carries which of this
  entry's edges is recorded only for the uncinate. *(Class 1 — Frontiers in Neuroanatomy
  17:1240545, 2023, human. Web search 2026-07-23, abstract only. Candidate — awaiting Micky's verification. **Three of the four have entries in
  `18_white_matter_tracts`, and that file declares this region by name** — one input line naming all
  four pathways and one output line over the uncinate, both routing-only with the payload owed at the
  region ends. **The middle longitudinal fasciculus has no entry there or anywhere**, which that file
  records as an owed correction at this entry; the sentence above is corrected to say *three*.)*
- **Grey-matter volume:** temporal-pole cortex ~5.0 cm³ per hemisphere (~5.04 ± 0.96 cm³,
  Blaizot et al. 2010; temporal-pole definitions vary, so soft). Density
  cross-check: ~103M / ~5.0 cm³ ≈ ~20,000 neurons/mm³ — typical association-cortex packing,
  well below V1's ~60,000.
- **White-matter volume:** unknown. **Myelination:** the region is **dysgranular to agranular** on
  the gradient recorded under Internal structure, and no g-ratio or intracortical-myelin measure is
  recorded. **Owed** — and worth taking, because at the insula the same postero-dorsal to
  antero-ventral gradient was found to be **myeloarchitectonic as well as laminar**, which would be
  the checkable form of the gradient claim here.
**Two coverage findings, recorded here because this is the entry whose edges reach them.**
**Perirhinal cortex and parahippocampal cortex have no entry in any file checked against this one**, and
two files' edges point at them — this entry's and the inferotemporal entry's, the latter naming
perirhinal cortex explicitly as the step by which the ventral stream reaches the hippocampal
formation. Separately, **eight of this entry's eleven edges are declared at both ends, and six of the eight
were written at the far end after this entry marked them owed** — the pattern of a one-entry file
whose edges get settled from the other side. Of the remaining three: the inferotemporal producer
covers this region inside a class endpoint, the auditory producer names it as a waypoint in a chain,
and the perirhinal / parahippocampal target has no entry anywhere.

---

---

## References

*(Under source design §2a: the citing line carries the key, and the authors, title, journal, volume,
pages and method sit here. Species stays inline. Every line below is a **candidate** awaiting
Micky's verification; none is verified. Each full reference given here was obtained by a web search
against publisher or journal records — no reference is written from recall. Keys reading **owed**
were not searched. **No line here carries a line number**: a pointer into the file goes stale on the
next edit and fails silently, and two of the pointers this section used to carry had already gone
stale against each other.)*

**10 distinct keys, 20 mentions. 5 searched; 5 owed.**

**This file has the smallest key list in the source and the highest proportion searched.** 5
of 10 keys carry a reference; the owed ones are *Fan et al. 2013*, *Pascual et al. 2015*,
*Neuroscience and Biobehavioral Reviews 115:134, 2020*, *Wu & Amaral 2015*, and the classical
*Brodmann* and *von Economo & Koskinas* descriptions, named without a year or an edition.

**The duplicate key is consolidated.** *Cerebral Cortex 20:2198, 2010* and *Insausti lineage,
PMC2923216* were the same paper — Blaizot et al. 2010 — cited under two short forms for two
different facts, with nothing in the file recording that the two rested on one source. All three
citing lines now use one key, and it is the author–date form the searched record supports.

**Two keys are a reporting paper and the paper it reports, and both are now named as such.**
*Córcoles-Parada et al. 2019* is cited for results its own text attributes to *Muñoz-López et al.
2015*; the file previously named the second as a lineage without a paper and the first by accession
only. The citing lines read *Muñoz-López et al. 2015 as reported in Córcoles-Parada et al. 2019*.

**One searched reference bears on a claim rather than only on a citation**, and it is flagged on its
own line rather than acted on: see the *Córcoles-Parada et al. 2019* entry on the share of area
38DL's input that is auditory, and the *Bothwell et al. 2001* entry on the provenance of this
entry's neuron count. Neither is a change to the entry; both are for Micky.

- **Blaizot et al. 2010** — Blaizot, X., Mansilla, F., Insausti, A.M., Constans, J.M., Salinas-Alamán, A., Pró-Sistiaga, P., Mohedano-Moriano, A. & Insausti, R. (2010). The human parahippocampal region: I. Temporal pole cytoarchitectonic and MRI correlation. *Cerebral Cortex* 20(9): 2198–2212; doi 10.1093/cercor/bhp289. **Human.** Cytoarchitectonics correlated with structural magnetic resonance images. *(Oxford University Press publisher record.)* **The file cited this paper under a second key, *Insausti lineage, PMC2923216*, for the grey-matter volume — the accession resolves to this paper. One key is now used at all three citing lines.** *(searched 2026-08-11; candidate.)*
- **Bothwell et al. 2001** — Bothwell, S., Meredith, G.E., Phillips, J., Staunton, H., Doherty, C., Grigorenko, E., Glazier, S., Deadwyler, S.A., O'Donovan, C.A. & Farrell, M. (2001). Neuronal hypertrophy in the neocortex of patients with temporal lobe epilepsy. *Journal of Neuroscience* 21(13): 4789–4800; doi 10.1523/JNEUROSCI.21-13-04789.2001; PMC6762344. Design-based stereology on Brodmann area 38, estimating volume and cell number. *(Society for Neuroscience publisher record and PubMed Central.)* **The sample is not normal brain, and the entry does not say so.** The material is **eight patients undergoing surgery for medically intractable temporal lobe epilepsy** (mean age 31.0 ± 4.1 years, range 10–48), with and without hippocampal sclerosis; area 38 is the tissue a temporal lobectomy removes, which is why it was available to count. The paper's subject is neuronal **hypertrophy and cortical atrophy** in that tissue. So the entry's ~103M — its only human neuron count, and marked *verified human stereology* — rests on **resected epileptic neocortex**. The entry's qualifier “in typical cases” presumably points at the non-sclerotic subgroup; whether that subgroup is a stand-in for normal cortex is a question for the citing line, not for this list. *(searched 2026-08-11; candidate.)*
- **Brodmann and von Economo & Koskinas** — **owed**: not searched.
- **Córcoles-Parada et al. 2019** — Córcoles-Parada, M., Ubero-Martínez, M., Morris, R.G.M., Insausti, R., Mishkin, M. & Muñoz-López, M. (2019). Frontal and insular input to the dorsolateral temporal pole in primates: implications for auditory memory. *Frontiers in Neuroscience* 13: 1099; doi 10.3389/fnins.2019.01099. **Primate.** *(Frontiers publisher record and PubMed Central.)* **Two findings, both for the citing lines rather than for this list.** **First, the file cites the reporting paper where the reporting paper cites a primary one.** Both claims the file attaches to this accession — that area 38DL's main input arises in the rostral superior temporal gyrus, and that its outputs reach the entorhinal, rostral perirhinal and posterior parahippocampal cortices — are attributed *inside* this 2019 paper to **Muñoz-López et al. 2015**, the entry above. The file's phrase *lineage as reported in* is doing exactly the right work, and the primary paper is now named. **Second, and load-bearing: this paper's own headline may cut against.** It reports that **about 50% of the cortical input to area 38DL comes from frontal and insular cortex** — medial frontal 25%, orbitofrontal 15%, insular 10% — with the rostral superior temporal gyrus auditory areas accounting for **30%**, the superior temporal sulcus polysensory area 10%, and medial temporal cortex 10%. So the auditory input is the **largest single temporal** source but not a majority of the whole, and's *principal input* is a claim the cited paper qualifies. The entry already declares orbitofrontal and insular inputs on separate lines; what it does not declare is that on this source's numbers those two together outweigh the auditory one. *(searched 2026-08-11; candidate.)*
- **Fan et al. 2013** — **owed**: not searched.
- **Frontiers in Neuroanatomy 17:1240545, 2023** — Structural connectivity of cytoarchitectonically distinct human left temporal pole subregions: a diffusion magnetic resonance imaging tractography study. *Frontiers in Neuroanatomy* 17: 1240545, 2023; doi 10.3389/fnana.2023.1240545. **Human.** *(Frontiers publisher record. **The author list was not captured by this search and is owed.**)* Two notes for the citing lines. **The study is of the *left* temporal pole**, whichand 236 do not say — and this entry elsewhere records a left/right question it leaves open. Its three subregions are the dorsal, ventrolateral and ventromedial ones the file names. *(searched 2026-08-11; candidate.)*
- **Muñoz-López et al. 2015** — Muñoz-López, M., Insausti, R., Mohedano-Moriano, A., Mishkin, M. & Saunders, R.C. (2015). Anatomical pathways for auditory memory II: information from rostral superior temporal gyrus to dorsolateral temporal pole and medial temporal cortex. *Frontiers in Neuroscience* 9: 158; doi 10.3389/fnins.2015.00158; PubMed 26041980; PMC4435056. **Macaque.** Retrograde (Fast Blue, Diamidino Yellow) and anterograde (biotinylated dextran amine) tracer injections in the rostral superior temporal gyrus and in area 38DL. *(Frontiers publisher record and PubMed.)* **This is the primary paper behind both claims the file attributes to the lineage** — see the PMC6861303 entry below. *(searched 2026-08-11; candidate.)*
- **Neuroscience and Biobehavioral Reviews 115:134, 2020** — **owed**: not searched.
- **Pascual et al. 2015** — **owed**: not searched.
- **Wu & Amaral 2015** — **owed**: not searched.
