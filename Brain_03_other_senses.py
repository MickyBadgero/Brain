"""Brain — 03 other senses: olfaction, taste, and the vestibular apparatus.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

These three senses break the template the first two sections were built on.
Olfaction reaches cortex with no thalamic relay and therefore no thalamic gate -- the
only sense that does.  Taste relays through the thalamus but lands in the insula and
frontal operculum rather than on a neocortical strip.  Vestibular sensation has no
dedicated primary cortex at all, and it is two senses on two transducers, neither of
whose payload can be interpreted without the other.

Almost nothing here is counted.  Eleven of the twelve populations below carry no
neuron count, and the twelfth is 50,000 mitral cells.  That is not a small section but
an uncounted one: piriform cortex is a large allocortical area and the insula a large
cortical one, and neither is priced, because no clean human count exists and not
because the structures are small.

The one derived width in the section is the map's first that is neither zero nor one.
A receptor-to-mitral convergence of about 800 gives ceil(log2 800) = 10 bits.  Held in
a machine integer that becomes 16, the widest realisation gap in the map so far,
because 10 bits sits further from a container boundary than any earlier derived width.
Bit-packing closes the gap and costs unpacking on every read; padding spends the
memory instead.  That trade is this file's to record and it is never a reason to
shrink anything.

Time constants appear here and edge latencies do not, and the two must not be
confused.  An edge latency says when a signal arrives; a time constant says how long a
stage holds what it received.  Every edge latency in this section is underived and
reads None.  What is stated is state: the canal afferent's velocity signal decays with
a constant of 3-5 seconds, and velocity storage in the nuclei lengthens that to at
least 15-25 seconds.  Those live on the structures, never on the edges.

Against the tens of microseconds at which the auditory section computes, 15-25 seconds
of persisted state spans about 6.4 orders of magnitude.  No single update interval is
comfortable across that, and the constraint is recorded rather than resolved: the
scheduling discipline is not set.

Four element classes appear and only one is a threshold gate.  The olfactory sensory
neuron and the taste receptor cell are transducers.  The vestibular hair cells are not
neurons and are graded: their store is underived and is not zero, which is a different
statement from the photoreceptor's zero.  And the epithelium's sustentacular and basal
cells fit no class in the shared vocabulary at all -- see the note on that structure.

A fifth kind of internal transfer appears here and is deliberately not an edge.  In
the olfactory epithelium the basal stem cells produce new sensory neurons throughout
life; that line is a developmental transfer carrying no signal.  Writing it as an edge
would put a signal path in this file that does not exist.  A structure that
continuously rebuilds its own front end has no representation in fixed arrays, and
that is a finding rather than an omission.
"""

from __future__ import annotations

from Brain_config import (
    CONTESTED, EVENT_DRIVEN, Edge, GRADED, MODULATORY, NOT_APPLICABLE, NO_FRAME,
    OWED, PER_EAR, PER_HEMISPHERE, PER_SIDE, Population, ROUTING, Representation, Structure,
    THRESHOLD_GATE, TO_DERIVE, TRANSDUCER, allocate, class_endpoint, edge_report,
    emission, fan_in_map, far, here, learn, representation_report, schedule,
    sizing_report, unstemmed,
)

STEM = "03_other_senses"

# Far files reached from this section.  The stem, never the number: the number fixes
# data-flow position and the section names the structure, and a bare number goes
# silently wrong the moment a file is split, merged or renumbered.
#
# Three files are checked against this one, so three stems are written here.
# Every other named far end below carries no stem, which means the reading has not
# been done -- not that no far end exists.
BRAINSTEM = "14_brainstem_midbrain_hypothalamus"
SPINAL = "16_spinal_cord"

# Coordinate frames used more than once below.  Chemical identity is not a coordinate
# and neither is a category, so both resolve to NO_FRAME; they are named separately
# because they are different biological statements reaching the same allocation.
CHEMOTOPIC = "chemotopic -- adjacency means chemical similarity, not spatial proximity"
HEAD_FIXED_CANAL = "head-fixed, three canal axes; the basis is oblique, angles owed"
HEAD_FIXED_MACULA = "head-fixed, a distributed directional code rather than a basis"

# --------------------------------------------------------------------------
# Structures.
#
# Counts and their basis are the architecture's.  Where a count does not divide among
# the sub-elements the entry names, `partitions` is False, and an array for one of
# those sub-elements cannot be sized however well the sub-element is described.  In
# this section no structure partitions, and only one has a count to partition.
# --------------------------------------------------------------------------

OLFACTORY_EPITHELIUM = Structure(
    "olfactory epithelium",
    (
        # A transducer stores no threshold and the log2 cost does not apply.  The
        # store is zero here for a reason the model already contains: the cell has no
        # neural input, so there is no count of active inputs to compare against a
        # threshold, exactly as for a fan-in of one.  The caveat is that the model's
        # count has no referent at all -- what this cell thresholds is receptor
        # occupancy, and occupancy is not an input line.
        #
        # Unlike every other sensory front end in the map, the transducer is itself a
        # neuron whose own axon enters the brain: no separate primary afferent, no
        # ganglion, and no relay before the first central synapse.
        Population("olfactory sensory neurons", TRANSDUCER, PER_SIDE, 40_000_000, None,
                   note="the count is flagged above as inherited from the bulb entry, "
                        "not independently sourced, with human estimates varying "
                        "widely; each neuron expresses exactly one receptor gene, "
                        "chosen stochastically and then held"),
        # No class in the shared vocabulary fits these two, and that is recorded
        # rather than resolved by picking the nearest.  They are not transducers, they
        # carry no other structure's edges, and nothing above says they compute.  What
        # the architecture states is only that they are not threshold gates and their
        # store is underived, and GRADED is the one class whose store is underived
        # rather than zero -- so it is used for that numeric property alone and is not
        # a claim that these cells compute with graded potential.
        Population("sustentacular and basal cells", GRADED, PER_SIDE, None, None,
                   note="no element class fits; GRADED is used because its store is "
                        "underived rather than zero, which is what the rung above "
                        "states, and not as a claim about how they respond"),
    ),
    subelements=("olfactory sensory neurons", "sustentacular cells",
                 "basal stem cells"),
    rank=2,
    axes=("receptor type", "position in the epithelium"),
    partitions=False,
)
# Receptor-type extent is CONTESTED and not underived: 350-400 intact types on one
# reading, 100-200 on another.  Contested means measured and yielding readings that
# disagree, so it needs adjudication between existing results rather than a new
# measurement, and writing "to derive" over it would assert that nobody has looked.
#
# The position axis exists physically and indexes nothing.  The signal is not spatial,
# there is no receptor sheet mapping the world, and position says nothing about where
# the odorant came from.  It is allocated because the neurons occupy positions; it
# must never be indexed by a consumer.  The receptor protein itself steers the axon to
# its glomerulus, so the projection out of this sheet does not depend on position at
# all: a construction that sampled a neighbourhood in this axis would be building the
# wrong thing.
RECEPTOR_TYPE_EXTENT = CONTESTED
RECEPTOR_TYPES_HIGH_READING = (350, 400)
RECEPTOR_TYPES_LOW_READING = (100, 200)

