# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-15
---

---

# FILE 18 OF 20 — WHITE-MATTER TRACTS

**What is in this file.** The five major white-matter structures — corpus callosum, internal capsule, fornix, the arcuate / superior longitudinal fasciculus, and the medial longitudinal fasciculus. Transmission, not processing: these entries carry no transform.

**Size:** 618 non-blank lines, ~15.3k tokens / 59 kB (kB = 1024 bytes, truncated). **Entries:** 5. **Reference keys:** 12, over 13 mentions — eight of them deferred to file 2, where six are carried and two are not.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file, with the date each was last worked:**

- **Corpus callosum — the great interhemispheric commissure (with the anterior commissure)** — pass 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements under the transmission-only convention; the auditory and inferior-frontal routed edges confirmed two-ended against files 2 and 11; Internal structure slot added with the five sectors as sub-elements and no internal edges; the three smaller commissures recorded as tracts bundled into this entry with no routed edge at either end
- **Internal capsule — the great projection tract (cortex ↔ subcortex / brainstem / cord)** — pass 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements; each limb mapped to the region-to-region edge it carries and its far-end file; the corticothalamic collateral into the thalamic reticular nucleus written from file 12; Internal structure slot added with the five limbs as sub-elements and no internal edges
- **Fornix — the hippocampal output tract (Papez)** — pass 2026-08-15 — the prefrontal destination set added as a seventh routed edge, two-ended against files 8 and 11; **the tract recorded as the sole route for that connection**, a finding rather than a routing statement and the first of its kind in this file; the limb researched and settled as pre-commissural, discharging what file 8 left owed; a ventral-striatal destination named in the same source and recorded as owed at file 9 *(prior pass 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements; six routed edges confirmed two-ended against files 8, 12, 13 and 14, including the three separately-typed septal return limbs; Internal structure slot added with the pre- and post-commissural limbs as sub-elements and no internal edges)*
- **Arcuate fasciculus / superior longitudinal fasciculus — the dorsal language tract (with the long association fasciculi)** — pass 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements; the supramarginal and inferior-frontal routed edges confirmed two-ended against files 6 and 11; the entry recorded as five tracts in one slot set; the inferior fronto-occipital fasciculus recorded as carrying no edge declared anywhere in the source; Internal structure slot added
- **Medial longitudinal fasciculus — the gaze-yoking brainstem tract (paired, brainstem tegmentum)** — pass 2026-07-25 — new entry; the gaze-yoking tract, written because it carries more declared traffic than three of the four tracts already here; the vestibulo-ocular routed edge confirmed two-ended against files 3 and 15; the abducens internuclear yoking limb recorded as owed at file 15; the nucleus named for the tract distinguished from the tract; Internal structure slot added with the ascending and descending limbs as sub-elements and no internal edges

---

# WHITE-MATTER TRACTS (commissural / projection / association — transmission, no processing)

*The cabling between the grey-matter regions already described — these compute nothing, like the
optic-chiasm entry. Recorded as fibre-tract entries: the load-bearing slot is the **axon count** and
myelination, and neurons and synapses read **none**. Three classes — commissural (between
hemispheres), projection (cortex ↔ subcortex / brainstem / cord), and association (within a
hemisphere).*

***What "already recorded elsewhere" means, stated precisely, because this preamble used to overstate
it.*** *Many tracts are **named on the edges of the entries that use them** — the optic nerve and
radiation, the medial and lateral lemniscus, the three cerebellar peduncles, the corticospinal tract,
the stria terminalis and ventral amygdalofugal pathway, the stria medullaris and fasciculus
retroflexus, the mammillothalamic tract, the medial longitudinal fasciculus. **Being named on an edge
is not having an entry.** Checked across all twenty files on 2026-07-25: the **only** tract entries in
the source are the **optic chiasm** (file 1), the **spinal cord white matter** (file 16), and the four
below. The cerebellum entry (file 10) had already caught this preamble's earlier wording and recorded
that none of the three peduncles has an entry here; that wording is corrected rather than defended.
**Whether a named-but-entry-less tract warrants an entry is a decision, not a finding**, and the
candidates are collected at the end of this file.*

## Corpus callosum — the great interhemispheric commissure (with the anterior commissure)

- **Function:** the largest white-matter tract in the brain — interhemispheric transmission linking
  mostly homotopic (and some heterotopic) cortex, with either integrating or inhibitory (lateralising)
  effect. Topographic: rostrum and genu (prefrontal — thin, slow fibres), body (motor /
  somatosensory), isthmus and splenium (parietal / temporal / occipital — the largest, fastest fibres,
  including the visual splenium). The **anterior commissure** is the smaller, older commissure (more
  than ten times smaller), linking the two temporal lobes, olfactory structures, and amygdalae; the
  **hippocampal** and **posterior** (pupillary / vertical-gaze) commissures are smaller still.
  **Refined from the auditory pass, and the refinement generalises a warning.**
  - **Laminar routing is asymmetric between origin and termination.** For the auditory fibres,
    origin is **layers 3 and 5** (about 90% of the projection) and termination is **throughout layers
    2–6**, densest in **2 and 3** and **sparsest in layer 4**. **The callosal input avoids the
    layer the thalamic driver targets.**
  - **How much of a map is callosally connected differs by modality, and this entry's "homotopic"
    hides it.** In **vision** the connections are restricted to the representation of the
    **vertical meridian**; in **somatosensation**, to **proximal body** representations — in both,
    to the representational **midline**, where two half-maps must be joined. In **audition** there
    is no such midline and the connections are **widespread across the entire tonotopic map**.
    **So "homotopic" is true of all three and describes something different in each**, and a
    reader taking the visual case as the general one would badly misjudge the auditory bandwidth.
  - **Auditory transcallosal fibres run in the central body, posterior body and dorsal splenium** —
    which refines this entry's "isthmus and splenium (parietal / temporal / occipital)" for the
    auditory case specifically.
  - **Sensory association cortices are more callosally connected than primary sensory cortices**,
    and carry proportionally more heterotopic traffic.
  - **The functional sign is not fixed.** All callosal fibres are excitatory pyramidal-cell axons;
    the inhibitory effects reported in every modality are **feedforward, through local interneurons
    the fibres excite**. This entry's "either integrating or inhibitory (lateralising) effect" is
    therefore right about the outcome and should not be read as two kinds of fibre. **In the
    auditory case the lateralising effect is measurable: callosotomy in rhesus abolishes a
    left-right asymmetry rather than merely disconnecting it**, which makes the asymmetry an
    equilibrium the edge maintains.
  *(Class 1 — Imig & Brugge 1978; Kelly & Wong 1981; Code & Winer 1985, 1986; Lee & Winer 2008;
  Lomber et al. 1994; Clarke et al. 1995; Gazzaniga 1987; Poremba et al. 2004. Stated in full at
  the primary auditory cortex entry. **Six of those eight keys are verified there and two are not
  present anywhere in that file** — see the reference section below, which checked the deferral.)*
