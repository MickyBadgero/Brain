# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-21
---

---

# FILE 3 OF 20 — OTHER SENSES

**What is in this file.** The three senses that do not have a pathway section of their own: olfaction (epithelium, bulb and piriform cortex — the one sense that reaches cortex without a thalamic relay), taste, and the vestibular apparatus with its central nuclei.

**Size:** 880 lines, ~17.7k tokens (estimated from bytes, not tokenised). **Entries:** 7.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file:**

- **Olfactory epithelium — the chemical transducer (olfactory cleft, sensory front end)**
- **Olfactory bulb (layered forebrain outgrowth)**
- **Piriform + primary olfactory cortex (three-layered allocortex)**
- **Gustatory pathway — nucleus of the solitary tract → ventral posteromedial parvocellular thalamic nucleus → insular taste cortex**
- **Semicircular canals — the rotation transducer (membranous labyrinth, sensory front end)**
- **Otolith organs (utricle, saccule) — the linear-acceleration transducer (membranous labyrinth, sensory front end)**
- **Vestibular nuclei and the central vestibular pathway — where attitude is computed (brainstem → thalamus → parieto-insular cortex)**

---

# OTHER SENSES (olfactory, gustatory, vestibular)

*Three sensory systems that break the clean receptor → thalamus → dedicated-primary-cortex
template of vision, audition, and somatosensation. **Olfaction** is the exception to the
thalamic rule: the olfactory bulb projects directly to a three-layered allocortex (piriform
and its neighbours), bypassing the thalamus entirely — the only sense to do so. **Taste** does
relay through the thalamus (the ventral posteromedial parvocellular nucleus) but arrives in the insula / frontal operculum rather than a
neocortical strip, and in primates it skips the pontine parabrachial relay that rodents use.
**Vestibular** sensation has no dedicated unimodal primary cortex at all — its cortical
representation is distributed and inherently multisensory (a parieto-insular core plus areas
already in this map, the medial superior temporal and ventral intraparietal areas) — and it is
**two senses on two transducers, not one**: the
semicircular canals transduce rotation, the otolith organs transduce linear acceleration with
gravity inseparably summed into it, and **attitude is transduced by neither** — it is computed
centrally from the two lines together with vision. Taste and vestibular both land in the insula;
the insula's broader interoceptive / salience role is left for its own section.*

## Olfactory epithelium — the chemical transducer (olfactory cleft, sensory front end)

- **Function:** turns airborne molecules into a neural signal. A patch of pseudostratified
  neuroepithelium in the **olfactory cleft**, the roof of each nasal cavity, covered by mucus into
  which the receptor cells project cilia. Odorants dissolve in the mucus and bind receptor proteins
  on those cilia. **Unlike every other sensory front end in this file, the transducer is itself a
  neuron whose own axon enters the brain** — there is no separate primary afferent, no ganglion, and
  no relay before the first central synapse.
- **Three things make this entry unlike the retina and cochlea entries, and all three matter
  downstream:**
  1. **The receptor cells are neurons and they project directly into the central nervous system.**
     Their unmyelinated axons bundle into the **fila olfactoria**, pass through the perforations of
     the **cribriform plate**, and terminate in the olfactory bulb. This is the **shortest path from
     the outside world to the brain anywhere in the body** — and the reason the olfactory route
     is the one by which material can reach the central nervous system without crossing the
     blood–brain barrier.
  2. **They regenerate throughout life**, from basal stem cells in the epithelium, replacing neurons
     that die and re-growing their axons to the correct target. Essentially nothing else in the
     mature nervous system does this. **A front end that continuously rebuilds itself is an
     architectural fact, not a maintenance detail**: whatever holds the map stable cannot be the
     individual cells, because they are replaced.
  3. **The signal is not spatial.** There is no receptor sheet mapping the world. What a single
     neuron reports is the occupancy of **one receptor type**, and position in the epithelium carries
     no information about where the odorant came from.
  *(Class 1 — cell biology and regeneration: DeMaria & Ngai 2010. Candidates — awaiting Micky's
  verification.)*
- **The one-neuron-one-receptor rule is the entry's central structural fact.** Each olfactory
  sensory neuron expresses **exactly one** olfactory receptor gene out of the whole family, chosen
  stochastically during differentiation and then held for the life of the cell. Every neuron
  expressing a given receptor — scattered across a broad zone of the epithelium rather than
  clustered — sends its axon to **the same one or two glomeruli** in the bulb. The receptor protein
  itself participates in steering the axon there. **So the sorting that produces the bulb's
  chemotopic map is done by the receptor molecule, not by a topographic projection**, which is why
  adjacency in the bulb means chemical similarity and not adjacency in the world.
  *(Class 1 — Serizawa et al. 2003; Mombaerts 2004; Mori & Sakano 2011, as reviewed in DeMaria &
  Ngai 2010. Gene-swap evidence for receptor-directed targeting: Mombaerts et al. 1996, mouse.
  **Species: mouse for the targeting experiments.** Candidates.)*
- **Contested — how many receptor types a human actually has.** The olfactory receptor family is the
  largest gene family known, with roughly 1,000–1,400 genes in mouse. Human counts disagree
  substantially: one widely cited textbook account puts the human family at **500–750 genes with
  about 75% non-functional, so 100–200 working receptors**; the figure carried at the olfactory bulb
  entry is **350–400 intact types**. Both cannot be right, and the difference is not small — it is
  the difference between a two-fold and a four-fold pseudogene fraction. **Recorded as contested; no
  side taken.** *(Class 1 — the 500–750 / 100–200 figures: Purves, Neuroscience. The 350–400 figure
  is inherited from the olfactory bulb entry in this file and is not independently sourced.
  Candidate.)*
- **Inputs:**
  - **← airborne odorant molecules, dissolved in the olfactory mucus** — **carries:** chemical
    identity and concentration. **This is a chemical input, not a neural edge** — the same case as
    light at the retina, vibration at the cochlea, and blood-borne signals at the solitary nucleus.
    **Fan-in:** not applicable.
  - **← centrifugal modulation of the epithelium** — **payload unknown — owed**; whether the brain
    modulates its own chemical front end the way it modulates the cochlea through the olivocochlear
    efferents is not established. **Fan-in:** unknown.
- **Outputs:**
  - **→ Olfactory bulb**, via the **fila olfactoria / olfactory nerve (cranial nerve I)**, onto the
    **glomeruli** — **carries:** one component of a **combinatorial chemical code** — a single
    neuron reports how strongly its one receptor type is being occupied, and the odour's identity
    exists only in the pattern across types. Not a scalar, not a map of space, and **not
    frequency-analysed the way the cochlear output is** — there is no ordering of the chemical
    dimension corresponding to the tonotopic axis. **Fan-out:** each neuron's axon terminates in
    **one or two glomeruli**; the convergence at the receiving end is declared at the bulb as
    ~800 : 1. **Fan-in at this end: not applicable** — the neuron has no neural input to converge.
- **Internal structure and internal data flow:** three principal cell classes —
  **olfactory sensory neurons** (bipolar; a dendrite to the mucus surface bearing the receptor
  cilia, an unmyelinated axon to the bulb); **sustentacular (supporting) cells**, which maintain the
  mucus and the ionic environment; and **basal cells**, the **stem population** from which new
  sensory neurons are generated throughout life. Bowman's glands secrete the mucus.
  - **Internal edge — basal cells → olfactory sensory neurons: carries:** no signal. This is a
    **developmental transfer, not a data-flow edge** — cell replacement, recorded here because the
    slot would otherwise imply the population is fixed. **Fan-in / fan-out:** not applicable.
  - **Internal edge — sensory-neuron cilia → sensory-neuron soma: carries:** the transduction
    current, by propagation within one cell. **No edge is written for this** under the convention in
    the design file's §3: there is no second synapse. Recorded as **not applicable**.
  - **Transduction cascade, within the receptor cell:** odorant binds the receptor, a G-protein
    cascade raises cyclic AMP, a cyclic-nucleotide-gated channel opens, and a calcium-activated
    chloride current amplifies the result. **This is amplification inside a cell, not an internal
    edge**, and it is the chemical counterpart of the cochlear amplifier — but where the cochlea's
    amplifier is mechanical and shared across cells, this one is biochemical and private to each.
    *(Class 1 — DeMaria & Ngai 2010. Class 2 — the parallel to the cochlear amplifier is Claude's.
    Candidate.)*