OLFACTORY_BULB = Structure(
    "olfactory bulb",
    (
        # The one exactly-derived width in this section, and the map's first that is
        # neither zero nor one.
        Population("mitral and tufted cells", THRESHOLD_GATE, PER_SIDE, 50_000, 800,
                   note="fan-in ~800:1 receptor-to-mitral convergence, verified human "
                        "count"),
        # Interneurons vastly outnumber the projection neurons, so the bulb's total is
        # interneuron-dominated and soft, and the underived term is the larger one.
        Population("granule and periglomerular cells", THRESHOLD_GATE, PER_SIDE,
                   None, None,
                   note="no count recorded, and this is the majority of the store"),
    ),
    subelements=("olfactory nerve layer", "glomerular layer", "external plexiform",
                 "mitral cell layer", "internal plexiform", "granule cell layer"),
    rank=3,
    axes=("lamina", "glomerulus", "cell class"),
    partitions=False,
)
# The glomerular axis is the one indexable axis in this section, and its index is
# chemical identity rather than space.
#
# Its length is not a species constant.  The count ranges 3,000-9,300 across
# individuals, a 3.1x spread, so the correct value of this extent is a distribution
# and not a number.  Allocating the mean asserts a species value the measurement does
# not support, and what the code allocates against is owed.
GLOMERULUS_COUNT_MEAN = 5_568
GLOMERULUS_COUNT_SD = 830
GLOMERULUS_COUNT_RANGE = (3_000, 9_300)
LAMINA_COUNT = 6

PIRIFORM = Structure(
    "piriform and primary olfactory cortex",
    (
        # The afferent / associational segregation sorts the cell classes, so these
        # three are not interchangeable.  Semilunar cells are afferent-dominated and
        # send no feedback to the bulb; superficial pyramidal cells take weaker
        # afferent and stronger associational drive; deep pyramidal cells are mostly
        # driven by the recurrent circuit and receive the strongest recurrent
        # inhibition.  Sensory-driven and self-driven are not two states of this
        # network but two populations in it, ordered by depth.
        Population("semilunar cells (IIa)", THRESHOLD_GATE, PER_HEMISPHERE, None, None,
                   note="afferent-dominated; large spines in Ia but not Ib; sends no "
                        "feedback to the bulb"),
        Population("superficial pyramidal cells (IIb)", THRESHOLD_GATE,
                   PER_HEMISPHERE, None, None),
        Population("deep pyramidal cells (III)", THRESHOLD_GATE, PER_HEMISPHERE,
                   None, None),
        # Two inhibitory systems, each guarding its own input class.  A single
        # inhibition population over the structure would merge what the rung above
        # separates.
        Population("layer I horizontal and neurogliaform interneurons",
                   THRESHOLD_GATE, PER_HEMISPHERE, None, None,
                   note="take direct tract input and synapse on apical dendrites; "
                        "scoped to the afferent stream"),
        Population("layer II/III bitufted regular-spiking interneurons",
                   THRESHOLD_GATE, PER_HEMISPHERE, None, None,
                   note="take little tract input and synapse on somata and basal "
                        "dendrites; scoped to the associational stream"),
    ),
    subelements=("Ia", "Ib", "IIa", "IIb", "III"),
    rank=3,
    axes=("lamina", "cell class", "position"),
    partitions=False,
)
# Three-layered allocortex, two of whose layers subdivide, on piriform's own scheme.
# "Layer" here does not mean what it means in the isocortical entries.
#
# The position axis is not indexable and it is also not sized, and those are two
# different problems.  The bulb-to-piriform projection is non-topographic -- a
# glomerulus's output is distributed broadly across the sheet rather than to a matched
# location -- so the chemotopy present in the bulb is discarded at this synapse, and
# the association fibres are non-topographic too, so nothing restores it.  An axis
# that indexes nothing could still be allocated once its length were known, and this
# one's length is not: no clean human per-area count exists.
#
# The discarding of chemotopy is what makes the autoassociator possible, a
# content-addressable network being unable to use an input map.

