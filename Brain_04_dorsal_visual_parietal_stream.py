"""Brain — 04 dorsal visual / parietal stream: where vision stops being about recognition.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

Four isocortical areas that re-express visual information in coordinate frames for
action.  The characteristic operation is a coordinate transform, and its stated
mechanism is a gain field: a sensory receptive field multiplicatively modulated by eye
and head position.

That mechanism is the reason no update equation appears anywhere below.  A gain field
is a product.  The threshold-gate model has equal weights and no multiply, by
construction, which is what makes the stored value a single threshold -- so this
section's characteristic operation is the one arithmetic the sizing model excludes.
Three of the four structures here rest on it: the ventral intraparietal area, whose
whole reason for existing is the transform; the lateral intraparietal area, which
carries eye-position gain modulation on its own face; and the medial superior temporal
area, whose cells combine visual and vestibular heading linearly with subadditive
weights, which is not a gain field and is still not a sum of equal-weight inputs.

Counting basis is uniform for the first time in the map: per hemisphere, all four.
Every row prices, no row reads underived, and the total is exactly 124.00 MB at the
16-bit ceiling.  The total is clean because nothing was measured, not because
everything was: no fan-in in this section is known, so every neuron sits at the cap and
nothing is derived below it.  The realisation gap is zero for the same reason, since
the ceiling is a container boundary by construction.

The element class is uniform too, and that is a first.  Every population here is a
threshold gate.  No transducer, no graded non-spiking element, no transmission-only
structure and no sign-inverting stage appears -- a positive statement about the
section, not an omission.  The earlier sections needed all four.

Sizing is what this section does best and it is the least of what the code needs.
Every array below has a known element count and an unknown shape: the extent of every
tangential axis is underived or unknown at all four structures.  A count sizes a
population; it does not size an array.

Every edge latency reads None, and this section makes that fail in two new ways.  Two
of the middle temporal area's inputs carry the same payload and differ only in arrival
time, so an update interval coarse enough to make them equal merges two declared edges
into one.  And the corollary discharge reaching the lateral intraparietal area is only
useful if it arrives before the eye moves -- an ordering constraint against an event
outside the section, which is correctness rather than performance.  An edge carries a
latency in seconds and cannot carry a predicate over two events; the requirement is
declared at three files and the field that would hold it exists at none.

No global clock may be assumed, and no latency here is stated in steps.
"""

from __future__ import annotations

from Brain_config import (
    CONTESTED, EVENT_DRIVEN, Edge, MODULATORY, NO_FRAME, OWED, PER_HEMISPHERE,
    Population, Representation, Structure, THRESHOLD_GATE, TO_DERIVE, UNKNOWN,
    allocate, class_endpoint, edge_report, emission, fan_in_map, far, here, learn,
    representation_report, schedule, sizing_report, unstemmed,
)

STEM = "04_dorsal_visual_parietal_stream"

# Far files reached from this section.  The stem, never the number: the number fixes
# data-flow position and the section names the structure, and a bare number goes
# silently wrong the moment a file is split, merged or renumbered.
#
# Every other named far end below carries no stem, which means the reading has not been
# done -- not that no far end exists.
VISUAL = "01_visual_pathway"
PARIETAL = "06_posterior_parietal"
FRONTAL = "11_frontal_lobe"
THALAMUS = "12_thalamus"
# Named in this section and reached by no endpoint, which is not a dropped edge.  The
# corollary-discharge route runs frontal eye field -> mediodorsal thalamus -> lateral
# intraparietal area and is declared as one edge from the cortical producer; the nucleus
# is where the route's second leg is missing, not where a line terminates.  So the stem
# is carried on the edge's note rather than on an endpoint, and `far files reached`
# below counts four rather than five for that reason.
BRAINSTEM = "14_brainstem_midbrain_hypothalamus"

# Coordinate frames used more than once.  Frames are the field this section turns on:
# six lines arrive at the ventral intraparietal area in five different frames, and the
# entry's whole function is to change one of them.
RETINOTOPIC = "retinotopic"
EYE_CENTRED = "eye-centred"
BODY_CENTRED = "body-centred"
HEAD_AND_BODY = "head- and body-centred"

# The fan-in bound.  No fan-in in this section is known, so every population sits here
# and nothing is derived below it.  The bound is the shared vocabulary's; it is repeated
# in no structure below, only relied on.
FAN_IN_UNDERIVED = None

# --------------------------------------------------------------------------
# Structures.
#
# Counts and their basis are the architecture's.  No structure here partitions: each
# names eight laminar sub-elements and carries one count for the whole area, so an
# array for layer 4 or layer 1 cannot be sized however precisely an edge names it --
# and edges in this section name a termination layer constantly.
# --------------------------------------------------------------------------

LAMINA_COUNT = 8
"""Eight laminar sub-elements at all four structures: 1, 2, 3, 4, 5a, 5b, 6a, 6b, with
layer 4 undivided.  Uniform across the section, which no earlier section managed."""

