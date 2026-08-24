"""Brain — posterior parietal.

The anterior and medial intraparietal areas, the supramarginal and angular gyri, and
the precuneus: their structures, axes, edges, and the threshold-gate forward operation.

This file carries no history: no versions, no provenance, no "changed since", no
reference to sessions or prior files, no changelog, no "formerly", no commented-out
prior version.

The types that describe a structure, a population, an endpoint, a representation and
an edge come from Brain_config and are not redefined here.  An edge that leaves this
section is declared at both ends, in two files, and two files cannot describe one edge
in agreement when the type describing it is defined twice.  What lives here is the
content: this section's counts, axes, edges and findings.

The forward operation is writable for every population in this section, and on 37 of
its 55 edges there is nothing to send along it.  That is the section's shape.  The gates
can be built; the wires are mostly unnamed.  Sorting the 55 by content class gives
sensorimotor 9 typed and 9 not, perceptual 9 typed and 4 not, association 0 typed and
24 not — so association coupling is sufficient for an untypable payload and is not
necessary for one, since thirteen sensorimotor and perceptual lines are untyped as well.
The module computes that split rather than restating it, and reports it by class rather
than as one percentage, because a rate distributed at random would be a coverage problem
while a boundary with a location is a claim about where the description stops.

Every edge latency reads None, meaning to derive.  No time constant, no ordering
constraint and no conduction figure appears anywhere in this section.  What the section
constrains instead is the payload.

Three states this section needs are not kinds of "to derive" and are kept apart from it.
An axis that is not known to be an axis: PGa and PGp sit on a rostro-caudal gradient,
and a gradient is not a border, so whether an edge can terminate on PGa is a question
about whether PGa is a place — no count would settle it.  A target that is not a node:
two edges terminate on networks, which are sets defined by correlated activity rather
than by projection, so naming the members would manufacture the arity.  And an edge that
exists because the other end declared it: two projections to the lateral intraparietal
area were written so that the edge would have two ends, with no source naming either.
"""

from __future__ import annotations

from dataclasses import dataclass

import Brain_config as cfg
from Brain_config import (
    THRESHOLD_GATE, PER_HEMISPHERE, TO_DERIVE, UNKNOWN, OWED, CONTESTED,
    OPEN_STATES, EVENT_DRIVEN, NO_FRAME, DRIVER, MODULATORY,
    Population, Structure, Representation, Edge,
    far, here, class_endpoint, no_entry, unstemmed,
)

# --------------------------------------------------------------------------
# Element class: one, and none of the four exceptional classes appears here.
#
# Every population in all five structures is a threshold gate.  No structure in
# this section carries other structures' edges, converts a physical stimulus,
# responds without an action potential, or treats hyperpolarisation as the
# excitatory response.  That is a positive statement about the section, not an
# absence of information, and it is why the ordinary entry shape fits all five.
# --------------------------------------------------------------------------

GRANULAR_LAMINAE = ("1", "2", "3", "4", "5a", "5b", "6a", "6b")

# --------------------------------------------------------------------------
# Axis states.
#
# Brain_config carries the states a quantity can be in.  Two states this section
# needs describe an axis rather than a quantity, and they are declared here
# because no second module has yet needed them.  Moving them to Brain_config is
# owed the moment one does: a vocabulary term defined twice drifts, and nothing
# detects the drift.
#
# Neither is a kind of TO_DERIVE.  Writing "to derive" over INCOMPATIBLE_
# PARCELLATIONS asserts one division nobody has measured, when the problem is
# that several have been measured and do not align.  Writing it over
# GRADIENT_NOT_PARTITION asserts a size is missing, when what is missing is the
# division itself.
# --------------------------------------------------------------------------

EXACT = "exact"
INCOMPATIBLE_PARCELLATIONS = "incompatible parcellations"
GRADIENT_NOT_PARTITION = "gradient, not known to be a partition"

AXIS_STATES = (EXACT, TO_DERIVE, UNKNOWN, INCOMPATIBLE_PARCELLATIONS, GRADIENT_NOT_PARTITION)


@dataclass(frozen=True)
class Axis:
    """One axis of a structure's shape, with the state of its extent.

    Brain_config's Structure carries axis names and whether the count partitions to
    the sub-elements.  This holds the section's own content: how long each axis is,
    and in which of the states above.  `indexable` is False where an edge may not
    terminate on a position along the axis, whatever the extent says.
    """

    name: str
    extent: int | None
    state: str
    indexable: bool
    note: str = ""


# --------------------------------------------------------------------------
# Counts.
#
# A count and an analogy behave identically in arithmetic, so the difference can
# only live in a field set at the moment the number is written; it cannot be
# recovered afterwards.  allocate() returns the figure and the basis together, so
# a caller cannot obtain the size without the caveat.
#
# The three unpriced rows are unpriced differently, and the difference is what
# names the missing measurement.
# --------------------------------------------------------------------------

INTRAPARIETAL_ANALOGY = (
    "by analogy to the neighbouring measured intraparietal areas — the lateral at ~20M and the "
    "ventral at ~12M, whose counts live in 04_dorsal_visual_parietal_stream and are right as quoted there. No clean human count for this area. The figure may not be quoted as measured, and the "
    "two structures it sizes are not the same size as each other for any biological reason")

COUNT_BASIS = {
    "anterior intraparietal area": INTRAPARIETAL_ANALOGY,
    "medial intraparietal area / parietal reach region": INTRAPARIETAL_ANALOGY,
}

UNPRICED_BECAUSE = {
    "supramarginal gyrus":
        "a packing density and no volume. Association-cortex packing of order 20,000 neurons/mm3 "
        "is stated and the grey-matter volume slot reads unknown, so this row is one measurement "
        "short of a count. A density is one factor of a count and may not be promoted into one",
    "angular gyrus":
        "this section's own pricing method cannot reach it. The macaque has no angular gyrus in "
        "the strict sense, so even a homology-based estimate is loose, and the analogy that priced "
        "the two intraparietal areas is unavailable precisely where the payload is least writable. "
        "Those are independent facts that land on one entry",
    "precuneus":
        "neither factor of a count. No density and no volume: the description offers only a large "
        "medial-parietal association territory, and this is the barest of the three refusals",
}

# --------------------------------------------------------------------------
# Structures.
# --------------------------------------------------------------------------


def _cortex(count=None):
    return (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE, count, None),)


ANTERIOR_INTRAPARIETAL = Structure(
    "anterior intraparietal area", _cortex(15_000_000),
    subelements=GRANULAR_LAMINAE, rank=2, axes=("lamina", "position"), partitions=False)

MEDIAL_INTRAPARIETAL = Structure(
    "medial intraparietal area / parietal reach region", _cortex(15_000_000),
    subelements=("dorsal part", "ventral part", "anterior sector", "posterior sector")
                + GRANULAR_LAMINAE,
    rank=3, axes=("division", "lamina", "position"), partitions=False)

SUPRAMARGINAL_GYRUS = Structure(
    "supramarginal gyrus", _cortex(),
    subelements=("PFop", "PFt", "PF", "PFcm", "PFm") + GRANULAR_LAMINAE,
    rank=3, axes=("area", "lamina", "position"), partitions=False)

ANGULAR_GYRUS = Structure(
    "angular gyrus", _cortex(),
    subelements=("PGa", "PGp") + GRANULAR_LAMINAE,
    rank=3, axes=("division", "lamina", "position"), partitions=False)

PRECUNEUS = Structure(
    "precuneus", _cortex(),
    subelements=("anterior sensorimotor sector", "central cognitive sector",
                 "posterior visual sector", "7Am", "7Pm") + GRANULAR_LAMINAE,
    rank=3, axes=("sector", "lamina", "position"), partitions=False)

STRUCTURES = (ANTERIOR_INTRAPARIETAL, MEDIAL_INTRAPARIETAL, SUPRAMARGINAL_GYRUS,
              ANGULAR_GYRUS, PRECUNEUS)