GUSTATORY = Structure(
    # One entry, three stages, and it stays a bundle.  Splitting it here would invent
    # the arity two rungs below where the arity is known, and it would do it to a
    # stage whose file ownership is itself unresolved -- see the note below the
    # declaration.
    "gustatory pathway",
    (
        Population("taste receptor cells", TRANSDUCER, PER_SIDE, None, None,
                   note="read out through cranial nerves VII, IX and X"),
        Population("nucleus of the solitary tract, rostral", THRESHOLD_GATE,
                   PER_SIDE, None, None,
                   note="carries a full entry of its own in " + BRAINSTEM +
                        ", which defers the payload to this end; that entry names "
                        "seven subnuclei and a rostrocaudal gradient, and which one "
                        "the gustatory line leaves from is owed at this section's "
                        "source"),
        Population("ventral posteromedial parvocellular thalamic nucleus",
                   THRESHOLD_GATE, PER_HEMISPHERE, None, None,
                   note="recorded as having no entry in 12_thalamus under any name, "
                        "by that file and by " + BRAINSTEM + "; it is not absent from "
                        "the architecture, it is here, below the level a search for "
                        "entries can see"),
        Population("anterior insula and frontal operculum", THRESHOLD_GATE,
                   PER_HEMISPHERE, None, None,
                   note="primary gustatory cortex; inherently multisensory, carrying "
                        "somatosensory and thermal responses alongside taste"),
    ),
    subelements=(),
    rank=None,
    axes=(),
    partitions=False,
)
# Rank and axes are underived and sub-elements are owed throughout: no laminar or
# divisional partition of any of the three stages was established.  The rostral/caudal
# gradient of the disputed gustotopic hot spots is the only tangential organisation
# anyone has proposed, and it did not replicate.
#
# Three structures priced as none, and the first of the three is counted, or fails to
# be counted, in another file.
#
# Why the thalamic stage is invisible from both directions, which is the finding
# rather than the absence: the name differs in two places at once -- ventroposterior
# parvicellular and ventral posteromedial parvocellular are the same nucleus written
# with a different word order and a different vowel -- and this entry is a bundle, so
# the stage has no heading of its own to be matched against.  Owed at the source, and
# it is a decision rather than a repair: either the stage becomes an entry in the
# thalamus file and this one cites it, or that file records that the nucleus is
# described here.  Not moved: moving a stage between files would re-terminate three
# files' edges on a structure whose owner has not been decided.

SEMICIRCULAR_CANALS = Structure(
    "semicircular canals",
    (
        # Hair cells are not neurons and are the same class as the cochlear hair
        # cells.  Their store is underived and is not zero, which is a different
        # statement from the photoreceptor's zero: zero would assert they hold
        # nothing, and log2(fan-in) would assert a threshold they do not have.
        Population("crista hair cells", GRADED, PER_EAR, None, None,
                   note="every hair cell in a crista is aligned along that canal's "
                        "axis with kinocilia in the same direction, so an entire "
                        "crista has one directional sensitivity"),
    ),
    subelements=("horizontal canal", "anterior canal", "posterior canal"),
    rank=1,
    axes=("canal",),
    partitions=False,
)
# Extent exactly three per ear, and this is the only extent in the map that is exact,
# small and physical.  The organ is not a map and not a population code but one scalar
# per canal, and the three canals' anatomical orientations are the three basis vectors
# of the payload.
CANAL_COUNT = 3

# And the basis is oblique.  Substantial deviations from orthogonality, angle symmetry
# and coplanarity are the rule across 39 mammal species, and the degree of deviation is
# negatively correlated with estimated vestibular sensitivity -- so the departures are
# functional rather than noise, and orthogonality is a misleading descriptor.  A
# consumer cannot assume an orthonormal triad and read components off directly.
#
# This is None and not an identity matrix on purpose.  An identity here is not a
# placeholder: it is the specific assumption named above as misleading, and the
# deviations it would erase are the ones doing the work.  Initialising it to the
# identity would be building the less sensitive organ deliberately.
CANAL_BASIS_DIRECTION_COSINES = None  # owed: the human inter-canal angles

# The transducer's own dynamics.  This is a state time constant and never an edge
# latency: it says how long the cupula holds what it received, not when a signal
# arrives.  Every edge below carries latency None.
CANAL_VELOCITY_DECAY_TAU_S = (3.0, 5.0)
CANAL_VELOCITY_RESOLUTION_DEG_S = 2.0
CANAL_VELOCITY_MAX_DEG_S = None  # "hundreds of deg/s"; not a number, so not written

OTOLITH_ORGANS = Structure(
    "otolith organs",
    (
        Population("macular hair cells", GRADED, PER_EAR, None, None,
                   note="aligned in a multitude of directions, with polarity "
                        "reversing across the striola, so a macula emits a "
                        "distributed directional code and not a basis"),
    ),
    subelements=("utricle", "saccule"),
    rank=2,
    axes=("macula", "preferred direction"),
    partitions=False,
)
# Two maculae per ear, set close to orthogonal: the utricle roughly horizontal, the
# saccule roughly vertical.  Stated in words and not in numbers, and it fails the same
# way the canal basis does.
MACULA_COUNT = 2
MACULA_ORIENTATION_ANGLES = None  # owed, as the canal angles are
PREFERRED_DIRECTION_EXTENT = None  # owed, and it must not be set to 2 or 3

# One sense, two payload formats, and they must not be described alike.  In a crista
# every hair cell shares one directional sensitivity, so the organ emits one scalar
# per canal and the three canal axes are the basis.  In a macula the direction must be
# decoded from a population rather than read off, and no rung above names the decoder.
# A population-vector readout is the obvious candidate and it is not written here.

VESTIBULAR_NUCLEI = Structure(
    "vestibular nuclei and the central vestibular pathway",
    (
        Population("vestibular nucleus neurons", THRESHOLD_GATE, PER_SIDE, None, None,
                   note="the cell-class axis is partly named by response rather than "
                        "by place: type II vestibular-only neurons increase firing "
                        "with rotation toward the contralateral canal, so the "
                        "population is distinguished by what it responds to and which "
                        "side drives it, not by where it sits; further partition owed"),
        # The basis changes inside one structure, which is why it is carried on the
        # population rather than assumed for the file.
        Population("parieto-insular vestibular cortex", THRESHOLD_GATE,
                   PER_HEMISPHERE, None, None,
                   note="posterior insula / parietal operculum / retroinsular, human "
                        "homologue debated; there is no dedicated primary vestibular "
                        "cortex and this is the one sense without one"),
    ),
    subelements=("superior nucleus", "medial nucleus", "lateral nucleus",
                 "inferior nucleus"),
    rank=2,
    axes=("nucleus", "cell class"),
    partitions=False,
)
NUCLEUS_COUNT = 4

