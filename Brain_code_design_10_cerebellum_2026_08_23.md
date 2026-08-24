# Brain code design — 10 cerebellum

**Date:** 2026-08-23
**Rung:** code design (algorithms).
**Derived from:** `Brain_architecture_10_cerebellum_2026_08_23.md` and
`Brain_code_design_spec_2026_08_20.md`, and from nothing else.
**Implements:** `Brain_10_cerebellum.py`.

**This file carries no history**: no versions, no provenance, no "changed since", no reference to
sessions or prior files, no changelog, no "formerly", no commented-out prior version.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
**character for character**, so that at coding time only this file need be open.

**The §3 diff is not a check on this pair, and must not be reported as one.** The architecture file
named above and this file were worked in the same session, and two records written in one sitting
from one reading **agree by construction and certify nothing.** The copy is still worth having —
it is what makes this document standalone — but the mechanical check it normally supplies is
**owed, at a later pass, against an architecture file this one did not sit beside.**

---

## 0. The headline: this section falsifies the model's central simplification, from two directions

The architecture rung states the modelling choice and flags it as the one to watch: a threshold is
real structure, **equal weights are not**, and a structure the source describes as computing with
graded weights is **a finding against the model rather than a structure to be flattened to fit it.**

**The cerebellum is that structure**, and it arrives at the same conclusion twice by different routes.

**First: the one wins.** A Purkinje cell receives **~335,000 parallel fibres and exactly one climbing
fibre**, and the climbing fibre drives an all-or-none complex spike whatever the parallel fibres are
doing. Under equal weights one active input adds **1** to a count that can reach **335,001**. For the
climbing fibre to decide the output its weight must be about **335,000×** the others' — **18.4 bits
of dynamic range between two inputs to the same cell.** Equal weights is precisely the assumption
that removes that range. **This is not a missing value; the operation is not expressible.**

**Second: the plasticity operates on the assumption itself.** The complex spike **depresses the
parallel-fibre–Purkinje synapse** — long-term depression, one synapse at a time, gated and timed.
**The model stores one number per neuron precisely because the synapses are equal by construction.
There is nowhere to put a change to one synapse of 335,000.**

The two are one finding: the first says the assumption cannot represent what the structure *does*,
the second that it cannot represent what it *learns*. **The source records the same gap at its own
rung** — a payload on an inter-region edge whose effect is a change to an internal edge's transfer,
marked *a limit of the representation rather than a gap in the anatomy.*

**Nothing here proposes a fix.** What the obvious extension would cost is computed rather than
assumed, because memory is a derived requirement and never a constraint to design against:

| | store, whole cerebellum |
|---|---|
| threshold-gate model as it stands | **17.32 GB** |
| per-synapse weights at 1 bit | **1.28 TB** (74×) |
| per-synapse weights at int8 | **10.22 TB** (590×) |
| per-synapse weights at fp32 | **40.87 TB** (2,359×) |

**Whether the model is extended, replaced, or left as it stands is Micky's**, and §5's Update
equation fields below are written so that they state what they are waiting on rather than choosing.

---


# Cerebellar cortex — the repeating microcircuit

## Contract — copied verbatim from the architecture entry

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

## Algorithm

- **Transform.** **Two named operations in series, and the second has no name.**

  **Stage 1, mossy-fibre terminals → granule cells: sparse expansion recoding.** A projection from
  ~200M input lines onto ~69B units, each unit taking **~4** inputs, one per dendrite. In standard
  terms this is a **high-dimensional sparse random projection followed by a threshold**, and the
  operation's whole purpose is stated: patterns that arrived similar leave **separable**. **The
  fan-in of ~4 is what makes it an expansion rather than an average** — a unit with four inputs
  cannot average anything — and that is a property of the arithmetic, not a description of it.

  **Stage 2, granule cells → Purkinje cells: no standard name fits, and that is recorded as a
  finding about the structure.** The architecture states it directly: expansion-recoded input
  arrives on ~335,000 parallel fibres, graded inhibition leaves, and **the operation between them —
  a weighted sum, a threshold, a temporal pattern — is not stated.** The entry's own phrase, *the
  sheet's summed verdict*, is the only description available, and **a picture of an operation is not
  an operation.** Under §5 that is a finding and it is written as one rather than resolved by
  choosing the nearest textbook operation.

  **And the operation the model would supply is the one §0 falsifies.** Even if *weighted sum
  against a threshold* were adopted, it could not express the climbing fibre, whose single line
  overrides 335,000 others. **So this stage is blocked twice over: the source does not name the
  transform, and the model's default cannot carry the input that decides the output.**

  **Stage 3, the inhibitory interneurons: sign, no content.** Golgi cells close a feedback loop onto
  the granule population; stellate and basket cells apply feedforward inhibition onto the Purkinje
  cell, on the dendrites and on the soma and initial segment respectively. **All three carry no
  content**, which is a positive statement about the payload and not an owed one. **Their transform
  is a sign inversion**, and the model has no inverting term — the gap the architecture rung records
  from the outer retina, arriving here on three ordinary spiking edges.

