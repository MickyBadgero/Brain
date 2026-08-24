"""Brain — 01 visual pathway: the ventral line, retina to inferotemporal cortex.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

Colour is computed in the eye and not downstream.  Three cone classes are read out by
three ganglion classes with opponency already formed, so the bus leaving the retina
carries three chromatic classes rather than one intensity signal, and any stage
downstream that reads hue is reading this.

Counting basis is not uniform along this line.  The retina and optic nerve are
counted per eye, the chiasm's through-traffic both eyes combined, and everything from
the lateral geniculate nucleus onward per hemisphere.  The chiasm is where the basis
changes: it takes two per-eye buses in and emits two per-hemisphere ones, and it is
where each optic tract begins carrying the contralateral hemifield of both eyes
rather than one whole eye.

The line is not a feedforward chain.  The corticothalamic projection from V1 back to
the lateral geniculate nucleus supplies about 30% of that nucleus's synapses, a
descending arm outnumbering the ascending drive it regulates, and every cortical
stage here returns a feedback edge to the stage below it.  Every structure is
therefore live from the outset: a stage brought up later would leave those loops
open, and an open loop is not a loop.

Two edges here are not projections.  The retina's input is light, photon flux imaged
on the photoreceptor sheet, an optical arrival whose fan-in is not applicable rather
than underived.  The optic chiasm has no synapse, so its edges are routing statements
and their fan-in and fan-out are none.  Neither takes conduction-plus-synaptic time,
and both still take real time.

Every edge latency on this line is underived and reads None.  None is not a licence
to substitute zero or a uniform interval.  One timing fact exists and it is internal
rather than an edge: a subpopulation of geniculate relay cells, the lagged class,
carries a delay introduced by triadic inhibition, with slower-rising and more
sustained responses than the non-lagged class.
"""

from __future__ import annotations

from Brain_config import (
    BOTH_EYES, CLASS_ENDPOINT, CONTESTED, DRIVER, EVENT_DRIVEN, Edge, Endpoint,
    GRADED, MODULATORY, NOT_APPLICABLE, NO_FRAME, OWED, PER_EYE, PER_HEMISPHERE,
    PER_SIDE, Population, ROUTING, Representation, Structure, THRESHOLD_GATE,
    TO_DERIVE, TRANSDUCER, TRANSMISSION, allocate, class_endpoint, edge_report,
    emission, fan_in_map, far, here, learn, no_entry, representation_report,
    schedule, sizing_report,
)

STEM = "01_visual_pathway"

# Far files reached from this section.  The stem, never the number: the number fixes
# data-flow position and the section names the structure, and a bare number goes
# silently wrong the moment a file is split, merged or renumbered.
AUDITORY = "02_auditory_pathway"
DORSAL = "04_dorsal_visual_parietal_stream"
PARIETAL = "06_posterior_parietal"
ANTERIOR_TEMPORAL = "07_anterior_temporal_lobe"
MEDIAL_TEMPORAL = "08_medial_temporal_lobe"
BASAL_GANGLIA = "09_basal_ganglia"
FRONTAL = "11_frontal_lobe"
THALAMUS = "12_thalamus"
BRAINSTEM = "14_brainstem_midbrain_hypothalamus"

RETINOTOPIC = "retinotopic"
MONOCULAR = "retinotopic, monocular"
BINOCULAR = "retinotopic, binocular"

# --------------------------------------------------------------------------
# Structures.
#
# Counts and their basis are the architecture's.  Where a count does not divide
# among the sub-elements the entry names, `partitions` is False, and an array for
# one of those sub-elements cannot be sized however well the sub-element is
# described.  The geniculate nucleus is the one structure here whose count does
# partition, and it closes against its own headline.
# --------------------------------------------------------------------------

RETINA = Structure(
    "retina",
    (
        # A ganglion cell's fan-in is not the photoreceptor count: convergence onto
        # it runs through the bipolar cells and is not recorded.
        Population("ganglion cells", THRESHOLD_GATE, PER_EYE, 1_200_000, None),
        # A transducer stores no threshold and the log2 cost does not apply.
        Population("photoreceptors", TRANSDUCER, PER_EYE, 97_000_000, None,
                   sign_inverting=True,
                   note="hyperpolarise to light and release more transmitter in the "
                        "dark; these cells do not spike, so hyperpolarising is not "
                        "inhibiting and hyperpolarisation is the excitatory response"),
        # Horizontal cells build the antagonistic surround in space, amacrine cells
        # build the transient response in time: two lateral populations acting on
        # different axes.  All three respond with graded membrane potential and
        # generate no action potential, and no count is recorded for any of them.
        Population("horizontal / bipolar / amacrine", GRADED, PER_EYE, None, None,
                   note="store is not established; neither zero nor log2(fan-in)"),
    ),
    subelements=("photoreceptors", "horizontal cells", "bipolar cells",
                 "amacrine cells", "ganglion cells"),
    rank=3,
    axes=("sub-element", "H", "W"),
    partitions=False,
)
# The retinal grid is a space-variant sampling lattice and not a raster: peak foveal
# cone density is ~199,000/mm2, falling to ~32,200 / ~19,300 / ~11,600 per mm2 at 0.5
# / 1.0 / 1.5 mm out.  H and W are underived because no retinal surface area is
# recorded, and the eccentricity function is the correspondence rule the ganglion
# output edge needs.

