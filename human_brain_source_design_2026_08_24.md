# Human brain source — design file

**Date:** 2026-08-24
**Owner:** Micky.
**Purpose:** the specification for the source — what it is for, what may enter it, and the shape of
an entry. **The source is not one file.** It is **twenty files**, one per
pathway section, named `human_brain_<nn>_<section>_<date>.md`; section 8 below is the map and the
working protocol. **Hand this file to Claude in source sessions only.** Brain-architecture, Kythera, design-document, and code sessions do not need it.

**Why it exists.** The source file and CLAUDE.md were both carrying the source's design, in
different words, and neither of them is the right place for it. CLAUDE.md is an instruction file
for Claude and governs five other rungs besides this one; the source file is a description of the
human brain, and a rule about how to write about the brain is not a fact about the brain. Two
partial copies of a spec, in two files, is an un-normalized table: they duplicate, and where they
duplicate they can conflict. This file is the single copy.

**The line, and it is the whole point of the split:** *the design of the file is not content of
the file.* The source contains the brain. It does not contain the rules for writing about the
brain, the state of any pass over it, or the history of how it got that way.

**An open question is asked out loud, never parked in a file.** The rule is in CLAUDE.md and is
not restated here — two partial copies of a rule is the un-normalized table this file exists to
avoid. What belongs here is only what it cost this file: it used to end with a list of open design
questions, five of them, and the list was the problem, because a question written down is a question
that *feels* handled. The list is gone and no section replaces it.

---

## 1. What the source is

A faithful description of the human brain as it is — anatomy, function, and data flow between
regions — with physical numbers recorded where they have been verified against primary literature.

It is **not** a model and **not** a build. It contains no device, no RAM, no model units, and no
modeling choices — no learning rules, no "ported from X," no predict/error framing. Those belong
to the Brain architecture document, which is derived from it.

Here: what the brain *is*, not how it will be built.

**The source does not simplify for a downstream rung's convenience.** A scheme that would be tidier
to implement, or uniform across regions where the brain is not uniform, is a decision for the
architecture or the software design — and the software design is where approximation is legitimate
and expected. If a region has four sublayers where its neighbour has one, the source says four and
one. Flattening it here would put the approximation in the one file whose whole purpose is to be
the thing everything else is checked against, and nothing downstream could then recover what was
lost.

**Scope:** the whole human brain, described as it is — no pruning. Regions are added as their data
flow is described and their claims verified. The **non-neuronal layer** (glia, vasculature /
blood–brain barrier, ventricles / CSF) is **out of scope** by decision, not deferred. The
**peripheral and enteric nervous systems** lie outside its CNS scope.

**Peripheral sensory transducers are in scope.** *(Settled by Micky.)* The end organs
that turn a physical stimulus into a neural signal — retina, cochlea, olfactory epithelium,
semicircular canals, otolith organs, taste buds, the skin and muscle receptors — get entries, even
where the tissue is peripheral rather than central. **They are where the data flow starts**, and a
description of data flow that begins one synapse inside the brain has an undeclared origin on every
sensory line: the first central entry's input edge points at nothing, and the payload arriving on it
cannot be checked against what the transducer actually produces.

The ruling is what makes the vestibular entries correct rather than anomalous, and it is what puts
the **cochlea** in file 02 and the **olfactory epithelium** in file 03. **Every sensory line in the
source begins at its transducer.**

The boundary this does *not* move: peripheral **nerves** and **ganglia** that only carry a signal
without transducing it stay out of scope, as does everything beyond the transducer on the body side —
muscle, skeleton and their dynamics remain outside, and the motor edges that point at them keep
saying so.

## 2. The verified-only rule

A region enters the file only when its anatomy and data flow are **verified against primary
literature**. Physical numbers are recorded per the slot list below; a number that is the best the
literature currently offers is recorded even though it carries a measurement range — that is the
nature of the number, not a defect. A slot with no measured figure reads **unknown**, or **not
applicable** where the region has no such property — see the four slot states at the end of §3, and
note that a **payload** is the one slot that may not read a bare *unknown* (§4).

**Two kinds of verification, running in opposite directions.** **Data** — anything asserting how the
brain is: numbers, edges, payloads, references, species, methods — is verified **up the ladder** and,
at the source rung, **against the literature**. **Never against a person**, because there is a fact of
the matter outside this project and agreement is not evidence of it. **Instruction** — anything
asserting how this project works: slots, file contents, naming, the provenance classes, the sweep
order, and **every design file including this one** — is verified **by Micky and by nothing else**.
There is no rung above a design file and no literature about this project; **its ground truth is his
intent.**

**The test is what would settle a dispute about the line.** If a paper could settle it, it is data. If
only Micky could, it is instruction. **Claude may not research its way to an instruction**, and **may
not ask Micky to stand in for the literature.**

*(This distinction is why the sentence it replaced went wrong. "Verification is Micky's" was **true of
instruction and false of data**, and said which of the two it meant nowhere — so the true half
licensed the false half, and every rung below inherited the pair as one rule. A rule that is right
about one class and wrong about another, stated without naming the class, is the shape that survives
re-reading: each restatement is faithful to the one above it.)*

**Verification runs up the ladder, not to a person — for data.** A claim is verified by checking it
against the rung above it. **At the source rung there is no rung above, so the check runs to the
literature** — and where the literature has no answer, to research that goes and finds one.
**Verification is therefore an act, not a permission**, and Claude performs it rather than requesting
it.

**What this rules out.** A data line does not become true because Micky read it, and it does not stay
unverified because he has not. **Claude does not hand Micky a list of lines to check in place of
doing the checking** — a research result arrives verified against its sources, with its **method and
species** on it, or it arrives marked as what it is. Where a claim rests on recall, on a reading, or
on a citation nobody opened, **that is the unverified thing, and the repair is to open the source or
run the search, not to pass the doubt along.**

**What is Micky's, beyond instruction.** Scope and sequence — which files, which sweep, how much of a
session to spend. And the standing decision to be told what changed: **anything new entering a source
file is reported to him before work continues**, because a line that entered quietly cannot be
distinguished later from one that was always there. **That is a notification rule, not a gate.**

A data question that lands at the source rung is a question for the research, and Claude answers it by
searching. **It becomes a question for Micky only when the session has too little budget left to
search — and in that case Claude asks before searching, never instead of searching.** This is also
why a gap inherited from the source is never patched at a lower rung.

**A citation is not evidence that anything was checked.** A correct-looking, correctly-formatted,
entirely plausible citation can be produced from recall alone. If no source was opened and no
search was run, that fact is part of what Micky is being asked to verify.

**Provenance classes.** A payload
line, or the parenthetical on its edge, carries a **provenance class** and a **verification tag**.
The class is one of:

- **Class 1** — direct literature, with method, species and citation.
- **Class 2** — Claude's synthesis or reading.
- **Class 3** — general / textbook anatomy.

A single line may split classes across its parts — Class 1 for a decoded fact, Class 2 for the
reading placed on it. **Each carries what it was verified against, not who read it** —
**verified against ⟨source or search⟩ ⟨date⟩** — because the tag has to survive being read years
later by someone who cannot ask the reader what they checked. A line whose check has not been run
is a **candidate** and says so.

### 2a. The reference section

*(That the source needs one is Micky's decision; what follows is the shape it takes and the reason
each constraint is on it.)*

**Each file carries, as its last section, the literature its own entries cite.** One line per
distinct source: the **key**, which is the short form exactly as written inline, then the **full
reference** — authors, title, journal or book, volume, pages, year — with **species** and
**method** where the citation carries them, because §2's Class 1 requires both and neither is
recoverable from the key.

**A note on the word, because two different things were briefly called the same thing.**
These lines are **references**. ***Expansion* has one meaning in this project: what an
abbreviation stands for** — §6a's sense, *cornu Ammonis* field 1 for **CA1** — and it is not used
for anything else. A reference is not an expansion of its key, an addition to an existing entry is
not an expansion, and a new entry produced by new research is not one either. A reference is a
reference.

**It is not history, which is why §7 admits it.** A reference is a property of the claim, not of a
pass over the file. It records nothing about when a source was read, by whom, or in which session.
It changes when the literature changes and at no other time.

**It does not restate what each source supports.** The binding of a claim to its source stays
inline, on the line making the claim, where it already is. The reference section carries no
statement of what any source is evidence for. A second record of that binding is the un-normalized
table this file exists to avoid, and it would drift silently, because nothing would check either
copy against the other.