# Velocity storage lengthens the canal line's constant to at least this, and the
# content is unchanged: only its persistence alters.  The map has no other edge whose
# declared transformation is purely temporal.  The mechanism is owed -- nothing above
# says what implements the integrator -- so the factor is recorded and no integrator
# is written.  A state time constant, never an edge latency.
VELOCITY_STORAGE_TAU_S = (15.0, 25.0)

STRUCTURES = (OLFACTORY_EPITHELIUM, OLFACTORY_BULB, PIRIFORM, GUSTATORY,
              SEMICIRCULAR_CANALS, OTOLITH_ORGANS, VESTIBULAR_NUCLEI)

# This file lists seventeen populations where the section totals above it list twelve
# rows, and the difference is granularity rather than content.  The rung above pools
# piriform's five cell classes into one row and does not give the taste receptor cells
# a row at all, while its entries name all six; the populations here follow the
# entries.  No figure moves: every added population is uncounted, so the stated total
# is the same 0.063 MB and only the count of unstated stores rises, from eleven to
# fifteen.  That larger count is the same gap read at a finer grain and is not a new
# one -- which is worth saying, because a bare 15 against a bare 11 would look like
# four stores had gone missing.

# --------------------------------------------------------------------------
# Edges.
#
# A modulatory edge sets whether, when and how strongly content passes and adds no
# content of its own.  Three of the bulb's four input lines are declared above with no
# chemical content, so a forward operation that summed all inputs alike would be
# reading a gain as evidence: the role is carried on the edge rather than inferred.
#
# Every latency here is None.  None is not a licence to substitute zero or a uniform
# interval.  The two time constants this section states are state and live on the
# structures above.
# --------------------------------------------------------------------------

