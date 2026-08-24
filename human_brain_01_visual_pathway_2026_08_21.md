# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-21
---

---

# FILE 1 OF 20 — VISUAL PATHWAY

**What is in this file.** The ventral visual stream, front to back: the retina where colour is
already computed, the chiasm, the lateral geniculate nucleus, and the cortical chain V1 → V2 →
V3/V3A → V4 → inferotemporal cortex. This is the most fully worked line in the source and the one
the slot standard was developed on.

**Size:** 1564 lines, ~33.5k tokens (estimated from bytes, not tokenised). **Entries:** 8.

**Cross-file status of the marks in this file.** Marks against files 4 (dorsal visual / parietal
stream), 5 (sensorimotor loop), 6 (posterior parietal), 7 (anterior temporal lobe), 8 (medial
temporal lobe), 11 (frontal lobe) and 17 (insula / claustrum / habenula / cingulate remainder) are
**checked** against the far file. Marks against 2 (auditory), 3 (other senses), 9, 10, 12–16 and
18–20 are **unchecked**.

**This file is one section of the source. Edges cross into other files; an endpoint named here that
has no entry here lives in another file. Do not treat a missing endpoint as a missing region without
checking the other files.**

**Entries in this file:**

- **Retina (sensory front end, neural tissue of the eye)**
- **Optic chiasm (fiber crossing)**
- **Lateral geniculate nucleus (visual thalamus)**
- **V1 — primary visual cortex (striate cortex, isocortex)**
- **V2 — secondary visual cortex (ventral stream, isocortex)**
- **V3 / V3A — early extrastriate (intermediate tier, dorsal-leaning; isocortex)**
- **V4 — ventral visual area (ventral stream, isocortex)**
- **Inferotemporal cortex (ventral stream endpoint, isocortex)**

---

# VISUAL PATHWAY

## Retina (sensory front end, neural tissue of the eye)

- **Function:** phototransduction and the first stage of visual processing —
  light to neural signal, with center-surround spatial processing, ON/OFF
  channel splitting, and **cone-opponent (color) processing** before the signal
  leaves the eye. The **color computation happens here, in the eye, not downstream.** Three
  cone classes, defined by their opsins — **long-wavelength, medium-wavelength and short-wavelength**
  (Nathans et al. 1986) — are read out by three ganglion-cell classes, and the opponency is
  already formed at the ganglion-cell output. The **midget** cell is spatially *and* spectrally
  opponent by construction: in central retina its receptive-field center draws from a single cone
  (long- or medium-wavelength) and its antagonistic surround from the opposite class (Reid & Shapley
  1992; Reid & Shapley 2002 —
  center/surround segregation of long- and medium-wavelength input in ~80% of central parvocellular
  cells; surrounds
  in the periphery are mixed rather than cone-selective, Field et al. 2010). The **small
  bistratified** cell opposes a short-wavelength-cone ON signal to a combined
  long-plus-medium-wavelength OFF signal, driven by a
  blue-specific bipolar cell (Dacey & Lee 1994). The **parasol** cell sums long- and
  medium-wavelength input and is not
  color-opponent (Gouras 1968; Shapley & Perry 1986).
  **Contested, recorded not smoothed:** some OFF-midget cells receive short-wavelength-cone input (a
  short-wavelength-OFF
  midget pathway; Tsukamoto & Omi 2015; Wool et al. 2019), and the classification of the
  small bistratified cell as a "pure color" unit has been questioned (Field et al. 2007;
  Tailby et al. 2010; cf. Crook et al. 2009). The three-channel account above is the
  mainstream one and is what this document carries.
- **Inputs:**
  - **light** (the world) — **carries:** photon flux across the spectrum, imaged on the
    photoreceptor sheet; a mechanical/optical input, not a neural edge, and the only region in
    this file whose input is not another region. **Fan-in:** not applicable.
- **Outputs:** all four leave as **retinal ganglion cell axons in the optic nerve**, which splits
  at the chiasm. Four targets, three of them non-image-forming:
  - **→ optic chiasm → lateral geniculate nucleus** (the image-forming line; ~80/10/8–10% of the ganglion population)
    — **carries:** three parallel channel classes, each spatially retinotopic, each split ON and
    OFF, and **each declaring its spectral content**:
    **midget / parvocellular (~80%)** — fine spatial detail, sustained; **red–green cone-opponent
    (long-wavelength versus medium-wavelength)**;
    **parasol / magnocellular (~10%)** — coarse spatial detail, transient, motion; **achromatic
    (long- plus medium-wavelength)**, not cone-opponent;
    **bistratified / koniocellular (~8–10%)** — **blue–yellow cone-opponent (short-wavelength-ON
    versus long-plus-medium-wavelength-OFF)**.
    The bus leaving the eye therefore carries **three chromatic classes, not one intensity
    signal**; any downstream stage that reads hue or surface color is reading this.
    **Does not carry:** absolute illuminant level (it is discounted by adaptation in the eye),
    binocular disparity (the eyes are still separate), or any oriented-edge code.
    **Fan-out:** unknown (the ganglion-cell divergence onto lateral geniculate nucleus relay cells
    is not recorded here).
  - **→ superior colliculus, superficial layers** (the retinotectal projection) — **carries:**
    retinotopic luminance transients for orienting; **payload otherwise unknown — owed.**
    **"Minority collateral" is now two separate claims, and both are measured.** *Minority:* not
    more than **10%** of macaque retinal ganglion cells project here, about **6%** near the fovea,
    rising slightly with eccentricity — the reverse of the geniculate line's foveal emphasis, and
    the reason this is not a second copy of the image-forming bus. The projecting cells are
    small-to-medium-bodied and sparsely branched, of magnocellular and koniocellular type rather
    than midget. *Collateral:* the retinal input to the macaque colliculus is reported to derive
    from **branching axons that also project to the lateral geniculate nucleus** — so this is
    largely not a separate ganglion-cell population with its own axon, but a branch off the
    geniculate line. **A consumer that treats this edge as an independent channel would be wrong
    about where its content comes from.** **Fan-out:** unknown. *(Class 1 — Perry & Cowey 1984,
    macaque; Zheng et al. 2024, macaque. Web search, abstracts only. Not yet verified for the
    source.)*
    **Contested at the far end, and stated in full there:** whether this edge drives spiking in the
    colliculus at all in the awake adult primate is now directly disputed — see the superior
    colliculus entry.
  - **→ olivary pretectal nucleus** — **carries:** **ambient luminance as a scalar** — a
    slow, broad-field "how much light is falling on this eye" signal for the pupillary light
    reflex, from broad-field luminance-detector ganglion cells that contain melanopsin and are
    intrinsically photosensitive while also taking rod and cone input. **Not an image, and not
    retinotopic in its use**: the receiving cells' dendrites span the whole nucleus, so whatever
    spatial structure arrives is integrated away (see that entry). **Does not carry:** hue, form,
    motion, or eye of origin in any form the reflex uses — the response is equal in both eyes.
    **The split at the chiasm applies to this edge too**: temporal retina reaches the ipsilateral
    nucleus and nasal retina the contralateral one, and in macaque the two densities are **nearly
    equal**, which is why the direct and consensual responses match. **Fan-out:** unknown.
    *(Class 1 — Gamlin, Zhang & Clarke 1995, rhesus; Brain Struct Funct, PMC6957570, macaque. Web
    search, abstracts only. Not yet verified for the source.)*
  - **→ suprachiasmatic nucleus** (retinohypothalamic tract, melanopsin ganglion cells) —
    **carries:** slow ambient irradiance — a "how bright is the world" scalar for circadian
    entrainment, not an image and not a color signal. **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.** Species noted per line; the circuit is largely primate and mammalian
  general.)*

  **Sub-elements by cell class: five, in a three-deep chain with two lateral populations.**
  - **Photoreceptors** — rods, and cones of three classes, as the Neurons field records.
  - **Horizontal cells** — lateral, at the first synaptic stage.
  - **Bipolar cells** — the middle of the chain, in ON and OFF types.
  - **Amacrine cells** — lateral, at the second synaptic stage.
  - **Ganglion cells** — the output, in the classes the Outputs field already names.

  **Sub-elements by layer: two synaptic layers, and they are where the lateral populations act.**
  The **outer plexiform layer** holds the photoreceptor–horizontal–bipolar synapses; the **inner
  plexiform layer** holds the bipolar–amacrine–ganglion synapses. The chain runs
  photoreceptor → bipolar → ganglion **vertically**, and horizontal cells and amacrine cells
  spread **laterally** across it, one in each synaptic layer. *(Class 3 — general anatomy; Current
  Biology 9:R666, 1999.)*

  **Almost nothing here spikes, and the exception marks where distance begins.** Photoreceptors,
  horizontal cells and bipolar cells respond to light with **slow graded changes in membrane
  potential** and generate **no action potentials**. Ganglion cells spike; **some** amacrine cells
  spike and some do not. So the retina computes in analogue and converts to spikes at exactly the
  cell whose axon has to leave the eye — the conversion tracks **transmission distance**, not depth
  in the processing chain. *(Class 1 — Werblin & Dowling 1969; Baylor & Fuortes 1970; Kaneko 1970;
  Current Biology 9:R666, 1999.)*

  **Contested, recorded not smoothed:** one type of ON bipolar cell has been shown to carry a large
  sodium current and to fire **one to three all-or-nothing action potentials** at light onset, with
  millisecond precision, while also producing graded responses to continuous stimuli. So "bipolar
  cells do not spike" is a strong generalisation with at least one demonstrated exception, in a cell
  proposed to belong to a dedicated fast dark-to-light pathway. *(Class 1 — J Neurosci 32:297,
  2012; ground squirrel.)*

  **The sign convention is inverted here relative to the rest of the file, and it is not a
  formality.** Photoreceptors **hyperpolarise** in response to light and release **more**
  transmitter in the dark. Because these cells do not spike, hyperpolarisation is not inhibition:
  in the outer retina a hyperpolarising response **is** the excitatory response. Any downstream
  account that reads depolarisation as activation and hyperpolarisation as suppression will read
  the outer retina exactly backwards. *(Class 1 — Dowling 1991.)*

  **The ON/OFF split is made at one synapse, by receptor type, and not by a separate circuit.**
  Both bipolar classes receive the same glutamate from the same photoreceptors. The **OFF** bipolar
  cell carries ionotropic receptors and is **sign-conserving** — glutamate depolarises it, so it
  is depolarised in darkness. The **ON** bipolar cell carries metabotropic receptors that are
  inhibitory to glutamate and is **sign-inverting** — glutamate hyperpolarises it, so it is
  depolarised in light. The entire ON/OFF channel structure that the rest of the visual line
  carries forward originates in that one difference of receptor at one synapse. Pharmacologically
  blocking the metabotropic pathway in the eye abolishes the ON response downstream in the thalamus
  and leaves the OFF response intact. *(Class 1 — Schiller 1995; Schiller 2010;
  the thalamic block, Nature 297:580, 1982; monkey.)*

  **Internal edges:**
  - **photoreceptor → OFF bipolar cell** (outer plexiform layer) — **carries:** the graded
    photoreceptor signal, **sign-conserved**. **Fan-in:** unknown. **Fan-out:** unknown.
  - **photoreceptor → ON bipolar cell** (outer plexiform layer) — **carries:** the same graded
    signal, **sign-inverted at the receptor**. **Fan-in:** unknown. **Fan-out:** unknown.
  - **photoreceptor → horizontal cell** — **carries:** the same graded signal; excitatory.
    **Fan-in:** unknown. **Fan-out:** unknown.
  - **horizontal cell → photoreceptor** (feedback, to the *surrounding* photoreceptors) —
    **carries:** inhibition, spatially offset from the cell that drove it. **This edge is the
    antagonistic surround** — the centre–surround structure the Function field claims is built
    here and nowhere earlier. **Fan-in:** unknown. **Fan-out:** unknown.
  - **horizontal cell ↔ horizontal cell** (gap junctions) — **carries:** direct electrical
    coupling, forming a lateral network rather than a set of independent cells; the coupling is
    **modulated by dopamine**, so the spatial extent of the surround is itself adjustable.
    **Fan-in:** unknown. **Fan-out:** unknown.
  - **bipolar cell → ganglion cell** (inner plexiform layer) — **carries:** the centre–surround,
    sign-split signal. The ganglion cell's receptive field is derived from the bipolar cells that
    feed it. **Fan-in:** unknown. **Fan-out:** unknown.
  - **bipolar cell → amacrine cell** — **carries:** the same. **Fan-in:** unknown. **Fan-out:**
    unknown.
  - **amacrine cell → bipolar cell terminal** — **carries:** inhibition applied **presynaptically**,
    controlling transmission from the bipolar cell to the ganglion cell rather than inhibiting the
    ganglion cell directly. **Fan-in:** unknown. **Fan-out:** unknown.
  - **amacrine cell → ganglion cell** — **carries:** the transient and motion-sensitive component;
    amacrine cells strongly shape the **time course** of the ganglion cell's response and are the
    reason transient and ON–OFF ganglion responses exist at all. **Fan-in:** unknown. **Fan-out:**
    unknown.
  - **amacrine cell ↔ amacrine cell** (gap junctions, dopamine-modulated) — **carries:** electrical
    coupling, as with the horizontal cells. **Fan-in:** unknown. **Fan-out:** unknown.

  **What the two lateral populations do differently.** The horizontal cells act in **space** — they
  build the antagonistic surround at the first synapse. The amacrine cells act in **time** — they
  build the transient response at the second. The retina's centre–surround and its ON/OFF split
  therefore have different origins, at different depths, by different mechanisms, and the entry's
  Function field lists them together as though they were one operation. *(Class 1 — Current Biology
  9:R666, 1999.)*

  **Sub-element counts: partly available and not carried here.** The Neurons field records
  photoreceptor and cone-class counts and the ganglion-cell total. **No count is recorded for
  horizontal, bipolar or amacrine cells**, and the amacrine population in particular is known to
  comprise many morphological types. **Owed.**
- **Neurons:** photoreceptors ~126M (textbook: ~120M rods + ~6M cones) /
  ~97M (primary measurement, Curcio et al. 1990; rods ~92M range 78–107M,
  cones ~4.6M range 4.08–5.29M). Rod:cone ≈ 20:1 overall, but strongly
  eccentricity-dependent: ≈ 1:1 near the center and ≈ 30:1 in the periphery
  (Curcio et al. 1990). Both figures are literature-standard; the document carries both.
  Retinal ganglion cells: see Axons (their axons are the optic nerve).
  **Cone classes, of the ~4.6M cones:** **long-wavelength : medium-wavelength ≈ 2 : 1** on average
  in the central fovea, but
  **highly variable between individuals** — psychophysical estimates range from ~0.33:1 to ~10:1
  (Colour and Vision Research Laboratory topographic distributions; Hofer et al. 2005); a genuine
  between-individual spread, not
  measurement error, and color vision is largely unaffected by it. **short-wavelength cones ≈
  5–10%** of cones,
  absent from the central foveola, **nonrandomly but irregularly distributed** (Williams et al.
  1981; Ahnelt et al. 1987; Curcio et al. 1991); long- and medium-wavelength cones appear randomly
  interleaved (Curcio et al.
  1991). **Peak foveal cone density ≈ 199,000 cones/mm²**, individually variable (100,000–324,000)
  (Curcio et al. 1990), falling steeply with eccentricity (~32,200 / ~19,300 / ~11,600 cones/mm² at
  0.5 / 1.0 / 1.5 mm from the foveal center; adaptive optics), and higher along the horizontal
  meridians than the vertical at matched eccentricity.
