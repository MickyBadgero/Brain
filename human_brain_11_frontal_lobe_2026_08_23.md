# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-23
---

---

# FILE 11 OF 20 — FRONTAL LOBE

**What is in this file.** The frontal lobe: premotor and supplementary motor areas, frontal eye fields, the two language-adjacent inferior frontal regions, dorsolateral and ventrolateral prefrontal cortex, orbitofrontal/ventromedial prefrontal cortex, anterior cingulate, and frontopolar cortex. This section holds the largest concentration of owed payloads in the source.

**Size:** 1675 lines, ~37.1k tokens / ~145 kB (estimated from bytes, not tokenised; kB = 1024 bytes, truncated). **Entries:** 9. **Edge lines:** 106 — 63 in, 43 out. **Internal structure slots:** 9 of 9. **Reference keys:** 45, over 64 mentions.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Premotor cortex and the supplementary motor areas (Brodmann area 6)**
- **Frontal eye fields (Brodmann area 8)**
- **Broca's area — inferior frontal gyrus (Brodmann area 44, pars opercularis; Brodmann area 45, pars triangularis)**
- **Right inferior frontal gyrus — affective-prosody production (right Brodmann area 44 / 45 homologue)**
- **Dorsolateral prefrontal cortex (Brodmann areas 9 and 46)**
- **Ventrolateral prefrontal cortex (Brodmann areas 45 and 47)**
- **Orbitofrontal / ventromedial prefrontal cortex (orbitofrontal cortex: Brodmann areas 11 and 13; ventromedial prefrontal cortex: Brodmann areas 14, 25 and 32)**
- **Anterior cingulate cortex (Brodmann areas 24 and 32)**
- **Frontopolar cortex (Brodmann area 10)**

**Two `##` sections in this file are commentary rather than entries** — the developmental-timing
section and the electrical-stimulation section — and the References section is a third. None of the
three is counted above.

**Cross-file status of the marks in this file.** Marks against file 8 (medial temporal lobe) are
**checked** against the far file. Marks against 4 (dorsal visual / parietal stream), 5 (sensorimotor
loop), 6 (posterior parietal), 7 (anterior temporal lobe), 9 (basal ganglia), 10 (cerebellum), 12
(thalamus), 13 (neuromodulatory systems), 14 (brainstem / midbrain / hypothalamus), 17 (insula /
claustrum / habenula / cingulate remainder) and 18 (white-matter tracts) are **unverified**: the far
file has been read beside this one, and has not been re-read against this file's current state.
Marks against 1 (visual pathway), 2 (auditory pathway), 3 (other senses), 15 (cranial-nerve nuclei),
16 (spinal cord), 19 and 20 are **unchecked**: those files have not been read beside this one at all.

---

# FRONTAL LOBE

*Neuron budget: the prefrontal cortex (granular frontal, anterior to the corpus callosum) holds
**~8% of all cortical neurons** — and, notably, that fraction is **constant across primates, not
human-expanded** (Gabi & Herculano-Houzel 2016; eight primate species including human). That is **~640M per
hemisphere** (of ~8B cortical per hemisphere), even though the prefrontal cortex occupies ~30% of
cortical surface — it is thick but low-density (granular, small-celled). Per-area human
stereological counts barely exist — the prefrontal cortex is the **least-counted cortex** — so the
sub-area counts below are soft, drawn against that ~640M budget. Primary motor cortex is in the
sensorimotor section; premotor is posterior frontal, outside the prefrontal 8%.*

***Eleven edges in three other files terminate on premotor sub-elements — F2, F4 and F5 — that
this file's single combined premotor entry does not name in its heading, and three more terminate on
a frontal-eye-field pursuit area that this heading does not name either.*** *Both are carried in the
Internal structure slots of the two entries that own them.*

---

## Premotor cortex and the supplementary motor areas (Brodmann area 6)

- **Function:** motor planning and sequencing — the stage between association cortex and primary
  motor cortex. Lateral premotor cortex maps sensory-guided reach and grasp; the supplementary and
  pre-supplementary motor areas handle internally-generated action sequences and initiation. Closes
  the sensorimotor loop into primary motor cortex.
  **This entry is one heading over at least five areas that other files address separately** — see
  Internal structure.
- **Inputs:**
  - **← superior parietal area 5** (principally area PE, and the caudal dorsal premotor target) —
    **carries:** limb position and the reach specification, in a **contested** reference frame —
    reported as body-, shoulder- and hand-centred across studies. **On the payload rule the frame
    is part of the payload, so this arrives with its payload unsettled.** **Fan-in:** unknown. **The
    producer declares it and names dorsal premotor cortex** (file 5), where the dispute is recorded
    in full.
  - **← the anterior intraparietal area**, onto **F5** — **carries:** a **hand configuration** —
    grip type (precision versus whole-hand) and the wrist and finger posture the object affords.
    **The payload change at the producer is a translation between ontologies**: an object's physical
    properties go in and a posture of the body comes out. **Fan-in:** unknown. **The producer
    declares it and names F5** (file 6), and records that this entry covered it under a class,
    carried no `carries:` line and no fan-in, and named no sub-element — marked there as an owed
    cross-file edit here.
  - **← the medial intraparietal area**, onto **F2** — **carries:** a **reach vector** — the
    direction, and more weakly the amplitude, of an intended reach, in a **mixture** of gaze-centred,
    hand-centred and intermediate frames, and **effector-specific** (arm, not eye). The mixed frame
    is not vagueness: the producer states the code genuinely is intermediate, and a consumer that
    assumes one pure frame will be wrong. **Fan-in:** unknown. **The producer declares it and names
    F2** (file 6), with the same owed edit recorded.
  - **← the ventral intraparietal area**, onto **F4** — **carries:** object location and motion in
    **head- and body-centred** coordinates — peripersonal space. **Fan-in:** unknown. **The producer
    declares it and names F4** (file 4), and records that this entry holds one combined premotor
    entry whose Inputs name no sub-element.
  - **← the supramarginal gyrus** — **carries:** a **praxis / action-sequence code** — the learned
    structure of a skilled act. **Payload only partly writable — owed**, at the producer's end:
    "the plan of a skilled action" has no units and no frame, and calling it a code does not make it
    one. **Fan-in:** unknown. **The producer declares it** (file 6) and records that this entry's
    Inputs name posterior parietal as a class.
  - **← the precuneus**, from its anterior sensorimotor sector — **carries:** reach and
    body-configuration signals, body-centred — the one edge out of that entry whose payload can be
    written. **Fan-in:** unknown. **The producer declares it** (file 6) and records this entry's
    class.
  - **← the primary somatosensory cortex (S1), from area 3a** — **carries:** limb and joint
    configuration — the feedback signal that closes the sensorimotor loop. **A payload type, not
    just a label:** single-unit recording during controlled digit movement distinguishes
    **single-digit position-scaled**, **multi-digit position-scaled** and **posture-selective**
    cells, so what arrives is a graded position variable per digit plus a categorical posture
    signal, not an undifferentiated "proprioception." **Fan-in:** unknown. **The producer declares it** (file 5), which records that this entry
    does not declare the input at all. *(Transcribed from the primary somatosensory
    cortex entry, file 5 — a derivation from another file in this source, not a literature check.
    **Candidate:** no source has been opened for this edge at either end.)*
  - **← the secondary somatosensory cortex (S2), principally from the parietal ventral area** —
    **carries:** tactile and proprioceptive information in a form usable for reaching and grasping.
    **Payload otherwise unknown — owed.** **Fan-in:** unknown. **The producer declares it** (file 5).
  - **← the ventral anterior / ventral lateral thalamus** — **carries:** the basal-ganglia
    **selection** (which action is released) and the cerebellar **correction** (how it is shaped),
    combined on one relay. **Fan-in:** unknown. **The producer declares it and names this area**,
    but as bare prose — that entry's Outputs slot reads "M1 [primary motor cortex], premotor, SMA
    [supplementary motor area]," with no `carries:` and no fan-out (file 12). **Owed at file 12:
    type it.**
  - **← the midcingulate cortex**, via the cingulate motor areas — **carries:** payload **owed**;
    at the producer's end this is the convergence of reward or non-reward outcome with action and
    spatial information, turned into a motor plan. **Fan-in:** unknown. **The producer declares it** (file 17), whose Outputs name the supplementary,
    pre-supplementary and premotor fields and primary motor cortex.
  - **← the anterior cingulate cortex** — **carries:** payload **unknown — owed**, at both ends.
    **Fan-in:** unknown. **The producer is in this file and declares it**, also owed there.
  - **← the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus** —
    **carries:** the **valence tag** — a gain on perception, attention and memory encoding, carrying
    no identity information of its own. **Payload otherwise owed. Fan-in:** unknown. Terminations in
    **ventral area 6**, continuous with the label in Brodmann area 45 at the Broca and ventrolateral
    entries, and lighter label in **dorsal area 6** on the medial wall and dorsal convexity, arriving
    continuous with the anterior cingulate label rather than separately. **Ipsilateral only**, and
    terminating in **deep layer I, layer II and layer VI**. **The producer declares it** (file 8), which split it out of a *widespread cortex* class by
    research and marked the edit owed here.
    **Which sub-element receives it is owed and is not resolvable from the producer's evidence.**
    This entry names **F2**, **F4** and **F5**; **F4 and F5 sit in ventral area 6**, where the denser
    half terminates, but the producing study divides area 6 dorsally and ventrally rather than by
    those names. **Owed: map the two divisions onto this entry's sub-elements, or leave the edge on
    the entry whole and say so.** *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015. Macaque. **Verified against the publisher record 2026-08-15**; full text read.)*
  - **← the dorsolateral and ventrolateral prefrontal cortex** (goals) — **carries:** payload
    **unknown — owed**; goal and task context. **Fan-in:** unknown. **Both producers are in this
    file**; the dorsolateral entry names premotor cortex among its outputs, the ventrolateral entry
    does not.
- **Outputs:**
  - **→ primary motor cortex** — **carries:** the planned action — a movement, already sequenced and
    shaped, not yet a muscle command. **Fan-out:** unknown. **The consumer declares it and names this
    area** (file 5), and records that this end is untyped — "**Owed at file 11: type it.**"
  - **→ the corticospinal tract**, directly, from a minority of cells — **carries:** payload
    **owed**; whether the direct premotor corticospinal projection carries the same content as the
    primary motor one is not stated here. **Fan-out:** unknown. **The consumer of the corticospinal
    tract is the muscles, which have no entry** — the primary motor entry records that boundary as
    the map's largest open boundary on the output side, and this edge inherits it.
  - **→ the basal ganglia**, to the motor striatum — **carries:** this area's contribution to the
    **candidate actions** — the set of competitors the striatum selects among. **Fan-out:** unknown.
    **The consumer declares its cortical source as a class** — "← nearly all of cortex" (file 9) —
    which covers this area without naming it, and that file records the class question as open and
    unresolved. **Not resolved here either.**
  - **→ superior parietal area 5** — **carries:** motor and premotor signals, plausibly including an
    **efference copy**; **payload owed — the producing studies establish the projection, not its
    content**, and the efference-copy reading is marked Class 2 at the far end. **Fan-out:**
    unknown. **The consumer declares it** (file 5), whose
    Inputs name "M1 [primary motor cortex], the supplementary motor area, and caudal dorsal premotor
    cortex."
  - **→ the medial intraparietal area**, from **F2**, and **→ the medial intraparietal area from
    F4 and F5** — **carries:** payload **owed. Fan-out:** unknown. **The consumer declares it** (file 6), which records these as a **return**
    limb from the very areas its output edge targets, and marks the far ends undeclared. **Written
    now.**
  - **→ the middle temporal area**? **No.** *(Checked and not written: the middle temporal entry
    (file 4) declares an input from the frontal eye field, not from this area. Recorded so the check
    is not repeated.)*
- **Internal structure and internal data flow:** *(This is the entry in the source where the
  sub-element deficit costs the most, because other files terminate edges on sub-elements this
  entry does not name.)*

  **Divisional sub-elements: at least five, and the heading names none of them.** The Function
  field names three groupings — lateral premotor, the supplementary motor area, and the
  pre-supplementary motor area — and other files name three further subdivisions that this entry
  must own: **F2** (dorsocaudal premotor, the reach target), **F4** (the peripersonal-space target)
  and **F5** (the grasp target). In the conventional correspondence F2 is dorsal premotor cortex and
  F4 and F5 are ventral premotor cortex, so the minimum set is **dorsal premotor (F2)**, **ventral
  premotor (F4 and F5)**, the **supplementary motor area** and the **pre-supplementary motor area**.
  *(Class 3 for the correspondence, which is standard; the sub-element names are taken from the
  files that terminate edges on them — 4, 5 and 6.)*

  **Eleven edges in three files terminate on these sub-elements, and the count is the finding.**
  File 6 sends the anterior intraparietal area to F5 and the medial intraparietal area to F2, and
  names F2, F4 and F5 as sources of a return limb; file 4 sends the ventral intraparietal area to
  F4; file 5 names caudal dorsal premotor cortex and the supplementary motor area as separate
  sources. **Every one of those was previously answered here by the word "premotor."** **Owed:
  assign each of this entry's twelve inputs and six outputs to a sub-element**, which is now
  possible for the six that arrive from files 4, 5 and 6 because their producers already name the
  target.

  **The supplementary and pre-supplementary areas are not lateral premotor cortex and the entry's
  own Function says so.** It assigns them internally-generated action sequences and initiation
  against lateral premotor's sensory-guided reach and grasp — **two different payload sources,
  external and internal** — and every edge above is written to the whole. **The split is
  load-bearing rather than descriptive**, because the parietal inputs are precisely the
  sensory-guided ones and the cingulate input is precisely the internally-generated one.

  **Laminar sub-elements: eight, with a caveat this entry shares with primary motor cortex** —
  **1, 2, 3, 4, 5a, 5b, 6a, 6b**. But the Neurons slot below describes this area as
  **agranular-to-dysgranular**, so layer 4 is thin or absent over part of it, and **the file's
  standard laminar block routes three edges through layer 4**. As at primary motor cortex and the
  temporal pole, transcribing it whole would assert a circuit the entry's own description denies
  over part of its extent. **The block is therefore not written and the internal edges read owed,
  per sub-element.** *(Class 3 for the eight; **Class 2** — the incompatibility is Claude's reading
  of this entry's own Neurons slot, offered to be checked. This is the **fourth** entry where the
  boilerplate fails.)*

  **Tangential sub-elements: owed.** The Function field asserts a mapping of sensory-guided reach
  and grasp, which implies a body map; whether it is somatotopic in the sense primary motor cortex's
  is, is not established here.

  **Internal edges: owed, all of them.** No edge between any two of the five sub-elements is
  recorded, in either direction — including the one the Function field implies most strongly, from
  the pre-supplementary to the supplementary motor area.
- **Neurons:** soft / unknown — posterior frontal, outside the prefrontal 8%; agranular-to-
  dysgranular, lower density than granular prefrontal cortex.
- **Synapses:** unknown. **Axons:** the corticospinal tract, in part (count unknown; the primary
  motor entry carries the ~1M-per-side order estimate for the tract as a whole).
  **Grey-matter volume:** unknown. **White-matter volume:** unknown. **Myelination:** unknown.

## Frontal eye fields (Brodmann area 8)

- **Function:** voluntary saccade generation and endogenous control of gaze and attention — the
  frontal node of the oculomotor loop, closing the lateral-intraparietal → frontal-eye-field →
  superior-colliculus circuit.
