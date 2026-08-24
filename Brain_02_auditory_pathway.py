"""Brain — 02 auditory pathway: cochlea to the temporal-lobe endpoints.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

STRUCTURES 1-5 ARE WRITTEN HERE: cochlea, cochlear nucleus, superior olivary complex,
inferior colliculus, medial geniculate nucleus.  Structures 6-11 -- primary auditory
cortex, auditory belt, auditory parabelt, anterior superior temporal gyrus and sulcus,
posterior superior temporal gyrus and the Sylvian parieto-temporal area, and the
right-hemisphere prosodic homologues -- are NOT written.  Their absence is a gap in
this file and not a statement that the pathway ends at the thalamus.  Edges naming
them are declared and marked pending, so the descending cortical limbs are visible as
present-and-unreachable rather than silently missing.

Timing is the payload here rather than a property of it, and that governs the whole
file.  Three structures compute on arrival-time differences at the tens-of-microseconds
scale.  Phase locking at low frequencies means the timing of the waveform is part of
what the auditory nerve carries, not merely the schedule on which it arrives.  So the
substitution available to a visual module -- set every edge equal and lose only
accuracy -- is not available here: set the two bilateral inputs of the medial superior
olive equal and it computes nothing at all.  No numerical edge latency is stated
anywhere in this section, so every edge below reads None, and None is not a licence to
substitute zero or a uniform interval.

The tonotopic map is inherited and never computed.  Position along the cochlear tube
maps to frequency by the mechanics of the basilar membrane's graded stiffness and mass,
so what leaves the ear is already sorted and every downstream structure inherits the
map.  Nothing in this file computes a spectrum.

The cochlear sheet is one-dimensional: position is frequency and there is no second
axis, where a retinotopic sheet has two.  Every array below is shaped accordingly.  An
array shaped like a visual sheet would give this pathway a dimension the organ has not
got.

Counting basis changes twice along the line: per ear at the cochlea, per side through
the brainstem, per hemisphere from the cochlear nucleus and in cortex.  Above the
parabelt the per-hemisphere convention breaks down entirely, because the two
hemispheres stop being counterparts -- which is in the six entries not written here.

Three edges in this section are not projections.  The cochlea's input is
sound-pressure vibration by way of the middle ear, an acoustic arrival whose fan-in is
not applicable rather than underived.  The cochlear amplifier is a mechanical loop
inside the sensory organ, outer hair cells adding force back into the basilar-membrane
travelling wave through prestin.  And the acoustic reflex reaches the cochlea through a
middle-ear muscle rather than onto neural structure.
"""

from __future__ import annotations

from Brain_config import (
    BOTH_EYES, CONTESTED, DRIVER, EVENT_DRIVEN, Edge, Endpoint, GRADED,
    MODULATORY, NOT_APPLICABLE, NO_FRAME, OWED, PER_EAR, PER_HEMISPHERE, PER_SIDE,
    Population, ROUTING, Representation, Structure, THRESHOLD_GATE, TO_DERIVE,
    TRANSDUCER, UNKNOWN, allocate, class_endpoint, edge_report, emission, fan_in_map,
    far, here, learn, no_entry, pending, representation_report, route, schedule,
    sizing_report, unstemmed,
)

STEM = "02_auditory_pathway"

# Far files reached from the five structures written here.  The stem is written only
# where the far file has been read against this one.  Several endpoints below name a
# structure and carry no stem: those are readings not yet done, and inventing a stem
# for them would derive connectivity at the wrong rung -- the endpoint would resolve,
# and nothing would have checked that it resolves right.
CRANIAL_NERVE_NUCLEI = "15_cranial_nerve_nuclei"

TONOTOPIC = "tonotopic"
TONOTOPIC_MONAURAL = "tonotopic, monaural"

# --------------------------------------------------------------------------
# Structures.
# --------------------------------------------------------------------------

