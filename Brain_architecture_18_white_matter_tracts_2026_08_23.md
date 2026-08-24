# Brain architecture — 18 white matter tracts

**Date:** 2026-08-23
**Derived from:** `human_brain_18_white_matter_tracts_2026_07_25.md` — five entries: the corpus
callosum, the internal capsule, the fornix, the arcuate / superior longitudinal fasciculus, and the
medial longitudinal fasciculus.
**One source file for content.** The rung spec was in hand.

**Cross-file checks contained in this file.** Each line names another file whose shared edges with
this one are diffed and stemmed.

- `07_anterior_temporal_lobe`. **Three routed edges checked. The temporal pole's four association
  pathways are declared there by name, and that file records edge attribution as established only for
  the uncinate fasciculus; the uncinate's orbitofrontal / ventrolateral limb is two-ended; and the
  middle longitudinal fasciculus is named there as having an entry here, which it does not have here
  or anywhere.**
- `10_cerebellum`. **Checked from that file's side by locating the endpoints, not by an end-to-end
  read here. No edge of that file names a structure in this one as an endpoint.** What it names, on
  seven edges and always as the route rather than the endpoint, is the **three cerebellar
  peduncles** — superior, middle and inferior — and **none of the three has an entry here or
  anywhere**, this file's entries being the corpus callosum, the internal capsule, the fornix, the
  arcuate / superior longitudinal fasciculus and the medial longitudinal fasciculus. **This is the
  same class of gap as the middle longitudinal fasciculus above and it is the larger instance**: the
  peduncles are where the conduction times for every cerebellar edge would live, and every edge in
  that section reads *to derive*. **Inherited from that file's source; not repairable here.**

**Far ends are otherwise not read, and the response taken is to record the dependency rather than
fetch it.** Routed edges reach into files 2, 3, 5, 6, 7, 8, 11, 12, 13, 14, 15 and 16 — twelve of the
nineteen others. Each edge below names the file its far end sits in and the state of that far end's
declaration as the source records it; **no far end's content is written from memory.**

---

## 0. What this section is

**Every entry here computes nothing.** Five transmission-only structures: they carry other entries'
edges, no synapse occurs in any of them, and their neuron and synapse slots read **none**. This is
the class the entry template was not written for, and it fills the template unchanged with two fields
reading in ways no grey-matter entry does.

- **34 routed-edge declarations — 15 in, 19 out — and zero internal edges.** Not one of the five
  entries has an internal edge, and in each case that is a **positive statement**: no synapse occurs
  in a tract, so its sub-elements are parallel channels rather than a circuit. **This is the first
  section in which "internal data flow: not applicable" is the correct reading everywhere**, rather
  than a gap standing in for one.
- **Parameter memory is zero at every entry, and it is zero for a stronger reason than a
  transducer's.** A transducer stores no threshold; a tract has no neurons to store one in.
- **The one firm number in the file is the corpus callosum's axon count**, about 200 million, counted
  by electron microscopy in human material.

**And the section carries the substrate for something no other section can supply.** A tract is
where a conduction time would be derived from — fibre calibre, myelination, and length. **Section 2b
records what the file actually holds against what a latency needs, and the gap is specific.**

---

## 1. Endpoint kinds

The source's rule is that an endpoint is a named region with an entry of its own. This section's 34
routed edges land on four kinds of thing, and a fifth case appears here that does not appear in a
grey-matter section.

| kind | count | state |
|---|---|---|
| named region with an entry | 21 | fine |
| named region with **no entry anywhere** | 2 | a gap with a named repair |
| **two named regions, one with an entry and one without** | 1 | the fornix's septal return |
| named regions, and **no entry declares the routed edge** | 2 | the two smaller commissural limbs |
| a **class, intrinsic to a tract** | 4 | not a defect — see below |
| a **class, resolvable and owed** | 3 | a gap with a named repair |
| a **stream** rather than a region | 1 | not repairable by naming |

**The three regions with no entry anywhere are two standing items and one new one.** The **red
nucleus** and the **pontine nuclei** take corticorubral and frontopontine fibres through the internal
capsule's posterior and anterior limbs; neither has an entry in any of the twenty files, and the
corticopontine stage is recorded elsewhere as a processing stage rather than a relay, so **a computing
stage sits inside the cerebro-cerebellar loop with no slot and this section adds two more routed
edges pointing at it.** The **septal nuclei** consume the fornix's pre-commissural limb and likewise
have no entry.

**A class endpoint at a tract is not the same defect it is at a grey-matter entry, and the source says
why.** A commissure linking most of the cortex to most of the cortex has no smaller honest producer,
so *the cerebral cortex of either hemisphere* and *homotopic cortex of the opposite hemisphere* are
**intrinsic to the structure rather than failures of the line**. The same holds for the internal
capsule's *the cerebral cortex* and *the thalamus*. **What is resolvable is which region-to-region
edges are actually declared as routed through the tract**, and the entries below carry those by name.

**Three class endpoints are not intrinsic and are marked as owed at the source**: *heterotopic cortex
of the opposite hemisphere*, where no entry in the source declares a heterotopic callosal edge;
*occipito-temporal cortex*, where the ventral stream the tract is said to carry runs between entries
in files 1 and 7 and neither declares a routed edge; and *the cingulate midline nodes*, which is the
one class endpoint with four far ends declaring it by name.