- **Arrays.** Two per sub-element: `threshold`, at `ceil(log2(fan_in))` bits per unit, and `active`,
  at one bit per unit. Counting basis **whole cerebellum, both sides**, per the copied Sizing field.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `granule.threshold` | (69_000_000_000,) | uint2, bit-packed | 0…3 | count of active inputs |
  | `granule.active` | (69_000_000_000,) | 1 bit | {0,1} | dimensionless |
  | `purkinje.threshold` | (30_500_000,) | uint19, bit-packed | 0…335_000 | count of active inputs |
  | `purkinje.active` | (30_500_000,) | 1 bit | {0,1} | dimensionless |
  | `golgi.*` | to derive | — | — | — |
  | `stellate.*` | to derive | — | — | — |
  | `basket.*` | to derive | — | — | — |

  **Three of the five cell classes cannot be allocated**, their counts being *owed* at the source.
  **The tangential axes cannot be allocated either**, for a different reason: the copied Shape field
  gives rank 3 `(lamina, H, W)` with three laminae named and settled, and **H × W is a tile grid the
  structure's lattice organisation denies.** So the arrays above are written **flat, per
  sub-element**, which is the only form the numbers support; **a rank-3 allocation would assert a
  tangential index the architecture explicitly refuses.**

  **The realisation gap is unusually large at both ends and for opposite reasons.** No integer type
  is 2 or 19 bits wide. Bit-packed, the granule threshold is **17.25 GB**; padded to `uint8` it is
  **69 GB — a 4× gap, the largest in the project**, and 4× of 17 GB is 52 GB, larger than every
  other section's total combined. The Purkinje threshold padded to `uint32` is **122 MB** against
  **72.44 MB** derived. **Both are compute-versus-memory trades at the container and neither is
  architectural.** Recorded as found; **not a reason to shrink anything.**

- **Parameters.** Every one below is **derived from the architecture's own counts**. **None is
  chosen**, and no parameter in this entry has an origin other than the rung above.

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `granule_count` | 69_000_000_000 | neurons, whole | copied Sizing field |
  | `purkinje_count` | 30_500_000 | neurons, whole | copied Sizing field |
  | `granule_fan_in` | 4 | mossy inputs per cell | copied Function field |
  | `purkinje_fan_in` | 335_000 | parallel-fibre synapses per cell | copied Sizing field |
  | `climbing_fan_in` | 1 | climbing fibres per Purkinje cell | copied Inputs field |
  | `granule_bits` | 2 | bits | `ceil(log2(4))`, computed |
  | `purkinje_bits` | 19 | bits | `ceil(log2(335_000)) = ceil(18.35)`, computed |
  | `mossy_fan_out` | 500 | granule cells per mossy fibre | copied Function field — **rat** |
  | `pf_purkinje_fan_out` | 150_000 | Purkinje cells per mossy fibre | copied Function field — **rat** |
  | `parallel_fibre_length` | 5–6 | mm along the folium | copied Function field |
  | `unfolded_surface` | 1_590 | cm² | copied Shape field |
  | `tile_pitch` | **to derive** | mm | **not recorded at any rung, and the shape class needs two** |

  **Two of the twelve are rat figures and are labelled**, because mixing them with human counts is
  not a valid check; the copied Sizing field records why the check cannot be run and what candidate
  the arithmetic yields instead (**~1,380 granule cells per fibre**, on two stated assumptions).
  **A module that reported the mismatch as a discrepancy would be manufacturing a finding.**

