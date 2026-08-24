# Brain code design documents — design file

**Date:** 2026-08-20
**Owner:** Micky.
**Purpose:** the specification for `Brain_code_design_<nn>_<section>_<date>.md` — the rung between the
Brain architecture and the Brain code. **Hand this to Claude in Brain code-design sessions only.**
Kythera sessions do not get this file and do not need it.

**This file stands alone on purpose.** The twins are never worked in the same session, so a design
file that only makes sense beside its counterpart is useless. Where this duplicates the Kythera
code-design file, the duplication is deliberate.

**The line:** *the design of the document is not content of the document.* A code design document
contains algorithms. It does not contain the rules for writing algorithms, the state of any pass over
it, or the history of how it got that way.

**Co-load budget, because it is a correctness matter and not tidiness.** A code-design session holds
CLAUDE.md, this file, the architecture file being worked, and — where the algorithm needs what the
architecture did not carry — its one source file. Every one of those is paid on every session, while
any single architecture file is paid once. This file is kept small for that reason.

---

## 1. What the rung is

The architecture says **what each structure is, what it takes in, what it puts out, what shape it has,
how big it is, and how long its edges take.** The code design document says **what algorithm realizes
it.**

**One design entry per architecture entry, same names, same order.**

**But the architecture's structure count is not the source's entry count, and this rung inherits the
consequence.** Several source entries bundle multiple structures into one slot set — the basal ganglia
entry covers striatum, pallidum, subthalamic nucleus and substantia nigra; the corpus callosum entry
carries four tracts; the arcuate entry carries five. Where the architecture entry is still a bundle,
**the design entry is a bundle too, and the split is owed at the source.** It is not silently split
here: splitting invents the arity, and it invents it two rungs below where the arity is known.

## 2. Standalone, not companion

Each design document **restates the contract and then adds the algorithm**, so that at coding time
only the design file needs to be loaded, not the architecture file beside it.

This is the same reasoning that makes the architecture standalone against the source: the rung above
is too large to co-load, and keeping two documents aligned by hand — forever — is a failure mode with
no verification procedure behind it. The duplication is guarded by a fidelity pass, like every other
rung.

## 3. Contract fields are copied verbatim

**Copied from the architecture entry character for character** — not re-derived, not paraphrased, not
summarized:

- **Function → structure**
- **Inputs**
- **Outputs**
- **Sizing**
- **Shape**
- **Edge latency**
- **Invariant conformance**
- **Justification (biological)**

**The set is the whole architecture entry**, and that is the simpler rule as well as the safer one:
there is no field a design entry may re-derive rather than copy, so there is no boundary to remember
and none to get wrong.

Verbatim copy has **no translation failure mode**; only paraphrase loses content. The fidelity pass on
a design document therefore **diffs** those fields against the architecture, and any difference is a
defect found **mechanically**. The design document's own writing is confined to the algorithm
sections, where there is nothing yet to be faithful to.

**Shape and Edge latency are contract, not commentary.** Shape is the rank, the axes and the extent of
each axis, or *to derive* per axis — it is the thing the code allocates against, and a structure that
cannot be allocated has not been specified. Edge latency is per edge, in real time units, and it is
what the scheduling discipline is eventually decided over. A design entry that carries Inputs, Outputs
and Sizing but not these two has copied the description of a structure and dropped the two fields the
code is written from.

**Function → structure, Invariant conformance and Justification (biological) are copied for three
different reasons, and each is load-bearing.**

- **Function → structure** is what §5's Transform must realize. Without it in the design entry the
  transform has no stated purpose beside it, and §2's standalone requirement fails at exactly the
  moment it matters — a coder with only the design file could not tell whether the operation written
  is the operation the structure is for. It is also where the divisional sub-elements are established
  or ruled out, which §5's Arrays field allocates against.
- **Invariant conformance** is a claim about the structure that **the code can break silently** —
  co-instantiation in particular, since a stage that comes online later is a natural thing for code to
  do and a thing the architecture forbids. A silent break needs the claim in front of the person
  writing the code, not one rung up.
