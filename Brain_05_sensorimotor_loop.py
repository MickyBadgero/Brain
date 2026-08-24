"""Brain — 05 sensorimotor loop: the section where the loop leaves the brain.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

Primary motor cortex drives muscles; the muscles, the skeleton and their dynamics have
no entry anywhere; and the return path runs through the world -- the movement's
consequence read back through proprioception.  The loop closes through the body, not
inside the brain.

That is this section's largest fact and it has three exact consequences here.  The
corticospinal output edge has a payload and no consumer, so its endpoint names a
structure with no entry in any file.  The return line has a payload and no producer.
And the loop cannot be closed by any amount of work at this rung -- so a design that
closed it by feeding the motor command back as its own consequence, which is the
obvious thing to reach for, would have built a system with no body and no world, and it
would run.  Nothing below does that; the two ends are declared open and left open.

This is also the first sensory section in the map with no transducer entry.  The
mechanoreceptors and proprioceptors are this pathway's transducers and they arrive from
a body that has no entry, so the transducer is outside the map at the input end and the
effector is outside it at the output end.  Every population below is a threshold gate
or an inhibitory interneuron modelled as one.

Counting basis is per hemisphere throughout, and one structure is unpriced.  Five of
six rows carry a count.  Recomputed: 138M neurons and 276.00 MB at the 16-bit ceiling,
with the four somatosensory areas summing to 80M and 160.00 MB.  The realisation gap is
zero because every width is the ceiling: no fan-in in this section is known, so nothing
is derived below the cap.  A zero gap and an unmeasured fan-in are the same fact stated
twice.

The first partition in the map is here.  Primary somatosensory cortex is given no total
-- it is given four counts, one per cytoarchitectonic area, and the total is what has to
be derived.  So allocation closes at the sub-element level for the first time, for four
sub-elements.  It buys exactly that and no more: every fan-in in the section is
underived, so the one structure that can be allocated still cannot have its edges sized.
Allocation and connection are separate closures, and this section closes the first for
one structure and the second for none.

Every edge latency reads None, and no time constant and no ordering constraint is stated
anywhere in this section -- the first section since chunk 01 of which that is true.  What
this section constrains instead is the graph, and it constrains it in an unusual
direction: whether the four somatosensory areas are serial or parallel is contested by
two methods that are not measuring the same thing, and the architecture keeps both edge
sets rather than choosing.  So the edge set below is knowingly larger than the anatomy
may be.  Every other open state in this project makes the code smaller than the biology;
this one makes it larger, and nothing is pruned.

Two arithmetic cautions are honoured here rather than restated.  The 87% figure at the
dorsal column nuclei counts cells responding to two or more nerve territories, not
contacts per neuron, so `fan_in` there reads None and not 2 and not 276.  The ~10%
nociceptive figure at the thalamus is carried forward unverified, so there is no
`nociceptive_fraction` parameter anywhere below.  Both would slot into a parameter table
without looking wrong, which is why they are named.

No global clock may be assumed, and no latency here is stated in steps.
"""

from __future__ import annotations

from Brain_config import (
    CONTESTED, EVENT_DRIVEN, Edge, MODULATORY, NOT_APPLICABLE, NO_FRAME, OWED,
    PER_HEMISPHERE, Population, Representation, Structure, THRESHOLD_GATE, TO_DERIVE,
    UNKNOWN, allocate, class_endpoint, edge_report, emission, fan_in_map, far, here,
    learn, no_entry, representation_report, schedule, sizing_report, unstemmed,
)

STEM = "05_sensorimotor_loop"

# Far files reached from this section.  The stem, never the number: the number fixes
# data-flow position and the section names the structure, and a bare number goes
# silently wrong the moment a file is split, merged or renumbered.
#
# Every other named far end below carries no stem, which means the reading has not been
# done -- not that no far end exists.
PARIETAL = "06_posterior_parietal"
FRONTAL = "11_frontal_lobe"
INSULA = "17_insula_claustrum_habenula"
DORSAL_VISUAL = "04_dorsal_visual_parietal_stream"

# Coordinate frames used more than once.  The skin and the body are different frames and
# the distinction is load-bearing: the cutaneous payload is about where on the skin, the
# proprioceptive payload is about the body's configuration and not the world's.
SOMATOTOPIC = "somatotopic -- the skin surface"
BODY_CONFIG = "the body's configuration, not the world's"
SKIN_JOINT = "skin / joint"

# The fan-in bound.  No fan-in in this section is known, at any structure, so every
# population sits here and nothing is derived below it.
FAN_IN_UNDERIVED = None

# --------------------------------------------------------------------------
# The laminar block and its scope.
#
# The architecture assigns the scope statement to this rung.  It is stated here as a
# scope and not as arithmetic: naming which entries may carry a Class-3 laminar claim is
# not the same as deriving an update equation from it, and no entry below writes one.
#
# The block is laminae 1, 2, 3, 4, 5a, 5b, 6a, 6b with 4 -> 2/3, 2/3 -> 5a and 5b,
# 6a -> 4, 6a -> 5a, 6b -> 6a, and within-sub-element recurrence.  It is Class 3
# throughout -- the general cortical pattern, not a measurement made at any entry that
# carries it.
#
# Its scope is granular isocortex and nothing else.  Three of its six edges route
# through layer 4, so an entry whose own Function denies layer 4 cannot take the block
# without asserting a circuit that entry denies.  Nine entries across five files cannot
# take it and they fail in four different ways -- uniformly agranular, agranular across
# a gradient, agranular across an internal border, and not isocortex at all -- so a
# single exception clause would not cover them.
#
# In this file the block applies to primary somatosensory cortex, the second
# somatosensory area and superior parietal area 5, and is withheld at primary motor
# cortex, whose laminae are seven and not eight.  The dorsal column nuclei and the
# ventral posterior thalamus are not cortex and the question does not arise.
# --------------------------------------------------------------------------

GRANULAR_LAMINAE = ("1", "2", "3", "4", "5a", "5b", "6a", "6b")
AGRANULAR_LAMINAE = ("1", "2", "3", "5a", "5b", "6a", "6b")

# --------------------------------------------------------------------------
# Structures.
# --------------------------------------------------------------------------