- **Inputs:** *(This entry is **transmission, not processing**. Its edges are **routing statements**,
  not payload transfers: the payload is typed at the cortical entry that produces it and again at the
  one that consumes it, and the lines here record which region-to-region edge rides on which sector of
  this tract. Fan-in and fan-out read **none** throughout, because no synapse occurs here — the same
  form the optic-chiasm entry uses.)*
  - **← the cerebral cortex of either hemisphere**, from **callosal projection neurons in layers 3
    and 5** — **carries:** routing only; no transform. **Fan-in:** none (no synapse here). **This
    endpoint names a class** covering nearly every cortical entry in the source, and the class is
    intrinsic to the structure rather than a defect in the line: a commissure linking most of the
    cortex to most of the cortex has no smaller honest producer. **What can be resolved is which
    edges are actually declared as routed through it**, and two are, below.
  - **← the primary auditory cortex**, from the contralateral side, through the **central body,
    posterior body and dorsal splenium** — **carries:** routing only; the payload at both ends is
    **the same frequency band's activity from the other hemisphere, which sharpens rather than adds**.
    **Fan-in:** none. **Both ends of the region-to-region edge are in file 2**, whose primary
    auditory cortex declares the callosal input and names these three sectors. **Two-ended, and the
    sector attribution is declared at that end and matched here.**
  - **← the inferior frontal gyrus**, from the contralateral side — **carries:** routing only;
    payload **owed** at the region-to-region ends. **Fan-in:** none. **The consumer declares it**
    (file 11), whose right inferior frontal gyrus entry transcribed this entry's laminar detail onto
    that edge. **Two-ended.**
- **Outputs:**
  - **→ the homotopic cortex of the opposite hemisphere**, terminating **throughout layers 2–6**,
    densest in **2 and 3** and sparsest in **layer 4** — **carries:** routing only; no transform.
    **Fan-out:** none (no synapse here). **Same class endpoint as the input limb**, and the same
    reason.
  - **→ heterotopic cortex of the opposite hemisphere** — **carries:** routing only. **Fan-out:**
    none. **A separate limb, not a variant of the one above**: the sensory association cortices carry
    proportionally more of this traffic than the primary sensory cortices do, so the two limbs have
    different origins and different densities. **This endpoint names a class and no entry in the
    source declares a heterotopic callosal edge. Owed: name one, or record that the source has none.**
  - **→ the contralateral temporal lobe, olfactory structures and amygdala**, via the **anterior
    commissure** — **carries:** routing only. **Fan-out:** none. **No entry in the source declares an
    edge routed through the anterior commissure.** File 8 names it, but as the landmark at which the
    fornix splits, not as a tract carrying one of its edges. **So this limb has traffic described in
    prose and no declared edge at either end. Owed at both ends.**
  - **→ the contralateral hippocampal formation**, via the **hippocampal commissure**, and **→ the
    contralateral pretectal and vertical-gaze structures**, via the **posterior commissure** —
    **carries:** routing only. **Fan-out:** none. **Neither string appears anywhere in the source
    outside this entry**, checked 2026-07-25. The posterior commissure's stated function — pupillary
    and vertical-gaze — belongs to structures that do have entries, the pretectum and the gaze
    integrators (file 15), and that entry does not name it. **Owed: two tracts with a stated function
    and no traffic declared at either end.**
- **Internal structure and internal data flow:** **sub-elements: five sectors** — **rostrum**,
  **genu**, **body** (with its anterior, central and posterior parts), **isthmus** and **splenium**.
  They meet §3's test for sub-elements rather than properties on two grounds at once: **they carry
  different traffic to different targets** (prefrontal at the rostrum and genu, motor and
  somatosensory through the body, parietal, temporal and occipital at the isthmus and splenium) **and
  they differ in fibre calibre**, thin and slow rostrally against large and fast caudally, which is a
  transmission-rate difference and therefore a property of the payload's timing. The routed edges
  above are already written on this division — the auditory edge on the central body, posterior body
  and dorsal splenium.
  **There are no internal edges.** No synapse occurs here, so the sectors are parallel channels rather
  than a circuit; this entry has sub-elements and a routing rule and no internal data flow, the same
  shape the optic-chiasm entry records. **This is a positive "not applicable," not an unfilled gap.**
  **Owed — this entry is four tracts, not one.** The anterior, hippocampal and posterior commissures
  are separate commissural tracts with their own endpoints, and none of them shares this tract's
  five-sector topography, so they are not sub-elements of it. They are bundled into this entry by the
  heading and by nothing else. **Owed: give them entries, or state why a commissure smaller than the
  callosum does not warrant one.**
  *(Class 1 for the sector topography and the auditory sector attribution, from the sources listed
  under Function; Class 3 for the standard rostrum-to-splenium division. The reading that fibre
  calibre makes the sectors sub-elements rather than properties is Claude's, Class 2. No primary
  source was opened and no search was run for this entry in this pass.)*
- **Neurons:** none (fibre tract; a few interstitial intracallosal neurons). **Synapses:** none.
- **Axons:** **about 200 million** (range 200–300 million; Aboitiz et al. 1992, **electron
  microscopy** — the primary human count; the callosum's well-defined borders make it one of the few
  exactly-countable tracts). Cross-sectional area about 500–700 mm². Thin, slow fibres dominate (genu
  and association traffic); a minority of large, fast 3–5 µm fibres cross the isthmus and splenium
  (motor, visual).
- **Grey-matter volume:** not applicable. **White-matter volume:** the single largest white-matter
  structure in the brain; specific figure not recorded. **Myelination:** chiefly myelinated; g-ratio
  tracks the thin-to-thick gradient.
- **Pass:** 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements under the transmission-only convention; the auditory and inferior-frontal routed edges confirmed two-ended against files 2 and 11; Internal structure slot added with the five sectors as sub-elements and no internal edges; the three smaller commissures recorded as tracts bundled into this entry with no routed edge at either end

## Internal capsule — the great projection tract (cortex ↔ subcortex / brainstem / cord)

