# Brain architecture — 10 cerebellum

**Date:** 2026-08-23
**Derived from:** `human_brain_10_cerebellum_2026_08_22.md` — three structures: the cerebellar
cortex, the deep cerebellar nuclei, and the inferior olive. **One source file, and no other content
source.**

**Counting basis: whole cerebellum, both sides**, with the per-hemisphere value alongside — the
second section worked whose basis is not per hemisphere, after the basal ganglia, and the convention
names the cerebellum explicitly as one of the structures reported whole.

**This section enters with hard numbers rather than soft ones**, and it is the only one worked so far
of which that is true. The isotropic-fractionator and Danish stereology lineages both converge here,
so counts, a synapse figure and a surface area are all measured. **Two consequences follow that no
previous section could produce: the sizing arithmetic can be checked against itself in four separate
ways, and the tile calculation can be run backwards.**

**Cross-file checks contained in this file, and by what method.** Two levels of check are recorded
here and they are not equivalent.

- **Diffed at this rung, both files read end to end** — `03_other_senses`, `05_sensorimotor_loop`,
  `12_thalamus`, `13_neuromodulatory_systems`, `14_brainstem_midbrain_hypothalamus`,
  `15_cranial_nerve_nuclei`,
  `16_spinal_cord`. **Five edges
  are two-ended, two of them carrying the same measured figures at both ends; one endpoint of this
  file's is the origin of a load-bearing gap recorded in another file; and one names a thalamic
  structure with no entry.**
  **The `14_brainstem_midbrain_hypothalamus` check carries a sixth two-ended edge and three
  negatives.** That file declares **one** edge shared with this one — the fastigial limb into the
  reticular formation — and **no other structure in either file names the other**. The three
  negatives: it describes **no inferior olive**, confirming by an end-to-end read what this file had
  concluded from a search; and it confirms, from its own side, that **neither the pontine nuclei nor
  the red nucleus has an entry there**, which is where they would belong anatomically. **What the
  located-edge check had missed on the one shared edge is the naming**, and it is the defect that
  makes an edge invisible — see the deep-nuclei entry.
  **The `15_cranial_nerve_nuclei` check carries no edge into this file and resolves a claim against
  it.**
  That file names this section **once**, as one term of a four-producer bullet, and **declares no
  other cerebellar endpoint anywhere.** **No entry here declares any output reaching it**, so the
  claim is consumer-only from that side and unsupported from this one; the reading is at the deep
  nuclei entry below.
- **Checked at the far end only, by locating the matching edge in that file without reading it
  through** — `18_white_matter_tracts`. **A located edge
  confirms that the
  far end declares something; it does not confirm that the two ends agree on payload, sub-element or
  arity, and it cannot find an edge the far file writes under a name not searched for.**
  **`18_white_matter_tracts` cannot be diffed**, because what this file names there has no entry to
  diff against; see the far ends below.
- **Checked and closed as carrying no edge** — `04_dorsal_visual_parietal_stream`. It names **Purkinje
  cells of the cerebellar nodulus and uvula** as the site where the tilt-versus-translation ambiguity
  is resolved **upstream of its own input**, not as an endpoint: its edge is `← vestibular nuclei by
  way of the thalamus`, and the cerebellar stage sits behind it. **That route runs through
  `03_other_senses`, which is diffed above and which declares this file's flocculonodular limb**, so
  the claim resolves through a file already read and adds no far end here. *(Located by search, not
  by an end-to-end read; recorded as a negative so it is not re-opened.)*

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, not its number**, where the
far file is checked against this one. An endpoint with no stem is unchecked, and that is not a claim
that none exists.

**Far ends.** Edges leave into `03_other_senses`, `05_sensorimotor_loop`, `12_thalamus`,
`13_neuromodulatory_systems`, `14_brainstem_midbrain_hypothalamus` and `16_spinal_cord`. **All six
are now diffed at this rung**, per the list above. **The one far file still checked at the far end
only is `18_white_matter_tracts`**, and its marks carry the weaker warrant. **No edge of this file
names a structure there as an endpoint.** What this file names on seven edges is the **three
cerebellar peduncles** — superior, middle and inferior — always as the **route** and never as an
endpoint, and **the source records that all three have an entry nowhere**, that file's entries being
the corpus callosum, the internal capsule, the fornix, the arcuate / superior longitudinal
fasciculus and the medial longitudinal fasciculus. **This matters here for one reason: a tract is
where the physical substrate of a latency lives, and every edge in this section reads *to derive*.**
So the structures that would carry the missing conduction times are the three that have no entry.
**Inherited; §2 forbids repairing it here.** *(The peduncles' absence is Class 1 from the source. The
far file's entry list was checked by heading, not by an end-to-end read.)*
**The source's own caution is inherited for what it does not check:**
files 1, 2, 6, 19 and 20. **Files 4 and 15 have left that list**, 4 checked and carrying no edge, 15
diffed end to end and carrying a claim this file does not support.

---

## The two regions that are not here, and the loop that needs them

**The pontine nuclei and the red nucleus are named on five edges in this section and neither has an
entry in any file** — the mossy-fibre input to the cortex, the mossy limb of the deep nuclei's
collateral input, both of the deep nuclei's rubral outputs, and the descending limb of the
dentato-rubro-olivary loop. **A third name, the mesodiencephalic
junction, resolves to no entry either.**

**This is the cerebro-cerebellar loop the design file already records as not satisfiable, and this is
the section it lives in.** The design file's statement is that the loop runs through the pontine
nuclei and the red nucleus, that neither has an entry, and that **the corticopontine stage is
recorded as transforming the payload rather than relaying it** — so a computing stage sits inside the
loop with no slot.

**The source has now established what that transform is, and it is larger than "transforms the
payload" suggests.** Three findings, each of which changes what arrives at this section:

1. **It is not a copy: the relay diverges and then reconverges.** The corticopontine projection is
   markedly divergent and the pontocerebellar projection markedly convergent, and together they
   integrate cerebrocortical information before it arrives. **Each small spot of this cortex receives
   afferents from many widely separated pontine cell clusters**, so a granule cell's single mossy
   input is a mixture of spatially separated cortical sources.
2. **It is not nearly the whole cortex.** In monkey there is an almost total lack of projections from
   large parts of prefrontal and temporal cortices. The input arises from **layer 5**, and subcortical
   sources contribute only a few percent.
3. **The map is reweighted in transit, with a direction.** Within the corticopontine projections from
   visual and somatosensory areas there is a **de-emphasis of central vision and of the distal parts
   of the extremities** — *the relay discards precisely the parts of the map the cortical areas
   themselves magnify.*

**So the cerebellum does not receive cortex's state. It receives a reweighted, integrated projection
of part of it.** A region that performs that cannot be left as a name on an edge. **Owed at the
source: give the pontine nuclei an entry and type what leaves them.** Not patched here.

**Neither section owns these two alone, and that is a fact about the loop rather than an unmade
decision.** Anatomically they are brainstem; functionally they are stations on the cerebro-cerebellar
and dentato-rubro-olivary loops described here, and **the source's sections are split by data flow,
so this loop runs through two of them.**

**The brainstem section agrees, and it says so in its own invariants.** `14_brainstem_midbrain_
hypothalamus`, read end to end against this file, records both structures as having no entry
anywhere, marks them **owed as new entries belonging jointly to that section and this one**, and
carries the corticopontine *transforms-rather-than-relays* finding in its co-instantiation
paragraph. **So the two files reach the same conclusion independently and neither claims the
repair.** The repair is the source's, and it is one decision for both files rather than two.

**But the far end's attribution of where the edges are is wrong, and the correction is small and
mechanical.** That file lists these two among **six structures "named on this section's edges" with
no entry anywhere** — and they are named on **no edge in that file**, as an endpoint or as a route.
The other four of its six are on its edges; these two are on **this** file's, all five of them. **The
error matters because it aims the repair at the wrong file:** a reader deciding whether to write the
pontine-nuclei entry would look for the edges that entry must satisfy, search that section, and find
none. **Owed at `14_brainstem_midbrain_hypothalamus`: say that these two are named on
`10_cerebellum`'s edges and owed jointly.** *(The far end's list and this file's five edges are both
Class 1; that the two disagree about which file carries the edges is the finding here.)*

