# Brain architecture — design file

**Date:** 2026-08-19
**Owner:** Micky.
**Purpose:** the specification for `Brain_architecture_<nn>_<section>_<date>.md` — what that document is for, what
may enter it, the shape of an entry, and how it is verified. **Hand this to Claude in Brain
architecture sessions only.** Kythera sessions do not get this file, and do not need it.

**This file stands alone on purpose.** The twins are never worked in the same session, so a design
file that only makes sense beside its counterpart is useless. Where this duplicates the Kythera
design file, the duplication is deliberate.

**The line:** *the design of the document is not content of the document.* The architecture contains
the architecture. It does not contain the rules for writing an architecture, the state of any pass
over it, or the history of how it got that way.

---

## 1. What the Brain architecture is

The **biological** architecture. It specifies the structural units, the data flow between them, the
memory each unit requires, the latency on each edge, and each unit's conformance to the structural
invariants — with **biological justification throughout**.

It is the build-facing companion to the description: where the description records what the structure
*is*, this document states the structure that realizes it.

**No learning rule, no device, and no chosen hardware appear here.** The compute and memory a
structure needs are *derived* from the biology, never fitted to a part.

**The scope boundary is the source's and is inherited, not re-decided here.** In: the whole central
nervous system, and the **peripheral sensory transducers** — retina, cochlea, olfactory epithelium,
semicircular canals, otolith organs, taste buds, skin and muscle receptors — because they are where
the data flow starts. Out: the **non-neuronal layer** (glia, vasculature, ventricles / CSF) by
decision rather than deferral; the **peripheral and enteric nervous systems**; peripheral **nerves
and ganglia** that carry a signal without transducing it; and everything past the transducer on the
body side — **muscle, skeleton and their dynamics.** An architecture edge that points at the body
side says so, exactly as the source's does.

**What moves is therefore not specified anywhere on the ladder.** The driver pools drive something
no rung describes. Whatever it turns out to be will be servos or artificial muscle, which do not
have the dynamics of real muscle, so staying biological does not dodge the problem — it relocates
it. **Not scoped, not decided, and not this document's to decide.**

## 2. Derivation path, and the only content source that counts

**The source is twenty files**, `human_brain_<nn>_<section>_<date>.md`, in data-flow order. They are
the **ground truth and the only content source**, and the Brain architecture is derived from them
directly. Nothing carries from any other architecture file — not text, not history, not hardware.
**An architecture file is never a content source for another architecture file.**

**No session loads the whole source.** It is far past a session's capacity, so co-loading it with this
file and the architecture is impossible and is not attempted. A session gets **the files one
architecture file needs — its own source file (§10). The file map — filenames, contents, entry counts
and sizes — lives once, in the source's own design file, and is deliberately **not** copied here.**

**Reaching a file the session does not hold.** Most edges leave their own section, so every pass will
meet endpoints whose far end sits in a file it does not have — file 01 alone reaches into files 2, 4,
6, 8, 9, 11, 12, 13, 14 and 15. Two permitted responses, and the session says out loud which it took:
**ask Micky for that file**, or **record the far-end dependency in the architecture file at hand**,
naming the source file and structure. Writing an edge whose far end was never read is
not a third option — it produces an architecture that passes inspection on its own and disagrees
with a source file nobody opened.

**Keyword search across the files a session was not handed is correct and intended** — locating the
far end of an edge, checking whether a region has an entry, counting occurrences of a claim. The
prohibition on skimming applies to the files the session *was* handed, which are read top to bottom.

**Repair order — attribute before repairing.** When a fidelity pass finds a gap, find which rung it
entered on before fixing anything.
- Wrong here but right in the source → introduced in derivation; fix here.
- Wrong in the source too → the repair starts at the source, which is **the rung where claims are
  checked against the literature**. **A gap found there is a research request**, not a stop: search it,
  bring back a candidate carrying its **method and species**, and let the candidate wait at the gate.
  Claude may offer candidate figures; **a figure enters carrying what it was verified against, or it
  is marked a candidate** — verification runs to the literature, never to a person. **The verified-only
  rule governs what enters, not whether the work gets done** —
  stopping at the gate without searching is the work not being done, wearing the rule as a reason.
  Ask before searching only when the session's remaining budget will not cover the search, and say
  that is why.
- **Never patch this rung for a gap inherited from the source, and never leave one silent.** Patching
  creates an added edge, and the next fidelity pass will correctly flag it and delete it. **Recording
  does not**: the gap is written into the architecture file at hand, at the entry it belongs to,
  naming what is missing and which rung it must be repaired at. **A gap that is neither patched nor
  recorded reads, on the next pass, exactly like a subject with nothing to say about it** — and the
  pass that could have seen it is the one that just ended.
- **A repair that lands at the source stops the pass and is reported before architecture work
  resumes.** Reading a source file to attribute a finding is ordinary and needs no announcement.
  **Writing to one does not**: under the source's verified-only rule anything
  new entering a source file carries **what it was verified against** — a source opened or a search
  run — or it is marked a **candidate** and says so. Either way **Micky is told what was written
  before the pass continues**, which is a notification rule and not a gate.
- **Data and instruction verify in opposite directions.** Everything above concerns **data** — claims
  about how the brain is — which verifies up the ladder and, at the source rung, against the
  literature, **never against a person**. **Instruction** — how this project works, including this
  design file — verifies **against Micky and nothing else**, there being no rung above a design file.
  **If a paper could settle a dispute about the line it is data; if only Micky could, it is
  instruction.** A repair to this file is instruction and is his; a repair to an edge or a figure in
  an architecture file is data and is researched. The reason is that a
  candidate and a verified line read identically once the session that wrote them is gone, and the
  architecture edits that follow will have been built on whichever it was. **Stopping is what keeps
  the two distinguishable.** A pass that backtracks silently and carries on delivers an architecture
  resting on a source change nobody agreed to. The source carries its **own inventory of known
  gaps**, so most inherited gaps are identifiable before they are re-discovered — see §9.