- **Update equation.** **Not written, and it is blocked at three independent points.** The entry
  records each rather than substituting a default, because a substituted default is indistinguishable
  from a derived one once the session that chose it is gone.

  1. **The stored value is the wrong shape for this structure** — §0. A per-neuron threshold cannot
     express a single input that overrides 335,000, and no choice at this rung repairs that.
  2. **`fan_in(j)` is a count and not a map.** This entry states **four** fan quantities, more than
     any section worked, and **none is a pattern**: ~4 mossy inputs says how many, not which;
     ~335,000 parallel fibres likewise. **The third is worse than absent** — the parallel-fibre
     lattice is a positive statement that *which* is set by **geometry**, and no pitch is recorded to
     compute the geometry from. Connection topology is unset and requires agreement before it is
     chosen.
  3. **Graded against binary emission is unset**, so the width of a value on a line is unset, and
     the inhibitory stages need an **inverting term** the model does not have.

  **What the module may therefore contain is the operation and not a use of it:** a
  `threshold_gate(active_counts, thresholds)` that fires where the count reaches the stored
  threshold, present so that §0's two findings can be stated **with arithmetic rather than by
  assertion**, and `allocate()` returning sized-but-not-fillable arrays.

- **State carried between updates.** **`active` only**, one bit per unit, and it is not parameter
  memory and is never summed with it.

  **And this entry needs a second kind of state it cannot size.** The climbing-fibre payload is *one
  bit with a timestamp* and its stated condition is that it **must arrive while the error is still
  present or it teaches nothing** — which requires the structure to hold *the error is still present*
  across an interval. **Neither the interval nor the arrival latency has a number**, so the state
  exists as a requirement with no extent. **It is recorded here and not sized**, and it is not
  parameter memory.

- **Edge storage.** `line_count × ceil(latency ÷ update_interval) × bytes_per_value`.

  | term | value |
  |---|---|
  | incoming line count | 6 declared inputs; **~200M input fibres** is the only line figure the architecture carries |
  | outgoing line count | 2 declared outputs, from ~30.5M Purkinje cells |
  | internal line count | 8 internal edges, one of them ~1.02 × 10¹³ contacts |
  | latency, every edge | **to derive** — copied Edge latency field |
  | update interval | **unset** — the scheduling discipline is Micky's |
  | bytes per value | **unset** — graded against binary emission is Micky's |

  **Three of six terms are unset, so the figure is not computed and no partial is presented as a
  total.** It is never summed with parameter memory or with state.

- **Adaptation.** **The rule is described in full and still cannot be implemented, and the reason is
  not that the rule is unset.**

  **Site:** the parallel-fibre–Purkinje synapse. **Sign:** depression. **Trigger:** the climbing
  fibre's complex spike. **Timing:** it must arrive while the error is still present. **Off-switch:**
  the deep nuclei inhibit the inferior olive once the error is learned — *the loop that turns the
  teacher off* — and that loop closes inside this file at both ends.

  **That is more of a learning rule than the project has met anywhere**, and **setting the learning
  rule would not unblock it.** The model has no per-synapse value to depress; §0 would still stand.
  **Learning rules are Micky's** and this entry assumes none.

- **Open.**
  - **The equal-weight assumption** — §0. Not on the standing list of unset items, and it is what
    stops this entry.
  - **Inter-structure connection topology**, and with it the lattice geometry and both tangential
    pitches. Requires agreement before it is touched.
  - **Tile geometry**, and the prior question of whether the Sheet class fits at all. The copied
    Shape field records that it does not.
  - **Sparsity**, which is load-bearing here rather than incidental: the entry's payload change *is*
    the expansion recoding, the architecture says the recoding depends on the granule population
    being **sparsely active**, and **the Golgi loop that keeps it sparse has unknown fan at both
    ends.** So a declared operation rests on an unset decision and on a circuit whose numbers are
    missing.
  - **Graded against binary emission**, and the inverting term the three inhibitory stages need.
  - **The scheduling discipline** — §6 below.
  - **Counts for Golgi, stellate and basket cells**, *owed* at the source.

---


# Deep cerebellar nuclei — the sole output stage

## Contract — copied verbatim from the architecture entry

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
    here is the one that barely exists in a human, and the one that does the work was missing until
    the source's last pass.**
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
    bullet.** That file already records the split-by-target as owed; this pass supplies the second
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

