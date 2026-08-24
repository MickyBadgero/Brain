"""Brain — cerebellum: cortex, deep nuclei, and the inferior olive.

Three structures and one microcircuit repeated on a massive scale. The cerebellar
cortex holds ~69B neurons - about 80% of all the brain's - in ~10% of its volume,
and it is the best-counted part of the brain, so this section enters with hard
numbers where the others enter with soft ones.

Counting basis is the whole cerebellum, both sides, with the per-hemisphere value
alongside. Second section worked whose basis is not per hemisphere.

This section is a finding against the forward model's central simplification, and
the finding arrives twice from two directions.

The model is a threshold gate over EQUAL-WEIGHT inputs: it fires when the count of
active inputs crosses a stored threshold, and equal weights are what collapse a
neuron's stored state to that one number. The design file says in advance that a
threshold is real structure and equal weights are not, and that a structure the
source describes as computing with graded weights is a finding against the model
rather than a structure to be flattened to fit it. This is that structure.

First: the one wins. A Purkinje cell receives ~335,000 parallel fibres and exactly
one climbing fibre, and the climbing fibre drives an all-or-none complex spike
whatever the parallel fibres are doing. Under equal weights one active input adds 1
to a count that can reach 335,001. For one input to override 335,000 others its
weight must be about five orders of magnitude larger than theirs, which is the
assumption the model removes.

Second: the plasticity operates on the assumption itself. The complex spike
depresses the parallel-fibre-Purkinje synapse - long-term depression, one synapse at
a time. A model that stores one number per neuron because its synapses are equal by
construction has nowhere to put a change to one synapse of 335,000.

Neither is repaired here. Extending or replacing the model is not this rung's
decision, and the cost of the obvious extension is computed rather than assumed:
see synapse_store_if_weights_are_per_synapse().

Every edge latency reads None, meaning to derive. The climbing fibre carries a
stated timing requirement - it must arrive while the error is still present or it
teaches nothing - with no number on the latency and none on the window.

The vocabulary is imported and not redefined. Structure, Population, Endpoint,
Representation and Edge are declared once, in Brain_config, because an edge that
leaves this file is declared at both ends in two files, and two files cannot
describe one edge in agreement when the type describing it is defined twice. What
stays here is the content: the counts, shapes, extents and findings, which is where
they are derived and where a fidelity pass diffs them against the architecture.
"""

from math import ceil, log2

from Brain_config import (
    # element classes
    THRESHOLD_GATE,
    # open states
    TO_DERIVE, NOT_APPLICABLE, UNKNOWN, OWED,
    # counting bases
    WHOLE,
    # endpoint kinds and constructors
    Endpoint, far, here, no_entry, class_endpoint,
    # representation
    Representation, EVENT_DRIVEN, NO_FRAME,
    # populations and structures
    Population, Structure, FAN_IN_CEILING_BITS,
    # edges
    Edge, DRIVER, MODULATORY,
    # reports
    edge_report as config_edge_report,
    representation_report,
)

BASIS = WHOLE + " cerebellum, both sides"

# Count states for the sub-element slots. These are not element classes and do not
# belong in the shared vocabulary: they record how well the source counted a slot,
# which is content and differs per file.
COUNTED = "counted"
SOFT = "recorded as soft, no figure"

# --------------------------------------------------------------------------
# Structures. Populations carry the counts and fan-ins; the count state of each
# slot is held alongside, keyed by (structure, population).
# --------------------------------------------------------------------------

CEREBELLAR_CORTEX = Structure(
    name="cerebellar cortex",
    populations=(
        # The lowest fan-in in the map, and the reason the granule layer can expand
        # rather than average: a cell with four inputs cannot average anything.
        Population("granule cells", THRESHOLD_GATE, BASIS, count=69_000_000_000,
                   fan_in=4,
                   note="3-7 dendrites, ~4 in human, one mossy input each; "
                        "essentially the entire count, and the most abundant neuron "
                        "in the central nervous system"),
        # The highest fan-in in the map, and the one place the 16-bit log2 ceiling
        # is exceeded. The figure moved: the widely-cited ~175,000 is a retired rat
        # estimate; ~335,000 is direct human reconstruction.
        Population("Purkinje cells", THRESHOLD_GATE, BASIS, count=30_500_000,
                   fan_in=335_000,
                   note="~300,000-500,000 spines, headline ~360,000, ~93% carrying a "
                        "presynaptic partner -> ~335,000 parallel-fibre synapses, plus "
                        "the single climbing fibre; the sole output of the cortex, "
                        "inhibitory onto the deep nuclei"),
        Population("Golgi cells", THRESHOLD_GATE, BASIS,
                   note="projects back onto granule cells; the loop that keeps the "
                        "granule population sparse"),
        Population("stellate cells", THRESHOLD_GATE, BASIS,
                   note="onto Purkinje dendrites"),
        Population("basket cells", THRESHOLD_GATE, BASIS,
                   note="onto the Purkinje soma and initial segment"),
    ),
    rank=3,
    axes=("lamina", "H", "W"),
    partitions=False,
)

DEEP_NUCLEI = Structure(
    name="deep cerebellar nuclei",
    populations=(
        Population("dentate nucleus", THRESHOLD_GATE, BASIS, count=5_000_000,
                   note="lateral, the largest; reads the cognitive and association "
                        "hemispheres; to the thalamus and the parvocellular red nucleus"),
        Population("interposed nuclei (globose and emboliform)", THRESHOLD_GATE, BASIS,
                   note="paravermal, limb coordination; to the magnocellular red "
                        "nucleus. Counted as one nucleus or two - the source records "
                        "the ambiguity and does not resolve it"),
        Population("fastigial nucleus", THRESHOLD_GATE, BASIS,
                   note="medial; vermal and flocculonodular - axial posture, balance, "
                        "eye movements; to the vestibular nuclei and reticular formation"),
    ),
    rank=2,
    axes=("division", "N"),
    partitions=False,
)