- **Function:** the compact projection highway funnelling every corticofugal and thalamocortical fibre
  between the caudate nucleus and thalamus (medial) and the lentiform nucleus (lateral). **Anterior
  limb:** frontopontine fibres and the anterior thalamic radiation, serving the prefrontal cortex.
  **Genu:** corticobulbar fibres, to the cranial-nerve motor nuclei. **Posterior limb:** the
  **corticospinal tract**, the corticorubral fibres, and the superior thalamic radiation
  (somatosensory, to the primary somatosensory cortex). **Retrolenticular part:** the **optic
  radiation**, from the lateral geniculate nucleus to the primary visual cortex. **Sublenticular
  part:** the **auditory radiation**, from the medial geniculate nucleus to the primary auditory
  cortex. A bottleneck whose small lacunar lesions cause dense hemiplegia.
- **Inputs:** *(Routing statements, not payload transfers; fan-in and fan-out read **none**
  throughout, as at the corpus callosum above.)*
  - **← the cerebral cortex**, corticofugal fibres from every lobe — **carries:** routing only; no
    transform. **Fan-in:** none (no synapse here). **This endpoint names a class**, and as with the
    callosum the class is intrinsic to the structure. **The named corticofugal edges that other
    entries declare as routed through this tract are:** the **corticospinal tract from the primary
    motor cortex** (files 5 and 16, the latter naming this tract explicitly), and the corticothalamic
    return traffic below.
  - **← the thalamus**, thalamocortical fibres from every relay nucleus — **carries:** routing only.
    **Fan-in:** none. **This endpoint names a class.** The named thalamocortical edges declared as
    routed through this tract are the **optic radiation** (file 12's lateral geniculate traffic to
    file 1's primary visual cortex), the **auditory radiation** (to file 2's primary auditory
    cortex), the **superior thalamic radiation** (file 5's ventral posterior complex to the primary
    somatosensory cortex), and the **anterior thalamic radiation** (file 12's mediodorsal nucleus to
    the prefrontal cortex, file 11).
- **Outputs:**
  - **→ the brainstem and spinal cord**, through the **posterior limb** and **genu** — **carries:**
    routing only; the corticospinal and corticobulbar motor commands, typed at their cortical origins
    and at the ventral horn and cranial-nerve nuclei that consume them. **Fan-out:** none. **The
    consumer declares this tract by name** (file 16), whose spinal white-matter entry records "the
    corticospinal tract from the primary motor cortex through the internal capsule those entries
    recorded." **Two-ended.**
  - **→ the thalamic reticular nucleus**, from corticothalamic fibres traversing this tract —
    **carries:** routing only; the collateral copy of the cortex's outgoing traffic that the
    reticular nucleus gates on. **Fan-out:** none. **The consumer declares it** (file 12), which
    records that only about three quarters of the corticothalamic fibres passing through this tract
    gave visible collaterals there, so roughly a quarter did not. **Two-ended, and that quarter is a
    finding about this tract rather than about the nucleus: the capsule is not a uniform bundle at
    this level.**
  - **→ the red nucleus**, corticorubral fibres through the **posterior limb** — **carries:** routing
    only. **Fan-out:** none. **This consumer has no entry in any of the twenty files** — a standing
    item, recorded at files 10, 14 and 16 as well. **Owed at the consumer's end, which does not yet
    exist.**
  - **→ the pontine nuclei**, frontopontine fibres through the **anterior limb** — **carries:**
    routing only. **Fan-out:** none. **This consumer has no entry in any of the twenty files** — the
    other half of the same standing item, and the load-bearing half, since the corticopontine stage is
    recorded elsewhere as a processing stage rather than a relay. **Owed at the consumer's end, which
    does not yet exist.**
- **Internal structure and internal data flow:** **sub-elements: five parts** — the **anterior
  limb**, the **genu**, the **posterior limb**, the **retrolenticular part** and the **sublenticular
  part**. They meet §3's test decisively: **each carries a different fibre system to a different
  target**, and every routed edge above is already attributed to one of them. **There are no internal
  edges** — no synapse occurs here, so the parts are parallel channels and not a circuit, the same
  shape as the corpus callosum and the optic chiasm. **This is a positive "not applicable."**
  *(Class 3 — general anatomy for the five parts and their fibre systems; the collateral figure is
  Class 1 at its far end, file 12. The reading that the un-collateralised quarter is a fact about the
  capsule is Claude's, Class 2. No primary source was opened and no search was run for this entry in
  this pass.)*
- **Neurons:** none. **Synapses:** none.
- **Axons:** carries the **corticospinal tract at about 1 million axons per side** (classic order
  estimate; about 1.1 million pyramidal-tract fibres above the decussation, secondary compilation)
  plus the thalamocortical radiations (counts unknown). **The per-limb split of that total is
  unknown**, which is what would be needed to size any one of the routed edges above.
- **Grey-matter volume:** not applicable. **White-matter volume:** not recorded. **Myelination:**
  heavily myelinated projection tract.
- **Pass:** 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements; each limb mapped to the region-to-region edge it carries and its far-end file; the corticothalamic collateral into the thalamic reticular nucleus written from file 12; Internal structure slot added with the five limbs as sub-elements and no internal edges

## Fornix — the hippocampal output tract (Papez)

- **Function:** the principal output (and return input) pathway of the hippocampal formation — fimbria
  → crus → body → columns, splitting at the anterior commissure into a **post-commissural** limb to
  the **mammillary bodies** and **anterior thalamus** (the Papez memory circuit) and a
  **pre-commissural** limb to the septum, basal forebrain **and prefrontal cortex**; the
  septo-hippocampal (cholinergic, theta-pacing) fibres return through it. Topography: the lateral fornix carries the anterior
  hippocampus and the medial fornix the posterior hippocampus; the left carries verbal and the right
  visuospatial memory.
- **Inputs:** *(Routing statements, not payload transfers; fan-in and fan-out read **none**
  throughout. **This is the best-declared tract in the file** — six of its routed edges are written at
  both of their region ends, in four different files, by passes that did not consult each other.)*
  - **← the hippocampal formation**, from the **subiculum**, into the **fimbria** — **carries:**
    routing only; the payload at the region ends is the **completed episode** — the bound, retrievable
    pattern, addressable by any fragment of itself, and only partly writable there, since "an episode"
    has no units and no frame. **Fan-in:** none (no synapse here). **The producer declares an edge to
    this tract by name and explains it as a routing statement** (file 8), which then writes the
    regions it reaches as their own edges. **Two-ended, and the far end already uses this
    convention.**
  - **← the medial septum, cholinergic cells** — **carries:** routing only; the payload at the region
    ends is a cholinergic modulatory signal. **Fan-in:** none. **Both region ends declare it** (file
    13 as producer, file 8 as consumer), each naming this tract and the pre-commissural limb.
    **Two-ended.**
  - **← the medial septum, parvalbumin-expressing GABAergic pacemaker cells** — **carries:** routing
    only; the payload at the region ends is the **theta timing reference**. **Fan-in:** none. **Both
    region ends declare it** (files 13 and 8), each naming this tract. **Two-ended.**
  - **← the medial septum, glutamatergic cells** — **carries:** routing only; the payload at the
    region ends is a **tonic drive**. **Fan-in:** none. **Both region ends declare it** (files 13 and
    8). **Two-ended.** *(The three septal limbs are three separate lines here because they are three
    separate lines at both region ends — three cell populations in one nucleus with three different
    payloads riding the same tract. A tract entry that collapsed them would lose a distinction the
    grey-matter entries had already made.)*