EDGES: tuple[Edge, ...] = (

    # --- olfactory epithelium -------------------------------------------
    Edge(class_endpoint("airborne odorant molecules dissolved in the mucus"),
         here("olfactory epithelium", "olfactory sensory neurons"),
         carries="chemical identity and concentration",
         role=ROUTING,
         representation=Representation("chemical identity and concentration",
                                       TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="a chemical arrival and not a neural edge; fan-in is " + NOT_APPLICABLE
              + ". Chemical identity is not a coordinate, so the frame is none rather "
                "than underived."),

    Edge(class_endpoint("centrifugal modulation of the epithelium"),
         here("olfactory epithelium", "olfactory sensory neurons"),
         carries=OWED,
         role=MODULATORY,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="whether this edge exists at all is what the rung above declines to "
              "assert. It is the gain loop onto the chemical front end that the "
              "auditory section closes and this one cannot confirm closes, so "
              "co-instantiation cannot be shown satisfied for it -- there may be no "
              "loop."),

    Edge(here("olfactory epithelium", "olfactory sensory neurons"),
         here("olfactory bulb", "glomerular layer"),
         carries="one component of a combinatorial chemical code: a single neuron "
                 "reports how strongly its one receptor type is occupied, and the "
                 "odour's identity exists only in the pattern across types",
         representation=Representation("receptor occupancy, per receptor type",
                                       TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         fan_out=2,
         note="fan-out is one or two glomeruli per axon, recorded here at the upper "
              "bound. Not a scalar, not a map of space, and not frequency-analysed "
              "the way the cochlear output is: there is no ordering of the chemical "
              "dimension corresponding to the tonotopic axis, so a consumer "
              "allocating an ordered axis would assert a neighbourhood relation the "
              "biology does not have."),

    # --- olfactory bulb -------------------------------------------------
    Edge(here("piriform and primary olfactory cortex"), here("olfactory bulb"),
         carries="gain and state, no chemical content",
         role=MODULATORY,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="the pyramidal cells send this feedback and the semilunar cells do not; "
              "the afferent-dominated class is the one that does not talk back"),

    Edge(unstemmed("basal forebrain, raphe and locus coeruleus"),
         here("olfactory bulb"),
         carries="centrifugal neuromodulation: gain and state, no chemical content",
         role=MODULATORY,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("olfactory bulb", "mitral cell layer"),
         here("piriform and primary olfactory cortex", "Ia"),
         carries="the decorrelated glomerular pattern, sharpened by inhibition, "
                 "chiefly ipsilateral, by the lateral olfactory tract, monosynaptic, "
                 "and straight to cortex with no thalamic relay and therefore no "
                 "thalamic gate",
         representation=Representation(TO_DERIVE, "normalised, and that is the "
                                       "payload change", EVENT_DRIVEN, CHEMOTOPIC),
         note="the frame on this line is the producer's and it does not survive the "
              "synapse: the projection is non-topographic and the chemotopy is "
              "discarded at the far end. A consumer inheriting the frame from this "
              "line would be right at the producer and wrong at itself. That payload "
              "change is what makes the autoassociator possible and the rung above "
              "records that it is not stated in the consumer's own edge fields."),

    Edge(here("olfactory bulb", "mitral cell layer"),
         unstemmed("anterior olfactory nucleus, olfactory tubercle, cortical "
                   "amygdala and rostral entorhinal cortex"),
         carries="the decorrelated glomerular pattern, as above",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       CHEMOTOPIC),
         note="four named targets on one line, none of whose files has been opened "
              "beside this one. Not split here: splitting an endpoint against far "
              "ends nobody has read is the same defect as writing an edge whose far "
              "end was never read."),

    # The one synaptic arrangement in this section that the directed edge type cannot
    # express, declared once and marked.  The mitral / tufted lateral dendrite and the
    # granule cell spine form a dendrodendritic reciprocal synapse: one synaptic
    # apposition carrying signal in both directions, not two edges.  Writing it as two
    # asserts two synapses where there is one; writing it as one asserts a direction
    # it does not have.  What a reciprocal apposition is in code changes the shared
    # edge type, which every module imports, so it is surfaced rather than chosen.
    Edge(here("olfactory bulb", "mitral cell layer"),
         here("olfactory bulb", "granule cell layer"),
         carries="one reciprocal dendrodendritic apposition, signal in both "
                 "directions",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       CHEMOTOPIC),
         note="RECIPROCAL: this is one apposition and not a directed pair. The "
              "direction written here is an artefact of the edge type and carries no "
              "claim. Owed above this rung."),

    # Lateral inhibition here operates over a non-spatial neighbourhood, and it is the
    # item most likely to be got wrong in code.  Short-axon cells inhibit between
    # glomeruli, and because glomerular adjacency is chemotopic, lateral means lateral
    # in chemical similarity.  Every other instance of lateral inhibition in the map
    # operates over a map of the world.  A convolution over adjacent glomerular
    # indices is what a coder reaches for and it would assert that index adjacency
    # equals chemical similarity, which the chemotopic claim says qualitatively and
    # does not quantify.  The metric is owed at the architecture rung.
    Edge(here("olfactory bulb", "glomerular layer"),
         here("olfactory bulb", "glomerular layer"),
         carries="short-axon cell inhibition between glomeruli",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       CHEMOTOPIC),
         note="the neighbourhood is chemical and no rung above supplies a similarity "
              "metric over it, so no neighbourhood operator is written"),

    # --- piriform and primary olfactory cortex --------------------------
    Edge(here("piriform and primary olfactory cortex", "III"),
         here("piriform and primary olfactory cortex", "Ib"),
         carries="the network's own state; the feedback that completes a partial "
                 "pattern",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="the map's only declared intra-regional recurrent edge that is "
              "load-bearing for its entry's stated function rather than noted in "
              "passing. A staged bring-up that omitted it would not have a degraded "
              "autoassociator; it would have no autoassociator. This structure and "
              "its own recurrence come up together or not at all."),

    Edge(unstemmed("orbitofrontal and entorhinal cortex, amygdala, and "
                   "neuromodulatory nuclei"),
         here("piriform and primary olfactory cortex"),
         carries="context, value and state",
         role=MODULATORY,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    Edge(here("piriform and primary olfactory cortex"),
         unstemmed("orbitofrontal cortex"),
         carries="the odour object: a completed, content-addressed identity rather "
                 "than a receptor pattern, directly and by the mediodorsal thalamus",
         representation=Representation("a category", TO_DERIVE, EVENT_DRIVEN,
                                       NO_FRAME),
         note="the payload has become a category -- which smell, not how much of what "
              "chemical -- and a category has no coordinate frame. The change of kind "
              "is this structure's whole function and the rung above records that it "
              "is written into the payload and nowhere typed as a transformation."),

    Edge(here("piriform and primary olfactory cortex"), unstemmed("amygdala"),
         carries="the odour object, for hedonic and emotional evaluation",
         representation=Representation("a category", TO_DERIVE, EVENT_DRIVEN,
                                       NO_FRAME)),

    Edge(here("piriform and primary olfactory cortex"),
         unstemmed("entorhinal cortex, thence the hippocampal formation"),
         carries="the odour object as an element of an episode",
         representation=Representation("a category", TO_DERIVE, EVENT_DRIVEN,
                                       NO_FRAME)),

    Edge(here("piriform and primary olfactory cortex"), unstemmed("hypothalamus"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED)),

    # --- gustatory pathway ----------------------------------------------
    Edge(class_endpoint("tastants at the taste buds"),
         here("gustatory pathway", "taste receptor cells"),
         carries="dissolved tastants",
         role=ROUTING,
         representation=Representation("chemical identity and concentration",
                                       TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="a chemical arrival and not a neural edge; fan-in is " + NOT_APPLICABLE),

    Edge(here("gustatory pathway", "taste receptor cells"),
         far("nucleus of the solitary tract, rostral", BRAINSTEM),
         carries="taste quality and intensity, plus oral somatosensation "
                 "(temperature, texture, viscosity, fat, capsaicin): a "
                 "five-ish-dimensional quality vector with an intensity scalar",
         representation=Representation("quality channels and an intensity scalar",
                                       TO_DERIVE, EVENT_DRIVEN,
                                       "no spatial map of the world, only a crude "
                                       "map of the tongue"),
         note="by cranial nerves VII, IX and X. The far entry defers the payload to "
              "this end and this end types it. The far end carries a partition this "
              "one does not -- seven subnuclei, one of them parvicellular, and a "
              "rostrocaudal gradient -- so which subnucleus the line leaves from is "
              "owed at this section's source. The same stage is also a population of "
              "this file's bundled structure, which is the bundle showing through."),

    # The two internal links of the bundle.  They come from the entry's Function
    # field, which states the chain, and not from its Inputs and Outputs, which type
    # only the ends.  Recorded because the distinction matters: an internal edge has
    # both ends inside one entry and therefore has no two-ended check at all.
    Edge(far("nucleus of the solitary tract, rostral", BRAINSTEM),
         here("gustatory pathway",
              "ventral posteromedial parvocellular thalamic nucleus"),
         carries="the quality vector, relayed",
         representation=Representation("quality channels and an intensity scalar",
                                       TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="in primates this line skips the pontine parabrachial relay that "
              "rodents use"),

    Edge(here("gustatory pathway",
              "ventral posteromedial parvocellular thalamic nucleus"),
         here("gustatory pathway", "anterior insula and frontal operculum"),
         carries="the same vector, relayed, chiefly ipsilateral",
         representation=Representation("quality channels and an intensity scalar",
                                       TO_DERIVE, EVENT_DRIVEN,
                                       "chiefly ipsilateral; crude tongue map only"),
         note="the payload description on this line cannot be right as written, and "
              "the copy is faithful rather than smoothed. The rung above states that "
              "as the signal proceeds to the hindbrain and higher, coding becomes "
              "more distributed and temporal patterns become important, so the "
              "quality vector is progressively re-encoded into an ensemble pattern "
              "across exactly this span, and the same payload description must not be "
              "carried at every stage. Recorded as a finding against the architecture "
              "entry."),

    Edge(here("gustatory pathway", "anterior insula and frontal operculum"),
         unstemmed("orbitofrontal cortex"),
         carries="quality and intensity, independent of hunger",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="the payload changes at the next stage and not this one: the primary "
              "cortex declares what is in the mouth and the secondary declares what "
              "it is worth. So no equation in this structure may make its output "
              "depend on hunger, satiety or value."),

    Edge(here("gustatory pathway", "anterior insula and frontal operculum"),
         unstemmed("amygdala"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="reciprocal"),

    Edge(here("gustatory pathway", "anterior insula and frontal operculum"),
         unstemmed("hypothalamus"),
         carries=OWED,
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="feeding; reciprocal"),

    # --- semicircular canals --------------------------------------------
    Edge(class_endpoint("head angular motion"),
         here("semicircular canals", "horizontal canal"),
         carries="mechanical rotation onto the hair cells of the three cristae",
         role=ROUTING,
         representation=Representation("angular velocity of the head", TO_DERIVE,
                                       EVENT_DRIVEN, "world"),
         note="a mechanical arrival by the inertial lag of the endolymph, and not a "
              "neural edge; fan-in is " + NOT_APPLICABLE + ". A payload change "
              "happens here, before the first synapse, performed by fluid mechanics: "
              "the canal is a heavily damped torsion pendulum, viscous drag dominates "
              "inertia, and across the band of natural head movement the mechanics "
              "integrate the angular acceleration that drives them, so the afferent's "
              "firing is proportional to velocity and peaks at peak velocity rather "
              "than peak acceleration. The map has no other instance of a transform "
              "executed outside the nervous system."),

    Edge(here("semicircular canals"),
         here("vestibular nuclei and the central vestibular pathway",
              "superior and medial nuclei"),
         carries="head angular velocity, three-axis, head-fixed, band-limited with no "
                 "direct-current term, one triplet per ear; does not carry linear "
                 "acceleration, gravity, tilt or attitude",
         representation=Representation("deg/s", "~2 deg/s discriminable, sensitive to "
                                       "hundreds of deg/s; no direct-current term",
                                       EVENT_DRIVEN, HEAD_FIXED_CANAL),
         note="by the superior division of the vestibular ganglion and cranial nerve "
              "VIII. The only line in this file whose units, range and frame are all "
              "stated, and it is still not closed, because the frame is a basis whose "
              "vectors have no numbers. The width the range implies is "
              "ceil(log2(2 * omega_max / 2 deg/s)) and omega_max is not a number, so "
              "the expression is carried and not evaluated."),

    Edge(here("semicircular canals"),
         far("cerebellar cortex", "10_cerebellum", sub="flocculonodular lobe"),
         carries="the same rotation-rate signal, unrelayed",
         representation=Representation("deg/s", "as the nuclear line", EVENT_DRIVEN,
                                       HEAD_FIXED_CANAL),
         note="a branch that bypasses the nuclei; the same payload as the line above "
              "and not a second signal, so it is not allocated twice. Two-ended, and "
              "this end is the specific one: that file carries this limb inside a "
              "single afferent line naming the canals, the otolith organs and the "
              "vestibular nuclei together, under one payload clause. The split is "
              "owed there and every term it needs is here."),

    # --- otolith organs -------------------------------------------------
    Edge(class_endpoint("head linear acceleration and gravity"),
         here("otolith organs", "utricle"),
         carries="mechanical shear by way of the otoconial mass",
         role=ROUTING,
         representation=Representation("acceleration, gravity included and "
                                       "inseparable", TO_DERIVE, EVENT_DRIVEN,
                                       "world"),
         note="a mechanical arrival through the weight and inertia of the otoconial "
              "mass, and not a neural edge; fan-in is " + NOT_APPLICABLE + ". The "
              "inertia of the mass shears the bundles under acceleration and its "
              "weight shears them under tilt, and the two are the same shear."),

    Edge(here("otolith organs"),
         here("vestibular nuclei and the central vestibular pathway",
              "lateral and inferior nuclei"),
         carries="the gravito-inertial acceleration vector, head-fixed, with a "
                 "direct-current term: a maintained tilt produces a maintained "
                 "signal; does not carry rotation rate, and does not carry tilt or "
                 "attitude separately from translation -- the two leave the ear "
                 "summed, and the sum is the signal",
         representation=Representation(TO_DERIVE, "with a direct-current term; tilt "
                                       "and translation unresolved", EVENT_DRIVEN,
                                       HEAD_FIXED_MACULA),
         note="by the inferior division of the vestibular ganglion and cranial nerve "
              "VIII. The direct-current term is the representational difference from "
              "the canal line and it is not cosmetic: the canal loses steady state by "
              "construction and this line does not, so a consumer normalising both "
              "the same way would destroy the only signal that survives a constant "
              "stimulus. The ambiguity is a consequence of physics and not a "
              "limitation of the organ: gravity and linear acceleration are "
              "indistinguishable to any accelerometer."),

    Edge(here("otolith organs"),
         far("cerebellar cortex", "10_cerebellum",
             sub="flocculonodular lobe, nodulus and uvula"),
         carries="the same vector, unrelayed",
         representation=Representation(TO_DERIVE, "as the nuclear line", EVENT_DRIVEN,
                                       HEAD_FIXED_MACULA),
         note="the direct branch; the same payload as the line above. Two-ended, and "
              "this end names the destination sub-element where the far end names the "
              "flocculonodular lobe entire."),

    # --- vestibular nuclei and the central vestibular pathway -----------
    Edge(far("cerebellar cortex", "10_cerebellum",
             sub="flocculonodular lobe, nodulus and uvula"),
         here("vestibular nuclei and the central vestibular pathway"),
         carries="the return arm of the computation, the internal model's correction",
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="two-ended, and that file records this as the one exception to its rule "
              "that the cerebellar cortex projects nowhere but the deep nuclei. This "
              "end names the finer origin."),

    Edge(far("deep cerebellar nuclei", "10_cerebellum", sub="fastigial nucleus"),
         here("vestibular nuclei and the central vestibular pathway"),
         carries="axial posture, balance and eye-movement corrections",
         representation=Representation(OWED, OWED, EVENT_DRIVEN, OWED),
         note="declared at the producer's end only and written here from it. This is a "
              "second and separate cerebellar source: the line above arrives from the "
              "cerebellar cortex directly, this one from the output nuclei, and the two "
              "are different structures with different payloads. Both payloads are owed, "
              "which is the condition under which two lines look interchangeable and are "
              "not. The far end bundles this limb with a reticular one and owes that "
              "split."),

    # The cerebellar half of this route is consumer-only: 10_cerebellum declares no
    # output carrying vision or proprioception here, and its two outputs that reach
    # this structure carry graded inhibition and postural correction instead.  Owed
    # there: name the carrying structure, or withdraw the cerebellar half.
    Edge(class_endpoint("vision and proprioception, by the cortical vestibular areas "
                        "and the cerebellum"),
         here("vestibular nuclei and the central vestibular pathway"),
         carries="optic flow and body configuration, as the second and third "
                 "estimates of the same quantity",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="not additional content but the same content in other frames, so "
              "combining them requires a common frame that no rung supplies. This is "
              "why the estimate survives when one line is degraded and why it can be "
              "fooled when vision and the labyrinth disagree."),

    Edge(here("vestibular nuclei and the central vestibular pathway"),
         unstemmed("oculomotor nuclei III, IV and VI"),
         carries="the vestibulo-ocular reflex command, an eye-velocity signal equal "
                 "and opposite to head rotation, driven chiefly by the canal line",
         representation=Representation("eye velocity", TO_DERIVE, EVENT_DRIVEN,
                                       "eye"),
         note="by the medial longitudinal fasciculus"),

    Edge(here("vestibular nuclei and the central vestibular pathway", "lateral nucleus"),
         far("spinal cord", SPINAL),
         carries="an antigravity postural command, driven chiefly by the otolith line "
                 "by way of the lateral nucleus",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, "body"),
         note="by the vestibulospinal tracts. The far file carries this limb inside a "
              "five-tract descending bundle whose payload it marks owed and declines "
              "to split, because splitting would invent the arity of the five "
              "payloads. This line is one of the five and it is typed at this end, so "
              "the far end's owed is accurate for the bundle and not for this member."),

    Edge(here("vestibular nuclei and the central vestibular pathway"),
         far("cerebellar cortex", "10_cerebellum"),
         carries="both transducer lines plus the current estimate",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="two-ended, and this is the limb that carries a computed quantity rather "
              "than a transducer signal, which the far end's bundled afferent line types "
              "correctly but cannot attribute, since it names three sources under one "
              "payload clause."),

    Edge(here("vestibular nuclei and the central vestibular pathway"),
         unstemmed("thalamus: ventroposterior, ventral lateral and intralaminar"),
         carries="the computed estimate: head attitude and self-motion, with gravity "
                 "separated from linear acceleration",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, "head"),
         note="thence to parieto-insular vestibular cortex, area 2v, area 3a, and on "
              "to the hippocampal formation. This is not the transducer signal, and "
              "that distinction is the whole reason the structure exists: what "
              "ascends is a result, not a measurement. So no output line of this "
              "structure may carry an input through unchanged. The medial superior "
              "temporal and ventral intraparietal areas are not direct thalamic "
              "targets on this line and the route to them is contested -- there is "
              "reported to be a lack of anatomical evidence for "
              "a thalamic vestibular projection to the medial superior temporal area, "
              "and response dynamics and latency order the three areas as a "
              "cortico-cortical route predicts. Re-deriving the route is owed, and it "
              "reads " + CONTESTED + " rather than underived."),

    Edge(here("vestibular nuclei and the central vestibular pathway",
              "parieto-insular vestibular cortex"),
         unstemmed("ventral intraparietal area, thence the medial superior temporal "
                   "area"),
         carries="the same computed estimate in a frame that changes at each step",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "intermediate between head- and body-centred "
                                       "at parieto-insular, body-centred at ventral "
                                       "intraparietal, approximately head-centred at "
                                       "medial superior temporal"),
         note="the line a consumer will get wrong, and the reason the frame is "
              "declared here rather than at the structure: one payload, three hops, a "
              "different frame at each, and the change is not monotonic -- head, then "
              "body, then head again. A consumer inheriting the frame from the "
              "producing structure would be right once and wrong twice."),
)