INFERIOR_OLIVE = Structure(
    name="inferior olive",
    populations=(
        Population("principal olive, medial and dorsal accessory olives",
                   THRESHOLD_GATE, BASIS,
                   note="conventionally divided and addressing different cerebellar "
                        "zones, but no subdivision is named in the entry. It matters "
                        "because the output payload's only addressing is 'which "
                        "population'"),
        Population("cell classes", THRESHOLD_GATE, BASIS,
                   note="not enumerated anywhere in the entry"),
    ),
    rank=2,
    axes=("cell class", "N"),
    partitions=False,
)

STRUCTURES = (CEREBELLAR_CORTEX, DEEP_NUCLEI, INFERIOR_OLIVE)

# The count state of every sub-element slot, keyed by (structure name, population
# name). Held here rather than on Population because it is a statement about how
# well the source counted this section, not part of the shared vocabulary.
SLOT_STATE = {
    ("cerebellar cortex", "granule cells"): COUNTED,
    ("cerebellar cortex", "Purkinje cells"): COUNTED,
    ("cerebellar cortex", "Golgi cells"): OWED,
    ("cerebellar cortex", "stellate cells"): OWED,
    ("cerebellar cortex", "basket cells"): OWED,
    ("deep cerebellar nuclei", "dentate nucleus"): COUNTED,
    ("deep cerebellar nuclei", "interposed nuclei (globose and emboliform)"): SOFT,
    ("deep cerebellar nuclei", "fastigial nucleus"): SOFT,
    ("inferior olive", "principal olive, medial and dorsal accessory olives"): OWED,
    ("inferior olive", "cell classes"): UNKNOWN,
}

# Laminar and tangential organisation. Not a Structure field at this rung; recorded
# here because the shape classes have no slot for either and the gap is the finding.
LAMINAE = {
    "cerebellar cortex": "three - molecular, Purkinje cell, granular. The eight-layer "
                         "isocortical block does not apply; this is the furthest of "
                         "the nine exception entries from it, being the only one whose "
                         "tissue is not cerebral cortex",
    "deep cerebellar nuclei": NOT_APPLICABLE + " - nuclei, not cortex",
    "inferior olive": NOT_APPLICABLE,
}

TANGENTIAL = {
    "cerebellar cortex": "the parallel fibre: a lattice, not a parcellation. An edge "
                         "cannot terminate on a compartment here",
    "deep cerebellar nuclei": "the zonal correspondence with the cortex is the "
                              "organisation, and it is owed: which Purkinje zone "
                              "projects to which nucleus is stated only as a matching",
    "inferior olive": "the gap-junction coupling is the organisation and it is not a "
                      "parcellation: a coupled cluster is a dynamic grouping rather "
                      "than an anatomical compartment. Whether the clusters have fixed "
                      "boundaries an edge could terminate on is owed",
}

# --------------------------------------------------------------------------
# Measured figures the module re-derives rather than transcribes.
# --------------------------------------------------------------------------

PURKINJE_SYNAPSES = 335_000
GRANULE_TOTAL = 69_000_000_000
PURKINJE_TOTAL = 30_500_000

# The other primary method, and the only term that moves this section's figure.
STEREOLOGY_GRANULE_ONLY = (101_000_000_000, 109_000_000_000)

RETIRED = (
    (175_000, "a rat parallel-fibre estimate, widely cited for human"),
    (1e14, "a parallel-fibre-Purkinje contact total that reconciles with nothing"),
)

# The design file's own worked example, which brackets the retired figure.
DESIGN_FILE_EXAMPLE = (150_000, 200_000, 18)

SURFACE_CM2 = {"cerebellar cortex": 1590.0, "dentate nucleus": 18.6}
VOLUME_CM3_IN_VIVO = (130.0, 150.0)
WHOLE_BRAIN_NEURONS = 86_000_000_000

# Rat fan-out figures. Labelled, because mixing them with human counts is not a
# valid check and the module says so rather than reporting a discrepancy.
RAT_MOSSY_TO_GRANULE = 500
RAT_MOSSY_TO_PURKINJE = 150_000
INPUT_FIBRE_ORDER = 200_000_000

# --------------------------------------------------------------------------
# Edges.
#
# Every cross-file endpoint carries the far file's stem, <nn>_<section>, never its
# number alone. A bare number goes silently wrong the moment a file is split or
# renumbered, and the code has no reader to notice; Endpoint's own validation
# rejects a stem that does not begin <nn>_.
# --------------------------------------------------------------------------

# Payload states. How well the source types what an edge carries, which is content.
NAMED = "named without units, range or frame"
PARTIAL = "one component named, the rest owed"
PAYLOAD_OWED = "owed"
TYPED = "typed: content, addressing and a timing condition all stated"

CX = "cerebellar cortex"
DN = "deep cerebellar nuclei"
IO = "inferior olive"

# The far files this section reaches, by stem.
S_SENSES = "03_other_senses"
S_SENSORIMOTOR = "05_sensorimotor_loop"
S_THALAMUS = "12_thalamus"
S_NEUROMOD = "13_neuromodulatory_systems"
S_BRAINSTEM = "14_brainstem_midbrain_hypothalamus"
S_SPINAL = "16_spinal_cord"

# The climbing fibre is the best-typed payload in the sections worked: content,
# addressing and a timing condition are all stated. It is the one Representation
# here that is not entirely to derive.
CLIMBING_FIBRE_REP = Representation(
    units="one all-or-none complex spike per event",
    value_range="binary: it fired or it did not",
    update_timing=EVENT_DRIVEN + ", and it must arrive while the error is still "
                                 "present or it teaches nothing - the window has no number",
    frame=NO_FRAME + " - not a magnitude and not a direction, a WHEN; the only "
                     "addressing is which coupled population fired",
)