- **Inputs:**
  - **← the lateral intraparietal area** — **carries:** a **priority (salience) map** — one scalar
    per retinotopic location, ranking it by behavioural priority (bottom-up salience plus top-down
    attention plus reward), modality-free. **Fan-in:** unknown. **The producer declares it and names
    this area** (file 4), and records that this entry's Inputs name it. Two-ended and agreeing.
  - **← posterior parietal cortex** (beyond the lateral intraparietal area) — **carries:** payload
    **owed. This endpoint is a class** and does not resolve; no other parietal entry declares an output to this area. **Owed: name the source, or
    withdraw.** **Fan-in:** unknown.
  - **← the dorsolateral prefrontal cortex** (goals) — **carries:** payload **unknown — owed**;
    goal and task context. **Fan-in:** unknown. **The producer is in this file and names this area
    among its outputs**, untyped there.
  - **← the mediodorsal thalamus** — **carries:** **no categorical content** — a modulatory
    amplification of this cortex's own recurrent activity, sustaining representations that are
    generated in and belong to the cortex. **Fan-in:** unknown. **The producer declares it as a
    class that covers all prefrontal divisions** (file 12). *(Payload transcribed from that entry, which is Class 1 there and rests on Schmitt et al. 2017, mouse — **verified against the journal record 2026-08-12**, per the reference section below.)*
  - **← the caudal auditory belt, directly** — **carries:** sound-source location, as an **opponent
    hemifield rate code** and **not** as a map. Declared at the belt's end; this area is a direct target of the auditory "where" stream, which is the plainest available
    statement of what that stream is *for* — moving the eyes to a sound. **Fan-in:** unknown.
    **Far end in file `02_auditory_pathway`; unchecked.** *(Class 1 — Romanski et
    al. 1999, rhesus. **Verified against the journal record 2026-08-12**; see the reference section.)*
- **Outputs:**
  - **→ the superior colliculus** — **carries:** a saccade command — the selected target. **Payload
    otherwise unknown — owed. Fan-out:** unknown. **Far end in file `14_brainstem_midbrain_hypothalamus`; the collicular entry is unchecked.**
  - **→ brainstem saccade generators** — **carries:** payload **owed. This endpoint is a class**
    and the cranial-nerve-nuclei file (`15_cranial_nerve_nuclei`) is unchecked as well as unresolved. **Fan-out:** unknown.
  - **→ the lateral intraparietal area** (corollary discharge / efference copy of the saccade
    command) — **carries:** an efference copy of the impending saccade, which is what lets the
    consumer remap its priority map across the movement. **Fan-out:** unknown. **The consumer
    declares it** (file 4) and records that the relay path is stated as running through the
    mediodorsal thalamus, but that **the mediodorsal entry names prefrontal cortex only**, so the
    relay nucleus is unnamed. **Owed at file 12, or here: name the relay.**
  - **→ the middle temporal area**, terminating in **all cortical layers** — **carries:** the
    spatial code (the far end types it more fully). **Fan-out:** unknown. **The consumer declares it** (file 4).
  - **→ the medial superior temporal area**, reciprocally, **from the pursuit area** — **carries:**
    pursuit and eye-movement signals; **payload owed** at both ends. **Fan-out:** unknown.
    **The consumer declares it** (file 4).
  - **→ the ventral intraparietal area**, reciprocally, **from the pursuit area** — **carries:**
    payload **owed. Fan-out:** unknown. **The consumer declares it** (file 4). **Written
    now.**
- **Internal structure and internal data flow:**


  **Divisional sub-elements: two, and the second is named by another file and not by this heading.** The
  **saccade area** and the **pursuit area**. **Three edges in file 4 terminate on the pursuit area
  by name** — from the medial superior temporal area reciprocally, and from the ventral
  intraparietal area reciprocally — and that file records against each that **this entry names no
  pursuit area and no pursuit function**, marking the edits owed here.
  **The Function field still does not mention pursuit**, and until it does the entry claims a
  saccade area's job under a heading that owns two areas. **Owed: give the pursuit area a function
  statement, and say whether the two areas share afferents.** *(Class 1 for the pursuit area's
  existence and its parietal connections — the sources are recorded at the medial superior temporal
  and ventral intraparietal entries, file 4. **Candidate:** the sources are recorded at that entry and
  none was opened here.)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. Granular
  frontal isocortex, unlike the premotor entry above. *(Class 3.)*

  **Tangential sub-elements: owed.** A saccade area that generates movements to retinotopic targets
  implies a motor map of saccade vectors; whether it is a compartmentation an edge could terminate
  on is not established here.

  **Internal edges — laminar.** *(All **Class 3**.)* **4 → 2/3**; **2/3 → 5a and 5b** with
  reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated;
  **within-sub-element recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — saccade area ↔ pursuit area: owed.** None is recorded, and the two movement
  classes must be coordinated somewhere, since a pursuit movement is interrupted by saccades.
- **Neurons:** soft / unknown. **Synapses / Axons / volumes / Myelination:** unknown.

## Broca's area — inferior frontal gyrus (Brodmann area 44, pars opercularis; Brodmann area 45, pars triangularis)

- **Function:** speech production and syntax. **Brodmann area 44** (agranular, premotor-adjacent) —
  phonological and articulatory sequencing, and hierarchical or syntactic structure; **Brodmann area
  45** (granular) — controlled semantic retrieval and selection. Strongly left-lateralised. The
  frontal terminus of the auditory dorsal ("where" / audiomotor) stream.
- **Inputs:**
  - **← the posterior superior temporal gyrus and area Spt** (audiomotor), via the **arcuate
    fasciculus** — **carries:** the auditory-to-motor mapping and phonological form. **Payload
    otherwise unknown — owed. Fan-in:** unknown. **Far end in file `02_auditory_pathway`; unchecked.** The tract is recorded in the white-matter file, which notes a rare absolute
    estimate against it: **direct connections between the posterior temporal and inferior frontal
    language regions are surprisingly sparse, under ~5% of the axons in the arcuate trunk** — a
    median of about 6,200 axons between areas within a hemisphere. **That is a fan figure for this
    edge and it is not in the fan-in slot**, because it counts the tract's inter-areal axons rather
    than contacts per cell. **Owed: reconcile the two measures.**
  - **← the supramarginal gyrus**, via the arcuate fasciculus and superior longitudinal fasciculus
    III — **carries:** a **praxis / action-sequence code** and, on the left, a **phonological code**
    — the sound-form of words for the articulatory route. **Payload only partly writable — owed** at
    the producer's end. **Fan-in:** unknown. **The producer declares it** (file 6), which records that this entry's Inputs name the posterior superior
    temporal gyrus, ventrolateral prefrontal cortex and premotor cortex, and **not** the
    supramarginal gyrus — although this entry's Outputs name a reciprocal temporoparietal link.
  - **← the ventrolateral prefrontal cortex** — **carries:** payload **unknown — owed**; controlled
    semantic retrieval and selection, in the producer's terms. **Fan-in:** unknown. **The producer
    is in this file and names this area among its outputs**, untyped there.
  - **← premotor cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The producer
    is in this file and does not declare it**: that entry's Outputs name primary motor cortex, the
    corticospinal tract, the basal ganglia and three parietal targets. **Owed at that entry.**
- **Outputs:**
  - **→ premotor and primary motor cortex** (articulation) — **carries:** the articulatory plan —
    the phonological and syntactic structure rendered as a motor sequence. **Payload otherwise
    unknown — owed**, and this is the entry's central untyped payload: what a *syntactic structure*
    is, on a wire, has no units, no range and no frame. **Fan-out:** unknown. **The premotor
    consumer is in this file and does not declare it** — see that entry's Inputs. **Owed at that
    entry.**
  - **→ temporoparietal cortex**, reciprocally — **carries:** payload **owed. This endpoint is a
    class**; the one member that resolves is the supramarginal gyrus, which declares the reciprocal
    input (file 6). **Owed: name the others, or narrow the endpoint.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(The entry's Function field names two sub-areas,
  assigns each a distinct job, and — unusually — records that they differ in laminar type.)*

  **Divisional sub-elements: four, of which two are named in the heading** — **Brodmann
  area 44 (pars opercularis)** and **Brodmann area 45 (pars triangularis)**, each of which
  subdivides. Receptor architecture splits **Brodmann area 44 into dorsal 44d and ventral 44v**, and
  **Brodmann area 45 into anterior 45a and posterior 45p**; a cytoarchitectonic lineage splits
  Brodmann area 45 into a **rostral 45A** and a **caudal 45B**. **Whether 45A/45B and 45a/45p are
  one border under two names was not established.** *(Class 1 — 44d/44v and 45a/45p: Amunts et al. 2010, human; 45A/45B: the Petrides & Pandya cytoarchitectonic lineage. Located by web search 2026-07-23; secondary and encyclopaedic sources, no primary paper opened. **Candidates:** what was opened was not the record that would settle these subdivisions.)*

  **Brodmann area 45 is claimed by this entry and by the ventrolateral prefrontal entry, and both
  claims are real.** Broca's area is classically Brodmann area 44 plus Brodmann area 45; that entry
  is Brodmann area 45 plus Brodmann area 47. **Brodmann area 45 is the member the two conventional
  groupings share**, so the overlap is inherited from the naming schemes rather than introduced by
  this file. The suggested resolution — **45B / 45p to this entry, 45A / 45a to the ventrolateral
  one** — is recorded in full at that entry, along with the finding that the Brodmann area 44 /
  Brodmann area 45 border itself sits on sulci that are absent or displaced in a large fraction of
  hemispheres. **Until it is settled, the "→ Broca's area" edge written at that entry crosses a
  boundary whose location is not agreed.**

  **The laminar description of Brodmann area 45 is specific and was not in this file.** Layer III
  holds small to medium pyramidal cells in its upper part and, in its deeper part, **clusters of
  large, deeply stained, densely packed pyramidal neurons**; **layer IV is well developed**. Layer
  Va holds medium pyramidal cells and layer Vb is cell-sparse, so **layer VI is clearly separated
  from Va**. **The combination of the deep-layer-III clusters with a well-developed layer 4 is what
  distinguishes this area from all its neighbours** — which is the sharpest laminar signature
  recorded anywhere in this file, and it is a genuine sub-element-level fact rather than the generic
  block. *(Class 1 — the Brodmann / Sarkissov / Amunts cytoarchitectonic lineage as summarised in
  the secondary literature; web search 2026-07-23, no primary paper opened. Candidate.)*

  **The two differ in laminar type, and that is stated in the entry and not carried anywhere else.**
  Brodmann area 44 is **agranular**, Brodmann area 45 is **granular** with a thicker layer 4. **So
  the file's standard eight-layer block is correct for Brodmann area 45 and wrong for Brodmann area
  44**, within one entry — a case the source has not met before, since primary motor cortex is
  agranular throughout and the temporal pole varies along a gradient rather than across a border.
  **The block is written for Brodmann area 45 only.** *(Class 3 for the laminar sets; the
  agranular/granular difference is Class 1 and already in this entry's Myelination slot.)*

  **Laminar sub-elements: eight in Brodmann area 45** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**. **Seven in
  Brodmann area 44** — **1, 2, 3, 5a, 5b, 6a, 6b**, layer 4 thin or absent, as at primary motor
  cortex.

  **The sub-elements sort this entry's edges and no edge above says which it reaches.** The Function
  field assigns phonological and articulatory sequencing to Brodmann area 44 and controlled semantic
  retrieval to Brodmann area 45; the audiomotor input and the articulatory output are Brodmann area
  44's business, the ventrolateral prefrontal input and the semantic side Brodmann area 45's.
  **Owed: assign each edge**, which would also settle whether the supramarginal gyrus's two payloads
  — praxis and phonological — arrive on the same sub-element.

  **Tangential sub-elements: unknown.**

  **Internal edges — Brodmann area 45 → Brodmann area 44: owed.** The Function field's account is a
  pipeline from semantic selection to articulatory sequencing, which requires an edge between the
  two sub-areas, and none is recorded.

  **Internal edges — laminar, Brodmann area 45 only.** *(Class 3.)* **4 → 2/3**; **2/3 → 5a and 5b**
  with reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**; **6b → 6a**; within-sub-element
  recurrence. **For Brodmann area 44 the internal edges are owed**, as at primary motor cortex.
- **Neurons:** soft — no absolute count in hand, but Brodmann area 44 and Brodmann area 45 are among
  the few frontal areas with human stereology (Uylings, Jacobsen, Zilles & Amunts 2006, human: volume and total neuron number, left and right, in five men and five women — a significant left-greater-than-right neuron-number asymmetry in male Brodmann area 44). Human Brodmann area 44
  and Brodmann area 45 are up to ~6.6× larger than the chimpanzee homologue (Schenker et al.); the
  absolute per-area count sits in that lineage but is not extractable here.
- **Synapses:** unknown. **Axons:** the arcuate fasciculus and superior longitudinal fasciculus
  (counts unknown as a tract; the ~6,200-axon inter-areal median is recorded on the input edge
  above). **Grey-matter volume:** Brodmann area 44 ~3.8 cm³ left / ~2.5 cm³ right (Amunts et al.,
  human — a ~1.5× leftward asymmetry). **White-matter volume:** unknown. **Myelination:** Brodmann
  area 44 agranular, Brodmann area 45 granular (thicker layer 4).

## Right inferior frontal gyrus — affective-prosody production (right Brodmann area 44 / 45 homologue, isocortex)

- **Function:** the **production / expressive** node for **affective (emotional) prosody** — the
  right-hemisphere homologue of Broca's area (right Brodmann areas 44 and 45), the frontal
  complement to the right perceptual prosodic homologues already in the Auditory pathway. On Ross's
  classic account the right hemisphere organises the **affective components of language** the way
  the left organises the propositional ones: a right anterior or frontal lesion produces **motor
  (expressive) aprosodia** — speech gone flat and monotone, unable to *impose* emotional intonation
  — mirroring Broca's aphasia, while right posterior lesions give receptive aprosodia (the
  perceptual side, the right superior temporal homologues) (Ross 1981, "the aprosodias"; Ross &
  Monnot 2008). The clinical weight is real: aprosodia after right-hemisphere stroke is about as
  common as aphasia after left-hemisphere stroke (Gorelick & Ross 1987). The lateralisation is a
  **bias, not a clean dichotomy** — producing emotional prosody activates the inferior frontal gyrus
  **bilaterally** (Brodmann areas 44, 45 and 47, extending into anterior insula) with a **larger
  right-hemisphere extent** — so this is the right-dominant end of a bilateral network, in the same
  spirit as the primary auditory temporal / spectral asymmetry.
- **Inputs:**
  - **← the right auditory prosodic stream** (right superior temporal gyrus and sulcus homologues)
    — **carries:** payload **owed**; the perceptual side of affective prosody. **Fan-in:** unknown.
    **Far end in file `02_auditory_pathway`; unchecked.**
  - **← the amygdala**, from the **basal and accessory basal** nuclei — **carries:** the **valence
    tag** — a gain on perception, attention and memory encoding, carrying no identity information of
    its own. **Fan-in:** unknown. **The producer declares it and names this area** (file 8), where
    this area is one of five cortical consumers split out of a class endpoint.
  - **← the anterior insula** — **carries:** the **salience signal** — *this event is behaviourally
    relevant now*. **Payload otherwise unknown — owed** at the producer's end, which records that
    whether what leaves is a scalar, a pointer or a switching command is not established.
    **Fan-in:** unknown. **The producer declares its cortical target as a class** — "→ Anterior
    cingulate cortex and prefrontal cortex" (file 17) — which covers this area without naming it.
    **Owed as a cross-file edit at that entry (file 17).**
  - **← the orbitofrontal cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown.
    **The producer is in this file and declares it**: the orbitofrontal / ventromedial entry carries `→ the right inferior frontal gyrus` in its Outputs. **Two-ended.**
  - **← premotor cortex** — **carries:** payload **unknown — owed. Fan-in:** unknown. **The producer
    is in this file and does not declare it. Owed at that entry.**
  - **← the contralateral inferior frontal gyrus**, via the **corpus callosum** — **carries:**
    payload **owed. Fan-in:** unknown. **The tract has an entry** (file 18), which records that
    callosal origin is layers 3 and 5 and termination is throughout layers 2–6, densest in 2 and 3
    and sparsest in layer 4 — **so the callosal input avoids the layer the thalamic driver targets**
    — and that all callosal fibres are excitatory, the inhibitory effects being feedforward through
    local interneurons. **That laminar detail belongs on this edge and was not here.** *(Transcribed
    from the corpus callosum entry, file 18. Candidate.)*
- **Outputs:**
  - **→ premotor and primary motor cortex** — **carries:** the **articulatory prosody** — pitch,
    loudness, timing and stress. **This is the one payload in this entry that can nearly be typed**:
    each of the four is a physical parameter with a scale, unlike the "affective components" the
    Function field otherwise trades in. **Payload otherwise unknown — owed**, because the mapping
    from an emotional category to those four parameters is not stated. **Fan-out:** unknown. **The
    premotor consumer is in this file and does not declare it. Owed at that entry.**
  - **→ right temporoparietal cortex**, reciprocally — **carries:** payload **owed**; the
    production terminus that the auditory pathway's right-prosodic-homologues entry and its summary
    both pointed to. **This endpoint is a class. Fan-out:** unknown. **Far end in file `02_auditory_pathway`; unchecked.**
