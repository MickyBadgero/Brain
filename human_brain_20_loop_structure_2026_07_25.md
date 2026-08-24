# Human Brain — Description and Data Flow
**Author:** Micky Badgero
**Date:** 2026-07-25
---

---

# FILE 20 OF 20 — LOOP STRUCTURE

**What is in this file.** Synthesis prose, not entries. How the loops close and re-enter, and which of them the source can and cannot follow around.

**Size:** 139 non-blank lines, ~3.4k tokens / 14 kB. **Entries:** 0.

**This file is one section of the source. Edges cross into other files; an endpoint named here that has no entry here lives in another file. Do not treat a missing endpoint as a missing region without checking the other files.**

**This file carries no entries, so it carries no entry pass stamps, and the header block that would be generated from them is empty.** One file-level stamp stands in its place, at the foot of the file. **Whether a synthesis file should carry a file-level stamp at all is open.**

---

# LOOP STRUCTURE (synthesis — how the loops close and re-enter)

*Like cross-modal integration, this is a synthesis rather than new tissue: it gathers the re-entrant
loops the other files already trace and makes their shared structure explicit. It adds no region and no
number and carries no slot template. The structural fact it records is that the brain's pathways are
not one-way feedforward chains that run to a final stage — **every major pathway in this map closes back
on itself**. Activity re-enters the same circuit continuously, offset by conduction and synaptic delay,
while fresh input keeps arriving on the same path; the feedback arms already drawn in each file **are**
that re-entrant channel, so nothing new needs tracing. There is no terminating stage — continuous
re-entry with delay is the resting condition of the tissue.*

***What this file may claim about closure, and what it may not.*** *The list below used to be headed
"all already in the map," and the closing paragraph used to say that tracing the loops "surfaced no
missing region and no broken loop." **Checked joint by joint against all twenty files on 2026-07-25,
both statements are false.** Three of the eight loops pass through a stage the source does not
describe, and a fourth has a joint declared at one end only. **The structural claim survives intact** —
the loops do close in the brain, and the re-entrant architecture is the point of the file — but **a
loop this document can follow around and a loop it merely believes closes are different things**, and
the difference is now recorded on each loop rather than smoothed into a clean list. The all-clear was
the more comfortable statement, which is why it needed checking rather than repeating.*

**The loops that close, and the state of each joint in the map:**

- **Thalamo-cortical / cortico-thalamic** — every sensory relay (the lateral geniculate, medial
  geniculate and ventral posterior nuclei) and higher-order nucleus (mediodorsal, pulvinar, ventral
  anterior / ventral lateral) is reciprocally wired with its cortical area, and the descending
  cortico-thalamic projection outnumbers the ascending drive (primary visual cortex → lateral
  geniculate; primary auditory cortex → medial geniculate). The fastest loop, on the order of
  milliseconds. **Every joint has an entry** (files 1, 2, 5, 12). **The one qualification the map now
  carries**: of the corticothalamic fibres traversing the internal capsule, only about three quarters
  were found to give visible collaterals into the thalamic reticular nucleus, so the descending arm is
  not a uniform bundle at that level.
- **Cortico-cortical feedback** — each sensory hierarchy is bidirectional (primary visual cortex ↔ V2 ↔
  V4 ↔ inferotemporal cortex; auditory core ↔ belt ↔ parabelt ↔ superior temporal gyrus; primary
  somatosensory ↔ secondary somatosensory ↔ parietal cortex), the feedback arm shaping the lower stage.
  **Every joint has an entry** (files 1, 2, 5, 6).