OPTIC_CHIASM = Structure(
    "optic chiasm",
    # A fibre tract: no neurons, no synapse, no transform, no state.  Its two
    # sub-structures are parallel channels rather than a circuit, sorted by the line
    # of decussation, which is normally aligned with the fovea and is a
    # developmental variable rather than a structural given.  Crossed to uncrossed is
    # about 53:47 in the neurotypical human, a consequence of the orbits having
    # rotated forward: total decussation is the lateral-eyed arrangement, and the
    # slight majority for crossing follows from the nasal retina being the larger
    # sector once the boundary sits at the fovea.
    (Population("fibres", TRANSMISSION, BOTH_EYES, 0, None,
                note="through-traffic ~2M fibres both eyes combined, of which about "
                     "5% are bound for structures other than the two geniculate "
                     "nuclei"),),
    subelements=("crossed bundle", "uncrossed bundle"),
    rank=1,
    axes=("routing index",),
    partitions=False,
)

LGN = Structure(
    "lateral geniculate nucleus",
    (
        # Relay cells fire in burst mode (hyperpolarised, high-gain, nonlinear) or
        # tonic mode (depolarised, near-linear), and the modulatory inputs move them
        # between the two.  The mechanism is a change of transfer function rather
        # than of message, which is why this is a gate and not a wire.
        Population("relay cells", THRESHOLD_GATE, PER_SIDE, 1_770_000, None,
                   note="~75-80% of the nucleus; a lagged subpopulation is delayed "
                        "by triadic inhibition, the only timing datum on this line "
                        "and internal rather than an edge"),
        # The local interneuron releases transmitter from its dendrites without an
        # action potential, so it crosses no threshold.  The ~1.77M headline does not
        # separate the two classes, so the 16-bit bound above covers a population of
        # which a fifth to a quarter is not a threshold gate.
        Population("local interneurons", GRADED, PER_SIDE, None, None,
                   note="~20-25% of the nucleus; store is not established"),
    ),
    subelements=("lamina 1", "lamina 2", "lamina 3", "lamina 4", "lamina 5",
                 "lamina 6", "koniocellular sublayer per lamina"),
    rank=3,
    axes=("lamina", "H", "W"),
    partitions=True,
)
# The one structure on this line whose count partitions to its sub-elements, and it
# closes: magnocellular ~0.22M over laminae 1-2 is ~110,000 per lamina, parvocellular
# ~1.55M over 3-6 is ~387,500 per lamina, summing to ~1.77M against the headline.
# Volumetric density ~104 mm3 over ~1.77M is ~17,019 neurons/mm3.  The eye assignment
# per lamina is owed, so the lamina axis is ordered and not yet labelled.
LGN_MAGNO_PER_LAMINA = 220_000 // 2
LGN_PARVO_PER_LAMINA = 1_550_000 // 4

V1 = Structure(
    "V1",
    # The eyes first combine here, which is what makes this the stage where eye of
    # origin is consumed and discarded.  Orientation, disparity and spatial-frequency
    # tuning are built here and carried by none of the four geniculate inputs, which
    # are together a minority of V1's excitatory synapses; most is intracortical.
    # Fan-in is disputed across a 6.5x range and under log2 that whole range costs 12
    # to 14 bits, so the neuron count is the sensitive term and the fan-in is not.
    (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE,
                300_000_000, 15_000, fan_in_low=2_300, fan_in_high=15_000,
                note="2,300-5,600 measured in macaque V1, ~7,000 as a human cortical "
                     "average, ~15,000 from human synapse and neuron densities"),),
    # Eleven laminar sub-elements against the eight of general cortex: layer 4's
    # sublamination is V1's alone and merges to a single layer 4 at V2.
    subelements=("1", "2", "3", "4A", "4B", "4Ca", "4Cb", "5a", "5b", "6a", "6b"),
    rank=3,
    axes=("sub-element", "H", "W"),
    partitions=False,
)
# Surface density is derivable and the pitch is not.  ~60,000 neurons/mm3 over ~2 mm
# thickness is ~120,000 per mm2 of surface; ~2,600 mm2 x 120,000 = 312M, closing
# independently against the ~280-310M headline.  H and W are underived because V1's
# tangential pitch is not recorded: the cytochrome-oxidase blobs are named with no
# spacing given.
V1_NEURONS_PER_MM2_SURFACE = 120_000
V1_SURFACE_MM2 = 2_600