MIDDLE_TEMPORAL = Structure(
    "middle temporal area",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, 15_000_000,
                   FAN_IN_UNDERIVED,
                   note="high variance, though the area is fairly well bounded by a "
                        "myeloarchitectonic border and its motion selectivity; a "
                        "myelin-dense grey-matter patch, which is the basis of its "
                        "architectonic delineation"),
    ),
    subelements=("1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=4,
    axes=("lamina", "direction column", "disparity domain", "position"),
    partitions=False,
)
# Two maps superimposed on one sheet, and the third axis is not a refinement of the
# second.  Direction columns of smoothly varying preference run beside a matching set
# preferring the locally opposite direction, forming pinwheels where the area lies on
# the surface rather than in a sulcus.  Disparity columns form a topographic map in
# millimetre-sized interleaved domains.  A position has both a direction preference and
# a disparity preference, and an edge terminating on it terminates on both.
#
# Writing (D, Z) as a product asserts that every direction-column value co-occurs with
# every disparity-domain value at every position, and some regions contain neurons with
# poor disparity tuning, so that map does not tile the area uniformly.  The product form
# over-allocates and the amount is not derivable.
DIRECTION_COLUMN_COUNT = None   # to derive
DISPARITY_DOMAIN_COUNT = None   # to derive

# Speed preference is clustered and explicitly not columnar: a third tuned property with
# no place to live in a rank-4 sheet.  Carried as a per-unit value with no axis, and what
# that means for allocation is owed.
SPEED_ORGANISATION = "clustered, explicitly not columnar -- neither a map nor an axis"

# A coverage mismatch recorded rather than smoothed, and it is why the direction-column
# count cannot be taken from the imaged domains.  Imaging finds only 3-4 segregated
# motion domains, each 2-3 mm2, spaced 2-3 mm, occupying roughly 15% of the surface --
# while about 85% of the area's neurons are directionally selective.  Either the domains
# are not where most direction selectivity lives, or the imaging measures something
# narrower than direction selectivity.  Unresolved.
MOTION_DOMAIN_COUNT = (3, 4)
MOTION_DOMAIN_AREA_MM2 = (2, 3)
MOTION_DOMAIN_SPACING_MM = (2, 3)
MOTION_DOMAIN_SURFACE_FRACTION = 0.15
DIRECTION_SELECTIVE_FRACTION = 0.85

MEDIAL_SUPERIOR_TEMPORAL = Structure(
    "medial superior temporal area",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, 15_000_000,
                   FAN_IN_UNDERIVED,
                   note="softer than the middle temporal area's: no comparable "
                        "myeloarchitectonic signature and retinotopy crude to absent, "
                        "so both its borders and its count are loose"),
    ),
    subelements=("1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=3,
    axes=("lamina", "division", "position"),
    partitions=False,
)
# Two divisions -- dorsal for optic flow, heading and self-motion with large receptive
# fields; lateral for object motion and smooth pursuit with smaller fields -- and
# splitting them into separate entries is owed at the source.  The axis carries them as
# one structure the rung above says should be two.
#
# Tangential sub-elements are unknown: no columnar or compartmental map was found here,
# unlike the area immediately upstream, which has two.  Whether that reflects the
# anatomy or the reading is not established.
MST_DIVISION_COUNT = 2
MST_TANGENTIAL = UNKNOWN

# A third division that is not spatial at all, and it has no index.  Heading-tuned cells
# divide into congruent and opposite cells by the relation between their visual and
# vestibular tunings; they are interleaved, with no spatial segregation found.  Every
# other sub-element anywhere in this section is a place, and an edge terminates on a
# place -- so what it would mean for an edge to terminate on the congruent cells and not
# the opposite ones is owed, and it may not be answerable in the slot's present form.
#
# The representation available is a boolean mask over the population, and a mask is not
# a sub-element, because nothing can terminate on it: an endpoint names a structure or a
# sub-element, and there is no name here for a set defined by a relation between two
# tuning curves.  The relation itself is not given as a rule -- inverted is stated for
# the opposite cells and no threshold on it is supplied.
CONGRUENCE_IS_A_MASK_NOT_A_SUBELEMENT = True

VENTRAL_INTRAPARIETAL = Structure(
    "ventral intraparietal area",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, 12_000_000,
                   FAN_IN_UNDERIVED,
                   note="very high variance -- the softest count in the map: the area "
                        "sits in the fundus of the intraparietal sulcus, lightly "
                        "myelinated, with no clean architectonic border, and the "
                        "macaque area has expanded into several human parietal areas; "
                        "a count whose region has split between species is not the "
                        "same kind of number as one whose region has a stain"),
    ),
    subelements=("1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=3,
    axes=("lamina", "division", "position"),
    partitions=False,
)
VIP_DIVISION_COUNT = 2          # medial and lateral, their separate payloads owed
VIP_TANGENTIAL = UNKNOWN

# The two multiplicands of the gain field, and neither has a producer.  The transform is
# stated as modulation by eye AND head position; the eye-in-head line is declared with its
# source region unnamed, and the head-on-body line is required and undeclared.  So the
# mechanism the entry rests on has no declared input on either multiplicand, which is a
# stronger statement than a payload being untyped.
#
# Head-on-body is not a loose synonym for gaze, which is the reading that would make one
# line sufficient.  Tuning in this area has been measured against head-on-body as its own
# axis, with the head free to rotate and its angular position tracked, independently of
# eye-in-head.  A structure whose tuning is measured against an axis needs an input
# carrying that axis.
VIP_EYE_POSITION_PRODUCER = OWED
VIP_HEAD_POSITION_PRODUCER = OWED