INTERNAL_EDGES: tuple[Edge, ...] = (
    Edge(here(CX, "mossy-fibre terminals"), here(CX, "granule cells"),
         carries="the afferent payload, whichever of the four mossy systems it "
                 "arrived on; fan-out ~500 granule cells per mossy fibre (rat)",
         note="the mossy limb does not resolve to one producer - four sources, one "
              "with no entry; splitting this line by source is owed"),
    Edge(here(CX, "granule cells"), here(CX, "Purkinje cells"),
         carries="the expansion-recoded afferent payload: the same information in a "
                 "different code, spread into an enormous sparsely-active population "
                 "so that patterns which arrived similar leave separable. This is the "
                 "entry's payload change and the point of the structure"),
    Edge(here(CX, "granule cells"), here(CX, "Golgi cells"),
         carries="via the parallel fibres"),
    Edge(here(CX, "Golgi cells"), here(CX, "granule cells"),
         carries="feedback inhibition onto the expansion stage; no content. This is "
                 "the loop that keeps the granule population sparse, which the "
                 "expansion recoding depends on, and the entry asserts the sparseness "
                 "without it",
         role=MODULATORY),
    Edge(here(CX, "granule cells"), here(CX, "stellate cells"),
         carries="via the parallel fibres"),
    Edge(here(CX, "granule cells"), here(CX, "basket cells"),
         carries="via the parallel fibres"),
    Edge(here(CX, "stellate cells"), here(CX, "Purkinje cells"),
         carries="feedforward inhibition onto the output stage, on the dendrites; "
                 "no content",
         role=MODULATORY),
    Edge(here(CX, "basket cells"), here(CX, "Purkinje cells"),
         carries="feedforward inhibition, on the soma and initial segment; no content",
         role=MODULATORY),
    # The one non-synaptic internal edge in the sections worked.
    Edge(here(IO, "olivary neuron"), here(IO, "olivary neuron"),
         carries="electrotonic coupling of subthreshold oscillations, producing the "
                 "near-synchronous burst. These neurons are among the most densely "
                 "gap-junction-coupled in the brain",
         role=MODULATORY,
         note="non-synaptic: gap junctions, not a synaptic projection"),
)

EDGES: tuple[Edge, ...] = INTERNAL_EDGES + (
    # ---- cerebellar cortex, in ----
    Edge(no_entry("pontine nuclei"), here(CX, "granule cells"),
         carries="an integrated mixture of cortical activity - intention, plan and "
                 "context drawn from many cortical areas at once and NOT a copy of any "
                 "one of them; mossy fibres, middle cerebellar peduncle, crossed",
         note="no entry in any file, and it computes - see PONTINE_TRANSFORM"),
    Edge(far("spinocerebellar tracts", S_SPINAL), here(CX, "granule cells"),
         carries="body proprioception - the actual configuration, unconscious; "
                 "ipsilateral",
         note="two-ended: the producer declares it"),
    Edge(far("external cuneate nucleus", S_SENSORIMOTOR), here(CX, "granule cells"),
         carries="proprioception only. The producer records that this edge and its "
                 "thalamocortical sibling carry the same payload to two destinations "
                 "of different kinds - one becoming a reportable percept, one writing "
                 "procedural change",
         note="two-ended: the producer declares it and names the sub-element"),
    Edge(far("semicircular canals, otolith organs, and vestibular nuclei", S_SENSES),
         here(CX, "granule cells"),
         carries="rotation rate and gravito-inertial acceleration, and the nuclei's "
                 "computed estimate; to the flocculonodular lobe",
         note="this line names three sources at once and splitting it is owed here; "
              "the far end supplies every term the split needs"),
    Edge(here(IO), here(CX, "Purkinje cells"),
         carries="the instructive error signal - one all-or-none complex spike saying "
                 "that was wrong. One bit with a timestamp: it must arrive while the "
                 "error is still present or it teaches nothing. Fan-in exactly one",
         representation=CLIMBING_FIBRE_REP,
         note="producer is in this file and declares it"),
    Edge(far("locus coeruleus", S_NEUROMOD), here(CX),
         carries=TO_DERIVE + " - noradrenaline setting global gain, in the producer's terms",
         role=MODULATORY,
         note="a named edge at the far end, not a brain-wide class"),

    # ---- cerebellar cortex, out ----
    Edge(here(CX, "Purkinje cells"), here(DN),
         carries="graded inhibition - the Purkinje sheet's summed verdict on the "
                 "expansion-recoded input. The cortex projects nowhere else except "
                 "the vestibular line",
         note="consumer is in this file and declares it"),
    Edge(here(CX, "flocculonodular lobe"), far("vestibular nuclei", S_SENSES),
         carries="graded inhibition, direct. The one exception to 'the cortex projects "
                 "nowhere else', and it sits inside the clause asserting the rule",
         note="producer-only: the far end declares no matching input"),

    # ---- deep nuclei, in ----
    Edge(here(CX, "Purkinje cells"), here(DN),
         carries="graded inhibition - the cortex's verdict",
         note="producer is in this file"),
    Edge(class_endpoint("collaterals of the mossy and climbing afferents"), here(DN),
         carries="the raw input, excitatory, arriving alongside the verdict on it",
         note="the climbing limb has a producer in this file; the mossy limb does not "
              "resolve - four sources, one with no entry and two unchecked. Owed: "
              "split this line by source"),

    # ---- deep nuclei, out ----
    Edge(here(DN, "interposed nuclei (globose and emboliform)"),
         no_entry("magnocellular red nucleus"),
         carries="a correction - the difference between what cortex intended and what "
                 "the cerebellum predicts will actually happen. The nuclei are "
                 "tonically active and the Purkinje sheet sculpts that firing, so the "
                 "payload is a modulation of an ongoing signal, not a command from "
                 "rest. In the human this target is markedly reduced and its "
                 "rubrospinal tract vestigial",
         note="no entry in any file"),
    Edge(here(DN, "dentate nucleus"), no_entry("parvocellular red nucleus"),
         carries=TO_DERIVE + " - the descending limb of the dentato-rubro-olivary "
                 "loop. In the human this is the part that occupies most of the "
                 "nucleus's volume, so the edge written first is the one that barely "
                 "exists and this is the one that does the work",
         note="no entry in any file"),
    Edge(here(DN, "dentate nucleus"),
         far("ventral anterior / ventral lateral nuclei", S_THALAMUS),
         carries="the same correction; superior cerebellar peduncle, decussating, "
                 "onward to motor, premotor and prefrontal cortex. Fan-out: "
                 "cortex-to-output-nucleus areal ratio ~85:1",
         note="two-ended: the consumer names these nuclei, untyped there"),
    Edge(here(DN), far("intralaminar nuclei", S_THALAMUS),
         carries=TO_DERIVE,
         note="payload owed at both ends"),
    Edge(here(DN, "fastigial nucleus"), far("vestibular nuclei", S_SENSES),
         carries="axial posture, balance, and eye-movement corrections",
         note="producer-only at the far end; splitting this line is owed"),
    Edge(here(DN, "fastigial nucleus"), far("reticular formation", S_BRAINSTEM),
         carries="axial posture, balance, and eye-movement corrections",
         note="two-ended: the consumer declares it and names the source nucleus, "
              "untyped there"),
    Edge(here(DN), here(IO),
         carries="suppression of the error signal once the error is learned - the loop "
                 "that turns the teacher off; inhibitory",
         role=MODULATORY,
         note="consumer is in this file and declares it"),

    # ---- inferior olive, in ----
    Edge(far("spinal cord grey matter", S_SPINAL), here(IO),
         carries="somatosensory error - the actual consequence, against which the "
                 "prediction failed",
         note="two-ended: the producer declares it"),
    Edge(far("dorsal column nuclei", S_SENSORIMOTOR), here(IO),
         carries="the same somatosensory error",
         note="consumer-only: the producer declares no such edge; owed there, or "
              "withdraw the limb here"),
    Edge(no_entry("red nucleus and the mesodiencephalic junction"), here(IO),
         carries="the descending limb of the dentato-rubro-olivary loop",
         note="the red nucleus has no entry in any file; the mesodiencephalic "
              "junction is a region name that resolves to no entry either"),
    Edge(here(DN), here(IO),
         carries="suppression - this error is already accounted for; inhibitory",
         role=MODULATORY,
         note="producer is in this file"),

    # ---- inferior olive, out ----
    Edge(here(IO), here(CX, "Purkinje cells"),
         carries="the instructive signal: a single all-or-none complex spike per "
                 "event, timed to the error. Not a magnitude and not a direction - a "
                 "WHEN. Gap-junction coupling makes these fire in near-synchronous "
                 "bursts across a population, so the payload is also WHICH "
                 "POPULATION, which is the only addressing it has. One climbing fibre "
                 "per Purkinje cell, crossing",
         representation=CLIMBING_FIBRE_REP,
         note="consumer is in this file"),
    Edge(here(IO), here(DN),
         carries="the same instructive signal, as collaterals. Split from the Purkinje "
                 "line: the two targets are different entries and only the first is "
                 "one-to-one",
         note="consumer is in this file"),
)