- **Synapses:** unknown.
- **Axons:** optic nerve ~1.0–1.2M ganglion-cell axons per eye. Retina→lateral geniculate nucleus
  compression ≈ 100:1 average, space-variant (~1:1 at fovea, up to ~1000:1 far
  periphery — i.e. foveated).
- **Grey-matter volume:** unknown (retina is not cortical grey; volume not
  recorded here).
- **White-matter volume:** unknown.
- **Myelination:** optic nerve is myelinated (retinal ganglion cell axons);
  per-fiber g-ratio unknown.

## Optic chiasm (fiber crossing)

- **Function:** routing, not computation. Fibers cross so each hemisphere
  receives the contralateral visual hemifield. **No synapse, no transform — and this claim has now
  been checked rather than asserted.** What the checking found: every report of neurons *at* the
  chiasm is **developmental**. An inverted-V array of neurons expressing L1, CD44 and SSEA-1
  occupies the ventral diencephalon **before** the retinal axons arrive; the arriving axons do not
  penetrate it but turn along its anterior border, which is what gives the chiasm its X shape. The
  described function of those cells is **axon guidance**, not transmission. No report was found of
  a persisting adult population here, of a synapse, or of any transform.
  **That is an absence in what was searched, not a demonstration of absence.** No study was found
  that looked for adult chiasmatic neurons and reported none; the developmental literature simply
  stops at birth. So the claim stands as **unfalsified rather than verified**, and the honest form
  is: nothing reached so far gives the chiasm a payload change. *(Class 1 for the
  developmental neurons — Sretavan & Mason 1994 lineage; Physiol Rev 81:1393, 2001; PubMed 15951026;
  mouse embryo. Class 2 for the reading placed on the absence. Web search;
  no primary paper opened. Not yet verified for the source.)*
- **Inputs:**
  - **← retina** (optic nerve, both eyes) — **carries:** the eye's full three-class ganglion bus
    (midget red–green, parasol achromatic, bistratified blue–yellow; retinotopic, ON and OFF), one
    per eye, still monocular and still whole-hemifield. **Fan-in:** none (no synapse here).
- **Outputs:**
  - **→ lateral geniculate nucleus of each hemisphere** (optic tract) — **carries:** the same
    payload, unchanged — nothing is added, removed, or transformed. What changes is **which fibers
    go where**: nasal fibers cross, temporal fibers stay ipsilateral, so each optic tract now
    carries the **contralateral visual hemifield of both eyes** rather than one whole eye.
    **Eye of origin is part of this payload and must be declared as such.** Each fibre still carries
    exactly one eye's signal — the tract is two interleaved monocular buses sharing a hemifield, not
    a merged one — and the two are kept apart, unmixed, until the primary visual cortex. Downstream
    entries that describe the signal only as "monocular" are under-declaring: **which** eye is a
    property the receiving structures are organised around. **Fan-out:** none (no synapse here).
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.**)*

  **Sub-elements: two fibre bundles, sorted by a spatial boundary on the retina.** The **crossed
  bundle**, from ganglion cells nasal to the fovea, and the **uncrossed bundle**, from ganglion
  cells temporal to it. There are **no internal edges** — no synapse occurs here, so this entry has
  sub-elements and a routing rule but no internal data flow, which is a shape the slot has not taken
  before.

  **The sorting rule is a line, and the line has a position.** The **line of decussation** separates
  the ganglion cells that project across from those that do not, and it is **normally aligned with
  the fovea**. That alignment is what makes the two hemifields divide cleanly at the point of
  fixation. It is not fixed by anatomy alone: in albinism the line is displaced on average about
  **8 degrees into the temporal retina**, and crossing is correspondingly increased — which is the
  clearest evidence that the boundary is a developmental variable rather than a structural given.
  *(Class 1 — bioRxiv 633347; StatPearls, Neuroanatomy, Optic Chiasm; human.)*

  **Ratio: about 53 crossed to 47 uncrossed** in the neurotypical human, one source giving a band of
  53–57% crossing. **Total traffic: about 2 million fibres** through the chiasm, both eyes combined —
  consistent with the per-eye optic-nerve figure in the retina entry. **About 5%** are destined for
  structures other than the two geniculate nuclei: the suprachiasmatic nucleus, the pretectal
  region, and eye-movement structures, all of which this file's retina entry already declares as
  separate output edges. *(Class 1 — StatPearls, Neuroanatomy, Optic Chiasm; Eye (Lond),
  s41433-024-03137-7, 2024; human.)*

  **Why the ratio is not 50:50, and why it is not 100:0.** In lateral-eyed animals the optic fibres
  decussate **entirely**. The uncrossed proportion rises as the orbits rotate forward and the
  binocular field grows. The 53:47 figure is therefore a consequence of eye placement, and the
  slight majority for crossing reflects the nasal retina being the larger sector once the boundary
  sits at the fovea. *(Class 1 — clinical anatomy review; comparative.)*
- **Neurons:** none (fiber tract, not a nucleus) — and this is the same claim as the one in
  Function, so it carries the same status: no adult human count exists because no adult population
  has been reported, and no search was found that tested for one. The neurons described at this
  site are the embryonic guidance array.
- **Synapses:** none reported; see Function for what that rests on.
- **Axons:** the crossing/non-crossing ganglion-cell axons (nasal fibers cross,
  temporal fibers stay ipsilateral).
- **Grey-matter volume:** not applicable. **White-matter volume:** unknown.
  **Myelination:** myelinated tract; g-ratio unknown.

## Lateral geniculate nucleus (visual thalamus)

- **Function:** thalamic relay from retina to V1 — and the relay is **a gate, not a wire**. Six
  layers (1–2 magnocellular, 3–6 parvocellular, with koniocellular sublayers between); each layer
  monocular (driven by one eye). Retina is the functional driver but a small minority of
  synapses; the majority of lateral geniculate nucleus synaptic input is non-retinal (cortical feedback,
  thalamic reticular nucleus, brainstem).
- **Gating — what the other ~90% of the synapses are for.** The retinal input is the **driver**: it
  alone sets what the message *is* (the receptive field, the opponency, the eye of origin). The far
  larger non-retinal input is **modulatory**: it sets **whether, when, and how strongly** that
  message is passed on, and it adds no content of its own — the driver/modulator distinction
  (Sherman & Guillery 1998). The three modulator sources are the ones this entry's Inputs already
  name: **corticothalamic feedback from V1 layer 6** (~30% of synapses — the largest single
  non-retinal source, and a *descending* projection that outnumbers the ascending drive it
  regulates); the **thalamic reticular nucleus**, whose GABAergic shell every thalamocortical and
  corticothalamic axon passes through and drives — the attentional "searchlight" (Crick 1984, and
  see the reticular-nucleus entry); and the **brainstem** cholinergic / noradrenergic /
  serotonergic arousal input.
  **The mechanism of the gate is known, and it is a change of transfer function rather than of
  message.** Relay cells fire in two modes — **burst** (hyperpolarised, the T-type calcium
  conductance de-inactivated: high-gain, nonlinear, detection-like) and **tonic** (depolarised:
  near-linear, faithful transmission) — and the modulatory inputs move cells between the two
  (Sherman 2001). The retinal payload is not rewritten by this; it is admitted, attenuated, or
  transformed in how faithfully it is carried.
  **This is measurable ahead of cortex:** attention modulates the human lateral geniculate nucleus
  response, so
  attentional gain is present in the visual data flow **before V1** (O'Connor et al. 2002). The
  consequence for the map is that the first place the visual stream is *selected*
  is the thalamus, not the cortex — and that a stage described only as a "relay" would have made
  that unstatable.
- **Inputs:**
  - **← retina** (via the optic chiasm / optic tract; **~5–10% of lateral geniculate nucleus synapses**, Hamos et al.
    1987 — a small minority of synapses and the *sole driver*) — **carries:** the eye's three
    ganglion channel classes, retinotopic, ON and OFF, still monocular, and each with its spectral
    content already formed: **midget → red–green (long-wavelength versus medium-wavelength)**,
    **bistratified → blue–yellow
    (short-wavelength versus long-plus-medium-wavelength)**, **parasol → achromatic**. The three map
    **one-to-one onto the three layer classes** —
    parvocellular layers 3–6 ← midget; koniocellular sublayers ← small bistratified; magnocellular
    layers 1–2 ← parasol (Wiesel & Hubel 1966; De Valois et al. 1966; Derrington, Krauskopf &
    Lennie 1984; Martin et al. 1997; Roy et al. 2009). The three cardinal chromatic classes
    described physiologically by De Valois et al. (1966) were later matched to these three
    ganglion-cell types. **Fan-in:** unknown (a relay cell is driven by very few retinal
    afferents — the classic figure is one to a few — but no human count is pinned here).
  - **← V1 6a** (corticothalamic feedback; **~30% of synapses**, the largest single
    non-retinal source) — **carries:** no new visual content. A **modulatory** signal that sets
    whether and how strongly the retinal payload passes (see Function). **Fan-in:** unknown.
  - **← thalamic reticular nucleus** — **carries:** inhibition; a gain/gate control, no content.
    **Fan-in:** unknown.
  - **← brainstem** (cholinergic / noradrenergic / serotonergic) — **carries:** arousal state,
    which sets the relay cells' burst-vs-tonic mode; no content. **Fan-in:** unknown.
- **Outputs:**
  *The projection to V1 is **three edges, not one**. The three layer classes stay segregated and
  terminate on **three different sub-elements of V1**, and only two of the three reach layer 4. The
  relay does not mix the classes and does not create them: color arrives at the lateral geniculate
  nucleus already formed
  in the eye and leaves it substantially intact (Usrey et al. 1999). **What the gate changes is not
  the payload but its passage** — admitted or attenuated, carried more or less faithfully according
  to the relay cell's mode. The content leaving is the content that entered; the* selection *is what
  the thalamus adds. **None of the three carries:** orientation, binocular disparity, or any cortical
  code — none of these exist yet. (Written as three edges, matching V1's own sub-elements rather than
  a bare "layer 4". Class 3 — general anatomy. Not yet verified for the source.)*
  - **→ V1 4Cα**, via the optic radiation, from **magnocellular layers 1–2** — **carries:** the
    achromatic channel, retinotopic, point-to-point, still **monocular** (the eyes first combine in
    V1). **Fan-out:** unknown.
  - **→ V1 4Cβ**, via the optic radiation, from **parvocellular layers 3–6** — **carries:**
    red–green (long-wavelength versus medium-wavelength), retinotopic, point-to-point, still
    monocular. **Fan-out:** unknown.
  - **→ V1, the cytochrome-oxidase blobs of layers 2/3 and layer 1**, via the optic radiation, from the
    **koniocellular sublayers** — **carries:** blue–yellow (short-wavelength versus
    long-plus-medium-wavelength), retinotopic, still monocular.
    **This edge does not terminate in layer 4.** **Fan-out:** unknown.
  - **→ V1 4A**, collaterals of the parvocellular and koniocellular projections — **carries:** a
    collateral copy of those two channels. **Payload beyond that — owed.** **Fan-out:** unknown.
  - **→ the middle temporal area, direct — bypassing V1 entirely** — **carries:** payload **owed**;
    enough to support motion sensitivity, on the evidence of what survives when V1 is destroyed.
    The projecting cells are **mostly koniocellular**, they send **virtually no collateral axons to
    V1**, and they number about **10% of the V1 population that innervates the middle temporal
    area**. **This contradicts the framing the rest of this entry assumes** — that the relay funnels
    everything into a primary area which then redistributes it. A second, small, direct line runs
    past V1 to a cortical area not conventionally called primary, and it is the leading explanation
    for residual motion sensitivity after V1 injury. **Fan-out:** unknown. *(Class 1 — Sincich et
    al. 2004, macaque. Not yet
    verified for the source.)*
  - **→ thalamic reticular nucleus** (collaterals of the thalamocortical axons) — **carries:** a
    copy of the outgoing signal, which is what drives the gate that regulates it. **Fan-out:**
    unknown.
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.** Species are noted per line; much of the synaptic work is cat and mouse.)*

  **Sub-elements by layer: six, plus the koniocellular sublayers.** **Layers 1 and 2**
  (magnocellular), **layers 3, 4, 5 and 6** (parvocellular), and a **koniocellular sublayer ventral
  to each** of the six. Each layer is **monocular**, and the layers **alternate by eye** — this is
  the structure that
  keeps the two eyes separate up to the cortex.

  **The eye assignment per layer is owed.** The conventional statement is that layers 1, 4 and 6
  receive the **contralateral** eye and layers 2, 3 and 5 the **ipsilateral** eye. That is
  **Class 3 — textbook recall, and unconfirmed by any search**, so it is recorded here as the claim
  to check rather than as a fact carried. Until it is checked, the
  four output edges below name a channel class and an eye-alternating layer set, but cannot name
  which layer carries which eye. The status of the interlaminar zones is disputed: they have been
  argued to belong to the adjacent perigeniculate nucleus rather than to this one. *(Class 3 for the
  laminar scheme; Class 1 for the dispute — J Neurosci 16:5923, 1996, ferret.)*

  **Sub-elements by cell class: two, in a fixed ratio.** **Relay cells** — the thalamocortical
  projection neurons, about **75–80%** of the nucleus — and **local interneurons**, about
  **20–25%**, which project nowhere outside it. *(Class 1 — Springer lateral geniculate nucleus
  models review; cat and
  mouse.)*

  **The signature internal structure is the triad, and it is unusual enough to state carefully.**
  A single retinal terminal contacts **both** a relay-cell dendrite **and** the dendritic terminal of
  a local interneuron; that same interneuron terminal then contacts **the same relay-cell dendrite**.
  The three elements are wrapped in a glial sheath, forming a **glomerulus**. The arrangement gives
  precise, local, feedforward inhibition of one relay dendrite by the very input that excites it.
  Triads form on grape-like appendages at branch points of the relay dendrite, and they are
  **selective by relay-cell class** — abundant on one class, absent on another, which received all
  terminal types without positional selectivity and engaged in no triads. *(Class 1 — Hamos et al.
  1985; Hamos et al. 1987; Rapisardi & Miles 1984; Morgan & Lichtman 2020; cat and mouse.)*

  **The interneuron's inhibitory output is not a spike, and that matters for the payload rule.**
  The interneuron has two kinds of release site: **axonal** terminals, and **dendritic** presynaptic
  specialisations at the ends of long thin processes. The dendritic ones — the ones inside the triad
  — can **release transmitter without generating an action potential**. So one internal edge in this
  entry carries a signal that is not a rate on an axon, and any description of "what is on the wire"
  that assumes spikes on axons does not cover it. *(Class 1 — Cox & Beatty 2017; J Neurosci
  33:1887, 2013; cat.)*

  **A quantitative asymmetry that inverts the intuitive picture.** Of the synaptic inputs onto
  **interneuron** dendrites, over **60%** are retinal. The corresponding figures for the two relay
  cell classes are **20%** and **7%**. The retina therefore drives the inhibitory local population
  far harder than it drives the cells that actually project to cortex — consistent with this entry's
  existing statement that retinal input is a minority of what relay cells receive, and sharpening
  it: the retina's main synaptic target inside this nucleus is not the relay cell. *(Class 1 —
  PMC10064015; cat.)*

  **Internal edges:**
  - **retinal terminal → relay-cell dendrite** — **carries:** the retinal payload, the driver input.
    A minority of the relay cell's synapses. **Fan-in:** unknown. **Fan-out:** unknown.
  - **retinal terminal → local interneuron dendritic terminal** — **carries:** the same retinal
    payload. Over 60% of that interneuron dendrite's input. **Fan-in:** unknown. **Fan-out:**
    unknown.
  - **local interneuron dendritic terminal → the same relay-cell dendrite** (the third leg of the
    triad) — **carries:** feedforward inhibition, locally scoped to one dendrite, released without
    a spike. **Fan-in:** unknown. **Fan-out:** unknown.
  - **local interneuron axonal terminal → relay cells** — **carries:** inhibition, on the
    conventional axonal route, and not confined to one dendrite. A single interneuron has been shown
    to participate in several kinds of inhibition and to innervate much of the visual thalamus, so
    these two edges are two output modes of **one** population, not two populations. **Fan-in:**
    unknown. **Fan-out:** unknown.
  - **relay-cell axon collateral → perigeniculate nucleus → relay cells** — **carries:** feedback
    inhibition, the second of the two inhibitory loops. Together the local and perigeniculate
    connections supply about **30% of the synapses on relay cells**. **Fan-in:** unknown.
    **Fan-out:** unknown. *(Class 1 — Current Biology 11:R656, 2001; cat.)*

  **Where the entry's non-retinal inputs land, which the Inputs field above does not say.** The
  corticothalamic feedback from V1's 6a innervates **relay cells, local interneurons and the
  perigeniculate nucleus alike**; the brainstem excites relay cells directly; and the perigeniculate
  nucleus itself receives an inhibitory projection **from the basal forebrain** — now declared at
  both ends, at the basal forebrain entry and at the thalamic reticular nucleus entry, of which the
  perigeniculate nucleus is the visual sector. Two such projections exist and they differ in sign:
  a parvalbumin GABAergic one that disinhibits the relay, and a cholinergic one whose stimulation
  promotes sleep. *(Class 1 — Current
  Biology 11:R656, 2001; PMC3447820, mouse.)*

  **One consequence for this entry's headline claim.** The Outputs field states that the content
  leaving is the content that entered and that selection is all the thalamus adds. The triad
  qualifies that: a class of relay cell — **lagged cells** — carries a **time delay** introduced by
  the triadic inhibition, is dependent on the inhibitory receptors there, and has slower-rising,
  more sustained responses than its non-lagged counterpart. So the nucleus also adds a **timing**
  transformation, to a subpopulation. Whether that counts as a change of payload or a change of its
  arrival time is a question this file's payload rule has not had to answer before. *(Class 1 —
  J Neurosci 33:1887, 2013; cat.)*
