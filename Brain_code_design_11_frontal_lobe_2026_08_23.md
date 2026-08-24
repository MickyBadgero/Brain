# Brain code design — 11 frontal lobe

**Date:** 2026-08-23
**Rung:** code design (algorithms).
**Derived from:** `Brain_architecture_11_frontal_lobe_2026_08_23.md` and
`Brain_code_design_spec_2026_08_20.md`, and from nothing else.
**Implements:** `Brain_11_frontal_lobe.py`.

**This file carries no history**: no versions, no provenance, no "changed since", no reference to
sessions or prior files, no changelog, no "formerly", no commented-out prior version.

**Standalone, not a companion.** Every contract field below is copied from the architecture entry
**character for character**, so that at coding time only this file need be open.

**The §3 diff is not a check on this pair, and the reason here is stronger than the usual one.** The
contract blocks below were **extracted mechanically** from the architecture file named above rather
than re-typed. A character-for-character diff against *that* file will therefore always pass, and it
certifies **exactness of transcription and nothing else** — not that two readings agreed. The
mechanical check §3 normally supplies is **owed at a later pass**, against an architecture file this
one did not sit beside.

---

## 0. The headline: this is the section with no numbers, and the shape of the absence is uniform

Every other section worked enters with some arithmetic. **This one enters with none.** Not one of the
nine structures has a neuron count, and not one edge has a fan-in — so under the threshold-gate
sizing model, **parameter memory = neurons × log₂(fan-in) / 8 bytes**, *both* terms are open at
*every* structure. Nine Sizing fields read *to derive* and they are **one gap with nine instances**,
not nine independent gaps.

**Three quantities are nevertheless closed, and they are the whole of the arithmetic this file has.**

1. **An aggregate ceiling.** Granular frontal cortex anterior to the corpus callosum holds **~640M
   neurons per hemisphere**, a fraction **constant across primates** rather than human-expanded.

        prefrontal parameter memory ≤ 640,000,000 × 16 / 8 = 1.28 GB per hemisphere
        at 12 bits (fan-in ~4,100)                          = 0.96 GB per hemisphere

   **The whole granular prefrontal parameter store therefore sits between ~0.96 and ~1.28 GB per
   hemisphere across the entire plausible fan-in range — a spread of 1.33×.** Pinning a fan-in
   anywhere in prefrontal cortex moves the figure by at most a third; **the per-area partition of
   the 640M is what every individual Sizing field is waiting on.** The aggregate is nearly closed and
   the partition is entirely open. **This is a sum over structures and is never entered against one
   of them.**

2. **A volume, at one structure.** Brodmann area 44 is **~3.8 cm³ left against ~2.5 cm³ right**, a
   ~1.52× leftward asymmetry, and the architecture records that a human stereological study reporting
   **volume and total neuron number** for areas 44 and 45 is named at the source without the neuron
   figure being transcribed. **So the cheapest open number in this file closes by reading a paper
   already cited, not by new measurement.**

3. **An ordering constraint.** Brodmann area 10 is the largest single prefrontal subdivision, so
   structure 9's share of the 640M exceeds every other prefrontal structure's. **That bounds the
   partition without fixing any term of it.**

**And one absence is total rather than partial.** Every edge latency in this section reads *to
derive*: no conduction time, no synaptic delay, no loop latency, and **no myelination figure at any
of the nine structures** to derive a conduction time from. Timing here is not partly known — it is
absent, and §7 below is what that costs.

**The element class is uniform and that is a positive statement.** Every population in this section
is a **threshold gate**. There is no transducer, no graded non-spiking element, no sign-inverting
stage and no transmission-only structure anywhere in the nine, so the four §5a classes collapse to
one and the module needs one code path where the visual line needs three. What blocks this module is
arithmetic and topography instead.

## 0a. The declaration count and the edge count are different units, and they reconcile

**The architecture states 106 edge declarations — 63 in, 43 out.** A declaration is a bullet in an
Inputs or an Outputs field; **an edge is one object.** The two are not the same unit, and the
difference is exact rather than approximate:

**Eleven edges have both ends inside this file.** Seven of the eleven are declared at **both** ends —
once in the producer's Outputs and once in the consumer's Inputs — and the redundancy is what makes a
payload mechanically checkable one rung up. **It does not survive into a rung where an edge is one
object.**

        106 declarations − 7 written twice = 99 distinct edges

**The remaining four in-file edges are declared at one end only, and all four are one inherited
gap**: premotor cortex declares neither its edge to Broca's area nor its edge to the right inferior
frontal gyrus, and neither of those declares its return. **Recorded at the entries that own them;
not repaired here.**

**The per-entry counts and the header agree**, and the module rebuilds them from its own edge table
rather than transcribing them — 13/6, 5/6, 4/2, 6/2, 8/7, 7/5, 10/10, 6/4, 4/1, summing to 63 in and
43 out. **That is a check this rung can actually run**, and it is the only arithmetic in the file
that closes.

---|---|---|---|---|
| 1 premotor | 13 | twelve | 19 | eighteen |
| 5 dorsolateral | 8 | seven | 15 | fourteen |
| 6 ventrolateral | 7 | six | 12 | eleven |
| 7 orbitofrontal / ventromedial | 10 | nine | 20 | nineteen |
| 8 anterior cingulate | 6 | five | 10 | nine |

**The five short edges are the five that entry's own text names**: the amygdalar limbs to premotor,
dorsolateral and ventrolateral cortex, and the hippocampal limbs to the orbitofrontal / ventromedial
and anterior cingulate structures. **The file header's own totals are the correct ones** — 106 edges,
63 in, 43 out — and the per-structure counts sum to 101, which is 106 less those five. The
architecture's whole-file line *every one of the 101 edges in this file reads to derive* and its
*all 58 fan-ins and all 42 fan-outs* both carry the same shortfall.

**The copies below are unchanged, because a design file may not patch a defect inherited from the
rung above** — a patched copy would silently stop being a copy, and the next fidelity pass would
correctly flag the repair as drift. **The repair belongs at the architecture rung**, where it is
arithmetic over that file's own edge lists and needs nothing from the source. **It is recorded at
each of the five entries below, in the Open field, and it is not left silent.**

*(The recomputation is this rung's, over the copied fields. That the five short edges are the five
named ones is inferred by matching the shortfall against the entries' own text; nothing above states
the connection.)*

---


# 1. Premotor cortex and the supplementary motor areas (Brodmann area 6)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Motor planning and sequencing — the stage between association cortex and
  primary motor cortex. Lateral premotor cortex maps sensory-guided reach and grasp; the
  supplementary and pre-supplementary motor areas handle internally-generated action sequences and
  initiation. The structural form is an agranular-to-dysgranular frontal sheet in posterior frontal
  cortex, carrying **at least five divisional sub-elements**: dorsal premotor cortex (**F2**),
  ventral premotor cortex (**F4** and **F5**), the **supplementary motor area**, and the
  **pre-supplementary motor area**. The split is load-bearing rather than descriptive: the
  sensory-guided payloads arrive from parietal cortex and the internally-generated ones from
  cingulate cortex, and they arrive on different sub-elements.