- **Justification (biological)** is what §6 requires the design document and the code to stay in.
  Copying the architecture's own justification puts the biological reason in the file where the
  comments are written from; stating the rule without supplying the reason leaves the coder to
  reconstruct one, and a reconstructed justification is recall wearing the register of derivation.

*(The matching change in Kythera's code-design spec is owed and is Micky's to make, since the twins
are never worked in one session.)*

**A verbatim copy is only a check when the two documents were written in separate passes.** Two
records written in one sitting from one reading agree by construction and certify nothing. This is the
same caution the architecture rung carries about two-ended edges and the source rung carries about its
payload diff, and it applies here with the same force: **if an architecture file and its design file
are produced in the same session, §3's diff is not a check on that pair and must not be reported as
one.**

## 4. Representation — the field the architecture does not have

Declared **once per line**, and **inherited by every consumer of that line**:

- **units**
- **numeric range and normalization**
- **update timing** — the rate at which the *producer* emits a new value, in real time units, where
  the producer has a rate of its own (a sensor's sampling rate is the clear case). Where it does not,
  the entry says so: a structure driven by its inputs emits when its inputs change, and
  **"event-driven" is the honest answer**, not a rate borrowed from somewhere else. There is no system
  clock to borrow one from.
- **coordinate frame**

**Latency is not declared here.** It is an architecture field, copied verbatim under §3. A design
entry that re-states a latency has created a second record of a quantity that already has one, and the
two will disagree.

**Why this field exists, and why the architecture cannot catch what it catches.** Architecture-level
failure is *omission* — a structure or edge that didn't survive — and a diff against the source finds
it. Design-level failure is different: **every structure satisfies its own contract and the
composition still does not run**, because two neighbouring structures each read the shared line
correctly and **disagree about what its numbers mean**. Representation pins units, range, rate and
frame once, **at the line rather than at the structure**. It is the guard against data-flow drift: a
consumer that assumes a different representation than the producer declares becomes a mechanical
check, not a diagram reconstructed after the fact.

**Open and unasked: whether this field survives in its present form at all.** The source already
declares, on every edge, what that edge carries — the property, its units, its coordinate frame, and
where it matters what it explicitly does **not** carry — written twice, at the producer and at the
consumer, which is what makes it mechanically checkable there. The architecture template has no field
for it, and the architecture design file records that gap as open and Micky's to set. So units, range
and frame are declared at the source, dropped at the architecture, and reinvented here under a
different name and with no two-ended check. **If the architecture gains a payload field, most of
Representation becomes a verbatim copy under §3 rather than design-rung writing, and only update
timing remains this rung's own.** *(That the three rungs are describing one quantity is Claude's
reading. The source's payload slot and the architecture's missing field are Class 1 from those two
design files.)*

## 5. What a design entry must contain

The architecture entry says what a structure *is*. The design entry says what it *does*, in terms that
can be transcribed into code **without inventing anything**. Every entry carries all of these:

- **Transform.** The named operation, in standard engineering or computer-science terms — "two-
  dimensional oriented bandpass convolution, then half-wave rectification," not a description of what
  such a thing would be like. If no standard name fits, **that is a finding about the structure and it
  is recorded as one.** A picture of an operation is not an operation.