- **Neurons:** **~1.8M total per side** — modern human unbiased stereology (optical
  fractionator): normal controls ~1.77M (magnocellular ~0.22M + parvocellular ~1.55M) in
  ~104 mm³ (Dorph-Petersen et al. 2008). Older direct counts cluster ~1.0–1.2M (Chacko 1948,
  Sullivan 1958, Kupfer 1967); one stereology study runs high at ~3.5M (Selemon & Begović
  2007, treated as an outlier). The older ~1M "standard figure" (Wandell 1995) — basis of the
  ~40:1 V1:lateral geniculate nucleus ratio that paired 140M V1 with ~1M lateral geniculate nucleus
  — is superseded here; against the firmed
  V1 headline the stereological ~1.8M implies a V1:lateral geniculate nucleus ratio nearer ~160:1.
- **Synapses:** proportions known (retinal ~5–10%; cortical feedback ~30%; rest
  reticular/brainstem); absolute count unknown.
- **Axons:** optic radiation to V1; count unknown.
- **Grey-matter volume:** ~100 mm³ per hemisphere (postmortem range ~77–115 mm³,
  Andrews, Halpern & Purves 1997; in-vivo magnetic resonance imaging means ~80–120 mm³ per side across
  studies). The 2–3× individual variation is intrinsic and correlated across the
  visual system (optic tract, lateral geniculate nucleus, V1 co-vary in the same brain — Andrews,
  Halpern & Purves 1997), not
  measurement error. **White-matter volume:** unknown. **Myelination:** unknown.
- **Density cross-check available:** ~1.77M neurons / ~104 mm³ ≈ ~17,000 neurons/mm³
  (Dorph-Petersen et al. 2008, within-study) — close to the inferior colliculus's ~18,750/mm³ (Wong et al.
  2019) and far below V1's ~60,000/mm³, the expected loose packing of subcortical relays.

## V1 — primary visual cortex (striate cortex, isocortex)

- **Function:** first cortical stage. Binocular convergence (eyes first combine
  here — the basis of ocular-dominance columns), orientation maps, a precise
  retinotopic map of the visual field.
  Oriented-edge / spatial-frequency
  selectivity. **Color: the first cortical transformation of the cone-opponent signal** — the eye's
  signal is *transformed* here, not created here. Two kinds of color cell are present, and both
  matter (Shapley & Hawken 2011): **single-opponent** cells, chromatically opponent and spatially
  low-pass (best below ~0.5 cycles/degree, unresponsive above ~2 c/deg), which respond to large
  regions of uniform color; and **double-opponent** cells, chromatically opponent **and** spatially
  opponent — center excited by one color and inhibited by its opponent, surround reversed, best at
  ~2 c/deg — which respond to **color edges** and are the standard proposed substrate for color
  constancy downstream (Johnson, Hawken & Shapley 2001; Johnson, Hawken & Shapley 2008; Conway et al. 2010).
  **Organization:** color-preferring cells concentrate in the **cytochrome-oxidase blobs** of
  layers 2/3, and an individual blob tends to carry **one** opponency type — red/green or
  blue/yellow, not both (Ts'o & Gilbert 1988; Lu & Roe 2008). **Note on the historical view:** the
  modular account in which color was handled outside V1 and only "properly" at V4 is superseded;
  V1's role in color is far larger than it appeared in the 1980s, and color and form are not
  separable streams in cortex (Shapley & Hawken 2011).
- **Inputs:**
  *The geniculate drive is **three edges, not one**: the three channel classes terminate on
  three different sub-elements, and only two of the three reach layer 4 at all. Together they are a
  **minority** of V1's excitatory synapses — most V1 excitatory input is intracortical. None of the
  three carries orientation, binocular disparity, or spatial-frequency tuning; all three are built
  here. (Class 3 — general anatomy; web search; Webvision; Stanford *Foundations of Vision*, ch. 6.
  Not yet verified for the source.)*
  - **← lateral geniculate nucleus, magnocellular layers 1–2**, onto **4Cα**, point-to-point retinotopic — **carries:**
    the achromatic channel, fast-transient, ON and OFF, still monocular. **Fan-in:** unknown.
    **Fan-out** at the lateral geniculate nucleus end: unknown.
  - **← lateral geniculate nucleus, parvocellular layers 3–6**, onto **4Cβ**, point-to-point retinotopic — **carries:**
    the red–green (long-wavelength versus medium-wavelength) channel, sustained, ON and OFF, still
    monocular. **Fan-in:** unknown.
  - **← lateral geniculate nucleus, koniocellular sublayers**, onto the **cytochrome-oxidase blobs of layers 2/3** and onto **layer 1** —
    **carries:** the blue–yellow (short-wavelength versus long-plus-medium-wavelength) channel,
    still monocular. The blob termination is
    reported specifically in layer 3; the blobs themselves span layers 2 and 3. **This edge does not
    terminate in layer 4 at all**: the koniocellular class bypasses the granular layer and arrives
    directly in the supragranular
    tier and in layer 1. **This is the edge V1's blue–yellow cells read.** **Fan-in:** unknown.
  - **← lateral geniculate nucleus, parvocellular and koniocellular collaterals**, onto **4A** — **carries:** a
    collateral copy of the same two channels; 4A is proposed as a site where the magnocellular,
    parvocellular and koniocellular
    streams are recombined. **Payload beyond that — owed.** **Fan-in:** unknown.
  - **← V2, V3, V4 and the middle temporal area** (cortical feedback), principally onto **layer 1**, and also onto
    layers 2, 5 and 6 — **carries:** contextual and attentional modulation — figure–ground and
    border-ownership context, attentional gain; not a new stimulus code. **Payload otherwise
    unknown — owed.** Descending input **avoids layer 4**, which is what distinguishes a feedback
    edge from a forward one at the receiving end. On layer 1 it terminates on apical tufts belonging
    to cells housed in layers 2/3 and 5 (see Internal structure), and mainly on **spines** — 84% and
    77% for the two axons reconstructed. The **originating** layers are reported as **3A and 6**;
    a separate line of work places a supragranular feedback origin specifically in **layer 2**, and
    the two are not obviously the same claim. **Fan-in:** unknown. *(Class 1 — Kennedy/Bullier
    lineage, macaque; PMC6665918.
    Not yet verified for the source.)*
  - **← the posterior inferotemporal cortex (area TEO), the anterior inferotemporal cortex, temporal area TF, temporal area TH, occipitotemporal and superior temporal sulcal cortex, and caudal
    intraparietal cortex** (long-range feedback) — **carries:** payload **owed**. Cortical afferents
    to V1 are **not confined to the prestriate areas**, which is the general assumption; anterograde
    injection in anterior occipital and temporal areas consistently produces labelled terminals in
    V1. **Fan-in:** unknown. *(Class 1 — PubMed 8075534, macaque. Not yet
    verified for the source.)*
- **Outputs:** the forward output to V2 is **segregated by content**, but **how many streams it
  divides into is contested, and the laminar composition of each is measured and is not what the
  simple account says**. Three groupings are in the literature: **three** streams (blobs → thin,
  interblobs → pale, 4B → thick; Livingstone & Hubel 1984; Livingstone & Hubel 1987; Livingstone &
  Hubel 1988); **two** (patches → thin,
  interpatches → pale *and* thick, on the finding that pale and thick take common input; Sincich &
  Horton 2002a; Sincich & Horton 2005); and **four** (blob columns → thin, blob/interblob **border**
  columns →
  thick, interblob centres → one pale stripe, layer 2/3–4A interblobs → the other pale stripe, on
  the finding that the two pale stripes of a cycle are anatomically distinct; Federer et al. 2009;
  Federer et al. 2013). The edges below are stated by **target stripe class**, which is the axis all
  three
  groupings agree on, with the measured laminar composition on each. *(Class 1 — macaque; Sincich &
  Horton 2010. Not yet verified for the source.)*
  - **→ V2 thin stripes**, predominantly from the **cytochrome-oxidase blobs of layers 2/3** — **carries:** the
    cortical colour signal, single- and double-opponent, red/green and blue/yellow, retinotopic.
    **This is the edge V2's hue is computed from.** ~81% of the labelled source cells lie in
    patches, with sparse additional contribution from 4A, 4B and 5/6. **Contested:** one report
    found patches and interpatches projecting equally to thin stripes, which would break the
    blob-to-colour correspondence; the 81% count was made to test that and did not reproduce it.
    **Fan-out:** unknown.
  - **→ V2 pale stripes** — **carries:** oriented edges, contour, spatial frequency — form without
    hue. Pale stripes take **the richest projection from V1** of the three. Measured composition:
    **layer 2/3 87%, 4B 10%, 4A 2%, layers 5/6 2%**, concentrated in interpatches. **Fan-out:**
    unknown.
  - **→ V2 thick stripes** — **carries:** direction of motion and binocular disparity, achromatic,
    coarse-spatial. Measured composition: **layer 2/3 67%, 4B 23%, 4A 7%, layers 5/6 2%**,
    concentrated in interpatches except in 5/6, with the interpatch bias stronger in layer 2/3
    (84%) than in 4B (75%). The 4B cells projecting to V2 are about **80% pyramidal**, the class
    that receives both stream types (see Internal structure). **The simple statement that thick
    stripes come from 4B understates layer 2/3 and overstates 4B: 4B is the minority contributor at
    23%.** 4B's share is
    nonetheless higher here than at the pale stripes, which is consistent with thick-stripe cells'
    motion and disparity selectivity. **Fan-out:** unknown.
  - **→ the middle temporal area (V5) directly**, from **4B, predominantly its spiny-stellate class** — **carries:**
    direction of motion and binocular disparity, achromatic, coarse-spatial; the fast few-hop route
    to the motion integrator. Of the 4B cells labelled from the middle temporal area, about **76%**
    are spiny stellate
    (range 67–93%) and 24% pyramidal — the reverse of the V2-projecting population, which is about
    **80% pyramidal**. The two populations are **largely separate cells**: dual-tracer injection
    into V2 and the middle temporal area labelled two large intermingled but single-labelled groups
    within 4B, with fewer
    than about 5% double-labelled ("manifold") neurons projecting to both. the middle temporal
    area-projecting cells are
    distributed **indiscriminately with respect to the cytochrome-oxidase compartment** in 4B.
    **Fan-out:** unknown.
    *(Class 1 — Sincich & Horton 2003; Nassi & Callaway 2007; macaque. Not yet
    verified for the source.)*
  - **→ V4**, direct — **carries:** payload **owed**. A **sparse** projection, and
    **restricted to roughly the central 6° of the visual field**; the principal V1-to-V4 route is
    through V2. **Fan-out:** unknown. *(Class 1 — Yukie &
    Iwai 1985, rhesus; as reported in PMC8000025. Not yet verified for the source.)*
  - **→ V3**, from **4B** — **carries:** direction of motion and disparity, achromatic; a **major**
    input, and one of the three routes by which 4B's product reaches the motion areas — directly to
    the middle temporal area, through V2's thick stripes, and through V3. Note the asymmetry: **V3
    has a V1 connection and the ventral posterior area does
    not**, so the two cannot be
    treated as one target. **Fan-out:** unknown. *(Class 1 — Felleman, Burkhalter & Van Essen 1997,
    macaque. Not yet verified for the source.)*
  - **→ V2, from layers 5/6** — **carries:** payload **owed**. A small component (~2% of the
    source cells for both pale and thick stripes) that the three-stream account omits entirely, and
    which is **not** concentrated in interpatches the way the layer 2/3 and 4B components are.
    **Fan-out:** unknown.
  - **→ V2, from 4A** — **carries:** payload **owed**. 7% of thick-stripe input, 2% of pale.
    **Fan-out:** unknown.
    **Contested, recorded not smoothed:** the textbook reading of this edge is
    *magnocellular-driven*, and direct measurement of local input to individual 4B neurons does not
    support it as an exclusive claim — most 4B cells receive
    strong input from both the magnocellular- and parvocellular-recipient sublaminae (Yabuta &
    Callaway 1996, macaque). 4B additionally holds two output cell classes,
    pyramids carrying both stream types and spiny stellates, with the middle temporal area drawing
    roughly 80% of its
    4B input from spiny stellates. *(**Candidate — not yet verified for the source.**)*
  - **→ lateral geniculate nucleus** (corticothalamic feedback from **6a**) — **carries:** no visual content; the
    modulatory signal that gates the relay feeding V1 (see the lateral geniculate nucleus entry).
    The originating
    sub-element is the upper sublayer of layer 6, whose axons reach the first-order relay and the
    thalamic reticular nucleus with rod-like modulatory terminals; the lower sublayer's axons reach
    higher-order thalamic regions instead. *(Class 1 — PMC6131091; PMC2885865. Not yet verified for
    the source.)* **Fan-out:**
    unknown.
  - **→ higher-order thalamus**, from **6b** — **carries:** payload **owed**. Distinct from both
    the 6a and the layer-5 thalamic projections: 6b reaches higher-order nuclei but **not** the
    reticular nucleus, and its terminal varicosities are markedly smaller and simpler than layer
    5's. *(Class 1 — PMC6018949, mouse.
    Not yet verified for the source.)* **Fan-out:** unknown.
  - **→ superior colliculus**, from **5b** — **carries:** retinotopic salience for orienting.
    **Payload otherwise unknown — owed.** The layer assignment is the subcortically-projecting
    sublayer of layer 5; the source describing the projection does not itself sublaminate it.
    *(Class 2 — the projection is Class 1 general anatomy, the sublayer assignment is a reading
    placed on it here. Not yet verified for the source.)* **Fan-out:** unknown.
  - **→ lower visual areas** (descending), from **layer 2** — **carries:** payload **owed**. A
    supragranular feedback stream arises in layer 2 in every extrastriate visual area examined,
    alongside the classical infragranular feedback, so **layers 2 and 3 are not interchangeable**
    as origins. *(Class 1 — Markov et al. 2014, macaque, as reported in PMC8244994. Not yet verified
    for the source.)* **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(From web search. No full
  paper was opened — abstracts and search excerpts only. Species noted per line and largely
  non-human. **Nothing in this block is yet verified for the source.**)*

  **Sub-elements.** V1 is the most finely divided area of cortex, and its divisions are not the
  general cortical ones. Eleven are named here: **1, 2, 3, 4A, 4B, 4Cα, 4Cβ, 5a, 5b, 6a, 6b**.
  Layer 4's four sublaminae **merge into a single layer 4 in V2** and in cortex generally, so this
  division is V1's alone; general cortex divides only 5 and 6, giving eight. *(Class 3 — PMC4360995;
  ScienceDirect striate-cortex overview.)* Primate V1 is reported to
  carry further unique subdivisions of layer 3 beyond these eleven; they are not enumerated here.
  *(Class 1 — PMC11048015, comparative human/non-human-primate/rodent.)*

  **4B's classification is disputed and is recorded as disputed.** The name in common use is 4B,
  and it is kept. A well-supported reading holds that only the sublamina below the myelinated band
  — 4C in Brodmann's terms — is layer 4 in anthropoid primates, and that 4A and 4B belong to
  **layer 3**; one recent source states plainly that the band is a subdivision of layer 3 despite
  the traditional name. The edges below carry the function either way: 4B receives no geniculate
  drive and originates outward projections, which is what an output sub-element does whatever it is
  numbered. *(Class 1 — PMC4360995, human/chimpanzee/macaque; the Hässler lineage across 16 primate
  species.)*

  **A dangling requirement: eye of origin.** This entry's Function field asserts binocular
  convergence, ocular-dominance columns, and binocular disparity — all three of which **consume
  the eye each signal came from**. The chiasm entry now declares eye of origin as part of its
  payload, and the geniculate keeps the two eyes in separate layers. But the four geniculate input
  edges above describe their payload only as "still monocular" — they do not say **which** eye, and
  no edge anywhere in this line does. A property that is structurally load-bearing at this stage is
  therefore consumed here and declared on no incoming edge. **Owed: carry eye of origin as a named
  payload component on every edge from the chiasm to this stage's layer 4, and state where it is
  discarded** — which is here, and which is what "binocular convergence" means.

  **Layer 1 is a place whose receiving membrane belongs elsewhere.** It is the only cortical layer
  without excitatory cell bodies. **Resident population:** four distinct GABAergic interneuron
  types, each with its own molecular profile, morphology and electrophysiology. **Owners of the
  receiving membrane:** the apical tuft dendrites of pyramidal cells whose somata sit in layers 2/3
  and 5 — so an edge terminating here reaches a population housed in another sub-element, by
  propagation within one cell and not by a second synapse. It is also a **transport layer**,
  carrying long-range cortico-cortical axons, higher-order thalamic axons, and a basal-forebrain
  cholinergic projection that is specifically enriched in it; in human prefrontal cortex the
  density of its myelinated axons rises from childhood to adulthood. *(Class 1 — Schuman et al.
  2019, mouse; Neuron layer-1 review 2023; PMC6417186, human lateral prefrontal cortex. Human and
  mouse
  layer-1 interneuron repertoires diverge, with human types having no mouse counterpart — bioRxiv
  2022.10.24.511199.)*

  Roughly 20% of the neurons in layers 2–6 are inhibitory interneurons that do not project outside
  the area. *(Class 3 — Webvision.)*

  **Internal edges:**
  - **4Cα → 4B** — **carries:** the achromatic channel toward its outward projections.
    **Fan-in:** unknown. **Fan-out:** unknown. *(Class 3 — textbook route, Lund 1988 lineage.)*
  - **4Cα and the parvocellular-recipient sublaminae → 4B — converging, but only onto one of 4B's
    two cell classes.** Direct measurement of local functional input to individual 4B neurons, by
    intracellular recording with laser-scanning photostimulation, found most 4B cells receiving
    strong input from both stream classes. **The later cell-class account resolves how**, and it
    resolves the apparent conflict with the textbook single-stream reading:
    - **4B spiny stellates receive magnocellular input only**, from 4Cα directly. These are the
      cells that project to the middle temporal area.
    - **4B pyramids receive both**: magnocellular from 4Cα directly, **and** parvocellular by a
      route that does not terminate in 4B at all — 4Cβ projects to **layer 3**, where it contacts
      the **apical dendrites of the 4B pyramids**. These are the cells that project to V2.

    So the convergence is real, is confined to one cell class, and part of it happens on membrane
    that lies **outside the sub-element the cell belongs to** — the same owner/place distinction the
    slot records for layer 1, here in the other direction. **Consequence: the direct route to the
    motion integrator is magnocellular, and the route through V2 is mixed.** **Fan-in:** unknown.
    **Fan-out:** unknown. *(Class 1 — Yabuta & Callaway 1996; Yabuta et al. 2001;
    Nassi & Callaway 2007; macaque, as reported in Cerebral Cortex 30:3483, 2020.)*
  - **4Cβ → 4A** — **carries:** the red–green channel into the recombination sublamina.
    **Fan-in:** unknown. **Fan-out:** unknown. *(Class 3 — textbook route.)*
  - **4B → 4A** — **carries:** payload **owed**. 4A is described as receiving projections from 4B
    as well as collaterals from the parvocellular and koniocellular classes, which makes it a
    convergence point rather than
    a step on one lane. **Fan-in:** unknown. **Fan-out:** unknown. *(Class 3 — Webvision lineage.)*
  - **4A → the cytochrome-oxidase blobs and interblobs of layers 2/3** — **carries:** the chromatic and form signals
    into the supragranular tier; this is the route the blob and interblob output edges depend on.
    **Fan-in:** unknown. **Fan-out:** unknown. *(Class 3 — textbook route.)*
  - **4C → layer 3, and to layers 5 and 6** — **carries:** payload **owed**. Layer 4 cells are
    described as projecting principally to layer 3 and also to layers 5 and 6. **Fan-in:** unknown.
    **Fan-out:** unknown. *(Class 3 — Webvision lineage.)*
  - **layers 2/3 → 5a and 5b** — **carries:** the supragranular product into the deep output tier.
    Reported as the strongest single interlaminar connection in quantitative circuit
    reconstruction, about one third of the local circuit's total synaptic current, with the
    reciprocal **5a → 2/3** connection second. **Fan-in:** unknown. **Fan-out:** unknown.
    *(Class 1 — Binzegger, Douglas & Martin 2004, cat V1, as reported in the review at PMC3777738.
    The primary paper was not opened.)*
  - **6a → 4, and 6a → 5a** — **carries:** modulation, no new stimulus content, and the two
    effects have **opposite sign** — activating layer 6 corticothalamic cells suppressed layer 4
    while driving spikes in 5a pyramidal cells, whose axons ramify densely there. The
    corticothalamic cells of layer 6 branch **intracortically as well as back to the relay**, so
    they act at both ends of the thalamocortical link. **Fan-in:** unknown. **Fan-out:** unknown.
    *(Class 1 — Kim et al. 2014, mouse visual and somatosensory cortex; PMC6131091; Ahmed et al.
    1994 for the layer-4 synapse counts.)*
  - **6b → 6a, and 6b → layers 5 and 6 generally** — **carries:** a local excitatory recruitment,
    **gated by arousal state**: 6b excitatory neurons carry an orexin receptor found almost
    exclusively in them, and the proposal is that they recruit 6a so that thalamocortical signalling
    there becomes more reliable when the system is aroused. This is the one internal edge in this
    entry whose payload is a **state**, not a stimulus signal. **Fan-in:** unknown. **Fan-out:**
    unknown. *(Class 1 — Frontiers in Neuroanatomy 12:1, 2018, citing Clancy & Cauller 1999, Marx
    & Feldmeyer 2013, Hay et al. 2015; rodent.)*
  - **6b → layer 1** — **carries:** payload **owed**. **Fan-in:** unknown. **Fan-out:** unknown.
    *(Class 1 — Neuron layer-1 review 2023.)*
  - **within-sub-element recurrence, 4C and layers 2/3** — **carries:** amplification of a
    numerically minor afferent drive. This is the actual claim of the canonical-microcircuit
    proposal, which is a theory about within-layer amplification rather than a wiring diagram.
    Recurrent connectivity is highest in layers 2/3. **Fan-in:** unknown. **Fan-out:** unknown.
    *(Class 1 — Douglas, Martin & Whitteridge 1989; Douglas & Martin 1991; Douglas & Martin 2004; cat V1.)*
  - **descending and thalamic arrival on layer 1** — **carries:** contextual and attentional
    modulation onto the apical tufts, meeting feedforward drive arriving at the somata in other
    sub-elements. Thalamic input to layer 1 is dense and highly convergent rather than sparse.
    **Fan-in:** unknown. **Fan-out:** unknown. *(Class 1 — Rubio-Garrido et al. 2009, rat, ~4,500
    layer-1-projecting thalamocortical neurons per mm². The coincidence
    reading, Larkum 2013, is **Class 2** as applied here.)*

  **Constraint on the routing above, not itself an edge: layer 4 is not an obligatory distribution
  hub.** Sensory-evoked responses in layers 5/6 arise from direct thalamocortical synapses at the
  same latency as layer 4, with substantial thalamic convergence onto 5b; pharmacological
  inactivation of layer 4 left synaptic input to layers 5/6 unchanged. The thalamus drives an upper
  stratum (4 and 2/3) and a lower stratum (5/6) **in parallel**. If that holds in primate V1, this
  entry's Inputs are incomplete — there would be a direct geniculate edge onto 5b that is not
  recorded above. *(Class 1 — Constantinople & Bruno 2013; **rat somatosensory
  cortex**. Whether it generalises to primate V1 is not established, and the missing edge is not
  written on the strength of a different area in a different species.)*

  **Sub-element counts:** unknown. Human V1 laminar density — neuronal and non-neuronal, layer by
  layer — is reported at an overall ~79,000 neurons/mm³, about 35% of macaque V1's density, with
  laminar proportions similar between the two species. That is the datum a per-sub-element count
  would come from; **the abstract is what was opened, and no per-layer figure is carried here.**
  *(Class 1 — Cerebral Cortex 34:2, bhad512, 2024, human.)*
