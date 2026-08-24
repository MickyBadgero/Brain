# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-08-12
---

---

# FILE 16 OF 20 — SPINAL CORD

**What is in this file.** The spinal cord: grey matter organised by Rexed lamina, white-matter tracts, and the segmental reflex arcs and central pattern generators. The grey-matter entry is the origin of the pain, temperature and interoception line.

**Size:** 486 lines, ~11.0k tokens / ~45 kB (estimated from bytes, not tokenised). **Entries:** 3. **Edge lines:** 15 region-to-region (6 in, 9 out) + 11 internal edges + 6 tract-routing statements. **Internal structure slots:** 3 of 3. **Pass stamps:** 3 of 3. **Reference keys:** 22, over 32 mentions — two of them shared with file 14.

**Full conversion pass 2026-07-24.** The two entries still in pre-conversion prose — white matter, and reflex arcs / central pattern generators — were converted, and the grey-matter entry (converted 2026-07-19) is unchanged. **All three entries now carry typed edges (or their transmission-only equivalent), Internal-structure slots, and pass stamps.** Two of the three are special cases handled by the established conventions rather than by forcing payload edges: the **white matter is transmission-only** (like the optic chiasm and the file-18 tracts, its edges are routing statements, not transfers), and the **reflex / central-pattern-generator entry adds no new tissue** (its computations are internal edges among the grey-matter entry's already-counted neurons, not new regions).

**Naming pass 2026-07-28.** Every bare abbreviation was expanded to the full name, per the written-out-names convention: **central nervous system**, **periaqueductal gray**, **primary motor cortex**, **rostral ventromedial medulla**, **intermediolateral cell column**, **central pattern generator**, **gamma-aminobutyric acid**. Two abbreviations remain, each **once, in parentheses, at the entry that owns the name** — *intermediolateral cell column (IML)* and *central pattern generators (CPG)*. Rexed lamina numerals (I–X), spinal segment levels (C8, T1, L2, S2) and the afferent fibre classes (Ia, Ib) are names rather than abbreviations and are unchanged. No content changed.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**Entries in this file, with the date each was last worked:**

- **Spinal cord grey matter — segmental sensorimotor and autonomic core (Rexed laminae; dorsal / intermediate / ventral horns)** — pass 2026-07-28 — abbreviations expanded to full names — pass 2026-07-19 — prose slots converted to typed edges — lamina-I output quantified, parabrachial and ventrolateral medulla found dominant over the thalamic line
- **Spinal cord white matter — the ascending / descending fibre columns (funiculi)** — pass 2026-07-28 — abbreviations expanded to full names — pass 2026-07-24 — prose converted to typed tract-routing statements (transmission-only, no payload edges); each tract mapped to the grey-matter edge it carries; Internal structure not applicable; red nucleus noted as a standing §9a item
- **Spinal reflex arcs and central pattern generators — the intrinsic segmental / propriospinal circuits** — pass 2026-07-28 — abbreviations expanded to full names — pass 2026-07-24 — prose converted; no region-to-region edge of its own (afferents/efferents are the grey-matter entry's); the six reflex arcs and the central pattern generator typed as internal edges; mesencephalic-locomotor start/speed command owed at file 14; Internal structure slot added

---

# SPINAL CORD

*The caudal continuation of the central nervous system below the medulla — the **final common path** for motor output and
the **entry gate** for body sensation, and the one remaining scoped structure (it had appeared in this
map only as the intermediolateral-cell-column waypoint in the pineal sympathetic chain). Its layout is
the **inverse of the cerebrum**: central **grey matter** (an H- / butterfly-shaped core, organised into
Rexed laminae I–X) wrapped in peripheral **white matter** (the ascending and descending fibre columns).
It is **segmental** — 31 pairs of spinal nerves (8 cervical, 12 thoracic, 5 lumbar, 5 sacral, 1
coccygeal) — with two enlargements (cervical, for the upper limb; lumbosacral, for the lower). Beyond
relaying, it **computes**: the segmental reflex arcs and the locomotor central pattern generators are
intrinsic spinal circuits. **Number convention:** the cord is bilateral-segmental, not hemispheric, so
counts are given **whole (both sides)** with the per-side value alongside where known, following the
basal-ganglia / cerebellum treatment. It enters with **two firm human counts** — a whole-cord neuron
total and a lumbosacral motor-neuron count — that between them correct a long-standing textbook
overestimate.*

## Spinal cord grey matter — segmental sensorimotor and autonomic core (Rexed laminae; dorsal / intermediate / ventral horns)

- **Function:** the segmental processing core, laminated dorsal-to-ventral (Rexed 1952, cat scheme,
  applied to human). **Dorsal horn (laminae I–VI) = sensory:** lamina I (marginal zone) is the origin
  of the **lamina-I spinothalamic** projection carrying pain / temperature / itch / interoception (the
  pathway the Insula and thalamus entries named); lamina II (**substantia gelatinosa**) is the site of
  the **pain "gate"** — where descending control from the periaqueductal gray / rostral ventromedial medulla modulates
  incoming nociception **at the first synapse** (Melzack & Wall 1965; the dorsal-horn terminus the
  periaqueductal-gray descending-analgesia circuit pointed to); laminae III–VI (nucleus proprius and
  deeper) take mechanoreceptive and convergent input. **Intermediate zone (lamina VII):** **Clarke's
  column / nucleus dorsalis** (≈ C8–L2/3) is the origin of the **dorsal spinocerebellar** tract; the
  **intermediolateral cell column (IML, ≈ T1–L2/3)** holds the **sympathetic preganglionic** neurons
  (the pineal-chain waypoint), with the **sacral parasympathetic** nucleus (S2–S4) nearby. **Ventral
  horn (laminae VIII–IX) = motor:** the **motor-neuron pools** — **alpha** motor neurons (to extrafusal
  muscle) and **gamma** motor neurons (to muscle-spindle intrafusal fibres) — the **final common path**
  onto skeletal muscle (Sherrington). The pools are somatotopic (medial = axial / trunk, lateral =
  distal limb; flexor pools dorsal, extensor ventral). Lamina X rings the central canal.
- **Inputs:**
  - **← primary sensory afferents via the dorsal roots** (cell bodies in the dorsal-root ganglia,
    outside this file's central-nervous-system scope) — **carries:** the whole peripheral
    somatosensory payload, **sorted by modality onto different laminae**: nociceptive and
    thermoreceptive afferents terminate mainly in **laminae I and II**, low-threshold
    mechanoreceptive afferents in **laminae III–VI**. Many nociceptive afferents contain
    **substance P**, released from their central terminals on noxious stimulation, acting on the
    **neurokinin-1 receptor**, which is present at high density in lamina I. **Fan-in:** unknown.
    *(Class 1 — modality-specific lamination and substance P / neurokinin-1 receptor: Todd, Molecular
    Pain 13, 2017, review; Rexed 1952, cat. Candidate — awaiting Micky's verification.)*
  - **← descending motor tracts** — corticospinal (directly onto distal-limb motor neurons in
    humans, and via interneurons), reticulospinal, vestibulospinal, rubrospinal and tectospinal —
    **carries:** motor commands and postural drive onto interneurons and motor neurons.
    **Payload otherwise unknown — owed** (these are five distinct edges collapsed onto one line
    because their payloads have not been separately typed). **Fan-in:** unknown.
  - **← periaqueductal gray and the rostral ventromedial medulla** (descending modulatory) —
    **carries:** the **analgesic gate** — descending control that modulates incoming nociception
    **at the first synapse**, in lamina II. No stimulus content; a gain applied to another edge's
    payload. **Fan-in:** unknown.
  - **← raphe nuclei and hypothalamus** (modulatory, onto the dorsal horn and the intermediolateral
    cell column) — **carries:** neuromodulatory state; no stimulus content. **Payload otherwise
    unknown — owed.** **Fan-in:** unknown.
  - **← Rostral ventrolateral medulla**, onto the **intermediolateral cell column** — **carries:**
    the excitatory presympathetic drive that sets vasomotor tone and cardiac sympathetic output;
    generated by intrinsically pacemaking cells rather than relayed. **Fan-in:** unknown.
    *(**Written to close the two-ended diff** against that entry. Candidate.)*
- **Outputs:**
  - **→ Posterior / ventromedial-posterior thalamus**, from **lamina I** (crossed
    spinothalamic) — **carries:** the three labelled lines typed at the receiving entry —
    nociceptive-specific from fusiform cells, thermoreceptive-specific from pyramidal cells, and
    polymodal nociceptive from multipolar cells — with measured central conduction latencies of
    roughly 131, 59 and 72 ms respectively. **Fan-out:** unknown.
    **This edge is a minority of lamina I's output, and the file previously treated it as the
    pathway.** In rat lumbar enlargement, spinothalamic cells are about **5%** of the roughly **400
    lamina I projection neurons per side per segment**; in the cervical enlargement, where there are
    about **215** per side, they are about **42%**. So the thalamic share is not a constant of the
    cord — it varies several-fold along it.
    *(Class 1 — Al-Khater & Todd, J Comp Neurol 515:629, 2009, and Al-Khater, Kerr & Todd, J Comp
    Neurol 511:1, 2008, rat, retrograde tracing with stereological estimation; Spike, Puskár, Andrew
    & Todd, 2003, rat lumbar. **Species: rat. No human figure found.** Candidates.)*
  - **→ Lateral parabrachial nucleus**, from **lamina I** — **carries:** the same three labelled
    lines, read at the far end for their **affective** rather than discriminative content. This is
    the **dominant** supraspinal destination of lamina I: about **85%** of lumbar lamina I
    projection cells label from here or the caudal ventrolateral medulla on the contralateral side,
    and a review of the same literature puts ~95% of ascending lamina I neurons on this target.
    **Most fibres reaching other targets send collaterals here**, so this is largely the same
    population as the thalamic and periaqueductal edges rather than an additional one.
    **Fan-out:** unknown.
  - **→ Caudal ventrolateral medulla**, from **lamina I** — **carries:** the same payload; the far
    end is also the baroreflex's inhibitory relay, and whether the lamina-I input contacts those
    same neurons is **owed**. **Fan-out:** unknown.
    *(Class 1 for both — Spike, Puskár, Andrew & Todd, 2003, rat, paired retrograde tracer
    injections; Sugimura, Takahashi, Watabe & Kato, J Neurophysiol 115:2721, 2016, review.
    **Species: rat.** Candidates — awaiting Micky's verification.)*
  - **→ periaqueductal gray**, from **lamina I** — **carries:** payload **owed**. About **120**
    lamina I cells per side in the rat L4 segment project here, and **over 90% of them can also be
    labelled from the caudal ventrolateral medulla or the lateral parabrachial area** — so this is
    largely a *collateral* of the preceding edge, not an independent population, the same
    branching-axon situation the retina–colliculus edge records. **Fan-out:** unknown.
    *(Class 1 — Spike et al. 2003, rat. Candidate.)*
  - **→ caudal thalamus**, from **laminae III/IV neurokinin-1-receptor-expressing neurons with long
    dorsal dendrites reaching lamina I** — **carries:** payload **owed**; a second, separate
    spinothalamic population. It is **85%** of those cells in cervical C6 but only **17%** in lumbar
    L5, and it projects apparently exclusively to caudal thalamus, whose targets are the second
    somatosensory and insular cortices. **Fan-out:** unknown.
    *(Class 1 — Al-Khater, Kerr & Todd, J Comp Neurol 511:1, 2008, rat. Candidate.)*
  - **→ Cerebellum**, from **Clarke's column / nucleus dorsalis** (≈ C8–L2/3), via the **dorsal
    spinocerebellar tract** — **carries:** unconscious proprioception — body configuration.
    **Fan-out:** unknown.
  - **→ Inferior olive** — **carries:** somatosensory **error**, the actual consequence against
    which the prediction failed (typed at the receiving entry). **Fan-out:** unknown.
  - **→ skeletal muscle, via the ventral roots**, from the **motor-neuron pools** — **carries:** the
    final motor command; alpha motor neurons to extrafusal muscle, gamma motor neurons to
    muscle-spindle intrafusal fibres. **The consumer at the far end is not in this map** — muscle,
    skeleton and their dynamics have no entry, the same open boundary the primary motor cortex corticospinal edge
    declares. **Fan-out:** unknown.
  - **→ sympathetic chain ganglia**, from the **intermediolateral cell column** (≈ T1–L2/3) —
    **carries:** preganglionic sympathetic drive (the pineal-chain waypoint). **The far end lies
    outside this file's central-nervous-system scope.** **Fan-out:** unknown.
- **Internal structure and internal data flow:** the Rexed laminae, dorsal to ventral, named in the
  Function slot above. The quantitative fact that organises the dorsal horn is that **projection
  neurons are a small minority**: they are concentrated in lamina I, largely **absent from lamina
  II**, and scattered through laminae III–VI. **90–95% of lamina I neurons and virtually all lamina
  II neurons are interneurons**, and about **80%** of the lamina I projection cells express the
  neurokinin-1 receptor. The interneurons divide into inhibitory (gamma-aminobutyric acid and/or glycine) and
  excitatory (glutamatergic) classes; many also have propriospinal axons extending several segments.
  - **Internal edge — primary afferent terminals → lamina I and II interneurons: carries:** the
    nociceptive and thermoreceptive payload before any gating. **Fan-in / fan-out:** unknown.
  - **Internal edge — lamina II inhibitory interneurons → lamina I projection neurons: carries:**
    inhibition; this is the substrate of the pain gate, the point at which the descending
    periaqueductal-gray / rostral-ventromedial-medulla edge acts. **Fan-in / fan-out:** unknown.
  - **Internal edge — laminae III/IV dorsal dendrites → lamina I: carries:** not a synaptic transfer
    but the **dendritic reach** of the laminae III/IV projection population into lamina I; recorded
    under the convention that the receiving membrane's owner is named and **no second internal edge
    is written for propagation within one cell**. **Fan-in / fan-out:** n/a.
  - **Internal edge — dorsal-horn interneurons → ventral-horn motor pools (segmental reflex arc):
    carries:** the reflex drive; typed in the *Spinal reflex arcs and central pattern generators*
    entry. **Fan-in / fan-out:** unknown.
  *(Class 1 — interneuron proportions and projection-cell distribution: Todd, Molecular Pain 13,
  2017, review of rat material; Al Ghamdi, Polgár & Todd, Neuroscience 164:1794, 2009. **Species:
  rat throughout.** Candidates — awaiting Micky's verification.)*
- **Neurons:** **whole cord ~200 million (197–222M; both sides)** — the **first direct human count**
  (Bahney & von Bartheld 2018, isotropic fractionator + stereology): ~1.5–1.7 billion total cells,
  **glia-dominated** (glia–neuron ratio ~6:1), with **no significant cervical / thoracic / lumbar
  composition difference**. This **corrects the long-quoted ~1 billion neurons** (Kalat 1998, a
  textbook figure) and the ~13.5–20M cross-species extrapolations (Gelfan 1963, from dog;
  Herculano-Houzel et al. 2016, from monkey) — all of which were extrapolations, not human
  measurements. Motor neurons are a **tiny fraction** of that total (well under 0.1%): **lumbosacral
  (L1–S3) limb motor neurons ~52,000–62,000**, roughly **equal on each side** (Tomlinson, Irving &
  Rebeiz 1973; Tomlinson & Irving 1977, 47 human cords), **stable to ~60 years then declining** (~25%
  average loss into old age).
- **Synapses:** unknown. **Axons:** the dorsal / ventral roots and ascending / descending fibres (see
  the white-matter entry); counts unknown. **Grey-matter volume:** the grey is the central core of a
  cord ~43–45 cm long / ~35 g (soft secondary-compilation figures, Watson, Paxinos & Kayalioglu 2009);
  per-segment grey volume not recorded. **White-matter volume / Myelination:** see the white-matter
  entry.
- **Pass:** 2026-07-28 — abbreviations expanded to full names (central nervous system, periaqueductal gray, intermediolateral cell column, gamma-aminobutyric acid, primary motor cortex); *(IML)* kept once at the name's owning mention
- **Pass:** 2026-07-19 — prose slots converted to typed edges — lamina-I output quantified, parabrachial and ventrolateral medulla found dominant over the thalamic line

## Spinal cord white matter — the ascending / descending fibre columns (funiculi)

- **Function:** the cord's cabling — transmission, like the white-matter-tract entries, but inseparable
  from the cord, so given its own slot. Three funiculi carry the long tracts. **Ascending:** the
  **dorsal columns** (fasciculus **gracilis**, lower body / below ~T6, + **cuneatus**, upper body /
  above ~T6) — fine touch, vibration, and conscious proprioception, ascending **ipsilaterally** to the
  dorsal-column (gracile / cuneate) nuclei already in the map; the **anterolateral / spinothalamic**
  system — pain, temperature, crude touch, interoception — which **crosses at the segmental level**
  (through the anterior white commissure) and ascends **contralaterally** to the ventral posterior
  lateral nucleus and, for the lamina-I stream, the posterior / ventromedial-posterior thalamus →
  insula (the routes those entries named); and the **spinocerebellar** tracts (dorsal, from Clarke's
  column, ipsilateral, via the inferior peduncle; ventral, crossed then re-crossing, via the superior
  peduncle) carrying unconscious proprioception to the cerebellum. **Descending:** the **lateral
  corticospinal** tract (crossed at the medullary **pyramidal decussation** — most fibres, ~85–90% —
  driving distal-limb voluntary movement; the corticospinal tract from the primary motor cortex through the internal capsule
  those entries recorded) with the smaller **anterior corticospinal** tract (uncrossed, axial);
  **reticulospinal** (posture, locomotion, tone); **vestibulospinal** (antigravity / balance);
  **rubrospinal** (small, largely vestigial in humans); **tectospinal** (head orienting — the
  superior-colliculus → cervical-cord tract); and the **descending modulatory** fibres (raphe /
  rostral ventromedial medulla → dorsal horn, the analgesia limb; hypothalamospinal, autonomic).
- **Inputs / Outputs:** *(This entry is **transmission, not processing** — like the optic chiasm and
  the white-matter-tract entries, it computes nothing, so its edges are **routing statements**, not
  payload transfers. Each tract's payload is typed at the grey-matter end that produces or consumes
  it; the lines below record which tract carries which edge and in which direction, so a reader can
  find the fibre a given grey-matter edge rides on. Producers/consumers named are the far ends; this
  entry does not re-type their payloads.)*
  - **Ascending, dorsal columns** — carry the grey matter's fine-touch / proprioception traffic
    **ipsilaterally → the gracile and cuneate nuclei** (file 5's dorsal-column nuclei). Routing only.
  - **Ascending, anterolateral / spinothalamic** — carry lamina I's three labelled pain/temperature
    lines, crossed, **→ the posterior / ventromedial-posterior thalamus** (file 12) and **→ the
    ventral posterior lateral nucleus** (file 5); this is the fibre the grey-matter entry's lamina-I
    thalamic edge rides on. Routing only.
  - **Ascending, spinocerebellar** — carry Clarke's-column unconscious proprioception **→ the
    cerebellum** (file 10, via the inferior and superior peduncles). Routing only.
  - **Descending, corticospinal** — carries the motor command **from the primary motor cortex → the ventral-horn motor
    pools** (file 5 declares "→ muscles, via the corticospinal tract"; file 11 declares a minority
    direct corticospinal origin). Crossed at the pyramidal decussation. Routing only.
  - **Descending, reticulospinal / vestibulospinal / tectospinal / rubrospinal** — carry postural,
    balance, orienting and (vestigial) limb drive **from the reticular formation, vestibular nuclei,
    superior colliculus and red nucleus** (files 14, 3, 14; the red nucleus has no entry — a standing
    §9a item) **→ the ventral horn**. Routing only.
  - **Descending, modulatory** — carry the analgesic and autonomic gate **from the raphe, rostral
    ventromedial medulla, locus coeruleus and hypothalamus → the dorsal horn and intermediolateral
    cell column** (files 13, 14). Routing only.
- **Internal structure and internal data flow:** **not applicable** — a fibre-column compartment with
  no grey-matter microcircuit of its own (a scattering of propriospinal interneurons excepted, and
  those are counted and computed in the grey-matter and reflex entries, not here). Like the tract
  entries in file 18, this entry has no internal edges because it has no internal processing. *(A
  positive "not applicable," a statement about the tissue, not an unfilled gap.)*
- **Neurons:** none (fibre columns; a scattering of propriospinal interneurons excepted).
- **Synapses:** none.
- **Axons:** the funicular tracts — including the **corticospinal at an order ~1 million axons per
  side** (the estimate the internal-capsule entry recorded); other per-tract counts unknown.
- **Grey-matter volume:** not applicable.
- **White-matter volume:** the peripheral columns are the bulk of the cord's cross-section rostrally
  (largest in the cervical cord, where the full ascending / descending traffic is present); no
  verified per-level figure recorded (soft).
- **Myelination:** heavily myelinated columns (the white appearance); per-fibre g-ratio unknown.
- **Pass:** 2026-07-28 — abbreviations expanded to full names (primary motor cortex)
- **Pass:** 2026-07-24 — prose Inputs / Outputs converted to typed tract-routing statements (not payload edges, per the transmission-only convention used for the optic chiasm and the file-18 tracts); each tract mapped to the grey-matter edge it carries and its far-end file; Internal structure recorded not applicable; the red nucleus (rubrospinal origin) noted as a standing §9a item

## Spinal reflex arcs and central pattern generators — the intrinsic segmental / propriospinal circuits

- **Function:** the cord's **own computation** — **no new tissue**, since these are grey-matter
  interneuron and motor-neuron circuits already counted in the grey-matter entry (recorded here the way
  the cross-modal-integration section gathers convergence without adding counts). **Reflex arcs:** the
  **monosynaptic stretch (myotatic) reflex** (Ia muscle-spindle afferent → alpha motor neuron — the
  only monosynaptic reflex, e.g. the knee-jerk; Liddell & Sherrington), **reciprocal inhibition** (a Ia
  inhibitory interneuron relaxing the antagonist), the **Golgi-tendon (Ib) autogenic inhibition**, the
  polysynaptic **flexor-withdrawal reflex with crossed extension** (nociceptive: withdraw the stimulated
  limb, extend the other to bear weight), **Renshaw recurrent inhibition** of motor neurons (Renshaw
  1941), and the **gamma loop** (gamma motor neurons set spindle sensitivity; alpha–gamma
  co-activation). **Central pattern generators (CPG):** intrinsic **lumbar** (leg) and cervical (arm)
  interneuron networks that generate the rhythmic, alternating flexor / extensor and left / right
  **locomotor pattern without descending command or sensory feedback** (the "intrinsic factor," Graham
  Brown 1911, half-centre model; the fictive-locomotion lineage, Grillner). The brainstem
  **mesencephalic locomotor region** (reticular formation) initiates stepping and sets its speed, while
  the spinal central pattern generator shapes the pattern — human evidence includes rhythmic stepping-like output evoked by
  epidural stimulation of the lumbar cord after spinal-cord injury.
- **Inputs / Outputs:** *(This entry **adds no new tissue and no region-to-region edge of its own** —
  its afferents and efferents are exactly the grey-matter entry's: primary afferents and descending
  drive in, motor-neuron output out. What is proper to this entry is a set of **internal edges among
  grey-matter neurons**, typed below. The one external edge worth naming is the initiating drive.)*
  - **← the mesencephalic locomotor region** (reticular formation, file 14) — **carries:** a
    **start / speed command for locomotion** — not the pattern itself but the go-signal and its rate;
    the central pattern generator shapes the rhythm, this input triggers and scales it. **Fan-in:** unknown. **The far end
    is the reticular-formation entry (file 14)**, whose descending pattern-generator role names
    locomotion; whether it types this specific edge is **owed as a cross-file check at file 14.**
- **Internal structure and internal data flow:** the reflex arcs and central pattern generators, as **internal edges among
  the grey-matter entry's neurons** — no new tissue, so these are typed here as the computations the
  cord performs on itself:
  - **Internal edge — Ia muscle-spindle afferent → alpha motor neuron** (monosynaptic) — **carries:**
    the stretch-reflex drive, muscle-length error correcting itself in one synapse; the only
    monosynaptic reflex. **Fan-in / fan-out:** unknown.
  - **Internal edge — Ia inhibitory interneuron → antagonist alpha motor neuron** — **carries:**
    reciprocal inhibition, relaxing the antagonist so the reflex movement is not opposed.
    **Fan-in / fan-out:** unknown.
  - **Internal edge — Ib Golgi-tendon afferent → (interneuron) → homonymous alpha motor neuron** —
    **carries:** autogenic inhibition, a tension signal limiting force. **Fan-in / fan-out:** unknown.
  - **Internal edge — nociceptive afferent → flexor interneuron pool → ipsilateral flexors + crossed
    extensors** — **carries:** the polysynaptic flexor-withdrawal-with-crossed-extension pattern —
    withdraw the stimulated limb, extend the other to bear weight. **Fan-in / fan-out:** unknown.
  - **Internal edge — alpha motor-neuron collateral → Renshaw cell → same and neighbouring motor
    neurons** — **carries:** recurrent inhibition, a negative-feedback gain control on motor-neuron
    output. **Fan-in / fan-out:** unknown.
  - **Internal edge — gamma motor neuron → intrafusal spindle fibre → (Ia afferent) → alpha motor
    neuron** (the gamma loop) — **carries:** the spindle-sensitivity setting, keeping the stretch
    reflex responsive across muscle lengths via alpha–gamma co-activation. **Fan-in / fan-out:**
    unknown.
  - **Internal edge — central-pattern-generator interneuron network → flexor / extensor and left / right motor pools** —
    **carries:** the rhythmic, alternating locomotor pattern, generated intrinsically without
    descending command or sensory feedback. This is the entry's most distinctive computation — a
    lower rung building a temporal pattern from tonic drive. **Fan-in / fan-out:** unknown.
  *(All Class 1 / classic physiology — Sherrington, Liddell & Sherrington, Renshaw 1941, Graham Brown
  1911, Grillner's fictive-locomotion lineage; species mixed cat/rodent with human epidural-stimulation
  confirmation of the lumbar central pattern generator. Candidates — awaiting Micky's verification.)*
- **Neurons:** no new counts — the interneurons and motor neurons are those of the grey-matter entry.
- **Synapses:** unknown (the reflex-arc and central-pattern-generator synapses are among the grey-matter entry's uncounted
  synapses).
- **Axons:** the propriospinal interneuron axons (several segments' reach) and the segmental
  reflex-arc collaterals; counts unknown.
- **Grey-matter volume:** not applicable (shared with the grey-matter entry).
- **White-matter volume:** not applicable.
- **Myelination:** not applicable.
- **Pass:** 2026-07-28 — abbreviations expanded to full names (central pattern generator); *(CPG)* kept once at the entry that owns the name
- **Pass:** 2026-07-24 — prose Inputs / Outputs converted; the entry recorded as adding no region-to-region edge of its own (afferents/efferents are the grey-matter entry's), with the mesencephalic-locomotor start/speed command typed as the one external input (owed at file 14); the six reflex arcs and the central pattern generator typed as internal edges among the grey-matter neurons; Internal structure slot added

**The spinal cord is described and verified:** central grey (Rexed laminae — dorsal-horn sensory with
the Melzack–Wall pain gate and the lamina-I spinothalamic origin, intermediate Clarke's column and the
intermediolateral cell column, ventral-horn motor pools as Sherrington's final common path) wrapped in
ascending (dorsal-column, spinothalamic, spinocerebellar) and descending (cortico-, reticulo-,
vestibulo-, rubro-, tecto-spinal and raphe / rostral-ventromedial-medulla modulatory) white-matter columns, with the segmental
reflex arcs and the locomotor central pattern generators as its intrinsic circuitry. This **closes the
tracts that dangled onto the cord** from elsewhere in the map — the **corticospinal** terminus
(primary motor cortex / internal capsule), the **dorsal-column** origin (→ gracile / cuneate nuclei), the
**spinocerebellar** origin (→ cerebellum), the **tectospinal** tract (superior colliculus → cervical
cord), the **rostral ventromedial medulla → dorsal-horn** descending-analgesia limb (periaqueductal gray), and the **intermediolateral-cell-column
sympathetic** waypoint (the pineal chain). It enters with the **first direct human neuron count** (~200M,
glia-dominated ~6:1; Bahney & von Bartheld 2018 — correcting the old ~1-billion extrapolation) and a
firm **lumbosacral motor-neuron count** (~52–62k; Tomlinson & Irving lineage); length / weight
(~43–45 cm / ~35 g) are soft, and synapses / axons / white-matter volume stay unknown.

---


## References

*(Section added 2026-08-12 under source design §2a. Every line below is a **candidate**
awaiting Micky's verification; none is verified. Each full reference given here was obtained by
a web search run in this pass against publisher, journal or PubMed records — no reference is
written from recall. Keys reading **owed** were not searched in this pass.)*

**22 distinct keys, 32 mentions. 4 papers resolved to a full reference across 5 keys; 17 owed.**

**Two keys are shared with file 14, and one of them carries a claim that is copied between the two
files word for word.** *Spike, Puskár, Andrew & Todd, 2003* and *Sugimura, Takahashi, Watabe &
Kato, J Neurophysiol 115:2721, 2016* appear here and at file 14, supporting the two ends of the
same edges — lamina I's projections to the lateral parabrachial nucleus, the caudal ventrolateral
medulla and the periaqueductal grey, produced here and consumed there. **The ~85% and ~95%
sentence at lines 103–105 is the same sentence as file 14's lines 320–323**, and the candidate
discrepancy recorded in file 14's reference section therefore exists at both ends. See the
*Spike* entry. **If it is a correction, it has to be made twice.**

**Two different 85% figures sit twenty lines apart in this file, from two different papers, about
two different things.** Line 103's is the share of lumbar lamina I projection cells labelled from
the parabrachial nucleus; line 123's is the share of laminae III/IV neurokinin-1-receptor neurons
in cervical segment C6 that are spinothalamic. **The second is confirmed exactly by this pass; the
first is the disputed one.** They are unrelated, and a reader skimming will merge them.

**One figure in this file has no cited source.** Line 95's **~215 lamina I projection neurons per
side in the cervical enlargement** is the denominator of the 42% on the next line. It is not in
either Al-Khater paper — the cervical total was explicitly *not known* at the time of the 2009
one — and on this pass's reading it comes from **Polgár, Wright & Todd 2010**, which this file does
not cite. See the *Al-Khater & Todd* entry. **Owed at the citing line.**

**The file's headline human count is confirmed to the digit, and its sample size is not stated
anywhere.** See the *Bahney & von Bartheld 2018* entry: every number on lines 162–165 matches the
paper, and the paper's own title says "a human."

**Species composition of the four resolved: three rat, one human plus cynomolgus monkey.** The
file's own species discipline here is the best in the source — the citing lines say **"Species:
rat"** in bold at three separate blocks, and line 100 goes further and records that no human figure
was found. **Nothing in this section corrects that; it confirms it.** Seventeen keys are unsearched,
eleven of them the classic-physiology names in the reflex entry, which the file already marks as a
class rather than as individual citations.


- **Al Ghamdi, Polgár & Todd, Neuroscience 164:1794, 2009** — **owed**: not searched in this pass.
  It carries, with the Todd review, the interneuron proportions the dorsal-horn Internal-structure
  slot is organised on. *(Line 160.)*
- **Al-Khater & Todd, J Comp Neurol 515:629, 2009** — Al-Khater, K.M. & Todd, A.J. (2009).
  Collateral projections of neurons in laminae I, III, and IV of rat spinal cord to thalamus,
  periaqueductal gray matter, and lateral parabrachial area. *Journal of Comparative Neurology*
  515(6): 629–646; doi 10.1002/cne.22081; PubMed 19496168; free in PubMed Central. **Rat**,
  multiple retrograde tracers with confocal microscopy. *(Wiley publisher record and PubMed.)*
  **Two findings, and the second is the one to act on.** **First, the paper's own lumbar thalamic
  proportion is 4%, not 5%.** Its text gives ~15 lamina I spinothalamic neurons per side in L4
  against ~400 lamina I projection neurons, and states the proportion as **4%**; the later
  Polgár, Wright & Todd paper rounds the same quantity to approximately 5%, which is what line 94
  carries. Either is defensible; **the file should say which it is following.** **Second, the ~215
  cervical figure at line 95 is not from this paper and is not from the 2008 one.** The 2010 paper
  by the same group opens by recording that the total number of lamina I projection neurons in the
  cervical enlargement **was not known** — which is what that paper set out to establish. **On this
  pass's reading the 215 comes from Polgár, E., Wright, L.L. & Todd, A.J., *A quantitative study of
  brainstem projections from lamina I neurons in the cervical and lumbar enlargement of the rat*,
  *Brain Research* 1308: 58–67, 2010; doi 10.1016/j.brainres.2009.10.041; PubMed 19854164** — and
  90 ÷ 215 is the 42% on line 96, which is how the two figures were paired. **No line in this file
  cites that paper and none is added here**, per §2a; it is named so the denominator can be
  attributed. **Owed at line 95: cite the source of the 215, or drop the percentage.** *(searched
  2026-08-12; candidate. Line 98.)*
- **Al-Khater, Kerr & Todd, J Comp Neurol 511:1, 2008** — Al-Khater, K.M., Kerr, R. & Todd, A.J.
  (2008). A quantitative study of spinothalamic neurons in laminae I, III, and IV in lumbar and
  cervical segments of the rat spinal cord. *Journal of Comparative Neurology* 511(1): 1–18; doi
  10.1002/cne.21811; PubMed 18720412; free in PubMed Central. **Rat**, retrograde tracer injections
  targeting the **posterior triangular nucleus** at the caudal end of the thalamus — a region the
  paper notes was missed by many earlier retrograde studies, which is why its counts differ from
  the older literature. *(Wiley publisher record and PubMed.)* **Line 123's two percentages are the
  paper's, exactly: 85% of the laminae III/IV neurokinin-1-receptor neurons in C6 and 17% of those
  in L5.** **And the paper carries the absolute counts behind line 94's percentage, which the file
  does not record**: about **90** lamina I spinothalamic neurons per side in C7 and about **15** in
  L4, with some of the C7 population projecting only to the posterior triangular nucleus. **Those
  two numbers are more transportable than the percentage** — a percentage moves when its
  denominator is re-measured, as line 95's has been. *(searched 2026-08-12; candidate. Lines 98,
  126.)*
- **Bahney & von Bartheld 2018** — Bahney, J. & von Bartheld, C.S. (2018). The cellular composition
  and glia–neuron ratio in the spinal cord of a human and a nonhuman primate: comparison with other
  species and brain regions. *The Anatomical Record* 301(4): 697–710; doi 10.1002/ar.23728.
  **Human and cynomolgus monkey.** Isotropic fractionator and stereology, both applied.
  *(Wiley publisher record.)* **Every number on lines 162–165 matches the paper**: 1.5–1.7 billion
  cells, 197–222 million neurons, a composition of 13.4% neurons / 12.2% endothelial / 74.8% glial,
  a glia–neuron ratio of **5.6–7.1** — which the file rounds to ~6:1 — and **no significant
  segmental difference** between cervical, thoracic and lumbar levels. **Three things the file does
  not say.** **First, the sample size, which is nowhere in the file and is the thing a "first direct
  human count" most needs.** The paper's own title says *a* human; a secondary source citing it
  reports three human specimens. **This pass did not settle which, and it should be settled before
  the figure is treated as firm.** **Second, the endothelial fraction** — 12.2% of cells are
  endothelial, so "glia-dominated ~6:1" is a ratio computed after those are set aside, and the file
  reports the ratio without the composition it rests on. **Third, the correction the paper claims is
  narrower than the one the file attributes to it.** The paper states that previous reports
  overestimated the **non-neuronal-to-neuron ratio**; line 165's claim that it corrects a
  long-quoted ~1 billion *neuron* figure is a further step, and this pass read only abstract-level
  material. **Owed: check that line against the paper's own text.** **A live disagreement is also on
  record**: Ruiz-Sauri et al., *Journal of Anatomy*, 2019, obtained substantially higher glia-neuron
  ratios in human thoracic cord and attribute the gap to counting technique. **No line cites that
  paper and none is added here**, per §2a. *(searched 2026-08-12; candidate. Lines 163, 318.)*
- **Gelfan 1963** — **owed**: not searched in this pass. Named on the citing line as a dog
  extrapolation, which is the file's own reason for setting it aside. *(Line 166.)*
- **Graham Brown 1911** — **owed**: not searched in this pass. The half-centre model and the
  "intrinsic factor," which is the founding claim of the central-pattern-generator entry.
  **The most load-bearing of the classic-physiology keys.** *(Lines 254, 293.)*
- **Grillner** — **owed**: not searched; **the key carries no year and no title**, written as "the
  fictive-locomotion lineage." *(Lines 255, 294.)*
- **Herculano-Houzel et al. 2016** — **owed**: not searched in this pass. Named on the citing line
  as a monkey extrapolation. **Note that a key of this form is also in file 11** — *Gabi &
  Herculano-Houzel 2016*, resolved there to a *Proceedings of the National Academy of Sciences*
  paper on prefrontal neuron fractions — **and this is a different work about the spinal cord.**
  Two same-year keys, same senior author, different papers, two files. *(Line 167.)*
- **Kalat 1998** — **owed**: not searched in this pass. Declared on the citing line as a textbook
  figure, which is the file recording its own provenance correctly. *(Line 165.)*
- **Liddell & Sherrington** — **owed**: not searched; **the key carries no year.** *(Lines 247,
  293.)*
- **Melzack & Wall 1965** — **owed**: not searched in this pass. **It is the gate-control paper the
  whole dorsal-horn Function slot and one internal edge are built on**, and it is the single most
  cited claim in this file's entries. **Highest-value owed key here.** *(Line 51.)*
- **Renshaw 1941** — **owed**: not searched in this pass. *(Lines 250, 293.)*
- **Rexed 1952** — **owed**: not searched in this pass. Cat, declared as such on both citing lines,
  with the file also recording that the scheme is applied to human — which is the right way to carry
  a cross-species framework and is worth keeping when the reference is filled. *(Lines 46, 70.)*
- **Sherrington** — **owed**: not searched; **the key carries no year and no title.** It is the
  final-common-path attribution. *(Lines 59, 293.)*
- **Spike et al. 2003** — **the same work as the key below**, cited in short form at the
  periaqueductal-grey edge. See that entry. **Owed at the citing lines: use one key.** *(Line 120.)*
- **Spike, Puskár, Andrew & Todd, 2003** — Spike, R.C., Puskár, Z., Andrew, D. & Todd, A.J. (2003).
  A quantitative and morphological study of projection neurons in lamina I of the rat lumbar spinal
  cord. *European Journal of Neuroscience* 18(9): 2433–2448; doi 10.1046/j.1460-9568.2003.02981.x;
  PubMed 14622144. **Rat**, L4 lumbar segment, retrograde tracing with paired tracers.
  *(Wiley publisher record and PubMed; searched in this pass sequence while working file 14, which
  cites the same paper at three entries.)* **This paper is the source of the ~400 figure at line 94**
  — the later literature attributes the estimate of about 400 lamina I projection neurons per side
  in L4 to it, and puts them at roughly 6% of the lamina's total neuronal population, a fraction
  this file does not carry. **The candidate discrepancy recorded at file 14 applies here word for
  word.** Lines 103–105 give ~85% of lumbar lamina I projection cells labelling **from the
  parabrachial nucleus or the caudal ventrolateral medulla**, and ~95% of ascending lamina I neurons
  targeting the parabrachial nucleus. **The literature citing this paper states both differently** —
  that a parabrachial injection **alone** labels ~85%, and that those include **more than 95% of the
  cells projecting to the periaqueductal grey.** **Read from a secondary citation, not from the
  paper**, so it is a candidate at both ends and not a correction. **Owed: open Spike et al. once
  and settle it for files 14 and 16 together.** *(searched 2026-08-12; candidate. Lines 99, 112;
  same work at line 120.)*
- **Sugimura, Takahashi, Watabe & Kato, J Neurophysiol 115:2721, 2016** — **owed**: not searched in
  this pass, **and owed at file 14 as well**, where the same key appears at two lines. The citing
  line declares it a review. *(Line 113.)*
- **Todd, Molecular Pain 13, 2017** — **owed**: not searched in this pass. A review, declared as one
  at both citing lines. **It carries the file's four sharpest dorsal-horn proportions** — 90–95% of
  lamina I neurons and virtually all lamina II neurons being interneurons, and about 80% of lamina I
  projection cells expressing the neurokinin-1 receptor — plus the modality-specific lamination and
  the substance P / neurokinin-1 pairing. **Highest-value owed key after Melzack & Wall.** *(Lines
  69, 159.)*
- **Tomlinson & Irving 1977** — **owed**: not searched in this pass. With the 1973 paper, the second
  of the file's two firm human counts; the citing line records 47 human cords. *(Line 170.)*
- **Tomlinson & Irving lineage** — **the same body of work as the two Tomlinson keys above**,
  written as a lineage in the closing paragraph. **Owed at the citing lines: use one key, or say
  what the lineage contains.** *(Line 319.)*
- **Tomlinson, Irving & Rebeiz 1973** — **owed**: not searched in this pass. *(Line 169.)*
- **Watson, Paxinos & Kayalioglu 2009** — **owed**: not searched in this pass. Declared on the
  citing line as a soft secondary compilation, which is the file recording its own provenance
  correctly. *(Line 174.)*