V2 = Structure(
    "V2",
    # First real composition of visual features: contour integration and illusory
    # contour, angle and junction selectivity, border-ownership and figure-ground,
    # naturalistic texture, and hue.  V1 cannot distinguish naturalistic texture from
    # spectrum-matched noise and V2 can, which is a discriminative constraint on
    # whatever operation is eventually written for it.
    (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE, 210_000_000, None,
                note="scaled from V1 at ~0.715x: ~0.55x V1's density over ~1.3x V1's "
                     "area, so a derived figure rather than a measured one"),),
    # Two orthogonal sub-element axes, not a hierarchy: every stripe class carries
    # the full set of layers and every layer runs through all three stripe classes.
    subelements=("thin stripes", "pale stripes", "thick stripes",
                 "1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=4,
    axes=("lamina", "stripe class", "H", "W"),
    partitions=False,
)
# Two tangential tilings are measured here and they are the only measured pitches on
# this line.  They are not the same tiling and neither is derivable from the other.
# A caution the shape carries: the stripe class is defined by cytochrome-oxidase
# staining in layer 3 while the densest input field is in layer 4, and the two do not
# coincide, so the stripe axis is not in register with the lamina axis and an index
# pair naming both picks out a place that is not well defined.
V2_STRIPE_CYCLE_MM = (3.5, 4.0)
V2_PATCH_MM = (0.211, 0.342)
V2_SURFACE_MM2 = 3_380

V3 = Structure(
    "V3 / V3A",
    # V3 is retinotopic and combines contour and dynamic form with early motion,
    # roughly half its neurons direction-selective.  V3A is a distinct area, strongly
    # motion-responsive in humans, carrying a full contralateral hemifield map
    # against V3's quarter-field.  The stream assignment is genuinely debated, which
    # is why a section named for the ventral stream holds it.
    (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE, None, None,
                note="no clean per-area human count and the boundaries are "
                     "themselves contested; no store can be stated"),),
    subelements=("1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=3,
    axes=("lamina", "H", "W"),
    partitions=False,
)
# The only structure on this line with no store at all: the count is underived, so
# not even the 16-bit ceiling yields a figure.  Whether a repeating compartmentation
# of V1's or V2's kind exists here is not established, so the tangential
# sub-elements are underived as well.  V3 and V3A do not share a coordinate frame --
# quarter-field against full hemifield -- and two different extents cannot be one
# array; the entry is a bundle above and the split is a source decision.

V4 = Structure(
    "V4",
    # Intermediate-complexity vision: curvature and shape-part selectivity, the first
    # explicit part code, above V2's junctions and below inferotemporal objects;
    # colour constancy with the illuminant discounted; texture and surface
    # segmentation at larger scale; and strong attentional gain.  Receptive fields
    # larger than V2's and retinotopy coarser.
    (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE, 50_000_000, None,
                note="best available; the area's boundary is itself contested"),),
    # The tangential sub-elements carry different content and are not a tiling of one
    # population: glob cells' responses track perceptual colour space and retain hue
    # tuning across luminance contrast, interglob cells prefer luminance contrast
    # regardless of hue.
    subelements=("globs", "interglobs",
                 "1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=4,
    axes=("lamina", "module class", "H", "W"),
    partitions=False,
)
# Cytochrome oxidase fails beyond V2, so a V4 module boundary is drawn by the pattern
# of input each module receives -- the same connectivity map a forward operation
# needs and does not have.  The tangential extent therefore cannot be fixed before
# the topology is set.  Module pitch is measured; the surface area is not, so the
# module count does not follow.
V4_MODULE_PITCH_MM = (1.0, 3.0)

IT = Structure(
    "inferotemporal cortex",
    # Top of the ventral "what" stream: object and face identity invariant to
    # position, size, pose and lighting.  This is where the payload stops being a
    # signal and becomes a category, and "the identity of the thing", with no
    # coordinate frame, is a phrase and not a type.  The structural consequence is
    # that no units can be stated on any output edge below.
    (Population("cortical neurons", THRESHOLD_GATE, PER_HEMISPHERE, 120_000_000, None,
                note="order-of-magnitude; no clean primary human count exists. "
                     "Ordinary association cortex at ~20-40,000/mm3, so V1's "
                     "density-derived figure does not carry here"),),
    # Two divisional sub-structures in series, with the complexity gradient
    # continuous rather than stepped: cells needing complex features are already
    # present posteriorly and in V4 in small proportion.  So the division axis is not
    # a pipeline boundary.  Posteriorly the globs of V4 continue and the rank is 4;
    # anteriorly the feature columns have no discrete borders -- a continuous mapping
    # of complex feature space across partially overlapping columns -- and a
    # continuous map has no compartment axis to index, so the rank is 3.
    subelements=("posterior division", "anterior division",
                 "1", "2", "3", "4", "5a", "5b", "6a", "6b"),
    rank=None,
    axes=("lamina", "division (posterior only)", "H", "W"),
    partitions=False,
)

STRUCTURES = (RETINA, OPTIC_CHIASM, LGN, V1, V2, V3, V4, IT)

# --------------------------------------------------------------------------
# Edges.
#
# An edge names its target sub-element wherever the biology terminates on one.  The
# geniculate drive into V1 is four edges onto four different sub-elements and one of
# the four does not reach layer 4 at all, so collapsing them to "-> V1" would delete
# a structural claim about where each channel arrives.
#
# A modulatory edge sets whether, when and how strongly content passes and adds no
# content of its own.  A forward operation that sums all inputs alike treats a gain
# as evidence, which is why the role is carried on the edge rather than inferred.
# --------------------------------------------------------------------------