---

## Structural invariants

**Whole-pathway co-instantiation.** Three loops, in three different states, and the contrast is worth
stating together because it separates a repairable gap from a satisfied one:

- **The olivo-cortico-nuclear loop is closed entirely inside this section and is satisfied.** The
  inferior olive drives every Purkinje cell; the Purkinje cells inhibit the deep nuclei; the deep
  nuclei inhibit the inferior olive — *suppression of the error signal once the error is learned, the
  loop that turns the teacher off.* **All three stages have entries here, all three limbs are written
  at both ends, and none can be staged.** This is the first loop in the sections worked that is
  wholly satisfiable at this rung.
- **The cerebro-cerebellar loop is not satisfiable**, for the reason above: the pontine nuclei have no
  entry, and they compute.
- **The dentato-rubro-olivary loop — the Guillain–Mollaret triangle — has two of its three vertices
  in this file and the third nowhere.** Dentate nucleus → contralateral red nucleus → ipsilateral
  inferior olive → contralateral cerebellum. **The missing vertex is the red nucleus.**

**Crossings are load-bearing here and are carried.** The corticopontine relay is crossed; the
climbing fibres cross; the superior cerebellar peduncle decussates. **Because both the corticopontine
input and the deep nuclei's thalamic output cross, each cerebellar hemisphere serves the
contralateral cortex and the ipsilateral body.** That double crossing is exactly the case the design
file warns is easiest to lose, because both ends see a same-side connection.

**Per-edge latency.** Every edge carries a nonzero, finite, heterogeneous latency in real time units.
**Every edge in this section reads *to derive*.**

**And this section states a timing requirement as the condition on its learning signal.** The
climbing fibre's payload is *one bit with a timestamp*: **it must arrive while the error is still
present or it teaches nothing.** That is a bound on one edge's latency, stated as a functional
requirement, with no number on either side of it — neither the latency nor the width of the window it
must fall inside. **Recorded as a dangling requirement.** It is the third consecutive section whose
mechanism is a timing relation and whose timings are all unmeasured.

**A new edge class, and the design file's existing ruling covers it.** The inferior olive's internal
edge is **electrotonic coupling through gap junctions** — olivary neuron ↔ olivary neuron, carrying
subthreshold oscillations and producing the near-synchronous burst. **This is not conduction plus
synaptic transmission**, so the invariant's biological justification does not reach it, exactly as it
does not reach the endocrine, blood-borne, optical and mechanical edges the design file already
lists. **Its requirement still holds: the coupling takes real, finite, small time.** *(That the
existing ruling extends to this class is Claude's reading; the edge itself is Class 1 from the
source.)*
**This is the case where *nonzero* is most strained**, because a gap junction has no transmitter step
at all and its delay is set by membrane and junctional properties rather than by release. It is
recorded as the closest thing in the map to a zero-latency edge, and it is not one.

---

## Cerebellar cortex — the repeating microcircuit