- **Neurons:** **~280–310M per hemisphere** (from the
  density × confirmed-volume product). The older **~140M** (Wandell's lateral geniculate
  nucleus-ratio figure;
  Leuba & Kraftsik 1994; Stanford *Foundations of Vision*, ~1.5×10⁸) is retained as a
  **lower bound**: human V1 density ~60,000/mm³ (Pakkenberg & Gundersen) × the confirmed
  ~5.2 cm³ volume (Andrews, Halpern & Purves 1997) ≈ ~300M, and modern isotropic-fractionator counts
  in primate V1 run higher still (macaque ~416M, chimp ~675M; Herculano-Houzel lineage).
  Headline set to the density × volume value; the count remains method-dependent
  (older stereology-via-lateral geniculate nucleus-ratio low, fractionator high).
- **Synapses:** no direct human V1 count. Two anchors now bound it. **(1) Primate V1
  (macaque area 17):** ~2,300–5,600 synapses/neuron (O'Kusky & Colonnier 1982 low end;
  Cragg 1967 high end); density ~2.8–8.3×10⁸/mm³. **(2) Human neocortex (temporal lobe,
  direct electron microscopy):** density ~9.13×10⁸/mm³ (Alonso-Nanclares et al. 2008) — same order
  as the primate V1 figure, so it **corroborates it with a
  human number**; DeFelipe's cortical average is ~7,000 synapses/neuron (range
  1,000–10,000). Cross-primate synapse density is near-invariant (Sherwood et al. 2020).
  Human-anchored total ≈ 9.13×10⁸/mm³ × ~5.2 cm³ ≈ **~4.7×10¹² synapses/hemisphere** —
  provisional: the density-based per-neuron figure (~15,000, = synapse density ÷ neuron
  density) sits above both the primate V1 indegree (2,300–5,600) and DeFelipe's cortical
  average (~7,000). That gap is genuine and unexplained — V1's high neuron packing should
  pull synapses/neuron *down*, not up — so per-neuron for V1 stays open even though the
  density and total are now human-anchored.
- **Axons:** unknown.
- **Grey-matter volume:** V1 surface area ~26 cm²/hemisphere, thickness ~0.2 cm →
  ~5.2 cm³/hemisphere (from neuronal-density literature). Neuron density ~60,000
  neurons/mm³ (Pakkenberg & Gundersen) — the highest in cortex; V1 is the density
  outlier (~2.5× other areas).
- **White-matter volume:** unknown. **Myelination:** the stria of Gennari — the dense
  myelinated band **at 4B**, formed by axons running from 4Cα — defines striate cortex, and is
  what "striate" names; quantitative g-ratio unknown. It is visible to the naked eye in unstained
  primate section. *(Class 3 — Scholarpedia, Area V1.)*
- **Internal-consistency flag (resolved).** The volume was **not** the culprit — Andrews,
  Halpern & Purves 1997 measure human V1 at ~5.1–5.7 cm³/hemisphere (mean), confirming
  the ~5.2 cm³ here. The tension was **count vs density**, and the count was the soft term:
  ~60,000/mm³ × 5.2 cm³ ≈ 312M, versus the old ~140M (which would have implied
  ~27,000/mm³, contradicting the measured density). Resolved by revising the headline to
  the density × volume value (~280–310M), with ~140M kept as the lower bound. Residual open
  item: synapses/neuron (see Synapses).

## V2 — secondary visual cortex (ventral stream, isocortex)

- **Function:** first real composition of visual features — contour integration
  and illusory contours, angle/junction selectivity, border-ownership /
  figure–ground, naturalistic texture (distinguishes natural texture from
  spectrum-matched noise, which V1 cannot), hue. The three stripe classes carry
  different content onward: thin (hue) and pale (form) to the ventral route, thick
  (motion/disparity) to the dorsal route.
