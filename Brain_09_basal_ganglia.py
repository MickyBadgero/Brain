"""Brain — basal ganglia: the action-selection / value loop, and the ventral pallidum.

Two entries. The first is a bundle of six nuclei under one heading — striatum,
external and internal globus pallidus, subthalamic nucleus, substantia nigra pars
compacta and pars reticulata. The second, the ventral pallidum, is the ventral
counterpart of two of those six and is a peer entry rather than a sub-element.

Counting basis is mixed and is not per hemisphere. The basal ganglia is reported
whole - both hemispheres - with the per-side value alongside; the ventral pallidum
has no count at all. A section total across mixed bases is labelled mixed.

Two things in this section are findings against the forward model rather than gaps
in the description, and both are recorded here rather than worked around.

The first is sign. Every edge in this structure's mechanism is inhibitory or
disinhibitory: the direct pathway inhibits the output nuclei, which disinhibits the
thalamus; the output nuclei fire tonically and the selected action is the one whose
inhibition pauses. A threshold gate is a count of active inputs compared against a
stored threshold, and a count has no term for sign. So the model cannot express
this section's operation at all - not missing a parameter, but having no term for
the thing. In 01_visual_pathway the outer retina raises the same shape as a property
of one stage; here it is the whole mechanism.

The second is polarity of the activity bit. Everywhere else `active` set means the
line is carrying its signal. On this structure's outputs the informative event is a
cessation - the tonic firing pausing - so a reader taking `active` as the signal
reads the output exactly backwards.

Neither is repaired here. Extending or replacing the threshold-gate model is not
this rung's decision.

This file carries no history: no versions, no provenance, no "changed since", no
reference to sessions or prior files, no changelog, no "formerly", no commented-out
prior version. Comments explain only the functional basis (biological), Euler order,
and compute/memory tradeoffs.

A cross-file endpoint carries the far file's stem, <nn>_<section>. An endpoint
written "file NN" instead is one whose far file is unchecked against this section;
it is not a claim that no far end exists.

Every edge latency reads None, meaning to derive. There is not one timing figure in
the section, and the section's mechanism is a race: the hyperdirect stop must reach
the output nuclei before the direct pathway's go. A race with no times is not a race.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import ceil, log2

# --------------------------------------------------------------------------
# Count states.
#
# Kept distinct because each names a different repair. ORDER_ONLY is a bound rather
# than a number: turning an order of magnitude into a range shows how much is riding
# on it.
# --------------------------------------------------------------------------

COUNTED = "counted"
ORDER_ONLY = "order of magnitude only"
RESIDUAL = "no count of its own; exists only as the residual of a headline"
OWED = "owed"
UNKNOWN = "unknown"
NOT_APPLICABLE = "not applicable"

# Sign on an edge. The model has no term for this; recording it is how the gap
# stays visible instead of being flattened away.
EXCITES = "+"
INHIBITS = "-"
DISINHIBITS = "--"          # inhibition of an inhibitor: net facilitation
SIGN_UNSTATED = "?"


@dataclass(frozen=True)
class SubElement:
    name: str
    count: int | None = None            # a point count where one exists
    count_lo: int | None = None         # the ends of a stated order of magnitude
    count_hi: int | None = None
    state: str = COUNTED
    basis: str = "per hemisphere"
    fan_in: int | None = None
    note: str = ""
    emits_external: bool = False        # does an inter-region edge leave from here

    def bits(self) -> int:
        """Stored bits per neuron under the threshold-gate model."""
        if self.fan_in is None:
            return 16                   # log2 ceiling: any fan-in under ~65,000 fits
        return 0 if self.fan_in <= 1 else ceil(log2(self.fan_in))

    def bytes_range(self) -> tuple[int, int] | None:
        lo = self.count if self.count is not None else self.count_lo
        hi = self.count if self.count is not None else self.count_hi
        if lo is None or hi is None:
            return None
        return (lo * self.bits() // 8, hi * self.bits() // 8)


@dataclass(frozen=True)
class Structure:
    name: str
    shape_class: str
    subelements: tuple[SubElement, ...]
    basis: str
    headline_count: int | None = None
    headline_basis: str = ""
    bundled: bool = False
    bundle_note: str = ""
    volume_cm3: tuple[float, ...] = ()
    volume_note: str = ""

    def counted(self) -> tuple[SubElement, ...]:
        return tuple(s for s in self.subelements if s.state == COUNTED)

    def uncounted(self) -> tuple[SubElement, ...]:
        return tuple(s for s in self.subelements if s.state != COUNTED)


# The bundle. Six nuclei under one heading, carried as a bundle because the source
# names the six and in the same slot records that whether they should be six
# entries rather than six sub-elements is unsettled. Splitting here would answer a
# question the source holds open.
BASAL_GANGLIA = Structure(
    "basal ganglia",
    "non-laminated nucleus, rank 2: (cell class, N); the striatum additionally "
    "carries a named sector axis with no extent",
    (
        SubElement("striatum (caudate, putamen, nucleus accumbens)",
                   state=RESIDUAL,
                   note="the large majority of the headline; medium spiny neurons "
                        "are 85-95% of it, D1 and D2 roughly equal"),
        SubElement("external globus pallidus",
                   count_lo=100_000, count_hi=900_000, state=ORDER_ONLY,
                   note="'hundreds of thousands', Hardman stereology lineage"),
        SubElement("internal globus pallidus",
                   count_lo=100_000, count_hi=900_000, state=ORDER_ONLY,
                   emits_external=True,
                   note="'hundreds of thousands'; every output edge of this entry "
                        "leaves from here or the pars reticulata"),
        SubElement("subthalamic nucleus",
                   count=560_000, state=COUNTED,
                   note="human standard figure; cross-species ladder ~5,400 mouse / "
                        "~25,000 rat / ~155,000 macaque / ~560,000 human; "
                        "predominantly glutamatergic"),
        SubElement("substantia nigra pars compacta",
                   count_lo=400_000, count_hi=500_000, state=COUNTED,
                   note="dopaminergic cells, per side; ~0.9-1.0M bilateral; verified "
                        "- the population lost in Parkinson's disease"),
        SubElement("substantia nigra pars reticulata",
                   count_lo=100_000, count_hi=900_000, state=ORDER_ONLY,
                   emits_external=True,
                   note="'hundreds of thousands'"),
    ),
    basis="whole - both hemispheres, per-side alongside",
    headline_count=200_000_000,
    headline_basis="both hemispheres, stated as a lower bound (>200M)",
    bundled=True,
    bundle_note="six nuclei under one heading. The source names the six and records "
                "that whether they should be six entries rather than six "
                "sub-elements is unsettled. Recorded as a bundle whose split is "
                "owed at the source; not split here.",
    volume_cm3=(8.0, 10.0, 12.0),
    volume_note="striatum, the largest subcortical grey structure; ~5 cm3 per "
                "hemisphere, soft. The pallidum, subthalamic nucleus and substantia "
                "nigra have soft per-nucleus volumes and are not covered.",
)

VENTRAL_PALLIDUM = Structure(
    "ventral pallidum",
    "non-laminated nucleus, rank 2: (cell class, N)",
    (
        SubElement("posterior pole (opioid hedonic hotspot)", state=OWED,
                   note="a sub-element by the data-flow test: the Function field "
                        "assigns it a payload the rest does not carry. Owed whether "
                        "the anterior/posterior division is a boundary or a gradient"),
        SubElement("the remainder", state=OWED,
                   note="undivided here, and unnamed"),
        SubElement("cell classes", state=UNKNOWN,
                   note="GABAergic disinhibition and mu-opioid receptors are named "
                        "without saying whether they are separable populations"),
    ),
    basis="per hemisphere",
    headline_count=None,
    volume_cm3=(),
    volume_note="small, sub-cm3; no verified human figure recorded",
)

STRUCTURES = (BASAL_GANGLIA, VENTRAL_PALLIDUM)

# --------------------------------------------------------------------------
# The boundary problem, made mechanical.
#
# The dangling-edge diff collects every structure named on an edge and diffs it
# against the set of structures with entries. It catches a name with no entry. It
# does not catch one functional stage carrying two names at two levels of the
# hierarchy, which is what this file has: the ventral pallidum is a peer entry and
# is also the ventral counterpart of two sub-elements of the other entry.
#
# The check below is the analogue of the dangling-edge diff for that failure mode.
# --------------------------------------------------------------------------

LEVEL_COLLISIONS = (
    ("ventral pallidum", ("internal globus pallidus",
                          "substantia nigra pars reticulata"),
     "the ventral counterpart of these two, carried as a peer entry while they are "
     "sub-elements. Three cross-file edges are attributed at their far ends to the "
     "dorsal nuclei and claimed here by the ventral structure, and the two "
     "candidate sources do not carry the same payload."),
)


def level_collision_check() -> str:
    """Report structures that exist at two levels of the hierarchy at once."""
    entries = {s.name for s in STRUCTURES}
    subs = {e.name for s in STRUCTURES for e in s.subelements}
    out = []
    for peer, counterparts, why in LEVEL_COLLISIONS:
        assert peer in entries
        present = [c for c in counterparts if c in subs]
        out.append(f"  '{peer}' is an entry; its counterparts "
                   f"{present} are sub-elements of another entry.")
        out.append(f"    {why}")
    out.append("  The dangling-edge diff cannot find this: both names resolve, so "
               "nothing dangles.")
    out.append("  Owed at the source: decide whether the ventral loop is a "
               "sub-element set or a peer, and make the far ends match.")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Edges.
#
# `sign` is recorded even though the forward operation has no term for it. The
# alternative is to drop it, which would flatten the section's entire mechanism.
#
# `latency_s` is real time in seconds and is None on every edge. Never steps: a
# latency stated in steps has assumed a clock.
# --------------------------------------------------------------------------

NAMED = "named without units, range or frame"
PARTIAL = "one component named, the rest owed"
PAYLOAD_OWED = "owed"
TYPED_NEGATIVE = "typed, and the informative event is a cessation"


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    source_sub: str | None = None
    target_sub: str | None = None
    sign: str = SIGN_UNSTATED
    latency_s: float | None = None
    far_end_file: str = ""
    far_end_state: str = ""
    payload_state: str = PAYLOAD_OWED
    carries: str = ""
    internal: bool = False
    pathways: tuple[str, ...] = ()


BG, VP = "basal ganglia", "ventral pallidum"

# Internal edges: the three canonical pathways plus the training signal.
# Note that the indirect and hyperdirect pathways SHARE their final limb, so a
# count of pathways and a count of edges give different numbers.
INTERNAL_EDGES: tuple[Edge, ...] = (
    Edge(BG, BG, "D1 medium spiny neurons", "internal globus pallidus", INHIBITS,
         None, "", "", NAMED,
         "inhibition of the output nuclei, which disinhibits the thalamus and so "
         "facilitates the selected action", True, ("direct",)),
    Edge(BG, BG, "D1 medium spiny neurons", "substantia nigra pars reticulata", INHIBITS,
         None, "", "", NAMED, "as above", True, ("direct",)),

    Edge(BG, BG, "D2 medium spiny neurons", "external globus pallidus", INHIBITS,
         None, "", "", NAMED,
         "first of three transfers whose signs alternate; the net sign of the "
         "pathway is a product across them, not a property of it", True, ("indirect",)),
    Edge(BG, BG, "external globus pallidus", "subthalamic nucleus", INHIBITS,
         None, "", "", NAMED, "second transfer", True, ("indirect",)),
    # Shared limb: the indirect pathway's third transfer and the hyperdirect
    # pathway's second half are the same two edges.
    Edge(BG, BG, "subthalamic nucleus", "internal globus pallidus", EXCITES,
         None, "", "", NAMED,
         "third transfer of the indirect pathway and second half of the "
         "hyperdirect; net excitation of the output nuclei, which inhibits the "
         "thalamus and so suppresses competing actions", True,
         ("indirect", "hyperdirect")),
    Edge(BG, BG, "subthalamic nucleus", "substantia nigra pars reticulata", EXCITES,
         None, "", "", NAMED, "as above", True, ("indirect", "hyperdirect")),

    Edge(BG, BG, "substantia nigra pars compacta", "D1 medium spiny neurons", SIGN_UNSTATED,
         None, "", "", PARTIAL,
         "the reward-prediction error: a scalar, broadcast. One number, no content, "
         "no address - which is why it can train the whole array at once and why it "
         "cannot say what to do. Its sign on this class versus the other is the "
         "balance-setting mechanism and is owed", True, ("nigrostriatal",)),
    Edge(BG, BG, "substantia nigra pars compacta", "D2 medium spiny neurons", SIGN_UNSTATED,
         None, "", "", PARTIAL, "as above, with the opposite effect and the sign owed",
         True, ("nigrostriatal",)),
)

# The first half of the hyperdirect pathway is an inter-region edge the source's
# Inputs slot does not declare, because the cortical input line says the projection
# is mapped onto the striatum and this one bypasses the striatum. Recorded as owed
# at the source rather than written here: writing it would patch an inherited gap.
OWED_EDGES = (
    ("cortex", BG, "subthalamic nucleus",
     "the first half of the hyperdirect pathway. The cortical input line as worded "
     "excludes it. Owed at the source (09_basal_ganglia), not written here."),
    ("primary motor cortex", BG, "motor striatum",
     "the motor sector of the cortical input has no producer end at the one region "
     "the motor sector is named for. Owed at 05_sensorimotor_loop."),
)

EDGES: tuple[Edge, ...] = INTERNAL_EDGES + (
    # ---- basal ganglia, in ----
    Edge("nearly all of cortex", BG, None, "striatum", EXCITES, None, "many",
         "a class endpoint the source holds open as an unanswered question",
         NAMED,
         "the candidate actions: every action currently proposed by every cortical "
         "area, in parallel. The payload is a set of competitors, not a decision"),
    Edge("intralaminar nuclei of the thalamus", BG, None, "striatum", EXCITES, None, "file 12",
         "producer gives a sector split this end does not carry; owed here",
         PARTIAL, "arousal and a thalamostriatal drive parallel to cortex"),
    Edge("amygdala", BG, None, "striatum", SIGN_UNSTATED, None, "08_medial_temporal_lobe",
         "two-ended; this end is the fuller of the two", NAMED,
         "the valence tag - a gain on perception, attention and memory encoding, "
         "carrying no identity information of its own; onto the ventral striatum"),
    Edge("insula", BG, None, "striatum", SIGN_UNSTATED, None, "file 17",
         "two-ended, owed at both", PAYLOAD_OWED, "onto the ventral striatum"),
    Edge("orbitofrontal and ventromedial prefrontal cortex", BG, None, "striatum",
         SIGN_UNSTATED, None, "11_frontal_lobe", "producer names the ventral striatum specifically",
         PARTIAL, "value - the expected value of the options; untyped at the producer"),
    Edge("ventral tegmental area", BG, None, "striatum", SIGN_UNSTATED, None, "13_neuromodulatory_systems",
         "producer declares it and names this structure", PARTIAL,
         "dopamine carrying reward-prediction error, onto the nucleus accumbens; "
         "the mesolimbic limb, parallel to the pars compacta's nigrostriatal one"),
    Edge("lateral habenula", BG, None, "substantia nigra pars compacta", INHIBITS,
         None, "file 17", "producer's end only; the intermediate stage holds a full entry in "
         "14_brainstem_midbrain_hypothalamus, and this edge names it inside the "
         "endpoint rather than terminating on it",
         NAMED,
         "a negative reward-prediction error - the mirror image of the dopamine "
         "signal, delivered as inhibition of the dopamine cells, via the "
         "rostromedial tegmental nucleus"),
    Edge(VP, BG, None, "nucleus accumbens / ventral striatum",
         SIGN_UNSTATED, None, "",
         "the producer is the other entry in this file and declares it as the "
         "return limb of its own output line",
         PAYLOAD_OWED, ""),
    Edge(VP, BG, None, "subthalamic nucleus", SIGN_UNSTATED, None, "",
         "producer is the other entry in this file", PARTIAL,
         "the limbic-motor interface signal"),

    # ---- basal ganglia, out. All from the internal globus pallidus and/or the
    # pars reticulata, and all carrying the same negative payload.
    Edge(BG, "ventral anterior / ventral lateral thalamus", "internal globus pallidus",
         None, INHIBITS, None, "file 12", "consumer names both source nuclei, untyped there",
         TYPED_NEGATIVE,
         "tonic inhibition, selectively released. The output nuclei fire constantly "
         "and the selected action is the one whose inhibition pauses. Nothing here "
         "carries the action itself"),
    Edge(BG, "mediodorsal thalamus", "internal globus pallidus", None, INHIBITS,
         None, "file 12", "consumer's end only; typed there, which is why it can be typed here",
         TYPED_NEGATIVE, "the same, as a gate on which prefrontal loops may proceed"),
    Edge(BG, "superior colliculus", "substantia nigra pars reticulata", None, INHIBITS,
         None, "file 14", "two-ended and agreeing; consumer types it in the same terms",
         TYPED_NEGATIVE,
         "the same, released to permit a saccade; the gate on the lateral "
         "intraparietal area's priority map. Its informative event is a cessation"),
    Edge(BG, "lateral habenula", "internal globus pallidus", None, SIGN_UNSTATED,
         None, "file 17", "consumer's end only", PARTIAL,
         "the basal-ganglia 'no-reward' signal, in the consumer's terms"),
    Edge(BG, "ventral pallidum", "nucleus accumbens / ventral striatum", None, INHIBITS,
         None, "", "the consumer is the other entry in this file and declares it",
         NAMED, "the limbic loop's selection - which motivated action has been "
                "chosen; GABAergic, substance-P. The first output of this entry "
                "that does not leave from the internal globus pallidus or the pars "
                "reticulata"),
    Edge(BG, "ventral pallidum", "subthalamic nucleus", None, SIGN_UNSTATED,
         None, "", "the consumer is the other entry in this file and declares it",
         PAYLOAD_OWED, ""),
    Edge(BG, "thalamic reticular nucleus", "internal globus pallidus", None, INHIBITS,
         None, "file 12",
         "consumer records that whether these terminate there or on the relay "
         "nuclei directly is not distinguished and is owed",
         PAYLOAD_OWED,
         "GABAergic inhibition. If they terminate on the relay nuclei directly, "
         "this edge and the two thalamic edges above are one projection described twice"),

    # ---- ventral pallidum, in ----
    Edge("nucleus accumbens", VP, None, None, INHIBITS, None, "",
         "the producer is a sub-element of the other entry and declares it",
         NAMED, "the limbic loop's selection - which motivated action has been "
                "chosen; GABAergic, substance-P; the dominant input"),
    Edge("amygdala", VP, None, None, SIGN_UNSTATED, None, "08_medial_temporal_lobe",
         "producer declares it and names this structure", PARTIAL, "the valence tag"),
    Edge("hippocampal formation", VP, "subiculum", None, SIGN_UNSTATED, None, "08_medial_temporal_lobe",
         "producer declares it and names this structure", PARTIAL, "episodic context"),
    Edge("orbital and medial prefrontal cortex", VP, None, None, SIGN_UNSTATED, None, "11_frontal_lobe",
         "producer declares it on its own line, untyped there", PARTIAL,
         "value - the expected value of the options; includes infralimbic cortex, "
         "area 25, which the producer covers as an unnamed sub-element"),
    Edge("lateral hypothalamus", VP, None, None, SIGN_UNSTATED, None, "file 14",
         "the producer declares a class that covers this structure without naming it; owed there",
         PARTIAL, "need state"),
    Edge("ventral tegmental area", VP, None, None, SIGN_UNSTATED, None, "13_neuromodulatory_systems",
         "the producer declares no such edge; owed there or withdraw", PARTIAL,
         "prediction error"),
    Edge("lateral parabrachial nucleus", VP, None, None, SIGN_UNSTATED, None, "file 14",
         "the producer names a basal-forebrain class that may or may not include "
         "this structure; owed there", PAYLOAD_OWED, ""),
    Edge("subthalamic nucleus", VP, None, None, EXCITES, None, "",
         "the producer is a sub-element of the other entry and declares it",
         PAYLOAD_OWED, ""),

    # ---- ventral pallidum, out ----
    Edge(VP, "mediodorsal thalamus", None, None, INHIBITS, None, "12_thalamus",
         "two-ended: the consumer declares a separate limbic limb via this structure", PARTIAL,
         "released inhibition closing the limbic loop, and on the same cells a "
         "computed relative-value signal. Value is computed here, not passed"),
    Edge(VP, "ventral tegmental area", None, None, DISINHIBITS, None, "13_neuromodulatory_systems",
         "two-ended; the consumer states the termination this end does not", NAMED,
         "disinhibition of dopamine; the ventral-pallidum to ventral-tegmental-area "
         "to accumbens motivational limb"),
    Edge(VP, "lateral habenula", None, None, SIGN_UNSTATED, None, "17_insula_claustrum_habenula",
         "two-ended: the consumer declares this structure on its own line beside "
         "the dorsal pallidal source", PAYLOAD_OWED, ""),
    Edge(VP, "subthalamic nucleus", None, None, SIGN_UNSTATED, None, "",
         "the consumer is a sub-element of the other entry and declares it", PARTIAL,
         "the limbic-motor interface signal"),
    Edge(VP, "nucleus accumbens", None, None, SIGN_UNSTATED, None, "",
         "the consumer is a sub-element of the other entry and declares it", PARTIAL,
         "the limbic-motor interface signal, returning"),
)

SOURCE_EDGE_LINE_COUNT = 30      # the source counts bullets: 17 in, 13 out

# Endpoints the source names that are classes rather than structures. Three, in two
# different states.
UNRESOLVED_CLASS_ENDPOINTS = (
    ("nearly all of cortex", BG, "in",
     "HELD OPEN by the source as an unanswered question, not marked a defect: "
     "splitting would produce dozens of edges asserting one payload, and the claim "
     "the line makes - a convergence of nearly all cortex - may not be expressible "
     "as a list. Written as an edge, not split."),
    (BG, "the brainstem", "out",
     "a defect. The brainstem file was read at the source and no entry declares an "
     "input from this structure. Owed: name the target or withdraw. Not written."),
    (VP, "reticular and extrapyramidal motor systems", "out",
     "a defect. The reticular formation entry declares no input from this "
     "structure, and 'extrapyramidal motor systems' names no region at all. "
     "Owed: name the targets or withdraw. Not written."),
)

# Tracts named as carrying this section's edges. A tract is where the physical
# substrate of a latency lives, and none of the three has an entry anywhere.
TRACTS = (
    ("ansa lenticularis", "no entry in the white-matter file"),
    ("lenticular fasciculus", "no entry in the white-matter file"),
    ("nigrostriatal bundle", "no entry in the white-matter file"),
)

# --------------------------------------------------------------------------
# Forward operation, and the two places this section breaks it.
# --------------------------------------------------------------------------


def threshold_gate(active_counts, thresholds):
    """Fire where the count of active inputs reaches the stored threshold.

    Integer comparison only. No weights and no multiply, because equal weights
    reduce the dot product to a count; no gradient, because nothing here is
    differentiated.

    This is correct for every neuron in the sections worked so far and it does not
    express this one. See sign_problem() below.
    """
    if len(active_counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(active_counts, thresholds)]


def sign_problem() -> str:
    """The section's mechanism has a sign and the forward model has no term for it."""
    signed = [e for e in EDGES if e.sign in (INHIBITS, DISINHIBITS)]
    unstated = [e for e in EDGES if e.sign == SIGN_UNSTATED]
    excit = [e for e in EDGES if e.sign == EXCITES]
    return (
        f"  edges carrying inhibition or disinhibition: {len(signed)} of {len(EDGES)}\n"
        f"  edges carrying excitation:                   {len(excit)}\n"
        f"  edges whose sign the source does not state:  {len(unstated)}\n"
        "\n"
        "  count[j] = sum of active inputs; active[j] = count[j] >= threshold[j].\n"
        "  A count has no term for sign. An inhibitory input cannot subtract from a\n"
        "  count of active inputs, so the direct pathway - which selects an action by\n"
        "  inhibiting an inhibitor - is not expressible.\n"
        "\n"
        "  This is not a missing parameter. It is a finding against the model, of the\n"
        "  same class the design file records for graded weights: a structure the\n"
        "  source describes as computing by inhibition is a finding, not a structure to\n"
        "  be flattened to fit. The outer retina raised the same problem as a property\n"
        "  of one stage; here it is the whole mechanism.\n"
        "\n"
        "  Extending or replacing the model is not this rung's decision."
    )