- **Function → structure.** **One canonical circuit tiled across the whole structure.** Two afferent
  systems drive it — **mossy fibres**, carrying sensorimotor and cortical information, and **climbing
  fibres**, one per Purkinje cell, carrying an instructive error signal. **Purkinje cells are the sole
  output**, and their projection is inhibitory. **The two afferent payloads are different in kind, and
  that is the structural fact of the whole cerebellum.**

  **Functional topography — one circuit, many jobs.** The **anterior lobe (lobules I–V) plus lobule
  VIII** is the sensorimotor cerebellum, two somatotopic maps looped with cerebral sensorimotor
  cortex; the **posterior lobe (lobules VI–VII)** is the cognitive and limbic cerebellum, looped with
  prefrontal, posterior-parietal, superior-temporal and cingulate cortex — **language lateralises to
  the right cerebellar hemisphere, spatial cognition to the left**; the **flocculonodular lobe
  (lobule X) plus vermis** is the vestibulocerebellum. Three matching lesion syndromes: cerebellar
  motor, cerebellar cognitive-affective, and vestibulo-cerebellar.

  **Laminar sub-elements: three** — the **molecular layer**, the **Purkinje cell layer**, the
  **granular layer**. **The eight-layer isocortical block does not apply and is not written.** Of the
  nine entries across five files that cannot take the block, **this is the furthest from it, being
  the only one whose tissue is not cerebral cortex at all.**

  **Cell-class sub-elements: five** — **granule**, **Purkinje**, **Golgi**, **stellate** and
  **basket** cells. Each meets the floor-of-the-hierarchy test by having its own targets: the granule
  cell's axon becomes the parallel fibre, the Purkinje cell is the sole output, the Golgi cell
  projects back onto granule cells, and stellate and basket cells project onto Purkinje cells.

  **Tangential sub-elements: the parallel fibre is the tangential organisation, and it is geometric
  rather than compartmental.** Granule axons ascend and bifurcate to run **~5–6 mm along the length
  of the folium**, crossing the flat dendritic fans of many Purkinje cells at right angles. **An edge
  cannot terminate on a compartment here — the organisation is a lattice, not a parcellation.**

  **Internal edges:**
  - **mossy-fibre terminals → granule cells** — the afferent payload, whichever of the four mossy
    systems it arrived on. **Fan-in: 3–7 dendrites per granule cell, ~4 in human, one mossy input
    each — the lowest fan-in in the map, and the reason the granule layer can expand rather than
    average. Fan-out: ~500 granule cells per mossy fibre** *(rat).*
  - **granule cells → Purkinje cells, via the parallel fibres** — the **expansion-recoded** afferent
    payload: the same information in a different code, spread into an enormous, sparsely-active
    population so that patterns which arrived similar leave **separable**. **This is the entry's
    payload change and the point of the structure.** **Fan-in: ~335,000 parallel-fibre synapses per
    Purkinje cell. Fan-out: ~150,000 Purkinje cells per mossy fibre** *(rat)*; per granule cell,
    ~148 parallel-fibre–Purkinje contacts, derived below.
  - **granule cells → Golgi cells**, and **Golgi cells → granule cells** — feedback inhibition onto
    the expansion stage; **no content**. **This is the loop that keeps the granule population sparse,
    which the expansion recoding depends on, and the entry asserts the sparseness without it.**
    Fan-in / fan-out: to derive.
  - **granule cells → stellate and basket cells**, and **stellate and basket cells → Purkinje
    cells** — feedforward inhibition onto the output stage; no content. The basket cell's terminal is
    on the Purkinje soma and initial segment, the stellate cell's on the dendrites. Fan-in / fan-out:
    to derive.
  - **The climbing fibre → Purkinje cell edge is an inter-region edge terminating on a sub-element,
    and its effect is internal.** The complex spike depresses the **parallel-fibre–Purkinje** synapse.
    **The source records that it has no way to express this** — a payload on an inter-region edge
    whose effect is a change to an internal edge's transfer — **and records it as a limit of the
    representation rather than a gap in the anatomy.**

  **What the sheet computes with the verdict is not written.** Expansion-recoded input arrives on
  ~335,000 parallel fibres per Purkinje cell; graded inhibition leaves. **The operation between them —
  a weighted sum, a threshold, a temporal pattern — is not stated**, and the entry's own phrase, the
  sheet's *summed verdict*, is the only description of it. **This is the eighth entry in the source
  whose stated function has no declared internal substrate, and the mildest of the eight**: the
  sub-elements, their edges and two of the fan figures *are* written, so what is missing is the
  transfer function rather than the circuit.

- **Inputs.**
  - **← pontine nuclei** (mossy fibres, middle cerebellar peduncle, crossed) — an **integrated
    mixture of cortical activity**: intention, plan and context drawn from many cortical areas at
    once and **not a copy of any one of them**. Fan-in: ~4 per granule cell, one mossy input per
    dendrite. **The producer has no entry in any file.** *(See the section head; owed at the source.)*
  - **← spinocerebellar tracts** (`16_spinal_cord`) (mossy fibres, inferior peduncle, ipsilateral) —
    body proprioception, the actual configuration, unconscious. Fan-in: as above. **Two-ended and
   .** That file declares `→ cerebellum, from Clarke's column / nucleus dorsalis
    (≈ C8–L2/3), via the dorsal spinocerebellar tract` and types it **unconscious proprioception, body
    configuration** — the same payload in the same words.
    **The far end carries three things this line does not.** It names the **cell group of origin** —
    Clarke's column — and its **segmental range**, C8–L2/3, which is a sub-element of its lamina VII
    with a bounded extent; and its white-matter entry records the **double crossing** of the *ventral*
    spinocerebellar tract, crossed then re-crossing, which this line's *ipsilateral* does not cover.
    **So this endpoint is one line here and two tracts with different crossing patterns there.**
    **Owed here: split the dorsal and ventral limbs**, since the far end distinguishes them and this
    section's own invariants record crossings as load-bearing.
  - **← external cuneate nucleus** (cuneocerebellar tract, mossy fibres, inferior peduncle) —
    proprioception only. Fan-in: as above. *(`05_sensorimotor_loop`, diffed end to end.
    **Two-ended**, and that file records that **this edge and its thalamocortical sibling carry the
    same payload to two destinations of different kinds** — one becoming a reportable percept, one
    writing procedural change — and states that a build folding the cerebellar branch into the motor
    loop would still pass a consistency check unless the duplication is said. **The edge index cannot
    see this pair**: that end names its target `cerebellum`, which matches no entry heading in this
    file, so the endpoint resolves to nothing and the edge is invisible from both directions. **Owed
    at that file: name the receiving entry.**)*
  - **← semicircular canals, otolith organs, and vestibular nuclei** (mossy fibres, to the
    flocculonodular lobe) — rotation rate and gravito-inertial acceleration, and the nuclei's computed
    estimate. Fan-in: as above. *(`03_other_senses`, diffed end to end. **Two-ended three times over,
    and the far end already carries the split this line owes, with a payload on each limb**: the
    semicircular canals declare `→ cerebellum` (flocculonodular lobe) **on a branch that bypasses the
    nuclei**, carrying the rotation-rate signal unrelayed; the otolith organs declare `→ cerebellum`
    (flocculonodular lobe, **nodulus and uvula**) on the direct branch, carrying the gravito-inertial
    vector unrelayed; and the vestibular nuclei declare `→ cerebellum` carrying **both lines plus the
    current estimate**. **So the three limbs differ in payload and two of them differ in destination
    sub-element.** **Splitting this line is owed and the far end supplies every term the split
    needs** — this is the one owed item in the section that requires no new research.)*
  - **← inferior olive** (climbing fibres, inferior peduncle, crossed) — the **instructive error
    signal**: one all-or-none complex spike saying *that was wrong*. **One climbing fibre per Purkinje
    cell**, and the payload is **one bit with a timestamp** — it must arrive while the error is still
    present or it teaches nothing. **Fan-in: exactly one.** *(Producer is in this file and declares
    it.)*
  - **← locus coeruleus** — payload owed; noradrenaline setting global gain, in the producer's terms.
    Fan-in: to derive. *(`13_neuromodulatory_systems`, diffed end to end. **Two-ended, and
    the producer names this structure on its own line** — `→ cerebellar cortex`, noradrenaline setting
    global gain, payload owed there — **declared separately from its `→ the entire cerebral cortex`
    class endpoint.** **The mark this line carried, that the producer declares its targets as a
    brain-wide class covering this structure, is wrong and is withdrawn.** That file records the same
    correction for a different consumer: its hippocampal edge had been read at the far end as arriving
    inside the brain-wide class, and it too is a named edge there. **A diffuse modulator arriving on a
    circuit whose whole account is two afferent systems is worth having visible**, which is why it is
    carried as an edge rather than left inside a class.)*