## 3. Vocabulary — biological

Justifications are **biological only**. Engineering terms (memory in bytes, bandwidth) are allowed
only where a size or budget must be named; the *reason* stays biological. Size in generic memory
(bytes / GB / TB), **not VRAM** — VRAM presumes a GPU, and no hardware is named yet.

**When a biological word carries a fact, the fact must survive the word.** Deleting or replacing a
word must not delete the claim. Check what a sentence is *asserting* before dropping its vocabulary.
*(The worked case: a summary line reading "cochlea → cochlear nucleus → …" reduced to "cochlear
nucleus → …" drops the claim that anything precedes the first central station, and what is left reads
as complete.)*

**Names are written out; an abbreviation is a second label, never the only one.** A structure is
written by its full name, with the literature's abbreviation given **once, in parentheses, at the
entry that owns the name**. This is the source's convention and it is inherited here for a reason
specific to this rung: **the dangling-edge diff of §9 only works if names are unique**, and an
abbreviation is a second string for the same structure — the diff cannot tell that the two match. A
letter-string that carries a dominant meaning in another field is spelled out in full rather than
kept; the collisions that bite hardest are short, uppercase, and drawn from the same naming habit as
the reader's other life. **AI** for the anterior insula is the standing example, and it collides
with the field this project is in.

**Two of the source's own entry headings are bare abbreviations** — file 1's inferotemporal
cortex and file 4's ventral intraparietal area. A heading is what other files quote when they name
an endpoint, so those two are the ones most likely to enter this document as a second name for a
structure that already has one. **Write the full name; do not carry the heading's string.**

## 4. Structural invariants

Two rules bind every structure and every edge. Each is stated once in the document, with its
biological justification, and its conformance is noted per structure. Violating either yields a
structure that cannot be built correctly.

**Whole-pathway co-instantiation.** Every structural unit exists and is active from the outset. No
sequential bring-up, no unit that comes online later, no enable flag gating a unit off until
"needed." A feedback loop with a missing stage in it is not a loop.
*Biological why:* the pathway forms and runs as one active loop, not as a chain switched on stage by
stage — the kitten-carousel argument. **The source states the general case directly**: every major
pathway in the map closes back on itself, there is no terminating stage, and the feedback arms drawn
in each file *are* the re-entrant channel.

**Two of the source's named loops pass through stages the source does not describe, and one is not
closable in principle.** The **cerebro-cerebellar** loop runs through the pontine nuclei and the red
nucleus, neither of which has an entry anywhere in the twenty files — and the corticopontine stage
is recorded as *transforming* the payload rather than relaying it, so a computing stage sits inside
the loop with no slot. The **hippocampal / Papez** loop's return arm runs via parahippocampal
cortex, which likewise has no entry. **A missing stage inside a closed loop is worse than a missing
terminus**: it breaks traceability rather than leaving a visible dangling end. **Co-instantiation
therefore cannot be satisfied for those two loops at this rung**, and the repair is the source's, not
this document's. The **circadian** loop is a different case: its closing limb is melatonin in the
bloodstream and one of its forward joints is a peripheral ganglion that transduces nothing, so it is
closed in the body and **outside the source's boundary by rule** rather than missing from it.

**Per-edge latency.** No edge has zero latency, and no two edges need the same latency. Every
projection takes a nonzero, finite time to carry a signal. That time is a property of the **edge**,
is stated in **real time units**, and is **heterogeneous**. An edge whose latency the biology has
not fixed reads **to derive**. An edge with a latency of zero does not exist.
*Biological why:* conduction and synaptic transmission take real time, and those times differ by
orders of magnitude across the map. Where timing is itself the signal, the spread across edges *is*
the computation and not noise around it.

**The spread is now measured at the loop scale and it is enormous** — the source's loop inventory
runs from the millisecond-order thalamo-cortical and cortico-cortical loops, through the
intermediate basal-ganglia and cerebro-cerebellar loops, to a twenty-four-hour circadian loop, with
the fast loops running *inside* the slow ones and none of them coming to rest. That is the
per-edge-latency invariant's strongest support: no single delay, and no single update rate, can serve
a system whose loops nest across that range.

*A finding about the source, recorded and not repaired here, and it is narrow.* The source states
that span as **ten orders of magnitude** and illustrates it with **a millisecond against a day**,
which computes to **7.94**. But the floor the exponent needs **is** in the source: file 02 records the interaural time-difference computation as **working at tens of
microseconds**, and gives it a structural consequence — the trapezoid body and lateral lemniscus are
heavily myelinated because speed matters at that scale. **Tens of microseconds against a day is 9.24 to
9.94 orders, so ten is right and the illustrative pair is wrong.** The repair is to the endpoints
quoted, not to the exponent, and it belongs at the source rung. **Quote the span with the binaural
floor, or do not quote a pair.**