def polarity_problem() -> str:
    """The activity bit means the opposite thing on this structure's outputs."""
    neg = [e for e in EDGES if e.payload_state == TYPED_NEGATIVE]
    return (
        f"  output edges whose informative event is a cessation: {len(neg)}\n"
        "  Everywhere else `active` set means the line is carrying its signal. The\n"
        "  output nuclei fire tonically and the selected action is the one whose\n"
        "  inhibition pauses, so on these edges the informative event is `active`\n"
        "  going clear. A consumer that expects a positive command on this edge has\n"
        "  misread the structure, and so would a reader of the activity array.\n"
        "  Recorded rather than repaired: the representation convention is not this\n"
        "  rung's to set."
    )


def allocate(structure: Structure, subelement: str):
    """Size the threshold and activity arrays for one sub-element.

    This regresses against the previous section, and it regresses in the least
    convenient place. Two of this bundle's six nuclei have a count and neither is on
    an output edge; every output leaves from a nucleus whose count is an order of
    magnitude. So allocation is blocked precisely at the emitting sub-elements.
    """
    for s in structure.subelements:
        if s.name == subelement:
            rng = s.bytes_range()
            if rng is None:
                raise NotImplementedError(
                    f"{structure.name} / {subelement}: no count. State is "
                    f"'{s.state}'. {s.note}"
                )
            lo, hi = rng
            if s.state == ORDER_ONLY:
                raise NotImplementedError(
                    f"{structure.name} / {subelement}: '{s.state}'. The stated order "
                    f"spans {s.count_lo:,} to {s.count_hi:,}, a factor of "
                    f"{s.count_hi/s.count_lo:.0f}, giving {lo/1e6:.2f}-{hi/1e6:.2f} MB. "
                    f"An order of magnitude is a bound, not a number, and allocating "
                    f"against either end would pick one."
                    + ("  This sub-element is on an output edge."
                       if s.emits_external else "")
                )
            n_lo = s.count if s.count is not None else s.count_lo
            n_hi = s.count if s.count is not None else s.count_hi
            return {
                "neurons": (n_lo, n_hi),
                "basis": s.basis,
                "threshold_bits": s.bits(),
                "threshold_bytes": (lo, hi),
                "active_bytes": (n_lo // 8, n_hi // 8),
                "fillable": False,
                "why_not_fillable": "connection topology is unset; the array can be "
                                    "sized and not populated",
            }
    raise ValueError(f"{subelement!r} is not a sub-element of {structure.name}")


def fan_in_map(structure: Structure):
    """Which source lines converge on each neuron.

    Not implementable, and this section states the convergence as its mechanism
    while leaving every fan slot unknown. Something over 100M striatal cells per
    side reduce onto output nuclei of order 10^5 per side, and the source says that
    ratio IS the selection - the arithmetic the competition has to perform.

    So the one number the mechanism rests on is open across a factor of nine,
    because the denominator is an order of magnitude rather than a count.
    """
    raise NotImplementedError(
        "connection topology is not set; the section states its convergence ratio "
        "as the mechanism and every fan-in and fan-out slot reads unknown"
    )


def select(*args, **kwargs):
    """The competition that reduces the candidate set to one.

    Candidate actions arrive in parallel; tonic inhibition leaves, selectively
    released. The step between has no edge. The lateral interactions within the
    striatum and the subthalamic nucleus's role in the global stop are the obvious
    substrates and neither is typed.

    This is the seventh entry in the source whose stated function has no declared
    internal substrate. It is not this rung's to invent.
    """
    raise NotImplementedError(
        "the selection step has no declared internal substrate: candidate actions "
        "arrive and a released inhibition leaves, and no edge says what reduces the "
        "set to one"
    )


def step(*args, **kwargs):
    """There is no step, and here the absence removes the mechanism rather than deferring it.

    Every edge has a nonzero, finite, heterogeneous latency in real time, and there
    is no global clock in the described system to replace them with. A loop with
    real heterogeneous delays settles by its own dynamics; the same loop broken by
    registers becomes an iterated map whose trajectory depends on the update rate.

    This section's function is a race. The hyperdirect pathway is a fast global stop
    whose speed is structural - it reaches the subthalamic nucleus from cortex
    directly, bypassing the striatum, so it traverses fewer stages than the direct or
    indirect routes. Which of the three arrives first at the output nuclei decides
    whether an action proceeds. A stop that arrives after the go it was meant to
    cancel is not a stop.

    Under a uniform step the three pathways would arrive in an order set by their
    stage counts alone, which is a different system from one whose ordering is set by
    conduction and synaptic delay. Here that substitution does not merely approximate
    the mechanism, it supplies it - the answer would be an artifact of the step.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; "
        "every edge latency in this section reads 'to derive', and the section's "
        "mechanism is a race between three pathways with no time on any of them"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    As with CA3, this is the section where the absence removes a declared function
    rather than leaving it unimproved. The nigrostriatal edge carries a
    reward-prediction error whose entire purpose is to train the loop, and the
    Function field names reinforcement learning as half of what this structure does.
    A structure whose thresholds are never written does not learn from a prediction
    error.

    Worse than at CA3 in one respect: the signal is present and typed. The scalar is
    described, its broadcast character is described, and its opposite signs on the
    two cell classes are named as the balance-setting mechanism. What is missing is
    only the rule that consumes it.
    """
    raise NotImplementedError(
        "no learning rule is set; the reward-prediction error on the nigrostriatal "
        "edge is described in full and there is nothing to consume it"
    )


# --------------------------------------------------------------------------
# Derived sizing — independent recomputation, not transcription.
# --------------------------------------------------------------------------


def residual_report() -> str:
    """How much of the headline is striatum, given what the other nuclei hold."""
    per_side = BASAL_GANGLIA.headline_count / 2
    lo = hi = 0
    for s in BASAL_GANGLIA.subelements:
        if s.state == RESIDUAL:
            continue
        a = s.count if s.count is not None else s.count_lo
        b = s.count if s.count is not None else s.count_hi
        lo += a
        hi += b
    out = [f"  headline: >{BASAL_GANGLIA.headline_count/1e6:.0f}M "
           f"({BASAL_GANGLIA.headline_basis}) -> >{per_side/1e6:.0f}M per side",
           f"  the five non-striatal nuclei, summed across their stated ranges: "
           f"{lo/1e6:.2f}M to {hi/1e6:.2f}M per side",
           f"  so the striatum is {(per_side-hi)/1e6:.2f}M to {(per_side-lo)/1e6:.2f}M "
           f"= {100*(per_side-hi)/per_side:.1f}% to {100*(per_side-lo)/per_side:.1f}% "
           f"of the count",
           "  The headline is a striatal count wearing the whole structure's name."]
    return "\n".join(out)


def convergence_report() -> str:
    per_side = BASAL_GANGLIA.headline_count / 2
    out = ["  the source states this ratio IS the selection - the arithmetic the "
           "competition has to perform:"]
    for o in (100_000, 500_000, 900_000):
        out.append(f"    >{per_side/1e6:.0f}M striatal per side onto output nuclei of "
                   f"{o:,} per side -> {per_side/o:,.0f}:1")
    out.append("  a factor of nine in the ratio, inherited entirely from the "
               "output nuclei being an order rather than a count.")
    return "\n".join(out)


def sizing_report() -> str:
    lines = [f"{'structure / sub-element':50} {'neurons':>24} {'bits':>5} {'store':>20}"]
    for s in STRUCTURES:
        for e in s.subelements:
            rng = e.bytes_range()
            if rng is None:
                lines.append(f"{s.name + ' / ' + e.name:50} {e.state:>24} {'-':>5} "
                             f"{'to derive':>20}")
                continue
            lo, hi = rng
            n = (f"{e.count:,}" if e.count is not None
                 else f"{e.count_lo:,}-{e.count_hi:,}")
            store = (f"{lo/1e6:.2f} MB" if lo == hi
                     else f"{lo/1e6:.2f}-{hi/1e6:.2f} MB")
            lines.append(f"{s.name + ' / ' + e.name:50} {n:>24} {e.bits():>5} {store:>20}")
    h = BASAL_GANGLIA.headline_count
    lines.append("")
    lines.append(f"headline store: {h*16/8/1e6:,.0f} MB whole (both hemispheres), "
                 f"{h/2*16/8/1e6:,.0f} MB per side")
    lines.append("a ceiling on the counted part - fan-in is absent, so 16 bits is the")
    lines.append("log2 cap - and a floor on the section, since the ventral pallidum has")
    lines.append("no count and four of the bundle's six nuclei have none either.")
    lines.append("BASIS IS MIXED. The section total is not one number.")
    return "\n".join(lines)


def fan_in_sensitivity() -> str:
    h = BASAL_GANGLIA.headline_count
    out = ["  fan-in     bits    whole-structure store"]
    for f in (1_000, 10_000, 30_000):
        b = ceil(log2(f))
        out.append(f"  {f:>6}   {b:>4}     {h*b/8/1e6:>8,.0f} MB")
    out.append(f"  unknown     16     {h*16/8/1e6:>8,.0f} MB   (the log2 ceiling)")
    out.append("  the count is the sensitive term and the fan-in is not.")
    return "\n".join(out)


def density_cross_check() -> str:
    h = BASAL_GANGLIA.headline_count
    out = [f"  {BASAL_GANGLIA.volume_note}"]
    for v in BASAL_GANGLIA.volume_cm3:
        out.append(f"    >{h/1e6:.0f}M / {v:.1f} cm3 -> {h/(v*1000):9,.0f} /mm3")
    out.append("  the cross-check covers the striatum and nothing else, which is")
    out.append("  consistent: the striatum is where nearly all the neurons are.")
    out.append(f"  {VENTRAL_PALLIDUM.name}: {VENTRAL_PALLIDUM.volume_note} "
               f"- no cross-check can be run")
    return "\n".join(out)


def cross_species_check() -> str:
    """The one figure in the section with an independent check."""
    ladder = (("mouse", 5_400), ("rat", 25_000), ("macaque", 155_000), ("human", 560_000))
    out = ["  subthalamic nucleus across species:"]
    prev = None
    for k, v in ladder:
        step_ = f"   x{v/prev:.2f}" if prev else ""
        out.append(f"    {k:8} {v:>8,}{step_}")
        prev = v
    out.append(f"  human/macaque = {560_000/155_000:.2f}  (source states ~3.6x) - holds")
    return "\n".join(out)


def edge_report() -> str:
    internal = [e for e in EDGES if e.internal]
    external = [e for e in EDGES if not e.internal]
    stated = [e for e in EDGES if e.latency_s is not None]
    out = [f"  edges: {len(EDGES)}  ({len(external)} between structures, "
           f"{len(internal)} inside one structure)",
           f"  the source counts {SOURCE_EDGE_LINE_COUNT} bullets, 17 in and 13 out",
           f"  reconciliation: {SOURCE_EDGE_LINE_COUNT} bullets "
           f"- {len([c for c in UNRESOLVED_CLASS_ENDPOINTS if c[2] == 'out'])} "
           f"unwritten class endpoints + 1 compound bullet naming two targets = "
           f"{SOURCE_EDGE_LINE_COUNT - len([c for c in UNRESOLVED_CLASS_ENDPOINTS if c[2] == 'out']) + 1}"
           f"   [{'matches' if len(external) == SOURCE_EDGE_LINE_COUNT - len([c for c in UNRESOLVED_CLASS_ENDPOINTS if c[2] == 'out']) + 1 else 'DOES NOT MATCH'}]",
           f"  with a stated latency: {len(stated)}    to derive: {len(EDGES)-len(stated)}"]
    for state in (NAMED, PARTIAL, PAYLOAD_OWED, TYPED_NEGATIVE):
        n = len([e for e in EDGES if e.payload_state == state])
        out.append(f"  payloads {state}: {n}")
    # pathways vs edges: the indirect and hyperdirect share their final limb
    paths = sorted({p for e in EDGES for p in e.pathways})
    out.append(f"  named internal pathways: {len(paths)} ({', '.join(paths)})")
    shared = [e for e in EDGES if len(e.pathways) > 1]
    out.append(f"  edges carried by more than one pathway: {len(shared)} - "
               f"a count of pathways and a count of edges give different numbers")
    out.append("  endpoints that are classes:")
    for a, b, d, why in UNRESOLVED_CLASS_ENDPOINTS:
        out.append(f"    [{d}] {a} -> {b}")
        out.append(f"        {why}")
    out.append("  edges the source identifies as owed and that are NOT written here:")
    for src, tgt, sub, why in OWED_EDGES:
        out.append(f"    {src} -> {tgt}" + (f" ({sub})" if sub else ""))
        out.append(f"        {why}")
    out.append("  tracts named as carrying these edges, none with an entry anywhere:")
    for t, note in TRACTS:
        out.append(f"    {t} - {note}")
    return "\n".join(out)


if __name__ == "__main__":
    print("bundle:")
    print(f"  {BASAL_GANGLIA.bundle_note}")
    print()
    print("boundary check (the dangling-edge diff cannot find this):")
    print(level_collision_check())
    print()
    print(sizing_report())
    print()
    print("residual arithmetic:")
    print(residual_report())
    print()
    print("convergence:")
    print(convergence_report())
    print()
    print("threshold width if a fan-in is ever measured:")
    print(fan_in_sensitivity())
    print()
    print("density cross-check:")
    print(density_cross_check())
    print()
    print("independent check:")
    print(cross_species_check())
    print()
    print("sign:")
    print(sign_problem())
    print()
    print("polarity:")
    print(polarity_problem())
    print()
    print("edges:")
    print(edge_report())
    print()
    print("allocation:")
    for s in STRUCTURES:
        for e in s.subelements:
            try:
                a = allocate(s, e.name)
                print(f"  {s.name + ' / ' + e.name:50} "
                      f"threshold {a['threshold_bytes'][0]/1e6:6.2f} MB   sized, not fillable")
            except NotImplementedError as exc:
                print(f"  {s.name + ' / ' + e.name:50} blocked")
                print(f"      {exc}")
    print()
    for fn, label in ((fan_in_map, "connectivity"), (select, "selection"),
                      (step, "scheduler"), (learn, "learning")):
        try:
            fn(BASAL_GANGLIA) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