- **Inputs:**
  *Each forward edge from V1 terminates in **layer 4**, in patchy terminal fields, with weaker
  label extending into the other layers. **The terminal fields are not in register with the
  cytochrome-oxidase
  stripes**: the darkest cytochrome-oxidase staining is in layer 3 and does not coincide with the
  densest band of
  V1 input to layer 4. So "layer 4 of the thin stripes" is **not** a safe way to name a target —
  the tangential compartment defined by cytochrome-oxidase and the tangential compartment defined by
  input are
  offset, and the stripe classes below name the cytochrome-oxidase one. (Class 1 — Sincich & Horton
  2002b, macaque, anterograde [3H]proline. Not yet verified for the source.) The measured laminar
  composition of each edge is recorded at the V1 end.*
  - **← auditory parabelt, caudal division** (on the caudally-directed stream) — **carries:**
    payload **owed** — sound-source location and motion, in whatever form survives the trip.
    **This edge was absent from the entry and it runs the wrong way for this file's usual
    assumptions**: an auditory association area writing into secondary visual cortex, rather than
    vision feeding a multimodal stage. **Which tangential compartment it reaches — thin, thick or
    pale — is not recorded**, and the answer would say a great deal, since the thick stripes are
    the motion and disparity channel and an auditory motion signal arriving there would be
    functionally pointed. **Owed.** **Fan-in:** unknown. *(Class 1 for the projection's existence —
    PMC4001064, 2014, macaque; the terminal compartment was not established. Not
    yet verified for the source.)*
  - **← V1, predominantly the cytochrome-oxidase blobs of layers 2/3**, into the **thin stripes** — **carries:**
    the cortical color signal (single- and double-opponent, red/green and blue/yellow),
    retinotopic. **This is the edge V2's hue is computed from.** **Fan-in:** unknown.
  - **← V1, predominantly the inter-blob regions of layers 2/3, with a 4B component**, into the
    **pale stripes** — **carries:** oriented edges, contour, spatial frequency. The richest of the
    three V1 projections. **Fan-in:** unknown.
  - **← V1, layers 2/3 and 4B**, into the **thick stripes** — **carries:** direction of motion and
    binocular disparity, achromatic. **Fan-in:** unknown.
  - **← V1, 4A and layers 5/6**, into the pale and thick stripes — **carries:** payload **owed**.
    Minor components the three-stream account omits. **Fan-in:** unknown.
  - **← V4, the middle temporal area and higher areas** (cortical feedback), principally onto **layer 1** — **carries:**
    payload **owed**; descending input avoids layer 4. **Fan-in:** unknown. *(Class 3 — general
    anatomy. Not yet verified for the source.)*
- **Outputs:**
  *Forward edges leave from **layers 2/3** of the named stripe class; the descending edge leaves
  from layer 2 and the infragranular layers. Same basis as the Inputs note above — the general
  cortical pattern, not a V2 measurement. (Class 3, except the layer-2 descending origin, which is
  Class 1 — Markov et al. 2014, macaque. Not yet verified for the source.)*
  - **→ the posterior inferotemporal cortex**, direct — **carries:** payload **owed**. A **jumping
    projection** that skips V4 — the step-by-step chain V1 → V2 → V4 → the inferotemporal cortex is
    the numerically
    dominant route but not the only one, and V2 reaches the posterior division of the inferotemporal
    cortex without a V4
    relay. **Fan-out:** unknown. *(Class 1 — Nakamura et al. 1993, macaque. Not yet verified for the
    source.)*
  - **→ V4** (ventral), from **layers 2/3 of the thin and pale stripes** — **carries:** hue,
    contour and illusory contour, angle and junction, border-ownership / figure–ground assignment,
    naturalistic texture — retinotopic, receptive fields larger than V1's. **Fan-out:** unknown.
  - **→ V3 / V3A** (the intermediate tier), from **layers 2/3** — **carries:** contour and dynamic
    form with early motion. **Payload otherwise unknown — owed.** **Fan-out:** unknown.
  - **→ the middle temporal area (V5)** (dorsal), from **layers 2/3 of the thick stripes** — **carries:** motion direction
    and disparity, achromatic. **Fan-out:** unknown.
  - **→ V1** (feedback), from **layer 2 and the infragranular layers**, onto V1's layer 1 —
    **carries:** figure–ground and border-ownership context; not a new stimulus code. **Payload
    otherwise unknown — owed.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.** Read the provenance marks closely: almost nothing in this block is a
  measurement made in V2.)*

  **Two axes of sub-element, and they are orthogonal.** V2 divides **tangentially** into three
  cytochrome-oxidase stripe classes — **thin, pale, thick** — and **laminarly** into layers. The
  stripes are the same kind of division as V1's blobs and interblobs: a tangential partition of the
  sheet, not a layer. Every stripe class has the full set of layers, and every layer runs through
  all three stripe classes.

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**. **Layer 4 is undivided here.**
  V1's four sublaminae merge into a single layer 4 in V2, which is the boundary at which V1's
  eleven-fold division stops being the cortical pattern and eight becomes it. *(Class 3 —
  PMC4360995: Brodmann's three sublayers of V1 layer 4 merge to form a single layer
  4 in V2.)*

  **Tangential sub-elements: three** — thin, pale, thick stripes, each taking a different V1 origin
  and sending to a different target, as the Inputs and Outputs above record.

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made in V2. Recorded so that the routing is stated somewhere rather than assumed,
  and marked so that no one mistakes them for V2 data.)*
  - **4 → 2/3** — **carries:** the arriving forward signal into the output tier. **Fan-in:**
    unknown. **Fan-out:** unknown.
  - **2/3 → 5a and 5b**, with the reciprocal **5a → 2/3** — **carries:** the supragranular product
    into the deep output tier. **Fan-in:** unknown. **Fan-out:** unknown.
  - **6a → 4, and 6a → 5a** — **carries:** modulation, no new stimulus content, opposite signs on
    the two targets. **Fan-in:** unknown. **Fan-out:** unknown.
  - **6b → 6a** — **carries:** an arousal-gated local recruitment. **Fan-in:** unknown.
    **Fan-out:** unknown.
  - **within-sub-element recurrence, layer 4 and layers 2/3** — **carries:** amplification of a
    numerically minor afferent drive. **Fan-in:** unknown. **Fan-out:** unknown.

  **Internal edges — tangential: the connections exist, and they cross stripe classes.** Intrinsic
  horizontal connections in V2 are a dense network of horizontally projecting fibres organised in
  columnar patches, each patch about 211 μm wide by 342 μm long, with the labelling from a single
  injection extending **4–5 mm** across the surface. **Axonal patches were found in all three
  stripe compartments**, and injections straddling a thick/pale border projected across it. Since
  the stripe cycle repeats about every 3.5–4 mm centre-to-centre, a 4–5 mm horizontal spread
  necessarily reaches beyond the injected stripe and into its neighbours. Independently, the study
  of V2's intrinsic connections that examined this directly reports **evidence for interaction
  between the different functional streams** — that is its finding, not an incidental observation.
  Functional organisation crosses the boundary too: orientation domains in V2 **ignore the border
  between thick and pale stripes**. **Payload: owed** — that the edges exist is established here;
  what they carry is not. **Fan-in:** unknown. **Fan-out:** unknown. *(Class 1 — Malach, Tootell &
  Malonek 1994, squirrel monkey; Levitt, Yoshioka & Lund 1994, macaque. Not yet verified for the
  source.)*

  V2's headline function is composition, and contour bound to hue would have to cross stripe classes
  somewhere. **The
  substrate for that crossing is present inside V2.** It is not necessary to push the binding
  downstream.

  **How the two axes interact: the stripes are full-thickness columns, but they are not in register
  with the input.** The stripes are columns in the broad sense — a regular repeating variation in
  function **spanning most or all of the cortical layers**, throughout V2. *(Class 1 — J Neurosci
  36:1841, 2016, human and non-human primate.)*

  **But the tangential compartment is defined differently at different depths, and the two
  definitions are offset.** The darkest cytochrome-oxidase staining — which is what names a stripe —
  appears in
  **layer 3**, while the densest patchy terminal field from V1 is in **layer 4**, and the two **do
  not coincide**. *(Class 1 — Sincich & Horton 2002b, macaque.)* So a phrase like
  "layer 4 of the thin stripe" picks out a place that is not well defined: it names a laminar
  position by a tangential compartment identified at a different depth. **The relationship between the
  cytochrome-oxidase
  compartment and the input compartment through the cortical depth is unknown**, and it is the
  thing that would have to be pinned down before a stripe can be treated as a single addressable
  unit.

  **Also unresolved: how many tangential compartments there are.** The pale stripes may be two
  distinct compartments rather than one — in a stripe cycle the two pale stripes differ in the
  laminar origin of the V1 projection they receive, anatomically in macaque and marmoset. If that
  holds, V2's tangential axis has **four** classes, not three. *(Class 1 — Federer et al. 2013;
  Federer et al. 2009.)*
- **Neurons:** **~200–220M per hemisphere** (scaled from the V1 count).
  V2 ≈ 0.715 × V1 by its own derivation — ~0.55× V1 neuron density but ~1.3× V1 cortical
  area — so ~300M × 1.3 × 0.55 ≈ 214M. Band scales proportionally (~160–245M). At V1's 140M
  lower bound, V2 ≈ 100M correspondingly.
- **Consistency check (resolved).** V2 scales with V1; the ratio V2 ≈ 0.715 × V1 holds,
  and V2 < V1 (the ventral-hierarchy shrink) is preserved (~200–220M < ~280–310M).
- **Synapses:** unknown. **Axons:** unknown.
- **Grey-matter volume:** unknown (larger surface area than V1; specific figure
  not recorded). **White-matter volume:** unknown. **Myelination:** unknown.

## V3 / V3A — early extrastriate (intermediate tier, dorsal-leaning; isocortex)