**What it buys is a check in both directions, inside one file.** Every short form used inline has
an entry in the list; every entry in the list is used by some line in the file. A key with no
reference is a citation that entered without one. A reference with no key outlived the claim it
supported — the more interesting failure, because the line was reworded or removed and the file
still asserts the literature behind it. Neither direction needs another file, and neither needs
the writer to be trusted.

**Per file, and a source used in six files appears in all six.** A source file must be workable
alone: the rungs below cannot co-load twenty files, and a shared reference file would put a
cross-file lookup in the path of every downstream question, including questions asked while chasing
a defect in code. The duplication is not a cost where it falls heaviest. **Edge citations are the
shared ones**, and §4 writes every edge twice — so one source appearing at both ends of an edge is
a second, independently written record of the same quantity, and a disagreement between the two
files is a finding of exactly the kind the two-ended diff exists to produce.

**A reference is written only where it was searched in the pass that wrote it, and the search is
declared.** What makes a reference trustworthy is not who typed it but whether it has a far end.
A searched one has several — the journal, the volume, the pages, all checkable against the record
that produced them. A recalled one has none: a correctly-formatted, entirely plausible citation
costs nothing to generate, §2 says so already, and a reference list is the highest-yield surface
in the project for that failure, being a page of well-formed citations with nothing on the page to
check them against. **A reference that cannot be attributed to a search run in that pass is not
written**, and a key left unsearched reads **owed** in §3's sense: more is needed and it is known
what.

**Recall is not a source, and neither are most of the places recall comes from.** What a model
holds about a paper is drawn substantially from encyclopaedia entries, aggregator pages and
discussion rather than from the paper or its publisher — none of them dependable for authors,
volume, pages or year, and all of them fluent enough to read as authoritative. The reference is
taken from **the publisher's record, the journal's own listing, or the paper itself**. Where only
a secondary listing was available, the line says so.

**A reference enters verified against the record it was taken from, or it enters as a candidate.**
**Searching is the verification, not a step before it** — a reference read off the publisher's
record, the journal's listing or the paper itself is checked, and takes **verified against ⟨record⟩
⟨date⟩** the way any Class 1 line does. A reference produced from recall, or matched to a key
without opening anything, is a **candidate** and says which of the two it is. **The distinction is
whether something was opened, not who read the result.**

**Where a key matches more than one paper, resolving it is a reading and is marked Class 2.** The
key alone cannot decide — *Curcio et al. 1990* names both a photoreceptor-topography paper and a
ganglion-cell-topography paper, same journal, same year, same tissue. The resolution is made
against what the citing line claims, which is why building this section is not extraction.

**Claude does not add a source no line cites.**

**The file's species composition becomes visible, which it is not entry by entry.** Class 1
requires species on the citation and the requirement is met line by line — so a file resting
largely on rat and cat work reads, entry by entry, exactly like one resting on human work. Gathered
in one place the balance is legible at a glance. That is something the section produces, not a
reason it exists.

**The short form goes inline; the full reference goes here, and nowhere else.** *(Settled by
Micky.)* A citing line carries the **key** — *Bakola et al. 2010* — and nothing more of the
reference. The authors, title, journal, volume, pages, year and method sit on that key's line in
this section. **Species is the exception and stays inline**, because entries argue from it — that a
figure is rat and not human, that an internal edge is typed from cat physiology — and an argument
cannot be read with its premise on another page. Where a key names no author, **the volume and page
*are* the short form**, since they are what pins one paper, and they stay inline for that reason.

**No line numbers, here or in the entries.** A reference line does not record which lines of the
file use its key, and this section's prose does not point at lines either. A line pointer is a
second record of a binding the file already holds, every edit above it invalidates it, and nothing
checks it — the same un-normalized table this section refuses for what-a-source-supports. The check
this section is built on is **a string match on the key**, which needs no pointer to run.

**Ordered by short form, alphabetically**, because the check is a string match and whoever runs it
is matching strings.

**Nothing enters because it is relevant.** The list is what this file cites, not what bears on its
subject. A source no line cites has no entry in it, however good the source is.

**What it costs.** Every file grows, so §8's size column goes stale on each file that gains a
reference section, and the map is re-measured per §8 rather than adjusted. Whether the section has
a form in files 19 and 20, which carry no entries and cite through prose, is **open and unasked**.

## 3. Per-region slot template

Every region carries the same skeleton, so gaps are visible at a glance:

- **Region** — name and anatomical type
- **Function** — what it does (biological terms only)
- **Inputs** — where it receives from. **One line per incoming edge**, and each line carries three
  things: the **source region** (a named region with an entry of its own, never a class);
  **carries:** the payload arriving on that edge — the property, its quality or units, its
  coordinate frame, and where it matters, what it explicitly does **not** carry; and **fan-in:**
  the contacts per receiving neuron from that source, or unknown.
- **Outputs** — where it projects to. **One line per outgoing edge**, carrying the same three
  things from the other side: the **target region**; **carries:** the payload leaving on that edge;
  and **fan-out:** the contacts per source neuron onto that target, or unknown.
  (Inputs/Outputs are the data flow; kept separate so loop directions are explicit.)
- **Internal structure and internal data flow** — the region's sub-elements, and the flow
  **between them**, on the same discipline as Inputs and Outputs: **one line per internal edge**,
  each carrying the **source sub-element**, the **target sub-element**, **carries:** the payload on
  that internal edge, and **fan-in:** and **fan-out:**, or unknown. Both are recorded for the
  reason §5 gives for inter-region edges: fan-in is what the sizing arithmetic runs on, and fan-out
  is what building the projection requires. Reads **unknown** where the region's internal
  organisation has not been described, and **owed** where it has been described but its internal
  edges have not been typed. *(These are two of the four slot states set out at the end of this
  section. They are not the payload rule's pair: a payload's two un-typed states are **owed** and
  **resisted** — §4 — and a payload never reads a bare* unknown.*)*

  **Names are written out; an abbreviation is a second label, never the only one.** A region,
  sub-element, tract or nucleus is written by its full name. Where the literature's abbreviation is
  what a reader will meet elsewhere, it is given **once, in parentheses, at the entry that owns the
  name** — *anterior inferotemporal cortex (area TE)* — and the full name is used everywhere else.
  Codes that are not descriptive of anything are the case this rule exists for: **V1** and **V4**
  tell a reader roughly what they are, **TE**, **TEO**, **VTF** and **PIP** tell them nothing, and a
  file whose purpose is to be checked by a reader cannot assume the reader already holds the key.
  The same applies to method abbreviations in provenance marks — name the tracer or the technique.

  **The floor of the hierarchy is whatever is in the brain.** *(Settled by Micky.)*
  There is no stated depth limit and there is not going to be one, because a limit set in this file
  would be a property of the file rather than of its subject. The slot goes as deep as the brain's
  own organisation goes: where a sublayer divides into cell classes that **project to different
  targets or carry different payloads**, those cell classes are sub-elements in their own right, and
  the internal edges between them are written. V1's layer 4B is the working case — its two output
  cell classes have different targets, so they are sub-elements, not properties of 4B. Where a
  division makes no difference to what arrives or leaves, it is a property of the element it sits
  in. **The test is the data flow, not the depth.**

  **A sub-element is named, never classed.** The same rule Inputs and Outputs carry for regions
  applies inside them: write **4Cα**, not "the magnocellular-recipient sublayer"; write **6b**, not
  "the deep sublayer of layer 6". A class resolves to whatever the reader supplies, and an edge
  pointing at a class cannot be checked. Where the literature's name is contested, the contested
  name is still the name — see below.

  **Where the receiving membrane belongs to a population housed elsewhere, the sub-element records
  the owner.** Most sub-elements are both a place and a population, and the distinction never
  arises. **Layer 1 is the case where it does**: an edge arriving there mostly terminates on apical
  tuft dendrites belonging to cells whose somata sit in layers 2/3 and 5, so the sub-element
  receiving the edge and the population owning the receiving membrane are different things. The
  convention is that the edge terminates where it physically terminates — on the sub-element — and
  the sub-element's own line records which populations own the receiving membrane, alongside any
  population resident in it. **No second internal edge is written for this.** There is no second
  synapse; the signal reaches the soma by propagation within one cell, and inventing an edge for it
  would put a transfer in the file that does not exist.

  *Why this slot exists, and what its absence cost.* Inputs and Outputs record only edges that
  **cross a region boundary**. Without a slot of its own, a region's internal circuit has nowhere
  to go, so it lands wherever the writer happened to put it — and it did: the cerebellar cortex
  carries its microcircuit as prose inside **Function**, plus an orphan "internal payload change"
  bullet filed under **Outputs** with no target region; V1 carries its laminar organisation as
  **parentheticals on inter-region edges** ("onto layer 4", "from layer 4B"); and most regions
  carry nothing at all. **The three cases are indistinguishable from outside.** A slot template
  exists so gaps are visible at a glance, and this was the one gap the template could not show —
  which is how V1's layer 4B came to have three outgoing edges and no statable input, with nothing
  in the file marking the hole.

  It is not a cortical-layer problem. It applies wherever a region computes with a described
  internal organisation — the cerebellar cortex's mossy-fibre/granule/parallel-fibre/Purkinje
  circuit, the retina's photoreceptor-bipolar-ganglion chain with its horizontal and amacrine
  interneurons, the hippocampal formation's entorhinal to dentate gyrus to *cornu Ammonis* 3 to
  *cornu Ammonis* 1 to subiculum chain, the spinal grey matter's laminae, the cochlear nucleus's
  parallel cell classes.

  **The transmission-only shape of this slot: sub-elements, a routing rule, and no internal edges.**
  *(**Seven entries take it**: the optic chiasm, the spinal cord white matter, and the five tracts in
  file 18.)* A fibre tract has real sub-elements by §3's own
  test — the corpus callosum's five sectors carry different traffic to different targets at different
  fibre calibres, the internal capsule's five limbs carry different fibre systems, the fornix's pre-
  and post-commissural limbs run to entirely different targets — but it has **no internal edges,
  because no synapse occurs in it**, so its sub-elements are parallel channels rather than a circuit.
  The slot therefore reads: the sub-element set, then **internal data flow: not applicable**, as a
  **positive statement about the tissue and not an unfilled gap**. **Segments along a tract's course
  are properties, not sub-elements** — the fornix's fimbria, crus, body and columns are the same
  fibres in sequence, so they fail the different-target test that its two limbs pass.

  **The matching form for a tract's Inputs and Outputs is a routing statement, not a payload transfer.**
  The payload is typed at the grey-matter entry that produces it and again at the one that consumes it;
  the tract's lines record **which region-to-region edge rides on which part of it**, and **fan-in and
  fan-out read *none* (no synapse here)**. This is settled by three independent passes reaching it —
  the optic chiasm, file 16's spinal white matter, and file 8, whose hippocampal entry writes an edge
  to the fornix and states in the entry that it is a routing statement rather than a transfer, with the
  regions it reaches written as their own edges.