DORSAL_COLUMN_NUCLEI = Structure(
    # A bundle: three nuclei plus a trigeminal relay in one slot set.  The split is owed
    # at the source, and the shape names three axes where the bundle names four things --
    # where the trigeminal relay sits in (nucleus, territory, position) is not stated and
    # is not guessed here.
    "dorsal column nuclei and trigeminal relay",
    (
        Population("relay and projection neurons", THRESHOLD_GATE, PER_HEMISPHERE,
                   500_000, FAN_IN_UNDERIVED,
                   note="soft, no clean human count, and no separate count for the "
                        "external cuneate nucleus -- the sub-element the cerebellar "
                        "edge leaves from, so the one edge in this entry whose source "
                        "is a named sub-element cannot be sized"),
    ),
    subelements=("gracile nucleus", "cuneate nucleus", "external cuneate nucleus",
                 "cluster region", "reticular region"),
    rank=3,
    axes=("nucleus", "territory", "somatotopic position"),
    partitions=False,
)
# The somatotopic axis means different things in the two territories, and that is the
# entry's central structural fact rather than a detail.  The cluster region -- the middle
# third, pars rotunda in the primate cuneate -- holds tightly packed cells in
# cytochrome-oxidase-dense patches separated by cell-poor septa, receiving afferents from
# glabrous skin of the digits and pads, punctate and high-acuity, one body part per
# cluster.  The reticular region rostral and caudal to it holds small and large multipolar
# cells receiving diffuse terminations with intersegmental overlap rather than somatotopic
# lamination.
#
# So an index into this axis addresses one body part in one territory and a region of
# overlap in the other, and no rung above supplies the mapping for either.  An array
# indexed uniformly along it asserts a uniform meaning the structure does not have.
NUCLEUS_COUNT = 3
TERRITORY_COUNT = 2

# The convergence figure, recorded so that it is visibly not a fan-in.  In anaesthetised
# macaque, 87% of 317 recorded cuneate and external-cuneate cells responded to
# stimulation of two or more peripheral nerves -- 276 cells.  It counts cells responding
# to two or more nerve territories, not contacts per neuron, and the architecture says
# the two are different measurements.  `fan_in` above reads None.
CONVERGENCE_CELLS_RESPONDING = 276
CONVERGENCE_CELLS_RECORDED = 317

VENTRAL_POSTERIOR_THALAMUS = Structure(
    "ventral posterior thalamus",
    (
        Population("relay cells", THRESHOLD_GATE, PER_HEMISPHERE, 2_500_000,
                   FAN_IN_UNDERIVED,
                   note="soft -- the largest primary sensory relay, above the lateral "
                        "and medial geniculate nuclei at ~1.8-2.3M, about 1.2x the "
                        "geniculate midpoint, its body-surface and proprioceptive "
                        "afferent load exceeding the retina's or cochlea's. No separate "
                        "core-versus-matrix count was found."),
    ),
    subelements=("ventral posterior lateral nucleus", "ventral posterior medial nucleus",
                 "ventral posterior inferior nucleus", "basal ventral medial nucleus",
                 "parvalbumin core", "calbindin matrix"),
    rank=3,
    axes=("subnucleus", "compartment", "somatotopic position"),
    partitions=False,
)
# The compartment axis does not fit inside this structure, and that is a finding about
# the description's representation and not only about the thalamus.  The matrix runs
# uninterrupted from the ventral posterior medial and lateral nuclei into the ventral
# posterior inferior and basal ventral medial nuclei, and on into the anterior pulvinar
# and the posterior and ventral lateral nuclei.  Per-region edges cannot express a
# population that crosses region boundaries.
#
# Neither available allocation is honest: allocating the matrix here asserts a boundary
# the biology does not have, and allocating it separately in each region asserts several
# populations where there is one.  Neither is written.
SUBNUCLEUS_COUNT = 4    # on the scheme used; the parallel scheme does not have four
COMPARTMENT_COUNT = 2   # core and matrix, and no count for either

# The subnucleus scheme is itself contested.  The four-subnucleus scheme and a parallel
# literature's ventroposterior / ventroposterior superior / ventroposterior inferior
# scheme are not a relabelling of each other: they cut the proprioceptive relay out as a
# separate nucleus.  The edges carry the function either way, so no edge below depends on
# the choice -- but the arity does.
SUBNUCLEUS_SCHEME = CONTESTED

PRIMARY_SOMATOSENSORY = Structure(
    # The one structure in the map that can be allocated sub-element by sub-element.
    # It is given no total: four counts, one per cytoarchitectonic area, and the total
    # is what has to be derived.
    "primary somatosensory cortex",
    (
        Population("area 3a", THRESHOLD_GATE, PER_HEMISPHERE, 15_000_000,
                   FAN_IN_UNDERIVED,
                   note="proprioceptive core, at the border with primary motor cortex, "
                        "receiving group Ia muscle-spindle afferents"),
        Population("area 3b", THRESHOLD_GATE, PER_HEMISPHERE, 25_000_000,
                   FAN_IN_UNDERIVED,
                   note="cutaneous core, the true primary, with the finest somatotopic "
                        "map; divides further into digit modules"),
        Population("area 1", THRESHOLD_GATE, PER_HEMISPHERE, 20_000_000,
                   FAN_IN_UNDERIVED,
                   note="cutaneous secondary, texture and motion across the skin; "
                        "divides further into digit modules"),
        Population("area 2", THRESHOLD_GATE, PER_HEMISPHERE, 20_000_000,
                   FAN_IN_UNDERIVED,
                   note="cutaneous-and-deep tertiary, size, shape and stereognosis, "
                        "where cutaneous and deep inputs converge"),
    ),
    subelements=("area 3a", "area 3b", "area 1", "area 2"),
    rank=3,
    axes=("area", "lamina", "somatotopic position"),
    partitions=True,
)
# partitions=True for the first time in the map.  The count divides among the four areas
# because the four counts are what is stated; it does not divide among the eight laminae,
# so allocation closes one level down from the total and not two.
#
# The somatotopic axis is plastic, reorganising after input change, and an extent that
# moves with experience is not the same kind of extent as one that does not.  An
# underived extent is a number nobody has supplied; this is an extent with no single true
# value at any time, and a fixed-extent array asserts a stability the structure does not
# have.  What a re-organising axis is in code is not settled at any rung.
S1_SOMATOTOPIC_AXIS_IS_PLASTIC = True
DIGIT_MODULE_COUNT = None       # to derive, and only in areas 3b and 1
THALAMIC_SHARE_OF_LAYER1 = 0.32  # thalamic input is a minority of long-range input

SECOND_SOMATOSENSORY = Structure(
    # A bundle: three fields in one slot set.  The split is owed at the source.
    "second somatosensory area",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, None, FAN_IN_UNDERIVED,
                   note="unknown -- the only unpriced structure in this section, and "
                        "everything else in its slot list is unknown too. Neurons here "
                        "are less modality-specific than in primary somatosensory "
                        "cortex, so the parallel cutaneous and deep channels the "
                        "previous structure preserves are not preserved here, and "
                        "nothing above says what replaces them."),
    ),
    subelements=("second somatosensory area", "parietal ventral area",
                 "ventral somatosensory area"),
    rank=3,
    axes=("field", "map position", "lamina"),
    partitions=False,
)
# The map axis reverses at the seam, and no other axis in the map does this.  The second
# somatosensory and parietal ventral areas are mirror-symmetric body maps joined at the
# hand, foot and face representations, so the position axis runs one way in one field and
# the other way in the other.  A single monotonic index across the field axis is wrong at
# the seam, and the seam is not located by any number given above.
#
# The field axis carries a connectivity difference as well as a position reversal: the
# parietal ventral area's callosal connections are restricted to its own homologue and
# the second somatosensory area's are not, so the two fields differ in how much of the
# other hemisphere they see.
FIELD_COUNT = 3
SEAM_POSITION = None    # not given
S2_COUNT_STATE = UNKNOWN  # it exists and has not been measured: an experiment to run