- **Inputs.**
  - ← **superior parietal area 5**, principally area PE (`05_sensorimotor_loop`).
  - ← **the anterior intraparietal area**, terminating on **F5** (`06_posterior_parietal`).
  - ← **the medial intraparietal area**, terminating on **F2** (`06_posterior_parietal`).
  - ← **the ventral intraparietal area**, terminating on **F4**
  (`04_dorsal_visual_parietal_stream`). *(Written by full name;
    the source file's own heading for this structure is a bare abbreviation.)*
  - ← **the supramarginal gyrus** (`06_posterior_parietal`).
  - ← **the precuneus**, from its anterior sensorimotor sector (`06_posterior_parietal`).
  - ← **the primary somatosensory cortex**, from **area 3a** (`05_sensorimotor_loop`).
  - ← **the secondary somatosensory cortex**, principally from the **parietal ventral area**
  (`05_sensorimotor_loop`).
  - ← **the ventral anterior / ventral lateral thalamus** (`12_thalamus`).
  - ← **the midcingulate cortex**, via the **cingulate motor areas**
    (`17_insula_claustrum_habenula`). **Two-ended and confirmed**: the producer declares
    `→ supplementary and pre-supplementary motor areas and premotor cortex`, names the cingulate motor
    areas as the route in the same words, and types it at its own end as *the convergence of reward or
    non-reward outcome with action and spatial information, turned into a motor plan*. **Payload owed
    at that end and untyped at this one**, so the type above is the producer's and is carried, not
    asserted here.
  - ← **the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus**
    (`08_medial_temporal_lobe`) — the **valence tag**: a gain on perception, attention and memory
    encoding, carrying no identity of its own; payload otherwise owed. Terminations in **ventral
    area 6**, continuous with the area 45 label at the Broca and ventrolateral entries, and lighter
    in **dorsal area 6**; **ipsilateral only**, in deep layer I, layer II and layer VI. **Two-ended.**
    **Which sub-element receives it is owed**: this structure names **F2**, **F4** and **F5**, F4 and
    F5 sit in ventral area 6 where the denser half terminates, and the producing study divides area 6
    dorsally and ventrally rather than by those names.
  - ← **the anterior cingulate cortex** (structure 8 below).
  - ← **the dorsolateral prefrontal cortex** (structure 5 below). **The ventrolateral prefrontal
    cortex is named alongside it at the source and does not declare the output** (structure 6 below);
    that half of the edge is an inherited gap and is not repaired here.

  **Two further inbound edges are declared only at their producers, both inside this file** —
  Broca's area → premotor and primary motor cortex, and the right inferior frontal gyrus → premotor
  and primary motor cortex. **The source records both as owed at this structure and this rung does
  not patch them**; they are carried on the producers' Outputs below.

  **Owed at the source: assign each of these inputs to one of the five divisional sub-elements.**
  Six of them are already assignable because their producers name the target.

- **Outputs.**
  - → **primary motor cortex** (`05_sensorimotor_loop`).
  - → **the corticospinal tract**, from a minority of cells. **The tract's consumer is muscle, which
    is outside the map's scope on the body side**; this edge terminates at the scope boundary.
  - → **the basal ganglia**, to the **motor striatum** (`09_basal_ganglia`). The consumer declares its
    cortical source as a class covering all of cortex, so this edge is two-ended only in one direction.
    **Confirmed and the note holds.** **The sector this line names is load-bearing at the far
    end and unusable there:** that entry marks its striatal **motor / associative / limbic** partition
    as a tangential axis that is *named and unbounded*, with no internal edges between sectors — **so
    this edge terminates on a partition the consumer has named and cannot allocate against.** Three of
    this file's four striatal producers name a sector; see the frontopolar entry's note for the count.
  - → **superior parietal area 5** (`05_sensorimotor_loop`).
  - → **the medial intraparietal area**, from **F2** (`06_posterior_parietal`).
  - → **the medial intraparietal area**, from **F4** and **F5** (`06_posterior_parietal`).

  **The two preceding edges are one bullet at the source, split here because they leave from
  different sub-elements.** Six edges stand against five source bullets for that reason; collapsing
  them would lose which sub-element each departs from.

  **And the split is what answers a line at the far end.** That entry's Inputs slot carries one line
  reading *← cingulate area 23, dorsocaudal premotor area F2, and ventral premotor areas F4 and F5*,
  marked **owed, and none of the three far ends declares it.** **Two of those three are this
  structure, and it declares both** — F2 on one bullet, F4 and F5 on the other, named at the
  sub-element the far end names. **So that line does not hold for the premotor limbs**, and it is
  untested for the cingulate one, whose far end is in `17_insula_claustrum_habenula` and is
  unchecked. Owed at `06_posterior_parietal`. **The far end writes the three sources on one line and
  this file writes the premotor pair on two, so a diff by line rather than by endpoint sees no
  match** — which is why the two can disagree unnoticed.

  **Recorded negative:** there is **no** edge from this structure to the middle temporal area. The
  middle temporal entry (`04_dorsal_visual_parietal_stream`) declares its frontal input from the
  frontal eye fields instead.

- **Sizing.** **To derive**, both terms. Neuron count unknown; this structure is **outside the ~640M
  granular prefrontal budget** — it is posterior frontal and agranular-to-dysgranular, with lower
  density than granular prefrontal cortex, and the source says so explicitly. Fan-in unknown on all
  thirteen inputs. Basis: per hemisphere. Synapses, axon counts, grey- and white-matter volumes all
  unknown; the corticospinal contribution is unquantified here.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated **once per divisional
  sub-element**, so five arrays at minimum, not one.
  - Laminar axis: **to derive per divisional sub-element.** Eight laminar sub-elements are named
    (1, 2, 3, 4, 5a, 5b, 6a, 6b), but the sheet is agranular-to-dysgranular and layer 4 is thin or
    absent over part of its extent, so the extent is not uniform across the tangential axes and the
    source declines to assert the standard block here.
  - Tangential axes **H, W: to derive.** No pitch measured. Whether the sheet carries a somatotopic
    map at all is open at the source — the Function field's reach-and-grasp mapping implies a body
    map and does not establish one.

- **Edge latency.** **To derive** on all nineteen edges. No timing figure at the source, and
  myelination unknown, so no conduction time is derivable either.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied. This structure is a stage in the sensorimotor loop — out to
    primary motor cortex and the basal ganglia, back through the ventral anterior / ventral lateral
    thalamus carrying the basal-ganglia selection and the cerebellar correction on one relay — and in
    reciprocal parietal loops with files 4, 5 and 6. Every arm closes outside this file. The
    corticospinal arm terminates at the scope boundary and is not required to close.
  - *Per-edge latency:* satisfied in form. Every edge is a neural projection, none is zero, none is
    assumed equal to another; values open.

- **Justification (biological).** The structure is a distinct stage because the payloads entering it
  are not muscle commands and the payload leaving it toward primary motor cortex is a sequenced,
  shaped movement that is still not a muscle command. Five sub-elements rather than one because the
  afferents segregate by sub-element in the biology — grasp affordances onto F5, reach vectors onto
  F2, peripersonal space onto F4 — and because the supplementary and pre-supplementary areas take
  internally-generated rather than sensory-guided drive. The agranular-to-dysgranular architecture is
  the reason the laminar extent cannot be asserted uniformly: layer 4 is the granular layer, and this
  sheet does not have one throughout.

## Algorithm

- **Transform.** **No standard name fits, and under §5 that is a finding about the structure rather
  than a licence to pick the nearest textbook operation.** The copied Function field gives the stage
  a job — motor planning and sequencing, between association cortex and primary motor cortex — and
  the copied Justification states what leaves as *a sequenced, shaped movement that is still not a
  muscle command*. **Neither is an operation over arrays.** A picture of an operation is not an
  operation, and nothing at the rung above says what the sequencing *does* to a value.

  **What is nameable is the element and the routing, and they are two different statements.** Every
  unit is a **threshold gate** over equal-weight inputs: it fires when the count of active inputs
  reaches a stored threshold, so the only value held per unit is that threshold, at log₂(fan-in)
  bits. And the copied Function field makes the sub-element segregation load-bearing rather than
  descriptive: **sensory-guided payloads arrive from parietal cortex onto F2, F4 and F5, and
  internally-generated ones from cingulate cortex onto the supplementary and pre-supplementary
  areas.** That is a routing constraint the module must carry on the edges — it is why an edge here
  names a sub-element — and it is not itself a transform.

- **Arrays.** Two per divisional sub-element: `threshold`, at `ceil(log2(fan_in))` bits per unit,
  and `active`, at one bit per unit. **Five divisional sub-elements, so ten arrays, and not one of
  them can be sized.** Basis: per hemisphere, per the copied Sizing field.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `F2.threshold`, `F4.threshold`, `F5.threshold` | (to derive,) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `SMA.threshold`, `preSMA.threshold` | (to derive,) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `*.active` | (to derive,) | 1 bit | {0,1} | dimensionless |

  **The rank-3 shape the contract gives cannot be instantiated, and the two axes fail for different
  reasons.** The copied Shape field is `(laminar sub-element, H, W)` per divisional sub-element. The
  **laminar** extent is *to derive per sub-element* because the sheet is agranular-to-dysgranular and
  layer 4 is thin or absent over part of its extent — so the standard eight-layer block is wrong
  somewhere on it and the source declines to assert one. The **tangential** extent is *to derive*
  because **no pitch is measured anywhere in this file**, and because whether the sheet carries a
  somatotopic map at all is open at the source. **A rank-3 allocation here would assert both a
  laminar set and a tile grid the rung above refuses**, so the arrays are written flat per
  sub-element, which is the only form the numbers support.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive** | neurons, per hemisphere | copied Sizing field — unknown, and explicitly **outside** the ~640M granular prefrontal budget |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | the log₂ cap, computed; a **bound, not a measurement** |
  | `divisional_sub_elements` | 5 | — | copied Function field: F2, F4, F5, supplementary, pre-supplementary |
  | `laminar_extent` | **to derive**, per sub-element | laminae | copied Shape field |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **`threshold_bits ≤ 16` is the one entry that looks like a value and is not.** Any fan-in up to
  ~65,000 costs at most 16 bits, so the bound holds without a measurement — and using it *as* a
  measurement is what makes the realisation gap read zero here, since `uint16` holds 16 bits exactly.
  **That zero is an artefact of the bound and would mislead anyone sizing these arrays.**

- **Update equation.** **Not written, and blocked at three independent points**, each recorded rather
  than defaulted, because a substituted default is indistinguishable from a derived one once the
  session that chose it is gone.

  1. **No count and no fan-in**, so there is nothing to allocate and nothing to compare against.
  2. **`fan_in(j)` is needed as a map and is not even present as a count.** Worse than the visual
     line, where a topography is described in prose and formalising it would need authorisation:
     **here there is no described geometry to formalise.** Whether this sheet is somatotopic is open
     at the source.
  3. **Graded against binary emission is unset**, so the width of a value on a line is unset.

- **State carried between updates.** **`active` only**, one bit per unit, written at the end of the
  update. **It is not parameter memory and is never summed with it.** Size: to derive, with the
  count.

- **Edge storage.** `line_count × ceil(latency ÷ update_interval) × bytes_per_value`.

  | term | value |
  |---|---|
  | incoming line count | **13 declared inputs** — bullets in the copied Inputs field |
  | outgoing line count | **6 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field |
  | update interval | **unset** — the scheduling discipline is Micky's |
  | bytes per value | **unset** — graded against binary emission is Micky's |

  **Three of five terms are unset, so no figure is computed and no partial is presented as a total.**
  Never summed with parameter memory or with state.

- **Adaptation.** **None.** No learning rule is set, so nothing writes a threshold: thresholds are
  read-only construction constants and this structure runs open-loop. **Learning rules are Micky's**
  and this entry assumes none.

- **Open.**
    rung and is not made here.**
  - **Which of the five sub-elements receives each input.** The copied Inputs field records this as
    owed at the source and notes that six are already assignable because their producers name the
    target. **Until it is settled, ten arrays exist and no edge can be attached to a specific one.**
  - **Which sub-element the amygdalar limb reaches**, which the copied field records as not
    resolvable from the producer's evidence: the producing study divides area 6 dorsally and
    ventrally, and this structure is divided by F-number.
  - **Whether the sheet is somatotopic at all** — the prior question to any tangential index.
  - **Tile geometry, sparsity, connection topology, the scheduling discipline.** Surface before
    touching.
  - **The corticospinal edge terminates at the scope boundary and the module must record it as
    terminating, not as dangling.** Its consumer is muscle, which is outside the map on the body
    side; an edge recorded as unresolved there would be a false positive on the one check this
    module can actually run.

---

# 2. Frontal eye fields (Brodmann area 8)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Voluntary saccade generation and endogenous control of gaze and
  attention — the frontal node of the oculomotor loop, closing the lateral intraparietal area →
  frontal eye field → superior colliculus circuit. Granular frontal isocortex, unlike the premotor
  sheet above. **Two divisional sub-elements: the saccade area and the pursuit area.** The source's
  Function statement covers the saccade area only; the pursuit area has no function statement and is
  owed one at the source.

- **Inputs.**
  - ← **the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`). Two-ended and agreeing.
  - **A consumer declares an output from this structure that this entry does not declare, found.** `01_visual_pathway`'s V4 entry declares `← frontal eye field, terminating in all
    cortical layers — the spatial attentional gain`. **No output to V4 appears below.** The nearest
    thing that does is `→ the middle temporal area, terminating in all cortical layers` — **the same
    lamination and the same phrasing, to a different consumer in a different file.** So either this
    structure has two all-layer visual outputs and one is missing here, or one edge has been recorded
    against the wrong consumer at one of the two ends. **Owed at the source, and the two candidate
    repairs are not equivalent** — adding an edge and re-terminating an edge have different
    consequences for V4's fan-in.
  - ← **posterior parietal cortex**, beyond the lateral intraparietal area. **Class endpoint, and it
    resolves nowhere**: the parietal files were read at the source and no other parietal structure
    declares an output here. Owed at the source: name the structure, or withdraw the edge.
  - ← **the dorsolateral prefrontal cortex** (structure 5 below).
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **This edge is not declared there as a class covering all prefrontal divisions**, a reading the
    producer's input-side class invites and which is wrong. That entry declares **five
    separate named outputs**, one per consumer, this structure among them, each on its own line and
    each typed in the words above. **The class it does declare is on the return limbs, not this
    one**: its Inputs carry `← prefrontal cortex, layer 6, reciprocal — the modulator` and
    `← prefrontal cortex, layer 5 — the driver`, both marked class endpoints. **Reading the
    producer's input-side class as describing its output side is the available error here**, and it
    is available at all six entries in this file that declare this input.
    **What that opens is a further question.** The producer
    marks its own cell-class axis *to derive* — magnocellular, parvocellular and densocellular are
    named in its literature and none is written in — and states that **whether the five consumers
    receive the same amplification or differently-tuned ones is not stated at either end, and that
    this is what decides whether five edges or one is the right arity.** **A consumer that believes
    it sits inside a class has no reason to ask which division reaches it.** The belief suppressed
    the question at six sites at once. **Owed at the source: which division, and whether the
    amplification is tuned per consumer.**
  - ← **the caudal auditory belt**, directly (`02_auditory_pathway`). **Confirmed two-ended:** that file's auditory belt declares `→ prefrontal cortex, directly` with the **caudal**
    belt reaching the caudal principal sulcus and **this structure by name**, and states what the
    payload is for — **moving the eyes to the sound**, the "where" stream's motor purpose. **The
    producer writes all three of its prefrontal targets on one line**, so the arity is owed there and
    not here.

- **Outputs.**
  - → **the superior colliculus** (`14_brainstem_midbrain_hypothalamus`). **Discharged:**
    that file's superior colliculus entry declares `← frontal eye field → the intermediate layers` and
    types the payload as **a saccade goal, the cortically selected target location in eye-centred
    coordinates**, payload otherwise owed. **So this end is the untyped one**, and the termination layer
    — the intermediate layers, not the superficial visual ones — exists only at the consumer.
  - → **brainstem saccade generators**. **Class endpoint**, and unchecked — the cranial-nerve-nuclei
    file was not read at the source.
  - → **the lateral intraparietal area**, carrying the corollary discharge of the saccade command
    (`04_dorsal_visual_parietal_stream`). **The relay nucleus on this path is unnamed**: the path is
    stated as running through the
    mediodorsal thalamus. **That entry's **first** named output is
    `→ frontal eye fields`, this structure, typed as modulatory amplification. **So the relay names
    this structure; what it does not name is the onward parietal limb**, and its output list contains
    no intraparietal target of any kind. **The gap sits on the second leg of the path, not the
    first.** Owed at the source, in `12_thalamus` or here: state whether the
    corollary discharge leaves that nucleus for parietal cortex, or route it elsewhere.
  - → **the middle temporal area**, terminating in **all cortical layers**
    (`04_dorsal_visual_parietal_stream`). **Two-ended and confirmed**, declared
    at both ends with the same lamination. **That end is the typed one** — it carries the payload as
    *the spatial attentional gain signal: an enhancement or suppression by location, not a stimulus
    code*, and this line carries none.
    **This sharpens the V4 question recorded above rather than answering it.** The two consumers
    separate: **this edge is two-ended and V4's is producer-less.** So the shared wording is **not**
    evidence that one edge was mis-copied into two files — it is evidence that a single general
    description was instantiated at two consumers and declared back at one. **The repair is
    unambiguous: establish the V4 limb here, or withdraw it there.**
  - → **the medial superior temporal area**, reciprocally, **from the pursuit area**
    (`04_dorsal_visual_parietal_stream`). **Two-ended and confirmed**, typed at the far end
    as pursuit and gaze-target velocity and untyped here.
  - → **the ventral intraparietal area**, reciprocally, **from the pursuit area**
    (`04_dorsal_visual_parietal_stream`). **Two-ended and confirmed**, the far end owing
    the payload as this end does.

  **These two lines answer three lines in that file and create a problem here.** Its medial superior
  temporal and ventral intraparietal entries each state that **the frontal lobe file names no pursuit
  area and no pursuit function anywhere** — stated three times across the two entries, and not true:
  **this file names one, on the two lines above.** Owed at `04_dorsal_visual_parietal_stream`.
  **But it names it and does not describe it.** The pursuit area appears here only as a sub-element attribution on two
  outputs: **it has no heading, no count, no shape axis and no inputs**, and this structure's Sizing
  reads *to derive* on both terms with no partition of any kind.
  **What that costs is a payload with nowhere to live.** The far end states that the pursuit area
  **carries visual, vestibular and combined heading tuning of its own, so it is not simply
  downstream** — a claim about this structure, made in another file, about a sub-element this file
  mentions twice and never characterises. **Vestibular tuning in the frontal eye fields has no slot
  here at all.** **Owed at the source: give the pursuit area an entry, or state that this entry
  covers it and carry the far end's tuning claim into it.**

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown; the source does not attribute
  this structure to the ~640M granular prefrontal budget, though it is granular frontal isocortex.
  Fan-in unknown on all five inputs. Basis: per hemisphere. Synapses, axons, volumes and myelination
  all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated **twice**, once for
  the saccade area and once for the pursuit area.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular frontal isocortex.
  - Tangential axes **H, W: to derive.** No pitch measured. A saccade area generating movements to
    retinotopic targets implies a motor map of saccade vectors, but whether that map is a
    compartmentation an edge could terminate on is not established at the source.

- **Edge latency.** **To derive** on all eleven edges.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the oculomotor loop — lateral intraparietal area in, superior
    colliculus out, corollary discharge back to the lateral intraparietal area, closing through file
    4 and file 14. **Not checkable for two arms**: the brainstem saccade generators are a class with
    no structure, and the corollary-discharge relay nucleus is unnamed. Both are inherited.
  - *Per-edge latency:* satisfied in form; values open. **This is the structure where the absence
    hurts most in this file** — a saccade command, its corollary discharge, and the remapping the
    consumer performs across the movement are all timing-defined operations, and not one of the three
    edges has a time on it.

- **Justification (biological).** The frontal node of a loop whose other nodes are parietal and
  collicular; it is granular where the premotor sheet is not, which is why the standard laminar
  extent holds here and not there. Two sub-elements because saccades and smooth pursuit are different
  movement classes with different parietal partners — the pursuit area's partners are the medial
  superior temporal and ventral intraparietal areas, and the source records those edges terminating
  on it by name. **The internal edge between the two areas is not recorded and the biology requires
  one**: a pursuit movement is interrupted by saccades, so the two classes are coordinated somewhere.

## Algorithm

- **Transform.** **No standard name fits for the structure as a whole, and the two sub-elements are
  in different states.** The copied Function field gives the **saccade area** a job — voluntary
  saccade generation and endogenous control of gaze and attention — and the copied Outputs field
  says what leaves it: **a saccade goal, the cortically selected target location in eye-centred
  coordinates**, typed at the consumer in `14_brainstem_midbrain_hypothalamus` and untyped here.
  **A goal in a stated frame is a payload, not an operation**: nothing above says how the goal is
  computed from the parietal input.

  **The pursuit area is worse than untransformed — it is uncharacterised.** The copied Function
  field records that the source's Function statement covers the saccade area only. The pursuit area
  appears in this contract **only as a sub-element attribution on two outputs**: no function
  statement, no count, no shape axis, no inputs. **And a far end makes a positive claim about it**
  that this contract has nowhere to put — that it carries **visual, vestibular and combined heading
  tuning of its own, so it is not simply downstream.** **Vestibular tuning in this structure has no
  slot at any rung.** Under §5 that is recorded as a finding, not resolved.

- **Arrays.** Two per divisional sub-element; **two sub-elements, so four arrays**, none sizable.
  Basis: per hemisphere.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `saccade.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `saccade.active` | (to derive, 8, H, W) | 1 bit | {0,1} | dimensionless |
  | `pursuit.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `pursuit.active` | (to derive, 8, H, W) | 1 bit | {0,1} | dimensionless |

  **This is one of only three entries in the file whose laminar axis is a number rather than a
  state.** The copied Shape field gives **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided,
  granular frontal isocortex. **So the laminar axis is allocatable and the other two axes are not**,
  and the module must be able to express that mixture: an axis with an extent beside two without one.
  **H and W remain to derive** — no pitch — and the copied Shape field adds a second obstacle
  specific to this structure: a saccade area generating movements to retinotopic targets **implies** a
  motor map of saccade vectors, but **whether that map is a compartmentation an edge could terminate
  on is not established.** An implied map is not an index.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive** | neurons, per hemisphere | copied Sizing field — soft / unknown; **not attributed to the ~640M budget** though the tissue is granular frontal isocortex |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | log₂ cap, computed |
  | `laminar_extent` | **8** | laminae | copied Shape field — a settled number |
  | `divisional_sub_elements` | 2 | — | copied Function field: saccade area, pursuit area |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **The unattributed budget line is a parameter question and not a note.** The tissue is granular
  frontal isocortex, which is what the ~640M figure is defined over, and the source does not put this
  structure inside it. **The module must therefore not add this structure to the aggregate**, and
  must not silently exclude it either: it records the structure as *granular frontal, budget
  attribution not stated*, which is a third state and the only true one.

- **Update equation.** **Not written.** Blocked as at structure 1 — no count, no fan-in map, emission
  unset — and blocked additionally by the pursuit area having **no inputs at all** in the contract:
  an update equation for a sub-element with no declared afferents would have to invent them.

- **State carried between updates.** **`active` only**, one bit per unit. Not parameter memory.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **5 declared inputs** |
  | outgoing line count | **6 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all eleven |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed.** And the copied Invariant conformance field marks this as **the structure where
  the absence hurts most in this file**: a saccade command, its corollary discharge, and the
  remapping the consumer performs across the movement are all timing-defined operations, and not one
  of the three edges has a time on it. **A timing-defined operation with no time is not a slow
  operation; it is an unspecified one.**

- **Adaptation.** **None.** No learning rule is set.

- **Open.**
  - **The pursuit area: no function statement, no count, no shape axis, no inputs, and a far-end
    tuning claim with nowhere to live.** Owed at the source.
  - **The V4 limb.** The copied Inputs field records a consumer in `01_visual_pathway` declaring an
    input from this structure that this contract does not declare, with the same lamination and
    phrasing as the middle-temporal output that *is* two-ended. **The module records the edge as
    consumer-declared and does not write it**, and the two candidate repairs — add an edge, or
    re-terminate one — are **not equivalent for V4's fan-in.**
  - **The corollary-discharge relay nucleus is unnamed** on the second leg of the path to the lateral
    intraparietal area. The module cannot route what has no name.
  - **`posterior parietal cortex, beyond the lateral intraparietal area` is a class endpoint that
    resolves nowhere**, and `brainstem saccade generators` is a class whose file was not read.
  - **Which mediodorsal division reaches this structure, and whether the amplification is tuned per
    consumer** — the copied Inputs field records that this decides whether five edges or one is the
    right arity, at five sites at once.
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# 3. Broca's area — inferior frontal gyrus (Brodmann area 44, pars opercularis; Brodmann area 45, pars triangularis)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Speech production and syntax; the frontal terminus of the auditory dorsal
  (audiomotor) stream. Strongly left-lateralised. **Two divisional sub-elements with different jobs
  and different architecture** — **Brodmann area 44**, agranular and premotor-adjacent, doing
  phonological and articulatory sequencing and hierarchical structure; **Brodmann area 45**,
  granular, doing controlled semantic retrieval and selection. **Each subdivides further**: receptor
  architecture splits area 44 into **44d** and **44v** and area 45 into **45a** and **45p**, and a
  cytoarchitectonic lineage splits area 45 into a rostral **45A** and a caudal **45B**. Whether
  45A/45B and 45a/45p are one border under two names is not established at the source.

- **Inputs.**
  - ← **the posterior superior temporal gyrus and area Spt**, via the **arcuate fasciculus**
    (file 2; the tract has an entry in file 18). Far end unchecked at the source.
  - ← **the supramarginal gyrus**, via the **arcuate fasciculus** and **superior longitudinal
    fasciculus III** (`06_posterior_parietal`).
  - ← **the ventrolateral prefrontal cortex** (structure 6 below). **This edge crosses a boundary
    whose location is not agreed** — see Shape.
  - ← **premotor cortex** (structure 1 above). **The producer does not declare it**; inherited gap,
    not repaired here.

- **Outputs.**
  - → **premotor cortex and primary motor cortex**, for articulation (structure 1 above;
  `05_sensorimotor_loop`).
    **The premotor consumer in this file does not declare this edge.** Inherited; owed at the source.
    **The primary motor consumer does not declare it either, checked.** That entry's Inputs
    slot names four sources — area 3a, premotor cortex, superior parietal area 5, and the ventral
    anterior / ventral lateral thalamus — **and no inferior-frontal source of any kind.** So this edge
    is producer-only at **both** of its two named targets, not just the in-file one, and the owed
    repair is two edges at two files rather than one.
  - → **temporoparietal cortex**, reciprocally. **Class endpoint.** One member resolves — the
    supramarginal gyrus, which declares the reciprocal input (`06_posterior_parietal`). The others
    are unnamed. Owed at
    the source: name them, or narrow the endpoint.

- **Sizing.** **To derive**, both terms — but **this is the cheapest open figure in the file.** The
  source names a human stereological study reporting volume and total neuron number for areas 44 and
  45, left and right, and reports a significant left-greater-than-right neuron-number asymmetry in
  area 44, without transcribing the count. What it does carry is grey-matter volume: **area 44 ~3.8
  cm³ left, ~2.5 cm³ right**, a ~1.52× leftward asymmetry. Fan-in unknown on all four inputs. Basis:
  per hemisphere, and the asymmetry is why that basis matters here.
  - **One fan-like figure exists and must not be entered as a fan-in.** The arcuate trunk carries a
    median of about 6,200 axons between areas within a hemisphere, and direct posterior-temporal to
    inferior-frontal connections are under ~5% of it. That counts a tract's inter-areal axons, not
    contacts per cell, so it does not enter log₂(fan-in). Reconciling the two measures is owed at the
    source.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated **once per divisional
  sub-element**, and **the two do not have the same rank-3 extent**:
  - **Brodmann area 45: laminar axis = 8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b. Granular, with a
    well-developed layer 4. The source records a specific laminar signature here: layer III holds
    small-to-medium pyramidal cells above and **clusters of large, deeply stained, densely packed
    pyramidal neurons** in its deeper part; layer Va holds medium pyramidal cells and layer Vb is
    cell-sparse, so layer VI separates clearly from Va. **The combination of the deep-layer-III
    clusters with a well-developed layer 4 is what distinguishes this area from all its neighbours**
    — the sharpest laminar signature anywhere in this file, and a sub-element-level measurement rather
    than a generic block.
  - **Brodmann area 44: laminar axis = 7** — 1, 2, 3, 5a, 5b, 6a, 6b. Agranular; layer 4 thin or
    absent.
  - **So a single laminar extent is wrong within one structure.** This is the case that forces the
    laminar axis to be a property of the divisional sub-element rather than of the structure.
  - Tangential axes **H, W: to derive.** No pitch measured. **And the tangential boundary itself is
    not reliably placeable**: the area 44 / area 45 border is conventionally taken at the ascending
    ramus of the lateral sulcus, but the ascending and horizontal rami are highly variable and the
    sulcus diagonalis is present in only about half of hemispheres. **That is not a naming dispute
    and cannot be fixed by renaming** — it is a statement that the two sub-elements' tangential
    extents are individually variable.
  - **Brodmann area 45 is claimed by this structure and by the ventrolateral prefrontal cortex below,
    and both claims are real** — Broca's area is classically 44 plus 45, the ventrolateral structure
    is 45 plus 47, and 45 is the member the two conventional groupings share. The source proposes
    assigning **45B / 45p** here and **45A / 45a** to the ventrolateral structure, and records the
    proposal as unadopted. **Until it is adopted the two structures overlap and their Shapes cannot
    both be allocated.**

- **Edge latency.** **To derive** on all six edges. The arcuate fasciculus has an entry in file 18
  and is where a conduction time for two of them would be derived from; myelination is unknown there
  as it is here.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the audiomotor loop — posterior superior temporal gyrus and
    supramarginal gyrus in via the arcuate fasciculus, temporoparietal cortex back out reciprocally —
    which closes through files 2 and 6. **Not checkable for the temporoparietal arm**, which is a
    class.
  - *Per-edge latency:* satisfied in form; values open.
  - **Not conformant on Shape**, and the defect is inherited: a structure whose tangential extent
    overlaps another structure's cannot be allocated, and this one does until the area 45 assignment
    is settled at the source.

- **Justification (biological).** The two sub-elements differ in cytoarchitecture, not only in job:
  one is agranular and one granular, which is the same structural distinction that separates premotor
  from prefrontal cortex above, occurring here **inside one structure**. Left lateralisation is
  structural rather than functional shorthand — it appears as a volume and neuron-number asymmetry —
  which is why the right homologue is a separate structure below rather than a mirrored copy of this
  one. **The internal edge from area 45 to area 44 is required by the Function statement** — a
  pipeline from semantic selection to articulatory sequencing needs one — **and is not recorded at the
  source.**

## Algorithm

- **Transform.** **Two named jobs in series and no named operation for either.** The copied Function
  field assigns **phonological and articulatory sequencing and hierarchical structure** to Brodmann
  area 44 and **controlled semantic retrieval and selection** to Brodmann area 45. The copied Outputs
  field types what leaves as **the articulatory plan — the phonological and syntactic structure
  rendered as a motor sequence.** Under §5 this is a finding and it is the sharpest instance of it in
  the file: **what a syntactic structure *is*, on a wire, has no units, no range and no frame**, so
  there is no array for the transform to produce.

  **And the series itself has no edge.** The copied Justification field states that the Function
  statement *requires* an internal edge from area 45 to area 44 — a pipeline from semantic selection
  to articulatory sequencing needs one — and that **it is not recorded at the source.** So the
  module can declare the two sub-elements and cannot connect them.

- **Arrays.** Two per divisional sub-element; **two sub-elements, four arrays.** Basis: per
  hemisphere, and **the asymmetry is why that basis matters here** rather than being a convention.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `area44.threshold` | (to derive, **7**, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `area44.active` | (to derive, **7**, H, W) | 1 bit | {0,1} | dimensionless |
  | `area45.threshold` | (to derive, **8**, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `area45.active` | (to derive, **8**, H, W) | 1 bit | {0,1} | dimensionless |

  **This is the entry that forces the laminar axis to belong to the sub-element and not to the
  structure**, and it is the only place in the file where two settled laminar numbers sit inside one
  contract: **area 44 is agranular at 7 laminae, area 45 is granular at 8.** A single laminar extent
  would be wrong at one of them. **The module's shape type must therefore carry the laminar extent
  per sub-element**, and a design that hangs it on the structure would be unable to express this
  entry at all.

  **Allocation is nevertheless blocked twice, and the second block is not a missing number.** Beyond
  the absent count, **Brodmann area 45 is claimed by this structure and by structure 6, and both
  claims are real** — the classical groupings are 44+45 and 45+47 and area 45 is the shared member.
  The copied Shape field carries the source's proposed division, **45B / 45p here and 45A / 45a
  there**, and records it as **unadopted**. **A missing partition leaves an array unsized; an
  unresolved overlap makes two arrays wrong together in a way that sums cleanly and looks right.**
  The module must refuse to allocate either, and refuse for that reason specifically.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive** | neurons, per hemisphere | copied Sizing field — **the cheapest open figure in the file** |
  | `grey_matter_volume`, area 44 | **3.8 left / 2.5 right** | cm³ | copied Sizing field |
  | `volume_asymmetry`, area 44 | **1.52×** leftward | ratio | `3.8 / 2.5`, computed |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `arcuate_interareal_axons` | ~6,200 median; direct posterior-temporal→inferior-frontal **< ~5%** | axons | copied Sizing field — **must not be entered as a fan-in** |
  | `laminar_extent`, area 44 | **7** | laminae | copied Shape field |
  | `laminar_extent`, area 45 | **8** | laminae | copied Shape field |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **The arcuate figure is the one number in this file a module could wrongly use.** It counts a
  tract's inter-areal axons, not contacts per cell, so **it does not enter `log2(fan_in)`** — the
  copied Sizing field says so explicitly and records reconciling the two measures as owed at the
  source. **A module that fed 6,200 into the log₂ term would produce a confident 13-bit width from a
  quantity that is not a fan-in.** Guarding against exactly that is why the figure is carried here at
  all.

- **Update equation.** **Not written.** No count, no fan-in map, emission unset — and the transform
  itself is unnamed, so there is no equation to block on in the first place.

- **State carried between updates.** **`active` only**, one bit per unit. Not parameter memory.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **4 declared inputs** |
  | outgoing line count | **2 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all six |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed.** The copied field names `18_white_matter_tracts` as where a conduction time for
  two of the six would be derived from, and records that **myelination is unknown there as it is
  here** — so the substrate exists and carries no number either.

- **Adaptation.** **None.** No learning rule is set.

- **Open.**
  - **The Brodmann area 45 assignment.** Until the source adopts a division, **two of the nine
    structures cannot be told apart**, and neither can be allocated. This is the only such case in
    the file.
  - **The internal edge area 45 → area 44**, required by the copied Function and Justification fields
    and unrecorded at the source.
  - **The area 44 / area 45 tangential boundary is individually variable** — the ascending and
    horizontal rami vary and the sulcus diagonalis is present in about half of hemispheres — which
    the copied Shape field marks as **not a naming dispute and not fixable by renaming.** It is a
    statement about what a fixed `H, W` would mean here.
  - **The output to premotor and primary motor cortex is producer-only at both named targets**, one
    in this file and one in `05_sensorimotor_loop`. The module records two unpaired ends, not one.
  - **`temporoparietal cortex` is a class endpoint** with one member resolving.
  - **The copied Invariant conformance field declares this structure not conformant on Shape**, and
    the module must carry that: a structure whose tangential extent overlaps another's cannot be
    allocated. **A non-conformance is a state to report, not a flag to clear.**

---

# 4. Right inferior frontal gyrus — affective-prosody production (right Brodmann area 44 / 45 homologue)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** The production node for affective (emotional) prosody — the
  right-hemisphere homologue of Broca's area, and the frontal complement to the right perceptual
  prosodic homologues in the auditory file. A right anterior frontal lesion produces motor
  (expressive) aprosodia: speech gone flat and monotone, unable to impose emotional intonation,
  mirroring Broca's aphasia on the left. **The lateralisation is a bias, not a dichotomy** —
  producing emotional prosody activates the inferior frontal gyrus bilaterally with a larger
  right-hemisphere extent — so this is the right-dominant end of a bilateral network. Isocortex.
  **Two divisional sub-elements by homology: right Brodmann area 44 and right Brodmann area 45.**

- **Inputs.**
  - ← **the right auditory prosodic stream** — the right superior temporal gyrus and sulcus
    homologues (file 2). Far end unchecked at the source.
  - ← **the amygdala**, from the **basal** and **accessory basal** nuclei (`08_medial_temporal_lobe`).
  - ← **the anterior insula** (`17_insula_claustrum_habenula`) — the **salience signal**: *this event
    is behaviourally relevant now*; payload otherwise owed. **Two-ended and confirmed.**
    **The producer declares `→ right inferior frontal gyrus` on its own line**, having split that
    line out of a compound naming one region and one class, so it reaches this structure by name and
    not inside a class.
  - ← **the orbitofrontal cortex** (structure 7 below). **The producer does not declare it**;
    inherited gap.
  - ← **premotor cortex** (structure 1 above). **The producer does not declare it**; inherited gap.
  - ← **the contralateral inferior frontal gyrus**, via the **corpus callosum** (file 18).
    **The laminar termination is specified and is load-bearing**: callosal origin is layers 3 and 5,
    termination is throughout layers 2–6, densest in 2 and 3 and **sparsest in layer 4** — so this
    input **avoids the layer a thalamic driver targets**. All callosal fibres are excitatory; the
    inhibitory effects are feedforward through local interneurons.

- **Outputs.**
  - → **premotor cortex and primary motor cortex** (structure 1 above; `05_sensorimotor_loop`).
  **The premotor
    consumer in this file does not declare it**; inherited gap. **The primary motor consumer does not
    declare it either, checked** — the same result as the homologous edge at Broca's area,
    and from the same reading of that entry's four-source Inputs slot.
  - → **right temporoparietal cortex**, reciprocally. **Class endpoint**, and it was marked unchecked
    with the far end placed in the auditory file. **Checked against `06_posterior_parietal`,
    and the placement was too narrow.** That file's supramarginal gyrus entry states that its ventral
    part, together with the posterior superior temporal sulcus, **forms the right-dominant
    temporoparietal junction of the ventral-attention network** — so a candidate for this class sits in
    the parietal file and not only in the auditory one.
    **What was found there is not a resolution but a second class facing this one.** That entry's own
    Outputs slot declares an output to the **ventral-attention frontoparietal network**, typed there
    as a reorienting
    signal — *a one-bit interrupt with a location attached* — and marked there as an endpoint that
    **does not resolve to nodes.** **So each end declares a class whose description names the other
    end's network, and neither declares the other structure by name.** Two unresolved classes pointing
    at each other are not a two-ended edge, and reading one as confirming the other would manufacture
    an edge from two absences. **Owed at the source: name the node at one end or the other.**
- **Sizing.** **To derive**, both terms. No clean per-area count. **It is bounded above by the left
  side**: this is the smaller side of the documented left-greater-than-right area 44 asymmetry, so
  once Broca's count is firmed this structure's is bounded below it. Grey-matter volume unknown here,
  **but bounded above by the ~2.5 cm³ right-side figure recorded at Broca's entry, which is the same
  measurement recorded from the other side.** Reconciling the two records is owed at the source.
  Fan-in unknown on all six inputs. Basis: per hemisphere — right.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element.
  - Laminar axis: **contested for this side.** By homology it would be 8 in area 45 and 7 in area 44,
    as on the left. Whether the agranular/granular difference holds on the right is not established,
    and it is exactly the kind of property the documented left-right asymmetry might not preserve.
    **To derive.**
  - Tangential axes **H, W: to derive.** No pitch measured.
  - **The Function statement extends this structure past its own boundary.**
    Producing emotional prosody activates areas 44, 45 **and 47**, extending into **anterior insula**
    — area 47 belongs to the ventrolateral structure below and the anterior insula to
    `17_insula_claustrum_habenula`. **An edge connects to one of them**: this entry's Inputs slot declares `← the anterior insula`,
    and the producer declares it back by name. **A claim that no edge connects to either would
    contradict this entry's own Inputs slot, and no cross-file read is needed to see that** — only
    reading the entry whole. **The area 47 half stands**: the ventrolateral structure below declares no output here.
    **Owed at the source: write the area 47 edge, or state that that half is co-activation rather than
    connection.**

- **Edge latency.** **To derive** on all eight edges. The callosal edge is the one whose physical
  substrate is described — the corpus callosum has an entry in file 18 — and its myelination is
  unknown there.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the prosodic loop through the auditory file, and for the
    callosal loop with the contralateral structure. **Not checkable for the temporoparietal arm**
    (class) and for three arms whose producers do not declare them.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** A separate structure from Broca's area rather than a mirrored copy,
  because the two sides are not identical: the volume and neuron-number asymmetry is measured, and
  the jobs differ — propositional language on the left, affective components on the right. The
  clinical evidence is symmetric in weight: aprosodia after right-hemisphere stroke is about as
  common as aphasia after left-hemisphere stroke. **The callosal input's laminar profile is a
  structural claim, not a detail** — an input that avoids layer 4 is not arriving as a driver, and
  that distinction is what makes the two hemispheres one network rather than two.

## Algorithm

- **Transform.** **No standard name fits.** The copied Function field gives the job — production of
  affective prosody — and the copied Justification field gives the clinical evidence, but the
  operation that turns an amodal or semantic input into an intonation contour is stated nowhere.
  What *is* stated, and is structural rather than descriptive, is **the lateralisation is a bias, not
  a dichotomy**: producing emotional prosody activates the inferior frontal gyrus bilaterally with a
  larger right-hemisphere extent. **So this structure is the right-dominant end of a bilateral
  network, and the module must not model it as a mirror of structure 3.**

  **One input carries a transform-relevant fact the module can act on.** The copied Inputs field
  specifies the callosal input's lamination: origin in layers 3 and 5, termination throughout layers
  2–6, **densest in 2 and 3 and sparsest in layer 4** — so it **avoids the layer a thalamic driver
  targets**. All callosal fibres are excitatory; the inhibitory effects are feedforward through local
  interneurons. **An input that avoids layer 4 is not arriving as a driver**, which the copied
  Justification field states directly. **The module carries that edge with `role = MODULATORY`, and
  that is the one role assignment in this entry licensed by the contract rather than read into it.**

- **Arrays.** Two per divisional sub-element; **two sub-elements by homology, four arrays.** Basis:
  **per hemisphere — right**, and this is the one entry in the file whose basis names a side.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `right_area44.threshold` | (to derive, **to derive**, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `right_area45.threshold` | (to derive, **to derive**, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `*.active` | (to derive, …) | 1 bit | {0,1} | dimensionless |

  **The laminar axis is *contested for this side*, and copying that state matters.** By homology it
  would be 8 in area 45 and 7 in area 44, as on the left; **whether the agranular/granular difference
  holds on the right is not established**, and the copied Shape field records it as exactly the kind
  of property the documented left-right asymmetry might not preserve. **Writing 7 and 8 here would
  turn a homology argument into a measurement**, which is the §5b failure of writing *to derive* — or
  worse, a value — over a state the rung above distinguished.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive**, and **bounded above by structure 3's** | neurons, per hemisphere (right) | copied Sizing field |
  | `grey_matter_volume` | **to derive**, **bounded above by ~2.5 cm³** | cm³ | copied Sizing field — the right-side figure recorded at structure 3 |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `laminar_extent` | **contested** | laminae | copied Shape field |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **Two of these are ordering constraints rather than values, and the module must represent them as
  such.** *Bounded above by the left side* is a real datum — it comes from the documented
  left-greater-than-right area 44 asymmetry — and it is **not a number**. A module that stored it as
  a number would have invented one; a module that dropped it would have discarded a constraint that
  becomes a value the moment structure 3's count is transcribed. **The copied Sizing field also
  records that the ~2.5 cm³ figure is the same measurement recorded from the other side, and that
  reconciling the two records is owed at the source.**

- **Update equation.** **Not written.** No count, no fan-in map, emission unset; and the laminar
  extent is contested, so even the array rank cannot be fixed.

- **State carried between updates.** **`active` only**, one bit per unit. Not parameter memory.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **6 declared inputs** |
  | outgoing line count | **2 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all eight |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed.** The callosal edge is the one whose physical substrate is described — the corpus
  callosum has an entry in `18_white_matter_tracts` — and **its myelination is unknown there.**

- **Adaptation.** **None.** No learning rule is set.

- **Open.**
  - **Three inbound edges have no producer declaration** — from the orbitofrontal structure, from
    premotor cortex, and the output to premotor and primary motor cortex is producer-only at both
    targets. All inherited; the module records them unpaired rather than repairing them.
  - **`right temporoparietal cortex` is a class endpoint facing a second class.** The copied Outputs
    field records that the far end in `06_posterior_parietal` declares an output to the
    *ventral-attention frontoparietal network*, itself an endpoint that does not resolve to nodes.
    **Two unresolved classes pointing at each other are not a two-ended edge**, and the module must
    not pair them: reading one as confirming the other would manufacture an edge from two absences.
  - **The area 47 co-activation.** The copied Shape field records that producing emotional prosody
    activates areas 44, 45 **and 47**, and that structure 6 declares no output here. **Owed at the
    source: write the edge, or state that that half is co-activation rather than connection.**
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# 5. Dorsolateral prefrontal cortex (Brodmann areas 9 and 46)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Working memory, executive control, goal maintenance and top-down
  attention — holding and manipulating information across delays and biasing posterior cortex toward
  goals. The action-control, "where" apex of prefrontal cortex. Granular prefrontal isocortex, thick
  but low-density. **Two divisional sub-elements are named — Brodmann area 9 and Brodmann area 46 —
  and no edge uses either**, although other files address this structure as *area 46* specifically,
  so the finer name is already in use outside it. **A third location is named by an edge and not by
  the heading**: the **caudal principal sulcus**, which is a location within area 46 rather than
  either named area. Whether it is a sub-element of area 46 or a separate one is owed at the source.

- **Inputs.**
  - ← **the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`), which names **area
  46**. Two-ended and agreeing.
  - ← **the angular gyrus** (macaque area 7a) (`06_posterior_parietal`). **The producer declares an
    output to the ventrolateral prefrontal cortex and not to this structure**, so this edge has no
    producer end. Owed at the source: establish it, or withdraw it.
    That entry's Outputs slot carries three lines — a four-member default-mode class naming the
    ventrolateral prefrontal cortex explicitly, and two intraparietal edges — **and no dorsolateral
    target under any name.** The distinction is the producer's own: it separates the two prefrontal
    divisions and names only the ventral one.
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.** **This is the edge the structure's headline function
    depends on** — see Justification.
  - ← **the ventral tegmental area**, the mesocortical projection (`13_neuromodulatory_systems`).
    **Two-ended and confirmed, and this end is the untyped one.** The producer types it as
    dopamine **setting the gain** on prefrontal working-memory and rule representations, payload
    otherwise owed, and this line takes that wording. **This structure is the only entry in this file
    that declares the limb** — the ventrolateral, orbitofrontal / ventromedial, cingulate and
    frontopolar entries declare no dopaminergic input under any name, and the producer marks *which of
    the five prefrontal entries receive it* as owed. **So the class has exactly one member here.**
    **That bears on this structure's own gain story**: it already takes modulatory amplification from
    the mediodorsal thalamus, so **two different gain sources are declared onto one structure and
    neither entry says how they differ.** **Owed at the source.**
  - ← **other prefrontal cortex.** **Class endpoint**, unresolved. Of the four in-file candidates,
    the anterior cingulate cortex declares an output here and the frontopolar cortex declares one to
    a class that covers it; the ventrolateral and orbitofrontal structures declare nothing. Owed at
    the source: name the others, or withdraw.
  - ← **the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus**
    (`08_medial_temporal_lobe`) — the **valence tag**, as at the other prefrontal consumers; payload
    otherwise owed. Terminations in **Brodmann area 9** medially and laterally and **patchily in area
    46**, in the lower bank of the principal sulcus; **ipsilateral only**, in deep layer I, layer II
    and layer VI. **Two-ended.** **The lightest and least consistent of the producer's four lateral
    edges** — the area 46 label was present in one hemisphere and absent in the other of the same
    animal, and absent altogether in a second case. **The area 46 limb lands on this structure's own
    unused divisional sub-elements**, which the Internal structure slot records as named in the
    heading and used by no edge; the producer names both areas, so this is the first edge here that
    could be assigned. **Owed: assign it.**
  - ← **the anterior cingulate cortex** (structure 8 below).
  - ← **the caudal auditory belt**, directly, onto the **caudal principal sulcus** (file 2).
    Unchecked at the source.
  - **Recorded negative: there is no insular input to this structure.**
    `17_insula_claustrum_habenula` split a compound cortical output into named lines and left open
    *whether the class had covered the dorsolateral prefrontal cortex*. **This Inputs slot was read
    against that question and declares no insular source of any kind.** So either the class never
    covered this structure, or it did and the consumer does not carry it. **The question is closed as
    a negative rather than left unchecked**, which is the stronger of the two states.