- **Neurons** — count (+ range / source), or unknown
- **Synapses** — count and synapses/neuron, or unknown
- **Axons** — long-range fiber count / projection, or unknown
- **Grey-matter volume** — or unknown
- **White-matter volume** — or unknown
- **Myelination** — g-ratio / white fraction, or unknown

**Every slot appears in every entry.** *(Settled by Micky, and it applies to all slots, not only the
internal-structure one.)*
A slot is never omitted, because an omitted slot and an unknown slot are indistinguishable from
outside, and the template exists precisely so gaps are visible at a glance. Each slot reads one of:

- **its content**, where it is known;
- **not applicable** — where the region genuinely has no such property or function. This is a
  positive statement about the brain and is as informative as a filled slot; it is not a way of
  avoiding one, and it is wrong wherever the function exists but has not been looked up;
- **unknown** — the property exists and has not been measured or described (a measurement awaiting
  an instrument), or, for internal structure, the region's organisation has not been described;
- **owed** — described but not yet typed: for a payload, the edge exists and no one has decoded it;
  for internal structure, the sub-elements are described and their internal edges are not written.
  *Owed* is the mark that says **more research is needed and it is known what research**.

  *(**resisted** is the fourth payload state and is not a gap — see §4.)*

**Retrofitting is therefore not a separate pass and not optional.** Roughly sixty entries currently
omit the internal-structure slot; each of them is missing a required line, and the line is added when
that entry is next worked. Order follows the data flow, not a sweep.

### 3a. The standard laminar block, and what it is a claim about

Most cortical entries carry the same **Class-3** laminar description: sub-elements **1, 2, 3, 4,
5a, 5b, 6a, 6b**, with internal edges **4 → 2/3**; **2/3 → 5a and 5b** with reciprocal **5a → 2/3**;
**6a → 4** and **6a → 5a**, opposite signs; **6b → 6a**, arousal-gated; and within-sub-element
recurrence in 4 and 2/3.

**It is not a default and it is not boilerplate. It is a claim about granular isocortex**, and
**three of its edges route through layer 4.** Where an entry's own Function, Neurons or Myelination
slot says the tissue is agranular, dysgranular, allocortical or not cortex at all, **transcribing
the block asserts a circuit that entry denies**, and it must not be written. The correct record is
the sub-element set the tissue actually has, with the internal edges marked **owed**.

**Nine entries across five files cannot take it, and they fail in four distinct ways** — which is
why one exception clause will not do:

| how it fails | entries |
|---|---|
| **uniformly agranular** | primary motor cortex (5); premotor cortex (11); anterior cingulate cortex (11) |
| **agranular across a gradient** | temporal pole (7) |
| **agranular across an internal border** | Broca's area (11), BA44 agranular / BA45 granular; orbitofrontal / ventromedial (11), BA25 agranular; right inferior frontal gyrus (11), by homology |
| **not isocortex** | hippocampal formation (8), three-layered allocortex; cerebellar cortex (10), three-layered and not cerebral cortex |

**Three further entries in file 17 take the same four forms**, needing no fifth column. **Insula** is
*agranular across a gradient*, granular postero-dorsally to agranular antero-ventrally, joining the
temporal pole. **Midcingulate cortex** is *agranular across a gradient* as well, agranular to
dysgranular across its extent. **Retrosplenial cortex** is *agranular across an internal border*, area
29 granular against area 30 dysgranular, joining Broca's area — and its heading states the border, so
the block is excludable from the entry's own title. **Twelve entries across six files fill the table,
and that the four columns absorb all of them is weak evidence the four are the real set** — weak
because six of twenty files have contributed to it.

**Checking the block against the entry's own laminar description is part of writing the slot**, not
an optional refinement. The failure is silent otherwise: a copied block reads as complete, and the
two-ended diff cannot catch it because internal edges have only one end.

## 4. The payload rule

**Every edge is written twice — once in the producer's Outputs and once in the consumer's Inputs —
and the two payload declarations must say the same thing.** That redundancy is the point: it makes
the payload **mechanically checkable**. Diff the two ends of every edge; a disagreement is a
defect, found without anyone having to notice anything.

A property that a region's Function consumes but that no incoming edge declares is a **dangling
requirement** — the mirror image of a dangling edge, an edge with a target and no source — and it
fails silently for the same reason: each end reads as complete on its own, and only the pair is
broken.

**The diff detects a disagreement between two declarations and is blind to the absence of both, and
that is a property of the instrument rather than a gap in its coverage.** An edge missing from **one** end fails the diff and is caught. An edge
missing from **both** ends produces two files that are internally consistent, agree with each other,
and pass every check that can be run — because there is nothing written for the check to compare.
**Every edge absent from the whole source is absent in exactly this way**, so the count of them is
not merely unknown, it is *unmeasurable by the source's own instrument*.

**The worked case, and it is not obscure.** The hippocampal formation and the medial prefrontal
cortex are both long-standing entries, both named in several files, and both reach the same third
parties — the ventral pallidum, the angular gyrus, the posterior cingulate. **Neither declared any
edge to the other, in either direction, in any file.** The direct projection is real, well described
in the primate literature, arises from the subiculum, and runs by the fornix and by no other route;
its return arm is indirect, through a thalamic nucleus the source does not describe. **The absence
had survived every pass over both files** and was found only when a third file was held open beside
them and the literature was consulted.

**So the only instrument that finds this class is two files read together *against the literature*,
and reading two files together is not enough by itself.** The 08–11 pair had been read together
before and the absence survived it, because each file was checked against what the other *said*.
**A both-ends-absent edge is invisible to any procedure whose evidence is the documents.** This is
the standing argument for §2's rule that verification at the source rung runs to the literature: not
only because a written claim may be wrong, but because **a claim that was never written cannot be
wrong, and cannot be caught.** *(The finding is Class 2 — Claude's reading of what the instrument
can and cannot do. The worked case is Class 1 and is cited at the entries.)*