SUPERIOR_PARIETAL_AREA_5 = Structure(
    "superior parietal area 5",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, 25_000_000,
                   FAN_IN_UNDERIVED,
                   note="soft, no per-subdivision count found -- so this structure has "
                        "the sub-elements and not the partition, the ordinary case, and "
                        "it is the direct contrast with primary somatosensory cortex. "
                        "Human area 5 overlaps all three subdivisions and is "
                        "distinguished by a dense concentration of "
                        "SMI-32-immunoreactive pyramidal neurons in layers III and V."),
    ),
    subelements=("PE", "PEa", "PEc"),
    rank=2,
    axes=("subdivision", "position"),
    partitions=False,
)
# The three subdivisions form an anterior-to-caudal functional gradient: PE on the gyral
# convexity, most sensitive to limb proprioception and encoding arm position with the
# most independence from gaze; PEa on the medial bank of the intraparietal sulcus,
# proprioceptive and kinematic, the reach-planning end; PEc caudally, sensitive to
# proprioception and gaze together, linked to lower-limb motor representations,
# vestibular cortex and optic-flow areas, with a proposed role in locomotion and limb
# coordination in the environment rather than reaching alone.
#
# A gradient is not a partition and the array has to be one or the other.  Which of the
# two this axis is is not stated, and the difference matters: gaze-dependence varies
# along it, so an edge terminating on "area 5" lands on cells whose gaze sensitivity
# depends on where along the gradient they sit.
SUBDIVISION_COUNT = 3

# The output frame is contested, and on this project's payload rule the coordinate frame
# is part of the payload -- so an unsettled frame is an unsettled payload.  Reported
# frames are body-, shoulder- and hand-centred across different studies, and in area PE
# specifically a memorised target's distance is encoded relative to the initial hand
# position rather than to the body.  The far ends have not withdrawn: the medial
# intraparietal area and the precuneus both type the frame as body-centred, so the two
# ends disagree about the frame, which is a payload disagreement and not a wording one.
AREA_5_OUTPUT_FRAME = CONTESTED

# About 15% of PEc's labelled afferent neurons lie in the posterior cingulate area PEci
# and a further 10% elsewhere on the medial surface.
PEC_CINGULATE_SHARE = 0.15
PEC_MEDIAL_OTHER_SHARE = 0.10

PRIMARY_MOTOR = Structure(
    "primary motor cortex",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, 30_000_000,
                   FAN_IN_UNDERIVED,
                   note="soft. Agranular cortex -- thin or absent layer 4, layer-5 "
                        "pyramidal and Betz-cell heavy, because it is output-dominated"),
    ),
    subelements=AGRANULAR_LAMINAE,
    rank=2,
    axes=("lamina", "somatotopic position"),
    partitions=False,
)
# Seven laminae, not eight, and that is this entry's structural fact.  The standard
# laminar block is withheld here and the withholding is the finding: three of its edges
# terminate on or leave from layer 4, which this entry says is thin or absent, so
# transcribing it would assert a circuit the entry's own Function denies.  The internal
# edges therefore read owed, and this structure has no internal edges at all -- the only
# cortical entry in this file of which that is true.
#
# The tangential axis's status is owed, and it is a different open state from an axis
# with no extent: whether the somatotopic motor map and the movement primitives are a
# compartmentation an edge could terminate on, or a continuous map, is not established.
# This entry has both problems at once.
M1_TANGENTIAL_SUBELEMENTS = OWED

STRUCTURES = (DORSAL_COLUMN_NUCLEI, VENTRAL_POSTERIOR_THALAMUS, PRIMARY_SOMATOSENSORY,
              SECOND_SOMATOSENSORY, SUPERIOR_PARIETAL_AREA_5, PRIMARY_MOTOR)

# --------------------------------------------------------------------------
# Edges.
#
# Every latency here is None.  None is not a licence to substitute zero or a uniform
# interval: no time constant and no ordering constraint is stated anywhere in this
# section, the first section since chunk 01 of which that is true.
#
# Two of the modulatory lines below are spatially structured rather than scalar.  The
# corticocuneate gain has a centre of facilitation and a surround of inhibition, so
# applying it needs the somatotopic index of the line it modulates; reducing it to a
# scalar would delete the sharpening the edge exists to perform.
# --------------------------------------------------------------------------