- **Outputs.**
  - → **the lateral intraparietal area** (`04_dorsal_visual_parietal_stream`), which names **area 46**.
  - → **the anterior intraparietal area** (`06_posterior_parietal`), which declares an input from
  prefrontal areas 46
    and 12.
  - → **sensory cortex**, top-down bias. **Class endpoint**, remaining after the two parietal members
    above are split out, and unchecked at the source — the visual and auditory files were not read there.
    **Checked against `05_sensorimotor_loop` and closed as a negative for that file.**
    Neither somatosensory entry admits a frontal source of any kind: primary somatosensory cortex
    declares two inputs, both from the ventral posterior thalamus, one onto the core and one onto the
    matrix; the second somatosensory area declares the thalamus, the anterior pulvinar, primary
    somatosensory cortex and its callosal partners. **So either this class never covered somatosensory
    cortex, or it did and neither consumer carries it.** The visual and auditory members remain
    unchecked — this closes one file, not the class.
  - → **the frontal eye fields** (structure 2 above).
  - → **premotor cortex** (structure 1 above).
  - → **the basal ganglia**, to the **associative striatum** (`09_basal_ganglia`). The consumer
    declares its cortical source as a class. **Confirmed**, and the same sector caveat
    applies as at premotor cortex above.
  - → **the anterior cingulate cortex** (structure 8 below).

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere** — see the sizing basis above; this structure's share of that
  budget is the open quantity, not the budget. Fan-in unknown on all eight inputs. Basis: per
  hemisphere. Synapses, axons, volumes and myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, so at least two arrays.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular prefrontal
    isocortex.
  - Tangential axes **H, W: to derive.** No pitch measured. **And the tangential organisation is
    load-bearing here in a way it is not elsewhere in this file**: working memory across delays is
    standardly attributed to recurrent local connectivity, so the extent over which recurrence runs
    is the structure's stated function. Owed at the source.

