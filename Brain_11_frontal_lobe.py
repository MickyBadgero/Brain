"""Brain — frontal lobe: premotor cortex to the frontal pole.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

Nine structures, twenty-five divisional sub-elements, 99 edges, and not one number
to size any of it.  No structure here has a neuron count and no edge has
a fan-in, so under the sizing model - parameter memory = neurons x log2(fan-in) / 8
bytes - both terms are open at every structure.  Nine Sizing fields read "to derive"
and they are one gap with nine instances, not nine independent gaps.  Every
per-structure store therefore reads None, and the sizing report correctly returns
nothing per structure: a report that returned plausible figures would be lying.

One aggregate is closed and it bounds most of the file.  Granular frontal cortex
anterior to the corpus callosum holds ~640M neurons per hemisphere, a fraction
constant across primates rather than human-expanded.  Under the log2 cap the whole
granular prefrontal parameter store sits between ~0.96 and ~1.28 GB per hemisphere
across the entire plausible fan-in range - a spread of 1.33x.  That is a SUM over
structures and is never entered against one of them; the per-area partition of the
640M is what every individual Sizing field is waiting on.

The element class is uniform, and that is a positive statement about this section
rather than an omission.  Every population here is a threshold gate: it fires when
the count of active inputs reaches a stored threshold, so the only value held per
neuron is that threshold.  There is no transducer, no graded non-spiking element, no
sign-inverting stage and no transmission-only structure anywhere in the nine, so the
four element classes collapse to one and this module needs one code path where the
visual line needs three.  What blocks it is arithmetic and topography instead.

Counting basis is uniform - per hemisphere at every structure - and that is not a
licence to fold the two sides together.  Broca's area and its right-hemisphere
homologue are separate structures doing different jobs, with a measured volume and
neuron-number asymmetry between them, and a single number covering both would assert
a symmetry the biology denies.

Every edge latency reads None, meaning to derive, on all 106.  The absence is total
rather than partial: no conduction time, no synaptic delay, no loop latency, and no
myelination figure at any of the nine structures to derive one from.  None is not a
licence to substitute zero or a uniform interval.  The delays are heterogeneous and
are what make a re-entrant loop well defined, and there is no global clock in the
described system to replace them with.  This section's loops are the slow ones: an
interval short enough to carry the finest edge in the system would be set by the
fastest loop in the map, which lies in sections this module does not hold.

The vocabulary is imported and not redefined.  Structure, Population, Endpoint,
Representation and Edge are declared once, in Brain_config, because an edge that
leaves this file is declared at both ends in two files, and two files cannot describe
one edge in agreement when the type describing it is defined twice.  What stays here
is the content: the counts, shapes, extents, sub-elements, edges and findings, which
is where they are derived and where a fidelity pass diffs them against the
architecture entry above.

Every cross-file endpoint carries the far file's stem, <nn>_<section>, never its
number alone; Endpoint's own validation rejects a stem that does not begin <nn>_.  An
endpoint with no stem is a reading not yet done, not a claim that no far end exists,
and the states are told apart rather than collapsed.
"""

from Brain_config import (
    # element classes
    THRESHOLD_GATE,
    # open states
    TO_DERIVE, UNKNOWN, OWED, CONTESTED, RESISTED,
    # counting basis
    PER_HEMISPHERE,
    # endpoint kinds and constructors
    Endpoint, far, here, class_endpoint, unstemmed,
    CLASS_ENDPOINT, NO_ENTRY, UNSTEMMED, LOCAL,
    # representation
    Representation, EVENT_DRIVEN, NO_FRAME,
    # populations and structures
    Population, Structure, FAN_IN_CEILING_BITS,
    # edges
    Edge, DRIVER, MODULATORY,
    # shared reports and the unset decisions
    sizing_report as config_sizing_report,
    edge_report as config_edge_report,
    representation_report,
)

BASIS = PER_HEMISPHERE

# Granular frontal cortex anterior to the corpus callosum, per hemisphere.  A sum
# over structures; never attributed to one of them.
PREFRONTAL_NEURON_BUDGET = 640_000_000

# The laminar sets named in this file.  Neither is a default: which one applies is a
# claim about the architecture of the named area, and where the source does not
# settle it the sub-element carries an open state instead of a set.
GRANULAR_8 = ("1", "2", "3", "4", "5a", "5b", "6a", "6b")
AGRANULAR_7 = ("1", "2", "3", "5a", "5b", "6a", "6b")

# States a laminar extent can be in beyond a set.  These are content, not shared
# vocabulary: they record how well this section's source settled a slot.
BOUNDED_AT_7 = "to derive per sub-element, bounded at 7"

# --------------------------------------------------------------------------
# Structures, in data-flow order.
#
# Sub-elements are the endpoints edges have, not a further level of detail below
# them.  partitions=False everywhere: the neuron count does not divide among the
# sub-elements because there is no neuron count to divide.
# --------------------------------------------------------------------------


def _cortex(name="cortical neurons", note=""):
    """Every population in this section: a cortical threshold gate, both terms open."""
    return Population(name, THRESHOLD_GATE, BASIS, count=None, fan_in=None, note=note)