EDGES: tuple[Edge, ...] = (

    # --- retina ---------------------------------------------------------
    Edge(Endpoint("the world", kind=CLASS_ENDPOINT), here("retina", "photoreceptors"),
         carries="light: photon flux imaged on the photoreceptor sheet",
         role=ROUTING,
         representation=Representation("photon flux", TO_DERIVE, EVENT_DRIVEN,
                                       "retinal image plane, space-variant"),
         note="an optical arrival and not a neural edge; fan-in is " + NOT_APPLICABLE),

    Edge(here("retina", "ganglion cells"), here("optic chiasm"),
         carries="three ganglion channel classes: midget/parvocellular ~80% "
                 "(red-green cone-opponent, sustained, fine detail), "
                 "parasol/magnocellular ~10% (achromatic, transient, coarse), "
                 "bistratified/koniocellular ~8-10% (blue-yellow cone-opponent)",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, space-variant lattice, monocular")),

    Edge(here("retina", "ganglion cells"),
         far("superior colliculus", BRAINSTEM, "stratum griseum superficiale"),
         carries="not more than 10% of ganglion cells, about 6% near the fovea and "
                 "rising with eccentricity, largely a branch off the geniculate line "
                 "rather than an independent population",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),

    Edge(here("retina", "ganglion cells"), no_entry("olivary pretectal nucleus"),
         carries="from broad-field melanopsin-containing luminance detectors",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "broad-field; not retinotopic"),
         note="the nucleus has no entry in any file while its own consumer is "
              "declared, so the two-hop route to the colliculus is declared at both "
              "ends with no entry for the stage between them -- and that stage is "
              "where the transform would live, a broad-field luminance detector's "
              "output not being the same object as a scalar delivered to premotor "
              "layers. Owed at this section's source."),

    Edge(here("retina", "ganglion cells"),
         far("suprachiasmatic nucleus", BRAINSTEM),
         carries="irradiance, a lights-on signal: ambient luminance for clock "
                 "entrainment, by the retinohypothalamic tract, and explicitly not "
                 "spatial vision",
         representation=Representation("irradiance", TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="typed at the consumer and not here. Every other output of this "
              "structure is spatial and nothing at this end marks this one as "
              "different in kind, so a consumer reading only this end would allocate "
              "a retinotopic map for a scalar. Owed at this section's source: the "
              "payload and the tract name."),

    # --- optic chiasm ---------------------------------------------------
    # No synapse, so both edges are routing statements and their fan-in and fan-out
    # are none.  The frame changes and the content does not: this is the only joint
    # on the line where that is true.
    Edge(here("optic chiasm"), here("lateral geniculate nucleus"),
         carries="the same content, unchanged; what changes is which fibres go where",
         role=ROUTING,
         representation=Representation("unchanged from the ganglion bus", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       "hemifield of both eyes, per side"),
         note="a myelinated tract whose g-ratio is unrecorded, so the substrate of "
              "the delay is named and the number is not; this is where a latency "
              "derivation on this line would start"),

    # --- lateral geniculate nucleus -------------------------------------
    # The retina is the sole driver and a small minority of the synapses; the larger
    # non-retinal input is modulatory and adds no content.
    Edge(here("retina", "ganglion cells"), here("lateral geniculate nucleus"),
         carries="the three ganglion classes mapping one-to-one onto the three layer "
                 "classes: parvocellular laminae 3-6 from midget, koniocellular "
                 "sublayers from bistratified, magnocellular laminae 1-2 from parasol",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, MONOCULAR),
         note="~5-10% of this nucleus's synapses and the only driver; classically one "
              "to a few retinal afferents per relay cell, with no human figure"),

    Edge(here("V1", "6a"), here("lateral geniculate nucleus"),
         carries="corticothalamic feedback; no content",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, in register with the relay it gates"),
         note="~30% of synapses, the largest single non-retinal source, and a "
              "descending arm outnumbering the ascending drive it regulates"),

    Edge(far("thalamic reticular nucleus", THALAMUS),
         here("lateral geniculate nucleus"),
         carries="inhibition: a gain and gate control, carrying no content",
         role=MODULATORY,
         representation=Representation("inhibition", TO_DERIVE, EVENT_DRIVEN,
                                       "visual sector of the reticular sheet"),
         note="the producer names the visual sector of that sheet explicitly and both "
              "ends agree the payload carries no content"),

    Edge(class_endpoint("brainstem, cholinergic / noradrenergic / serotonergic"),
         here("lateral geniculate nucleus"),
         carries="arousal state, which sets the relay cells' burst-versus-tonic mode: "
                 "a mode and not a message",
         role=MODULATORY,
         representation=Representation("arousal state", TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="names a class and no structure; needs splitting at the source before "
              "it can carry a stem"),

    Edge(here("lateral geniculate nucleus", "magnocellular laminae 1-2"),
         here("V1", "4Ca"),
         carries="achromatic, point-to-point, still monocular",
         representation=Representation("achromatic", TO_DERIVE, EVENT_DRIVEN, MONOCULAR),
         note="via the optic radiation"),
    Edge(here("lateral geniculate nucleus", "parvocellular laminae 3-6"),
         here("V1", "4Cb"),
         carries="red-green, point-to-point, monocular",
         representation=Representation("red-green", TO_DERIVE, EVENT_DRIVEN, MONOCULAR)),
    Edge(here("lateral geniculate nucleus", "koniocellular sublayers"),
         here("V1", "cytochrome-oxidase blobs of layers 2/3, and layer 1"),
         carries="blue-yellow, monocular",
         representation=Representation("blue-yellow", TO_DERIVE, EVENT_DRIVEN, MONOCULAR),
         note="this edge does not terminate in layer 4 at all"),
    Edge(here("lateral geniculate nucleus",
              "parvocellular and koniocellular collaterals"),
         here("V1", "4A"),
         carries="collateral copy of the parvocellular and koniocellular channels",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, MONOCULAR)),

    Edge(here("lateral geniculate nucleus", "koniocellular"),
         far("middle temporal area", DORSAL),
         carries=OWED,
         representation=Representation(OWED, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="direct, bypassing V1 entirely; mostly koniocellular cells sending "
              "virtually no collateral to V1 and numbering about 10% of the V1 "
              "population that innervates that area. The consumer marks the payload "
              "owed as well and adds that the edge is sufficient to support motion "
              "sensitivity without V1, so both ends agree, and they agree that "
              "neither can type it -- the honest state and not a defect at either end"),

    Edge(here("lateral geniculate nucleus"),
         far("thalamic reticular nucleus", THALAMUS),
         carries="a copy of the outgoing signal, which drives the gate that "
                 "regulates it",
         representation=Representation("as the output it copies", TO_DERIVE,
                                       EVENT_DRIVEN, RETINOTOPIC),
         note="collaterals of the thalamocortical axons"),

    # --- V1 -------------------------------------------------------------
    # The forward output to V2 is segregated by content.  The number of streams is
    # contested -- three, two, or four groupings -- so the edges are stated by target
    # stripe class, the axis all three groupings agree on.
    Edge(here("V1", "cytochrome-oxidase blobs of layers 2/3"),
         here("V2", "thin stripes"),
         carries="cortical colour, single- and double-opponent",
         representation=Representation("cortical colour", TO_DERIVE, EVENT_DRIVEN,
                                       BINOCULAR),
         note="~81% of labelled source cells in patches"),
    Edge(here("V1", "layers 2/3 87%, 4B 10%, 4A 2%, layers 5/6 2%"),
         here("V2", "pale stripes"),
         carries="oriented edge, contour, spatial frequency",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, BINOCULAR),
         note="the richest of the three"),
    Edge(here("V1", "layers 2/3 67%, 4B 23%, 4A 7%, layers 5/6 2%"),
         here("V2", "thick stripes"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, BINOCULAR),
         note="4B is the minority contributor here, which the simple account inverts"),
    Edge(here("V1", "4A"), here("V2", "pale and thick stripes"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, BINOCULAR),
         note="a minor component the three-stream account omits"),
    Edge(here("V1", "layers 5/6"), here("V2", "pale and thick stripes"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, BINOCULAR),
         note="a minor component the three-stream account omits"),

    Edge(here("V1", "4B, predominantly its spiny-stellate class"),
         far("middle temporal area", DORSAL),
         carries=OWED,
         representation=Representation(OWED, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="~76% spiny stellate against ~24% pyramidal, the reverse of the "
              "V2-projecting population and largely separate cells, under ~5% "
              "double-labelled. This end declares no payload and no termination "
              "layer and the consumer declares both -- direction of motion and "
              "binocular disparity, achromatic, coarse-spatial, onto layer 4, on the "
              "fast few-hop route. The producer's end is the deficient one and the "
              "repair is owed at this section's source."),

    Edge(here("V1", "4B"), here("V3 / V3A"),
         carries="motion direction and disparity, achromatic; a major input",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),
    Edge(here("V1"), here("V4"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, central ~6 degrees only"),
         note="direct and sparse"),

    Edge(here("V1", "6b"), far("higher-order thalamus", THALAMUS),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="reaching higher-order nuclei but not the reticular nucleus"),
    Edge(here("V1", "5b"), far("superior colliculus", BRAINSTEM, "superficial layers"),
         carries="retinotopic salience for orienting; not a stimulus code",
         representation=Representation("salience", TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="the termination is named at the consumer and not here. The contest "
              "recorded at the retina turns on this edge: if the colliculus's visual "
              "drive arrives through the geniculate and V1 then this is the edge "
              "carrying it, and the retinotectal one is not"),
    Edge(here("V1", "layer 2"), class_endpoint("lower visual areas"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="a supragranular descending stream distinct from the classical "
              "infragranular one, so layers 2 and 3 are not interchangeable as "
              "origins. Names a class and no structure"),

    # Feedback terminates principally on layer 1, avoiding layer 4, which is what
    # distinguishes a feedback edge at the receiving end.  On layer 1 it lands on
    # apical tufts belonging to cells housed in layers 2/3 and 5.
    Edge(class_endpoint("V2, V3, V4 and the middle temporal area"),
         here("V1", "layer 1, also 2, 5 and 6"),
         carries="contextual and attentional modulation, figure-ground and "
                 "border-ownership context, attentional gain; not a new stimulus code",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, in register"),
         note="a four-source class line and the arity is the defect. The middle "
              "temporal limb resolves into " + DORSAL + " and is typed at that end "
              "only, which records that which of the four contributes which part of "
              "the payload is owed. Splitting this into four named edges is owed at "
              "this section's source"),
    Edge(class_endpoint("posterior and anterior inferotemporal cortex, temporal areas "
                        "TF and TH, occipitotemporal and superior temporal sulcal "
                        "cortex, caudal intraparietal cortex"),
         here("V1", "layer 1"),
         carries=TO_DERIVE,
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="long-range feedback; cortical afferents to V1 are not confined to the "
              "prestriate areas"),

    # --- V2 -------------------------------------------------------------
    Edge(far("auditory parabelt, caudal division", AUDITORY), here("V2"),
         carries="location and motion, typed at the producer",
         representation=Representation("location and motion", TO_DERIVE, EVENT_DRIVEN,
                                       "auditory, not retinotopic"),
         note="an auditory association area writing into secondary visual cortex, and "
              "the one cross-modal line on this line. The producer declares it only "
              "inside a class line whose other far ends mostly have no matching "
              "declaration; this limb is an exception because this end declares it. "
              "Which tangential compartment it reaches is unrecorded and the answer "
              "would matter: thick stripes are the motion and disparity channel, so "
              "thick stripes are the candidate on the two payloads together, and "
              "neither end states it. The frame change from auditory to retinotopic "
              "needs a correspondence and neither end supplies one. Owed at both "
              "sources."),
    Edge(class_endpoint("V4, middle temporal area and higher areas"),
         here("V2", "layer 1"),
         carries=OWED,
         role=MODULATORY,
         representation=Representation(OWED, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="avoiding layer 4. The middle temporal limb is declared at its producer "
              "too and reads owed at both ends there, so this is an edge both ends "
              "agree is untyped rather than one end's omission. The class line's "
              "arity is owed at this section's source"),

    Edge(here("V2", "layers 2/3 of the thin and pale stripes"), here("V4"),
         carries="hue, contour and junction, border-ownership, texture",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="modular and only partly segregated: a V4 injection labels thin stripes "
              "exclusively, or interstripes exclusively, or specific combinations, in "
              "interdigitating clusters 1-3 mm wide. The two streams converge in some "
              "V4 modules and stay separate in others -- the first anatomically "
              "demonstrated cross-stream convergence in the ventral chain"),
    Edge(here("V2", "layers 2/3 of the thick stripes"),
         far("middle temporal area", DORSAL, "layer 4"),
         carries=CONTESTED,
         representation=Representation(CONTESTED, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="the consumer declares binocular disparity, high-speed sensitivity and "
              "the surround suppression underlying motion opponency, achromatic and "
              "retinotopic, and records a substantive disagreement about direction: "
              "this section's source declares direction and disparity, while the "
              "consumer assigns direction to the direct V1 4B route on the strength "
              "of reversible inactivation -- cooling V2 and V3 degrades disparity "
              "tuning disproportionately relative to direction tuning. A causal "
              "inactivation result outranks an unqualified connectivity statement, so "
              "the payload should be disparity-weighted. Recorded and not resolved "
              "here; the payload is the source's. Owed at this section's source"),
    Edge(here("V2", "layers 2/3"), here("V3 / V3A"),
         carries="contour, junction, figure-ground",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),
    Edge(here("V2"), here("inferotemporal cortex", "posterior division"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="direct: a jumping projection that skips V4, declared at both ends"),
    Edge(here("V2", "layer 2 and the infragranular layers"), here("V1", "layer 1"),
         carries="figure-ground and border-ownership context",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, in register")),

    # --- V3 / V3A -------------------------------------------------------
    Edge(far("superior colliculus", BRAINSTEM), here("V3 / V3A"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="di-synaptic, relayed through the pulvinar in " + THALAMUS + ": a "
              "subcortical route into the motion areas that does not pass through V1, "
              "so it is not in register with the V1 and V2 inputs by construction"),
    Edge(class_endpoint("higher dorsal and parietal areas"), here("V3 / V3A", "layer 1"),
         carries=TO_DERIVE,
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="names a class and no structure"),

    Edge(here("V3 / V3A"), far("middle temporal area", DORSAL, "layer 4"),
         carries="dynamic form, contour bound to direction of motion",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="the two ends declare this payload in the same words and it is the only "
              "edge between these two sections of which that is true. The agreement "
              "certifies less than it appears to: it is a check only if the two ends "
              "were written in separate passes, and whether they were is not knowable "
              "from either file"),
    Edge(here("V3 / V3A"), here("V4"),
         carries="contour and dynamic form; payload otherwise " + OWED,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),
    Edge(here("V3 / V3A"), no_entry("V4 transitional area, ventral occipitotemporal "
                                    "area, visually responsive part of temporal area F"),
         carries="contour and dynamic form; payload otherwise " + OWED,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="three endpoints, none with an entry anywhere; the V4 transitional area "
              "is a V3 target and not the ventral posterior area target"),
    Edge(here("V3 / V3A"), no_entry("dorsomedial area, dorsal prelunate area"),
         carries="dynamic form; payload otherwise " + OWED,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="part of a five-endpoint compound line whose split is owed at this "
              "section's source; these two are the source's own extrastriate family "
              "and have no entry anywhere"),
    Edge(here("V3 / V3A"), far("ventral intraparietal area", DORSAL),
         carries="dynamic form, contour bound to direction of motion",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="typed at the far end more fully than the compound line types it here"),
    Edge(here("V3 / V3A"), far("ventral lateral intraparietal area", DORSAL),
         carries="dynamic form; payload otherwise " + OWED,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="the ventral subdivision of the lateral intraparietal area"),
    Edge(here("V3 / V3A"), here("V1", "layer 1"),
         carries=TO_DERIVE, role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),
    Edge(here("V3 / V3A"), here("V2", "layer 1"),
         carries=TO_DERIVE, role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),

    # --- V4 -------------------------------------------------------------
    Edge(far("frontal eye field", FRONTAL), here("V4", "all cortical layers"),
         carries="spatial attentional gain: an enhancement or suppression applied by "
                 "location, and not a stimulus code",
         role=MODULATORY,
         representation=Representation("gain", TO_DERIVE, EVENT_DRIVEN,
                                       "spatial, by location"),
         note="the edge supplying the attentional modulation the function asserts, and "
              "the frontal eye field is the only one of the four attention-implicated "
              "structures shown to modulate visual-cortical firing through its own "
              "direct projection"),
    Edge(far("pulvinar", THALAMUS), here("V4", "middle layers"),
         carries=CONTESTED,
         representation=Representation(CONTESTED, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC),
         note="terminating densely in the middle layers, the layers a forward edge "
              "would use rather than the layer feedback uses. This end declares no "
              "payload and the producer declares one, and the two are in tension: the "
              "producer types it as largely reflecting the cortical driver -- "
              "orientation, direction and motion selectivity, but not a new "
              "representation -- plus attentional gain and cross-areal synchrony. "
              "That is an echo of cortex where the termination recorded here is the "
              "anatomy of a drive. A middle-layer termination is feedforward in form "
              "and a cortically-derived payload is feedback in content, and a "
              "thalamic relay can plausibly be both. Owed: state whether the laminar "
              "heuristic is being relied on to assert a payload, or only to record a "
              "termination pattern"),
    Edge(class_endpoint("inferotemporal cortex and higher ventral areas"),
         here("V4", "layer 1"),
         carries=TO_DERIVE, role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, RETINOTOPIC)),

    Edge(here("V4"), here("inferotemporal cortex", "posterior division"),
         carries="intermediate shape, surface colour with the illuminant discounted, "
                 "segmented surface and texture at large scale",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, coarse")),
    Edge(here("V4"), here("V2", "layer 1"),
         carries=OWED, role=MODULATORY,
         representation=Representation(OWED, TO_DERIVE, EVENT_DRIVEN,
                                       "retinotopic, in register"),
         note="about 75% of its synapses onto spines there"),

    # --- inferotemporal cortex ------------------------------------------
    # Every output below has no units, no range and no coordinate frame, and that is
    # a finding rather than an omission: "the identity of the thing" is a phrase and
    # not a type, and this is the first stage on the line of which that is true.  The
    # outward fan is concentrated at the anterior division rather than spread along
    # the structure.
    Edge(here("V4"), here("inferotemporal cortex",
                          "posterior part of the anterior division"),
         carries="curvature and shape parts, illuminant-discounted surface colour, "
                 "segmented texture",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "coarse retinotopy")),
    Edge(class_endpoint("perirhinal cortex, prefrontal cortex and amygdala"),
         here("inferotemporal cortex", "layer 1"),
         carries=TO_DERIVE, role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="these return limbs close loops whose far ends are outside this section"),

    Edge(here("inferotemporal cortex", "anterior division"),
         no_entry("perirhinal cortex (areas 35 and 36)"),
         carries="the identity code, and the anatomical step by which the ventral "
                 "stream reaches the hippocampal formation",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME)),
    Edge(here("inferotemporal cortex", "anterior division"),
         far("hippocampal formation", MEDIAL_TEMPORAL),
         carries="the identity code as one element of an episode",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME)),
    Edge(here("inferotemporal cortex", "anterior division"),
         far("prefrontal cortex, ventrolateral", FRONTAL),
         carries="identity, for controlled retrieval and selection",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME),
         note="the consumer types no payload, so this end is the only typed one. This "
              "entry declares no orbitofrontal output while the consumer's "
              "orbitofrontal entry declares an input from here, reading '<- the "
              "inferotemporal and temporal cortex, orbital', and that is a separate "
              "structure in that file from the ventrolateral one, so this line does "
              "not cover it. That edge is declared at the consumer and at no "
              "producer. Owed at this section's source: declare it here, or it is "
              "withdrawn there"),
    Edge(here("inferotemporal cortex", "anterior division"),
         far("amygdala", MEDIAL_TEMPORAL),
         carries="identity, for affective evaluation",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME)),
    Edge(here("inferotemporal cortex", "anterior division"),
         far("striatum", BASAL_GANGLIA),
         carries="identity, putting the ventral stream's output into the "
                 "action-selection loop and not only into memory and evaluation",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME)),
    Edge(here("inferotemporal cortex",
              "lower bank of the superior temporal sulcus and the middle temporal gyrus"),
         far("anterior intraparietal area", PARIETAL),
         carries="object identity, invariant to position, size, pose and lighting, "
                 "delivered into the grasp channel",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME),
         note="the only projection out of the ventral stream and into the parietal "
              "lobe in this section. The consumer asserts that this producer declares "
              "nothing on this edge, and that assertion is false: this entry declares "
              "it, so the repair is owed at the consumer. The edge itself is a "
              "candidate and this end should not "
              "read as settled -- the source marks it from a macaque retrograde-tracer "
              "study located by web search, with the abstract only read and no full "
              "paper opened, awaiting verification under the verified-only rule"),
    Edge(here("inferotemporal cortex", "anterior division"),
         far("the distributed conceptual / semantic system, via the temporal pole",
             ANTERIOR_TEMPORAL),
         carries="view-invariant object and face identity",
         representation=Representation("identity, a category", NO_FRAME, EVENT_DRIVEN,
                                       NO_FRAME),
         note="this endpoint names a system and not a structure, and it is inherited "
              "in that form -- a class endpoint owed a split at the source. The "
              "temporal pole is a named region with an entry and the consumer declares "
              "the matching input, so a direct edge has a far end that already declares "
              "it, but writing one here would add a claim the source does not make. "
              "What lies beyond the temporal pole is not this entry's to name: that "
              "consumer's outputs carry the amodal concept onward and it records that "
              "'amodal concept' is a phrase and not a type -- no units, no range, no "
              "coordinate frame -- so the system this edge ultimately serves is "
              "untyped at the only end that can type it"),
)

# --------------------------------------------------------------------------
# Derived sizing -- an independent recomputation from counts and fan-ins, not a
# transcription of the table above the rung.
# --------------------------------------------------------------------------


def lgn_partition_closes() -> str:
    """The one count on this line that divides among its sub-elements."""
    magno, parvo = 220_000, 1_550_000
    return (f"  magnocellular {magno:,} over laminae 1-2 = {LGN_MAGNO_PER_LAMINA:,} "
            f"per lamina\n"
            f"  parvocellular {parvo:,} over laminae 3-6 = {LGN_PARVO_PER_LAMINA:,} "
            f"per lamina\n"
            f"  sum {magno + parvo:,} against the ~1,770,000 headline")


def v1_surface_closes() -> str:
    """Surface density closes independently against the headline count."""
    derived = V1_SURFACE_MM2 * V1_NEURONS_PER_MM2_SURFACE
    return (f"  {V1_SURFACE_MM2:,} mm2 x {V1_NEURONS_PER_MM2_SURFACE:,} per mm2 = "
            f"{derived/1e6:.0f}M against the ~280-310M headline")


def v1_realisation_gap() -> str:
    """The derived threshold width against the width a machine integer takes.

    No integer type is 12 or 14 bits wide.  Bit-packing closes the gap and costs
    unpacking on every read; padding spends memory instead.  That trade is this
    file's to record and it is never a reason to shrink anything.
    """
    p = V1.populations[0]
    lo, hi = p.threshold_bits_range
    out = []
    for bits in range(lo, hi + 1):
        derived = p.count * bits / 8
        realised = p.count * 16 / 8
        out.append(f"  {bits} bits derived = {derived/1e6:6.1f} MB, "
                   f"uint16 realised = {realised/1e6:6.1f} MB, "
                   f"gap {100*(realised-derived)/derived:4.1f}%")
    return "\n".join(out)


def unpartitioned() -> str:
    """Structures naming sub-elements their count does not divide among.

    An edge terminating on one of these names a place whose extent is unknown, which
    blocks allocation rather than description.
    """
    out = []
    for s in STRUCTURES:
        if s.subelements and not s.partitions:
            counts = [p.count for p in s.populations if p.count]
            total = f"{sum(counts):,}" if counts else TO_DERIVE
            landing = sum(1 for e in EDGES
                          if e.target.name == s.name and e.target.sub)
            out.append(f"  {s.name:28} {len(s.subelements):2d} sub-elements, "
                       f"one count of {total:>13}, {landing} edges land on a "
                       f"sub-element")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report(STRUCTURES, f"Brain {STEM}"))
    print()
    print("counts that close independently:")
    print(lgn_partition_closes())
    print(v1_surface_closes())
    print()
    print("V1 threshold width, derived against realised:")
    print(v1_realisation_gap())
    print()
    print(edge_report(EDGES))
    print()
    print("sub-elements without a partition of the count:")
    print(unpartitioned())
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