## Algorithm

- **Transform.** **No standard name fits, and under §5 that is recorded as a finding about the
  structure rather than resolved by choosing the nearest operation.**

  The copied Function field states the transfer and does not type it: **tonically-active excitatory
  nuclei whose firing is *sculpted* by graded Purkinje inhibition**, with a **correction** leaving.
  **What sculpting is, on a wire — subtraction, division, or a change in timing — is not stated**,
  and those three are different operations with different arithmetic and different failure modes.
  The entry's own claim that the payload is *a modulation of an ongoing signal rather than a command
  issued from rest* is a claim about exactly that unstated operation.

  **The tonic term is the load-bearing part and it is where the model has no slot.** A structure that
  fires constantly and is sculpted can encode a correction **in both directions on a single line**;
  a structure firing from rest cannot. `count[j] = Σ active_source[i]` has no standing output and no
  inverting term, so **neither half of the described operation is expressible**: not the tonic drive,
  and not the inhibition that shapes it. **This is the sign gap again**, and the architecture rung
  records the same construction elsewhere — a threshold element in a delayed feedback path is an
  ordinary relaxation oscillator, so **free-running activity is available from connectivity plus
  delay and is not a missing operation; what is missing is the sign.**

  **The convergence is nameable even though the transform is not.** A sheet of 30.5M Purkinje cells
  reduces onto nuclei covering **one eighty-fifth** of its area, and that ratio re-derives
  independently from the two surfaces — 1,590 cm² ÷ 18.6 cm² = **85.5**. **That is this file's only
  fan figure with a second written record**, the consumer at `12_thalamus` carrying it too.

- **Arrays.** Two per sub-element, as above. Basis **whole cerebellum, both sides.**

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `dentate.threshold` | (5_000_000,) | uint16 | 0…65_535 | count of active inputs |
  | `dentate.active` | (5_000_000,) | 1 bit | {0,1} | dimensionless |
  | `interposed.*` | **to derive** | — | — | — |
  | `fastigial.*` | **to derive** | — | — | — |

  **The partition covers one of three nuclei, and the two uncounted ones are the sources of four of
  the seven output edges** — so the entry can allocate the nucleus that carries the fewest declared
  outputs and cannot allocate the two that carry the most. **The division axis has extent 3 or 4**,
  the ambiguity being the source's own and carried rather than resolved, so **even the length of the
  sub-element axis is not settled**: an array indexed by division cannot be given a first dimension.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `dentate_count` | 5_000_000 | neurons, whole | copied Sizing field |
  | `interposed_count` | **soft, no figure** | neurons | copied Sizing field |
  | `fastigial_count` | **soft, no figure** | neurons | copied Sizing field |
  | `dentate_bits` | 16 | bits | the log₂ **ceiling**, fan-in being *to derive* |
  | `dentate_surface` | 18.6 | cm² | copied Sizing field |
  | `cortex_to_nucleus_ratio` | 85 : 1 | areal | copied Outputs field; re-derives as 85.5 |
  | `division_extent` | **3 or 4** | sub-elements | copied Shape field — carried, not resolved |

  **`dentate_bits` is a ceiling and not a width.** It is the 16-bit bound used where a fan-in is
  underived, and writing it as a measured width would assert a convergence figure the source does not
  supply. **The store it gives — ≤ 10.0 MB whole — is therefore an upper bound**, and the entry says
  so rather than presenting it as a figure.

- **Update equation.** **Not written.** Blocked at the transform itself, which is the unusual case:
  elsewhere the operation is named and its parameters are missing, and here **the operation is not
  named.** Three further blocks stand behind it — the inverting term the tonic-and-sculpted shape
  requires, `fan_in(j)` as a map, and graded against binary emission.

  **The zonal correspondence would be needed even with all three settled.** The copied Function field
  records that the nuclei are *matched to the cortical zones above* and that **which Purkinje zone
  projects to which nucleus is stated only as that matching**, the parasagittal organisation it rests
  on being described in neither entry. **So the dominant input's wiring is owed at the source**, and
  it is the input the whole entry is about.