PREMOTOR = Structure(
    name="premotor cortex and the supplementary motor areas",
    populations=(_cortex(note="outside the ~640M granular prefrontal budget: posterior "
                              "frontal, agranular-to-dysgranular, lower density, and the "
                              "source says so explicitly"),),
    subelements=("F2 - dorsal premotor", "F4 - ventral premotor", "F5 - ventral premotor",
                 "supplementary motor area", "pre-supplementary motor area"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

FRONTAL_EYE_FIELDS = Structure(
    name="frontal eye fields",
    populations=(_cortex(note="granular frontal isocortex, and the source does not "
                              "attribute it to the ~640M budget - recorded as a third "
                              "state, neither inside nor excluded"),),
    subelements=("saccade area", "pursuit area"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

BROCA = Structure(
    name="Broca's area - inferior frontal gyrus",
    populations=(_cortex(note="the cheapest open count in the file: a human "
                              "stereological study reporting volume and total neuron "
                              "number for areas 44 and 45 is cited at the source with "
                              "the neuron figure not transcribed"),),
    subelements=("Brodmann area 44 - pars opercularis", "Brodmann area 45 - pars triangularis"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

RIGHT_IFG = Structure(
    name="right inferior frontal gyrus",
    populations=(_cortex(note="bounded above by Broca's count once that is firmed - the "
                              "smaller side of the documented left-greater-than-right "
                              "area 44 asymmetry. An ordering constraint, not a number"),),
    subelements=("right Brodmann area 44", "right Brodmann area 45"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

DORSOLATERAL = Structure(
    name="dorsolateral prefrontal cortex",
    populations=(_cortex(note="inside the ~640M granular prefrontal budget; its share of "
                              "that budget is the open quantity, not the budget"),),
    subelements=("Brodmann area 9", "Brodmann area 46", "caudal principal sulcus"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

VENTROLATERAL = Structure(
    name="ventrolateral prefrontal cortex",
    populations=(_cortex(note="inside the ~640M budget, and the area 45 overlap with "
                              "Broca's area makes even the partition ill-posed: a count "
                              "for area 45 cannot be assigned to one structure or the "
                              "other while both claim it undivided"),),
    subelements=("Brodmann area 45", "Brodmann area 47"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

ORBITOFRONTAL = Structure(
    name="orbitofrontal / ventromedial prefrontal cortex",
    populations=(_cortex(note="inside the ~640M budget with a caveat: the budget is "
                              "defined over granular frontal cortex and area 25 is "
                              "agranular, so the five sub-elements are not all inside it "
                              "on the same footing"),),
    subelements=("Brodmann area 11", "Brodmann area 13", "Brodmann area 14",
                 "Brodmann area 25", "Brodmann area 32"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

ANTERIOR_CINGULATE = Structure(
    name="anterior cingulate cortex",
    populations=(_cortex(note="NOT attributed to the ~640M budget and not to be counted "
                              "inside it without a decision: the budget is defined over "
                              "granular frontal cortex and this cortex is "
                              "agranular-to-dysgranular"),),
    subelements=("Brodmann area 24", "Brodmann area 32"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

FRONTOPOLAR = Structure(
    name="frontopolar cortex",
    populations=(_cortex(note="inside the ~640M budget and taking the largest share of "
                              "it - the largest single prefrontal subdivision. An "
                              "ordering constraint on the partition, and the only one "
                              "the file supplies"),),
    subelements=("medial / midline", "lateral"),
    rank=3,
    axes=("laminar sub-element", "H", "W"),
    partitions=False,
)

STRUCTURES = (PREMOTOR, FRONTAL_EYE_FIELDS, BROCA, RIGHT_IFG, DORSOLATERAL,
              VENTROLATERAL, ORBITOFRONTAL, ANTERIOR_CINGULATE, FRONTOPOLAR)

# --------------------------------------------------------------------------
# Laminar extent, per divisional sub-element.
#
# It sits here rather than on the structure because it differs WITHIN a structure:
# Brodmann area 44 is agranular at 7 and area 45 is granular at 8, inside one entry.
# A design that hung this on the structure could not express that entry at all.
#
# The open states are kept distinct and are not collapsed to one another.  UNKNOWN,
# OWED and CONTESTED say different things, and writing TO_DERIVE over CONTESTED would
# assert nobody has looked when the problem is that several people have and disagree.
# --------------------------------------------------------------------------

LAMINAE = {
    ("premotor cortex and the supplementary motor areas", "*"):
        TO_DERIVE + " per sub-element - eight laminae are named, but the sheet is "
                    "agranular-to-dysgranular and layer 4 is thin or absent over part of "
                    "its extent, so the extent is not uniform across the tangential axes",
    ("frontal eye fields", "saccade area"): GRANULAR_8,
    ("frontal eye fields", "pursuit area"): GRANULAR_8,
    ("Broca's area - inferior frontal gyrus", "Brodmann area 44 - pars opercularis"): AGRANULAR_7,
    ("Broca's area - inferior frontal gyrus", "Brodmann area 45 - pars triangularis"): GRANULAR_8,
    ("right inferior frontal gyrus", "right Brodmann area 44"):
        CONTESTED + " for this side - by homology it would be 7, and whether the "
                    "agranular/granular difference holds on the right is not established",
    ("right inferior frontal gyrus", "right Brodmann area 45"):
        CONTESTED + " for this side - by homology it would be 8",
    ("dorsolateral prefrontal cortex", "*"): GRANULAR_8,
    ("ventrolateral prefrontal cortex", "*"): GRANULAR_8,
    ("orbitofrontal / ventromedial prefrontal cortex", "*"):
        TO_DERIVE + " per sub-element AND differing across them - areas 11 and 13 orbital "
                    "granular-to-dysgranular, area 25 agranular, area 32 transitional",
    ("anterior cingulate cortex", "*"): BOUNDED_AT_7,
    ("frontopolar cortex", "*"): GRANULAR_8,
}

# Tangential organisation.  Every extent reads to derive because no tile pitch is
# measured anywhere in this file, in millimetres or micrometres.  What differs
# between structures is the prior question of whether there is a map to index at all.
TANGENTIAL = {
    "premotor cortex and the supplementary motor areas":
        "whether the sheet is somatotopic at all is open at the source: the "
        "reach-and-grasp mapping implies a body map and does not establish one",
    "frontal eye fields":
        "a saccade area generating movements to retinotopic targets implies a motor map "
        "of saccade vectors; whether that map is a compartmentation an edge could "
        "terminate on is not established. An implied map is not an index",
    "Broca's area - inferior frontal gyrus":
        "the area 44 / area 45 border is conventionally taken at the ascending ramus of "
        "the lateral sulcus, and the rami are highly variable while the sulcus diagonalis "
        "is present in about half of hemispheres. Not a naming dispute and not fixable by "
        "renaming: the two sub-elements' tangential extents are individually variable",
    "right inferior frontal gyrus": "no pitch measured",
    "dorsolateral prefrontal cortex":
        "load-bearing here in a way it is not elsewhere: working memory across delays is "
        "attributed to recurrent local connectivity, so the extent over which recurrence "
        "runs IS the structure's stated function, and it is unsized",
    "ventrolateral prefrontal cortex":
        "the tangential extent overlaps Broca's and the overlap is real, not a "
        "bookkeeping error; it is also wider than area 45, imaging routinely including "
        "area 47 and ventral area 6 in what is called Broca's region",
    "orbitofrontal / ventromedial prefrontal cortex":
        "the value axis this structure computes on is body-relative - zero and slope set "
        "by motivational state, there being no receptors for reward - and whether that "
        "axis is a spatial organisation here or a population code is not established",
    "anterior cingulate cortex": "no pitch measured",
    "frontopolar cortex":
        "the medial/lateral division is the one tangential boundary in this file with a "
        "quantitative basis - the afferent-origin fractions - and it is still not a pitch",
}

# Sub-elements whose status is provisional rather than settled.  Declared, and not
# allocated: allocating the sulcus as a peer of area 46 would double-count, and
# folding it in would discard a distinction two far ends are using.
PROVISIONAL_SUBELEMENTS = {
    ("dorsolateral prefrontal cortex", "caudal principal sulcus"):
        "named by an edge and not by the heading - a location within area 46 rather than "
        "either named area; whether it is a sub-element of area 46 or a separate one is "
        "owed at the source",
}

# A cell class, not a sheet axis, and it would not become one.  A large projection
# cell type concentrated in this structure and in the insula.  Whether it has its own
# targets - and so whether an edge could terminate on it - is not stated at the
# source, so it is declared beside the shape rather than inside it.
CELL_CLASS_SUBELEMENTS = {
    "anterior cingulate cortex": ("von Economo (spindle) neurons",
                                  "sub-element status not established"),
}

# Two structures claim one undivided area.  Inherited from the naming schemes -
# Broca's area is classically 44 plus 45, the ventrolateral structure is 45 plus 47 -
# and not a bookkeeping error.  A proposed division exists and is unadopted, so
# allocation of either structure is blocked and not merely unsized: a missing
# partition leaves an array unsized, an unresolved overlap makes two arrays wrong
# together in a way that sums cleanly and looks right.
CONTESTED_SUBELEMENTS = (
    ("Brodmann area 45",
     "Broca's area - inferior frontal gyrus",
     "ventrolateral prefrontal cortex",
     "proposed at the source: 45B / 45p to Broca's area, 45A / 45a to the "
     "ventrolateral structure - UNADOPTED"),
)

# A second name for one sub-element, carried because two edges in this file
# terminate on it under that name.  Without the correspondence those edges land on a
# name this structure does not use.
SUBELEMENT_ALIASES = {
    ("ventrolateral prefrontal cortex", "area 12"): "Brodmann area 47",
}

# --------------------------------------------------------------------------
# Edges.
#
# The architecture declares 106 edge bullets: 63 in, 43 out.  Eleven of those edges
# have both ends in this file, and seven of the eleven are written at both ends - once
# in the producer's Outputs and once in the consumer's Inputs.  That redundancy is what
# makes a payload mechanically checkable one rung up; it does not survive into a rung
# where an edge is ONE OBJECT.  So 106 declarations collapse to 99 edges here, and the
# collapse is arithmetic rather than a dropped edge: 106 - 7 = 99.
#
# The remaining four in-file edges are declared at ONE end only, and all four are the
# same inherited gap: premotor cortex declares neither its edge to Broca's area nor its
# edge to the right inferior frontal gyrus, and neither of those declares its return.
# They are held below so the declaration count can be reconstructed exactly.
#
# latency_s is real time in seconds and is None on every edge here, meaning to
# derive.  It is never expressed in steps: a latency stated in steps has assumed a
# clock.
# --------------------------------------------------------------------------

PM = "premotor cortex and the supplementary motor areas"
FEF = "frontal eye fields"
BRO = "Broca's area - inferior frontal gyrus"
RIF = "right inferior frontal gyrus"
DL = "dorsolateral prefrontal cortex"
VL = "ventrolateral prefrontal cortex"
OFC = "orbitofrontal / ventromedial prefrontal cortex"
ACC = "anterior cingulate cortex"
FP = "frontopolar cortex"

S_VISUAL = "01_visual_pathway"
S_PARIETAL_DORSAL = "04_dorsal_visual_parietal_stream"
S_SENSORIMOTOR = "05_sensorimotor_loop"
S_POSTERIOR_PARIETAL = "06_posterior_parietal"
S_TEMPORAL_POLE = "07_anterior_temporal_lobe"
S_MEDIAL_TEMPORAL = "08_medial_temporal_lobe"
S_BASAL_GANGLIA = "09_basal_ganglia"
S_THALAMUS = "12_thalamus"
S_NEUROMOD = "13_neuromodulatory_systems"
S_BRAINSTEM = "14_brainstem_midbrain_hypothalamus"
S_INSULA = "17_insula_claustrum_habenula"

# Representations that are not entirely open.  Declared once per line and inherited
# by every consumer of that line.  Update timing is event-driven on every line in
# this file without exception: no structure here is a sensor, none has a rate of its
# own, and there is no system clock to borrow one from.

MEDIODORSAL_AMPLIFICATION = Representation(
    units="a gain on the consumer's own recurrent activity - not a content line",
    value_range=TO_DERIVE + " - a gain inherits the range of what it acts on",
    update_timing=EVENT_DRIVEN,
    frame=NO_FRAME + " - no categorical content of any kind",
)

REWARD_VALUE = Representation(
    units="scalar reward value: expected magnitude, and the mismatch between expected "
          "and received - firing to unexpected reward and to expected-but-omitted reward",
    value_range=TO_DERIVE,
    update_timing=EVENT_DRIVEN,
    frame="body-relative - zero and slope set by bodily and motivational state. The one "
          "stated coordinate frame in this file",
)

SACCADE_GOAL = Representation(
    units="a saccade goal: the cortically selected target location",
    value_range=TO_DERIVE,
    update_timing=EVENT_DRIVEN,
    frame="eye-centred",
)

VALENCE_TAG = Representation(
    units="a gain on perception, attention and memory encoding, carrying no identity of "
          "its own",
    value_range=TO_DERIVE,
    update_timing=EVENT_DRIVEN,
    frame=NO_FRAME,
)

# The four in-file edges the architecture declares at one end only.  Kept as data
# rather than as prose so that the per-structure declaration counts can be rebuilt from
# this file and checked against the entries above.
PRODUCER_SILENT = frozenset({(PM, BRO), (PM, RIF)})
"""Declared in the consumer's Inputs; the producer's Outputs slot does not carry them."""

CONSUMER_SILENT = frozenset({(BRO, PM), (RIF, PM)})
"""Declared in the producer's Outputs; the consumer's Inputs slot does not carry them."""

ARCHITECTURE_DECLARATIONS = (63, 43)
"""In and out bullet counts stated by the architecture header, for the check below."""

EDGES: tuple[Edge, ...] = (
    # ---- 1. premotor cortex and the supplementary motor areas: 13 in, 6 out ----
    Edge(far("superior parietal area 5", S_SENSORIMOTOR, "area PE"), here(PM),
         note="the producer names dorsal premotor cortex; the reference frame is "
              "contested there - body-, shoulder- and hand-centred across studies - and "
              "on the payload rule the frame is part of the payload"),
    Edge(far("anterior intraparietal area", S_POSTERIOR_PARIETAL), here(PM, "F5 - ventral premotor")),
    Edge(far("medial intraparietal area", S_POSTERIOR_PARIETAL), here(PM, "F2 - dorsal premotor")),
    Edge(far("ventral intraparietal area", S_PARIETAL_DORSAL), here(PM, "F4 - ventral premotor")),
    Edge(far("supramarginal gyrus", S_POSTERIOR_PARIETAL), here(PM)),
    Edge(far("precuneus", S_POSTERIOR_PARIETAL, "anterior sensorimotor sector"), here(PM)),
    Edge(far("primary somatosensory cortex", S_SENSORIMOTOR, "area 3a"), here(PM)),
    Edge(far("secondary somatosensory cortex", S_SENSORIMOTOR, "parietal ventral area"),
         here(PM)),
    Edge(far("ventral anterior / ventral lateral thalamus", S_THALAMUS), here(PM)),
    Edge(far("midcingulate cortex", S_INSULA, "cingulate motor areas"), here(PM),
         carries="the convergence of reward or non-reward outcome with action and spatial "
                 "information, turned into a motor plan",
         note="two-ended and confirmed; the type is the producer's and is carried, not "
              "asserted here. Payload owed at that end and untyped at this one"),
    Edge(far("amygdala", S_MEDIAL_TEMPORAL,
             "intermediate and magnocellular divisions of the basal nucleus"), here(PM),
         carries="the valence tag; payload otherwise owed",
         role=MODULATORY, representation=VALENCE_TAG,
         note="two-ended. Terminations in ventral area 6, lighter in dorsal area 6; "
              "ipsilateral only; deep layer I, layer II and layer VI. WHICH sub-element "
              "receives it is owed and is not resolvable from the producer's evidence - "
              "the study divides area 6 dorsally and ventrally, this structure by F-number"),

    Edge(here(PM), far("primary motor cortex", S_SENSORIMOTOR),
         carries="the planned action - a movement, already sequenced and shaped, not yet "
                 "a muscle command"),
    Edge(here(PM), unstemmed("corticospinal tract"),
         note="from a minority of cells. The tract's consumer is muscle, which is outside "
              "the map's scope on the body side: this edge terminates at the SCOPE "
              "BOUNDARY. It does not close, and that is correct rather than defective"),
    Edge(here(PM), far("basal ganglia", S_BASAL_GANGLIA, "motor striatum"),
         note="the consumer declares its cortical source as a class covering all of "
              "cortex, so this edge is two-ended in one direction only. The sector named "
              "here is load-bearing at the far end and unusable there: that entry marks "
              "its motor / associative / limbic partition as named and unbounded"),
    Edge(here(PM), far("superior parietal area 5", S_SENSORIMOTOR)),
    Edge(here(PM, "F2 - dorsal premotor"), far("medial intraparietal area", S_POSTERIOR_PARIETAL)),
    Edge(here(PM, "F4 and F5 - ventral premotor"),
         far("medial intraparietal area", S_POSTERIOR_PARIETAL),
         note="one bullet at the source, split from the F2 limb because they leave from "
              "different sub-elements; collapsing them would lose which sub-element each "
              "departs from"),

    # ---- 2. frontal eye fields: 5 in, 6 out ----
    Edge(far("lateral intraparietal area", S_PARIETAL_DORSAL), here(FEF),
         note="two-ended and agreeing"),
    Edge(class_endpoint("posterior parietal cortex, beyond the lateral intraparietal area"),
         here(FEF),
         note="class endpoint, and it resolves nowhere: the parietal files were read at "
              "the source and no other parietal structure declares an output here"),
    Edge(far("mediodorsal nucleus", S_THALAMUS), here(FEF),
         carries="no categorical content; modulatory amplification, raising the gain of "
                 "this structure's local recurrent connectivity",
         role=MODULATORY, representation=MEDIODORSAL_AMPLIFICATION,
         note="declared at the producer as five separate named outputs, one per consumer, "
              "not as a class. WHICH division, and whether the amplification is tuned per "
              "consumer, is owed at the source and decides whether five edges or one is "
              "the right arity"),
    Edge(far("caudal auditory belt", "02_auditory_pathway"), here(FEF),
         carries="the where stream's motor purpose - moving the eyes to the sound",
         note="confirmed two-ended; the producer writes all three of its prefrontal "
              "targets on one line, so the arity is owed there and not here"),

    Edge(here(FEF), far("superior colliculus", S_BRAINSTEM, "intermediate layers"),
         carries="a saccade goal - the cortically selected target location in eye-centred "
                 "coordinates; payload otherwise owed",
         representation=SACCADE_GOAL,
         note="typed at the consumer and untyped at the producer; the termination layer - "
              "intermediate, not the superficial visual ones - exists only at the consumer"),
    Edge(here(FEF), class_endpoint("brainstem saccade generators"),
         note="class endpoint, and unchecked - the cranial-nerve-nuclei file was not read "
              "at the source"),
    Edge(here(FEF), far("lateral intraparietal area", S_PARIETAL_DORSAL),
         carries="the corollary discharge of the saccade command",
         note="the relay nucleus on the second leg is unnamed: the mediodorsal entry names "
              "this structure and contains no intraparietal target of any kind. Owed at "
              "the source, in 12_thalamus or here"),
    Edge(here(FEF), far("middle temporal area", S_PARIETAL_DORSAL, "all cortical layers"),
         note="two-ended and confirmed; the far end is the typed one, carrying the spatial "
              "attentional gain signal - an enhancement or suppression by location, not a "
              "stimulus code"),
    Edge(here(FEF, "pursuit area"), far("medial superior temporal area", S_PARIETAL_DORSAL),
         note="reciprocal; two-ended and confirmed, typed at the far end as pursuit and "
              "gaze-target velocity"),
    Edge(here(FEF, "pursuit area"), far("ventral intraparietal area", S_PARIETAL_DORSAL),
         note="reciprocal; two-ended and confirmed, the far end owing the payload as this "
              "end does"),

    # ---- 3. Broca's area: 4 in, 2 out ----
    Edge(unstemmed("posterior superior temporal gyrus and area Spt"), here(BRO),
         note="via the arcuate fasciculus, which has an entry in 18_white_matter_tracts. "
              "Far end unchecked at the source"),
    Edge(far("supramarginal gyrus", S_POSTERIOR_PARIETAL), here(BRO),
         note="via the arcuate fasciculus and superior longitudinal fasciculus III"),
    Edge(here(PM), here(BRO),
         note="DECLARED AT THIS END ONLY: the producer does not declare it; inherited gap"),

    Edge(here(BRO), here(PM),
         carries="the articulatory plan - the phonological and syntactic structure "
                 "rendered as a motor sequence; payload otherwise owed",
         note="COMPOUND ENDPOINT: the source names premotor AND primary motor cortex on "
              "one bullet. Producer-only at BOTH targets - neither this file's premotor "
              "structure nor primary motor cortex in 05_sensorimotor_loop declares it - so "
              "the owed repair is two edges at two files, not one. Splitting the endpoint "
              "is owed at the source"),
    Edge(here(BRO), class_endpoint("temporoparietal cortex"),
         note="reciprocal. One member resolves - the supramarginal gyrus, which declares "
              "the reciprocal input in 06_posterior_parietal; the others are unnamed"),

    # ---- 4. right inferior frontal gyrus: 6 in, 2 out ----
    Edge(unstemmed("right auditory prosodic stream - right superior temporal gyrus and "
                   "sulcus homologues"), here(RIF),
         note="far end unchecked at the source"),
    Edge(far("amygdala", S_MEDIAL_TEMPORAL, "basal and accessory basal nuclei"), here(RIF)),
    Edge(far("anterior insula", S_INSULA), here(RIF),
         carries="the salience signal: this event is behaviourally relevant now; payload "
                 "otherwise owed",
         note="two-ended and confirmed; the producer declares this structure on its own "
              "line"),
    Edge(here(PM), here(RIF),
         note="DECLARED AT THIS END ONLY: the producer does not declare it; inherited gap"),
    Edge(unstemmed("contralateral inferior frontal gyrus"), here(RIF),
         role=MODULATORY,
         note="via the corpus callosum, which has an entry in 18_white_matter_tracts. "
              "Origin layers 3 and 5, termination throughout layers 2-6, densest in 2 and "
              "3 and SPARSEST IN LAYER 4 - so it avoids the layer a thalamic driver "
              "targets, which is why the role is modulatory rather than driving. All "
              "callosal fibres are excitatory; inhibitory effects are feedforward through "
              "local interneurons"),

    Edge(here(RIF), here(PM),
         note="COMPOUND ENDPOINT: premotor AND primary motor cortex on one bullet. The "
              "premotor consumer does not declare it; the primary motor consumer does not "
              "declare it either, checked - the same result as the homologous edge at "
              "Broca's area"),
    Edge(here(RIF), class_endpoint("right temporoparietal cortex"),
         note="reciprocal. The far end in 06_posterior_parietal declares an output to the "
              "ventral-attention frontoparietal network, itself an endpoint that does not "
              "resolve to nodes. TWO UNRESOLVED CLASSES POINTING AT EACH OTHER ARE NOT A "
              "TWO-ENDED EDGE and are not paired here"),

    # ---- 5. dorsolateral prefrontal cortex: 8 in, 7 out ----
    Edge(far("lateral intraparietal area", S_PARIETAL_DORSAL), here(DL, "Brodmann area 46"),
         note="two-ended and agreeing; the producer names area 46"),
    Edge(far("angular gyrus", S_POSTERIOR_PARIETAL), here(DL),
         note="macaque area 7a. The producer declares an output to the ventrolateral "
              "prefrontal cortex and not to this structure, confirmed by reading that "
              "entry: consumer-only. Owed at the source - establish it, or withdraw it"),
    Edge(far("mediodorsal nucleus", S_THALAMUS), here(DL),
         carries="no categorical content; modulatory amplification, raising the gain of "
                 "this structure's local recurrent connectivity",
         role=MODULATORY, representation=MEDIODORSAL_AMPLIFICATION,
         note="the edge this structure's headline function depends on"),
    Edge(far("ventral tegmental area", S_NEUROMOD), here(DL),
         carries="dopamine setting the gain on prefrontal working-memory and rule "
                 "representations; payload otherwise owed",
         role=MODULATORY,
         note="the mesocortical projection. Two-ended and confirmed, and this is the ONLY "
              "entry in this file that declares the limb, so the producer's class has "
              "exactly one member here. Two different gain sources are therefore declared "
              "onto one structure and neither entry says how they differ - owed at the "
              "source"),
    Edge(class_endpoint("other prefrontal cortex"), here(DL),
         note="unresolved. Of the four in-file candidates the anterior cingulate cortex "
              "declares an output here and the frontopolar cortex declares one to a class "
              "that covers it; the ventrolateral and orbitofrontal structures declare "
              "nothing"),
    Edge(far("amygdala", S_MEDIAL_TEMPORAL,
             "intermediate and magnocellular divisions of the basal nucleus"), here(DL),
         carries="the valence tag; payload otherwise owed",
         role=MODULATORY, representation=VALENCE_TAG,
         note="two-ended. Terminations in Brodmann area 9 medially and laterally and "
              "patchily in area 46, lower bank of the principal sulcus; ipsilateral only; "
              "deep layer I, layer II and layer VI. The lightest and least consistent of "
              "the producer's four lateral edges. The area 46 limb lands on this "
              "structure's own unused divisional sub-elements and could be assigned - owed"),
    Edge(unstemmed("caudal auditory belt"), here(DL, "caudal principal sulcus"),
         note="directly. Unchecked at the source; the same producer is stemmed at the "
              "frontal eye fields, where it was read"),

    Edge(here(DL), far("lateral intraparietal area", S_PARIETAL_DORSAL),
         note="the consumer names area 46"),
    Edge(here(DL), far("anterior intraparietal area", S_POSTERIOR_PARIETAL),
         note="the consumer declares an input from prefrontal areas 46 and 12"),
    Edge(here(DL), class_endpoint("sensory cortex"),
         carries="top-down bias",
         note="the remainder after the two parietal members are split out. CLOSED AS A "
              "NEGATIVE against 05_sensorimotor_loop - neither somatosensory entry admits "
              "a frontal source of any kind - which closes one file, not the class. The "
              "visual and auditory members remain unchecked"),
    Edge(here(DL), here(FEF)),
    Edge(here(DL), here(PM),
         note="the source names the ventrolateral prefrontal cortex alongside it and that "
              "structure declares no such output; the other half is an inherited gap"),
    Edge(here(DL), far("basal ganglia", S_BASAL_GANGLIA, "associative striatum"),
         note="the consumer declares its cortical source as a class; the same sector caveat "
              "applies as at premotor cortex"),
    Edge(here(DL), here(ACC)),

    # ---- 6. ventrolateral prefrontal cortex: 7 in, 5 out ----
    Edge(far("temporal pole", S_TEMPORAL_POLE), here(VL),
         carries="the amodal concept, for controlled retrieval and selection",
         note="two-ended, confirmed; the producer types it where this end does not, and "
              "records this end as declaring the edge and typing nothing"),
    Edge(far("inferotemporal cortex", S_VISUAL), here(VL),
         carries="identity, for controlled retrieval and selection",
         note="two-ended, confirmed directly at the producer; the producer types the "
              "payload where this end does not"),
    Edge(far("mediodorsal nucleus", S_THALAMUS), here(VL),
         carries="no categorical content; modulatory amplification, raising the gain of "
                 "this structure's local recurrent connectivity",
         role=MODULATORY, representation=MEDIODORSAL_AMPLIFICATION),
    Edge(unstemmed("anterior auditory belt"), here(VL, "Brodmann area 47"),
         note="directly, onto areas 12 and 45 - area 12 resolved to Brodmann area 47 by "
              "this file's own alias. The auditory what stream reaching prefrontal cortex "
              "without waiting for the temporal endpoints. Unchecked at the source"),
    Edge(far("amygdala", S_MEDIAL_TEMPORAL,
             "intermediate and magnocellular divisions of the basal nucleus"),
         here(VL, "Brodmann area 47"),
         carries="the valence tag; payload otherwise owed",
         role=MODULATORY, representation=VALENCE_TAG,
         note="two-ended, and the DENSEST of the producer's four lateral edges: "
              "terminations across area 12 in deep layer I, layer II and layer VI, "
              "continuing dorsally into much of Brodmann area 45; ipsilateral only. A "
              "second independent external demand on the same unmade division"),
    Edge(far("supramarginal gyrus", S_POSTERIOR_PARIETAL), here(VL)),
    Edge(far("angular gyrus", S_POSTERIOR_PARIETAL), here(VL)),

    Edge(here(VL), here(BRO),
         note="the two structures share Brodmann area 45, so this edge crosses a boundary "
              "whose location is not agreed - see CONTESTED_SUBELEMENTS"),
    Edge(here(VL), class_endpoint("temporal cortex"),
         carries="retrieval bias",
         note="resolves nowhere: the temporal pole does not declare an input from this "
              "structure, and the auditory and visual files were not read at the source"),
    Edge(here(VL), far("basal ganglia", S_BASAL_GANGLIA),
         note="the one of this file's four striatal producers that names NO sector, where "
              "premotor, dorsolateral and orbitofrontal each name one. Owed here: name the "
              "sector, or establish that this projection is not sectored"),
    Edge(here(VL), far("supramarginal gyrus", S_POSTERIOR_PARIETAL),
         note="reciprocal, via the arcuate fasciculus and superior longitudinal "
              "fasciculus III"),
    Edge(here(VL, "Brodmann area 47"),
         far("anterior intraparietal area", S_POSTERIOR_PARIETAL),
         note="from area 12, resolved to Brodmann area 47 by this file's own alias"),

    # ---- 7. orbitofrontal / ventromedial prefrontal cortex: 10 in, 10 out ----
    Edge(far("hippocampal formation", S_MEDIAL_TEMPORAL,
             "subiculum, with prosubiculum and distal CA1"), here(OFC),
         carries="the completed episode; payload otherwise owed at both ends",
         note="via the FORNIX AND BY NO OTHER ROUTE, so the tract is a condition on the "
              "edge and not a description of it. Terminating principally in layer III of "
              "Brodmann areas 11, 13, 14 and 25; ipsilateral only. Two-ended, and the "
              "first edge in the file with a claim on this structure's named-but-unused "
              "sub-elements - the assignment arrives WITH the edge"),
    Edge(far("amygdala", S_MEDIAL_TEMPORAL, "basal and accessory basal nuclei"), here(OFC),
         note="orbital"),
    Edge(unstemmed("gustatory pathway and olfactory cortex"), here(OFC),
         note="orbital. COMPOUND ENDPOINT: two modalities are not one source, and "
              "splitting the line is owed. Unchecked at the source"),
    Edge(far("inferotemporal and temporal cortex", S_VISUAL), here(OFC),
         note="orbital. COMPOUND ENDPOINT, and consumer-only: checked, and the producer "
              "declares one prefrontal output only - to the ventrolateral structure, which "
              "is a separate entry here. Owed at the source: declare it, or withdraw it"),
    Edge(far("basal ganglia", S_BASAL_GANGLIA,
             "ventral pallidum, via the mediodorsal thalamus"), here(OFC),
         note="THREE-FILE CONTRADICTION and this entry is one of the three ends. This line "
              "believes the limb leaves the ventral pallidum; 12_thalamus declares the "
              "mediodorsal basal-ganglia input from the internal globus pallidus and "
              "substantia nigra pars reticulata; 09_basal_ganglia cannot say which, the "
              "ventral pallidum being an entry there while the dorsal nuclei are "
              "sub-elements of a different entry. The payloads differ and that is what "
              "puts it on the wire: tonic inhibition alone from the dorsal nuclei, "
              "inhibition PLUS a computed relative value from the ventral pallidum"),
    Edge(far("mediodorsal nucleus", S_THALAMUS), here(OFC),
         carries="no categorical content; modulatory amplification, raising the gain of "
                 "this structure's local recurrent connectivity",
         role=MODULATORY, representation=MEDIODORSAL_AMPLIFICATION),
    Edge(far("posterior cingulate cortex", S_INSULA), here(OFC),
         note="medial. Two-ended and confirmed; the producer names it the medial-prefrontal "
              "default-mode partner, which is the medial half of this structure and not the "
              "orbital half - so the far end is already treating this structure as two. "
              "Payload owed at both ends"),
    Edge(far("precuneus", S_POSTERIOR_PARIETAL), here(OFC),
         note="medial. Two-ended and confirmed"),
    Edge(far("angular gyrus", S_POSTERIOR_PARIETAL), here(OFC),
         note="medial. NOT two-ended by name: the producer's Outputs name the ventrolateral "
              "prefrontal cortex, and the only line that could carry this edge is its "
              "four-member default-mode partners class, which it marks unresolved. A "
              "located candidate for that class rather than a declared edge"),
    Edge(far("insula", S_INSULA), here(OFC),
         carries="the salience signal and the interoceptive state; payload otherwise owed",
         note="reciprocal. Two-ended and confirmed; the producer declares this structure by "
              "name and types the interoceptive state as the reciprocal limb"),

    Edge(here(OFC), far("amygdala", S_MEDIAL_TEMPORAL)),
    Edge(here(OFC), far("bed nucleus of the stria terminalis", S_MEDIAL_TEMPORAL)),
    Edge(here(OFC), far("hypothalamus", S_BRAINSTEM),
         note="PRODUCER-ONLY, checked: that entry's Inputs declare no prefrontal or "
              "orbitofrontal source under any name. Owed at the source - accept it there, "
              "or withdraw it here"),
    Edge(here(OFC), far("ventral striatum", S_BASAL_GANGLIA),
         note="two-ended and confirmed, and this end is the untyped one. The far end writes "
              "the edge as its own line rather than inside its cortical class, precisely "
              "because this producer names the ventral sector, and types the payload as "
              "value - the expected value of the options. Owed here: type it, or take the "
              "producer's wording"),
    Edge(here(OFC), far("ventral pallidum", S_BASAL_GANGLIA),
         note="two-ended and confirmed. The consumer's line also names infralimbic cortex, "
              "which is Brodmann area 25 and therefore a sub-element of this structure that "
              "the heading names and no edge uses - both ends record the same sub-element "
              "debt from opposite sides. Payload owed here; the far end types it as value"),
    Edge(here(OFC), far("temporal pole", S_TEMPORAL_POLE),
         carries="value; payload owed at both ends beyond that",
         note="two-ended, confirmed"),
    Edge(here(OFC), far("insula", S_INSULA),
         note="two-ended and confirmed; payload owed at both ends, which the producer's "
              "line marks in the same words"),
    Edge(here(OFC), here(RIF)),
    Edge(here(OFC), unstemmed("periaqueductal gray")),
    Edge(here(OFC), class_endpoint("autonomic centres"),
         note="the remainder after the periaqueductal gray is split out, and it resolves "
              "nowhere. Owed at the source: name them"),

    # ---- 8. anterior cingulate cortex: 6 in, 4 out ----
    Edge(far("insula", S_INSULA), here(ACC),
         carries="the salience signal: this event is behaviourally relevant now",
         note="two-ended and confirmed, the producer marking it salience -> control and "
              "this end being the untyped one. WHETHER WHAT LEAVES IS A SCALAR, A POINTER "
              "OR A SWITCHING COMMAND IS NOT ESTABLISHED at the producer, and that "
              "non-establishment is stated there rather than glossed"),
    Edge(far("hippocampal formation", S_MEDIAL_TEMPORAL, "subiculum"), here(ACC),
         carries="the completed episode; payload otherwise owed at both ends",
         note="via the fornix. Terminating in layer III of Brodmann area 24a ONLY; "
              "ipsilateral only. Two-ended. The sub-element restriction is finer than this "
              "structure's own headings and it CANNOT CURRENTLY BE RECEIVED: the divisional "
              "sub-elements are areas 24 and 32 undivided. Owed: divide area 24, or record "
              "that this edge carries a claim the structure cannot yet receive"),
    Edge(far("amygdala", S_MEDIAL_TEMPORAL), here(ACC)),
    Edge(far("midline / intralaminar thalamus", S_THALAMUS), here(ACC),
         note="the producer declares this structure on its own line, the diffuse cortical "
              "class beside it being explicitly the residue of the line the named edge came "
              "out of. Payload owed at both ends. A SECOND thalamic edge reaches this "
              "structure and is not declared here - the anterior nuclei, the cingulate half "
              "of the classical Papez target, declared at one end only. This line names one "
              "thalamic source and there are two"),
    Edge(far("midcingulate cortex", S_INSULA, "via the cingulum"), here(ACC),
         note="reciprocal; two-ended and confirmed; payload owed at both ends, and the "
              "producer names the same route. The only relationship in this entry complete "
              "at both ends in both directions"),

    Edge(here(ACC), here(DL), carries="recruiting control"),
    Edge(here(ACC), far("midcingulate cortex", S_INSULA),
         carries="a scalar reward-value signal: expected reward magnitude, and a response "
                 "to the mismatch between expected and received reward, firing to "
                 "unexpected reward and to expected-but-omitted reward",
         representation=REWARD_VALUE,
         note="two-ended and confirmed. The consumer carries this payload verbatim and "
              "records it as the only edge in that section with a stated coordinate frame - "
              "so the two ends are copies and their agreement certifies transmission, not "
              "corroboration"),
    Edge(here(ACC), here(PM)),
    Edge(here(ACC), class_endpoint("autonomic centres"),
         note="the far side of these centres - the visceral effectors they drive - is "
              "outside the map's scope, so this edge terminates at the SCOPE BOUNDARY on "
              "its output side. It is nonetheless a class endpoint on THIS side of the "
              "boundary: the brainstem autonomic nuclei that would receive it have entries "
              "and none was checked"),

    # ---- 9. frontopolar cortex: 4 in, 1 out ----
    Edge(class_endpoint("other association / prefrontal cortex"), here(FP, "lateral"),
         note="supramodal. Unresolved: NONE of the four other prefrontal structures in this "
              "file declares an output here. Owed at the source as cross-file edits within "
              "file 11, or withdraw"),
    Edge(unstemmed("auditory association cortex - the anterior belt, the parabelt, the "
                   "rostral superior temporal gyrus and the temporal pole"),
         here(FP, "medial / midline"),
         note="directly and densely. COMPOUND ENDPOINT naming four sources across two "
              "files. The belt and parabelt limbs are confirmed - 02_auditory_pathway's "
              "belt entry declares the frontal pole among its direct prefrontal targets by "
              "name - while the temporal-pole limb is declared here and at no producer, "
              "re-checked against 07_anterior_temporal_lobe"),
    Edge(class_endpoint("other sensory modalities - parietal, inferior temporal and "
                        "occipital cortex"), here(FP),
         note="present but of lower density. A THREEFOLD class: each term names a lobe "
              "rather than a structure. The parietal limb was checked and no structure in "
              "file 4 or file 6 declares an output here"),
    Edge(far("mediodorsal nucleus", S_THALAMUS), here(FP),
         carries="no categorical content; modulatory amplification, raising the gain of "
                 "this structure's local recurrent connectivity",
         role=MODULATORY, representation=MEDIODORSAL_AMPLIFICATION),

    Edge(here(FP), class_endpoint("other frontal / prefrontal cortex"),
         note="from the structure as a whole; whether the signal leaves from one part is "
              "not stated. Unresolved: NONE of the four other prefrontal structures in this "
              "file declares an input from here"),
)

# Edges checked and found not to exist.  A checked absence is carried so the check is
# not repeated, and it is not an edge: neither is counted in the 106.
NEGATIVE_EDGES = (
    (PM, "middle temporal area",
     "the consumer declares its frontal input from the frontal eye fields instead"),
    ("insula", DL,
     "17_insula_claustrum_habenula left open whether its split-out cortical output class "
     "had covered this structure; this structure's Inputs declare no insular source of any "
     "kind, so either the class never covered it or the consumer does not carry it. A "
     "recorded negative, not an absence of evidence"),
)

# Edges a far end declares that no structure here declares.  Recorded, and NOT written
# as edges: writing an edge on the far end's declaration alone would assert a
# projection this file has read nothing for.
FAR_END_ONLY = (
    (ACC, "insula", S_INSULA, "the return arm of a relationship the far end calls "
                              "reciprocal, unconfirmed at its producer"),
    (ACC, "lateral habenula", S_INSULA, "typed there a bad-outcome expectation, one of "
                                        "three cortical limbs of the value brake"),
    (ACC, "posterior cingulate cortex", S_INSULA, "payload owed at the far end"),
    (OFC, "lateral habenula", S_INSULA, "onto the lateral habenula from the ventromedial "
                                        "half, typed a bad-outcome expectation"),
    (FEF, "V4", S_VISUAL, "V4 declares an input from the frontal eye field terminating in "
                          "all cortical layers - the same lamination and phrasing as the "
                          "middle temporal output that IS two-ended. Adding an edge and "
                          "re-terminating one are NOT equivalent for V4's fan-in"),
)

# Whole-file absences.  Each is one finding rather than several, and neither is
# repairable at this rung.
WHOLE_FILE_ABSENCES = (
    "no structure in this file declares an output to any THALAMIC nucleus, while seven "
    "declare a thalamic input. 12_thalamus declares the return traffic as two class "
    "endpoints - a layer-6 reciprocal modulator and a layer-5 driver - and the layer-5 "
    "driver is what makes that nucleus a higher-order, cortically-driven relay rather than "
    "a first-order sensory one. The drive originates here and is declared nowhere here",
    "no structure in this file declares an output to any NEUROMODULATORY nucleus, covering "
    "four of that file's endpoints at once. This file receives four brain-wide modulatory "
    "projections and declares one of them, and sends four ascending control limbs and "
    "declares none",
)

# --------------------------------------------------------------------------
# Forward operation.
#
# The whole of what the rungs above specify, and faithful to the sizing model:
# equal weights, so the stored value is a threshold, and the cell fires when the
# count of active inputs reaches it.
# --------------------------------------------------------------------------


def threshold_gate(active_counts, thresholds):
    """Fire where the count of active inputs reaches the stored threshold.

    Integer comparison only.  No weights and no multiply, because equal weights
    reduce the dot product to a count; no gradient, because nothing here is
    differentiated.
    """
    if len(active_counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(active_counts, thresholds)]


def fan_in_map(structure: Structure, subelement: str | None = None):
    """Which source lines converge on each neuron.

    Not implementable here, and for a sharper reason than a missing authorisation.
    Elsewhere a topography is described in prose and formalising it would mean
    writing a geometry without agreement.  Here THERE IS NO DESCRIBED GEOMETRY TO
    FORMALISE: whether premotor cortex is somatotopic is not established, whether the
    saccade area's motor map is a compartmentation an edge could terminate on is not
    established, and whether the orbitofrontal body-relative value axis is a spatial
    organisation or a population code is not established.  The one boundary with a
    quantitative basis, frontopolar's medial/lateral divide, partitions afferents
    rather than supplying coordinates.

    So this needs the measurement first and the agreement second.  Both are the
    inter-structure connection topology and neither is this rung's to choose.
    """
    raise NotImplementedError(
        "connection topology is not set, and in this section it is not described "
        "either: no structure here has a recorded map, so there is no stated geometry "
        "to formalise"
    )


def allocate(structure: Structure, subelement: str):
    """Size the threshold and activity arrays for one divisional sub-element.

    Blocked twice, and the second block is not a missing number.

    First, the granularity mismatch: sizing is stated per structure, edges terminate
    on sub-elements, and no partition connects them - here with nothing to partition,
    every structure's neuron count being unstated.

    Second, at Brodmann area 45, two structures claim the same neurons.  A missing
    partition leaves an array unsized; an unresolved overlap makes two arrays wrong
    together in a way that sums cleanly and looks right.
    """
    canonical = SUBELEMENT_ALIASES.get((structure.name, subelement), subelement)
    if canonical not in structure.subelements:
        raise ValueError(f"{subelement!r} is not a sub-element of {structure.name}")

    for area, owner_a, owner_b, proposal in CONTESTED_SUBELEMENTS:
        if canonical.startswith(area) and structure.name in (owner_a, owner_b):
            raise NotImplementedError(
                f"{area!r} is claimed by both {owner_a!r} and {owner_b!r}; {proposal}. "
                f"Allocating either structure double-counts the shared area, and no "
                f"neuron count exists to partition in the first place"
            )

    if (structure.name, canonical) in PROVISIONAL_SUBELEMENTS:
        raise NotImplementedError(
            f"{canonical!r} is provisional: "
            f"{PROVISIONAL_SUBELEMENTS[(structure.name, canonical)]}. Allocating it as a "
            f"peer would double-count; folding it in would discard a distinction two far "
            f"ends are using"
        )

    raise NotImplementedError(
        f"{structure.name} carries no neuron count at all, across "
        f"{len(structure.subelements)} sub-elements, so there is nothing to partition and "
        f"the array for {canonical!r} cannot be sized. Tile geometry and sparsity are also "
        f"unset and both must be surfaced before they are chosen"
    )


def step(*args, **kwargs):
    """There is no step, and this is the point rather than an omission.

    Every edge in this section has a nonzero, finite, heterogeneous latency in real
    time, and there is no global clock in the described system to replace them with.
    A loop with real heterogeneous delays settles by its own dynamics; the same loop
    broken by registers becomes an iterated map whose trajectory depends on the
    update rate.  Two different systems computing two different things.

    Setting every latency equal and choosing an interval short enough to carry the
    finest one is a legitimate thing this rung may eventually do - but the finest one
    is not known here and is not this section's to know.  Every structure here sits
    on loops that leave the frontal lobe and return, so the interval would be set by
    the fastest loop in the map, which lies in sections this module does not hold.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; every "
        "edge latency in this section reads to derive, and the interval a uniform delay "
        "would take is set by the fastest loop in the map, not by any loop here"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    A threshold that is never written is a construction cost rather than a memory,
    which is why this module is still coherent without it: thresholds are read-only
    and the section runs open-loop.
    """
    raise NotImplementedError("no learning rule is set")


# --------------------------------------------------------------------------
# Derived reporting.  Every figure below is recomputed from the declarations in
# this file rather than transcribed from the rung above.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    return config_sizing_report(
        STRUCTURES, "sizing - recomputed from counts and fan-ins, not transcribed")


def prefrontal_ceiling() -> str:
    """The one closed quantity: a sum over structures, never a per-structure figure."""
    out = ["granular frontal cortex anterior to the corpus callosum: "
           f"{PREFRONTAL_NEURON_BUDGET:,} neurons per hemisphere",
           "  the fraction is constant across primates, not human-expanded"]
    for bits, fan_in in ((12, 4_096), (13, 8_192), (14, 16_384), (16, 65_536)):
        gb = PREFRONTAL_NEURON_BUDGET * bits / 8 / 1e9
        out.append(f"  at {bits:>2} bits (fan-in ~{fan_in:>6,}): {gb:.3f} GB per hemisphere")
    lo = PREFRONTAL_NEURON_BUDGET * 12 / 8
    hi = PREFRONTAL_NEURON_BUDGET * FAN_IN_CEILING_BITS / 8
    out.append(f"  spread across the whole plausible fan-in range: {hi/lo:.3f}x")
    out.append("  this is a SUM over structures. It is never entered against any one of")
    out.append("  them, and the per-area partition is what every Sizing field waits on.")
    out.append("  the only partition constraint the file supplies is an ORDERING: the")
    out.append("  frontopolar share exceeds every other prefrontal structure's.")
    return "\n".join(out)


def edge_count_check() -> str:
    """Rebuild the architecture's declaration counts from this file's edges.

    Two records of one quantity exist one rung up - a count stated per entry, and a
    total stated in the header - and where they disagree the disagreement is
    arithmetic and can be shown rather than asserted.

    An edge is one object here and a declaration is one bullet there, so the two are
    not the same unit: an in-file edge written at both ends is two declarations and
    one edge.  The mapping is exact and is reconstructed rather than assumed.
    """
    names = {s.name for s in STRUCTURES}
    per = {n: [0, 0] for n in names}
    for e in EDGES:
        pair = (e.source.name, e.target.name)
        if e.target.kind == LOCAL and e.target.name in names and pair not in CONSUMER_SILENT:
            per[e.target.name][0] += 1
        if e.source.kind == LOCAL and e.source.name in names and pair not in PRODUCER_SILENT:
            per[e.source.name][1] += 1
    out = [f"{'structure':50} {'in':>4} {'out':>4} {'decl':>6}"]
    tin = tout = 0
    for s in STRUCTURES:
        i, o = per[s.name]
        tin += i
        tout += o
        out.append(f"{s.name:50} {i:>4} {o:>4} {i + o:>6}")
    ai, ao = ARCHITECTURE_DECLARATIONS
    agree = (tin, tout) == (ai, ao)
    out.append("")
    out.append(f"{'declarations rebuilt':50} {tin:>4} {tout:>4} {tin + tout:>6}")
    out.append(f"{'architecture header states':50} {ai:>4} {ao:>4} {ai + ao:>6}"
               f"   -> {'AGREES' if agree else 'DISAGREES'}")
    in_file = [e for e in EDGES if e.source.kind == LOCAL and e.target.kind == LOCAL]
    both = [e for e in in_file
            if (e.source.name, e.target.name) not in PRODUCER_SILENT
            and (e.source.name, e.target.name) not in CONSUMER_SILENT]
    out.append(f"  edges held here: {len(EDGES)}; in-file: {len(in_file)}, of which "
               f"{len(both)} are declared at both ends")
    out.append(f"  {len(EDGES)} + {len(both)} = {len(EDGES) + len(both)} declarations")
    out.append("")
    out.append("the per-entry Sizing and Edge latency counts, against the entries' own")
    out.append("Inputs lists. Five disagree, and the five short edges are the five limbs")
    out.append("from 08_medial_temporal_lobe - three amygdalar, two hippocampal:")
    stated = ((PREMOTOR.name, 12, 18), (DORSOLATERAL.name, 7, 14),
              (VENTROLATERAL.name, 6, 11), (ORBITOFRONTAL.name, 9, 19),
              (ANTERIOR_CINGULATE.name, 5, 9))
    short = 0
    for name, si, se in stated:
        i, o = per[name]
        short += i - si
        out.append(f"  {name[:44]:44} stated {si:>3} in / {se:>3} edges;  "
                   f"declared {i:>3} in / {i + o:>3} edges")
    total = ai + ao
    out.append(f"  total shortfall: {short} edges;  {total} - {short} = {total - short}, "
               f"which is the file-level")
    out.append("  edge-count line and the fan-in / fan-out line, both derived from these.")
    return "\n".join(out)


def edge_resolution_report() -> str:
    """Every edge must resolve to something, or it points at nowhere.

    The dangling-edge diff is the only check that finds a missing stage, because a
    missing stage leaves no hole where it should be - it leaves a pointer to nowhere
    somewhere else.  Two edges are excluded from the unresolved count by rule and not
    by convenience: the corticospinal projection terminates at the scope boundary on
    the body side, and the autonomic-centres output terminates at it on the far side.
    """
    names = {s.name for s in STRUCTURES}
    in_file = cross = klass = unread = unresolved = 0
    hits = []
    for e in EDGES:
        if e.source.kind == LOCAL and e.target.kind == LOCAL:
            in_file += 1
        elif CLASS_ENDPOINT in (e.source.kind, e.target.kind):
            klass += 1
        elif e.crosses_file:
            cross += 1
        elif UNSTEMMED in (e.source.kind, e.target.kind):
            unread += 1
        elif NO_ENTRY in (e.source.kind, e.target.kind):
            pass
        else:
            unresolved += 1
            hits.append(f"    {e.source.name} -> {e.target.name}")
    stems = sorted({e.source.stem or e.target.stem for e in EDGES if e.crosses_file})
    out = [f"edge declarations                      {len(EDGES)}",
           f"  both ends in this file               {in_file}",
           f"  far end stemmed to a named file      {cross}",
           f"  far end named, file not yet opened   {unread}   (no stem; a reading not "
           f"yet done, not a gap in the map)",
           f"  endpoint is a class                  {klass}   (no unit to "
           f"co-instantiate; splitting is a source decision)",
           f"  UNRESOLVED - a pointer at nowhere    {unresolved}"]
    out.extend(hits)
    out.append(f"far files reached by stem: {len(stems)}")
    for s in stems:
        n = sum(1 for e in EDGES if s in (e.source.stem, e.target.stem))
        out.append(f"    {s:38} {n:>3}")
    # An edge with both ends in this file should be declared once at each end.
    counted = {}
    for e in EDGES:
        if e.source.kind == LOCAL and e.target.kind == LOCAL:
            counted[(e.source.name, e.target.name)] = \
                counted.get((e.source.name, e.target.name), 0) + 1
    one_ended = []
    for (a, b) in counted:
        if (b, a) not in counted:
            one_ended.append(f"    {a} -> {b}")
    out.append("")
    out.append(f"in-file edges with no return declaration: {len(one_ended)}")
    out.extend(sorted(one_ended))
    out.append("  a one-way in-file edge is not necessarily a defect - most of these are")
    out.append("  genuinely one-way - but the producer-side gaps this file inherits show")
    out.append("  up here as a number rather than as prose.")
    out.append("")
    out.append(f"recorded negatives (checked absences, not edges): {len(NEGATIVE_EDGES)}")
    for a, b, why in NEGATIVE_EDGES:
        out.append(f"    {a} -x-> {b}")
    out.append(f"far-end-only edges (declared there, not written here): {len(FAR_END_ONLY)}")
    for a, b, stem, why in FAR_END_ONLY:
        out.append(f"    {a} -> {b}   [{stem}]")
    out.append("")
    for a in WHOLE_FILE_ABSENCES:
        out.append("WHOLE-FILE ABSENCE: " + a.split(".")[0])
    return "\n".join(out)


def latency_report() -> str:
    timed = [e for e in EDGES if e.latency_s is not None]
    return (f"edges: {len(EDGES)}    with a stated latency: {len(timed)}    "
            f"to derive: {len(EDGES) - len(timed)}\n"
            "  the absence is total rather than partial: no conduction time, no synaptic\n"
            "  delay, no loop latency, and no myelination figure at any of the nine\n"
            "  structures to derive one from.")


def shape_report() -> str:
    """Rank-3 sheets, one per divisional sub-element; every tangential extent open."""
    out = [f"{'structure':50} {'sub-elements':>13} {'laminar extent':>16}"]
    subs = settled = 0
    for s in STRUCTURES:
        subs += len(s.subelements)
        per_sub = [LAMINAE.get((s.name, e), LAMINAE.get((s.name, "*")))
                   for e in s.subelements]
        n = sum(1 for v in per_sub if isinstance(v, tuple))
        settled += n
        shown = {len(v) if isinstance(v, tuple) else "open" for v in per_sub}
        out.append(f"{s.name:50} {len(s.subelements):>13} "
                   f"{'/'.join(str(x) for x in sorted(shown, key=str)):>16}")
    out.append("")
    out.append(f"divisional sub-elements declared: {subs}; "
               f"laminar extent settled at {settled} of {subs}")
    out.append(f"provisional rather than settled: {len(PROVISIONAL_SUBELEMENTS)} "
               f"(+{len(CELL_CLASS_SUBELEMENTS)} cell class, which is not a sheet axis)")
    out.append("every tangential extent (H, W) reads 'to derive': no tile pitch is measured")
    out.append("anywhere in this file, in millimetres or micrometres. One measurement per")
    out.append("structure would convert the whole Shape from open to computed.")
    out.append("")
    out.append("two structures cannot be allocated at all until an assignment is adopted:")
    for area, a, b, proposal in CONTESTED_SUBELEMENTS:
        out.append(f"  {area}: claimed by {a} and by {b}")
        out.append(f"    {proposal}")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report())
    print()
    print(prefrontal_ceiling())
    print()
    print(shape_report())
    print()
    print(latency_report())
    print()
    print(edge_count_check())
    print()
    print(edge_resolution_report())
    print()
    print(representation_report(EDGES))
    print()
    for fn, label in ((step, "scheduler"), (learn, "learning")):
        try:
            fn()
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
    for fn, args, label in ((fan_in_map, (DORSOLATERAL,), "connectivity"),
                            (allocate, (PREMOTOR, "F5 - ventral premotor"), "allocation"),
                            (allocate, (BROCA, "Brodmann area 45 - pars triangularis"),
                             "overlap"),
                            (allocate, (DORSOLATERAL, "caudal principal sulcus"),
                             "provisional")):
        try:
            fn(*args)
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