- **Arrays.** Every input array and every output array: name, shape (from the copied Shape field, or
  expressions over the architecture's own counts), data type, numeric range, and units.
- **Parameters.** Each one named in full, with its unit, its value or range, and its **origin** —
  derived from the architecture's counts, computed from the source, or **chosen**. A chosen parameter
  says **who chose it and on what grounds.**
- **Update equation.** The arithmetic that produces the outputs from the inputs, the state, and the
  parameters. Written so that transcribing it into code requires **no decision**.
- **State carried between updates.** Name, shape, data type, initial value, and the point in the
  update at which it is written. **State memory is not parameter memory and the two are never summed
  into one figure.**
- **Edge storage.** The values in flight, which the per-edge-latency invariant creates:
  `edge_storage = line_count × ceil(latency ÷ update_interval) × bytes_per_value`. The architecture
  rung states this figure is **not sizable there**, because it scales with the reciprocal of the update
  interval and therefore waits on the scheduling discipline. **It lands here.** Until the discipline is
  set the entry records the line count, the copied latency, and the bytes per value, and states that
  the interval is unset — which is the whole figure except one term. It is never summed with parameter
  memory or with state.
- **Adaptation.** The rule that changes any stored parameter, or an explicit statement that none
  changes and why. **Learning rules are Micky's call.** An entry may record that the rule is not yet
  set; it may **not** quietly assume one.
- **Open.** What is not fixed, named. An open item is a **question for Micky**, not a placeholder for
  Claude to fill in later.

**The completion test, and it is mechanical:** an entry is finished when **the code can be written from
it without making a single further choice.** If writing the code would require a decision, the decision
belongs in the entry, and the entry is not finished.

### 5a. Four classes the Transform field was not written for

Each of these has a structure that computes nothing, or computes in a way "a named operation over
arrays" does not describe. All four are settled at the rungs above, and **the entry must not be forced
into the ordinary shape.**

- **Transmission-only structures.** Seven source entries carry other entries' edges and compute
  nothing — the optic chiasm, the spinal cord white matter, and the five tracts of the white-matter
  file. Their Sizing reads **zero parameter memory**, their fan-in and fan-out read **none** because no
  synapse occurs there, and their Shape is a **routing index from source line to destination, rank 1** —
  **not an activity array**. The design entry's Transform is a routing statement; there is no update
  equation and there is no state. Writing a zero-length array asserts state the structure does not
  hold. These entries are load-bearing anyway: **a tract is where the physical substrate of a latency
  lives**, and a derived conduction time is derived from it.
- **Transducers.** A transducer is not a threshold gate, stores no threshold, and its Sizing does not
  come from the log₂ cost. Its transform converts a physical stimulus, and its input edge is not a
  projection — the retina's input is photon flux imaged on a sheet, and fan-in reads *not applicable*.
- **Graded, non-spiking elements.** A class that **computes, is not a transducer, and does not cross a
  threshold**: the retina's horizontal and bipolar cells respond with graded membrane potential and
  generate no action potentials, and the lateral geniculate's local interneuron releases transmitter
  from dendrites without an action potential. **What such an element stores is not settled by the
  threshold-gate model and must not be defaulted to zero or to log₂(fan-in)** — zero asserts it holds
  nothing, log₂(fan-in) asserts a threshold it does not have. It reads *to derive*, and how these are
  modelled at all is Micky's.
- **Sign-inverting stages.** In the outer retina **hyperpolarisation is the excitatory response** —
  photoreceptors hyperpolarise to light and release more transmitter in the dark, and because these
  cells do not spike, hyperpolarising is not inhibiting. An update equation that reads depolarisation
  as activation has the stage exactly backwards. This is a constraint on the arithmetic, not on the
  structure.

### 5b. "To derive" must not absorb the states above it

**"To derive" is an honest answer only for a quantity the *source* has not yet supplied.** It is not an
answer for a quantity we simply have not chosen.

And it is not a single state. The rungs above distinguish, and the distinctions are actionable:
**not applicable** (the property does not exist — a positive statement, as informative as a filled
slot); **unknown** (it exists and has not been measured — an experiment to run); **owed** (described
but not yet typed — more research is needed and it is known what research); **resisted** (decoded, and
yielding no shared format — a result, not a gap); and **contested** (measured, and yielding several
readings that disagree — this needs adjudication between existing results, not a new measurement).

**Writing "to derive" over any of them makes a claim the rung above did not make.** Over *not
applicable* it asserts something is there to derive; over *resisted* it discards a finding; over
*contested* it asserts nobody has looked when the problem is that several people have and disagree.
**Copy the state, do not translate it.**

## 6. Justification stays biological

**The architecture's own justification arrives in each entry as a §3 copy**, so this section governs
what is written *beside* it — the design rung's reasoning about the algorithm, and every comment in
the code. The copy supplies the biological reason; it does not license a second, re-derived one.

Justifications in the Brain code design documents and in the Brain code are **biological**. Engineering
terms are allowed where a size, budget, or standard operation must be named; the *reason* stays
biological. Sizes in generic memory (bytes / GB / TB), **not VRAM**.

**Memory is a derived requirement, never a limit to design against.** Never shrink, cap, or simplify a
structure, count, array or size because a memory figure looks large. A large number is a finding to
record. *Mechanical trigger:* any time you are about to bound or reduce something **because of
memory**, stop.

**No hardware named** — no board, no chip, no part number. The design documents may name a device
*class* where the architecture derives a requirement for one (a camera, a microphone, an actuator), but
never a part. Hardware is chosen after the architecture is derived, not during.

**Watch every sentence containing *cycle*, *frame*, *step*, *tick*, or *register*, and ask whether it
has just invented a clock the system does not have.** A uniform one-step delay is a legitimate thing
this rung may eventually choose — it is an implementation choice and it is Micky's — but until it is
chosen it may not appear in an update equation as though it were given.

## 7. No history — and it must be stated in the files themselves

The architecture's rule binds the design documents and the code identically: **no versions, no
provenance, no "changed since," no reference to sessions or prior files, no changelog, no "formerly,"
no commented-out prior version.**

And it must be **stated in them** — in each design document's front matter, and in **each code file's
header** — not only in a design file. Stating it only elsewhere fails in a specific way: while working
on code, comments get written that violate the rule, because the rule is not in front of the person
writing the comment. **A file that carries its own past gives a reader two truths and no way to tell
which is live.**

When editing code, **update the comment in the same edit.** Comments explain only the functional basis
(biological), Euler order, and compute/memory tradeoffs.

**There are no pass stamps, here or at any rung.** A stamp is pass state wearing a date, and the rule
above forbids it. A file handed to a session in isolation says what standard it is at by its contents
— the copied contract fields of §3, the entry contents required by §5, and the far-end dependencies
recorded under §9 — each of which is checkable against the file rather than asserted about it.

## 8. One design file per architecture file, and the names that must correspond

**The Brain code design is a set of twenty files, not one document.** File `nn` is written from
`Brain_architecture_<nn>_<section>_<date>.md`, this file, and CLAUDE.md, and from nothing else. There
are **no chunks and no seams at this rung**, because the source's own file boundaries are the only
boundaries anywhere on the ladder.

**The name is the architecture's name with the prefix and the date changed, and nothing else changed:**

    human_brain_         <nn>_<section>   _<date>.md
    Brain_architecture_  <nn>_<section>   _<date>.md
    Brain_code_design_   <nn>_<section>   _<date>.md
    Brain_               <nn>_<section>   .py

**What the date means is CLAUDE.md's and is not restated here**, so that this rung cannot drift from
it.

**`<nn>_<section>` is one string, lifted verbatim.** Not re-worded, not tidied, not expanded to
describe the contents better. A section name written from a file's *contents* drifts from the name
written from its *filename*, and the two then disagree silently. **Copy the string; do not describe the
file.**

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, never its number alone.** The
same rule this section gives for filenames governs every reference between files, for the same reason:
the number fixes data-flow position, the section names the structure, and either alone is ambiguous. A
bare number goes **silently** wrong the moment a file is split, merged or renumbered, while the section
string still names the structure set after the number has moved. At this rung the stem arrives with the
verbatim copy of §3 — an Inputs or Outputs field copied character for character brings its stems with
it, and **a design file carrying fewer stems than the architecture file above it has dropped edges,
which is a count rather than a reading.** That is a mechanical check this rung otherwise lacks.
**Stems are written on touch, never by an independent sweep**, and only where the far file has been read
beside the file at hand. An endpoint with no stem means *not yet worked beside its far end*; it is not a
claim that no far end exists.

**The code file carries the number and no date**, because the number is load-bearing — it must
correspond across the twins — and a date is not. **Two code files carry neither**, and they are §8a.

**No file map is copied into this file.** The map of stems lives at the source rung and is re-derived
there when files are added, split or renamed; a second copy here would be a second record with no
mechanism keeping it true, and a wrong map fails silently. Read the stem off the architecture file in
hand.

**Correspondence across the twins is file-number correspondence.** Brain file `nn` and Kythera file
`nn` derive from source file `nn` and cover the same structures, which is what makes the comparison
pass possible. The section strings differ, because no Kythera file may contain a biological word, and
the number carries the correspondence alone. **If the source is ever split further, both twins gain a
file at the same number in the same position.** *(The matching change in Kythera's code-design spec is
owed and is Micky's to make, since the twins are never worked in one session.)*

**Design entries are large, and a design file may not fit one session.** A finished design entry runs
several times the length of the architecture entry above it, because shapes, types, parameters,
equations, state and edge storage all have to be written out. **The response is not to split the file.**
There is no seam here to split on, and inventing one breaks the number correspondence. If a design file
will not fit, that is a finding about the size of the source file it descends from — a split there is a
source decision, and both twins follow it.

**Deliver early rather than whole.** A design file that is coherent for three of its structures and
presented is worth more than a complete one that a session ending mid-pass took with it. Write, present,
keep improving in place, re-present.

### 8a. The code base is not only the numbered modules

**Two code files carry no number and no date:**

    Brain_config.py    the declarations every numbered module imports
    Brain_live.py      the driver

**Why they carry no number.** A number is load-bearing on a numbered module for two reasons: it fixes
data-flow position within the set, and it must correspond across the twins. **Neither reason applies
here.** There is one of each, they sit outside the data-flow order rather than at a position in it, and
the twin correspondence is carried by the name alone — `Kythera_config.py`, `Kythera_live.py`.
Numbering them would put a number where nothing depends on it and would collide with the numbered set.
*(The matching change in Kythera's code-design spec is owed and is Micky's to make, since the twins are
never worked in one session.)*

**Config holds what more than one module must agree about, declared once.** The element classes of
§5a, and the types that describe a structure, a population and an edge. **The reason is mechanical and
it is the same reason §3 copies verbatim rather than paraphrasing.** An edge that leaves file `nn` is
declared at both ends, in two files; two files cannot describe one edge in agreement when the type
describing it is defined twice, because the two definitions drift and nothing detects the drift. A
private edge type per module makes every cross-file edge a translation, and translation is the failure
mode this rung is built to avoid.

**A cross-file endpoint in code carries the far file's stem, exactly as §8 requires of the documents.**
Not the file number: a bare number goes silently wrong the moment a file is split or renumbered, and
the code has no reader to notice.

**What config does not hold:** the counts, shapes and extents of any structure. Those belong to the
numbered module for the section they describe, because that is where they are derived and where a
fidelity pass diffs them against the architecture entry above. Config holds the vocabulary; the modules
hold the content.

**Live is the driver, and it is not a training script.** The system has no separate training and
inference modes — it learns continuously while it functions — so there is no run to enter and exit, no
phase to switch between, and no epoch. **A driver written as train-then-infer would build a system the
architecture does not describe**, and it would do it in the file least likely to be diffed against
anything.

**Live cannot be written until the scheduling discipline is set, and the discipline is §10's largest
open item.** What a driver *is* — a loop, an event queue, a set of sensor-timed callbacks — is not a
free choice made in the driver; it is the scheduling discipline wearing a filename. Until Micky sets
it, `Brain_live.py` may exist and may state what it is waiting on, and it may not choose. **Watch every
sentence in it containing *cycle*, *frame*, *step*, *tick* or *register*** — §6's trigger applies here
with more force than anywhere else on the rung, because this is the one file whose whole subject is
when things happen.

**§7 binds both files.** Each carries the no-history rule in its own header, like every other code
file, and neither carries a changelog, a "formerly," or a commented-out prior version.

## 9. Fidelity verification

Micky hands Claude **a design file and the one architecture file it was derived from**, and Claude
verifies the pair **top to bottom** — full sequential read of both, no keyword search as a substitute.

- **Diff the copied contract fields** (§3) character for character. Any difference is a defect.
- **Verify in both directions.** An algorithm, array, parameter or equation with nothing above it to
  license it is drift exactly as an omission is, and it is **harder to catch**, because a well-formed
  invented equation reads exactly like a derived one.
- **Re-derive every number rather than eye-balling it**, and **compute with bash, not mentally.**
- **Attribute before repairing.** Wrong here but right in the architecture → introduced in derivation,
  fix here. Wrong in the architecture too → the repair starts there, and if it is wrong there because
  the source is, it starts at the source, which is **the rung where claims are checked against the
  literature**. **A gap found there is a research request**, not a stop: search it, bring back a
  candidate carrying its **method and species**, and let the candidate wait at the gate. **Never patch
  this rung for a gap inherited from above, and never leave one silent.** Patching creates an added
  edge, and the next fidelity pass will correctly flag it and delete it. **Recording does not**: the
  gap is written into the file at hand, at the entry it belongs to, naming what is missing and which
  rung it must be repaired at. **A gap that is neither patched nor recorded reads, on the next pass,
  exactly like a subject with nothing to say about it** — and the pass that could have seen it is the
  one that just ended.
- **A repair that lands at a rung above stops the pass and is reported before design work resumes.**
  Reading the architecture or the source to attribute a finding is ordinary and needs no announcement.
  **Writing to either does not.** Under the source's verified-only rule anything
  new entering a source file carries **what it was verified against** — a source opened or a search
  run — or it is marked a **candidate** and says so, and Micky is told either way. **The rule governs
  what enters, not whether the work gets done**; stopping without searching is the work not being
  done, wearing the rule as a reason. **Verification runs up the ladder to the literature, never to a
  person — for data.** The reason for
  stopping is that a candidate and a verified line read identically
  once the session that wrote them is gone, and every design edit made afterwards will have been built
  on whichever it was. **Stopping is what keeps the two distinguishable.**
- **Data and instruction verify in opposite directions.** **Data** — claims about how the brain is —
  verifies up the ladder and, at the source rung, against the literature, **never against a person**.
  **Instruction** — how this project works, including this spec and every design file — verifies
  **against Micky and nothing else**, there being no rung above a design file and no literature about
  this project. **If a paper could settle a dispute about the line it is data; if only Micky could, it
  is instruction.** The scheduling discipline, the learning rules and the other items in §10 are
  **instruction**, which is why no amount of research settles them, and why Claude may not research
  its way to one.
- **Reaching a structure the session does not hold.** Most edges leave their own file. Two permitted
  responses, and the session says out loud which it took: **ask Micky for that file**, or **record the
  far-end dependency in the file at hand**, naming the file and structure. Writing an algorithm whose
  far end was never read is not a third option.

**Twin comparison** — this twin against Kythera — is a **separate session**, never mixed with build
work. Compare **in overlapping runs of adjacent numbers**, not pair by pair: a pair-by-pair check sees
each file only against its counterpart and is **blind to data-flow drift *between* files**, where a
line's producer is in one file and its consumer in the next. With twenty files and edges crossing
boundaries constantly, that blindness is the normal case and not the exception.

## 10. What belongs to Micky and may not be assumed here

- **The scheduling discipline** — a global step, event-driven, or sensor-timed. This is the design
  rung's decision to make and it is **Micky's**, not Claude's. It is the largest open item at this rung.
  Everything in the Representation field's update timing, every copied Edge latency, and the whole edge
  storage figure feed it — **and so does the entire shape of `Brain_live.py`**, which is why that file
  waits rather than choosing (§8a).
- **The learning rules.**
- **Graded vs binary emission**, and the unit's expressiveness — the centre–surround / threshold-gate
  question.
- Anything that would trigger a fresh start: tile geometry, sparsity, inter-structure connection
  topology, any `register_buffer()` shape. **Surface and get explicit agreement first.**

An item on this list is not a slot to be filled in later. **It is asked out loud, in the conversation,
in the turn it arises**, and the answer is written into the section it governs. A question parked in a
file is a question nobody asks.