- **State carried between updates.** **`active` only.** **But the described structure needs more than
  a bit**: *tonically active* is a standing output, which under the relaxation-oscillator reading is
  a property of connectivity plus delay rather than of stored state — **and that reading is available
  only once the sign exists.** Until then the entry has a declared behaviour with no state to hold it
  and no mechanism to generate it. **Recorded; not sized, and not invented.**

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | 2 declared inputs, one of them the whole 30.5M Purkinje sheet |
  | outgoing line count | **7 declared outputs**, the most of any entry in the section |
  | internal line count | **owed, all of them** — no edge between any two of the three nuclei is recorded |
  | latency, every edge | **to derive** |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Three of the seven outputs cross into files whose consumers do not exist or do not declare
  back**, which does not change the storage arithmetic and does change what a build can connect:
  two rubral limbs whose consumer has **no entry in any file**, and the vestibular limb, which is
  **producer-only** against `03_other_senses`.

- **Adaptation.** **None is described at this structure, and that is a positive statement rather than
  an omission.** The section's plasticity is at the parallel-fibre–Purkinje synapse one stage
  upstream, and this entry's role in it is the **off-switch** — its inhibitory output to the inferior
  olive suppresses the error signal once the error is learned. **So this structure participates in a
  learning rule without storing anything the rule writes.** No stored parameter here changes.

- **Open.**
  - **The transform itself.** *Sculpting* is not an operation; subtraction, division and a timing
    change are three, and the entry cannot be coded until one is named. **This is a source question,
    not a choice for this rung.**
  - **The inverting term**, without which neither the tonic output nor the inhibition that shapes it
    can be written.
  - **Counts for the interposed and fastigial nuclei**, *soft* at the source — and they carry four of
    the seven outputs.
  - **The division extent, 3 or 4.** An array axis cannot be allocated against an ambiguity.
  - **Internal edges, all of them**, and the zonal correspondence with the cortex.
  - **Which of the three nuclei the intralaminar limb leaves from**, owed at both ends.
  - **The split of the vestibular and reticular line**, which the far end supplies for the reticular
    target and not for the vestibular one — and neither end can say which of the three payload terms
    goes to which target.

---


# Inferior olive — the climbing-fibre source

## Contract — copied verbatim from the architecture entry

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

## Algorithm

- **Transform.** **A standard name does fit here, and it is the only entry in the section of which
  that is true** — with one term of it unallocatable.

  **A population of coupled oscillators.** Each unit has an **intrinsic subthreshold oscillation**;
  units are **electrotonically coupled through gap junctions**; the coupling pulls neighbouring
  phases together so that a cluster **fires in a near-synchronous burst**. That is a named
  construction — coupled relaxation oscillators with diffusive coupling — and the architecture rung
  already records that a threshold element in a delayed feedback path **is** a relaxation oscillator,
  so the mechanism is available to the model from connectivity plus delay **once the sign exists.**

  **The output transform is a rate-to-event conversion with almost no content.** What leaves is
  **one all-or-none complex spike per event, timed to the error** — *not a magnitude and not a
  direction, a **when***. **One bit with a timestamp.**

  **And the addressing is the part that cannot be allocated.** Because coupled units burst together,
  the payload is also ***which population*** — and the copied Function field records that **no
  subdivision is named in this entry**, the divisional sub-elements being *owed*. **So the only
  addressing the payload has is an index into a set the entry does not enumerate.** That is not a
  missing count; it is a missing axis, and **an array cannot be indexed by it.**

  **The coupling is not a synapse and the shape vocabulary has no slot for it.** A coupled cluster is
  **a dynamic grouping rather than an anatomical compartment**, so it is neither a sub-element an edge
  can terminate on nor a tangential map — and **whether the clusters have fixed boundaries at all is
  owed.** A build that allocated clusters as fixed groups would assert an anatomy the source declines
  to assert; one that ignored them would delete the payload's only addressing.

