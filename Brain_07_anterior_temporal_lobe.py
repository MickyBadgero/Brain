"""Brain — anterior temporal lobe, the temporal pole.

One structure: the convergence apex of the ventral "what" streams and the semantic hub
where visual object identity and auditory word identity are bound into amodal concepts.

This file carries no history: no versions, no provenance, no "changed since", no
reference to sessions or prior files, no changelog, no "formerly", no commented-out
prior version.

The types that describe a structure, a population, an endpoint, a representation and an
edge come from Brain_config and are not redefined here.  Every edge in this section
leaves it, so every one is declared in two files, and two files cannot describe one edge
in agreement when the type describing it is defined twice.  What lives here is the
content: this section's count, axes, edges and findings.

Every neuron is a threshold gate.  There is no transducer, no graded non-spiking
element, no transmission-only structure and no sign-inverting stage, so the forward
operation covers every neuron in the section without exception.  That is a positive
statement about the section, not an absence of information.

What the operation cannot be run with is four terms.  Connection topology is unset, and
this section is worse off than one whose topography is described in prose and merely
needs turning into a function: no map, no convergence gradient and no ordering principle
on any axis is recorded here at all, so an unauthorised guess would have nothing to be a
guess at.  Sign arithmetic is unset, and doubly so, because the standard laminar block
that would supply at least one sign relationship is not available in this section.  No
rule writes a threshold.  And the scheduling discipline is unset while two loops close
through this structure.

The standard eight-layer block is a claim about granular isocortex and this region
cannot take it: agranular medially, dysgranular dorsolaterally, on a gradient, so layer
4 is absent at one end and thin at the other while three of the block's edges route
through layer 4.  No laminar edge set is carried here and none may be transcribed from a
granular section.

Two states this section needs are kept apart from "to derive" because no measurement
would resolve them into it.  The subdivision extent is contested: four published schemes
give two, three, three and four divisions and do not reduce to one another, so this waits
on an adjudication between results rather than on a decision-maker or an experiment.  And
the region's declared computation has no declared substrate: the auditory input lands on
the dorsal subdivision, the semantic output leaves the ventrolateral one, and no edge
between any two subdivisions is recorded in either direction under any scheme — so a
module implementing every neuron correctly still does not implement what the region does.

Every edge latency reads None, meaning to derive.  This section records no timing
statement of any kind, not even a qualitative one.  None is not a licence to substitute
zero or a uniform step.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2

import Brain_config as cfg
from Brain_config import (
    THRESHOLD_GATE, PER_HEMISPHERE, TO_DERIVE, UNKNOWN, OWED, CONTESTED,
    OPEN_STATES, EVENT_DRIVEN, NO_FRAME, DRIVER, MODULATORY,
    Population, Structure, Representation, Edge,
    far, here, class_endpoint, no_entry, unstemmed,
)

# Stems for the six files checked against the architecture.  A stem is one string
# lifted verbatim.
VIS = "01_visual_pathway"
AUD = "02_auditory_pathway"
PARIETAL = "06_posterior_parietal"
MEDIAL_TEMPORAL = "08_medial_temporal_lobe"
FRONTAL = "11_frontal_lobe"
INSULA = "17_insula_claustrum_habenula"

# --------------------------------------------------------------------------
# Axis states.
#
# Brain_config carries the states a quantity can be in.  One state this section
# needs describes an axis rather than a quantity and is declared here because no
# second module has yet needed it.  Moving it to Brain_config is owed the moment one
# does: a vocabulary term defined twice drifts, and nothing detects the drift.
#
# It is not a kind of TO_DERIVE.  Writing "to derive" over it asserts that nobody has
# looked, when the problem is that four groups have looked and disagree — and the two
# call for different work, one an experiment and the other an adjudication.
# --------------------------------------------------------------------------

EXACT = "exact"
INCOMPATIBLE_PARCELLATIONS = "incompatible parcellations"


@dataclass(frozen=True)
class Axis:
    """One axis of the structure's shape, with the state of its extent.

    `indexable` is False where an edge may not terminate on a position along the axis,
    whatever the extent says.
    """

    name: str
    extent: int | None
    state: str
    indexable: bool
    note: str = ""


@dataclass(frozen=True)
class SubdivisionScheme:
    """One published parcellation of this region.

    Four are live and they do not reduce to one another.  The object is a gradient —
    agranular medially, dysgranular dorsolaterally, changing progressively — and a
    gradient is what different instruments cut differently, which is why four schemes
    coexist without any of them being wrong.
    """

    basis: str
    divisions: tuple[str, ...]

    @property
    def extent(self) -> int:
        return len(self.divisions)


# The subdivisions sort this entry's edges, which is what makes them load-bearing
# rather than descriptive: the auditory input lands dorsally, the semantic output
# leaves ventrolaterally, the limbic traffic is ventromedial.  The connectional
# assignments agree across the schemes even where the boundaries do not.
SUBDIVISION_SCHEMES = (
    SubdivisionScheme("cytoarchitecture, human, two fields",
                      ("lateral temporopolar", "medial and ventral")),
    SubdivisionScheme("cytoarchitecture, human, three fields",
                      ("dorsal", "ventrolateral", "ventromedial")),
    SubdivisionScheme("anatomical connectivity, human",
                      ("dorsal", "lateral", "medial")),
    SubdivisionScheme("functional and anatomical network, human",
                      ("dorsal", "ventromedial", "medial", "anterolateral")),
)

CONNECTIONAL_ASSIGNMENT = (
    ("dorsal / dorsolateral",
     "takes the auditory input; emits to entorhinal, rostral perirhinal and posterior "
     "parahippocampal cortex; reported strongly connected with parietal cortex"),
    ("ventrolateral / anterolateral", "the default-semantic network node"),
    ("ventromedial / medial",
     "the limbic and paralimbic connections — amygdala, hippocampus, entorhinal and "
     "parahippocampal cortex, orbitofrontal cortex — largely via the uncinate fasciculus"),
)

# --------------------------------------------------------------------------
# Structure.
#
# The count is single-sourced: neither cortical thickness nor surface area is
# recorded, so the surface-density route that would confirm a headline count
# independently cannot be started, and it is short two terms rather than one.
# --------------------------------------------------------------------------

GREY_MATTER_CM3 = (4.08, 5.04, 6.00)   # ~5.04 +/- 0.96 per hemisphere; definitions vary

COUNT_IS_SINGLE_SOURCED = (
    "no second route: cortical thickness and surface area are both unrecorded, so the "
    "surface-density cross-check cannot be started and the volumetric density is the "
    "one term of it in hand"
)

TEMPORAL_POLE = Structure(
    "temporal pole",
    # Synapses are unrecorded, so fan_in is None and the store sits at the 16-bit
    # log2 ceiling.  The ceiling is doing all the work and the figure is a bound
    # rather than an estimate: the fan-in is absent, not ranged.
    (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE, 103_000_000, None),),
    # Laminae are owed per subdivision, so the tuple carries no laminar members: the
    # standard block may not be transcribed from a granular section.  The subdivision
    # names are carried from all four schemes without choosing among them.
    subelements=tuple(dict.fromkeys(d for s in SUBDIVISION_SCHEMES for d in s.divisions)),
    rank=4,
    axes=("lamina", "subdivision", "H", "W"),
    partitions=False,
)

STRUCTURES = (TEMPORAL_POLE,)

AXES = (
    Axis("lamina", None, OWED, False,
         "owed, per subdivision. Not unknown and not to-derive: the eight-layer block is "
         "positively wrong over part of the region, and the partial pattern that is recorded — "
         "thin layer II, a size gradient of pyramids through layer III, a thin layer IV, large "
         "dark pyramids in layer V, a layer VI spreading into the underlying white matter — is "
         "for the temporopolar cortex proper rather than for the whole entry. A partial pattern "
         "for part of the entry is not a laminar set for the entry, and it is known what "
         "research would close it"),
    Axis("subdivision", None, INCOMPATIBLE_PARCELLATIONS, False,
         "contested, extent 2, 3, 3 or 4 under four schemes that do not reduce to one another. "
         "Four groups have looked and disagree, so this needs adjudication between published "
         "results and not a measurement — and unlike every other unset item here, no "
         "decision-maker on this project can supply one"),
    Axis("H", None, TO_DERIVE, True, "no tangential pitch measured"),
    Axis("W", None, TO_DERIVE, True, "tangential sub-elements unknown"),
)

# The four association pathways reported to supply this region's structural
# connectivity: the physical substrate a conduction time would be derived from.
# Counts, lengths, diameters and g-ratios are all unrecorded, and only the first is
# assigned to particular edges.
TRACTS = (
    ("uncinate fasciculus",
     "carries the ventromedial subdivision's limbic and orbitofrontal traffic"),
    ("inferior longitudinal fasciculus", "edge assignment unrecorded"),
    ("middle longitudinal fasciculus",
     "edge assignment unrecorded; and no entry in 18_white_matter_tracts or anywhere "
     "else, which that file records as an owed correction at this section's source"),
    ("arcuate fasciculus", "edge assignment unrecorded"),
)

# --------------------------------------------------------------------------
# Edges.
#
# Every one of the twelve leaves the section.  Six far files are checked against the
# architecture — 01_visual_pathway, 02_auditory_pathway, 06_posterior_parietal,
# 08_medial_temporal_lobe, 11_frontal_lobe, 17_insula_claustrum_habenula — and every
# edge landing in one of them carries a diffed far-end state.  Two endpoints have no
# entry in any file at all.
#
# The source counts eleven edge lines and twelve are declared here.  The difference is
# one output line naming two structures — rostral perirhinal and posterior
# parahippocampal cortex — and an edge names its target structure rather than a
# pair.  The arity is explicit in the source, so splitting invents nothing.
#
# Every edge belongs to a subdivision and none of them says which, so the sub-element
# fields are empty throughout: the connectional evidence assigns them by class and
# the per-edge assignment is owed at the source.
#
# latency_s is real time in seconds and is None on every edge, because the biology
# records none.  It is never expressed in steps: a latency stated in steps has
# assumed a clock.
# --------------------------------------------------------------------------

# Not one payload in this section is typed, so the three states below are the whole
# range and collapsing them would hide which is which.  None of them is "typed".
NAMED = "named, not typed"
PARTIAL = "one component named, the rest owed"
WHOLLY_OWED = "wholly owed"

# The far end is checked against this section, or it is not, or it does not exist.
DIFFED = "diffed"                    # far file checked against the architecture
DEPENDENCY = "far-end dependency"    # far file named by stem, unchecked
NO_FAR_END = "no entry in any file at all"

THIS = "temporal pole"


@dataclass(frozen=True)
class Declared:
    """One edge as this section declares it, with the marks its own findings need.

    The edge itself is Brain_config's type.  What is added here is content: how far
    the description gets with the payload, and in what state the far end is.
    """

    edge: Edge
    payload_state: str = WHOLLY_OWED
    far_end: str = DIFFED

    @property
    def label(self) -> str:
        return f"{self.edge.source.name} -> {self.edge.target.name}"


def rep(units=TO_DERIVE, value_range=TO_DERIVE, frame=TO_DERIVE):
    """This structure has no rate of its own, so every line is event-driven.

    It is not a sensor and is not described as emitting on a schedule; it is driven
    by its inputs and emits when they change.  There is no system clock to borrow a
    rate from, and borrowing one would invent what the per-edge-latency invariant
    forbids.
    """
    return Representation(units=units, value_range=value_range,
                          update_timing=EVENT_DRIVEN, frame=frame)


UNTYPED = rep()

# The amodal concept: the payload on all six outputs.  It is a phrase and not a type
# — no units, no range, no coordinate frame, no declared channel structure — and the
# one thing known about it is a negative.  That negative is a finding rather than a
# gap: the lesion of this region is semantic dementia, a progressive loss of word and
# object meaning together, and one lesion taking out two modalities' meaning at once
# is the behavioural signature of a shared amodal representation rather than of two
# modal ones side by side.
AMODAL = rep(units="none — the amodal concept has no units",
             value_range="none",
             frame="none, and the absence is the content: modality has been lost")

EDGES: tuple[Declared, ...] = (
    # ---- inputs ----------------------------------------------------------
    Declared(Edge(far("rostral superior temporal gyrus", AUD), here(THIS),
                  "talker-invariant word and sound-object identity, the auditory 'what' "
                  "endpoint; the principal input to the dorsolateral subdivision",
                  representation=rep("owed", "owed", NO_FRAME),
                  note="two-ended: that file's anterior superior temporal gyrus entry declares "
                       "this region as a target and already names where this region sends the "
                       "code next, which matches this entry's own ventrolateral prefrontal "
                       "output. The producer writes it as a chained compound — two targets and "
                       "an onward hop on one line — so the arity is owed there"),
             NAMED, DIFFED),
    Declared(Edge(far("anterior inferotemporal cortex / ventral temporal", VIS), here(THIS),
                  "view-invariant object and face identity",
                  representation=rep("owed", "owed", NO_FRAME),
                  note="two-ended, and both endpoints are structures: that entry writes this "
                       "region as the named consumer and the distributed conceptual / semantic "
                       "system as what lies beyond it. The payloads agree"),
             NAMED, DIFFED),
    Declared(Edge(far("orbitofrontal cortex", FRONTAL), here(THIS),
                  "value, and nothing else typed: the rest of the payload is owed",
                  role=MODULATORY,
                  representation=rep("owed", "owed", NO_FRAME),
                  note="two-ended: that file's orbitofrontal / ventromedial prefrontal entry "
                       "declares this region by name. Neither end types the payload beyond "
                       "value, so the payload is owed at both"),
             PARTIAL, DIFFED),
    Declared(Edge(far("insular cortex", INSULA), here(THIS),
                  "interoceptive context, and the rest of the payload owed",
                  representation=rep("owed", "owed", NO_FRAME),
                  note="two-ended: that file's insula entry declares this region by name on an "
                       "output line typed interoceptive context with the rest owed, and names it "
                       "among its own inputs on a line marked reciprocal. Both limbs of the "
                       "reciprocity it asserts are written at that end"),
             PARTIAL, DIFFED),
    Declared(Edge(far("angular gyrus", PARIETAL), here(THIS),
                  "owed at both ends",
                  representation=rep("owed", "owed", NO_FRAME),
                  note="two-ended, and written from the producer's side: that file's angular "
                       "gyrus entry declares an output to the distributed conceptual / semantic "
                       "system via the temporal pole, the hippocampal formation, ventrolateral "
                       "prefrontal cortex and the default-mode partners, names this structure "
                       "explicitly among the four targets, and records the edge as owed as a "
                       "cross-file edit at this section's source. That producer line is a "
                       "compound of four targets and one network endpoint and is owed a split "
                       "there, so the arity at that end may change and the limb naming this "
                       "structure will not"),
             WHOLLY_OWED, DIFFED),
    Declared(Edge(far("amygdala", MEDIAL_TEMPORAL,
                      sub="basal / accessory basal nuclei"), here(THIS),
                  "the valence tag: a gain on perception, attention and memory encoding, "
                  "carrying no identity information of its own",
                  role=MODULATORY,
                  representation=rep("owed", "owed", NO_FRAME),
                  note="two-ended and the payloads agree in the same words: that entry declares "
                       "this region on its own line, attributed to the basal / accessory basal "
                       "nuclei and typed the valence tag — the named consumer, not a member of a "
                       "'widespread cortex' class. Fan-out is to derive there as fan-in is here, "
                       "so the edge is typed at both ends and quantified at neither. Carrying no "
                       "identity of its own is a constraint on what the gate may do with it "
                       "rather than a type"),
             NAMED, DIFFED),

    # ---- outputs ---------------------------------------------------------
    Declared(Edge(here(THIS), far("entorhinal cortex", MEDIAL_TEMPORAL,
                                  sub="entorhinal cortex"),
                  "the amodal concept, toward the hippocampal formation",
                  representation=AMODAL,
                  note="two-ended and the sub-element agrees: the hippocampal formation entry "
                       "declares this region on its own line, naming the sub-element this line "
                       "names, typed an amodal concept, and marks the payload owed at the "
                       "producer where modality-loss is the only checkable property in hand — "
                       "this section's own sentence about its own payload, arriving from the "
                       "other side. That entry's inferotemporal edge is a separate edge"),
             WHOLLY_OWED, DIFFED),
    Declared(Edge(here(THIS), no_entry("rostral perirhinal cortex"),
                  "the amodal concept",
                  representation=AMODAL,
                  note="no entry in any file at all, and two further files' edges point at the "
                       "same region: the inferotemporal entry in "
                       "01_visual_pathway names perirhinal cortex explicitly as the step by "
                       "which the ventral stream reaches the hippocampal formation, and "
                       "08_medial_temporal_lobe records the same gap from its own side. Inherited "
                       "gap; not patched here. A payload with one end missing cannot be checked "
                       "at all, which is a different state from a payload owed at two ends"),
             WHOLLY_OWED, NO_FAR_END),
    Declared(Edge(here(THIS), no_entry("posterior parahippocampal cortex"),
                  "the amodal concept",
                  representation=AMODAL,
                  note="no entry in any file at all. Inherited gap; not patched "
                       "here. This and the perirhinal edge were one compound source line naming "
                       "two structures, split because an edge names its target structure"),
             WHOLLY_OWED, NO_FAR_END),
    Declared(Edge(here(THIS), far("ventrolateral prefrontal cortex", FRONTAL),
                  "the amodal concept, for controlled retrieval and selection",
                  representation=AMODAL,
                  note="two-ended and typed at both: that far end declares this region on its "
                       "own line, typed an amodal concept, with the payload owed there as here. "
                       "Fan-in is to derive there as fan-out is here, so the edge is typed at "
                       "both ends and quantified at neither"),
             WHOLLY_OWED, DIFFED),
    Declared(Edge(here(THIS), far("amygdala", MEDIAL_TEMPORAL),
                  "the amodal concept, for affective evaluation",
                  representation=AMODAL,
                  note="two-ended: that entry declares this region on its own line, typed an "
                       "amodal concept for affective evaluation — this end's payload in this "
                       "end's words — and marks it owed for the same reason this section does. "
                       "This is the return limb of the amygdala loop, and the loop closes at "
                       "both ends"),
             WHOLLY_OWED, DIFFED),
    Declared(Edge(here(THIS), far("insular cortex", INSULA),
                  "the amodal concept",
                  representation=AMODAL,
                  note="two-ended: that file carries it as 'emotional, evaluative and "
                       "social context' and marks that its own largest gap, context being a "
                       "function word rather than a type with a range and a frame. Payload owed "
                       "at both ends, and the two ends agree that it is not writable"),
             WHOLLY_OWED, DIFFED),
)

SOURCE_EDGE_LINE_COUNT = 11

# The two reciprocal loops that close through this structure, and the reason
# co-instantiation binds: neither can be staged, and a register would break both.
LOOPS = (
    ("temporal pole <-> insular cortex",
     "the interoceptive context arrives and the output limb leaves; both limbs written "
     "here, and the far end's output limb owed at 17_insula_claustrum_habenula"),
    ("temporal pole <-> amygdala",
     "the valence tag arrives and the amodal concept leaves for affective evaluation; "
     "closed at both ends and verifiable from either"),
)

# Asserted against this structure and deliberately not written as an edge.
UNRESOLVED_INBOUND = ()

# Asserted against this structure, written as an edge, and still owed a repair at the
# producer rather than here.
INBOUND_OWED_AT_PRODUCER = (
    "06_posterior_parietal's angular gyrus entry names this structure explicitly among the "
    "four targets of one compound output line, one of which is a network endpoint. The limb "
    "naming this structure survives the split that line is owed; the arity at that end does "
    "not. Owed at that file",
)

# Declared at a consumer and at no producer: the mirror-image defect.
UNDECLARED_AT_THIS_PRODUCER = (
    "11_frontal_lobe's frontopolar entry records taking temporal input including the "
    "temporal pole. The six outputs above contain no frontopolar target, so that edge is "
    "declared at the consumer and at no producer. Owed at this section's source — either "
    "declare it here or it is withdrawn there",
)

# A stated function with no declared substrate.
DANGLING_REQUIREMENT = (
    "binding across modalities. The Function claims visual and auditory identity are bound "
    "into amodal concepts here; the connectional evidence puts the auditory input on the "
    "dorsal subdivision and the semantic output on the ventrolateral one; and no edge between "
    "any two subdivisions is recorded, in either direction, under any of the four schemes. "
    "The step is not merely unnamed — its two ends are known to sit on different subdivisions "
    "with nothing written between them. A missing region is a missing node and announces "
    "itself; this is a missing edge inside the one entry the file has, and nothing in the "
    "entry's shape makes it visible"
)

# Figures that may not be promoted into a width or an array size at this rung.
MEASUREMENT_CAUTIONS = (
    ("the 206.0 MB parameter store",
     "a ceiling and not an estimate: the fan-in is absent rather than ranged, so the 16-bit "
     "log2 cap is doing all the work and the true figure is at or below it"),
    ("the ~103M neuron count",
     "single-sourced. " + COUNT_IS_SINGLE_SOURCED),
    ("association-cortex packing of ~20,400 neurons/mm3",
     "one term of a calculation that needs two more. It is derived from the count and the "
     "volume, so it is not an independent confirmation of the count, and the surface-density "
     "route it would feed needs a thickness and a surface area that are both unrecorded"),
)

# --------------------------------------------------------------------------
# Forward operation.
#
# The specified part is writable for every neuron here, and four of its terms are
# unset.  The operation itself is not in question: every neuron is a threshold gate
# and none is described as doing anything else.
# --------------------------------------------------------------------------


def threshold_gate(counts, thresholds):
    """Fire where the summed input reaches the stored threshold.

    count[j]  = sum over fan_in(j) of sign(i, j) * active_source[i]
    active[j] = count[j] >= threshold[j]

    Integer comparison only: no weights and no multiply, because equal weights reduce
    the dot product to a count; no gradient, because nothing here is differentiated.
    This is the second half only.  The sum is the caller's, because sign() is unset
    and a bare sum would silently assert that every input is excitatory.
    """
    if len(counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(counts, thresholds)]


def sign(source_sub, target_sub):
    """The sign an incoming edge contributes with.

    Not set at any rung, and doubly open in this section: the standard laminar block
    that supplies at least one sign relationship elsewhere is unavailable here, so
    there is not even an internal edge whose sign could be named.
    """
    raise NotImplementedError(
        "sign arithmetic is not set at any rung, and this section carries no internal edge "
        "set from which a sign relationship could be read: the standard laminar block is a "
        "claim about granular isocortex and this region cannot take it"
    )


def fan_in_map(structure: Structure):
    """Which source lines converge on each neuron.

    Connection topology is unset at every rung and requires explicit agreement before
    it is touched.  This section is blocked harder than one whose topography is
    described in prose: no map, no convergence gradient and no ordering principle on
    any axis is recorded, and fan-in reads to derive on all twelve edges.  That is
    not a harder version of the prose problem — it is the state where an unauthorised
    guess would have nothing to be a guess at.
    """
    raise NotImplementedError(
        "connection topology is not set, and no topography of any kind is recorded for "
        "this structure to derive one from: fan-in reads to derive on all "
        f"{len(EDGES)} edges"
    )


def transform(structure: Structure, *args, **kwargs):
    """Place the operation the structure's Function requires between its arrays.

    Not implementable, and the module cannot even state the missing operation's
    signature, because neither the payload arriving nor the payload leaving is typed.
    """
    raise NotImplementedError(f"{structure.name}: {DANGLING_REQUIREMENT}")


bind = transform   # the region's declared computation, under the name the Function uses


def allocate(structure: Structure, subelement: str | None = None):
    """Size the threshold and activity arrays.

    The region-level allocation succeeds and returns the ceiling flag with the figure,
    because a ceiling and a measurement behave identically in arithmetic and a caller
    must not be able to obtain the size without the caveat.

    No sub-element allocation succeeds, and the refusals are not interchangeable.  One
    of the four axes fails for a reason no measurement would fix.
    """
    if subelement is None:
        p = structure.populations[0]
        return {"structure": structure.name,
                "neurons": p.count,
                "threshold_bits": p.threshold_bits,
                "threshold_bytes": p.parameter_bytes,
                "active_bytes": p.count // 8,
                "width_is_a_ceiling": p.fan_in is None,
                "count_basis": COUNT_IS_SINGLE_SOURCED}

    for axis in AXES:
        if axis.state == INCOMPATIBLE_PARCELLATIONS and subelement in structure.subelements:
            raise NotImplementedError(
                f"{structure.name}: the {axis.name} axis extent is contested across "
                f"{len(SUBDIVISION_SCHEMES)} schemes giving "
                f"{sorted(s.extent for s in SUBDIVISION_SCHEMES)} divisions, and no extent can "
                f"be taken. This is not a number nobody has measured; picking one would take a "
                f"side in a literature dispute and propagate it into every buffer shape "
                f"downstream. {axis.note}"
            )
    raise NotImplementedError(
        f"{structure.name}: none of the four axes of {structure.axes} has an extent, and they "
        f"are open in three different states — "
        + "; ".join(f"{a.name}: {a.state}" for a in AXES)
    )


def order_updates(structure: Structure):
    """Put the section's edges in the order they are evaluated.

    Refused.  Two loops close through this structure, on four limbs with real,
    different and unmeasured delays.  A loop with heterogeneous real delays settles by
    its own dynamics; the same loop broken by registers becomes an iterated map whose
    trajectory depends on the update rate, and those are two different systems
    computing two different things.

    Setting every latency equal and choosing an interval short enough to carry the
    finest one is a legitimate thing this rung may decide to do.  The finest one is not
    known: this section records no timing statement of any kind, not even a qualitative
    one, so even that shortcut has no parameter.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; every edge "
        "latency in this section reads to derive, so a uniform interval has no value to take "
        "either, and both loops would be broken by a register: "
        + "; ".join(name for name, _ in LOOPS)
    )