- **Neurons:** ~40 million per side — **inherited from the olfactory bulb entry in this file and not
  independently sourced**, and human estimates in the literature vary widely. Flagged
  for verification rather than asserted.
- **Synapses:** unknown. **Axons:** one unmyelinated axon per sensory neuron, bundled as the fila
  olfactoria. **Grey-matter volume:** not applicable — this is not central tissue.
  **White-matter volume:** not applicable. **Myelination:** none — the olfactory nerve is
  unmyelinated, which is part of why olfactory conduction is slow.

## Olfactory bulb (layered forebrain outgrowth)

- **Function:** the first olfactory processing stage. Olfactory sensory neuron axons expressing
  one receptor type converge onto glomeruli (a 2-D chemotopic "odour map"); mitral and tufted
  cells (the principal / projection neurons) read the glomerular pattern and, shaped by granule-
  and periglomerular-cell inhibition (dendrodendritic, reciprocal), send it on. A site of
  lifelong adult neurogenesis (new interneurons integrated continually).
- **Inputs:**
  - **← Olfactory epithelium**, its olfactory sensory neurons (~40 million/side, ~350–400 intact
    receptor types — **the receptor-type count is contested**; see that entry, via cranial nerve I)
    — **carries:** a **combinatorial chemical code** — one receptor type
    per neuron, all neurons of a type converging on one glomerulus, so the payload is a *pattern
    across ~5,500 glomeruli*, not a scalar and not a map of space. There is no topography of the
    world here: the "map" is chemotopic, and adjacency means chemical similarity, not adjacency in
    the world. **Fan-in:** ~800 : 1 receptor-to-mitral convergence.
  - **← piriform** (cortical feedback) and **← basal forebrain / raphe / locus coeruleus**
    (centrifugal neuromodulation) — **carries:** gain and state; no chemical content. **Payload
    otherwise unknown — owed.** **Fan-in:** unknown.
- **Outputs:**
  - **→ piriform and the rest of primary olfactory cortex** (lateral olfactory tract; also anterior
    olfactory nucleus, olfactory tubercle, cortical amygdala, rostral entorhinal) — **carries:** the
    **decorrelated glomerular pattern** — the odour identity as a sparse pattern over mitral/tufted
    cells, sharpened by granule- and periglomerular-cell inhibition. Chiefly ipsilateral, and — the
    structural oddity of this sense — **it goes straight to cortex with no thalamic relay and
    therefore no thalamic gate.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full paper
  was opened — abstracts and excerpts only. Rodent for the circuit; **human for the neurogenesis
  finding, which is the important one.** Nothing here is yet verified for the source.)*

  **Laminar sub-elements: six, and they are not cortical layers.** From the surface inward:
  **olfactory nerve layer**, **glomerular layer**, **external plexiform layer**, **mitral cell
  layer**, **internal plexiform layer**, **granule cell layer**. As with the superior colliculus's
  seven, these share the word "layer" with the neocortical scheme and nothing else; the bulb is a
  three-layered-allocortex-adjacent structure, not isocortex.

  **What the bulb computes, named as operations rather than as a transform.** The glomerular input
  is described in the literature as a simple genetically-organised map, **radically transformed** by
  interneuron interaction with the output cells. The named operations are **gain control**,
  **contrast enhancement**, **spatial decorrelation**, and **temporal synchronisation**. **Note
  what is not in that list: no change of reference frame, no binding, no categorisation.** The
  payload leaves in the same format it arrived — a pattern over glomerular channels — cleaned up.
  **This is the clearest case in the file of a stage whose payload change is a normalisation
  rather than a re-expression**, and it is the same class of operation the auditory callosal edge
  turned out to perform. *(Class 1 — Kay & Stopfer 2006; Cleland 2010; Lepousez et al., as reviewed
  in PMC4968158.)*

  **Internal edges:**
  - **olfactory sensory neuron axons → glomerulus** — **carries:** the combinatorial chemical code,
    one receptor type per glomerulus. **Fan-in:** ~800 : 1 onto mitral cells overall.
  - **mitral / tufted lateral dendrites ↔ granule cell spines** (dendrodendritic, **reciprocal**) —
    **carries:** lateral inhibition, and the reciprocity is the structural oddity: **one synaptic
    apposition carrying signal in both directions**, rather than two edges. **This file has no other
    instance of a bidirectional single synapse**, and a rung below that assumes edges are directed
    would have to special-case it. **Fan-in / fan-out:** unknown.
  - **periglomerular cells → within the glomerulus** — **carries:** intraglomerular inhibition;
    gain control at the input stage. **Fan-in / fan-out:** unknown.
  - **short-axon cells → between glomeruli** — **carries:** interglomerular inhibition — the
    substrate of contrast enhancement across the chemical space. **Note that "lateral" here means
    lateral in *chemical similarity*, not in space**, because the glomerular adjacency is
    chemotopic. **A lateral-inhibition mechanism operating over a non-spatial neighbourhood is
    worth carrying explicitly**, since every other instance of lateral inhibition in this file
    operates over a map of the world. **Fan-in / fan-out:** unknown.

  **Cell-class sub-elements: mitral and tufted cells are grouped as one in this entry and there is
  evidence they are two.** Adult-born and neonatally-born granule cells settle at different depths
  of the granule layer and **preferentially contact mitral and tufted cells respectively** — so the
  two output classes have differently-sourced inhibitory partners. Whether they carry different
  payloads to different targets is **not established here** and is **owed**; the
  possibility that this is a parallel-labelled-line arrangement like the cochlear nucleus's is
  open. *(Class 1 for the differential contact — Front Neural Circuits 18:1467203, 2024, rodent.)*

  **Adult neurogenesis: the rodent finding does not transfer to human, and this is the most
  project-relevant divergence the file has recorded.** In rodents the bulb is one of two lifelong
  neurogenic regions: progenitors migrate in from the subventricular zone along the rostral
  migratory stream and differentiate in place, **~95% becoming inhibitory granule cells**, and the
  circuit's cellular composition is therefore under constant turnover.
  **In humans it appears not to happen.** Carbon-14 dating of human olfactory bulb neurons found
  adult neurogenesis with long-term survival to be **extremely limited**; neuroblast migration to
  the bulb is reported only in infants up to about **18 months** and absent in the adult brain.
  Human neuroblasts appear instead to migrate toward the **striatum** — a different destination,
  not merely a reduced one. Hippocampal neurogenesis, by contrast, is more conserved across
  mammals.
  **Caveats, and they are real.** The finding remains described in the literature as a matter of
  debate; the carbon-dating cohort was forensic-autopsy material weighted toward neuropsychiatric
  disease and substance abuse, and a commentary on the paper notes explicitly that it cannot rule
  out ongoing bulbar neurogenesis in people whose olfactory demands are high. **A negative in that
  sample is not a negative in the species.**
  **Why it matters beyond this entry.** The rodent bulb is the canonical example of a circuit that
  maintains **stable representations while its own components are continuously replaced** — the
  stability-plasticity problem solved by adding cells. If the human bulb does not do this, then the
  most-cited mammalian instance of continuous structural learning is **not a human mechanism**, and
  whatever humans do instead in this modality is achieved without cell addition. **Recorded here
  because it bears on the project's premise, not only on this entry.**
  **One qualification on what the rodent version buys, since it is usually over-stated.** Reducing
  bulbar granule cells impairs odour **discrimination** but leaves detection thresholds and
  short-term olfactory memory intact; and olfactory training was found to increase, decrease, or
  have no effect on the survival of newly generated neurons depending on timing. **The link from
  neurogenesis to learning is real but neither simple nor monotonic.** *(Class 1 — Bergmann et al.
  2012, human carbon-14; Sanai et al. 2011; Ernst et al. 2014; Gheusi et al. 2000; Mouret et al.
  2008; Neuron commentary 2012. Not yet verified for the source.)*