SOURCE_EDGE_LINE_COUNT = 21      # the source counts bullets: 12 in, 9 out


def _key(e: Edge):
    return (e.source.name, e.source.sub, e.target.name, e.target.sub)


# Payload state per edge. Explicit rather than inferred, and validated below, so a
# new edge cannot slip in without one.
PAYLOAD_STATE = {
    (CX, "mossy-fibre terminals", CX, "granule cells"): PARTIAL,
    (CX, "granule cells", CX, "Purkinje cells"): NAMED,
    (CX, "granule cells", CX, "Golgi cells"): NAMED,
    (CX, "Golgi cells", CX, "granule cells"): NAMED,
    (CX, "granule cells", CX, "stellate cells"): NAMED,
    (CX, "granule cells", CX, "basket cells"): NAMED,
    (CX, "stellate cells", CX, "Purkinje cells"): NAMED,
    (CX, "basket cells", CX, "Purkinje cells"): NAMED,
    (IO, "olivary neuron", IO, "olivary neuron"): NAMED,
    ("pontine nuclei", None, CX, "granule cells"): NAMED,
    ("spinocerebellar tracts", None, CX, "granule cells"): NAMED,
    ("external cuneate nucleus", None, CX, "granule cells"): NAMED,
    ("semicircular canals, otolith organs, and vestibular nuclei", None,
     CX, "granule cells"): PARTIAL,
    (IO, None, CX, "Purkinje cells"): TYPED,
    ("locus coeruleus", None, CX, None): PAYLOAD_OWED,
    (CX, "Purkinje cells", DN, None): NAMED,
    (CX, "flocculonodular lobe", "vestibular nuclei", None): NAMED,
    ("collaterals of the mossy and climbing afferents", None, DN, None): NAMED,
    (DN, "interposed nuclei (globose and emboliform)",
     "magnocellular red nucleus", None): NAMED,
    (DN, "dentate nucleus", "parvocellular red nucleus", None): PAYLOAD_OWED,
    (DN, "dentate nucleus", "ventral anterior / ventral lateral nuclei", None): NAMED,
    (DN, None, "intralaminar nuclei", None): PAYLOAD_OWED,
    (DN, "fastigial nucleus", "vestibular nuclei", None): NAMED,
    (DN, "fastigial nucleus", "reticular formation", None): NAMED,
    (DN, None, IO, None): NAMED,
    ("spinal cord grey matter", None, IO, None): NAMED,
    ("dorsal column nuclei", None, IO, None): NAMED,
    ("red nucleus and the mesodiencephalic junction", None, IO, None): PARTIAL,
    (IO, None, DN, None): NAMED,
}

# The one non-synaptic edge in the sections worked.
NON_SYNAPTIC = {(IO, "olivary neuron", IO, "olivary neuron")}

# The corticopontine relay: a processing stage carried as a name on an edge.
PONTINE_TRANSFORM = (
    "not a copy - the relay diverges then reconverges, integrating cerebrocortical "
    "information before it arrives; each small spot of this cortex receives afferents "
    "from many widely separated pontine cell clusters",
    "not nearly the whole cortex - an almost total lack of projections from large "
    "parts of prefrontal and temporal cortices in monkey; the input arises from layer "
    "5 and subcortical sources contribute a few percent",
    "the map is reweighted in transit, with a direction - a de-emphasis of central "
    "vision and of the distal parts of the extremities, so the relay discards "
    "precisely the parts of the map the cortical areas themselves magnify",
)