- **Edge latency.** **To derive** on all fifteen edges. **The absence is load-bearing at this
  structure**: a delay period is a duration, and the structure whose job is to hold information
  across delays has no time on any edge into or out of it.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the parietal loop (file 4, reciprocal), the thalamic loop (file
    12), the cortico-striatal loop (file 9), and the cingulate loop (structure 8, reciprocal). **Not
    checkable for two arms** — "other prefrontal cortex" and "sensory cortex" are classes — and one
    inbound arm, from the angular gyrus, has no producer at all. All inherited.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The thalamic input is what makes this a distinct stage rather than
  a region of cortex that happens to be persistently active: it carries **no categorical content**
  and amplifies the cortex's own recurrent connectivity, sustaining rule and working-memory
  representations that are generated in and belong to the cortex. **The thalamus is a temporal
  scaffold, not a source.** That has a direct structural consequence for the build: **the content
  this structure holds lives on an internal recurrent edge, and no such edge is recorded at the
  source.** The external evidence points at the missing edge more specifically here than anywhere
  else in this file — the function is a claim about internal connectivity, and the thalamic edge is
  typed as amplifying exactly that. Naming the dopaminergic producer matters for the same reason: the
  mesocortical projection to this structure is one of the map's best-known edges and had been carried
  as an adjective rather than a source.

## Algorithm

- **Transform.** **The named function is a claim about internal connectivity, and the internal edge
  it names is not recorded.** The copied Function field gives working memory, executive control, goal
  maintenance and top-down attention — **holding and manipulating information across delays.** The
  copied Justification field then states the mechanism the rung above commits to: the thalamic input
  carries **no categorical content** and amplifies **the cortex's own recurrent connectivity**,
  sustaining representations that are generated in and belong to the cortex. **The thalamus is a
  temporal scaffold, not a source.**

  **So the transform is recurrent and the recurrence has no edge.** The copied Justification field
  says it in the file's own words: *the content this structure holds lives on an internal recurrent
  edge, and no such edge is recorded at the source.* **This is the one entry in the file where the
  external evidence points at a missing internal edge specifically rather than generally**, because
  the thalamic edge is typed as amplifying exactly the connectivity that is not declared. Under §5
  the transform is therefore recorded as **a recurrent operation whose recurrent term does not
  exist at any rung**, and it is not supplied here.

- **Arrays.** Two per divisional sub-element. **Two named sub-elements plus one provisional, so four
  or six arrays depending on a question the source has not answered.** Basis: per hemisphere.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `area9.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `area46.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `caudal_principal_sulcus.*` | **provisional** | — | — | — |
  | `*.active` | (to derive, 8, H, W) | 1 bit | {0,1} | dimensionless |

  **The third sub-element is named by an edge and not by the heading.** The copied Function field
  records the **caudal principal sulcus** as a location within area 46 rather than either named area,
  and marks *whether it is a sub-element of area 46 or a separate one* as owed. **The module
  declares it as provisional and does not allocate it**, because allocating it as a peer of area 46
  would double-count and folding it in would discard a distinction two far ends are using.

  **The tangential axis is load-bearing here in a way it is not elsewhere in this file.** The copied
  Shape field states why: **working memory across delays is standardly attributed to recurrent local
  connectivity, so the extent over which recurrence runs is the structure's stated function.** `H, W`
  being *to derive* is therefore not one open axis among many — it is the structure's own mechanism
  left unsized.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive**, **inside the ~640M budget** | neurons, per hemisphere | copied Sizing field |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | log₂ cap, computed |
  | `laminar_extent` | **8** | laminae | copied Shape field — granular prefrontal isocortex |
  | `divisional_sub_elements` | 2 named, 1 provisional | — | copied Function field |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **This structure's share of the 640M is the open quantity, not the budget.** The module must be
  built so the aggregate can never be entered against one structure: it is a sum, and the four
  structures declaring themselves inside it partition it in unknown proportions.

- **Update equation.** **Not written**, and this entry adds a failure the others do not have. Beyond
  the three standard blocks — no count, no fan-in map, emission unset — **two different gain sources
  are declared onto this one structure and neither entry says how they differ.** The copied Inputs
  field carries the mediodorsal **modulatory amplification** and the ventral tegmental **dopamine
  setting the gain** on working-memory and rule representations, and marks the difference **owed at
  the source.** **An update equation with two ungrounded gain terms would have to invent how they
  compose**, and composition is the whole question.