- **Neurons:** glomeruli **~5,568 ± 830 per bulb** (range ~3,000–9,300; Maresh et al. 2008,
  human) — a ~16 : 1 glomerulus-to-receptor-type convergence (5,568 / ~350), far higher than
  the rodent ~2 : 1; mitral cells **~50,000** per bulb (Bhatnagar et al. 1987, human; ~50,900 at age 25); interneurons (granule,
  periglomerular) vastly outnumber the projection neurons, so the bulb's total is
  interneuron-dominated (soft). Receptor-to-mitral convergence ≈ 800 : 1.
- **Synapses:** dendrodendritic reciprocal mitral↔granule synapses (the bulb's characteristic
  motif); absolute count unknown.
- **Axons:** olfactory nerve (receptor axons in) ~40M/side; lateral olfactory tract (mitral /
  tufted axons out), count unknown.
- **Grey-matter volume:** **~50 mm³ per bulb** in young adults, declining ~0.19 mm³/yr with age
  (~37 mm³ by age 95; Bhatnagar et al. 1987, human). No reliable left–right difference.
- **White-matter volume:** unknown. **Myelination:** lateral olfactory tract myelinated;
  g-ratio unknown.

## Piriform + primary olfactory cortex (three-layered allocortex)

- **Function:** the largest primary olfactory area — forms and stores odour-object
  representations by associative (content-addressable) recurrent processing on a pyramidal-cell
  network, much like a cortical autoassociator; supports odour identification, pattern
  completion, and rapid olfactory learning. Anterior piriform is weighted to odour identity,
  posterior to category / association.
- **Inputs:**
  - **← olfactory bulb** (lateral olfactory tract, monosynaptic, outer layer) — **carries:** the
    sparse glomerular odour pattern. **Fan-in:** unknown.
  - **← its own recurrent (associational) fibres** — **carries:** the network's own current state —
    the autoassociator's feedback, which is what completes a partial pattern. **Fan-in:** unknown.
  - **← orbitofrontal and entorhinal cortex, amygdala, neuromodulatory nuclei** (feedback) —
    **carries:** context, value, and state. **Payload otherwise unknown — owed.** **Fan-in:**
    unknown.
- **Outputs:**
  - **→ orbitofrontal cortex** (directly, and via the mediodorsal thalamus) — **carries:** the
    **odour object** — a completed, content-addressed identity rather than a receptor pattern. As at
    the inferotemporal cortex, the payload has become a category: "which smell," not "how much of what chemical."
    **Fan-out:** unknown.
  - **→ amygdala** — **carries:** the odour object, for hedonic / emotional evaluation.
    **Fan-out:** unknown.
  - **→ entorhinal cortex → hippocampal formation** — **carries:** the odour object, as an element
    of an episode. **Fan-out:** unknown.
  - **→ hypothalamus**; **→ olfactory bulb** (reciprocal feedback) — **payload unknown — owed.**
    **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search; abstracts and
  excerpts only. Nothing here is yet verified for the source.)*

  **Laminar sub-elements: three layers, two of which subdivide — and this is *piriform's own*
  laminar scheme, not the neocortical one.** Stated explicitly because the word "layer" in this
  entry means something different from what it means in the isocortical entries, and the sublayer
  names **Ia, Ib, IIa, IIb** are standard in the olfactory-cortex literature and used nowhere else
  in this file.
  - **Layer I** — superficial plexiform; many axons and dendrites, few somata. **Layer Ia**, the
    outer part, receives the **afferent** fibres from olfactory-bulb mitral and tufted cells via
    the lateral olfactory tract. **Layer Ib**, the inner part, receives **associational** fibres
    from piriform's own principal cells and from other olfactory cortical areas.
  - **Layer II** — compact, densely packed with the principal cells. **Layer IIa** holds
    **semilunar** cells; **layer IIb** holds **superficial pyramidal** cells.
  - **Layer III** — lower somatic density; **deep pyramidal** and multipolar cells, and a high
    density of associational fibres like layer Ib.

  **The afferent/associational segregation is strict, and it produces a gradient across cell
  classes.** Afferent input goes to layer Ia; associational input to layers Ib through III. The
  principal cells sit at different points along that divide: **semilunar cells** carry large spines
  in Ia **but not in Ib** and are afferent-dominated, receiving stronger single-fibre bulbar input;
  **superficial pyramidal cells** receive weaker afferent and stronger associational drive; **deep
  pyramidal cells** are mostly driven by the recurrent circuit and receive the strongest recurrent
  inhibition. **So "sensory-driven" and "self-driven" are not two states of this network but two
  populations in it**, ordered by depth — described in the source literature as two layers of
  synaptic processing, afferent and associational, within one cortex. **Semilunar cells also do not
  send feedback to the olfactory bulb** while the pyramidal cells do, so the afferent-dominated
  class is the one that does not talk back. *(Class 1 — Suzuki & Bekkers 2011, mouse;
  Neville & Haberly 2004; Haberly & Feig 1983; Price 1973.)*

  **The same-dendrite, different-depth geometry, and it is now the fourth instance.** Sensory input
  and network feedback arrive on one apical dendrite at different depths — as at the cortical
  layer-1 tuft, the dorsal cochlear nucleus's fusiform cell, and the medial superior olive's
  bipolar cell. **At four instances across four unrelated structures this looks like a design
  pattern rather than a coincidence**, and the pattern is specific: *the two streams are separated
  by distance along a dendrite rather than by different cells.*

  **Inhibition is split the same way.** **Feedforward** inhibition comes from **layer I horizontal
  and neurogliaform** interneurons, which take direct lateral-olfactory-tract input and synapse on
  the **apical dendrites** — scoped to the afferent stream. **Feedback** inhibition comes from
  **layer II/III bitufted regular-spiking** interneurons, which receive little direct tract input
  and synapse on **somata and basal dendrites** — scoped to the associational stream. **One
  structure, two inhibitory systems, each guarding its own input class.** *(Class 1 — Stokes &
  Isaacson 2010; Suzuki & Bekkers 2010; Large et al. 2016; rodent.)*

  **One challenge to the classical laminar account, recorded not smoothed.** A Golgi study reports
  that afferent fibres **penetrate beyond layer I into layer II**, contrary to the general notion
  that olfactory afferents resolve within layer I. If right, the segregation above is strict only
  to first order. *(Class 1 — Vargas-Barroso et al. 2013, albino rat. Single study; not
  corroborated.)*

  **It is two synapses from the outside world.** Receptor → bulb → here. **No thalamic relay, and
  therefore no thalamic gate**, which the bulb's entry already notes; stated again here because it
  is *this* structure that is unusually exposed. Every other primary sensory cortex in this file
  sits behind a relay that can be closed.

  **Internal edges:**
  - **bulbar afferents → layer 1a** — **carries:** the sparse decorrelated glomerular pattern.
    **The projection is famously non-topographic**: a given glomerulus's output is distributed
    broadly across the piriform sheet rather than to a matched location, so **the chemotopy present
    in the bulb is discarded at this synapse**. That discarding is a payload change this entry does
    not currently state, and it is the one that makes the autoassociator possible — a
    content-addressable network cannot use an input map. **There is accordingly no spatial mapping
    of odour-evoked activity anywhere in this structure**, and the association fibres are
    non-topographic too, so nothing here restores it. **One possible exception worth carrying:**
    there may be a spatial organisation based on **efferent target** rather than on input — the
    tissue ordered by where its cells project rather than by what they receive, which is a kind of
    map this file has no other instance of. **Owed.** **Fan-in:** unknown. *(Class 1 — the Haberly
    lineage as compiled in the ScienceDirect piriform overview; Nat Commun 7:12238, 2016, for
    layer-specific gene expression defining distinct projection targets.)*
  - **layer 2/3 pyramidal cells → layer 1b, back onto layer 2/3** (recurrent associational) —
    **carries:** the network's own state; the feedback that completes a partial pattern. **This is
    the file's only declared *intra*-regional recurrent edge that is load-bearing for the entry's
    stated function** rather than noted in passing. **Fan-in / fan-out:** unknown.

  **The trigeminal chemosensory system reaches this structure, and the file does not name it as a
  chemical pathway anywhere.** Nasal irritants — ammonia, carbon dioxide, ethanol, acetic acid,
  capsaicin, menthol, air pollutants — are transduced by **nociceptive free endings of the
  trigeminal nerve**, not by olfactory receptors. Their route is the **spinal trigeminal nucleus →
  ventral posterior medial thalamus → somatosensory and pain cortex**, and the file already carries
  that pathway *as somatosensation*, without recording that a chemical stimulus class rides it.
  Two edges connect it to olfaction proper: **trigeminal collaterals project directly to the
  olfactory epithelium and the olfactory bulb**, and the odourless trigeminal stimulant carbon
  dioxide **evokes responses in piriform cortex**. Trigeminal ganglion cells are also **unique
  among primary sensory neurons in having two axonal branches entering the central nervous system
  at widely separated points**. *(Class 1 — Purves, Neuroscience, ch. 15; Brand 2006; J Neurosci
  34:341, 2014; Wesson 2013. Not yet verified for the source.)*

  **Trigeminal chemesthesis is not a faster danger channel sitting behind olfaction, and the
  thresholds are what settle it.** The natural reading is that the irritant line is the quick alarm
  and olfaction the slower identification channel. **The thresholds run the other way.** Trigeminal detection thresholds are
  **much higher** than olfactory ones — when irritants are presented to people who have lost their
  sense of smell, perceptual thresholds are about **100 times higher** than in normal subjects who
  perceive the same compounds as odours. **So there is no more-sensitive chemical alarm sitting
  behind olfaction; the irritant channel fires later, at higher dose, not earlier.**
  What trigeminal activation does supply is a set of **damage-limitation reflexes** — increased
  salivation, tearing, nasal secretion, vasodilation, sweating, **decreased respiratory rate**, and
  bronchoconstriction. **That is a different job from warning**: it reduces further intake once
  intake has already occurred. **Recorded because it sharpens what the chemical senses are for.**
  Detection in these modalities never precedes exposure — the molecule must already be inside — and
  the second chemical channel does not fix that, it only limits the dose afterwards.
  **They are also not two clean streams.** Most odorants stimulate trigeminal fibres and most
  irritants have an odour; human nasal chemical sensation is described as **one integrated
  multimodal afferent signal** rather than two. And the coupling runs both ways: patients with
  olfactory loss show **raised** trigeminal thresholds, though at least one study reports anosmic
  and normosmic irritation sensitivity as comparable. **Contested; recorded, not resolved.**
  *(Class 1 — Purves, Neuroscience, ch. 15, for the 100× figure; Cometto-Muñiz & Simons 2015;
  Neurosci Biobehav Rev 30:908, 2006; Neurosci Lett 2009 for the raised thresholds; PubMed 9580447
  for the contrary result. Not yet verified for the source.)*