MISSING_REGIONS = (
    ("pontine nuclei", "named on 1 edge; it computes, so it cannot be left as a name"),
    ("magnocellular red nucleus", "named on 1 edge"),
    ("parvocellular red nucleus", "named on 2 edges"),
    ("mesodiencephalic junction", "a region name that resolves to no entry"),
)

# Three far ends name this section by a region word matching no entry heading here.
# The repair is at the source; the module carries the state rather than hiding it.
UNRESOLVED_AT_FAR_END = (
    (S_SENSORIMOTOR, "-> cerebellum"),
    (S_BRAINSTEM, "<- cerebellum"),
    ("15_cranial_nerve_nuclei", "cerebellum, as one term of a four-producer bullet"),
)

# --------------------------------------------------------------------------
# The forward operation, and the two findings against it.
# --------------------------------------------------------------------------


def threshold_gate(active_counts, thresholds):
    """Fire where the count of active inputs reaches the stored threshold.

    Equal weights, so the dot product reduces to a count and the only stored value
    per neuron is the threshold. That reduction is the modelling choice the whole
    sizing method rests on, and it is the choice this section falsifies. See
    the_one_wins() and plasticity_target().
    """
    if len(active_counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(active_counts, thresholds)]


def the_one_wins() -> str:
    """A single input overriding 335,000 others is not expressible under equal weights."""
    pf = PURKINJE_SYNAPSES
    return (
        f"  A Purkinje cell receives ~{pf:,} parallel fibres and exactly ONE climbing\n"
        f"  fibre. The climbing fibre drives an all-or-none complex spike whatever the\n"
        f"  parallel fibres are doing. The source states it in one line: "
        f"~{pf:,} parallel-fibre\n"
        f"  inputs against one climbing fibre, and the one wins.\n"
        f"\n"
        f"  Under equal weights one active input adds 1 to a count that can reach "
        f"{pf+1:,}.\n"
        f"  For the climbing fibre to decide the output, its weight must be about\n"
        f"  {pf:,}x the others' - roughly {log2(pf):.1f} bits of dynamic range between two\n"
        f"  inputs to the same cell. Equal weights is exactly the assumption that\n"
        f"  removes that range.\n"
        f"\n"
        f"  This is not a missing value. It is a finding against the model, and the\n"
        f"  design file names the case in advance: a threshold is real structure,\n"
        f"  equal weights are not, and a structure the source describes as computing\n"
        f"  with graded weights is a finding rather than a structure to be flattened."
    )


def plasticity_target() -> str:
    """The learning mechanism operates on the assumption the model removes."""
    return (
        "  The complex spike depresses the parallel-fibre-Purkinje synapse - long-term\n"
        "  depression, one synapse at a time, gated by the climbing fibre and timed.\n"
        "\n"
        "  The model stores ONE number per neuron precisely because its synapses are\n"
        "  equal by construction. There is nowhere to put a change to one synapse of\n"
        f"  {PURKINJE_SYNAPSES:,}. The two findings are the same finding: the first says the\n"
        "  equal-weight assumption cannot represent the structure's operation, the\n"
        "  second says it cannot represent what the structure learns.\n"
        "\n"
        "  The source separately records that it has no way to express this either -\n"
        "  a payload on an inter-region edge whose effect is a change to an internal\n"
        "  edge's transfer - and marks it a limit of the representation rather than a\n"
        "  gap in the anatomy. So the gap is present at two rungs for two reasons."
    )


def synapse_store_if_weights_are_per_synapse() -> str:
    """What the obvious extension would cost. Recorded, not proposed.

    Memory is a derived requirement and never a constraint to design against, so
    this is not an argument against per-synapse weights. It is the number that
    would follow, computed rather than assumed.
    """
    contacts = PURKINJE_TOTAL * PURKINJE_SYNAPSES
    thr = GRANULE_TOTAL * 2 // 8 + PURKINJE_TOTAL * ceil(log2(PURKINJE_SYNAPSES)) // 8
    out = [f"  parallel-fibre-Purkinje contacts, whole cerebellum: {contacts:.3e}",
           f"  threshold-gate store as it stands:            {thr/1e9:8.2f} GB"]
    for bits, lab in ((1, "1 bit per synapse"), (8, "int8"), (32, "fp32")):
        b = contacts * bits / 8
        out.append(f"  per-synapse weights at {lab:18} {b/1e12:8.2f} TB   "
                   f"({b/thr:,.0f}x the threshold-gate store)")
    out.append("  The design file records a lived failure of exactly this shape: an")
    out.append("  fp32-per-synapse V1 sizing gave 18.8 TB and was fixed at the model,")
    out.append("  never by choosing a cap. The number above is recorded as found.")
    return "\n".join(out)


def allocate(structure: Structure, population: str):
    """Size the threshold and activity arrays for one sub-element."""
    for p in structure.populations:
        if p.name == population:
            state = SLOT_STATE[(structure.name, p.name)]
            if p.count is None:
                raise NotImplementedError(
                    f"{structure.name} / {population}: no count. State is "
                    f"'{state}'. {p.note}"
                )
            return {
                "neurons": p.count,
                "basis": p.basis,
                "threshold_bits": p.threshold_bits,
                "threshold_bytes": p.parameter_bytes,
                "realised_bytes": p.realised_bytes,
                "active_bytes": p.count // 8,
                "fillable": False,
                "why_not_fillable": "connection topology is unset; and for the "
                                    "Purkinje cell the stored value is the wrong "
                                    "shape - see the_one_wins()",
            }
    raise ValueError(f"{population!r} is not a population of {structure.name}")