- **Cortico-basal-ganglia-thalamo-cortical** — cortex → striatum → (direct / indirect / hyperdirect) →
  internal globus pallidus and substantia nigra pars reticulata → ventral anterior / ventral lateral
  thalamus → cortex: the action-selection loop. **The dorsal loop's joints all have entries** (files 5,
  9, 11, 12). **The limbic variant does not close cleanly in the map:** ventral striatum → ventral
  pallidum → mediodorsal thalamus → prefrontal cortex, where the **ventral pallidum → mediodorsal**
  joint is declared at the producer's end only — that entry (file 9) records the consumer as naming a
  pallidal source and naming the **dorsal** nuclei only, and marks the edit owed at file 12. **The two
  candidate sources carry different payloads**, which is why the open joint matters here more than a
  missing line usually would: tonic inhibition alone from the dorsal nuclei, against inhibition **plus
  a computed relative value** from the ventral pallidum, which that entry records as computing value
  rather than relaying it. **A loop whose gain stage might or might not be inside it is not yet a
  traced loop.**
- **Cerebro-cerebellar** — cortex → pontine nuclei → cerebellar cortex → deep cerebellar nuclei →
  ventral lateral / ventral anterior thalamus → cortex, crossed at both the corticopontine and the
  dentatothalamic limb. **This loop passes through two stages the source does not describe.** The
  **pontine nuclei** have no entry in any of the twenty files, and neither does the **red nucleus**,
  which carries the other cerebellar efferent limb; both are named on edges in file 10 and are standing
  items. **The pontine gap is the load-bearing one**: the corticopontine stage is recorded elsewhere in
  the source as a **processing stage rather than a relay** — corticopontine divergence followed by
  pontocerebellar convergence, with an origin population that excludes large parts of prefrontal and
  temporal cortex — so a region that **transforms the payload** sits inside this loop with no slot to
  record the transform. **The loop cannot be followed around in this document.** A third limb this list
  does not name also belongs to the system: the **inferior olive**, the climbing-fibre source, which
  does have an entry (file 10); whether its own re-entrant arm closes is **not established here** and
  is owed.
- **Hippocampal / Papez** — entorhinal cortex → dentate gyrus → *cornu Ammonis* field 3 → *cornu
  Ammonis* field 1 → subiculum → fornix → mammillary bodies → anterior thalamus → cingulate and
  retrosplenial cortex → entorhinal cortex, with the ***cornu Ammonis* field 3 recurrent
  autoassociator** nested inside it as a tight local loop. **Most joints have entries** (files 8, 12,
  17, 18; the mammillary bodies as a named sub-element of the hypothalamus entry, file 14, whose
  mammillothalamic edge is two-ended). **Two joints are soft.** The return arm from retrosplenial
  cortex to entorhinal cortex runs **via parahippocampal cortex, which has no entry in any of the
  twenty files** and is named as a producer by four files. And the **anterior thalamus → cingulate**
  limb is declared at the thalamic end and **not** at the cortical one: that entry (file 12) records
  the anterior cingulate consumer as declaring a midline / intralaminar thalamic input and not this
  one, and the posterior cingulate as not declaring this input either. **So the classical cingulate
  target of the Papez circuit is unconfirmed at its consumers**, while the retrosplenial target is
  two-ended.
- **Oculomotor** — the lateral intraparietal area ↔ the frontal eye fields ↔ the superior colliculus:
  the saccade and attention loop, released by disinhibition from the substantia nigra pars reticulata.
  **Those joints have entries** (files 4, 11, 14), and the motor arm beyond them is now described as
  well — superior colliculus → the saccade burst generators → the ocular motor nuclei → the extraocular
  muscles (files 14, 15), where the payload change is typed as **spatial to temporal**, a place code in
  and a timed burst out. **The return arm is where this loop is open.** Three separate entries consume
  an **eye-position or efference-copy signal** and **no region in the source produces it**; the
  source's own inventory of unnamed sources records that three of its four items are the same missing
  signal, wanted independently by three consumers. **That is one region to find, not three, and until
  it is found the oculomotor loop has a described forward path and an undescribed return.**