COCHLEA = Structure(
    "cochlea",
    (
        # Fan-in is exactly one: each type I neuron contacts one inner hair cell.
        # log2(1) = 0 -- a neuron with a single input stores no threshold, because
        # there is no count to compare against.  The first structure in the map where
        # a known fan-in drives the cost to zero rather than an unknown one leaving it
        # open.
        Population("type I spiral ganglion", THRESHOLD_GATE, PER_EAR, 31_500, 1,
                   note="a pure divergence with no convergence at all: fan-out 5-30 "
                        "type I neurons per inner hair cell, fan-in exactly one"),
        # These fibres are not required for hearing.  The current reading is a damage
        # signal from the organ of Corti: same nerve, same tonotopic order, same
        # target, and not audition.
        Population("type II spiral ganglion", THRESHOLD_GATE, PER_EAR, 2_500, 12,
                   note="~5-10% of the ganglion, unmyelinated; fan-in ~12, the "
                        "opposite arity to the type I line"),
        # Not neurons: sensory epithelial cells producing graded receptor potentials
        # with no action potentials at all.  Neither the transducer exception nor the
        # threshold-gate model reaches them, so the store is neither zero nor
        # log2(fan-in).  The widest such gap in either of the first two sections.
        Population("inner and outer hair cells", GRADED, PER_EAR, 15_500, None,
                   note="~3,500 inner (the transducers, carrying essentially all "
                        "sound information) and ~12,000 outer (the amplifier, motile, "
                        "adding mechanical energy back into the travelling wave)"),
    ),
    subelements=("inner hair cells", "outer hair cells",
                 "type I spiral ganglion", "type II spiral ganglion"),
    rank=2,
    axes=("cell class", "position along the tube"),
    partitions=True,
)
# Position is frequency, base to apex, high to low, over a ~35 mm tube.  The tonotopic
# axis is the only map axis.  Extents are measured throughout, which makes this the one
# structure in either of the first two sections whose arrays could be sized today --
# and they still cannot be allocated, because tile geometry and sparsity are unset.
COCHLEA_TUBE_MM = 35
COCHLEA_INNER_HAIR_CELLS = 3_500
COCHLEA_OUTER_HAIR_CELLS = 12_000
# The organ runs on a battery it supplies itself: the middle fluid compartment is held
# at a standing positive voltage, the endocochlear potential, supplied by the structure
# and not by the stimulus.  It is what the transduction current runs on and the reason
# the organ responds to vibrations of atomic dimension.  No figure is recorded.
COCHLEA_ENDOCOCHLEAR_POTENTIAL_V = None
# Abolishing prestin costs 40-60 dB, roughly a hundredfold.  An unamplified cochlea is
# not a degraded version of the same structure, which is why the mechanical loop cannot
# be staged.  The loop's output is observable from outside the head as otoacoustic
# emissions.
COCHLEA_AMPLIFIER_GAIN_DB = (40, 60)

COCHLEAR_NUCLEUS = Structure(
    "cochlear nucleus",
    (
        # A fan-in of one or two by axosomatic endbulb of Held gives log2(2) = 1.  The
        # structure's most timing-critical cell is its cheapest, and that is not a
        # coincidence: timing fidelity is bought by synapse morphology rather than by
        # circuitry, and a stage that averaged many afferents could not do it.  The
        # terminal is large enough to generate an extracellular prepotential before the
        # receiving cell's own spike, with exceptionally low jitter between the two.
        Population("spherical bushy cells", THRESHOLD_GATE, PER_HEMISPHERE, None, 2,
                   note="fan-in one or two and little else; extent unknown because the "
                        "~0.5M total partitions across neither divisions nor classes"),
        # Soft: no clean human count.  The architecture records this as a gap in what
        # has been counted rather than in what has been sectioned -- the structure has
        # been looked at and the number has not been taken, which is an experiment to
        # run and not a derivation to perform.
        Population("all other classes", THRESHOLD_GATE, PER_HEMISPHERE, 500_000, None,
                   note="T-stellate (spectrum), octopus (broadband onset by "
                        "coincidence), fusiform (monaural spectral-notch elevation "
                        "cues), inhibitory D-stellate, dorsal interneurons; fan-in "
                        + UNKNOWN),
    ),
    subelements=("anteroventral division", "posteroventral division", "dorsal division",
                 "spherical bushy", "globular bushy", "T-stellate", "D-stellate",
                 "octopus", "fusiform", "dorsal interneurons"),
    rank=3,
    axes=("division", "cell class", "position along the tonotopic axis"),
    partitions=False,
)
# Three divisions, each holding a complete tonotopic map -- three maps of frequency per
# side rather than one, so the tonotopic extent is repeated three times rather than
# divided three ways.
COCHLEAR_NUCLEUS_DIVISIONS = 3
# The division axis may not be indexable in a human.  The ventral cell classes lie
# intermixed within the cochlear nerve branches, so the boundary that defines the
# sub-elements may not be drawable -- which makes "onto the anteroventral division" a
# checkable endpoint in a cat and possibly not in us.  An array indexed on a boundary
# that cannot be drawn asserts a partition the tissue may not have.
COCHLEAR_NUCLEUS_DIVISION_AXIS_INDEXABLE = None