def lattice_shape_problem() -> str:
    """The tangential axes do not fit the sheet class's tile grid."""
    return (
        "  The sheet class defines H x W as a tangential TILE GRID. This structure's\n"
        "  tangential organisation is a LATTICE WITH A DIRECTION: granule axons ascend,\n"
        "  bifurcate, and run ~5-6 mm along the folium, crossing the flat dendritic\n"
        "  fans of many Purkinje cells at right angles.\n"
        "\n"
        "  So connectivity is anisotropic by construction - long in one tangential\n"
        "  direction, thin in the other. A square tile grid with a single pitch asserts\n"
        "  an isotropy the structure denies, and no pitch is recorded for either axis.\n"
        "  The source states it directly: an edge cannot terminate on a compartment\n"
        "  here, because the organisation is a lattice and not a parcellation."
    )


def fan_in_map(structure: Structure):
    """Which source lines converge on each neuron.

    Not implementable. This section has more fan figures than any other worked -
    four of them - and none is a pattern.
    """
    raise NotImplementedError(
        "connection topology is not set. This section states four fan quantities and "
        "no pattern; the lattice geometry that would give the pattern has no pitch"
    )


def step(*args, **kwargs):
    """There is no step, and this section makes the finest-latency question concrete."""
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; every "
        "edge latency reads 'to derive', and the climbing fibre's stated timing "
        "condition has no number on either side of it"
    )


def learn(*args, **kwargs):
    """The learning rule is unset, and this section describes one in full."""
    raise NotImplementedError(
        "no learning rule is set - and this section's rule is described in full and "
        "still could not be implemented, because the threshold-gate model stores one "
        "value per neuron and long-term depression modifies one synapse of ~335,000"
    )


# --------------------------------------------------------------------------
# Derived arithmetic — independent recomputation.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    lines = [f"{'structure / sub-element':52} {'neurons':>16} {'fan-in':>9} "
             f"{'bits':>5} {'store':>12}"]
    total = 0
    for s in STRUCTURES:
        for p in s.populations:
            b = p.parameter_bytes
            if b is None:
                state = SLOT_STATE[(s.name, p.name)]
                lines.append(f"{s.name + ' / ' + p.name:52} {state[:16]:>16} {'-':>9} "
                             f"{'-':>5} {'to derive':>12}")
                continue
            total += b
            f = f"{p.fan_in:,}" if p.fan_in else "to derive"
            store = f"{b/1e9:.2f} GB" if b >= 1e9 else f"{b/1e6:.2f} MB"
            lines.append(f"{s.name + ' / ' + p.name:52} {p.count:>16,} {f:>9} "
                         f"{p.threshold_bits:>5} {store:>12}")
    lines.append("")
    lines.append(f"stated total: {total/1e9:.2f} GB ({BASIS}), "
                 f"{total/2/1e9:.2f} GB per hemisphere")
    lines.append("It is a FLOOR: three of the ten slots have no count, and "
                 "Structure.parameter_bytes")
    lines.append("returns None for all three structures for that reason - a partial "
                 "sum reads as a total.")
    gb = GRANULE_TOTAL * 2 // 8
    pb = PURKINJE_TOTAL * ceil(log2(PURKINJE_SYNAPSES)) // 8
    lines.append(f"granule cells are {100*gb/total:.2f}% of it at 2 bits each;")
    lines.append(f"Purkinje cells are {100*pb/total:.3f}% at "
                 f"{ceil(log2(PURKINJE_SYNAPSES))} bits each - "
                 f"{ceil(log2(PURKINJE_SYNAPSES))/2:.1f}x the width, "
                 f"{GRANULE_TOTAL/PURKINJE_TOTAL:,.0f}x less numerous.")
    lines.append("Memory tracks neuron count, not synapse count. Here that is a")
    lines.append("measurement rather than an argument.")
    return "\n".join(lines)


def log2_ceiling_report() -> str:
    """The one structure whose fan-in exceeds 16 bits, and the figure that moved."""
    lo, hi, stated = DESIGN_FILE_EXAMPLE
    out = [f"  the design file's worked example: ~{lo:,}-{hi:,} per Purkinje cell, "
           f"approx {stated} bits"]
    for f in (lo, 175_000, hi, PURKINJE_SYNAPSES):
        tag = ""
        if f == 175_000:
            tag = "   <- RETIRED by the source as a rat estimate"
        elif f == PURKINJE_SYNAPSES:
            tag = "   <- the source's human figure"
        out.append(f"    {f:>7,} -> log2 = {log2(f):5.2f} -> {ceil(log2(f)):>2} bits{tag}")
    out.append(f"  so the width is {ceil(log2(PURKINJE_SYNAPSES))} bits, not {stated}.")
    out.append("  the design file's range brackets the retired figure.")
    out.append(f"  this is the only structure in the sections worked whose fan-in "
               f"exceeds the {FAN_IN_CEILING_BITS}-bit log2 ceiling, and it exceeds "
               f"it by {ceil(log2(PURKINJE_SYNAPSES))-FAN_IN_CEILING_BITS}.")
    for f, why in RETIRED:
        out.append(f"  retired: {f:,.0f} - {why}" if f < 1e13
                   else f"  retired: {f:.0e} - {why}")
    return "\n".join(out)


def method_tension() -> str:
    base = GRANULE_TOTAL * 2 / 8
    out = [f"  isotropic fractionator, TOTAL neurons:      {GRANULE_TOTAL/1e9:5.0f}B "
           f"-> {base/1e9:6.2f} GB"]
    for n in STEREOLOGY_GRANULE_ONLY:
        out.append(f"  Danish stereology, GRANULE CELLS ALONE:    {n/1e9:5.0f}B "
                   f"-> {n*2/8/1e9:6.2f} GB   ({n/GRANULE_TOTAL:.2f}x)")
    lo = STEREOLOGY_GRANULE_ONLY[0] * 2 / 8 / base
    hi = STEREOLOGY_GRANULE_ONLY[1] * 2 / 8 / base
    out.append(f"  the spread carried through to the store: {lo:.2f}-{hi:.2f}x")
    out.append("  Both are primary, unbiased methods. Recorded, not resolved.")
    out.append("  This is the only term that moves the section's figure.")
    return "\n".join(out)