- **Value / aversion** — the mesolimbic dopamine loop (ventral tegmental area → ventral striatum →
  ventral pallidum → back toward the ventral tegmental area) with its opponent brake, lateral habenula
  → rostromedial tegmental nucleus → ventral tegmental area and substantia nigra pars compacta.
  **Every joint now has an entry.** The rostromedial tegmental nucleus was for a long time named on
  four files' edges with no slot anywhere — the sign-inverting stage without which there is no route
  from the habenula's excitatory output to a *decrease* in dopamine — and it now has an entry (file
  14), with both of its dopaminergic outputs confirmed two-ended. **The brake limb of this loop is
  therefore traceable end to end**, which is not true of the mesolimbic limb itself: the ventral
  pallidum → ventral tegmental area joint is declared at the producer's end only, and its consumer
  entry (file 13) names other sources and not that one.
- **Circadian** — suprachiasmatic nucleus → paraventricular nucleus → intermediolateral cell column of
  the spinal cord → superior cervical ganglion → pineal gland → melatonin → back onto the
  suprachiasmatic nucleus. The slowest loop, about twenty-four hours. **This is the one loop in the
  list that does not close over axons.** Its return limb is **melatonin in the bloodstream** — the
  pineal entry types it as an endocrine terminal with a separate suprachiasmatic feedback arm, not as a
  projection — and one of its forward joints, the **superior cervical ganglion**, is a peripheral
  ganglion that transduces nothing and is therefore outside the source's scope by rule. **So the
  circadian loop is closed in the body and not closable in this document**, and that is a statement
  about the source's boundary rather than a gap in it.

**Where the loops branch and are gated:** the thalamic gates — the thalamic reticular nucleus's
inhibitory shell and the subthalamic zona incerta acting on the higher-order thalamus (file 12);
**basal-ganglia disinhibition**, where a pause in the tonic firing of the substantia nigra pars
reticulata or the internal globus pallidus releases the thalamic or collicular target, and where the
informative event is a **cessation** rather than a signal (files 9 and 14, two-ended and agreeing on
that point); the **attentional priority maps** in the lateral intraparietal area and the superior
colliculus, ranking locations for the next orienting movement; and **neuromodulatory gain** — the
acetylcholine, norepinephrine, serotonin, and dopamine systems setting how strongly a loop responds
without carrying its content (file 13).

**Nested timescales:** the loops span a hierarchy — from the millisecond-order thalamo-cortical and
cortico-cortical loops, through the intermediate basal-ganglia and cerebro-cerebellar loops, to the
slow hippocampal / consolidation and value-learning loops, out to the twenty-four-hour circadian loop.
The fast loops run **inside** the slow ones: many thalamo-cortical cycles complete within one
basal-ganglia selection, many selections within one circadian cycle, and none of them comes to rest at
an endpoint. **The span is not merely wide, it is ten orders of magnitude** — a millisecond against a
day — and the slowest loop is also the only one whose closing limb is chemical rather than axonal,
which may be the same fact twice.

**Honest boundary:** this synthesis is *structural*, not *quantitative*. Pinning the loops' actual
latencies — thalamo-cortical conduction, cortico-cortical delay, the circadian period — is a separate
literature effort, and loop latency is **not** one of the per-region number slots this document keeps,
so, as with cross-modal integration, the loop structure is recorded here as data flow rather than as
new numbers. **What tracing it does surface, stated positively rather than as an all-clear:** the
re-entrant architecture holds everywhere it was checked, and the incomplete joints cluster — three of
the four soft ones (pontine nuclei, red nucleus, parahippocampal cortex) are **regions named on edges
with no entry**, and the fourth (the eye-position signal) is a **producer nobody has named at all**.
**Those are the same defect class in four places, not four separate problems**, and they are all
recorded on the entries whose edges dangle, which is where the repair belongs.

- **Pass:** 2026-07-25 — abbreviations expanded to full names, including the burned-in hippocampal field names and a within-file collision on one letter-string; every loop's joints checked against all twenty files and the state of each recorded; the claim that all joints were in the map and the closing all-clear both corrected, three loops found to pass through undescribed stages and two more to have one-ended joints; the rostromedial tegmental nucleus's new entry recorded as closing the aversion brake end to end; the circadian loop recorded as the one that does not close over axons; free-text pass state removed; one file-level stamp used in place of the empty entry-stamp block

---

