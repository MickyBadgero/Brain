"""Brain — brainstem, midbrain and hypothalamus: the subcortical core.

Structures, edges and the threshold-gate forward operation for the superior
colliculus, the lateral parabrachial nucleus, the caudal and rostral ventrolateral
medulla, the nucleus of the solitary tract, the periaqueductal grey, the
hypothalamus, the pineal gland, the reticular formation and the rostromedial
tegmental nucleus.  Each neuron is a threshold gate over equal-weight inputs: it
fires when the count of active inputs crosses a stored threshold, so the only
value held per neuron is that threshold, at log2(fan-in) bits.  No weights, no
multiply, no gradient.

Nine of the ten structures have no neuron count, and that is what makes this
module different from the visual and neuromodulatory ones.  The visual line knew
its array sizes and not its wiring; the neuromodulatory line knew its sizes and
could not express what its structures emit; here there is no N to allocate
against at all.  An array whose length is unknown is not a partly specified array.

The missing counts are a measurement absent from the literature, not a decision
withheld from this rung, so they are recorded as absent rather than raised on.
Three structures may not be countable in the form an array wants: the
periaqueductal grey is defined by function and column, the reticular formation by
connectivity and transmitter, and the caudal ventrolateral medulla's boundary is
contested between two parcellations.  A count needs a border.  Those three are
marked borderless, which is a different state from uncounted.

One structure has no neurons at all.  The pineal gland is secretory tissue that
transduces a clock signal into a hormone; its store is a positive zero, not a gap,
and what it holds is a scalar concentration over time that neither array here can
represent.

Counting basis is not uniform: paired nuclei per side, midline structures whole,
and the nucleus of the solitary tract changes basis along its own length, spanning
the midline caudally and splitting into halves rostral to the area postrema.

Every edge latency is unstated in the biology and reads None.  None means "to
derive" and is not a licence to substitute zero or a uniform step — and this is
the section where a uniform step is worst, because the slowest loop here has a
twenty-four-hour period while a synaptic delay is tens of microseconds.  The
suprachiasmatic clock in the contract is a biological oscillator inside the
system, not a clock for the system.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import ceil, log2

# --------------------------------------------------------------------------
# Element classes.  Only the first occurs among the counted neurons here; the
# third is the pineal's case and has no representation in this vocabulary.
# --------------------------------------------------------------------------

THRESHOLD_GATE = "threshold_gate"   # spikes; stores a threshold at log2(fan-in) bits
TRANSDUCER = "transducer"           # converts a physical stimulus; stores no threshold
SECRETORY = "secretory"             # not a neuron; holds a concentration, not a bit

# --------------------------------------------------------------------------
# Edge classes.  Four kinds here are not conduction plus synaptic transmission,
# and the last two are distinguished only by whether a consumer exists: the same
# hormone in the same bloodstream reaches a named receptor-bearing target on one
# limb and no target region at all on the other.
# --------------------------------------------------------------------------

SYNAPTIC = "synaptic"                  # conduction plus synaptic transmission
CHEMICAL_IN = "chemical_from_blood"    # sensed directly; no producer region, fan-in n/a
HORMONAL = "hormonal"                  # released into blood; no target region, no consumer
HORMONAL_TARGETED = "hormonal_targeted"  # into blood, but onto a named receptor-bearing consumer

# --------------------------------------------------------------------------
# Counting bases.
# --------------------------------------------------------------------------

PER_SIDE = "per side"
WHOLE_MIDLINE = "whole (midline)"
WHOLE_BOTH = "whole (both sides)"
MIXED_ALONG_LENGTH = "per side rostrally / whole caudally"
MIXED_WITHIN_ENTRY = "mixed within one entry"

# --------------------------------------------------------------------------
# Structures.
#
# `count` is None wherever the biology has not fixed it, which is everywhere but
# one sub-element.  `borderless` marks a structure defined without a countable
# border, where None may not be resolvable by measurement at all.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Population:
    name: str
    kind: str
    basis: str
    count: int | None            # None where the biology has not fixed it
    fan_in: int | None           # None everywhere in this section
    fan_in_bound: int = 16       # log2 cap: any fan-in under ~65,000 fits 16 bits

    @property
    def threshold_bits(self) -> int | None:
        if self.kind == TRANSDUCER:
            return 0
        if self.kind == SECRETORY:
            return 0             # a positive zero: no neurons, so no thresholds
        if self.fan_in is None:
            return self.fan_in_bound
        if self.fan_in <= 1:
            return 0
        return ceil(log2(self.fan_in))

    @property
    def parameter_bytes(self) -> int | None:
        bits = self.threshold_bits
        if bits is None:
            return None
        if self.kind == SECRETORY:
            return 0             # known to be zero, not unknown
        if self.count is None:
            return None
        return self.count * bits // 8


@dataclass(frozen=True)
class Structure:
    name: str
    populations: tuple[Population, ...]
    subelements: tuple[str, ...] = ()
    borderless: bool = False     # defined without a countable border
    bundle: bool = False         # several regions in one entry; split owed at the source
    note: str = ""

    @property
    def parameter_bytes(self) -> int | None:
        total = 0
        for p in self.populations:
            b = p.parameter_bytes
            if b is None:
                return None      # a partial sum would read as a total
            total += b
        return total


SUPERIOR_COLLICULUS = Structure(
    "superior colliculus",
    (Population("all laminae", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("stratum zonale", "stratum griseum superficiale", "stratum opticum",
                 "stratum griseum intermediale", "stratum album intermediale",
                 "stratum griseum profundum", "stratum album profundum",
                 "rostral pole (fixation zone)", "burst neurons", "buildup neurons"),
    note=("a sheet: one tangential map serves every lamina, visual, auditory, somatosensory "
          "and motor in register across depth, which is what makes see-it-look-at-it local. "
          "Burst and buildup cells are two payloads on one map and are not separated "
          "spatially, so the cell-class axis does not partition the tissue."),
)

LATERAL_PARABRACHIAL = Structure(
    "lateral parabrachial nucleus",
    (Population("all subnuclei", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("subparabrachial nucleus (Kolliker-Fuse)", "lateral crescent",
                 "further unnamed subnuclei"),
    note=("receives a carbon copy of most nociceptive information the cord sends anywhere, "
          "by axon collaterals of fibres reaching other targets; treating the spinothalamic "
          "and spinoparabrachial lines as independent channels double-counts the source."),
)

CAUDAL_VENTROLATERAL_MEDULLA = Structure(
    "caudal ventrolateral medulla",
    (Population("all cell classes", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("GABAergic baro-activated", "cholinergic cardiovagal motor",
                 "A1 noradrenergic (competing parcellation)"),
    borderless=True,
    note=("the boundary itself is contested: a later parcellation places the baroreflex "
          "GABAergic neurons in an intermediate ventrolateral medulla and reserves this name "
          "for the A1 noradrenergic region. The data flow is not in dispute; the border is."),
)

NUCLEUS_SOLITARY_TRACT = Structure(
    "nucleus of the solitary tract",
    (Population("all subnuclei", THRESHOLD_GATE, MIXED_ALONG_LENGTH, None, None),),
    subelements=("interstitial", "central", "dorsomedial", "medial", "parvicellular",
                 "ventrolateral", "commissural"),
    note=("viscerotopy is a gradient and not a set of organ-exclusive compartments, so an "
          "edge terminating on 'the gastrointestinal subnucleus' selects nothing definite. "
          "Same shape problem as the anterior inferotemporal feature map, different tissue."),
)

ROSTRAL_VENTROLATERAL_MEDULLA = Structure(
    "rostral ventrolateral medulla",
    (Population("all C1 groups", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("bulbospinal presympathetic", "hypothalamus-projecting",
                 "parasympathetic-regulating"),
    note=("its cells are intrinsic pacemakers, so the sympathetic tone is generated rather "
          "than relayed and the baroreflex is a subtraction from a standing output. The "
          "bulbospinal cells have brainstem collaterals, so the three groups may not partition."),
)

PERIAQUEDUCTAL_GREY = Structure(
    "periaqueductal grey",
    (Population("all columns", THRESHOLD_GATE, WHOLE_MIDLINE, None, None),),
    subelements=("dorsomedial column", "dorsolateral column", "lateral column",
                 "ventrolateral column"),
    borderless=True,
    note=("defined by function and column rather than by a countable border. The columns are "
          "load-bearing endpoints: two output edges leave the ventrolateral one specifically. "
          "No internal edge between columns is described and it is not established one exists."),
)

HYPOTHALAMUS = Structure(
    "hypothalamus",
    (Population("suprachiasmatic nucleus", THRESHOLD_GATE, PER_SIDE, 50_000, None),
     Population("arcuate nucleus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("lateral hypothalamus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("ventromedial nucleus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("medial preoptic area", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("ventrolateral preoptic nucleus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("paraventricular nucleus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("supraoptic nucleus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("mammillary bodies", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("dorsomedial nucleus", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None),
     Population("further sub-nuclei", THRESHOLD_GATE, MIXED_WITHIN_ENTRY, None, None)),
    bundle=True,
    note=("at least eleven sub-nuclei, each effectively its own region with its own edges. "
          "Recorded as a bundle whose split is owed at the source: splitting it here would "
          "invent the arity. The suprachiasmatic count is the only firm figure in the section, "
          "and it does not reconcile with the reported sub-cubic-millimetre volume, so no "
          "density is asserted."),
)

PINEAL_GLAND = Structure(
    "pineal gland",
    (Population("pinealocytes", SECRETORY, WHOLE_MIDLINE, None, None),),
    note=("no neurons: about 95% pinealocytes, secretory endocrine cells. Zero parameter "
          "memory as a positive statement, not a gap. What it holds is a scalar melatonin "
          "concentration varying in time, which neither the threshold nor the activity array "
          "can represent. Its one firm physical figure is a volume, ~90-210 cubic millimetres."),
)

RETICULAR_FORMATION = Structure(
    "reticular formation",
    (Population("bordered sub-nuclei", THRESHOLD_GATE, WHOLE_BOTH, None, None),
     Population("diffuse remainder", THRESHOLD_GATE, WHOLE_BOTH, None, None)),
    subelements=("pre-Botzinger complex", "paramedian pontine reticular formation",
                 "rostral interstitial nucleus of the medial longitudinal fasciculus",
                 "pedunculopontine tegmental nucleus", "laterodorsal tegmental nucleus"),
    borderless=True,
    note=("two shapes in one entry. The named sub-nuclei have real borders; the remainder is "
          "a mesh whose boundaries are genuinely indistinct rather than merely unwritten, so "
          "its sub-element axis is absent rather than unmeasured. Treating the whole as one "
          "array asserts a homogeneity the tissue denies; keeping only the named nuclei "
          "discards the arousal engine, which is the part without borders."),
)

ROSTROMEDIAL_TEGMENTAL = Structure(
    "rostromedial tegmental nucleus",
    (Population("GABAergic projection neurons (~72%)", THRESHOLD_GATE, PER_SIDE, None, None),
     Population("non-GABAergic", THRESHOLD_GATE, PER_SIDE, None, None)),
    subelements=("core", "periphery"),
    note=("performs the habenula-to-dopamine sign inversion with a whole nucleus of ordinary "
          "spiking cells, where the outer retina performs the same logical operation at a "
          "receptor on a non-spiking cell. A ratio without a total sizes nothing: the 72% "
          "partitions an uncounted population."),
)

STRUCTURES = (SUPERIOR_COLLICULUS, LATERAL_PARABRACHIAL, CAUDAL_VENTROLATERAL_MEDULLA,
              NUCLEUS_SOLITARY_TRACT, ROSTRAL_VENTROLATERAL_MEDULLA, PERIAQUEDUCTAL_GREY,
              HYPOTHALAMUS, PINEAL_GLAND, RETICULAR_FORMATION, ROSTROMEDIAL_TEGMENTAL)

STRUCTURE_NAMES = {s.name for s in STRUCTURES}

# Named on this section's edges and holding no entry anywhere.  Carried so that a
# reader does not mistake a well-formed edge for a traceable path.
NO_ENTRY_ANYWHERE = (
    "rostral ventromedial medulla",       # the descending-analgesia relay
    "pontine nuclei",                     # a computing stage inside the cerebro-cerebellar loop
    "red nucleus",                        # the other stage of the same loop
    "lateral septum",
    "posterior pituitary",                # endocrine release site, recorded as a terminal
    "anterior pituitary",                 # endocrine release site, recorded as a terminal
    "superior cervical ganglion",         # peripheral, outside the scope boundary by rule
)

# --------------------------------------------------------------------------
# Edges.
#
# One record per architecture bullet, carried without splitting or merging, so
# the count here is checkable against the source's own header.  Where a single
# bullet names more than one endpoint, `names_multiple` records how many, because
# that is exactly where a transcription count can drift.
#
# `latency_s` is real time in seconds and is None on every edge here, because the
# biology records none.  It is never expressed in steps: a latency stated in steps
# has assumed a clock.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    source_sub: str | None = None
    target_sub: str | None = None
    latency_s: float | None = None      # None = to derive
    endpoint_is_class: bool = False     # names a class, not a structure
    edge_class: str = SYNAPTIC
    names_multiple: int = 1             # endpoints named in this one bullet
    far_end_file: int | None = None
    carries: str = ""


EDGES: tuple[Edge, ...] = (
    # ---- superior colliculus, in (8) ----
    Edge("retina", "superior colliculus", None, "stratum griseum superficiale", None, False,
         SYNAPTIC, 1, 1,
         "retinotopic luminance transients; payload owed AND contested, not merely owed"),
    Edge("V1", "superior colliculus", "layer 5b", "superficial layers", None, False,
         SYNAPTIC, 1, 1, "retinotopic salience for orienting; payload otherwise owed"),
    Edge("extrastriate and parietal cortex", "superior colliculus",
         "ventral lateral intraparietal area", "intermediate layers", None, False,
         SYNAPTIC, 1, 4,
         "the priority map: one scalar per retinotopic location, modality-free"),
    Edge("frontal eye field", "superior colliculus", None, "intermediate layers", None, False,
         SYNAPTIC, 1, 11, "a saccade goal in eye-centred coordinates; payload otherwise owed"),
    Edge("inferior colliculus", "superior colliculus", None, None, None, False, SYNAPTIC, 1, 2,
         "auditory azimuth and elevation, not a map; the map is built here, not relayed in"),
    Edge("somatosensory afferents", "superior colliculus", None, None, None, False,
         SYNAPTIC, 1, None, "body-surface location of touch, somatotopic; payload otherwise owed"),
    Edge("olivary pretectal nucleus", "superior colliculus", None,
         "stratum griseum intermediale", None, False, SYNAPTIC, 1, 15,
         "a luminance scalar arriving in the premotor rather than the visual layers"),
    Edge("substantia nigra pars reticulata", "superior colliculus", None, None, None, False,
         SYNAPTIC, 1, 9,
         "tonic inhibition and its release; a gate whose informative event is a cessation"),

    # ---- superior colliculus, out (5) ----
    Edge("superior colliculus", "reticular formation", "intermediate and deep layers",
         "saccade burst generators", None, False, SYNAPTIC, 2, 14,
         "a saccade displacement vector as a place code; the payload is a position in tissue"),
    Edge("superior colliculus", "cervical spinal cord", "deep layers", None, None, False,
         SYNAPTIC, 1, 16, "head and body orienting command, via the tectospinal tract"),
    Edge("superior colliculus", "pulvinar and other thalamus", "intermediate and deep layers",
         None, None, True, SYNAPTIC, 1, 12,
         "payload owed; the colliculo-pulvinar-cortical route parallel to the geniculostriate one"),
    Edge("superior colliculus", "V3 and the middle temporal area", None, None, None, False,
         SYNAPTIC, 2, 1, "payload owed; di-synaptic via the pulvinar, reaching those two selectively"),
    Edge("superior colliculus", "frontal eye field and lateral intraparietal area", None, None,
         None, False, SYNAPTIC, 2, 11,
         "corollary discharge; its usefulness depends on arriving BEFORE the movement"),

    # ---- lateral parabrachial nucleus, in (2 edge bullets; the collateral note is not an edge) ----
    Edge("spinal cord grey matter, lamina I", "lateral parabrachial nucleus", "lamina I", None,
         None, False, SYNAPTIC, 2, 16,
         "nociceptive, thermoreceptive and pruritic; also names the caudal spinal trigeminal "
         "nucleus in the same bullet"),
    Edge("nucleus of the solitary tract", "lateral parabrachial nucleus", None, None, None,
         False, SYNAPTIC, 1, 14, "visceral and gustatory; payload owed"),

    # ---- lateral parabrachial nucleus, out (6) ----
    Edge("lateral parabrachial nucleus", "amygdala", None, "central nucleus", None, False,
         SYNAPTIC, 1, 8,
         "the affective nociceptive payload; 'unpleasantness' is a phrase, not a type - owed"),
    Edge("lateral parabrachial nucleus", "bed nucleus of the stria terminalis", None, None,
         None, False, SYNAPTIC, 1, 8, "payload owed"),
    Edge("lateral parabrachial nucleus", "hypothalamus", None,
         "lateral, ventromedial, dorsomedial, arcuate, median and lateral preoptic", None,
         False, SYNAPTIC, 6, 14,
         "body-state signals driving autonomic and ingestive responses; payload otherwise owed"),
    Edge("lateral parabrachial nucleus", "intralaminar and ventroposterior parvicellular thalamus",
         None, None, None, False, SYNAPTIC, 2, 12, "payload owed"),
    Edge("lateral parabrachial nucleus", "insula and infralimbic cortex", None, None, None,
         False, SYNAPTIC, 2, 11, "payload owed"),
    Edge("lateral parabrachial nucleus", "basal forebrain", None,
         "nucleus basalis of Meynert / substantia innominata", None, False, SYNAPTIC, 1, 13,
         "payload owed"),

    # ---- caudal ventrolateral medulla, in (2) ----
    Edge("spinal cord grey matter, lamina I", "caudal ventrolateral medulla", "lamina I", None,
         None, False, SYNAPTIC, 1, 16, "nociceptive and thermoreceptive, typed at the spinal entry"),
    Edge("nucleus of the solitary tract", "caudal ventrolateral medulla", None, None, None,
         False, SYNAPTIC, 1, 14,
         "arterial pressure, a tonic excitatory drive proportional to baroreceptor firing"),

    # ---- caudal ventrolateral medulla, out (1) ----
    Edge("caudal ventrolateral medulla", "rostral ventrolateral medulla", None,
         "presympathetic neurons", None, False, SYNAPTIC, 1, 14,
         "SIGN-INVERTING: tonic inhibition; excitation here becomes suppression there"),

    # ---- nucleus of the solitary tract, in (4) ----
    Edge("taste afferents (facial, glossopharyngeal, vagus)", "nucleus of the solitary tract",
         None, None, None, False, SYNAPTIC, 3, None,
         "taste quality and intensity, topographically ordered by oral location; "
         "the receptors lie outside the scope boundary"),
    Edge("vagal and glossopharyngeal visceral afferents", "nucleus of the solitary tract",
         None, None, None, False, SYNAPTIC, 2, None,
         "arterial pressure, blood chemistry, lung inflation, gastrointestinal distension"),
    Edge("the bloodstream", "nucleus of the solitary tract", None, None, None, False,
         CHEMICAL_IN, 1, None,
         "glucose, leptin and angiotensin II concentrations; no producer region, fan-in n/a"),
    Edge("insula, hypothalamus and amygdala", "nucleus of the solitary tract", None, None,
         None, False, SYNAPTIC, 3, 14, "descending; payload owed"),

    # ---- nucleus of the solitary tract, out (5) ----
    Edge("nucleus of the solitary tract", "lateral parabrachial nucleus", None, None, None,
         False, SYNAPTIC, 1, 14, "the visceral and gustatory payload for relay to limbic forebrain"),
    Edge("nucleus of the solitary tract", "caudal ventrolateral medulla", None, None, None,
         False, SYNAPTIC, 1, 14,
         "arterial pressure, the excitatory drive that makes the baroreflex's inhibitory limb work"),
    Edge("nucleus of the solitary tract", "gustatory pathway", None,
         "parvicellular ventral posteromedial thalamus to insular taste cortex", None, False,
         SYNAPTIC, 2, 12, "taste quality and intensity, typed at the gustatory entry"),
    Edge("nucleus of the solitary tract", "branchiomotor and visceromotor nuclei", None,
         "dorsal motor nucleus of the vagus", None, False, SYNAPTIC, 2, 15,
         "the afferent limb of vagal reflexes; payload otherwise owed"),
    Edge("nucleus of the solitary tract", "hypothalamus", None, None, None, False,
         SYNAPTIC, 1, 14, "payload owed"),

    # ---- rostral ventrolateral medulla, in (3 bullets) ----
    Edge("caudal ventrolateral medulla", "rostral ventrolateral medulla", None, None, None,
         False, SYNAPTIC, 1, 14, "GABAergic inhibition, tonic; the baroreflex's sign inversion"),
    Edge("nucleus of the solitary tract", "rostral ventrolateral medulla", None, None, None,
         False, SYNAPTIC, 1, 14, "direct, alongside the indirect route; payload owed"),
    Edge("hypothalamus and periaqueductal grey", "rostral ventrolateral medulla", None, None,
         None, False, SYNAPTIC, 2, 14, "payload owed; both producers are in this section"),

    # ---- rostral ventrolateral medulla, out (3) ----
    Edge("rostral ventrolateral medulla", "spinal cord grey matter", None,
         "intermediolateral cell column", None, False, SYNAPTIC, 1, 16,
         "the excitatory presympathetic drive setting vasomotor tone and cardiac output"),
    Edge("rostral ventrolateral medulla", "hypothalamus", "non-bulbospinal C1 group",
         "paraventricular nucleus", None, False, SYNAPTIC, 1, 14,
         "regulates vasopressin and adrenocorticotropic hormone release and sodium intake"),
    Edge("rostral ventrolateral medulla", "locus coeruleus, raphe nuclei and dorsal vagal complex",
         None, None, None, False, SYNAPTIC, 3, 13,
         "payload owed; bulbospinal collaterals, so not necessarily separate populations"),

    # ---- periaqueductal grey, in (4) ----
    Edge("amygdala", "periaqueductal grey", "central nucleus", None, None, False, SYNAPTIC, 1, 8,
         "a valence and urgency signal driving defence; no identity information"),
    Edge("hypothalamus", "periaqueductal grey", None, None, None, False, SYNAPTIC, 1, 14,
         "payload owed; defensive and autonomic drive"),
    Edge("ventromedial and orbital prefrontal cortex", "periaqueductal grey", None, None, None,
         False, SYNAPTIC, 2, 11, "payload owed; top-down control of defence and analgesia"),
    Edge("spinal cord, lamina I", "periaqueductal grey", "lamina I", None, None, False,
         SYNAPTIC, 1, 16,
         "ascending nociceptive; ~120 cells per side and over 90% are collaterals, "
         "a branching axon rather than an independent population"),

    # ---- periaqueductal grey, out (5) ----
    Edge("periaqueductal grey", "rostral ventromedial medulla", "ventrolateral column", None,
         None, False, SYNAPTIC, 1, None,
         "the descending analgesic command; the target has NO ENTRY in any file"),
    Edge("periaqueductal grey", "spinal dorsal horn", None, "laminae I and II", None, False,
         SYNAPTIC, 1, 16,
         "the analgesic GATE: a gain applied to incoming nociception at the first synapse"),
    Edge("periaqueductal grey", "locus coeruleus", "ventrolateral column", None, None, False,
         SYNAPTIC, 1, 13, "payload owed; the noradrenergic limb of descending analgesia"),
    Edge("periaqueductal grey", "vocal and autonomic premotor targets", None, None, None, True,
         SYNAPTIC, 2, 14, "payload owed; the innate vocalisation and freezing motor pattern"),
    Edge("periaqueductal grey", "thalamus", None, None, None, True, SYNAPTIC, 1, 12,
         "payload owed; the affective pain projection"),

    # ---- hypothalamus, in (6) ----
    Edge("amygdala", "hypothalamus", "central nucleus", None, None, False, SYNAPTIC, 1, 8,
         "a valence and urgency signal via the stria terminalis and ventral amygdalofugal "
         "pathway; neither tract has an entry"),
    Edge("hippocampal formation", "hypothalamus", None, None, None, False, SYNAPTIC, 1, 8,
         "payload owed; via the fornix"),
    Edge("the septum", "hypothalamus", None, None, None, True, SYNAPTIC, 1, None,
         "payload owed; the lateral septum has no entry anywhere"),
    Edge("nucleus of the solitary tract", "hypothalamus", None, None, None, False,
         SYNAPTIC, 1, 14, "payload owed; visceral and cardiovascular state"),
    Edge("retina", "hypothalamus", "melanopsin ganglion cells", "suprachiasmatic nucleus", None,
         False, SYNAPTIC, 1, 1,
         "an irradiance 'lights-on' signal for clock entrainment, not spatial vision; "
         "the only edge in the section terminating on a sub-element that has a count"),
    Edge("blood-borne signals", "hypothalamus", None,
         "circumventricular organs (median eminence, organum vasculosum, subfornical organ)",
         None, False, CHEMICAL_IN, 1, None,
         "leptin, ghrelin, glucose, osmolality, temperature as chemical concentration; "
         "no producer region by design, fan-in n/a"),

    # ---- hypothalamus, out (7) ----
    Edge("hypothalamus", "posterior pituitary", "magnocellular supraoptic and paraventricular",
         None, None, False, HORMONAL, 1, None,
         "oxytocin and vasopressin into blood; an endocrine terminal, not an owed edge"),
    Edge("hypothalamus", "anterior pituitary", "parvocellular neurons", None, None, False,
         HORMONAL, 1, None,
         "releasing and inhibiting hormones via the hypophyseal portal blood; a terminal"),
    Edge("hypothalamus", "periaqueductal grey, brainstem and spinal cord", None, None, None,
         True, SYNAPTIC, 3, 14,
         "payload owed; descending autonomic and defensive drive. Two of the three resolve; "
         "the 'brainstem' remainder names a class"),
    Edge("hypothalamus", "anterior thalamic nuclei", "mammillary bodies", None, None, False,
         SYNAPTIC, 1, 12,
         "payload owed; the Papez memory relay, via the mammillothalamic tract (entry in file 18)"),
    Edge("hypothalamus", "brainstem tegmentum", None, None, None, True, SYNAPTIC, 1, 13,
         "payload owed; several far ends exist in file 13 and the class is not resolved"),
    Edge("hypothalamus", "pineal gland", "paraventricular nucleus", None, None, False,
         SYNAPTIC, 1, 14,
         "the circadian 'it is night' disinhibition, via intermediolateral cell column and "
         "superior cervical ganglion; a multisynaptic functional route with one joint out of scope"),
    Edge("hypothalamus", "widespread limbic and cortical targets", None, None, None, True,
         SYNAPTIC, 1, None, "payload owed; names a class and does not resolve"),

    # ---- pineal gland, in (1) ----
    Edge("superior cervical ganglion", "pineal gland", None, "pinealocytes", None, False,
         SYNAPTIC, 1, 20,
         "noradrenaline (norepinephrine) gated by the clock: a darkness permission signal, "
         "not content. The ganglion is peripheral and outside the scope boundary"),

    # ---- pineal gland, out (2) ----
    Edge("pineal gland", "the general circulation and cerebrospinal fluid", None, None, None,
         False, HORMONAL, 1, None,
         "melatonin; a producer, a payload and a real effect, and NO TARGET REGION at all"),
    Edge("pineal gland", "hypothalamus", None, "suprachiasmatic nucleus", None, False,
         HORMONAL_TARGETED, 1, 14,
         "melatonin as a phase-feedback signal closing the circadian loop; a real edge "
         "because the target bears receptors"),

    # ---- reticular formation, in (5) ----
    Edge("collaterals of the ascending sensory systems", "reticular formation", None, None,
         None, True, SYNAPTIC, 1, None, "payload owed; the non-specific drive maintaining arousal"),
    Edge("cerebellum", "reticular formation", "fastigial nucleus", None, None, False,
         SYNAPTIC, 1, 10, "payload owed"),
    Edge("periaqueductal grey", "reticular formation", None, None, None, False, SYNAPTIC, 1, 14,
         "payload owed; the vocal and freezing motor patterns"),
    Edge("hypothalamus", "reticular formation", None, None, None, False, SYNAPTIC, 1, 14,
         "payload owed; named only inside the producer's 'brainstem tegmentum' class"),
    Edge("cerebral cortex", "reticular formation", None, None, None, True, SYNAPTIC, 1, 11,
         "payload owed; the frontal eye field onto the saccade burst generators is the sharpest case"),

    # ---- reticular formation, out (4) ----
    Edge("reticular formation", "intralaminar thalamus", None, None, None, False,
         SYNAPTIC, 1, 12, "payload owed; the ascending arousal drive"),
    Edge("reticular formation", "cerebral cortex", None, None, None, True, SYNAPTIC, 1, None,
         "the arousal and gain signal, no content; much of it is delivered by the "
         "monoaminergic and cholinergic nuclei instead, and the two limbs are not distinguished"),
    Edge("reticular formation", "spinal cord", None, None, None, False, SYNAPTIC, 1, 16,
         "payload owed; reticulospinal postural tone, locomotion drive and autonomic control"),
    Edge("reticular formation", "cranial-nerve motor nuclei", None, None, None, True,
         SYNAPTIC, 1, 15, "payload owed; the premotor sequencing signal"),

    # ---- rostromedial tegmental nucleus, in (4) ----
    Edge("lateral habenula", "rostromedial tegmental nucleus", None, None, None, False,
         SYNAPTIC, 1, 17,
         "a negative / aversive value signal; the major input and the one that defines the nucleus"),
    Edge("laterodorsal and pedunculopontine tegmental nuclei", "rostromedial tegmental nucleus",
         None, None, None, False, SYNAPTIC, 2, 14,
         "payload owed; a cholinergic input. The far end is in this section and does not yet "
         "type the edge - an owed edit inside file 14"),
    Edge("extended amygdala, lateral septum and periaqueductal grey",
         "rostromedial tegmental nucleus", None, None, None, False, SYNAPTIC, 3, 14,
         "payload owed; aversion-related and defensive-state inputs"),
    Edge("substantia nigra", "rostromedial tegmental nucleus", None, None, None, False,
         SYNAPTIC, 1, 9, "payload owed; a lesser input"),

    # ---- rostromedial tegmental nucleus, out (3) ----
    Edge("rostromedial tegmental nucleus", "ventral tegmental area", None, "dopamine neurons",
         None, False, SYNAPTIC, 1, 13,
         "SIGN-INVERTED inhibition: a GABAergic brake, a negative gain on dopamine firing"),
    Edge("rostromedial tegmental nucleus", "substantia nigra pars compacta", None,
         "dopamine neurons", None, False, SYNAPTIC, 1, 9,
         "the same inhibition; stimulation suppresses ~90% of pars-compacta dopamine cells"),
    Edge("rostromedial tegmental nucleus", "hypothalamus and other targets beyond the dopamine "
         "midbrain", None, None, None, True, SYNAPTIC, 2, 14, "payload owed"),
)

# The source's own header count, carried so the module can diff against it.
SOURCE_HEADER_EDGE_COUNT = {"in": 39, "out": 41, "total": 80}
ARCHITECTURE_TRANSCRIPTION = {"in": 40, "out": 41, "total": 81}

# Which entry's Inputs or Outputs list each bullet was carried from, in the order
# EDGES is written.  An edge with both ends inside this section appears twice in
# the source - once under the producer's Outputs and once under the consumer's
# Inputs - so "in" and "out" are positions in a document, not properties of an
# edge, and the counts only diff against the source header if they are read that
# way.  (entry, incoming bullets, outgoing bullets)
ENTRY_BLOCKS = (
    ("superior colliculus", 8, 5),
    ("lateral parabrachial nucleus", 2, 6),
    ("caudal ventrolateral medulla", 2, 1),
    ("nucleus of the solitary tract", 4, 5),
    ("rostral ventrolateral medulla", 3, 3),
    ("periaqueductal grey", 4, 5),
    ("hypothalamus", 6, 7),
    ("pineal gland", 1, 2),
    ("reticular formation", 5, 4),
    ("rostromedial tegmental nucleus", 4, 3),
)


def _listed_under() -> list[str]:
    """Label each EDGES record 'in' or 'out' by the block it was written in."""
    labels: list[str] = []
    for _entry, n_in, n_out in ENTRY_BLOCKS:
        labels.extend(["in"] * n_in)
        labels.extend(["out"] * n_out)
    return labels

# A structural note that appears in the architecture's Inputs list but is not an
# edge: it names no producer.  Kept out of EDGES so the count stays checkable.
PARABRACHIAL_COLLATERAL_NOTE = (
    "A large fraction of the ascending fibres reaching other targets send axon "
    "collaterals to the lateral parabrachial nucleus, so it receives a carbon copy of "
    "most nociceptive information the cord sends anywhere. Treating the spinothalamic "
    "and spinoparabrachial lines as independent channels would double-count the source "
    "population. This is a qualification on the arity of the ascending system, not an edge."
)

# --------------------------------------------------------------------------
# Forward operation.
# --------------------------------------------------------------------------


def threshold_gate(active_counts, thresholds):
    """Fire where the count of active inputs reaches the stored threshold.

    Integer comparison only.  Correct for every neuron in this section: no
    transducer and no graded non-spiking population is described among the ten,
    so log2(fan-in) applies to every neuron that has a count.  There is one.
    """
    if len(active_counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(active_counts, thresholds)]


# --------------------------------------------------------------------------
# The operations the contract names and the model has no term for.
#
# Two of the four close together: given an inverting term, a standing output
# falls out of connectivity and delay with no further mechanism.
# --------------------------------------------------------------------------


def invert_sign(*args, **kwargs):
    """Make an edge subtract from the target's count rather than add to it.

    Not implementable under the sizing model.  `count[j] = sum(active_source[i])`
    has no negative term, and the caudal ventrolateral medulla's output is
    explicitly sign-inverting: excitation there becomes suppression of sympathetic
    drive at the rostral ventrolateral medulla.

    This is the cheapest instance of the gap anywhere in the map.  Where the outer
    retina performs the same logical operation at a receptor on a graded,
    non-spiking cell, here it is a whole nucleus of ordinary spiking cells whose
    effect on the target is to reduce its count - and the rostromedial tegmental
    nucleus does the same for dopamine.  No receptor-level mechanism is involved,
    so a solution written here needs nothing that is not already in the model
    except the sign itself.
    """
    raise NotImplementedError(
        "a count of active inputs has no inverting term; supplying one changes the "
        "model and is not this rung's decision - but it is the cheapest place on the "
        "map to supply it, and it closes free_running_drive() at the same time"
    )


def free_running_drive(*args, **kwargs):
    """Produce a standing output with no input, for the baroreflex to subtract from.

    Not implementable as written, and NOT a separate missing operation.  A
    stateless threshold gate cannot fire at zero input.  A threshold gate in a
    delayed feedback loop is an ordinary relaxation oscillator, and the
    per-edge-latency invariant already puts a nonzero delay on every edge - so
    free-running activity is available to the model as a property of connectivity
    plus delay, given an inverting stage.  See invert_sign().

    What the source does not settle is whether the biology's pacemaking is
    cell-intrinsic - pacemaker conductances in the membrane - or survives in slice
    because local recurrence survives with it.  The first needs an element-level
    mechanism; the second needs nothing new.  Owed at the source.
    """
    raise NotImplementedError(
        "blocked on invert_sign(), not on a separate mechanism; and whether the "
        "biology generates this in the membrane or in the circuit is owed at the source"
    )


def apply_gate(*args, **kwargs):
    """Apply a gain to how much of another structure's content gets through.

    Not implementable under the sizing model.  The periaqueductal grey's descending
    analgesic output carries no nociceptive content; its effect is to change how
    much of the spinal dorsal horn's content crosses the first synapse.  A count of
    active inputs over a threshold has no multiplicand.

    This is the same problem the diffuse neuromodulators raise, arriving on a
    single named edge with a single named target - which makes it the tractable
    instance, testable without first deciding what a brain-wide modulator does.
    """
    raise NotImplementedError(
        "a multiplicative gate has no term in a count of active inputs over a "
        "threshold; this is the map's most tractable instance of that gap"
    )


def hormonal_transport(*args, **kwargs):
    """Carry a concentration through blood to a receptor, or to nowhere in particular.

    Not implementable, and not for want of a number.  Three edges here release into
    blood.  One reaches a named receptor-bearing consumer and is a real edge; one
    reaches no target region at all; two carry chemical concentration inward with
    no producer region.  None has a fan-in list, and a concentration is not an
    activity bit.  The latency is synthesis, secretion, circulation and receptor
    binding, which shares no term with a conduction delay.
    """
    raise NotImplementedError(
        "no representation here holds a concentration, and an edge with no target "
        "region has no consumer to deliver to"
    )


# --------------------------------------------------------------------------
# Blocked on decisions above or beside this rung, and one thing that is not a
# decision at all.
# --------------------------------------------------------------------------


def fan_in_map(structure: Structure, subelement: str | None = None):
    """Which source lines converge on each neuron.

    Not implementable, and here it is not even the binding constraint.  Every
    fan-in on all eighty edges reads unknown - but a connectivity map is indexed by
    neuron, and for nine of ten structures there are no neurons to index.
    Connectivity is blocked behind extent in this section, which inverts the usual
    order.
    """
    raise NotImplementedError(
        "connection topology is not set; and for nine of ten structures there is no "
        "N to index it against"
    )


def allocate(structure: Structure, population_name: str):
    """Size the threshold and activity arrays for one population.

    Succeeds for exactly one population in the section.  Everything else has no
    count - and for the three borderless structures the count may not be
    obtainable in the form an array wants, which is a different state from
    unmeasured.
    """
    for p in structure.populations:
        if p.name == population_name:
            if p.kind == SECRETORY:
                raise NotImplementedError(
                    f"{structure.name} has no neurons; what it holds is a scalar "
                    f"concentration over time, which neither array can represent"
                )
            if p.count is None:
                why = ("no countable border - the structure is defined by function, "
                       "connectivity or a contested boundary, so this may not be "
                       "measurable in the form an array wants"
                       if structure.borderless else
                       "no count in the literature; a measurement, not a decision")
                raise NotImplementedError(f"{structure.name} / {population_name}: {why}")
            return {"neurons": p.count, "threshold_bits": p.threshold_bits,
                    "threshold_bytes": p.parameter_bytes, "active_bits": p.count}
    raise ValueError(f"{population_name!r} is not a population of {structure.name}")


def step(*args, **kwargs):
    """There is no step, and this section makes the shortcut quantitatively worst.

    Every edge latency here reads to derive, and the scheduling discipline is not
    set and is not this rung's to choose.  The sanctioned shortcut - set every
    latency equal and pick a step short enough to carry the finest one - has no
    parameter, because the finest is unknown.

    And the spread makes it worse than elsewhere.  The slowest loop in this
    section has a twenty-four-hour period while a synaptic delay is tens of
    microseconds: eight to nine orders of magnitude inside one section.  See
    uniform_step_cost() for the arithmetic.

    The suprachiasmatic clock in the contract is a biological oscillator inside
    the system, not a clock for the system.  A twenty-four-hour period is exactly
    the sort of number that invites being treated as a frame boundary.  It paces
    the circadian loop and nothing else.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; "
        "the circadian period in the contract is one loop's payload, not an update rate"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set."""
    raise NotImplementedError("no learning rule is set")


# --------------------------------------------------------------------------
# Derived reports - recomputation, not transcription.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    lines = [f"{'structure / population':52} {'basis':34} {'neurons':>10} {'store':>12}"]
    total, sizable, absent, borderless_rows = 0, 0, 0, 0
    for s in STRUCTURES:
        for p in s.populations:
            b = p.parameter_bytes
            count = f"{p.count:,}" if p.count is not None else "-"
            if p.kind == SECRETORY:
                store, note = "0 (no neurons)", ""
            elif b is None:
                store = "to derive"
                absent += 1
                if s.borderless:
                    borderless_rows += 1
            else:
                store = f"{b/1e6:.3f} MB"
                total += b
                sizable += 1
            flag = "  [borderless]" if s.borderless and p.count is None else ""
            lines.append(f"{s.name + ' / ' + p.name:52} {p.basis:34} {count:>10} {store:>12}{flag}")
    lines.append("")
    lines.append(f"populations with a derivable store: {sizable}")
    lines.append(f"populations with no count:          {absent}"
                 f"  (of which borderless: {borderless_rows})")
    lines.append(f"stated total: {total/1e6:.2f} MB   (mixed basis, width at the 16-bit ceiling)")
    lines.append("A count needs a border. 'Borderless' marks structures defined by function, "
                 "connectivity")
    lines.append("or a contested boundary, where 'to derive' may promise more than an "
                 "experiment can settle.")
    return "\n".join(lines)


def edge_count_check() -> str:
    """Diff this module's edge table against the source header and the architecture.

    The architecture recorded a one-line discrepancy last pass and attributed it to
    a compound bullet.  Counting here resolves which reading produced which number.
    """
    labels = _listed_under()
    if len(labels) != len(EDGES):
        return (f"  BLOCK TABLE OUT OF STEP: ENTRY_BLOCKS accounts for {len(labels)} bullets "
                f"and EDGES holds {len(EDGES)}. Fix before reading anything below.")
    ins = [e for e, lab in zip(EDGES, labels) if lab == "in"]
    outs = [e for e, lab in zip(EDGES, labels) if lab == "out"]
    internal = [e for e in EDGES
                if e.source in STRUCTURE_NAMES and e.target in STRUCTURE_NAMES]
    compound = [e for e in EDGES if e.names_multiple > 1]
    endpoints_named = sum(e.names_multiple for e in EDGES)
    out = [
        f"  source file header:        {SOURCE_HEADER_EDGE_COUNT['in']} in, "
        f"{SOURCE_HEADER_EDGE_COUNT['out']} out, {SOURCE_HEADER_EDGE_COUNT['total']} total",
        f"  architecture transcription:{ARCHITECTURE_TRANSCRIPTION['in']:3} in, "
        f"{ARCHITECTURE_TRANSCRIPTION['out']} out, {ARCHITECTURE_TRANSCRIPTION['total']} total",
        f"  this module's edge table:  {len(ins)} in, {len(outs)} out, {len(EDGES)} total",
        "",
        f"  bullets whose edge has both ends inside this section: {len(internal)}",
        "    (each such edge is written twice in the source, once per entry)",
        f"  bullets naming more than one endpoint:    {len(compound)}",
        f"  distinct endpoints those bullets name:    {endpoints_named} across {len(EDGES)} bullets",
    ]
    if len(ins) == SOURCE_HEADER_EDGE_COUNT["in"] and len(outs) == SOURCE_HEADER_EDGE_COUNT["out"]:
        out.append("")
        out.append("  RESOLVED: this module agrees with the source header. The architecture's")
        out.append("  extra incoming line was the parabrachial collateral bullet, which names no")
        out.append("  producer and is a qualification on the ascending system's arity, not an edge.")
        out.append("  It is carried as PARABRACHIAL_COLLATERAL_NOTE rather than dropped.")
    else:
        out.append("")
        out.append("  UNRESOLVED: the counts do not agree; do not smooth this over.")
    return "\n".join(out)


def edge_class_report() -> str:
    by_class: dict[str, list[Edge]] = {}
    for e in EDGES:
        by_class.setdefault(e.edge_class, []).append(e)
    lines = []
    for cls, es in by_class.items():
        lines.append(f"  {cls:20} {len(es):3}")
    classes = [e for e in EDGES if e.endpoint_is_class]
    timed = [e for e in EDGES if e.latency_s is not None]
    no_entry = [e for e in EDGES
                if e.target in NO_ENTRY_ANYWHERE or e.source in NO_ENTRY_ANYWHERE]
    lines.append(f"  {'endpoint names a class':20} {len(classes):3}")
    lines.append(f"  {'endpoint has no entry':20} {len(no_entry):3}  "
                 f"(of {len(NO_ENTRY_ANYWHERE)} such regions named in the section)")
    lines.append(f"  {'latency stated':20} {len(timed):3}   to derive: {len(EDGES) - len(timed)}")
    return "\n".join(lines)


def uniform_step_cost() -> str:
    """What a single uniform step costs against a twenty-four-hour loop.

    The point is not the size of the number.  It is that one step must resolve a
    synaptic delay and span a day at the same time, and those differ by eight to
    nine orders of magnitude inside this one section.
    """
    day_s = 24 * 60 * 60
    lines = []
    for fine_s in (1e-3, 1e-4, 5e-5):
        lines.append(f"  step {fine_s*1e6:8.1f} us  ->  {day_s/fine_s:>17,.0f} steps "
                     f"per circadian period")
    lines.append("  The finest latency in this section is unknown; every edge reads 'to derive'.")
    return "\n".join(lines)


def payload_gap_report() -> str:
    gaps = (
        ("sign inversion", "caudal ventrolateral medulla -> rostral ventrolateral medulla",
         invert_sign),
        ("standing output", "rostral ventrolateral medulla, intrinsic pacemakers",
         free_running_drive),
        ("gain at another's synapse", "periaqueductal grey -> spinal dorsal horn", apply_gate),
        ("hormonal transport", "hypothalamus and pineal -> blood", hormonal_transport),
    )
    out = []
    for label, where, fn in gaps:
        try:
            fn()
        except NotImplementedError as exc:
            out.append(f"  {label:26} on {where}\n      {exc}")
    out.append("")
    out.append("  TWO OF THESE FOUR CLOSE TOGETHER: given an inverting term, a standing output")
    out.append("  falls out of connectivity plus the delay the latency invariant already requires.")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report())
    print()
    print("edge count, checked against the source header and the architecture:")
    print(edge_count_check())
    print()
    print("edges by class:")
    print(edge_class_report())
    print()
    print("what a uniform step would cost here:")
    print(uniform_step_cost())
    print()
    print("payloads with no operation in the model:")
    print(payload_gap_report())
    print()
    print("blocked:")
    for fn, label in ((fan_in_map, "connectivity"), (step, "scheduler"), (learn, "learning")):
        try:
            fn(SUPERIOR_COLLICULUS) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"  {label:14} {exc}")
    for structure, pop in ((HYPOTHALAMUS, "suprachiasmatic nucleus"),
                           (PERIAQUEDUCTAL_GREY, "all columns"),
                           (SUPERIOR_COLLICULUS, "all laminae"),
                           (PINEAL_GLAND, "pinealocytes")):
        try:
            print(f"  {'allocation':14} {structure.name} / {pop}: {allocate(structure, pop)}")
        except NotImplementedError as exc:
            print(f"  {'allocation':14} {exc}")