LAMINA_GRANULAR = Axis("lamina", 8, EXACT, True,
                       "granular association isocortex, layer 4 undivided")

AXES = {
    "anterior intraparietal area": (
        LAMINA_GRANULAR,
        Axis("position", None, TO_DERIVE, True, ""),
        # The only closed divisional axis in the section, closed by a negative
        # result rather than by silence.
        Axis("division", 0, EXACT, False,
             "none, and established rather than absent: receptor-architectonic mapping of the whole "
             "intraparietal sulcus divides this area's neighbours — the ventral into medial and "
             "lateral, the lateral into dorsal and ventral, the medial into dorsal and ventral — and "
             "leaves this one undivided. A negative result from a study that would have found a "
             "division, recorded as such rather than as unknown"),
        Axis("tangential", None, OWED, False,
             "owed: the Function asserts selectivity for grip type, precision against whole-hand — a "
             "categorical property that is columnar elsewhere in this section — and whether grip "
             "types cluster spatially was not established. Until it is, no edge may terminate below "
             "the region level"),
    ),
    "medial intraparietal area / parietal reach region": (
        Axis("lamina", 8, EXACT, True,
             "granular, layer 4 undivided, with two distinct bands of Baillarger in myelin stain. "
             "The bands belong to the fibre plexus in layers 4 and 5b rather than to a cell "
             "population, so they are a property of this axis and not a population to allocate"),
        Axis("division", 2, INCOMPATIBLE_PARCELLATIONS, True,
             "receptor architecture gives a dorsal and a ventral part, their separate payloads owed "
             "and the reach literature not using the division at all — a division the physiology has "
             "not caught up with. Tracer plus tractography gives instead an anterior and a posterior "
             "sector, on gradient-like connectivity profiles rather than on a border. A gradient "
             "with sectors and a receptor border with two parts are not the same claim about the "
             "same tissue, and there is no basis here for choosing. No per-division count under "
             "either parcellation"),
        Axis("position", None, TO_DERIVE, True, ""),
        Axis("tangential", None, UNKNOWN, False, "unknown"),
    ),
    "supramarginal gyrus": (
        LAMINA_GRANULAR,
        Axis("area", 5, INCOMPATIBLE_PARCELLATIONS, True,
             "PFop, PFt, PF, PFcm, PFm — cytoarchitectonic before they are functional, their "
             "separate payloads owed, and every edge terminates on the whole gyrus. Two further "
             "divisions cross-cut them and neither maps cleanly onto them: a dorsal/ventral split at "
             "the temporoparietal junction, and a left/right functional asymmetry. Three schemes "
             "over one piece of cortex, none aligning, while the Function asserts at least three "
             "distinct jobs — so an edge terminating on the whole gyrus is under-specified and "
             "splitting is owed. No per-area count"),
        Axis("position", None, TO_DERIVE, True, ""),
        Axis("tangential", None, UNKNOWN, False,
             "unknown; no columnar or compartmental repeat found"),
    ),
    "angular gyrus": (
        LAMINA_GRANULAR,
        # The section's sharpest representation finding, and the one refusal no
        # measurement would remove.
        Axis("division", 2, GRADIENT_NOT_PARTITION, False,
             "PGa rostral and PGp caudal, on a stated rostro-caudal gradient from "
             "ventrolateral-prefrontal-coupled and more attentional to hippocampal and "
             "default-mode-coupled and more mnemonic. A gradient is not a border: whether these are "
             "compartments an edge can terminate on, or two ends of a continuum with no boundary, is "
             "not established. If it is a partition it sorts six of this entry's input edges — "
             "prefrontal and priority-map to PGa, hippocampal and default-mode to PGp — so resolving "
             "it would change the arity of six edges at once, which is why the question is not idle"),
        Axis("position", None, TO_DERIVE, True, ""),
        Axis("tangential", None, UNKNOWN, False, "unknown"),
    ),
    "precuneus": (
        Axis("lamina", 8, EXACT, True, "granular medial association isocortex"),
        Axis("sector", 3, INCOMPATIBLE_PARCELLATIONS, True,
             "an anterior sensorimotor sector (reach, area-5 coupled), a central cognitive / "
             "default-mode sector, and a posterior visual sector (occipital-coupled), against the "
             "architectonic pair 7Am and 7Pm — an anterior/posterior pair against a three-sector "
             "gradient — and whether they are the same division under two names or a cross-cutting "
             "one is owed. No per-sector count either, so this axis is unsized and contested at "
             "once, the only axis in the section of which that is true"),
        Axis("position", None, TO_DERIVE, True, ""),
        Axis("tangential", None, UNKNOWN, False, "unknown"),
    ),
}

# The left/right functional asymmetry is not a sub-element and is covered by the
# per-hemisphere counting basis.  Whether the angular gradient runs the same way on
# both sides is unknown, so that convention carries an unchecked assumption here.
HEMISPHERIC_ASSUMPTION = (
    "the per-hemisphere basis assumes the two hemispheres take the same shape; the angular gyrus's "
    "rostro-caudal gradient is not known to be the same on both sides, and the supramarginal gyrus "
    "carries a stated left/right functional asymmetry")

# --------------------------------------------------------------------------
# The internal laminar block.
#
# The writable part of every entry's transform, and the same block in all five:
# uniform, and still a per-structure field, because the value is not uniform across
# the map and a field that happens to hold one value is still a field.
#
# The block is data and is not ordered.  Two edges are within-sub-element
# recurrence and one closes a reciprocal loop, and each reads an activity value
# that the same update writes.  Which value that is — this update's or the one
# before it — is the scheduling discipline, and it is not this rung's to choose.
# --------------------------------------------------------------------------

INTERNAL_BLOCK = (
    ("4", "2/3", "excitatory", "granular input to the supragranular layers"),
    ("2/3", "5a", "excitatory", "supragranular to infragranular output"),
    ("2/3", "5b", "excitatory", "supragranular to infragranular output"),
    ("5a", "2/3", "excitatory", "the reciprocal limb, closing a loop"),
    ("6a", "4", "to derive", "opposite in sign to 6a -> 5a; which sign is which is not stated"),
    ("6a", "5a", "to derive", "opposite in sign to 6a -> 4; which sign is which is not stated"),
    ("6b", "6a", "excitatory", "arousal-gated"),
    ("4", "4", "excitatory", "within-sub-element recurrence"),
    ("2/3", "2/3", "excitatory", "within-sub-element recurrence"),
)

RECURRENT = tuple((a, b) for a, b, _, _ in INTERNAL_BLOCK if a == b or (a, b) == ("5a", "2/3"))

# --------------------------------------------------------------------------
# Edges.
#
# A cross-file endpoint carries the far file's stem.  Five files were read beside
# this section — 01_visual_pathway, 04_dorsal_visual_parietal_stream,
# 05_sensorimotor_loop, 11_frontal_lobe and 17_insula_claustrum_habenula — and only
# endpoints the rung above stemmed carry a stem here.  An unstemmed endpoint is a
# reading not yet done, not a claim that no far end exists; writing the stem here
# would derive connectivity at the wrong rung, since the endpoint would resolve and
# nothing would have checked that it resolves right.
#
# Payload state is the word the rung above uses.  Representation is this rung's own
# field, and where the two disagree the report says so rather than reconciling them:
# a reconciliation would leave one record standing for two readings.
# --------------------------------------------------------------------------

TYPED, PARTLY_WRITABLE, UNKNOWN_OWED = "typed", "only partly writable — owed", "unknown — owed"

SENSORIMOTOR, PERCEPTUAL, ASSOCIATION = "sensorimotor", "perceptual", "association / default-mode"

# A network is not a class and not a route.  A class is visibly unresolved and
# invites splitting; a route names a circuit; a network is a set of regions defined
# by correlated activity, and naming its members turns one edge into several and
# asserts each member receives the same payload.  Brain_config has no bucket for
# this kind, so its edge_report does not count these; adding one there is owed.
NETWORK_ENDPOINT = "network"