# --------------------------------------------------------------------------
# The internal edge this section most needs and does not have.
#
# Neither transducer alone can disambiguate tilt from translation, and the resolution
# is the specific convergence of canal and otolith signals onto central vestibular
# neurons.  The entry above declares both inputs and does not declare the meeting, so
# the convergence edge, and which cells carry it, is owed.
#
# At this rung that has an exact cost: the structure's central function has no
# internal edge to transcribe.  Two input arrays arrive, one output is described, and
# the line between them is written at no rung.  It is left absent and named rather
# than invented, because a well-formed invented edge reads exactly like a derived one.
# --------------------------------------------------------------------------

OWED_INTERNAL_EDGES = (
    ("vestibular nuclei and the central vestibular pathway",
     "the convergence of canal and otolith signals onto central vestibular neurons -- "
     "the structure's central function, and the internal edge that matters most here"),
    ("vestibular nuclei and the central vestibular pathway",
     "whatever implements velocity storage; the lengthening factor is stated and the "
     "mechanism is not"),
    ("olfactory bulb",
     "the chemical similarity metric the short-axon lateral inhibition operates over"),
    ("gustatory pathway",
     "which subnucleus of the solitary tract the gustatory line leaves from; the far "
     "end has the axis and this end has none"),
    ("otolith organs",
     "the decoder that turns the distributed directional code into a direction"),
)