- **Neurons:** soft/unknown — no clean human per-area count; three-layered allocortex (like the
  hippocampal formation), fewer-layered than neocortex.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.
- *The other primary-olfactory members are described elsewhere in this map — the cortical /
  medial amygdala (Amygdala) and the rostral entorhinal cortex (Hippocampal formation); the
  anterior olfactory nucleus and olfactory tubercle are small and given no separate slot. The
  secondary olfactory cortex is the orbitofrontal cortex (Frontal lobe).*

## Gustatory pathway — nucleus of the solitary tract → ventral posteromedial parvocellular thalamic nucleus → insular taste cortex

- **Function:** taste. Taste-bud receptor cells (sweet, salt, sour, bitter, umami) are read out
  through three cranial nerves; the central pathway carries taste quality and intensity plus
  oral somatosensation (temperature, texture, viscosity, fat, capsaicin) to the insula, where
  the **primary gustatory cortex** (anterior insula + frontal operculum) represents them
  independently of hunger — sensory, not yet reward. The **orbitofrontal cortex** is the
  secondary taste cortex, where taste combines by learning with smell and vision into *flavour*
  and takes on reward value and hunger-dependent, sensory-specific satiety.
- **Inputs:**
  - **← taste buds** via cranial nerves VII (chorda tympani), IX (glossopharyngeal) and X (vagus) → rostral
    **nucleus of the solitary tract** — **carries:** taste **quality** (sweet, salt, sour, bitter,
    umami) and **intensity**, plus oral somatosensation (temperature, texture, viscosity, fat,
    capsaicin). A five-ish-dimensional quality vector with an intensity scalar — no spatial map of
    the world, only a crude map of the tongue. **Fan-in:** unknown.
  - **← the ventral posteromedial parvocellular thalamic nucleus** → the anterior insula and frontal operculum — **carries:** the same quality-and-intensity vector, relayed;
    chiefly ipsilateral. In primates this line **skips** the pontine parabrachial relay rodents use.
    **Fan-in:** unknown.
- **Outputs:**
  - **→ orbitofrontal cortex**, from the primary gustatory cortex — **carries:** taste
    quality and intensity, **independent of hunger** — sensory, not yet reward. **The payload
    changes at the next stage, not this one**, and that is the load-bearing fact: the orbitofrontal
    cortex binds this with smell and vision into **flavour**, and *there* it acquires reward value
    and hunger-dependent, sensory-specific satiety. The primary cortex declares what is in the
    mouth; the secondary declares what it is worth. **Fan-out:** unknown.
  - **→ amygdala** and **→ hypothalamus** (feeding) — **carries:** taste quality with hedonic
    valence attached downstream; reciprocal. **Payload otherwise unknown — owed.** **Fan-out:**
    unknown.