**Not every edge in the source is a projection.** The source types **endocrine and blood-borne
edges** — the pineal's melatonin arm, the hypothalamus's blood-borne sensing — and it types an
**optical** one at the very first structure of the very first file: the retina's input is *light*,
photon flux imaged on the photoreceptor sheet, explicitly recorded as not a neural edge and with
fan-in *not applicable*. **So the first edge in the whole map is not a projection**, which makes this a
general case and not a late curiosity. None of these is conduction plus synaptic transmission, so
**the invariant's justification does not cover them**, and its requirement still does: they take real,
finite, wildly different time. An architecture carrying such an edge states its latency in real time
units and does not claim the biological *why* above as the reason. *(Inferred by Claude from the
source's typing of those edges; the entries are Class 1 from the source, the reading is not.)*

**A third class, and it is mechanical.** The cochlear amplifier is a feedback loop *inside the sensory
organ*: the outer hair cells add force back into the basilar-membrane travelling wave through prestin,
a voltage-driven protein that changes cell length directly. The source types it as an internal edge
whose **fan-in and fan-out read *not applicable — the transfer is mechanical***. Abolishing it costs
40–60 dB. **So a load-bearing edge in the map moves force, not signal**, and no synaptic or conduction
term applies to it at all.

**There is no global clock in the described system, and none may be assumed.** A continuously operating brain
runs on propagation delay, not on a shared beat. What makes a re-entrant loop well-defined is not a
register but the physical delay already on every edge. A loop with real, heterogeneous delays settles
by its own dynamics; the same loop broken by registers becomes an iterated map whose trajectory
depends on the update rate. Those are two different systems computing two different things. **Uniform
delay is not an approximation of heterogeneous delay; it is a substitution.**

**A uniform one-step delay is an implementation choice, not an invariant.** Setting every latency
equal, and choosing a step short enough to carry the finest one, is a legitimate thing the **code**
rung may decide to do. It is not a fact the description supports, it is not architecture, and it must never
be written into this document as though it were. **Watch every sentence containing *cycle*, *frame*,
*step*, *tick*, or *register*, and ask whether it has just invented a clock the system does not
have.** Choosing the **scheduling discipline** belongs to the design rung and is **Micky's**; it is
not set, it gates the edge-storage figure in §6, and an entry may record that it is unset but may
not quietly assume one.

## 5. Per-structure entry template

**Every structure in a Brain architecture file gets the same fields, in the same order, so that a
missing one is visible at a glance.** That is the whole reason for a template: an omitted field and an
open field look identical unless the field is always present.

**The fields exist to hold what the source describes.** Where the source describes something no field
holds, the field list is wrong and gets a new field — the source is the specification and this
template is not. Adding one obliges a **retrofit** over structures already written: the field is added
to a structure when that structure is next worked, in data-flow order, not in a sweep. That is a cost
in work, and work is never a reason to leave the description unrecorded.

- **Function → structure** — what the unit does, and the structural form that does it.
- **Inputs** — where it receives from.
- **Outputs** — where it projects to. (Kept separate so loop directions stay explicit.)
- **Sizing** — parameter memory under the threshold-gate model of §6, in bytes.
- **Shape** — rank, axes and extents under §6a, or **to derive** per axis. A structure that cannot be
  allocated has not been specified.
- **Edge latency** — per edge, in real time units, or **to derive**. Never in frames, cycles, or
  steps: a latency stated in steps has assumed a clock.
- **Invariant conformance** — how the unit satisfies co-instantiation and per-edge latency.
- **Justification (biological).**

**An edge names its target structure, not its class.** "Gain-control feedback to the sensory front
end" is a defect the moment there is more than one sensory front end: it fails silently instead of
visibly, and it reads as complete at both ends. Name the structure.

**And where the source terminates an edge on a sub-element, the edge names the sub-element.** This is
not a refinement of the rule above, it is what the rule requires as soon as the source is read: the
geniculate drive into V1 is **four** edges terminating on **4Cα**, **4Cβ**, the cytochrome-oxidase
blobs of layers 2/3 with layer 1, and **4A** — and one of the four does not reach layer 4 at all.
Collapsing them to "→ V1" loses the fact that the blue–yellow channel bypasses the granular layer,
which is a structural claim about where a channel arrives. **The consequence for §9 is mechanical: the
name set the dangling-edge diff runs on must contain sub-elements as well as structures**, or the diff
will report 4Cα as a structure with no entry and be right for the wrong reason.

**Crossings and laterality are load-bearing.** Never drop a crossing, a decussation, a bilateral
projection, or a crossed-then-recrossed route. They set which side each line serves and cannot be
re-derived from either endpoint. A double crossing is especially easy to lose, because both ends see
a same-side connection.

**Added edges are drift too.** Fidelity runs both ways. An Inputs/Outputs entry that is **not in the
source** is as much a defect as one that is missing, and it is **harder to catch**, because a
well-formed invented edge reads exactly like a derived one.

### 5a. Two things the source's slot template carries and this one does not. **Open.**

Stated as the finding it is, with no options and nowhere here to record an answer.

- **Internal structure and internal data flow.** The source requires of **every** entry a slot
  naming the region's sub-elements and the typed edges **between them** — each with a payload, a
  fan-in and a fan-out, on the same discipline as inter-region edges. Sub-elements go as deep as the
  described organisation, the test being whether a division projects to different targets or
  carries a different payload. This template has **no field for any of it**, so a derivation that
  follows the template drops every structure's internal circuit. It is also a **sizing** matter and
  not only a shape one: §6's own worked fan-ins — the granule cell and the Purkinje cell — are
  properties of *internal* edges of one entry, so the arithmetic this document already performs is
  reading a slot the template does not have.
- **The payload on every edge.** The source writes each edge twice, in the producer's Outputs and
  the consumer's Inputs, and each declaration carries what the edge *carries* — the property, its
  units, its coordinate frame, and where it matters what it explicitly does **not** carry. That
  redundancy is what makes a payload mechanically checkable. This template's Inputs and Outputs
  fields name endpoints and carry no payload, so a build-facing document derived from it states which
  structures are wired together and not what is on the wire.

**Nothing about the template's own stability is what stands in the way of either.** The description records
internal circuits whose divisions project to different targets and carry different payloads, and it
has a payload on every edge; a template answerable to the description therefore has fields for them, and
the cost of adding the fields is the retrofit named at the head of this section. **What the fields
are called and what exactly they must contain is Micky's to set**, and until it is set an entry
neither invents them nor pretends the description has nothing in them. *(That the description's carrying
these things obliges the fields is Claude's reading. The source's slots are Class 1.)*

**Tested against file 01, and the internal-structure gap is a blocker rather than an omission.** A
structure's sub-elements cannot be relegated to a field that does not exist, because **the Inputs and
Outputs fields depend on them**: the geniculate edges terminate on 4Cα, 4Cβ, the blobs of layers 2/3
and 4A; V1's forward output leaves from named sub-elements with measured laminar composition (thick
stripes: layers 2/3 67%, 4B 23%, 4A 7%, layers 5/6 2%) and from **two distinct cell classes of one
sub-element** — 4B's spiny stellates project to the middle temporal area and its pyramids to V2, and
they are largely separate cells. A file 01 architecture written with no sub-element vocabulary cannot
state its own Inputs and Outputs at all. **The sub-elements are therefore not a further level of
detail below the edges; they are the endpoints the edges have.**