step = order_updates


def edge_storage(declared: Declared):
    """Values in flight on one edge, which the per-edge-latency invariant creates.

    line_count * ceil(latency / update_interval) * bytes_per_value, and in this section
    every term is unavailable on every edge.  The design rung expects one unset term,
    the update interval; here there are four, and they are recorded rather than
    estimated past, because a figure computed from assumed terms enters the file
    looking exactly like a derived one.  Never summed with parameter memory or state.
    """
    r = declared.edge.representation
    missing = ["line_count: fan-in and fan-out both read to derive, and no axon count is "
               "stated for any of the four named tracts",
               "latency: to derive, on all twelve edges",
               "update_interval: unset, and waiting on the scheduling discipline"]
    if r.units in OPEN_STATES or _is_open(r.units):
        missing.append("bytes_per_value: the payload is not typed, and none in this section is")
    raise NotImplementedError(f"{declared.label}: " + "; ".join(missing))


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    That is recorded rather than assumed.  A threshold that is never written is a
    construction cost rather than a memory, which is why the module is still coherent
    without it: thresholds are read-only buffers and the section runs open-loop.  It is
    the one unset item that still leaves a runnable artifact.
    """
    raise NotImplementedError("no learning rule is set, and it is not this rung's to choose")


def _is_open(value: str) -> bool:
    """True where a representation slot names a state rather than a value.

    A slot may be open inside a sentence as well as on its own — "owed at the producer"
    is as open as "owed" — so this looks for the state word anywhere in the string.
    """
    low = value.lower()
    return value in OPEN_STATES or any(w in low for w in
                                       ("owed", "unknown", "contested", "to derive",
                                        "not stated", "none"))


# --------------------------------------------------------------------------
# Derived reporting.  Every figure is recomputed here, never transcribed.
# --------------------------------------------------------------------------


# Owed to Brain_config, recorded here rather than changed there, because config is
# shared by every numbered module and a change to it is not this module's to make.
CONFIG_OWED = (
    "cfg.sizing_report() hardcodes '(mixed basis)' and 'the total is a floor'. Neither holds "
    "here: the basis is uniform per hemisphere, and the total is a CEILING because the width "
    "is a log2 cap over an absent fan-in rather than a measured width. A floor and a ceiling "
    "are opposite claims about the same number, so this module computes its own headline "
    "instead of printing config's and contradicting it two lines later",
    "Brain_config carries no axis-extent state for INCOMPATIBLE_PARCELLATIONS, which is "
    "declared locally above. Moving it there is owed the moment a second module needs it",
)


def sizing_report() -> str:
    out = ["anterior temporal lobe — parameter memory"]
    p = TEMPORAL_POLE.populations[0]
    out.append(f"  {TEMPORAL_POLE.name} / {p.name:<22} {p.basis:<16} {p.count:>13,} "
               f"{p.threshold_bits:>3} bits   {p.parameter_bytes/1e6:.3f} MB")
    out.append(f"  stated total: {p.parameter_bytes/1e6:.2f} MB   (basis uniform: {p.basis})")
    out.append("")
    out.append(f"  activity bitmap {p.count/8/1e6:.3f} MB, threshold store "
               f"{p.parameter_bytes/1e6:.1f} MB")
    out.append("  the total is a CEILING, not a floor: the fan-in is absent rather than ranged,")
    out.append("  so 16 bits is the log2 cap doing all the work and the true figure is at or")
    out.append("  below it. What would move it is a synapse count.")
    out.append(f"  {COUNT_IS_SINGLE_SOURCED}")
    out.append("  state memory and edge storage are not in this total and are never summed with it")
    out.append("  memory is a derived requirement, not a limit to design against")
    return "\n".join(out)


def fan_in_sensitivity() -> str:
    """What a synapse count would do to the figure, if one is ever measured."""
    n = TEMPORAL_POLE.populations[0].count
    out = ["  fan-in     bits    derived store    realised in uint16     gap"]
    for fan_in in (256, 1_000, 4_000, 16_000, 65_000):
        derived = ceil(log2(fan_in))
        container = 8 if derived <= 8 else 16
        d, r = n * derived / 8, n * container / 8
        out.append(f"  {fan_in:>6}   {derived:>4}     {d/1e6:8.1f} MB     "
                   f"uint{container:<2} {r/1e6:8.1f} MB   {100*(r-d)/d:5.1f}%")
    out.append(f"  absent      16     {n*16/8/1e6:8.1f} MB     uint16  "
               f"{n*16/8/1e6:8.1f} MB     0.0%")
    out.append("  the zero gap is the signature of an absent measurement, not of a good fit:")
    out.append("  the derived width IS 16 because the fan-in is unknown, so uint16 is exact.")
    out.append("  the moment a synapse count arrives the derived width drops and the gap opens.")
    out.append("  and because 16 is a ceiling, the allocated array is correct at every fan-in")
    out.append("  the biology could turn out to have: it cannot be wrong, only wasteful.")
    return "\n".join(out)


def density_cross_check() -> str:
    """Recompute neurons/mm3 across the whole stated volume range, not at its centre."""
    n = TEMPORAL_POLE.populations[0].count
    lo, mid, hi = GREY_MATTER_CM3
    out = []
    for label, cm3 in (("low", lo), ("centre", mid), ("high", hi)):
        out.append(f"  {label:>6}  {cm3:.2f} cm3 -> {n/(cm3*1000.0):9,.0f} neurons/mm3")
    centre = n / (mid * 1000.0)
    out.append(f"  V1 for comparison:      ~60,000 neurons/mm3 "
               f"(this structure is {centre/60000:.2f} of it at the centre value)")
    out.append("  ordinary association-cortex packing. the neighbouring superior temporal gyrus")
    out.append(f"  association cortex is ~145M against this ~103M, a ratio of {145/103:.2f}.")
    out.append("  this is not an independent confirmation of the count: the density is derived")
    out.append("  FROM the count and the volume, so it closes against the source's ~20,000 by")
    out.append("  construction. an independent route needs a thickness and a surface area.")
    return "\n".join(out)


def shape_report() -> str:
    out = [f"  sheet, rank {TEMPORAL_POLE.rank}: {TEMPORAL_POLE.axes}"]
    for a in AXES:
        out.append(f"    {a.name:<12}  {a.state:<28}  {a.note[:60]}")
    out.append("  four axes, open in three different states; a single 'to derive' would hide that")
    out.append("  the contested one is not waiting on a decision-maker but on an adjudication")
    out.append("  between published results, which no decision on this project can supply:")
    for sc in SUBDIVISION_SCHEMES:
        out.append(f"    {sc.extent} — {', '.join(sc.divisions)}   [{sc.basis}]")
    out.append("  the schemes' connectional assignments agree even where the boundaries do not:")
    for div, what in CONNECTIONAL_ASSIGNMENT:
        out.append(f"    {div:<30} {what[:72]}")
    out.append("  every edge belongs to a subdivision and no edge declares which: owed at source")
    out.append("  no laminar edge set is carried: the standard eight-layer block routes three of")
    out.append("  its edges through a layer 4 that is absent at one end of this region")
    return "\n".join(out)


def payload_report() -> str:
    out = [f"  edges: {len(EDGES)}    payloads with units, a range or a coordinate frame: 0"]
    out.append(f"  the source counts {SOURCE_EDGE_LINE_COUNT} edge lines; the extra one is the "
               f"compound output line naming two structures, split here")
    for state in (NAMED, PARTIAL, WHOLLY_OWED):
        n = sum(1 for d in EDGES if d.payload_state == state)
        out.append(f"    {state:<38} {n:>3}")
    out.append("  zero typed of twelve, and the zero is a finding rather than a coverage gap:")
    out.append("  this is where the payload stops being modal. every stage below this one on the")
    out.append("  ventral line carries something with a frame; what leaves here is defined by")
    out.append("  what it has lost, and the one checkable property is that negative.")
    out.append("  so Representation has nothing to hold on any line in this section, and the")
    out.append("  two-ends-disagree check it exists to give is unavailable here entirely.")
    return "\n".join(out)


def far_end_report() -> str:
    out = []
    for state in (DIFFED, DEPENDENCY, NO_FAR_END):
        rows = [d for d in EDGES if d.far_end == state]
        out.append(f"  {state}: {len(rows)}")
        for d in rows:
            out.append(f"      {d.label}")
    out.append("  a diffed far end is checked against the architecture; a dependency names")
    out.append("  the file by stem and asserts nothing about its contents; an endpoint with no")
    out.append("  entry has nobody to be diffed against at all.")
    out.append("  a payload owed at two ends can be closed by research at either end;")
    out.append("  a payload with one end missing cannot be checked at all.")
    out.append("  a stub for a missing endpoint would supply the consumer and destroy the check.")
    return "\n".join(out)


def dangling_requirement_report() -> str:
    out = [f"  stated functions with no declared substrate: 1", f"      {DANGLING_REQUIREMENT}"]
    out.append("  the module implements every neuron in this structure correctly and does not")
    out.append("  implement what the region does.")
    out.append("  edges asserted against this structure and not written:")
    for a in UNRESOLVED_INBOUND or ("none",):
        out.append(f"      {a}")
    out.append("  edges written here whose repair is owed at the producer:")
    for a in INBOUND_OWED_AT_PRODUCER:
        out.append(f"      {a}")
    out.append("  edges declared at a consumer with no producer here:")
    for a in UNDECLARED_AT_THIS_PRODUCER:
        out.append(f"      {a}")
    return "\n".join(out)


def loop_report() -> str:
    out = [f"  closed loops running through this structure: {len(LOOPS)}"]
    for name, what in LOOPS:
        out.append(f"      {name}: {what}")
    out.append("  co-instantiation: satisfied at the region level, unstatable at the sub-element")
    out.append("  level, because the sub-elements the edges attach to have no edges between them")
    out.append("  and the binding the function claims is exactly such an edge.")
    out.append("  a register on any limb turns a loop that settles by its own dynamics into an")
    out.append("  iterated map whose trajectory depends on the update rate.")
    return "\n".join(out)


def latency_report() -> str:
    stated = [d for d in EDGES if d.edge.latency_s is not None]
    out = [f"  edges with a stated latency: {len(stated)}    to derive: "
           f"{len(EDGES) - len(stated)}"]
    out.append("  no timing figure of any kind is recorded in this section, not even a")
    out.append("  qualitative one. the substrate is named where the number is not:")
    for name, note in TRACTS:
        out.append(f"      {name} — {note}")
    out.append("  one edge class of twelve has a named physical carrier; no length, diameter or")
    out.append("  g-ratio is recorded for any of the four tracts.")
    return "\n".join(out)


def measurement_caution_report() -> str:
    out = []
    for figure, why in MEASUREMENT_CAUTIONS:
        out.append(f"  {figure}")
        out.append(f"      {why}")
    out.append("  none of these may be promoted into a width or an array size at this rung")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report())
    print("\nthreshold width against a synapse count, if one is ever measured:")
    print(fan_in_sensitivity())
    print("\ndensity cross-check:")
    print(density_cross_check())
    print("\nshape:")
    print(shape_report())
    print("\nedges:")
    print(cfg.edge_report([d.edge for d in EDGES]))
    print("\nthe payload boundary:")
    print(payload_report())
    print("\nfar ends:")
    print(far_end_report())
    print("\nloops:")
    print(loop_report())
    print("\nlatency:")
    print(latency_report())
    print("\nstated functions with no declared substrate:")
    print(dangling_requirement_report())
    print("\nmeasurements that must not be promoted:")
    print(measurement_caution_report())
    print("\nowed to Brain_config, not changed there:")
    for item in CONFIG_OWED:
        print(f"  {item}")
    print()
    for fn, label, args in ((sign, "sign", (None, None)),
                            (fan_in_map, "connectivity", (TEMPORAL_POLE,)),
                            (transform, "binding", (TEMPORAL_POLE,)),
                            (order_updates, "scheduler", (TEMPORAL_POLE,)),
                            (learn, "learning", ())):
        try:
            fn(*args)
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
    try:
        edge_storage(EDGES[0])
    except NotImplementedError as exc:
        print(f"{'edge storage':14} blocked: {exc}")
    for sub in ("dorsal", None):
        if sub is None:
            continue
        try:
            allocate(TEMPORAL_POLE, sub)
        except NotImplementedError as exc:
            print(f"{'allocation':14} blocked: {exc}")
    print()
    a = allocate(TEMPORAL_POLE)
    print(f"allocation ok: {a['structure']}: {a['neurons']:,} neurons, {a['threshold_bits']} bits "
          f"(a CEILING: {a['width_is_a_ceiling']}), {a['threshold_bytes']/1e6:.1f} MB thresholds, "
          f"{a['active_bytes']/1e6:.3f} MB activity")