- **Internal structure and internal data flow:** *(From web search; abstracts and
  excerpts only. Rodent for the imaging, human for the functional imaging where noted. Nothing here
  is yet verified for the source.)*

  **The five-quality alphabet is real at the receptor and does not survive the ascent, and the
  entry's "five-ish-dimensional quality vector" therefore describes only the first synapse.** Taste
  receptor proteins are expressed in **non-overlapping sets of cells** within taste buds, which is
  what makes a discrete alphabet available at all and is the main evidence for **labelled-line**
  coding. But taste buds contain **both narrowly and broadly tuned cells**, and the literature's
  own summary of the whole axis is that **as gustatory signals proceed to the hindbrain and higher,
  coding becomes more distributed and temporal patterns of activity become important**. **So the
  quality vector is progressively re-encoded into an ensemble pattern as it ascends, and the file
  should not carry the same payload description at every stage of this pathway.**
  *(Class 1 — Chandrashekar et al. 2006 for the labelled-line case; Tomchik et al. 2007 for the
  across-fibre case; review, PubMed 30788507, 2019.)*

  **Three coding models are live, not two.**
  - **Labelled line** — neurons and pathways dedicated to single qualities. Supported by the
    non-overlapping receptor expression.
  - **Across-fibre / combinatorial / ensemble** — quality carried by simultaneous activity across
    fibres, with minimal information in any single neuron. Supported by recordings from multiple
    laboratories in multiple species.
  - **Temporal** — quality embedded in the **cadence** of impulses rather than in which cells fire
    or how fast. **This file has no other payload of that form anywhere**, and it is the one a lower
    rung would find hardest to implement, since it makes spike timing the message rather than its
    carrier. Recorded because its absence elsewhere may be a gap in the file rather than in nature.

  **The gustotopic map: claimed, then contradicted, and this is the sixth map claim this file has
  had to qualify.** Two-photon calcium imaging in anaesthetised mouse reported quality-specific
  **"hot spots"** of narrowly tuned neurons in insular cortex — sweet rostral, bitter caudal — with
  the virtual absence of broadly tuned cells. **A later study using a more sensitive calcium
  indicator, under the same anaesthesia, found the opposite**: neurons broadly tuned, no specific
  spatial organisation. The discrepancy is attributed to indicator sensitivity, since the more
  sensitive reporter detects weaker responses to multiple tastes in the same cell — **the earlier
  study's narrow tuning may have been a detection threshold rather than a property of the tissue.**
  Imaging in **alert** mice subsequently found taste-responsive cells that could be narrowly *or*
  broadly tuned and were **sparsely scattered** across the surface. Prior electrophysiology from
  several laboratories and species already supported ensemble coding.
  **In human the answer is the same.** High-resolution functional imaging with multivariate
  analysis finds distinct taste qualities represented by **distributed spatial patterns** rather
  than by distinct topographic areas — one review is titled to the effect that there is no
  gustotopic representation in the human brain.
  **Recorded verdict: no map; a spatial population code.** *(Class 1 — Chen et al. 2011,
  anaesthetised mouse; Fletcher et al. 2017, mouse; Chen et al. 2020, alert mice; Avery et al. 2020;
  Chikazoe et al. 2019; J Neurosci 40:1042, 2020, human. Not yet verified for the source.)*

  **The convergence with olfaction is the finding worth carrying.** The human imaging work draws the
  comparison itself: taste quality is encoded in insular cortex **like odour in piriform cortex** —
  dispersed ensembles, no topography. **Both chemical senses arrive at cortex as distributed
  population patterns over a non-spatial quality space, and neither builds a map at any stage.**
  **Against the pattern this file found in vision and hearing, where map claims were repeatedly
  over-stated but the underlying topography is real, the chemical senses are the case where there
  was never a map to over-state.** That makes them the control condition, and they behave like one.

  **A caution specific to this cortex.** The insula is **inherently multisensory** — it carries
  somatosensory and thermal responses alongside taste — which makes isolating taste-evoked activity
  from oral somatosensation difficult, and is a live confound in every study above. The entry's own
  Inputs field already declares oral somatosensation arriving on the same edges as taste.

  **Sub-elements: owed throughout.** No laminar or divisional partition of the nucleus of the
  solitary tract, the ventral posteromedial parvocellular thalamic nucleus, or the anterior insula
  and frontal operculum is established here. **The rostral/caudal gradient of the disputed
  hot spots is the only tangential organisation anyone has proposed, and it did not replicate.**
- **Neurons:** soft/unknown throughout (the nucleus of the solitary tract, the ventral posteromedial parvocellular thalamic nucleus, the anterior insula and frontal operculum); no clean human counts.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Semicircular canals — the rotation transducer (membranous labyrinth, sensory front end)

- **Function:** transduction of head **rotation**, and nothing else. Three fluid-filled canals per
  ear (horizontal, anterior, posterior), set close to mutually orthogonal, each ending in a
  swelling (the ampulla) whose sensory epithelium (the **crista**) carries hair cells with their
  bundles embedded in a gelatinous **cupula** that spans the duct. When the head rotates, the
  endolymph lags by inertia and deflects the cupula, which shears the hair bundles. The canals of
  the two ears work as **coplanar pairs** in push-pull (a rotation that excites one member inhibits
  its partner) (Blanks, Curthoys & Markham 1975).
- **What the line carries, and it is not what the mechanics are driven by.** The canal is
  mechanically a heavily damped **torsion pendulum** (Steinhausen 1933; van Egmond, Groen &
  Jongkees 1949): the viscous drag of the endolymph dominates its inertia, so across the band of
  natural head movement the mechanics **integrate** the angular acceleration that drives them, and
  the cupula's deflection — hence the afferent's firing — is proportional to head angular
  **velocity** (Goldberg & Fernández 1971). The afferent is therefore a **rotation-rate** line, not
  an angular-acceleration line. The line is also **high-passed**: a rotation held at constant
  velocity decays away over seconds as the cupula returns to rest, so a **steady rotation is not
  held** — there is no direct-current term. (The central stage partially restores it; see velocity storage in
  the vestibular-nuclei entry.)
- **Does not carry:** linear acceleration, gravity, tilt, or attitude. A canal is blind to all four.
- **Inputs:**
  - **← head angular motion** (the world) — **carries:** mechanical rotation of the head, onto the
    hair cells of the three cristae; not a neural edge. **Fan-in:** not applicable.
- **Outputs:**
  - **→ vestibular nuclei** (chiefly superior and medial), via the **superior division** of the
    vestibular (Scarpa's) ganglion and cranial nerve VIII — **carries:** head angular **velocity**, three-axis,
    head-fixed frame, band-limited (**no direct-current**), one triplet per ear. **Does not carry:** linear
    acceleration, gravity, tilt, or attitude. **Fan-out:** unknown.
  - **→ cerebellum** (flocculonodular lobe), on a branch that bypasses the nuclei — **carries:** the
    same rotation-rate signal, unrelayed. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search; abstracts and
  excerpts only. Nothing here is yet verified for the source.)*

  **This is the one payload in the file that can be stated exactly, and the reason is the receptor
  geometry.** Every hair cell in a given crista is **aligned along that canal's axis**, and all of
  them are oriented with their kinocilia in the **same direction** — so an entire crista has one
  directional sensitivity. The organ is therefore not a map and not a population code but **one
  scalar per canal**, and the three canals' anatomical orientations **are** the three basis vectors.
  **The payload is an angular-velocity 3-vector expressed in a basis fixed to the skull.**
  Every other entry in this file has had to say "a pattern over" or "a vector whose dimensions are
  owed." Here the dimensions are the three canal planes, and they are physical objects.
  *(Class 1 — standard vestibular anatomy; the alignment statement from the aerospace-medicine compilation,
  citing the primary literature.)*

  **But "set close to mutually orthogonal" is a heuristic the measurements do not support, and the
  correction has teeth.** High-resolution X-ray computed tomography of **39 mammal species** found
  that **substantial deviations from orthogonality, angle symmetry, and coplanarity are the rule**,
  not the exception. Worse for the idealisation: the degree to which a species' canals deviate from
  orthogonality is **negatively correlated with estimated vestibular sensitivity** — so the
  departures are functional, not noise. The authors conclude that orthogonality, symmetry and
  coplanarity are **misleading descriptors** whose over-emphasis obscures a large amount of
  functionally relevant variation.
  **What this changes for the file:** the basis is real, and it is **oblique and species-specific**.
  A consumer of this edge cannot assume an orthonormal triad and read components off directly; it
  needs the actual inter-canal angles, and those are a per-species — possibly per-individual —
  parameter this file does not carry. **Owed: the human angles.** **One more instance of a clean
  geometric idealisation asserted where the measurement says otherwise — a recurring shape in this
  section.** *(Class 1 — PMC3834179, 39 mammal species. Not yet verified for the source.)*

  **The payload is velocity, not acceleration, and the integration is mechanical rather than
  neural.** The canal is stimulated by angular **acceleration**, but the elasticity of the cupula
  working against the viscosity of the endolymph makes the cupular deflection — and therefore the
  afferent firing rate — proportional to head **velocity** over the physiological band. Peak firing
  occurs at peak angular velocity, not peak acceleration. **So a payload change happens before the
  first synapse, performed by fluid mechanics**, and the file has no other instance of a transform
  executed outside the nervous system. The mechanical integration is imperfect: the velocity signal
  **decays with a time constant of 3–5 seconds**, which is why the next stage has to repair it (see
  the vestibular nuclei entry). Afferents discriminate head-velocity differences of about
  **2 deg/s** and remain sensitive up to hundreds of deg/s. *(Class 1 — Purves, Neuroscience, ch.
  14; PMC5561016; PMC6520623.)*
- **Neurons:** soft / unknown — hair-cell and ganglion-cell counts not recorded here (no clean human
  figure taken).
- **Synapses:** unknown. **Axons:** the canal division of the vestibular nerve; count unknown.
  **Grey-matter volume:** not applicable (peripheral sensory epithelium, not brain grey — as with the retina).
  **White-matter volume:** unknown. **Myelination:** the vestibular nerve is myelinated; g-ratio
  unknown.