# --------------------------------------------------------------------------
# Reporting.  Every figure below is recomputed from the counts above rather than
# transcribed.
# --------------------------------------------------------------------------


def mitral_width() -> str:
    """The section's one derived width, and what a machine integer costs it.

    No integer type is 10 bits wide.  Bit-packing closes the gap and costs unpacking
    on every read; padding spends the memory instead.  That trade is this file's to
    record and it is never a reason to shrink anything: memory is a derived
    requirement, not a limit to design against.
    """
    p = OLFACTORY_BULB.populations[0]
    derived, realised = p.parameter_bytes, p.realised_bytes
    return (f"  fan-in {p.fan_in} -> ceil(log2) = {p.threshold_bits} bits\n"
            f"  {p.count:,} cells: derived {derived:,} bytes = {derived/1e6:.3f} MB\n"
            f"  held in uint16   : realised {realised:,} bytes = {realised/1e6:.3f} MB\n"
            f"  gap {100*(realised-derived)/derived:.0f}% -- the widest in the map so "
            f"far, 10 bits sitting furthest from a container boundary")


def glomerular_extent() -> str:
    """The axis whose correct value is a distribution and not a number.

    Allocating the mean asserts a species value the measurement does not support.
    """
    lo, hi = GLOMERULUS_COUNT_RANGE
    return (f"  mean {GLOMERULUS_COUNT_MEAN:,} +/- {GLOMERULUS_COUNT_SD:,} per bulb, "
            f"range {lo:,}-{hi:,}\n"
            f"  spread {hi/lo:.1f}x across individuals -- the axis length is not a "
            f"property of the species")