**The two stream endpoints are a kind this project has not met before.** *The ventral semantic stream*
and, at the temporal pole, a set of four pathways with no edge attributed to any but one. A stream is
neither a region nor a class of regions — it is a claim about a route, and **an edge whose target is a
route has no consumer at all.**

---

## 2. Structural invariants

### 2a. Whole-pathway co-instantiation

Every tract exists and is live from the outset; a cable does not come online later. Conformance is
noted per entry, and three statements hold across the section.

- **Satisfiable for the Papez limb, and this section is what closed it.** Hippocampal formation →
  fornix post-commissural limb → mammillary bodies → mammillothalamic tract → anterior thalamus →
  cingulate and retrosplenial cortex. Every stage has an entry, and the fornix's own edge is declared
  at both region ends in files 8, 12 and 14. **The mammillothalamic tract itself has no entry**, so
  the loop is traceable through regions and not through all of its cabling.
- **Not satisfiable for the corticorubral and frontopontine limbs**, whose consumers do not exist.
- **The mirror case, and it is this section's own.** Three tracts have a stated function and **no
  declared traffic at either end** — the anterior commissure, the posterior commissure, and the
  inferior fronto-occipital fasciculus. A tract with no routed edge is the mirror of a region named on
  an edge with no entry, and **it fails more silently**, because the entry reads as complete on its
  own and no diff over endpoints will ever reach it. **Co-instantiation is vacuous for a structure
  nothing routes through**: it is live from the outset and carries nothing.

### 2b. Per-edge latency — and this is the section that was supposed to supply it

Every routed edge carries a nonzero, finite, heterogeneous latency in real time units. **All 34 read
*to derive*.**

**That is not the finding. The finding is what this section holds against what a conduction time
needs.** A conduction time is a length divided by a velocity, and a velocity is derived from fibre
diameter and myelination. The file's myelination and axon slots hold:

| entry | fibre calibre | myelination | length |
|---|---|---|---|
| corpus callosum | thin and slow rostrally; a minority of **3–5 µm** large fast fibres crossing isthmus and splenium | chiefly myelinated; **g-ratio tracks the thin-to-thick gradient** — no figure | not recorded |
| internal capsule | not recorded | heavily myelinated | not recorded |
| fornix | not recorded | myelinated | not recorded |
| arcuate / superior longitudinal fasciculus | not recorded | myelinated association fibres | not recorded |
| medial longitudinal fasciculus | not recorded | heavily myelinated, among the earliest to myelinate; **g-ratio unknown** | not recorded |