def cross_checks() -> str:
    """The source's own cross-checks, re-derived rather than trusted."""
    contacts = PURKINJE_TOTAL * PURKINJE_SYNAPSES
    out = [f"  {PURKINJE_TOTAL:,} Purkinje x {PURKINJE_SYNAPSES:,} synapses = "
           f"{contacts:.3e}   (source ~1.02e13)  [closes]",
           f"  that total / {GRANULE_TOTAL/1e9:.0f}B granule cells = "
           f"{contacts/GRANULE_TOTAL:.0f} contacts per granule cell   "
           f"(source ~148)  [closes]",
           f"  the retired 1e14 total would need {1e14/GRANULE_TOTAL:,.0f} per granule "
           f"cell - no reconciliation   [confirms the retirement]",
           f"  granule:Purkinje convergence = {GRANULE_TOTAL/PURKINJE_TOTAL:,.0f}:1   "
           f"(source ~2,000-3,000:1)  [closes]",
           f"  share of whole-brain neurons = "
           f"{100*GRANULE_TOTAL/WHOLE_BRAIN_NEURONS:.1f}%   (source ~80%)  [closes]",
           f"  cortex:dentate surface ratio = "
           f"{SURFACE_CM2['cerebellar cortex']/SURFACE_CM2['dentate nucleus']:.1f}:1   "
           f"(source states the areal ratio as ~85:1)  [closes, independently]"]
    return "\n".join(out)


def mossy_fan_out_note() -> str:
    """Two figures do not reconcile, and the caveats matter more than the gap."""
    conv = GRANULE_TOTAL * 4
    implied_fibres = conv / RAT_MOSSY_TO_GRANULE
    per_granule = int(PURKINJE_TOTAL * PURKINJE_SYNAPSES / GRANULE_TOTAL)
    out = [
        f"  convergence side: {GRANULE_TOTAL/1e9:.0f}B granule cells x ~4 mossy inputs "
        f"= {conv:.3e} contacts",
        f"  divergence side at the rat figure of ~{RAT_MOSSY_TO_GRANULE} granule cells "
        f"per mossy fibre",
        f"    -> needs {implied_fibres/1e6:,.0f}M mossy fibres against the stated "
        f"~{INPUT_FIBRE_ORDER/1e6:.0f}M input-fibre order  "
        f"({implied_fibres/INPUT_FIBRE_ORDER:.2f}x)",
        f"  and {RAT_MOSSY_TO_GRANULE} x {per_granule} Purkinje contacts per granule "
        f"cell = {RAT_MOSSY_TO_GRANULE*per_granule:,} against the stated "
        f"~{RAT_MOSSY_TO_PURKINJE:,}  "
        f"({RAT_MOSSY_TO_PURKINJE/(RAT_MOSSY_TO_GRANULE*per_granule):.2f}x)",
        "",
        "  NOT reported as a discrepancy. Both gaps run through the same rat figure,",
        "  and the source labels it as rat. Three things could account for either",
        "  without any of them being an error:",
        "    - the fan-out is rat and the counts are human;",
        "    - 'input fibre' may not mean 'mossy afferent axon', since climbing fibres",
        "      also enter the peduncles;",
        "    - one afferent axon branches into many mossy terminals, so counting axons",
        "      and counting terminals are different arithmetic.",
        "  The check cannot be run, because there is no human mossy fan-out figure.",
        "",
        f"  What the arithmetic DOES yield is a candidate for one: if the "
        f"~{INPUT_FIBRE_ORDER/1e6:.0f}M figure",
        "  counts mossy afferent axons and each granule cell takes 4, the human mossy",
        f"  fan-out is ~{conv/INPUT_FIBRE_ORDER:,.0f} granule cells per fibre, not "
        f"~{RAT_MOSSY_TO_GRANULE}. Offered to be checked.",
    ]
    return "\n".join(out)


def surface_density() -> str:
    """The one structure where the tile calculation can run backwards."""
    area_mm2 = SURFACE_CM2["cerebellar cortex"] * 100
    out = [f"  unfolded surface {SURFACE_CM2['cerebellar cortex']:.0f} cm2 = "
           f"{area_mm2:,.0f} mm2 (~78% of the neocortex)",
           f"  {GRANULE_TOTAL/1e9:.0f}B / {area_mm2:,.0f} mm2 = "
           f"{GRANULE_TOTAL/area_mm2:,.0f} neurons per mm2 of surface",
           f"    V1: ~120,000 per mm2  ->  {GRANULE_TOTAL/area_mm2/120000:.1f}x"]
    for v in VOLUME_CM3_IN_VIVO:
        out.append(f"  volumetric at {v:.0f} cm3 in vivo: "
                   f"{GRANULE_TOTAL/(v*1000):,.0f} /mm3")
    out.append(f"    V1: ~60,000 /mm3  ->  up to "
               f"{GRANULE_TOTAL/(VOLUME_CM3_IN_VIVO[0]*1000)/60000:.1f}x")
    out.append("  Everywhere else surface area is the missing term. Here it is measured,")
    out.append("  so the calculation runs backwards. The PITCH is still missing - and")
    out.append("  here it is missing in a form the shape classes have no slot for.")
    return "\n".join(out)


# --------------------------------------------------------------------------
# Edge reporting and the mechanical checks over the table.
# --------------------------------------------------------------------------


def unique_edges() -> tuple[Edge, ...]:
    """De-duplicate edges the source writes at both ends.

    The source writes each edge twice - in the producer's Outputs and the
    consumer's Inputs - and that redundancy is what makes a payload mechanically
    checkable. At this rung an edge is one object, so the two declarations collapse
    to one. Three of this section's edges are internal to it and therefore appear
    at both ends: Purkinje -> deep nuclei, deep nuclei -> inferior olive, and
    inferior olive -> Purkinje.
    """
    seen, out = set(), []
    for e in EDGES:
        k = _key(e)
        if k in seen:
            continue
        seen.add(k)
        out.append(e)
    return tuple(out)


def payload_state(e: Edge) -> str:
    return PAYLOAD_STATE[_key(e)]