**A payload may never be left blank the way a synapse count may.** A synapse count is a
**measurement**: it exists whether or not anyone has taken it, and *unknown* is an honest answer
awaiting an instrument. A payload is **not a measurement**. It is a statement of what the signal
*is*, in a document whose declared purpose is data flow. If it cannot be written, the edge is not
understood — a hole in the file's core purpose, not a gap in its instrumentation. An unfilled
payload therefore reads **payload unknown — owed**, loudly, and is never quietly left off.

**Two reasons a payload can be un-typed, and the source marks which.** *Owed* is the default just
described: no one has decoded the edge, so its payload is a fillable gap awaiting a recording — it
points at an experiment to run. But an edge can be **decoded and still yield no shared low-dimensional
format**: the signal was read, and no coordinate frame the receiver already shares was found. That is a
different state and a stronger claim — not "not yet measured" but "measured, and it does not resolve
into a shared format." The source marks it **resisted** rather than owed. The distinction is actionable:
*owed* is a gap; *resisted* is a candidate finding about the region — that its content has no shared
frame and exerts itself, if at all, as gain or as a selection on a signal that does. Do not let a
*resisted* edge decay into *owed* (that discards a real result), nor an *owed* edge harden into
*resisted* (that manufactures one). Both still read, loudly, as payloads that do not convert; the mark
records *why*.

**The completion test for an entry:** an entry is finished when you can say what leaves it on a
wire. It gets harder as the data climbs — at the retina the payload is three chromatic channels;
at V4 it is surface colour with the illuminant discounted; at the temporal pole it is "an amodal
concept"; at the prefrontal cortex it is "a goal"; at the insula's anterior pole it is "a subjective
feeling"; and at the claustrum it cannot be written at all, which is the strongest form — that entry's
four candidate functions are each a claim about one output edge whose payload is owed. The last four
are phrases or blanks, not types, and an entry whose payload cannot be written is an entry whose
function is not actually understood. The slot is a detector for that.

**Where those cases cluster is itself a finding, recorded at file 19.** They are the convergence nodes
whose claim *is* that modality-specific formats become modality-independent — and a payload is a
statement about format, so the place where format is said to dissolve is the place where the payload
cannot be stated. The superior colliculus, whose binding is spatial **registration** rather than format
conversion, types its output without difficulty. **All the failing cases currently read *owed*; whether
any should read *resisted* is open and unasked.** *(The pattern is Class 2 — Claude's reading. That
each individual payload is owed is Class 1 from the entries.)*

**When internal detail changes an edge's arity, the other end has to be re-checked.** Describing a
region's sub-elements does not only add lines to the new slot — it can **split an existing
inter-region edge**. V1's input is one line onto "layer 4" while layer 4 is undivided; once 4Cα and
4Cβ are named it is **two** edges, with different payloads and different fan-ins. The producer's
Outputs at the far end still carries one. That is a payload disagreement of exactly the kind the
two-ended diff exists to catch, and it will be introduced *by the act of adding internal detail*.
So a pass that adds sub-elements to a region must re-run the diff on every edge whose arity it
changed — the cost of the internal-structure slot is not an append, it is a re-check.

**Caution on the two-ended diff.** It is only a check when *both* ends were written independently.
Two ends written in the same pass, from the same sentence, agree by construction and certify
nothing.

**The diff now crosses files, and that is the split's one real cost.** Most edges leave their own
section: of the resolvable endpoints, **46% cross a section boundary**, and
they cross diffusely — no pair of sections carries more than five. So a session working one file
will reach edges whose far end sits in a file it does not have. There are exactly two permitted
responses, and the session says out loud which one it took:

- **Ask Micky for that file**, work both ends, and return both.
- **Record the far-end change in the file at hand**, explicitly, as an owed cross-file edit naming
  the file and entry it is owed at only if both source files have independent research as backup.

**A cross-file endpoint carries the far file's stem, `<nn>_<section>`, never its number alone.** The
number fixes data-flow position and the section names the structure; either alone is ambiguous, and a
bare number goes **silently** wrong the moment a file is split, merged or renumbered — which §8 says
this source may yet do, the auditory file being large enough to be awkward and the visual file next.
The section string still names the structure set after the number has moved. **The stem is where the
second of the two responses above lands**: an owed cross-file edit names the file it is owed at, and
the stem is that name.

**Stems are written on touch, never by an independent sweep**, and only where the far file has been
read beside the file at hand — writing a stem to a file nobody opened is this section's own prohibition
in a new costume. An endpoint with no stem therefore means *not yet worked beside its far end*, and is
**not** a claim that no far end exists. Two states are distinguishable and only one is visible: an
endpoint carrying a bare number announces that a far end lives elsewhere and fails only to say where;
an endpoint carrying nothing announces nothing and reads as complete. **The second is the worse state
and it is the commoner one.**

**Writing an edge whose far end was never read is not a third option.** It produces a file that
passes inspection on its own and disagrees with a file nobody opened — the exact failure the
two-ended diff exists to catch, reintroduced by the mechanism meant to make the source workable.

**The two-ended diff does not work on internal edges.** An inter-region edge is written twice, in
two entries, by two passes — which is what makes the disagreement mechanical. An internal edge has
both of its ends inside a single entry, usually written in one sitting, so it agrees by
construction and certifies nothing. Internal edges therefore have **no mechanical check**, and
their payloads have to be read rather than diffed. The completion test still applies to them: an
internal edge whose payload cannot be written is an internal edge that is not understood.

## 5. Fan-in and fan-out are both recorded, for different reasons

**Fan-in** is what the accuracy and sizing arithmetic runs on downstream: a neuron's stored value
is set by the count of contacts converging on it. **Fan-out** is not needed for that arithmetic —
but it is needed to *build* the thing, because a projection cannot be constructed from the
receiving end alone, and re-deriving it once per design iteration is a cost paid over and over.

Both are edge properties, recorded where the literature gives them and **unknown** where it does
not. Neither is a substitute for the payload: a fan-in says how many lines arrive, and says nothing
whatever about what is on them.

## 6. Number conventions

- Cortical neuron counts are **per hemisphere** unless stated. *(Settled by Micky.)* **A whole-brain count would only be meaningful if the brain were
  symmetrical, and it is not.** Broca's area and its right-hemisphere counterpart are the standing
  example: they are not the same region doing the same job on two sides, and a single number
  covering both would assert a symmetry that does not exist and would hide the asymmetry that is
  the interesting fact. Where the literature reports a structure whole, see the next line.
- Structures usually reported whole in the literature (cerebellum, basal ganglia, spinal cord,
  midline nuclei) are tagged as whole with the per-side value alongside.
- Where slots constrain one another — neurons × fan-in against stated synapse totals; divergence ×
  source count against convergence × target count — the cross-check is run and any gap is recorded
  as a **finding about the source**, not smoothed away.
- Arithmetic that will be quoted is **computed, not done mentally.**
- **A contested name is recorded as contested, not resolved by preference.** Where the literature
  disagrees about what a sub-element *is* — the standing dispute over whether **4B** is a sublayer
  of layer 4 or of layer 3 is the working example — the source keeps the name in common use, states
  that the classification is disputed and what the competing reading is, and lets the region's
  **edges** carry the function. Which number a sub-element wears is nomenclature; what arrives on it
  and what leaves it is data flow, and only the second is what this file is for. This is the same
  treatment the cross-check line above gives a failed constraint: recorded as a finding, not
  smoothed away.

### 6a. Abbreviation convention, and the per-file cleanup

**The base rule is existing, not new.** ***Expansion* means one thing in this project and this is
where it is defined: what an abbreviation stands for.** *Cornu Ammonis* field 1 is the expansion of
**CA1**. Nothing else in the source or in the rungs below it is called an expansion — not a
reference, not an addition to an existing entry, not a new entry produced by research. Spelling an
abbreviation out in full at its first occurrence
in every file — written as "full name (ABBR)", never introduced pre-defined — is a standing
convention (plausibly already stated in CLAUDE.md, which is not visible from inside a working
session, so this subsection does **not** redefine it and should be reconciled with CLAUDE.md's
wording when both are in hand). A term used only once or twice in an entry is spelled out each time
and not abbreviated at all — the abbreviation earns its space only by recurring within the entry.