- **Internal structure and internal data flow:**


  **Divisional sub-elements: two, by homology** — the right **Brodmann area 44** and right
  **Brodmann area 45**, mirroring the left-hemisphere entry above, which records that Brodmann area
  44 is agranular and Brodmann area 45 granular. **Whether that laminar difference holds on the
  right is not established here**, and it is exactly the kind of thing the documented
  left-greater-than-right asymmetry might not preserve. **Owed.**

  **The Function field extends this area beyond its own heading and the entry does not follow
  through.** It records that producing emotional prosody activates Brodmann area 44, Brodmann area
  45 **and Brodmann area 47**, extending into **anterior insula**. Brodmann area 47 is held by the
  ventrolateral prefrontal entry in this file and the anterior insula by file 17. **So the
  functional network named here crosses two entry boundaries and one file boundary, and no edge in
  this entry connects to either.** **Owed: write the edges, or state that the activation is
  co-activation rather than connection.**

  **Laminar sub-elements:** as the left-hemisphere entry — **eight in Brodmann area 45**, **seven in
  Brodmann area 44**; see there. **Contested for this side.**

  **Tangential sub-elements: unknown. Internal edges: owed, all of them.**
- **Neurons:** soft / unknown — no clean human per-area count; but it is the **smaller side** of the
  documented left-greater-than-right Brodmann area 44 volume and neuron-number asymmetry (Amunts,
  Uylings & Zilles, the lineage the Broca entry names), so once the left side is firmed the right
  homologue is bounded below it.
- **Synapses:** unknown. **Axons:** callosal and right-hemisphere association fibres (counts
  unknown). **Grey-matter volume:** unknown — but bounded above by the left Brodmann area 44 figure
  of ~2.5 cm³ right recorded at the Broca entry, which is the same measurement. **Owed: reconcile
  the two entries, which record one asymmetry from two sides.** **White-matter volume:** unknown.
  **Myelination:** unknown.

## Dorsolateral prefrontal cortex (Brodmann areas 9 and 46)

- **Function:** working memory, executive control, goal maintenance and top-down attention —
  holding and manipulating information across delays and biasing posterior cortex toward goals. The
  action-control, "where" apex of the prefrontal cortex.
- **Inputs:**
  - **← the lateral intraparietal area** — **carries:** the **priority (salience) map** — one scalar
    per retinotopic location, ranking it by behavioural priority, modality-free. **Fan-in:**
    unknown. **The producer declares it and names this area** (file 4): "→ prefrontal area 46 —
    carries: the same priority map. **The far end agrees and names this area**." Two-ended and
    agreeing.
  - **← the angular gyrus** (macaque area 7a) — **carries:** payload **owed**, and the producer
    marks its output payload the loudest owed in that file. **Fan-in:** unknown. **The producer
    declares an output to the ventrolateral prefrontal cortex and not to this area** (file 6).
    **So the "area 7a" term in the previous prose line has no producer end here. Owed: establish
    whether this edge exists, or withdraw it.**
  - **← the mediodorsal thalamus** — **carries:** **no categorical content** — a modulatory
    amplification of this cortex's own recurrent connectivity, sustaining rule and working-memory
    representations that are generated in, and belong to, the cortex. **The thalamus is a temporal
    scaffold for those representations, not their source.** **Fan-in:** unknown. **The producer
    declares it as a class covering all prefrontal divisions** (file 12). **This is the edge the
    entry's headline function depends on**: working memory across delays is what the amplification
    sustains. *(Class 1 — Schmitt et al. 2017. Mouse. **Verified against the journal record 2026-08-12**; see the reference section.)*
  - **← the ventral tegmental area** (the mesocortical projection) — **carries:** payload **owed**;
    dopamine. **Fan-in:** unknown. **The producer declares it** (file 13), whose Outputs name
    prefrontal cortex.
  - **← other prefrontal cortex** — **carries:** payload **owed. This endpoint is a class** and does
    not resolve; the in-file candidates are the ventrolateral, orbitofrontal, anterior cingulate and
    frontopolar entries, of which the anterior cingulate declares an output to this area and the
    frontopolar declares one to a class that covers it. **Owed: name the others, or withdraw.**
    **Fan-in:** unknown.
  - **← the anterior cingulate cortex** — **carries:** a signal **recruiting cognitive control under
    conflict**. The conflict content has **no coordinate frame and no explicit decoded format of its
    own**; it acts by **raising the gain** on the already-framed coding of the correct sensorimotor
    response. **Fan-in:** unknown. **The producer is in this file and declares it, typed and verified.** *(Class 1 — **Ebitz et al. 2020**. Human, epilepsy patients across two cohorts. **Verified against the bioRxiv record 2026-08-15.** **The study is a preprint and was not peer-reviewed.** **So the class mark on this edge stands on unrefereed work, and that is recorded on the edge rather than in the reference section, because it bears on how much weight the edge can carry.**)* **This edge is resisted, not owed** — the absence of an explicit conflict-coding
    axis was decoded rather than merely unmeasured.)*
  - **← the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus** —
    **carries:** the **valence tag**, as at the other prefrontal consumers. **Payload otherwise
    owed. Fan-in:** unknown. Terminations in **Brodmann area 9** medially and laterally, and
    **patchily in area 46**, in the lower bank of the principal sulcus; **ipsilateral only**, in
    **deep layer I, layer II and layer VI**. **This is the lightest and least consistent of the
    producer's four lateral edges** — the area 46 label was present in one hemisphere and absent in
    the other of the same animal, and absent altogether in a second case. **The producer declares it** (file 8).
    **The area 46 limb lands on this entry's own unused divisional sub-elements**, which the
    Internal structure slot records as named in the heading and used by no edge; the producer names
    both areas, so this is the first edge here that could be assigned. **Owed: assign it.** *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015. Macaque. **Verified against the publisher record 2026-08-15**; full text read.)*
  - **← the caudal auditory belt, directly onto the caudal principal sulcus** — **carries:**
    sound-source location, as an opponent hemifield rate code. Declared at the belt's end. **Fan-in:** unknown. **Far end in file `02_auditory_pathway`; unchecked.** *(Class 1 — Romanski et al. 1999, rhesus. **Verified against the journal record 2026-08-12**; see the reference section.)*
- **Outputs:**
  - **→ the lateral intraparietal area** — **carries:** **top-down goal relevance — a weighting, not
    a stimulus.** **Fan-out:** unknown. **The consumer declares it and names area 46** (file 4), and
    records that this entry's Outputs answer it **only as a class** — "parietal and sensory cortex
    (top-down bias)".
  - **→ the anterior intraparietal area** — **carries:** **goal / task context. Payload otherwise
    unknown — owed. Fan-out:** unknown. **The consumer declares an input from prefrontal areas 46
    and 12** (file 6) and records that this entry's Outputs are "a class that is compatible with
    this payload and does not name this area".
  - **→ sensory cortex** (top-down bias) — **carries:** payload **owed. This endpoint remains a
    class** after the two parietal members above are split out. The visual and auditory files are unchecked as well as unresolved. **Owed: name the sensory areas.**
    **Fan-out:** unknown.
  - **→ the frontal eye fields** — **carries:** payload **unknown — owed**; goal and task context.
    **Fan-out:** unknown. **The consumer is in this file and declares it**, untyped there.
  - **→ premotor cortex** — **carries:** payload **unknown — owed. Fan-out:** unknown. **The
    consumer is in this file** and now declares it, split out of its prose term "prefrontal (goals)".
  - **→ the basal ganglia**, to the associative striatum — **carries:** this area's contribution to
    the **candidate actions**. **Fan-out:** unknown. **The consumer declares its cortical source as
    a class** (file 9), which records the class question as open.
  - **→ the anterior cingulate cortex** — **carries:** payload **unknown — owed** at both ends.
    **Fan-out:** unknown. **The consumer is in this file and declares it**, owed there too.
- **Internal structure and internal data flow:**


  **Divisional sub-elements: two, named in the heading and used by no edge** — **Brodmann area 9**
  and **Brodmann area 46**. Other files address this entry as "prefrontal area 46" specifically —
  the lateral intraparietal and anterior intraparietal entries both do — **so the finer name is in
  use elsewhere and unavailable here.** **Owed: assign each edge to Brodmann area 9 or Brodmann area
  46**, beginning with the two parietal ones, whose producers already say 46 — **and with the amygdalar input, whose producer names both areas and distinguishes them by density and by consistency.**

  **A third subdivision is named by an edge and not by the heading.** The auditory input arrives
  "onto the **caudal principal sulcus**", which is a location within Brodmann area 46 rather than
  either named area. **Owed: say whether the caudal principal sulcus is a sub-element of Brodmann
  area 46 or a separate one.**

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. Granular
  prefrontal isocortex — thick but low-density, per the file's neuron budget. *(Class 3.)*

  **Tangential sub-elements: one — the *stripe*, and it is the only tangential
  partition anywhere in this file.** *(**Class 2**: obtained by search 2026-08-14, macaque. The studies are named on each block below and were opened; **what is Class 2 is the reading placed on them, not their existence.**
  The dimensions below are the sources' and the reading is marked where it occurs.)*

  **The pattern is specific to this entry's areas among the cortical areas tested.** Small biocytin
  injections comparing laterally-spreading pyramidal projections across macaque cortex gave a
  **punctate, discontinuous patch** pattern in visual areas V1, V2 and V4, somatosensory areas 3b, 1
  and 2, and motor area 4 — and **stripe-like connectivity in prefrontal areas 9 and 46**, which are
  exactly the two divisional sub-elements named above. *(Lund, Yoshioka & Levitt 1993. Macaque.)*

  **Extents, and this is the first tangential extent in this file.** Stripe **width ≈ 0.2–0.8 mm**;
  the one study reporting both dimensions gives **≈ 275 × 1,800 μm**; **lateral spread 2–8 mm within
  the supragranular layers.** **A pitch relation is reported rather than assumed:** the width of the
  **terminal-free gaps is closely scaled to the width of the stripes** — so the axis has a spacing
  rule and not only a member size. *(Lund, Yoshioka & Levitt 1993; Levitt, Lewis, Yoshioka & Lund
  1993; Pucak et al. 1996.)*

  **Long-range inputs land on the same axis, at the same dimensions.** Anterogradely- and
  retrogradely-labelled **associational** stripes were very similar to each other **and to the
  intrinsic stripes**, with divergence, convergence and reciprocity characterising both. The authors
  suggest from the consistent size that the stripes **may represent basic functional units** of
  primate prefrontal cortex. *(Pucak et al. 1996. Macaque. **The "basic functional unit" reading is the authors' suggestion and
  is not an established result.**)*

  **The stripe projection is excitatory onto pyramidal cells, which constrains what an algorithm on
  this axis can be.** Biotinylated-dextran-amine injection into **layer 3 of macaque area 9**,
  examined by electron microscopy: the labelled intrinsic collaterals formed **exclusively asymmetric
  synapses**, and **95.6% of postsynaptic structures were dendritic spines**, presumably of other
  pyramidal neurons. *(Melchitzky et al. 1998. Macaque.)* **So lateral spread on this axis is excitation and not inhibition, and any competition
  between stripes must be built from something this measurement does not contain.**

  **What this does and does not license, stated because the distinction decides whether edges move.**
  **It names the axis and gives it an extent. It does not assign any producer to any stripe.** Nothing
  found establishes that a *named* far end — the lateral intraparietal input, the mediodorsal
  thalamic input, the anterior cingulate input — terminates in a stripe distinguishable from the
  others. **Membership: to derive.** **No edge in this file or in the architecture rung may be
  re-terminated on a named stripe until a producer-to-stripe assignment exists**, because assigning
  one would invent the arity, which §2 forbids. **The axis therefore blocks allocation rather than
  enabling it** — the same state as the sector axes recorded in file 12.

  **Coverage, so the silence is not read as a negative.** These studies examined **areas 9 and 46 in
  macaque**. **Not human**, and **not this file's other eight entries**, which are **unchecked rather
  than negative** on this axis. **Owed: whether the stripe pattern holds in human, and whether it
  holds in Brodmann areas 45, 47, 10, 11, 13, 14, 25, 32, 24, 8 and 6.**

  **Why the axis was searched for, recorded so the motivation is visible.** Working memory across
  delays is standardly attributed to recurrent local connectivity, and the mediodorsal input above is
  typed as amplifying exactly that — **so this entry's headline function is a claim about an internal
  edge, and the internal edge is not written.** *(That a partition of this shape — a set of sources
  landing on interdigitated territory of a fixed size — is the shape of a comparison or a competition
  rather than of a filter, and so narrows the algorithm class, is Claude's reading, offered to be
  checked. It is not a finding, and the excitatory-target result above is a reason to hold it
  loosely.)*

  **Internal edges — laminar.** *(All **Class 3**.)* **4 → 2/3**; **2/3 → 5a and 5b** with
  reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated;
  **within-sub-element recurrence in 4 and 2/3**.

  **Internal edges — the recurrence that holds the representation: owed, and it is the entry's whole
  claim.** The Function field says this area holds and manipulates information across delays. The
  thalamic edge says the thalamus amplifies the cortex's own recurrent connectivity and does not
  supply the content. **So the content is held on an internal recurrent edge that this entry does
  not write** — the Class-3 within-sub-element recurrence above is a generic placeholder, not a
  measurement of this area. This is the **ninth** entry in the source where the stated function has
  no declared internal substrate, and it is the one where the external evidence most specifically
  points at the missing edge.
- **Neurons:** soft / unknown (part of the ~640M prefrontal budget). **Synapses / Axons / volumes /
  Myelination:** unknown.

## Ventrolateral prefrontal cortex (Brodmann areas 45 and 47)

- **Function:** controlled retrieval and selection — of words, semantic knowledge and responses;
  the "what" / semantic-control counterpart to the dorsolateral entry.
  **This entry also owns area 12**, which two edges in file 6 name and this entry's heading does
  not — see Internal structure.
- **Inputs:**
  - **← the temporal pole** — **carries:** an **amodal concept** — a representation of the thing
    that is no longer visual or auditory or tactile. **Payload unknown — owed** at the producer's
    end, where the modality-loss is recorded as the only checkable property in hand. **Fan-in:**
    unknown. **The producer declares it and names this area** (file 7).
  - **← the inferotemporal cortex** — **carries:** object and face identity, invariant to position,
    size, pose and lighting. **Fan-in:** unknown. **Far end in file `01_visual_pathway`; unchecked** — though file 6 records, from its own reading of that file, that
    the inferotemporal Outputs name ventrolateral prefrontal cortex, so the edge is expected to be
    two-ended.
  - **← the mediodorsal thalamus** — **carries:** **no categorical content** — modulatory
    amplification of this cortex's own recurrent activity. **Fan-in:** unknown. **The producer
    declares it as a class covering all prefrontal divisions** (file 12).
  - **← the anterior auditory belt, directly** — **carries:** call and identity features; **no
    location**. Declared at the belt's end; **areas 12 and 45** are targets of
    the auditory "what" stream, which reaches prefrontal cortex without waiting for the temporal
    endpoints. **Fan-in:** unknown. **Far end in file `02_auditory_pathway`; unchecked.** *(Class 1 — Romanski et al. 1999, rhesus. **Verified against the journal record 2026-08-12**; see the reference section.)*
  - **← the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus** —
    **carries:** the **valence tag**, as at the other prefrontal consumers. **Payload otherwise
    owed. Fan-in:** unknown. **This is the densest of the producer's four lateral edges**:
    terminations across **area 12** — which this entry's Internal structure slot resolves to
    **Brodmann area 47** — in deep layer I, layer II and layer VI, continuing dorsally into much of
    **Brodmann area 45**. **Ipsilateral only. The producer declares it** (file 8).
    **This is a second edge assigning itself to areas 12 and 45 specifically, and it arrives from a
    different file and a different modality than the first.** The Internal structure slot below
    records the divisional internal edges as owed on the ground that nothing distinguishes what
    Brodmann area 45, Brodmann area 47 and area 12 each carry, and notes that the anterior auditory
    belt input already makes such an assignment. **Two independent external demands on one unmade
    division is a different state from one**, and the slot is amended accordingly.
    **And the Brodmann area 45 limb lands in the territory this entry disputes with the Broca
    entry.** The producer terminated the edge here rather than splitting it, because this entry also
    holds area 47, which carries the denser half — and declined to write a Broca limb, on the ground
    that the macaque has no Broca's area and area 45 there is a cytoarchitectonic territory rather
    than a language region, so splitting it would assert a homology the study cannot support.
    **Owed: settle the overlap, and re-terminate this edge if the settlement moves Brodmann area
    45.** *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015. Macaque. **Verified against the publisher record 2026-08-15**; full text read.)*
  - **← the supramarginal gyrus** — **carries:** a **praxis / action-sequence code** and, on the
    left, a **phonological code**. **Payload only partly writable — owed** at the producer's end.
    **Fan-in:** unknown. **The producer declares it**
    (file 6), which records that this entry's Outputs name Broca, temporal cortex and the
    basal-ganglia loop — no parietal target at all.
  - **← the angular gyrus** — **carries:** payload **unknown — owed**, and the producer records it
    as the loudest owed payload in its file: what the angular gyrus emits is described as concepts
    and events, which are not types. **Fan-in:** unknown. **The producer declares it** (file 6), which records that this entry's Inputs name the anterior
    temporal lobe, inferotemporal cortex, the mediodorsal thalamus and the anterior auditory belt —
    **not the angular gyrus**.