- **Arrays.** **None can be allocated. Every extent in this entry is open**, and the two axes are
  open in *different* states, which the copied Shape field keeps apart: the divisional axis is
  **owed**, the cell-class axis **unknown**, and N **to derive**.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `olive.threshold` | (**owed**, **unknown**, **to derive**) | — | — | — |
  | `olive.active` | (**owed**, **unknown**, **to derive**) | — | — | — |

  **Writing *to derive* across all three would make a claim the rung above does not make.** *Owed*
  means described and not yet typed — more research is needed and it is known what research. *Unknown*
  means the property exists and has not been measured. **They call for different work and the states
  are copied rather than translated.**

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `olive_count` | **to derive** | neurons | copied Sizing field — soft, no clean human count |
  | `climbing_fan_out_to_purkinje` | **1** | Purkinje cell per climbing fibre | copied Outputs field |
  | `climbing_fan_out_to_nuclei` | **to derive** | — | copied Outputs field |
  | `subdivision_count` | **owed** | subnuclei | copied Function field |
  | `cell_class_count` | **unknown** | classes | copied Function field |
  | `coupling_latency` | **to derive** | seconds | copied Edge latency field |

  **`climbing_fan_out_to_purkinje = 1` is the map's sharpest asymmetry** and it is the one number in
  the entry that is not open: **exactly one climbing fibre per Purkinje cell**, against ~335,000
  parallel fibres onto the same cell. **It is also the only fan quantity anywhere in this section that
  is a pattern and not merely a count** — a one-to-one map needs no further wiring information, so
  this single edge is the one edge in the file whose topology is fully specified.

- **Update equation.** **Not written**, and this entry is blocked earlier than the other two: there is
  **no array to write it over.** Beyond that, the same three blocks stand — the sign, the emission
  question, and the connection topology, the last of which is satisfied for the Purkinje limb alone.

  **The oscillation would need a term the model does not have**, and here the requirement is explicit
  rather than inferred: a subthreshold oscillation is a *sub*-threshold quantity, and a unit whose
  only state is `active ∈ {0,1}` has nothing that varies below threshold. **So this entry needs either
  a graded internal variable or a circuit construction that produces the oscillation from delay** —
  and which of the two the biology uses is **not settled at the source**, exactly as it is not settled
  for the brainstem's intrinsically pacemaking cells. **The same question, in two files, and one
  answer would serve both.** *(That the two are the same question is Claude's reading; both
  physiologies are Class 1 from their sources.)*

- **State carried between updates.** **`active`, and a phase.** The phase is required by the
  described mechanism and has **no width, no range and no update rate**; it is recorded as needed and
  not sized. **It is not parameter memory.**

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | 4 declared inputs, one of them from a structure with no entry anywhere |
  | outgoing line count | 2 declared outputs; the Purkinje limb is **one line per Purkinje cell — 30.5M lines** |
  | internal line count | 1, **non-synaptic**, extent unknown |
  | latency, every edge | **to derive**, and the gap-junction edge is **the case where *nonzero* is most strained** |
  | update interval | **unset** |
  | bytes per value | **unset** — though this payload is the one place in the section where **one bit** is the stated width |

  **The Purkinje limb is the one edge in the section whose line count is known exactly**, because the
  fan-out is one and the target count is measured: **30,500,000 lines.** Every other term is open.

- **Adaptation.** **Nothing stored here changes.** This structure is the **source** of the teaching
  signal rather than a site of plasticity, and the rule it triggers writes at the parallel-fibre–
  Purkinje synapse in the cortex entry. **Its own adaptation is at the loop level and not at a
  parameter**: the deep nuclei inhibit it once the error is learned, so **the teacher is turned off by
  connectivity rather than by a stored value being written.** That is a positive statement about this
  entry, not an owed one.

- **Open.**
  - **The divisional subnuclei**, *owed* — and it blocks the payload rather than merely the
    description, because *which population* is the only addressing the output has.
  - **The cell classes**, *unknown*.
  - **A neuron count**, and with it every array in the entry. **No density cross-check can be run**:
    synapses unknown, grey-matter volume unknown, and the copied Sizing field records this as the
    third structure in the sections worked with no independent arithmetic available at all.
  - **Whether the coupled clusters have fixed boundaries an edge could terminate on.**
  - **Whether the subthreshold oscillation is cell-intrinsic or circuit-generated**, which decides
    whether the model needs a new element-level mechanism or only the inverting term it already owes.
  - **The gap-junction edge's latency**, and with it the question of how small *nonzero* may be.

---


# Section-level material

## 6. Edges, and the count that reconciles