**One fibre-calibre figure across five tracts, no g-ratio anywhere, and no length anywhere.** So the
section that is the physical substrate of every latency in the map supplies, for one tract, the
diameter of its fast minority — and nothing else that a velocity needs. **Even with a velocity there
would be no time, because no tract in the file has a length.** *(The slot contents are Class 1 from
the source. That length is the missing third term, and that its absence blocks the derivation
independently of the other two, is Claude's reading.)*

**The gradient is itself a finding about the invariant.** The callosum's fibres run thin and slow
rostrally to large and fast caudally, and the source records that as a property of the *sectors*.
So **one tract carries a spread of conduction velocities across its own cross-section** — which is
the per-edge-latency invariant's heterogeneity appearing inside a single structure, not only between
structures.

**No global clock may be assumed**, and nothing in this section supplies one.

---

## 3. Corpus callosum — the great interhemispheric commissure

- **Function → structure.** The largest white-matter tract in the brain: interhemispheric
  transmission linking mostly homotopic and some heterotopic cortex, with either integrating or
  inhibitory (lateralising) effect. Topographic — rostrum and genu carry prefrontal traffic on thin
  slow fibres, the body carries motor and somatosensory, the isthmus and splenium carry parietal,
  temporal and occipital on the largest and fastest fibres. **The functional sign is not two kinds of
  fibre**: all callosal fibres are excitatory pyramidal axons and the inhibitory effects reported in
  every modality are feedforward, through local interneurons the fibres excite. In the auditory case
  the lateralising effect is measurable — callosotomy abolishes a left–right asymmetry rather than
  merely disconnecting it, **which makes the asymmetry an equilibrium this edge maintains.**

  **Laminar routing is asymmetric between origin and termination.** Origin is layers 3 and 5, about
  90% of the auditory projection; termination is throughout layers 2–6, densest in 2 and 3 and
  **sparsest in layer 4**. **The callosal input avoids the layer the thalamic driver targets.**

  **"Homotopic" describes something different in each modality.** In vision the connections are
  restricted to the representation of the **vertical meridian**; in somatosensation to **proximal
  body** representations — in both, to the representational midline where two half-maps must be
  joined. In audition there is **no such midline** and the connections are **widespread across the
  entire tonotopic map.**

  **Sub-elements: five sectors** — rostrum, genu, body (anterior, central and posterior parts),
  isthmus, splenium. They meet the sub-element test on two grounds at once: different traffic to
  different targets, **and** different fibre calibre, which is a transmission-rate difference and
  therefore a property of the payload's timing.

  **Internal edges: not applicable** — no synapse occurs here, so the sectors are parallel channels
  and not a circuit. A positive statement.

  **This entry is four tracts, not one.** The anterior, hippocampal and posterior commissures have
  their own endpoints and none shares this tract's five-sector topography, so they are not
  sub-elements of it. **Recorded as a bundle; the split is owed at the source and is not made here.**

- **Inputs.** Three routed edges. *(Routing statements, not payload transfers. Fan-in reads **none**
  throughout, because no synapse occurs here.)*
  - **← the cerebral cortex of either hemisphere**, from callosal projection neurons in **layers 3
    and 5** — routing only. Fan-in: none. **A class endpoint, and intrinsic to the structure.**
  - **← the primary auditory cortex**, contralateral, through the **central body, posterior body and
    dorsal splenium** — routing only; the payload at the region ends is the same frequency band's
    activity from the other hemisphere, **which sharpens rather than adds**. Fan-in: none. *(File 2,
    both region ends. Two-ended, and the sector attribution is declared there and matched here.)*
  - **← the inferior frontal gyrus**, contralateral — routing only; payload owed at the region ends.
    Fan-in: none. *(File 11; two-ended.)*

- **Outputs.** Four routed edges.
  - **→ the homotopic cortex of the opposite hemisphere**, terminating throughout **layers 2–6**,
    densest in 2 and 3, **sparsest in layer 4** — routing only. Fan-out: none. **Same class endpoint
    as the input limb and the same reason.**
  - **→ heterotopic cortex of the opposite hemisphere** — routing only. Fan-out: none. **A separate
    limb, not a variant**: sensory association cortices carry proportionally more of this traffic than
    primary sensory cortices, so the two limbs have different origins and different densities. **A
    class endpoint, and no entry in the source declares a heterotopic callosal edge.** *(Owed at the
    source.)*
  - **→ the contralateral temporal lobe, olfactory structures and amygdala**, via the **anterior
    commissure** — routing only. Fan-out: none. **No entry in the source declares an edge routed
    through the anterior commissure.** *(Owed at both ends.)*
  - **→ the contralateral hippocampal formation** via the **hippocampal commissure**, and **→ the
    contralateral pretectal and vertical-gaze structures** via the **posterior commissure** — routing
    only. Fan-out: none. **Neither string appears anywhere in the source outside this entry.** The
    posterior commissure's stated function belongs to structures that do have entries — the pretectum
    and the gaze integrators in file 15 — and that entry does not name it. *(Owed at both ends.)*

- **Sizing.** Basis: **whole**, a midline commissure. **Neurons: none** (a fibre tract, with a few
  interstitial intracallosal neurons). **Synapses: none. Parameter memory: zero** — and zero because
  there are no neurons to hold a threshold, not because a threshold was struck.
  **Axons: about 200 million**, range 200–300 million, by electron microscopy in human material —
  **the one firm number in the section**, and the callosum's well-defined borders are what make it one
  of the few exactly-countable tracts. Cross-sectional area about **500–700 mm²**.
  **Grey-matter volume: not applicable. White-matter volume:** the single largest white-matter
  structure in the brain; **no figure recorded.**

- **Shape.** **Transmission-only: a routing index, rank 1** — not an activity array. Recording it as a
  zero-length tensor would assert state it does not hold.
  **The extent is bounded and not fixed, and the two bounds are three orders apart.** At routed-edge
  granularity the index has **7** entries. At line granularity it has one entry per axon —
  **200–300 million.** Which applies is downstream of the inter-structure connection topology, which
  is unset, so **the extent reads: 7 at edge granularity, 200–300M at line granularity, and the choice
  between them is not this rung's.**
  **The per-sector partition is unknown**, so the index cannot be split across the five sectors even
  though every routed edge is attributed to one.

- **Edge latency.** All 7 routed edges **to derive** — and see §2b: this is the one entry with a fibre
  calibre, and it has neither a g-ratio figure nor a length.

- **Invariant conformance.** Co-instantiation: satisfied for the tract itself; **vacuous for three of
  the four tracts bundled here**, which carry no declared traffic at either end. Per-edge latency:
  satisfied in form, all to derive, **and heterogeneous within this single structure** because fibre
  calibre varies rostrocaudally across its own sectors.

- **Justification (biological).** **The interesting claim is not that the two hemispheres are
  connected — it is what they are connected *for*, and the description says three different things
  under one word.** Where a sensory map has a representational midline, the callosum joins two
  half-maps and its connections are restricted to the seam: the vertical meridian in vision, proximal
  body in somatosensation. Where there is no midline to join, as in audition, the connections are
  widespread across the whole map. **So a callosal edge is a seam-stitching device in one modality and
  a whole-map coupling in another**, and a build that read the visual case as the general one would
  under-provision the auditory bandwidth by a wide margin.
  The second claim is about sign. All the fibres are excitatory and the inhibition is feedforward
  through interneurons they excite, **so the lateralising effect is a property of the target circuit
  and not of the cable** — and the callosotomy result makes it an equilibrium the edge actively
  maintains rather than a static asymmetry it merely reveals.

---

## 4. Internal capsule — the great projection tract

- **Function → structure.** The compact projection highway funnelling every corticofugal and
  thalamocortical fibre between the caudate nucleus and thalamus medially and the lentiform nucleus
  laterally. A bottleneck whose small lacunar lesions cause dense hemiplegia.

  **Sub-elements: five parts**, each carrying a different fibre system to a different target, and
  every routed edge below is attributed to one of them. **Anterior limb** — frontopontine fibres and
  the anterior thalamic radiation, serving prefrontal cortex. **Genu** — corticobulbar fibres to the
  cranial-nerve motor nuclei. **Posterior limb** — the corticospinal tract, the corticorubral fibres,
  and the superior thalamic radiation. **Retrolenticular part** — the optic radiation, lateral
  geniculate nucleus to primary visual cortex. **Sublenticular part** — the auditory radiation, medial
  geniculate nucleus to primary auditory cortex.

  **Internal edges: not applicable.** Parallel channels, not a circuit.

- **Inputs.** Two routed edges. *(Routing statements; fan-in reads **none** throughout.)*
  - **← the cerebral cortex**, corticofugal fibres from every lobe — routing only. Fan-in: none.
    **A class endpoint, intrinsic to the structure.** The named corticofugal edges other entries
    declare as routed through this tract are the **corticospinal tract from the primary motor
    cortex** *(files 5 and 16, the latter naming this tract explicitly)* and the corticothalamic
    return traffic below.
  - **← the thalamus**, thalamocortical fibres from every relay nucleus — routing only. Fan-in: none.
    **A class endpoint.** The named thalamocortical edges declared as routed here are the **optic
    radiation** *(file 12 to file 1)*, the **auditory radiation** *(to file 2)*, the **superior
    thalamic radiation** *(file 5)*, and the **anterior thalamic radiation** *(file 12's mediodorsal
    nucleus to file 11)*.

- **Outputs.** Four routed edges.
  - **→ the brainstem and spinal cord**, through the **posterior limb** and **genu** — routing only;
    the corticospinal and corticobulbar motor commands, typed at their cortical origins and at the
    ventral horn and cranial-nerve nuclei that consume them. Fan-out: none. *(File 16 declares this
    tract by name. Two-ended.)*
  - **→ the thalamic reticular nucleus**, from corticothalamic fibres traversing this tract — routing
    only; the collateral copy of the cortex's outgoing traffic that the reticular nucleus gates on.
    Fan-out: none. *(File 12, which records that only about three quarters of the corticothalamic
    fibres passing through gave visible collaterals there. Two-ended, **and that quarter is a finding
    about this tract rather than about the nucleus: the capsule is not a uniform bundle at this
    level.**)*
  - **→ the red nucleus**, corticorubral fibres through the **posterior limb** — routing only.
    Fan-out: none. **This consumer has no entry in any of the twenty files.** *(Owed at a consumer
    that does not yet exist.)*
  - **→ the pontine nuclei**, frontopontine fibres through the **anterior limb** — routing only.
    Fan-out: none. **This consumer has no entry in any of the twenty files**, and it is **the
    load-bearing half**, because the corticopontine stage is recorded elsewhere as transforming the
    payload rather than relaying it. *(Owed at a consumer that does not yet exist.)*

- **Sizing.** Basis: **per side.** **Neurons: none. Synapses: none. Parameter memory: zero.**
  **Axons:** carries the **corticospinal tract at about 1 million axons per side** — a classic order
  estimate, with about **1.1 million pyramidal-tract fibres above the decussation** from a secondary
  compilation — plus the thalamocortical radiations, counts unknown. **The per-limb split of that
  total is unknown**, and that split is precisely what would be needed to size any one of the routed
  edges above.
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**

- **Shape.** **Routing index, rank 1.** Extent: **6** at routed-edge granularity; at line granularity
  the corticospinal component alone is **~1–1.1 million**, and the radiations are unknown, so the
  full line count is **to derive**. **The per-limb partition is unknown**, so the index cannot be split
  across the five parts even though every routed edge is attributed to one.

- **Edge latency.** All 6 routed edges **to derive.** No fibre calibre, no g-ratio and no length are
  recorded, so nothing here supports a derivation.

- **Invariant conformance.** Co-instantiation: **not satisfiable for two of its six routed edges**,
  whose consumers — the red nucleus and the pontine nuclei — have no entry anywhere. Per-edge latency:
  satisfied in form, all to derive.

- **Justification (biological).** **This entry is where the map's geometry becomes a resource
  constraint, and the description says so through a lesion.** Every corticofugal and thalamocortical
  fibre in the hemisphere passes through one compact bundle, which is why a lacunar lesion of a few
  millimetres produces dense hemiplegia where a cortical lesion of the same volume would not. **A
  bottleneck is an architectural fact and not only a clinical one**: it says the map's long-range
  traffic is not distributed but funnelled, and that the funnel is organised by destination rather
  than by origin — five limbs, five fibre systems, five targets.
  **And the un-collateralised quarter is the entry's sharpest datum.** About three quarters of the
  corticothalamic fibres crossing this tract give a visible collateral to the reticular nucleus and
  roughly a quarter do not, **so the copy the thalamic gate runs on is a sample of the cortex's
  outgoing traffic and not all of it.** That is a claim about what the gate can possibly know.

---

## 5. Fornix — the hippocampal output tract

- **Function → structure.** The principal output and return-input pathway of the hippocampal
  formation: fimbria → crus → body → columns, splitting at the anterior commissure into a
  **post-commissural** limb to the mammillary bodies and anterior thalamus — the Papez memory
  circuit — and a **pre-commissural** limb to the septum and basal forebrain, through which the
  septo-hippocampal cholinergic and theta-pacing fibres return. Topography: the lateral fornix carries
  the anterior hippocampus and the medial fornix the posterior; the left carries verbal and the right
  visuospatial memory.

  **Sub-elements: the pre-commissural and post-commissural limbs**, on the strongest ground in this
  section — **they run in opposite functional directions to entirely different targets**, and every
  routed edge is attributed to one of them. **The fimbria, crus, body and columns are properties of
  the tract's course, not sub-elements**: the same fibres pass through all four in sequence. A second
  division does meet the test — **lateral fornix carries the anterior hippocampus and medial fornix
  the posterior**, a different origin and therefore a different payload — and **whether it is
  preserved as far as the targets is owed.**

  **Internal edges: not applicable.**

- **Inputs.** Four routed edges. **This is the best-declared tract in the section** — six of its routed
  edges are written at both region ends, in four different files, by passes that did not consult each
  other. *(Fan-in reads **none** throughout.)*
  - **← the hippocampal formation**, from the **subiculum**, into the **fimbria** — routing only; the
    payload at the region ends is the **completed episode**, the bound retrievable pattern addressable
    by any fragment of itself, and **only partly writable there**, since an episode has no units and
    no frame. Fan-in: none. *(File 8, which declares an edge to this tract by name and explains it as
    a routing statement, then writes the regions it reaches as their own edges. Two-ended, and the far
    end already uses this convention.)*
  - **← the medial septum, cholinergic cells** — routing only; the payload at the region ends is a
    cholinergic modulatory signal. Fan-in: none. *(Files 13 and 8, each naming this tract and the
    pre-commissural limb. Two-ended.)*
  - **← the medial septum, parvalbumin-expressing GABAergic pacemaker cells** — routing only; the
    payload at the region ends is the **theta timing reference**. Fan-in: none. *(Files 13 and 8.
    Two-ended.)*
  - **← the medial septum, glutamatergic cells** — routing only; the payload at the region ends is a
    **tonic drive**. Fan-in: none. *(Files 13 and 8. Two-ended.)*
    **The three septal limbs are three lines because they are three lines at both region ends** —
    three cell populations in one nucleus with three different payloads riding one tract. A tract
    entry that collapsed them would lose a distinction the grey-matter entries had already made.

- **Outputs.** Three routed edges.
  - **→ the mammillary bodies and the anterior thalamic nuclei**, through the **post-commissural
    limb** — routing only; the completed episode. Fan-out: none. *(File 8 as producer; file 12's
    anterior nuclei name the subiculum and this limb; file 14 holds the mammillary end. Two-ended.)*
    **This is the Papez limb, and every stage of it now has an entry** — though the
    **mammillothalamic tract** that carries its next leg does not.
  - **→ the hypothalamus** — routing only; payload owed at both region ends. Fan-out: none. *(Files 8
    and 14, each naming this tract. Two-ended, owed at both.)*
  - **→ the septum and basal forebrain**, through the **pre-commissural limb** — routing only;
    payload owed at the region ends. Fan-out: none. *(File 8 names this limb.)* **The consumer is
    split:** the basal forebrain has an entry in file 13 and **the septal nuclei have no entry in any
    of the twenty files.** **So the return arm of the septo-hippocampal loop has a described tract, a
    described payload at one end, and no entry for the structure at the other.**

- **Sizing.** Basis: **per side.** **Neurons: none. Synapses: none. Parameter memory: zero.**
  **Axons:** soft, no clean human count pinned; classic order about **1 million**. **The per-limb
  split is unknown**, and the pre-commissural limb's share is what would size the septo-hippocampal
  return.
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**

- **Shape.** **Routing index, rank 1.** Extent: **7** at routed-edge granularity, **~1 million** at
  line granularity on a soft order estimate. **The per-limb partition is unknown.**

- **Edge latency.** All 7 routed edges **to derive.** Myelination reads *myelinated tract* with no
  g-ratio; no calibre and no length are recorded.
  **One payload in this entry is itself a timing signal**, which makes the missing latency load-bearing
  rather than incidental: the parvalbumin-expressing septal limb carries a **theta timing reference**,
  and a timing reference delivered over a cable of unknown delay is a reference to an unknown phase.

- **Invariant conformance.** Co-instantiation: **not satisfiable for the pre-commissural return**,
  whose septal consumer has no entry. Satisfied for the Papez limb, which is the section's one fully
  instantiable route. Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** **This tract is the reason the hippocampal formation can be a
  memory system rather than a memory store.** Its two limbs run in opposite functional directions to
  different targets: the post-commissural limb carries the completed episode out to the Papez circuit,
  and the pre-commissural limb carries the septal return in — cholinergic modulation, a theta timing
  reference, and a tonic drive, on three separate lines from three cell populations in one nucleus.
  **A structure whose output cable also carries its own pacing signal is a loop and not a pipeline**,
  and the description makes that legible only because the three septal payloads were typed separately
  at both region ends before this tract had an entry.

---

## 6. Arcuate fasciculus / superior longitudinal fasciculus — the dorsal language tract

- **Function → structure.** The dorsal-stream association tract arching from temporoparietal cortex —
  the posterior superior temporal gyrus, the sylvian parieto-temporal area and the supramarginal
  gyrus — to the frontal lobe at Broca's area and premotor cortex: the audiomotor and phonological
  "where" pathway, **left-dominant for language.** Part of the superior longitudinal fasciculus
  system.

  **Sub-elements: the three numbered branches of the superior longitudinal fasciculus, I, II and
  III**, which meet the test because they connect different cortical territories, and **branch III is
  already named on the supramarginal routed edge by both of its region ends.** The **arcuate** is the
  arching temporo-frontal component of the same system; **whether it is a branch of that system or a
  tract adjacent to it is contested in the literature and is recorded as contested**, not resolved by
  preference — the same treatment the source gives the dispute over layer 4B.

  **Internal edges: not applicable.**

  **This entry is five tracts, not one.** The **inferior longitudinal**, **inferior fronto-occipital**,
  **uncinate** and **cingulum** fasciculi are separate association tracts with separate endpoints, and
  none is a branch of the superior longitudinal system. **Recorded as a bundle; the split is owed at
  the source.** The bundling has a visible cost: **three of the five carry no declared traffic while
  the cingulum has four declarations.**

- **Inputs.** Three routed edges. *(Fan-in reads **none** throughout.)*
  - **← the supramarginal gyrus** — routing only; the payload at the region ends is a **praxis /
    action-sequence code** and, on the left, a **phonological code** — the sound-form of words for the
    articulatory route, only partly writable there. Fan-in: none. *(File 6 as producer and file 11's
    Broca's area as consumer, both naming this tract and **branch III** specifically. Two-ended.)*
  - **← the posterior superior temporal gyrus and the sylvian parieto-temporal area** — routing only;
    payload owed at the region ends. Fan-in: none. *(File 11 declares it; file 2's auditory entries
    name this tract as carrying the stream forward. Two-ended.)*
  - **← the temporal pole**, over the **uncinate fasciculus**, the **inferior longitudinal
    fasciculus**, the **middle longitudinal fasciculus** and this tract — routing only; payload owed.
    Fan-in: none. *(`07_anterior_temporal_lobe` declares all four by name and records that which pathway carries
    which of its edges is established only for the uncinate. **That entry also states these tracts have their
    own entries here, which is wrong for the middle longitudinal fasciculus** — it has no entry here
    or anywhere. Owed as a cross-file edit at `07_anterior_temporal_lobe`.)*

- **Outputs.** Five routed edges.
  - **→ Broca's area and premotor cortex** — routing only. Fan-out: none. *(Files 6 and 11,
    reciprocally with the supramarginal input. Two-ended.)*
  - **→ the orbitofrontal and ventrolateral prefrontal cortex**, over the **uncinate fasciculus** —
    routing only; payload owed at the region ends. Fan-out: none. *(`07_anterior_temporal_lobe` declares this tract by
    name, and it is the one association pathway there whose edge attribution is established.
    Two-ended.)*
  - **→ the cingulate midline nodes**, over the **cingulum** — routing only. Fan-out: none. **Four
    entries declare this tract by name** — the anterior cingulate cortex in file 11 and the
    midcingulate, posterior cingulate and retrosplenial entries in file 17, the last three recording
    it as routing rather than as an edge, **which is the convention this entry uses.** Two-ended.
  - **→ occipito-temporal cortex**, over the **inferior longitudinal fasciculus** — routing only.
    Fan-out: none. **Named at one far end only** *(`07_anterior_temporal_lobe`)*. **The ventral "what" stream this tract is
    said to carry runs between entries in files 1 and 7, and neither declares an edge routed through
    it.** *(Owed at both ends.)*
  - **→ the ventral semantic stream**, over the **inferior fronto-occipital fasciculus** — routing
    only. Fan-out: none. **This string appears nowhere in the source outside this entry**: no entry
    names it, no edge is declared as routed through it, and its endpoints are given here as a stream
    rather than as regions. **A tract with a stated function and no traffic.** *(Owed: attribute an
    edge to it, or withdraw it.)*

- **Sizing.** Basis: **per hemisphere**, and this is the one entry in the section where the basis
  carries a functional claim rather than a convention: the tract is **left-dominant for language**, so
  the two sides are not copies.
  **Neurons: none. Synapses: none. Parameter memory: zero.**
  **Axons:** counts largely unknown, **and one rare absolute estimate exists and does not fit the
  slots.** Direct connections between the posterior and anterior language regions are **surprisingly
  sparse — under about 5% of the axons in the arcuate / superior longitudinal trunk** — with a median
  of about **6,200 axons between areas within a hemisphere** and about **1,300
  interhemispherically.** **That figure counts inter-areal axons rather than contacts per cell, so it
  is a fan measure that fits neither the fan-in nor the fan-out slot**, and the far end (file 11)
  records the same mismatch and marks it owed. *(Owed at both ends: reconcile the two measures.)*
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**

- **Shape.** **Routing index, rank 1.** Extent: **8** at routed-edge granularity; at line granularity
  **to derive** — the trunk's total is not recorded, and the only absolute figure available is the
  6,200-axon inter-areal median, which is a different quantity. **The per-branch partition across I,
  II and III is unknown.**

- **Edge latency.** All 8 routed edges **to derive.** Myelination reads *myelinated association
  fibres*; no calibre, no g-ratio, no length.

- **Invariant conformance.** Co-instantiation: satisfied for the tract; **vacuous for the inferior
  fronto-occipital fasciculus**, which carries no declared traffic at either end, and **unstatable for
  the inferior longitudinal fasciculus**, whose stream is named at one end only. Per-edge latency:
  satisfied in form, all to derive.

- **Justification (biological).** **The sparse-connection finding is the entry's real content and it
  cuts against the tract's own headline.** This is called the dorsal language pathway, and the direct
  posterior-to-anterior connections are under about 5% of its axons — a median of roughly 6,200
  between areas. **So the language route is not a thick dedicated cable between two regions; it is a
  thin direct component inside a much larger bundle carrying other traffic.** A build that provisioned
  the arcuate from its reputation would over-provision the language edge by more than an order of
  magnitude.
  The second point is about laterality. **Left-dominance for language means the per-hemisphere
  convention here is not bookkeeping** — the two sides carry different functional loads over the same
  anatomy, which is exactly the asymmetry the per-hemisphere ruling exists to keep visible.

---

## 7. Medial longitudinal fasciculus — the gaze-yoking brainstem tract

- **Function → structure.** A paired, heavily myelinated tegmental tract running the length of the
  brainstem beneath the floor of the fourth ventricle and the cerebral aqueduct, from the rostral
  midbrain to the cervical cord. **The common cable of conjugate gaze**: it carries the
  vestibulo-ocular reflex command from the vestibular nuclei forward to the ocular motor nuclei, it
  **yokes the two eyes** by carrying the abducens internuclear axons across to the contralateral
  medial-rectus motor pool, and it carries the medial vestibulospinal fibres down to the cervical
  cord. Its lesion produces **internuclear ophthalmoplegia** — adduction fails on the side of the
  lesion while the abducting eye shows nystagmus — **which is the clinical signature that makes the
  yoking edge visible as a separate thing from either motor nucleus.**

  **A naming caution.** The **rostral interstitial nucleus of the medial longitudinal fasciculus** is
  a grey-matter nucleus named for its position beside this tract, **not a part of it.** It is the
  vertical saccade burst generator, it is named on edges in files 14 and 15, and it belongs to the
  reticular-formation entry. **The string appears in the source in two entirely different roles**, and
  a name-matching diff will collect the nucleus with the tract.

  **Sub-elements: an ascending limb and a descending limb** — different targets and different
  payloads, with the ascending limb carrying the vestibulo-ocular and yoking traffic rostrally and the
  descending limb carrying the medial vestibulospinal fibres caudally. Every routed edge is attributed
  to one of them.

  **Internal edges: not applicable.**

- **Inputs.** Three routed edges. *(Fan-in reads **none** throughout.)*
  - **← the vestibular nuclei** — routing only; the payload at the region ends is the
    **vestibulo-ocular reflex command**, an eye-velocity signal **equal and opposite to head
    rotation**, driven chiefly by the semicircular-canal line, and the fastest gaze-stabilising
    reflex. Fan-in: none. *(Files 3 and 15, both naming this tract. Two-ended.)*
  - **← the abducens nucleus**, from its **internuclear neurons** — routing only; the payload at the
    region end is the yoking signal that makes the two eyes move together in horizontal gaze. Fan-in:
    none. *(File 15's ocular-motor-nuclei entry names this tract and records the edge as one that
    should be typed as an internal edge, marking it owed. Owed at that entry.)*
  - **← the gaze neural integrators** — the **nucleus prepositus hypoglossi** with the medial
    vestibular nucleus for horizontal, and the **interstitial nucleus of Cajal** for vertical —
    routing only; the payload at the region ends is **eye position**, the integrated signal that holds
    the eye where the burst put it. Fan-in: none. **Neither far end names this tract.** *(Owed at both
    ends. This line is Class 3 at the source and is not transcribed from a declaring far end.)*

- **Outputs.** Three routed edges.
  - **→ the ocular motor nuclei** — the **oculomotor**, **trochlear** and **abducens** nuclei —
    routing only. Fan-out: none. *(Files 3 and 15, both naming this tract. Two-ended.)* **This is the
    edge that makes the entry worth writing**: one of the few routed edges in the source declared,
    named and typed at both region ends before its tract had an entry at all.
  - **→ the contralateral oculomotor medial-rectus pool**, from the abducens internuclear neurons —
    routing only. Fan-out: none. *(Owed at file 15.)* **This limb crosses the midline and no other
    limb of this tract does, and that crossing is what conjugate horizontal gaze consists of.**
  - **→ the cervical spinal cord**, as the **medial vestibulospinal** fibres — routing only; the
    payload at the region ends is a head- and neck-stabilising postural command. Fan-out: none.
    **Neither far end names this tract**, and **neither separates the medial vestibulospinal tract
    from the lateral one** — the lateral descends in the ventral funiculus and the medial descends
    here, to different targets and different segmental levels. *(Owed at both ends: split the
    vestibulospinal endpoint into its medial and lateral limbs. Class 3 at the source.)*

- **Sizing.** Basis: **per side** — the tract is paired. **Neurons: none. Synapses: none. Parameter
  memory: zero.** **Axons: unknown, at either limb. The per-limb split is unknown**, as at the other
  tracts in the section.
  **Grey-matter volume: not applicable. White-matter volume: not recorded.**

- **Shape.** **Routing index, rank 1.** Extent: **6** at routed-edge granularity; at line granularity
  **to derive** — no axon count is recorded at either limb. **The per-limb partition is unknown.**

- **Edge latency.** All 6 routed edges **to derive** — **and this is the entry where that reads worst.**
  Myelination is recorded as **heavily myelinated and among the earliest tracts in the brain to
  myelinate**, which is a qualitative statement that speed matters here; the **g-ratio is explicitly
  unknown**, no calibre is recorded, and no length is recorded. **So the description says this cable is
  built for speed and supplies no term of the velocity.**

- **Invariant conformance.** Co-instantiation: satisfied — every region this tract connects has an
  entry, which is true of no other entry in the section. **The yoking limb is unstatable below the
  structure level**, because its far end is recorded as an internal edge that has not been typed.
  Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** **This entry is the section's argument that a tract can be a
  computation's substrate without computing.** Conjugate gaze is not a property of either ocular motor
  nucleus; it is a property of the cable that yokes them, and the clinical signature proves it — a
  lesion of the tract dissociates the two eyes while both motor nuclei remain intact. **So the
  structure that computes nothing is the structure whose loss removes the function.**
  The timing claim is sharper here than anywhere else in the section. The vestibulo-ocular reflex is
  described as the **fastest gaze-stabilising reflex**, and the tract that carries it is **among the
  earliest in the brain to myelinate.** Both statements are about conduction speed, and **the entry
  carries neither a g-ratio nor a calibre nor a length** — so the one tract in the section whose
  function is explicitly a speed claim is the one with the fewest terms toward a velocity.

---

## 8. Section totals

**Parameter memory is zero at every entry, and the total is zero.** Not *to derive* — zero, because
no entry has a neuron to hold a threshold.

| structure | basis | neurons | axons | parameter memory |
|---|---|---|---|---|
| Corpus callosum | whole | none | **~200M** (200–300M) | **0** |
| Internal capsule | per side | none | ~1–1.1M corticospinal; radiations unknown | **0** |
| Fornix | per side | none | ~1M, soft order | **0** |
| Arcuate / superior longitudinal fasciculus | per hemisphere | none | unknown; ~6,200 inter-areal median | **0** |
| Medial longitudinal fasciculus | per side | none | unknown | **0** |
| **total** | **mixed** | **none** | **mixed bases; not summable** | **0** |

**The axon column is not summable and is labelled so.** Three bases appear — whole, per side, per
hemisphere — and the callosum's count is the only one measured rather than estimated.

### 8a. The routing index is a fourth memory class, and it is the section's largest number

**The shape class for a transmission-only structure is a routing index, and an index is storage.** It
is not parameter memory — there is no threshold. It is not state — nothing is carried between updates.
It is not edge storage — those are the values in flight, not the map that routes them. **So the
architecture's three memory classes do not cover it**, and a reader summing the Sizing column above
will read zero for a section that will not be free to build.

Computed from the axon counts the source carries, at one index entry per line, with the destination
index width taken as ⌈log₂(lines)⌉:

| structure | lines | index width | routing index |
|---|---|---|---|
| Corpus callosum | 200M | 28 bits | **700 MB** |
| Corpus callosum, upper bound | 300M | 29 bits | **1.09 GB** |
| Internal capsule, corticospinal only | 1.0–1.1M | 20–21 bits | 2.5–2.9 MB |
| Fornix | ~1M | 20 bits | ~2.5 MB |

**The corpus callosum's routing index is larger than V1's entire threshold store**, which the sizing
method puts at 450–525 MB — for a structure whose parameter memory is zero. **That is the finding: the
cheapest structures in the map by the sizing method are among the most expensive to wire.**

**It is a bound and not a figure, in two directions at once.** The line granularity may be wrong — if
the topology routes at edge granularity the index has 34 entries across the whole section, not 200
million — and the width is a floor, since a destination index that must also name a sub-element is
wider. **Which granularity applies is downstream of the inter-structure connection topology, which is
unset.** *(The axon counts are Class 1 from the source and the arithmetic is computed. That the
routing index is a fourth memory class, and the choice of ⌈log₂(lines)⌉ as its width, are Claude's
reading, offered to be checked.)*

### 8b. Edge storage

Not sizable at this rung — it depends on the scheduling discipline, which is unset. **What can be said
is where it will be large**, and in this section that is the corpus callosum for the same reason its
routing index is: 200 million lines, each holding values in flight for the duration of a conduction
delay that is itself *to derive*.

### 8c. What this section could have supplied and does not

**A tract is where the physical substrate of a latency lives, and this is the tract file.** Across five
entries it carries **one fibre-calibre figure** (3–5 µm, for the callosum's fast minority), **no
g-ratio anywhere**, and **no length anywhere.** A conduction time needs all three.

**So every edge latency in the map reads *to derive*, and the section that would resolve them cannot.**
That is not a defect in this file — it is a statement about what the description currently holds, and
it names the measurement that would move the most: **a length and a g-ratio per tract**, which is a
smaller research target than the payload work the grey-matter sections need.