## Otolith organs (utricle, saccule) — the linear-acceleration transducer (membranous labyrinth, sensory front end)

- **Function:** transduction of **linear acceleration**, gravity included and inseparable from it.
  Two maculae per ear, set close to orthogonal — the **utricle** roughly horizontal (sensing
  acceleration in the horizontal plane, and head tilt away from upright), the **saccule** roughly
  vertical (sensing vertical acceleration and tilt in the sagittal plane). The hair bundles are
  loaded by an **otoconial mass** — a layer of calcium-carbonate crystals in a gel — whose inertia
  shears them when the head accelerates, and whose weight shears them when the head tilts.
- **What the line carries, and why it is a sum rather than a measurement.** The macula transduces
  the **gravito-inertial force**: the vector sum of gravity and linear acceleration (Fernández &
  Goldberg 1976). By the equivalence of gravitational and inertial acceleration, the two terms
  produce the **same shear on the same hair cells**, so an otolith afferent **cannot distinguish a
  steady tilt from a steady linear acceleration** (Angelaki & Cullen 2008). The ambiguity is in the
  physics, not in the tissue, and no otolith organ anywhere resolves it. Unlike the canals, this
  line **does hold a direct-current term** — a maintained tilt produces a maintained signal.
- **Does not carry:** rotation rate, and — this is the load-bearing negative — **attitude**. Tilt
  and translation leave the ear summed into one vector and are separated only centrally
  (see the vestibular-nuclei entry). **There is no attitude receptor.**
- **Inputs:**
  - **← head linear acceleration and gravity** (the world) — **carries:** mechanical shear on the
    hair cells of the two maculae, via the otoconial mass; not a neural edge. **Fan-in:** not applicable.
- **Outputs:**
  - **→ vestibular nuclei** (chiefly lateral and inferior), via the **inferior division** of the
    vestibular (Scarpa's) ganglion (utricular fibers running partly with the superior division) and
    cranial nerve VIII — **carries:** the **gravito-inertial acceleration vector**, head-fixed frame, **with
    direct-current**. **Does not carry:** rotation rate; and — the load-bearing negative — **not tilt or
    attitude separately from translation.** The two leave the ear summed, and the sum is the signal.
    **Fan-out:** unknown.
  - **→ cerebellum** (flocculonodular lobe, nodulus / uvula), on the direct branch — **carries:**
    the same gravito-inertial vector, unrelayed. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search; abstracts and
  excerpts only. Nothing here is yet verified for the source.)*

  **The otolith payload is a different format from the canal payload, inside the same sense.** In a
  crista, every hair cell shares one directional sensitivity, which is what makes the canal signal a
  single basis component. In a **macula** the hair cells are aligned in a **multitude of
  directions**, with polarity reversing across the **striola**. **So the otolith organs do not
  supply basis vectors; they supply a distributed directional code across a population**, from
  which the acceleration direction must be decoded rather than read off.
  **One sense, two payload formats, and the file should not describe them alike.** The canals hand
  the brain a 3-vector in a fixed skull basis; the otoliths hand it a population pattern whose
  preferred directions tile the plane. *(Class 1 — the alignment contrast as compiled in the
  aerospace-medicine compilation of the primary literature; standard vestibular anatomy for the
  striola.)*

  **The ambiguity is not a limitation of the organ but a consequence of physics, and it is total.**
  Gravity and linear acceleration are indistinguishable to any accelerometer — the equivalence
  principle — so the otolith output is a **gravito-inertial** vector with no decomposition. The
  literature states the consequence plainly: **neither the semicircular canals nor the otolith
  organs are capable of providing unambiguous information about head motion and orientation.**
  **Both transducers are individually insufficient, and this is the file's clearest case of a
  payload that is only interpretable in combination with another edge.** Resolution requires
  convergence of canal and otolith signals centrally — declared at the vestibular nuclei's end.
  *(Class 1 — Angelaki 2004 lineage; ScienceDirect vestibular overview. Not yet verified for the
  source.)*
- **Neurons:** soft / unknown — hair-cell and ganglion-cell counts not recorded here.
- **Synapses:** unknown. **Axons:** the otolith division of the vestibular nerve; count unknown.
  **Grey-matter volume:** not applicable (peripheral sensory epithelium). **White-matter volume:** unknown.
  **Myelination:** the vestibular nerve is myelinated; g-ratio unknown.

## Vestibular nuclei and the central vestibular pathway — where attitude is computed (brainstem → thalamus → parieto-insular cortex)

- **Function:** the central stage that reads the **two** vestibular lines, drives the fast reflexes
  directly, and **computes what neither transducer can sense**. The four nuclei (superior, medial,
  lateral, inferior) sit at the pontomedullary junction. **Attitude — the direction of gravity
  relative to the head, the "subjective vertical" — is a computed quantity, not a sensed one.** The
  otolith line arrives carrying gravity and linear acceleration summed into one vector; the canal
  line arrives carrying rotation rate, which says how the head has *turned* relative to gravity. The
  central neurons combine the two — an internal model of the physical laws of motion rather than a
  measurement — and so separate the gravity term from the acceleration term (Angelaki, Shaikh, Green
  & Dickman 2004; Merfeld, Zupan & Peterka 1999). Vision (the optical line, via the cortical
  vestibular areas and the cerebellum) and proprioception are combined with them, which is why the
  estimate survives when one line is degraded and why it can be fooled when vision and the labyrinth
  disagree. The nuclei also perform **velocity storage** — a central integrator that lengthens the
  canal line's effective time constant well beyond the cupula's own (Raphan, Matsuo & Cohen 1979),
  partially restoring the low-frequency content the transducer's high-pass discards.
- **No dedicated primary cortex.** This is the one sense without one: the reflex loops are driven
  from the brainstem, and the cortical representation is distributed and inherently multisensory.
  Its core cortical region is the **parieto-insular vestibular cortex** — posterior insula /
  parietal operculum / retroinsular (human homologue debated) — for subjective vertical and
  self-motion; further vestibular cortex includes **area 2v**, **area 3a**, and the
  already-described **medial superior temporal** and **ventral intraparietal** areas.
- **Inputs:**
  - **← semicircular canals** (cranial nerve VIII) — **carries:** head angular velocity, three-axis,
    head-fixed, no direct-current. **Fan-in:** unknown.
  - **← otolith organs** (cranial nerve VIII) — **carries:** the gravito-inertial acceleration vector,
    head-fixed, with direct-current, tilt and translation unresolved. **Fan-in:** unknown.
  - **← cerebellum** (flocculonodular lobe, nodulus / uvula) — **carries:** the return arm of the
    computation — the internal model's correction. **Payload otherwise unknown — owed.** **Fan-in:**
    unknown.
  - **← vision and proprioception** (via the cortical vestibular areas and the cerebellum) —
    **carries:** optic flow and body configuration, as the second and third estimates of the same
    quantity. **Fan-in:** unknown.
