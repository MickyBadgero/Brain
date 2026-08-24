# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-21
---

---

# FILE 4 OF 20 — DORSAL VISUAL / PARIETAL STREAM

**What is in this file.** The dorsal visual stream: the motion areas — the middle temporal area (V5) and the medial superior temporal area — and the ventral and lateral intraparietal areas — where visual information is re-expressed in coordinate frames for action rather than for recognition.

**Size:** 907 lines, ~18.6k tokens (estimated from bytes, not tokenised). **Entries:** 4. **Edge lines:** 53 — 30 in, 23 out.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Middle temporal area (V5; dorsal stream, isocortex)**
- **Medial superior temporal area (dorsal stream, isocortex)**
- **Ventral intraparietal area (parietal, isocortex)**
- **Lateral intraparietal area (parietal, isocortex)**

**Cross-file status of the marks in this file.** Marks against files 1 (visual pathway), 6 (posterior parietal), 11 (frontal lobe) and 12 (thalamus) are **checked** against the far file. Marks against 2 (auditory), 3 (other senses), 5 (sensorimotor), 8 (medial temporal), 10 (cerebellum), 14 (brainstem/midbrain) and 17 (insula) are **unchecked**.

---

# DORSAL VISUAL / PARIETAL STREAM

## Middle temporal area (V5; dorsal stream, isocortex)

- **Function:** motion processing — direction selectivity (columnar), speed
  tuning, motion integration (local components → global pattern motion, resolving
  the aperture problem), motion-in-depth and disparity, and motion opponency /
  antagonistic surrounds yielding figure–ground from motion.
- **Inputs:**
  *The three cortical feedforward routes carry **different** things, which reversible inactivation
  separates: cooling V2 and V3 degrades the middle temporal area's **binocular-disparity** tuning
  disproportionately relative to its **direction** tuning, and also costs responsiveness to fast
  speeds and some surround suppression, while speed and size information survives. So the direct
  route from V1 carries direction, and the indirect routes through V2 and V3 carry disparity, high
  speeds and surround suppression. (Class 1 — Ponce, Lomber & Born 2008; J Neurosci 31:3894, 2011;
  macaque. Not yet verified for the source.)*
  - **← V2 thick stripes**, from **layers 2/3** of that stripe class, onto **layer 4** —
    **carries:** binocular disparity, high-speed sensitivity, and the surround suppression
    underlying motion opponency; achromatic, retinotopic. **Fan-in:** unknown.
    **The two ends disagree about direction, and the disagreement is substantive rather than
    clerical.** The producer's end declares this edge as carrying **motion direction and
    disparity**, achromatic. This end declares direction as arriving on the **direct V1 route** and
    not on this one, on the strength of reversible inactivation: cooling V2 and V3 degrades
    disparity tuning disproportionately relative to direction tuning. **A causal inactivation result
    outranks an unqualified connectivity statement**, so this end's reading is the better supported
    one — but the producer's end is where the repair belongs. **Owed as a cross-file edit at the
    V2 entry (file 1): remove direction from this edge, or state why the inactivation result does
    not bear on it.** *(Class 1 — Ponce, Lomber & Born 2008; J Neurosci 31:3894, 2011; macaque.)*
  - **← V3**, onto **layer 4** — **carries:** the same class of contribution as the V2 route —
    disparity and high-speed sensitivity — plus dynamic form, contour bound to direction of motion.
    **Fan-in:** unknown. *(Class 1 —
    Ungerleider & Desimone 1986; Ponce, Lomber & Born 2008; macaque. Not yet verified for the
    source.)*
  - **← lateral geniculate nucleus, direct — bypassing V1** — **carries:** payload **owed**;
    sufficient to support motion sensitivity without V1. Mostly **koniocellular** cells, sending
    virtually no collaterals to V1, numbering about **10%** of the V1 population that innervates
    this area. **This is a thalamic input to a non-primary cortical area**, and it is the leading
    account of blindsight's residual motion sensitivity. **Fan-in:** unknown. **The producer's end declares this edge in the same terms** — payload owed, mostly
    koniocellular, virtually no collaterals to V1, about 10% of the V1 population. That end adds
    that the edge **contradicts the framing the rest of its own entry assumes**: that the relay
    funnels everything into a primary area which then redistributes it. **The agreement certifies
    nothing** — both ends carry the same single citation and were written from the same sentence,
    which is the case §4 says the two-ended diff does not cover. *(Class 1 — Sincich, Park, Wohlgemuth & Horton 2004, macaque. Not yet
    verified for the source.)*
  - **← superior colliculus, di-synaptically via the pulvinar** — **carries:** payload **owed**.
    The relay from the colliculus reaches **this area and V3 selectively** — a subcortical route
    into the motion areas that does not pass through V1. **The source describing it names both
    targets, so both ends declare it.** **Fan-in:** unknown.
    *(Class 1 — Lyon, Nassi & Callaway 2010, macaque. Not yet verified
    for the source.)*
  - **← pulvinar** — **carries:** two things on the same wire, per the producer's own declaration:
    **(a)** a visual signal that largely **reflects its cortical driver's content** — selective for
    orientation, direction and motion, but not a representation the cortex lacks; and **(b)** a
    **coordinating payload** — attentional gain and cross-areal synchrony. A second candidate
    subcortical route past V1; pharmacological inactivation of the pulvinar in macaque affects
    blindsight performance, so this edge and the geniculate one are **competing or complementary
    explanations of the same residual capacity**, not established alternatives. **Fan-in:** unknown.
    **Fan-out at the producer:** each pulvinar cell reaches the input layers of ~2–3 cortical areas.
    *(Class 1 — Kinoshita et al. 2019, macaque, for the blindsight result. The payload is
    transcribed from the pulvinar entry's Outputs, where it is Class 1 for the primate selectivity
    and the inactivation effects and Class 2 for the two-part framing, and is **verified for the
    source by Micky**. That entry names its targets as a class — "multiple visual,
    parietal and temporal cortical areas" — so **whether this area is among them is inference,
    Class 2, and is owed** at the pulvinar entry, which should name this area explicitly or exclude
    it.)*
  - **← frontal eye field**, terminating in **all cortical layers** — **carries:** the spatial
    attentional gain signal, as at V4 — an enhancement or suppression by location, not a stimulus
    code. **Fan-in:** unknown. **Declared at this end only:** the frontal eye field entry's Outputs
    slot names the superior colliculus, the brainstem saccade generators, and a reciprocal link with
    the lateral intraparietal area, and does not name this area. **Owed as a cross-file edit at the
    frontal eye field entry (file 11).** *(Class 1 — Anderson, Kennedy & Martin 2011, macaque. Not yet verified for the source.)*
  - **← the medial superior temporal area** (feedback), principally onto **layer 1** — **carries:**
    payload **owed**. Declared at that area's end, also owed. **Fan-in:** unknown. *(Class 3.)*
  - **← posterior parietal areas** (feedback), principally onto **layer 1** — **carries:** payload
    **owed**. **This endpoint is a class and does not resolve.** The posterior parietal file declares no such output: none of its five entries — the anterior and medial intraparietal areas, the
    supramarginal and angular gyri, the precuneus — declares an output to this area, and the
    supramarginal gyrus declares traffic in the **opposite** direction only. **Owed: name the
    posterior parietal region that emits this feedback, or withdraw the edge.** **Fan-in:** unknown.
    *(Class 3.)*
  - **← V1 4B, predominantly its spiny-stellate class**, onto **layer 4** (the direct route) —
    **carries:** direction of motion and binocular disparity, achromatic, coarse-spatial, on the
    **fast few-hop route** — fewer stages, so it arrives earlier; the payload is the same as the
    indirect routes carry, the latency is not. **Fan-in:** unknown. *(Class 1 — Sincich & Horton 2003; Yabuta & Callaway 1996; Yabuta et al. 2001; Nassi & Callaway 2007; macaque. Not yet verified for the source.)*

    **The *magnocellular* annotation on this edge is not contested, and carries no contested mark.**
    The dispute belongs to the V1 entry and does not apply to this edge. What the V1 entry actually disputes is 4B **as a whole**: most 4B cells do take strong
    input from both the magnocellular- and parvocellular-recipient sublaminae, so "4B is
    magnocellular" is false of the sub-element. But 4B's two output cell classes are **separate
    populations with separate inputs**, and the split runs along the same line as the split in
    targets:
    - **Spiny stellates** receive magnocellular input **only**, from 4Cα directly. **These are the
      cells that project here.**
    - **Pyramids** receive both — magnocellular from 4Cα, and parvocellular by a route that does
      not terminate in 4B at all: 4Cβ projects to **layer 3**, where it contacts the pyramids'
      apical dendrites. **These are the cells that project to V2.**

    So the mixing is real, is confined to one cell class, and that cell class is not this edge's
    source. **The direct route to this area is magnocellular; the route through V2 is mixed.** The
    contested mark was attached to the wrong population, and marking a settled edge contested is the
    mirror of leaving a contested one unmarked — it discards a real result. *(Class 1 — Yabuta & Callaway 1996; Yabuta et al. 2001; Nassi & Callaway 2007; macaque, as reported in Cerebral Cortex 30:3483, 2020. Stated in full at the V1 entry, which is where the resolution lives.)*

    **A separate dispute at the V1 entry survives this and does not touch the payload: 4B's layer
    number.** A well-supported reading holds that only the sublamina below the myelinated band is
    layer 4 in anthropoid primates and that 4A and 4B belong to **layer 3**. The name in common use
    is 4B and is kept at both ends. Which number the sub-element wears is nomenclature; what leaves
    it is data flow, and only the second is what this file is for. *(Class 1 — Balaram, Young &
    Kaas, PMC4360995, human/chimpanzee/macaque; the Hässler lineage across 16 primate species.)*

    **Two 4B populations carry near-mirror-image compositions, and taking one for the other is the
    error to avoid here.** The producer's end gives **76% spiny stellate** (range 67–93%) and 24%
    pyramidal for the cells labelled from this area — while **80% pyramidal** is the composition of
    the **V2**-projecting 4B population, which is the reverse figure for the other target. The two populations are largely separate cells:
    dual-tracer injection into V2 and this area labelled two large intermingled but single-labelled
    groups, with fewer than about **5%** double-labelled. The 4B cells projecting here are
    distributed **indiscriminately with respect to the cytochrome-oxidase compartment**.
    *(Class 1 — Sincich & Horton 2003; Nassi & Callaway 2007; macaque.)*