- **Outputs:**
  - **→ Broca's area** (language) — **carries:** payload **unknown — owed**; controlled semantic
    retrieval feeding articulatory sequencing. **Fan-out:** unknown. **The consumer is in this file
    and declares it**, untyped there. *(The two entries share Brodmann area 45, which makes this
    edge's status unclear — see Internal structure.)*
  - **→ temporal cortex** (retrieval bias) — **carries:** payload **owed. This endpoint is a class**
    and does not resolve. The temporal-pole entry (file 7) does not declare an input from this area;
    the auditory and visual files were not read. **Owed: name the target.** **Fan-out:** unknown.
  - **→ the basal ganglia** — **carries:** this area's contribution to the **candidate actions**.
    **Fan-out:** unknown. **The consumer declares its cortical source as a class** (file 9).
  - **→ the supramarginal gyrus**, reciprocally via the arcuate fasciculus and superior longitudinal
    fasciculus III — **carries:** task and articulatory context. **Payload otherwise unknown —
    owed. Fan-out:** unknown. **The consumer declares it**
    (file 6), which records "**The producer declares nothing.**"
  - **→ the anterior intraparietal area**, from **area 12** — **carries:** goal / task context.
    **Payload otherwise unknown — owed. Fan-out:** unknown. **The consumer declares it** (file 6), which records that this entry — "the entry that owns
    area 12" — declares **no parietal target at all**, and marks the edit owed here.
- **Internal structure and internal data flow:**


  **Divisional sub-elements: three, and the heading names two.** **Brodmann area 45**, **Brodmann
  area 47**, and **area 12** — the last named by file 6 as belonging to this entry and by the
  auditory input edge above, and absent from the heading. **Settled: area 12 is Brodmann area 47.** Brodmann's own area 47 "incorporates the region that Brodmann
  identified as area 12 in the monkey," which is why the area is written **47/12** in much of the
  primate literature. **So this entry has two sub-elements, not three, and the heading should read
  Brodmann area 45 / Brodmann area 47 (= macaque area 12).** **Owed: put the correspondence in the
  heading**, so that the edges other files write to "area 12" — the auditory "what" input and the
  anterior intraparietal output — land on a name this entry uses. *(Class 1 — the Brodmann 47 /
  macaque 12 correspondence, standard and long-established; located by web search 2026-07-23,
  encyclopaedic sources only, no primary paper opened. **Candidate:** secondary sources were opened
  and the primary record was not.)*

  **Brodmann area 45 is shared with the Broca entry, and the research says both entries have a real
  claim on it.** Broca's area is classically Brodmann area 44 plus Brodmann area 45; this entry is
  Brodmann area 45 plus Brodmann area 47. **Brodmann area 45 is the overlap, and it is the overlap
  because the two conventional groupings genuinely both include it** — this is not a bookkeeping
  error in the file but an inherited feature of the two naming schemes. **Nor is the region
  indivisible: Brodmann area 45 subdivides.** Cytoarchitectonically it splits into a **rostral 45A**
  and a **caudal 45B**, the defining feature of the parent area being clusters of large, deeply
  stained pyramidal neurons in the deeper part of layer III together with a well-developed layer 4.
  Receptor-architectonic mapping splits the same territory into an **anterior 45a** and a
  **posterior 45p**, and splits Brodmann area 44 in the other axis into **44d** and **44v**. **Two schemes, two methods, and whether 45A/45B and 45a/45p are the same border under two names is not established.**

  **The resolution this suggests, and it is not the one recorded before the research.** The previous
  note here guessed that the two entries divide Brodmann area 45 **by function rather than by
  architecture**. **That guess was wrong in its specifics** — an architectonic division exists. The
  natural assignment is **45B / 45p, caudal and abutting Brodmann area 44, to the Broca entry**, and
  **45A / 45a, rostral and continuous with Brodmann area 47, to this one**. **Owed: adopt it, or
  reject it — but the file should stop having two headings claim one undivided area.** *(Class 1 for the subdivisions — 45A/45B in the Petrides & Pandya cytoarchitectonic lineage; 44d/44v and 45a/45p from Amunts et al. 2010, human. **Class 2** — the caudal-to-Broca /
  rostral-to-here assignment is Claude's, offered to be checked. Web search 2026-07-23; secondary
  and encyclopaedic sources, no primary paper opened. Candidates.)*

  **A caution the research also turned up, and it bears on every edge in both entries.** The
  Brodmann area 44 / Brodmann area 45 border is conventionally taken at the ascending ramus of the
  lateral sulcus, but **the sulci are highly variable**: variation in the ascending and horizontal
  rami complicates identification of Brodmann area 45 at all, and the sulcus diagonalis within the
  pars opercularis is present in only about half of hemispheres. **So the boundary these two entries
  are arguing over is one that individual brains do not reliably place in the same location**, which
  is a different kind of problem from a naming dispute and cannot be fixed by renaming. *(Class 1 —
  Uylings et al. 2000; Sprung-Much & Petrides 2018, human. Same search caveat. Candidates.)*

  **And the overlap is wider than Brodmann area 45.** Functional imaging routinely includes **pars
  orbitalis (Brodmann area 47)** and the ventral part of **Brodmann area 6** in what is called
  "Broca's region," which would put this entry's other sub-element and part of the premotor entry
  inside the Broca entry's functional territory as well. **Recorded, not resolved.**

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided; granular
  prefrontal isocortex. *(Class 3.)* **Note the tension with the Broca entry**, which records
  Brodmann area 45 as granular and Brodmann area 44 as agranular — consistent, and worth carrying
  because the same area is described in two places.

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**.)* **4 → 2/3**; **2/3 → 5a and 5b** with
  reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**; **6b → 6a**; within-sub-element recurrence.

  **Internal edges — divisional: owed, and under two independent external demands.**
  Nothing distinguishes what Brodmann area 45, Brodmann area 47 and area 12 each carry. The auditory input edge assigns itself to "areas 12 and 45" specifically; **the amygdalar input makes the same assignment**, densest in area 12 and continuing into Brodmann area 45. **Two
  assignments, from two files and two modalities, on one unmade division.** **That is a different
  state from one**: a single external assignment can be an idiosyncrasy of the producing study, and
  two agreeing ones on the same boundary are evidence that the boundary is real and that this entry
  is the only place it is missing. **Owed: divide the entry, or state why the assignments cannot be
  received.**
- **Neurons:** soft / unknown (part of the ~640M prefrontal budget). **Synapses / Axons / volumes /
  Myelination:** unknown.

## Orbitofrontal / ventromedial prefrontal cortex (orbitofrontal cortex, OFC: Brodmann areas 11 and 13; ventromedial prefrontal cortex, vmPFC: Brodmann areas 14, 25 and 32)

- **Function:** value, reward and outcome-based decision-making; emotion regulation and social or
  affective evaluation. Assigns and updates the expected value of options.
- **Inputs:**
  - **← the amygdala**, from the **basal and accessory basal** nuclei — **carries:** the **valence
    tag** — a gain on perception, attention and memory encoding, carrying no identity information of
    its own. **Fan-in:** unknown. **The producer declares it and names this area** (file 8), where
    this area is one of five cortical consumers split out of a class endpoint.
  - **← the hippocampal formation**, from the **subiculum** (with the adjacent **prosubiculum** and
    distal **CA1**), via the **fornix** — **carries:** the **completed episode**; **payload
    otherwise owed at both ends**, the producer recording the same limit on its parietal and
    cingulate limbs. **Fan-in:** unknown. Terminating principally in **layer III** of Brodmann areas
    **11**, **13**, **14** and **25**; **ipsilateral only**. **The producer declares it** (file 8), which records that this entry declared no
    medial-temporal source of any kind.
    ***This edge uses four of this entry's five named-but-unused sub-elements, and it is the first
    edge in the file with a claim on any of them.*** *The Internal structure slot below records them
    as the largest such set in the file. The producer's evidence names the termination areas
    individually, so the assignment arrives with the edge rather than being owed after it.*
    ***And the route is load-bearing rather than descriptive.*** *The projection travels by the
    fornix and by no other route — established by injecting the tracer in animals whose fornix had
    been transected beforehand, in which no prefrontal label appeared at all while comparable intact
    injections showed it. **There is no lateral-prefrontal limb**: the dorsolateral, ventrolateral,
    Broca and frontal-eye-field entries receive nothing directly from that structure. **And there is
    no return limb** — this entry does not project back, the return running instead through the
    nucleus reuniens of the midline thalamus, which has no entry anywhere in the source. **So this
    is a one-way cortical edge whose loop closes through a region the source does not describe.**
    Owed at file 12, with the entry.*
    ***A limit that belongs on the edge.*** *The termination areas are Carmichael and Price's
    macaque parcellation. **Whether macaque areas 14r, 14c and 25 map cleanly onto the human areas
    this entry's heading names is not established by that study and is not asserted here.** *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015. Macaque. **Verified against the publisher record 2026-08-15**; full text read.)*
  - **← the gustatory pathway** and **← olfactory cortex** — **carries:** taste and odour quality.
    **Payload otherwise unknown — owed. Fan-in:** unknown. **Far ends in file `03_other_senses`; unchecked.** **Splitting this line is owed** once they are checked: two
    modalities are not one source.
  - **← the inferotemporal and temporal cortex** (object value) — **carries:** object and face
    identity, on which a value is then assigned. **Fan-in:** unknown. **Far end in file `01_visual_pathway`; unchecked.**
  - **← the basal ganglia**, via the **ventral pallidum → mediodorsal thalamus** limb of the limbic
    loop — **carries:** released inhibition closing the limbic loop, and, on the same cells, a
    **relative-value signal** — the ventral pallidum codes the value of reward outcomes faster and
    more robustly than the accumbens upstream, so value is computed there and not merely passed.
    **Fan-in:** unknown. **The producer declares it** (file 9), which records that the mediodorsal
    entry attributes its basal-ganglia input to the dorsal pallidum rather than to the ventral one,
    and marks that unresolved. **The ambiguity is inherited by this edge.**
  - **← the mediodorsal thalamus** — **carries:** **no categorical content** — modulatory
    amplification of this cortex's own recurrent activity. **Fan-in:** unknown. **The producer
    declares it as a class covering all prefrontal divisions** (file 12).
  - **← the posterior cingulate cortex** — **carries:** payload **owed. Fan-in:** unknown.
    **The producer declares it** (file 17), whose Outputs
    name "the DMN [default mode network] partners (**medial prefrontal**, angular gyrus, precuneus,
    medial temporal lobe)".
  - **← the precuneus** — **carries:** payload **owed. Fan-in:** unknown. **The producer declares it** (file 6), which records that this entry's
    Inputs "name the amygdala, gustatory and olfactory cortex, inferotemporal / temporal cortex, the
    basal-ganglia limbic loop and mediodorsal thalamus — not this area."
  - **← the angular gyrus** — **carries:** payload **owed. Fan-in:** unknown. **The producer declares it** (file 6), same status.
  - **← the insula** — **carries:** the **salience signal**, and reciprocally the interoceptive
    state; **payload otherwise owed**. **Fan-in:** unknown. **The producer names this area among its
    own inputs in a line marked reciprocal** (file 17) and declares its cortical output as a class
    covering it. **Owed at file 17: write the output limb by name.**