**The second rule, and it is Micky's, is the cross-field collision check.** Frequency of past use is not the test, and is in fact the trap: DG, CA1 and CA3 have been
used for the hippocampal subfields so long that their expansions (dentate gyrus; *cornu Ammonis*
fields 1 and 3) are no longer in anyone's working memory — familiarity has hidden the abbreviations
rather than justified them. "We have used it many times" is not a reason to keep a bare
letter-string.

**The test is collision: does the letter-string have a more common meaning in some other field?**
The type case is **HCN**, used here for the *hyperpolarization-activated cyclic-nucleotide-gated* ion
channel (file 13) — but HCN reads far more commonly as **hydrogen cyanide**, so the string drops a
poison's formula into a passage about ion channels, exactly where the ambiguity is worst. The
colliding domain is **not just chemistry**: it is chemistry, genetics, clinical medicine,
engineering, physics, government / military acronyms, even stock-ticker symbols — anywhere a short
string carries a dominant meaning a reader imports from another life. Clearing an abbreviation is
therefore a **per-string research question** across those domains, not a count, and not something a
single file's conversion pass can settle. Where a string collides, the term is spelled out in full
(the channel becomes *hyperpolarization-activated cyclic-nucleotide-gated channel*, its current the
*pacemaker / hyperpolarization-activated current*, not "I_h").

**The check is case-sensitive, and the casing is load-bearing.** The string must be cleared exactly
as written, case included, because case is often the disambiguator in real notation: **Ca**
(calcium) vs **CA** (*cornu Ammonis*) vs **ca.** (circa); **mS** (millisiemens) vs **ms**
(millisecond); **Gi** (a G-protein) vs **GI** (gastrointestinal); **I_h** vs **IH**. A cleanup that
normalises or uppercases casually will either manufacture collisions that were not there or hide
ones that were — so the pass must preserve original casing and treat differently-cased strings as
different symbols.

**The cleanup is per-file, one file at a time, alongside the architecture passes.** *(Micky's
ruling.)* **Cleared, case-exact grep returning nothing: files 15, 17, 18, 19 and 20.** The remaining
fifteen are open.

**Per-string cross-field research is what clearing an abbreviation for *retention* costs, not what
removing one costs**, and removal is almost always available: a colliding string **spelled out in
full** is collision-proof by construction and needs no research to justify. That is why the cleanup
runs as a rider on a file pass without relocating the problem. What a file pass does **not** produce
is the worked table below, which is owed for any string somebody wants to keep.

**Still owed — the worked table**, for retention decisions only: each abbreviation in use (as written,
case-exact), its intended expansion, and whether the string collides with a more common meaning in any
field.

**Offenders, non-exhaustive, with the colliding meaning that condemns each.** Those marked *cleared*
are gone from the five cleared files and may survive in the other fifteen; the rest are open.

- **HCN** — hydrogen cyanide (file 13). Open. The case this subsection was written for.
- **CN** — the cyanide ion (file 15). *Cleared.* The same collision as HCN, one letter shorter.
- **SCN** — thiocyanate (file 20, and the suprachiasmatic nucleus throughout). *Cleared in 20.* Third
  member of the same chemical family, which suggests the family is worth sweeping as a family.
- **AI** — artificial intelligence, for the anterior insula (file 17). *Cleared.* The collision is with
  the field this whole project is in.
- **MCC** — Matthews correlation coefficient, for the midcingulate cortex (file 17). *Cleared.*
- **PCC** — Pearson correlation coefficient, for the posterior cingulate cortex (files 17, 20).
  *Cleared.* With the row above: **two adjacent cingulate fields whose abbreviations are both standard
  machine-learning metrics.**
- **WM** — working memory, for white matter (file 18). *Cleared.* The collision is inside this
  document's own subject.
- **VP** — the ventral pallidum, for the ventral posterior thalamus (file 20), where both are joints of
  the same loop and both appear within three lines. *Cleared.* **A within-source collision, not a
  cross-field one** — a class this subsection did not anticipate and the one the collision test cannot
  find by looking outward.
- **VIP** — vasoactive intestinal peptide, for the ventral intraparietal area (file 19). *Cleared in
  19*, and it is an **entry heading in file 4**, so the collision survives where it does most harm.
- **IT** — information technology, for inferotemporal cortex (files 19, 20). *Cleared in those*, and
  likewise an **entry heading in file 1**.
- **M1** — the Apple M1 processor, the M1 money supply, for primary motor cortex (files 17, 18, 20).
  *Cleared.*
- **SMA** — the SubMiniature-A connector, spinal muscular atrophy, for the supplementary motor area
  (file 17). *Cleared.*
- **A1** — the first cell of a spreadsheet, for primary auditory cortex (files 18, 20). *Cleared.*
- **GPi** — glycosylphosphatidylinositol, for the internal globus pallidus (file 20). *Cleared.*
- **EM** — expectation-maximisation, for electron microscopy (file 18). *Cleared.* A **method**
  abbreviation in a provenance mark, which §3 already forbids separately.
- **LHb / MHb** — **Hb is haemoglobin**, embedded (file 17). *Cleared.* The collision is inside the
  string rather than equal to it, which no whole-string comparison would catch.
- **S1 / S2** — the sacral nerve roots, the first and second heart sounds (files 17, 18, 20).
  *Cleared.*
- **DG / CA1 / CA3** — the burned-in hippocampal set whose expansions have gone invisible (file 20).
  *Cleared in 20*, open in file 8, which owns them.
- **The singly-used coinages VMpo, RMTg, aMCC, PIVC** — *aMCC and PIVC cleared* (file 17); *VMpo and
  RMTg cleared in files 17, 18 and 20* and open where they are heading text (files 12, 14).
- **n/a** — not a collision but a **slot-state term**: §3 names the state *not applicable*, and "n/a"
  is a fourth spelling of it (file 18). *Cleared.*

**Two general findings from the five files, both Class 2 — Claude's reading, offered to be checked.**
The first is that the strings that collide worst are **short, uppercase, and drawn from the same
naming habit as the metrics and hardware of the reader's other life**, so a computing-literate reader
is at *more* risk from this document than a lay one. The second is that **an abbreviation in an entry
heading is worse than one in prose**, because the heading is what other files quote when they name an
endpoint — which is why VIP and IT surviving in files 4 and 1 matters more than their being cleared in
19 and 20.

## 7. What does not belong in the source

The source contains the brain. It does not contain:

- **Its own design.** The slot template, the payload rule, the verified-only rule, the number
  conventions — all of it lives here, in this file, not in the source's front matter. A passing
  reference to a rule inside an entry's prose is legitimate: an entry may say why a payload is hard to
  type without restating the payload rule.
- **The state of any pass over it.** Which sections are converted, what a session concluded, what the
  plan is. There are no pass stamps and no header block generated from them. What is *owed* or
  *contested* is not pass state at all — it is a statement about the brain's description, it belongs on
  the entry, and the payload rule already requires it there.
- **History.** No versions, no rev numbers, no "changed since," no reference to sessions or prior
  files. The date in the filename is the date the file was **last regenerated**, not a version
  marker. *(The rule is CLAUDE.md's and governs every rung; it is named here because this is the
  list of what the source excludes.)*
- **Rules invented to repair the file.** Provenance classes, repair order, fidelity procedure, the
  added-edges-are-drift hazard — these govern how Claude works, not what a brain is. They stay in
  CLAUDE.md.

## 8. The source is twenty files

**The split is verified lossless: the twenty files concatenate back to a single source
byte-identical.** The seam is the **H1 pathway section** — not a good seam (see §4), but when no seam
is cheap the right move is to make the seam *cheap to cross* rather than hunt for a better one.

**Why the split is necessary.** One file would stand at ~371k tokens. With CLAUDE.md and this file
beside it, no work could begin inside a 200k session at all.

**The size measurement, and the headroom it is spending.** The figures are computed from the files'
own byte counts (bytes ÷ 4), not tokenised, so they are estimates — but estimates of the same kind
throughout. **Only one measurement is kept; a superseded one is discarded, never stacked beside it.**

- **The whole source: ~371k tokens / ~1,447 kB across 20 files.**
- **Median file: ~16.4k tokens. Largest: file 2 at ~42.3k, with file 11 at ~42.3k level with it**,
  past the point this section calls "large enough to be awkward on its own."
- **Non-blank lines: 15,835.** This figure is method-independent — counted the same way the split's
  losslessness is verified — so it does not depend on the byte estimate at all.
- **The reference sections are the growth, and it continues as long as the source files are worked.**
  Every file carries one under §2a. **The section was specified knowing it would cost this.**