- **Outputs:**
  - **→ the medial superior temporal area** — **carries:** **integrated global motion** — local component motions resolved into
    a single pattern-motion direction (the aperture problem solved), speed, motion-in-depth, and
    figure–ground from motion opponency. The transformation is *local vectors in, one vector per
    region out*. **Fan-out:** unknown.
  - **→ smooth-pursuit oculomotor circuitry** — **carries:** target velocity, as a pursuit command.
    **This endpoint is a class and names no region.** Three files hold candidates — the frontal
    lobe's pursuit area of the frontal eye field, the cerebellum, the gaze integrators in the
    cranial-nerve-nuclei file — and the frontal-lobe file **contains no pursuit-area entry at all**, only a whole frontal-eye-field entry that does not mention pursuit.
    **Owed: name the target region.** **Fan-out:** unknown.
  - **→ the ventral intraparietal area** — **carries:** payload **owed** at this end. **The
    consumer's end types it** as motion and optic flow **in eye-centred (retinotopic) coordinates**,
    and states that the frame is not changed by the receiving stage. **The two ends disagree: one
    owed, one typed, and neither cites a source for the payload.** Not repaired here — which end is
    right is a source judgment. **Fan-out:** unknown. *(Class 3 — general connectivity.)*
  - **→ the lateral intraparietal area** — **carries:** payload **owed** at this end. **The
    consumer's end types it** as visual motion and optic flow, retinotopic, **and attributes that
    declaration to this end, where nothing is declared.** That attribution is false; the payload disagreement stands and is not repaired here.
    **Fan-out:** unknown. *(Class 3 — general connectivity.)*
  - **→ V1** (feedback), principally onto **layer 1** and also onto layers 2, 5 and 6 —
    **carries:** contextual and attentional modulation — figure–ground and border-ownership
    context, and attentional gain; **not a new stimulus code**. Descending input **avoids layer
    4**, which is what distinguishes a feedback edge from a forward one at the receiving end. On
    layer 1 it terminates on apical tufts belonging to cells housed in layers 2/3 and 5, and mainly
    on **spines**. **Transcribed from the consumer's end, which types it where this end had it
    owed**; that end also marks the remainder owed, so the payload is **partly typed and still
    partly owed** at both. The consumer's end declares this edge inside a four-source class — V2,
    V3, V4 and this area — so **which of the four contributes which part of that payload is owed**.
    **Fan-out:** unknown. *(Class 1 — Kennedy/Bullier lineage, macaque; Anderson & Martin, PMC6665918. Not yet verified for the source.)*
  - **→ V2** (feedback), principally onto **layer 1** — **payload unknown — owed.** The consumer's end **declares it owed as well**, inside a class — V4, this area, and
    higher areas — so the edge is owed at both ends and neither end names the other alone.
    **Fan-out:** unknown. *(Class 3 — general anatomy.)*
