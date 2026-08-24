"""Brain 18 — white matter tracts.

The cabling between the grey-matter regions: the corpus callosum, the internal
capsule, the fornix, the arcuate / superior longitudinal fasciculus, and the medial
longitudinal fasciculus.

WHAT THIS MODULE IS
-------------------
Every structure here is transmission-only.  No synapse occurs in a tract, so there
are no neurons, no thresholds, and no parameter memory at all — zero, and zero
because there is nothing to hold a threshold in, not because a threshold was struck.

The update equation is therefore complete in form and is the whole of the operation:

    out[line](t) = in[line](t - latency[channel(line)])

Nothing further about the arithmetic needs deciding.  What is missing is the delay
term and one decision about granularity, and the module raises on both rather than
choosing.  That is a different position from a section whose operation cannot be
named: here the operation is named and one quantity is absent.

A tract is where a conduction time would be derived from — fibre calibre,
myelination and length.  Across five entries this section carries one calibre
figure, no g-ratio anywhere, and no length anywhere, so all thirty-four latencies
read "to derive" and the module reports that as its own diagnosis rather than
substituting a uniform step.

NO HISTORY IN THIS FILE
-----------------------
No versions, no revision numbers, no "changed since", no provenance, no changelog,
no "formerly", no commented-out prior version.  A file that carries its own past
gives a reader two truths and no way to tell which is live.  When code here is
edited, its comment is updated in the same edit.

Comments explain the biological basis, and where relevant the compute or memory
tradeoff.  No hardware is named: the architecture sizes the hardware, not the
reverse.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from enum import Enum
from typing import Iterable


# ---------------------------------------------------------------------------
# Slot states, copied from the rungs above rather than translated.  Each names a
# different repair, and collapsing them into one "to derive" would make a claim
# the rung above did not make.
# ---------------------------------------------------------------------------

class SlotState(Enum):
    CONTENT = "content"
    NOT_APPLICABLE = "not applicable"   # a positive statement about the tissue
    UNKNOWN = "unknown"                 # exists, not measured — an experiment to run
    OWED = "owed"                       # described, not typed — known what research
    CONTESTED = "contested"             # measured several ways, needing adjudication
    TO_DERIVE = "to derive"             # the source has not supplied it


class EndpointKind(Enum):
    REGION_WITH_ENTRY = "a named region with an entry of its own"
    REGION_NO_ENTRY = "a named region with no entry in any of the twenty files"
    REGION_SPLIT = "two named regions, one with an entry and one without"
    REGION_NO_TRAFFIC = "named regions, and no entry declares the routed edge"
    CLASS_INTRINSIC = ("a class, and intrinsic to a tract: a commissure linking most "
                       "of cortex to most of cortex has no smaller honest producer")
    CLASS_OWED = "a class, and resolvable — owed at the source"
    STREAM = "a route rather than a region; an edge whose target is a route has no consumer"


class FarEnd(Enum):
    TWO_ENDED = "both region ends declare this routed edge and name this tract"
    ONE_END_ONLY = "named at one region end only"
    DECLARES_NO_SUCH_EDGE = "the far end has an entry and declares no routed edge here"
    NO_ENTRY = "the far end has no entry anywhere"
    NONE_DECLARED = "no entry in the source declares an edge routed through this limb"


class Direction(Enum):
    IN = "in"
    OUT = "out"


class Blocked(RuntimeError):
    """Raised where running would require a decision the description has not made.

    Carries the missing item and the rung that owns the repair, so a caller can tell
    a research gap from an unmade decision without reading the source.
    """

    def __init__(self, operation: str, missing: str, owner: str) -> None:
        super().__init__(f"{operation}: {missing} [repair owned by: {owner}]")
        self.operation, self.missing, self.owner = operation, missing, owner


# ---------------------------------------------------------------------------
# Data classes.
#
# There is no Population and no threshold array in this module.  A tract holds no
# neurons, so charging it either would assert structure it does not have — the same
# error as charging a threshold to a photoreceptor, one class further out.
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Channel:
    """A sub-element of a tract: a parallel channel, never a circuit stage.

    Tract sub-elements pass the different-target test and have no edges between
    them, because no synapse occurs in a tract.  Segments along a tract's course
    (the fornix's fimbria, crus, body, columns) are properties and not channels:
    the same fibres pass through all of them in sequence.
    """
    name: str
    note: str = ""


@dataclass(frozen=True)
class Tract:
    key: str
    name: str
    basis: str                        # whole / per side / per hemisphere
    bundled_tracts: tuple[str, ...]   # this entry's own tract first
    channels: tuple[Channel, ...]
    axons: tuple[int, int] | None     # (low, high) lines, or None where unrecorded
    axons_note: str
    per_channel_split: SlotState      # what would partition the index across channels
    calibre: str                      # fibre diameter, toward a conduction velocity
    myelination: str
    length: SlotState                 # the third term of a conduction time
    justification: str                # biological


@dataclass(frozen=True)
class RoutedEdge:
    """A region-to-region edge that rides on a tract.

    Not a payload transfer.  The payload is typed at the region that produces it and
    again at the one that consumes it; this line records which edge rides on which
    channel.  Fan-in and fan-out read none throughout, because no synapse occurs
    here.
    """
    tract: str
    direction: Direction
    endpoint: str
    kind: EndpointKind = EndpointKind.REGION_WITH_ENTRY
    far_file: str = ""
    far_state: FarEnd = FarEnd.DECLARES_NO_SUCH_EDGE
    channel: str = ""                 # the sub-element this edge is attributed to
    region_payload: str = ""          # typed at the region ends, carried not owned
    crosses_midline: bool = False
    note: str = ""

    # Uniform across the section and named rather than stored per edge: every fan
    # slot reads none, and every one of the 34 latencies reads "to derive".
    fan = SlotState.NOT_APPLICABLE
    latency = SlotState.TO_DERIVE


# ---------------------------------------------------------------------------
# The five tracts, in the architecture's order, which is the source's order.
# ---------------------------------------------------------------------------

TRACTS: tuple[Tract, ...] = (
    Tract(
        key="corpus_callosum",
        name="Corpus callosum — the great interhemispheric commissure",
        basis="whole",
        bundled_tracts=("corpus callosum", "anterior commissure",
                        "hippocampal commissure", "posterior commissure"),
        channels=(
            Channel("rostrum", "prefrontal; thin, slow fibres"),
            Channel("genu", "prefrontal; thin, slow fibres"),
            Channel("body", "motor and somatosensory; anterior, central, posterior parts"),
            Channel("isthmus", "parietal, temporal, occipital; large, fast fibres"),
            Channel("splenium", "parietal, temporal, occipital; large, fast fibres"),
        ),
        axons=(200_000_000, 300_000_000),
        axons_note=("electron microscopy in human material; the callosum's well-defined "
                    "borders make it one of the few exactly-countable tracts"),
        per_channel_split=SlotState.UNKNOWN,
        calibre="thin and slow rostrally; a minority of 3-5 um large fast fibres caudally",
        myelination="chiefly myelinated; g-ratio tracks the thin-to-thick gradient, no figure",
        length=SlotState.UNKNOWN,
        justification=(
            "Homotopic describes something different in each modality.  Where a "
            "sensory map has a representational midline the callosum joins two "
            "half-maps and its connections are restricted to the seam - the vertical "
            "meridian in vision, proximal body in somatosensation.  Where there is no "
            "midline, as in audition, they are widespread across the whole tonotopic "
            "map.  So a callosal edge is a seam-stitching device in one modality and a "
            "whole-map coupling in another, and a build reading the visual case as "
            "general would under-provision the auditory bandwidth badly.  All the "
            "fibres are excitatory and the inhibition is feedforward through "
            "interneurons they excite, so the lateralising effect is a property of the "
            "target circuit and not of the cable."
        ),
    ),
    Tract(
        key="internal_capsule",
        name="Internal capsule — the great projection tract",
        basis="per side",
        bundled_tracts=("internal capsule",),
        channels=(
            Channel("anterior limb", "frontopontine fibres; anterior thalamic radiation"),
            Channel("genu", "corticobulbar fibres to the cranial-nerve motor nuclei"),
            Channel("posterior limb", "corticospinal, corticorubral, superior thalamic radiation"),
            Channel("retrolenticular part", "the optic radiation"),
            Channel("sublenticular part", "the auditory radiation"),
        ),
        axons=(1_000_000, 1_100_000),
        axons_note=("the corticospinal component only, a classic order estimate; about "
                    "1.1 million pyramidal-tract fibres above the decussation from a "
                    "secondary compilation.  The thalamocortical radiations are unknown, "
                    "so the tract's full line count is not this figure"),
        per_channel_split=SlotState.UNKNOWN,
        calibre="not recorded",
        myelination="heavily myelinated projection tract; no g-ratio",
        length=SlotState.UNKNOWN,
        justification=(
            "This is where the map's geometry becomes a resource constraint, and the "
            "description says so through a lesion: every corticofugal and "
            "thalamocortical fibre in the hemisphere passes through one compact "
            "bundle, which is why a lacunar lesion of a few millimetres produces dense "
            "hemiplegia where a cortical lesion of the same volume would not.  The "
            "funnel is organised by destination rather than by origin - five limbs, "
            "five fibre systems, five targets.  And about a quarter of the "
            "corticothalamic fibres crossing it give no visible collateral to the "
            "reticular nucleus, so the copy the thalamic gate runs on is a sample of "
            "the cortex's outgoing traffic and not all of it."
        ),
    ),
    Tract(
        key="fornix",
        name="Fornix — the hippocampal output tract",
        basis="per side",
        bundled_tracts=("fornix",),
        channels=(
            Channel("post-commissural limb", "to mammillary bodies and anterior thalamus; Papez"),
            Channel("pre-commissural limb", "to septum and basal forebrain; the septal return"),
        ),
        axons=(1_000_000, 1_000_000),
        axons_note="soft, no clean human count pinned; classic order about 1 million",
        per_channel_split=SlotState.UNKNOWN,
        calibre="not recorded",
        myelination="myelinated tract; no g-ratio",
        length=SlotState.UNKNOWN,
        justification=(
            "This tract is why the hippocampal formation is a memory system rather "
            "than a memory store.  Its two limbs run in opposite functional directions "
            "to different targets: the post-commissural limb carries the completed "
            "episode out to the Papez circuit, and the pre-commissural limb carries "
            "the septal return in - cholinergic modulation, a theta timing reference "
            "and a tonic drive, on three separate lines from three cell populations in "
            "one nucleus.  A structure whose output cable also carries its own pacing "
            "signal is a loop and not a pipeline."
        ),
    ),
    Tract(
        key="arcuate_slf",
        name="Arcuate fasciculus / superior longitudinal fasciculus — the dorsal language tract",
        basis="per hemisphere",
        bundled_tracts=("arcuate / superior longitudinal fasciculus",
                        "inferior longitudinal fasciculus",
                        "inferior fronto-occipital fasciculus",
                        "uncinate fasciculus", "cingulum"),
        channels=(
            Channel("superior longitudinal fasciculus branch I", ""),
            Channel("superior longitudinal fasciculus branch II", ""),
            Channel("superior longitudinal fasciculus branch III",
                    "named on the supramarginal edge by both region ends"),
            Channel("arcuate",
                    "the arching temporo-frontal component; whether it is a branch of "
                    "the system or a tract beside it is contested and is carried as "
                    "contested, not resolved by preference"),
        ),
        axons=None,
        axons_note=("counts largely unknown.  One rare absolute estimate exists and "
                    "fits neither fan slot: a median of about 6,200 axons between "
                    "areas within a hemisphere and about 1,300 interhemispherically, "
                    "stated as under about 5% of the trunk.  It counts inter-areal "
                    "axons rather than contacts per cell; reconciliation is owed at "
                    "both ends"),
        per_channel_split=SlotState.UNKNOWN,
        calibre="not recorded",
        myelination="myelinated association fibres; no g-ratio",
        length=SlotState.UNKNOWN,
        justification=(
            "The sparse-connection finding cuts against the tract's own headline.  "
            "This is called the dorsal language pathway and the direct "
            "posterior-to-anterior connections are under about 5% of its axons.  So "
            "the language route is not a thick dedicated cable between two regions; it "
            "is a thin direct component inside a much larger bundle carrying other "
            "traffic, and a build provisioning it from its reputation would "
            "over-provision by more than an order of magnitude.  Left-dominance for "
            "language means the per-hemisphere basis here is not bookkeeping: the two "
            "sides carry different functional loads over the same anatomy."
        ),
    ),
    Tract(
        key="medial_longitudinal_fasciculus",
        name="Medial longitudinal fasciculus — the gaze-yoking brainstem tract",
        basis="per side",
        bundled_tracts=("medial longitudinal fasciculus",),
        channels=(
            Channel("ascending limb", "vestibulo-ocular and yoking traffic, rostral"),
            Channel("descending limb", "medial vestibulospinal fibres, caudal"),
        ),
        axons=None,
        axons_note="unknown at either limb",
        per_channel_split=SlotState.UNKNOWN,
        calibre="not recorded",
        myelination=("heavily myelinated, among the earliest tracts in the brain to "
                     "myelinate; g-ratio explicitly unknown"),
        length=SlotState.UNKNOWN,
        justification=(
            "This entry is the argument that a tract can be a computation's substrate "
            "without computing.  Conjugate gaze is not a property of either ocular "
            "motor nucleus; it is a property of the cable that yokes them, and the "
            "clinical signature proves it - a lesion of the tract dissociates the two "
            "eyes while both motor nuclei remain intact.  So the structure that "
            "computes nothing is the structure whose loss removes the function.  Its "
            "function is explicitly a speed claim - the fastest gaze-stabilising "
            "reflex, on a cable among the earliest to myelinate - and it carries no "
            "term of a velocity."
        ),
    ),
)

TRACT_BY_KEY = {t.key: t for t in TRACTS}

# Tracts bundled into an entry that carry no declared edge at either end.  This is
# the mirror of a region named on an edge with no entry, and it fails more silently,
# because the entry reads as complete on its own.
TRAFFICLESS_TRACTS: tuple[tuple[str, str], ...] = (
    ("anterior commissure", "corpus_callosum"),
    ("posterior commissure", "corpus_callosum"),
    ("inferior fronto-occipital fasciculus", "arcuate_slf"),
)

# Named on other entries' routed edges and having no entry anywhere in the source.
TRACTS_WITHOUT_ENTRIES: tuple[str, ...] = (
    "mammillothalamic tract",          # carries the Papez limb's next leg
    "middle longitudinal fasciculus",  # file 7 wrongly believes it has an entry here
)


# ---------------------------------------------------------------------------
# The 34 routed-edge declarations, entry by entry, in the architecture's order.
# ---------------------------------------------------------------------------

IN, OUT = Direction.IN, Direction.OUT
REGION, NOENTRY = EndpointKind.REGION_WITH_ENTRY, EndpointKind.REGION_NO_ENTRY
SPLIT, NOTRAFFIC = EndpointKind.REGION_SPLIT, EndpointKind.REGION_NO_TRAFFIC
CLASS_IN, CLASS_OWED = EndpointKind.CLASS_INTRINSIC, EndpointKind.CLASS_OWED
STREAM = EndpointKind.STREAM


def _r(tract: str, direction: Direction, endpoint: str, **kw) -> RoutedEdge:
    return RoutedEdge(tract=tract, direction=direction, endpoint=endpoint, **kw)


EDGES: tuple[RoutedEdge, ...] = (

    # -- Corpus callosum: three in, four out -------------------------------
    _r("corpus_callosum", IN, "the cerebral cortex of either hemisphere", kind=CLASS_IN,
       note="from callosal projection neurons in layers 3 and 5"),
    _r("corpus_callosum", IN, "the primary auditory cortex", far_file="2",
       far_state=FarEnd.TWO_ENDED, channel="body / splenium",
       region_payload=("the same frequency band's activity from the other hemisphere, "
                       "which sharpens rather than adds"),
       note="central body, posterior body and dorsal splenium; sector attribution "
            "declared at the far end and matched here"),
    _r("corpus_callosum", IN, "the inferior frontal gyrus", far_file="11",
       far_state=FarEnd.TWO_ENDED),
    _r("corpus_callosum", OUT, "the homotopic cortex of the opposite hemisphere",
       kind=CLASS_IN,
       note="terminates throughout layers 2-6, densest in 2 and 3, sparsest in layer 4 "
            "- the callosal input avoids the layer the thalamic driver targets"),
    _r("corpus_callosum", OUT, "heterotopic cortex of the opposite hemisphere",
       kind=CLASS_OWED, far_state=FarEnd.NONE_DECLARED,
       note="a separate limb, not a variant: sensory association cortices carry "
            "proportionally more of this traffic than primary sensory cortices"),
    _r("corpus_callosum", OUT,
       "the contralateral temporal lobe, olfactory structures and amygdala",
       kind=NOTRAFFIC, far_state=FarEnd.NONE_DECLARED, channel="anterior commissure",
       note="no entry in the source declares an edge routed through the anterior "
            "commissure"),
    _r("corpus_callosum", OUT,
       "the contralateral hippocampal formation, and the contralateral pretectal "
       "and vertical-gaze structures",
       kind=NOTRAFFIC, far_state=FarEnd.NONE_DECLARED,
       channel="hippocampal / posterior commissure",
       note="neither commissure's name appears anywhere in the source outside this "
            "entry; the posterior commissure's stated function belongs to structures "
            "that do have entries, and that entry does not name it"),

    # -- Internal capsule: two in, four out --------------------------------
    _r("internal_capsule", IN, "the cerebral cortex", kind=CLASS_IN,
       note="corticofugal fibres from every lobe; the named edges routed here are the "
            "corticospinal tract and the corticothalamic return traffic"),
    _r("internal_capsule", IN, "the thalamus", kind=CLASS_IN,
       note="the named thalamocortical edges routed here are the optic, auditory, "
            "superior thalamic and anterior thalamic radiations"),
    _r("internal_capsule", OUT, "the brainstem and spinal cord", far_file="16",
       far_state=FarEnd.TWO_ENDED, channel="posterior limb / genu",
       region_payload=("the corticospinal and corticobulbar motor commands, typed at "
                       "their cortical origins and at the ventral horn and "
                       "cranial-nerve nuclei that consume them")),
    _r("internal_capsule", OUT, "the thalamic reticular nucleus", far_file="12",
       far_state=FarEnd.TWO_ENDED,
       region_payload="the collateral copy of the cortex's outgoing traffic that the "
                      "reticular nucleus gates on",
       note="only about three quarters of the corticothalamic fibres passing through "
            "gave visible collaterals, so roughly a quarter did not - a finding about "
            "this tract rather than about the nucleus"),
    _r("internal_capsule", OUT, "the red nucleus", kind=NOENTRY,
       far_state=FarEnd.NO_ENTRY, channel="posterior limb",
       note="corticorubral fibres; the consumer has no entry in any of the twenty files"),
    _r("internal_capsule", OUT, "the pontine nuclei", kind=NOENTRY,
       far_state=FarEnd.NO_ENTRY, channel="anterior limb",
       note="frontopontine fibres; the load-bearing half, because the corticopontine "
            "stage is recorded elsewhere as transforming the payload rather than "
            "relaying it"),

    # -- Fornix: four in, three out ----------------------------------------
    _r("fornix", IN, "the hippocampal formation", far_file="8",
       far_state=FarEnd.TWO_ENDED, channel="post-commissural limb",
       region_payload=("the completed episode - the bound retrievable pattern, "
                       "addressable by any fragment of itself, and only partly "
                       "writable there, since an episode has no units and no frame"),
       note="from the subiculum, into the fimbria; the far end already writes its edge "
            "to this tract as a routing statement"),
    _r("fornix", IN, "the medial septum, cholinergic cells", far_file="13",
       far_state=FarEnd.TWO_ENDED, channel="pre-commissural limb",
       region_payload="a cholinergic modulatory signal"),
    _r("fornix", IN, "the medial septum, parvalbumin-expressing GABAergic pacemaker cells",
       far_file="13", far_state=FarEnd.TWO_ENDED, channel="pre-commissural limb",
       region_payload="the theta timing reference",
       note="the one line in the section whose entire content is a timing reference, "
            "so an unstated delay on it changes what the value means rather than only "
            "when it arrives"),
    _r("fornix", IN, "the medial septum, glutamatergic cells", far_file="13",
       far_state=FarEnd.TWO_ENDED, channel="pre-commissural limb",
       region_payload="a tonic drive"),
    _r("fornix", OUT, "the mammillary bodies and the anterior thalamic nuclei",
       far_file="8/12/14", far_state=FarEnd.TWO_ENDED, channel="post-commissural limb",
       region_payload="the completed episode",
       note="the Papez limb; every region stage has an entry, and the "
            "mammillothalamic tract carrying its next leg does not"),
    _r("fornix", OUT, "the hypothalamus", far_file="8/14", far_state=FarEnd.TWO_ENDED,
       note="payload owed at both region ends"),
    _r("fornix", OUT, "the septum and basal forebrain", kind=SPLIT, far_file="13",
       far_state=FarEnd.NO_ENTRY, channel="pre-commissural limb",
       note="the basal forebrain has an entry; the septal nuclei have no entry in any "
            "of the twenty files, so the return arm of the septo-hippocampal loop has "
            "a described tract, a described payload at one end, and no entry at the "
            "other"),

    # -- Arcuate / superior longitudinal fasciculus: three in, five out ----
    _r("arcuate_slf", IN, "the supramarginal gyrus", far_file="6/11",
       far_state=FarEnd.TWO_ENDED,
       channel="superior longitudinal fasciculus branch III",
       region_payload=("a praxis / action-sequence code and, on the left, a "
                       "phonological code - the sound-form of words for the "
                       "articulatory route, only partly writable there"),
       note="both region ends name this tract and branch III specifically"),
    _r("arcuate_slf", IN,
       "the posterior superior temporal gyrus and the sylvian parieto-temporal area",
       far_file="11", far_state=FarEnd.TWO_ENDED),
    _r("arcuate_slf", IN, "the temporal pole", far_file="7",
       far_state=FarEnd.ONE_END_ONLY,
       note="over the uncinate, inferior longitudinal, middle longitudinal and this "
            "tract; which pathway carries which edge is established only for the "
            "uncinate, and the far end wrongly states the middle longitudinal "
            "fasciculus has an entry here"),
    _r("arcuate_slf", OUT, "Broca's area and premotor cortex", far_file="6/11",
       far_state=FarEnd.TWO_ENDED),
    _r("arcuate_slf", OUT, "the orbitofrontal and ventrolateral prefrontal cortex",
       far_file="7", far_state=FarEnd.TWO_ENDED, channel="uncinate fasciculus",
       note="the one association pathway at that far end whose edge attribution is "
            "established"),
    _r("arcuate_slf", OUT, "the cingulate midline nodes", kind=CLASS_OWED,
       far_file="11/17", far_state=FarEnd.TWO_ENDED, channel="cingulum",
       note="four entries declare this tract by name, three of them recording it as "
            "routing rather than as an edge, which is the convention this entry uses"),
    _r("arcuate_slf", OUT, "occipito-temporal cortex", kind=CLASS_OWED, far_file="7",
       far_state=FarEnd.ONE_END_ONLY, channel="inferior longitudinal fasciculus",
       note="the ventral what-stream this tract is said to carry runs between entries "
            "in files 1 and 7, and neither declares a routed edge"),
    _r("arcuate_slf", OUT, "the ventral semantic stream", kind=STREAM,
       far_state=FarEnd.NONE_DECLARED, channel="inferior fronto-occipital fasciculus",
       note="the string appears nowhere in the source outside this entry; a tract with "
            "a stated function and no traffic"),

    # -- Medial longitudinal fasciculus: three in, three out ---------------
    _r("medial_longitudinal_fasciculus", IN, "the vestibular nuclei", far_file="3/15",
       far_state=FarEnd.TWO_ENDED, channel="ascending limb",
       region_payload=("the vestibulo-ocular reflex command - an eye-velocity signal "
                       "equal and opposite to head rotation, driven chiefly by the "
                       "semicircular-canal line, and the fastest gaze-stabilising "
                       "reflex")),
    _r("medial_longitudinal_fasciculus", IN, "the abducens nucleus", far_file="15",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE, channel="ascending limb",
       region_payload="the yoking signal that makes the two eyes move together in "
                      "horizontal gaze",
       note="from its internuclear neurons; the far end records the edge as one that "
            "should be typed as an internal edge and marks it owed"),
    _r("medial_longitudinal_fasciculus", IN, "the gaze neural integrators", far_file="15",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE, channel="ascending limb",
       region_payload="eye position - the integrated signal that holds the eye where "
                      "the burst put it",
       note="nucleus prepositus hypoglossi with the medial vestibular nucleus for "
            "horizontal, interstitial nucleus of Cajal for vertical; neither far end "
            "names this tract"),
    _r("medial_longitudinal_fasciculus", OUT, "the ocular motor nuclei", far_file="3/15",
       far_state=FarEnd.TWO_ENDED, channel="ascending limb",
       note="the oculomotor, trochlear and abducens nuclei; one of the few routed "
            "edges in the source declared, named and typed at both region ends before "
            "its tract had an entry at all"),
    _r("medial_longitudinal_fasciculus", OUT,
       "the contralateral oculomotor medial-rectus pool", far_file="15",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE, channel="ascending limb",
       crosses_midline=True,
       note="from the abducens internuclear neurons; this limb crosses the midline and "
            "no other limb of this tract does, and that crossing is what conjugate "
            "horizontal gaze consists of"),
    _r("medial_longitudinal_fasciculus", OUT, "the cervical spinal cord", far_file="3/16",
       far_state=FarEnd.DECLARES_NO_SUCH_EDGE, channel="descending limb",
       region_payload="a head- and neck-stabilising postural command",
       note="as the medial vestibulospinal fibres; neither far end names this tract, "
            "and neither separates the medial vestibulospinal tract from the lateral "
            "one, which descends elsewhere to different targets"),
)

# The three terms a conduction time needs, per tract, read off the entries above
# rather than sniffed out of their prose.  Only the corpus callosum records a fibre
# calibre, and it records one for its fast minority only; no entry records a g-ratio
# figure or a length.
LATENCY_TERMS: dict[str, tuple[SlotState, SlotState, SlotState]] = {
    #                                  calibre              g-ratio             length
    "corpus_callosum":                (SlotState.CONTENT,  SlotState.UNKNOWN, SlotState.UNKNOWN),
    "internal_capsule":               (SlotState.UNKNOWN,  SlotState.UNKNOWN, SlotState.UNKNOWN),
    "fornix":                         (SlotState.UNKNOWN,  SlotState.UNKNOWN, SlotState.UNKNOWN),
    "arcuate_slf":                    (SlotState.UNKNOWN,  SlotState.UNKNOWN, SlotState.UNKNOWN),
    "medial_longitudinal_fasciculus": (SlotState.UNKNOWN,  SlotState.UNKNOWN, SlotState.UNKNOWN),
}

# The architecture's own figures, held so the module's counts can be compared
# against them rather than assumed to agree.
ARCHITECTURE_FIGURES = {
    "routed_declarations": 34,
    "inbound": 15,
    "outbound": 19,
    "internal_edges": 0,
    "bundled_tracts": 12,
    "trafficless_tracts": 3,
}


# ---------------------------------------------------------------------------
# The operation.
# ---------------------------------------------------------------------------

def route(edge: RoutedEdge) -> str:
    """Return the delay expression for one routed edge.

    A tract applies a delay and nothing else.  There is no arithmetic to specify,
    no threshold to compare against, and no sign convention to fix, because nothing
    is compared with anything.  The form is complete:

        out[line](t) = in[line](t - latency[channel(line)])

    This returns the expression.  Evaluating it needs the delay, which reads
    "to derive" on all thirty-four edges.
    """
    channel = edge.channel or "the tract"
    return f"out[line](t) = in[line](t - latency[{channel}])   # latency: to derive"


def evaluate(edge: RoutedEdge, t: float):
    """Apply the delay.  Not runnable."""
    raise Blocked(
        f"evaluate({edge.tract} {edge.direction.value} {edge.endpoint!r})",
        "the conduction delay reads 'to derive'; a conduction time is a length over a "
        "velocity, and the section carries one fibre calibre, no g-ratio anywhere and "
        "no length anywhere",
        "the source - a length and a g-ratio per tract",
    )


def allocate(tract: Tract):
    """Size the routing index for one tract.  Blocked on a decision, not a measurement.

    A transmission-only structure's shape is a routing index from source line to
    destination, rank 1 - not an activity array.  Recording it as a zero-length
    tensor would assert state it does not hold.

    The extent is known at both bounds and the choice between them is unset: a
    routed edge is a region-to-region relation and a line is an axon, and the corpus
    callosum carries seven of the first and two to three hundred million of the
    second.  Which granularity the index is built at is downstream of the
    inter-structure connection topology.
    """
    lo, hi = index_bounds(tract)
    raise Blocked(
        f"allocate({tract.key!r})",
        f"the routing granularity is unset: the index has {lo} entries at routed-edge "
        f"granularity and {hi if hi else 'an unrecorded number'} at line granularity, "
        f"and the per-channel partition reads {tract.per_channel_split.value}",
        "Micky - inter-structure connection topology is on the "
        "surface-before-touching list",
    )


def step(*args, **kwargs):
    """There is no step, and that is the point rather than an omission.

    Every routed edge carries a nonzero, finite, heterogeneous delay in real time,
    and there is no global clock in the described system to replace them with.  A
    loop with real heterogeneous delays settles by its own dynamics; the same loop
    broken by registers becomes an iterated map whose trajectory depends on the
    update rate.  Uniform delay is a substitution, not an approximation.

    This section is where the substitution would bite hardest, because a tract's
    entire runtime memory is the delay line: setting every latency equal does not
    only change the dynamics, it changes the memory requirement.
    """
    raise Blocked(
        "step()",
        "the scheduling discipline is not set and all 34 edge latencies read "
        "'to derive', so a uniform interval has no value to take either",
        "Micky - the scheduling discipline is the design rung's largest open item",
    )


def learn(*args, **kwargs):
    """Adaptation is not applicable here, which is stronger than 'not set'.

    A tract holds no stored parameter, so there is nothing a learning rule could act
    on.  This is the one section where the absence of a rule is a positive statement
    about the structure rather than a decision waiting to be made.
    """
    raise Blocked(
        "learn()",
        "not applicable: a transmission-only structure holds no stored parameter for "
        "a rule to change",
        "nobody - this one is a property of the biology, not a gap",
    )


# ---------------------------------------------------------------------------
# Reports.
# ---------------------------------------------------------------------------

def index_bounds(tract: Tract) -> tuple[int, int | None]:
    """(routed-edge extent, line extent) for a tract's routing index."""
    edges = len([e for e in EDGES if e.tract == tract.key])
    return edges, (tract.axons[1] if tract.axons else None)


def index_bytes(lines: int) -> tuple[int, int]:
    """(index width in bits, store in bytes) for a rank-1 routing index."""
    bits = math.ceil(math.log2(lines))
    return bits, lines * bits // 8


def edge_reconciliation() -> str:
    ins = [e for e in EDGES if e.direction is Direction.IN]
    outs = [e for e in EDGES if e.direction is Direction.OUT]
    lines = [
        "ROUTED-EDGE RECONCILIATION",
        f"  in-declarations   {len(ins):3d}   (architecture: {ARCHITECTURE_FIGURES['inbound']})",
        f"  out-declarations  {len(outs):3d}   (architecture: {ARCHITECTURE_FIGURES['outbound']})",
        f"  total             {len(EDGES):3d}   (architecture: {ARCHITECTURE_FIGURES['routed_declarations']})",
        f"  internal edges      0   (architecture: {ARCHITECTURE_FIGURES['internal_edges']})",
        "",
        "  The zero is a positive statement at every entry: no synapse occurs in a",
        "  tract, so its sub-elements are parallel channels and not a circuit.",
        "",
        "  No declaration is a duplicate.  No tract in this file routes an edge to",
        "  another tract in this file, so 34 declarations are 34 distinct edges.",
    ]
    return "\n".join(lines)


def endpoint_census() -> str:
    counts: dict[EndpointKind, int] = {k: 0 for k in EndpointKind}
    for e in EDGES:
        counts[e.kind] += 1
    lines = ["ENDPOINT CENSUS"]
    for kind, n in counts.items():
        if n:
            lines.append(f"  {n:3d}  {kind.name.lower():20s} {kind.value}")
    lines.append("")
    lines.append("  A class endpoint at a tract is not the defect it is at a grey-matter")
    lines.append("  entry.  A commissure linking most of cortex to most of cortex has no")
    lines.append("  smaller honest producer, so those endpoints are intrinsic.  The ones")
    lines.append("  separated as owed are resolvable and have not been resolved.")
    lines.append("")
    lines.append("  regions with no entry anywhere:")
    for e in EDGES:
        if e.kind in (EndpointKind.REGION_NO_ENTRY, EndpointKind.REGION_SPLIT):
            lines.append(f"    {e.tract:32s} {e.direction.value:4s} {e.endpoint}")
    return "\n".join(lines)


def trafficless_report() -> str:
    """Tracts with a stated function and no declared edge at either end.

    The mirror of a region named on an edge with no entry, and it fails more
    silently: the entry reads as complete on its own, and no diff over endpoints
    will ever reach it.
    """
    lines = ["TRACTS WITH A STATED FUNCTION AND NO DECLARED TRAFFIC",
             f"  {len(TRAFFICLESS_TRACTS)} of the "
             f"{sum(len(t.bundled_tracts) for t in TRACTS)} tracts these five entries cover"
             f"   (architecture: {ARCHITECTURE_FIGURES['trafficless_tracts']})"]
    for name, owner in TRAFFICLESS_TRACTS:
        lines.append(f"    {name:44s} bundled into {owner}")
    lines.append("")
    lines.append("  And tracts named on other entries' edges with no entry anywhere:")
    for name in TRACTS_WITHOUT_ENTRIES:
        lines.append(f"    {name}")
    return "\n".join(lines)


def bundle_report() -> str:
    lines = ["BUNDLES — five entries, more than five tracts"]
    total = 0
    for t in TRACTS:
        n = len(t.bundled_tracts)
        total += n
        mark = "  <- bundle, split owed at the source" if n > 1 else ""
        lines.append(f"  {t.key:32s} {n} tract{'s' if n > 1 else ' '}{mark}")
        if n > 1:
            for b in t.bundled_tracts[1:]:
                lines.append(f"      also carries: {b}")
    lines.append(f"  {'total':32s} {total}"
                 f"   (architecture: {ARCHITECTURE_FIGURES['bundled_tracts']})")
    lines.append("")
    lines.append("  Not split here: splitting invents the arity, two rungs below where")
    lines.append("  the arity is known.")
    return "\n".join(lines)


def routing_index_report() -> str:
    """The fourth memory class, and the section's largest number.

    A routing index is not parameter memory - there is no threshold.  It is not
    state - nothing is carried between updates.  It is not edge storage - those are
    the values in flight, not the map that routes them.  So the architecture's three
    memory classes do not cover it, and a reader summing a Sizing column of zeros
    will read zero for a section that will not be free to build.
    """
    lines = ["ROUTING INDEX — rank 1, and not an activity array",
             f"  {'tract':32s} {'edges':>6} {'lines':>14} {'width':>6} {'store':>12}"]
    for t in TRACTS:
        lo, hi = index_bounds(t)
        if hi is None:
            lines.append(f"  {t.key:32s} {lo:6d} {'to derive':>14} {'-':>6} {'-':>12}")
            continue
        bits, byts = index_bytes(hi)
        lines.append(f"  {t.key:32s} {lo:6d} {hi:14,} {bits:4d} b "
                     f"{byts/1e6:9.1f} MB")
    lines.append("")
    lines.append("  The corpus callosum's index at line granularity exceeds the largest")
    lines.append("  parameter store in the map, for a structure whose parameter memory is")
    lines.append("  zero.  The cheapest structures by the sizing method are among the most")
    lines.append("  expensive to wire.")
    lines.append("")
    lines.append("  It is a bound in two directions, not a figure: the line granularity may")
    lines.append("  be wrong, and the width is a floor, since an index that must also name a")
    lines.append("  sub-element is wider.  Which granularity applies is downstream of the")
    lines.append("  connection topology, which is unset.")
    return "\n".join(lines)


def latency_substrate_report() -> str:
    """What a conduction time needs against what the section holds.

    A conduction time is a length over a velocity, and a velocity comes from fibre
    calibre and myelination.  This is the file those terms live in.
    """
    lines = ["LATENCY SUBSTRATE — a conduction time is length / velocity",
             f"  {'tract':32s} {'calibre':>10} {'g-ratio':>9} {'length':>10}"]
    have = [0, 0, 0]
    for t in TRACTS:
        terms = LATENCY_TERMS[t.key]
        for i, present in enumerate(terms):
            have[i] += present is not SlotState.UNKNOWN
        cells = ["partial" if p is SlotState.CONTENT and i == 0 else
                 "yes" if p is SlotState.CONTENT else "none"
                 for i, p in enumerate(terms)]
        lines.append(f"  {t.key:32s} {cells[0]:>10} {cells[1]:>9} {cells[2]:>10}")
    lines.append("")
    lines.append(f"  {have[0]} fibre-calibre figure across {len(TRACTS)} tracts, "
                 f"{have[1]} g-ratios, {have[2]} lengths.")
    lines.append("  So every latency in the section reads 'to derive', and the section")
    lines.append("  that would resolve them cannot.  The measurement that would move the")
    lines.append("  most is small and specific: a length and a g-ratio per tract.")
    return "\n".join(lines)


def sizing_report() -> str:
    lines = ["SIZING — parameter memory is zero at every entry",
             f"  {'tract':32s} {'basis':16} {'neurons':>8} {'axons':>28} {'param':>7}"]
    for t in TRACTS:
        ax = (f"{t.axons[0]:,} - {t.axons[1]:,}" if t.axons and t.axons[0] != t.axons[1]
              else f"~{t.axons[0]:,}" if t.axons else "unknown")
        lines.append(f"  {t.key:32s} {t.basis:16} {'none':>8} {ax:>28} {'0':>7}")
    lines.append("")
    lines.append("  Zero because there are no neurons to hold a threshold, not because a")
    lines.append("  threshold was struck.  The axon column is not summable: three bases")
    lines.append("  appear, and only the callosum's count is measured rather than estimated.")
    return "\n".join(lines)


def completion_test() -> str:
    blockers = {
        "corpus_callosum": "routing granularity; per-sector partition; every delay",
        "internal_capsule": "per-limb partition; the radiations' line counts; every delay",
        "fornix": "per-limb partition; every delay - and one payload IS a timing reference",
        "arcuate_slf": "per-branch partition; every delay; how laterality is expressed",
        "medial_longitudinal_fasciculus":
            "per-limb partition; every delay; how the crossing is carried",
    }
    lines = ["COMPLETION TEST — none of the five is finished"]
    for t in TRACTS:
        lines.append(f"  {t.key:32s} no   {blockers[t.key]}")
    lines.append("")
    lines.append("  The shape of the failure differs from a grey-matter section's.  Every")
    lines.append("  operation here is named, the update equation is complete in form at all")
    lines.append("  five entries, and what is missing is one quantity - the delay - plus one")
    lines.append("  decision about granularity.  That makes this the cheapest section worked")
    lines.append("  so far to finish, and it names its own price: a length and a g-ratio per")
    lines.append("  tract, and a ruling on routing granularity.  Neither is a payload")
    lines.append("  question and neither needs the connection topology.")
    return "\n".join(lines)


def report() -> str:
    return "\n\n".join((
        edge_reconciliation(),
        endpoint_census(),
        bundle_report(),
        trafficless_report(),
        sizing_report(),
        routing_index_report(),
        latency_substrate_report(),
        completion_test(),
    ))


if __name__ == "__main__":
    print(report())
    print()
    print("DELAY EXPRESSIONS, first three:")
    for e in EDGES[:3]:
        print(f"  {e.tract} {e.direction.value:4s} {e.endpoint[:44]:44s} {route(e)}")
    print()
    for fn, arg, label in ((evaluate, (EDGES[0], 0.0), "evaluation"),
                           (allocate, (TRACTS[0],), "allocation"),
                           (step, (), "scheduler"),
                           (learn, (), "adaptation")):
        try:
            fn(*arg)
        except Blocked as exc:
            print(f"{label:12} blocked: {exc}")