- **Fixed overhead is ~29.8k tokens** — CLAUDE.md ~9.8k plus this file ~20.0k — before a single
  source file is opened, so a session working the median file starts near **46k**. **This file is
  larger than fourteen of the twenty files it describes.**
- **A maintenance section that mis-measures itself is the case with no outside check**, since
  nothing else in the project has reason to look. The two figures above are computed from the
  files' own byte counts on the same method as every other row, not carried forward.

The overhead figure is the one to watch, and it is the reason §7 keeps this file's own design out of
the source: the overhead is paid on *every* session, on every file, whereas any one source file is
paid once. *(Measurements Class 1, computed. The reading placed on them — that the split's headroom is
being consumed rather than merely used — is Class 2.)*

**Each file carries**, above its content: what is in it, its size, its entry list, and a warning
that edges cross into other files — so an endpoint named in a file with no entry in that file is
**not** a missing region until the other files have been checked. **Below its content it carries the
reference section §2a specifies.**

### The working protocol

1. Micky hands Claude **the next file in data-flow order**, plus this file and CLAUDE.md.
2. Claude works it entry by entry, at the slot standard in §3, under the verified-only rule in §2.
3. On reaching an edge whose far end is in another file, Claude takes one of the two responses in
   §4 — **ask for that file**, or **record the cross-file edit as owed** — and says which it took.
4. Claude returns **every file it changed, complete**, and **only** those. A file read for reference
   and not modified is not returned; handing it back unchanged puts a second copy in Micky's hands
   and invites editing the wrong one.
5. Every changed file has its **header block updated in the same edit**, so no file ever describes
   itself wrongly.

**The weakening this accepts, stated plainly.** "Complete files, not patches" means complete *section*
files. A session can return an internally consistent file while breaking an edge in a file it never
opened. This is the price of the source being workable at all, and it is paid knowingly.

**A cross-file mark records only what the writing file could see of the far file, and nothing more.
It is *unverified*, never *outstanding*, until the far file has actually been opened beside it.** Two
files worked in parallel each read the other's unrevised state and write marks against it, so a mark
can be discharged at the far end before anyone reads it — and a mark can be flatly false, asserting
that a producer declares no such edge over an edge that producer declares, having been written from
the near file's own declaration rather than from the far file.

**What this does not license is a sweep.** The repair is not to re-check every pair; it is to read
the far file when the near file is worked, and to write what was checked. A mark discharged by
reading is worth more than twenty marks re-flagged by a script, because the script cannot type a
payload.

### The map

**Needs to be updated every time the source files are changed!**

| # | file | contents | entries | tokens / size |
|---|---|---|---|---|
| 1 | `01_visual_pathway` | VISUAL PATHWAY | 8 | 33.5k / 130 kB |
| 2 | `02_auditory_pathway` | AUDITORY PATHWAY (through the temporal lobe) | 11 | 42.3k / 165 kB |
| 3 | `03_other_senses` | OTHER SENSES (olfactory, gustatory, vestibular) | 7 | 17.7k / 69 kB |
| 4 | `04_dorsal_visual_parietal_stream` | DORSAL VISUAL / PARIETAL STREAM | 4 | 18.6k / 72 kB |
| 5 | `05_sensorimotor_loop` | SENSORIMOTOR LOOP (body-side) | 6 | 15.3k / 59 kB |
| 6 | `06_posterior_parietal` | POSTERIOR PARIETAL (remainder — inferior parietal lobule, grasp/reach intraparietal, precuneus) | 5 | 17.4k / 68 kB |
| 7 | `07_anterior_temporal_lobe` | ANTERIOR TEMPORAL LOBE | 1 | 7.2k / 28 kB |
| 8 | `08_medial_temporal_lobe` | MEDIAL TEMPORAL LOBE | 3 | 22.5k / 87 kB |
| 9 | `09_basal_ganglia` | BASAL GANGLIA | 2 | 9.3k / 36 kB |
| 10 | `10_cerebellum` | CEREBELLUM | 3 | 13.5k / 52 kB |
| 11 | `11_frontal_lobe` | FRONTAL LOBE | 9 | 42.3k / 165 kB |
| 12 | `12_thalamus` | THALAMUS (higher-order, motor, limbic, and gating nuclei) | 9 | 25.7k / 100 kB |
| 13 | `13_neuromodulatory_systems` | NEUROMODULATORY SYSTEMS (brainstem + basal forebrain) | 4 | 13.3k / 51 kB |
| 14 | `14_brainstem_midbrain_hypothalamus` | BRAINSTEM / MIDBRAIN / HYPOTHALAMUS | 10 | 27.2k / 106 kB |
| 15 | `15_cranial_nerve_nuclei` | CRANIAL-NERVE NUCLEI AND FINER BRAINSTEM DETAIL (segmental motor / sensory nuclei, pretectum, gaze integrators) | 4 | 12.1k / 47 kB |
| 16 | `16_spinal_cord` | SPINAL CORD | 3 | 11.2k / 43 kB |
| 17 | `17_insula_claustrum_habenula` | INSULA, CLAUSTRUM, HABENULA, CINGULATE remainder (the salience / interoception / value-brake / limbic-midline wall) | 6 | 19.7k / 76 kB |
| 18 | `18_white_matter_tracts` | WHITE-MATTER TRACTS (commissural / projection / association — transmission, no processing) | 5 | 15.3k / 59 kB |
| 19 | `19_cross_modal_integration` | CROSS-MODAL INTEGRATION (synthesis — where the senses meet) | 0 | 3.0k / 11 kB |
| 20 | `20_loop_structure` | LOOP STRUCTURE (synthesis — how the loops close and re-enter) | 0 | 3.4k / 13 kB |
| | **total** | | **100** | **370.5k / 1447 kB** |

**No row rests on a figure nobody checked. The file column carries stems, not filenames**, so a
row cannot go stale when a file is regenerated; only the counts can.

**Every numbered file in a rung has to be regenerated after a numbered file is changed.** **A change
that touches every file at once is exactly the change that will not think to re-derive the map**,
because it has no single file to hang the re-derivation on — and a pass working the files rather than
the map is the shape that misses it.

**The entry count's method, and the naive version over-counts.** The column is **`##` headings, less
References, less any section that is commentary rather than a structure** — file 11 carries two `##`
sections that are not entries, its developmental-timing and electrical-stimulation sections, and every
file carries a `##` References section under §2a. **A naive heading count returns 102 + References;
the true entry count is 100.** The rows above exclude both. This is the same judgement §9's
`NOT_A_STRUCTURE` list makes at the architecture rung, needed here too.

**Auditory at 42.3k and file 11 at 42.3k are the two files large enough to be awkward on their own**,
and they are now level: the margin between them, wide when this line was last derived, is gone. The
auditory file would split cleanly at the belt if it is reopened, and file 11's
seam is obvious: its granular prefrontal entries and its motor/premotor/eye-field entries share a lobe
and very little else.

**The kB column's unit, which is load-bearing.** This column uses **kB = 1024 bytes, truncated**,
not 1000. **A later pass using 1000-byte kB will read about 2.4% high on every row at once** and will
look exactly like a one-directional method error when it is only a unit mismatch. Since §8 assigns
this column the job of a **checksum**, an undeclared unit is the one defect that would make the
checksum fire on a file that is fine.*

**What the size column is for, and the failure that justifies it.** A copy of a file in hand can
measure short against its row while its own header agrees with itself — **a complete, coherent file
that passes every check runnable on it alone, and is simply not the current one.** **Date-in-filename
catches a renamed file and cannot catch this**, since two copies can be legitimately named for the
same day. What catches it is **a second, independently-derived record of the same quantity** — the
same principle as §4's two-ended diff, applied to file size instead of to a payload. **That is the
argument for maintaining this column even though it is tedious: it is not documentation, it is a
checksum**, and smoothing a disagreement to the nearer number destroys exactly the signal that is
working.

**The standing rule: where two copies of a file are present, only the newest is used.** **The
likeliest way two copies arise is not carelessness but the ordinary shape of a delivery**: a new file
is uploaded and the old one is not removed, and both are legitimately named for the day they were
written. **Date-in-filename is what makes the rule executable** — without it there is no newest, only
two files.