- **Outputs.**
  - **→ deep cerebellar nuclei**, from the **Purkinje cells** — **graded inhibition**, the Purkinje
    sheet's summed verdict on the expansion-recoded input. Fan-out: to derive. **The cortex projects
    nowhere else except the line below.**
  - **→ vestibular nuclei**, from the **flocculonodular lobe**, directly — graded inhibition. Fan-out:
    to derive. *(`03_other_senses`, diffed end to end. **Two-ended:** that file declares
    `← cerebellum` (flocculonodular lobe, **nodulus and uvula**) as *the return arm of the
    computation, the internal model's correction*, payload otherwise owed there. **The far end names
    a finer origin than this one does** — nodulus and uvula against this line's whole flocculonodular
    lobe — so **owed here: name the sub-element the limb leaves from.** **The one exception to "the
    cortex projects nowhere else", and a rule's exception cannot be carried inside the clause
    asserting the rule.**)*

- **Sizing.** Basis: **whole cerebellum, both sides**, per-hemisphere alongside.

  | sub-element | count (whole) | fan-in | bits | parameter memory |
  |---|---|---|---|---|
  | granule cells | **~69B** *(essentially the entire count)* | **~4** | **2** | **17.25 GB** |
  | Purkinje cells | ~30.5M | **~335,000** | **19** | 72.44 MB |
  | Golgi, stellate, basket cells | to derive | to derive | ≤ 16 | to derive |
  | **structure total** | **~69B** | | | **~17.32 GB whole, ~8.66 GB per hemisphere** |

  **This structure is the proof case for the design file's own claim that memory tracks neuron count
  and not synapse count, and the measurement is stark.** The granule cell has **the lowest fan-in in
  the map** and the Purkinje cell **the highest**. The Purkinje threshold is **9.5× as wide** — 19
  bits against 2 — and Purkinje cells are **2,262× less numerous. They contribute 0.42% of the
  store.** Everything else is granule cells at two bits each.

  **The design file's worked fan-in example for this cell is now stale, and the correction moves it
  by a bit.** That example reads *~150k–200k in a Purkinje cell, ≈ 18 bits*. **The source has retired
  the figure that range brackets** — ~175,000, Napper & Harvey 1988 — as a **rat estimate obtained by
  multiplying a spine-density equation by an average dendritic length, running six to seven times
  above measured reality**, with direct rodent counts giving ~35,000. **The human figure from direct
  morphological reconstruction is ~300,000–500,000 spines, headline ~360,000, of which ~93% carry a
  presynaptic partner — so ~335,000 actual parallel-fibre synapses.** log₂(335,000) = 18.35, so
  **the width is 19 bits, not 18.** *(The retirement and the human figure are Class 1 from the source.
  That the design file's example inherits the retired figure is Claude's reading, offered to be
  checked.)*

  **This is the only structure in the sections worked whose fan-in exceeds the 16-bit log₂ ceiling**,
  and it exceeds it by three bits.

  **The method tension is the only sensitive term, and it moves the figure by more than half.** The
  older Danish stereology counts **granule cells alone at ~101–109B**, against the fractionator's
  *total*-neuron figure of 69B — **1.46× to 1.58×.** Both are primary, unbiased methods; the
  discrepancy is method-dependent and is recorded, not resolved. **Carried through the sizing it gives
  17.25 GB against 25.25–27.25 GB**, and nothing else in the entry moves the number at all.

  **Four cross-checks re-derived, and all four close.**
  - ~30.5M Purkinje cells × ~335,000 synapses = **1.022 × 10¹³** parallel-fibre–Purkinje contacts,
    against the source's ~1.02 × 10¹³.
  - That total ÷ 69B granule cells = **148** contacts per granule cell, against the source's ~148 —
    consistent with a parallel fibre crossing many Purkinje dendritic trees and synapsing with about
    half of them. **The retired ~10¹⁴ total admits no such reconciliation: it would demand ~1,449.**
  - 69B ÷ 30.5M = **2,262 : 1** granule-to-Purkinje convergence, inside the source's ~2,000–3,000 : 1.
  - **80.2%** of an ~86B whole-brain count, against the source's ~80%.

  **Two cross-checks do *not* close, and the caveats matter more than the gaps.** Taking the human
  granule count at 4 mossy inputs each gives 2.76 × 10¹¹ mossy–granule contacts; at ~500 granule
  cells per mossy fibre that needs **552M mossy fibres against the ~200M input-fibre order the source
  states — 2.76×.** And 500 granule cells × 148 Purkinje contacts each gives 74,000 Purkinje cells
  reached per mossy fibre **against the stated ~150,000 — 2.03×.**
  **Both gaps run through the same rat figure**, and the source labels it as rat. Three things could
  account for either without any of them being an error: the fan-out is rat and the counts are human;
  *input fibre* may not mean *mossy afferent axon*, since climbing fibres also enter the peduncles;
  and a single afferent axon branches into many mossy terminals, so counting axons and counting
  terminals are different arithmetic. **The check is therefore not run against a human fan-out,
  because there is none.**
  **What the arithmetic does yield is a candidate for one:** if the ~200M figure counts mossy afferent
  axons and each granule cell takes 4, then the human mossy fan-out is **~1,380 granule cells per
  fibre**, not ~500. *(Claude's derivation from two of the source's own figures, offered to be checked;
  it rests on the two assumptions just named.)*