**29 unique edges at this rung: 20 between structures, 9 inside one.** The source counts **21
bullets**, 12 in and 9 out, and the reconciliation is arithmetic rather than assertion:

    21 bullets − 3 pairs written at both ends (6 bullets covering 3 edges)
                + 2 compound bullets naming two targets each
              = 20 between structures

Those three pairs are the edges internal to the **section** — Purkinje → deep nuclei, deep nuclei →
inferior olive, inferior olive → Purkinje — which the source writes at both ends and which **collapse
to one object each here**, because the redundancy that makes a payload mechanically checkable at the
source does not survive into a rung where an edge is one object.

**Payload states: 22 named, 3 partial, 3 owed, 1 typed.** The typed one is the climbing fibre's,
which states content, addressing **and** a timing condition together, and is the best-typed payload
in the sections worked.

**Every edge latency reads *to derive*. All 29.**

### Far ends, and what the module must record on each

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, never its number alone.** A
bare number goes silently wrong the moment a file is split or renumbered, and the code has no reader
to notice. **The module's edge table must therefore carry stems**, and the states below are the ones
the architecture rung establishes.

| far end | state the module records |
|---|---|
| `03_other_senses` | vestibular inputs, three limbs under one line — **splitting owed here, and the far end supplies every term the split needs** |
| `03_other_senses` | cortical and fastigial vestibular outputs — the fastigial one is **producer-only** |
| `05_sensorimotor_loop` | external cuneate nucleus in; dorsal column nuclei in, **the producer declaring no such edge** |
| `12_thalamus` | ventral anterior / ventral lateral, **typed at both ends**; intralaminar, **payload owed at both** |
| `13_neuromodulatory_systems` | locus coeruleus in, **a named edge there and not a brain-wide class** |
| `14_brainstem_midbrain_hypothalamus` | fastigial → reticular formation, **two-ended** |
| `16_spinal_cord` | spinocerebellar tracts in, **two-ended**; spinal grey → inferior olive, **two-ended** |
| **no entry in any file** | pontine nuclei, magnocellular red nucleus, parvocellular red nucleus, mesodiencephalic junction |

**Four regions named on edges have no entry in any file**, and **the pontine one is the load-bearing
case, because it computes.** The corticopontine relay **diverges then reconverges**, integrating
widely separated cortical sources; it covers **not nearly the whole cortex**, with an almost total
lack of projection from large parts of prefrontal and temporal cortex and an origin in **layer 5**;
and **the map is reweighted in transit with a direction** — a de-emphasis of central vision and of
the distal extremities, so *the relay discards precisely the parts of the map the cortical areas
themselves magnify.* **So the cerebellum does not receive cortex's state. It receives a reweighted,
integrated projection of part of it.** A region that performs that cannot be left as a name on an
edge, and **the module records it as a processing stage rather than as a relay.**

### One naming defect the module cannot repair and must not hide

**Three far ends name this section by a region word that matches no entry heading in it** —
`05_sensorimotor_loop` writing `→ cerebellum`, `14_brainstem_midbrain_hypothalamus` writing
`← cerebellum`, and `15_cranial_nerve_nuclei` naming *cerebellum* as one term of a four-producer
bullet. **This file's entries are the cerebellar cortex, the deep cerebellar nuclei and the inferior
olive**, so those endpoints resolve to nothing and **the edges pair at neither end** — producer-only
here, unresolved there. **The repair is at the source and is not made at this rung.** What the module
does is carry the far-end state honestly, so that an endpoint recorded as unpaired is not mistaken
for an endpoint that does not exist.

## 7. The scheduler, and a timing condition with no number on either side

**All 29 latencies read *to derive*.** **The climbing fibre carries a timing *condition* rather than
a timing value: the complex spike must arrive while the error is still present or it teaches
nothing.**

That is a bound on one edge's latency **relative to the persistence of a signal elsewhere**, and
**neither side has a number** — not the latency, and not the width of the window. **Under a uniform
step the relation would be set by the step size**: the instructive signal would land inside or
outside the window according to a number chosen at this rung, and **whether the structure learned
anything would be an artifact of that choice.**

This is the third consecutive section whose mechanism is a timing relation with no timings. **The
pattern is worth naming: in each case the source states the ordering or the window as the mechanism
and records no figure, so a uniform step does not degrade the mechanism — it supplies it.**

**The scheduling discipline is Micky's and is not set.** The module reaches it by calling a function
that raises, rather than by quietly choosing.