SUPERIOR_OLIVE = Structure(
    "superior olivary complex",
    (
        # Firm human unbiased stereology, among the few in the auditory brainstem.  The
        # two structures doing the localisation arithmetic are together smaller than a
        # rounding error against any cortical area in this section.
        Population("medial superior olive", THRESHOLD_GATE, PER_SIDE, 15_500, None,
                   note="extracts interaural time differences by coincidence detection "
                        "on a bipolar cell whose two dendrites point in opposite "
                        "directions -- one cell's two inputs segregated by compartment, "
                        "so the geometry is the computation"),
        Population("lateral superior olive", THRESHOLD_GATE, PER_SIDE, 5_600, None,
                   note="extracts interaural level differences as a subtraction: "
                        "ipsilateral excitation against contralateral inhibition"),
        # The calyx of Held is a one-to-one giant terminal, so fan-in is one and the
        # store is zero bits -- even a firm count would add nothing to the parameter
        # store.  A giant one-to-one terminal is how a sign inversion is bought without
        # adding jitter; averaging afferents to reach the same inversion would invert
        # the mechanism.
        Population("medial nucleus of the trapezoid body", THRESHOLD_GATE, PER_SIDE,
                   None, 1,
                   note="count is disputed rather than merely absent: reported as well "
                        "established by one line of work and as vestigial or absent by "
                        "four others"),
        Population("periolivary nuclei", THRESHOLD_GATE, PER_SIDE, None, None,
                   note="uncounted"),
    ),
    subelements=("medial superior olive", "lateral superior olive",
                 "medial nucleus of the trapezoid body",
                 "lateral nucleus of the trapezoid body", "periolivary nuclei"),
    rank=2,
    axes=("nucleus", "position along the tonotopic axis"),
    partitions=True,
)
# The medial superior olive's somata lie in a thin sagittal sheet with the two dendrites
# extending in opposite directions, so the structure is a sheet one cell thick with the
# binaural comparison across its thickness.  The thickness is not an extent to allocate;
# it is where the comparison happens.
#
# The coincidence detector's tuning is manufactured by timed glycinergic inhibition and
# not by a difference in axonal path length: blocking the inhibition shifts a cell's
# best interaural time difference toward zero.  That inverts the classical delay-line
# account, and it means the inhibitory internal edges are functional rather than
# modulatory.  An implementation treating inhibition here as a gain term has deleted the
# thing that sets the tuning.
#
# The output format is decoded and disputed, which is neither to derive nor settled:
# it has been measured and the readings disagree.  Three are live -- a place code in a
# map of interaural delay (verified in birds, and mammals evolved the computation
# independently), a hemispheric opponent population rate code read out by the slope of
# the response-azimuth function, and a chinchilla result finding best delays clustered
# near zero and inside the physiological range.  No array here is indexed by azimuth.
SUPERIOR_OLIVE_AZIMUTH_FORMAT = CONTESTED
# Least species-transferable structure in the pathway, and the disagreement is about
# which nuclei exist.  Every inhibitory internal edge originates in the trapezoid body,
# so if the human nucleus is absent, the sign-inverting term of the level computation
# and the timed inhibition that sets time-difference tuning arrive from somewhere else
# or work differently in us.  The edges are kept because the function is attested in
# human psychophysics; the substrate is recorded as disputed.

INFERIOR_COLLICULUS = Structure(
    "inferior colliculus",
    (
        # Verified human primary measurement, one of the firmest figures in the section.
        Population("central nucleus", THRESHOLD_GATE, PER_SIDE, 420_000, None,
                   note="lemniscal, tonotopic; built of 10-12 fibrodendritic laminae "
                        "each an isofrequency plane"),
        # ~0.6M whole colliculus less ~420,000 central leaves ~180,000, and the
        # architecture does not divide that between the two, so neither can be sized.
        Population("dorsal and external cortices", THRESHOLD_GATE, PER_SIDE, 180_000,
                   None,
                   note="non-lemniscal, multimodal, and where the descending cortical "
                        "projection lands; the split between the two is to derive"),
    ),
    subelements=("central nucleus", "dorsal cortex", "external cortex"),
    rank=3,
    axes=("division", "lamina", "position within lamina"),
    partitions=True,
)
# The partition is derivable and closes: ~420,000 over 10-12 laminae is ~35,000 to
# ~42,000 per lamina, in ~22.4 mm3 at ~18,750 neurons/mm3, consistent with the loose
# packing of subcortical relays and far below cortical density.  The lamina axis IS the
# frequency axis, which is what makes the shape and the map the same object here -- so
# unlike every cortical entry in these two sections, the tonotopic index needs no
# separate correspondence rule.
INFERIOR_COLLICULUS_LAMINAE = (10, 12)
INFERIOR_COLLICULUS_VOLUME_MM3 = 22.4
# Morphology does not predict sign here, which is unlike the rest of this section: both
# the disc-shaped class (confined to one lamina) and the stellate class (crossing two or
# more) can be glutamatergic or glycinergic/GABAergic.  An implementation that assigns
# sign by cell class has imported a rule this structure breaks.
#
# Across frequency bands the only stated route is the translaminar stellate cell, so any
# across-frequency integration here must take it.  That is a positive constraint on the
# topology rather than an absence.
#
# Obligatory is right; summed is not established.  Terminals from the different
# ascending pathways are interleaved in different sublaminae and remain functionally
# segregated at this level, so the lines all arrive in a shared tonotopic frame --
# whether they are combined here or merely brought into register is not settled by the
# anatomy, and the parallel structure the cochlear nucleus creates may survive this
# stage.  Nothing below combines them.
INFERIOR_COLLICULUS_LINES_COMBINED = None