**The payload gap has a worked demonstration in the same file.** V1's function consumes **eye of
origin** — binocular convergence, ocular-dominance columns, disparity all require it — the chiasm
declares it as a payload component, and the geniculate's four output edges say only "still monocular"
without saying which eye. The source records that as a dangling requirement on the entry. **A template
with no payload field cannot represent the defect, so a derivation inherits it with nowhere to mark
it** — and inherits it silently, which §9's repair order exists to prevent.

### 5b. Two classes the template was not written for

**Transmission-only structures.** The source holds **seven** entries that compute nothing and
carry other entries' edges — the optic chiasm, the spinal cord white matter, and the five tracts of
the white-matter file. Their shape is settled at the source: real sub-elements (parallel channels,
not a circuit), **internal data flow: not applicable** as a positive statement, **Inputs and Outputs
as routing statements rather than payload transfers**, and **fan-in and fan-out reading *none*,
because no synapse occurs there**. Their neuron and synapse slots read **none**.

**Transducers**, likewise: the source's scope decision puts every sensory line's first stage in the
map, and a transducer is not a threshold gate (§6).

Both fill the existing template rather than needing a new one, and both make its **Sizing** field
read **zero parameter memory** for a structure that is nonetheless load-bearing. **A tract is also
where the physical substrate of a latency lives** — the myelination slot is populated across the
source, and the tract entries are what a derived conduction time would be derived from. *(The
source's shape for these entries is Class 1. That they fill this template unchanged, and that their
sizing is zero rather than to-derive, is Claude's reading and is not the source's claim.)*

## 6. Sizing method — threshold-gate parameter memory

**This one is a model, and it is the place to say so.** A threshold is real structure; **equal weights
are not** — real synapses differ in strength, and the equal-weight assumption is what collapses a
neuron's stored state to one number and makes the cost log₂(fan-in). It is the modeling choice the
whole method rests on, and it is answerable to the description in the same direction as everything
else: a structure the source describes as computing with graded weights is a finding against this
model, not a structure to be flattened to fit it.

Each neuron is a **threshold gate over equal-weight inputs**: it fires when the count of active
inputs crosses a threshold. Under equal weights the only stored value per neuron is that
**threshold**, costing **log₂(fan-in) bits**.

- **Parameter memory per structure = neurons × log₂(fan-in) / 8 bytes.**
- **Fan-out is never stored.** A projection's cost lives on the *target's* fan-in. (The source
  records fan-out anyway, and for a different reason: a projection cannot be *constructed* from the
  receiving end alone. That is a build requirement, not a memory one, and the two do not conflict.)
- **Synapses are not stored as individual weights.** The synapse count enters only by setting the
  fan-in whose logarithm fixes the per-neuron cost. log₂ caps hard — any fan-in ≤ ~65,000 is ≤ 16
  bits — so **memory tracks neuron count, not synapse count.**
- **Per structure, never averaged.** Fan-in ranges from ~4 in a granule cell (2 bits) to ~150k–200k
  in a Purkinje cell (≈ 18 bits). Both of those are fan-ins on **internal** edges — see §5a.
- **A fan-in of one costs zero bits, and the source states several.** log₂(1) = 0: a neuron with a
  single input has no count to compare against a threshold, so it stores nothing. This is not a corner
  case — file 02 gives **three exactly-known fan-ins**, and two are one: a type I spiral ganglion
  neuron contacts exactly one inner hair cell, and the medial nucleus of the trapezoid body's
  principal cell receives one calyx of Held. The spherical bushy cell's one-or-two endbulbs cost 1
  bit. **The pathway's most timing-critical stages are its cheapest, and for the same reason they are
  precise** — a low fan-in is what buys timing fidelity. Do not treat a zero here as a missing value:
  it is a measured one, and it is different from the transducer's zero and from a graded element's
  to-derive.
- **The log₂ bound absorbs fan-in disputes, and the test measured by how much.** V1's synapses per
  neuron is open across a **6.5× range** in the source — 2,300–5,600 measured in macaque V1, ~7,000 as
  a human cortical average, ~15,000 derived from human synapse and neuron densities, a gap the source
  records as genuine and unexplained. Under log₂ that whole range is **12 to 14 bits**, moving V1's
  store by 1.17×. The **neuron count** over the same structure is open across 2.1× (~140M lower bound
  against ~280–310M headline) and moves it by 2.1×. **So the count is the sensitive term and the
  fan-in is not**, which is worth knowing before spending research effort: pinning synapses per neuron
  would sharpen almost nothing, and pinning a neuron count halves or doubles a figure.
- **A transducer is not a threshold gate.** It stores no threshold and the log₂ cost does not apply.
  *(Charging a threshold to every photoreceptor produces a retina store that does not exist. The
  repair is to strike it, not to tighten it.)*