def network(name):
    """An endpoint naming a network rather than a region."""
    return cfg.Endpoint(name, kind=NETWORK_ENDPOINT)


@dataclass(frozen=True)
class Declared:
    """One edge as this section declares it, with the marks the section's own findings need.

    The edge itself is Brain_config's type.  What is added here is content: what the
    payload is about, whether the line was written only because the far end declared
    it, whether its agreement with a far end certifies anything, and how many
    endpoints share the line.
    """

    edge: Edge
    payload_state: str = OWED
    content_class: str = ASSOCIATION
    single_ended_origin: bool = False   # written so the edge would have two ends
    certifies_nothing: bool = False     # one end transcribed from the other
    compound_line: int = 0              # endpoints named on one line; splitting owed

    @property
    def label(self) -> str:
        return f"{self.edge.source.name} -> {self.edge.target.name}"


def rep(units=TO_DERIVE, value_range=TO_DERIVE, frame=TO_DERIVE):
    """No structure here has a rate of its own, so every line is event-driven.

    That is a statement and not a placeholder: none of the five is a sensor, all five
    are driven by their inputs, and there is no system clock to borrow a rate from.
    """
    return Representation(units=units, value_range=value_range,
                          update_timing=EVENT_DRIVEN, frame=frame)


UNTYPED = rep()

# Stems for the five files checked against this section.
VIS, DORSAL, SENSORIMOTOR_LOOP, FRONTAL, INSULA = (
    "01_visual_pathway", "04_dorsal_visual_parietal_stream", "05_sensorimotor_loop",
    "11_frontal_lobe", "17_insula_claustrum_habenula")

# Named on this section's edges with no entry in any file the pass read.  The first
# three are the reach channel's visual origin, so the channel is described from its
# second stage onward.  Visual and visuomotor cortex, plainly in scope, and absent.
MISSING_PRODUCERS = ("V6", "the dorsal subdivision of V6A", "the ventral subdivision of V6A",
                     "the caudal intraparietal area")

AIP, MIP = "anterior intraparietal area", "medial intraparietal area"
SMG, AG, PCUN = "supramarginal gyrus", "angular gyrus", "precuneus"