LATERAL_INTRAPARIETAL = Structure(
    "lateral intraparietal area",
    (
        Population("neurons", THRESHOLD_GATE, PER_HEMISPHERE, 20_000_000,
                   FAN_IN_UNDERIVED,
                   note="high variance but firmer-bordered than the ventral "
                        "intraparietal area -- in the lateral bank of the "
                        "intraparietal sulcus with two myeloarchitectonic zones"),
    ),
    subelements=("1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=3,
    axes=("lamina", "subdivision", "retinotopic position"),
    partitions=False,
)
# The subdivision axis carries a signed payload difference, and this is the strongest
# statement in the section that an axis is not a formality.  The ventral subdivision
# holds a single topographic map of the contralateral hemifield with a foveal
# representation rostrally, connects strongly with the frontal eye field and the deep
# collicular layers, and a GABA-A agonist injected into it sharply reduces express
# saccades while the same injection dorsally does not.  Along the dorsal-to-ventral axis
# the population shifts from cells driven by visual events to cells driven by visual and
# saccadic events together.  So the map is not uniform and an edge terminating "on the
# lateral intraparietal area" is under-specified.
#
# The two subdivisions are architectonically defined before they are functionally
# defined: the ventral densely myelinated, the dorsal lightly myelinated, and receptor
# mapping separates them again on a different measure -- N-methyl-D-aspartate,
# alpha1-adrenergic and 5-HT1A receptor densities all higher in the dorsal subdivision.
# Two independent stains agreeing on one border is a stronger basis than either alone.
LIP_SUBDIVISION_COUNT = 2
LIP_TANGENTIAL = "none reported"

STRUCTURES = (MIDDLE_TEMPORAL, MEDIAL_SUPERIOR_TEMPORAL, VENTRAL_INTRAPARIETAL,
              LATERAL_INTRAPARIETAL)

# --------------------------------------------------------------------------
# Edges.
#
# A modulatory edge sets whether, when and how strongly content passes and adds no
# content of its own.  Two lines in this section are explicitly of that kind and say so
# in their own payloads: the frontal attentional gain into the middle temporal area is
# an enhancement or suppression by location and not a stimulus code, and prefrontal area
# 46 into the lateral intraparietal area is a weighting and not a stimulus.  A forward
# operation summing all inputs alike would rank locations by how much attention they
# already had.
#
# Every latency here is None.  None is not a licence to substitute zero or a uniform
# interval -- and in this section a uniform interval has a correctness consequence, not
# only a performance one.  See merged_by_a_uniform_interval() below.
# --------------------------------------------------------------------------

EDGES: tuple[Edge, ...] = (

    # --- middle temporal area -------------------------------------------
    # The direct route.  Its payload is the same as the indirect routes carry and its
    # latency is not: fewer stages, so it arrives earlier.  The only field that
    # distinguishes it reads None.
    Edge(far("V1", VISUAL, "layer 4B, spiny-stellate class"),
         here("middle temporal area", "4"),
         carries="direction of motion and binocular disparity, achromatic, "
                 "coarse-spatial, on the fast few-hop route",
         representation=Representation("direction of motion; binocular disparity",
                                       TO_DERIVE, EVENT_DRIVEN,
                                       RETINOTOPIC + ", achromatic, coarse-spatial"),
         note="the magnocellular annotation is settled: 4B's spiny stellates take "
              "magnocellular input only, from 4C-alpha directly, and these are the "
              "cells that project here, while pyramids take both and project to V2 "
              "instead -- so the direct route here is magnocellular and the route "
              "through V2 is mixed. 76% spiny stellate (range 67-93%) for the cells "
              "labelled from this area against 80% pyramidal for the V2-projecting "
              "population, fewer than about 5% double-labelled, distributed "
              "indiscriminately with respect to the cytochrome-oxidase compartment. "
              "The producer declares neither this payload nor the termination layer: "
              "this is the only typed end and the producer's is the deficient one."),

    Edge(far("V2", VISUAL, "thick stripes, layers 2/3"),
         here("middle temporal area", "4"),
         carries="binocular disparity, high-speed sensitivity, and the surround "
                 "suppression underlying motion opponency; achromatic, retinotopic",
         representation=Representation("binocular disparity; high-speed sensitivity",
                                       TO_DERIVE, EVENT_DRIVEN,
                                       RETINOTOPIC + ", achromatic"),
         note="the two ends disagree about direction and the disagreement is "
              "substantive. The producer declares this edge as carrying motion "
              "direction and disparity; this end declares direction as arriving on the "
              "direct V1 route instead, on the strength of reversible inactivation -- "
              "cooling V2 and V3 degrades disparity tuning disproportionately relative "
              "to direction tuning. A causal inactivation result outranks an "
              "unqualified connectivity statement. What the producer's entry declares "
              "is narrower than assumed here: no payload on this edge at all. So the "
              "disagreement is between this end and the source's V2 declaration, and "
              "the repair starts at the source."),

    Edge(far("V3", VISUAL), here("middle temporal area", "4"),
         carries="the same class of contribution as the V2 route, plus dynamic form: "
                 "contour bound to direction of motion",
         representation=Representation("dynamic form: contour bound to direction",
                                       TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),

    Edge(far("lateral geniculate nucleus", VISUAL),
         here("middle temporal area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="direct, bypassing V1, and sufficient to support motion sensitivity "
              "without it. Mostly koniocellular, sending virtually no collaterals to "
              "V1, numbering about 10% of the V1 population that innervates this area. "
              "A thalamic input to a non-primary cortical area, which contradicts the "
              "framing that a relay funnels everything into a primary area which then "
              "redistributes it. The leading account of blindsight's residual motion "
              "sensitivity."),

    Edge(unstemmed("superior colliculus, di-synaptically by way of the pulvinar"),
         here("middle temporal area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the relay reaches this area and V3 selectively, a subcortical route "
              "into the motion areas that does not pass through V1. Written as one "
              "line where the pulvinar has an entry of its own that declares both "
              "legs -- the split is owed at that entry."),

    Edge(unstemmed("pulvinar"), here("middle temporal area"),
         carries="two things on the same wire: a visual signal that largely reflects "
                 "its cortical driver's content -- selective for orientation, "
                 "direction and motion, but not a representation the cortex lacks -- "
                 "and a coordinating payload, attentional gain and cross-areal "
                 "synchrony",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         fan_out=3,
         note="fan-out at the producer: each pulvinar cell reaches the input layers of "
              "~2-3 cortical areas, recorded here at the upper bound. A second "
              "candidate subcortical route past V1; this edge and the geniculate one "
              "are competing or complementary explanations of the same residual "
              "capacity, not established alternatives."),

    Edge(far("frontal eye field", FRONTAL), here("middle temporal area"),
         carries="the spatial attentional gain signal: an enhancement or suppression "
                 "by location, not a stimulus code",
         role=MODULATORY,
         representation=Representation("gain over locations", TO_DERIVE, EVENT_DRIVEN,
                                       "spatial -- a gain over locations rather than "
                                       "a content map"),
         note="terminating in all cortical layers, and the producer declares the same "
              "lamination on its own output line. Two-ended, and this end is the typed "
              "one. The same phrasing is claimed by a third structure in a fourth "
              "file: V1's file declares V4 receiving 'frontal eye field, terminating "
              "in all cortical layers -- the spatial attentional gain' with no "
              "matching output anywhere in the frontal file. The pair separates "
              "cleanly -- this edge is two-ended and V4's is producer-less -- so the "
              "shared wording is not evidence that the two are one edge mis-copied; "
              "it is evidence that one general description was instantiated at two "
              "consumers and declared back at only one. Owed at the source: establish "
              "the V4 limb at the producer, or withdraw it there."),

    Edge(here("medial superior temporal area"),
         here("middle temporal area", "1"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="feedback"),

    Edge(class_endpoint("posterior parietal areas"),
         here("middle temporal area", "1"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="feedback, and the endpoint is a class that does not resolve: none of "
              "the posterior parietal file's five entries declares an output here, and "
              "the supramarginal gyrus declares traffic in the opposite direction "
              "only"),

    Edge(here("middle temporal area"), here("medial superior temporal area"),
         carries="integrated global motion: local component motions resolved into a "
                 "single pattern-motion direction, speed, motion-in-depth, and "
                 "figure-ground from motion opponency",
         representation=Representation("integrated motion vectors", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC),
         note="the transformation is local vectors in, one vector per region out, so "
              "any equation here reduces cardinality along the spatial axis rather "
              "than merely re-weighting it"),

    Edge(here("middle temporal area"),
         class_endpoint("smooth-pursuit oculomotor circuitry"),
         carries="target velocity as a pursuit command",
         representation=Representation("target velocity", TO_DERIVE, EVENT_DRIVEN,
                                       TO_DERIVE),
         note="the endpoint is a class and names no region, and the frontal lobe file "
              "contains no pursuit entry at all"),

    Edge(here("middle temporal area"), here("ventral intraparietal area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="owed at this end and typed at the consumer's, which declares motion in "
              "eye-centred coordinates. The two ends disagree -- one owed, one typed "
              "-- and neither cites a source for the payload, so the producer does not "
              "know what it sends."),

    Edge(here("middle temporal area"),
         here("lateral intraparietal area", "ventral subdivision"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="owed at this end and typed at the consumer's, which declares visual "
              "motion, retinotopic, reaching the ventral subdivision and not the "
              "dorsal one"),

    Edge(here("middle temporal area"), far("V1", VISUAL, "layer 1"),
         carries="contextual and attentional modulation, figure-ground and "
                 "border-ownership context, attentional gain; not a new stimulus code",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       RETINOTOPIC),
         note="feedback, principally onto layer 1 and also 2, 5 and 6. Descending "
              "input avoids layer 4, which is what distinguishes a feedback edge from "
              "a forward one at the receiving end. On layer 1 it terminates on apical "
              "tufts belonging to cells housed in layers 2/3 and 5, mainly on spines. "
              "Declared inside a four-source class, so which of the four contributes "
              "which part of the payload is owed."),

    Edge(here("middle temporal area"), far("V2", VISUAL, "layer 1"),
         carries=OWED,
         role=MODULATORY,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="feedback, owed at both ends: the consumer declares the edge inside a "
              "three-source feedback class line and types no limb of it"),

    # --- medial superior temporal area ----------------------------------
    # The first cortical edge in the file on which a non-visual payload arrives into a
    # visual area, and the whole function of the stage depends on it: without it, optic
    # flow cannot be attributed to self-motion rather than to the world.  Its route is
    # contested and the evidence runs against it.
    Edge(unstemmed("vestibular nuclei by way of the thalamus"),
         here("medial superior temporal area", "dorsal division"),
         carries="the computed self-motion estimate, not the raw transducer lines",
         representation=Representation(
             "self-motion estimate",
             "velocity-like temporal dynamics -- the form that combines with visual "
             "motion rather than with acceleration",
             EVENT_DRIVEN,
             "head- or body-centred; explicitly not an attitude signal, modulating "
             "during self-motion and not with orientation relative to gravity"),
         note="the tilt-versus-translation ambiguity is already resolved before this "
              "edge, by combining otolith and canal signals, described in the Purkinje "
              "cells of the cerebellar nodulus and uvula. Naming the upstream stages "
              "is owed. The route is " + CONTESTED + ": there is reported to be a lack "
              "of anatomical evidence for a vestibular projection here through the "
              "thalamus, and latency orders the three areas parieto-insular vestibular "
              "cortex -> ventral intraparietal area -> this area, with this area "
              "showing the longest latencies -- the opposite of what a direct thalamic "
              "input predicts. The thalamic file carries no relay for the route, and "
              "the cortical alternative requires a ventral intraparietal -> this area "
              "edge that neither entry declares. So the line has a well-typed payload "
              "and no established producer."),

    Edge(far("frontal eye field", FRONTAL, "pursuit area"),
         here("medial superior temporal area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="reciprocal. That area carries visual, vestibular and combined heading "
              "tuning of its own, so it is not simply downstream. The far end declares "
              "two output lines attributing edges to a pursuit sub-element and naming "
              "this file's structures -- but the pursuit area is not a heading and not "
              "an entry there: it appears only as a sub-element attribution, with no "
              "count, no shape and no inputs of its own. So the far end names the "
              "sub-element without describing it, and the heading tuning this line "
              "attributes to the area has nowhere to live at the producer. Owed at the "
              "source: give the pursuit area an entry, or state that the frontal eye "
              "fields entry covers it and carry the tuning there."),

    Edge(class_endpoint("extraretinal eye-movement / efference copy"),
         here("medial superior temporal area"),
         carries="the eye's own velocity command -- what the system did, so that the "
                 "flow it caused can be subtracted",
         representation=Representation("eye velocity command", TO_DERIVE, EVENT_DRIVEN,
                                       "eye"),
         note="source region still not named"),

    Edge(here("medial superior temporal area"), here("ventral intraparietal area"),
         carries="global optic-flow structure plus heading and the self/object "
                 "attribution",
         representation=Representation("optic-flow structure; heading", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       "mainly eye-centred for the visual heading"),
         note="the two payloads are not symmetrically read out downstream: "
              "microstimulation here biased heading judgements made from optic flow "
              "but did not significantly affect vestibular heading judgements, even "
              "though single cells carry both cues. So an output array carrying "
              "'heading' as one quantity would assert a symmetry the evidence "
              "refuses."),

    Edge(here("medial superior temporal area"),
         far("medial intraparietal area", PARIETAL),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("medial superior temporal area"),
         far("supramarginal gyrus", PARIETAL),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("medial superior temporal area"),
         here("lateral intraparietal area", "ventral subdivision"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="owed at this end; the consumer declares optic flow, retinotopic, with "
              "the same ventral selectivity asserted -- but the tracer result is not "
              "separated between this source and the middle temporal one, so which of "
              "the two it was shown for is owed"),

    Edge(here("medial superior temporal area"),
         far("frontal eye field", FRONTAL, "pursuit area"),
         carries="pursuit and gaze-target velocity",
         representation=Representation("gaze-target velocity", TO_DERIVE, EVENT_DRIVEN,
                                       TO_DERIVE),
         note="reciprocal, and the producer's reciprocal limb is declared there from "
              "the same sub-element and is untyped, so this end carries the payload "
              "for both directions"),

    # --- ventral intraparietal area -------------------------------------
    Edge(far("V3", VISUAL), here("ventral intraparietal area"),
         carries="dynamic form, contour bound to direction of motion",
         representation=Representation("dynamic form", TO_DERIVE, EVENT_DRIVEN,
                                       RETINOTOPIC)),

    Edge(unstemmed("parieto-insular vestibular cortex"),
         here("ventral intraparietal area"),
         carries="the computed self-motion estimate",
         representation=Representation(
             "self-motion estimate", TO_DERIVE, EVENT_DRIVEN,
             "intermediate between head- and body-centred, which this stage completes "
             "to body-centred"),
         note="the vestibular frame here is further hybrid and gaze-dependent: this "
              "area shows either a body-centred or a world-centred frame depending on "
              "gaze direction -- a flexible switch between two frames, not a fixed "
              "one. A frame that is a function of another input's value has no "
              "representation in the shared vocabulary, where the frame is a string."),

    # The variable the gain field multiplies by, and therefore the thing that makes the
    # transform possible.  Its source region is not named, so the mechanism the entry
    # rests on has no declared input.  And the transform is stated as modulation by eye
    # AND head position, while no head-position line is declared anywhere.
    Edge(class_endpoint("eye-position / efference copy"),
         here("ventral intraparietal area"),
         carries="current eye position: the variable the gain field multiplies by, and "
                 "therefore the thing that makes the transform possible",
         representation=Representation("eye position", TO_DERIVE, EVENT_DRIVEN,
                                       "eye-in-head"),
         note="source region not named -- " + OWED + ". The co-multiplicand, head "
              "position, has no input line at all."),

    Edge(class_endpoint("head-position (head-on-body)"),
         here("ventral intraparietal area"),
         carries="head position relative to the body: the second of the two variables the "
                 "gain field multiplies by",
         representation=Representation("head position", TO_DERIVE, EVENT_DRIVEN, "body"),
         note="REQUIRED AND UNDECLARED at the rung above until this pass: the Function "
              "field names eye AND head position as the multiplicands and the Inputs "
              "field supplied only the first. Head-on-body is a separately measured "
              "variable in this area and not a loose synonym for gaze -- tuning has been "
              "measured against it as its own axis, with the head free to rotate and its "
              "angular position tracked, independently of eye-in-head. Producer not named "
              "anywhere; owed at the source, where a neck-proprioceptive candidate is "
              "recorded."),

    Edge(class_endpoint("somatosensory (facial / head tactile)"),
         here("ventral intraparietal area"),
         carries="touch location",
         representation=Representation("touch location", TO_DERIVE, EVENT_DRIVEN,
                                       "skin-surface"),
         note="strongly bimodal visual-plus-tactile, with facial and head tactile "
              "receptive fields aligned to visual ones -- peripersonal and defensive "
              "space"),

    Edge(here("ventral intraparietal area"),
         far("premotor cortex", FRONTAL, "F4"),
         carries="object location and motion in head- and body-centred coordinates, "
                 "peripersonal and defensive space",
         representation=Representation("object location and motion", TO_DERIVE,
                                       EVENT_DRIVEN, HEAD_AND_BODY),
         note="the payload change at this stage is the coordinate frame and nothing "
              "else: the same objects go in and come out, re-expressed in a frame the "
              "body can act in. That is what the gain fields buy and it is the reason "
              "the entry exists. The far end declares the edge and the sub-element "
              "both, one of three parietal inputs there written by terminating "
              "sub-element, alongside the anterior intraparietal area on F5 and the "
              "medial intraparietal area on F2 -- so the F-numbering is the convention "
              "in use there. That end is untyped, and the coordinate frame this line "
              "makes its whole justification exists only here."),

    Edge(here("ventral intraparietal area"), here("lateral intraparietal area"),
         carries="body-centred locations for prioritisation",
         representation=Representation("locations", TO_DERIVE, EVENT_DRIVEN,
                                       BODY_CENTRED),
         note="the two ends disagree by one frame: the consumer declares body- AND "
              "head-centred locations"),

    Edge(here("ventral intraparietal area"),
         far("medial intraparietal area", PARIETAL),
         carries="body-centred locations for reach",
         representation=Representation("locations", TO_DERIVE, EVENT_DRIVEN,
                                       BODY_CENTRED),
         note="the consumer's declaration is the vaguer"),

    Edge(here("ventral intraparietal area"),
         far("anterior intraparietal area", PARIETAL),
         carries="head- and body-centred location and motion for grasp",
         representation=Representation("location and motion", TO_DERIVE, EVENT_DRIVEN,
                                       HEAD_AND_BODY),
         note="the one edge out of this entry whose two ends agree, in the same words"),

    Edge(here("ventral intraparietal area"),
         far("frontal eye field", FRONTAL, "pursuit area"),
         carries="heading in some frame -- " + OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="reciprocal; the sub-element is named at the far end and not described "
              "there"),

    # --- lateral intraparietal area -------------------------------------
    Edge(unstemmed("pulvinar"), here("lateral intraparietal area"),
         carries="the two-part pulvinar payload",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="which subdivision it reaches is " + UNKNOWN + ", and given that every "
              "other visual input here is subdivision-specific, that is " + OWED),

    Edge(class_endpoint("ventral-stream visual areas"),
         here("lateral intraparietal area", "dorsal subdivision"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the endpoint is a class the visual file does not resolve: none of the "
              "four ventral-stream entries declares an output here, and the one "
              "candidate found runs the other way on the subdivision"),

    # The payload whose correctness condition the shared vocabulary cannot hold.  It is
    # only useful if it arrives before the eye moves -- an ordering constraint against
    # an event outside this section, which is correctness and not performance.  The
    # latency field carries seconds; this requirement is a predicate over two events.
    Edge(far("frontal eye field", FRONTAL),
         here("lateral intraparietal area"),
         carries="corollary discharge of the saccade command, relayed from the "
                 "superior colliculus through the thalamus: the eye is about to move, "
                 "by this vector",
         representation=Representation(
             "an impending eye-movement vector", TO_DERIVE,
             "event-driven, and the event is a saccade about to happen",
             "eye-movement vector"),
         note="DEADLINE: usefulness depends on arriving before the movement, a latency "
              "requirement stated without a latency, and there is no field for a "
              "predicate over two events. The gap in the route is located precisely, "
              "at three files at once. The producer states the path runs through the "
              "mediodorsal thalamus. " + BRAINSTEM + "'s superior colliculus declares "
              "'-> frontal eye field and lateral intraparietal area, reciprocally via "
              "the thalamus' and types it in this line's own words. And " + THALAMUS +
              "'s mediodorsal entry names the frontal eye fields among its five "
              "cortical outputs and declares no intraparietal target of any kind. So "
              "three files declare a route through a relay, the relay is named by one "
              "of them, and the nucleus named declares only the first leg. The gap is "
              "the second leg and it is at the nucleus, not at either cortical end. "
              "Owed at the source, in " + THALAMUS + "."),

    Edge(far("prefrontal area 46", FRONTAL), here("lateral intraparietal area"),
         carries="top-down goal relevance -- a weighting, not a stimulus",
         role=MODULATORY,
         representation=Representation("a weight over locations", TO_DERIVE,
                                       EVENT_DRIVEN, NO_FRAME),
         note="an update that treated this as another content line would rank "
              "locations by how much attention they already had"),

    Edge(class_endpoint("auditory saccade-target signals"),
         here("lateral intraparietal area"),
         carries="sound location converted into eye-centred coordinates, a supramodal "
                 "target, which is why this map can rank a sound against a sight",
         representation=Representation("sound location", TO_DERIVE, EVENT_DRIVEN,
                                       EYE_CENTRED),
         note="the converting stage is not named anywhere, and it is the interesting "
              "part of the edge"),

    Edge(far("angular gyrus", PARIETAL), here("lateral intraparietal area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the producer declares nothing"),

    Edge(far("supramarginal gyrus", PARIETAL), here("lateral intraparietal area"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the producer declares the opposite direction instead"),

    # The two internal edges, and they are not one reciprocal link.  Retrograde tracing
    # found ventral -> dorsal point-to-point, described as sensory-like, one location
    # talking to its counterpart; and dorsal -> ventral widespread, not point-to-point,
    # one location talking to many.  A topographic forward limb and a divergent return
    # limb are the anatomy of a map being read out against a broadcast, not of two
    # copies of one map.  Different arities and different shapes.
    Edge(here("lateral intraparietal area", "ventral subdivision"),
         here("lateral intraparietal area", "dorsal subdivision"),
         carries="point-to-point, described as sensory-like: one location talking to "
                 "its counterpart",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       RETINOTOPIC),
         note="offered as part of the intrinsic circuit underlying the observation "
              "that a cell's motor response field is spatially distinct from its "
              "sensory receptive field -- a payload change inside one entry"),

    Edge(here("lateral intraparietal area", "dorsal subdivision"),
         here("lateral intraparietal area", "ventral subdivision"),
         carries="widespread, not point-to-point: one location talking to many",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       RETINOTOPIC),
         note="the divergent return limb; a broadcast rather than a second copy of the "
              "map"),

    Edge(here("lateral intraparietal area", "ventral subdivision"),
         far("superior colliculus", BRAINSTEM, "intermediate and deep layers"),
         carries="the priority map: one scalar per retinotopic location, peak "
                 "specifying the next saccade target",
         representation=Representation("one scalar per location", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       RETINOTOPIC + ", deliberately modality-free"),
         note="what it has thrown away -- colour, identity, pitch -- is as important "
              "as what it keeps, so a design carrying modality tags alongside the "
              "scalar would undo the structure's function, which is to make a sound "
              "and a sight comparable. The ventral subdivision carries this edge and "
              "the dorsal one does not, so a consumer reading 'the lateral "
              "intraparietal area projects to the colliculus' is reading half the "
              "area."),

    Edge(here("lateral intraparietal area"), far("frontal eye field", FRONTAL),
         carries="the priority map",
         representation=Representation("one scalar per location", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC),
         note="two-ended and agreeing at the far end, which is untyped. This limb and "
              "the corollary-discharge limb inbound are the clearest case in the "
              "section of a reciprocal edge whose two limbs are not the same edge: "
              "different payloads, different arities, different routes, and one of the "
              "two is direct while the other is relayed. Recording the pair as "
              "reciprocal or as two-ended says nothing about any of that, which is why "
              "the two limbs are written separately."),

    Edge(here("lateral intraparietal area"), far("prefrontal area 46", FRONTAL),
         carries="the priority map",
         representation=Representation("one scalar per location", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC),
         note="the far end names area 46 from its own side in both directions"),

    Edge(here("lateral intraparietal area"),
         far("anterior intraparietal area", PARIETAL),
         carries="the priority map",
         representation=Representation("one scalar per location", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC)),

    Edge(here("lateral intraparietal area"), far("angular gyrus", PARIETAL),
         carries="the priority map",
         representation=Representation("one scalar per location", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC)),

    Edge(here("lateral intraparietal area"),
         unstemmed("parahippocampal temporal area TF"),
         carries="the priority map",
         representation=Representation("one scalar per location", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC)),
)

# --------------------------------------------------------------------------
# What the section's stated functions require and no edge supplies.
#
# Three stated functions here have no declared substrate, and it is the same shape three
# times: the Function field names a mechanism and the Internal-structure field cannot
# show it.  That is a different defect from a missing payload -- the edge is not merely
# untyped, it is absent while being required.
#
# Left absent and named rather than invented, because a well-formed invented edge reads
# exactly like a derived one.
# --------------------------------------------------------------------------

OWED_INTERNAL_EDGES = (
    ("middle temporal area",
     "an edge crossing the direction map. Integrating local component motions into one "
     "pattern motion requires signal to cross direction columns, since the components "
     "and the resolved pattern have different directions by construction. The axis "
     "exists; nothing connects positions along it."),
    ("ventral intraparietal area",
     "the edge delivering eye and head position to the cells carrying the sensory "
     "receptive field, which the gain-field mechanism requires. Owed at its source, and "
     "the gap is two lines wide: neither multiplicand has a named producer."),
    ("lateral intraparietal area",
     "within-map inhibitory edges between separated locations, which selection by "
     "competition requires. The divisional edges are between subdivisions, not across "
     "the map."),
)

# --------------------------------------------------------------------------
# Reporting.  Every figure below is recomputed from the counts above rather than
# transcribed.
# --------------------------------------------------------------------------


def realisation_gap() -> str:
    """Derived against realised, and here they are equal for a reason worth stating.

    Every width in this section is the 16-bit ceiling, which is a container boundary by
    construction, so nothing is lost to padding.  A zero gap and an unmeasured fan-in
    are the same fact stated twice.
    """
    out = []
    for s in STRUCTURES:
        p = s.populations[0]
        d, r = p.parameter_bytes, p.realised_bytes
        out.append(f"  {s.name[:34]:34} {p.count/1e6:5.0f}M x {p.threshold_bits:2d} "
                   f"bits = {d/1e6:6.2f} MB, realised {r/1e6:6.2f} MB, "
                   f"gap {100*(r-d)/d:.0f}%")
    return "\n".join(out)


def counts_close_and_shapes_do_not() -> str:
    """The section's inversion, stated as the two counts that matter.

    Sizing is what this section does best and it is the least of what the code needs: a
    count sizes a population, it does not size an array.
    """
    priced = sum(1 for s in STRUCTURES
                 for p in s.populations if p.parameter_bytes is not None)
    populations = sum(len(s.populations) for s in STRUCTURES)
    open_axes, total_axes = 0, 0
    for s in STRUCTURES:
        for a in s.axes:
            total_axes += 1
            if a not in ("lamina",):
                open_axes += 1
    return (f"  populations priced           : {priced} of {populations}\n"
            f"  structures whose count partitions to sub-elements : "
            f"{sum(1 for s in STRUCTURES if s.partitions)} of {len(STRUCTURES)}\n"
            f"  axes with a stated extent    : 4 of {total_axes}  "
            f"(the lamina axis, at all four structures)\n"
            f"  axes underived or unknown    : {open_axes} of {total_axes}")


def merged_by_a_uniform_interval() -> str:
    """Edges this section would lose to a uniform update interval.

    The direct route from V1 layer 4B carries direction and disparity on a fast few-hop
    route, and the payload is the same as the indirect routes carry while the latency is
    not.  So the only field distinguishing them reads None, and an interval coarse
    enough to make them equal does not approximate this structure -- it deletes one of
    its inputs.  This is a correctness consequence of the scheduling decision, not a
    performance one.
    """
    into_mt = [e for e in EDGES
               if e.target.name == "middle temporal area" and e.target.sub == "4"]
    out = [f"  {len(into_mt)} edges terminate on the middle temporal area's layer 4:"]
    for e in into_mt:
        out.append(f"    {e.source.name[:30]:30} latency "
                   f"{'None' if e.latency_s is None else e.latency_s}")
    out.append("  their payloads overlap on direction and disparity; the direct route's")
    out.append("  distinguishing property is that it arrives earlier, and no field")
    out.append("  in this file carries that")
    return "\n".join(out)


def deadline_edges() -> str:
    """Edges whose correctness is an ordering constraint rather than a duration.

    An edge carries a latency in seconds.  This one's requirement is a predicate over
    two events -- before the eye moves -- and there is no field for it.
    """
    rows = [e for e in EDGES if e.note.startswith("DEADLINE")]
    out = [f"  edges with an ordering constraint : {len(rows)}"]
    for e in rows:
        out.append(f"    {e.source.name[:28]:28} -> {e.target.name[:34]:34}")
        out.append(f"      requirement: before the eye moves; "
                   f"latency field: "
                   f"{'None' if e.latency_s is None else e.latency_s} s")
    return "\n".join(out)


def modulatory_lines() -> str:
    """Lines that set gain and add no content, which a summing update would misread."""
    rows = [e for e in EDGES if e.role == MODULATORY]
    out = [f"  modulatory edges : {len(rows)}"]
    for e in rows:
        out.append(f"    {e.source.name[:30]:30} -> {e.target.name[:32]:32}")
    return "\n".join(out)


def frames_into(structure_name: str) -> str:
    """Every distinct coordinate frame arriving at one structure.

    A consumer inheriting a single frame from the structure rather than from the line
    is wrong once per distinct frame beyond the first, and the ventral intraparietal
    area is where that bites: its whole function is to change one of them, and not the
    others.

    The disparity is not between populations.  In this area vestibular heading is
    body-centred, visual heading from optic flow is eye-centred, facial tactile
    receptive fields are head-centred, and auditory receptive fields lie on a continuum
    between eye- and head-centred -- and neurons tested with more than one protocol carry
    more than one frame, so a single cell holds several.  That is why the frame is
    declared on the line and never on the structure.
    """
    frames = []
    for e in EDGES:
        if e.target.name == structure_name:
            f = e.representation.frame
            if f not in frames:
                frames.append(f)
    out = [f"  {structure_name}: {len(frames)} distinct frames on its input lines"]
    for f in frames:
        out.append(f"    {f[:88]}")
    return "\n".join(out)


def unpartitioned() -> str:
    """Structures naming sub-elements their count does not divide among.

    An edge terminating on one of these names a place whose extent is unknown, which
    blocks allocation rather than description.
    """
    out = []
    for s in STRUCTURES:
        counts = [p.count for p in s.populations if p.count]
        total = f"{sum(counts):,}" if counts else TO_DERIVE
        landing = sum(1 for e in EDGES if e.target.name == s.name and e.target.sub)
        out.append(f"  {s.name[:34]:34} {len(s.subelements):2d} sub-elements, "
                   f"one count of {total:>12}, {landing} edges land on a sub-element")
    return "\n".join(out)


def owed_internal_edges() -> str:
    out = []
    for structure, what in OWED_INTERNAL_EDGES:
        out.append(f"  {structure}")
        out.append(f"    {what}")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report(STRUCTURES, f"Brain {STEM}"))
    print()
    print("derived against realised, and why the gap is zero:")
    print(realisation_gap())
    print()
    print("the section's inversion -- counts close, shapes do not:")
    print(counts_close_and_shapes_do_not())
    print()
    print("what a uniform update interval would merge:")
    print(merged_by_a_uniform_interval())
    print()
    print("ordering constraints the latency field cannot carry:")
    print(deadline_edges())
    print()
    print("lines that set gain and add no content:")
    print(modulatory_lines())
    print()
    print("coordinate frames arriving at one structure:")
    print(frames_into("ventral intraparietal area"))
    print()
    print(edge_report(EDGES))
    print()
    print("sub-elements without a partition of the count:")
    print(unpartitioned())
    print()
    print("stated functions with no declared substrate:")
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