def table_checks() -> str:
    """Mechanical checks over the edge table itself.

    Every one of these is a count rather than a reading, which is the only kind of
    check this rung has over its own edges.
    """
    uniq = unique_edges()
    out = []

    missing = [k for k in (_key(e) for e in uniq) if k not in PAYLOAD_STATE]
    out.append(f"  every edge carries a payload state      : "
               f"{'yes' if not missing else 'NO -> ' + str(missing)}")

    cross = [e for e in uniq if e.crosses_file]
    unstemmed = [e for e in cross
                 if not (e.source.stem or e.target.stem).startswith(tuple("0123456789"))]
    out.append(f"  every cross-file endpoint carries a stem: "
               f"{'yes' if not unstemmed else 'NO'}")

    stems = sorted({e.source.stem or e.target.stem for e in cross})
    out.append(f"  far files reached by stem              : {len(stems)}")
    for s in stems:
        n = sum(1 for e in cross if s in (e.source.stem, e.target.stem))
        out.append(f"    {s:42} {n:3d}")

    out.append(f"  sub-element slots                      : {len(SLOT_STATE)}")
    for state in (COUNTED, OWED, SOFT, UNKNOWN):
        n = sum(1 for v in SLOT_STATE.values() if v == state)
        out.append(f"    {state:38} {n:3d}")
    out.append("    the design file says nine slots and then lists 3+4+2+1 = 10.")
    out.append("    Ten are implemented. The discrepancy is the design file's and is")
    out.append("    reported rather than silently resolved either way.")
    return "\n".join(out)


def edge_report() -> str:
    uniq = unique_edges()
    dupes = len(EDGES) - len(uniq)
    # "Inside one" means inside one STRUCTURE, not inside one file: an edge from
    # the Purkinje cells to the deep nuclei crosses two entries and is between
    # structures even though both ends are local.
    internal = [e for e in uniq if e.source.name == e.target.name]
    external = [e for e in uniq if e.source.name != e.target.name]
    stated = [e for e in uniq if e.latency_s is not None]
    nonsyn = [e for e in uniq if _key(e) in NON_SYNAPTIC]
    expected = SOURCE_EDGE_LINE_COUNT - dupes + 2
    out = [f"  declarations: {len(EDGES)}; unique edges: {len(uniq)}  "
           f"({dupes} written at both ends, collapsed)",
           f"    {len(external)} between structures, {len(internal)} inside one",
           f"  the source counts {SOURCE_EDGE_LINE_COUNT} bullets, 12 in and 9 out",
           f"  reconciliation: {SOURCE_EDGE_LINE_COUNT} bullets - {dupes} pairs written "
           f"at both ends ({2*dupes} bullets, {dupes} edges) + 2 compound bullets "
           f"naming two targets = {expected}"
           f"   [{'matches' if len(external) == expected else 'DOES NOT MATCH'}]",
           f"  with a stated latency: {len(stated)}    to derive: {len(uniq)-len(stated)}",
           f"  non-synaptic edges: {len(nonsyn)}"]
    for e in nonsyn:
        out.append(f"    {e.source.sub} <-> {e.target.sub}: {e.note}")
    out.append("      The invariant's biological justification is conduction plus")
    out.append("      synaptic transmission, so it does not reach this edge - as it does")
    out.append("      not reach the endocrine, optical and mechanical edges the design")
    out.append("      file already lists. Its REQUIREMENT still holds. This is the case")
    out.append("      where 'nonzero' is most strained, and it is not zero.")
    for state in (NAMED, PARTIAL, PAYLOAD_OWED, TYPED):
        n = len([e for e in uniq if payload_state(e) == state])
        out.append(f"  payloads {state}: {n}")
    out.append("  regions named on edges with no entry in any file:")
    for r, why in MISSING_REGIONS:
        out.append(f"    {r} - {why}")
    out.append("  far ends naming this section by a word matching no entry heading here:")
    for stem, word in UNRESOLVED_AT_FAR_END:
        out.append(f"    {stem:42} {word}")
    out.append("    Those edges pair at neither end - producer-only here, unresolved")
    out.append("    there. The repair is at the source and is not made at this rung.")
    out.append("  the corticopontine relay is a PROCESSING STAGE, not a relay:")
    for t in PONTINE_TRANSFORM:
        out.append(f"    - {t}")
    out.append("    So the cerebellum does not receive cortex's state. It receives a")
    out.append("    reweighted, integrated projection of part of it.")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report())
    print()
    print("the log2 ceiling, and a figure the source has retired:")
    print(log2_ceiling_report())
    print()
    print("the only term that moves the figure:")
    print(method_tension())
    print()
    print("cross-checks re-derived:")
    print(cross_checks())
    print()
    print("two figures that do not reconcile:")
    print(mossy_fan_out_note())
    print()
    print("surface density:")
    print(surface_density())
    print()
    print("FINDING AGAINST THE MODEL (1) - the one wins:")
    print(the_one_wins())
    print()
    print("FINDING AGAINST THE MODEL (2) - the plasticity target:")
    print(plasticity_target())
    print()
    print("what the obvious extension would cost:")
    print(synapse_store_if_weights_are_per_synapse())
    print()
    print("shape:")
    print(lattice_shape_problem())
    print()
    print("edges:")
    print(edge_report())
    print()
    print("edge-table checks:")
    print(table_checks())
    print()
    print("edges, counted by the shared vocabulary:")
    print(config_edge_report(unique_edges()))
    print()
    print(representation_report(unique_edges()))
    print()
    print("allocation:")
    for s in STRUCTURES:
        for p in s.populations:
            try:
                a = allocate(s, p.name)
                b = a["threshold_bytes"]
                st = f"{b/1e9:.2f} GB" if b >= 1e9 else f"{b/1e6:.2f} MB"
                print(f"  {s.name + ' / ' + p.name:52} threshold {st:>9}   "
                      f"{a['threshold_bits']:>2} bits   sized, not fillable")
            except NotImplementedError as exc:
                print(f"  {s.name + ' / ' + p.name:52} blocked - "
                      f"{exc.args[0].split('State is ')[-1][:60]}")
    print()
    for fn, label in ((fan_in_map, "connectivity"), (step, "scheduler"),
                      (learn, "learning")):
        try:
            fn(CEREBELLAR_CORTEX) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