## 8. What blocks the implementation

| needed for | item | state |
|---|---|---|
| the forward operation and the learning rule alike | **the equal-weight assumption** | **not on the standing list of unset items, and it is what stops this module** — §0 |
| the deep nuclei's transform, and three inhibitory stages in the cortex | **an inverting term** | not in the model; the sign gap, arriving here on ordinary spiking edges |
| `fan_in(j)` | **inter-structure connection topology** | not set; and the lattice geometry that would give it has no pitch |
| the tangential axes | **tile geometry** | not set, **and the shape class does not fit** |
| whether `active` is dense or sparse | **sparsity** | not set, **and the structure's declared operation depends on it** |
| the width of a value on a line | **graded against binary emission** | not set |
| sizing | **buffer shapes** | **3 of 9 sub-element slots size** |
| the update loop | **the scheduling discipline** | not set — §7 |
| whether `threshold` is ever written | **the learning rule** | not set, **and this section describes one in full** |

**Each of the unset items is Micky's**, and each requires surfacing and explicit agreement before it
is touched. **An item on this list is not a slot to be filled in later.**

## 9. Completion test

**A design entry is finished when the module can be written from it without opening the architecture
and without making a single further choice.**

**Not finished, and the reason is specific to this section.** Other files were blocked on wiring,
scheduling and allocation — things the rung below supplies once a decision is made. **This one can
write the forward operation and cannot use it**, because the operation's central assumption is
exactly what this structure's decisive input and its entire plasticity mechanism act upon. **Setting
every open item on §8's list would leave §0 standing.**

**What the module may implement, and does:**

- three structures and **nine sub-element slots**, each carrying its own count state — *counted* (3),
  *owed* (4), *soft, no figure* (2), *unknown* (1);
- **29 unique edge declarations**, each with its kind — including **the one non-synaptic internal
  edge in the sections worked** — the far file's **stem**, the state of that far end, and its payload
  state;
- the threshold-gate forward operation, with the two findings against it reported **with arithmetic
  rather than assertion**;
- what the obvious extension would cost, at three widths, so the finding carries a number;
- **six cross-checks re-derived against the source's stated values, all closing** — including the
  85 : 1 areal ratio, which closes from an independent route;
- the log₂ ceiling report, showing the width moving from 18 bits to 19;
- the method tension carried through to the store as a **1.46–1.58×** spread;
- a mossy fan-out note that **declines to report a discrepancy**, states the three reasons the check
  cannot be run, and derives a candidate human fan-out from two of the source's own figures;
- the lattice shape problem, stating why the Sheet class's tile grid does not fit;
- surface density computed forwards — **the one section where that is possible.**

**The mossy fan-out note is the one worth singling out.** Every other check in this module either
closes or names a finding. That one had the shape of a **2.76×** discrepancy in the source and **is
not one** — it is three unlabelled species and unit mismatches stacked on a rat figure the source
labelled honestly. **Reporting it as a defect would have been a manufactured finding, and the
module's job there was to not make one.**

## 10. Two things the module must be built to import, and one it currently does not

**`Brain_config.py` holds the vocabulary and this module must use it.** The element classes, and the
`Structure`, `Population`, `Endpoint`, `Representation` and `Edge` types, are defined **once**, there.
**The reason is mechanical and it is the same reason §3 copies verbatim rather than paraphrasing:** an
edge that leaves this file is declared at both ends, in two files, and **two files cannot describe one
edge in agreement when the type describing it is defined twice**, because the two definitions drift
and nothing detects the drift. **A private edge type per module makes every cross-file edge a
translation**, and translation is the failure mode this rung exists to avoid.

**`Brain_10_cerebellum.py` currently defines its own `Edge`, `Structure` and `SubElement` types and
imports nothing**, and its edge table carries **bare file numbers** where the far file's stem is
required. **That is a defect against this rung's spec and against the config file's own `Endpoint`
validation**, which rejects a stem that does not begin `<nn>_`. **Recorded here because the repair is
the module's, and the module is written from this document.**

**What stays in the module and not in config: the counts, shapes and extents of every structure
above.** Config holds the vocabulary; the numbered module holds the content, because that is where it
is derived and where a fidelity pass diffs it against the architecture entry.