def convergence_range() -> str:
    """A contest in one entry propagating into another entry's shape.

    The glomerulus-per-receptor-type convergence depends on a receptor count the rung
    above records as contested, so the same measured glomerular count supports a
    four-fold range of convergence.
    """
    out = []
    for label, (lo, hi) in (("350-400 intact types", RECEPTOR_TYPES_HIGH_READING),
                            ("100-200 types", RECEPTOR_TYPES_LOW_READING)):
        a = GLOMERULUS_COUNT_MEAN / hi
        b = GLOMERULUS_COUNT_MEAN / lo
        out.append(f"  {label:22} -> {a:.1f} : 1 to {b:.1f} : 1")
    out.append(f"  receptor-type extent is {RECEPTOR_TYPE_EXTENT}, which needs "
               f"adjudication between existing")
    out.append("  results rather than a new measurement, and must not read underived")
    return "\n".join(out)


def time_constants() -> str:
    """State, never latency, and this file is where the two would be confused.

    An edge latency says when a signal arrives; a time constant says how long a stage
    holds what it received.  Every edge above carries latency None.
    """
    c_lo, c_hi = CANAL_VELOCITY_DECAY_TAU_S
    v_lo, v_hi = VELOCITY_STORAGE_TAU_S
    return (f"  canal cupula decay        {c_lo:g}-{c_hi:g} s   (state, on the "
            f"transducer)\n"
            f"  velocity storage          {v_lo:g}-{v_hi:g} s   (state, in the "
            f"nuclei)\n"
            f"  lengthening               {v_lo/c_hi:.1f}x to {v_hi/c_lo:.1f}x   "
            f"(content unchanged; only persistence alters)\n"
            f"  edges with a stated latency in this file: "
            f"{sum(1 for e in EDGES if e.latency_s is not None)}")


def dynamic_range() -> str:
    """The constraint this section places on a decision it does not make.

    The auditory section computes at tens of microseconds; this one holds state for
    tens of seconds.  No single update interval is comfortable across that span, and
    the scheduling discipline is not set.
    """
    from math import log10
    fast = 10e-6
    slow = VELOCITY_STORAGE_TAU_S[1]
    return (f"  {slow:g} s against {fast*1e6:g} us = {slow/fast:.2e}, about "
            f"{log10(slow/fast):.1f} orders of magnitude\n"
            f"  ~{log10(slow/fast)/log10(2):.0f} bits of time, and no single interval "
            f"serves it comfortably")


def exact_extents() -> str:
    """The three facts about extent that are unlike anything in the first two sections."""
    return (
        f"  an axis that exists physically and indexes nothing : "
        f"position in the epithelium\n"
        f"  an extent exact, small and physical                : "
        f"{CANAL_COUNT} canals per ear, "
        f"basis {'OWED' if CANAL_BASIS_DIRECTION_COSINES is None else 'set'}\n"
        f"  an extent varying "
        f"{GLOMERULUS_COUNT_RANGE[1]/GLOMERULUS_COUNT_RANGE[0]:.1f}x between "
        f"individuals        : glomeruli per bulb")


def unpartitioned() -> str:
    """Structures naming sub-elements their count does not divide among.

    An edge terminating on one of these names a place whose extent is unknown, which
    blocks allocation rather than description.
    """
    out = []
    for s in STRUCTURES:
        if not s.subelements:
            continue
        counts = [p.count for p in s.populations if p.count]
        total = f"{sum(counts):,}" if counts else TO_DERIVE
        landing = sum(1 for e in EDGES if e.target.name == s.name and e.target.sub)
        out.append(f"  {s.name[:44]:44} {len(s.subelements):2d} sub-elements, "
                   f"count {total:>12}, {landing} edges land on one")
    return "\n".join(out)


def owed_internal_edges() -> str:
    out = []
    for structure, what in OWED_INTERNAL_EDGES:
        out.append(f"  {structure[:40]:40} {what}")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report(STRUCTURES, f"Brain {STEM}"))
    print()
    print("the one derived width in this section:")
    print(mitral_width())
    print()
    print("the glomerular axis:")
    print(glomerular_extent())
    print()
    print("convergence, and a contest propagating into a shape:")
    print(convergence_range())
    print()
    print("time constants, which are state and not latency:")
    print(time_constants())
    print()
    print("the span this section and the auditory one bracket:")
    print(dynamic_range())
    print()
    print("extents:")
    print(exact_extents())
    print()
    print(edge_report(EDGES))
    print()
    print("sub-elements without a partition of the count:")
    print(unpartitioned())
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