MEDIAL_GENICULATE = Structure(
    "medial geniculate nucleus",
    (
        # Soft: no direct human count.  Bracketed two independent ways that agree --
        # comparability with the lateral geniculate nucleus's firm ~1.8M, and a volume
        # cross-check at that nucleus's ~17,000 neurons/mm3 against this one's verified
        # ~134 mm3, giving ~2.3M.  Neither is a direct human count.
        Population("relay cells", THRESHOLD_GATE, PER_HEMISPHERE, 2_050_000, None,
                   note="~1.8-2.3M soft; the store is quoted at the 2.05M midpoint"),
        # If the primate interneuron proportion holds, roughly a quarter of the total
        # are local inhibitory cells projecting nowhere outside the nucleus -- so they
        # are not part of the thalamocortical output.  That changes the output extent
        # without changing the array.
        Population("local interneurons", GRADED, PER_HEMISPHERE, None, None,
                   note="~25% of the total if the primate proportion holds; store is "
                        "not established"),
    ),
    subelements=("ventral division", "dorsal division", "medial division"),
    rank=3,
    axes=("division", "lamina", "position"),
    partitions=False,
)
# Row width is a measured pitch, one of the few in the map -- and it is a pitch and not
# an extent, so it constrains the lamina axis without sizing it.
MEDIAL_GENICULATE_ROW_WIDTH_UM = (50, 100)
MEDIAL_GENICULATE_VOLUME_MM3 = 134
# Roughly 20% of the collicular driving input is GABAergic to the ventral and medial
# divisions, ~11% to the dorsal.  The edge that sets what the message is also carries a
# substantial inhibitory component, so a stage modelling it as pure excitatory drive
# would be wrong about a fifth of it.  The sign is not a property of the edge; it is a
# mixture within the edge.
MEDIAL_GENICULATE_COLLICULAR_GABAERGIC = {"ventral": 0.20, "medial": 0.20, "dorsal": 0.11}
# The sharpest species-transfer hazard in the pathway.  The GABAergic local interneuron
# proportion runs from under 1% in bat and rat -- some divisions with none at all -- to
# 25% or more in cat and monkey, primate thalamus generally 25-30%.  This is specific to
# the auditory thalamus: the lateral geniculate nucleus holds about the same proportion
# across species, and so do the colliculus and auditory cortex.  Only this nucleus swings
# that way.  In rodent its inhibition comes from the reticular nucleus alone; in cat,
# monkey and by extension human there are two independent inhibitory systems.  A circuit
# for this structure taken from mouse would be missing an entire population present in us.

STRUCTURES = (COCHLEA, COCHLEAR_NUCLEUS, SUPERIOR_OLIVE, INFERIOR_COLLICULUS,
              MEDIAL_GENICULATE)

# Named here so the edges below can reach them honestly.  An entry not yet written is
# not the same as a structure with no entry anywhere, and typing it as either LOCAL or
# NO_ENTRY would state something false.
PRIMARY_AUDITORY_CORTEX = "primary auditory cortex"
AUDITORY_BELT = "auditory belt"
AUDITORY_PARABELT = "auditory parabelt"

# --------------------------------------------------------------------------
# Edges.
# --------------------------------------------------------------------------