- **Outputs:**
  - **→ the mammillary bodies and the anterior thalamic nuclei**, through the **post-commissural
    limb** — **carries:** routing only; the completed episode, as above. **Fan-out:** none. **Both
    region ends declare it** (file 8 as producer; file 12's anterior nuclei name the subiculum and
    this limb by name, and file 14 holds the mammillary end). **Two-ended.** **This is the Papez limb**
    — hippocampal formation → mammillary bodies → mammillothalamic tract → anterior thalamus →
    cingulate and retrosplenial cortex — and every stage of it now has an entry.
  - **→ the hypothalamus** — **carries:** routing only; payload **owed** at both region ends.
    **Fan-out:** none. **Both region ends declare it** (files 8 and 14), each naming this tract.
    **Two-ended, and owed at both ends.**
  - **→ the orbitofrontal / ventromedial prefrontal cortex and the anterior cingulate cortex**,
    through the **pre-commissural limb** — **carries:** routing only; the payload at the region ends
    is the **completed episode**, as on the fimbrial input above and owed at both ends there.
    **Fan-out:** none. **Both region ends declare it** (file 8 as producer, from the subiculum; file
    11 at its orbitofrontal / ventromedial and anterior cingulate entries, written 2026-08-15).
    **Two-ended. Added 2026-08-15, and this tract carried no prefrontal traffic before that date.**
    ***This is the one routed edge in the file for which the tract is a positive finding rather than
    a route.*** *The producing study established that this projection travels by the fornix **and by
    no other route** — by injecting the tracer in macaques whose fornix had been transected months
    beforehand, in which **no prefrontal label appeared at all**, while comparable injections in
    intact animals showed it. **So for this edge the tract is not cabling that could be described or
    skipped: cutting it abolishes the connection, and no parallel path carries it.** Every other line
    in this entry records which tract an edge rides on; this one records that there is only one.
    **A transmission entry can carry a finding after all, and the finding is a negative about
    alternatives.** *(Class 1 — Aggleton, Wright, Rosene & Saunders 2015, *Cerebral Cortex*
    25(11):4351, macaque, anterograde autoradiography with fornix-transected cases. **Verified
    against the Oxford Academic publisher record, 2026-08-15**; open access, full text read.)*
    ***Which limb, researched 2026-08-15 and now settled.*** *The producing study did not divide the
    tract at the anterior commissure, and file 8 recorded the limb as **owed** rather than inferring
    it from the targets' position. **It is the pre-commissural limb**, which innervates orbital and
    medial prefrontal cortex; the post-commissural limb goes to the anterior thalamus, hypothalamus
    and mammillary bodies.* *(Class 1 — **Coad, Craig, Louch, Aggleton, Vann & Metzler-Baddeley
    2020**, *Precommissural and postcommissural fornix microstructure in healthy aging and
    cognition*, **Brain and Neuroscience Advances**; doi 10.1177/2398212819899316; PubMed 32219177.
    Human, 149 asymptomatic participants, multi-parametric magnetic resonance imaging. **Verified
    against the SAGE publisher record and PubMed, 2026-08-15.** **The limb assignment is that
    paper's anatomical background rather than its result**, and it cites Aggleton 2015 among its
    sources for it — so the assignment and the sole-route finding come from the same lineage and are
    **not two independent confirmations**.)*
    ***And the same background names a third pre-commissural destination this source does not
    carry.*** *The pre-commissural fornix is described as innervating the **ventral striatum /
    nucleus accumbens** alongside the basal forebrain and prefrontal cortex. **No entry in this
    source routes a hippocampal edge to the ventral striatum through this tract** — file 8's
    hippocampal formation declares an output to the **ventral pallidum**, which is the next stage
    rather than this one. **Owed: check file 9 for a hippocampal input to the accumbens, and if it
    exists, route it here.**
  - **→ the septum and basal forebrain**, through the **pre-commissural limb** — **carries:** routing
    only; payload **owed** at the region ends. **Fan-out:** none. **The producer declares it** (file
    8), naming this limb. **The consumer is split:** the basal forebrain has an entry (file 13) and
    the **septal nuclei have no entry in any of the twenty files**, checked 2026-07-25 — the same
    missing producer the habenula entry records at its stria-medullaris input. **So the return arm of
    the septo-hippocampal loop has a described tract, a described payload at one end, and no entry for
    the structure at the other.**
- **Internal structure and internal data flow:** **sub-elements: the pre-commissural limb and the
  post-commissural limb**, which are sub-elements on the strongest ground in this file — **they run in
  opposite functional directions to entirely different targets**, and every routed edge above is
  already attributed to one of them. The **fimbria, crus, body and columns** are the tract's segments
  along its length rather than parallel channels: the same fibres pass through all four in sequence,
  so they are **properties of the tract's course, not sub-elements**, by §3's test that a sub-element
  is distinguished by a different target or a different payload.
  **The pre / post division was strengthened on 2026-08-15 and is now the best-evidenced sub-element
  pair in the file.** It was written on general anatomy; it now rests on a human imaging study that
  measures the two limbs **separately** and finds them forming distinct networks — basal-forebrain
  and frontal on one side, diencephalic on the other. **A sub-element division a method can resolve
  is on different ground from one a description asserts**, and this one can now be measured rather
  than only stated. **The prefrontal destination added above rides the pre-commissural limb**, so
  three destination sets sit on that one sub-element — septum and basal forebrain, prefrontal cortex,
  and the owed ventral-striatal one — while the post-commissural limb carries the Papez traffic
  alone.
  A second division does meet the test
  — the **lateral fornix** carries the anterior hippocampus and the **medial fornix** the posterior
  hippocampus, which is a different origin and therefore a different payload; whether it is preserved
  as far as the targets is **owed**.
  **There are no internal edges** — no synapse occurs here. **A positive "not applicable."**
  *(Class 3 — general anatomy for the segments and the lateral / medial topography; **no source has
  been opened for those, so they are unverified — owed.** **Class 1 for the pre / post limb division
  and its two destination networks** — Coad et al. 2020, verified against the publisher record
  2026-08-15. The reading that the segments are properties and the limbs are sub-elements is
  Claude's, Class 2, applying §3's test.)*