- **Shape.** **Sheet, rank 3: (lamina, H, W)** — three laminae, named and settled, which is unusual.
  **But the tangential axes are the finding.** The design file's Sheet class defines H × W as a
  **tangential tile grid**, and **this structure's tangential organisation is a lattice with a
  direction.** Parallel fibres run 5–6 mm along the folium and cross Purkinje dendritic fans at right
  angles, so **connectivity is anisotropic by construction — long in one tangential direction, thin
  in the other. A square tile grid with a single pitch asserts an isotropy the structure denies**, and
  no pitch is recorded for either axis. *(That the lattice does not fit the tile-grid axis definition
  is Claude's reading; the lattice geometry is Class 1.)*

  **The tile calculation can be run backwards here, and this is the only structure in the sections
  worked where it can.** Elsewhere surface area is the missing term; here it is measured. **The
  unfolded surface is ~1,590 cm² ≈ 78% of the neocortex** — roughly a 1 m × 10 cm strip, ~85% of it
  buried in fissures. So:
  - **~69B ÷ 159,000 mm² = ~434,000 neurons per mm² of surface**, against V1's ~120,000 — **3.6×.**
  - Volumetrically, over ~130–150 cm³ in vivo, **~460,000 to ~531,000 neurons/mm³**, against V1's
    ~60,000 — **up to 8.8×.**
  **The pitch is still the missing term**, as everywhere else, and here it is missing in a form the
  shape classes do not have a slot for.

- **Edge latency.** All edges **to derive.** **The climbing fibre carries a stated timing requirement
  and no number** — see the invariants above.

- **Invariant conformance.** Co-instantiation: **satisfied**, and this is the first entry in the
  sections worked of which that can be said without qualification at the structure level — its
  output loop through the deep nuclei and the inferior olive closes entirely inside this file.
  **Not satisfiable for the cerebro-cerebellar loop**, whose pontine stage has no entry and computes.
  Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** The counts and the payloads say the same thing twice, and it is the
  clearest instance of that pattern in the sections worked. **The structure is an expansion followed
  by a convergence:** ~200M input fibres onto ~69B granule cells, then 2,262 granule cells onto each
  Purkinje cell, then ~30.5M Purkinje cells onto deep nuclei whose areal ratio to the cortex is 85:1.
  **The expansion is what makes similar inputs separable and the convergence is what turns the result
  back into one verdict**, and the granule cell's fan-in of ~4 is the reason the expansion is an
  expansion rather than an average — a cell with four inputs cannot average anything.
  **The second justification is about why the instructive signal can be one bit.** A single climbing
  fibre per Purkinje cell, all-or-none, carrying *when* rather than *what* or *how much*. It can
  afford to carry no content because the content is already present on 335,000 parallel fibres; its
  only job is to say *now*. **That division — an enormous addressed input and a single unaddressed
  timing signal — is what the two afferent systems are for, and it is why their payloads are
  different in kind rather than different in degree.**

## Deep cerebellar nuclei — the sole output stage

- **Function → structure.** **The only output of the cerebellum.** Inhibition from the Purkinje sheet
  **sculpts** the firing of these **tonically-active excitatory** nuclei, whose output *is* the
  cerebellar contribution to movement and cognition.

  **Divisional sub-elements: three, or four depending on how one is counted** — the **dentate**
  nucleus (lateral, the largest; reads the cognitive and association hemispheres), the **interposed**
  nuclei (**globose** and **emboliform**, counted as one or two; paravermal, limb coordination), and
  the **fastigial** nucleus (medial; vermal and flocculonodular — axial posture, balance, eye
  movements). **Recorded as it stands rather than resolved by preference**, which is the treatment the
  source gives V1's layer 4B and the subdivision counts of the insula and the temporal pole.
  **The sub-elements sort this entry's output edges and the Function field already does the sorting**
  — dentate to the thalamus and the association loop, interposed to the red nucleus, fastigial to the
  vestibular and reticular nuclei. **Every output edge below names the nucleus it leaves from.**
  **Laminar sub-elements: not applicable** — nuclei, not cortex.
  **Tangential sub-elements: the zonal correspondence with the cortex is the organisation, and it is
  owed.** The nuclei are *matched to the cortical zones above*, and **which Purkinje zone projects to
  which nucleus is stated only as that matching** — the parasagittal zonal organisation it rests on is
  described in neither entry.
  **Internal edges: owed, all of them.** No edge between any two of the three nuclei is recorded.

  **The transfer this entry performs is stated and not typed.** Tonic excitatory firing is **sculpted**
  by graded Purkinje inhibition and what leaves is a correction. **What sculpting is, on a wire —
  subtraction, division, a change in timing — is not stated**, and the entry's claim that the payload
  is *a modulation of an ongoing signal rather than a command from rest* is a claim about exactly that
  operation.

- **Inputs.**
  - **← Purkinje cells of the cerebellar cortex** (GABAergic, the dominant input) — **graded
    inhibition**, the cortex's verdict. Fan-in: to derive.
  - **← collaterals of the mossy and climbing afferents** — the raw input, excitatory, **arriving
    alongside the verdict on it**. Fan-in: to derive. **The climbing-fibre limb has a producer in this
    file. The mossy-fibre limb does not resolve**: its four sources are the pontine nuclei (**no entry
    anywhere**), the spinocerebellar tracts (`16_spinal_cord`, which declares the cerebellar target
    and not this one), the external cuneate nucleus (`05_sensorimotor_loop`, which declares only the
    cortical target) and the vestibular system (`03_other_senses`, which declares two cerebellar
    branches and neither to these nuclei). **So three of the four far ends are checked and none of
    them declares this limb; the fourth has no entry.** **Owed: split this line by source.**

- **Outputs.**
  - **→ contralateral magnocellular red nucleus** (superior cerebellar peduncle, decussating), from
    the **interposed** nuclei — a **correction**: the difference between what cortex intended and what
    the cerebellum predicts will actually happen. **The nuclei are tonically active and the Purkinje
    sheet sculpts that firing, so the payload is a modulation of an ongoing signal, not a command
    issued from rest.** Fan-out: to derive. **The consumer has no entry in any file.**
    **And the human case is the opposite of the textbook one.** The red nucleus has two
    cytoarchitectonic subdivisions: the caudal **magnocellular** part, which receives from the
    interposed nuclei and gives rise to the rubrospinal tract, and the rostral **parvocellular** part,
    which receives from the dentate and projects to the inferior olivary complex. **In the human the
    magnocellular part is markedly reduced and the rubrospinal tract is vestigial** — few large
    fibres, not traceable below the upper cervical segments — **while the parvocellular part occupies
    most of the nucleus's volume and its rubro-olivary fibres are very numerous. So the edge written
    here is the one that barely exists in a human, and the one that does the work is the
    parvocellular limb on the next line.**
  - **→ parvocellular red nucleus**, from the **dentate** nucleus — payload owed; **the descending
    limb of the dentato-rubro-olivary loop**, which returns to this structure through the inferior
    olive. Fan-out: to derive. **The consumer has no entry in any file.**
  - **→ ventral anterior / ventral lateral thalamus** (`12_thalamus`) (superior cerebellar peduncle,
    decussating), onward to motor, premotor and prefrontal cortex, chiefly from the **dentate** — the
    same correction. **Fan-out: the cerebellar-cortex to output-nucleus areal ratio is ~85 : 1**, one
    of the few fan figures this file carries.
    **The far end types this edge.** That entry declares `← deep cerebellar nuclei, chiefly the
    dentate, via the superior cerebellar
    peduncle, decussating` and **types it: the cerebellar correction, the forward-model error
    correction that shapes an action already selected.** **Two-ended, typed at both ends, agreeing on
    the source sub-element, on the peduncle and on the decussation.**
    **And the 85 : 1 figure is carried at both ends**, the consumer recording it explicitly as a
    fan-out at the producer. **That is this file's only fan figure appearing independently in another
    file**, which makes it the one number here with a second written record.
    **This line is also the origin of a gap that file records as load-bearing.**
    That entry's `→ prefrontal cortex` output is a class endpoint it calls **the section's load-bearing
    gap**: no prefrontal structure in `11_frontal_lobe` declares this nucleus as an input, and the
    reason the limb is claimed at all is **the onward-clause in this line** — *motor, premotor and
    prefrontal cortex* — which that file attributes to its producer, this entry. **So the cerebellar
    claim to a prefrontal target is made here and is unsupported at the only end that could support
    it.** **Owed at the source: establish which cortical areas the dentate limb reaches through that
    relay, or narrow the onward-clause.** **Not narrowed here** — the clause is the source's.
  - **→ intralaminar nuclei of the thalamus** (`12_thalamus`) — payload owed. Fan-out: to derive.
    **Two-ended and, payload owed at both ends** — that entry declares
    `← deep cerebellar nuclei` and marks it owed from its side too. **Neither end names the nucleus of
    origin**, where the sibling edge above names the dentate. **Owed: say which of the three nuclei
    this limb leaves from**, since this entry's divisional axis exists and the Function field already
    sorts the other outputs by it.
  - **→ vestibular nuclei** and **→ reticular formation**, from the **fastigial** nucleus (inferior
    peduncle) — axial posture, balance, and eye-movement corrections. Fan-out: to derive.
    *(**The reticular limb is two-ended and confirmed, both files read end to end**
    (`14_brainstem_midbrain_hypothalamus`). That file's reticular formation entry declares the limb
    **on its own line, separately from every other input**, and **names the fastigial nucleus as the
    source** — so the split this line owes is already supported at the far end for this target, and
    what stays owed is the vestibular one. **The payload exists at this end only**: this line types
    it *axial posture, balance, and eye-movement corrections* and the far end marks it **owed**.
    **Owed there: take the payload from the producer.**
    **The far end names its source `cerebellum`, and that is the defect worth carrying.** This file's
    entry headings are the cerebellar cortex, the deep cerebellar nuclei and the inferior olive;
    **`cerebellum` matches none of them**, so the endpoint resolves to nothing and the edge is
    **invisible from that direction to any diff run on names** — it reads as producer-only from here
    and as an unresolved endpoint from there, which is one edge wearing two different failures.
    **This is the second instance of exactly this defect on this file's edges**, after
    `05_sensorimotor_loop`'s `→ cerebellum` recorded at the external cuneate line above — **one
    incoming and one outgoing, which makes it a property of how other files name this one rather than
    one file's slip.** **Owed at `14_brainstem_midbrain_hypothalamus`: name the producing entry**,
    which is the deep cerebellar nuclei and not the cerebellum.
    **Neither end names where in the reticular formation the limb arrives**, and that far entry
    records that only some of its sub-elements have borders at all while the remainder is a mesh — so
    this may be an endpoint that cannot be named in the ordinary way rather than one that has not
    been. *(That reading is Claude's; the far entry's two-shapes record is Class 1 there.)*
    **The vestibular limb is producer-only, and the end-to-end diff against `03_other_senses` is what
    shows it**: that file's vestibular nuclei entry declares one cerebellar input and attributes it to
    the **flocculonodular lobe** — the cortex — not to these nuclei. **So two different cerebellar
    structures reach the vestibular nuclei, the cortical one directly and these nuclei by the fastigial,
    and the far end carries only the first.** A search for *cerebellum* at that end finds a match and
    reports the edge two-ended, which is what a located-edge check would have concluded here.
    **Owed at `03_other_senses`: declare the fastigial input, or establish that its cerebellar line
    covers both sources.** **Splitting this line is owed** — the two targets carry different payloads
    and neither end can say which of the three terms goes to which.)*
  - **→ inferior olive** (inhibitory feedback) — **suppression of the error signal once the error is
    learned: the loop that turns the teacher off.** Fan-out: to derive. *(Consumer is in this file.)*
  - **An edge is asserted against this section from `15_cranial_nerve_nuclei` and is not written
    here.** That file's pretectum-and-gaze-integrator entry declares
    `← superior colliculus, frontal eye fields, vestibular nuclei and cerebellum, onto the integrators
    and burst generators`, payload owed, and records the bullet as **naming four producers**. **That
    is the only place in that file where this section is named at all**, and it is one term of four
    inside one bullet rather than an endpoint of its own — so **it carries no stem, names no
    sub-element, and cannot declare an edge back.** **No entry in this file declares any output
    reaching that file under any name** — this entry's seven outputs, the cortex's two and the olive's
    two account for every cerebellar efferent written here, and none of them reaches the nucleus
    prepositus hypoglossi, the interstitial nucleus of Cajal, or the burst generators. **The edge is
    not written in**, because writing it on the far end's declaration alone would assert a projection
    this section has read nothing for.
    **The far end's own reasoning about a sibling term of the same bullet decides most of this, and it
    was not applied to the cerebellar term.** That file checked the **collicular** term and found it
    splits: two-ended for the burst generators, consumer-only for the integrators — because **the
    burst generators are `14_brainstem_midbrain_hypothalamus`'s own sub-elements and not that entry's**,
    so a confirmed limb to them lands in file 14 and not in file 15. **The same is true of the
    cerebellar term**, and it has a consequence this file can state: **the burst generators are
    sub-elements of the reticular formation entry that this nucleus's fastigial limb already
    reaches**, so a cerebellar drive onto them would be **the edge declared above seen at a finer
    grain, not a second edge.** *(Claude's reading; the sub-element attribution and the collicular
    split are Class 1 from that file.)*
    **What remains is the integrator half, and the most economical reading is that it is not this
    file's edge either.** The gaze integrators are the nucleus prepositus hypoglossi and the
    interstitial nucleus of Cajal, and **nothing here reaches them.** But the same bullet names the
    **vestibular nuclei** as a separate producer, that file's sibling line declares the
    vestibulo-ocular command `← the vestibular nuclei` two-ended against `03_other_senses`, and **this
    file declares two edges into the vestibular nuclei** — the cortex's flocculonodular limb and this
    nucleus's fastigial one. **So the cerebellar influence on gaze holding has a declared two-hop route
    through a structure that bullet already names, and *and cerebellum* may be naming an upstream
    station rather than a producer.** **That is the same shape as `04_dorsal_visual_parietal_stream`'s
    nodulus-and-uvula mention**, closed above for the same reason. *(Claude's reading, offered to be
    checked. What would settle it is whether that entry means a monosynaptic cerebellar input; the
    source does not say, and no fan-in is stated on the bullet.)*
    **Owed at `15_cranial_nerve_nuclei`: split that bullet by producer as well as by target.** Of its
    four producers, one is checked and lands in file 14, one is checked here and declares nothing,
    one is two-ended elsewhere in the same entry, and one is unchecked — **four states under one
    bullet.** That file already records the split-by-target as owed; this file supplies the second
    axis. **The endpoint there says *cerebellum*, which is the third instance in this file of a far
    end naming this section by a word that matches no entry heading in it** — after
    `05_sensorimotor_loop`'s outgoing one and `14_brainstem_midbrain_hypothalamus`'s incoming one.
    **Three files, three directions, one word.** **Owed at the source: the far ends name this section
    by a region word, and the region has no entry — the entries are the cerebellar cortex, the deep
    cerebellar nuclei and the inferior olive.**

- **Sizing.** Basis: **whole cerebellum, both sides.**
  **Dentate ~5.0M whole** (~2.5M per hemisphere); fan-in to derive, so ≤ 16 bits → **≤ 10.0 MB
  whole.** **Interposed and fastigial: to derive** — recorded as smaller and soft.
  **So the partition covers one of three nuclei**, and the two uncounted ones are the sources of four
  of the seven output edges.
  **The one fan figure re-derives exactly and from an independent route.** The stated
  cortex-to-output-nucleus areal ratio is ~85 : 1; the cortex's unfolded surface is ~1,590 cm² and the
  dentate's is ~18.6 cm², and **1,590 ÷ 18.6 = 85.5.** The ratio is the surface ratio, and both
  surfaces come from the same measurement lineage.

- **Shape.** **Non-laminated nucleus, rank 2: (division, N)** — division axis at extent **3 or 4**,
  and the ambiguity is the source's own and is carried, not resolved. **N is populated for one of the
  three.** Grey-matter volume unknown; **dentate surface ~18.6 cm² is the only geometric figure**, and
  a surface without a thickness gives no volumetric density, so **no density cross-check runs.**

- **Edge latency.** All edges **to derive.**

- **Invariant conformance.** Co-instantiation: **satisfied for the loop with the cortex and the
  inferior olive**, all inside this file; **not satisfiable for either rubral output**, whose consumer
  has no entry. Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** The 85:1 convergence is the whole argument for why this stage
  exists. **A sheet of 30.5M Purkinje cells reduces onto nuclei covering one eighty-fifth of its
  area**, and the payload changes character across that reduction: graded inhibition in, a modulation
  of tonic firing out. **The tonic activity is the load-bearing part** — a structure that fires
  constantly and is sculpted can encode a correction in both directions on a single line, which a
  structure firing from rest cannot. That is why the entry insists the payload is not a command.

## Inferior olive — the climbing-fibre source

- **Function → structure.** The **sole source of climbing fibres**. **Electrotonically coupled**
  olivary neurons with **intrinsic subthreshold oscillations** fire in near-synchronous bursts; each
  drives its target Purkinje cell to an all-or-none **complex spike** that signals movement error and
  **gates plasticity at the parallel-fibre synapse**. It sits at the apex of the
  dentato-rubro-olivary loop.

  **Divisional sub-elements: owed.** The complex is conventionally divided into a principal olive and
  medial and dorsal accessory olives whose projections address different cerebellar zones — **but no
  subdivision is named in this entry.** *Owed* rather than *unknown*: the sub-elements are known to
  exist and to have been described. **It matters because the entry's own output payload says the
  addressing is *which population*, and a population with no named parts cannot be addressed here.**
  **Cell-class sub-elements: unknown.**
  **Tangential sub-elements: the gap-junction coupling is the organisation, and it is not a
  parcellation.** Near-synchronous bursting across an electrotonically coupled population is the
  mechanism by which the payload acquires its *which population* component. **A coupled cluster is a
  dynamic grouping rather than an anatomical compartment**, so it is tangential structure of a kind
  the slot has not met before — closer to the parallel-fibre lattice than to a set of areas.
  **Whether the clusters have fixed boundaries an edge could terminate on is owed.**

  **Internal edges: one, and it is not a synapse.**
  - **olivary neuron ↔ olivary neuron, via gap junctions** — electrotonic coupling of subthreshold
    oscillations, producing the near-synchronous burst. **A non-synaptic internal edge**, and the
    source has met only two comparable cases, both of which are non-axonal *inputs* rather than
    internal transfers. Fan-in / fan-out: to derive. *(These neurons are among the most densely
    gap-junction-coupled in the brain — a statement about this edge that the source had filed under
    myelination for want of anywhere else to put it.)*

- **Inputs.**
  - **← spinal cord grey matter** (`16_spinal_cord`) — somatosensory **error**: the actual
    consequence, against which the prediction failed. Fan-in: to derive. **Two-ended**, that entry
    declaring `→ inferior olive` and typing it in the same words — *the actual
    consequence against which a prediction failed.*
    **The endpoint resolves here and not in `14_brainstem_midbrain_hypothalamus`**, which describes no
    inferior olive. **Confirmed by an end-to-end read of that file, where it had been concluded from a
    search**: its ten entries are the superior colliculus, the lateral parabrachial nucleus, the caudal
    and rostral ventrolateral medulla, the nucleus of the solitary tract, the periaqueductal grey, the
    hypothalamus, the pineal gland, the reticular formation and the rostromedial tegmental nucleus, and
    **the olive appears in none of them as an entry or as a sub-element.**
    **An endpoint addressed to the wrong file is mis-addressed rather than dangling**,
    and the two are worth telling apart: one is a repair at the naming, the other a missing region.
    **This structure is the mirror of the two regions that are not here.** It is medullary tissue with
    its entry in the cerebellar file, exactly as the pontine nuclei and the red nucleus are brainstem
    tissue whose edges are in the cerebellar file — **the same data-flow split producing a structure in
    the unexpected file in one direction and a structure in no file in the other.** The difference is
    that this one **has a heading**, so it is findable by any check that reads headings, which the
    other two are not. *(That the three cases are one consequence of the source's data-flow split is
    Claude's reading; the split itself is Class 1 from the source.)*
    **Two similar names sit in other files and neither is this structure** — the **superior olivary
    complex** (`02_auditory_pathway`) and the **olivary pretectal nucleus**, described inside a bundled
    entry in `15_cranial_nerve_nuclei`. **A search for *olive* or *olivary* across the map returns all
    three**, which is the same exposure `14_brainstem_midbrain_hypothalamus` records for the rostral
    ventrolateral and ventromedial medulla. Recorded because this file is exposed to it, not repaired.
  - **← dorsal column nuclei** — the same somatosensory error. Fan-in: to derive. **The producer
  declares no such edge, and this is a recorded negative rather than an unchecked
    mark**: `05_sensorimotor_loop` was read end to end, and its dorsal column nuclei entry declares
    three outputs — the ventral posterior thalamus, the cerebellum by the cuneocerebellar tract from
    the external cuneate nucleus, and the dorsal cochlear nucleus — **and no olivary target under any
    name**. *(Owed at `05_sensorimotor_loop`, or withdraw the limb.)*
  - **← red nucleus and the mesodiencephalic junction** — the descending limb of the
    dentato-rubro-olivary loop; payload otherwise owed. Fan-in: to derive. **The red nucleus has no
    entry in any file, and the mesodiencephalic junction is a region name that resolves to no entry
    either.**
  - **← deep cerebellar nuclei** (inhibitory) — **suppression**: *this error is already accounted
    for.* Fan-in: to derive. *(Producer is in this file.)*

- **Outputs.**
  - **→ every Purkinje cell of the cerebellar cortex** (climbing fibres, crossing, one-to-one) —
    the **instructive signal**: a single all-or-none complex spike per event, timed to the error.
    **Not a magnitude and not a direction — a *when*.** The gap-junction coupling means these fire in
    near-synchronous bursts across a population, **so the payload is also *which population*, which is
    the only addressing it has.** **Fan-out: one climbing fibre per Purkinje cell**, and the map's
    sharpest asymmetry against the parallel-fibre fan-in.
  - **→ deep cerebellar nuclei**, collaterals — the same instructive signal. Fan-out: to derive.
    *(Split from the line above: **the two targets are different entries and only the first is
    one-to-one.** The source records the split as owed; it is taken here because the arity is explicit
    and the two endpoints are named.)*

- **Sizing.** Basis: whole cerebellum. **Neurons: to derive** — soft, no clean human count recorded.
  **Parameter memory: to derive.** Synapses unknown. Grey-matter volume unknown. **No density
  cross-check can be run**, and this is the third structure in the sections worked with no independent
  arithmetic available at all.

- **Shape.** **Non-laminated nucleus, rank 2: (cell class, N)** — **and no axis has an extent.** The
  divisional axis is *owed*, the cell-class axis *unknown*, N to derive.

- **Edge latency.** All edges **to derive.** **The gap-junction internal edge is the case where
  *nonzero* is most strained** — see the invariants above.

- **Invariant conformance.** Co-instantiation: **satisfied for the olivo-cortico-nuclear loop**, whose
  three stages are all in this file; **not satisfiable for the dentato-rubro-olivary loop**, whose
  red-nucleus vertex has no entry. Per-edge latency: satisfied in form, all to derive.

- **Justification (biological).** This structure's whole design is to make one bit expensive enough to
  be worth listening to. **One climbing fibre per Purkinje cell, all-or-none, and the target cell has
  335,000 other inputs** — the signal's authority cannot come from its share of the input, so it comes
  from its exclusivity and its timing. **The gap junctions supply the only addressing available**: a
  signal carrying no content and no magnitude can still say *which population*, because the population
  that bursts together is the message. That is why the coupling is structure and not noise, and why
  the entry's subnuclei being owed blocks the payload rather than merely the description.

---

## Section totals

**Basis: whole cerebellum, both sides**, with per-hemisphere alongside.

| structure | count (whole) | bits/neuron | parameter memory (whole) |
|---|---|---|---|
| Cerebellar cortex — granule cells | ~69B | **2** | **17.25 GB** |
| Cerebellar cortex — Purkinje cells | ~30.5M | **19** | 72.44 MB |
| Cerebellar cortex — Golgi, stellate, basket | to derive | ≤ 16 | to derive |
| Deep cerebellar nuclei — dentate | ~5.0M | ≤ 16 | ≤ 10.0 MB |
| Deep cerebellar nuclei — interposed, fastigial | to derive | ≤ 16 | to derive |
| Inferior olive | to derive | ≤ 16 | to derive |
| **stated total** | **~69B** | | **~17.33 GB whole, ~8.67 GB per hemisphere** |

**This is by far the largest figure in the sections worked — roughly forty times the whole visual
pathway — and it is a floor.** Three of the six rows have no count, and one of the three uncounted
rows is a whole structure.

**It is also the section that most sharply confirms the sizing method's central claim.** The two
extremes of fan-in in the entire map sit in one structure: **2 bits and 19 bits, a 9.5× spread in
width — and the 2-bit cell holds 99.5% of the store**, because there are 2,262 of it for every one of
the other. **Memory tracks neuron count, not synapse count**, and here it is not an argument but a
measurement.

**What would move the number is the method tension and nothing else.** At the Danish stereology
granule count of ~101–109B rather than the fractionator's 69B total, the figure runs **25.25 to
27.25 GB.** Pinning the Purkinje fan-in — the largest and best-measured synapse figure in the whole
source — **would change the total by less than half a percent.**

**Memory is not a binding constraint here and the figure is not to be reduced.** It is a derived
requirement recorded as found.