- **State carried between updates.** **`active` only**, one bit per unit, formally. **But this entry
  is where that formal answer is visibly wrong**, and the module says so rather than reporting a
  clean field: a structure whose job is to hold information across delays holds state **on the
  recurrent edge that is not recorded**, and no `active` bit written at the end of one update
  expresses a delay period. **The state exists as a requirement with no extent**, exactly as the
  latency does, and it is not parameter memory.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **8 declared inputs** |
  | outgoing line count | **7 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all fourteen |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed.** The copied Edge latency field marks the absence **load-bearing at this
  structure**: *a delay period is a duration, and the structure whose job is to hold information
  across delays has no time on any edge into or out of it.*

- **Adaptation.** **None.** No learning rule is set. **And this is the entry where that costs the
  most**, since goal maintenance and rule representation are what the copied Function field is about;
  the module runs it open-loop and says so.

- **Open.**
  - **How the two gain sources compose.** Owed at the source.
  - **The recurrent internal edge.** Required by the copied Function and Justification fields,
    unrecorded at any rung.
  - **The caudal principal sulcus: sub-element of area 46, or separate.**
  - **The amygdalar limb is the first edge here that could be assigned to a named sub-element** — the
    producer names both area 9 and area 46 — and the copied Inputs field marks assigning it as owed.
  - **The angular gyrus input has no producer at all**, confirmed by reading that entry; **`other
    prefrontal cortex` and `sensory cortex` are class endpoints**, the second closed as a negative
    against `05_sensorimotor_loop` only.
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# 6. Ventrolateral prefrontal cortex (Brodmann areas 45 and 47)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Controlled retrieval and selection — of words, semantic knowledge and
  responses; the "what" / semantic-control counterpart to the dorsolateral structure above. Granular
  prefrontal isocortex. **Two divisional sub-elements: Brodmann area 45 and Brodmann area 47.**
  **Area 47 is macaque area 12** — Brodmann's own area 47 incorporates the region he identified as
  area 12 in the monkey, which is why the literature writes the area as 47/12. Two other files
  terminate edges on "area 12", so the correspondence is load-bearing: without it those edges land on
  a name this structure does not use. Owed at the source: put the correspondence in the heading.