- **Neurons:** none. **Synapses:** none.
- **Axons:** soft / no clean human count pinned (classic order about 1 million). **The per-limb split
  is unknown**, and the pre-commissural limb's share is what would size the septo-hippocampal return.
- **Grey-matter volume:** not applicable. **White-matter volume:** not recorded. **Myelination:**
  myelinated tract.
- **Pass:** 2026-08-15 — the prefrontal destination set written as a routed edge and confirmed two-ended against files 8 and 11; the fornix-transection evidence recorded, making this the one edge here for which the tract is load-bearing rather than descriptive; the limb researched and settled as pre-commissural, discharging the mark file 8 left owed; the pre / post sub-element division upgraded from general anatomy to a measured one; the pre-commissural ventral-striatal destination recorded as owed at file 9
- **Pass:** 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements; six routed edges confirmed two-ended against files 8, 12, 13 and 14, including the three separately-typed septal return limbs; Internal structure slot added with the pre- and post-commissural limbs as sub-elements and no internal edges

## Arcuate fasciculus / superior longitudinal fasciculus — the dorsal language tract (with the long association fasciculi)

- **Function:** the dorsal-stream association tract arching from temporoparietal cortex (the posterior
  superior temporal gyrus and the sylvian parieto-temporal area, and the supramarginal gyrus) to the
  frontal lobe (Broca's area, Brodmann areas 44 and 45, and premotor cortex) — the audiomotor and
  phonological "where" pathway, left-dominant for language. Part of the **superior longitudinal
  fasciculus** system, whose branches are numbered I, II and III. Companion long association fasciculi
  carry the other cortico-cortical streams already described: the **inferior longitudinal fasciculus**
  (occipito-temporal — the ventral "what" stream), the **inferior fronto-occipital fasciculus**
  (ventral semantic), the **uncinate fasciculus** (temporal pole ↔ orbitofrontal and ventrolateral
  prefrontal cortex — the ventral limbic link the temporal-pole and orbitofrontal entries imply), and
  the **cingulum** (beneath the cingulate cortex — linking the default-mode and Papez midline nodes,
  the tract the cingulate entries use).
- **Inputs:** *(Routing statements, not payload transfers; fan-in and fan-out read **none**
  throughout.)*
  - **← the supramarginal gyrus** — **carries:** routing only; the payload at the region ends is a
    **praxis / action-sequence code** and, on the left, a **phonological code** — the sound-form of
    words for the articulatory route, only partly writable there. **Fan-in:** none (no synapse here).
    **Both region ends declare it** (file 6 as producer, file 11's Broca's area as consumer), and both
    name this tract and **superior longitudinal fasciculus branch III** specifically. **Two-ended.**
  - **← the posterior superior temporal gyrus and the sylvian parieto-temporal area** — **carries:**
    routing only; payload **owed** at the region ends. **Fan-in:** none. **The consumer declares it**
    (file 11), and file 2's auditory entries name this tract as the one carrying the stream forward.
    **Two-ended.**
  - **← the temporal pole**, over the **uncinate fasciculus**, the **inferior longitudinal
    fasciculus**, the **middle longitudinal fasciculus** and this tract — **carries:** routing only;
    payload **owed**. **Fan-in:** none. **The far end declares all four by name** (file 7) and records
    that which pathway carries which of its edges is established only for the uncinate. **It also
    records that these tracts "have their own entries in the white-matter-tracts file," and that is
    wrong for the middle longitudinal fasciculus**, which has no entry here or anywhere, checked
    2026-07-25. **Owed as a cross-file edit at that entry (file 7).**
- **Outputs:**
  - **→ Broca's area and premotor cortex** — **carries:** routing only. **Fan-out:** none. **Both
    region ends declare it** (files 6 and 11), reciprocally with the supramarginal input above.
    **Two-ended.**
  - **→ the orbitofrontal and ventrolateral prefrontal cortex**, over the **uncinate fasciculus** —
    **carries:** routing only; payload **owed** at the region ends. **Fan-out:** none. **The far end
    declares this tract by name** (file 7), which is the one association pathway there whose edge
    attribution is established. **Two-ended.**
  - **→ the cingulate midline nodes**, over the **cingulum** — **carries:** routing only. **Fan-out:**
    none. **Four entries declare this tract by name** — the anterior cingulate cortex (file 11) and
    the midcingulate, posterior cingulate and retrosplenial entries (file 17), the last three
    recording it as routing rather than as an edge, which is the convention this entry uses.
    **Two-ended.**
  - **→ occipito-temporal cortex**, over the **inferior longitudinal fasciculus** — **carries:**
    routing only. **Fan-out:** none. **Named at one far end only** (file 7, as one of four pathways
    with no edge attributed to it). **The ventral "what" stream this tract is said to carry runs
    between entries in files 1 and 7, and neither declares an edge routed through it. Owed at both
    ends.**
  - **→ the ventral semantic stream**, over the **inferior fronto-occipital fasciculus** —
    **carries:** routing only. **Fan-out:** none. **This string appears nowhere in the source outside
    this entry**, checked 2026-07-25: no entry names it, no edge is declared as routed through it, and
    its endpoints are given here only as a stream and not as regions. **It is a tract with a stated
    function and no traffic** — the mirror of a dangling endpoint, and it fails silently for the same
    reason. **Owed: attribute an edge to it, or withdraw it.**
- **Internal structure and internal data flow:** **sub-elements: the three numbered branches of the
  superior longitudinal fasciculus — I, II and III** — which meet §3's test because they connect
  different cortical territories, and **branch III is already named on the supramarginal routed edge
  above** by both of its region ends. The **arcuate** is recorded as the arching temporo-frontal
  component of the same system; whether it is a branch of it or a tract adjacent to it is **contested
  in the literature and recorded as contested rather than resolved by preference**, in the same way
  the source records the dispute over layer 4B.
  **There are no internal edges** — no synapse occurs here. **A positive "not applicable."**
  **Owed — this entry is five tracts, not one.** The inferior longitudinal, inferior fronto-occipital,
  uncinate and cingulum fasciculi are separate association tracts with separate endpoints, and none of
  them is a branch of the superior longitudinal fasciculus system. They are bundled into this entry by
  the heading and by nothing else, which is why three of them have no declared traffic while the
  cingulum has four declarations. **Owed: give them entries, or state why the association tracts are
  held as a set when the commissural and projection tracts are not.**
  *(Class 3 — general anatomy for the branches and the companion fasciculi; the branch-III attribution
  is Class 1 at its far ends, files 6 and 11. The reading that the arcuate's status is contested, and
  that the entry is five tracts, is Claude's, Class 2. No primary source was opened and no search was
  run for this entry in this pass.)*
- **Neurons:** none. **Synapses:** none.
- **Axons:** counts largely unknown, but a rare absolute estimate exists — direct connections between
  the posterior and anterior language regions are **surprisingly sparse**, under about 5% of the axons
  in the arcuate / superior longitudinal trunk (Zikopoulos & Barbas lineage, absolute-axon-number
  estimate: a median of about 6,200 axons between areas within a hemisphere and about 1,300
  interhemispherically). **That figure is a fan measure on a routed edge and it does not fit the fan
  slots**: it counts inter-areal axons rather than contacts per cell, and the far end (file 11)
  records the same mismatch and marks it owed. **Owed at both ends: reconcile the two measures.**
- **Grey-matter volume:** not applicable. **White-matter volume:** not recorded. **Myelination:**
  myelinated association fibres.
- **Pass:** 2026-07-25 — abbreviations expanded to full names; prose Inputs / Outputs converted to typed routing statements; the supramarginal and inferior-frontal routed edges confirmed two-ended against files 6 and 11; the entry recorded as five tracts in one slot set; the inferior fronto-occipital fasciculus recorded as carrying no edge declared anywhere in the source; Internal structure slot added

## Medial longitudinal fasciculus — the gaze-yoking brainstem tract (paired, brainstem tegmentum)

- **Function:** a paired, heavily myelinated tegmental tract running the length of the brainstem just
  beneath the floor of the fourth ventricle and the cerebral aqueduct, from the rostral midbrain to
  the cervical cord. It is the common cable of **conjugate gaze**: it carries the vestibulo-ocular
  reflex command from the vestibular nuclei forward to the ocular motor nuclei, it **yokes the two
  eyes** by carrying the abducens internuclear axons across to the contralateral medial-rectus motor
  pool, and it carries the medial vestibulospinal fibres down to the cervical cord. Its lesion
  produces **internuclear ophthalmoplegia** — adduction fails on the side of the lesion while the
  abducting eye shows nystagmus — which is the clinical signature that makes the yoking edge visible
  as a separate thing from either motor nucleus.
  **A naming caution this entry exists to hold.** The **rostral interstitial nucleus of the medial
  longitudinal fasciculus** is a **grey-matter nucleus named for its position beside this tract**, not
  a part of it. It is the vertical saccade burst generator, it is named on edges in files 14 and 15,
  and it belongs to the reticular-formation entry (file 14), which records it as an owed sub-element.
  **The string therefore appears in the source in two entirely different roles**, and a reader
  matching on the tract's name will collect the nucleus with it.
- **Inputs:** *(Routing statements, not payload transfers; fan-in and fan-out read **none**
  throughout, as at the other tract entries.)*
  - **← the vestibular nuclei** — **carries:** routing only; the payload at the region ends is the
    **vestibulo-ocular reflex command** — an eye-velocity signal equal and opposite to head rotation,
    driven chiefly by the semicircular-canal line, and the fastest gaze-stabilising reflex.
    **Fan-in:** none (no synapse here). **Both region ends declare it and name this tract** (file 3 as
    producer, file 15 as consumer). **Two-ended.**
  - **← the abducens nucleus**, from its **internuclear neurons** — **carries:** routing only; the
    payload at the region end is the yoking signal that makes the two eyes move together in
    horizontal gaze. **Fan-in:** none. **The far end is inside file 15's ocular-motor-nuclei entry**,
    which names this tract and records the edge as one that "is named in Function and should be typed
    as an internal edge," marking it **owed**. **Owed at that entry: type it.**
  - **← the gaze neural integrators** — the **nucleus prepositus hypoglossi** with the medial
    vestibular nucleus (horizontal) and the **interstitial nucleus of Cajal** (vertical) —
    **carries:** routing only; the payload at the region ends is **eye position**, the integrated
    signal that holds the eye where the burst put it. **Fan-in:** none. **Neither far end names this
    tract** (file 15 declares the integrator edge to the ocular motor nuclei and attributes no tract
    to it). **Owed at both ends**, and this line is **Class 3** here, not transcribed from a
    declaring far end.
- **Outputs:**
  - **→ the ocular motor nuclei** — the **oculomotor**, **trochlear** and **abducens** nuclei
    (cranial nerves III, IV and VI) — **carries:** routing only. **Fan-out:** none. **Both region
    ends declare it and name this tract** (files 3 and 15). **Two-ended**, and this is the edge that
    makes the entry worth writing: it is one of the few routed edges in the source declared, named
    and typed at both of its region ends before its tract had an entry at all.
  - **→ the contralateral oculomotor medial-rectus pool**, from the abducens internuclear neurons —
    **carries:** routing only. **Fan-out:** none. **Owed at file 15**, as above. **This limb crosses
    the midline**, which no other limb of this tract does, and that crossing is what conjugate
    horizontal gaze consists of.
  - **→ the cervical spinal cord**, as the **medial vestibulospinal** fibres — **carries:** routing
    only; the payload at the region ends is a head- and neck-stabilising postural command.
    **Fan-out:** none. **Neither far end names this tract:** the vestibular entry's output reads
    "→ spinal cord (vestibulospinal tracts)" (file 3) and the spinal white-matter entry names
    "vestibulospinal (antigravity / balance)" among its descending columns (file 16), and **neither
    separates the medial tract from the lateral one** — the lateral vestibulospinal tract descends in
    the ventral funiculus and the medial descends here, to different targets and different segmental
    levels. **Owed at both ends: split the vestibulospinal endpoint into its medial and lateral
    limbs.** **Class 3** here.
- **Internal structure and internal data flow:** **sub-elements: an ascending limb and a descending
  limb.** They meet §3's test — **different targets and different payloads**: the ascending limb
  carries the vestibulo-ocular and yoking traffic rostrally to the ocular motor nuclei, and the
  descending limb carries the medial vestibulospinal fibres caudally to the cervical cord. Every
  routed edge above is already attributed to one of them. **There are no internal edges** — no synapse
  occurs here, so the limbs are parallel channels and not a circuit. **A positive "not applicable."**
  *(Class 3 — general brainstem anatomy for the tract's course, its two limbs and the internuclear
  ophthalmoplegia sign; Class 1 at the far ends for the vestibulo-ocular payload, files 3 and 15. The
  reading that the two limbs are sub-elements rather than properties is Claude's, Class 2. No primary
  source was opened and no search was run for this entry in this pass.)*
- **Neurons:** none (fibre tract). **Synapses:** none.
- **Axons:** counts unknown, at either limb. **The per-limb split is unknown**, as at the other tracts
  in this file.
- **Grey-matter volume:** not applicable. **White-matter volume:** not recorded. **Myelination:**
  heavily myelinated, and among the earliest tracts in the brain to myelinate; g-ratio unknown.
- **Pass:** 2026-07-25 — new entry; the gaze-yoking tract, written because it carries more declared traffic than three of the four tracts already here; the vestibulo-ocular routed edge confirmed two-ended against files 3 and 15; the abducens internuclear yoking limb recorded as owed at file 15; the nucleus named for the tract distinguished from the tract; Internal structure slot added with the ascending and descending limbs as sub-elements and no internal edges

**The white-matter highways are described:** the corpus callosum (with the anterior commissure)
between the hemispheres, the internal capsule between cortex and the subcortical and spinal targets,
the fornix as the hippocampal and Papez output, the arcuate / superior longitudinal fasciculus
(with the inferior longitudinal, inferior fronto-occipital, uncinate and cingulum fasciculi) as the
intrahemispheric association streams, and the medial longitudinal fasciculus as the brainstem gaze
cable — transmission only, no processing, like the optic chiasm and the spinal white-matter columns. The one firm number is the callosum's **about 200 million axons**
(Aboitiz et al. 1992); the corticospinal figure of about 1 million is an order estimate, and the
fornix and association-fascicle counts stay soft, with the arcuate's sparse-connection finding
recorded.

**Tracts named on other files' edges with no entry anywhere**, checked across all twenty files on
2026-07-25. Whether any of them warrants an entry is a decision, not a finding, and it is recorded
here so the decision has an inventory to work from. **The heaviest of them, the medial longitudinal
fasciculus, has been taken off this list and given an entry above**, on the ground that it carried
more declared traffic — a routed edge typed at both region ends in files 3 and 15 — than three of the
four tracts that already had entries. The remainder: the **three cerebellar peduncles** (file 10, which
records their absence here); the **ansa lenticularis, lenticular fasciculus and nigrostriatal bundle**
(file 9, which records the same); the **middle longitudinal fasciculus** (file 7, which wrongly
believes it has an entry here); the **mammillothalamic tract** (files 8, 12 and 14); the **stria
medullaris** and **fasciculus retroflexus** (file 17); the **stria terminalis** and **ventral
amygdalofugal pathway** (file 8); the **perforant path** (file 8); the **medial** and **lateral
lemniscus**; the **optic nerve**, **optic tract** and **optic radiation**.

**And the inventory runs the other way too.** Three tracts in this file have a stated function and no
declared traffic at either end: the **anterior commissure**, the **posterior commissure**, and the
**inferior fronto-occipital fasciculus**. A tract with no routed edge is the mirror of a region named
on an edge with no entry, and it fails just as silently — the entry reads as complete on its own.

---


## References

*(Section added 2026-08-12 under source design §2a; **statuses corrected 2026-08-15** — a key read
off a publisher, journal or PubMed record **is verified against that record**, per §2a's rule that
searching *is* the verification, and verification of data does not run to a person at all. Each full
reference given here was obtained by
a web search run in this pass against publisher, journal or PubMed records — no reference is
written from recall. Keys reading **owed** were not searched in this pass.)*

**12 distinct keys, 13 mentions. 3 verified against a publisher or PubMed record; 6 resolved by
deferral to file 2; 2 deferrals that fail; 1 owed.** *(Two keys added 2026-08-15 with the fornix's
prefrontal edge — the first primary sources this file has opened for any entry other than the
callosum.)* The smallest key list in the source, which follows from the file's
own nature: transmission entries carry no payload, so they cite little.

**Two keys were added 2026-08-15, both at the fornix's prefrontal edge, and both were opened.**

- **Aggleton, Wright, Rosene & Saunders 2015 (Cerebral Cortex 25(11):4351)** — Complementary patterns of direct amygdala and hippocampal projections to the macaque prefrontal cortex; doi 10.1093/cercor/bhv019; PubMed 25715284. **Macaque**, 26 animals, anterograde autoradiography, **including cases with the fornix transected 2–12 months beforehand**. *(Oxford Academic publisher record, open access, full text read; searched 2026-08-15.)* **Verified.** **The transection cases are what make *the fornix is the only route* a positive finding rather than an untested assumption**, and that is the reason this key sits in a transmission file at all. *(Fornix, prefrontal output edge.)*
- **Coad, Craig, Louch, Aggleton, Vann & Metzler-Baddeley 2020 (Brain and Neuroscience Advances)** — Precommissural and postcommissural fornix microstructure in healthy aging and cognition; doi 10.1177/2398212819899316; PubMed 32219177. **Human**, 149 asymptomatic participants aged 38–71; multi-parametric magnetic resonance imaging — neurite orientation dispersion and density imaging, quantitative magnetisation transfer, T1-relaxometry. *(SAGE publisher record and PubMed; searched 2026-08-15.)* **Verified.** **Used here for its anatomical background, not its result** — the limb-to-destination assignment it states, citing Aggleton 2015 among others. **Its actual result supports the Internal structure slot instead**: the two limbs are separable by measurement and behave differently with age, which is what moved the pre / post division off general anatomy. **Owed: the limb assignment and the sole-route finding share a lineage, so they are one source and not two.** *(Fornix, prefrontal output edge and Internal structure.)*

**Eight of the ten keys are not carried here at all.** Line 80–81 says of the callosal block that
its sources are *stated in full at the primary auditory cortex entry* — file 2. **That is the right
practice and it is checkable, so this pass checked it**, against file 2's own §2a reference section
of 2026-08-11, with no search required.

**Six of the eight are there. Two are not, and they are not anywhere in file 2.** *Imig & Brugge
1978*, *Kelly & Wong 1981*, *Code & Winer 1985* and *1986* (as two separate entries there),
*Lee & Winer 2008*, *Gazzaniga 1987* and *Poremba et al. 2004* all appear in file 2's list.
**Lomber et al. 1994 and Clarke et al. 1995 appear nowhere in file 2 — not in its reference
section and not in its body.** **So this file defers eight keys to a file that carries six of
them.** The deferral reads as complete and is not. **Owed: carry those two here, or add them at
file 2.**

**Two of the six that do resolve resolve ambiguously.** File 2 lists *Code & Winer 1985* and *Code
& Winer 1986* as **two entries**; this file writes them as one key, *Code & Winer 1985, 1986*.
And file 2 lists both *Lee & Winer 2008* and *Lee & Winer 2008a* — **two 2008 papers** — while this
file's single key names neither. **Owed at line 79: split the first, disambiguate the second.**

**The file's one firm number rests on a method the file states differently from the paper.** Line
147 attributes the ~200 million callosal axons to *Aboitiz et al. 1992, electron microscopy*. **The
paper's own abstract attributes its regional density measurements to light microscopy.** See that
entry — the picture is genuinely mixed and the entry says so rather than declaring the line wrong.

**And the same paper's fibre-calibre pattern is not the gradient this file builds a §3 judgement
on.** Lines 129–131 call the callosal sectors sub-elements partly on the ground that fibre calibre
runs thin-and-slow rostrally to large-and-fast caudally. **The paper reports a non-monotonic
pattern.** See the entry. **This is the finding to act on**, because it is load-bearing for a
structural decision rather than for a number.

**Species: the one searched paper is human**, twenty brains. **Of the eight deferred keys, the
callosotomy result at lines 76–78 is declared rhesus on the line**, and the rest are not given a
species here — they are given one at file 2, which is the point of the deferral.


- **Aboitiz et al. 1992** — Aboitiz, F., Scheibel, A.B., Fisher, R.S. & Zaidel, E. (1992). Fiber
  composition of the human corpus callosum. *Brain Research* 598(1–2): 143–153; doi
  10.1016/0006-8993(92)90178-c; PubMed 1486477. **Human, post-mortem: twenty brains, ten female and
  ten male**, with fibre densities calculated in **ten regions** of the callosum. *(Elsevier
  publisher record and PubMed.)* **Three findings, in increasing order of consequence.**
  **First, the sample is worth carrying and the file does not have it.** Twenty brains balanced by
  sex is a strong basis for a "firm" count, and line 147 gives none — which matters because the same
  slot elsewhere in the source has been found resting on one specimen.
  **Second, the method attribution does not match the paper's abstract.** Line 147 says **electron
  microscopy**; **the abstract says the regional differentiation of fibre types was revealed by
  light microscopic examination.** Some of the later literature does describe the paper's
  calibre results as reported by electron microscopy, so the paper may have used both — a light-
  microscopic survey with an electron-microscopic subset — and this pass read only the abstract.
  **Owed: open the methods and say which measurement the count comes from**; the distinction is not
  cosmetic, because the smallest unmyelinated fibres are countable by one method and not the other,
  and they are exactly what a total axon number turns on.
  **Third, and this is the one to act on: the paper's calibre pattern is not monotonic, and this
  entry's Internal-structure slot treats it as though it were.** Lines 129–131 give the sectors
  sub-element status partly on the ground of fibre calibre running *thin and slow rostrally against
  large and fast caudally* — a gradient. **The paper reports thin fibres densest in the genu,
  falling to a minimum at the posterior midbody, then rising again towards the splenium with a local
  fall at the posterior pole, and large fibres in the complementary pattern — peaking at the
  posterior midbody, with a local rise at the posterior pole.** **So thin fibres are dense at both
  ends and sparse in the middle, and the large-fibre peak is the posterior midbody rather than the
  isthmus and splenium generally.** Line 149–151's summary and the §3 judgement above it both read
  the pattern as a single slope. **The sub-element conclusion may still hold** — a non-monotonic
  calibre profile still distinguishes the sectors from one another — **but it does not hold for the
  reason given.** **Owed: restate the calibre pattern, then re-check the judgement that rests on
  it.** **Note also that the ~200 million total is not itself in the abstract**, which reports
  densities per region; a total is density times cross-sectional area, which is why line 149 carries
  the area on the next breath. **Whether the paper states the total or the file computed it is
  owed.** *(searched 2026-08-12; candidate. Lines 147, 458.)*
- **Clarke et al. 1995** — **owed, and the deferral fails.** Line 80 lists it among the sources
  *stated in full at the primary auditory cortex entry*. **The string appears nowhere in file 2** —
  not in its 190-entry reference section and not in its body, checked 2026-08-12 against the
  2026-08-11 version. **So this key has no full reference anywhere in the source.** It is one of two
  keys in the callosal block that bear specifically on callosal rather than cortical anatomy, which
  makes its absence more than bookkeeping. **Owed: carry it here, or add it at file 2.** *(Line 80.)*
- **Code & Winer 1985, 1986** — **resolved by deferral, ambiguously.** File 2's reference section
  carries **two separate entries**, *Code & Winer 1985* and *Code & Winer 1986*. This key names both
  years in one string, so it points at two papers at once and a reader following it will not know
  which supports which of the laminar claims at lines 56–59. **Owed: split into two keys**, then the
  deferral is clean. *(Line 79.)*
- **Gazzaniga 1987** — **resolved by deferral.** Present in file 2's reference section. It is
  presumably the source of the callosotomy material behind lines 72–78, and the file declares that
  result **rhesus** on the line. *(Line 80.)*
- **Imig & Brugge 1978** — **resolved by deferral.** Present in file 2's reference section. *(Line
  79.)*
