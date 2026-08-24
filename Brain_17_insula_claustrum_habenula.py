"""Brain 17 — insula, claustrum, habenula, cingulate remainder.

The salience / interoception / value-brake / limbic-midline wall: the insula's
interoceptive-to-salience gradient, the claustrum, the habenula's value brake, and
the midcingulate, posterior cingulate and retrosplenial cortices.

WHAT THIS MODULE IS
-------------------
It carries the section's contract and refuses to run.  Every structure here is a
threshold gate over equal-weight inputs, and the forward operation is writable:

    count[j]  = sum over i in fan_in(j) of active_source[i]
    active[j] = count[j] >= threshold[j]

There is almost nothing to run it on.  No structure in the section has a neuron
count, every fan-in is unknown, all edge latencies are undetermined, and 49 of the
74 inter-region edge declarations carry a payload that is owed.  Four operations
the section's biology requires are blocked in four different ways, and each raises
with its own reason rather than being approximated.

The refusals are the point.  A module that guessed a count, a topology or an update
interval would run, and what it computed would be a property of the guess.

NO HISTORY IN THIS FILE
-----------------------
No versions, no revision numbers, no "changed since", no provenance, no changelog,
no "formerly", no commented-out prior version.  A file that carries its own past
gives a reader two truths and no way to tell which is live.  When code here is
edited, its comment is updated in the same edit.

Comments explain the biological basis, and where relevant the compute or memory
tradeoff.  No hardware is named anywhere: the architecture sizes the hardware, not
the reverse.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Iterable


# ---------------------------------------------------------------------------
# Slot states, copied from the rungs above rather than translated.
#
# The rung above distinguishes these because each names a different repair, and
# collapsing them into a single "to derive" would make a claim the description
# does not make: over NOT_APPLICABLE it asserts something is there to derive,
# over RESISTED it discards a result, over CONTESTED it asserts nobody has looked
# when the problem is that several people have and disagree.
# ---------------------------------------------------------------------------

class SlotState(Enum):
    CONTENT = "content"
    NOT_APPLICABLE = "not applicable"   # a positive statement about the tissue
    UNKNOWN = "unknown"                 # exists, not measured — an experiment to run
    OWED = "owed"                       # described, not typed — known what research
    RESISTED = "resisted"               # decoded, yielding no shared format
    CONTESTED = "contested"             # measured several ways, needing adjudication
    TO_DERIVE = "to derive"             # the source has not supplied it


class CountState(Enum):
    """Refinement of the source's ``soft / unknown`` neuron slot.

    Claude's reading, offered to be checked.  Carried alongside the source's own
    state, never in place of it, so the refinement cannot absorb the original.
    """
    UNCOUNTED_TISSUE_CLASS = (
        "association / paralimbic cortex, uncounted per-region in human; "
        "the repair is a stereology programme and it covers four structures at once"
    )
    SEGMENTATION_LIMITED = (
        "the boundary cannot be drawn reliably on a thin sheet; "
        "the repair is a method, not a measurement"
    )
    MEASURED_NOT_AS_CONTROL_ABSOLUTE = (
        "human stereology exists and reports volumes and disease-related changes "
        "rather than a control absolute; the cheapest repair in the section"
    )


class PayloadShape(Enum):
    """Four distances from a type, kept apart because they are four states."""
    OWED = "owed — the slot reads 'payload unknown, owed' and nothing else"
    NAME_ONLY = "a phrase with no units, no range and no frame"
    PARTIAL_TYPE = "some of the property, units or frame stated"
    STATED_ABSENCE = "checkable by what it explicitly does not carry"
    PROPERTY_IN_PLACE_OF_TYPE = "no units and no frame; a property makes it checkable"


class EndpointKind(Enum):
    REGION_WITH_ENTRY = "a named region with an entry of its own"
    REGION_NO_ENTRY = "a named region with no entry in any of the twenty files"
    CLASS = "a class, not a region — an edge pointing at one cannot be checked"
    NETWORK = "a set of regions defined by correlated activity, not by a projection"


class FarEnd(Enum):
    TWO_ENDED = "the far end declares this edge"
    DECLARES_NO_SUCH_EDGE = "the far end has an entry and does not declare this edge"
    NOT_CONFIRMED = "the far end was not read"
    NO_ENTRY = "the far end has no entry anywhere"
    UNRESOLVED_ARITY = "declared at the far end inside a compound line of unresolved arity"


class Direction(Enum):
    IN = "in"
    OUT = "out"
    INTERNAL = "internal"


class Blocked(RuntimeError):
    """Raised where running would require a decision the description has not made.

    Carries the item that is missing and the rung that owns the repair, so a caller
    can tell a research gap from an unmade decision without reading the source.
    """

    def __init__(self, operation: str, missing: str, owner: str) -> None:
        super().__init__(f"{operation}: {missing} [repair owned by: {owner}]")
        self.operation = operation
        self.missing = missing
        self.owner = owner


# ---------------------------------------------------------------------------
# Data classes.  A Coupling is deliberately not an Edge — see COUPLINGS below.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class SubElementGroup:
    structure: str
    axis: str
    members: tuple[str, ...]
    established: SlotState   # does the group meet the different-targets test?
    note: str = ""


@dataclass(frozen=True)
class Structure:
    key: str
    name: str
    basis: str                       # per hemisphere, or per side
    source_neuron_slot: SlotState
    count_state: CountState
    grey_matter_mm3: tuple[float, float] | None
    laminar_block: str               # inadmissible / admissible and unchecked / n/a
    shape_axes: tuple[str, ...]
    justification: str               # biological


@dataclass(frozen=True)
class Edge:
    owner: str                       # the entry the declaration sits in
    direction: Direction
    endpoint: str
    kind: EndpointKind = EndpointKind.REGION_WITH_ENTRY
    payload: str = ""
    shape: PayloadShape = PayloadShape.OWED
    states_absence: bool = False
    far_file: str = ""
    far_state: FarEnd = FarEnd.NOT_CONFIRMED
    two_ended: bool = False
    same_pass: bool = False           # both ends written in one pass: certifies nothing
    in_file: str = ""                 # the in-file structure key, where the far end is here
    onto: str = ""                    # sub-element the edge terminates on
    frm: str = ""                     # sub-element the edge leaves from
    note: str = ""

    # Fan slots and latency are uniform across this section and are named rather
    # than stored per edge: every fan-in and fan-out reads "to derive", and every
    # one of the 76 latencies reads "to derive".
    fan = SlotState.TO_DERIVE
    latency = SlotState.TO_DERIVE

    def producer(self) -> str:
        """Canonical producer name, for collapsing declarations onto edges."""
        if self.direction is Direction.IN:
            return self.in_file or self.endpoint
        return self.owner

    def consumer(self) -> str:
        if self.direction is Direction.IN:
            return self.owner
        return self.in_file or self.endpoint

    def key(self) -> tuple[str, str]:
        return (self.producer(), self.consumer())


@dataclass(frozen=True)
class Coupling:
    """A symmetric electrical coupling.  NOT an Edge, and that is load-bearing.

    An Edge has a source and a target; a gap junction has neither, or has both
    simultaneously.  Writing it as two directed edges would assert two transfers
    where there is one coupling, and would give it a latency in each direction
    where the physical claim is that there is effectively none.  Kept out of the
    edge set so it cannot be counted as an edge or scheduled as one.
    """
    structure: str
    members: tuple[str, ...]
    mechanism: str
    convention: SlotState = SlotState.OWED


# ---------------------------------------------------------------------------
# The six structures, in the architecture's order, which is data-flow order.
# ---------------------------------------------------------------------------

STRUCTURES: tuple[Structure, ...] = (
    Structure(
        key="insula",
        name="Insula — interoceptive / salience / emotional core",
        basis="per hemisphere",
        source_neuron_slot=SlotState.UNKNOWN,
        count_state=CountState.UNCOUNTED_TISSUE_CLASS,
        grey_matter_mm3=None,
        laminar_block="inadmissible — agranular across a gradient",
        shape_axes=("sector (extent contested: 2 / 3 / 16)", "N: to derive"),
        justification=(
            "The gradient is the computation.  Three cytoarchitectures and one "
            "directed chain through them: an objective body-state image enters the "
            "granular pole, is re-represented in the dysgranular middle, and is bound "
            "with limbic context at the agranular pole.  Both internal edges run in "
            "the direction of decreasing granularity — the tissue loses layer 4, the "
            "input layer, exactly where it stops receiving from outside and starts "
            "receiving from itself."
        ),
    ),
    Structure(
        key="claustrum",
        name="Claustrum — the most-connected hub",
        basis="per hemisphere",
        source_neuron_slot=SlotState.UNKNOWN,
        count_state=CountState.SEGMENTATION_LIMITED,
        grey_matter_mm3=None,
        laminar_block="not applicable — no cortical-style lamination",
        shape_axes=("cell class (3, status unestablished)", "dorsal / ventral (owed)",
                    "N: to derive"),
        justification=(
            "Four candidate functions, each a claim about one output edge whose "
            "payload is owed.  They are not four competing descriptions of a known "
            "signal; they are four guesses at an unknown one.  Every one of them is a "
            "claim about WHEN distributed activity is aligned rather than about WHAT "
            "is on the line, so the payload may be purely temporal — a shape the slot "
            "has no room for."
        ),
    ),
    Structure(
        key="habenula",
        name="Habenula — the value brake",
        basis="per side",
        source_neuron_slot=SlotState.UNKNOWN,
        count_state=CountState.MEASURED_NOT_AS_CONTROL_ABSOLUTE,
        grey_matter_mm3=(30.0, 36.0),
        laminar_block="not applicable — non-laminated nucleus",
        shape_axes=("division (extent 2, both named)", "subnuclei: owed", "N: to derive"),
        justification=(
            "A negative reward-prediction error is not the negation of a positive one "
            "— it is a separate line with its own tract, its own relay and its own "
            "transmitter.  The habenula does not brake dopamine; it excites something "
            "that does, and the inversion is attributed to the stage that performs it.  "
            "The description could have made worse-than-expected a sign on the dopamine "
            "wire and did not: the brain spends a nucleus, two tracts and a relay to "
            "keep the bad news on its own line."
        ),
    ),
    Structure(
        key="midcingulate",
        name="Midcingulate cortex — the action-outcome / cingulate-motor hub",
        basis="per hemisphere",
        source_neuron_slot=SlotState.UNKNOWN,
        count_state=CountState.UNCOUNTED_TISSUE_CLASS,
        grey_matter_mm3=None,
        laminar_block="inadmissible — agranular to dysgranular across its extent",
        shape_axes=("field (4 named, second level under 24-prime)", "N: to derive"),
        justification=(
            "A scalar value axis with a body-relative zero, a valence gain and a "
            "salience flag arrive; a motor plan leaves.  A motor plan has a "
            "body-centred frame and the value signal has a body-relative scalar one, "
            "so the operation is a change of frame from value to action rather than a "
            "combination within one frame.  The edge that would carry it is the "
            "internal one that is owed."
        ),
    ),
    Structure(
        key="posterior_cingulate",
        name="Posterior cingulate cortex — default-mode hub",
        basis="per hemisphere",
        source_neuron_slot=SlotState.UNKNOWN,
        count_state=CountState.UNCOUNTED_TISSUE_CLASS,
        grey_matter_mm3=None,
        laminar_block="admissible and unchecked — granular isocortex",
        shape_axes=("sector (dorsal: 23d, 31; ventral: 23a, 23b)", "N: to derive"),
        justification=(
            "The structure's distinctive fact is a negative and it sits on no edge: it "
            "deactivates as externally-focused task demand rises, which is a statement "
            "about a baseline the structure is driven DOWN from.  The sector division "
            "is written on the outputs and not one incoming edge says which sector it "
            "lands on — and a structure whose function is switching between two regimes "
            "needs to know which regime an input belongs to."
        ),
    ),
    Structure(
        key="retrosplenial",
        name="Retrosplenial cortex — the spatial / Papez node",
        basis="per hemisphere",
        source_neuron_slot=SlotState.UNKNOWN,
        count_state=CountState.UNCOUNTED_TISSUE_CLASS,
        grey_matter_mm3=None,
        laminar_block="inadmissible — spans a granular / dysgranular internal border",
        shape_axes=("area (29, 30; sub-element status owed)", "N: to derive"),
        justification=(
            "The one entry whose function is a stated transformation with named input "
            "and output frames: egocentric in, allocentric out.  That is a "
            "coordinate-frame conversion, which is the property a payload is supposed "
            "to declare, named at the structure level and absent from every edge.  The "
            "operation is a transform, not a selection or a gain — which constrains the "
            "owed internal edges more tightly than any other entry constrains its own.  "
            "And a frame conversion needs the self-motion signal that defines it, which "
            "no incoming edge declares."
        ),
    ),
)

STRUCTURE_BY_KEY = {s.key: s for s in STRUCTURES}


# ---------------------------------------------------------------------------
# Sub-element groupings.  None of them can be sized: N is to derive on every axis.
# ---------------------------------------------------------------------------

SUB_ELEMENT_GROUPS: tuple[SubElementGroup, ...] = (
    SubElementGroup("insula", "cytoarchitectonic sector",
                    ("granular", "dysgranular", "agranular"),
                    SlotState.CONTESTED,
                    "the gradient is not in dispute; the boundaries drawn across it are"),
    SubElementGroup("claustrum", "cell class",
                    ("pyramidal-like projection", "fusiform", "circular"),
                    SlotState.UNKNOWN,
                    "none meets the different-targets test"),
    SubElementGroup("claustrum", "dorsoventral division",
                    ("dorsal", "ventral"),
                    SlotState.OWED,
                    "the ventral sector carries the amygdala and cingulate connections"),
    SubElementGroup("habenula", "division",
                    ("medial habenula", "lateral habenula"),
                    SlotState.CONTENT,
                    "different transmitters, different inputs, entirely different targets"),
    SubElementGroup("habenula", "subnuclei",
                    (),
                    SlotState.OWED,
                    "described in the literature, not named here"),
    SubElementGroup("midcingulate", "prime field",
                    ("area 24-prime (a', b', c')", "area 32-prime"),
                    SlotState.CONTENT, ""),
    SubElementGroup("midcingulate", "cingulate motor area",
                    ("rostral cingulate motor area", "caudal cingulate motor area"),
                    SlotState.CONTENT,
                    "the output-capable sectors; named on the motor edges"),
    SubElementGroup("posterior_cingulate", "sector",
                    ("dorsal (23d, 31)", "ventral (23a, 23b)"),
                    SlotState.CONTENT,
                    "they project to different targets"),
    SubElementGroup("retrosplenial", "architectonic area",
                    ("area 29 (granular)", "area 30 (dysgranular)"),
                    SlotState.OWED,
                    "whether they project to different targets is the prior question"),
)


COUPLINGS: tuple[Coupling, ...] = (
    Coupling(
        structure="claustrum",
        members=("GABAergic interneuron network",),
        mechanism=("gap-junction electrical coupling among interneurons — not a "
                   "directed synapse, and the description has no convention for one"),
    ),
)


# ---------------------------------------------------------------------------
# The 76 edge declarations, entry by entry, in the architecture's order.
# ---------------------------------------------------------------------------

IN, OUT, INT = Direction.IN, Direction.OUT, Direction.INTERNAL
OWED, NAME, PART = PayloadShape.OWED, PayloadShape.NAME_ONLY, PayloadShape.PARTIAL_TYPE
ABSENCE, PROPERTY = PayloadShape.STATED_ABSENCE, PayloadShape.PROPERTY_IN_PLACE_OF_TYPE
REGION, NOENTRY = EndpointKind.REGION_WITH_ENTRY, EndpointKind.REGION_NO_ENTRY
CLASS, NETWORK = EndpointKind.CLASS, EndpointKind.NETWORK


def _e(owner: str, direction: Direction, endpoint: str, **kw) -> Edge:
    return Edge(owner=owner, direction=direction, endpoint=endpoint, **kw)


EDGES: tuple[Edge, ...] = (

    # -- Insula: ten inputs, eleven outputs, two internal ---------------------
    _e("insula", IN, "posterior / ventromedial-posterior thalamus",
       onto="dorsal posterior insula", shape=PART, far_file="12",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the body's physiological condition, the lamina-I interoceptive stream, "
               "somatotopically ordered",
       note="whether the three labelled spinal lines stay separate or merge is an "
            "arity question owed at both ends"),
    _e("insula", IN, "primary somatosensory cortex", frm="area 3a",
       far_file="5", far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("insula", IN, "secondary somatosensory cortex", frm="ventral somatosensory area",
       far_file="5", far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("insula", IN, "gustatory pathway", onto="anterior insula / frontal operculum",
       payload="taste quality and intensity", shape=PART, far_file="3",
       far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("insula", IN, "vestibular nuclei and the central vestibular pathway",
       onto="parieto-insular vestibular cortex", shape=PART, far_file="3",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="head rotation rate and gravito-inertial acceleration"),
    _e("insula", IN, "auditory parabelt", far_file="2",
       far_state=FarEnd.UNRESOLVED_ARITY,
       note="declared but not individually typed at either end"),
    _e("insula", IN, "amygdala", shape=NAME, states_absence=True, far_file="8",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the valence tag — a gain on perception, attention and memory encoding, "
               "carrying no identity information: the significance, not the thing"),
    _e("insula", IN, "temporal pole", far_file="7", far_state=FarEnd.TWO_ENDED,
       two_ended=True),
    _e("insula", IN, "orbitofrontal / ventromedial prefrontal cortex", far_file="11",
       far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("insula", IN, "anterior cingulate cortex", far_file="11",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       note="the return arm of a relationship this entry calls reciprocal is "
            "unconfirmed at its producer"),

    _e("insula", OUT, "anterior cingulate cortex", shape=NAME, far_file="11",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the salience signal — this event is behaviourally relevant now",
       note="whether what leaves is a scalar, a pointer or a switching command is "
            "not established"),
    _e("insula", OUT, "right inferior frontal gyrus", shape=NAME, far_file="11",
       far_state=FarEnd.TWO_ENDED, two_ended=True, payload="the salience signal"),
    _e("insula", OUT, "orbitofrontal / ventromedial prefrontal cortex", shape=NAME,
       far_file="11", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the salience signal and, reciprocally, the interoceptive state"),
    _e("insula", OUT, "temporal pole", shape=NAME, far_file="7",
       far_state=FarEnd.TWO_ENDED, two_ended=True, payload="interoceptive context"),
    _e("insula", OUT, "midcingulate cortex", shape=NAME, in_file="midcingulate",
       far_state=FarEnd.TWO_ENDED, two_ended=True, same_pass=True,
       payload="the salience / affect signal"),
    _e("insula", OUT, "amygdala", far_file="8", far_state=FarEnd.TWO_ENDED,
       two_ended=True),
    _e("insula", OUT, "bed nucleus of the stria terminalis", frm="anterior insula",
       shape=NAME, far_file="8", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="interoceptive state"),
    _e("insula", OUT, "hypothalamus", far_file="14", far_state=FarEnd.NOT_CONFIRMED),
    _e("insula", OUT, "basal ganglia", onto="ventral striatum", far_file="9",
       far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("insula", OUT, "habenula", onto="lateral habenula", shape=NAME,
       in_file="habenula", far_state=FarEnd.TWO_ENDED, two_ended=True, same_pass=True,
       payload="a bad-outcome expectation — an affective / evaluative signal that an "
               "outcome is worse than wanted"),
    _e("insula", OUT, "posterior / ventromedial-posterior thalamus", shape=ABSENCE,
       states_absence=True, far_file="12", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="no stimulus content; the driver / modulator gate"),

    _e("insula", INT, "mid (dysgranular) insula", frm="posterior (granular) insula",
       shape=PART,
       payload="the interoceptive body-state image, re-represented and integrated"),
    _e("insula", INT, "anterior (agranular) insula", frm="mid (dysgranular) insula",
       note="payload owed and the completion test fails here: 'a subjective feeling' "
            "is a phrase, not a type"),

    # -- Claustrum: five inputs, four outputs, all payloads owed --------------
    _e("claustrum", IN, "cerebral cortex, near all-to-all", kind=CLASS,
       note="the hardest class endpoint in the file; the description has no "
            "convention for an all-to-all endpoint and this entry is where it is "
            "first needed"),
    _e("claustrum", IN, "amygdala", onto="ventral claustrum", far_file="8",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE),
    _e("claustrum", IN, "cingulate cortex", kind=CLASS,
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       note="three of four candidate producers are entries in this same file; none "
            "of the four declares it"),
    _e("claustrum", IN, "hippocampus / subiculum", far_file="8",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE),
    _e("claustrum", IN, "neuromodulatory afferents", kind=CLASS, far_file="13",
       note="the four neuromodulatory entries each declare a brain-wide cortical "
            "class that would cover this structure without naming it"),

    _e("claustrum", OUT, "cerebral cortex, near all-to-all", kind=CLASS,
       note="the edge the entry's function depends on: binding, synchronisation, "
            "network switching and slow-oscillation control are all claims about "
            "what travels here, and none of them types it"),
    _e("claustrum", OUT, "amygdala", far_file="8", far_state=FarEnd.TWO_ENDED,
       two_ended=True),
    _e("claustrum", OUT, "hippocampus / subiculum", far_file="8",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE),
    _e("claustrum", OUT, "cingulate cortex", kind=CLASS,
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE),

    # -- Habenula: eight inputs over the stria medullaris, four outputs over
    #    the fasciculus retroflexus.  Neither tract has an entry anywhere, and a
    #    tract is where the physical substrate of a latency lives.
    _e("habenula", IN, "septal nuclei", onto="medial habenula", kind=NOENTRY,
       far_state=FarEnd.NO_ENTRY),
    _e("habenula", IN, "internal globus pallidus", onto="lateral habenula", shape=NAME,
       far_file="9", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the basal-ganglia 'no-reward' signal"),
    _e("habenula", IN, "ventral pallidum", onto="lateral habenula", far_file="9",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       note="file 9 still records this as an owed cross-file edit, which it is not"),
    _e("habenula", IN, "lateral hypothalamus", onto="lateral habenula", far_file="14",
       far_state=FarEnd.NOT_CONFIRMED),
    _e("habenula", IN, "suprachiasmatic nucleus", onto="lateral habenula", far_file="14",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE),
    _e("habenula", IN, "anterior cingulate cortex", onto="lateral habenula", shape=NAME,
       far_file="11", far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       payload="a bad-outcome expectation"),
    _e("habenula", IN, "anterior insula", onto="lateral habenula", shape=NAME,
       in_file="insula", far_state=FarEnd.TWO_ENDED, two_ended=True, same_pass=True,
       payload="a bad-outcome expectation"),
    _e("habenula", IN, "ventromedial prefrontal cortex", onto="lateral habenula",
       shape=NAME, far_file="11", far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       payload="a bad-outcome expectation"),

    _e("habenula", OUT, "interpeduncular nucleus", frm="medial habenula", kind=NOENTRY,
       far_state=FarEnd.NO_ENTRY,
       note="the string appears nowhere else in the source; the medial-habenular "
            "limb is described from its origin only"),
    _e("habenula", OUT, "rostromedial tegmental nucleus", frm="lateral habenula",
       shape=PART, far_file="14", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="a negative / aversive value signal — a glutamatergic excitatory drive "
               "encoding a worse-than-expected outcome, which that nucleus inverts in "
               "sign into inhibition of the dopamine cells",
       note="the best-typed edge in the section: sign, content, and a stated "
            "downstream inversion"),
    _e("habenula", OUT, "raphe nuclei", frm="lateral habenula", shape=PART,
       far_file="13", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the same negative / aversive value signal, modulating serotonin "
               "rather than dopamine"),
    _e("habenula", OUT, "pineal gland", frm="medial habenula", far_file="14",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       note="stated in the function slot as prose, and prose is not an edge: neither "
            "direction nor content is established at this end either"),

    # -- Midcingulate cortex: seven inputs, six outputs -----------------------
    _e("midcingulate", IN, "anterior cingulate cortex", shape=PART, far_file="11",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="a scalar reward-value signal — expected reward magnitude, and a "
               "response to the mismatch between expected and received reward; frame "
               "is a scalar value axis whose zero and slope are body-relative",
       note="the only edge in the section with a stated coordinate frame; the two "
            "ends are copies, so their agreement certifies little"),
    _e("midcingulate", IN, "amygdala", shape=NAME, states_absence=True, far_file="8",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the valence tag, carrying no identity information"),
    _e("midcingulate", IN, "anterior insula", shape=NAME, in_file="insula",
       far_state=FarEnd.TWO_ENDED, two_ended=True, same_pass=True,
       payload="the salience / affect signal"),
    _e("midcingulate", IN, "posterior parietal cortex", kind=CLASS, far_file="6",
       note="candidate producers in file 6; none confirmed"),
    _e("midcingulate", IN, "posterior cingulate cortex", in_file="posterior_cingulate",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE, same_pass=True,
       note="reciprocity is a relationship; an edge is not.  A reciprocal pair is two "
            "edges and each needs its own declaration at both of its own ends"),
    _e("midcingulate", IN, "midline and intralaminar thalamus", far_file="12",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       note="the producer declares its cortical target as a class covering this "
            "region without naming it"),
    _e("midcingulate", IN, "mediodorsal thalamus", far_file="12",
       far_state=FarEnd.NOT_CONFIRMED),

    _e("midcingulate", OUT,
       "supplementary and pre-supplementary motor areas and premotor cortex",
       frm="cingulate motor areas", far_file="11", far_state=FarEnd.TWO_ENDED,
       two_ended=True,
       note="at this end it is the convergence of outcome with action and spatial "
            "information, turned into a motor plan"),
    _e("midcingulate", OUT, "primary motor cortex", frm="cingulate motor areas",
       far_file="5", far_state=FarEnd.NOT_CONFIRMED),
    _e("midcingulate", OUT, "anterior cingulate cortex", far_file="11",
       far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("midcingulate", OUT, "posterior cingulate cortex", in_file="posterior_cingulate",
       far_state=FarEnd.TWO_ENDED, two_ended=True, same_pass=True),
    _e("midcingulate", OUT, "basal ganglia", kind=CLASS, far_file="9",
       note="the striatal target is likely and is not stated; naming the nucleus is "
            "owed here before the far end can be checked"),
    _e("midcingulate", OUT, "brainstem autonomic targets", kind=CLASS, far_file="14",
       note="file 14 holds the candidates and none was confirmed"),

    # -- Posterior cingulate cortex: six inputs, five outputs -----------------
    _e("posterior_cingulate", IN, "hippocampal formation", shape=PROPERTY, far_file="8",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the completed episode — the bound, retrievable pattern, addressable "
               "by any fragment of itself; no units and no frame, and "
               "content-addressability is what makes it checkable"),
    _e("posterior_cingulate", IN, "anterior cingulate cortex", far_file="11",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE),
    _e("posterior_cingulate", IN, "midcingulate cortex", in_file="midcingulate",
       far_state=FarEnd.TWO_ENDED, two_ended=True, same_pass=True),
    _e("posterior_cingulate", IN, "precuneus", far_file="6",
       far_state=FarEnd.NOT_CONFIRMED),
    _e("posterior_cingulate", IN, "posterior parietal cortex", kind=CLASS, far_file="6"),
    _e("posterior_cingulate", IN, "anterior thalamus", far_file="12",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       note="the posterior-cingulate limb of the classical limbic thalamic "
            "projection is unconfirmed at its producer"),

    _e("posterior_cingulate", OUT, "hippocampal formation", far_file="8",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       note="written by name, the class it was hidden in gone, and the payload still "
            "owed: naming the consumer is not typing the edge"),
    _e("posterior_cingulate", OUT, "precuneus", far_file="6",
       far_state=FarEnd.TWO_ENDED, two_ended=True),
    _e("posterior_cingulate", OUT, "angular gyrus", far_file="6",
       far_state=FarEnd.NOT_CONFIRMED),
    _e("posterior_cingulate", OUT, "orbitofrontal / ventromedial prefrontal cortex",
       far_file="11", far_state=FarEnd.NOT_CONFIRMED),
    _e("posterior_cingulate", OUT, "cognitive-control network", kind=NETWORK,
       frm="dorsal posterior cingulate cortex",
       note="not repairable by naming the members: listing them turns one edge into "
            "several and asserts each receives the same payload, which is not what a "
            "network claim says"),

    # -- Retrosplenial cortex: five inputs, three outputs ---------------------
    _e("retrosplenial", IN, "hippocampal formation", frm="subiculum", shape=PROPERTY,
       far_file="8", far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the completed episode, addressable by any fragment of itself"),
    _e("retrosplenial", IN, "anterior thalamic nuclei", far_file="12",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       note="the head-direction signal this entry's function depends on is carried by "
            "one division of the anterior nuclei, and that entry records its own "
            "divisions as unnamed and owed; naming them will split this edge"),
    _e("retrosplenial", IN, "parahippocampal cortex", kind=NOENTRY,
       far_state=FarEnd.NO_ENTRY,
       note="named as a producer by three other files as well; the stage the Papez "
            "return arm runs through"),
    _e("retrosplenial", IN, "posterior parietal cortex", kind=CLASS, far_file="6"),
    _e("retrosplenial", IN, "visual areas", kind=CLASS,
       note="the edge that would supply half of what the region is said to fuse"),

    _e("retrosplenial", OUT, "hippocampal formation", shape=PART, far_file="8",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the return arm of the spatial-memory loop — heading and landmark "
               "information after the egocentric-to-allocentric translation",
       note="the route runs via parahippocampal and entorhinal cortex, and "
            "parahippocampal cortex has no entry"),
    _e("retrosplenial", OUT, "anterior thalamic nuclei", far_file="12",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE,
       note="two-ended in intent only: the consumer records this as an edge it does "
            "not carry"),
    _e("retrosplenial", OUT, "precuneus", shape=PART, far_file="6",
       far_state=FarEnd.TWO_ENDED, two_ended=True,
       payload="the return arm of the spatial-memory loop"),
)


# Tract-routing statements.  Not edges: the cingulum has an entry in file 18 as
# transmission without processing, so the traffic on it belongs to the cingulate
# edges themselves.  Held separately so they cannot be counted as edges.
TRACT_ROUTING: tuple[tuple[str, str], ...] = (
    ("midcingulate", "the cingulum"),
    ("posterior_cingulate", "the cingulum"),
    ("retrosplenial", "the cingulum"),
)

# Tracts named as carrying this section's edges.  Two have entries and two do not,
# and a tract is where the physical substrate of a latency lives.
TRACTS: dict[str, str] = {
    "cingulum": "entry in file 18",
    "stria medullaris": "no entry anywhere — carries all habenular input",
    "fasciculus retroflexus": "no entry anywhere — carries all habenular output",
}

# The architecture's own figures, held so the module's counts can be compared
# against them rather than assumed to agree.
ARCHITECTURE_FIGURES = {
    "inter_region_declarations": 74,
    "internal_edges": 2,
    "fully_owed_declarations": 49,
    "two_ended_declarations": 24,
    "same_pass_declarations": 5,
    "sub_element_groups": 9,
    "source_design_typed_edges": 62,   # disagrees; left unsmoothed
}


# ---------------------------------------------------------------------------
# The forward operation.
# ---------------------------------------------------------------------------

def bits(fan_in: int | None) -> int:
    """Stored bits per neuron under the threshold-gate model.

    A neuron fires when the count of active inputs crosses a threshold, so under
    equal weights the only stored value per neuron is that threshold, costing
    log2(fan_in) bits.  Memory therefore tracks neuron count, not synapse count:
    log2 caps hard, and any fan-in below about 65,000 costs no more than 16 bits.

    With fan_in unknown the ceiling is returned.  It is a cap, not a measurement,
    and in this section it multiplies nothing.
    """
    if fan_in is None:
        return 16
    if fan_in < 1:
        raise ValueError("fan-in below one is not a fan-in")
    return math.ceil(math.log2(fan_in)) if fan_in > 1 else 0


def fan_in_map(structure: str) -> dict[str, int]:
    """Contacts converging on each neuron.  Not implementable in this section.

    Every fan slot in all six entries reads 'to derive', and the quantity that
    would supply them — inter-structure connection topology — is unset.  The
    claustrum makes the gap sharpest: its defining quantitative fact is that it is
    the most densely connected structure in the brain per unit volume, so the one
    thing known quantitatively about it is known about the one axis with no values.
    """
    raise Blocked(
        f"fan_in_map({structure!r})",
        "inter-structure connection topology is unset, and every fan slot in the "
        "section reads 'to derive'",
        "Micky — it is on the surface-before-touching list",
    )


def forward(structure: str) -> None:
    """count[j] = sum of active inputs; active[j] = count[j] >= threshold[j].

    The operation is writable and there is nothing to run it on: no neuron count on
    any structure, no fan-in on any edge, and no settled extent on any shape axis.
    """
    raise Blocked(
        f"forward({structure!r})",
        "no neuron count on any structure in the section and no fan-in on any edge",
        "the source — a stereology programme, a segmentation method, and a control "
        "absolute, in that order of cost",
    )


# ---------------------------------------------------------------------------
# The four blocked operations.  Four different blockers, kept apart because the
# repairs differ.
# ---------------------------------------------------------------------------

def bind():
    """Insula: bind the re-represented interoceptive image with limbic context.

    Blocked by a written edge with an unwritable payload.  The mid-to-anterior
    internal edge exists and is declared; its output type is 'a subjective feeling',
    which is a phrase and not a type.  The description gets you to the door.
    """
    raise Blocked(
        "bind()",
        "the mid-to-anterior internal edge is written and its payload fails the "
        "completion test: 'a subjective feeling' is a phrase, not a type",
        "the source — and it is one of the convergence nodes where format is said "
        "to dissolve, so it may be a finding about the payload slot itself",
    )


def converge():
    """Midcingulate: turn outcome and action into a motor plan.

    Blocked by an unwritten internal edge.  The transfer from the fields that
    receive outcome and action onto the motor areas that emit is the structure's
    whole claim, and it is not in the description.
    """
    raise Blocked(
        "converge()",
        "the internal edge from the receiving fields to the cingulate motor areas "
        "is owed, and that edge is the entry's stated function",
        "the source",
    )


def fuse():
    """Retrosplenial: fuse self-motion cues with visual landmarks.

    Blocked by an undeclared input.  The operation is a coordinate-frame conversion,
    egocentric in and allocentric out, and a frame conversion needs the self-motion
    signal that defines the transform.  No incoming edge declares any of the three
    cues, and the visual half arrives on a class endpoint.
    """
    raise Blocked(
        "fuse()",
        "no incoming edge declares vestibular, proprioceptive or motor-efference "
        "self-motion; both halves of the fusion are undeclared at their sources",
        "the source",
    )


def value_brake():
    """Habenula: emit the negative reward-prediction error.

    The only operation in the section whose blocker is the model rather than the
    description.  The payload is typed, the sign is stated, the inversion is
    attributed to the stage that performs it, and the consumer declares it — and a
    count of active inputs crossing a threshold has no term for the excitation's
    magnitude or for the downstream inversion.  A second gap sits under it: a
    prediction error needs an expected value, and no expectation is declared as
    stored anywhere in the entry.
    """
    raise Blocked(
        "value_brake()",
        "the threshold-gate model has no term for a graded excitation or for the "
        "sign inversion one stage downstream, and the expectation term of the "
        "prediction error is not declared as stored anywhere",
        "the model, and the source for the expectation term",
    )


def step():
    """Advance the section by one update.  There is no update to advance by.

    Per-edge latency is nonzero, finite and heterogeneous, in real time units and
    never in steps: a latency stated in steps has assumed a clock, and there is no
    global clock in the described system.  All 76 latencies read 'to derive'.

    The section carries one quantitative constraint on any latency, and it is on the
    edge that can least use it.  The claustrum regulates slow cortical oscillations
    at roughly 0.5 to 4 Hz — a period of 250 ms to 2 s — and a structure that
    regulates an oscillation must close its loop fast relative to that period.  So
    the claustro-cortical round trip has an upper bound of order the period, and the
    axons carrying it are exceptionally far-reaching, which is what makes the bound
    non-trivial rather than automatic.  The bound is recorded, not applied.
    """
    raise Blocked(
        "step()",
        "the scheduling discipline is not set and all 76 edge latencies read 'to "
        "derive'; the only recorded bound is the claustro-cortical round trip, of "
        "order 250 ms to 2 s, which is a ceiling and not a latency",
        "Micky — the scheduling discipline is the design rung's largest open item",
    )


def learn():
    """Adaptation.  No structure in the section declares one.

    Nothing here is described as changing as a result of what it computes.  The
    nearest thing is the lateral habenula's negative reward-prediction error, which
    is a teaching signal by the same logic as the nigrostriatal one — and it LEAVES
    this section rather than arriving in it.  So the section produces half of a
    reward-prediction error and stores nothing.

    The two halves are computed in different files by different structures with
    different transmitters: positive dopaminergic, negative glutamatergic and
    inverted to inhibition one stage downstream.  A rule that treats the error as
    one signed scalar will be asserting a merge the description does not make.
    """
    raise Blocked(
        "learn()",
        "no structure in the section declares a learning rule, a plasticity "
        "mechanism or a training signal it consumes",
        "Micky — learning rules are on the surface-before-touching list",
    )


# ---------------------------------------------------------------------------
# Reports.  These run: what the module can do is say precisely what is missing,
# sorted by the repair each gap needs.
# ---------------------------------------------------------------------------

def inter_region(edges: Iterable[Edge] = EDGES) -> list[Edge]:
    return [e for e in edges if e.direction is not Direction.INTERNAL]


def internal(edges: Iterable[Edge] = EDGES) -> list[Edge]:
    return [e for e in edges if e.direction is Direction.INTERNAL]


def distinct_edges(edges: Iterable[Edge] = EDGES) -> dict[tuple[str, str], list[Edge]]:
    """Collapse declarations onto edges.

    An edge between two entries in this file is declared twice, once in the
    producer's Outputs and once in the consumer's Inputs.  Sizing in-flight values
    on the declaration count would double-count those lines.
    """
    out: dict[tuple[str, str], list[Edge]] = {}
    for e in inter_region(edges):
        out.setdefault(e.key(), []).append(e)
    return out


def edge_reconciliation() -> str:
    ins = [e for e in EDGES if e.direction is Direction.IN]
    outs = [e for e in EDGES if e.direction is Direction.OUT]
    ints = internal()
    groups = distinct_edges()
    dupes = {k: v for k, v in groups.items() if len(v) > 1}
    lines = [
        "EDGE RECONCILIATION",
        f"  in-bullets in the source            {len(ins) + len(TRACT_ROUTING):3d}",
        f"  less tract-routing (not edges)      -{len(TRACT_ROUTING):2d}",
        f"  in-declarations                     {len(ins):3d}",
        f"  out-declarations                    {len(outs):3d}",
        f"  inter-region declarations           {len(ins) + len(outs):3d}"
        f"   (architecture: {ARCHITECTURE_FIGURES['inter_region_declarations']})",
        f"  internal edges                      {len(ints):3d}"
        f"   (architecture: {ARCHITECTURE_FIGURES['internal_edges']})",
        f"  total declarations                  {len(EDGES):3d}",
        "",
        f"  distinct inter-region edges         {len(groups):3d}",
        f"  + internal                          {len(ints):3d}",
        f"  = distinct edges                    {len(groups) + len(ints):3d}"
        "   <- the line count edge storage runs on",
        "",
        "  declared at both ends inside this file, so counted twice above:",
    ]
    for (p, c) in sorted(dupes):
        lines.append(f"    {p} -> {c}")
    lines.append("")
    lines.append(
        "  DISAGREEMENT, unsmoothed: the source design records this file's "
        f"conversion as producing {ARCHITECTURE_FIGURES['source_design_typed_edges']} "
        "typed edges.  Neither figure above is that.  A second independently-derived "
        "record of the same quantity is the mechanism that catches a stale file, and "
        "smoothing to the nearer number would destroy the signal."
    )
    return "\n".join(lines)


def endpoint_census() -> str:
    counts: dict[EndpointKind, int] = {k: 0 for k in EndpointKind}
    for e in inter_region():
        counts[e.kind] += 1
    lines = ["ENDPOINT CENSUS"]
    for kind, n in counts.items():
        lines.append(f"  {n:3d}  {kind.name.lower():20s} {kind.value}")
    lines.append(f"  {len(TRACT_ROUTING):3d}  tract_routing        not an edge")
    lines.append("")
    lines.append("  regions with no entry anywhere:")
    for e in inter_region():
        if e.kind is EndpointKind.REGION_NO_ENTRY:
            lines.append(f"    {e.owner:20s} {e.direction.value:8s} {e.endpoint}")
    lines.append(
        "  Two of the three are the medial habenula's only input and only output, so "
        "one of the habenula's two divisions is described as a relay between two "
        "blanks.  That is worse than a missing stage inside a loop: there is no loop "
        "to break, only one described structure with two undescribed sides."
    )
    return "\n".join(lines)


def class_families() -> str:
    """Eleven class endpoints, four decisions.  A family is one decision, not several."""
    fams: dict[str, list[Edge]] = {}
    for e in inter_region():
        if e.kind is EndpointKind.CLASS:
            fams.setdefault(e.endpoint, []).append(e)
    repeated = {k: v for k, v in fams.items() if len(v) > 1}
    lines = [
        "CLASS-ENDPOINT FAMILIES",
        f"  {sum(len(v) for v in fams.values())} endpoints -> {len(fams)} decisions",
        f"  {len(repeated)} of them are repeated families covering "
        f"{sum(len(v) for v in repeated.values())} of the endpoints, which is where "
        "the saving is: one decision, several edges",
        "",
    ]
    for name, group in sorted(fams.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        owners = ", ".join(sorted({e.owner for e in group}))
        lines.append(f"  {len(group)}x  {name}  [{owners}]")
    lines.append("")
    lines.append(
        "  'the cerebral cortex, near all-to-all' is not merely awkward to split: the "
        "connectivity is described as diffuse rather than precisely mapped, so "
        "resolving it into named producers would assert a specificity the literature "
        "does not report."
    )
    return "\n".join(lines)


def intra_file_diff() -> str:
    """Far ends that are entries in this same file and do not declare the edge.

    The cheapest repair in the section: no other file needs opening.
    """
    hits = [e for e in inter_region()
            if e.far_state is FarEnd.DECLARES_NO_SUCH_EDGE
            and (e.in_file or e.kind is EndpointKind.CLASS and "cingulate" in e.endpoint)]
    lines = ["INTRA-FILE DIFF — far ends inside this file that do not declare the edge"]
    for e in hits:
        lines.append(f"  {e.owner:20s} {e.direction.value:8s} {e.endpoint}")
    lines.append(
        "  Reciprocity is a relationship; an edge is not.  A reciprocal pair is two "
        "edges and each needs its own declaration at both of its own ends."
    )
    return "\n".join(lines)


def same_pass_report() -> str:
    """Two-ended agreements that certify nothing.

    Two ends written in one pass from one sentence agree by construction.  The
    agreements that certify something cross a file boundary and a date.
    """
    sp = [e for e in inter_region() if e.same_pass]
    te = [e for e in inter_region() if e.two_ended]
    groups = {k: v for k, v in distinct_edges().items()
              if any(e.same_pass for e in v)}
    lines = [
        "SAME-PASS CERTIFICATION",
        f"  declarations whose far end declares the edge  {len(te):3d}",
        "    (not comparable with the architecture's 24, which counts declarations "
        "the source marks with the word 'two-ended'; this is the wider question)",
        f"  of those, both ends written in one pass       {len(sp):3d}"
        f"   (architecture: {ARCHITECTURE_FIGURES['same_pass_declarations']})",
        f"  distinct edges affected                       {len(groups):3d}",
        "",
        "  DISAGREEMENT, unsmoothed: the architecture counts five same-pass "
        "declarations and this module counts every declaration carrying the caveat.  "
        "Same criterion, different totals.  Neither is adjusted to the other.",
        "",
        "  affected:",
    ]
    for e in sp:
        lines.append(f"    {e.owner:20s} {e.direction.value:8s} {e.endpoint}")
    return "\n".join(lines)


def count_state_report() -> str:
    """Six structures, zero counts, three states — and three different repairs."""
    by_state: dict[CountState, list[Structure]] = {}
    for s in STRUCTURES:
        by_state.setdefault(s.count_state, []).append(s)
    lines = ["COUNT STATES — the section sizes zero of "
             f"{len(SUB_ELEMENT_GROUPS)} sub-element groupings"]
    for state, members in by_state.items():
        names = ", ".join(s.key for s in members)
        lines.append(f"\n  {state.name}  [{len(members)}: {names}]")
        lines.append(f"    {state.value}")
    lines.append(
        "\n  The three are not degrees of one thing.  Four structures are blocked by "
        "one absent measurement programme, so the section needs three repairs and not "
        "six — and one of the three is worth four structures."
    )
    return "\n".join(lines)


def laminar_admissibility() -> str:
    """The four cortical structures, and why none has a layer axis.

    The standard laminar block is a claim about granular isocortex and three of its
    edges route through layer 4.  Where the tissue is agranular, transcribing it
    asserts a circuit the description denies.
    """
    lines = ["LAMINAR ADMISSIBILITY"]
    for s in STRUCTURES:
        if s.laminar_block.startswith("not applicable"):
            continue
        lines.append(f"  {s.key:20s} {s.laminar_block}")
    lines.append(
        "  Three inadmissible, one admissible and unchecked.  Setting tile geometry "
        "for granular isocortex would unblock one of the four and leave three exactly "
        "where they are."
    )
    return "\n".join(lines)


def habenula_density_table(
    densities: tuple[int, ...] = (10_000, 20_000, 50_000, 100_000),
) -> str:
    """What the section's one firm number buys, which is nothing on its own.

    A volume converts to a count only through a packing density, and no density
    appears anywhere in the section.  The densities below are chosen to bracket.
    None of them is a candidate figure for this tissue.
    """
    lo, hi = STRUCTURE_BY_KEY["habenula"].grey_matter_mm3
    lines = [
        "HABENULA — volume to count, run backwards",
        f"  grey matter {lo:.0f}-{hi:.0f} mm3 per side",
        "",
        f"  {'density /mm3':>14s}  {'neurons per side':>24s}  {'store at 16 bits':>20s}",
    ]
    first = last = None
    for d in densities:
        n_lo, n_hi = lo * d, hi * d
        mb_lo, mb_hi = n_lo * 16 / 8 / 1e6, n_hi * 16 / 8 / 1e6
        lines.append(f"  {d:14,d}  {n_lo:11,.0f} - {n_hi:10,.0f}  "
                     f"{mb_lo:8.2f} - {mb_hi:7.2f} MB")
        first = first or n_lo
        last = n_hi
    span = last / first
    lines.append("")
    lines.append(
        f"  Factor of {span:.0f} end to end, and {span / (hi / lo):.0f} of it comes "
        "from the density rather than the volume.  So the firm number is firm and "
        "buys nothing on its own."
    )
    voxel = 3.0 ** 3
    lines.append(
        f"  The volume is {lo / voxel:.1f} to {hi / voxel:.1f} functional-MRI voxels "
        "at 3 mm isotropic.  The structure that inverts the sign of the whole reward "
        "system sits at the resolution limit of the instrument that would image it."
    )
    return "\n".join(lines)


def edge_storage_report() -> str:
    """edge_storage = line_count * ceil(latency / update_interval) * bytes_per_value.

    Three of four terms are unset.  What can be said is where the figure will be
    large: the claustrum's near-all-to-all cortical projection on exceptionally
    far-reaching axons is the one place in the project so far where edge storage
    would plausibly dominate the parameter store, and it is the one whose topology
    is furthest from being stateable.
    """
    lines = ["EDGE STORAGE — lines produced per structure",
             "  line_count * ceil(latency / update_interval) * bytes_per_value"]
    total = 0
    for s in STRUCTURES:
        n = len([e for e in EDGES
                 if e.owner == s.key and e.direction is not Direction.IN])
        total += n
        lines.append(f"    {s.key:20s} {n:3d} lines")
    groups = distinct_edges()
    lines.append(f"    {'produced in section':20s} {total:3d}")
    lines.append(f"    {'distinct edges':20s} {len(groups) + len(internal()):3d}"
                 "  <- the section-level line count")
    lines.append("")
    lines.append("    latency          to derive on all "
                 f"{len(EDGES)} declarations")
    lines.append("    update_interval  UNSET — the scheduling discipline is Micky's")
    lines.append("    bytes_per_value  to derive — gated on graded vs binary emission")
    lines.append("  Not computable, and not estimated.")
    return "\n".join(lines)


def payload_report() -> str:
    shapes: dict[PayloadShape, int] = {s: 0 for s in PayloadShape}
    for e in inter_region():
        shapes[e.shape] += 1
    owed = shapes[PayloadShape.OWED]
    total = len(inter_region())
    lines = [
        "PAYLOAD SHAPES",
        f"  {owed} of {total} inter-region declarations are fully owed "
        f"({owed / total:.0%})"
        f"   (architecture: {ARCHITECTURE_FIGURES['fully_owed_declarations']})",
        "",
    ]
    for shape, n in shapes.items():
        if n:
            lines.append(f"  {n:3d}  {shape.name.lower():28s} {shape.value}")
    lines.append("")
    lines.append("  checkable by what they explicitly do NOT carry:")
    for e in EDGES:
        if e.states_absence:
            lines.append(f"    {e.owner:20s} {e.endpoint}")
    lines.append("")
    lines.append(
        "  and the narrower class — payloads whose informative event is a DECREASE, "
        "for which the activity bit has no polarity convention:"
    )
    lines.append("    insula               posterior / ventromedial-posterior thalamus"
                 "  (no stimulus content; the gate)")
    lines.append("    posterior_cingulate  deactivates as external task demand rises"
                 "  (a property of the structure, not of an edge, so it sits on no "
                 "line at all)")
    return "\n".join(lines)


def completion_test() -> str:
    """An entry is finished when the code can be written from it without a choice."""
    blockers = {
        "insula": "the output type of the mid-to-anterior edge; the layer axis; N",
        "claustrum": "the transform itself — four hypotheses, one untyped edge; "
                     "a representation for the coupling",
        "habenula": "where the expectation term lives; a packing density; N",
        "midcingulate": "the internal edge that is the entry's stated function; "
                        "the layer axis; N",
        "posterior_cingulate": "the dorsal-ventral connection; the baseline value; "
                               "the input sector attributions; N",
        "retrosplenial": "the self-motion producer; the two-frame array structure; N",
    }
    lines = ["COMPLETION TEST — none of the six is finished"]
    for s in STRUCTURES:
        lines.append(f"  {s.key:20s} no   {blockers[s.key]}")
    lines.append(
        "\n  The forward operation is writable and there is almost nothing to run it "
        "on.  Six of the blockers are decisions Micky has not made and would unblock "
        "other sections too; the payloads and the internal edges are research the "
        "source has not done, and no decision at any rung substitutes for them."
    )
    return "\n".join(lines)


def report() -> str:
    return "\n\n".join((
        edge_reconciliation(),
        endpoint_census(),
        class_families(),
        intra_file_diff(),
        same_pass_report(),
        payload_report(),
        count_state_report(),
        laminar_admissibility(),
        habenula_density_table(),
        edge_storage_report(),
        completion_test(),
    ))


if __name__ == "__main__":
    print(report())