- **Outputs:**
  - **→ oculomotor nuclei (III / IV / VI)**, via the medial longitudinal fasciculus — **carries:**
    the **vestibulo-ocular reflex** command — an eye-velocity signal equal and opposite to head
    rotation; driven chiefly by the canal line. **Fan-out:** unknown.
  - **→ spinal cord** (vestibulospinal tracts) — **carries:** an antigravity postural command;
    driven chiefly by the otolith line via the lateral nucleus. **Fan-out:** unknown.
  - **→ cerebellum** (flocculus / nodulus / vermis) — **carries:** both lines plus the current
    estimate. **Fan-out:** unknown.
  - **→ thalamus** (ventroposterior / ventral lateral / intralaminar) **→ parieto-insular
    vestibular cortex, area 2v, area 3a**, and on to the hippocampal formation — **carries:** the
    **computed** estimate — **head attitude and self-motion**, with gravity separated from linear
    acceleration. **This is not the transducer signal**, and that distinction is the whole reason
    the entry exists: what ascends is a result, not a measurement. **Fan-out:** unknown.

    **The medial superior temporal and ventral intraparietal areas are not direct thalamic targets
    on this line, and the route to them is contested.** There is reported to be **a lack of
    anatomical evidence for a thalamic vestibular projection to the medial superior temporal area**,
    and response dynamics and latency order the three areas **parieto-insular vestibular cortex →
    ventral intraparietal area → medial superior temporal area**, with the last showing the longest
    latencies. That ordering is what a **cortico-cortical** route predicts and not what a shared
    thalamic input predicts. Both entries take their vestibular input from the parieto-insular
    cortex, and **re-deriving the route is owed**. *(Class 1 — Chen, DeAngelis & Angelaki 2011;
    Chen, DeAngelis & Angelaki 2013; macaque. Not yet verified for the source.)*
  - **→ the cortical vestibular areas onward** — the parieto-insular vestibular cortex projects on
    to the ventral intraparietal area and thence to the medial superior temporal area — **carries:**
    the same computed estimate, in a frame that changes at each step: intermediate between head- and
    body-centred at the parieto-insular cortex, **body-centred** at the ventral intraparietal area,
    approximately **head-centred** at the medial superior temporal area. **Payload otherwise as
    above.** **Fan-out:** unknown. *(Class 1 — Chen, DeAngelis & Angelaki 2013, macaque. Not yet
    verified for the source.)*
- **Internal structure and internal data flow:** *(From web search; abstracts and
  excerpts only. Nothing here is yet verified for the source.)*

  **Velocity storage: a named, measured payload change, and it is a repair rather than a
  re-expression.** The canal afferent's velocity signal decays with a time constant of **3–5
  seconds**. The sense of rotation, the activity in these nuclei, and the nystagmus produced by a
  step change in head velocity all have a time constant of **at least 15–25 seconds**. The
  mechanism that converts the short peripheral time constant into the long central one is called
  the **velocity storage integrator**. **The payload's *content* is unchanged — it is still angular
  velocity — and only its *persistence* is altered.** This file has no other edge whose declared
  transformation is purely temporal, and it is a useful category to have: a stage that neither adds
  nor removes dimensions but extends the life of what it receives. **The mechanism is owed** —
  nothing read says what implements the integrator. *(Class 1 — PMC5561016 and the Raphan/Cohen lineage it reviews.)*

  **Cell classes: at least one named by response rather than by place.** Type II **vestibular-only**
  neurons increase firing with rotation toward the **contralateral** canal — so the nuclei carry a
  population distinguished by what it responds to and by which side drives it, not by where it sits.
  Further partition of the four nuclei by cell class is **not established here** and is
  **owed**.

  **The ambiguity resolution this entry's Function field claims has its substrate here, and it is
  a convergence.** Neither transducer alone can disambiguate tilt from translation; the resolution
  is the **specific convergence of semicircular-canal and otolith signals onto central vestibular
  neurons**. **So the internal edge that matters most in this entry is the one where two
  *inter-stage* inputs meet** — and the entry declares both inputs without declaring the meeting.
  **Owed: the convergence edge, and which cells carry it.** *(Class 1 — Straka & Dieringer 2004;
  Angelaki 2004, as reported in J Neurosci 28:8086, 2008. Not yet verified for the source.)*
- **Neurons:** soft / unknown (the four nuclei; the parieto-insular vestibular cortex) — no clean human counts recorded here.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** the vestibular nerve and the medial
  longitudinal fasciculus are myelinated; g-ratio unknown.

**The other senses are described:** olfaction (bulb → piriform / primary olfactory cortex, the
sole thalamus-bypassing sense, with verified human bulb numbers — ~5,500 glomeruli, ~50,000
mitral cells, ~50 mm³) → orbitofrontal secondary cortex; taste (nucleus of the solitary tract → ventral posteromedial parvocellular thalamic nucleus → anterior-insula /
operculum primary cortex → orbitofrontal flavour cortex); and vestibular sensation — **two
transducers, not one** (semicircular canals → rotation rate; otolith organs → gravito-inertial
acceleration) → vestibular nuclei → thalamus → parieto-insular cortex + area 2v/3a, and thence
cortically to the medial superior temporal and ventral intraparietal areas — a
sense with no dedicated primary cortex, and the one sense whose headline quantity (**attitude**) is
**computed centrally rather than transduced**, because a linear-acceleration transducer cannot
separate a steady tilt from a steady acceleration. Counts are verified for the olfactory bulb and
soft/unknown for the taste and vestibular transducers, relays, and cortices.

---

---

## References

*(Section under source design §2a. Every line below is a **candidate** awaiting Micky's
verification; none is verified.)*

**How to read a line.** A line **without** an **owed** mark was taken from a publisher or journal
record that was opened. A line marked **owed** was **not searched**, and whatever it carries —
journal, volume, page, year, species, method — is transcribed from this file's own citing lines and
from nothing else. **It is not a reference, and it is not evidence that anything was opened.** In
this file **every** line is owed: no reference here has been searched.

**65 distinct keys, 75 mentions. 0 searched; 65 owed.**

**The short form inline is the key here, exactly.** An entry cites *DeMaria & Ngai 2010*; the
authors, journal, volume, page, year and method sit on that key's line below and nowhere else.
Species stays inline, because several entries argue from it — mouse for the receptor-targeting
experiments, rodent for the bulb's neurogenesis, human for the carbon-14 result — and an argument
cannot be read with its premise on another page.

**Seven keys are malformed as extracted and cannot be searched until they are repaired at the citing
line.** *Lepousez et al.* carries no year. The *Haberly lineage* as compiled in the *ScienceDirect
piriform overview*, the *ScienceDirect vestibular overview*, the *aerospace-medicine compilation*
and the *Raphan/Cohen lineage* each name a body of work or an unattributed web overview rather than
a paper. *Neuron commentary 2012* and *Neurosci Lett 2009* give a journal and a year with no author,
volume or pages. A lineage or an overview page is a pointer, not a reference, and the repair —
naming the paper the citing claim rests on — belongs at the line making the claim, not here.

**Two key collisions, and both are in the file rather than in the extraction.** *Angelaki 2004* and
*Angelaki, Shaikh, Green & Dickman 2004* may be one paper written two ways; only the second gives an
author list, and which paper the two *Angelaki 2004* lines rest on is **owed at those lines**.
Separately, *Chen et al. 2011* is the two-photon gustatory imaging study and
*Chen, DeAngelis & Angelaki 2011* is a vestibular-cortex study — **different papers, same surname
and year**, distinguished in the file only by the fuller author list at the second. Resolving either
against its citing claim is a reading and would be Class 2.

**One key is a textbook rather than a paper**, cited at four lines: once with no chapter, via NCBI
Bookshelf NBK10824; twice at chapter 15; once at chapter 14. A textbook is a legitimate Class 3
source, but **the edition is given at none of the four**, and the Bookshelf identifier fixes only
the online copy. The chapter stays inline, as a locator within one source; the book is one key, not
three.

- **aerospace-medicine compilation** — **owed.** **A compilation citing the primary literature
  rather than a paper**, used for hair-cell alignment within a crista and for the contrasting
  multi-directional alignment across a macula. The repair belongs at the citing line.
- **Angelaki & Cullen 2008** — **owed.** The citing line carries nothing beyond the key.
- **Angelaki 2004** — **owed.** **May be the same paper as *Angelaki, Shaikh, Green & Dickman 2004*,
  written two ways** — see the note above. Which paper the two citing lines rest on is owed at those
  lines.
- **Angelaki, Shaikh, Green & Dickman 2004** — **owed.** Possibly the same paper as *Angelaki 2004*;
  this is the only one of the two carrying an author list.
- **Avery et al. 2020** — **owed.** Human functional imaging of taste quality.
- **Bergmann et al. 2012** — Bergmann et al., *Neuron* 74:634, 2012. **Human**; carbon-14 dating of
  olfactory bulb neurons. **owed.**