**The rule has one blind spot and it must be stated with the rule**, because it is the case the rule
cannot cover: A directory listing shows filenames, so the newest is identifiable if the date is in 
the filename and the rule applies. A project-knowledge search returns chunks, and a chunk does not 
reliably carry the filename it came from. So a search over a directory holding two copies can return 
content from the superseded one with nothing to mark it as superseded — and the failure is silent in 
the way §4 describes, since the stale text is internally coherent and simply out of date. 
**Therefore: the rule is a repair for a directory, not a defence against one.** The duplicate should 
be removed rather than tolerated, and where a search returns something that contradicts what a listing 
shows to be the newest file, the listing wins.

**Files 1, 2 and 3 — visual, auditory, other senses — are the most worked sensory lines**, and most
worked is not finished: the cochlea and the olfactory epithelium entered files 2 and 3 after those
sections had been called complete.

**Size tracks how recently a file was worked, not what it describes.** The order is **11 (42.3k), 2 (42.3k),
1 (33.5k), 14 (27.2k), 12 (25.7k), 8 (22.5k), 17 (19.7k), 4 (18.6k), 3 (17.7k), 6 (17.4k)**
— *medial temporal lobe* sits fifth on the strength of one research pass that added no entry at all.
**Expect any file to arrive in this bracket after it is worked, and to stay there.**

**Re-derive this map whenever files are added, split, renamed, *or worked*.** The last condition is
the one most easily missed: the trigger is not a structural change to the file set, it is an ordinary
content pass. *(Class 1 throughout — measured. The expectation about future passes is Class 2.)*

**Files 19 and 20 are synthesis prose and carry no entries**, so the entry list in their header
blocks is empty.

**A wrong map fails *silently***, which is the reason to re-derive rather than guess, and is exactly
what went wrong with the line-number chunk map this section replaces.

## 9. Dangling endpoints — the inventory

**What this section is.** One measurement, kept here rather than on the entries because it cannot
sit on them: an endpoint naming a region the source does not describe **has no entry to carry the
mark**, and a class endpoint's defect is only visible with every entry name in view at once. That
is the one case §7's record-it-on-the-deliverable rule does not reach. It records what was found,
never what should be done next; the repair for each item is written on the entry whose edge dangles,
when that file is next worked.

**Coverage, and it is the first thing to read.** This list is not one measurement. Its base is a
sweep over **8 of 20 files and 42 of 95 entries — 44%** — held: **1, 4, 5, 6, 7, 8, 11, 17**; not
held and not checked: **2, 3, 9, 10, 12, 13, 14, 15, 16, 18, 19, 20**. Everything since has been added
**by hand, one file's pass at a time**, so the list is a patchwork of that sweep and many amendments.
**Scanned by the sweep:** 278 edge lines, about 190 distinct endpoint strings.

**Every "missing" call below is provisional in one direction only** — the endpoint was checked against
the 42 entries held and found absent, and could still have an entry in one of the twelve files the
sweep did not hold. **Nothing here demonstrates absence.** The complement is not provisional:
endpoints that resolved into the 42 are resolved. Endpoints whose far ends plainly belong to a file
the sweep did not hold — the auditory belt, the cochlear nuclei, the olfactory tract, the gustatory
and vestibular pathways, the striatum, the cerebellum, the thalamic nuclei, the superior colliculus,
the hypothalamus, the brainstem, the spinal grey matter, the white-matter tracts — are **not listed**,
and were not checked either.

**The list is stale in *both* directions, and a one-directional staleness note would itself be a
defect**, because it tells a reader which way to discount a list that moves both ways. It
**understates** where a family was added by hand rather than by a re-run. It **overstates** where a
pass has closed a family and nothing removed it, and **9b's count of 21 class endpoints overstates**
for that reason. The typed-edge count across the source has risen steeply since the sweep — file 11
alone carries 101 typed edge lines against the 13 the sweep saw — and splitting compound lines is what
converts a class endpoint into named ones.

**Owed: re-run the sweep across all twenty files.** All twenty are in hand, so the re-run is
possible.

### 9a. Named regions with no entry in the entries held

**They cluster into families, and the clustering is the finding** — a family is one decision,
not several.

- **Medial parieto-occipital — the reach channel's origin.** **V6**; **V6A ventral subdivision**;
  **V6A dorsal subdivision**; **caudal intraparietal area**. Named on edges in files 6 and 1.
  Not plausibly in an unread file: all four are visual or visuomotor cortex and both files that
  would own them (1 and 4) are held. File 6's section head names V6A as the origin of the reach
  channel, so the channel is described from its second stage onward. Receptor mapping (eLife
  9:e55979, 2020, already cited in files 4 and 6) groups V6, V6Av and the caudal intraparietal
  territory with V3d and V3A, which are in file 1.
- **Parahippocampal — the ventral stream's route into memory.** **perirhinal cortex (areas 35 and
  36)**; **parahippocampal cortex**; **temporal area TF**; **temporal area TH**. Named on edges in
  files 1, 4 and 7. Not plausibly elsewhere: file 8 is the medial temporal lobe, is held, and
  carries three entries, none of them these. Entorhinal cortex, by contrast, **is** covered, as a
  sub-element of the hippocampal formation entry. **Five files' edges point into this family.**
  File 17's retrosplenial entry names **parahippocampal cortex** as a
  producer on its input side and as the route on its output side, and file 20 records the cost: the
  **Papez loop's return arm from retrosplenial to entorhinal cortex runs through this family**, so, as
  with the pontine nuclei, the gap sits inside a closed loop rather than at a terminus. **This family
  and the pontine one block two of the source's named loops between them.**
- **Extrastriate areas named by file 1's own edges.** **dorsomedial area**; **dorsal prelunate
  area**; **V4 transitional area**; **ventral occipitotemporal area**; **visually responsive part of
  temporal area F**. All named inside two compound output lines in the V3 / V3A entry — the entry
  that already carries an owed split of its own. (The **ventral posterior area** is named there too
  and is already marked as that owed split, not as a missing region.)
- **Parietal and cingulate areas named by files 5 and 6.** **parietal rostroventral area**;
  **parietal opercular area PGop**; **retroinsular area**; **cingulate area PEci**. Its partner
  **PFop is** covered, as a sub-element of the supramarginal gyrus entry, and cingulate areas 23 and
  24 are covered by the posterior and anterior cingulate entries — an asymmetry of exactly the kind
  that says nobody checked rather than that somebody decided.
- **Brainstem relay stations with no home.** The **rostral ventromedial medulla** — named as the
  relay of the periaqueductal gray's descending analgesia (file 14's periaqueductal entry) and as a
  producer of the spinal analgesic gate (file 16), owning no slot — and the **lateral septum**, named
  as an input to both the rostromedial tegmental nucleus and the hypothalamus, with no entry anywhere.
  Both are recorded on the entries whose edges dangle, per §7.

- **Cerebro-cerebellar loop stations — the corticopontine relay and the rubral vertex.** **pontine
  nuclei**; **red nucleus** (both its magnocellular and parvocellular parts). Named on **six** edges:
  five in file 10, and the **rubrospinal tract** dangling onto the cord's ventral horn from this
  entry-less nucleus, recorded as a routing statement in file 16's white-matter entry. Two further
  routed edges in file 18 have the same missing consumer — the internal capsule's corticorubral fibres
  through the posterior limb and its frontopontine fibres through the anterior limb. **They belong to
  files 10 and 14 together**, because the loop crosses the section boundary — anatomically ventral
  pons and ventral midbrain, functionally cerebellar-loop stations. Not plausibly elsewhere.
  **Both sit *inside* the cerebro-cerebellar loop, so that loop cannot be followed around in this
  document at all.** **The corticopontine relay is the load-bearing one**: it is a processing stage,
  not a relay — corticopontine divergence followed by pontocerebellar convergence, an origin
  population that excludes large parts of prefrontal and temporal cortex, and a de-emphasis of central
  vision and the distal extremities. **A region that transforms the payload cannot be left as a name
  on an edge.** For the red nucleus the human case inverts the textbook one: the magnocellular part is
  vestigial and the parvocellular part, which carries the dentate limb, occupies most of the volume.