EDGES: tuple[Declared, ...] = (
    # ---- anterior intraparietal area -------------------------------------
    Declared(Edge(no_entry("the caudal intraparietal area"), here(AIP),
                  "3-D surface shape from disparity and texture: the object's geometry, not its "
                  "identity",
                  representation=rep("owed at the producer", "owed", "owed"),
                  note="the producer has no entry anywhere; a stub would supply the signal and "
                       "destroy the payload check, which is the only thing making the edge "
                       "verifiable"),
             TYPED, PERCEPTUAL),
    Declared(Edge(far("lateral intraparietal area", DORSAL, sub="rostral part"), here(AIP),
                  "the priority map: which object is the current target",
                  representation=rep("one scalar per retinotopic location", "owed",
                                     "retinotopic"),
                  note="two-ended, and the two ends agree in the same words, which certifies less "
                       "than a diff of two independently written ends"),
             TYPED, PERCEPTUAL, certifies_nothing=True),
    Declared(Edge(far("lower-bank superior temporal sulcus / middle temporal gyrus", VIS), here(AIP),
                  "object identity, so the transformation here draws on ventral-stream identity as "
                  "well as dorsal-stream geometry",
                  representation=rep("owed at the producer", "owed", NO_FRAME),
                  note="the producer declares this edge, typed in the same words, so the edge is "
                       "two-ended and typed at both ends. It is Class 1 from a macaque retrograde "
                       "tracer study with the abstract only read and no full paper opened, so it is "
                       "declared at both ends and verified at neither; species and method travel "
                       "with the edge and are not promoted"),
             TYPED, PERCEPTUAL),
    Declared(Edge(far("secondary somatosensory cortex", SENSORIMOTOR_LOOP), here(AIP),
                  "tactile object identity and contact state",
                  representation=rep("owed", "owed", "owed"),
                  note="two-ended, confirmed: the producer declares this target by name and carries "
                       "no type for it, so the payload is this end's alone"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(far("ventral intraparietal area", DORSAL), here(AIP),
                  "object location and motion in head- and body-centred coordinates",
                  representation=rep("owed", "owed", "head- and body-centred"),
                  note="the producer declares this edge and types it in the same words, and adds "
                       "that it is the one edge out of that entry whose two ends agree"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(far("superior parietal area 5", SENSORIMOTOR_LOOP, sub="PE"), here(AIP),
                  "limb state: the arm and hand configuration against which the object's geometry "
                  "has to be expressed; payload otherwise owed",
                  representation=rep("owed", "owed", CONTESTED),
                  note="the frame is contested at the producer across body-, shoulder- and "
                       "hand-centred readings"),
             PARTLY_WRITABLE, SENSORIMOTOR),
    Declared(Edge(far("prefrontal areas 46 and 12", FRONTAL), here(AIP),
                  "goal / task context, owed", role=MODULATORY,
                  representation=UNTYPED,
                  note="both producers declare this edge by name. The dorsolateral entry declares "
                       "this target on its own line and not as a class; the ventrolateral entry "
                       "declares it from area 12 — so the pair supplies the area-46 / area-12 split "
                       "this line asserts from one side. Payload owed at all three ends: goal / "
                       "task context is a function and not a payload, and neither producer types it"),
             OWED, ASSOCIATION, compound_line=2),
    Declared(Edge(here(AIP), unstemmed("ventral premotor area F5"),
                  "a hand configuration: grip type, precision against whole-hand, and the wrist and "
                  "finger posture the object affords",
                  representation=rep("grip type is a category with two stated members; the posture "
                                     "has no stated units", "owed", "owed"),
                  note="onward to the primary motor cortex hand representation. The payload change "
                       "is a translation between ontologies — an object's physical properties go in "
                       "and a posture of the body comes out. Named and not typed: a payload that can "
                       "be described in a sentence is not thereby one that can be put on a wire"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(here(AIP), here(MIP),
                  "grasp-related object geometry into the reach channel, where the two "
                  "parieto-frontal channels actually meet",
                  representation=UNTYPED, note="payload owed at both ends"),
             OWED, SENSORIMOTOR),
    Declared(Edge(here(AIP), no_entry("the dorsal subdivision of V6A"),
                  "the same grasp-related object geometry",
                  representation=UNTYPED,
                  note="the far end has no entry, so this entry is open at both ends of the "
                       "geometry channel"),
             OWED, SENSORIMOTOR),

    # ---- medial intraparietal area ---------------------------------------
    Declared(Edge(no_entry("V6, and the ventral subdivision of V6A"), here(MIP),
                  "target location in the visual field, retinotopic",
                  representation=rep("owed at the producer", "owed", "retinotopic"),
                  note="this supplies the visual half of the frame mixture the output declares, so "
                       "the absent producer is not bookkeeping: the reach channel's visual input "
                       "has no producer anywhere, and the section head names V6A as the origin of "
                       "the whole channel"),
             TYPED, PERCEPTUAL, compound_line=2),
    Declared(Edge(far("primary somatosensory cortex, superior parietal area 5, primary motor cortex "
                      "and the medial motor fields", SENSORIMOTOR_LOOP), here(MIP),
                  "current arm configuration: the edge that makes the frame mixture possible",
                  representation=rep("owed", "owed", CONTESTED),
                  note="the frame is contested and this line does not assert body-centred. Reported "
                       "frames are body-, shoulder- and hand-centred across studies, and in area PE "
                       "a memorised target's distance is encoded relative to the initial hand "
                       "position. On the payload rule the frame is part of the payload, so this is "
                       "contested rather than owed — measured repeatedly, and the measurements "
                       "disagree. Four sources on one line; splitting owed"),
             CONTESTED, SENSORIMOTOR, compound_line=4),
    Declared(Edge(here(AIP), here(MIP), "grasp-related object geometry into the reach channel",
                  representation=UNTYPED, note="owed at both ends"),
             OWED, SENSORIMOTOR),
    Declared(Edge(far("ventral intraparietal area", DORSAL), here(MIP),
                  "body-centred locations, for reach",
                  representation=rep("owed", "owed", "body-centred"),
                  note="per the producer, whose end is more specific than this one"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(unstemmed("medial superior temporal area"), here(MIP), TO_DERIVE,
                  representation=UNTYPED, note="owed at both ends"),
             OWED, PERCEPTUAL),
    Declared(Edge(unstemmed("superior parietal area PEc"), here(MIP),
                  "spatial context and self-motion, owed",
                  representation=UNTYPED,
                  note="whether this and the area-5 output are one edge or two is owed"),
             OWED, SENSORIMOTOR),
    Declared(Edge(here(AG), here(MIP), TO_DERIVE, representation=UNTYPED,
                  note="owed; the producer is in this section and declares the output edge"),
             OWED, ASSOCIATION),
    Declared(Edge(here(PCUN), here(MIP), TO_DERIVE, representation=UNTYPED,
                  note="owed; the producer is in this section and declares the output edge"),
             OWED, ASSOCIATION),
    Declared(Edge(class_endpoint("temporo-parieto-occipital cortex"), here(MIP), TO_DERIVE,
                  representation=UNTYPED,
                  note="a class that does not resolve to a named region"),
             OWED, ASSOCIATION),
    Declared(Edge(far("cingulate area 23, dorsocaudal premotor area F2, and ventral premotor areas "
                      "F4 and F5", FRONTAL), here(MIP),
                  "owed — a return limb from the very areas the output edge targets",
                  representation=UNTYPED,
                  note="two of the three far ends declare it: the premotor entry declares this "
                       "target from F2 and from F4 and F5 as two separate bullets, split precisely "
                       "because they leave from different sub-elements, which are the sub-elements "
                       "this line names. The cingulate limb is untested — cingulate area 23 is "
                       "17_insula_claustrum_habenula's posterior cingulate cortex written as a "
                       "Brodmann number, which is how this cross-file edge stayed invisible as one. "
                       "Splitting is owed beyond tidiness: one line cannot carry three states"),
             OWED, ASSOCIATION, compound_line=3),
    Declared(Edge(here(MIP), far("dorsal premotor cortex", FRONTAL, sub="area F2"),
                  "a reach vector: direction and, more weakly, amplitude of an intended reach, "
                  "effector-specific for the arm and not the eye",
                  representation=rep("owed", "owed",
                                     "a mixture of gaze-centred, hand-centred and intermediate "
                                     "frames"),
                  note="onward to the primary motor cortex. The mixed frame is the declared frame "
                       "and not a missing one: the code genuinely is intermediate, and a consumer "
                       "assuming one pure frame will be wrong. The far end declares it by name, "
                       "terminating on F2, so the two ends name the same sub-element from both "
                       "sides; that end carries no type"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(here(MIP), far("superior parietal area 5", SENSORIMOTOR_LOOP, sub="PEa"),
                  TO_DERIVE, representation=UNTYPED,
                  note="two-ended: that entry's Inputs slot carries a four-source line including "
                       "this limb, naming the medial bank and area PEa in the same terms. The "
                       "reciprocal pair is closed and its limbs are not symmetric — the descending "
                       "limb carries limb state in a contested frame, this one has no typed payload "
                       "at all — and the asymmetry is the finding: the reach literature reads the "
                       "parietal-to-frontal direction and has not read this one"),
             OWED, SENSORIMOTOR),

    # ---- supramarginal gyrus ---------------------------------------------
    Declared(Edge(far("secondary somatosensory cortex", SENSORIMOTOR_LOOP), here(SMG),
                  "the object-level tactile payload: texture, shape and material, contact-point "
                  "invariant",
                  representation=rep("owed", "owed", "contact-point invariant"),
                  note="the producer declares this edge only inside its posterior parietal cortex "
                       "class and not by name, so this consumer is a located candidate for that "
                       "class and naming it is owed there"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(far("superior parietal area 5", SENSORIMOTOR_LOOP), here(SMG),
                  "body configuration",
                  representation=rep("owed", "owed", CONTESTED),
                  note="the far end was transcribed from this one, so the agreement certifies "
                       "nothing"),
             TYPED, SENSORIMOTOR, certifies_nothing=True),
    Declared(Edge(unstemmed("posterior superior temporal gyrus / Spt"), here(SMG),
                  "the auditory-to-motor mapping and phonological form",
                  representation=rep("owed", "owed", NO_FRAME),
                  note="far end in the auditory file, unchecked"),
             TYPED, PERCEPTUAL),
    Declared(Edge(unstemmed("medial superior temporal area"), here(SMG), TO_DERIVE,
                  representation=UNTYPED, note="owed at both ends"),
             OWED, PERCEPTUAL),
    Declared(Edge(unstemmed("lateral intraparietal area"), here(SMG),
                  "the priority (salience) map, ranking each location by behavioural priority",
                  representation=rep("one scalar per retinotopic location", "owed", "retinotopic"),
                  note=""),
             TYPED, PERCEPTUAL),
    Declared(Edge(unstemmed("middle temporal area"), here(SMG), "motion, owed",
                  representation=UNTYPED,
                  note="the producer declares nothing; its Outputs name no inferior parietal target"),
             OWED, PERCEPTUAL),
    Declared(Edge(far("ventrolateral prefrontal cortex", FRONTAL), here(SMG),
                  "task and articulatory context, owed", role=MODULATORY,
                  representation=UNTYPED,
                  note="reciprocal via the arcuate fasciculus and superior longitudinal fasciculus "
                       "III. The two prefrontal producers are in different states and must not be "
                       "carried as one judgement: the ventrolateral entry declares this target by "
                       "name, naming both tracts, while Broca's entry declares a temporoparietal "
                       "class and resolves this gyrus as its one named member — still a class, and "
                       "still the weaker state. Brodmann areas 44 and 45 are split across two "
                       "structures in that file and this line addresses them as one"),
             OWED, ASSOCIATION, compound_line=2),
    Declared(Edge(here(SMG), unstemmed("ventrolateral prefrontal / Broca and premotor cortex"),
                  "a praxis / action-sequence code, the learned structure of a skilled act, and on "
                  "the left a phonological code, the sound-form of words for the articulatory route",
                  representation=rep("none: the plan of a skilled action has no units", "owed",
                                     "none stated"),
                  note="two things this description can name and not type. Calling it a code does "
                       "not make it one — the first entry where the slot cannot be filled honestly, "
                       "and the detector working rather than failing. Splitting is owed: the two "
                       "codes go to different places and only one is left-lateralised"),
             PARTLY_WRITABLE, ASSOCIATION, compound_line=2),
    Declared(Edge(here(SMG), network("the ventral-attention frontoparietal network"),
                  "a reorienting signal: something behaviourally relevant just happened outside the "
                  "current focus",
                  representation=rep("one bit, plus a location", "{0, 1}; location owed",
                                     "the location's frame is owed"),
                  note="a one-bit interrupt with a location attached, as far as this description "
                       "can determine. The endpoint is a network and does not resolve. Its frontal "
                       "candidate exists and the endpoint still does not resolve, which is the "
                       "finding: 11_frontal_lobe's right inferior frontal gyrus declares a right "
                       "temporoparietal class of its own, this entry's Function names the "
                       "right-dominant temporoparietal junction, and neither end names the other "
                       "structure. Two unresolved classes that point at each other are not an edge. "
                       "Also checked: that entry declares no parietal input of any kind, and the "
                       "nearest resolved candidate, the insula in 17_insula_claustrum_habenula, "
                       "declares ten inputs and not one is parietal"),
             TYPED, SENSORIMOTOR),
    Declared(Edge(here(SMG), unstemmed("lateral intraparietal area"), TO_DERIVE,
                  representation=UNTYPED,
                  note="owed, asserted at the consumer's end with no independent support here, and "
                       "marked: nothing read establishes that this projection exists. Written at "
                       "this end so the edge would have two ends, and the far end records that the "
                       "producer declares the opposite direction instead"),
             OWED, ASSOCIATION, single_ended_origin=True, certifies_nothing=True),

    # ---- angular gyrus ---------------------------------------------------
    Declared(Edge(unstemmed("occipitotemporal cortex"), here(AG),
                  "object and face identity, and note what has already been discarded upstream: no "
                  "hue",
                  representation=rep("owed", "owed", NO_FRAME),
                  note="the producer declares nothing and nothing searched established the edge, so "
                       "it is open at both ends"),
             TYPED, PERCEPTUAL),
    Declared(Edge(unstemmed("superior temporal sulcus"), here(AG), "word and sound identity",
                  representation=rep("owed", "owed", NO_FRAME), note="far end unchecked"),
             TYPED, PERCEPTUAL),
    Declared(Edge(class_endpoint("somatosensory association cortex"), here(AG),
                  "tactile object identity", representation=UNTYPED,
                  note="both producers declare only a class and neither names this area"),
             UNKNOWN_OWED, SENSORIMOTOR),
    Declared(Edge(far("lateral intraparietal area", DORSAL, sub="ventral subdivision"), here(AG),
                  "the priority (salience) map: bottom-up salience plus top-down attention plus "
                  "reward, modality-free",
                  representation=rep("one scalar per retinotopic location", "owed", "retinotopic"),
                  note="the one input to this entry whose payload is fully typed. The producer "
                       "declares it in the same words and adds that the map leaves from the ventral "
                       "subdivision and not the whole area, so reading it as coming from the whole "
                       "area is reading half the area"),
             TYPED, PERCEPTUAL, certifies_nothing=True),
    Declared(Edge(unstemmed("hippocampal formation"), here(AG),
                  "a completed episode: the bound, retrievable pattern, addressable by any fragment "
                  "of itself",
                  representation=rep("none: an episode has no units", "owed",
                                     "none — content-addressable"),
                  note="the one checkable property in hand is that it is content-addressable, which "
                       "the identity codes on the other inputs are not"),
             PARTLY_WRITABLE, ASSOCIATION),
    Declared(Edge(far("posterior cingulate cortex", INSULA), here(AG), TO_DERIVE,
                  representation=UNTYPED,
                  note="two-ended and confirmed: the producer sorts this edge with the precuneus "
                       "and the medial prefrontal cortex into the same default-mode group this "
                       "entry lists it in — two files grouping the same three edges the same way, "
                       "from their own sides. Payload owed at both ends"),
             OWED, ASSOCIATION),
    Declared(Edge(here(PCUN), here(AG), TO_DERIVE, representation=UNTYPED,
                  note="owed at both ends, both ends in this section"),
             OWED, ASSOCIATION),
    Declared(Edge(far("medial prefrontal cortex", FRONTAL), here(AG), TO_DERIVE,
                  representation=UNTYPED,
                  note="owed as an absence at the producer: that file's orbitofrontal / ventromedial "
                       "entry declares ten outputs and not one is medial-parietal. The traffic "
                       "between that structure and this one runs one way, parietal to prefrontal"),
             OWED, ASSOCIATION),
    Declared(Edge(here(AG), network("default-mode partners, the hippocampal formation, "
                                    "ventrolateral prefrontal cortex, lateral temporal semantic "
                                    "cortex"),
                  TO_DERIVE, representation=UNTYPED,
                  note="PAYLOAD UNKNOWN — OWED, AND THIS IS THE LOUD ONE. The Function says this "
                       "region binds across modalities and over time into concepts and events; that "
                       "sentence reads as complete right up until you try to say what leaves it on "
                       "a wire, and then it fails — a concept and an event have no units, no range, "
                       "no coordinate frame and no channel structure. The four far ends are in "
                       "three states: 11_frontal_lobe's ventrolateral prefrontal entry declares "
                       "this source by name so that member is two-ended and untyped, the "
                       "hippocampal and lateral-temporal members are untested, and the fourth is a "
                       "network. A fifth consumer exists that this line does not name — that file's "
                       "orbitofrontal / ventromedial entry declares this source, marked Medial — so "
                       "the class has a consumer waiting on it and splitting is owed"),
             UNKNOWN_OWED, ASSOCIATION, compound_line=4),
    Declared(Edge(here(AG), unstemmed("lateral intraparietal area"), TO_DERIVE,
                  representation=UNTYPED,
                  note="owed, asserted at the consumer's end, Class 2, and no primary source names "
                       "it. Written at this end so the edge would have two ends"),
             OWED, ASSOCIATION, single_ended_origin=True, certifies_nothing=True),
    Declared(Edge(here(AG), here(MIP), TO_DERIVE, representation=UNTYPED,
                  note="owed, asserted at the consumer's end — but unlike the lateral intraparietal "
                       "edge this one does carry a primary source there"),
             OWED, ASSOCIATION, single_ended_origin=True),

    # ---- precuneus -------------------------------------------------------
    Declared(Edge(far("superior parietal area 5", SENSORIMOTOR_LOOP), here(PCUN),
                  "body configuration and spatial layout",
                  representation=rep("owed", "owed", "body-centred here, contested at the producer"),
                  note="the producer holds the frame unsettled across body-, shoulder- and "
                       "hand-centred readings, so the two ends disagree about the payload and not "
                       "about wording"),
             CONTESTED, SENSORIMOTOR),
    Declared(Edge(class_endpoint("dorsal-stream visual areas"), here(PCUN),
                  "spatial layout, otherwise owed", representation=UNTYPED,
                  note="a class that does not resolve, and none of the four dorsal-stream entries "
                       "declares an output here"),
             PARTLY_WRITABLE, PERCEPTUAL),
    Declared(Edge(far("posterior cingulate cortex", INSULA), here(PCUN), TO_DERIVE,
                  representation=UNTYPED,
                  note="two-ended and confirmed, the producer marking it two-ended by name in the "
                       "same terms; payload owed at both ends"),
             OWED, ASSOCIATION),
    Declared(Edge(far("retrosplenial cortex", INSULA), here(PCUN),
                  "the return arm of the spatial-memory loop: heading and landmark information "
                  "after the egocentric-to-allocentric translation",
                  representation=rep("owed", "owed", "allocentric, after translation"),
                  note="two-ended and confirmed, and not untyped at both ends: both ends carry the "
                       "same partial type and each marks the remainder owed, so what is owed is the "
                       "rest of the payload and not the whole of it. This edge matters more than an "
                       "added line usually does — the entry's headline function is scene "
                       "construction and the producer is where the frame translation that depends "
                       "on lives, and the producer independently records this entry as the one "
                       "consumer whose headline function the edge could supply"),
             PARTLY_WRITABLE, ASSOCIATION),
    Declared(Edge(here(AG), here(PCUN), TO_DERIVE, representation=UNTYPED,
                  note="owed, and the producer marks its own output payload the loudest owed in "
                       "the file"),
             OWED, ASSOCIATION),
    Declared(Edge(far("medial prefrontal cortex", FRONTAL), here(PCUN), TO_DERIVE,
                  representation=UNTYPED,
                  note="owed, and declares nothing is exact here: that file's orbitofrontal / "
                       "ventromedial entry carries no output to this structure under any name while "
                       "declaring an input from it. The reciprocal pair is open in one direction "
                       "and the open direction is the return one"),
             OWED, ASSOCIATION),
    Declared(Edge(class_endpoint("medial temporal lobe"), here(PCUN), TO_DERIVE,
                  representation=UNTYPED,
                  note="owed; the producer declares a class that covers this area without naming it"),
             OWED, ASSOCIATION),
    Declared(Edge(here(PCUN), far("posterior cingulate cortex", INSULA), TO_DERIVE,
                  representation=UNTYPED,
                  note="two-ended and confirmed, and this is the return limb the consumer's own "
                       "entry names. The reciprocal pair is closed and both limbs are untyped, "
                       "which is a different state from the pair being open. Self-referential "
                       "processing, first-person perspective and scene construction are functions, "
                       "not payloads"),
             UNKNOWN_OWED, ASSOCIATION),
    Declared(Edge(here(PCUN), here(AG), TO_DERIVE, representation=UNTYPED,
                  note="the consumer is in this section and declares it, also owed there"),
             UNKNOWN_OWED, ASSOCIATION),
    Declared(Edge(here(PCUN), here(MIP), TO_DERIVE, representation=UNTYPED,
                  note="owed, asserted at the consumer's end in this section, with a primary source "
                       "there"),
             OWED, ASSOCIATION, single_ended_origin=True),
    Declared(Edge(here(PCUN), far("medial prefrontal cortex and the medial temporal lobe", FRONTAL),
                  TO_DERIVE, representation=UNTYPED,
                  note="the prefrontal half is declared at its far end — that file's orbitofrontal "
                       "/ ventromedial entry declares this source, marked Medial — and the medial temporal half is untested, its far end unchecked. So the "
                       "splitting this line owes is forced: one target declares the edge and the "
                       "other is unchecked, and no single judgement describes both"),
             UNKNOWN_OWED, ASSOCIATION, compound_line=2),
    Declared(Edge(here(PCUN, sub="anterior sensorimotor sector"),
                  far("superior parietal area 5 and premotor cortex", SENSORIMOTOR_LOOP),
                  "reach and body-configuration signals",
                  representation=rep("owed", "owed", "body-centred"),
                  note="the one edge out of this entry whose payload can be written, and the one "
                       "coupled to area 5 rather than to the default-mode network. The area-5 end "
                       "was transcribed from this one and certifies nothing; the premotor end does "
                       "declare it, naming the anterior sensorimotor sector in this line's own "
                       "words, and that end is untyped — so the far ends supply the declaration and "
                       "not the payload, and the payload is written here only. Splitting is owed: "
                       "the two targets are in different files and in different states"),
             TYPED, SENSORIMOTOR, certifies_nothing=True, compound_line=2),
)

# The three coordinate-change holes the rung above says are one problem, not three.
COORDINATE_CHANGE_HOLES = (
    "anterior intraparietal area — the transform: object geometry in, hand posture out",
    "medial intraparietal area — the frame mixture: two frames in, a mixture out",
    "ventral intraparietal area (04_dorsal_visual_parietal_stream) — the gain-field mechanism",
)

# A property the Function slot consumes that no edge supplies.
DANGLING_REQUIREMENTS = {
    "anterior intraparietal area":
        "the transform itself. Object geometry arrives typed and a hand configuration leaves named, "
        "and nothing at any rung says what happens between them. The strong form: both ends are "
        "described and the step between them is not, so the gap is exactly one function wide and "
        "its signature is known",
    "medial intraparietal area / parietal reach region":
        "the frame mixture. Two incoming edges supply the two frames — the visual one from V6 and "
        "the ventral subdivision of V6A, the postural one from the somatosensory and motor areas — "
        "and no internal edge says where they meet. Worse than a missing mechanism alone, because "
        "the visual limb's producer has no entry either: the mixture lacks both a mechanism and one "
        "of its two operands",
    "supramarginal gyrus":
        "the somato-to-praxis conversion, and this entry is strictly worse off than the grasp one. "
        "Its output payload is not writable either, so the gap has no signature — a module could "
        "not state what the missing operation would have to return — and the entry fails the "
        "completion test at both the transform and the output, on a structure whose count is also "
        "unknown",
    "angular gyrus":
        "the PGa-to-PGp edge. The Function claims binding across modalities and over time; the "
        "attentional and mnemonic streams arrive on different divisions by the gradient account; so "
        "the binding, if it happens here, happens on an edge between the two divisions, and that "
        "edge is not written in either direction. It cannot be stated as a gap in the ordinary way, "
        "because the substrate it would run on is not known to be a place",
    "precuneus":
        "the inter-sector edge. No edge between any two of the three sectors is recorded, in either "
        "direction, while the Function claims scene construction and visuospatial imagery — which "
        "would have to combine the posterior visual sector's content with the central sector's "
        "retrieved episodic content",
}

# Figures that may not be promoted into a width or an array size at this rung.
MEASUREMENT_CAUTIONS = (
    ("association-cortex packing of order 20,000 neurons/mm3 at the supramarginal gyrus",
     "one factor of a count and not a count: the grey-matter volume slot reads unknown, so "
     "multiplying it into an array size would require a number nobody has"),
    ("~15M neurons at the anterior and medial intraparietal areas",
     "analogies and not measurements, drawn from the lateral ~20M and ventral ~12M counts in 04_dorsal_visual_parietal_stream, which are right as quoted there. They may not be quoted as "
     "measured, and the two structures are not thereby the same size as each other for any "
     "biological reason"),
    ("the lateral ~20M and ventral ~12M figures the analogy rests on",
     "carried from another file at second hand; no source was opened for them in this section"),
)


# --------------------------------------------------------------------------
# Forward operation.
#
# The specified part is writable for every population here and three of its four
# terms are unset.  The operation itself is not in question: every population is a
# threshold gate and none is described as doing anything else.
# --------------------------------------------------------------------------


def threshold_gate(counts, thresholds):
    """Fire where the summed input reaches the stored threshold.

    count[j] = sum over fan_in(j) of sign(i, j) * active_source[i]
    active[j] = count[j] >= threshold[j]

    This is the second half only.  The sum is the caller's, because sign() is unset
    and a bare sum would silently assert that every input is excitatory.
    """
    if len(counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(counts, thresholds)]


def sign(source_sub, target_sub):
    """The sign an internal or incoming edge contributes with.

    Not set at any rung.  The internal block requires it: 6a -> 4 and 6a -> 5a are
    stated to carry opposite signs, so at least one internal edge is subtractive, and
    how an inhibitory contribution combines with an excitatory one in the sum is
    stated nowhere.
    """
    raise NotImplementedError(
        "sign arithmetic is not set at any rung; the internal block states that 6a -> 4 and "
        "6a -> 5a carry opposite signs and does not say which sign is which, nor how the two "
        "combine in one sum"
    )


def fan_in_map(structure: Structure, subelement: str | None = None):
    """Which source lines converge on each neuron.

    Connection topology is unset at every rung and requires explicit agreement before
    it is touched.  And the declared edge set may exceed the anatomy: two edges were
    written at this end so that a one-ended declaration would have a second end, with
    no source naming either.  An edge written to make a diff pass has evidence on
    neither side, and the diff it passes is the very check that would have caught it.
    A surplus edge runs and produces output, which is what makes this harder to find
    than a missing one.
    """
    bad = [d for d in EDGES if d.single_ended_origin and d.certifies_nothing]
    raise NotImplementedError(
        "inter-structure connection topology is not set, and " + str(len(bad)) +
        " edges exist only because the other end declared them: " +
        "; ".join(d.label for d in bad)
    )


def order_internal_block(structure: Structure):
    """Put the internal block's edges in the order they are evaluated.

    Refused.  Two edges are within-sub-element recurrence and one closes the 5a to 2/3
    loop, and each reads an activity value that the same update writes.  Choosing
    whether the read takes this update's value or the previous one is choosing the
    scheduling discipline, which is not this rung's to make.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set, so the internal block is carried as edges and not "
        "ordered: " + ", ".join(f"{a} -> {b}" for a, b in RECURRENT) +
        " each read a value the same update writes"
    )


def transform(structure: Structure, *args, **kwargs):
    """Place the operation the structure's Function requires between its arrays.

    Not implementable anywhere in this section, and the reason differs by structure.
    At the anterior intraparietal area both ends are described and the step between
    them is not, so the gap is one function wide with a known signature.  At the
    supramarginal gyrus the output is not typed either, so the gap has no signature.
    At the angular gyrus the missing edge is internal to a division that may not exist.

    Three of the five are one problem in three places, not three problems, and
    reporting them separately would hide that.
    """
    raise NotImplementedError(f"{structure.name}: {DANGLING_REQUIREMENTS[structure.name]}")


def resolve_network_endpoint(declared: Declared):
    """Resolve an edge whose target is a network into the regions it terminates on.

    Refused, and the refusal is the point.  A network is a set of regions defined by
    correlated activity rather than by a projection, so naming its members turns one
    edge into several and asserts that each member receives the same payload, which is
    not what a network claim says.  Marking it leaves the arity visibly unknown rather
    than silently multiplied.
    """
    raise NotImplementedError(
        f"{declared.label}: the target is a network, not a region. Naming the members would "
        f"manufacture the arity, and how an edge to a network is written is open at the source"
    )


def allocate(structure: Structure, subelement: str | None = None):
    """Size the threshold and activity arrays.

    Two structures allocate and three refuse, and where a figure is returned the basis
    travels with it: a count and an analogy behave identically in arithmetic, so a
    caller must not be able to obtain the size without the caveat.

    No sub-element allocation succeeds anywhere in this section, and the refusals are
    not interchangeable — one of them fails for a reason no count would fix.
    """
    if subelement is None:
        p = structure.populations[0]
        if p.count is None:
            raise NotImplementedError(
                f"{structure.name} carries no neuron count, so no array can be sized for it — "
                f"{UNPRICED_BECAUSE[structure.name]}"
            )
        return {"structure": structure.name,
                "neurons": p.count,
                "threshold_bits": p.threshold_bits,
                "threshold_bytes": p.parameter_bytes,
                "active_bytes": p.count // 8,
                "count_basis": COUNT_BASIS.get(structure.name, "")}

    if subelement not in structure.subelements:
        raise ValueError(f"{subelement!r} is not a sub-element of {structure.name}")

    for axis in AXES[structure.name]:
        if axis.state == GRADIENT_NOT_PARTITION and subelement in ("PGa", "PGp"):
            raise NotImplementedError(
                f"{structure.name} states no count for {subelement!r}, and a count would not be "
                f"enough: the {axis.name} axis is a {axis.state}. {axis.note}"
            )
    raise NotImplementedError(
        f"{structure.name} states no count for {subelement!r}. No divisional axis in this section "
        f"is sized: none per medial-intraparietal division under either parcellation, none per "
        f"supramarginal architectonic area, none for PGa or PGp, none per precuneus sector"
    )


def edge_storage(declared: Declared):
    """Values in flight on one edge, which the per-edge-latency invariant creates.

    line_count * ceil(latency / update_interval) * bytes_per_value, and in this section
    every term is unavailable on every edge.  The design rung expects one unset term,
    the update interval; here there are four, and the entry records them rather than
    estimating past them, because a figure computed from assumed terms enters the file
    looking exactly like a derived one.  Never summed with parameter memory or state.
    """
    r = declared.edge.representation
    missing = []
    if declared.edge.fan_out is None:
        missing.append("line_count: fan-in is to derive and no axon count is stated")
    if declared.edge.latency_s is None:
        missing.append("latency: to derive, on every edge in this section")
    missing.append("update_interval: unset, and waiting on the scheduling discipline")
    if r.units in OPEN_STATES or not r.units:
        missing.append("bytes_per_value: the payload is not typed, so its width is unknown")
    value = cfg.edge_storage_bytes(declared.edge.fan_out, declared.edge.latency_s, None, None)
    if value is None:
        raise NotImplementedError(f"{declared.label}: " + "; ".join(missing))
    return value


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    No parameter in this section changes.  That is recorded rather than assumed: an
    entry may record that the rule is not set, and may not quietly choose one.
    """
    raise NotImplementedError("no learning rule is set, and it is not this rung's to choose")


def step(*args, **kwargs):
    """There is no step.  The scheduling discipline is not set and is not this rung's."""
    raise NotImplementedError("the scheduling discipline is not set")


# --------------------------------------------------------------------------
# Derived reporting.  Every figure is recomputed here, never transcribed.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    out = [cfg.sizing_report(STRUCTURES, "posterior parietal — parameter memory"), ""]
    for s in STRUCTURES:
        p = s.populations[0]
        if p.count is None:
            out.append(f"  {s.name}: unpriced — {UNPRICED_BECAUSE[s.name]}")
        else:
            out.append(f"  {s.name}: {p.count/1e6:.0f}M is an ANALOGY, not a measurement — "
                       f"{COUNT_BASIS[s.name]}")
            out.append(f"      activity bitmap {p.count/8/1e6:.3f} MB, "
                       f"threshold store {p.parameter_bytes/1e6:.2f} MB")
    out.append("")
    out.append("  state memory and edge storage are not in this total and are never summed with it")
    out.append("  memory is a derived requirement, not a limit to design against: nothing here is "
               "capped or simplified because a figure looks large")
    out.append(f"  {HEMISPHERIC_ASSUMPTION}")
    return "\n".join(out)


def payload_boundary_report() -> str:
    """The section's characteristic finding: the untyped edges are not scattered."""
    typed = [d for d in EDGES if d.payload_state == TYPED]
    untyped = [d for d in EDGES if d.payload_state != TYPED]
    out = [f"  edges: {len(EDGES)}    typed: {len(typed)}    not typed: {len(untyped)}"
           f"    ({100*len(typed)/len(EDGES):.1f}% typed)"]
    states: dict[str, int] = {}
    for d in EDGES:
        states[d.payload_state] = states.get(d.payload_state, 0) + 1
    for st, n in sorted(states.items(), key=lambda kv: -kv[1]):
        out.append(f"      {st:30} {n:>3}")
    out.append("")
    out.append("  by content class, which is where the boundary lies:")
    for cls in (SENSORIMOTOR, PERCEPTUAL, ASSOCIATION):
        t = sum(1 for d in typed if d.content_class == cls)
        u = sum(1 for d in untyped if d.content_class == cls)
        out.append(f"      {cls:28} typed {t:>3}   not typed {u:>3}")
    out.append("  a rate distributed at random would be a coverage problem, closed by more of the "
               "same work; a boundary with a location is a claim about where the description stops")
    out.append("  and the implication runs one way only: no association payload is typed, while "
               "sensorimotor and perceptual lines appear on both sides — association coupling is "
               "sufficient for an untypable payload here and is not necessary for one")
    ins = [d for d in EDGES if d.edge.target.name == AG]
    outs = [d for d in EDGES if d.edge.source.name == AG]
    out.append(f"  the angular gyrus is where it is sharpest: "
               f"{sum(1 for d in ins if d.payload_state == TYPED)} of {len(ins)} inputs typed, "
               f"{sum(1 for d in outs if d.payload_state == TYPED)} of {len(outs)} outputs typed")
    return "\n".join(out)


def _is_open(value: str) -> bool:
    """True where a representation slot names a state rather than a value.

    A slot may be open inside a sentence as well as on its own — "owed at the producer"
    is as open as "owed" — so this looks for the state word anywhere in the string
    rather than only at the start.
    """
    low = value.lower()
    return value in OPEN_STATES or any(w in low for w in
                                       ("owed", "unknown", "contested", "to derive", "not stated"))


def representation_disagreement_report() -> str:
    """Where the state word from the rung above and this rung's own field disagree.

    Two records of one thing, kept apart on purpose.  The state word is copied from
    above; the representation is written here.  Reconciling them would leave one record
    standing for two readings, so the disagreement is printed instead.
    """
    out = []
    for d in EDGES:
        r = d.edge.representation
        gaps = [n for n, v in (("units", r.units), ("range", r.value_range), ("frame", r.frame))
                if _is_open(v)]
        if d.payload_state == TYPED and gaps:
            out.append(f"  {d.label[:66]:66} state=typed, but {','.join(gaps)} not filled")
    head = (f"  lines the rung above calls typed whose representation is still open: {len(out)}\n"
            f"  a typed payload is not the same as a fully declared line; this is the gap between "
            f"them, and it is the check the Representation field exists to give")
    return "\n".join([head] + out)


def axis_status_report() -> str:
    out = []
    for s in STRUCTURES:
        for a in AXES[s.name]:
            if a.state in (GRADIENT_NOT_PARTITION, INCOMPATIBLE_PARCELLATIONS):
                out.append(f"  {s.name} / {a.name}: {a.state}")
    out.append("  an unmeasured extent is an axis that exists with its length open; PGa/PGp is "
               "different in kind, because the axis's existence is open and no count would close "
               "it — whether an edge can terminate on PGa is a question about whether PGa is a place")
    out.append("  and if it is a partition it sorts six input edges, so resolving it would change "
               "the arity of six edges at once")
    out.append("  three further entries hold two or three incompatible parcellations of one tissue "
               "side by side, and the description chooses none")
    return "\n".join(out)


def network_endpoint_report() -> str:
    e = [d for d in EDGES if NETWORK_ENDPOINT in (d.edge.source.kind, d.edge.target.kind)]
    out = [f"  edges whose target is a network rather than a region: {len(e)}"]
    for d in e:
        out.append(f"      {d.label}")
    out.append("  a network is a set of regions defined by correlated activity, not by a "
               "projection; naming the members turns one edge into several and asserts that each "
               "member receives the same payload, which is not what the network claim says")
    out.append("  Brain_config carries no endpoint kind for this, so its edge_report does not "
               "count these; adding one there is owed")
    return "\n".join(out)


def single_ended_origin_report() -> str:
    written = [d for d in EDGES if d.single_ended_origin]
    fabricated = [d for d in written if d.certifies_nothing]
    transcribed = [d for d in EDGES if d.certifies_nothing and not d.single_ended_origin]
    out = [f"  edges written so the edge would have two ends: {len(written)}, of which "
           f"{len(fabricated)} have no primary source at either end"]
    for d in fabricated:
        out.append(f"      {d.label}   (nothing read establishes that this projection exists)")
    out.append(f"  payloads transcribed from a far end rather than written independently: "
               f"{len(transcribed)}")
    for d in transcribed:
        out.append(f"      {d.label}")
    out.append("  such agreement certifies nothing, because that end was transcribed from this one")
    out.append("  an edge written to make a diff pass has evidence on neither side, and the diff "
               "it passes is the check that would have caught it")
    return "\n".join(out)


def dangling_requirement_report() -> str:
    out = [f"  stated functions with no declared substrate: {len(DANGLING_REQUIREMENTS)}"]
    for s in STRUCTURES:
        out.append(f"      {s.name}:")
        out.append(f"          {DANGLING_REQUIREMENTS[s.name]}")
    out.append("  and three of them are one problem, not three:")
    for h in COORDINATE_CHANGE_HOLES:
        out.append(f"      {h}")
    out.append("  three neighbouring entries whose stated function is a coordinate change, and "
               "none of the three can say where the change happens")
    return "\n".join(out)


def missing_producer_report() -> str:
    absent = [d for d in EDGES if cfg.NO_ENTRY in (d.edge.source.kind, d.edge.target.kind)]
    classes = [d for d in EDGES if cfg.CLASS_ENDPOINT in (d.edge.source.kind, d.edge.target.kind)]
    unread = [d for d in EDGES if cfg.UNSTEMMED in (d.edge.source.kind, d.edge.target.kind)]
    out = [f"  endpoints named here with no entry in any file the pass read: "
           f"{len(MISSING_PRODUCERS)}"]
    for m in MISSING_PRODUCERS:
        out.append(f"      {m}")
    out.append(f"  edges touching them: {len(absent)}")
    for d in absent:
        out.append(f"      {d.label}")
    out.append("  the section head names V6A as the origin of the whole reach channel, so the reach "
               "channel is described from its second stage onward and its visual input has no "
               "producer; these are visual and visuomotor cortex, plainly in scope, and absent")
    out.append("  a stub could drive the input and would destroy the check: the payload rule makes "
               "an edge checkable by writing it twice, and a consumer whose producer has no entry "
               "has a payload nobody can diff")
    out.append(f"  endpoints naming a class rather than a structure: {len(classes)}")
    for d in classes:
        out.append(f"      {d.label}")
    out.append(f"  endpoints whose far file is unchecked against this one, so no stem: "
               f"{len(unread)}   (unchecked, not a claim that no far end exists)")
    return "\n".join(out)


def compound_line_report() -> str:
    c = [d for d in EDGES if d.compound_line > 1]
    out = [f"  edge lines naming more than one endpoint, splitting owed: {len(c)}"]
    for d in c:
        out.append(f"      {d.compound_line} endpoints: {d.label}")
    return "\n".join(out)


def laminar_report() -> str:
    out = [f"  internal block edges carried per structure: {len(INTERNAL_BLOCK)}"]
    for a, b, sgn, why in INTERNAL_BLOCK:
        out.append(f"      {a:>4} -> {b:<4} {sgn:<10} {why}")
    out.append(f"  of these, reading a value the same update writes: "
               f"{', '.join(f'{a} -> {b}' for a, b in RECURRENT)}")
    out.append("  all five structures are granular association isocortex and all five take the "
               "same eight laminae, and the set stays a per-structure field: the value is not "
               "uniform across the map, and a field that happens to hold one value is still a field")
    out.append("  the medial intraparietal area's two bands of Baillarger belong to the fibre "
               "plexus in layers 4 and 5b, so they are a property of the lamina axis and not a "
               "population to allocate")
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
    print("\nedges:")
    print(cfg.edge_report([d.edge for d in EDGES]))
    print("\nthe payload boundary, and it has a location:")
    print(payload_boundary_report())
    print("\nrepresentation against the state word from above:")
    print(representation_disagreement_report())
    print("\naxes, one of which is not known to be an axis:")
    print(axis_status_report())
    print("\ntargets that are not nodes:")
    print(network_endpoint_report())
    print("\nedges that exist because the other end declared them:")
    print(single_ended_origin_report())
    print("\nstated functions with no declared substrate:")
    print(dangling_requirement_report())
    print("\nproducers that do not exist, and endpoints that do not resolve:")
    print(missing_producer_report())
    print("\ncompound lines:")
    print(compound_line_report())
    print("\nthe internal laminar block:")
    print(laminar_report())
    print("\nmeasurements that must not be promoted:")
    print(measurement_caution_report())
    print()
    for fn, label, args in ((sign, "sign", (None, None)),
                            (fan_in_map, "connectivity", (ANGULAR_GYRUS,)),
                            (order_internal_block, "block order", (ANGULAR_GYRUS,)),
                            (transform, "transform", (ANTERIOR_INTRAPARIETAL,)),
                            (learn, "learning", ()), (step, "scheduler", ())):
        try:
            fn(*args)
        except NotImplementedError as exc:
            print(f"{label:16} blocked: {exc}")
    for d in EDGES:
        if NETWORK_ENDPOINT in (d.edge.source.kind, d.edge.target.kind):
            try:
                resolve_network_endpoint(d)
            except NotImplementedError as exc:
                print(f"{'network target':16} blocked: {exc}")
            break
    try:
        edge_storage(EDGES[0])
    except NotImplementedError as exc:
        print(f"{'edge storage':16} blocked: {exc}")
    for st, sub in ((ANGULAR_GYRUS, None), (SUPRAMARGINAL_GYRUS, None), (PRECUNEUS, None),
                    (ANGULAR_GYRUS, "PGa"), (MEDIAL_INTRAPARIETAL, "dorsal part")):
        try:
            allocate(st, sub)
        except NotImplementedError as exc:
            print(f"{'allocation':16} blocked: {exc}")
    print()
    for st in (ANTERIOR_INTRAPARIETAL, MEDIAL_INTRAPARIETAL):
        a = allocate(st)
        print(f"allocation ok: {a['structure']}: {a['neurons']:,} neurons, "
              f"{a['threshold_bits']} bits, {a['threshold_bytes']/1e6:.2f} MB thresholds, "
              f"{a['active_bytes']/1e6:.3f} MB activity  [count basis: analogy]")