- **Function:** the tier just above V2, feeding the transition into the dorsal stream. **V3** (with its
  ventral counterpart the ventral posterior area) is retinotopic and combines contour / **dynamic
  form** with early motion —
  roughly half of macaque V3 neurons are direction-selective (Felleman & Van Essen 1987) — so it sits
  between V2's contour processing and the middle temporal area's motion. **V3A**, a distinct area
  between V3 and V4 (Van Essen
  & Zeki 1978; Zeki 1978), is strongly **motion-responsive in humans** and carries a full contralateral
  hemifield map (unlike V3's quarter-field) (Tootell et al. 1997); nearby lie V3B / V7
  (intraparietal sulcus area 0) and the
  kinetic-occipital region. Its stream assignment is genuinely
  debated — dorsal-leaning and
  motion-driven in humans, with weaker motion responses in macaque.
- **Inputs:**
  - **← V2, from layers 2/3** — **carries:** contour, junction, and figure–ground assignment;
    retinotopic. **Fan-in:** unknown.
  - **← V1, 4B** — **carries:** direction of motion and disparity, achromatic. A **major** input,
    and the basis for V3's association with the magnocellular-dominated stream. **Fan-in:** unknown.
    *(Class 1 — Felleman, Burkhalter & Van Essen 1997, macaque. Not yet
    verified for the source.)*
  - **← superior colliculus, di-synaptically** — **carries:** payload **owed**. A relay from the
    superior colliculus targets **V3 and the middle temporal area selectively** — a subcortical
    route into the motion
    areas that does not pass through V1. **Fan-in:** unknown. *(Class 1 — Lyon, Nassi & Callaway
    2010, as reported in PMC4900470. Not yet verified for the source.)*
  - **← higher dorsal and parietal areas** (feedback), principally onto **layer 1** — **carries:**
    payload **owed**. **Fan-in:** unknown. *(Class 3 — general anatomy.)*

  **V3 and the ventral posterior area are not the same target and this entry currently merges
  them.** Their connections
  differ in specific, recorded ways: **V3 connects with V1 and the V4 transitional area; the ventral
  posterior area does not.** **the ventral posterior area connects
  with the ventral occipitotemporal area, the dorsal prelunate area and the visually responsive part
  of temporal area F; V3 does not, or only rarely.** Both connect with V2, V3A, the posterior
  intraparietal area, V4, the middle temporal area, the dorsal medial superior temporal area
  and the ventral intraparietal area. Splitting them into separate entries is **owed**. *(Class 1 —
  Felleman, Burkhalter & Van
  Essen 1997, macaque.)*
- **Outputs:** *(forward edges leave from layers 2/3; the descending edges from layer 6 and the
  supragranular layers. Class 3 general pattern except where noted.)*
  - **→ the middle temporal area (V5)**, direct — **carries:** dynamic form — contour bound to direction of motion (roughly
    half of V3's neurons are direction-selective). One of the three routes carrying 4B's product to
    the motion integrator. **Fan-out:** unknown. *(Class 1 — Ungerleider & Desimone 1986, macaque.)*
  - **→ V3A / the dorsomedial area, the dorsal prelunate area, the ventral intraparietal area, the ventral lateral intraparietal area** (dorsal and posterior parietal) — **carries:** dynamic form, and
    in V3A a full contralateral hemifield map. **Payload otherwise unknown — owed.** **Fan-out:**
    unknown. *(Class 1 — Felleman, Burkhalter & Van Essen 1997.)*
  - **→ V4, the V4 transitional area, the visually responsive part of temporal area F, the ventral occipitotemporal area** (ventral and occipitotemporal — the tier where the two streams are still
    cross-linked) — **carries:** contour and dynamic form. **Payload otherwise unknown — owed.**
    the V4 transitional area is a V3 target and not the ventral posterior area target. **Fan-out:**
    unknown. *(Class 1 — Felleman, Burkhalter
    & Van Essen 1997.)*
  - **→ V1 / V2** (feedback), onto **layer 1** of the target — **payload unknown — owed.**
    **Fan-out:** unknown.
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, the general cortical set. Layer
  4 is undivided; the sublamination of V1's layer 4 stops at the V1/V2 border. *(Class 3.)*

  **Tangential sub-elements: unknown.** Whether V3 or V3A carries a repeating tangential
  compartmentalisation of the kind V1's patches and V2's stripes represent is not established here.
  Interdigitated colour- and disparity-selective columns **have** been reported
  in human V3 as well as V2, which would make V3's tangential axis real and analogous — but this is
  a single line of evidence and is not carried here as settled. *(Class 1 — J Neurosci 36:1841,
  2016, human. Recorded as a candidate, not as the region's organisation.)*

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made in V3 or V3A. Recorded so the routing is stated rather than assumed, and marked
  so no one mistakes them for V3 data.)*
  - **4 → 2/3**; **2/3 → 5a and 5b** with the reciprocal **5a → 2/3**; **6a → 4** and **6a → 5a**,
    opposite signs; **6b → 6a**, arousal-gated; **within-sub-element recurrence in 4 and 2/3**.
    **Fan-in:** unknown. **Fan-out:** unknown throughout.

  **One synaptic-composition figure is available for a related projection and is not V3's own:** the
  V2 → V3A projection forms about **76%** of its synapses on pyramidal dendritic spines, comparable
  to V1 → V2 in layer 4 (72%) and V2 → the middle temporal area (67%), and unlike V1 → the middle
  temporal area (54%, the difference attributed
  to large boutons making multiple somatic contacts). This is a property of the arriving axon, not of
  V3A's internal wiring, and is recorded here because it is the only quantitative figure carried
  anywhere in the file that touches V3A. *(Class 1 — Anderson & Martin 2005, as reported in
  PMC6665918; macaque.)*
- **Neurons:** soft / unknown — no clean human per-area count; retinotopically defined, with contested
  boundaries (V3 vs the ventral posterior area vs V3A vs V3B).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown. **White-matter volume:**
  unknown. **Myelination:** unknown.

## V4 — ventral visual area (ventral stream, isocortex)

- **Function:** intermediate-complexity vision — curvature and shape-part
  selectivity (the first explicit *part* code, above V2 junctions and below the inferotemporal cortex
  objects), color constancy / surface color (illuminant-discounted perceived
  color), texture/surface segmentation at larger scale, strong attentional gain.
  Receptive fields larger than V2, retinotopy coarser.
- **Inputs:**
  - **← V2** (thin and pale stripes) — **carries:** hue, contour and junction, border-ownership,
    texture; retinotopic. **V4's Function reads the hue on this edge** and combines it across
    space to discount the illuminant. **The projection is modular and only partly segregated**:
    a V4 injection labels V2 cells in thin stripes exclusively, *or* in interstripes exclusively,
    *or* in **specific combinations of the two**, in interdigitating non-overlapping clusters
    1–3 mm wide — and in some cases the two labelled fields are highly intermixed. So the thin and
    pale streams **converge in some V4 modules and stay separate in others**. This is the first
    place in the ventral chain where cross-stream convergence is demonstrated anatomically.
    **Fan-in:** unknown. *(Class 1 — Felleman, Xiao & McClendon 1997; Nakamura et al. 1993; macaque.
    Not yet verified for the
    source.)*
  - **← V3 / V3A** — **carries:** contour and dynamic form. **Payload otherwise unknown — owed.**
    **Fan-in:** unknown.
  - **← V1**, direct — **carries:** payload **owed**. **Sparse**, and restricted to roughly the
    **central 6°** of the visual field; the principal route from V1 is through V2. **Fan-in:**
    unknown. *(Class 1 — Yukie & Iwai 1985, rhesus. Not yet verified for the source.)*
  - **← frontal eye field**, terminating in **all cortical layers** — **carries:** the **spatial
    attentional gain signal** — an enhancement or suppression applied by location, not a stimulus
    code. The Function asserts strong attentional modulation, and this is the edge that supplies it.
    The frontal eye field is the one candidate shown to affect
    attentional
    modulation of firing rates in visual cortex *directly*; microstimulation or pharmacological
    activation of frontal eye field neurons enhances or suppresses V4 responses in the way
    allocating spatial
    attention does. The projection was tested for, and is consistent with, **preferential excitation
    of inhibitory neurons** in the target area. **Fan-in:** unknown. *(Class 1 — Anderson, Kennedy &
    Martin 2011, macaque; Moore & Armstrong 2003 lineage as
    reported in PNAS 121:e2304511121, 2024. Not yet verified for the source.)*
  - **← pulvinar** — **carries:** payload **owed** — a candidate is contextual and state-dependent
    modulation rather than a stimulus code. Pulvino-cortical projections are a major source of
    extrinsic input to the early visual areas, terminating in **layer 1 of V1 but densely in the
    middle layers of extrastriate areas** — so the pulvinar reaches V4 in the layers a *forward*
    edge would use, not the layer feedback uses. The pulvinar is reported to regulate transmission
    between cortical areas according to attentional demand. **Fan-in:** unknown. *(Class 1 —
    Rockland 2019, macaque; Saalmann et al. 2012. Not yet verified for the source.)*
  - **← the inferotemporal cortex and higher ventral areas** (feedback), principally onto **layer 1** — **carries:**
    payload **owed**. **Fan-in:** unknown. *(Class 3 — general anatomy.)*

  **Three sources of attentional influence, and they are not equivalent.** The frontal eye field,
  the lateral intraparietal area, the superior colliculus and the pulvinar are all implicated in
  attention; only the frontal eye field has been shown to modulate visual-cortical firing rates
  through its own
  direct projection. The others may act indirectly. Recorded so the entry does not collapse them
  into one edge.
- **Outputs:** *(forward edges leave from layers 2/3; descending edges from layer 6 and the
  supragranular layers. Class 3 general pattern except where noted.)*
  - **→ the inferotemporal cortex** (inferotemporal cortex), and to **posterior inferotemporal cortex** specifically —
    **carries:** intermediate shape — curvature and shape-part code, **surface color with the
    illuminant discounted** (perceived rather than retinal color), and segmented surfaces / texture
    at large scale; coarser retinotopy than V2. The colour-selective modules of V4 and of posterior
    inferotemporal cortex are treated in the literature as one population spanning both, sometimes
    called the V4 complex — so this edge runs **between two parts of one module system**, not
    between two unrelated stages. **Fan-out:** unknown.
  - **→ V2** (feedback), onto **layer 1** of the target — **payload unknown — owed.** The V4→V2
    projection targets mainly spines in layer 1, about 75% of its synapses. **Fan-out:** unknown.
    *(Class 1 — Anderson & Martin 2006, as reported in PMC6665918; macaque.)*
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.**)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, the general cortical set,
  layer 4 undivided. *(Class 3.)*

  **Tangential sub-elements: globs and interglobs — and they are defined differently from V1's and
  V2's.** V4 carries millimetre-sized colour-selective modules termed **globs**, with **interglobs**
  between them. They are the V4-stage member of a chain — blobs in V1, thin stripes in V2, globs in
  V4 — reported as a single modular architecture for colour that differs across areas **chiefly in
  scale**, the V2 and V4 domains being comparable to each other and much larger than V1's.

  **But cytochrome oxidase does not reveal them.** cytochrome-oxidase and the other stains **fail to
  yield reliable
  anatomical markers for modules beyond V1 and V2** — the histochemical signal for functionally
  distinct compartments vanishes at V4. V4's tangential sub-elements are therefore identified
  **functionally and connectionally** — by optical imaging, single-unit response, and the specific
  pattern of input each module receives — not by a stain. That is a different basis of definition
  from the one V1's patches and V2's stripes rest on, and it means the V2-entry problem of a
  compartment defined at one depth by a stain does not arise here in the same form; a different
  one does, since a module defined by its inputs is defined by the very edges the entry is trying to
  record. *(Class 1 — Felleman, Xiao & McClendon 1997; Conway et al. 2010; Neuron
  S0896-6273(20)30581-X, 2020; macaque.)*

  **Glob and interglob carry different content.** Glob cells' responses correlate more strongly with
  perceptual colour space, and hue can be read out from them at high accuracy invariant to
  luminance; interglob cells tend to prefer luminance contrast regardless of hue, and hue reads out
  only above chance. Glob cells retain hue tuning as luminance contrast is modulated. **Fan-in:**
  unknown. *(Class 1 — eNeuro 3(4):ENEURO.0039-16, 2016, macaque.)*

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made in V4.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout.

  **Internal edges — tangential: owed.** Whether globs and interglobs exchange signal, and what they
  would carry, is not established here. It matters for the same reason it
  mattered at V2: V4's function includes discounting the illuminant, which requires combining
  surface colour across space, and if that combination crosses module boundaries the edges are
  needed.
- **Neurons:** ~50M per hemisphere (best available estimate; genuine measurement
  uncertainty — hV4's boundary is itself contested). Ordering V4 < V2 holds
  (areas shrink up the ventral hierarchy).
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

## Inferotemporal cortex (ventral stream endpoint, isocortex)

- **Function:** top of the ventral "what" stream — invariant object and face
  identity, categorical representation invariant to nuisance transforms (position,
  size, pose, lighting). Two divisions in series: **the posterior inferotemporal cortex (area TEO) →
  the anterior inferotemporal cortex**, treated here as sub-elements of one entry (see Internal
  structure).
  Cells
  requiring complex features for maximal activation are already present in the posterior
  inferotemporal cortex and in V4, in small
  proportion — the complexity gradient is continuous rather than stepped. *(Class 1 — Kobatake &
  Tanaka 1994, macaque.)*
- **Inputs:**
  - **← V4**, onto the **posterior part of the anterior inferotemporal cortex** — **carries:** curvature and shape parts,
    illuminant-discounted surface color, segmented texture; coarse retinotopy. **Fan-in:** unknown.
    *(Class 1 — Saleem et al. 1992, macaque.)*
  - **← V2**, onto **the posterior inferotemporal cortex**, direct — **carries:** payload **owed**. A jumping projection
    bypassing V4, declared at the V2 end as well. **Fan-in:** unknown. *(Class 1 — Nakamura et al.
    1993, macaque. Not yet verified for the
    source.)*
  - **← perirhinal cortex, prefrontal cortex and amygdala** (feedback), principally onto **layer 1**
    — **carries:** payload **owed**. The forward edges to all three are recorded below; the return
    limbs are asserted here on the general reciprocity of cortico-cortical connections and are
    **Class 3**, not measured. **Fan-in:** unknown.
- **Outputs:**
  - **→ the distributed conceptual / semantic system** (via temporal pole) — **carries:** object
    and face **identity**, invariant to position, size, pose, and lighting. **This is where the
    payload stops being a signal and starts being a category**, and it is the first entry in the
    visual line whose payload cannot be written in units: "the identity of the thing," with no
    coordinate frame, is a phrase and not a type. Recorded as such rather than dressed up.
    **Fan-out:** unknown.
  - **→ medial temporal lobe / hippocampal formation** (episodic binding) — **carries:** the same
    identity code, as one element of an episode. **Fan-out:** unknown.
  - **→ prefrontal cortex** (ventrolateral) — **carries:** identity, for controlled retrieval and
    selection. **Fan-out:** unknown.
  - **→ amygdala** — **carries:** object / face identity for affective evaluation. **Fan-out:**
    unknown.
  - **→ perirhinal cortex (areas 35 and 36)** — **carries:** the identity code, into the
    medial-temporal memory system; this is the anatomical step by which the ventral stream's output
    reaches the hippocampal formation. **Fan-out:** unknown. *(Class 1 — Saleem & Tanaka
    lineage; Suzuki & Amaral 1994; macaque. Not yet verified for the source.)*
  - **→ striatum** (basal ganglia) — **carries:** payload **owed**. A subcortical target that puts the ventral stream's output into the action-selection
    loop rather than only into memory and evaluation. **Fan-out:** unknown. *(Class 1 — Iwai & Yukie
    1987; Saleem et al. 1993; macaque. Not yet verified for the source.)*
  - **→ the anterior intraparietal area**, from **the lower bank of the superior temporal sulcus and
    the middle temporal gyrus** — **carries:** object **identity** — the same categorical code the
    edges above carry, invariant to position, size, pose and lighting, delivered into the grasp
    channel. **Fan-out:** unknown.
    **This is the entry's only projection out of the ventral stream and into the parietal lobe.**
    The posterior parietal file's anterior intraparietal entry lists a ventral-stream input carrying
    object identity among its six afferents. Without this edge the file would describe a two-stream
    architecture with no edge between the streams above the early tiers. **What the
    receiving area does with
    it is the point:** visuomotor transformation for grasping there draws on **ventral**-stream
    object identity as well as **dorsal**-stream object geometry, which is the tracer study's own
    headline — direct anatomical connections with this cortex give that area a role linking the
    parieto-frontal grasping network to object recognition.
    **The origin sector is not one of this entry's two divisional sub-elements, and naming it is
    owed.** The projecting cells lie in the lower bank of the superior temporal sulcus and on the
    middle temporal gyrus — a **ventrolateral** sector of this cortex. This entry's Internal
    structure divides the region **posterior/anterior** (the posterior and anterior inferotemporal
    cortex, in series), which is a different axis, and the architectonic label for the ventrolateral
    sector is not established here. **Owed: name it, and state its relation to
    the posterior/anterior division — whether it is a part of one of them or a third sub-element on
    a second axis.**
    *(Class 1 — Borra et al. 2008, macaque. **The abstract is what was opened; the full paper was
    not.** Candidate — awaiting Micky's verification.)*

  **A second parietal edge is asserted against this entry and is *not* written, because no source
  for it was found.** The angular gyrus entry (file 6) declares an input from occipitotemporal
  cortex carrying object and face identity, and the same entry declares an output to "lateral
  temporal semantic cortex" which may or may not be this region. Neither is established here: the
  anterior-intraparietal projection has a source and the angular-gyrus one has none. **The two are
  recorded as separate problems in that file and are not repaired
  together here. Owed: settle whether an inferotemporal → angular gyrus edge exists.**

  **All of these projections are more numerous from the anterior inferotemporal cortex than from the
  earlier stages, and most numerous from the anterior inferotemporal cortex** — so the outward fan
  of the ventral
  stream is concentrated at its
  last sub-element, not spread evenly along it. *(Class 1 — Iwai & Yukie 1987; Ungerleider et al.
  1989; Cheng et al. 1993; Suzuki & Amaral 1994; macaque.)*
- **Internal structure and internal data flow:** *(**Nothing here is yet
  verified for the source.**)*

  **Divisional sub-elements: two in series** — **the posterior inferotemporal cortex (area TEO)**
  and **the anterior inferotemporal cortex**. **The architectonic label for the anterior division is
  owed:** the posterior division carries its literature label and the anterior one carries none.
  They are distinct areas with distinct connections and are held in one entry here only because the
  source treats the inferotemporal cortex as one region; **splitting
  them is owed**, on the
  same grounds V3 and the ventral posterior area are owed a split.

  **A third sub-element is required by an output edge and is not on that axis. Owed.** The
  projection to the anterior intraparietal area, declared in Outputs, leaves from
  **the lower bank of the superior temporal sulcus and the middle temporal gyrus** — a
  ventrolateral sector, not a position on the posterior-to-anterior series above. So this entry
  needs either a second divisional axis or a third named sub-element, and the architectonic label
  for the sector is not established here. **This is the same shape of problem the
  slot met at layer 4B in V1: an output edge whose source sub-element the entry cannot name.**
  *(Class 1 for the sector's location — Borra et al. 2008, macaque; abstract only. Class 2 — the
  reading that it constitutes a sub-element on a second axis is
  Claude's, offered to be checked.)*

  **Laminar sub-elements: eight** — **1, 2, 3, 4, 5a, 5b, 6a, 6b**, layer 4 undivided. *(Class 3.)*

  **Tangential sub-elements: two different kinds, in the two divisions, and the anterior kind is
  not a compartment at all.**

  - **Posteriorly**, the colour-selective **globs** described at V4 continue into the posterior inferotemporal cortex — the glob
    population is reported as spanning V4 and posterior inferotemporal cortex together, sometimes
    called the V4 complex. So the posterior inferotemporal cortex's tangential organisation is V4's,
    continued. *(Class 1 — Conway
    et al. 2010; PNAS 106, 2009; macaque.)*
  - **Anteriorly**, the anterior inferotemporal cortex is organised into **feature columns**: cells responding to similar
    moderately complex object features cluster in a region running perpendicular to the surface,
    and cells in different columns respond to different features. **But the borders between
    neighbouring columns are not discrete.** Optical imaging indicates a **continuous mapping of
    complex feature space** across a larger region containing several **partially overlapped**
    columns — closer to V1's orientation map, where the property changes gradually along the
    surface, than to V1's patches or V2's stripes, which are compartments with edges. *(Class 1 —
    Fujita et al. 1992; Tanaka 1996; Tanaka 2003; macaque.)*

  **This is a limit of the slot, and it is recorded rather than worked around.** A sub-element is
  something that can be named and pointed at, and an edge terminates on one. A continuous feature
  map has **no discrete sub-elements to name** — a position in it is a coordinate, not a
  compartment. So the anterior inferotemporal cortex's tangential axis cannot be written as a list
  of sub-elements without
  falsifying it. It is recorded here as a **continuous map, not a compartmentation**, and what an
  edge terminating "on the anterior inferotemporal cortex column" means is **owed**.

  **Internal edges — divisional.**
  - **the posterior inferotemporal cortex → the anterior inferotemporal cortex** — **carries:** payload **owed**; the complex-feature code, becoming more invariant.
    The projection is **specific and columnar** — anterograde tracing produces columnar foci — and
    its laminar distribution is **heterogeneous** and **not the standard forward pattern**: the
    posterior inferotemporal cortex
    projects not only to layer 4 but also to the layers above it, and single reconstructed axons
    from the columnar foci differ from one another in where they terminate. The columnar
    organisation of the anterior inferotemporal cortex shows a bias toward the superficial layers
    including layer 4, which may
    reflect exactly this input specificity. **Fan-in:** unknown. **Fan-out:** unknown. *(Class 1 —
    Saleem, Tanaka & Rockland 1993, macaque.)*

  **Internal edges — laminar.** *(All **Class 3**, the general cortical pattern rather than
  measurements made in the inferotemporal cortex.)* **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal
  **5a → 2/3**;
  **6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; **within-sub-element
  recurrence in 4 and 2/3**. **Fan-in** and **fan-out** unknown throughout. Note that the
  divisional edge above already contradicts the first of these as a description of the *incoming*
  projection, which does not confine itself to layer 4.

  **Internal edges — tangential: owed**, and see the limit noted above: for the anterior
  inferotemporal cortex the question may not
  be well posed in the form the slot asks it.
- **Neurons:** ~120M per hemisphere (best available; genuine high uncertainty —
  no clean primary human the inferotemporal cortex count exists, and even whole-brain totals carry a real
  band, 61–99B, Goriely 2024). Recorded as order-of-magnitude. *Why the V1 rescale does not propagate
  here:* the V1 revision was **density-driven and V1-specific** — V1 is the ~60,000/mm³ packing outlier —
  whereas the inferotemporal cortex is ordinary association cortex (~20–40k/mm³), so the rescale
  does not carry over; and ~120M
  sits cleanly between its verified temporal-lobe neighbours (temporal pole ~103M, superior temporal
  gyrus, von Economo area TA / Brodmann area 22 ~145M).
  The order-of-magnitude figure therefore stands.
- **Synapses:** unknown. **Axons:** unknown. **Grey-matter volume:** unknown.
  **White-matter volume:** unknown. **Myelination:** unknown.

**Ventral stream ordering V1 → V2 → V4 → the inferotemporal cortex is verified** (canonical; Ungerleider
& Mishkin; Felleman & Van Essen 1991).

**A note about what this file's title claims.** This file is described above as the
**ventral** visual stream, and that description is one edge short of accurate at both ends of
the hierarchy: the inferotemporal entry projects to a parietal area (above), and V3 / V3A is
dorsal-leaning by its own entry's account and is held here. Separately, three regions that neighbour
V3 / V3A have **no entry in any file** — **V6**, the two subdivisions of **V6A**, and the **caudal
intraparietal area** — and receptor-architectonic mapping groups V6, V6Av and the caudal
intraparietal area's territory into one caudal cluster **with V3d and V3A**, which are in this file.
**Owed, and it is a decision about the file map rather than about the brain: whether those three
join V3 / V3A here, or whether V3 / V3A joins them in the dorsal-stream file.** *(Class 1 for the
cluster — eLife 9:e55979, 2020, macaque, the same mapping already cited in
files 4 and 6. Candidate.)*

---

---

## References

*(Section under source design §2a: the citing line carries the key, and the authors, title,
journal, volume, pages and method sit here. Species stays inline, where the entries argue from it.
Every line below is a **candidate**; none is verified for the source. **Eight lines carry a
reference obtained by a web search against the publisher's or journal's record.** The rest read
**owed**: what follows the key on those lines is **transcribed from this file's own citing lines**,
not from any record — where the citing line carried a journal, volume, page or method, it is here;
where it carried nothing but the key, the line says so. A transcribed line is not a searched one
and does not become one by sitting in this section.)*

**172 distinct keys, 208 mentions. 8 searched; 164 owed.**

**Nine keys name a source that cannot be looked up from this file** — *clinical anatomy review*,
*ScienceDirect striate-cortex overview*, *Springer lateral geniculate nucleus models review*,
*Kennedy/Bullier lineage*, *Saleem & Tanaka lineage*, *Hässler lineage*, *Neuron layer-1 review
2023*, *Ungerleider & Mishkin* and *Pakkenberg & Gundersen*: the citing line gives no author, no
year, or no identifier, so no search can be run from what the file holds. Each is marked on its own
line. **Repairing them is repair at the citing line, not here.**

**Four keys were written more than one way inline, which defeats the string match this section is
built on**, and each is now read as one source: *Andrews 1997* / *Andrews et al. 1997* /
*Andrews, Halpern & Purves 1997*; *Neuron review 2023* / *Neuron layer-1 review 2023*; *StatPearls*
/ *StatPearls, Neuroanatomy, Optic Chiasm*; and *Alonso-Nanclares, Gonzalez-Soriano, Rodriguez &
DeFelipe 2008*, shortened to the standard *et al.* form. **The readings are Class 2** and are noted
on the lines they affect.

- **Ahmed et al. 1994** — cited for layer-4 synapse counts in cat V1. No journal, volume or page at the citing line. **owed**: not searched.
- **Ahnelt et al. 1987** — Ahnelt, P.K., Kolb, H. & Pflug, R. (1987). Identification of a subtype of cone photoreceptor, likely to be blue sensitive, in the human retina. *Journal of Comparative Neurology* 255(1): 18–34. **Human.** Light microscopy of foveal and peripheral retina. *(searched; candidate.)*
- **Alonso-Nanclares et al. 2008** — Alonso-Nanclares, Gonzalez-Soriano, Rodriguez & DeFelipe, 2008. Human neocortex, temporal lobe; direct electron microscopy. Written inline in full author form until this pass and shortened to the standard *et al.* key. **owed**: not searched.
- **Anderson & Martin 2005** — as reported in PMC6665918; macaque. **owed**: not searched.
- **Anderson & Martin 2006** — as reported in PMC6665918; macaque. **owed**: not searched.
- **Anderson, Kennedy & Martin 2011** — *J Neurosci* 31:10872, 2011. Macaque; anterograde biotinylated dextran amine. **owed**: not searched.
- **Andrews, Halpern & Purves 1997** — human lateral geniculate nucleus and V1 volumes, and their co-variation within a brain. **The file wrote this key three ways** — *Andrews 1997*, *Andrews et al. 1997* and the full form — and they are read here as one paper. That reading is **Class 2**; it has not been checked against the record. **owed**: not searched.
- **Baylor & Fuortes 1970** — Baylor, D.A. & Fuortes, M.G.F. (1970). Electrical responses of single cones in the retina of the turtle. *Journal of Physiology (London)* 207: 77–92. **Turtle.** Intracellular recording. *(searched; candidate.)*
- **Binzegger, Douglas & Martin 2004** — cat V1; quantitative circuit reconstruction, as reported in the review at PMC3777738. The primary paper was not opened. **owed**: not searched.
- **bioRxiv 633347** — line of decussation and its displacement in albinism; human. **owed**: not searched.
- **bioRxiv 2022.10.24.511199** — Allen Institute patch-seq; human and mouse layer-1 interneuron repertoires. **owed**: not searched.
- **Borra et al. 2008** — Borra, Belmalih, Calzavara, Gerbella, Murata, Rozzi & Luppino, "Cortical connections of the macaque anterior intraparietal area," *Cerebral Cortex* 18:1094, 2008. Macaque; retrograde tracer. **The abstract is what was opened; the full paper was not.** **owed**: not searched.
- **Brain Struct Funct, PMC6957570** — "Pupillary light reflex circuits in the macaque," *Brain Struct Funct*; also carried at the citing line as s00429-019-02003-7. Macaque. Abstract only. **owed**: not searched.
- **Cerebral Cortex 34:2, bhad512, 2024** — human V1 laminar neuronal and non-neuronal density. Abstract only. **owed**: not searched.
- **Cerebral Cortex 30:3483, 2020** — reporting the 4B cell-class account; macaque. **owed**: not searched.
- **Chacko 1948** — older direct count of lateral geniculate neurons. No journal, volume or page at the citing line. **owed**: not searched.
- **Cheng et al. 1993** — inferotemporal projections; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Clancy & Cauller 1999** — cited within *Frontiers in Neuroanatomy* 12:1, 2018; rodent layer 6b. **owed**: not searched.
- **clinical anatomy review** — **No author, year or identifier at the citing line**, so the source cannot be looked up from this file. Cited for why the chiasmatic crossing ratio is neither 50:50 nor 100:0; comparative. **owed**: not searched.
- **Colour and Vision Research Laboratory** — topographic distributions of cone classes; human. Database rather than a paper; the citing line names no page. **owed**: not searched.
- **Constantinople & Bruno 2013** — *Science* 340:1591, 2013. **Rat somatosensory cortex.** **owed**: not searched.
- **Conway et al. 2010** — colour modules across V1, V2, V4 and posterior inferotemporal cortex; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Cox & Beatty 2017** — dendritic release by geniculate local interneurons; cat. No journal, volume or page at the citing line. **owed**: not searched.
- **Cragg 1967** — macaque area 17 synapses per neuron, high end. No journal, volume or page at the citing line. **owed**: not searched.
- **Crick 1984** — the thalamic reticular "searchlight" proposal. No journal, volume or page at the citing line. **owed**: not searched.
- **Crook et al. 2009** — cited against the pure-colour reading of the small bistratified cell. No journal, volume or page at the citing line. **owed**: not searched.
- **Curcio et al. 1990** — Curcio, C.A., Sloan, K.R., Kalina, R.E. & Hendrickson, A.E. (1990). Human photoreceptor topography. *Journal of Comparative Neurology* 292(4): 497–523. **Human.** Eight whole-mounted retinas from seven individuals aged 27–44; direct counts. *(searched; candidate.)*
- **Curcio et al. 1991** — Curcio, C.A., Allen, K.A., Sloan, K.R., Lerea, C.L., Hurley, J.B., Klock, I.B. & Milam, A.H. (1991). Distribution and morphology of human cone photoreceptors stained with anti-blue opsin. *Journal of Comparative Neurology* 312(4): 610–624. **Human.** Immunostaining. *(searched; candidate.)*
- **Current Biology 9:R666, 1999** — retinal cell classes, the graded/spiking division, and the space/time division of labour between horizontal and amacrine cells. **owed**: not searched.
- **Current Biology 11:R656, 2001** — geniculate inhibitory loops and their share of relay-cell synapses; cat. **owed**: not searched.
- **Dacey & Lee 1994** — the blue-specific bipolar drive to the small bistratified cell. No journal, volume or page at the citing line. **owed**: not searched.
- **De Valois et al. 1966** — the three cardinal chromatic classes described physiologically. No journal, volume or page at the citing line. **owed**: not searched.
- **Derrington, Krauskopf & Lennie 1984** — chromatic mechanisms in the lateral geniculate nucleus. No journal, volume or page at the citing line. **owed**: not searched.
- **Dorph-Petersen et al. 2008** — modern unbiased stereology (optical fractionator) of the human lateral geniculate nucleus. No journal, volume or page at the citing line. **owed**: not searched.
- **Douglas & Martin 1991** — recurrent amplification in cat V1. No journal, volume or page at the citing line. **owed**: not searched.
- **Douglas & Martin 2004** — the canonical-microcircuit proposal; cat V1. No journal, volume or page at the citing line. **owed**: not searched.
- **Douglas, Martin & Whitteridge 1989** — cat V1 intracellular work behind the canonical microcircuit. No journal, volume or page at the citing line. **owed**: not searched.
- **Dowling 1991** — Dowling, *Encyclopedia of Human Biology*, 1991; the retinal sign convention. **owed**: not searched.
- **eLife 9:e55979, 2020** — receptor autoradiography, macaque; the caudal cluster grouping V6, V6Av and caudal intraparietal territory with V3d and V3A. Also cited in files 4 and 6. **owed**: not searched.
- **eNeuro 3(4):ENEURO.0039-16, 2016** — glob and interglob response differences; macaque. **owed**: not searched.
- **Eye (Lond), s41433-024-03137-7, 2024** — chiasmatic fibre totals and crossing proportions; human. **owed**: not searched.
- **Federer et al. 2009** — *J Neurosci* 29:15455, 2009; the two pale stripes as distinct compartments. **owed**: not searched.
- **Federer et al. 2013** — *J Neurosci* 33:11530, 2013; macaque and marmoset. **owed**: not searched.
- **Felleman & Van Essen 1987** — direction selectivity in macaque V3. No journal, volume or page at the citing line. **owed**: not searched.
- **Felleman & Van Essen 1991** — the cortical hierarchy; cited for the ventral ordering. No journal, volume or page at the citing line. **owed**: not searched.
- **Felleman, Burkhalter & Van Essen 1997** — *J Comp Neurol* 379:21, 1997. Macaque; V3 and the ventral posterior area and their differing connections. **owed**: not searched.
- **Felleman, Xiao & McClendon 1997** — *J Neurosci* 17:3185, 1997. Macaque; modular V2-to-V4 convergence. **owed**: not searched.
- **Field et al. 2007** — cited against the pure-colour reading of the small bistratified cell. No journal, volume or page at the citing line. **owed**: not searched.
- **Field et al. 2010** — peripheral midget surrounds are mixed rather than cone-selective. No journal, volume or page at the citing line. **owed**: not searched.
- **Frontiers in Neuroanatomy 12:1, 2018** — layer 6b, its orexin receptor and its recruitment of 6a; rodent. Cites Clancy & Cauller 1999, Marx & Feldmeyer 2013 and Hay et al. 2015. **owed**: not searched.
- **Fujita et al. 1992** — Fujita, Tanaka, Ito et al., *Nature* 360:343, 1992. Macaque; feature columns in anterior inferotemporal cortex. **owed**: not searched.
- **Gamlin, Zhang & Clarke 1995** — *Exp Brain Res* 106:169, 1995. Rhesus; single-unit recording. Abstract only. **owed**: not searched.
- **Goriely 2024** — whole-brain neuron totals and their band. No journal, volume or page at the citing line. **owed**: not searched.
- **Gouras 1968** — the parasol cell as achromatic. No journal, volume or page at the citing line. **owed**: not searched.
- **Hamos et al. 1985** — geniculate triads and glomeruli; cat. No journal, volume or page at the citing line. **owed**: not searched.
- **Hamos et al. 1987** — the retinal share of geniculate synapses; cat. No journal, volume or page at the citing line. **owed**: not searched.
- **Hässler lineage** — **No year or identifier at the citing line**; cited across 16 primate species for the 4B classification dispute. **owed**: not searched.
- **Hay et al. 2015** — cited within *Frontiers in Neuroanatomy* 12:1, 2018; rodent. **owed**: not searched.
- **Hofer et al. 2005** — Hofer, H., Carroll, J., Neitz, J., Neitz, M. & Williams, D.R. (2005). Organization of the human trichromatic cone mosaic. *Journal of Neuroscience* 25(42): 9669–9679. **Human.** Adaptive-optics retinal imaging in living eyes. *(searched; candidate.)*
- **Iwai & Yukie 1987** — inferotemporal projections to the striatum and the anterior bias of the outward fan; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **J Neurosci 32:297, 2012** — the spiking ON bipolar cell; ground squirrel. **owed**: not searched.
- **J Neurosci 16:5923, 1996** — the interlaminar-zone dispute; ferret. **owed**: not searched.
- **J Neurosci 33:1887, 2013** — dendritic release without a spike, and lagged relay cells; cat. **owed**: not searched.
- **J Neurosci 36:1841, 2016** — stripes as full-thickness columns, and the colour/disparity columns reported in human V3; human and non-human primate. **owed**: not searched.
- **Johnson, Hawken & Shapley 2001** — double-opponent cells in V1. No journal, volume or page at the citing line. **owed**: not searched.
- **Johnson, Hawken & Shapley 2008** — double-opponent cells in V1. No journal, volume or page at the citing line. **owed**: not searched.
- **Kaneko 1970** — Kaneko, A. (1970). Physiological and morphological identification of horizontal, bipolar and amacrine cells in goldfish retina. *Journal of Physiology (London)* 207: 623–633. **Goldfish.** Intracellular recording with dye marking. *(searched; candidate.)*
- **Kennedy/Bullier lineage** — **No year or identifier at the citing line.** Macaque; retrograde fast blue. Feedback origins in layers 3A and 6. **owed**: not searched.
- **Kim et al. 2014** — *J Neurosci* 34:9656, 2014. Mouse visual and somatosensory cortex; the opposite-sign layer-6 effects on layer 4 and 5a. **owed**: not searched.
- **Kobatake & Tanaka 1994** — complex-feature cells across V4 and inferotemporal cortex; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Kupfer 1967** — older direct count of lateral geniculate neurons. No journal, volume or page at the citing line. **owed**: not searched.
- **Larkum 2013** — the coincidence-detection reading of layer-1 arrival; applied in this file as **Class 2**. No journal, volume or page at the citing line. **owed**: not searched.
- **Leuba & Kraftsik 1994** — the older ~140M human V1 neuron figure. No journal, volume or page at the citing line. **owed**: not searched.
- **Levitt, Yoshioka & Lund 1994** — *J Comp Neurol* 342:551, 1994. Macaque; V2 intrinsic connections. **owed**: not searched.
- **Livingstone & Hubel 1984** — the three-stream account of V1 to V2. No journal, volume or page at the citing line. **owed**: not searched.
- **Livingstone & Hubel 1987** — the three-stream account of V1 to V2. No journal, volume or page at the citing line. **owed**: not searched.
- **Livingstone & Hubel 1988** — the three-stream account of V1 to V2. No journal, volume or page at the citing line. **owed**: not searched.
- **Lu & Roe 2008** — one opponency type per blob. No journal, volume or page at the citing line. **owed**: not searched.
- **Lund 1988** — cited as a lineage for the 4Cα-to-4B route. No journal, volume or page at the citing line. **owed**: not searched.
- **Lyon, Nassi & Callaway 2010** — the di-synaptic collicular route to V3 and the middle temporal area, as reported in PMC4900470. **owed**: not searched.
- **Malach, Tootell & Malonek 1994** — *Cereb Cortex* 4:151, 1994. Squirrel monkey; biocytin with optical imaging. **owed**: not searched.
- **Markov et al. 2014** — macaque; the supragranular (layer 2) feedback origin, as reported in PMC8244994. **owed**: not searched.
- **Martin et al. 1997** — koniocellular blue-yellow physiology. No journal, volume or page at the citing line. **owed**: not searched.
- **Marx & Feldmeyer 2013** — cited within *Frontiers in Neuroanatomy* 12:1, 2018; rodent layer 6b. **owed**: not searched.
- **Moore & Armstrong 2003** — frontal eye field microstimulation and V4 gain, as reported in *PNAS* 121:e2304511121, 2024. **owed**: not searched.
- **Morgan & Lichtman 2020** — *Neuron* 106:468, 2020. Cat and mouse; triad selectivity by relay-cell class. **owed**: not searched.
- **Nakamura et al. 1993** — Nakamura, Gattass, Desimone & Ungerleider, *J Neurosci* 13:3681, 1993. Macaque; the V2 projection that skips V4, and V2-to-V4 modularity. **owed**: not searched.
- **Nassi & Callaway 2007** — the two 4B output cell classes; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Nathans et al. 1986** — Nathans, J., Thomas, D. & Hogness, D.S. (1986). Molecular genetics of human color vision: the genes encoding blue, green, and red pigments. *Science* 232(4747): 193–202. **Human.** Genomic and complementary DNA cloning and sequencing. *(A companion paper, Nathans, Piantanida, Eddy, Shows & Hogness, Science 232(4747): 203–210, shares the year; the citing line concerns the pigment genes, so it is the 193–202 paper.)* *(searched; candidate.)*
- **Nature 297:580, 1982** — pharmacological block of the ON pathway and its thalamic consequence; monkey. **owed**: not searched.
- **Neuron layer-1 review 2023** — layer 1 as a transport layer and the 6b-to-layer-1 edge. **The file wrote this key two ways** — *Neuron review 2023* and *Neuron layer-1 review 2023* — and they are read here as one source; that reading is **Class 2**. No volume or page at either citing line. **owed**: not searched.
- **Neuron S0896-6273(20)30581-X, 2020** — colour modules beyond V1 and V2; macaque. **owed**: not searched.
- **O'Connor et al. 2002** — O'Connor, Fukui, Pinsk & Kastner, 2002; attentional modulation of the human lateral geniculate nucleus. No journal, volume or page at the citing line. **owed**: not searched.
- **O'Kusky & Colonnier 1982** — macaque area 17 synapses per neuron, low end. No journal, volume or page at the citing line. **owed**: not searched.
- **Pakkenberg & Gundersen** — **No year at the citing line.** Human V1 neuron density, ~60,000/mm³. **owed**: not searched.
- **Perry & Cowey 1984** — *Neuroscience* 12:1125, 1984. Macaque; horseradish peroxidase. Abstract only. **owed**: not searched.
- **Physiol Rev 81:1393, 2001** — development of the chiasm; mouse embryo. **owed**: not searched.
- **PMC2885865** — neocortical layer 6 review; the two sublayers' differing thalamic targets. **owed**: not searched.
- **PMC3447820** — the basal-forebrain projection to the perigeniculate nucleus; mouse. **owed**: not searched.
- **PMC3777738** — review reporting Binzegger, Douglas & Martin 2004. **owed**: not searched.
- **PMC4001064, 2014** — Hackett lineage, 2014. Macaque; the caudal auditory parabelt projection into V2. **owed**: not searched.
- **PMC4360995** — Balaram, Young & Kaas. Human, chimpanzee and macaque; V1's laminar subdivisions and their merging at V2. **owed**: not searched.
- **PMC4900470** — reporting Lyon, Nassi & Callaway 2010. **owed**: not searched.
- **PMC6018949** — mouse; a marker line labelling layer 6b across the whole cortical mantle. **owed**: not searched.
- **PMC6131091** — Sherman, corticofugal review; layer 6a terminals at the first-order relay and the reticular nucleus. **owed**: not searched.
- **PMC6417186** — human lateral prefrontal cortex; layer-1 myelinated axon density from childhood to adulthood. **owed**: not searched.
- **PMC6665918** — Anderson & Martin, synaptic reconstruction; the review reporting Anderson & Martin 2005 and 2006. Macaque. **owed**: not searched.
- **PMC8000025** — reporting Yukie & Iwai 1985. **owed**: not searched.
- **PMC8244994** — Vezoli / Kennedy, *NeuroImage* 2020; reporting Markov et al. 2014. **owed**: not searched.
- **PMC10064015** — cat; three-dimensional electron microscopy with volume-based bouton sorting. **owed**: not searched.
- **PMC11048015** — comparative human, non-human primate and rodent; further subdivisions of V1 layer 3. **owed**: not searched.
- **PNAS 106, 2009** — the glob population spanning V4 and posterior inferotemporal cortex; macaque. No page at the citing line. **owed**: not searched.
- **PNAS 121:e2304511121, 2024** — reporting the Moore & Armstrong 2003 lineage. **owed**: not searched.
- **PubMed 8075534** — macaque; retrograde fast blue. Long-range temporal and parietal afferents to V1. **owed**: not searched.
- **PubMed 15951026** — development of the chiasm; mouse embryo. **owed**: not searched.
- **Rapisardi & Miles 1984** — geniculate triads; cat. No journal, volume or page at the citing line. **owed**: not searched.
- **Reid & Shapley 1992** — cone-specific centre/surround segregation in central parvocellular cells. No journal, volume or page at the citing line. **owed**: not searched.
- **Reid & Shapley 2002** — cone-specific centre/surround segregation in central parvocellular cells. No journal, volume or page at the citing line. **owed**: not searched.
- **Rockland 2019** — *Vision* 4:1, 2019. Macaque; single-axon reconstruction of pulvino-cortical projections. **owed**: not searched.
- **Roy et al. 2009** — koniocellular blue-yellow physiology. No journal, volume or page at the citing line. **owed**: not searched.
- **Rubio-Garrido et al. 2009** — *Cerebral Cortex* 19:2380, 2009. Rat; layer-1-projecting thalamocortical neurons. **owed**: not searched.
- **Saalmann et al. 2012** — *Science* 337:753, 2012; the pulvinar regulating transmission by attentional demand. **owed**: not searched.
- **Saleem & Tanaka lineage** — **No year or identifier at the citing line**; the inferotemporal projection to perirhinal cortex; macaque. **owed**: not searched.
- **Saleem et al. 1992** — the V4 projection onto the posterior part of anterior inferotemporal cortex; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Saleem et al. 1993** — the inferotemporal projection to the striatum; macaque. No journal, volume or page at the citing line. **Whether this is the same paper as Saleem, Tanaka & Rockland 1993 is not established**, and the two are kept as separate keys until it is. **owed**: not searched.
- **Saleem, Tanaka & Rockland 1993** — *Cereb Cortex* 3:454, 1993. Macaque; *Phaseolus vulgaris* leucoagglutinin single-axon reconstruction of the posterior-to-anterior inferotemporal projection. **owed**: not searched.
- **Schiller 1995** — the ON/OFF split at the bipolar receptor. No journal, volume or page at the citing line. **owed**: not searched.
- **Schiller 2010** — *PNAS* 107:17087, 2010; the ON/OFF split at the bipolar receptor. **owed**: not searched.
- **Scholarpedia, Area V1** — the stria of Gennari. **owed**: not searched.
- **Schuman et al. 2019** — *J Neurosci* 39:125, 2019. Mouse; the four layer-1 interneuron types. **owed**: not searched.
- **ScienceDirect striate-cortex overview** — **No author, year or identifier at the citing line**, so the source cannot be looked up from this file. Cited for V1's laminar subdivisions. **owed**: not searched.
- **Selemon & Begović 2007** — a stereology study of the lateral geniculate nucleus running high at ~3.5M, treated in this file as an outlier. No journal, volume or page at the citing line. **owed**: not searched.
- **Shapley & Hawken 2011** — single- and double-opponent cells, and the superseding of the modular colour account. No journal, volume or page at the citing line. **owed**: not searched.
- **Shapley & Perry 1986** — the parasol cell as achromatic. No journal, volume or page at the citing line. **owed**: not searched.
- **Sherman 2001** — burst and tonic relay modes. No journal, volume or page at the citing line. **owed**: not searched.
- **Sherman & Guillery 1998** — the driver/modulator distinction. No journal, volume or page at the citing line. **owed**: not searched.
- **Sherwood et al. 2020** — near-invariant cross-primate synapse density. No journal, volume or page at the citing line. **owed**: not searched.
- **Sincich & Horton 2002a** — the two-stream reading of V1 to V2. No journal, volume or page at the citing line. **owed**: not searched.
- **Sincich & Horton 2002b** — *J Comp Neurol*, 2002b. Macaque; anterograde [3H]proline. The cytochrome-oxidase compartment and the input compartment are offset in depth. **owed**: not searched.
- **Sincich & Horton 2003** — *J Neurosci* 23:5684, 2003. Macaque; the two 4B output populations. **owed**: not searched.
- **Sincich & Horton 2005** — the two-stream reading of V1 to V2. No journal, volume or page at the citing line. **owed**: not searched.
- **Sincich & Horton 2010** — *J Neurosci* 30:6963, 2010. Macaque; retrograde tracer counts giving the laminar composition of each V1-to-V2 edge. **owed**: not searched.
- **Sincich et al. 2004** — Sincich, Park, Wohlgemuth & Horton, *Nature Neuroscience* 7:1123, 2004. Macaque; retrograde tracer. The direct geniculate line to the middle temporal area. **owed**: not searched.
- **Springer lateral geniculate nucleus models review** — **No author, year or identifier at the citing line**, so the source cannot be looked up from this file. Cited for the relay-cell / interneuron ratio; cat and mouse. **owed**: not searched.
- **Sretavan & Mason 1994** — *Neuron* 12:1055, 1994. Mouse embryo; the developmental guidance array at the chiasm. **owed**: not searched.
- **Stanford *Foundations of Vision*** — cited for V1 input and for the older ~1.5×10⁸ V1 neuron figure; chapter 6 at one citing line. **owed**: not searched.
- **StatPearls, Neuroanatomy, Optic Chiasm** — human. **A second citing line wrote the key as a bare *StatPearls*** and is read here as the same chapter; that reading is **Class 2**. **owed**: not searched.
- **Sullivan 1958** — older direct count of lateral geniculate neurons. No journal, volume or page at the citing line. **owed**: not searched.
- **Suzuki & Amaral 1994** — perirhinal and parahippocampal afferents; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Tailby et al. 2010** — cited against the pure-colour reading of the small bistratified cell. No journal, volume or page at the citing line. **owed**: not searched.
- **Tanaka 1996** — *Annu Rev Neurosci* 19:109, 1996. Macaque; feature columns in anterior inferotemporal cortex. **owed**: not searched.
- **Tanaka 2003** — *Cereb Cortex* 13:90, 2003. Macaque; the continuous mapping of complex feature space. **owed**: not searched.
- **Tootell et al. 1997** — the full hemifield map of human V3A. No journal, volume or page at the citing line. **owed**: not searched.
- **Ts'o & Gilbert 1988** — one opponency type per blob. No journal, volume or page at the citing line. **owed**: not searched.
- **Tsukamoto & Omi 2015** — short-wavelength input to OFF-midget cells. No journal, volume or page at the citing line. **owed**: not searched.
- **Ungerleider & Desimone 1986** — the V3 projection to the middle temporal area; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Ungerleider & Mishkin** — **No year at the citing line**; cited for the canonical ventral ordering. **owed**: not searched.
- **Ungerleider et al. 1989** — inferotemporal outward projections; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Usrey et al. 1999** — colour arriving at the lateral geniculate nucleus already formed and leaving substantially intact. No journal, volume or page at the citing line. **owed**: not searched.
- **Van Essen & Zeki 1978** — V3A as a distinct area. No journal, volume or page at the citing line. **owed**: not searched.
- **Wandell 1995** — the older ~1M lateral geniculate figure and the ~40:1 V1 ratio built on it. No journal, volume or page at the citing line. **owed**: not searched.
- **Webvision** — Kolb, Fernandez & Nelson (eds), *Webvision: The Organization of the Retina and Visual System*, hosted on NCBI Bookshelf. Cited for V1 input, the interneuron fraction, and the 4A and 4C routes; one citing line writes it *Webvision, NCBI Bookshelf* and two write *Webvision lineage*. **owed**: not searched.
- **Werblin & Dowling 1969** — Werblin, F.S. & Dowling, J.E. (1969). Organization of the retina of the mudpuppy, *Necturus maculosus*. II. Intracellular recording. *Journal of Neurophysiology* 32: 339–355. **Mudpuppy (*Necturus maculosus*).** Intracellular recording. *(searched; candidate.)*
- **Wiesel & Hubel 1966** — the one-to-one mapping of ganglion classes onto geniculate layer classes. No journal, volume or page at the citing line. **owed**: not searched.
- **Williams et al. 1981** — the irregular, nonrandom distribution of short-wavelength cones. No journal, volume or page at the citing line. **owed**: not searched.
- **Wong et al. 2019** — inferior colliculus neuronal density, used here as the cross-check comparator. No journal, volume or page at the citing line. **owed**: not searched.
- **Wool et al. 2019** — short-wavelength input to OFF-midget cells. No journal, volume or page at the citing line. **owed**: not searched.
- **Yabuta & Callaway 1996** — *Nature* 380:442, 1996. Macaque; local input to individual 4B neurons by laser-scanning photostimulation. **owed**: not searched.
- **Yabuta et al. 2001** — the 4B cell-class account; macaque. No journal, volume or page at the citing line. **owed**: not searched.
- **Yukie & Iwai 1985** — *Brain Res* 346:383, 1985. Rhesus; laminar origin of the direct V1-to-V4 projection, as reported in PMC8000025. **owed**: not searched.
- **Zeki 1978** — V3A as a distinct area. No journal, volume or page at the citing line. **owed**: not searched.
- **Zheng et al. 2024** — Zheng, Adams, Horton et al., *J Neurosci* 44, 2024. Macaque. Abstract only; no page at the citing line. **owed**: not searched.