- **Kelly & Wong 1981** — **resolved by deferral.** Present in file 2's reference section. *(Line
  79.)*
- **Lee & Winer 2008** — **resolved by deferral, ambiguously.** File 2's reference section carries
  **both** *Lee & Winer 2008* **and** *Lee & Winer 2008a* — two papers from the same authors in the
  same year. This key names one of them and cannot distinguish them. **Owed: say which, or carry
  both.** *(Line 79.)*
- **Lomber et al. 1994** — **owed, and the deferral fails.** As with *Clarke et al. 1995*: listed at
  line 80 as stated in full at file 2, **and the string appears nowhere in file 2**, checked
  2026-08-12. **The two failing deferrals are adjacent on the same line**, which is consistent with
  their having been added to this block after the block's own sources were written, and never
  carried back. **Owed: carry it here, or add it at file 2.** *(Line 80.)*
- **Poremba et al. 2004** — **resolved by deferral.** Present in file 2's reference section, which
  also carries a *Poremba et al. 2003*. *(Line 80.)*
- **Zikopoulos & Barbas lineage** — **owed**: not searched in this pass, **and the key carries no
  year and no title**, written as a lineage. **It is the file's second quantitative claim and its
  most surprising one** — that direct connections between the posterior and anterior language
  regions are under about 5% of the axons in the arcuate trunk, with a median of about 6,200
  inter-areal axons within a hemisphere and about 1,300 interhemispherically. **The citing line
  already records the harder problem**: those are inter-areal axon counts and the source's fan slots
  want contacts per cell, so the figure does not fit the slot it would go in, and file 11 records the
  same mismatch and marks it owed at that end. **Searching this key does not resolve that; it is a
  convention question, not a reference question.** But the reference is owed regardless, and it is
  the only key in this file whose claim is not deferred to another file. *(Line 371.)*