EDGES: tuple[Edge, ...] = (

    # --- dorsal column nuclei and trigeminal relay ----------------------
    Edge(class_endpoint("mechanoreceptor afferents"),
         here("dorsal column nuclei and trigeminal relay"),
         carries="cutaneous: touch, pressure, vibration -- intensity per skin location, "
                 "somatotopic",
         representation=Representation("intensity per skin location", TO_DERIVE,
                                       EVENT_DRIVEN, SOMATOTOPIC),
         note="the producer is outside the map: this pathway's transducers arrive from "
              "a body that has no entry, so no sampling rate is stated and none is "
              "borrowed. Fan-in: no contacts-per-neuron figure found. The 87% "
              "convergence figure is a different measurement -- it counts cells "
              "responding to two or more nerve territories, not contacts per neuron -- "
              "and it is not promoted into a fan-in here."),

    Edge(class_endpoint("proprioceptor afferents"),
         here("dorsal column nuclei and trigeminal relay"),
         carries="muscle spindle length and rate, Golgi tendon force, joint angle",
         representation=Representation("length, rate, force, joint angle", TO_DERIVE,
                                       EVENT_DRIVEN, BODY_CONFIG),
         note="two distinct payloads on one relay, and this is the second; the producer "
              "is outside the map"),

    Edge(here("primary somatosensory cortex"),
         here("dorsal column nuclei and trigeminal relay"),
         carries="no new stimulus content; a movement-contingent gain signal",
         role=MODULATORY,
         representation=Representation(
             "gain", "attenuating, comparable to that seen in cerebral cortex and "
             "larger than in the spinal cord", EVENT_DRIVEN,
             "somatotopic, and organised centre-surround: facilitation centrally, "
             "inhibition peripherally"),
         note="corticocuneate, from the hand regions of areas 3b, 3a and 1/2, "
              "bilateral. Not a scalar gain: the cortical fibres produce a central zone "
              "of facilitation surrounded by a peripheral zone of inhibition, which is "
              "a spatial sharpening operation, so applying it needs the somatotopic "
              "index of the line it modulates. The centre-surround arithmetic is "
              "Micky's and none is written."),

    Edge(here("primary motor cortex"),
         here("dorsal column nuclei and trigeminal relay"),
         carries="the same movement-contingent gain signal, from the forelimb region",
         role=MODULATORY,
         representation=Representation(
             "gain", TO_DERIVE, EVENT_DRIVEN,
             "somatotopic, centre-surround"),
         note="corticocuneate, bilateral, arriving on the same target as the "
              "somatosensory limb, and its distinctness from that limb is " + OWED +
              ": the retrograde study labelled both and whether they carry the same "
              "content is not established. So two edges are declared where there may be "
              "one payload -- the second place in this file where the graph is "
              "knowingly a superset."),

    Edge(here("dorsal column nuclei and trigeminal relay"),
         here("ventral posterior thalamus", "parvalbumin core"),
         carries="both payloads, somatotopic, with the cutaneous and deep submodalities "
                 "kept separate",
         representation=Representation("both payloads, submodalities separate",
                                       "a minority of the synapses", EVENT_DRIVEN,
                                       SOMATOTOPIC),
         note="by the medial lemniscus and trigeminothalamic tract. Its terminals form "
              "triadic synapses with GABAergic presynaptic dendrites -- an arrangement "
              "the spinothalamic input does not have, and one the shared edge type has "
              "no field for. The separation is carried through the structure rather "
              "than re-established at the far end, so no equation here may merge the "
              "two payloads."),

    # One of two edges carrying one payload to destinations of different kinds.  They are
    # identical in units, range, timing and frame, and they must not be deduplicated: the
    # cortical copy becomes reportable and this one writes procedural change, motor
    # learning being cerebellum-dependent.  A learning channel that operates without
    # perceptual access is an architectural fact, not an absence of one.
    Edge(here("dorsal column nuclei and trigeminal relay", "external cuneate nucleus"),
         unstemmed("cerebellum"),
         carries="proprioception only, body configuration, unconscious",
         representation=Representation("length, rate, force, joint angle", TO_DERIVE,
                                       EVENT_DRIVEN, BODY_CONFIG),
         note="by the cuneocerebellar tract. DO NOT DEDUPLICATE against the thalamic "
              "proprioceptive line: the two copies differ in what kind of memory they "
              "write, not in whether they are used, and merging them deletes an "
              "architectural fact rather than a redundancy. This edge's line count is "
              "unobtainable rather than merely underived -- its source sub-element has "
              "no separate count."),

    Edge(here("dorsal column nuclei and trigeminal relay"),
         unstemmed("dorsal cochlear nucleus"),
         carries="the head, face and neck configuration copy, used to cancel "
                 "self-generated sound",
         representation=Representation("head, face and neck configuration", TO_DERIVE,
                                       EVENT_DRIVEN, "head/face/neck configuration"),
         note="contested at the receiving end: the granule-cell domain carrying this "
              "copy is decreased or absent in primates, so what receives this edge in a "
              "human is " + OWED),

    # --- ventral posterior thalamus -------------------------------------
    Edge(unstemmed("spinal cord grey matter, laminae I and IV-VIII"),
         here("ventral posterior thalamus", "calbindin matrix"),
         carries="pain, temperature and crude touch",
         representation=Representation("pain, temperature, crude touch", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       "diffuse -- terminating preferentially in the "
                                       "matrix, not point-to-point"),
         note="spinothalamic, and with the spinal trigeminal nucleus. No triads, unlike "
              "the lemniscal input. Whether the lamina-I pain and temperature stream "
              "relays here at all is " + CONTESTED + ": one account concentrates "
              "lamina-I terminations in a separate posterior ventral medial nucleus, "
              "the other routes spinothalamic input into this complex's matrix, and the "
              "two accounts are not reconciled. The ~10% nociceptive figure is carried "
              "forward unverified and is not written as a parameter."),

    Edge(here("primary somatosensory cortex"), here("ventral posterior thalamus"),
         carries="no stimulus content -- the gate",
         role=MODULATORY,
         representation=Representation("gate", TO_DERIVE, EVENT_DRIVEN, NO_FRAME)),

    Edge(unstemmed("thalamic reticular nucleus"), here("ventral posterior thalamus"),
         carries="no stimulus content -- the gate",
         role=MODULATORY,
         representation=Representation("gate", TO_DERIVE, EVENT_DRIVEN, NO_FRAME)),

    Edge(here("ventral posterior thalamus", "parvalbumin core"),
         here("primary somatosensory cortex", "layers 3B and 4"),
         carries="the somatotopic payload, gated, not transformed",
         representation=Representation(
             "cutaneous intensity; proprioceptive configuration", TO_DERIVE,
             EVENT_DRIVEN,
             "topographic and point-to-point, sorted by submodality: proprioception -> "
             "area 3a, cutaneous -> area 3b"),
         note="this is the edge that carries the map. The submodality sort is a routing "
              "of the output onto two different cortical targets rather than a "
              "computation, and an equation that mixed the submodalities before the "
              "sort would have made the sort impossible."),

    Edge(here("ventral posterior thalamus", "calbindin matrix"),
         here("primary somatosensory cortex", "layer 1"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN,
                                       "not topographic and not confined to one "
                                       "cortical area"),
         note="payload " + OWED + " at both ends: what a non-topographic thalamic "
              "broadcast to layer 1 delivers, as a type with a range and a frame, is "
              "not established anywhere. It terminates on apical tuft dendrites "
              "belonging to cells whose somata sit in layers 2/3 and 5, with no second "
              "internal edge written for the propagation to those somata -- so the line "
              "arrives at a place and nothing carries it to the cells it belongs to. "
              "Whether a unit has compartments is Micky's."),

    Edge(here("ventral posterior thalamus"), here("second somatosensory area"),
         carries="deep-receptor signals from muscles and joints, little if any "
                 "cutaneous content",
         representation=Representation("deep-receptor signals", TO_DERIVE,
                                       EVENT_DRIVEN, TO_DERIVE),
         note="from the ventral posterior inferior nucleus and the ventral posterior "
              "superior territory. This is the entry's correction: these fields receive "
              "little if any cutaneous input from the thalamus, so their cutaneous "
              "payload must arrive through the cortical edge, and an account that "
              "treats this region as a second cutaneous relay fed from the thalamus has "
              "the modality backwards."),

    # --- primary somatosensory cortex -----------------------------------
    # The four intracortical edges of the rising code.  They exist under the serial
    # reading; the four direct thalamic edges exist under the parallel one; and the
    # architecture keeps both rather than choosing, because irreversible ablation and
    # reversible inactivation are not measuring the same thing.  Both sets are declared
    # and neither is marked preferred.
    Edge(here("primary somatosensory cortex", "area 3b"),
         here("primary somatosensory cortex", "area 1"),
         carries="point pressure and adaptation rate, elaborating toward texture and "
                 "motion across the skin",
         representation=Representation("pressure, adaptation rate", TO_DERIVE,
                                       EVENT_DRIVEN, SOMATOTOPIC),
         note="CONTESTED TOPOLOGY: whether the four areas are a chain or four partly "
              "independent lines is disputed, and this edge set is one of the two the "
              "architecture keeps"),

    Edge(here("primary somatosensory cortex", "area 1"),
         here("primary somatosensory cortex", "area 2"),
         carries="toward size and shape",
         representation=Representation("texture, motion across the skin", TO_DERIVE,
                                       EVENT_DRIVEN, SOMATOTOPIC),
         note="CONTESTED TOPOLOGY, as above"),

    Edge(here("primary somatosensory cortex", "area 3a"),
         here("primary somatosensory cortex", "area 2"),
         carries="the deep payload converging with the cutaneous stream",
         representation=Representation("limb and joint configuration", TO_DERIVE,
                                       EVENT_DRIVEN, SKIN_JOINT),
         note="the transfer that makes stereognosis possible. The modality split is "
              "preserved to here -- cutaneous by areas 3b and 1, deep by 3a and 2, as "
              "parallel channels rather than one merged stream -- so an equation "
              "merging the two streams before area 2 would destroy the convergence "
              "this edge exists to deliver. CONTESTED TOPOLOGY, as above."),

    Edge(here("primary somatosensory cortex", "area 3b"),
         here("primary somatosensory cortex", "area 2"),
         carries="direct",
         representation=Representation("pressure, adaptation rate", TO_DERIVE,
                                       EVENT_DRIVEN, SOMATOTOPIC),
         note="CONTESTED TOPOLOGY, as above"),

    Edge(here("primary somatosensory cortex", "area 2"),
         here("second somatosensory area"),
         carries="size, shape and stereognosis, cutaneous and deep combined -- the "
                 "first place the payload describes an object rather than the skin",
         representation=Representation("size, shape, stereognosis", TO_DERIVE,
                                       EVENT_DRIVEN, "object, not skin"),
         note="the payload changes kind here and it is the only such change in this "
              "file. A consumer inheriting 'somatotopic' from the structure rather than "
              "from the line would be reading an object code as a skin map."),

    Edge(here("primary somatosensory cortex", "area 3a"),
         here("primary motor cortex"),
         carries="limb and joint configuration -- the feedback signal that closes the "
                 "sensorimotor loop",
         representation=Representation(
             "a graded position variable per digit plus a categorical posture signal",
             TO_DERIVE, EVENT_DRIVEN, "limb and joint configuration"),
         note="a payload type rather than a label: single-unit recording distinguishes "
              "single-digit position-scaled, multi-digit position-scaled, and "
              "posture-selective cells, so what leaves is a continuous vector and a "
              "discrete class travelling together, not an undifferentiated "
              "proprioception. A single array cannot carry both."),

    Edge(here("primary somatosensory cortex", "area 3a"),
         far("premotor cortex", FRONTAL),
         carries="limb and joint configuration",
         representation=Representation(
             "a graded position variable per digit plus a categorical posture signal",
             TO_DERIVE, EVENT_DRIVEN, "limb and joint configuration")),

    Edge(here("primary somatosensory cortex", "area 2"),
         here("superior parietal area 5"),
         carries="limb configuration and tactile object properties",
         representation=Representation("limb configuration, object properties",
                                       TO_DERIVE, EVENT_DRIVEN, SKIN_JOINT),
         note="principally from area 2 with area 3a. The frame here is the one that is "
              "re-expressed downstream, and downstream the frame is contested."),

    Edge(here("primary somatosensory cortex"),
         far("medial intraparietal area", PARIETAL),
         carries="limb configuration and tactile object properties",
         representation=Representation("limb configuration, object properties",
                                       TO_DERIVE, EVENT_DRIVEN, SKIN_JOINT),
         note="the far end declares a primary somatosensory source on a four-source "
              "line, and it is the only entry in that file that does -- the angular "
              "gyrus declares only a 'somatosensory association cortex' class, which is "
              "itself unresolved. So the parietal class narrows to one named member and "
              "one class facing a class, and naming this consumer at the architecture "
              "is " + OWED),

    Edge(here("primary somatosensory cortex", "area 3a"),
         far("insula", INSULA),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the far end was not tested"),

    Edge(here("primary somatosensory cortex"),
         class_endpoint("posterior parietal cortex"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="from areas 1 and 2; a class endpoint, and splitting it is a source "
              "decision"),

    # --- second somatosensory area --------------------------------------
    Edge(here("primary somatosensory cortex"), here("second somatosensory area"),
         carries="cutaneous by areas 3b and 1, deep by areas 3a and 2 -- two parallel "
                 "channels, not one merged stream",
         representation=Representation(
             "cutaneous and deep, on parallel channels", TO_DERIVE, EVENT_DRIVEN,
             "somatotopic on arrival; and this line carries the cutaneous payload, "
             "because the thalamic lines do not"),
         note="whether this edge is necessary for the region to respond is the disputed "
              "topology. Against the thalamic line into this structure, this is the "
              "entry's correction and it inverts the intuitive wiring."),

    Edge(unstemmed("anterior pulvinar"), here("second somatosensory area"),
         carries="deep-receptor signals, not cutaneous",
         representation=Representation("deep-receptor signals", TO_DERIVE,
                                       EVENT_DRIVEN, TO_DERIVE),
         note="declared at this end only -- the pulvinar entry names no somatosensory "
              "target -- so it is " + OWED + " or withdrawn. It is a second endpoint on "
              "a shared line, so splitting the line is owed too."),

    Edge(class_endpoint("contralateral second somatosensory area, area 3b and area 7b"),
         here("second somatosensory area"),
         carries="the opposite side's tactile payload, which is what makes the "
                 "bilateral receptive field",
         representation=Representation(
             "the opposite side's tactile payload", TO_DERIVE, EVENT_DRIVEN,
             "the other hemisphere's body map"),
         note="callosal, and the first line in this pathway carrying the other body "
              "side: receptive fields here are large and frequently bilateral, spanning "
              "multiple digits, the whole hand, or both hands. An implementation "
              "without this line does not have a degraded receptive field; it has a "
              "unilateral one. The three fields differ in how much of the other "
              "hemisphere they see -- the parietal ventral area's callosal connections "
              "are restricted to its own homologue and the second somatosensory area's "
              "are not."),

    Edge(here("second somatosensory area"),
         far("anterior intraparietal area", PARIETAL),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("second somatosensory area", "parietal ventral area"),
         far("premotor cortex", FRONTAL),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("second somatosensory area"), unstemmed("area 7b"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("second somatosensory area"),
         unstemmed("parietal rostroventral area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="far end unchecked"),

    Edge(here("second somatosensory area", "ventral somatosensory area"),
         far("insula", INSULA),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("second somatosensory area"), here("primary somatosensory cortex"),
         carries="feedback, no new stimulus content",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       SOMATOTOPIC),
         note="reciprocal; co-instantiation closes here"),

    # --- superior parietal area 5 ---------------------------------------
    Edge(far("medial bank of the intraparietal sulcus", PARIETAL, "area PEa"),
         here("superior parietal area 5", "PEa"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the far end declares this limb naming the medial bank and area PEa in "
              "the same terms, and marks its own payload owed -- so the limb is "
              "two-ended and untyped at both ends, which is a different state from "
              "having no producer. This line names four sources at once in the "
              "architecture (the medial bank, PGop, PFop and the retroinsular area); "
              "the other three are unchecked rather than absent, and splitting the line "
              "is owed at the source."),

    Edge(class_endpoint("PGop, PFop and the retroinsular area"),
         here("superior parietal area 5"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the three untested sources on the four-source line; far ends outside the "
              "files opened here"),

    Edge(far("precuneus", PARIETAL, "anterior sensorimotor sector"),
         here("superior parietal area 5"),
         carries="reach and body-configuration signals",
         representation=Representation("reach and body configuration", TO_DERIVE,
                                       EVENT_DRIVEN, "body-centred"),
         note="the far end calls this the one edge out of itself whose payload can be "
              "written, and records that this end was transcribed from it -- so the "
              "agreement between the two ends certifies nothing about the payload. It "
              "is one statement written twice, not two readings that matched."),

    Edge(far("supplementary motor area and caudal dorsal premotor cortex", FRONTAL),
         here("superior parietal area 5"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="two-ended, untyped there as here; the studies establish the projection, "
              "not its content"),

    # An in-file edge declared at one end only, which is a weaker state than a
    # cross-file one because nothing about file boundaries explains it.  The producer is
    # primary motor cortex, in this file, and its Outputs slot declares muscles, the
    # return through the world, the ventral anterior / ventral lateral thalamus and the
    # dorsal column nuclei, and no parietal target of any kind.  Owed at the source:
    # declare it at primary motor cortex, or withdraw it here.  Not repaired at this
    # rung, because writing it at the producer would assert a connection nothing here
    # has read for.
    Edge(here("primary motor cortex"), here("superior parietal area 5"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="CONSUMER-ONLY IN THIS FILE: the producer is in this same file and "
              "declares no parietal target of any kind. Owed at the source."),

    Edge(class_endpoint("posterior cingulate area PEci and cingulate areas 23 and 24"),
         here("superior parietal area 5", "PEc"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="substantial for PEc: about 15% of its labelled afferent neurons lie in "
              "PEci and a further 10% elsewhere on the medial surface -- 25% in total"),

    Edge(class_endpoint("gaze-position signals"),
         here("superior parietal area 5"),
         carries="eye position, and for PEc the interaction of gaze with hand position "
                 "rather than either alone",
         role=MODULATORY,
         representation=Representation("eye position", TO_DERIVE, EVENT_DRIVEN, "eye"),
         note="reaching PEc and PEa. For PEc this is not an independent content channel "
              "but a term the limb payload is expressed against -- the fourth structure "
              "in the map to have gaze modulate a non-visual payload, and the "
              "arithmetic is again the open unit-expressiveness question."),

    Edge(here("superior parietal area 5"), far("dorsal premotor cortex", FRONTAL),
         carries="limb position and the reach specification",
         representation=Representation("limb position, reach specification", TO_DERIVE,
                                       EVENT_DRIVEN, CONTESTED),
         note="the payload change across this region is the frame, not the content -- "
              "and the frame is " + CONTESTED + ", reported as body-, shoulder- and "
              "hand-centred across different studies, with area PE encoding a memorised "
              "target's distance relative to the initial hand position rather than to "
              "the body. On this project's payload rule the frame is part of the "
              "payload, so an unsettled frame is an unsettled payload."),

    Edge(here("superior parietal area 5", "PE"), here("primary motor cortex"),
         carries="limb position and the reach specification",
         representation=Representation("limb position, reach specification", TO_DERIVE,
                                       EVENT_DRIVEN, CONTESTED),
         note="reciprocal with area PE"),

    Edge(here("superior parietal area 5"),
         far("medial intraparietal area", PARIETAL),
         carries="the same limb state",
         representation=Representation("limb state", TO_DERIVE, EVENT_DRIVEN,
                                       CONTESTED),
         note="the far end types the frame as body-centred, so the two ends disagree "
              "about the frame -- a payload disagreement and not a wording one. This "
              "end was written independently of that one."),

    Edge(here("superior parietal area 5", "PE"),
         far("anterior intraparietal area", PARIETAL),
         carries="the same limb state",
         representation=Representation("limb state", TO_DERIVE, EVENT_DRIVEN,
                                       CONTESTED),
         note="written independently at the far end"),

    Edge(here("superior parietal area 5"), far("supramarginal gyrus", PARIETAL),
         carries="the same limb state",
         representation=Representation("limb state", TO_DERIVE, EVENT_DRIVEN,
                                       CONTESTED),
         note="the far end records that its end was transcribed from this one, so the "
              "two are one statement written twice and the agreement certifies nothing"),

    Edge(here("superior parietal area 5"), far("precuneus", PARIETAL),
         carries="the same limb state",
         representation=Representation("limb state", TO_DERIVE, EVENT_DRIVEN,
                                       CONTESTED),
         note="the far end types the frame as body-centred AND records that its end was "
              "transcribed from this one -- so it both disagrees and certifies nothing"),

    Edge(here("superior parietal area 5"),
         far("ventral intraparietal area", DORSAL_VISUAL),
         carries="the same limb state",
         representation=Representation("limb state", TO_DERIVE, EVENT_DRIVEN,
                                       CONTESTED),
         note="unchecked"),

    Edge(here("superior parietal area 5"),
         far("lateral intraparietal area", DORSAL_VISUAL),
         carries="the same limb state",
         representation=Representation("limb state", TO_DERIVE, EVENT_DRIVEN,
                                       CONTESTED),
         note="unchecked"),

    # --- primary motor cortex -------------------------------------------
    Edge(far("premotor cortex", FRONTAL), here("primary motor cortex"),
         carries="the planned action, already sequenced and shaped, not yet a muscle "
                 "command",
         representation=Representation("a planned action", TO_DERIVE, EVENT_DRIVEN,
                                       TO_DERIVE),
         note="the far end declares it and is untyped, so this end carries the payload"),

    Edge(unstemmed("thalamus, ventral anterior / ventral lateral"),
         here("primary motor cortex"),
         carries="the basal-ganglia selection (which action is released) and the "
                 "cerebellar correction (how it is shaped), combined on one relay",
         representation=Representation("selection and correction", TO_DERIVE,
                                       EVENT_DRIVEN, TO_DERIVE),
         note="two payloads of different kinds on one line; splitting it would require "
              "the relay to be split, which is another file's decision. The far end "
              "names this area and is untyped."),

    # The edge whose consumer is not in this map.  no_entry, not unstemmed: the muscles,
    # the skeleton and their dynamics have no entry in any file, which is a different
    # state from a far end whose file has not been opened.  Its line count is
    # unobtainable, having no far end to count against, and `motor_command`'s shape is
    # not derivable for the same reason -- every other output array in this file gets its
    # shape from what receives it.
    Edge(here("primary motor cortex"), no_entry("muscles"),
         carries="the motor command",
         representation=Representation("motor command", TO_DERIVE, EVENT_DRIVEN,
                                       "the body"),
         note="by the corticospinal tract. The consumer at the far end is not in this "
              "map, so this edge's payload is declared with no one to receive it. This "
              "is the map's largest open boundary on the output side, the mirror image "
              "of the retina's input edge."),

    # The return line, whose producer is outside the map.  It and the edge above are the
    # same physical loop and neither end of it is represented, so the two cannot be
    # checked against each other the way every other producer/consumer pair in this file
    # can.  A design that closed the loop by feeding the motor command back as its own
    # consequence would run and would be wrong.
    Edge(class_endpoint("the world"), here("primary somatosensory cortex"),
         carries="the movement's consequence, read back through proprioception",
         representation=Representation(
             "the movement's consequence", TO_DERIVE,
             "event-driven, and the event is outside the map", "the world"),
         fan_out=None,
         note="fan-out: " + NOT_APPLICABLE + ". The loop closes through the body, not "
              "inside the brain: a sensorimotor loop instantiated without a body is not "
              "a degraded loop -- the return edge has no producer."),

    Edge(here("primary motor cortex"),
         unstemmed("thalamus, ventral anterior / ventral lateral"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="corticothalamic and reciprocal; owed at both ends"),
)

# --------------------------------------------------------------------------
# Edges declared at producers in another file and deliberately not written above.
#
# Broca's area declares `-> premotor cortex and primary motor cortex, for articulation`,
# and the right inferior frontal gyrus declares the homologous edge for affective
# prosody.  That file records that its own premotor structure declares neither and marks
# both as inherited gaps owed at the source.  This end is the second consumer on both and
# does not declare them either -- so each edge is producer-only at BOTH of its named
# targets rather than at one, which is what that file had assumed.
#
# They are not written in, because writing an edge whose only support is the far end's
# declaration would assert a connection this file has read nothing for.  Owed at the
# source: accept both here, or narrow the producers' endpoint to premotor cortex alone.
# --------------------------------------------------------------------------

DECLARED_AT_PRODUCER_ONLY = (
    ("Broca's area", FRONTAL, "primary motor cortex",
     "-> premotor cortex and primary motor cortex, for articulation"),
    ("right inferior frontal gyrus", FRONTAL, "primary motor cortex",
     "the homologous edge for affective prosody"),
)

# --------------------------------------------------------------------------
# Internal edges the entries require and no rung supplies.
#
# Left absent and named rather than invented, because a well-formed invented edge reads
# exactly like a derived one.
# --------------------------------------------------------------------------

OWED_INTERNAL_EDGES = (
    ("primary somatosensory cortex",
     "the propagation from the layer-1 apical tuft to the somata in layers 2/3 and 5. "
     "The matrix line arrives at a place and nothing carries it to the cells it belongs "
     "to. A single-compartment unit cannot express it; whether a unit has compartments "
     "is Micky's."),
    ("primary motor cortex",
     "all of them. The standard laminar block is withheld because three of its edges "
     "route through layer 4, which this entry says is thin or absent, so transcribing "
     "it would assert a circuit the entry's own Function denies. This is the only "
     "cortical entry in this file with no internal edges at all."),
    ("superior parietal area 5",
     "whatever generates the persistent activity. Movement-related activity persists in "
     "the absence of sensory stimulation, so it is internally generated rather than "
     "driven -- and what generates it is stated at no rung."),
)


# --------------------------------------------------------------------------
# Reporting.  Every figure below is recomputed from the counts above rather than
# transcribed.
# --------------------------------------------------------------------------


def the_partition() -> str:
    """The first structure in the map that can be allocated sub-element by sub-element.

    Every previous section stated a total for a structure and named sub-elements the
    edges terminate on, with nothing connecting them.  Here primary somatosensory cortex
    is given no total at all: four counts, one per area, and the total is derived.
    """
    out = []
    for s in STRUCTURES:
        counts = [p.count for p in s.populations]
        stated = "yes" if s.partitions else "no "
        if all(c is not None for c in counts):
            total = f"{sum(counts)/1e6:6.1f}M"
        else:
            total = f"{UNKNOWN:>7}"
        out.append(f"  {s.name[:44]:44} {len(s.subelements):2d} sub-elements, "
                   f"total {total}, partitions {stated}")
    s1 = PRIMARY_SOMATOSENSORY
    per = "  ".join(f"{p.name}={p.count/1e6:.0f}M" for p in s1.populations)
    out.append(f"  and the one that does, by area: {per}")
    out.append(f"  derived total {sum(p.count for p in s1.populations)/1e6:.0f}M, "
               f"which the rung above does not state")
    return "\n".join(out)


def allocation_against_connection() -> str:
    """What the partition buys, and it is worth being precise about how little.

    Four arrays can be allocated where an unpartitioned count could not be.  It does
    not buy an
    edge: every fan-in in the section is underived, so the structure that can be
    allocated still cannot have its edges sized.  Allocation and connection are separate
    closures.
    """
    populations = sum(len(s.populations) for s in STRUCTURES)
    with_fan_in = sum(1 for s in STRUCTURES for p in s.populations
                      if p.fan_in is not None)
    allocatable = sum(len(s.populations) for s in STRUCTURES if s.partitions)
    return (f"  populations with a stated count : "
            f"{sum(1 for s in STRUCTURES for p in s.populations if p.count)} "
            f"of {populations}\n"
            f"  structures whose count partitions : "
            f"{sum(1 for s in STRUCTURES if s.partitions)} of {len(STRUCTURES)}\n"
            f"  populations allocatable at sub-element level : {allocatable}\n"
            f"  populations with a stated fan-in : {with_fan_in} of {populations}\n"
            f"  so allocation closes for {allocatable} and connection for "
            f"{with_fan_in}")


def realisation_gap() -> str:
    """Derived against realised, and here they are equal for a reason worth stating.

    Every width is the 16-bit ceiling, which is a container boundary by construction, so
    nothing is lost to padding.  A zero gap and an unmeasured fan-in are the same fact
    stated twice.
    """
    out, derived_total, realised_total = [], 0, 0
    for s in STRUCTURES:
        for p in s.populations:
            d, r = p.parameter_bytes, p.realised_bytes
            if d is None:
                out.append(f"  {(s.name + ' / ' + p.name)[:52]:52} "
                           f"{UNKNOWN:>10}")
                continue
            derived_total += d
            realised_total += r
            out.append(f"  {(s.name + ' / ' + p.name)[:52]:52} "
                       f"{p.count/1e6:5.1f}M x {p.threshold_bits:2d} bits = "
                       f"{d/1e6:6.2f} MB, realised {r/1e6:6.2f} MB")
    out.append(f"  {'stated total':52} {derived_total/1e6:6.2f} MB, "
               f"realised {realised_total/1e6:6.2f} MB, "
               f"gap {100*(realised_total-derived_total)/derived_total:.0f}%")
    return "\n".join(out)


def the_open_loop() -> str:
    """The two edges that are one physical loop with neither end represented."""
    out = []
    for e in EDGES:
        if e.target.kind == "no entry":
            out.append(f"  OUT: {e.source.name} -> {e.target.name}  "
                       f"(no entry in any file)")
            out.append(f"       payload declared, no one to receive it")
        if e.source.kind == "class" and e.source.name == "the world":
            out.append(f"  IN : {e.source.name} -> {e.target.name}")
            out.append(f"       payload declared, no producer; fan-out "
                       f"{NOT_APPLICABLE}")
    out.append("  the same physical loop, and the two rows cannot be checked against")
    out.append("  each other the way every other producer/consumer pair here can")
    return "\n".join(out)


def contested_topology() -> str:
    """The edge set that is knowingly larger than the anatomy may be.

    Whether the four somatosensory areas form a chain or four partly independent lines
    is disputed by two methods that are not measuring the same thing -- irreversible
    ablation reads serial, reversible inactivation reads parallel -- and the architecture
    keeps both edge sets rather than choosing.  Nothing is pruned here: deleting either
    would adjudicate a contest at the rung furthest from the evidence.
    """
    intracortical = [e for e in EDGES if "CONTESTED TOPOLOGY" in e.note]
    thalamic = [e for e in EDGES
                if e.source.name == "ventral posterior thalamus"
                and e.target.name == "primary somatosensory cortex"]
    out = [f"  intracortical chain edges (serial reading)  : {len(intracortical)}"]
    for e in intracortical:
        out.append(f"    {e.source.sub} -> {e.target.sub}")
    out.append(f"  direct thalamic edges (parallel reading)   : {len(thalamic)}")
    out.append("  both sets declared, neither marked preferred")
    out.append("  this is the one open state in the project that makes the code LARGER")
    out.append("  than the biology may be, rather than smaller")
    return "\n".join(out)


def duplicated_payloads() -> str:
    """Lines carrying one payload twice, which must not be deduplicated.

    Proprioception leaves the first relay on two edges to destinations of different
    kinds.  They are identical in units, range, timing and frame, and the difference is
    what kind of memory each writes: the cortical copy becomes reportable, the cerebellar
    copy writes procedural change.  A learning channel that operates without perceptual
    access is an architectural fact, not an absence of one.
    """
    rows = [e for e in EDGES if "DO NOT DEDUPLICATE" in e.note]
    out = [f"  edges marked against deduplication : {len(rows)}"]
    for e in rows:
        out.append(f"    {e.source.name[:34]:34} -> {e.target.name}")
    out.append("  and one more of a different kind: the corticocuneate gain is declared")
    out.append("  twice, by primary somatosensory and by primary motor cortex, onto the")
    out.append("  same target, and their distinctness is owed -- so two edges are")
    out.append("  declared where there may be one payload")
    return "\n".join(out)


def laminar_scope() -> str:
    """Which entries in this file may carry the Class-3 laminar block, and which not."""
    out = []
    for s in STRUCTURES:
        if s.name == "primary motor cortex":
            verdict = (f"WITHHELD -- agranular, {len(AGRANULAR_LAMINAE)} laminae, not "
                       f"{len(GRANULAR_LAMINAE)}")
        elif s.name in ("dorsal column nuclei and trigeminal relay",
                        "ventral posterior thalamus"):
            verdict = "not cortex -- the question does not arise"
        else:
            verdict = f"applies -- granular isocortex, {len(GRANULAR_LAMINAE)} laminae"
        out.append(f"  {s.name[:44]:44} {verdict}")
    out.append("  stating the scope does not license the block's arithmetic, and no")
    out.append("  entry writes an update equation from it")
    return "\n".join(out)


def figures_not_promoted() -> str:
    """Two figures the rung above forbids promoting into a width or a fraction."""
    pct = 100 * CONVERGENCE_CELLS_RESPONDING / CONVERGENCE_CELLS_RECORDED
    dcn = DORSAL_COLUMN_NUCLEI.populations[0]
    return (f"  87% convergence : {CONVERGENCE_CELLS_RESPONDING} of "
            f"{CONVERGENCE_CELLS_RECORDED} cells = {pct:.1f}%\n"
            f"    counts cells responding to two or more nerve territories, NOT\n"
            f"    contacts per neuron; fan_in at that structure reads "
            f"{dcn.fan_in}\n"
            f"  ~10% nociceptive at the thalamus : carried forward unverified,\n"
            f"    a candidate for removal or sourcing; no such parameter exists here")


def owed_internal_edges() -> str:
    out = []
    for structure, what in OWED_INTERNAL_EDGES:
        out.append(f"  {structure}")
        out.append(f"    {what}")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report(STRUCTURES, f"Brain {STEM}"))
    print()
    print("the first partition in the map:")
    print(the_partition())
    print()
    print("what the partition buys:")
    print(allocation_against_connection())
    print()
    print("derived against realised:")
    print(realisation_gap())
    print()
    print("the loop that does not close inside the map:")
    print(the_open_loop())
    print()
    print("the contested topology, and the superset it produces:")
    print(contested_topology())
    print()
    print("payloads carried twice on purpose:")
    print(duplicated_payloads())
    print()
    print("the laminar block's scope in this file:")
    print(laminar_scope())
    print()
    print("figures the rung above forbids promoting:")
    print(figures_not_promoted())
    print()
    print(edge_report(EDGES))
    print()
    print("internal edges owed above this rung:")
    print(owed_internal_edges())
    print()
    print(representation_report(EDGES))
    print()
    for fn, label in ((emission, "emission"), (fan_in_map, "connectivity"),
                      (allocate, "allocation"), (schedule, "scheduling"),
                      (learn, "learning")):
        try:
            fn()
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