- **Nor is a non-spiking element, and that exception is wider than the transducer one.** The retina's
  horizontal cells and bipolar cells respond with **graded changes in membrane potential and generate
  no action potentials**; some amacrine cells spike and some do not; only the ganglion cell reliably
  does, and the conversion to spikes therefore tracks **transmission distance** — the cell whose axon
  has to leave the eye — rather than depth in the processing chain. A bipolar cell is not a transducer
  and it computes: the entire ON/OFF split the rest of the visual line carries is made at one synapse
  by the receptor type on two bipolar classes, one sign-conserving and one sign-inverting. **So there
  is a class of element that computes, is not a transducer, and does not cross a threshold**, and the
  exception above does not reach it. The same shape appears again inside the lateral geniculate
  nucleus, where the local interneuron's dendritic release sites **release transmitter without
  generating an action potential**, so one of that structure's internal edges carries something that
  is not a rate on an axon.
  **What a graded element stores, if anything, is not settled by this method and must not be defaulted
  to zero or to log₂(fan-in).** Zero asserts it holds nothing; log₂(fan-in) asserts a threshold it
  does not have. It reads **to derive**, and it is a real quantity — three of the retina's five cell
  classes are in this state and none of the three has a count in the source either. *(That the
  threshold-gate model does not cover a graded element is Claude's reading; the non-spiking physiology
  is Class 1 from the source. Whether the model is extended, or these elements are modelled some other
  way, is Micky's.)*
- **A sign-inverting stage is not expressible as a count of active inputs crossing a threshold.** In
  the outer retina **hyperpolarisation is the excitatory response** — photoreceptors hyperpolarise to
  light and release more transmitter in the dark, and because these cells do not spike, hyperpolarising
  is not inhibiting. Any derivation that reads depolarisation as activation reads the outer retina
  exactly backwards. Recorded here because it is a constraint on the model, not on the structure.
- **A transmission-only structure stores nothing either**, for the stronger reason that it has no
  neurons at all (§5b).

**The source's entry count is not this document's structure count.** The source has **99 entries**
across the twenty files (counted), and several of them bundle **multiple structures** into one slot
set — the basal ganglia entry covers striatum, pallidum, subthalamic nucleus and substantia nigra;
the corpus callosum entry carries four tracts; the arcuate entry carries five. The source marks
those bundlings as owed on their own entries. **Sizing runs per structure, and the dangling-edge diff
needs one unique name per structure**, so a bundled source entry either becomes several entries here
or is recorded as a bundle whose split is owed **at the source**. It is not silently split at this
rung: splitting invents the arity.

**Three memory classes, and this document counts only the first.** Recorded because two of the three
have no slot anywhere, and a reader who sums the Sizing column will believe they have the memory
requirement.
1. **Parameter memory** — thresholds. The only class the Sizing fields carry. *(A threshold that is
   never written is a construction cost, not a memory. Whether any threshold is ever written is the
   learning rule, which is **not set**. An entry may record that it is not set; it may not quietly
   assume one.)*
2. **State** — values carried between updates that no rule stores (light adaptation is the clear
   case). **Not counted anywhere, and never summed with parameter memory.**
3. **Edge storage — the values in flight, which the per-edge-latency rule creates.**
   `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`.
   It scales with the **reciprocal of the update interval**, so it ties the timing decision directly
   to a resource. **Not sizable at this rung** — it depends on the scheduling discipline, which is
   Micky's and unmade. What can be said is *where it will be large*. **Recorded, not resolved.**

## 6a. Shape — the second calculation at this rung

Parameter memory is a scalar per structure and a scalar cannot be allocated against. **Every structure
also carries a Shape**: the rank of its array, what each axis is, and the extent of each axis or **to
derive**. This is derived the same way the memory figure is — counts, areas and pitches from the
description, no device anywhere in the arithmetic.

**Four shape classes cover what the description contains.**

1. **Sheet** — a tangential extent with a laminar stack. Rank 3: **(sub-element, H, W)**, where H × W
   is the tangential tile grid and the sub-element axis is laminar. All cortex, and the retina.
2. **Laminated nucleus** — rank 3 again, **(lamina, H, W)**, but the lamina axis is a **channel or an
   isofrequency plane** rather than a cortical layer, and the map axes may be fewer.
3. **Non-laminated nucleus** — rank 2, **(cell class, N)**, where no orderly map is recorded.
4. **Transmission-only** — **not an activity array at all.** A tract holds no neurons and no
   thresholds; its shape is a **routing index** from source line to destination, rank 1. Recording it
   as a zero-length tensor would assert it holds state it does not have.

**The map axis is 2-D in vision and 1-D in audition, and that falls out of the description rather than
being imposed.** A retinotopic sheet indexes the visual field in two dimensions; a tonotopic sheet
indexes frequency in one, with the second axis carrying something else or nothing. **A shape field
makes that difference explicit at the point where an array is allocated**, where the prose word "map"
does not.

**The tile calculation, and what it needs.**

    neurons per unit surface = volumetric density × thickness
    tiles = surface area ÷ (tile pitch)²
    neurons per tile = neurons per unit surface × (tile pitch)²
    parameter memory per tile = neurons per tile × ceil(log₂(fan-in)) ÷ 8

**Surface density is derivable well before pitch is.** V1: ~60,000 neurons/mm³ over ~2 mm thickness is
**~120,000 neurons per mm² of surface**, and ~2,600 mm² × 120,000 = **312M**, which closes against the
~280–310M headline — an independent route to the same figure. **The pitch is the missing term**, and
it is a single measurement per structure that converts the whole shape from *to derive* to computed.

**Tile pitch is a measurement, not a choice, and this is the line that keeps it at this rung.** The
description records it where it has been measured: V2's stripe cycle at **3.5–4 mm** centre-to-centre
and its intrinsic columnar patches at **211 × 342 µm** (≈ 0.0722 mm², giving **~46,800 patches** over
V2's ~3,380 mm²); V4's colour modules as **1–3 mm** clusters; the medial geniculate's cell rows at
**50–100 µm**. Where the description has no figure, the pitch reads **to derive** and the shape reads
**(sub-element, to derive, to derive)** — which is a marked gap, not an invitation to pick one.

**Sparsity is on the other side of that line and does not come here.** The description uses *sparse*
only qualitatively — a sparse projection, sparsely branched, sparsest in layer 4 — and never as a
fraction of a population active at once. **It is therefore a decision and not a measurement**, and a
decision does not enter this rung however convenient it would be to have it beside the shape.

**Counts must partition to the sub-elements the edges terminate on, or the partition reads *to
derive*.** A structure-level count and a sub-element-level edge do not connect, and the gap blocks
allocation rather than description. Most partitions are open; **the lateral geniculate nucleus shows
what a closed one looks like** — magnocellular ~0.22M over two layers is ~110,000 per layer,
parvocellular ~1.55M over four is ~387,500 per layer, and the two sum to the ~1.77M headline exactly.

## 7. Conventions

**Changing one obliges a retrofit over structures already written, and the decision is Micky's** —
not because a convention is fixed, but because a convention is a choice about how to write the
description down, and choices on this ladder are his. A convention that the source contradicts is
wrong and is changed; the cost of changing it is work, and work is never the reason a description
loses.

- **Order** = data-flow order = source order.
- **Every file carries, in its front matter, the list of cross-file checks it contains.** One line
  per far file that has been held open beside this one and whose shared edges are diffed and stemmed,
  **naming the far file by stem and carrying no date.** This is present state, not history: it records
  *which cross-file checks this document contains* — the same kind of statement as the far-end
  dependency block, and checkable against the file's own contents. It does not narrate what changed,
  who changed it, or what the file used to say, and it never says that a file lacking a line is an
  older copy. **A line is added when its check is done.**
  **What it is for and what it does not solve.** A filename's date says when a file was written, not
  which checks are in it. The list is what a reader who has the file open can check. **It does not
  help a reader choosing between copies before opening one** — for that, compare the candidate against
  the working copy directly; the comparison is mechanical, costs nothing, and belongs at the start of
  a pass rather than at the end.
- **A cross-file endpoint carries the far file's stem, `<nn>_<section>`, never its number alone.**
  The same rule §10 gives for filenames applies to every reference between files, and for the same
  reason: the number fixes data-flow position, the section names the structure, and either alone is
  ambiguous. A bare number is a pointer that goes **silently** wrong the moment a file is split,
  merged or renumbered, while the section string still names the structure set after the number has
  moved. The stem is one string lifted verbatim, never re-worded to describe the file better.
  **Two states exist and only one of them is visible.** An endpoint carrying a bare number announces
  that a far end lives elsewhere and merely fails to say where; an endpoint carrying nothing
  announces nothing and reads as complete. The second is the worse state and it is the commoner one.
  **Stems are written on touch, never by an independent sweep**, and only where the far file has been
  read against the file at hand — writing a stem to a file nobody opened is the same defect as
  writing an edge whose far end was never read. An endpoint with no stem therefore means *not yet
  worked beside its far end*, and is not a claim that no far end exists.
  **Writing the stem is the connection check, not a label applied after one.** Resolving an endpoint
  to a file is the work; the stem is where the result lands, on the entry, which is the only place a
  finding survives a session.
- **Counts** are **per hemisphere** unless stated. This is settled, and the reason is not tidiness:
  **a whole-brain count would only be meaningful if the brain were symmetrical, and it is not.**
  Broca's area and its right-hemisphere counterpart are not one region doing one job on two sides,
  and a single number covering both asserts a symmetry that does not exist while hiding the
  asymmetry that is the interesting fact. Structures the literature reports whole (cerebellum, basal
  ganglia, spinal cord, midline nuclei) are tagged as whole with the per-side value alongside.
  *(Settled at the source rung by Micky; inherited, not re-decided.)*
- **Per eye is a third basis, and it is not covered by per-hemisphere or by whole.** The retina is
  counted per eye, the optic nerve carries ~1.0–1.2M axons per eye, the chiasm's through-traffic is
  ~2M fibres **both eyes combined**, and everything from the lateral geniculate nucleus onward is per
  hemisphere. **Three bases inside one section, and the chiasm is where they change** — it takes two
  per-eye buses in and emits two per-hemisphere ones. So **each structure declares its own basis on
  its Sizing field**, and a section total across mixed bases is labelled as mixed rather than
  presented as one number. The same will apply anywhere a paired peripheral organ enters: the cochlea,
  the olfactory epithelium, the vestibular end organs. *(The three bases are Class 1 from file 01; the
  ruling that each structure declares its own is Claude's, offered to be checked.)*
- **Whether the left/right divergence from the auditory core onward earns a convention of its own is
  open.** The two hemispheres stop being identical copies there and genuinely diverge in function at
  the endpoints, while counts stay per hemisphere. The per-hemisphere ruling above requires that the
  asymmetry not be hidden; it does not say how an asymmetric pair is written.
- **Memory** in generic bytes / GB / TB (parameter memory, state memory); **not VRAM**.
- **Latency** per edge, real time units, heterogeneous. **Most read *to derive*, and that is still
  true of the source as it stands** — timing figures appear on only a handful of edges across the
  twenty files, concentrated in the thalamic, auditory and dorsal-stream files, and the source's own
  loop synthesis states that pinning loop latencies is a separate literature effort and that loop
  latency is not one of its number slots. None is invented. What the field records where it is open
  is *the shape of the ignorance* — which edges must be timed before code can be written — and that
  is its purpose at this rung.
- **Open values** read **to derive**.
- **"To derive" is not the source's *unknown*, and must not absorb the source's other slot states.**
  The source distinguishes four: *its content*; **not applicable**, where the description records
  no such property — a positive statement, as informative as a filled slot; **unknown**, where the
  property exists and has not been measured; and **owed**, where something is described but not yet
  typed, meaning *more research is needed and it is known what research*. Payloads carry a fifth,
  **resisted** — decoded, and yielding no shared format. **Writing "to derive" over a *not
  applicable* asserts that something is there to derive, which is an added claim**, and writing it
  over *resisted* discards a result. *(The four states are Class 1 from the source's design file;
  that this document's single term can silently absorb them is Claude's reading.)*
- **And a sixth state is in use that no list names: *contested*.** File 02's azimuth payload is
  **decoded, with three competing readings live** — a place code in a map of interaural delay, a
  hemispheric opponent rate code read out by slope, and a third result disagreeing with both. The
  source says explicitly that this **is not the same state as owed**. It is not *resisted* either:
  resisted means measured and yielding no shared format, while this is measured and yielding
  **several**. The same state recurs at the tonotopic map's axis, at the human core's field count, and
  at prosodic lateralisation. **An architecture writing "to derive" over any of these asserts that
  nobody has looked, when the problem is that several people have looked and disagree** — and the two
  call for different work: one needs an experiment, the other needs adjudication between existing
  results. *(That the source is using a state its own list does not name is Claude's reading, drawn
  from file 02's own wording.)*
- Invariants stated once up front; conformance noted per structure.

**Memory is not a binding constraint.** Memory is a *derived requirement*, never a limit to design
against. **Never shrink, cap, or simplify a structure, count, or size because a memory figure looks
large or would not fit some device.** No device is named on purpose — the architecture sizes the
hardware, not the reverse. A large memory number is a finding to record, not a problem to fix.
*Mechanical trigger:* any time you are about to bound or reduce a size **because of memory**, stop.
What may bind — bandwidth, update rate, interconnect — is separate and open; do not substitute a
memory ceiling for it. *(The failure this guards against: a sizing cut to fit a machine, when the real error is a modeling
choice — fp32-per-synapse gives V1 an 18.8 TB store — repaired at the model by the threshold-gate
method, never by choosing a cap to make the number acceptable.)*

## 8. No history, and no hardware

**No historical references of any kind, anywhere in the document.** No versions, no rev numbers, no
"changed since," no provenance, no "open questions next session," no references to sessions or chats
or prior files. Only functional references — the biological *why*. The date in the filename is a
creation date, not a version marker.

**The Derived from line is not a record of the past at all** — it is an assertion about the present 
that must hold. This file's parent is the current file at that stem. No-history forbids recording 
what was; this line asserts what is.

**There are no pass stamps, here or at any rung.** A stamp is pass state wearing a date, and the
rule above forbids it. A file handed to a session in isolation says what standard it is at by its
contents — the per-structure fields of §5, the far-end dependency block, and the cross-file check
list of §7 — each of which is checkable against the file rather than asserted about it.

**No hardware named anywhere** — not a board, not a chip. The purpose is the opposite: to *derive*
the hardware the source implies. No hardware is chosen until all the architecture is figured out.

## 9. Fidelity verification (against the source)

Micky hands Claude **an architecture file and the one source file it was derived from**, and Claude
verifies the pair **top to bottom** — full sequential read of both, no grep as a substitute. That is
the whole check for one file, and it is now a bounded job: the largest pair is file 2 at ~37.8k tokens
of source. The whole source is never handed over at once and no pass is scoped as though it could be.

- **Verify in BOTH directions:** content in the source but not here (omissions), **and** content here
  but not in the source (added edges, invented figures).
- **Run the dangling-edge diff.** Collect every structure named in any Inputs or Outputs field, and
  diff that set against the set of structures that have entries. An Outputs entry terminating on a
  structure with no entry — or an Inputs entry sourced from one — is a defect, and it is
  *mechanically findable*. It is the only check that finds a **missing stage**, because a missing
  stage leaves no hole where it should be; it leaves a pointer to nowhere somewhere else. **The diff
  only works if names are unique** — see §3 on abbreviations as second names.
- **Triage every diff hit against the source's own inventory before touching anything.** The source
  keeps a section listing what it knows it is missing: named regions with no entry anywhere (the
  pontine nuclei and red nucleus, parahippocampal and perirhinal cortex, the medial parieto-occipital
  reach-channel areas, the interpeduncular and septal nuclei, the rostral ventromedial medulla, the
  lateral septum), endpoints naming a **class** rather than a region, **payloads with no producer at
  all** (three of which are the same missing eye-position or efference-copy signal, wanted by three
  consumers — one region to find, not three), and **tracts named on other files' edges with no entry**.
  A hit that appears there is **inherited, and §2 forbids patching it here.** A hit that does not
  appear there was introduced in derivation and is fixed here. Skipping the triage is how an
  inherited gap becomes an invented structure. The inventory is itself marked stale in both
  directions by the source, so a hit's absence from it is not proof the gap is new.
- **Re-derive every number rather than eye-balling it.** Recompute each store from the stated count
  and fan-in, and re-sum every total. Totals drift silently. **Compute with bash, not mentally.**
- **Cross-check the source against itself** where slots constrain one another (neurons × fan-in vs
  stated synapse totals; divergence × source count vs convergence × target count). Gaps there are
  findings **about the source**, not about the architecture, and they are recorded, not smoothed.
- **A two-ended agreement is only a check when the two ends were written independently.** Two ends
  written in one pass from one sentence agree by construction and certify nothing. **Internal edges
  have both ends inside a single entry and therefore have no mechanical check at all** — their
  payloads have to be read, not diffed.
- **The check that crosses files, in place of an overlap check.** Each architecture file has exactly
  one source, so there are no overlapping ranges to diff. What stands in their place: when a source
  file is reworked, **every architecture file that names one of its structures on an edge is out of
  date**, not only the one derived from it. Nothing signals this automatically — there are no stamps
  to compare — so **the file to re-check is named by the pass that reworks the source**, at the entry
  whose edge it touched, and the §7 cross-file check list is where a reader sees which pairs have
  actually been read together.

**Twin comparison** (a Brain architecture file against the Kythera file of the same number) is a
**separate pass in its own session**, never mixed with build work. Compare **in overlapping runs of
adjacent numbers**, not one pair at a time: a pair-by-pair check sees each file only against its
counterpart and is blind to data-flow drift *between* files, where a line's producer is in one file and
its consumer in the next. With twenty files and the diff crossing file boundaries constantly — file 01
reaches ten other files — that blindness is the normal case and not the exception.

## 10. One architecture file per source file, and the downstream rungs

**The Brain architecture is a set of twenty files, not one document, and each is derived from exactly
one source file.** File NN is written from `human_brain_<nn>_<section>_<date>.md`, this design file,
and CLAUDE.md, and from nothing else.

**The name is the source's name with the prefix and the date changed, and nothing else changed.**

    human_brain_        <nn>_<section>        _<source date>.md
    Brain_architecture_ <nn>_<section>        _<creation date>.md

**The number and the section travel together, copied verbatim.** Not re-worded, not tidied, not
expanded to describe the contents better — `<nn>_<section>` is one string lifted from the source
filename. The number fixes data-flow position and the section names the structure; either one alone is
ambiguous, so neither is written without the other. The date is the creation date of the architecture
file, so it is today's date and not the source's.

**Why verbatim and not descriptive.** A section name written from the file's *contents* drifts from the
name written from its *filename*, and the two then disagree silently. File 17 is the live case: its
filename says `insula_claustrum_habenula` while its contents also cover the cingulate remainder, so a
description-derived name gives `17_insula_claustrum_habenula_cingulate` and points at a source file
that does not exist. **Copy the string; do not describe the file.** The table below therefore carries stems, not
descriptions — **and it carries nothing else.** Token counts and entry counts live once, in the
source's own design file, per §2; a second copy of them here would drift against that one with
nothing to detect the drift.

| # | `<nn>_<section>` — copied verbatim into both names |
|---|---|
| 1 | `01_visual_pathway` |
| 2 | `02_auditory_pathway` |
| 3 | `03_other_senses` |
| 4 | `04_dorsal_visual_parietal_stream` |
| 5 | `05_sensorimotor_loop` |
| 6 | `06_posterior_parietal` |
| 7 | `07_anterior_temporal_lobe` |
| 8 | `08_medial_temporal_lobe` |
| 9 | `09_basal_ganglia` |
| 10 | `10_cerebellum` |
| 11 | `11_frontal_lobe` |
| 12 | `12_thalamus` |
| 13 | `13_neuromodulatory_systems` |
| 14 | `14_brainstem_midbrain_hypothalamus` |
| 15 | `15_cranial_nerve_nuclei` |
| 16 | `16_spinal_cord` |
| 17 | `17_insula_claustrum_habenula` |
| 18 | `18_white_matter_tracts` |
| 19 | `19_cross_modal_integration` |
| 20 | `20_loop_structure` |

**A stem is the only correspondence marker the twins need.** Kythera's file at the same number carries
the same `<nn>` and, because no Kythera file may contain a biological word, **not** the same
`<section>` — that is the one place the two naming schemes must differ, and the number carries the
correspondence alone. *(Kythera's own design file governs how its section strings are formed; it is not
this file's to specify.)*

**Why one-to-one and not grouped.** Grouping source files into ten larger chunks does not survive
measurement against the source: the groups span a factor of seven, and three of them are larger than
the largest single source file. A file that must be co-loaded with its source, with this file, and
with CLAUDE.md has no room for the largest of them. One-to-one also removes the seam question
entirely: **there are no seams to get wrong, because the source's own file boundaries are the only
boundaries.**

**Correspondence across the twins is file-number correspondence.** Brain file NN and Kythera file NN
are derived from source file NN and cover the same structures, which is what makes the comparison pass
possible. It must not be broken: **if the source is ever split further, both twins gain a file at the
same number in the same position.** *(Kythera's design file carries the same rule in its own
vocabulary, and keeping the two in step is Micky's, since the twins are never worked in one session.)*

**Two source files carry no entries and therefore derive no structures.** Files 19 and 20 are synthesis
prose. What they carry is the loop inventory and the cross-modal convergence account, which bear on the
invariants in §4 and on the payload question in §5a. **Whether they get architecture files of their own,
or are read as input to all the others, is open** — the one-to-one rule as stated would give them empty
structure lists, and an empty file that exists only to keep a numbering scheme intact is worth less than
the numbering costs.

**The auditory file is the one source file large enough to be awkward on its own** and would split
cleanly at the belt if it is ever reopened; the frontal and visual files are next. Which files are
oversized, and by how much, is recorded once in the source's own design file. **A split is a source
decision, and both twins follow it.**

**Downstream file naming** (renamed so the code rung cannot be mistaken for this one):

- `Brain_code_design_NN_name_<date>.md` → `Brain_NN_name.py`, one per architecture file

The **code design document** is the rung below this one — it restates the contract and adds the
algorithm. **Its spec is not in this file and does not belong here.** It has one of its own:
`Brain_code_design_spec_<date>.md`, which governs that rung and the code below it, and which Micky
hands over in code-design sessions. Kythera's equivalent is a separate file, because no Kythera file
may contain a biological word.