- **The nucleus reuniens, and it is the most consequential item this section carries.** The **midline
  thalamic nuclei have no entry anywhere in the source**;
  the string *reuniens* occurs in none of the twenty files. File 12 carries eight entries, and its
  intralaminar entry holds the **centromedian** and **parafascicular** nuclei only, recording the
  remaining intralaminar members as owed and naming the midline group not at all. **Four edges
  terminate on it** — the hippocampal formation and the amygdala, in both directions, written in
  file 8 from primate tracing. **Its anatomical owner is not in doubt: file 12.**
  **What makes it worse than a missing terminus is what it carries.** Medial prefrontal cortex does
  not project directly to the hippocampus; **this nucleus is the entire return arm of the
  hippocampal–prefrontal loop.** So the source describes the outgoing limb of that loop as two
  typed edges and its return as a projection into a blank. **This is the pontine-nuclei shape
  again** — a missing region *inside* a closed loop rather than at its end — and it is the second such
  loop, after the cerebro-cerebellar one, that cannot be followed around in this document at all.
  *(A related endpoint with the same cause: file 11's anterior cingulate entry names its
  thalamic source as "the midline / intralaminar thalamus," a compound whose midline half has no
  referent.)*

- **The precentral opercular cortex, and it is a different kind of miss.** Named as a dense amygdalar
  target in the primate tracing behind file 8's lateral edges. **The source names the frontal operculum only as half of the primary gustatory
  cortex** (file 3, "anterior insula + frontal operculum") and again at file 17's insula entry —
  **and the precentral opercular area is a distinct field from gustatory cortex** in the parcellation
  the tracing uses, which labels both separately in the same sections. **So the nearest thing the
  source describes is a neighbour, not the same place**, which is the failure mode a reader is most
  likely to smooth over. **Which file owns it is genuinely unobvious** — frontal by position,
  opercular by neighbourhood, so 11, 3 and 5 are all plausible and none is clearly right.

- **The habenula's own two ends, and they are a matched pair.**
  **interpeduncular nucleus** — the **medial habenula's principal output**, and the string **appears
  nowhere in the source outside that one entry**. So the entire medial-habenular limb (nicotine aversion
  and withdrawal, the cholinergic / substance-P arm) is described from its origin only. Its anatomical
  owner is the ventral midbrain tegmentum, which is file 14.
  **septal nuclei** — the **medial habenula's principal input**, and now named as a producer by
  **three** files: file 17's habenula input, and file 14 twice, at the rostromedial tegmental entry and
  at the hypothalamus. **Which file owns the septal nuclei is not obvious**, and
  that is part of why they have no entry: they are basal forebrain, so file 13 is the nearest owner.
  **The pair is the finding.** A nucleus whose only major input and only major output both lack entries
  is described as a relay between two blanks — and the habenula is *not* a small item in the source: it
  carries the map's one firm epithalamic volume and closes the aversive-value hook.

### 9b. Endpoints naming a class or a network rather than a region

§3 requires a named region with an entry of its own. Twenty-one endpoints name a class instead, and
an edge pointing at one cannot be checked. In files 1, 4, 5, 6, 8 and 11: *posterior parietal areas
/ cortex; ventral-stream visual areas; dorsal-stream visual areas; occipitotemporal cortex;
somatosensory association cortex; temporo-parieto-occipital cortex; smooth-pursuit oculomotor
circuitry; the distributed conceptual / semantic system; lateral temporal semantic cortex; higher
dorsal and parietal areas; lower visual areas; higher ventral areas; widespread cortex; sensory
cortices; other association / prefrontal cortex; other frontal / prefrontal cortex; autonomic
centers; the medial motor fields; the medial bank of the intraparietal sulcus* (which resolves to
three areas, one of them in 9a).

**A class endpoint has two repairs and they are not the same act.** Splitting it against far ends
that already declare the edge **adds no claim**; splitting it against the literature **adds one claim
per member**, each of which then owes a cross-file edit. **The second is the only repair available
when the class is wide because nobody looked, rather than wide because the writer was compressing.**
The worked case is file 8's amygdala output, *widespread cortex (including feedback to sensory
areas)*: five members split against declared consumers, four more named from the literature with no
far end declaring them, and a residue — *feedback to sensory areas* — still a class, with files 1 and
2 not yet read beside file 8.

**Two of them are not repairable by naming, and that is a separate finding.** *Default-mode
partners* and *the ventral-attention frontoparietal network* name **networks** — sets of regions
defined by correlated activity, not by a projection. Naming the members turns one edge into several
and asserts that each member receives the same payload, which is not what a network claim says.
**How the source writes an edge to a network, or whether it refuses to, is open and unanswered.**
Two edges in file 6 wait on it.

***A worked datum for that question, and it is a datum, not an answer.*** *File 17's posterior
cingulate entry names four default-mode partners — medial prefrontal, angular gyrus, precuneus, medial
temporal lobe — as **four named consumer edges**, and the split is defensible only because **two of
those far ends declare the edge from their own side** (files 6 and 8, each recording it as owed at
file 17). The residual endpoint in the same entry — "the cognitive-control network," via the dorsal
posterior cingulate — is **not** split, because no far end declares it and naming members would
manufacture the arity. **So the shape that works is: split where the far ends already declare the
edges, refuse where they have not.** Whether that generalises into the convention, or is only what to
do when the members happen to be declared, is **Micky's to decide**; the two file-6 edges wait on it.*

### 9c. Unnamed sources — a payload with no producer at all

*eye-position / efference copy* (file 4, the ventral intraparietal gain-field mechanism);
*extraretinal eye-movement / efference copy* (file 4); *gaze-position signals* (file 5); *auditory
saccade-target signals, and the stage converting them to eye-centred coordinates* (file 4). All four
are already marked owed on their entries. They are collected because **three of the four are the
same missing signal** — an eye-position or eye-velocity copy, wanted independently by three entries.
That is one region to find, not three.

### 9d. Re-run condition

This inventory is **a measurement of a moment** and goes stale the way the map does. **All twenty
files are in hand, so the re-run is possible and has not been done.** Re-run it also after any pass
that splits compound edge lines — splitting is what converts a class endpoint into named ones, so the
counts in 9b fall as the source is worked and a stale count would understate the progress.

**§8's counter-measure applies here and has not been applied.** This section keeps each amendment
alongside what it supersedes, which is why it reads as a patchwork of one sweep and many hand
additions rather than as one measurement. **Keep the delta, discard the superseded inventory.**

### 9e. Tracts, which are a different class from regions

*The placement of this subsection is **Micky's call**. §9 was built for endpoints naming **regions**
the source does not describe, and a tract is not a region: it computes nothing, it carries other
entries' edges, and whether it warrants an entry at all is a decision rather than a finding. But the
two lists below have nowhere else to live, for exactly §9's stated reason — a tract with no entry has
no entry to carry the mark.*

**Tracts named on other files' edges with no entry anywhere**, checked across all twenty files. The
source carries seven tract entries — the optic chiasm (file 1), the spinal cord white matter (file
16), and five in file 18, one of them the **medial longitudinal fasciculus**, which earns its entry by
carrying more declared traffic (a routed edge typed at both region ends, in files 3 and 15) than three
of the others. **A tract that is *mentioned* in file 18 does not thereby have an entry**, and the
remainder below have none: the **three cerebellar
peduncles** (file 10, which records their absence); the **ansa lenticularis, lenticular fasciculus and
nigrostriatal bundle** (file 9, same); the **middle longitudinal fasciculus** (file 7); the
**corticobulbar tract** (file 15); the **mammillothalamic tract** (files 8, 12, 14); the **stria
medullaris** and **fasciculus retroflexus** (file 17); the **stria terminalis** and **ventral
amygdalofugal pathway** (file 8); the **perforant path** (file 8); the **medial** and **lateral
lemniscus**; the **optic nerve**, **optic tract** and **optic radiation**.

**One error shape recurs across the set and is worth naming: a file asserting what another file
contains, on the strength of that file's title.** Files 7, 10 and 15 each asserted that file 18
covered a tract — the middle longitudinal fasciculus, the cerebellar peduncles, the corticobulbar
tract — when that file only **mentioned** it, and none of the three had opened it. It is the
cross-file version of the defect §8 catches with a superseded copy: **a record that passes every check
that can be run on it alone.**

**And the inventory runs the other way — tracts with a stated function and no declared traffic at either
end.** The **anterior commissure**, the **posterior commissure**, and the **inferior fronto-occipital
fasciculus**: all three are described in file 18, all three have a stated function, and **no entry
anywhere declares an edge routed through any of them**. This is the **mirror of a dangling endpoint**
and it fails just as silently, because the entry reads as complete on its own. Two of the three are
commissures bundled into the corpus callosum entry, which is itself recorded there as **four tracts in
one entry**; the arcuate entry is recorded as **five**. Both bundlings are marked owed on their entries.