EDGES: tuple[Edge, ...] = (

    # --- cochlea --------------------------------------------------------
    Edge(class_endpoint("sound-pressure vibration, via the middle ear"),
         here("cochlea", "inner hair cells"),
         carries="mechanical, not a neural edge",
         role=ROUTING,
         representation=Representation("sound pressure", TO_DERIVE, EVENT_DRIVEN,
                                       NO_FRAME),
         note="an acoustic arrival; fan-in is " + NOT_APPLICABLE + ". The input has no "
              "coordinate frame and the outputs do, and the structure between them "
              "supplies the frame mechanically -- the one place in this file where a "
              "frame is created rather than inherited or transformed"),

    Edge(here("superior olivary complex"), here("cochlea", "outer hair cells"),
         carries="a gain command, no stimulus content",
         role=MODULATORY,
         representation=Representation("gain command", TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic position"),
         note="medial olivocochlear efferents. The brain sets the gain of its own front "
              "end before transduction: this is the map's most complete descending "
              "loop, closing on the transducer itself, and without it the front end has "
              "no set point"),

    Edge(far("branchiomotor / visceromotor nuclei", CRANIAL_NERVE_NUCLEI),
         here("cochlea"),
         carries="the acoustic reflex's attenuation, indirectly via the stapedius muscle",
         role=MODULATORY,
         representation=Representation("attenuation", TO_DERIVE, EVENT_DRIVEN, NO_FRAME),
         note="the effector is a middle-ear muscle, outside scope, so this is an "
              "influence on the acoustic input rather than an edge onto neural "
              "structure. The named producer has an entry and it declares the muscle, "
              "not this loop: its facial nucleus drives stapedius and its output line "
              "to orofacial striated muscle carries it, so the efferent half of this "
              "reflex is written at both ends. The afferent half is written at neither "
              "-- that entry declares no auditory input of any kind, and the drive onto "
              "it is declared only at this file's superior olivary complex, where the "
              "endpoint names an arc rather than a nucleus"),

    Edge(here("cochlea", "inner hair cells, via type I spiral ganglion neurons"),
         here("cochlear nucleus"),
         carries="energy in one narrow frequency band as a function of time, "
                 "tonotopically ordered, with waveform timing preserved by phase "
                 "locking at low frequencies",
         representation=Representation("energy per narrow band over time", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       "tonotopic, rank 1 -- position is frequency"),
         fan_out=30,
         note="~30,000 fibres. Fan-out 5-30 type I neurons per inner hair cell, fan-in "
              "exactly one: a pure divergence with no convergence at all. Waveform "
              "timing is part of the payload here and not the schedule it arrives on"),

    Edge(here("cochlea", "outer hair cells, via type II spiral ganglion neurons"),
         here("cochlear nucleus"),
         carries="not sound: the current reading is a damage signal from the organ of "
                 "Corti",
         representation=Representation("damage signal", TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic position"),
         note="~5-10% of the ganglion, unmyelinated, not required for hearing. It runs "
              "on the same nerve, in the same tonotopic order, to the same target, and "
              "it is not audition -- a consumer reading the auditory nerve as one bus "
              "of ~30,000 sound-carrying fibres has absorbed ~2,500 damage-signal "
              "fibres into the spectrum"),

    Edge(here("cochlea", "outer hair cells"), here("cochlea", "basilar membrane"),
         carries="force, added back into the travelling wave through prestin, a "
                 "voltage-driven membrane protein that changes cell length directly",
         role=ROUTING,
         representation=Representation("force", TO_DERIVE, "continuous, mechanical",
                                       "tonotopic position"),
         note="the cochlear amplifier: a mechanical feedback loop inside the sensory "
              "organ, fan-in and fan-out " + NOT_APPLICABLE + " because the transfer is "
              "mechanical. With light at the retina and the endocrine limbs elsewhere "
              "in the map, this is the third class of edge that takes real time and is "
              "not conduction plus synaptic transmission. It cannot be staged and is "
              "not a refinement: an unamplified cochlea is 40-60 dB less sensitive"),

    # --- cochlear nucleus -----------------------------------------------
    # Every auditory nerve fibre bifurcates on entry and reaches all three divisions, so
    # what differs between the labelled lines is the terminal type and the receiving
    # cell's intrinsic properties, not the source.  The lines are not parallel
    # processing of different inputs; they are different readings of the same input.  An
    # implementation that routes different inputs to different cell classes has built a
    # demultiplexer, and the structure is not one.
    Edge(unstemmed("dorsal column nuclei and trigeminal relay"),
         here("cochlear nucleus", "dorsal division, by way of the granule cells"),
         carries="somatosensory state of head, face, neck and pinna, for cancelling "
                 "self-generated sound",
         representation=Representation("somatosensory state", TO_DERIVE, EVENT_DRIVEN,
                                       "somatotopic -- not tonotopic"),
         note="the frame is not the one this structure uses and neither end supplies a "
              "correspondence. A signal cannot be subtracted from another until the two "
              "are on one axis, and self-motion cancellation is exactly a subtraction"),
    Edge(unstemmed("semicircular canals, otolith organs and vestibular nuclei"),
         here("cochlear nucleus", "dorsal division, by way of the granule cells"),
         carries="head rotation rate and gravito-inertial acceleration",
         representation=Representation("rotation rate and acceleration", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       "head-centred / gravito-inertial -- not tonotopic"),
         note="same correspondence gap as the row above"),
    Edge(pending(PRIMARY_AUDITORY_CORTEX), here("cochlear nucleus"),
         carries="gain and expectation, no new stimulus content",
         role=MODULATORY,
         representation=Representation("gain and expectation", TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, in register")),
    Edge(here("inferior colliculus"), here("cochlear nucleus"),
         carries="gain and expectation, no new stimulus content",
         role=MODULATORY,
         representation=Representation("gain and expectation", TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, in register")),
    Edge(here("superior olivary complex"), here("cochlear nucleus"),
         carries="inhibition, no content",
         role=MODULATORY,
         representation=Representation("inhibition", TO_DERIVE, EVENT_DRIVEN, TONOTOPIC),
         note="glycinergic"),

    Edge(here("cochlear nucleus", "spherical bushy cells"),
         here("superior olivary complex", "medial superior olive, bilaterally"),
         carries="the spectral vector with sub-millisecond arrival timing preserved, "
                 "monaural, one per ear; not itself a localisation signal but what the "
                 "differences are computed from",
         representation=Representation("phase-locked spectral vector", TO_DERIVE,
                                       EVENT_DRIVEN,
                                       "tonotopic, one copy per ear, neither carrying "
                                       "azimuth"),
         note="the payload is a pair and the pairing is the point: the difference is "
              "not taken until it arrives. These are two lines rather than one, the "
              "same payload distinguished only by arrival time, so equal latency would "
              "delete the function rather than approximate it"),
    Edge(here("cochlear nucleus", "spherical bushy cells"),
         here("superior olivary complex", "lateral superior olive, ipsilateral"),
         carries="the same monaural vector as excitation, uninverted; the positive term "
                 "of the subtraction",
         representation=Representation("phase-locked spectral vector", TO_DERIVE,
                                       EVENT_DRIVEN, TONOTOPIC_MONAURAL)),
    Edge(here("cochlear nucleus", "globular bushy cells"),
         here("superior olivary complex",
              "medial nucleus of the trapezoid body, contralateral"),
         carries="the same vector, which that nucleus then sign-inverts",
         representation=Representation("phase-locked spectral vector", TO_DERIVE,
                                       EVENT_DRIVEN, TONOTOPIC_MONAURAL),
         note="fan-in one: the calyx of Held is a one-to-one giant terminal"),

    Edge(here("cochlear nucleus", "T-stellate cells"),
         here("inferior colliculus", "central nucleus"),
         carries="the spectrum, rate-coded per band, timing not preserved",
         representation=Representation("spectrum, rate-coded per band", TO_DERIVE,
                                       EVENT_DRIVEN, TONOTOPIC),
         note="timing is preserved on the bushy line and discarded here, from the same "
              "input -- which is what a labelled line means at this rung"),
    Edge(here("cochlear nucleus", "octopus cells"),
         here("inferior colliculus", "central nucleus"),
         carries="broadband onset, a coincidence event marking a transient",
         representation=Representation("onset event", TO_DERIVE, EVENT_DRIVEN,
                                       "broadband: across the tonotopic array rather "
                                       "than at a position on it"),
         note="the octopus cell detects coincidence across the tonotopic array at the "
              "highest temporal precision in the brain, which makes the spread across "
              "its afferents the computation rather than a property of it. With every "
              "afferent latency set equal the spread is zero and the cell computes "
              "nothing. Its output is indexed by time rather than by place, and an "
              "array laid out on the tonotopic axis has nowhere to put it"),
    Edge(here("cochlear nucleus", "fusiform cells"),
         here("inferior colliculus", "central nucleus"),
         carries="monaural spectral-notch cues for elevation, with the self-motion "
                 "signal already subtracted",
         representation=Representation("spectral-notch elevation cue", TO_DERIVE,
                                       EVENT_DRIVEN, "tonotopic, and it encodes "
                                       "elevation")),

    # --- superior olivary complex ---------------------------------------
    Edge(pending(PRIMARY_AUDITORY_CORTEX), here("superior olivary complex"),
         carries=TO_DERIVE, role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, in register")),
    Edge(here("inferior colliculus"), here("superior olivary complex"),
         carries=TO_DERIVE, role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, in register")),

    Edge(here("superior olivary complex"),
         here("inferior colliculus", "central nucleus, bilaterally"),
         carries="horizontal sound location (azimuth); elevation is not on it",
         representation=Representation("azimuth", CONTESTED, EVENT_DRIVEN,
                                       "azimuth, and the form is decoded and disputed"),
         note="lateral lemniscus. This is the edge where timing stops being the payload "
              "and azimuth starts being it. What form azimuth takes on this wire is "
              "contested and the architecture must not assume a place code -- the one "
              "line in either of the first two sections whose representation is "
              "contested rather than to derive: it has been measured and the readings "
              "disagree. The consumer carries the instruction with it: a consumer of "
              "this edge must not assume a map"),

    Edge(here("superior olivary complex"), route("the acoustic-reflex arc (stapedius)"),
         carries="a loudness-triggered attenuation command; the effector is outside scope",
         representation=Representation("attenuation command", TO_DERIVE, EVENT_DRIVEN,
                                       NO_FRAME),
         note="this endpoint names a circuit and not a structure, and the structure it "
              "should name has an entry: the arc runs through the facial motor nucleus, "
              "a named sub-element of " + CRANIAL_NERVE_NUCLEI + "'s branchiomotor and "
              "visceromotor entry -- the one structure in that section with a firm human "
              "count, ~10,000 per side, corroborated against the myelinated-axon count "
              "of its own nerve. That entry declares the efferent limb to stapedius and "
              "declares no auditory input at all, so this edge has a producer here and "
              "no consumer there. The failure is in the endpoint's kind rather than in "
              "its spelling: a route cannot declare an input back, so no diff at either "
              "end can pair this edge, and it reads as terminating outside scope when "
              "its next stage is a counted nucleus two files away. An endpoint naming a "
              "loop hides a structure the same way a class endpoint hides a member, and "
              "it is worse in one respect -- a class is visibly unresolved, while an arc "
              "reads as a complete description. Owed at the source: retype to the facial "
              "motor nucleus, keeping stapedius as the terminus beyond it. Not retyped "
              "here, because changing an endpoint at this rung re-terminates an edge the "
              "source still carries as written"),

    # --- inferior colliculus --------------------------------------------
    Edge(no_entry("nuclei of the lateral lemniscus"),
         here("inferior colliculus", "central nucleus, bilaterally"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="these have no entry anywhere in the source, so this edge terminates at a "
              "structure the description does not describe. Inherited, and not repaired "
              "at this rung"),
    Edge(pending(PRIMARY_AUDITORY_CORTEX),
         here("inferior colliculus",
              "mainly the dorsal and external cortices, not the central nucleus"),
         carries="gain and expectation",
         role=MODULATORY,
         representation=Representation("gain and expectation", TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, in register"),
         note="heavy descending, and the termination is the finding: it avoids the "
              "central nucleus"),
    Edge(here("inferior colliculus"), here("inferior colliculus"),
         carries="commissural, to and from the contralateral copy",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, the far side's"),
         note="the per-side basis makes the far end a second instance of this structure "
              "rather than a different structure"),

    Edge(here("inferior colliculus", "central nucleus"),
         here("medial geniculate nucleus", "ventral division"),
         carries="the assembled auditory scene: tonotopic spectrum, periodicity and "
                 "duration tuning, and the binaural cues bound with the monaural "
                 "elevation cue",
         representation=Representation("the assembled auditory scene", TO_DERIVE,
                                       EVENT_DRIVEN, TONOTOPIC),
         note="brachium. A named majority source class: cholecystokinin disc-shaped "
              "neurons, ~63% of the excitatory population, projecting exclusively to "
              "that division -- the only named majority source class on any edge in "
              "either of the first two sections, and a fact about the topology rather "
              "than about the store"),
    Edge(here("inferior colliculus", "dorsal and external cortices"),
         here("medial geniculate nucleus", "dorsal and medial divisions"),
         carries="the non-lemniscal, broadly tuned signal",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "non-tonotopic")),
    Edge(here("inferior colliculus"), unstemmed("superior colliculus"),
         carries="auditory azimuth and elevation in a frame the orienting map can "
                 "register against the visual one",
         representation=Representation("azimuth and elevation", TO_DERIVE, EVENT_DRIVEN,
                                       "an orienting frame, registrable against a "
                                       "retinotopic one"),
         note="the one line in this section explicitly built to be registered against "
              "another modality's frame, and it names the requirement without supplying "
              "the correspondence. The visual side of that registration arrives "
              "retinotopically, and neither end states the transform between the two"),

    # --- medial geniculate nucleus --------------------------------------
    Edge(pending(PRIMARY_AUDITORY_CORTEX, "layer 6"),
         here("medial geniculate nucleus", "all three divisions"),
         carries="modulatory, no new content",
         role=MODULATORY,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "tonotopic, in register"),
         note="small terminals. Two edges from one structure, opposite in kind, "
              "distinguished by terminal morphology"),
    Edge(pending(PRIMARY_AUDITORY_CORTEX, "layer 5"),
         here("medial geniculate nucleus", "dorsal and medial divisions"),
         carries="cortical content, as a driver",
         role=DRIVER,
         representation=Representation("cortical content", TO_DERIVE, EVENT_DRIVEN,
                                       "cortical, not the ascending frame"),
         note="giant terminals are the signature of a driver, and this is what makes "
              "those two divisions higher-order. They cannot function at all without "
              "it, so for them co-instantiation is not a discipline but a precondition"),
    Edge(unstemmed("thalamic reticular nucleus"), here("medial geniculate nucleus"),
         carries="inhibition, the gate",
         role=MODULATORY,
         representation=Representation("inhibition", TO_DERIVE, EVENT_DRIVEN,
                                       "auditory sector of the reticular sheet"),
         note="that nucleus's auditory sector is itself layered by relay class, so the "
              "gate is applied separately to the first-order and higher-order relays"),

    Edge(here("medial geniculate nucleus", "ventral division"),
         pending(PRIMARY_AUDITORY_CORTEX),
         carries="the lemniscal payload, sharply tonotopic, relayed and gated, not "
                 "transformed",
         representation=Representation("the lemniscal payload", TO_DERIVE, EVENT_DRIVEN,
                                       "sharply tonotopic")),
    Edge(here("medial geniculate nucleus", "dorsal division"),
         pending(AUDITORY_BELT + " and " + AUDITORY_PARABELT),
         carries="the non-tonotopic, broadly tuned signal, and on the higher-order limb, "
                 "cortical content returning from layer 5",
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN,
                                       "non-tonotopic")),
    Edge(here("medial geniculate nucleus", "medial division"),
         class_endpoint("wide cortical targets and the amygdala"),
         carries="a coarse, broadly tuned multisensory alarm signal: enough to say "
                 "something loud and sudden happened, roughly there, and not enough to "
                 "identify it",
         representation=Representation("multisensory alarm", TO_DERIVE, EVENT_DRIVEN,
                                       "coarse and roughly spatial -- not tonotopic"),
         note="the payload is impoverished by design, and that is what makes it fast. A "
              "consumer reading it as a degraded copy of the ventral payload has "
              "mistaken a design for a deficiency"),
    Edge(here("medial geniculate nucleus", "medial division and associated nuclei"),
         here("inferior colliculus"),
         carries=TO_DERIVE,
         representation=Representation(TO_DERIVE, TO_DERIVE, EVENT_DRIVEN, TO_DERIVE),
         note="with a specific negative alongside: the ventral and dorsal divisions send "
              "no return projection to the colliculus, so the descending limb does not "
              "mirror the ascending one"),
)

# --------------------------------------------------------------------------
# Derived sizing -- recomputed from counts and fan-ins, not transcribed.
# --------------------------------------------------------------------------


def zero_bit_populations() -> str:
    """Thresholds absent by derivation rather than by omission.

    A fan-in of exactly one gives log2(1) = 0: there is no count to compare against, so
    the array does not exist.  Allocating a zero-length array would assert a store the
    structure has not got; leaving the row out silently would read as an oversight.
    """
    out = []
    for s in STRUCTURES:
        for p in s.populations:
            if p.fan_in == 1:
                out.append(f"  {s.name} / {p.name}: fan-in 1 -> 0 bits, no array")
    return "\n".join(out)


def colliculus_partition_closes() -> str:
    lo, hi = INFERIOR_COLLICULUS_LAMINAE
    n = INFERIOR_COLLICULUS.populations[0].count
    return (f"  {n:,} over {lo}-{hi} laminae = {n//hi:,} to {n//lo:,} per lamina\n"
            f"  {n:,} in {INFERIOR_COLLICULUS_VOLUME_MM3} mm3 = "
            f"{round(n/INFERIOR_COLLICULUS_VOLUME_MM3):,} neurons/mm3")


def geniculate_brackets() -> str:
    """Two independent brackets that agree, neither a direct human count."""
    volume_estimate = MEDIAL_GENICULATE_VOLUME_MM3 * 17_000
    return (f"  comparability with the lateral geniculate nucleus: ~1,800,000\n"
            f"  volume cross-check {MEDIAL_GENICULATE_VOLUME_MM3} mm3 x 17,000/mm3 = "
            f"{volume_estimate:,}\n"
            f"  the two bracket the ~1.8-2.3M figure; neither is a direct human count")


def timing_is_the_payload() -> str:
    """Where a uniform update interval would delete a function rather than blur it."""
    return (
        "  medial superior olive : two bilateral inputs, same payload, distinguished\n"
        "                          ONLY by arrival time -- equal latency computes nothing\n"
        "  octopus cell          : computes the spread across its afferents; equal\n"
        "                          latency makes the spread zero\n"
        "  auditory nerve        : phase locking makes waveform timing part of the\n"
        "                          payload, not the schedule it arrives on\n"
        "  scale                 : tens of microseconds, stated qualitatively, no figure")


def pending_entries() -> str:
    """Edges declared here whose far end is a structure in this file, not yet written."""
    out = []
    for e in EDGES:
        for end, direction in ((e.source, "<-"), (e.target, "->")):
            if end.kind == "pending":
                near = e.target.name if direction == "<-" else e.source.name
                out.append(f"  {near[:34]:34} {direction} {end.name[:38]:38}"
                           f"{' / ' + end.sub if end.sub else ''}")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report(STRUCTURES, f"Brain {STEM}  (structures 1-5 of 11)"))
    print()
    print("thresholds absent by derivation:")
    print(zero_bit_populations())
    print()
    print("the one partition that closes:")
    print(colliculus_partition_closes())
    print()
    print("the count derived by two agreeing brackets:")
    print(geniculate_brackets())
    print()
    print("where uniform latency deletes a function rather than blurring it:")
    print(timing_is_the_payload())
    print()
    print(edge_report(EDGES))
    print()
    print("edges reaching an entry not yet written in this file:")
    print(pending_entries())
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