- **Inputs.**
  - ← **the temporal pole** (`07_anterior_temporal_lobe`). **Two-ended, confirmed**, and
    the producer types it where this end does not: **the amodal concept, for controlled retrieval and
    selection.** That producer records this end as declaring the edge and naming the region and
    **typing nothing — no payload line and no fan-in — and marks it owed here.** It is.
  - ← **the inferotemporal cortex** (`01_visual_pathway`). **Confirmed at the producer itself and
    not through a third file**: its inferotemporal entry declares `→ prefrontal cortex, ventrolateral
    — identity, for controlled retrieval and selection`. **Two-ended, and the producer types the payload where this end does
    not**, naming both the content (identity) and the use (controlled retrieval and selection).
    *(Written by full name; the source file's own heading for this structure is a bare abbreviation.)*
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.**
  - ← **the anterior auditory belt**, directly, onto **areas 12 and 45** (file 2). Unchecked at the
    source. This is the auditory "what" stream reaching prefrontal cortex without waiting for the
    temporal endpoints.
  - ← **the amygdala**, from the **intermediate and magnocellular divisions of the basal nucleus**
    (`08_medial_temporal_lobe`) — the **valence tag**, as at the other prefrontal consumers; payload
    otherwise owed. **The densest of the producer's four lateral edges**: terminations across **area
    12**, which this structure's Internal structure slot resolves to **Brodmann area 47**, in deep
    layer I, layer II and layer VI, continuing dorsally into much of **Brodmann area 45**;
    **ipsilateral only**. **Two-ended.** **This is a second external edge assigning itself to areas 12
    and 45 specifically, arriving from a different file and a different modality than the anterior
    auditory belt above.** **Two independent external demands on one unmade division is a different
    state from one**, and the divisional internal edges below stay owed on stronger grounds than a single
    demand would give.
  - ← **the supramarginal gyrus** (`06_posterior_parietal`).
  - ← **the angular gyrus** (`06_posterior_parietal`).

- **Outputs.**
  - → **Broca's area** (structure 3 above). **The two structures share Brodmann area 45**, so this
    edge crosses a boundary whose location is not agreed — see Shape.
  - → **temporal cortex**, retrieval bias. **Class endpoint**, and it resolves nowhere: the temporal
    pole (file 7) does not declare an input from this structure, and the auditory and visual files
    were not read at the source. Owed: name the target.
  - → **the basal ganglia** (`09_basal_ganglia`). The consumer declares its cortical source as a
    class. **Confirmed. This is the one of this file's four striatal producers that names
    no sector**, where premotor, dorsolateral and orbitofrontal / ventromedial each name one.
    **Owed here: name the sector, or establish that this projection is not sectored.**
  - → **the supramarginal gyrus**, reciprocally, via the **arcuate fasciculus** and **superior
    longitudinal fasciculus III** (`06_posterior_parietal`).
  - → **the anterior intraparietal area**, from **area 12** (`06_posterior_parietal`).

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere**. Fan-in unknown on all seven inputs. Basis: per hemisphere.
  Synapses, axons, volumes and myelination all unknown. **The area 45 overlap with Broca's area makes
  even the partition ill-posed until it is settled**: a neuron count for area 45 cannot be assigned to
  one structure or the other while both claim it undivided.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular prefrontal
    isocortex. **Consistent with Broca's record of area 45 as granular**, which is worth holding
    because the same area is described at two structures.
  - Tangential axes **H, W: to derive.** No pitch measured.
  - **The tangential extent overlaps structure 3's and the overlap is real, not a bookkeeping
    error.** Broca's area is classically areas 44 plus 45; this structure is areas 45 plus 47; area
    45 is the member the two conventional groupings genuinely share. Area 45 is not indivisible — a
    cytoarchitectonic lineage splits it into rostral **45A** and caudal **45B**, and receptor
    architecture splits the same territory into anterior **45a** and posterior **45p** — but whether
    those are one border under two names is not established. **The source proposes 45A / 45a here,
    rostral and continuous with area 47, and 45B / 45p to Broca's area, caudal and abutting area 44,
    and records the proposal as unadopted.** Until it is adopted, neither structure can be allocated.
  - **The overlap is wider than area 45.** Functional imaging routinely includes pars orbitalis
    (area 47) and the ventral part of Brodmann area 6 in what is called "Broca's region", which would
    put this structure's other sub-element and part of structure 1 inside structure 3's functional
    territory. Recorded, unresolved at the source.

- **Edge latency.** **To derive** on all twelve edges. Two of them run in the arcuate fasciculus and
  superior longitudinal fasciculus III, which have entries in file 18 and are where their conduction
  times would be derived from.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the parietal loop (file 6, reciprocal), the thalamic loop (file
    12), the cortico-striatal loop (file 9), and the in-file link to Broca's area. **Not checkable for
    the temporal-cortex arm**, which is a class.
  - *Per-edge latency:* satisfied in form; values open.
  - **Not conformant on Shape**, for the same inherited reason as structure 3: two structures claim
    one undivided area, and neither can be allocated until the claim is divided.

- **Justification (biological).** The "what" counterpart to the dorsolateral structure: its afferents
  are the identity-bearing ones — the temporal pole's amodal concepts, inferotemporal object and face
  identity, the auditory *what* stream's call and identity features — where the dorsolateral
  structure's are spatial and attentional. That the auditory *what* stream arrives here directly,
  onto areas 12 and 45, rather than by way of the temporal endpoints, is a structural claim about
  where the stream terminates and is the reason the area-12 correspondence has to be carried.

## Algorithm

- **Transform.** **No standard name fits, and the job is a selection rather than a mapping.** The
  copied Function field gives **controlled retrieval and selection** — of words, semantic knowledge
  and responses — the "what" counterpart to structure 5. The copied Inputs field types two of the
  afferents at their producers: the temporal pole's **amodal concept, for controlled retrieval and
  selection**, and inferotemporal **identity, for controlled retrieval and selection**. **Both name
  the use and neither names the operation.** *Selection among candidates* is a nameable class of
  operation — a competition, a winner-take-all, a biased gate — and **nothing above says which**, so
  §5 records the gap rather than choosing one.

- **Arrays.** Two per divisional sub-element; **two sub-elements, four arrays.** Basis: per
  hemisphere.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `area45.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `area47.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `*.active` | (to derive, 8, H, W) | 1 bit | {0,1} | dimensionless |

  **Allocation is blocked by the same overlap as structure 3 and it is worth stating from this
  side.** The copied Sizing field puts it exactly: *a neuron count for area 45 cannot be assigned to
  one structure or the other while both claim it undivided* — **so even the partition is ill-posed**,
  not merely unresolved. And the copied Shape field records that **the overlap is wider than area
  45**: functional imaging routinely includes pars orbitalis (area 47) and the ventral part of
  Brodmann area 6 in what is called "Broca's region", which would put **this structure's other
  sub-element and part of structure 1** inside structure 3's functional territory.

  **`area47` carries a second name and the module must hold both.** The copied Function field records
  **area 47 is macaque area 12**, and marks putting the correspondence in the heading as owed.
  **Two edges in this contract terminate on "area 12"** — the anterior auditory belt onto areas 12
  and 45, and the amygdalar limb across area 12 — **so without the correspondence those edges land on
  a name this structure does not use.** The module resolves area 12 to area 47 on the edge and
  records that it is doing so.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive**, **inside the ~640M budget** | neurons, per hemisphere | copied Sizing field |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | log₂ cap, computed |
  | `laminar_extent` | **8** | laminae | copied Shape field — **consistent with structure 3's record of area 45 as granular**, which is worth holding because the same area is described at two structures |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

- **Update equation.** **Not written.** No count, no fan-in map, emission unset; and the transform is
  a selection whose rule is unnamed.

- **State carried between updates.** **`active` only**, one bit per unit. Not parameter memory.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **7 declared inputs** |
  | outgoing line count | **5 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all eleven |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed.** Two edges run in the arcuate fasciculus and superior longitudinal fasciculus III,
  which have entries in `18_white_matter_tracts` and are where their conduction times would be
  derived from.

- **Adaptation.** **None.** No learning rule is set.

- **Open.**
  - **The Brodmann area 45 assignment**, as at structure 3 — and here it makes the partition
    ill-posed as well as blocked.
  - **The internal division between areas 45 and 47 has two independent external demands on it** —
    the anterior auditory belt and the amygdalar limb, arriving from different files and different
    modalities, both terminating on areas 12 and 45 specifically. The copied Inputs field records
    that **two independent demands on one unmade division is a different state from one**, so the
    divisional internal edges stay owed on stronger grounds than a single demand would give.
  - **The striatal output names no sector**, where structures 1, 5 and 7 each name one. **Owed
    here**, per the copied Outputs field: name the sector, or establish that this projection is not
    sectored.
  - **`temporal cortex` is a class endpoint that resolves nowhere.**
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# 7. Orbitofrontal / ventromedial prefrontal cortex (orbitofrontal cortex: Brodmann areas 11 and 13; ventromedial prefrontal cortex: Brodmann areas 14, 25 and 32)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Value, reward and outcome-based decision-making; emotion regulation and
  social or affective evaluation. Assigns and updates the expected value of options. **Five divisional
  sub-elements are named and no edge uses any of them** — areas 11 and 13 orbitally, areas 14, 25 and
  32 medially. **This is the largest named-but-unused sub-element set in the file**, and other files
  are already treating the structure as two: file 9 names **infralimbic cortex**, which is area 25,
  and files 6 and 17 address it as **medial prefrontal cortex**, which is the ventromedial half and
  not the orbital half.
  **The edges sort into two systems and the Function statement covers both in one sentence.** Value,
  reward and outcome-based decision-making is orbital business; the default-mode inputs from the
  precuneus, angular gyrus and posterior cingulate cortex are medial and have nothing to do with
  taste or object value. Owed at the source: split the structure, or assign every edge to a
  sub-element. *(That the edges sort into two systems is inferred here from the edge list, not stated
  at the source as a split.)*

- **Inputs.**
  - ← **the hippocampal formation**, from the **subiculum** (with the adjacent **prosubiculum** and
    distal **CA1**), via the **fornix** (`08_medial_temporal_lobe`) — the **completed episode**;
    payload otherwise owed at both ends, the producer recording the same limit on its parietal and
    cingulate limbs. Terminating principally in **layer III** of Brodmann areas **11**, **13**, **14**
    and **25**; **ipsilateral only**. **Two-ended.** ***This edge uses four of this structure's five
    named-but-unused divisional sub-elements, and it is the first edge in the file with a claim on any
    of them*** — the producer's evidence names the termination areas individually, so the assignment
    arrives with the edge rather than being owed after it. ***And the route is load-bearing rather
    than descriptive***: the projection travels by the **fornix and by no other route**, so the tract
    is a condition on the edge and not a description of it.
  - ← **the amygdala**, from the **basal** and **accessory basal** nuclei
  (`08_medial_temporal_lobe`). Orbital.
  - ← **the gustatory pathway** and ← **olfactory cortex** (file 3). Orbital. Unchecked at the source,
    and **splitting the line is owed**: two modalities are not one source.
  - ← **the inferotemporal and temporal cortex** (`01_visual_pathway`). Orbital. **Checked, and the producer does not declare it.** That file's inferotemporal entry declares one
    prefrontal output only — `→ prefrontal cortex, ventrolateral` — and this structure is a **separate
    entry** in this file from the ventrolateral one, so the ventrolateral declaration does not cover
    it. **This edge is declared at the consumer and at no producer.** The endpoint is also compound —
    *inferotemporal* and *temporal cortex* are not one source — so the split is owed as well as the
    producer end. **Owed at the source: declare it at the producer, or withdraw it.**
  - ← **the basal ganglia**, via the **ventral pallidum → mediodorsal thalamus** limb of the limbic
    loop (`09_basal_ganglia`). **An ambiguity is inherited on this edge**: the mediodorsal entry
    attributes its basal-ganglia input to the dorsal pallidum rather than the ventral one, and that
    file marks it unresolved. **Checked, and the ambiguity is worse than inherited — it is
    a three-file contradiction and this entry is one of the three ends.** **This line believes the limb
    leaves the ventral pallidum**; `12_thalamus`'s mediodorsal entry declares its basal-ganglia input
    from the **internal globus pallidus and substantia nigra pars reticulata** and names no ventral
    source; and `09_basal_ganglia` cannot say which, because **the ventral pallidum is an entry there
    while the dorsal nuclei are sub-elements of a different entry** — one functional stage carried at
    two levels of the hierarchy. **The payloads differ and that is what puts it on the wire**: tonic
    inhibition alone from the dorsal nuclei, **inhibition plus a computed relative value** from the
    ventral pallidum, which that file records as computing value rather than relaying it. **So what
    arrives at this structure on this edge is not settled**, and this structure's value story is what
    depends on it. **Owed at the source, at the boundary question rather than per-edge.**
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.**
  - ← **the posterior cingulate cortex** (`17_insula_claustrum_habenula`). Medial. **Two-ended and confirmed.**
    **The producer's line carries the edge as *not confirmed* and that does not hold — this file
    declares it.** Owed at `17_insula_claustrum_habenula`. The producer names it *the medial-prefrontal
    default-mode partner*, which is the medial half of this structure and not the orbital half — **so
    the far end is already treating this structure as two, as file 9 and file 6 are.** Payload owed at
    both ends.
  - ← **the precuneus** (`06_posterior_parietal`). Medial. **Two-ended and confirmed.**
    **The producer's line carries a compound naming this structure and the medial temporal lobe as
    *neither far end declares it*, and that does not hold for this half — this structure declares
    it.** Owed at `06_posterior_parietal`. The medial temporal half of that compound is unchecked.
  - ← **the angular gyrus** (`06_posterior_parietal`). Medial. **Checked and it is not
    two-ended by name.** That entry's Outputs slot names the ventrolateral prefrontal cortex and not
    this structure; the only line that could carry this edge is its four-member **default-mode
    partners** class, which it marks as unresolved. **So this input is a located candidate for that
    class rather than a declared edge** — the class has a consumer here that declares the input by
    name, which narrows it by one member without closing it. Owed at the source: name the member, or
    withdraw this input.

  **Both parietal inputs above are one-way at this structure, and the direction is the same one.**
  This entry declares no output to the precuneus and none to the angular gyrus, and the far file
  records both absences from its own side — its precuneus entry marks its medial-prefrontal input
  *owed, one producer declares nothing*, and its angular gyrus entry marks the same input owed.
  **Both marks hold.** The Outputs slot below leaves for the amygdala, the bed
  nucleus, the hypothalamus, the ventral striatum and pallidum, the temporal pole, the insula, the
  right inferior frontal gyrus, the periaqueductal gray and a class of autonomic centres — **nothing
  medial-parietal.** So the medial wall's parietal traffic reaches this structure and does not return,
  which is the same shape the habenular finding below records in the opposite direction.
  - ← **the insula** (`17_insula_claustrum_habenula`), reciprocally — the **salience signal** and the
    **interoceptive state**; payload otherwise owed. **Two-ended and confirmed.**
    **The producer declares `→ orbitofrontal / ventromedial prefrontal cortex` by name and types
    it**, naming the interoceptive state as the reciprocal limb, so the edge arrives named and not
    inside a cortical class.

- **Outputs.**
  - → **the amygdala** (`08_medial_temporal_lobe`).
  - → **the bed nucleus of the stria terminalis** (`08_medial_temporal_lobe`).
  - → **the hypothalamus** (`14_brainstem_midbrain_hypothalamus`). **Checked and it is
    producer-only**: that entry's Inputs declare no prefrontal or orbitofrontal source under any
    name. **Owed at the source: accept it there, or withdraw it here.**
  - → **the ventral striatum** (`09_basal_ganglia`). **Two-ended and confirmed, and this
    end is the untyped one.** That entry writes the edge as its own line rather than inside its
    cortical class, precisely because this producer names the ventral sector, and types the payload as
    **value — the expected value of the options.** **This line takes no payload and the far end records
    that it does not.** **Owed here: type it, or take the producer's wording.**
  - → **the ventral pallidum** (`09_basal_ganglia`). The consumer's line also names **infralimbic
    cortex**, which is area 25 and therefore a sub-element of this structure that the heading names and
    no edge uses. **Two-ended and confirmed.** **That entry carries the edge as *the
    producer declares no such edge*, with the repair owed at this file, and that does not hold — it
    is declared, on this line.** Owed at `09_basal_ganglia`. **Both ends record the same
    sub-element debt from opposite sides** — the far end names infralimbic cortex on its endpoint, this
    end names area 25 in its heading, and **neither end has an edge that uses it.** **Payload owed
    here**, the far end typing it as **value** as it does for the striatal limb above.
  - → **the temporal pole** (`07_anterior_temporal_lobe`). **Two-ended, confirmed.** That entry
    declares `← orbitofrontal cortex — value`, and also states that **this file declares no temporal
    target at all.** **That is false — this line is the target.** Owed at
    `07_anterior_temporal_lobe`. **Payload is owed at both ends beyond *value*.**
  - → **the insula** (`17_insula_claustrum_habenula`). **Two-ended and confirmed; payload
    owed at both ends**, which the producer's line marks in the same words.
  - → **the right inferior frontal gyrus** (structure 4 above).
  - → **the periaqueductal gray** (file 14).
  - → **autonomic centres**, remainder. **Class endpoint** after the periaqueductal gray is split out,
    and it resolves nowhere. Owed at the source: name them.

  **One output the far end declares and this entry does not, found and not written as an
  edge.** `17_insula_claustrum_habenula`'s habenula entry declares `← ventromedial prefrontal cortex`,
  onto the **lateral habenula**, typed a **bad-outcome expectation**, and marks the producer as
  declaring no such edge. **It is correct: nothing below leaves for the habenula.** **Owed at the
  source.**
  **The endpoint it names is the medial half of this structure, not the whole**, which is the same
  split the posterior-cingulate input above already forces — so if the split is adopted, this edge and
  that one leave and arrive on the ventromedial sub-elements and neither belongs to the orbital ones.
  **Together with structure 8's habenular limb, two of the three cortical producers of that file's
  value brake are in this file and neither declares its edge.**

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere** — with the caveat that the budget is defined over *granular*
  frontal cortex and area 25 is agranular, so the five sub-elements are not all inside it on the same
  footing. Fan-in unknown on all ten inputs. Basis: per hemisphere. Synapses, axons, volumes and
  myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, so **five arrays**.
  - Laminar axis: **to derive, per sub-element, and it differs across them.** Areas 11 and 13 are
    orbital granular-to-dysgranular; area 25 (infralimbic) is **agranular**; area 32 is transitional.
    A single laminar extent is wrong across this structure, as it is across Broca's area, and the
    source declines to assert one. *(That the standard block does not hold across all five is the
    source's reading of the named areas' architecture, offered there to be checked.)*
  - Tangential axes **H, W: to derive.** No pitch measured. **And the tangential organisation is
    itself in question**: the value axis this structure computes on is **body-relative** — its zero
    and slope are set by motivational state, because there are no receptors for reward — and whether
    that axis is a spatial organisation here or a population code is not established at the source.

- **Edge latency.** **To derive** on all twenty edges. This is the widest edge fan in the file and
  not one of the twenty carries a time.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied for the limbic value loop — out to the ventral striatum and ventral
    pallidum, back via the ventral pallidum → mediodorsal thalamus limb — which closes through files 9
    and 12; and for the reciprocal amygdalar, insular and default-mode loops. **Not checkable for the
    autonomic-centres arm**, which is a class on this side of the scope boundary. Inherited.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The structure is where identity becomes value: object and face
  identity, taste and odour quality, a valence tag from the amygdala and an interoceptive state from
  the insula all arrive, and an expected value leaves toward the ventral striatum. **The step that
  performs that conversion has no edge at the source** — this is the structure in this file whose
  stated job most explicitly names an operation with no declared internal substrate. The value axis
  being body-relative is the reason the conversion cannot be a fixed function of the inputs: the same
  food's value falls once sated, so the mapping is modulated by a state the structure does not itself
  compute.

## Algorithm

- **Transform.** **This is the entry whose stated job most explicitly names an operation with no
  declared substrate.** The copied Justification field states it: **the structure is where identity
  becomes value** — object and face identity, taste and odour quality, a valence tag from the
  amygdala, an interoceptive state from the insula all arrive, and an **expected value** leaves toward
  the ventral striatum — and **the step that performs that conversion has no edge at the source.**

  **And the conversion cannot be a fixed function of the inputs, which is a constraint on any
  equation eventually written here.** The copied fields give the reason: **the value axis is
  body-relative** — its zero and slope are set by motivational state, *because there are no receptors
  for reward* — so **the same food's value falls once sated.** A stateless map from inputs to value
  is therefore ruled out by the contract, not merely unsupported by it. **What the modulating state
  is, and where it enters, is not declared**: this structure does not compute it.

  **A second transform-level fact is that this entry is two systems under one heading.** The copied
  Function field records five named-but-unused sub-elements — **the largest such set in the file** —
  and that **the edges sort into two systems**: value, reward and outcome-based decision-making is
  orbital business, while the default-mode inputs from the precuneus, angular gyrus and posterior
  cingulate cortex are medial and have nothing to do with taste or object value. **Other files are
  already treating the structure as two.** The module keeps one structure, because splitting invents
  the arity two rungs below where it is known.

- **Arrays.** Two per divisional sub-element; **five sub-elements, so ten arrays**, none sizable.
  Basis: per hemisphere.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `area11.*`, `area13.*` | (to derive, **to derive**, H, W) | ≤ uint16 / 1 bit | 0…fan-in / {0,1} | count / dimensionless |
  | `area14.*`, `area25.*`, `area32.*` | (to derive, **to derive**, H, W) | ≤ uint16 / 1 bit | 0…fan-in / {0,1} | count / dimensionless |

  **The laminar axis is *to derive per sub-element and it differs across them*** — areas 11 and 13
  orbital granular-to-dysgranular, **area 25 agranular**, area 32 transitional — so a single laminar
  extent is wrong across this structure as it is across structure 3. **This entry is why the laminar
  extent must be a per-sub-element field even though structure 3 already showed it**: there the two
  values were known and differed; here five values are unknown and are known to differ.

  **One edge does use the sub-elements, and it is the first in the file to do so.** The copied Inputs
  field carries the hippocampal projection terminating principally in **layer III of areas 11, 13, 14
  and 25**, ipsilateral only — **four of the five named-but-unused sub-elements, with the assignment
  arriving on the edge rather than owed after it.** The module records that termination on the edge,
  including the layer, because it is the only laminar termination in this entry.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive**, **inside the ~640M budget with a caveat** | neurons, per hemisphere | copied Sizing field |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | log₂ cap, computed |
  | `laminar_extent` | **to derive**, per sub-element, **and differing** | laminae | copied Shape field |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **The budget caveat is a real arithmetic hazard and the module must carry it.** The copied Sizing
  field states that the ~640M is defined over **granular** frontal cortex and **area 25 is
  agranular**, so **the five sub-elements are not all inside the budget on the same footing.** A
  module that put the whole structure inside the aggregate would be adding agranular tissue to a
  granular budget.

- **Update equation.** **Not written.** No count, no fan-in map, emission unset — **and the equation
  needs a modulating state term the contract does not supply**, per Transform above.

- **State carried between updates.** **`active` only**, one bit per unit, formally — **and formally
  is not enough here.** The body-relative value axis requires the structure's mapping to be modulated
  by a motivational state held across time, and **the contract declares no such state and no edge
  carrying it into this structure.** Recorded as a requirement with no extent; not parameter memory,
  never summed with it.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **10 declared inputs** |
  | outgoing line count | **10 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all nineteen |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed. This is the widest edge fan in the file and not one edge carries a time.**

- **Adaptation.** **None.** No learning rule is set — **and this entry's Function field is
  *updates* the expected value of options**, so the absence removes the verb from the job
  description. Recorded; not repaired.

- **Open.**
  - **Whether this structure is one or two.** Owed at the source: split it, or assign every edge to a
    sub-element.
  - **What arrives on the basal-ganglia edge is not settled, and it is a three-file contradiction
    rather than a local ambiguity.** This contract has the limb leaving the **ventral pallidum**;
    `12_thalamus` attributes the mediodorsal nucleus's basal-ganglia input to the **internal globus
    pallidus and substantia nigra pars reticulata**; and `09_basal_ganglia` cannot say which, because
    the ventral pallidum is an entry there while the dorsal nuclei are sub-elements of a different
    entry. **The payloads differ and that is what puts it on the wire** — tonic inhibition alone from
    the dorsal nuclei, **inhibition plus a computed relative value** from the ventral pallidum. **The
    module must not resolve this**; it records the contradiction and names the three ends.
  - **The hypothalamic output is producer-only**, checked; the inferotemporal input is
    **consumer-only**, checked, and its endpoint is compound as well.
  - **The gustatory and olfactory line names two modalities on one bullet** — splitting owed.
  - **The habenular limb the far end declares is absent here**, and so is any output to the precuneus
    or the angular gyrus: **medial-wall parietal traffic reaches this structure and does not
    return.** Recorded, not written.
  - **`autonomic centres` is a class endpoint** on this side of the scope boundary.
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# 8. Anterior cingulate cortex (Brodmann areas 24 and 32)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** Conflict and error monitoring, effort and outcome valuation, and
  motivation — the medial-wall control and salience node that signals when more control is needed.
  **Agranular-to-dysgranular cingulate cortex.** **Two divisional sub-elements are named and no edge
  uses either** — Brodmann areas 24 and 32. The midcingulate structure in file 17 uses the prime
  notation 24′ / 32′ for its own territory, which implies this structure holds the unprimed pair;
  the relationship between the two numberings is stated in neither and is owed at the source.
  **A cell-class sub-element is also present: von Economo (spindle) neurons**, a large projection cell
  type concentrated in this structure and in the insula. Whether it has its own targets — and so
  whether it is a sub-element an edge could terminate on — is not stated at the source.

- **Inputs.**
  - ← **the insula** (`17_insula_claustrum_habenula`) — the **salience signal**: *this event is
    behaviourally relevant now*. **Whether what leaves is a scalar, a pointer, or a switching command
    is not established at the producer**, and that non-establishment is stated there rather than
    glossed. Fan-in: to derive. **Two-ended and confirmed**, the producer marking it
    *salience → control*. **This end is the untyped one and takes the producer's type above.**
  - ← **the hippocampal formation**, from the **subiculum**, via the **fornix**
    (`08_medial_temporal_lobe`) — the **completed episode**; payload otherwise owed at both ends.
    Terminating in **layer III of Brodmann area 24a only**; **ipsilateral only**. **Two-ended.**
    ***The sub-element restriction is finer than this structure's own headings and it cannot
    currently receive it***: the Internal structure slot names Brodmann areas **24** and **32** as
    divisional sub-elements that no edge uses, and this edge terminates in **24a and not 24b or
    24c**. **Owed: divide Brodmann area 24, or record that this edge carries a sub-element claim the
    structure cannot yet receive.** **This is the second such demand in the file** — the
    ventrolateral structure has two on its own unmade division — and all three arrive from the same
    producer and the same study.
  - ← **the amygdala** (`08_medial_temporal_lobe`).
  - ← **the dorsolateral prefrontal cortex** (structure 5 above).
  - ← **the midline / intralaminar thalamus** (`12_thalamus`). **The producer does not declare its cortical
    target as a class covering this structure without naming it.** That entry declares
    `→ anterior cingulate cortex` **on its own line**, and marks the class beside it —
    `→ further cortex, diffusely, beyond the anterior cingulate` — explicitly as **the residue of the
    line the named edge came out of.** **The split is made there and this structure is the named
    member.** Payload owed at both ends.
    **A second thalamic edge reaches this structure and is not declared here.** That file's anterior
    nuclei entry declares `→ anterior cingulate cortex` and marks it *declared at one end only*,
    observing that this consumer names the midline / intralaminar thalamus and not that nucleus.
    **That mark is exact.** This line names one thalamic source and there are two.
    **Owed at the source: accept the anterior-nuclei limb here, or withdraw it there** — it is the
    cingulate half of the classical Papez target and it is unconfirmed at its consumer.
  - ← **the midcingulate cortex**, reciprocally, via the **cingulum**
    (`17_insula_claustrum_habenula`). **Two-ended and confirmed; payload owed at both
    ends**, and the producer names the same route. **The reciprocal pair with that structure is the
    only relationship in this entry that is complete at both ends in both directions** — the outgoing
    limb below is its partner.

- **Outputs.**
  - → **the dorsolateral prefrontal cortex** (structure 5 above), recruiting control.
  - → **the midcingulate cortex** (`17_insula_claustrum_habenula`) — a **scalar reward-value signal**:
    expected reward magnitude, and a response to the mismatch between expected and received reward,
    firing to unexpected reward and to expected-but-omitted reward. **Its coordinate frame is
    body-relative**, zero and slope set by bodily and motivational state. Fan-out: to derive.
    **Two-ended and confirmed.** The consumer carries this payload verbatim and records it
    as *the only edge in that section with a stated coordinate frame*. **The consumer also carries this
    end's caution — that the body-relative reading is Class 2, the source's own inference offered to be
    checked — so the two ends are copies and their agreement certifies transmission, not corroboration.**

  **Three outputs the far end declares and this entry does not, found and not written as
  edges.** `17_insula_claustrum_habenula` names this structure as the producer of an edge to **three
  of its six entries**, and this Outputs slot declares none of them:
  - **→ insula** — the far end's insula declares `← anterior cingulate cortex`, payload owed, and
    records that **the return arm of a relationship it calls reciprocal is unconfirmed at its
    producer.** This entry declares the inbound limb above and not this one.
  - **→ lateral habenula** — the far end types it a **bad-outcome expectation**, one of three cortical
    limbs of the value brake.
  - **→ posterior cingulate cortex** — payload owed at the far end.
  **All three are owed at the source, not written here from the far end's declaration.** **This is not three separate omissions but one shortfall**: this entry carries four
  outputs, and a structure that the adjacent file names as a producer three times over should not have
  a four-line Outputs slot. **The shortfall is invisible from inside this file, because every one of
  the three missing edges is a far end.**
  - → **premotor cortex and the supplementary motor areas** (structure 1 above).
  - → **autonomic centres.** **The far side of these centres — the visceral effectors they drive —
    is outside the map's scope, so this edge terminates at the scope boundary on its output side.**
    **It is nonetheless a Class endpoint on this side of the boundary**: the brainstem autonomic
    nuclei that would receive it have entries, and none was checked at the source. Naming them is a
    different question from the scope boundary and is owed.

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown. **This structure is not
  attributed to the ~640M budget** and should not be counted inside it without a decision: the budget
  is defined over granular frontal cortex anterior to the corpus callosum, and this cortex is
  agranular-to-dysgranular. Fan-in unknown on all six inputs. Basis: per hemisphere. Synapses, axons,
  volumes and myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, plus an open question about the cell-class sub-element, which is not a sheet axis and
  would not be one.
  - Laminar axis: **7, not 8** — layer 4 thin or absent, as this is agranular-to-dysgranular cortex.
    The source declines to assert the standard eight-layer block here and marks the laminar sets per
    sub-element as owed. **To derive per sub-element**, bounded at 7.
  - Tangential axes **H, W: to derive.** No pitch measured.

- **Edge latency.** **To derive** on all ten edges.

- **Invariant conformance.**
  - *Co-instantiation:* satisfied — reciprocal with the dorsolateral prefrontal cortex, reciprocal
    with the midcingulate cortex via the cingulum, and closing the salience pair with the insula.
    **Not checkable for the autonomic-centres arm**, which is a class up to the scope boundary.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The control signal this structure sends the dorsolateral prefrontal
  cortex is **not a conflict signal carrying its own frame**. Human single-unit recording during an
  interference conflict task, analysed with a method that tested explicitly for a conflict-coding
  axis, did not find one; what the signal does instead is raise the gain on the already-framed coding
  of the correct sensorimotor response, so that under conflict the population activity shifts along
  the response-coding directions. **That absence was decoded rather than merely unmeasured**, which
  is a different and stronger state than "not yet known", and it is the sharpest such result in this
  file. The reward output has the opposite character: a scalar value axis, coding expected reward
  magnitude and the mismatch between expected and received reward, whose zero and slope are
  body-relative in the same way the orbital value axis is. **So this structure's outputs are
  characterised and the operation that produces them is not** — nothing at the source says where
  conflict is detected inside it, and the internal edges, including area 24 ↔ area 32, are unrecorded.
  *(The gain-on-a-framed-signal reading and the body-relative reading of the reward axis are the
  source's own inferences, marked there as offered to be checked.)*

## Algorithm

- **Transform.** **The output is characterised and the operation that produces it is not — and the
  characterisation is unusually strong, which is what makes the gap sharp.** The copied Justification
  field records that the control signal to structure 5 is **not a conflict signal carrying its own
  frame**: human single-unit recording, analysed with a method that **tested explicitly for a
  conflict-coding axis, did not find one.** What the signal does instead is **raise the gain on the
  already-framed coding of the correct sensorimotor response**, so that under conflict the population
  activity shifts along the response-coding directions.

  **That absence was decoded rather than merely unmeasured**, which under §5b is **resisted**, a
  different and stronger state than *unknown* — and writing *to derive* over it would discard a
  finding. **The module carries it as a result.**

  **The reward output has the opposite character and is the best-typed line in the file.** The copied
  Outputs field gives it as **a scalar reward-value signal**: expected reward magnitude, and a
  response to the mismatch between expected and received reward, **firing to unexpected reward and to
  expected-but-omitted reward**, with a **body-relative coordinate frame**, zero and slope set by
  bodily and motivational state. **So one output is a gain with no frame of its own and the other is
  a scalar with a stated frame**, and nothing above says where inside the structure either is
  produced.

- **Arrays.** Two per divisional sub-element; **two sub-elements, four arrays**, plus a cell class
  that is **not a sheet axis and would not be one.** Basis: per hemisphere.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `area24.threshold` | (to derive, **≤ 7**, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `area32.threshold` | (to derive, **≤ 7**, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `*.active` | (to derive, **≤ 7**, H, W) | 1 bit | {0,1} | dimensionless |
  | von Economo (spindle) neurons | **not an array axis** | — | — | — |

  **The laminar axis is bounded rather than valued: 7, not 8**, layer 4 thin or absent, this being
  agranular-to-dysgranular cortex — and the copied Shape field marks the per-sub-element sets as
  **owed**. A bound is not a value and the module stores it as a bound.

  **The von Economo cell class is the one sub-element in the file that would break the shape type if
  admitted.** It is a large projection cell type concentrated here and in the insula; **whether it
  has its own targets — and so whether it is a sub-element an edge could terminate on — is not stated
  at the source.** A cell class is not a sheet axis, so the module declares it beside the shape and
  not inside it.

  **And one inbound edge makes a sub-element claim this structure cannot receive.** The hippocampal
  projection terminates in **layer III of Brodmann area 24a only** — not 24b or 24c — while this
  contract's divisional sub-elements are **area 24 and area 32** undivided. **Owed: divide area 24,
  or record that this edge carries a claim the structure cannot yet receive.** The module records the
  second, because dividing it here would invent the arity.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive**, **not attributed to the ~640M budget** | neurons, per hemisphere | copied Sizing field |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | log₂ cap, computed |
  | `laminar_extent` | **to derive**, bounded at **7** | laminae | copied Shape field |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **The budget exclusion is explicit and load-bearing**: the copied Sizing field says this structure
  **should not be counted inside the ~640M without a decision**, the budget being defined over
  granular frontal cortex anterior to the corpus callosum and this cortex being
  agranular-to-dysgranular. **The module excludes it and records that the exclusion is a stated
  decision, not an omission.**

- **Update equation.** **Not written.** No count, no fan-in map, emission unset — **and the two
  outputs would need two different equations**, one producing a gain with no frame and one a scalar
  in a body-relative frame, from an operation the contract does not locate anywhere inside the
  structure. **The internal edges, including area 24 ↔ area 32, are unrecorded.**

- **State carried between updates.** **`active` only**, one bit per unit. Not parameter memory.
  **The body-relative zero and slope of the reward axis are a state this structure's output depends
  on and this contract does not declare**, as at structure 7 and for the same stated reason.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **6 declared inputs** |
  | outgoing line count | **4 declared outputs** |
  | latency, every edge | **to derive** — copied Edge latency field, all nine |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed.**

- **Adaptation.** **None.** No learning rule is set. **The reward-mismatch response the copied
  Outputs field describes — firing to unexpected reward and to expected-but-omitted reward — is a
  prediction error in everything but name**, and a prediction error is the natural driver of a
  learning rule. **The module does not supply one.** Learning rules are Micky's.

- **Open.**
  - **Three outputs the adjacent file declares and this contract does not** — to the insula, to the
    lateral habenula, and to the posterior cingulate cortex. **Not one shortfall per edge but one
    shortfall**: a structure named as a producer to three of that file's six entries carries a
    four-line Outputs slot. **Owed at the source; not written here from the far end's declaration.**
  - **A second thalamic source is declared at its producer and not here** — the anterior nuclei,
    the cingulate half of the classical Papez target. This contract names one thalamic source and
    there are two.
  - **Whether the von Economo cell class is an endpoint an edge could terminate on.**
  - **The relationship between this structure's areas 24 / 32 and the midcingulate 24′ / 32′** is
    stated in neither file.
  - **`autonomic centres` is a class endpoint** whose brainstem members have entries and were not
    checked.
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# 9. Frontopolar cortex (Brodmann area 10)

## Contract — copied verbatim from the architecture entry

- **Function → structure.** The most anterior and largest granular prefrontal area — metacognition,
  prospective memory, and cognitive branching, the management of multiple goals and subgoals. Widely
  regarded as the least-understood cortical area, and relatively neuron-rich in humans. **Two
  divisional sub-elements, defined by where the afferents come from**: the **lateral** part, whose
  afferents are more than 90% from other frontal areas, and the **medial / midline** part, which takes
  substantial temporal-lobe input including clear auditory connections. **The two parts therefore sit
  at different distances from the sensory periphery inside one structure**, and an edge terminating
  "on frontopolar cortex" is under-specified. Splitting is owed at the source, and unusually the basis
  for it is already quantitative.

- **Inputs.**
  - ← **other association / prefrontal cortex**, supramodal, onto the **lateral** part. **Class
    endpoint**, unresolved: **none of the four other prefrontal structures in this file declares an
    output here.** Owed at the source as cross-file edits within file 11, or withdraw.
  - ← **auditory association cortex** — the **anterior belt**, the **parabelt**, the **rostral
    superior temporal gyrus** and the **temporal pole** — directly and densely, onto the **medial**
    part (files 2 and 7). **The producer does not declare the temporal-pole limb**
    (`07_anterior_temporal_lobe`): that file's six outputs contain no frontopolar target, so this limb is declared here and at no producer.
    Owed at that section's source: declare it there, or withdraw it here. **The belt and parabelt limbs
    are confirmed** — see structure 2 and structure 6, and `02_auditory_pathway`'s belt entry declares
    the frontal pole among its direct prefrontal targets by name.
  - ← **other sensory modalities** — **parietal**, **inferior temporal** and **occipital** cortex —
    present but of lower density. **Class endpoint**, and a threefold one: each of the three names a
    lobe rather than a structure. **The parietal limb was checked at the source and no structure in
    file 4 or file 6 declares an output here.** Owed: repair at those files, or withdraw the limb.
  - ← **the mediodorsal nucleus** (`12_thalamus`) — **no categorical content; modulatory
    amplification, raising the gain of this structure's local recurrent connectivity.**
    **The producer names this structure on its own output line and types it in the words above; it
    is not declared there as a class.** **See the frontal eye fields entry for the reading this
    corrects and for the arity question it opens.**

- **Outputs.**
  - → **other frontal / prefrontal cortex**, from the structure as a whole; whether the signal leaves
    from one part is not stated. **Class endpoint**, unresolved: **none of the four other prefrontal
    structures in this file declares an input from here.** Owed at the source as cross-file edits
    within file 11.

- **Sizing.** **To derive**, both terms. Neuron count soft / unknown, **part of the ~640M granular
  prefrontal budget per hemisphere**, and **this structure takes the largest share of it** — the
  source records Brodmann area 10 as the largest single prefrontal subdivision, and separately as
  relatively neuron-rich in humans. **That is an ordering constraint on the partition, not a count**:
  it says this structure's share exceeds every other prefrontal structure's, and it is the only
  partition constraint the file supplies. Fan-in unknown on all four inputs. Basis: per hemisphere.
  Synapses, axons, volumes and myelination all unknown.

- **Shape.** **Sheet**, rank 3 — **(laminar sub-element, H, W)** — instantiated once per divisional
  sub-element, so two arrays: medial and lateral.
  - Laminar axis: **8** — 1, 2, 3, 4, 5a, 5b, 6a, 6b, layer 4 undivided. Granular prefrontal
    isocortex.
  - Tangential axes **H, W: to derive.** No pitch measured. **The medial/lateral division is the one
    tangential boundary in this file with a quantitative basis** — the afferent-origin fractions above
    — and it is still not a pitch.
  - **A species caution attaches to the division and to the arrays it implies.** The pattern is very
    similar in Cebus and macaque despite more than 40 million years of separation, which is
    reassuring; but the **marmoset** differs, its labelled neurons extending ventrally into inferior
    temporal visual association cortex, which the other two do not show. **So a direct visual input to
    the frontal pole exists in at least one primate and not in others**, and which pattern the human
    follows is not established at the source.

- **Edge latency.** **To derive** on all five edges.

- **Invariant conformance.**
  - *Co-instantiation:* **not checkable, and this is the weakest case in the file.** Both of this
    structure's cortical arms — the supramodal input and the sole output — are classes that resolve
    nowhere, and the two structures that would close them are unnamed at both ends. The auditory arm
    reaches file 2, whose far end is unchecked, and the one limb that was checked, the temporal pole,
    does not declare it. Only the mediodorsal arm closes. All inherited; none repaired here.
  - *Per-edge latency:* satisfied in form; values open.

- **Justification (biological).** The structure's premise in the literature — supramodal, with little
  direct sensory input — **is true of the lateral part and false of the medial part**, and the
  correction is quantitative rather than a hedge: retrograde tracer injections in lateral area 10 find
  more than 90% of afferents arising from other frontal areas, while injections on the midline surface
  receive substantial temporal-lobe projections including clear auditory ones. **Among all prefrontal
  areas this one has the densest interconnections with auditory association cortex**, spanning a large
  antero-posterior extent of the superior temporal gyrus from the temporal pole back to parabelt and
  belt; auditory pathways make up the largest single component of its extrinsic connections, and it is
  described as the main frontal auditory field. **So audition is not one sensory exception to a
  supramodal rule here; it is this structure's principal external connection**, and the other
  modalities are present at lower density rather than absent. That inverts the premise the heading
  carries, and it is the reason the medial/lateral split is a structural fact rather than a
  refinement. **The internal edge between the two parts is required and not recorded**: if the medial
  part receives the acoustic input and the lateral part is the frontally-connected one, the two must
  communicate for the input to bear on the output at all.

## Algorithm

- **Transform.** **The least-understood cortical area in the file, and the contract is honest about
  it**: metacognition, prospective memory, and **cognitive branching — the management of multiple
  goals and subgoals.** No operation is named at any rung and none is supplied here.

  **What the contract does supply is a structural correction with a number behind it**, and it
  inverts the premise the heading carries. The copied Justification field: the literature's premise
  is *supramodal, with little direct sensory input*, and that **is true of the lateral part and false
  of the medial part.** Retrograde tracer injections in lateral area 10 find **more than 90% of
  afferents arising from other frontal areas**, while injections on the midline surface receive
  substantial temporal-lobe projections including clear auditory ones. **Among all prefrontal areas
  this one has the densest interconnections with auditory association cortex** — auditory pathways
  are the largest single component of its extrinsic connections, and it is described as **the main
  frontal auditory field.** **So audition is not one sensory exception to a supramodal rule here; it
  is this structure's principal external connection.**

  **That makes the medial/lateral split a structural fact and it leaves the two parts unconnected.**
  The copied Justification field states the consequence: **if the medial part receives the acoustic
  input and the lateral part is the frontally-connected one, the two must communicate for the input
  to bear on the output at all** — and **the internal edge between them is not recorded.** The module
  declares two parts and cannot connect them.

- **Arrays.** Two per divisional sub-element; **two sub-elements, four arrays.** Basis: per
  hemisphere.

  | array | shape | dtype | range | units |
  |---|---|---|---|---|
  | `medial.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `lateral.threshold` | (to derive, 8, H, W) | ≤ uint16 | 0…fan-in | count of active inputs |
  | `*.active` | (to derive, 8, H, W) | 1 bit | {0,1} | dimensionless |

  **The medial/lateral division is the one tangential boundary in this file with a quantitative
  basis — and it is still not a pitch.** The copied Shape field says both halves of that: the
  afferent-origin fractions are a real quantity, and they divide the structure by *where its inputs
  come from* rather than by a coordinate, so `H, W` remain **to derive** exactly as everywhere else.

  **A species caution attaches to the division and therefore to the arrays.** The pattern is very
  similar in Cebus and macaque despite more than 40 million years of separation; **the marmoset
  differs**, its labelled neurons extending ventrally into inferior temporal visual association
  cortex. **So a direct visual input to the frontal pole exists in at least one primate and not in
  others, and which pattern the human follows is not established.** The module carries the caution on
  the sub-element rather than dropping it, because the division is what the arrays are cut on.

- **Parameters.**

  | parameter | value | unit | origin |
  |---|---|---|---|
  | `neuron_count` | **to derive**, **inside the ~640M budget and taking the largest share of it** | neurons, per hemisphere | copied Sizing field |
  | `fan_in` | **to derive**, all inputs | inputs per unit | copied Sizing field |
  | `threshold_bits` | **≤ 16** | bits | log₂ cap, computed |
  | `laminar_extent` | **8** | laminae | copied Shape field — granular prefrontal isocortex |
  | `lateral_frontal_afferent_fraction` | **> 90%** | fraction of afferents | copied Function and Justification fields |
  | `tile_pitch` | **to derive** | mm | no figure at any rung |

  **The largest-share line is an ordering constraint on the partition, not a count**, and it is **the
  only partition constraint the file supplies.** It says this structure's share of the 640M exceeds
  every other prefrontal structure's. **The module stores it as an ordering relation** — a
  constraint that becomes arithmetic the moment any one share is measured — and never as a number.

- **Update equation.** **Not written.** No count, no fan-in map, emission unset; the transform is
  unnamed; and the internal edge the Justification field requires is unrecorded, so even the
  structure's own two halves cannot be composed.

- **State carried between updates.** **`active` only**, one bit per unit. Not parameter memory.

- **Edge storage.**

  | term | value |
  |---|---|
  | incoming line count | **4 declared inputs** |
  | outgoing line count | **1 declared output** |
  | latency, every edge | **to derive** — copied Edge latency field, all five |
  | update interval | **unset** |
  | bytes per value | **unset** |

  **Not computed. Five edges is the narrowest fan in the file**, against the largest share of the
  neuron budget.

- **Adaptation.** **None.** No learning rule is set.

- **Open.**
  - **Co-instantiation is not checkable here and this is the weakest case in the file**, per the
    copied Invariant conformance field: **both cortical arms — the supramodal input and the sole
    output — are classes that resolve nowhere**, and the two structures that would close them are
    unnamed at both ends. **Only the mediodorsal arm closes.** The module records a structure with
    one closed loop and two open classes; it does not report conformance.
  - **None of the four other prefrontal structures in this file declares an output here, and none
    declares an input from here.** Owed at the source as cross-file edits *within* file 11 — which is
    the one class of repair in this entry that needs no other file.
  - **The temporal-pole limb is declared here and at no producer**, re-checked at
    `07_anterior_temporal_lobe`.
  - **`other sensory modalities` is a threefold class** — parietal, inferior temporal and occipital
    cortex — **each naming a lobe rather than a structure**, and the parietal limb was checked
    against files 4 and 6 and found undeclared.
  - **The internal edge between the medial and lateral parts.**
  - Tile geometry, sparsity, connection topology, scheduling. Surface before touching.

---

# Section-level material

## 6. Edges, and what the module records on each

**106 edge declarations at this rung: 63 in, 43 out**, across nine structures. **Eighteen of the 106
are declarations of edges whose two ends are both in this file**, written once at each end, so the
106 declarations are **99 distinct edges** — §0a. *(The 106/63/43 are the architecture header's;
the in-file pairing and the distinct count are recomputed by the module from the declarations, not
transcribed.)*

**Every one of the 106 carries a latency of *to derive*. There is no exception anywhere in the
file.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, never its number alone.** A
bare number goes silently wrong the moment a file is split, merged or renumbered, and the code has no
reader to notice. **`Brain_config.Endpoint` rejects a stem that does not begin `<nn>_`**, so this is
enforced rather than asked for. Endpoints in this file's contract that carry no stem are recorded
with the state that fits — a class, a structure with no entry, a far end whose file has not been
opened beside this one — and **an endpoint without a stem is never a claim that no far end exists.**

**The far ends this file reaches, and the state the module records on each:**

| far file | state |
|---|---|
| `01_visual_pathway` | inferotemporal in to structure 6, **two-ended**; inferotemporal / temporal in to structure 7, **consumer-only and compound**; the V4 limb **declared there and not here** |
| `02_auditory_pathway` | caudal belt to structures 2 and 5, **confirmed at structure 2**; anterior belt to structure 6 and belt / parabelt to structure 9 — **the producer writes its prefrontal targets on one line, so the arity is owed there** |
| `04_dorsal_visual_parietal_stream` | lateral intraparietal both ways at 2 and 5, ventral intraparietal to F4 and from the pursuit area, middle temporal and medial superior temporal — **two-ended and confirmed** |
| `05_sensorimotor_loop` | superior parietal area 5 both ways, area 3a and the second somatosensory area in, primary motor out — **and the articulatory output is producer-only there as well as here** |
| `06_posterior_parietal` | supramarginal, precuneus, angular gyrus, anterior and medial intraparietal — the heaviest pairing in the file |
| `07_anterior_temporal_lobe` | temporal pole in to 6 and out from 7, **two-ended**; the frontopolar limb **declared here and at no producer** |
| `08_medial_temporal_lobe` | **five limbs in — three amygdalar to structures 1, 5 and 6, two hippocampal to structures 7 and 8**; amygdala and bed nucleus out from 7 |
| `09_basal_ganglia` | four cortico-striatal producers, **three naming a sector and one not**; ventral striatum and ventral pallidum out from 7 |
| `12_thalamus` | mediodorsal in to five structures, ventral anterior / ventral lateral in to 1, midline / intralaminar in to 8 — **and no structure in this file declares any output back** |
| `13_neuromodulatory_systems` | ventral tegmental in to structure 5 only, **the class having exactly one member here**; **no ascending limb is declared anywhere in this file** |
| `14_brainstem_midbrain_hypothalamus` | superior colliculus out, **discharged and typed at the consumer**; hypothalamus out, **producer-only**; periaqueductal gray out |
| `17_insula_claustrum_habenula` | insula both ways at 7 and 8, anterior insula in to 4, midcingulate both ways, posterior cingulate in to 7 — **and four outputs the far end declares that this file does not** |
| `18_white_matter_tracts` | the corpus callosum on structure 4's callosal edge; the arcuate and superior longitudinal fasciculus III on structures 3 and 6 |

**Two whole-file absences the module reports as findings rather than as gaps in its own table.**

1. **No structure declares an output to any thalamic nucleus.** Seven declare a thalamic *input*.
   `12_thalamus` declares the return traffic as two class endpoints — a layer-6 reciprocal modulator
   and a **layer-5 driver** — and **the layer-5 driver is what makes that nucleus a higher-order,
   cortically-driven relay rather than a first-order sensory one.** The drive originates here and is
   declared nowhere here. **Owed at the source; writing six edges on the far end's class alone would
   invent the per-structure arity that is precisely what is unknown.**
2. **No structure declares an output to any neuromodulatory nucleus**, covering four of that file's
   endpoints at once. **This file receives four brain-wide modulatory projections and declares one of
   them, and sends four ascending control limbs and declares none.**

**Eleven endpoints are classes** — brainstem saccade generators, autonomic centres, sensory cortex,
temporal cortex, temporoparietal cortex, other prefrontal cortex, other frontal cortex, other
association cortex, and the threefold sensory class at structure 9. **A class endpoint has no unit to
co-instantiate**, so co-instantiation is unverifiable on every edge that has one, and the module
reports that rather than passing them.

**One edge leaves the map by rule rather than by omission**: the premotor corticospinal projection
terminates at muscle, outside the source's scope on the body side. **It terminates at the scope
boundary; it does not close, and that is correct rather than defective.** The module's edge check
must not report it as unresolved.

**One recorded negative:** there is **no** edge from structure 1 to the middle temporal area — that
consumer declares its frontal input from the frontal eye fields instead. **A checked absence is
carried so the check is not repeated**, and it is not an edge.

## 7. Representation, per line

**Declared once per line and inherited by every consumer of that line** — units, numeric range and
normalization, update timing, and coordinate frame. **Latency is not declared here**: it is an
architecture field, copied under §3, and a second record of it would disagree with the first.

**Almost every line in this file is `to derive` on units, range and frame**, because the architecture
template has no payload field and this file's contract carries a payload only where the source's
producer typed one and the architecture carried it across. **Update timing is `event-driven` on every
line without exception**: no structure in this file is a sensor, none has a rate of its own, every
one is driven by its inputs, and **there is no system clock to borrow a rate from.**

**The lines that are not entirely open, and they are the module's whole Representation content:**

| line | what the contract fixes |
|---|---|
| mediodorsal nucleus → structures 2, 5, 6, 7, 9 | **no categorical content**; a modulatory amplification of the consumer's own recurrent activity — **role, not payload.** Frame: **none** |
| anterior cingulate → midcingulate | **scalar** reward value: expected magnitude, and the mismatch between expected and received. Frame: **body-relative**, zero and slope set by bodily and motivational state — **the one stated frame in the file** |
| frontal eye fields → superior colliculus | a saccade goal — the cortically selected target location, **eye-centred**. Typed at the consumer; **untyped at the producer** |
| amygdala → structures 1, 5, 6 | the **valence tag**: a gain on perception, attention and memory encoding, **carrying no identity of its own.** Frame: **none** |
| hippocampal formation → structures 7, 8 | the **completed episode**, payload otherwise owed at both ends; laminar termination stated |
| insula → structures 4, 7, 8 | the **salience signal** — *this event is behaviourally relevant now*. **Whether what leaves is a scalar, a pointer, or a switching command is not established at the producer**, and that non-establishment is stated rather than glossed |
| ventral tegmental area → structure 5 | dopamine **setting the gain** on working-memory and rule representations |
| structure 7 → ventral striatum / ventral pallidum | **value — the expected value of the options.** Typed at the consumer; **this file takes no payload and the far end records that it does not** |
| structure 1 → primary motor cortex | the planned action: sequenced and shaped, **not yet a muscle command** |

**Four of these are gains rather than content**, and the module marks them `role = MODULATORY` while
leaving `carries` open: a gain has no units of its own and inherits the range of what it acts on.
*(That the amygdalar valence tag is modulatory rather than driving is this rung's reading of the
copied phrase* carrying no identity of its own; *the mediodorsal case is the architecture's own
word.)*

## 8. The scheduler cannot be written, and the wall here is total

The second structural invariant is per-edge latency: nonzero, finite, **heterogeneous**, in real time
units, and **no global clock may be assumed.** A loop with real heterogeneous delays settles by its
own dynamics; the same loop broken by registers becomes an iterated map whose trajectory depends on
the update rate. **Those are two different systems computing two different things**, so a uniform
delay is a substitution and not an approximation.

**A uniform one-step delay is a legitimate thing this rung may eventually choose** — set every
latency equal and pick an interval short enough to carry the finest one. **It cannot be chosen here,
for three reasons and the third is specific to this file:**

1. **Every latency reads *to derive*** — no conduction time, no synaptic delay, no loop latency, and
   **no myelination figure at any of the nine structures** to derive one from. There is not even a
   qualitative timing fact to hang a bound on.
2. **The scheduling discipline is not set and is Micky's** — the largest open item at this rung.
3. **The loops this section sits on are the slow ones.** Every structure here is a node in a loop
   that **leaves the frontal lobe and returns** — through parietal cortex, thalamus, basal ganglia
   and cerebellum; through the superior colliculus; through the ventral striatum and pallidum. **An
   interval short enough to carry the finest edge in the system is set by the fastest loop in the
   map, not by the slowest**, and the fastest is nowhere near this file. So even a borrowed interval
   would be borrowed from a file this one does not hold, and would then govern structures whose own
   timescales are unmeasured.

**The module therefore contains no loop, no step counter and no `for t in range(...)`.** Where the
scheduler would go it raises. **Every sentence containing *cycle*, *frame*, *step*, *tick* or
*register* has been checked against the question of whether it invents a clock the system does not
have.**

## 9. What blocks the implementation

| what is missing | where it is missing from | which rung repairs it |
|---|---|---|
| **neuron counts, all nine structures** | the source | measurement — and **one of the nine closes by reading a paper already cited** |
| **fan-in, all 63 inputs** | the source | measurement |
| **tile pitch, all nine structures** | the source | measurement — one figure per structure converts every Shape from open to computed |
| **what any edge carries** | the architecture has no payload field | **an open field at the architecture rung**, recorded there as Micky's to set |
| **the Brodmann area 45 assignment** | proposed at the source, **unadopted** | the source — and until it is adopted **two structures cannot be told apart** |
| **the scheduling discipline** | not set | **Micky** |
| **the learning rules** | not set | **Micky** |
| **graded vs binary emission** | not set | **Micky** |
| **tile geometry, sparsity, connection topology** | not set | **Micky — surface before touching** |

**The neuron-count absence is what gives this file its character.** The module produces **zero stated
bytes across nine structures.** The only figure it can report is the ~0.96–1.28 GB aggregate ceiling,
which is a **sum** and cannot be attributed to any structure. **A sizing report that returns nothing
per structure is the correct output here, and a module returning plausible per-structure numbers
would be lying.**

**The learning rule's absence remains the least blocking**, for the standing reason: a threshold that
is never written is a construction cost, not a memory, so the module is coherent with `threshold` as
a read-only buffer. **It simply does not learn.**

## 10. Completion test

**An entry is finished when the code can be written from it without making a single further choice.**

**By that test every entry in this file is unfinished, and none of them can be finished at this
rung.** Nothing above is a gap in this document: **three are measurements owed at the source**
(counts, fan-ins, pitch), **one is an open field at the architecture rung** (the payload), **one is
an unadopted resolution at the source** (area 45), and **four are on the list that must be surfaced
before it is touched.**

**What the module does implement, and it is less than the sized sections' and is not nothing:**

- the structure, sub-element and edge declarations as data, including **twenty-five divisional
  sub-elements** and one cell class that is not a sheet axis, the laminar extents where the contract states them, and **the states where it does
  not** — `to derive`, `contested`, and a bound of 7 — kept distinct rather than collapsed;
- the threshold-gate forward operation, which is the whole of the arithmetic the rungs above specify;
- **an independent recomputation of the sizing table, which correctly returns nothing per structure**,
  and the aggregate prefrontal ceiling computed from the 640M figure and the log₂ cap;
- **a mechanical check that every one of the 106 declarations resolves** to a structure in this file,
  a named far-end file carrying a stem, a declared class endpoint, a structure with no entry, or the
  scope boundary — with the recorded negative and the scope-boundary edge excluded from the
  unresolved count rather than counted as failures;
- **a count of which in-file edges are declared at one end only**, which is where the inherited
  producer-side gaps show up as a number rather than as prose;
- **the declaration-count reconciliation of §0a**, rebuilt from the module's own edge table and
  checked against the architecture header structure by structure, so the agreement is a computed
  result and not an assertion in a document.

## 11. What the module imports, and what it may not redefine

**The vocabulary is imported and not redefined.** `Structure`, `Population`, `Endpoint`,
`Representation` and `Edge` are declared **once**, in `Brain_config.py`, together with the element
classes, the open states, the counting bases and the endpoint kinds. **The reason is mechanical and
it is the same reason §3 copies verbatim rather than paraphrasing:** an edge that leaves this file is
declared at both ends, in two files, and **two files cannot describe one edge in agreement when the
type describing it is defined twice.** A private edge type per module makes every cross-file edge a
translation, and translation is the failure this rung exists to avoid.

**What stays in the module is the content** — the counts, shapes, extents, sub-elements, edges and
findings of this section — **because that is where they are derived and where a fidelity pass diffs
them against the architecture entry above.** Config holds the vocabulary; the module holds the
content.

**Three shared behaviours are called rather than re-implemented:** `sizing_report`, `edge_report` and
`representation_report`. **And five unset decisions are reached by calling into config and raising,
not by quietly choosing** — `emission`, `fan_in_map`, `allocate`, `schedule` and `learn` — so that a
module that needs one of them stops with what it is waiting on and whose decision it is.