- **Outputs:**
  - **→ the amygdala** — **carries:** a **regulatory signal** — suppression or licensing of the
    response. **Payload otherwise unknown — owed. Fan-out:** unknown. **The consumer declares it and
    names this area** (file 8), and records "**Owed at file 11: type it.**"
  - **→ the bed nucleus of the stria terminalis** — **carries:** **regulatory control** —
    suppression or licensing of the *sustained* response, the same kind of signal this entry sends
    the amygdala. **Payload otherwise unknown — owed. Fan-out:** unknown. **The consumer declares it** (file 8), which records that this entry's
    Outputs name the amygdala, hypothalamus, ventral striatum and autonomic centres — not that
    structure.
  - **→ the hypothalamus** — **carries:** payload **owed. Fan-out:** unknown. **Far end in file `14_brainstem_midbrain_hypothalamus`; the hypothalamus entry is unchecked.**
  - **→ the ventral striatum** (value → action) — **carries:** **value** — the expected value of the
    options. **Payload otherwise unknown — owed. Fan-out:** unknown. **The consumer declares it and names this area** (file 9).
  - **→ the ventral pallidum** — **carries:** **value. Payload otherwise unknown — owed. Fan-out:**
    unknown. **The consumer declares it** (file 9), which
    records "**The producer declares no such edge** … **Owed as a cross-file edit at that entry
    (file 11).**" *(The consumer's line also names **infralimbic cortex**, which is
    Brodmann area 25 and therefore a sub-element of this entry that the heading names but no edge
    uses.)*
  - **→ the temporal pole** — **carries:** **value. Payload otherwise unknown — owed. Fan-out:**
    unknown. **The consumer declares it** (file 7),
    which records "**The producer declares nothing.**"
  - **→ the insula** — **carries:** payload **owed. Fan-out:** unknown. **The consumer declares it**
    (file 17), naming this area among its inputs.
  - **→ the right inferior frontal gyrus** — **carries:** payload **owed. Fan-out:** unknown. **The consumer is in this file and declares it.**
  - **→ the periaqueductal gray**, among the autonomic centres — **carries:** payload **owed.
    Fan-out:** unknown. **The consumer declares an input from ventromedial and orbital prefrontal
    cortex** (file 14, per the record at file 8's bed-nucleus entry).
  - **→ autonomic centres** (remainder) — **carries:** payload **owed. This endpoint is a class**
    and, after the periaqueductal gray is split out, does not otherwise resolve. **Owed: name them.**
    **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(This entry's heading names **five**
  cytoarchitectonic areas.)*

  **Divisional sub-elements: five, of which four are used by one edge and the fifth by none** —
  **Brodmann area 11** and **Brodmann area 13** (orbitofrontal), **Brodmann area 14**, **Brodmann
  area 25** and **Brodmann area 32** (ventromedial). ~~**This is the largest named-but-unused
  sub-element set in the file.**~~ **It was, until the hippocampal input above arrived carrying
  terminations in areas 11, 13, 14 and 25 by name.** **Brodmann area 32 remains unused.**
  **What that edge shows is not that the set is now in use but why it was idle**: the assignment
  came from *outside* the file, in a producer's tracing study, and nothing in this entry had ever
  demanded it. **A sub-element set goes unused when no edge is specific enough to need it, and edges
  become specific by being researched rather than by being converted.** Other files address parts of it separately: file 9 names **infralimbic cortex**, which is
  Brodmann area 25; files 6 and 17 address it as **medial prefrontal cortex**, which is the
  ventromedial half and not the orbitofrontal half. **So other files are already treating this entry
  as two entries, and the edges above inherit the ambiguity: the parietal and cingulate inputs are
  medial, the gustatory, olfactory and amygdalar inputs orbitofrontal.** **Owed: split the entry, or
  assign every edge to a sub-element.**

  **The orbitofrontal and ventromedial halves are given one Function statement and the edges say
  they do different things.** Value, reward and outcome-based decision-making is orbitofrontal
  business; the default-mode inputs from the precuneus, angular gyrus and posterior cingulate are
  medial and have nothing to do with taste or object value. **The Function field's single sentence
  covers a value system and a default-mode node.** *(**Class 2** — the reading that the edges sort
  into two systems is Claude's, offered to be checked.)*

  **Laminar sub-elements: contested within the entry, and the heading is the evidence.** Brodmann
  area 11 and Brodmann area 13 are orbital granular-to-dysgranular; Brodmann area 25 (infralimbic)
  is **agranular**; Brodmann area 32 is transitional. **So the file's eight-layer block is right for
  part of this entry and wrong for another part**, as at the Broca entry, and it is **not written
  whole**. **Owed: laminar sets per sub-element.** *(**Class 2** — the incompatibility is Claude's
  reading of the standard architecture of the named areas, offered to be checked. This is the
  **fifth** entry where the boilerplate fails.)*

  **Tangential sub-elements: owed.** The Function field asserts that value is *assigned and updated*
  — the orbitofrontal value axis is recorded elsewhere in the source as **body-relative**, its zero
  and slope set by motivational state, since there are no receptors for reward. **Whether that axis
  is a spatial organisation here or a population code is not established.**

  **Internal edges: owed, all of them.** None between any two of the five areas is recorded.

  **Where the value is assigned is not written.** Identity codes, taste and odour quality, a valence
  tag and an interoceptive state arrive; an expected value leaves. **The step that converts an
  identity into a value has no edge here** — the **tenth** entry in the source with that shape, and
  the one where the conversion is most explicitly the entry's stated job.
- **Neurons:** soft / unknown (part of the ~640M prefrontal budget). **Synapses / Axons / volumes /
  Myelination:** unknown.

## Anterior cingulate cortex (Brodmann areas 24 and 32)

- **Function:** conflict and error monitoring, effort and outcome valuation, and motivation — the
  medial-wall control and salience node that signals when more control is needed.
- **Inputs:**
  - **← the insula** — **carries:** a salience / control signal (a consumer-end copy of the insula →
    anterior cingulate output already written in this file; the two ends agreeing certifies nothing
    on its own). **Fan-in:** unknown. **Checked against file 17**, whose Outputs read
    "→ Anterior cingulate cortex and prefrontal cortex (salience → control) — carries: the salience
    signal — *this event is behaviourally relevant now*. **Payload otherwise unknown — owed**;
    whether what leaves is a scalar, a pointer, or a switching command is not established."
    **Consistent; the producer's fuller typing is now carried here.**
  - **← the amygdala** — **carries:** the **valence tag** — a gain on perception, attention and
    memory encoding, carrying no identity information of its own. **Fan-in:** unknown. **Typed from the producer** (file 8), which names this area among five cortical consumers split out of a class endpoint.
  - **← the hippocampal formation**, from the **subiculum**, via the **fornix**, terminating in
    **layer III of Brodmann area 24a only** — **carries:** the **completed episode**; **payload
    otherwise owed at both ends. Fan-in:** unknown. **Ipsilateral only. The producer declares it** (file 8).
    ***The sub-element restriction is finer than this entry's own headings and it cannot currently
    receive it.*** *The Internal structure slot names Brodmann areas 24 and 32 as divisional
    sub-elements that no edge uses; this edge terminates in **24a and not 24b or 24c**, a
    subdivision the entry does not hold. **Owed: divide Brodmann area 24, or record that this edge
    carries a sub-element claim the entry cannot yet receive.** **This is the second such demand in
    the file** — the ventrolateral entry has two on its own unmade division — and they arrive from
    the same producer and the same study.* *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015. Macaque. **Verified against the publisher record 2026-08-15**; full text read.)*
  - **← the dorsolateral prefrontal cortex** — **carries:** payload unknown — owed. **Fan-in:**
    unknown. **The producer is in this file and now declares it**, also owed there.
  - **← the midline / intralaminar thalamus** — **carries:** payload unknown — owed. **Fan-in:**
    unknown. **The producer declares its cortical target as a class** — "striatum (major) and cortex
    (diffuse)" (file 12) — which covers this area without naming it. **Owed as a cross-file edit at
    that entry (file 12).**
  - **← the midcingulate cortex**, reciprocally, via the **cingulum** — **carries:** payload
    **owed. Fan-in:** unknown. **The producer declares it** (file 17), naming reciprocal anterior
    and posterior cingulate links.
- **Outputs:**
  - **→ the dorsolateral prefrontal cortex** (recruit control) — **carries:** a signal recruiting
    cognitive control under conflict. The conflict content has **no coordinate frame and no explicit
    decoded format of its own**; it acts by **raising the gain** on the already-framed coding of the
    correct sensorimotor response (under conflict the population activity shifts along the
    response-coding directions, so the correct response is represented more strongly), rather than
    travelling as a conflict signal carrying its own frame. **Fan-out:** unknown.
    *(Class 1 — human dorsal-anterior-cingulate single units, a multi-source interference conflict
    task, analysed with targeted dimensionality reduction that tested for an explicit conflict-coding
    axis and did not find one. Because the absence was
    decoded rather than merely unmeasured, this edge is **resisted**, not **owed**.
    *The study
    reports three negatives and one positive: the firing-rate enhancement under conflict came
    **neither** from a discrete population of domain-general conflict-encoding neurons, **nor** from
    a distinct conflict-encoding response axis, **nor** as an epiphenomenon of co-activated action
    plans — and instead **conflict amplified the task-relevant information already encoded across
    the population**.* ***So the gain-on-a-framed-signal reading is not Claude's: it is the study's
    own conclusion, and the Class 2 mark this line carried is withdrawn.*** *What remains Class 2 is
    only the transfer of that conclusion onto this particular edge's payload.* ***And the class mark
    is weaker than it looked:*** *the work is a preprint. **The one edge in this file marked*
    resisted *rather than* owed *— the strongest epistemic claim the file makes about any absence —
    rests on unrefereed work.** A fourth finding the file should carry: the same study found the
    conflict effects **weaker and more heterogeneous in dorsolateral prefrontal cortex**, which is a
    comparative claim about the consumer of this very edge and is not written at that entry.
    **Owed there.*** *(Class 1 — **Ebitz et al. 2020**. Human, epilepsy patients across two cohorts. **Verified against the bioRxiv record 2026-08-15.** **The study is a preprint and was not peer-reviewed.** **So the class mark on this edge stands on unrefereed work, and that is recorded on the edge rather than in the reference section, because it bears on how much weight the edge can carry.**)*
  - **→ the midcingulate cortex** (reward / outcome) — **carries:** a **scalar reward-value signal**
    — expected reward magnitude, and a response to the mismatch between expected and received reward
    (firing to unexpected reward and to expected-but-omitted reward). It has a coordinate frame — a
    scalar value axis — but the axis's zero and slope are set by bodily and motivational state
    (there are no receptors for reward; the scale moves with need, as a food's value falls once
    sated). The frame is therefore **body-relative**, the same kind as the orbitofrontal value axis.
    **Fan-out:** unknown.
    *(Class 1 — macaque rostral-anterior-cingulate single units, coding expected-reward magnitude
    and reward-prediction-error in the literature's terms. **Unverified, and carrying no citation key**,
    as at the conflict edge above — **owed.** The body-relative reading is Claude's, Class 2, carried by analogy to the
    orbitofrontal satiety-dependence result and not separately shown here. This homes the
    reward/outcome payload on the edge that the midcingulate entry already declares from its end as
    ← ACC [anterior cingulate cortex] (reward / outcome), making that edge two-ended; the two ends
    are copies, so their agreement certifies nothing on its own.)*
  - **→ premotor and the supplementary motor areas** — **carries:** payload unknown — owed.
    **Fan-out:** unknown. **The consumer is in this file** and now declares it.
  - **→ autonomic centres** — **carries:** an autonomic / visceromotor command. The far side of
    these autonomic centres — the visceral effectors they drive — lies outside this document's
    central-nervous-system scope, so the edge terminates at the scope boundary on its output side.
    **Fan-out:** unknown. **The endpoint is nonetheless a class on this side of the boundary**: the brainstem autonomic nuclei that would receive it have entries, and none is checked.
    **Owed: name them, which is a different question from the scope boundary the entry already
    records.**
    *(Carries no citation of its own. **Unverified.**)*
- **Internal structure and internal data flow:** *(The entry's Neurons slot names a distinctive
  cell class.)*

  **Divisional sub-elements: two, named in the heading, and one now carries an edge finer than
  itself** — **Brodmann area 24** and **Brodmann area 32**. **The hippocampal input terminates in area 24a specifically**, which is a subdivision of Brodmann area 24 that this entry
  does not hold. **Owed: divide Brodmann area 24 into 24a, 24b and 24c, or record that the entry
  receives a claim it cannot represent.** The midcingulate entry (file 17) uses the "prime" notation 24′ / 32′ for
  its own territory, which implies this entry holds the unprimed pair; **the relationship between
  the two entries' area numbering should be stated in one of them and is stated in neither.**

  **Cell-class sub-element: von Economo (spindle) neurons.** A large projection cell type
  concentrated in this area and the insula, already recorded in the Neurons slot. **On the
  floor-of-the-hierarchy rule this is a sub-element if it has its own targets, and whether it does
  is not stated here.** **Owed** — and it matters, because this area and the insula are the two ends
  of the salience pair above, and a cell type shared by exactly those two is either the substrate of
  that pair or a coincidence.

  **Laminar sub-elements: seven, not eight.** This is **agranular-to-dysgranular** cingulate cortex
  — the midcingulate entry records the same for its own territory — so layer 4 is thin or absent and
  the file's standard block is **not written**. **Owed: laminar sets per sub-element.** This is the
  **sixth** entry where the boilerplate fails. *(**Class 2** — Claude's reading of the standard
  architecture of the named areas, offered to be checked.)*

  **Tangential sub-elements: unknown.**

  **Internal edges: owed, all of them**, including Brodmann area 24 ↔ Brodmann area 32.

  **Two outputs are typed and the operation that produces them is not.** The conflict signal is
  **resisted** — decoded, with no explicit conflict-coding axis found — and the reward signal has a
  body-relative scalar frame. **So this entry knows more about what leaves it than almost any other
  in the file, and still says nothing about where conflict is detected.** That is a cleaner version
  of the same hole: not an untyped payload, but a typed one with no declared source inside the
  region.
- **Neurons:** soft / unknown; notably contains **von Economo (spindle) neurons**, a large
  projection cell type concentrated in this area and the insula. **Synapses / Axons / volumes /
  Myelination:** unknown.

## Frontopolar cortex (Brodmann area 10)

- **Function:** the most anterior and largest granular prefrontal area — metacognition, prospective
  memory, and cognitive branching (managing multiple goals and subgoals). Widely regarded as the
  **least-understood cortical area**; relatively neuron-rich in humans (Semendeferi et al.).
- **Inputs:**
  - **← other association / prefrontal cortex** — supramodal. **The entry's "almost the whole of
    frontopolar's afferents, with little direct sensory input" is true of the *lateral* part of this
    area and false of the *medial* part**, and the correction is quantitative: retrograde tracer
    injections in **lateral** area 10 found **more than 90% of afferents arising from other frontal
    areas**, while injections on the **midline surface** received substantial temporal-lobe
    projections **including clear auditory connections**. The same medial/lateral difference is
    reported to match functional-connectivity findings in the human brain. **So this line and the
    auditory line below are not in conflict — they describe two different parts of one entry**, and
    the entry has been carrying a lateral-area-10 description under a whole-area heading. Specific
    source regions still owed. **carries:** payload unknown — owed. **Fan-in:** unknown.
    **This endpoint is a class and is unresolved**: the in-file candidates
    are the dorsolateral, ventrolateral, orbitofrontal and anterior cingulate entries, and **none of
    the four declares an output to this area**. **Owed as cross-file edits within this file, or
    withdraw.**
    *(Class 1 — Rosa et al. 2018. Cebus apella. **Verified against the journal record 2026-08-12**, which also showed this key carries the wrong year — see the reference section.)*
  - **← auditory association cortex — the anterior belt, the parabelt, the rostral superior
    temporal gyrus and the temporal pole — directly, and densely, onto the medial part** —
    **carries:** call and identity features; no location. Declared at the belt's end.
    **The scale of this input is the finding, and it inverts the entry's premise.** Among all
    prefrontal areas, **this one has the densest interconnections with auditory association
    cortex**, spanning a large antero-posterior extent of the superior temporal gyrus from the
    temporal pole back to the parabelt and belt. **Auditory pathways make up the largest single
    component of this area's extrinsic connections**, and it is described in the review literature
    as the main frontal "auditory field" — the major recipient of auditory input in the frontal
    lobe and the chief source of output back to auditory cortices. More generally, no sensory
    modality is more extensively represented in prefrontal cortex than the auditory one.
    **So this is not one sensory exception to a supramodal rule; audition is this area's principal
    external connection.** **What that input carries is acoustic structure rather than meaning** —
    the tests are stated at the belt's entry. The short version: prefrontal auditory responses
    cluster by **acoustic** similarity rather than by referent, and are **not** driven by pure tones
    or noise bursts — so the payload sits between raw sound and meaning, as an abstracted
    call-like class.
    **What this constrains at the output end.** This entry's output is written as a **selection into
    a store** — a pointer with no coordinate frame of its own, meaningful only through the stored
    representations it selects among. **An input carrying acoustic class rather than referent does
    not refute that reading, but it does remove the easiest support for it**: if what arrived were
    already-referential (words, in a human), the selection signal would have symbols to select
    among on the incoming side as well as the stored side. It does not. **So on the macaque
    evidence the referential binding is not happening on this edge, and must be attributed to the
    store or to a stage not yet named.** **Whether the human homologue's input is referential is
    untested here**, and it is precisely the point where this file's species-transfer hazard would
    bite hardest, because human speech would make the pointer reading fit without any new evidence
    for it. **Owed, and flagged as the load-bearing unknown for the output payload above.**
    **Fan-in:** unknown. **The temporal-pole limb is checked**: that entry's Outputs
    (file 7) name entorhinal, perirhinal and parahippocampal cortex, ventrolateral prefrontal
    cortex, the amygdala and the insula — **not this area**. **Owed as a cross-file edit at the
    temporal pole entry (file 7).** The belt and parabelt limbs are in file `02_auditory_pathway` and are **unchecked**. *(Class 1 — Romanski et al. 1999; Plakke & Romanski / Barbas lineage review, PMC3997038; Petrides & Pandya 2007; Markov et al. 2014. Rhesus macaque. **Verified against their records 2026-08-12**; see the reference section.)*
  - **← other sensory modalities: present but of lower density, and this is a real asymmetry rather
    than a gap in the searching.** Direct connections from **parietal, inferior temporal and
    occipital** cortex are reported as **typically of lower density** than this area's other
    corticocortical links — lower, not absent. **So the answer to "surely audition is not the only
    sense that reaches the frontal pole" is: it is not the only one, but it is the dominant one by
    a wide margin, and the asymmetry is the architectural fact worth carrying.** **carries:**
    payload **owed**. **Fan-in:** unknown. **The parietal limb is checked**: no entry in
    file 4 or file 6 declares an output to this area. **Owed at those files, or withdraw the limb.**
    *(Class 1 — PNAS 112:E1020, 2015, and the tracing literature it reviews; macaque. **Verified against
    the journal record 2026-08-12.**)*
  - **← the mediodorsal thalamus** — **carries:** no categorical content — a modulatory
    amplification of the cortex's own recurrent activity (a consumer-end copy of the mediodorsal →
    prefrontal-cortex output already written in this file, which covers all prefrontal divisions and
    so includes Brodmann area 10). **Fan-in:** unknown.
    *(Class 1 — inherited from the mediodorsal → prefrontal output entry (Schmitt et al. 2017, mouse; taken as general to the mediodorsal-thalamus–prefrontal-cortex loop), and **verified against the journal record 2026-08-12**. A copy of a producer edge already written, so the agreement certifies nothing on its own.)*
- **Outputs:**
  - **→ other frontal / prefrontal cortex** — specific target regions owed. **carries:** a goal /
    subgoal **selection** signal — a top-down signal that picks which stored goal representation is
    active — together with a learning-**state** signal (exploration versus exploitation). It does
    **not** carry an evaluation of the alternatives; that absence is decoded, not assumed. Where a
    selected goal resolves to a concrete target, the chosen **spatial position** is carried too, but
    that is the coordinate of the *selected* representation, not a coordinate frame frontopolar
    itself supplies. So the signal has no coordinate frame of its own: it is a selection into a
    store, meaningful only as far as the stored representations it selects among — and that store is
    the association / temporal-lobe representation system. **Fan-out:** unknown.
    **This endpoint is a class and is unresolved**: none of the four other
    prefrontal entries in this file declares an input from this area. **Owed as cross-file edits
    within this file.** **The class is load-bearing rather than cosmetic here**, because the pointer
    hypothesis below turns on *which* store is addressed, and an unnamed target cannot be a
    dereferenced address.
    *(Class 1 — macaque frontopolar single units in an object-in-place fast-learning task (coding of
    learning stage, exploration versus exploitation, and goal, and the explicit absence of
    alternative-evaluation coding), plus human transcranial magnetic stimulation (TMS) showing a causal role in directed but not random exploration.
    *(Class 1, macaque single units — **Nougaret et al. 2024**. Macaque, two animals. **Verified against the publisher record 2026-08-15.**
    The negative this entry leans on is the study's own stated result — its neurons represented
    learning stage, exploration versus exploitation and the goal of the action, and **did not support
    the hypothesis that frontal-pole neurons compute an evaluation of the alternatives**; only the
    chosen target's position was encoded, the unchosen target's was not.
    ***A restriction that bears on this entry's own medial/lateral divide and is not currently
    carried.*** *The arrays were in the **dorsal, lateral** part of area 10 — the study says so
    explicitly, contrasting it with the medial and orbital parts. **So the selection payload above is
    measured in the lateral part only**, which is the part this entry's Inputs slot describes as
    frontally-connected, and **not** the medial part that receives the auditory input. **The pointer
    hypothesis below assumes the two communicate, and the internal medial ↔ lateral edge it needs is
    recorded as owed.** The single-unit evidence therefore constrains one side of an internal edge
    that has never been written. **Owed: attribute the output payload to the lateral sub-element, or
    establish that the medial part carries it too.**
    Class 1, human causal arm — **Zajkowski, Kossut & Wilson 2017**. Human, fifteen participants. **Verified against the publisher record 2026-08-15**; peer-reviewed. **Right-hemisphere only**, which this entry does not record and
    which its output edge does not carry.)* Reading the signal as a selection bounded by the store it addresses is Claude's, Class 2,
    offered to be checked.)*
- **Internal structure and internal data flow:** *(The medial/lateral divide below rests on
  abstracts and excerpts; no primary record was opened, so everything in it is a **candidate**.)*

  **Divisional sub-elements: two, defined by where the afferents come from.** The **lateral** part
  is almost purely frontal in its inputs (more than 90%); the **medial** and midline part takes
  substantial temporal-lobe input, auditory prominently among it. **The two parts therefore sit at
  different distances from the sensory periphery inside one entry**, and an edge terminating "on
  frontopolar cortex" is under-specified in the same way "on the lateral intraparietal area" was
  before that entry was split by subdivision. **Splitting is owed**, and unusually the basis for it
  is already quantitative.
  **A species caution against carrying this straight to human.** The Cebus pattern is very similar
  to the macaque's despite more than 40 million years of separation, which is reassuring. But the
  **marmoset** differs: its labelled neurons extend ventrally into **inferior temporal visual
  association cortex**, which the Cebus and macaque patterns do not show. **So a direct visual input to the frontal pole exists in at least one primate and not in others**, and which pattern human follows is not established. *(Class 1 — Rosa et al. 2018, Cebus apella; Burman et al. 2011, marmoset.)*

  **The divide sorts this entry's inputs and the entry already says so.** The supramodal frontal
  input is lateral, the auditory input medial. **What it does not sort is the output**, which is
  written once for the whole area. **Owed: say whether the selection signal leaves from one part.**

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided; granular
  prefrontal isocortex, and the entry's Function field records it as relatively neuron-rich in
  humans. *(Class 3.)*

  **Tangential sub-elements: unknown.**

  **Internal edges — laminar.** *(All **Class 3**.)* **4 → 2/3**; **2/3 → 5a and 5b** with
  reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**; **6b → 6a**; within-sub-element recurrence.

  **Internal edges — medial ↔ lateral: owed, and the pointer hypothesis below needs one.** If the
  medial part receives the acoustic input and the lateral part is the frontally-connected one that
  emits the selection, then the two must communicate for the input to bear on the output at all —
  and no such edge is recorded.
- **Note — relational integration.** Frontopolar's characteristic operation is integrating multiple
  *relations* among representations. A relation has no standard coordinate basis unless its related
  items do, so the integrated result has **no coordinate frame** of its own.
  *(Class 1 exist — human functional magnetic resonance imaging (fMRI) dissociating relational
  integration from related processes, **but carrying no citation key** — the reference section below
  does not list it, so nothing has been opened for it. **Unverified; owed: find the study.** Class 2
  read — the no-frame reading is Claude's.)*
- **Note — the decoding here is thin.** Brodmann area 10 is barely characterised at the single-unit
  level (essentially the one macaque fast-learning study above, plus fMRI and stimulation). Its
  edges are therefore largely **owed** — no one has decoded them — rather than **resisted**
  (decoded, no format found); its walls should not be read as settled category findings. Value in
  frontopolar is in this state: human fMRI shows decision- and counterfactual-value correlates while
  the macaque single-unit study finds no alternative-evaluation — **contested, owed, not resolved.**
- **Note — hypothesis (owed — to test): frontopolar as an indirection / pointer machine.** Reading
  the output above — a **selection into a store** with no coordinate frame of its own — as an
  **address** rather than as absent content: frontopolar would emit a content-free **pointer**
  naming *which* stored representation to activate, while that representation's content lives in the
  association / temporal-lobe store it points into. On this reading the frameless payload is not a
  gap in the decoding but the correct **type** of the signal — an index, which has no coordinate
  frame because its meaning *is* the store it indexes. **Mechanism (assembled from Class-1 edges
  already in this file, not separately measured):** Brodmann area 10 holds and selects the address;
  the **basal-ganglia output** dereferences it — the "tonic inhibition, selectively released — which
  one is allowed to proceed" edge releases the addressed cortical loop; **the mediodorsal thalamus**
  sustains the released representation (the "amplifies a payload it does not itself carry" edge).
  The index operation would then live in the **cortico-striatal-thalamic loop**, not in Brodmann
  area 10's cortical sheet alone. **External support:** Kriete, Noelle, Cohen & O'Reilly 2013 proposes exactly this — prefrontal / basal-ganglia variable binding through
  indirection, an address in the computer-science pointer sense, with the basal ganglia supplying
  the selective gating and an output-gate limiting how much the selected representation drives
  posterior cortex. **Predicted decoding signature (unrun):** at the frontopolar output the
  **address decodes but the content does not** — which representation is selected is recoverable,
  what that representation *is* is not (recoverable only in the store); causal arm — interrupting
  the basal-ganglia gate should leave the address intact while the pointed-to representation fails
  to reactivate. Testing it needs **simultaneous frontopolar-plus-store recording**, a task that
  dissociates address from content, and a gating manipulation — a multi-area experiment, not
  settleable from this file. **Status: owed, not resisted.** Consistent with the one macaque study
  above (selection and explore/exploit coded; alternative-evaluation absent) and **not decided by
  it**; it does **not** enter the decoded `carries:` slots above.
  **The dereference limb rests on an edge whose own file marks the mechanism as missing.** File 9
writes the three canonical basal-ganglia pathways as typed internal edges, so the dereference limb of
the mechanism above is a circuit rather than a name — but that file records that the *selection step
itself*, what reduces the candidate set to one, has no declared internal substrate. **Worth knowing
before the prediction is taken as testable.**
  *(A hypothesis in the owed region — **not** verified against measurement, and marked
**unverified** in consequence. The pointer / indirection reading and the loop-mechanism assembly are
Claude's, **Class 2**, offered to be checked. The Kriete et al. 2013 model is external theory,
**Class 3**; its citation is verified and the claim is not, the work being a computational model
rather than a measurement of human Brodmann area 10. The macaque selection /
  explore-exploit coding, the basal-ganglia selectively-released-inhibition edge, and the
  mediodorsal amplification edge this leans on are the file's existing Class-1 entries.)*
- **Neurons:** soft / unknown (part of the ~640M prefrontal budget; Brodmann area 10 is the largest
  single prefrontal subdivision). **Synapses / Axons / volumes / Myelination:** unknown.

**Two findings about this file's own interior.**

**First, two Class-1 claims in this file rest on no citation key at all** — the macaque
rostral-anterior-cingulate reward / prediction-error single units, cited on the anterior cingulate
`→ midcingulate cortex` output, and the human functional-imaging result cited at the frontopolar
relational-integration note. **Each is marked Class 1 and names a study only by description**, and
both have been searched for and not identified from the description the file gives — **the
descriptions may not be specific enough to find the study from**, which is a second cost of citing
by description rather than by key. **Owed: identify them, or downgrade both class marks to
unverified recall.**

**A citation-free Class 1 is one step worse than the case CLAUDE.md warns about.** There, a
plausible citation is produced without a source being opened; here no citation is produced at all
and the class mark alone carries the claim. **A citation-free claim is not merely unsupported; it is
un-constrained, because the constraints live in the papers** — the three claims of this kind that
*have* since been identified each returned something the file did not have: one Class 2 mark
withdrawn, because the reading turned out to be the study's own conclusion; one class mark weakened,
because the conflict study is an unrefereed preprint and is the sole support for the only edge in
this file marked *resisted* rather than *owed*; and one edge given a restriction it did not carry,
because the frontopolar single-unit recordings were in the lateral part of area 10 only.
**§2a's reference section is what makes this findable**: a claim with no key cannot appear in the key
list, so the two records disagree by omission.

**Second, the sub-element deficit is this file's characteristic defect.** Six of the nine entries
name cytoarchitectonic subdivisions in their own headings — Brodmann areas 9 and 46, Brodmann areas
45 and 47, Brodmann areas 11 and 13 with Brodmann areas 14, 25 and 32, Brodmann areas 24 and 32,
Brodmann areas 44 and 45 — and **the only edges terminating on any of them arrive from outside the
file**: the amygdalar inputs, which name areas 9 and 46 and areas 12 and 45, and the hippocampal
inputs, which name areas 11, 13, 14, 25 and 24a. **No edge written from inside this file terminates
on a sub-element of its own entry.** Meanwhile other files terminate edges on sub-elements this file
does not name at all: **F2, F4 and F5** at the premotor entry, the **pursuit area** at the frontal
eye fields, **area 12** at the ventrolateral entry, **infralimbic cortex** at the orbitofrontal one.
**The finer anatomy is in use everywhere except in the entries that own it.**

**A finding about the source rather than about this file, recorded here because this is where it
surfaced.** **Five entries in this file cannot take the standard laminar block** — premotor
(agranular-to-dysgranular), Broca (Brodmann area 44 agranular, Brodmann area 45 granular), the right
inferior frontal gyrus (by homology), orbitofrontal / ventromedial (Brodmann area 25 agranular), and
the anterior cingulate (agranular-to-dysgranular). **With primary motor cortex, the temporal pole,
the hippocampal formation and the cerebellar cortex, that is nine entries across five files** for
which a Class-3 block written once and copied is wrong. **The block is not a default; it is a claim
about granular isocortex**, and the source should say so where it is defined.

---

## Developmental timing of this section's circuitry

*(**Class 2 throughout: the sources below were searched and are named, so what is Class 2 is the
reading placed on them rather than their existence.** No edge, payload or count in this file rests
on this section. The references are in §2a's section below.)*

**Why it is in this file and not another.** The claims below are **regionally specific to this
section** — they are statements that prefrontal cortex differs from the rest of cortex in *when* its
circuitry is finished, and the difference is measured in the associative cells that carry this
section's long-range edges. A file-level statement of a fact about one region belongs where the
region is described.

**1. The long-range scaffold is prenatal and the developmental process is subtractive.** Association
tracts reaching frontal cortex are present before birth and are visible in the living fetus:
**the uncinate fasciculus and inferior fronto-occipital fasciculus from about 20 gestational weeks**,
the cingulum during the third trimester, while the **arcuate and superior longitudinal fasciculi are
resolvable only late** *(In-utero association-tract tractography; Fetal association-tract dissection — both keys **owed** below)*.
They are visible while **unmyelinated**, because early diffusion anisotropy tracks axonal membrane
integrity rather than myelin.
**Axon number then falls rather than rises.** In rhesus monkey the corpus callosum goes from **4
million axons at embryonic day 65 to 188 million at birth**, against an adult average of **56
million** — a **3.5× overshoot** — and growth-cone counts show **axon addition occurs exclusively
before birth, with no postnatal addition.** The reduction is **selective axonal elimination, not
neuronal death**: the neurons survive and keep a local intracortical axon. *(LaMantia & Rakic 1990; Innocenti 2020. Rhesus monkey and cat.)*

**2. Prefrontal cortex holds its overproduced synapses far longer than the rest of cortex, and the
excess is in the cortico-cortical cells.** Spine density on **layer IIIC cortico-cortical** and
**layer V cortico-subcortical** pyramidal neurons of human dorsolateral prefrontal cortex was counted
across the lifespan. **Overproduction and elimination of synaptic spines continue beyond adolescence
and throughout the third decade of life** before stabilising at the adult level, against the prior
consensus that pruning completes in early adolescence. The **highest overproduction — two- to
threefold above adult values — and the most protracted, are in the layer IIIC associative
neurons.** *(Petanjek et al. 2011. Human.)*

**3. Two claims are being distinguished here and this file should not merge them.** The wire count
settles early and appears to settle everywhere at once; **the synapse count carried on those wires
stays inflated in this section for roughly two further decades.** Nothing found shows that prefrontal *long-range axon* elimination is delayed relative to sensory cortex — **the
protraction that is measured is synaptic, in the cells of origin of the long-range edges.**
**Owed: whether any count of prefrontal long-range axon number by age exists.**

**4. The regional-timing claim is contested, and both sides are recorded because the dispute is about
exactly this point.** One lineage holds that **synaptogenesis timing differs by area with prefrontal
latest** *(Huttenlocher & Dabholkar 1997. Human.)*; the other that overproduction is **concurrent across diverse cortical regions**, one clock
brain-wide *(Rakic et al. 1986. Macaque.)*
**Petanjek et al. 2011 has Rakic as an author and lands between them** — concurrent onset, prefrontal
elimination running decades longer.
**A sample limitation is recorded by the 2011 paper against the 1997 one and is carried here**: the
earlier work contained **a single 19-year-old specimen in the whole 15-to-32-year range**, which is
the window in which the prefrontal difference appears. **So the "pruning ends at puberty" consensus
rested on almost no observations where it mattered.** *(That the 1986 paper's methods are older and
cruder is a reasonable prior and is **not** a finding: all three studies count synapses by electron
microscopy, and the 1986 and 1997 disagreement is about sampling and region set, not technique.
Recorded so the assumption is not made silently.)*

**5. A caution the source of the finding states itself and this file carries.** The author's framing
is that protracted overproduction makes prefrontal microcircuits **the most environmentally plastic**
— not that they hold more information. **High spine density in an unpruned circuit is capacity not
yet committed**, and reading it as storage would be a payload claim the measurement does not make.

**6. What this bears on downstream, recorded as the reason it was searched.** A structure whose
long-range edges exist at birth and whose synapses are refined for twenty-five years is one whose
**edge set is early and whose parameter memory is late.** *(That this bears on the architecture rung's
co-instantiation invariant is Claude's reading, offered to be checked, and it is recorded at that rung
rather than argued here.)*

**7. Not in this file, and named so the gap is visible.** Engram-cell work bearing on this section
— prefrontal engram cells generated during initial learning, **silent** in the sense of not being
reactivable by a partial cue until they mature over weeks *(Kitamura et al. 2017)* — is **mouse**.
**Rodent medial prefrontal cortex is agranular and its homology to the granular prefrontal areas of
this file is disputed**; the usual mapping is onto **areas 32 and 25**, this file's anterior cingulate
and the infralimbic sub-element of the orbitofrontal / ventromedial entry, **and not onto Brodmann
areas 9, 46, 45 or 47.** **Owed: whether the laminar location of those engram cells is stated in the paper**, which the searches run did not return.

---

## Electrical stimulation of this section in conscious humans

*(**Class 2 throughout: the sources below were searched and are named, so what is Class 2 is the
reading placed on them rather than their existence.** No edge, payload or count in this file rests
on this section. References are in §2a's section below.)*

**The headline is a negative and it is the reason the section is here.** Stimulating this section in
awake humans **rarely produces experiential content.** In a review of eighty years of
stimulation-evoked memory phenomena, **94.1% of stimulations that evoked an experiential memory were
temporal**, although the parietal and frontal lobes — also part of memory networks — were stimulated
*(Curot et al. 2017 — key **owed**, see below)*. In a series of **75 presurgical patients** studied
with chronic intracerebral recording, responses came **most often from limbic structures, sometimes
from temporal isocortex, and rarely from frontal sites, except for simple motor activity and some
simple automatisms** *(Munari et al. 1993. Human.)*

**What frontal stimulation does produce is the interruption of a process rather than the playback of
a content**: speech arrest, negative motor responses, positive motor responses, somatosensory
phenomena. A probabilistic mapping study of the **medial** frontal wall in **38 epilepsy patients**
classified its findings in exactly those categories — positive motor, negative motor, somatosensory,
speech disturbance, and "other" *(Medial frontal probabilistic stimulation mapping — key **owed**.)*

**Two positive frontal exceptions are recorded, and both are single small studies.**

- **Anterior midcingulate cortex — the entry in this file for Brodmann areas 24 and 32.** Charge
  delivery there elicited **autonomic changes and the expectation of an imminent challenge coupled
  with a determined attitude to overcome it**, and resting-state connectivity placed the stimulation
  site at the core of a distributed network linking that cortex to frontoinsular, frontopolar and
  subcortical regions. **Two patients.** The authors state that stimulation studies of this cortex
  are exceedingly uncommon **because the region is very rarely implanted for clinical reasons.**
  *(Parvizi et al. 2013. Human.)* **What was evoked was a stance
  toward an unspecified future event — neither a memory nor a percept.**
- **Orbitofrontal cortex — the orbitofrontal / ventromedial entry.** Intracranial stimulation there
  has elicited **hallucinated smells** *(Orbitofrontal olfactory stimulation, 2018 — key **owed**.)* **This is the one region in
  this section carrying a primary sensory modality directly, which is a reason to treat it as the
  exception that fits rather than as a counterexample.**

**"Forced thinking" is named here because the distinction it forces is load-bearing.** The term is
Penfield and Jasper's and describes a **rare ictal manifestation of frontal seizures** — that is, it
occurs during **spontaneous seizure activity**, not under stimulation. Literature eliciting it by
**direct electrical stimulation** is scarce; one series reported **three such patients out of 52**
who underwent stereo-electroencephalographic exploration *(Mindruta et al. 2016 — key **owed**.)*
**So the same tissue yields content when a spreading discharge runs through it and yields little or
none when a brief focal pulse is delivered to it.** *(Whether that difference means the content is a
network-level state rather than a locally stored one is Claude's reading, offered to be checked, and
is not written as a finding. The alternative — that stimulation parameters and duration simply
differ, a seizure recruiting far more tissue for far longer — is not excluded by anything found.)*

**The site-specificity of what *does* come out, elsewhere, is recorded because it bears on what this
section is not.** Stimulation of **rhinal cortex mostly induced personal semantic reminiscences,
while only hippocampal stimulation induced episodic memories** *(Curot et al. 2017 — key **owed**.)*
**Content comes out where content is held**, and it does not come out here.

**Two selection effects, and neither has been separated from the finding.**

1. **Every subject is a patient.** These are epilepsy and tumour cases; pathology is presupposed, and
   in this section that pathology is sometimes frontal.
2. **The sharper one is where electrodes go.** Implantation follows suspected seizure onset, which is
   disproportionately temporal. One medial-frontal study notes that **stroke rarely affects the medial
   wall** and that **transcranial magnetic stimulation cannot easily reach its depths** — so this
   region is under-sampled by every available disruptive method at once.

**So the frontal silence is partly real and partly an artifact of sampling, and this file does not
claim to know the proportion. Almost no data is almost no data**, and the negative above is recorded
at that strength and no higher. **Owed: whether any stimulation series exists with frontal coverage
comparable to the temporal coverage these numbers rest on.**

**What it is not licence to do.** Nothing here changes a payload in this file. **A region that yields
no content under stimulation is not thereby established to hold none** — the sampling above is one
reason, and the second is that the inference from *stimulating X evokes Y* to *X represents Y* is not
sound in either direction. *(That the pattern is nonetheless consistent with this section modulating
rather than representing — the same shape as the mediodorsal thalamic output typed in file 12 as
amplification of the consumer's own recurrent dynamics rather than a message on a wire — is Claude's
reading, offered to be checked.)*

---

## References

*(Section under source design §2a. Each full reference given here was obtained by a search run
against a publisher, journal or PubMed record — so **a key given in full is verified against that
record**, per §2a's rule that searching *is* the verification. Keys reading **owed** have not been
searched, and the citation text for those keys, wherever it appears in this file, was written from
recall.)*

**45 distinct keys, 64 inline mentions.** Every key below is used by some line in this file, and
every short form used inline has a line below — the check §2a is built on, run in both directions
and closing in both.

**One key resolves to another key in this file rather than to a paper of its own.**
*Amunts, Uylings & Zilles*, at the right-inferior-frontal entry's Neurons slot, is written as "the
lineage the Broca entry names," and that lineage is *Uylings, Jacobsen, Zilles & Amunts 2006*. The
cross-reference is the file's own and is correct; it is recorded here because a reader matching
strings will not see it.

**One key matches more than one paper and is not resolved** — *Amunts et al.*, at the Broca entry's
Grey-matter volume slot, carrying the Brodmann area 44 figures. See its entry. This is §2a's stated
case, and resolving it is a reading, not extraction.

**Four searched references bear on a claim rather than only on a citation**, and each is
flagged on its own line rather than acted on: the *Gabi & Herculano-Houzel 2016* entry on
whether the prefrontal 8% is settled, the *Amunts et al. 2010* entry on whether 44d/44v and
45a/45p are established subdivisions, the *Petrides & Pandya cytoarchitectonic lineage* entry on
what 45A/45B names and in which species, and the *Ross & Monnot 2008* entry on which sentence in
the right-inferior-frontal entry the reference actually supports. None is a change to an entry;
each is recorded as owed on its own line.

**One searched key carries the wrong year** — *Rosa et al. 2018*, whose issue is dated 2019. See
that entry.

**Two Class-1 claims in this file have no key at all** and are listed here rather than left silent,
because a claim with no key cannot appear in a key list and is therefore invisible to exactly the
check this section performs.
1. **Macaque rostral-anterior-cingulate single units** coding expected reward magnitude and
   reward-prediction-error — cited on the anterior cingulate `→ midcingulate cortex` output.
2. **Human functional magnetic resonance imaging dissociating relational integration** from
   related processes — cited at the frontopolar relational-integration note.
**Both are searched-for and unfound, not unsearched**, and the likeliest reason is that the
descriptions are generic enough to match many studies. **Owed: identify them, or downgrade both
class marks to unverified recall.**

**The species composition of the searched keys, which §2a says this section makes visible.** Of the
keys carrying a full reference: **human** — Amunts et al. 2010 (post-mortem receptor and
cytoarchitectonic mapping), Uylings, Jacobsen, Zilles & Amunts 2006 (post-mortem stereology), Ross
1981 (ten lesion patients), Ross & Monnot 2008 (stroke patients), Ebitz et al. 2020 (epilepsy
patients), Zajkowski, Kossut & Wilson 2017 (fifteen participants), Petanjek et al. 2011,
Huttenlocher & Dabholkar 1997, Parvizi et al. 2013, Munari et al. 1993; **macaque** — Aggleton,
Wright, Rosene & Saunders 2015, Romanski et al. 1999, Nougaret et al. 2024, Rakic et al. 1986, Lund,
Yoshioka & Levitt 1993, Levitt, Lewis, Yoshioka & Lund 1993, Pucak et al. 1996, Melchitzky et al.
1998; **human plus macaque** — Petrides & Pandya 2002, with the connection data from monkey only;
**Cebus** — Rosa et al. 2018; **rhesus monkey and cat** — LaMantia & Rakic 1990; **mouse** —
Schmitt et al. 2017 and Kitamura et al. 2017; **eight primate species including human at a single
brain per species** — Gabi & Herculano-Houzel 2016.

**So most of this file's searched sources rest wholly or partly on non-human material**, and the
mouse one, Schmitt et al. 2017, is the paper five separate edges in this file transcribe their
payload from. **The keys reading *owed* are unsearched, so the file's full balance is not yet
legible.**

- **Aggleton, Wright, Rosene & Saunders 2015** — Aggleton, J.P., Wright, N.F., Rosene, D.L. & Saunders, R.C. (2015). Complementary patterns of direct amygdala and hippocampal projections to the macaque prefrontal cortex. *Cerebral Cortex* 25(11): 4351–4373. **Macaque.** Anterograde autoradiography; fornix-transected cases compared with intact ones for the hippocampal limb. *(Oxford Academic publisher record; open access, full text read 2026-08-15.)* **Cited at five edges across four entries** — the amygdalar inputs at the premotor, dorsolateral and ventrolateral entries and the hippocampal inputs at the orbitofrontal / ventromedial and anterior cingulate entries — **and it carried no line in this section at all**, which is the direction of §2a's check that fails silently.
- **Amunts et al.** — **owed, and the key is ambiguous.** The line carries Brodmann area 44
  grey-matter volumes of ~3.8 cm³ left and ~2.5 cm³ right, human. At least three papers in the
  Amunts lineage could carry such a figure — the 1999 *Journal of Comparative Neurology* 412:319–341
  cytoarchitecture-and-intersubject-variability paper, the 2003 *Journal of Comparative Neurology*
  465:72–89 asymmetry-and-developmental-changes paper, and *Uylings, Jacobsen, Zilles & Amunts 2006*, already cited at this same entry — and which one the figures came from is not established, nor whether they are volumes of the kind those papers report. **Owed: name the paper, or move the figures to the key
  that already carries them.** *(Not searched to resolution.)*
- **Amunts et al. 2010** — Amunts, K., Lenzen, M., Friederici, A.D., Schleicher, A., Morosan, P.,
  et al. (2010). Broca's region: novel organizational principles and multiple receptor mapping.
  *PLoS Biology* 8(9): e1000489; doi 10.1371/journal.pbio.1000489; PubMed 20877713. **Human**,
  post-mortem. In vitro receptor autoradiography, six receptor types, with quantitative
  cytoarchitectonic mapping. *(Public Library of Science publisher record and PubMed. **The author
  list past the fifth name was not captured by this search and is owed.**)* **Two findings for the
  citing lines.** **First, the paper qualifies the subdivisions the file treats as established.**
  It states that areas 44 and 45 were **not divided into 44d/44v or 45a/45p in every brain,
  because those areas were not present in all the brains studied.** The Broca and ventrolateral entries both write the four subdivisions without that qualifier, and the ventrolateral entry's proposed resolution — assigning 45p to the Broca entry and 45a to the ventrolateral one — rests on a border that the source paper says is not always there. **Second, the paper speaks to the file's own open question.** The Broca and ventrolateral entries both ask whether 45A/45B and 45a/45p are one border under two names and record it as unestablished. This paper's abstract states that its results offer **human homologues** to the
  recently described subdivision of area 45 in **macaque** brains — that is, it presents 45a/45p as
  the human counterpart of a macaque division rather than as a rival parcellation of the same
  tissue. See the *Petrides & Pandya cytoarchitectonic lineage* entry, which complicates this.
  *(searched 2026-08-12; candidate.)*
- **Amunts, Uylings & Zilles** — **not a separate source.** The line names it as "the lineage the Broca entry names," which is *Uylings, Jacobsen, Zilles & Amunts 2006*; see that entry for the reference and for what it does and does not establish. *(Established from this file's own cross-reference.)*
- **Brodmann / Sarkissov / Amunts cytoarchitectonic lineage** — **owed**: not searched. The citing line declares its own limit — summarised from secondary literature, no primary paper opened.
- **Burman et al. 2011** — **owed**: not searched.
- **Curot et al. 2017** — *Memory scrutinized through electrical brain stimulation: a review of 80
  years of experiential phenomena.* Neuroscience and Biobehavioral Reviews, 2017. **Authors, volume
  and pages: owed.** Source of the 94.1%-temporal figure and of the rhinal / hippocampal split.
- **Ebitz et al. 2020 (bioRxiv 2020.03.14.991745)** — Ebitz, R.B., Smith, E.H., Horga, G., Schevon, C.A., Yates, M.J., McKhann, G.M., Botvinick, M.M., Sheth, S.A. & Hayden, B.Y. (2020). Human dorsal anterior cingulate neurons signal conflict by amplifying task-relevant information. *bioRxiv* 2020.03.14.991745; doi 10.1101/2020.03.14.991745. **Human**, epilepsy patients over two cohorts; single units in dorsal anterior cingulate and a comparison dorsolateral-prefrontal dataset; multi-source interference task; targeted dimensionality reduction. *(bioRxiv record; searched 2026-08-15.)* **This is a preprint and was not peer-reviewed** — still cited as a preprint in 2024. **It is the sole support for the anterior cingulate conflict edge, which is the one edge in this file marked *resisted* rather than *owed*.** **Owed: check whether it has since been published, and if not, decide whether an unrefereed source can carry a *resisted* mark.**
- **Fetal association-tract dissection** — **owed.** *Development of associational fiber tracts in
  fetal human brain: a cadaveric laboratory investigation*, Brain Structure and Function, 2023;
  authors, volume and pages have not been obtained.
- **Gabi & Herculano-Houzel 2016** — Gabi, M., Neves, K., Masseron, C., Ribeiro, P.F.M.,
  Ventura-Antunes, L., Torres, L., Mota, B., Kaas, J.H. & Herculano-Houzel, S. (2016). No relative
  expansion of the number of prefrontal neurons in primate and human evolution. *Proceedings of the
  National Academy of Sciences* 113(34): 9617–9622; doi 10.1073/pnas.1610178113; PubMed 27503881.
  **Eight primate species including human.** Isotropic fractionator on 2-mm coronal slabs through
  one hemisphere, **one brain per species**. *(National Academy of Sciences publisher record and
  PubMed.)* **Two things the file's neuron-budget paragraph does not say.** **First, the sample is
  one brain per species**, which is what an ~8% figure quoted to two significant figures rests on.
  **Second, the constancy claim is contested in print.** The paper defines prefrontal cortex as cortex anterior to the genu of the corpus callosum — which this file's neuron-budget paragraph matches — and a
  2018 *PNAS* reanalysis using parcellation-based delineations (doi 10.1073/pnas.1721653115) argues
  that the genu proxy substantially underestimates prefrontal extent in humans, and reports a
  larger human-versus-macaque disparity on both delineations. **No line in this file cites that
  paper and none is added here**, per §2a; it is named so that the neuron-budget paragraph's "notably, that fraction is constant across primates, not human-expanded" can be read against a live dispute rather than as settled. *(searched 2026-08-12; candidate.)*
- **Gorelick & Ross 1987** — **owed**: not searched.
- **Huttenlocher & Dabholkar 1997** — Huttenlocher PR, Dabholkar AS. *Regional differences in
  synaptogenesis in human cerebral cortex.* Journal of Comparative Neurology 1997;387:167–178.
  **Species:** human. **Method:** electron-microscopic synapse counts.
- **Innocenti 2020** — *The target of exuberant projections in development.* Cerebral Cortex
  2020;30(6):3820–. **Authors, end page and species list: owed** — the record obtained carries the journal, year, volume, issue and start page only.
- **In-utero association-tract tractography** — **owed.** The fetal DTI study reporting the uncinate
  and inferior fronto-occipital fasciculi from ~20 gestational weeks; authors, journal, volume, pages
  and year have not been obtained.
- **Kitamura et al. 2017** — Kitamura T, Ogawa SK, Roy DS, Okuyama T, Morrissey MD, Smith LM,
  Redondo RL, Tonegawa S. *Engrams and circuits crucial for systems consolidation of a memory.*
  Science 2017;356(6333):73–78. **Species:** mouse. **Method:** activity-dependent cell labelling
  and optogenetic reactivation, contextual fear conditioning.
- **Kriete, Noelle, Cohen & O'Reilly 2013** — Kriete, T., Noelle, D.C., Cohen, J.D. & O'Reilly, R.C. (2013). Indirection and symbol-like processing in the prefrontal cortex and basal ganglia. *Proceedings of the National Academy of Sciences* 110(41): 16390–16395. **Not a species claim** — a computational model. **owed**: the reference is confirmed by web search and the publisher record has not been opened, so what is established is the citation, not the claim.
- **LaMantia & Rakic 1990** — LaMantia AS, Rakic P. *Axon overproduction and elimination in the
  corpus callosum of the developing rhesus monkey.* Journal of Neuroscience 1990;10:2156–2175.
  **Species:** rhesus monkey. **Method:** electron-microscopic axon counts.
- **Levitt, Lewis, Yoshioka & Lund 1993** — Levitt JB, Lewis DA, Yoshioka T, Lund JS. *Topography of
  pyramidal neuron intrinsic connections in macaque monkey prefrontal cortex (areas 9 and 46).*
  Journal of Comparative Neurology 1993;338(3):360–376. **Species:** macaque. **Method:** tracer
  injection, intra- and interlaminar pyramidal connectivity.
- **Lund, Yoshioka & Levitt 1993** — Lund JS, Yoshioka T, Levitt JB. *Comparison of intrinsic
  connectivity in different areas of macaque monkey cerebral cortex.* Cerebral Cortex
  1993;3(2):148–162. **Species:** macaque. **Method:** small biocytin injections into superficial
  layers, anterograde label, compared across V1, V2, V4, areas 3b, 1, 2, area 4 and prefrontal areas
  9 and 46.
- **Markov et al. 2014** — **owed**: not searched.
- **Medial frontal probabilistic stimulation mapping** — **owed.** The study of 38 epilepsy patients
  transforming discrete stimulation points into continuous probabilistic maps of the medial frontal
  wall; authors, journal, volume, pages and year have not been obtained.
- **Melchitzky et al. 1998** — Melchitzky DS, Sesack SR, Pucak ML, Lewis DA. *Synaptic targets of
  pyramidal neurons providing intrinsic horizontal connections in monkey prefrontal cortex.* Journal
  of Comparative Neurology 1998. **Volume and pages: owed** — the record obtained carries
  the authors, title, journal, year and method and not the volume or pages. **Species:** macaque.
  **Method:** biotinylated dextran amine injection into layer 3 of area 9, electron microscopy.
- **Mindruta et al. 2016** — *Intrusive thoughts elicited by direct electrical stimulation during
  stereo-electroencephalography.* Frontiers in Neurology, 2016. **Authors, volume and article number:
  owed.** Source of the three-of-52 figure for forced thinking under stimulation.
- **Munari et al. 1993** — *Clinical responses to electrical brain stimulation of the temporal and
  frontal lobes in patients with epilepsy. Pathophysiological implications.* 1993; 75 patients,
  chronic intracerebral electroencephalographic recording. **Authors beyond the first, journal,
  volume and pages: owed** — the record obtained carries the title, year, cohort and
  method and not the rest. **The first author is taken from the record and is not certain.**
- **Nougaret et al. 2024 (PLOS Biology 22(2):e3002500)** — Nougaret, S. et al. (2024). Neurons in the monkey frontopolar cortex encode learning stage and goal during a fast learning task. *PLOS Biology* 22(2): e3002500; doi 10.1371/journal.pbio.3002500; PubMed 38363801. **Macaque**, two animals, bilateral Utah arrays in the **dorsal / lateral** part of area 10; object-in-place fast-learning task. *(PLOS publisher record; searched 2026-08-15.)* **The author list beyond the first author is owed.** The lateral-only recording site is recorded on the citing edge because it constrains that entry's medial/lateral divide.
- **Orbitofrontal olfactory stimulation, 2018** — **owed.** The report of hallucinated smells elicited
  by intracranial stimulation of orbitofrontal cortex; authors, journal, volume, pages and year have not been obtained.
- **Parvizi et al. 2013** — Parvizi J, Rangarajan V, Shirer WR, Desai N, Greicius MD. *The will to
  persevere induced by electrical stimulation of the human cingulate gyrus.* Neuron
  2013;80(6):1359–1367. **Species:** human. **Method:** intracranial depth-electrode stimulation in
  two patients with refractory epilepsy, with seed-based resting-state functional connectivity.
- **Petanjek et al. 2011** — Petanjek Z, Judaš M, Šimić G, Rašin MR, Uylings HBM, Rakic P, Kostović I.
  *Extraordinary neoteny of synaptic spines in the human prefrontal cortex.* Proceedings of the
  National Academy of Sciences USA 2011;108(32):13281–13286. **Species:** human. **Method:**
  rapid-Golgi spine-density counts on layer IIIC and layer V pyramidal neurons, dorsolateral
  prefrontal cortex.
- **Petrides & Pandya 2007** — **owed**: not searched. Distinct from the
  cytoarchitectonic-lineage key below, which resolves to a 2002 paper.
- **Petrides & Pandya cytoarchitectonic lineage** — Petrides, M. & Pandya, D.N. (2002). Comparative
  cytoarchitectonic analysis of the human and the macaque ventrolateral prefrontal cortex and
  corticocortical connection patterns in the monkey. *European Journal of Neuroscience* 16(2):
  291–310; doi 10.1046/j.1460-9568.2001.02090.x; PubMed 12169111. **Human and macaque.**
  Comparative cytoarchitectonic analysis, with corticocortical connection patterns established by
  tract-tracing in the monkey only. *(European Journal of Neuroscience publisher record and PubMed.
  **The identification of this paper as the source of the 45A/45B labels is a reading, Class 2** —
  the citing lines give a lineage and no year, and the lineage runs across at least the 1994, 1999
  and 2002 papers.)* **A finding for the citing lines, and it cuts against how the file writes the
  labels.** The Broca and ventrolateral entries place *45A/45B* and *45a/45p* side by side as two parcellations of one territory and ask whether they are one border under two names. On the reading here they are
  not the same kind of object: **45A and 45B are labels used for the macaque** ventrolateral
  prefrontal cortex in this lineage, while **45a and 45p are human**, from Amunts et al. 2010, which
  presents them as the human homologue of the macaque division. **But a third usage exists**: the
  secondary reference literature also uses *45A/45B* for a **human dorsal-versus-ventral** split
  attributed to an Amunts et al. 2004 paper, which is neither the rostral/caudal axis the Broca entry's
  Divisional sub-elements slot gives nor the same species. **Three accounts of two labels, and which the file means is not settled.** **Owed at the citing lines: say which species and which axis, before the ventrolateral entry's proposed resolution is adopted or rejected.** *(searched 2026-08-12; candidate.)*
- **Plakke & Romanski / Barbas lineage review, PMC3997038** — **owed**: not searched. *Frontiers in Neuroscience*; the accession is what pins it until the rest is obtained.
- **PNAS 112:E1020, 2015** — **owed**: not searched.
- **Pucak et al. 1996** — Pucak ML, Levitt JB, Lund JS, Lewis DA. *Patterns of intrinsic and
  associational circuitry in monkey prefrontal cortex.* Journal of Comparative Neurology
  1996;376(4):614–630. **Species:** macaque. **Method:** anterograde and retrograde tracer injection,
  intrinsic and associational stripe dimensions compared.
- **Rakic et al. 1986** — Rakic P, Bourgeois JP, Eckenhoff MF, Zecevic N, Goldman-Rakic PS.
  *Concurrent overproduction of synapses in diverse regions of the primate cerebral cortex.*
  Science 1986;232:232–235. **Species:** macaque. **Method:** electron-microscopic synapse counts.
- **Romanski et al. 1999** — Romanski, L.M., Tian, B., Fritz, J., Mishkin, M., Goldman-Rakic, P.S.
  & Rauschecker, J.P. (1999). Dual streams of auditory afferents target multiple domains in the
  primate prefrontal cortex. *Nature Neuroscience* 2(12): 1131–1136; doi 10.1038/16056; PubMed
  10570492; PMC2778291. **Rhesus macaque.** Microelectrode recording combined with anatomical
  tract-tracing: multiple tracers injected into physiologically mapped anterolateral, mediolateral
  and caudolateral belt regions. *(Nature publisher record and PubMed.)* **The paper's own result
  matches all four citing lines and is worth having in one place, because the file spreads it
  across four entries.** Anterior belt was reciprocally connected with the **frontal pole (area
  10)**, the **rostral principal sulcus (area 46)** and **ventral prefrontal areas 12 and 45**;
  caudal belt was mainly connected with the **caudal principal sulcus (area 46)** and the **frontal
  eye fields (area 8a)**. The frontal-eye-field, dorsolateral and ventrolateral entries each cite a limb of that, and each names the right one. **One qualifier the file adds and the paper does not**: the frontopolar entry writes the auditory input as arriving "onto the **medial** part," and this paper says frontal pole (area 10) without a medial/lateral qualifier. That specification rests on the *Rosa et al. 2018* material cited in the frontopolar Internal structure slot, not on this paper. *(searched 2026-08-12; candidate.)*

- **Rosa et al. 2018** — Rosa, M.G.P., Soares, J.G.M., Chaplin,
  T.A., Majka, P., Bakola, S., Phillips, K.A., Reser, D.H. & Gattass, R. Cortical afferents of area
  10 in Cebus monkeys: implications for the evolution of the frontal pole. *Cerebral Cortex* 29(4):
  1473–1495; doi 10.1093/cercor/bhy044. **Cebus (New World capuchin) monkey.** Injections of
  retrograde tracers at different sites within area 10. *(Oxford University Press publisher
  record.)* **The year on this key does not match the publisher's record.** The issue is **April
  2019**, volume 29, issue 4; the paper appeared in advance access in 2018, which is presumably
  where the key's year came from. **Owed at the citing lines: 2019, or say "2018 advance access."**
  **What the paper supports is exactly what the entry claims, and the entry's account is accurate.**
  Injections throughout area 10 labelled neurons in a consistent set of dorsolateral, ventrolateral,
  orbital and medial frontal areas, superior temporal association cortex, and the posterior
  cingulate/retrosplenial region; **sites on the midline surface received more substantial
  temporal-lobe projections including clear auditory connections, whereas more lateral sites
  received over 90% of their afferents from other frontal areas**; the paper states this difference
  reflects functional-connectivity findings in the human brain, and that the Cebus pattern closely
  resembles the macaque's despite more than 40 million years of separation. The frontopolar entry's Inputs and its Internal structure slot carry all four of those, correctly. *(searched 2026-08-12; candidate.)*
- **Ross & Monnot 2008** — Ross, E.D. & Monnot, M. (2008). Neurology of affective prosody and its
  functional–anatomic organization in right hemisphere. *Brain and Language* 104(1): 51–74.
  **Human.** Patients with focal ischemic strokes, assessed with the Aprosodia Battery. *(Elsevier
  publisher record.)* **This paper supports the citing line's hedge rather than the strong claim.**
  It opens by recording that the organisation of affective prosody has **remained controversial**,
  because affective-prosodic deficits occur after left *or* right brain damage, and it notes that
  some subsequent studies confirmed the functional–anatomic approach and others confirmed neither
  its functional nor its anatomic basis. The right-inferior-frontal entry's Function field already says the lateralisation is a bias and not a clean dichotomy; **this reference is the evidence for that sentence and not only for the
  one before it.** *(searched 2026-08-12; candidate.)*
- **Ross 1981, "the aprosodias"** — Ross, E.D. (1981). The aprosodias: functional-anatomic
  organization of the affective components of language in the right hemisphere. *Archives of
  Neurology* 38(9): 561–569; doi 10.1001/archneur.1981.00510090055006; PubMed 7271534. **Human.**
  **Ten** right-handed patients with focal right-hemisphere lesions, examined at the bedside for
  spontaneous prosody, prosodic repetition, prosodic comprehension and comprehension of emotional
  gesturing — the same strategy used for the aphasias, which is what licenses the paper's parallel
  classification. *(American Medical Association publisher record and PubMed.)* **Two notes.**
  **The sample is ten patients and the method is clinical classification, not measurement**, which
  the citing line's phrase "Ross's classic account" carries only by implication. **And secondary
  listings of this paper disagree with the publisher on the volume** — at least one gives volume 40
  where the journal's own record gives 38. The 38 above is the publisher's. *(searched 2026-08-12;
  candidate.)*
- **Schenker et al.** — **owed**: not searched; the key carries no year.
- **Schmitt et al. 2017** — Schmitt, L.I., Wimmer, R.D., Nakajima, M., Happ, M.,
  Mofakham, S. & Halassa, M.M. (2017). Thalamic amplification of cortical connectivity sustains
  attentional control. *Nature* 545(7653): 219–223; doi 10.1038/nature22073; PubMed 28467827;
  PMC5570520. **Mouse.** Representation of two attention-guiding rules recorded in prefrontal
  cortex, with optogenetic manipulation of the mediodorsal nucleus. *(Nature publisher record,
  PubMed and PubMed Central.)* **The paper says what the file transcribes, in the file's own
  terms.** Its own summary is that the mediodorsal nucleus **amplifies the functional connectivity
  of prefrontal cortex, sustaining cortical representations of rule sets without relaying
  categorical information** — which is the "no categorical content … a modulatory amplification of this cortex's own recurrent activity" payload that the frontal-eye-field, dorsolateral, ventrolateral, orbitofrontal / ventromedial and frontopolar entries each carry. **The species caveat is already in the file** at the dorsolateral and frontopolar entries, and it is the load-bearing one: this is mouse work transcribed onto five human prefrontal divisions. *(searched 2026-08-12; candidate.)*
- **Semendeferi et al.** — **owed**: not searched; the key carries no year.
 
- **Sprung-Much & Petrides 2018** — **owed**: not searched.
- **Uylings et al. 2000** — **owed**: not searched. Note that the nearest paper the
  Broca-region searches surfaced in this lineage is dated **1999**, not 2000, so the year on this
  key may itself need checking.
- **Uylings, Jacobsen, Zilles & Amunts 2006** — Uylings, H.B.M., Jacobsen, A.M., Zilles,
  K. & Amunts, K. (2006). Left-right asymmetry in volume and number of neurons in adult Broca's
  area. *Cortex* 42(4): 652–658; doi 10.1016/s0010-9452(08)70401-5; PubMed 16881273. **Human.**
  Nissl-stained sections from left and right hemispheres of five adult men and five adult women.
  *(Elsevier publisher record and PubMed.)* **The citing line's claim is confirmed and is narrower
  than the paper.** The Broca entry's significant left-greater-than-right neuron-number asymmetry in male Brodmann area 44 is the paper's result. The paper also reports that Brodmann area 44 **volume**
  was greater on the left in **all ten** cases though significant only for men, and that Brodmann
  area 45 volume was greater on the left in six of ten including all five women, significant only
  for women — **a female-side asymmetry in area 45 that this file does not record anywhere**, and
  which bears on the right-inferior-frontal entry, since that entry bounds itself by the area 44 asymmetry alone. **This entry also answers the key *Amunts, Uylings & Zilles*.** *(searched 2026-08-12; candidate.)*
- **Zajkowski, Kossut & Wilson 2017 (eLife 6:e27430)** — Zajkowski, W., Kossut, M. & Wilson, R.C. (2017). A causal role for right frontopolar cortex in directed, but not random, exploration. *eLife* 6: e27430; doi 10.7554/eLife.27430. **Human**, fifteen participants; continuous theta-burst transcranial magnetic stimulation to **right** frontopolar cortex; the Horizon Task. *(eLife publisher record; searched 2026-08-15.)* Peer-reviewed. The right-hemisphere restriction is not carried on the citing edge. **Owed there.**