- **Bhatnagar et al. 1987** — **owed.** **Human**; mitral-cell counts and bulb volume by age.
- **Blanks, Curthoys & Markham 1975** — **owed.** Coplanar canal pairs in push-pull.
- **Brand 2006** — **owed.** Trigeminal chemosensation.
- **Chandrashekar et al. 2006** — **owed.** The labelled-line case for taste coding.
- **Chen et al. 2011** — **owed.** Anaesthetised mouse; two-photon calcium imaging of insular cortex
  — the gustatory "hot spot" study. **Not the same paper as *Chen, DeAngelis & Angelaki 2011*** —
  see the note above.
- **Chen et al. 2020** — **owed.** Alert mice; calcium imaging of insular taste responses.
- **Chen, DeAngelis & Angelaki 2011** — Chen, DeAngelis & Angelaki, *Journal of Neuroscience*
  31:3082, 2011. Macaque; vestibular cortex. **owed.**
- **Chen, DeAngelis & Angelaki 2013** — Chen, DeAngelis & Angelaki, *Neuron* 80:1310, 2013. Macaque;
  vestibular cortex. **owed.**
- **Chikazoe et al. 2019** — **owed.** **Human**; distributed representation of taste quality.
- **Cleland 2010** — **owed.** Bulbar computation, as reviewed in PMC4968158.
- **Cometto-Muñiz & Simons 2015** — **owed.** Nasal chemesthesis.
- **DeMaria & Ngai 2010** — DeMaria & Ngai, *Journal of Cell Biology* 191:443, 2010. Review of
  olfactory receptor cell biology and regeneration. **owed.**
- **Ernst et al. 2014** — **owed.** **Human**; neuroblast migration toward the striatum.
- **Fernández & Goldberg 1976** — **owed.** The otolith afferent as a gravito-inertial transducer.
- **Fletcher et al. 2017** — **owed.** Mouse; calcium imaging with a more sensitive indicator
  (GCaMP6), finding broad tuning and no gustotopic organisation.
- **Front Neural Circuits 18:1467203, 2024** — *Frontiers in Neural Circuits* 18:1467203, 2024.
  Rodent; differential contact of adult-born and neonatally-born granule cells onto mitral and
  tufted cells. **owed.**
- **Gheusi et al. 2000** — **owed.** Bulbar granule-cell reduction and odour discrimination.
- **Goldberg & Fernández 1971** — **owed.** The canal afferent as a rotation-rate line.
- **Haberly & Feig 1983** — **owed.** Piriform laminar organisation.
- **J Neurosci 28:8086, 2008** — *Journal of Neuroscience* 28:8086, 2008. Reports the
  Straka & Dieringer 2004 and Angelaki 2004 findings on canal–otolith convergence. **owed.**
- **J Neurosci 34:341, 2014** — *Journal of Neuroscience* 34:341, 2014. Trigeminal collaterals to
  the olfactory epithelium and bulb. **owed.**
- **J Neurosci 40:1042, 2020** — *Journal of Neuroscience* 40:1042, 2020. **Human**; high-resolution
  functional imaging with multivariate analysis of taste quality. **owed.**
- **Kay & Stopfer 2006** — **owed.** Bulbar computation, as reviewed in PMC4968158.
- **Large et al. 2016** — **owed.** Rodent; piriform feedback inhibition.
- **Lepousez et al.** — **owed.** **No year at the citing line**; reviewed in PMC4968158. It cannot
  be searched until the year is supplied at that line.
- **Maresh et al. 2008** — **owed.** **Human**; glomerular counts per bulb.
- **Merfeld, Zupan & Peterka 1999** — **owed.** The internal-model account of gravity/acceleration
  separation.
- **Mombaerts 2004** — **owed.** One-neuron-one-receptor, as reviewed in DeMaria & Ngai 2010.
- **Mombaerts et al. 1996** — **owed.** **Mouse**; gene-swap evidence for receptor-directed axon
  targeting.
- **Mori & Sakano 2011** — **owed.** Receptor-directed targeting, as reviewed in DeMaria & Ngai
  2010.
- **Mouret et al. 2008** — **owed.** Olfactory training and the survival of newly generated neurons.
- **Nat Commun 7:12238, 2016** — *Nature Communications* 7:12238, 2016. Layer-specific gene
  expression defining distinct piriform projection targets. **owed.**
- **Neuron commentary 2012** — **owed.** **A journal and a year with no author, volume or pages.** A
  commentary on the carbon-14 neurogenesis paper, noting that the finding cannot rule out ongoing
  bulbar neurogenesis where olfactory demand is high.
- **Neurosci Biobehav Rev 30:908, 2006** — *Neuroscience and Biobehavioral Reviews* 30:908, 2006.
  Nasal chemical sensation as one integrated multimodal afferent signal. **owed.**
- **Neurosci Lett 2009** — **owed.** **A journal and a year with no author, volume or pages.**
  Raised trigeminal thresholds in olfactory loss.
- **Neville & Haberly 2004** — **owed.** Piriform laminar organisation.
- **PMC3834179** — *PLoS One*; PubMed Central PMC3834179. X-ray computed tomography of
  semicircular-canal geometry in 39 mammal species. **owed.**
- **PMC4968158** — **owed.** A review of bulbar computation, compiling Kay & Stopfer 2006, Cleland
  2010 and Lepousez et al.
- **PMC5561016** — **owed.** Velocity storage and canal afferent dynamics.
- **PMC6520623** — **owed.** Canal afferent sensitivity and discrimination thresholds.
- **Price 1973** — **owed.** Piriform cell classes.
- **PubMed 30788507** — Review, 2019; PubMed 30788507. Taste coding becomes more distributed and
  more temporally patterned as signals ascend. **owed.**
- **PubMed 9580447** — **owed.** Reports anosmic and normosmic irritation sensitivity as comparable
  — the contrary result to the raised-threshold finding.
- **Purves, Neuroscience** — **owed.** A textbook, cited at four lines: once without a chapter (via
  NCBI Bookshelf NBK10824), twice at chapter 15, once at chapter 14. **The edition is given at none
  of them**, and the Bookshelf identifier fixes only the online copy. A textbook is a legitimate
  Class 3 source; the missing edition is the defect.
- **Raphan, Matsuo & Cohen 1979** — **owed.** Velocity storage as a central integrator.
- **Raphan/Cohen lineage** — **owed.** **A body of work rather than a paper**, reviewed in
  PMC5561016. The repair belongs at the citing line.
- **Sanai et al. 2011** — **owed.** **Human**; neuroblast migration to the bulb in infancy and its
  absence in the adult.
- **ScienceDirect piriform overview** — **owed.** **A body of work compiled on an unattributed web
  overview, not a paper.** The repair — naming the paper the citing claim rests on — belongs at the
  citing line.
- **ScienceDirect vestibular overview** — **owed.** **An unattributed web overview, not a paper.**
  The repair belongs at the citing line.
- **Serizawa et al. 2003** — **owed.** One-neuron-one-receptor, as reviewed in DeMaria & Ngai 2010.
- **Steinhausen 1933** — **owed.** The canal as a heavily damped torsion pendulum.
- **Stokes & Isaacson 2010** — **owed.** Rodent; feedforward inhibition in piriform cortex.
- **Straka & Dieringer 2004** — **owed.** Canal–otolith convergence onto central vestibular neurons.
- **Suzuki & Bekkers 2010** — **owed.** Rodent; piriform interneuron classes.
- **Suzuki & Bekkers 2011** — Suzuki & Bekkers, *Journal of Neuroscience* 31:2156, 2011. **Mouse**;
  patch-clamp recording with cluster analysis of piriform principal-cell classes. **owed.**
- **Tomchik et al. 2007** — **owed.** The across-fibre case for taste coding.
- **van Egmond, Groen & Jongkees 1949** — **owed.** The torsion-pendulum model of the canal.
- **Vargas-Barroso et al. 2013** — Vargas-Barroso et al., *Anatomical Record* 296, 2013. **Albino
  rat**; rapid-Golgi. Reports afferent fibres penetrating beyond layer I into layer II. **owed.**
- **Wesson 2013** — **owed.** Carbon dioxide evoking responses in piriform cortex.