- **Internal structure and internal data flow:** *(**Nothing here is yet verified
  for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. *(Class 3.)*

  **Tangential sub-elements: two superimposed columnar maps and one clustering that is not
  columnar.** This is a third kind of tangential organisation, distinct from both the discrete
  compartments of V1 and V2 and the continuous feature map of the anterior inferotemporal cortex:

  - **Direction columns.** Columns of smoothly varying preferred direction run side by side with a
    matching set preferring the locally opposite direction. Confirmed by metabolic labelling, and in
    New World monkeys — where this area lies on the surface rather than buried in a sulcus — the
    columns form **pinwheels** of direction preference. *(Class 1 — Albright, Desimone & Gross 1984; Geesaman et al. 1997; Xu et al. 2004; macaque and owl monkey.)*
  - **Disparity columns, coexisting with them.** A topographic map of preferred binocular disparity,
    in millimetre-sized domains that are interleaved across the area. **Some regions contain neurons
    with relatively poor disparity tuning**, so the map does not tile the area uniformly. *(Class 1 — DeAngelis & Newsome 1999, macaque.)*
  - **Speed preference: clustered but not columnar.** Neurons of similar preferred speed group
    together, and the organisation is explicitly **not** strictly columnar. *(Class 1 — Liu &
    Newsome 2003, macaque.)*

  **Two maps superimposed on one sheet is a different object from one compartmentation**, and it is
  what makes a single "sub-element" name insufficient here: a position in this area has *both* a
  direction preference and a disparity preference, and an edge terminating on it terminates on both.

  **A coverage mismatch worth recording rather than smoothing.** Imaging finds motion stimuli
  activating only **3–4 segregated motion domains**, each **2–3 mm²** and spaced **2–3 mm** apart,
  with sub-millimetre direction domains inside them — occupying roughly **15%** of the area's
  surface. Yet about **85%** of this area's neurons are directionally selective. Either the
  domains are not where most direction selectivity lives, or the imaging measures something
  narrower than direction selectivity. **Unresolved, and recorded as unresolved.** *(Class 1 — ScienceDirect S0301008224000200, 2024, macaque; Hu et al. 2018 for the 85% figure.)*

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — tangential: owed.** The functional claim in this entry's Function field —
  that local component motions are integrated into a single pattern motion, solving the aperture
  problem — **requires** signal to cross direction columns, since the component motions and the
  resolved pattern motion have different directions by construction. So an internal edge crossing
  the direction map is demanded by the stated function and is not recorded anywhere. This is a
  **dangling requirement** in the §4 sense, and it is the sharpest one in the visual line.
- **Neurons:** ~15M per hemisphere (best available; high variance, though this area is
  fairly well bounded by a myeloarchitectonic border and its motion selectivity).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** myelin-dense grey-matter
  patch (the basis of its architectonic delineation); quantitative value unknown.

## Medial superior temporal area (dorsal stream, isocortex)

- **Function:** global optic-flow structure over large receptive fields —
  expansion/contraction, rotation, deformation, translation; heading /
  focus-of-expansion; self- versus object-motion disambiguation; smooth-pursuit
  signals. Two sub-areas: the **dorsal division** (optic flow, heading, self-motion; large
  receptive fields) and the **lateral division** (object motion, smooth pursuit; smaller receptive
  fields). First dorsal stage that is not purely visual.
  **Visual and vestibular heading cues are carried by the same single neurons**, not by two
  populations that meet later: individual cells in the dorsal division are tuned to both, and
  combine them **linearly with subadditive weights**. Most cells prefer lateral heading directions
  and are broadly tuned, which makes the population most discriminating around straight ahead.
  *(Class 1 — Gu, Angelaki & DeAngelis 2008; Angelaki, Gu & DeAngelis 2011; macaque. Not yet verified for the source.)*
- **Inputs:**
  - **← the middle temporal area** — **carries:** integrated motion vectors, retinotopic.
    **Fan-in:** unknown.
  - **← vestibular nuclei** via the thalamus — **carries:** the *computed* self-motion estimate,
    not the raw transducer lines. **This is the first cortical edge in the file on which a
    non-visual payload arrives into a visual area**, and the whole function of the stage depends
    on it: without it, optic flow cannot be attributed to self-motion rather than to the world.
    Three properties constrain what is on this edge. It has **velocity-like temporal dynamics**,
    which is the form that combines with visual motion rather than with acceleration. It modulates
    **during self-motion and not with changes of orientation relative to gravity**, so it is not an
    attitude signal — the earlier wording here said "self-motion and attitude estimate" and the
    attitude part is not supported. And the ambiguity that makes a raw otolith signal useless — the
    same signal meaning tilt or translation — is **already resolved before this edge**, by
    combining otolith and semicircular-canal signals; that convergence has been described in the
    Purkinje cells of the cerebellar nodulus and uvula. So the upstream chain that computes this
    payload is partly identifiable, and **naming its stages is owed**. **Fan-in:** unknown.
    *(Class 1 — J Neurosci 29:8936, 2009; Yakusheva et al. 2007, 2008; macaque.)*

    **The route stated on this edge — "via the thalamus" — is contested, and the evidence runs
    against it.** There is reported to be **a lack of anatomical evidence for vestibular projections
    to this area through the thalamus**. Response dynamics and latency shift gradually along
    parieto-insular vestibular cortex → ventral intraparietal area → this area, with **this area
    showing the longest latencies of the three** — the opposite of what a direct thalamic input
    would predict, and consistent instead with the vestibular signal arriving here **cortically,
    late, and by way of the parietal areas**. The edge is left in place because the payload is not
    in doubt; the **route is marked contested** and re-deriving it is owed. *(Class 1 — Chen, A., DeAngelis & Angelaki 2011; Chen, X., DeAngelis & Angelaki 2013b; macaque. Not yet verified
    for the source.)*

    **The thalamic file carries no relay for this route.** None of its
    eight entries — mediodorsal, pulvinar, the posterior interoceptive relay, the motor ventral
    anterior / ventral lateral group, the anterior nuclei, the intralaminar nuclei, the reticular
    nucleus, the zona incerta — declares a vestibular input or a projection to this area. **The
    absence is one-sided evidence and not a disproof**: the first-order vestibular relay would sit
    in the ventral posterior complex, which is described in another file and was not read. But the
    contested route now has no declared substrate at either end, which is what the two-ended diff is
    for.

    **If the cortical alternative is right, it requires an edge this file does not declare.** The
    proposed route arrives here from the parietal areas, and the ventral intraparietal area's entry
    below states the same relocation from its own side. Neither entry declares a **ventral
    intraparietal area → this area** edge. **Owed: write that edge or reject the cortical route.**
  - **← the pursuit area of the frontal eye field**, reciprocally — **carries:** payload **owed**.
    This area and the ventral intraparietal area both have strong recurrent connections with it,
    and its neurons carry visual, vestibular and combined heading tuning of their own — so the
    frontal pursuit area is not simply downstream of this stage. **Fan-in:** unknown.
    **The far end has no entry.** The frontal lobe file holds a single frontal eye field entry whose Function is saccade generation, and it names **no pursuit area and
    no pursuit function anywhere**. So this edge, and the reciprocal one in Outputs, point at a
    sub-element that the source does not yet describe. **Owed as a cross-file edit at the frontal
    eye field entry (file 11): either give the pursuit area a sub-element under Internal structure
    or an entry of its own.** *(Class 1 — Gu, Cheng, Yang, DeAngelis & Angelaki 2016, macaque. Not yet verified for the source.)*
  - **← extraretinal eye-movement / efference copy** — **carries:** the eye's own velocity command —
    what the system *did*, so that the flow it caused can be subtracted. Source region **still not
    named**. **Owed: name the region that emits the efference copy.** The reciprocal edge from the
    frontal pursuit area above is a **candidate** carrier and is recorded as a candidate, not as
    the answer — nothing read identifies its payload. **Fan-in:** unknown.
- **Outputs:**
  - **→ the medial intraparietal area** — **carries:** payload **owed** here; the consumer's end
    declares it as **spatial context and self-motion**, itself marked owed, on a line that groups
    this area with six other sources. **Fan-out:** unknown. *(Class 1 at the consumer's end —
    eNeuro 4:ENEURO.0344-17, 2017, macaque.)*
  - **→ the supramarginal gyrus** — **carries:** payload **owed** here; the consumer's end declares
    an input from this area and the middle temporal area jointly, carrying **motion and the priority
    map**, untyped and uncited. **Fan-out:** unknown.
  - **→ the ventral intraparietal area** —
    **carries:** **global optic-flow structure** — expansion/contraction, rotation, deformation,
    translation — plus **heading** (the focus-of-expansion), and the self- versus object-motion
    attribution. The ventral intraparietal area carries heading neurons of the same visual-plus-
    vestibular kind — but **in different reference frames**, which is what distinguishes the two
    stages. Vestibular heading here is approximately **head-centred**, with a small shift toward
    eye-centred; in the ventral intraparietal area it is **body-centred**. Visual heading is
    approximately **eye-centred in both**. So the downstream stage is not a copy and not a check:
    it holds the same two cues with one of them re-expressed in a different frame. **Fan-out:**
    unknown. *(Class 1 — Fetsch et al. 2007; Chen, X., DeAngelis & Angelaki 2013b; J Neurosci 31:12036, 2011; macaque. Not yet verified for the source.)*
  - **→ the pursuit area of the frontal eye field**, reciprocally — **carries:** pursuit and
    gaze-target velocity. **Fan-out:** unknown.
  - **→ the lateral intraparietal area** — **carries:** payload **owed**. **The lateral intraparietal entry lists this area among its motion inputs and nothing here answers it.** The payload is owed at both ends, since the consumer's end types it as motion and optic flow but attributes that to the middle temporal area's end rather than to this one.
    **Fan-out:** unknown.
  - **→ the middle temporal area** (feedback), principally onto **layer 1** — **carries:** payload
    **owed**. **Fan-out:** unknown. *(Class 3.)*
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. *(Class 3.)*

  **Divisional sub-elements: two** — the **dorsal division** and the **lateral division**, with
  different receptive-field sizes and different jobs, as the Function field records. Splitting them
  into separate entries is **owed**, as for the two inferotemporal divisions and for V3 and the
  ventral posterior area.

  **A third division that is not spatial at all, and this is new for the slot.** Within the dorsal
  division, heading-tuned cells fall into two classes by the *relationship* between their two
  tunings: **congruent cells**, whose visual and vestibular heading preferences agree, and
  **opposite cells**, whose preferences are inverted. Under cue combination the two behave in
  opposite directions — congruent cells become **more** sensitive, in a way that parallels the
  animal's behavioural improvement, and opposite cells become **less** sensitive. *(Class 1 — Gu, Angelaki & DeAngelis 2008, macaque.)*

  **What the opposite cells are proposed to be for: separating self-motion from object motion.**
  If a cell's visual and vestibular heading preferences are inverted, its response reports the
  *disagreement* between the two cues — and a disagreement between optic flow and inertial motion is
  exactly the signature of something in the world moving independently of the observer. A population
  mixing congruent and opposite cells has therefore been proposed as the sensory substrate for the
  causal-inference problem the visual system faces here: deciding which part of the retinal motion
  was caused by self-motion and which by objects. A linear decode of such a mixed population
  approximates marginalising self-motion out. *(Class 1 — Kim, Angelaki & DeAngelis 2022; Sasaki, Angelaki & DeAngelis 2017; macaque.)*

  **A behavioural-model result is excluded from this entry rather than recorded, and the reason is
  worth stating.** The supporting literature also reports that human heading judgements in the
  presence of a moving object fit a Bayesian causal-inference model. That is a statement about a **model of behaviour**,
  not about what a region does or what is on a wire, and §1 of this file's design excludes
  modelling choices. It is also weakly constraining on its own terms: a competing account —
  forced fusion — has been fitted to the same domain, and the causal-inference model carries free
  parameters that let it absorb a wide range of data. The **anatomical and physiological** claim
  above stands on its own; the model fit added nothing to it and is not carried.

  **The specific evidential link is weaker than the claim.** Peer review of the 2022 result noted
  that the analyses did not isolate the opposite cells and test performance with and without them,
  so the contribution attributed to them specifically is inferred from the population result rather
  than demonstrated on that subpopulation. Recorded as a **candidate mechanism**, not a finding.

  **Nothing read gives these two classes a spatial segregation.** They are a division
  of the population, interleaved, defined by a relation between two response properties — not a
  layer, not a compartment, not a position in a map. Every sub-element recorded anywhere else in
  this file is a *place*; an edge terminates on a place. **What it would mean for an edge to
  terminate on the congruent cells and not the opposite ones is owed**, and it may not be
  answerable in the slot's present form. Recorded here because the functional difference is large
  and signed, not because the slot accommodates it.

  **Tangential sub-elements: unknown.** No columnar or compartmental map for heading, optic-flow
  type, or anything else is recorded for this area — unlike the middle temporal area
  immediately upstream, which has two. Whether that reflects the anatomy or the reading is not
  established.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — between the divisions and between the cell classes: owed.**

  **One causal asymmetry, recorded because it complicates the entry's own account.** Electrical
  microstimulation here **biased heading judgements made from optic flow** but did **not**
  significantly affect vestibular heading judgements — even though single cells carry both cues.
  So the two payloads arriving on the visual and vestibular edges are not symmetrically read out
  downstream, and the entry's Function should not be taken to mean the stage contributes to both
  equally. *(Class 1 — J Neurosci 32:2299, 2012, macaque.)*
- **Neurons:** ~15M per hemisphere (best available, and softer than the middle temporal area's:
  this area has no comparable myeloarchitectonic signature and its retinotopy is crude to absent,
  so both its borders and its count are loose).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Ventral intraparietal area (parietal, isocortex)

- **Function:** reference-frame transformation — coding of motion and location in frames other
  than the retinal one, implemented by gain fields (a sensory receptive field multiplicatively
  modulated by eye and head position). Multimodal: visual motion and optic flow, vestibular, tactile
  and auditory, and strongly bimodal visual-plus-tactile with facial and head tactile receptive
  fields aligned to visual ones (peripersonal / defensive space). Two sub-areas, medial and lateral.

  **The transformation is not applied to everything that arrives, and asserting that it is would
  overstate it.** The frames are **modality-specific and they do not converge here**:
  - **Vestibular** heading is **body-centred** — transformed out of the head-centred frame it
    arrives in.
  - **Visual** heading from optic flow is **approximately eye-centred** — *not* transformed. This
    was tested directly as a hypothesis and refused: no neuron in this area was found with
    head-centred visual heading tuning, and only a small proportion were intermediate between eye-
    and head-centred.

  **So the intuitive engineering solution — bring both cues into a common frame, then combine — is
  not what happens.** Across this area and the medial superior temporal area the visual signal stays
  mainly eye-centred and the vestibular signal is head- or body-centred, and single neurons
  nevertheless combine them. Whatever reconciles the frames is not a change of frame before
  combination. *(Class 1 — Chen, X., DeAngelis & Angelaki 2013a; Chen, X., DeAngelis & Angelaki 2013b; eLife 6:e29809, 2017; macaque. Not yet verified for the source.)*

  **The vestibular frame is further hybrid, and gaze-dependent.** Manipulating body orientation
  relative to the world separates a body-centred (egocentric) from a world-centred (allocentric)
  frame, and this area shows **either, depending on gaze direction** — with gaze fixed relative to
  the body, tuning shifts with body orientation, i.e. egocentric. **A flexible switch between two
  frames, not a fixed one.** *(Class 1 — Chen, X., DeAngelis & Angelaki 2018, macaque.)*
- **Inputs:**
  - **← the middle temporal area** — **carries:** motion, **in eye-centred (retinotopic)
    coordinates** — and it stays eye-centred here, so this edge's frame is *not* changed by the
    stage receiving it. **The producer's end declares this payload owed**, so the two ends disagree
    and neither cites a source. Not repaired here. **Fan-in:** unknown.
  - **← V3** — **carries:** dynamic form — contour bound to direction of motion. **Payload
    otherwise unknown — owed.** **The V3 entry names this area among its dorsal and parietal targets and nothing here answers it.** **Fan-in:** unknown. *(Class 1 — Felleman, Burkhalter & Van Essen 1997, macaque. Not yet verified for the source.)*
  - **← the medial superior temporal area** — **carries:** **global optic-flow structure** —
    expansion/contraction, rotation, deformation, translation — plus **heading** (the
    focus-of-expansion) and the self- versus object-motion attribution, per the producer's end.
    **Typing this line as "motion and optic flow" alone would drop the heading and the
    attribution**, which is the larger half of what the producer declares it sends; the payload here
    is taken from the producer's own declaration. Frame: visual heading is approximately
    **eye-centred** on this edge, vestibular heading is not carried on it. **Fan-in:** unknown.
    *(Class 1 at the producer's end — Fetsch et al. 2007; Chen, X., DeAngelis & Angelaki 2013b; J Neurosci 31:12036, 2011; macaque. Not yet verified for the source.)*
  - **← parieto-insular vestibular cortex** — **carries:** the computed self-motion estimate, in a
    frame **intermediate between head- and body-centred**, which this stage completes to
    body-centred. The route is not "via the thalamus": response dynamics and
    latency place this area **between** the parieto-insular cortex and the medial superior temporal
    area, and the vestibular signal is proposed to reach it from the parieto-insular cortex rather
    than from a thalamic relay. **Fan-in:** unknown. *(Class 1 — Chen, A., DeAngelis & Angelaki 2011; J Neurosci 31:12036, 2011; Chen, X., DeAngelis & Angelaki 2013b; macaque. Not yet verified for
    the source.)*
  - **← eye-position / efference copy** — **carries:** current eye position (eye-in-head) — one of
    the two variables the gain field multiplies by. Source region not named in this file.
    **Owed.** **Fan-in:** unknown.
  - **← head-position (head-on-body) — no line is declared and one is required.** The Function
    field names **eye and head position** as the multiplicands and the Inputs field supplies
    only the first. **Head-on-body is a separately measured variable in this area**, not a
    loose synonym for gaze: tuning has been measured against it as its own axis, with the head
    free to rotate and its angular position tracked, independently of eye-in-head.
    **Carries:** head position relative to the body. **Producer: not named anywhere — owed**,
    with a neck-proprioceptive candidate recorded below. **Fan-in:** unknown.
    *(Class 1 for the independent manipulation — Chen, X., DeAngelis & Angelaki 2013a; macaque. Class 2 for the inference that a declared input line is therefore required.)*
  - **← somatosensory (facial / head tactile)** — **carries:** touch location on the face and head,
    in a **skin-surface** frame. **Fan-in:** unknown.
- **Outputs:**
  - **→ premotor area F4** — **carries:** object location and motion in **head- and body-centered
    coordinates** — peripersonal and defensive space. **The payload change at this stage is the
    coordinate frame, and nothing else**: the same objects go in and come out, re-expressed in a
    frame the body can act in. That is what the gain fields buy, and it is the reason the entry
    exists. **Fan-out:** unknown. **The far end does not declare this edge and does not name F4.**
    The frontal lobe file holds one combined premotor entry whose Inputs
    read as prose — posterior parietal area 5 and the grasp/reach intraparietal areas, prefrontal
    goals, and basal-ganglia and cerebellar output via the motor thalamus. This area is not a
    grasp/reach intraparietal area, so it is not covered by that clause. **Owed as a cross-file edit
    at the premotor entry (file 11): declare this input, and name F4 as a sub-element, since three
    edges in this file terminate on it and the entry that owns the name does not use it.**
  - **→ the lateral intraparietal area** — **carries:** body-centred locations, for prioritisation.
    The consumer's end declares **body- and head-centred** locations, so the two ends disagree by
    one frame. Not repaired here. **Fan-out:** unknown.
  - **→ the medial intraparietal area** — **carries:** body-centred locations, for reach. The
    consumer's end declares this input inside a seven-source line carrying **spatial context and
    self-motion**, marked owed. **The two ends disagree**, and the consumer's is the vaguer.
    **Fan-out:** unknown. *(Class 1 at the consumer's end — eNeuro 4:ENEURO.0344-17, 2017,
    macaque.)*
  - **→ the anterior intraparietal area** — **carries:** object location and motion in **head- and
    body-centred coordinates**, for grasp. **This is the one edge out of this entry whose two ends
    agree**: the consumer's end declares the same payload in the same words. **Fan-out:** unknown.
  - **→ the pursuit area of the frontal eye field**, reciprocally — **carries:** payload **owed**;
    heading in some frame. That area's own visual heading signals are shifted **further toward
    head-centred** than the medial superior temporal area's, so the frame is still moving at that
    stage. **Same missing far end as the medial superior temporal area's two pursuit edges**: the
    frontal lobe file names no pursuit area. **Owed at file 11.** **Fan-out:** unknown. *(Class 1 —
    eLife 6:e29809, 2017, macaque. Not yet verified for the source.)*
- **Internal structure and internal data flow:** *(**Nothing here is yet verified
  for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. *(Class 3.)*

  **Divisional sub-elements: two** — a **medial** and a **lateral** sub-area. Their separate payloads
  are **owed**; the Function field names the division and nothing read distinguishes what each
  carries.

  **Tangential sub-elements: unknown.**

  **The reference frame is not a property of the area — it is a property of the signal, and
  possibly of the measurement.** Three findings have to sit together here:
  - Vestibular heading: **body-centred**, switching to world-centred with gaze.
  - Visual heading from large-field optic flow: **eye-centred**, with no head-centred cells found.
  - Visual receptive fields mapped with **moving bars**: reported **head-centred in a substantial
    proportion** of neurons.

  The last two are the same modality in the same area giving different answers, and the difference
  tracks the stimulus and the property measured rather than the cells. **Unresolved, and recorded as
  unresolved.** For a document whose purpose is to state what is on a wire, this is a warning: the
  frame of a payload here may not be well defined independently of what is being asked of it.
  *(Class 1 — J Neurophysiol 112:353, 2014; Chen, X., DeAngelis & Angelaki 2013a; macaque.)*

  **Two things the optic-flow paper settles about that disagreement, and one it does not.**
  *(Class 1 — Chen, X., DeAngelis & Angelaki 2013a; macaque.)*
  - **The moving-bar experiments could not have dissociated head from body.** Head position relative
    to the body was **not manipulated** in the studies reporting head-centred visual receptive
    fields, so head- and body-centred frames were not separable there. **The discrepancy is
    therefore not symmetric**: one side of it rests on a design that could distinguish the frames
    and the other on designs that could not.
  - **Shift and gain are confusable, and this is a measurement caution the file did not carry.**
    Most neurons in this area and in the medial superior temporal area respond best to lateral
    motion, so many have **monotonic tuning around straight ahead** — which makes a shift of the
    tuning curve hard to distinguish from a change in response gain **unless the complete tuning
    function is measured.** A frame claim and a gain claim are separable only under that condition.
  - **What is not settled, and the experiment that would settle it is named.** There is no
    particular reason that shifts in heading tuning and shifts in receptive-field location should be
    linked, and **the authors state that resolving it requires testing both properties — optic-flow
    tuning and receptive-field shift — in the same neurons.** That has not been done. **Owed**, and
    the research is now specified rather than open-ended.

  **The frame table for this area is wider than the two rows above, and every modality differs.**
  *(Class 1 — Chen, X., DeAngelis & Angelaki 2013a, reporting its own result and citing the others; macaque.)* Vestibular
  heading: **body-centred**. Visual heading from optic flow: **eye-centred** — displacement index
  0.89 ± 0.06 when eye position is varied relative to the head, and 0.97 ± 0.07 when head position
  is varied relative to the body, the latter not significantly different from a purely eye/head-
  centred frame. Of neurons classifiable on both axes, **52% were significantly eye-centred and none
  were head- or body-centred.** Facial **tactile** receptive fields: **head-centred**. **Auditory**
  receptive fields: a **continuum between eye- and head-centred**. **So four modalities arrive at
  one structure in four different frames, and the disparity is larger here than in the medial
  superior temporal area.** A subset of neurons was tested with both visual and vestibular
  protocols, so **the disparity holds within single multisensory cells and is not a difference
  between two populations.**

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — the gain-field mechanism: owed.** The Function field attributes the frame
  change to gain fields — a receptive field multiplicatively modulated by eye and head position.
  That requires the eye- and head-position signal to reach the same cells that carry the sensory
  receptive field, and **the edge carrying it is the one this entry still marks owed** at its
  source. Until that source is named, the mechanism the entry rests on has no declared input.

  **And the gap is two lines wide, not one — the Inputs field declares an eye-position line and no
  head-position line at all**, while the Function field names both as multiplicands.
  **Head position is a real and separately measured variable here and not a loose way of saying
  gaze.** *(Class 1 — Chen, X., DeAngelis & Angelaki 2013a; macaque.)* In that experiment the head was free to rotate in
  the horizontal plane on a collar and its angular position was tracked with a head coil, so eye-in-
  head and head-on-body were varied **independently**, across five combinations: [0°, −20°],
  [−20°, 0°], [0°, 0°], [20°, 0°], [0°, 20°]. Tuning was measured separately in an **Eye-versus-Head**
  and a **Head-versus-Body** condition. **A structure whose tuning is measured against head-on-body
  as its own axis needs a head-on-body input, and this entry declares none.**
  **What the paper does not supply is the producer**, and it does not claim to: it manipulates head
  position and does not say what carries it to this area. **So the owed item is now precise:** name
  the structure that delivers head-on-body position here, and the structure that delivers eye-in-head
  position, or establish that one line carries both. **Owed, and the research is specified.**

  **A candidate route for the head-on-body signal, recorded as a candidate and not as a finding.**
  *(Class 1 for the imaging result, Class 2 for its application to this entry — the paper names the intraparietal sulcus among its foci and does not identify this area. NeuroImage 2008, PubMed 18296073; **human**.)* Proprioceptive input from **neck muscle spindle receptors**
  signals head position relative to the rest of the body, and vibrating those muscles activates a
  network of **areas 3a, 2, S2 and the parieto-insular vestibular cortex** — described as receiving
  direct proprioceptive **thalamic** input — together with foci in the **intraparietal sulcus**,
  motor and premotor areas, and the frontal eye field. **If that is the route, the peripheral origin
  is the neck muscle spindles and the relay is the one this map already carries** as the cuneate
  nucleus serving upper body, neck and forelimb. **The spindle end of that chain is not in the map**,
  and neither is any edge from a somatosensory stage to this entry carrying head position.
- **Neurons:** ~12M per hemisphere (best available; very high variance — the
  softest count in the map. This area sits in the fundus of the intraparietal sulcus,
  lightly myelinated, with no clean architectonic border, and the macaque area has
  expanded into several human parietal areas).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Lateral intraparietal area (parietal, isocortex)

- **Function:** a priority (salience) map — a retinotopic map ranking locations by
  behavioral priority (bottom-up salience + top-down attention + reward), the peak
  selecting the next saccade target; selection is competition among locations
  through lateral inhibition. Supramodal (visual and, in eye-centered coordinates,
  auditory saccade targets). Predictive remapping: just before a saccade, cells
  shift receptive fields toward the post-saccadic location, driven by corollary
  discharge. Eye-position gain modulation. Two sub-elements, a **ventral** and a **dorsal**
  subdivision, described under Internal structure.
- **Inputs:**
  - **← the middle temporal area** — **carries:** visual motion, retinotopic. **This line does not
    point at the middle temporal area's end for the payload: that end declares it owed.** The
    payload here is uncited and is the only declaration of it; the disagreement is recorded at both
    ends and not repaired.
    **This edge reaches the ventral subdivision and not the dorsal one**, which is one of the two
    connectional facts the subdivision rests on. **Fan-in:** unknown. *(Class 1 for the subdivision selectivity — Blatt, Andersen & Stoner 1990, macaque. The payload
    itself carries no citation.)*
  - **← the medial superior temporal area** — **carries:** optic flow, retinotopic. **The producer
    end is declared at that entry and the payload is owed there.** The same
    ventral-subdivision selectivity is asserted here as for the middle temporal area, and **the 1990
    tracer result is not separated between the two sources in this file**, so which of the two the
    selectivity was shown for is **owed**. **Fan-in:** unknown.
  - **← pulvinar** — **carries:** the two-part pulvinar payload — a visual signal reflecting its
    cortical driver's content, plus attentional gain and cross-areal synchrony. **This edge is declared at the producer's end, which names this area explicitly.** **Fan-in:** unknown. **Fan-out at the producer:** each pulvinar cell reaches the input
    layers of ~2–3 cortical areas. *(Class 1 and Class 2 as recorded at the pulvinar entry;
    verified for the source by Micky. **Which subdivision it reaches is unknown**, and
    given that every other visual input to this area is subdivision-specific, that is owed.)*
  - **← ventral-stream visual areas**, onto the **dorsal** subdivision — **carries:** payload
    **owed**. The complement of the edge above: the dorsal subdivision takes ventral-stream input
    that the ventral subdivision does not. **This endpoint is a class, and the visual pathway file does not resolve it.** None of the four ventral-stream entries — V2, V4,
    the inferotemporal cortex, or V3's ventral counterpart — declares an output to this area. The
    one candidate found runs the other way on the subdivision: **V3's Outputs name "the ventral
    lateral intraparietal area"** among its dorsal and parietal targets, which would be the
    **ventral** subdivision, while this edge is declared onto the **dorsal** one — and V3 is the
    dorsal-leaning intermediate tier rather than a ventral-stream area. **Owed: name the
    ventral-stream regions, and settle whether the V3 edge is this edge under another name or a
    second, separate one.** **Fan-in:** unknown. *(Class 1 — Comms Biol 8, 2025, macaque; Felleman, Burkhalter & Van Essen 1997 for the V3 target list. Not yet verified
    for the source.)*
  - **← frontal eye field** (corollary discharge / efference copy of the saccade command, relayed
    from the superior colliculus through the thalamus) — **carries:** *the eye is about to move, by
    this vector* — which is what allows the predictive remapping of receptive fields **before** the
    movement. Timing is load-bearing: this payload is only useful if it arrives before the eye
    moves. **The three-stage route — superior colliculus → frontal eye field → here — is two edges
    and a relay and is not one line.** The middle one is a region with an entry of its own; written
    as a single line it would declare a source that is not this edge's producer. Split here.
    **Fan-in:** unknown.

    **The thalamic relay in that route is unnamed, and the thalamus file does not supply it.** That
    file is read against this one: no entry declares a superior colliculus input, and the
    mediodorsal nucleus — the classical relay for this route — declares its inputs as basal ganglia,
    amygdala and limbic cortex, and prefrontal cortex, with no collicular line, and its output as
    prefrontal cortex only. **Owed: name the relay nucleus, and write the edge at its entry.**
    The producer end is declared: the frontal eye field entry's Outputs names a reciprocal link with
    this area, though untyped and with no payload.

    **The defect this split repairs survives one entry above.** The middle temporal
    area's input from the superior colliculus "di-synaptically via the pulvinar" is written as one
    line, and the pulvinar has an entry of its own that declares both legs. **Owed at that entry:
    split it the way this one was split.**
  - **← prefrontal area 46** — **carries:** top-down goal relevance — a weighting, not a stimulus.
    **Payload otherwise unknown — owed.** **Fan-in:** unknown. **The far end declares it as a
    class**: the dorsolateral prefrontal entry's Outputs read "parietal and sensory cortex
    (top-down bias)", which is compatible with this payload and does not name this area. **Owed as
    a cross-file edit at that entry (file 11): name this area.**
  - **← auditory saccade-target signals** (from the auditory dorsal stream) — **carries:** sound
    location, **converted into eye-centered coordinates** — a supramodal target, which is why this
    map can rank a sound against a sight. **The converting stage is not named anywhere in this
    file, and it is the interesting part of this edge.** **Owed: name the region that performs the
    conversion.** **Fan-in:** unknown.
  - **← the ventral intraparietal area** — **carries:** body- and head-centered locations. Declared
    at that area's end, which says **body-centred** only, so the two ends disagree by one frame.
    Not repaired here. **Fan-in:** unknown.
  - **← the angular gyrus** — **carries:** payload **owed**. **The producer declares nothing.** In the posterior parietal file the angular gyrus entry's Outputs name
    default-mode partners, the hippocampal formation, ventrolateral prefrontal cortex and lateral
    temporal semantic cortex, and not this area — and that entry's output payload is itself marked
    the loudest owed in its file. **Owed as a cross-file edit at the angular gyrus entry (file 6),
    or withdraw the edge.** **Fan-in:** unknown.
  - **← the supramarginal gyrus** — **carries:** payload **owed**. **The producer declares nothing,
    and declares the opposite direction instead.** That entry's Outputs name ventrolateral
    prefrontal and premotor cortex and the ventral-attention network; its **Inputs** name this area
    as a source, carrying the priority map. So the only supramarginal link this source describes
    runs from here to there, and this line asserts the return limb with nothing at its far end.
    **Owed as a cross-file edit at the supramarginal gyrus entry (file 6), or withdraw the edge.**
    **Fan-in:** unknown.
- **Outputs:**
  - **→ frontal eye field** — **carries:** a **priority (salience) map**, as on the collicular edge
    below. **The far end agrees**: the frontal eye field entry's Inputs name this area and the
    priority map explicitly, which makes this one of the two edges out of this entry that check out.
    That end is untyped — no `carries:` line, no fan-in — so **typing it is owed at file 11**, but
    the payloads do not conflict. **Fan-out:** unknown.
  - **→ the superior colliculus**, from the **ventral**
    subdivision onto its intermediate and deep layers — **carries:** a **priority (salience) map** —
    one scalar per retinotopic location, ranking it by behavioural priority (bottom-up salience +
    top-down attention + reward), with the peak specifying the next saccade target. **The payload is
    a scalar field over space, and it is deliberately modality-free**: what it has thrown away —
    color, identity, pitch — is as important as what it keeps. Declared at the superior colliculus's
    end. **The ventral subdivision carries this edge and the dorsal one does not**, so a consumer
    reading "the lateral intraparietal area projects to the colliculus" is reading half the area.
    **Fan-out:** unknown. *(Class 1 — Chen et al., PNAS 113, 2016; macaque.)*
  - **→ the angular gyrus** — **carries:** the same priority map. **The far end declares nothing.**
    That entry's Inputs name occipitotemporal, superior temporal sulcus and somatosensory
    association streams, and the hippocampal formation with the default-mode network — not this
    area. **Owed as a cross-file edit at the angular gyrus entry (file 6).** **Fan-out:** unknown.
  - **→ prefrontal area 46** — **carries:** the same priority map. **The far end agrees and names
    this area**: the dorsolateral prefrontal entry's Inputs name the posterior
    parietal cortex — this area and area 7a — as spatial and attentional. Untyped there — **typing it is owed at file 11** — but "spatial /
    attentional" and "priority map" do not conflict. **Fan-out:** unknown.
  - **→ parahippocampal temporal area TF** — **carries:** the same priority map. Far end in the medial temporal lobe file; **unchecked here**. **Fan-out:** unknown.
  - **→ the anterior intraparietal area** — **carries:** the priority map — which object is the
    current target. Declared at the anterior intraparietal area's end, where it arrives from the
    rostral part of this area. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and search excerpts only; macaque throughout. **Nothing here is yet
  verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, the general cortical set, layer
  4 undivided. *(Class 3.)*

  **Divisional sub-elements: two, and they are architectonically defined before they are
  functionally defined.** The **ventral subdivision** is **densely myelinated**; the **dorsal
  subdivision**, adjacent to the angular gyrus's macaque counterpart, is **lightly myelinated**.
  Receptor mapping separates them again on a different measure: N-methyl-D-aspartate, α1-adrenergic
  and 5-HT1A receptor densities are all **higher in the dorsal** subdivision. **Two independent
  stains agreeing on one border is a stronger basis than either alone**, and it is a firmer footing
  than the tangential compartments recorded at V4 and the middle temporal area, which rest on
  function and connection. *(Class 1 — Blatt, Andersen & Stoner 1990; eLife 9:e55979, 2020.)*

  **The two subdivisions carry different payloads, and the difference is signed.** The ventral one
  holds a **single topographic map of the contralateral hemifield**, with a foveal representation in
  its rostral part; it connects strongly with the frontal eye field and the deep layers of the
  superior colliculus; injecting a GABA-A agonist into it **sharply reduces express saccades**,
  while the same injection into the dorsal subdivision does not. Along the dorsal-to-ventral axis
  the population shifts from cells driven by **visual** events to cells driven by **visual and
  saccadic** events together. **So the map is not uniform and an edge terminating "on the lateral
  intraparietal area" is under-specified.** *(Class 1 — Chen et al., PNAS 113, 2016; PNAS 107:4728, 2010, macaque; Liu, Yttri & Snyder 2010.)*

  **Tangential sub-elements: none reported.** No columnar or compartmental repeat of the kind V1's
  patches, V2's stripes or the middle temporal area's direction columns represent is recorded for
  this area.

  **Internal edges — divisional, and the two directions are different objects.** Retrograde tracing
  of the intrinsic connections found an **asymmetric loop**:
  - **ventral subdivision → dorsal subdivision** — **carries:** payload **owed**; the projection is
    **point-to-point**, described as sensory-like — one location talking to its counterpart.
    **Fan-in:** unknown. **Fan-out:** unknown.
  - **dorsal subdivision → ventral subdivision** — **carries:** payload **owed**; the return
    projection is **widespread**, not point-to-point — one location talking to many. **The
    asymmetry is the finding**: a topographic forward limb and a divergent return limb are the
    anatomy of a map being read out against a broadcast, not of two copies of one map. It is offered
    as the intrinsic circuit underlying the observation that a cell's **motor** response field is
    spatially distinct from its **sensory** receptive field — which is a payload change **inside**
    this entry, and the first one this file has had to record at that scale. **Fan-in:** unknown.
    **Fan-out:** unknown. *(Class 1 — Comms Biol 8, 2025, macaque.)*

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made here.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — the lateral inhibition the Function field rests on: owed.** The entry states
  that selection is competition among locations through lateral inhibition. That requires
  within-map inhibitory edges between separated locations, and **no such edge is recorded here**;
  the divisional edges above are between subdivisions, not across the map. Same shape of hole as the
  gain-field edge owed at the ventral intraparietal area: the mechanism the Function names has no
  declared substrate.
- **Neurons:** ~20M per hemisphere (best available; high variance, but
  firmer-bordered than the ventral intraparietal area — in the lateral bank of the intraparietal
  sulcus with two myeloarchitectonic zones).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown. **White-matter
  volume:** unknown. **Myelination:** the two subdivisions differ in it, and that is what defines
  them (see Internal structure); no g-ratio recorded.

---

---

## References

*(Section under source design §2a. Every line below is a **candidate** awaiting Micky's
verification; none is verified.)*

**How to read a line.** A line **without** an **owed** mark was taken from a publisher or journal
record that was opened. A line marked **owed** was **not searched**, and whatever it carries —
journal, volume, page, year, species, method — is transcribed from this file's own citing lines and
from nothing else. That is the file gathering what it already says in one place, so that the search,
when it is run, has a starting point. **It is not a reference, and it is not evidence that anything
was opened.**

**48 distinct keys, 76 mentions. 7 carry a searched reference; 41 owed.**

**The short form inline is the key here, exactly.** An entry cites *Ponce, Lomber & Born 2008*; the
authors, title, journal, volume, page, year and method sit on that key's line below and nowhere
else. Species stays inline, because entries argue from it — that a result is macaque and not human,
that a column layout is described in owl monkey — and an argument cannot be read with its premise
on another page.

**Fourteen keys are a journal, volume and page with no author** — *J Neurosci 31:3894, 2011*,
*eLife 6:e29809, 2017*, *eNeuro 4:ENEURO.0344-17, 2017* and the rest. For these the volume and page
**are** the short form: they are what pins one paper, so they stay inline rather than moving down
here. This file carries more of them than 02, 03 or 05 did.

**Four keys are malformed as extracted and cannot be searched until they are repaired at the citing
line.** Two name a body of work rather than a paper: the *Kennedy/Bullier lineage* and the *Hässler
lineage*. Two are a volume and a year with no page or article number: *Chen et al., PNAS 113, 2016*
and *Comms Biol 8, 2025*. Two more are short of a year rather than malformed — *Anderson & Martin,
PMC6665918* and *Balaram, Young & Kaas, PMC4360995* have authors and an accession and no year, and
the accession is what pins them until the year is supplied.

**One key is two papers and the file says so itself.** *Yakusheva et al. 2007, 2008* is written as a
single key spanning two years. It needs to become two keys before either can be checked.

**Four Chen keys carry the ordinary author–date disambiguators.** The file cited *Chen, DeAngelis &
Angelaki* for four papers, told apart inline only by the volume and page beside them. **The first
authors are two different people**: *J Neurosci* 31:3082 is **Aihua Chen**, while 33:18574, *Neuron*
80:1310 and *PNAS* 115:3305 are **Xiaodong Chen** — so the initial is in the key. **Two of the X.
Chen papers share a year**, so they carry **2013a** and **2013b**, ordered by journal name,
*Journal of Neuroscience* before *Neuron*. Both are edits to the citing lines rather than to this
section.

**One key was used inline and had no line here at all**, which is the direction of §2a's check that
fails silently: *NeuroImage 2008, PubMed 18296073*, cited for the neck-muscle-vibration candidate
route at the ventral intraparietal entry. It has a line now, marked owed.

**Three keys were written two ways inline**, which defeats the string match this section exists to
support. *PNAS 113, 2016* appeared once with its authors and once without; *J Neurosci 33:18574,
2013* appeared once as a bare journal key and elsewhere as an author key; and the *Hässler lineage*
carried its umlaut inline and lost it here. Each now reads one way in both places.

- **Albright, Desimone & Gross 1984** — *Journal of Neurophysiology* 51:16, 1984. **owed.**
- **Anderson & Martin, PMC6665918** — synaptic reconstruction. **owed.** No year on the key; that
  repair belongs at the citing line.
- **Anderson, Kennedy & Martin 2011** — *Journal of Neuroscience* 31:10872, 2011. Macaque. **owed.**
- **Angelaki, Gu & DeAngelis 2011** — *Journal of Physiology* 589:825, 2011. Macaque. **owed.**
- **Balaram, Young & Kaas, PMC4360995** — human, chimpanzee and macaque. **owed.** No year on the
  key.
- **Blatt, Andersen & Stoner 1990** — *Journal of Comparative Neurology* 299:421, 1990. Macaque;
  retrograde tracer. **owed.** The citing lines use this one result for two different sources' input
  selectivity and mark the separation owed.
- **Cerebral Cortex 30:3483, 2020** — **owed.** Cited as the secondary listing that reports the
  Yabuta and Nassi & Callaway results, not as a primary source.
- **Chen et al., PNAS 113, 2016** — **owed.** A volume and a year with no page or article number.
- **Chen, A., DeAngelis & Angelaki 2011** — Chen, A., DeAngelis, G.C. & Angelaki, D.E. (2011). A
  comparison of vestibular spatiotemporal tuning in macaque parietoinsular vestibular cortex,
  ventral intraparietal area, and medial superior temporal area. *Journal of Neuroscience* 31(8):
  3082–3094. **Macaque.** *(Located in the Neuron 80:1310 reference list — a secondary listing.
  Searched; candidate.)*
- **Chen, X., DeAngelis & Angelaki 2013a** — Chen, X., DeAngelis, G.C. & Angelaki, D.E. (2013).
  Eye-centered representation of optic flow tuning in the ventral intraparietal area. *Journal of
  Neuroscience* 33(47): 18574–18582; doi 10.1523/JNEUROSCI.2837-13.2013. **Macaque**, *Macaca
  mulatta*, two animals, four hemispheres, 161 neurons; extracellular single-unit recording with
  eye-in-head and head-on-body position varied independently; heading tuning quantified by a
  displacement index and by simultaneous von Mises model fits. *(**Full text opened and read
  2026-08-18** at the publisher's open article page; not a secondary listing and not a candidate.)*
- **Chen, X., DeAngelis & Angelaki 2013b** — Chen, X., DeAngelis, G.C. & Angelaki, D.E. (2013).
  Diverse spatial reference frames of vestibular signals in parietal cortex. *Neuron* 80(5):
  1310–1321; doi 10.1016/j.neuron.2013.09.006; PubMed 24239126. **Macaque.** Single-unit recording
  with eye and head position varied independently. *(Cell Press publisher record and PubMed Central.
  Searched; candidate.)*
- **Chen, X., DeAngelis & Angelaki 2018** — Chen, X., DeAngelis, G.C. & Angelaki, D.E. (2018).
  Flexible egocentric and allocentric representations of heading signals in parietal cortex.
  *Proceedings of the National Academy of Sciences USA* 115. **Macaque.** Head position varied
  relative to the body and eye position relative to the head. *(PNAS publisher record; the page
  number 3305 given inline in the file was not separately confirmed by this search. Searched;
  candidate.)*
- **Comms Biol 8, 2025** — retrograde tracer, and retrograde tracer plus recording at the second
  citing line. Macaque. **owed.** A volume and a year with no page or article number.
- **DeAngelis & Newsome 1999** — *Journal of Neuroscience* 19:1398, 1999. Macaque. **owed.**
- **eLife 6:e29809, 2017** — Macaque. **owed.**
- **eLife 9:e55979, 2020** — receptor autoradiography. **owed.**
- **eNeuro 4:ENEURO.0344-17, 2017** — Macaque. **owed.**
- **Felleman, Burkhalter & Van Essen 1997** — *Journal of Comparative Neurology* 379:21, 1997.
  Macaque. **owed.**
- **Fetsch et al. 2007** — Fetsch, C.R., Wang, S., Gu, Y., DeAngelis, G.C. & Angelaki, D.E. (2007).
  Spatial reference frames of visual, vestibular, and multimodal heading signals in the dorsal
  subdivision of the medial superior temporal area. *Journal of Neuroscience* 27(3): 700–712.
  **Macaque.** *(Located in publisher reference listings — a secondary listing. Searched;
  candidate.)*
- **Geesaman et al. 1997** — **owed.** The citing line carries nothing beyond the key.
- **Gu, Angelaki & DeAngelis 2008** — *Nature Neuroscience* 11:1201, 2008. Macaque. **owed.**
- **Gu, Cheng, Yang, DeAngelis & Angelaki 2016** — *Cerebral Cortex* 26:3785, 2016. Macaque.
  **owed.**
- **Hässler lineage** — across 16 primate species. **owed.** Names a body of work rather than a
  paper.
- **Hu et al. 2018** — **owed.** Cited for the 85% direction-selectivity figure and carrying nothing
  else.
- **J Neurophysiol 112:353, 2014** — Chen, X., DeAngelis, G.C. & Angelaki, D.E. (2014). Eye-centered
  visual receptive fields in the ventral intraparietal area. *Journal of Neurophysiology*; doi
  10.1152/jn.00057.2014. **Macaque.** Receptive fields mapped with a large-field multipatch
  random-dot stimulus, run explicitly against the earlier moving-bar results. *(American
  Physiological Society publisher record. **The volume and page written inline were not confirmed by
  this search** — the publisher page gives the digital object identifier and not the pagination.
  Searched; candidate.)* **This is a fifth X. Chen paper**, cited under a journal-only key rather
  than an author one; whether it should join the author keys above is a repair owed at the citing
  line.
- **J Neurosci 29:8936, 2009** — Macaque. **owed.**
- **J Neurosci 31:3894, 2011** — Macaque. **owed.**
- **J Neurosci 31:12036, 2011** — Chen, A. (first author not confirmed by this search), DeAngelis,
  G.C. & Angelaki, D.E. (2011). Representation of vestibular and visual cues to self-motion in
  ventral intraparietal cortex. *Journal of Neuroscience* 31: 12036–12052. **Macaque.** *(Located in
  a publisher reference listing that truncated the author list — a secondary listing. The first
  author is owed. Searched; candidate.)*
- **J Neurosci 32:2299, 2012** — Macaque. **owed.**
- **Kennedy/Bullier lineage** — retrograde fast blue. Macaque. **owed.** Names a body of work rather
  than a paper.
- **Kim, Angelaki & DeAngelis 2022** — *eLife* 11:e74971, 2022. Macaque. **owed.**
- **Kinoshita et al. 2019** — Macaque. **owed.**
- **Liu & Newsome 2003** — Macaque. **owed.**
- **Liu, Yttri & Snyder 2010** — *Nature Neuroscience* 13:495, 2010. **owed.**
- **Lyon, Nassi & Callaway 2010** — Macaque. **owed.** Reached only as reported in PMC4900470 — a
  secondary listing, and the citing line says so.
- **Nassi & Callaway 2007** — Macaque. **owed.**
- **NeuroImage 2008, PubMed 18296073** — **human**; functional imaging with a neck-muscle vibration
  paradigm; abstract read, full text not opened. **owed** — no author, title, volume or page was
  obtained, and the accession is what pins it.
- **PNAS 107:4728, 2010** — functional magnetic resonance imaging in behaving macaque. **owed.**
- **Ponce, Lomber & Born 2008** — Macaque. **owed.**
- **Sasaki, Angelaki & DeAngelis 2017** — *Journal of Neuroscience* 37:11204, 2017. Macaque.
  **owed.**
- **ScienceDirect S0301008224000200, 2024** — 7 tesla functional imaging. Macaque. **owed.** An
  accession and a year with no author.
- **Sincich & Horton 2003** — *Journal of Neuroscience* 23:5684, 2003. Macaque. **owed.**
- **Sincich, Park, Wohlgemuth & Horton 2004** — *Nature Neuroscience* 7:1123, 2004. Macaque;
  retrograde tracer. **owed.**
- **Ungerleider & Desimone 1986** — Macaque. **owed.**
- **Xu et al. 2004** — **owed.** The citing line carries nothing beyond the key; its species note,
  macaque and owl monkey, covers three keys jointly and is not separated between them.
- **Yabuta & Callaway 1996** — *Nature* 380:442, 1996. Macaque; intracellular recording with
  laser-scanning photostimulation. **owed.**
- **Yabuta et al. 2001** — Macaque. **owed.**
- **Yakusheva et al. 2007, 2008** — Macaque. **owed.** One key naming two papers; it needs to become
  two.
