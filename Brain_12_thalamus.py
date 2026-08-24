"""Brain — thalamus: the higher-order, motor, limbic and gating nuclei.

Structures, edges and the threshold-gate forward operation for the thalamic nuclei
that are not sensory relays, plus the adjacent zona incerta.  Each neuron is a
threshold gate over equal-weight inputs: it fires when the count of active inputs
crosses a stored threshold, so the only value held per neuron is that threshold, at
log2(fan-in) bits.  No weights, no multiply, no gradient.

Counting basis is uniform here: every structure is counted per side.

Six of the eight structures have no neuron count in the biology and five of those
six have no grey-matter volume either, so neither the direct route nor the
density-times-volume route reaches them.  The two that are counted close against
both routes, and that cross-check is recomputed below rather than trusted.

Every fan-in reads None, meaning "to derive".  Not one structure here has a
convergence figure of any kind, so every threshold width takes the 16-bit ceiling.

The forward operation covers a minority of this section's edges.  The dominant
payload in the thalamus is a gain or a gate, not content: the mediodorsal nucleus
amplifies a cortical loop without relaying categorical content, the pulvinar adds
attentional gain and cross-areal synchrony on top of content that mostly reflects
its cortical driver, and the thalamic reticular nucleus and the zona incerta carry
inhibition and no content at all.  A count of active inputs has no sign, so an
inhibitory line cannot be counted; and it has no scaling term, so a modulatory line
has nowhere to land except the threshold, which is the learning rule and is not set.
Edges are therefore typed by class in the data below, so the operation gap is
visible rather than argued.

Five things this module needs are not set at any rung above it, and each is on the
list that must be surfaced before it is touched: the inter-structure connection
topology, the tile geometry, the sparsity, the buffer shapes, and the scheduling
discipline.  Where each is needed the module raises rather than choosing.  A sixth,
the learning rule, is also unset; it is the one whose absence still leaves a
runnable artifact, because a threshold that is never written is a construction cost
rather than a memory.

Three edge latencies here are measured, and all three sit on one projection: the
lamina-I lines into the posterior / ventromedial-posterior territory arrive 59, 72
and 131 ms after the periphery.  That is the first real time on any edge in the
architecture, and it does not license a uniform step -- see `step`.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log10, log2

# --------------------------------------------------------------------------
# Element classes.
#
# Only one appears in this section.  Every structure here is a population of
# spiking neurons: no transducer, no transmission-only structure, and the one
# graded, non-spiking element of the thalamus -- the geniculate interneuron's
# dendritic release site -- belongs to another section.  The constants for the
# other classes are absent on purpose; adding them here would assert elements
# this section does not contain.
# --------------------------------------------------------------------------

THRESHOLD_GATE = "threshold_gate"   # spikes; stores a threshold at log2(fan-in) bits

# --------------------------------------------------------------------------
# Edge classes.
#
# What a line asks the receiving cell to do, which is not the same question as
# what kind of cell sends it.  Only DRIVER is expressible by the forward
# operation below.  MODULATORY sets gain and carries no receptive-field content;
# INHIBITORY carries inhibition and no content; DISINHIBITORY is INHIBITORY twice
# in series.  None of the last three has a term in a count of active inputs.
# --------------------------------------------------------------------------

DRIVER = "driver"                   # sets a receptive field or carries a payload
MODULATORY = "modulatory"           # sets gain; no receptive-field content
INHIBITORY = "inhibitory"           # inhibition; no content
DISINHIBITORY = "disinhibitory"     # inhibits an inhibitor; two sign inversions
ROUTING = "routing"                 # a collateral copy of traffic already sent

EXPRESSIBLE = frozenset({DRIVER, ROUTING})

# --------------------------------------------------------------------------
# Structures.
#
# Counts are the architecture's, carried with their basis.  `fan_in` is the
# convergence onto one neuron of this population where the biology fixes it, and
# None where it does not -- which is everywhere in this section.
#
# `volume_mm3` is carried because it is the only independent route to a count
# that this section supports: thalamic packing is ~1.0-1.8e4 neurons/mm3, so a
# pinned volume brackets a count.  It is not parameter memory and is never summed
# with one.
# --------------------------------------------------------------------------

THALAMIC_DENSITY_PER_MM3 = (1.0e4, 1.8e4)


@dataclass(frozen=True)
class Population:
    name: str
    kind: str
    basis: str
    count: tuple[int, int] | None      # (low, high); None where the biology has not fixed it
    fan_in: int | None                 # None where the biology has not fixed it
    fan_in_bound: int = 16             # log2 cap: any fan-in under ~65,000 fits 16 bits

    @property
    def threshold_bits(self) -> int:
        """Stored bits per neuron under the threshold-gate model."""
        if self.fan_in is None:
            return self.fan_in_bound
        if self.fan_in <= 1:
            return 0                   # nothing to threshold against a single input
        return ceil(log2(self.fan_in))

    @property
    def parameter_bytes(self) -> tuple[int, int] | None:
        if self.count is None:
            return None
        bits = self.threshold_bits
        return (self.count[0] * bits // 8, self.count[1] * bits // 8)


@dataclass(frozen=True)
class Structure:
    name: str
    populations: tuple[Population, ...]
    subelements: tuple[str, ...] = ()
    volume_mm3: tuple[float, float] | None = None

    @property
    def parameter_bytes(self) -> tuple[int, int] | None:
        """None if any population's store is unstated -- a partial sum would read as a total."""
        lo = hi = 0
        for p in self.populations:
            b = p.parameter_bytes
            if b is None:
                return None
            lo += b[0]
            hi += b[1]
        return (lo, hi)

    def density_bracket(self) -> tuple[float, float] | None:
        """Neurons implied by grey-matter volume at thalamic packing.

        The only mechanical cross-check this section supports, and it reaches two
        structures because the other six have no volume recorded.
        """
        if self.volume_mm3 is None:
            return None
        return (self.volume_mm3[0] * THALAMIC_DENSITY_PER_MM3[0],
                self.volume_mm3[1] * THALAMIC_DENSITY_PER_MM3[1])


PER_SIDE = "per side"

# Divisions named in the literature the count is drawn from, and in no described
# sub-element set; the five cortical outputs leave for five consumers and no
# division is assigned to one.
MEDIODORSAL = Structure(
    "mediodorsal nucleus",
    (Population("relay neurons", THRESHOLD_GATE, PER_SIDE, (10_000_000, 10_000_000), None),),
    subelements=("magnocellular", "parvocellular", "densocellular"),
    volume_mm3=(680.0, 990.0),
)

# Two output edges declare different payloads -- visual plus coordinating, and
# deep-receptor from the anterior division -- which is the reason to think they
# leave from different subdivisions.
PULVINAR = Structure(
    "pulvinar",
    (Population("relay neurons", THRESHOLD_GATE, PER_SIDE, (13_000_000, 26_000_000), None),),
    subelements=("anterior", "medial", "lateral", "inferior"),
    volume_mm3=(840.0, 1640.0),
)

# Two non-overlapping termination fields, and no internal edge between them is
# described; their reported near-non-overlap is a reason to expect none.  Borders
# are contested and indistinct, which is why no unbiased count exists.
POSTERIOR_VMP = Structure(
    "posterior / ventromedial-posterior thalamus",
    (Population("relay neurons", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("calbindin-immunoreactive field",
                 "calcitonin-gene-related-peptide field"),
)

# The two sub-elements are named in the biology and the input and output edges are
# typed at the level of the combined nucleus, so nothing assigns an edge to a
# division.  "With overlap" is the contested part.
VA_VL = Structure(
    "ventral anterior / ventral lateral nuclei",
    (Population("relay neurons", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("ventral lateral", "ventral anterior"),
)

# The standard divisions are not named in the description.  The head-direction
# signal the retrosplenial consumer describes is classically carried by one of
# them rather than by the group, so naming them is what would let that be an edge.
ANTERIOR = Structure(
    "anterior nuclei",
    (Population("relay neurons", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("anterodorsal", "anteroventral", "anteromedial"),
)

# The two named sub-elements are already load-bearing: the two striatal edges
# leave from different ones and reach different striatal sectors.  The wider group
# -- central lateral, paracentral, central medial -- is named nowhere.
INTRALAMINAR = Structure(
    "intralaminar nuclei",
    (Population("relay neurons", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("centromedian", "parafascicular"),
)

# Sectored by modality, and the sectors are load-bearing because the outputs leave
# from different ones.  The visual sector is the perigeniculate nucleus -- one
# structure under two names, recorded rather than resolved by preference.
RETICULAR = Structure(
    "thalamic reticular nucleus",
    (Population("inhibitory neurons", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("visual sector (perigeniculate)", "auditory sector",
                 "somatosensory sector", "motor sector"),
)

# Subthalamus, not thalamus.  Different sectors carry different functions and a
# parvalbumin population is named as the target of the amygdalar input, so
# sub-elements are described; none is named and no internal edge is written.
ZONA_INCERTA = Structure(
    "zona incerta",
    (Population("inhibitory neurons", THRESHOLD_GATE, PER_SIDE, None, None),),
    subelements=("rostral", "caudal", "parvalbumin population"),
)

STRUCTURES = (MEDIODORSAL, PULVINAR, POSTERIOR_VMP, VA_VL, ANTERIOR,
              INTRALAMINAR, RETICULAR, ZONA_INCERTA)

# --------------------------------------------------------------------------
# Edges.
#
# An edge names its target sub-element where the biology terminates on one, and
# its source sub-element where the biology leaves from one.  The two striatal
# edges below are the clear case: they leave from different named nuclei of one
# group for different striatal sectors, and collapsing them would delete a
# topographic claim.
#
# `latency_s` is real time in seconds.  Three edges here carry one; the rest are
# None, meaning "to derive".  It is never expressed in steps: a latency stated in
# steps has assumed a clock.
#
# An edge internal to this section is declared ONCE, at its producer.  The biology
# writes each edge twice, in the producer's Outputs and the consumer's Inputs, and
# that redundancy is what makes a payload mechanically checkable there -- but two
# copies here would be two arrays for one projection.
#
# `endpoint_is_class` marks an endpoint that names a class rather than a structure
# with an entry.  Those are inherited from the description and are not resolved
# here; patching one at this rung would invent an arity.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    kind: str
    source_sub: str | None = None
    target_sub: str | None = None
    latency_s: float | None = None      # None = to derive
    endpoint_is_class: bool = False
    one_ended: bool = False             # declared at one end only in the biology
    carries: str = ""


EDGES: tuple[Edge, ...] = (
    # --- mediodorsal nucleus -------------------------------------------------
    Edge("internal globus pallidus", "mediodorsal nucleus", INHIBITORY,
         carries="tonic inhibition, selectively released; a gate on which prefrontal "
                 "loops may proceed, not a positive content signal"),
    Edge("substantia nigra pars reticulata", "mediodorsal nucleus", INHIBITORY,
         carries="the same negative payload the basal-ganglia output carries at all "
                 "its thalamic targets"),
    Edge("amygdala", "mediodorsal nucleus", DRIVER,
         carries="limbic value / significance context; payload otherwise owed"),
    Edge("olfactory / limbic cortex", "mediodorsal nucleus", DRIVER,
         endpoint_is_class=True,
         carries="limbic value / significance context; payload otherwise owed"),
    Edge("prefrontal cortex", "mediodorsal nucleus", DRIVER, "layer 5",
         endpoint_is_class=True,
         carries="the cortical driver that makes this a higher-order nucleus; a subset "
                 "of relay cells instead have subcortical drivers"),
    Edge("prefrontal cortex", "mediodorsal nucleus", MODULATORY, "layer 6",
         endpoint_is_class=True,
         carries="no receptive-field content; corticothalamic feedback"),
    Edge("mediodorsal nucleus", "frontal eye fields", MODULATORY,
         carries="no categorical content; raises the gain of the consumer's local "
                 "recurrent connectivity"),
    Edge("mediodorsal nucleus", "dorsolateral prefrontal cortex", MODULATORY,
         carries="the same modulatory amplification"),
    Edge("mediodorsal nucleus", "ventrolateral prefrontal cortex", MODULATORY,
         carries="the same modulatory amplification"),
    Edge("mediodorsal nucleus", "orbitofrontal / ventromedial prefrontal cortex", MODULATORY,
         carries="the same modulatory amplification"),
    Edge("mediodorsal nucleus", "frontopolar cortex", MODULATORY,
         carries="the same modulatory amplification"),
    Edge("mediodorsal nucleus", "thalamic reticular nucleus", ROUTING,
         carries="a copy of this nucleus's outgoing traffic"),

    # --- pulvinar ------------------------------------------------------------
    Edge("visual cortex", "pulvinar", DRIVER, "layer 5", endpoint_is_class=True,
         carries="a feedforward cortical visual signal; the driver that sets the "
                 "pulvinar cell's receptive field"),
    Edge("superior colliculus", "pulvinar", DRIVER, "intermediate and deep layers",
         carries="a collicular visual signal, retinotopic salience and motion"),
    Edge("visual cortex", "pulvinar", MODULATORY, "layer 6", endpoint_is_class=True,
         carries="no receptive-field content; sets response gain and frequency"),
    Edge("long-range inhibitory sources", "pulvinar", INHIBITORY, endpoint_is_class=True,
         carries="inhibition, no content; the zona incerta is a candidate and is not "
                 "confirmed at either end"),
    Edge("pulvinar", "V4", DRIVER,
         carries="reflected cortical content plus attentional gain and cross-areal "
                 "synchrony; the consumer marks its own payload owed"),
    Edge("pulvinar", "middle temporal area", DRIVER,
         carries="the same two-part payload"),
    Edge("pulvinar", "lateral intraparietal area", DRIVER,
         carries="the same two-part payload"),
    Edge("pulvinar", "second somatosensory area", DRIVER, "anterior",
         carries="deep-receptor signals -- NOT the two-part visual payload this "
                 "structure declares elsewhere; a payload disagreement, unresolved"),
    Edge("pulvinar", "further visual, parietal and temporal cortex", DRIVER,
         endpoint_is_class=True,
         carries="the same two-part payload; each pulvinar cell reaches the input "
                 "layers of ~2-3 cortical areas"),
    Edge("pulvinar", "thalamic reticular nucleus", ROUTING,
         carries="a copy of this nucleus's outgoing traffic"),

    # --- posterior / ventromedial-posterior thalamus -------------------------
    # The one projection in the architecture with measured real time on it, and
    # the heterogeneity is inside the projection rather than between projections.
    Edge("spinal cord grey matter, lamina I", "posterior / ventromedial-posterior thalamus",
         DRIVER, "thermoreceptive-specific (pyramidal cells)",
         "calbindin-immunoreactive field", 0.059,
         carries="innocuous cooling; crossed anterolateral system, so this territory "
                 "serves the contralateral body"),
    Edge("spinal cord grey matter, lamina I", "posterior / ventromedial-posterior thalamus",
         DRIVER, "polymodal nociceptive (multipolar cells)",
         "calbindin-immunoreactive field", 0.072,
         carries="heat, pinch and cold"),
    Edge("spinal cord grey matter, lamina I", "posterior / ventromedial-posterior thalamus",
         DRIVER, "nociceptive-specific (fusiform cells)",
         "calbindin-immunoreactive field", 0.131,
         carries="pinch and/or heat; a pruriceptive population is reported within this group"),
    Edge("caudal spinal trigeminal nucleus", "posterior / ventromedial-posterior thalamus",
         DRIVER, None, "calbindin-immunoreactive field",
         carries="the same three labelled lines, for the face"),
    Edge("vagal / solitary / parabrachial visceral line",
         "posterior / ventromedial-posterior thalamus", DRIVER, None,
         "calcitonin-gene-related-peptide field",
         carries="visceral and cardiorespiratory state; a second termination field "
                 "rather than convergence onto the same cells"),
    Edge("insula", "posterior / ventromedial-posterior thalamus", MODULATORY,
         carries="no stimulus content; the driver / modulator gate"),
    Edge("zona incerta", "posterior / ventromedial-posterior thalamus", INHIBITORY,
         carries="inhibition, no content; the incerto-thalamic signature projection"),
    Edge("posterior / ventromedial-posterior thalamus", "dorsal posterior insula", DRIVER,
         carries="the body's physiological condition, somatotopically ordered "
                 "antero-posterior; whether the three lines stay separate here is owed"),
    Edge("posterior / ventromedial-posterior thalamus", "area 3a", DRIVER,
         carries="payload owed; a reported lesser projection"),
    Edge("posterior / ventromedial-posterior thalamus", "thalamic reticular nucleus", ROUTING,
         carries="a copy of this territory's outgoing traffic"),

    # --- ventral anterior / ventral lateral nuclei ---------------------------
    Edge("internal globus pallidus", "ventral anterior / ventral lateral nuclei", INHIBITORY,
         None, "ventral anterior",
         carries="tonic inhibition, selectively released; the selected action is the "
                 "one whose inhibition pauses, and nothing here carries the action"),
    Edge("substantia nigra pars reticulata", "ventral anterior / ventral lateral nuclei",
         INHIBITORY, None, "ventral anterior",
         carries="the same negative payload"),
    Edge("deep cerebellar nuclei (dentate)", "ventral anterior / ventral lateral nuclei",
         DRIVER, None, "ventral lateral",
         carries="the cerebellar correction; via the superior cerebellar peduncle, "
                 "decussating -- both this and the corticopontine input cross, so each "
                 "cerebellar hemisphere serves contralateral cortex and ipsilateral body"),
    Edge("primary motor cortex", "ventral anterior / ventral lateral nuclei", MODULATORY,
         carries="payload owed at both ends; corticothalamic and reciprocal"),
    Edge("ventral anterior / ventral lateral nuclei", "primary motor cortex", DRIVER,
         carries="basal-ganglia selection and cerebellar correction, combined on one relay"),
    Edge("ventral anterior / ventral lateral nuclei", "premotor and supplementary motor areas",
         DRIVER, carries="the same combined selection-and-correction payload"),
    Edge("ventral anterior / ventral lateral nuclei", "prefrontal cortex", DRIVER,
         endpoint_is_class=True, one_ended=True,
         carries="payload owed; NO prefrontal consumer declares this input, so either "
                 "the limb is missing at its consumers or it does not exist"),
    Edge("ventral anterior / ventral lateral nuclei", "thalamic reticular nucleus", ROUTING,
         carries="a copy of this nucleus's outgoing traffic"),

    # --- anterior nuclei -----------------------------------------------------
    Edge("mammillary bodies", "anterior nuclei", DRIVER,
         carries="payload owed; via the mammillothalamic tract"),
    Edge("subiculum", "anterior nuclei", DRIVER,
         carries="a completed episode -- the bound, retrievable pattern, addressable "
                 "by any fragment of itself; via the post-commissural fornix"),
    Edge("retrosplenial cortex", "anterior nuclei", MODULATORY, one_ended=True,
         carries="declared at the consumer's end only and missing here; a reciprocal "
                 "loop needs this limb and this entry carries no cortical input"),
    Edge("anterior nuclei", "retrosplenial cortex", DRIVER, carries="payload owed"),
    Edge("anterior nuclei", "anterior cingulate cortex", DRIVER, one_ended=True,
         carries="payload owed; the consumer declares a midline / intralaminar input "
                 "and not this one, so the cingulate half of Papez is unconfirmed"),
    Edge("anterior nuclei", "thalamic reticular nucleus", ROUTING,
         carries="a copy of this nucleus's outgoing traffic"),

    # --- intralaminar nuclei -------------------------------------------------
    Edge("reticular formation", "intralaminar nuclei", DRIVER,
         carries="payload owed; the arousal drive"),
    Edge("deep cerebellar nuclei", "intralaminar nuclei", DRIVER,
         carries="payload owed at both ends"),
    Edge("lateral parabrachial nucleus", "intralaminar nuclei", DRIVER,
         carries="payload owed"),
    Edge("internal globus pallidus", "intralaminar nuclei", INHIBITORY, one_ended=True,
         carries="payload owed; unconfirmed at the producer, whose declared thalamic "
                 "targets do not include this group"),
    Edge("substantia nigra pars reticulata", "intralaminar nuclei", INHIBITORY, one_ended=True,
         carries="payload owed; the same unconfirmed status"),
    Edge("cerebral cortex", "intralaminar nuclei", DRIVER, endpoint_is_class=True,
         carries="payload owed"),
    Edge("intralaminar nuclei", "motor striatum", DRIVER, "centromedian",
         carries="arousal and a thalamostriatal drive parallel to cortex"),
    Edge("intralaminar nuclei", "associative / limbic striatum", DRIVER, "parafascicular",
         carries="the same thalamostriatal drive"),
    Edge("intralaminar nuclei", "anterior cingulate cortex", DRIVER,
         carries="payload owed"),
    Edge("intralaminar nuclei", "further cortex, diffusely", DRIVER, endpoint_is_class=True,
         carries="payload owed; the residue of the class line the named edge came out of"),
    Edge("intralaminar nuclei", "thalamic reticular nucleus", ROUTING,
         carries="a copy of this group's outgoing traffic"),

    # --- thalamic reticular nucleus ------------------------------------------
    # The collateral input is the section's one measured connectivity fraction,
    # and the universal claim that would have made the class endpoint exempt is
    # false: 76% of ventrobasal relay axons collateralise here, so a quarter do
    # not; layer 6b sends none; layer 5 sends none except from frontal cortex.
    Edge("cortico-thalamic and thalamo-cortical axons", "thalamic reticular nucleus", ROUTING,
         endpoint_is_class=True,
         carries="a copy of the traffic in both directions; MOST, not all -- the split "
                 "by producer and layer is owed"),
    Edge("frontal cortex", "thalamic reticular nucleus", DRIVER, "layer 5",
         carries="monosynaptic, region-specific; a direct connection rather than a "
                 "passing collateral, distinct from the layer-6 route"),
    Edge("basal forebrain", "thalamic reticular nucleus", DISINHIBITORY,
         "parvalbumin-expressing neurons",
         carries="inhibition of this nucleus and therefore disinhibition of the relays "
                 "it inhibits; a tonic hold transiently released"),
    Edge("basal forebrain", "thalamic reticular nucleus", MODULATORY, "cholinergic neurons",
         carries="payload owed; driving these fibres here promotes sleep, opposite to "
                 "acetylcholine's general arousal role and to the parvalbumin edge"),
    Edge("internal globus pallidus", "thalamic reticular nucleus", INHIBITORY,
         carries="payload owed; whether this terminates here or on the relays directly "
                 "is not distinguished at either end"),
    Edge("substantia nigra pars reticulata", "thalamic reticular nucleus", INHIBITORY,
         carries="payload owed; the same ambiguity"),
    Edge("zona incerta", "thalamic reticular nucleus", INHIBITORY,
         carries="payload owed; the same ambiguity"),
    Edge("thalamic reticular nucleus", "mediodorsal nucleus", INHIBITORY,
         carries="inhibition; a gain and gate control, no content"),
    Edge("thalamic reticular nucleus", "pulvinar", INHIBITORY,
         carries="inhibitory gating of specific transthalamic pathways; no content"),
    Edge("thalamic reticular nucleus", "posterior / ventromedial-posterior thalamus", INHIBITORY,
         carries="inhibition; a gain and gate control, no content"),
    Edge("thalamic reticular nucleus", "ventral anterior / ventral lateral nuclei", INHIBITORY,
         carries="inhibition; a gain and gate control, no content"),
    Edge("thalamic reticular nucleus", "lateral geniculate nucleus", INHIBITORY,
         "visual sector (perigeniculate)",
         carries="inhibition; the visual sector and the perigeniculate nucleus are one "
                 "structure described at two scales"),
    Edge("thalamic reticular nucleus", "medial geniculate nucleus", INHIBITORY,
         "auditory sector", carries="inhibition; the gate"),
    Edge("thalamic reticular nucleus", "ventral posterior nuclear complex", INHIBITORY,
         "somatosensory sector", carries="inhibition; a gain and gate control, no content"),
    Edge("thalamic reticular nucleus", "anterior nuclei", INHIBITORY, one_ended=True,
         carries="inhibition; the consumer does not declare this input"),
    Edge("thalamic reticular nucleus", "intralaminar nuclei", INHIBITORY, one_ended=True,
         carries="inhibition; the consumer does not declare this input"),

    # --- zona incerta --------------------------------------------------------
    Edge("central nucleus of the amygdala", "zona incerta", DRIVER, None,
         "parvalbumin population",
         carries="payload owed; the producer's role in the pair is given as fear"),
    Edge("a near-whole-brain afferent field", "zona incerta", DRIVER, endpoint_is_class=True,
         carries="payload owed; seven class endpoints in one line -- cortex, basal "
                 "ganglia, thalamus, hypothalamus, brainstem, cerebellum, spinal cord"),
    Edge("zona incerta", "hypothalamus", INHIBITORY, carries="payload owed"),
    Edge("zona incerta", "periaqueductal gray", INHIBITORY,
         carries="payload owed; defensive behaviour"),
    Edge("zona incerta", "ventral tegmental area", INHIBITORY,
         carries="payload owed; feeding drive"),
    Edge("zona incerta", "rostral ventromedial medulla", INHIBITORY,
         carries="payload owed; descending pain control. This may be a named region "
                 "with no entry anywhere in the source"),
    Edge("zona incerta", "cerebral cortex", INHIBITORY, endpoint_is_class=True,
         carries="payload owed"),
    Edge("zona incerta", "spinal cord", INHIBITORY, carries="payload owed"),
)

# The one measured connectivity fraction in this section.  It says what fraction
# of a population projects, not which cells reach which targets, so it does not
# make `fan_in_map` writable; it is carried because it is the only topology
# number the biology supplies anywhere here.
VENTROBASAL_COLLATERAL_FRACTION = 0.76

# --------------------------------------------------------------------------
# Forward operation.
#
# This is the whole of what the rungs above specify, and it is faithful to the
# sizing model: equal weights, so the stored value is a threshold, and the cell
# fires when the count of active inputs reaches it.  It covers the driver edges
# and nothing else -- see `unexpressible_edges`.
# --------------------------------------------------------------------------


def threshold_gate(active_counts, thresholds):
    """Fire where the count of active inputs reaches the stored threshold.

    Integer comparison only.  No weights and no multiply, because equal weights
    reduce the dot product to a count; no gradient, because nothing here is
    differentiated.  No sign, which is why the inhibitory edges of this section
    have no term here.
    """
    if len(active_counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(active_counts, thresholds)]


def unexpressible_edges() -> tuple[Edge, ...]:
    """Edges the forward operation above has no term for.

    A modulatory edge sets the consumer's gain and carries no receptive-field
    content, so counting it as an input asserts content it does not have, and
    applying it to the threshold assumes the learning rule, which is not set.  An
    inhibitory edge has no sign to be counted with.  Neither is a defect in the
    biology; both are findings against the sizing model, and neither is resolved
    at this rung.
    """
    return tuple(e for e in EDGES if e.kind not in EXPRESSIBLE)


def fan_in_map(structure: Structure, subelement: str | None = None):
    """Which source lines converge on each neuron.

    Not implementable from the rungs above, and less implementable here than in
    the visual section.  There the architecture gave a scalar fan-in per structure
    and recorded the convergence pattern in prose -- point-to-point retinotopy
    with a space-variant compression ratio -- so writing this function meant
    writing down a geometry that was already described.

    Here there is neither.  Every fan-in in this section reads "to derive", and
    the biology records no convergence rule for any structure in it.  The two
    topographies it does record -- the antero-posterior head-to-foot somatotopy,
    and the centromedian / parafascicular striatal sector split -- say where a
    line lands, not how many lines land on a cell.  The one convergence figure in
    reach is a fan-out at a producer in another section, and fan-out is never
    stored.
    """
    raise NotImplementedError(
        "connection topology is not set; it must be surfaced before it is chosen. "
        "Every fan-in in this section reads 'to derive' and no convergence rule is "
        "recorded for any structure in it."
    )


def allocate(structure: Structure, subelement: str):
    """Size the threshold and activity arrays for one sub-element.

    Not implementable, and blocked twice.  The first block is the partition: a
    structure-level count does not divide to the sub-elements its edges terminate
    on.  The second is new at this file -- six of the eight structures have no
    count to partition, so for those the whole-structure array cannot be sized
    either, and five of the six have no grey-matter volume, so the density route
    does not reach them.
    """
    if subelement not in structure.subelements:
        raise ValueError(f"{subelement!r} is not a sub-element of {structure.name}")
    if structure.parameter_bytes is None:
        raise NotImplementedError(
            f"{structure.name} has no neuron count at all, so neither its own array "
            f"nor {subelement!r}'s can be sized. Tile geometry and sparsity are also "
            f"unset and both are surface-before-touching items."
        )
    raise NotImplementedError(
        f"{structure.name} carries one neuron count across "
        f"{len(structure.subelements)} sub-elements; no partition is recorded, so the "
        f"array for {subelement!r} cannot be sized. Tile geometry and sparsity are "
        f"also unset and both are surface-before-touching items."
    )


def step(*args, **kwargs):
    """There is no step, and this section is where refusing one costs something.

    The architecture sanctions a uniform one-step delay as a thing this rung may
    decide to do: set every latency equal and choose an interval short enough to
    carry the finest one.  In the visual section that shortcut had no parameter,
    because no latency was recorded at all.

    Here it has one.  The finest latency measured in this section is 59 ms, and a
    step of 59 ms or less would carry every latency this file states.

    It would also be wrong by nearly four orders of magnitude.  The interaural
    time-difference computation works at tens of microseconds, and a step sized
    from this section's floor would quantise it to nothing.  A uniform step is
    chosen against the finest latency in the system, not the finest in the file,
    and this file cannot see the system.  A shortcut with a plausible wrong
    parameter is more dangerous than one with no parameter, because a module that
    took it would look scheduled.

    Two further reasons, either of which stands alone.  The heterogeneity here is
    inside one projection -- three lamina-I lines arriving 72 ms apart, and the
    arrival order is the finding -- so a uniform delay does not coarsen it, it
    merges three lines the biology keeps separate.  And the loops nest three deep:
    seven relay-and-gate loops run inside the corticothalamic loops, and a loop
    broken by registers becomes an iterated map whose trajectory depends on the
    update rate.  Those are two different systems computing two different things.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; the "
        "59 ms floor measured here is a floor for this section only and is ~3.8 orders "
        "coarser than the finest computation in the map, so it is not a parameter"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    A threshold that is never written is a construction cost rather than a memory,
    which is why the module is still coherent without this.  At this section the
    absence costs more than it did at the visual one: the modulatory edges have
    nowhere to land except the threshold, so an unset learning rule is also what
    makes this section's dominant payload inexpressible.
    """
    raise NotImplementedError("no learning rule is set")


# --------------------------------------------------------------------------
# Derived sizing and checks -- independent recomputation, not transcription.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    lines, lo_total, hi_total, unstated = [], 0, 0, []
    lines.append(f"{'structure':46} {'basis':10} {'neurons':>21} {'bits':>5} {'store':>20}")
    for s in STRUCTURES:
        for p in s.populations:
            b = p.parameter_bytes
            if p.count is None:
                count, store = "to derive", "to derive"
                unstated.append(s.name)
            else:
                lo, hi = p.count
                count = f"{lo/1e6:.0f}M" if lo == hi else f"{lo/1e6:.0f}-{hi/1e6:.0f}M"
                store = (f"{b[0]/1e6:.1f} MB" if b[0] == b[1]
                         else f"{b[0]/1e6:.1f}-{b[1]/1e6:.1f} MB")
                lo_total += b[0]
                hi_total += b[1]
            lines.append(f"{s.name:46} {p.basis:10} {count:>21} "
                         f"{p.threshold_bits:>5} {store:>20}")
    lines.append("")
    lines.append(f"stated total: {lo_total/1e6:.1f}-{hi_total/1e6:.1f} MB   (per side)")
    lines.append(f"uncounted, so the total is a floor: {len(unstated)} of {len(STRUCTURES)}")
    for u in unstated:
        lines.append(f"    {u}")
    return "\n".join(lines)


def density_cross_check() -> str:
    """Volume x thalamic packing against the stated count.

    The only mechanical check this section supports, and it reaches two structures
    because the other six have no grey-matter volume recorded.
    """
    out = []
    for s in STRUCTURES:
        bracket = s.density_bracket()
        if bracket is None:
            out.append(f"  {s.name:46} no volume recorded; route unavailable")
            continue
        p = s.populations[0]
        stated = ("to derive" if p.count is None
                  else f"{p.count[0]/1e6:.0f}-{p.count[1]/1e6:.0f}M")
        closes = (p.count is not None
                  and bracket[0] <= p.count[1] and bracket[1] >= p.count[0])
        out.append(
            f"  {s.name:46} {s.volume_mm3[0]:.0f}-{s.volume_mm3[1]:.0f} mm3 -> "
            f"{bracket[0]/1e6:.1f}-{bracket[1]/1e6:.1f}M  vs stated {stated:>10}  "
            f"{'closes' if closes else 'DOES NOT CLOSE'}"
        )
    return "\n".join(out)


def edge_class_report() -> str:
    counts: dict[str, int] = {}
    for e in EDGES:
        counts[e.kind] = counts.get(e.kind, 0) + 1
    total = len(EDGES)
    blocked = len(unexpressible_edges())
    out = [f"edges: {total}"]
    for k in (DRIVER, ROUTING, MODULATORY, INHIBITORY, DISINHIBITORY):
        n = counts.get(k, 0)
        mark = "" if k in EXPRESSIBLE else "   <- no term in the forward operation"
        out.append(f"  {k:15} {n:>3}  ({100*n/total:4.1f}%){mark}")
    out.append(f"expressible by the specified forward operation: {total - blocked} of {total} "
               f"({100*(total-blocked)/total:.1f}%)")
    out.append(f"endpoints naming a class rather than a structure: "
               f"{sum(1 for e in EDGES if e.endpoint_is_class)}")
    out.append(f"declared at one end only in the biology: "
               f"{sum(1 for e in EDGES if e.one_ended)}")
    return "\n".join(out)


def latency_report() -> str:
    stated = [e for e in EDGES if e.latency_s is not None]
    out = [f"edges: {len(EDGES)}    with a measured latency: {len(stated)}    "
           f"to derive: {len(EDGES) - len(stated)}"]
    for e in sorted(stated, key=lambda x: x.latency_s):
        out.append(f"  {e.latency_s*1000:6.0f} ms   {e.source} / {e.source_sub}")
    if stated:
        lo = min(e.latency_s for e in stated)
        hi = max(e.latency_s for e in stated)
        out.append(f"  spread within one projection: {hi/lo:.2f}x, "
                   f"arrival range {1000*(hi-lo):.0f} ms")
        out.append(f"  finest here is {lo*1000:.0f} ms; the interaural computation "
                   f"elsewhere in the map works at ~2e-5 s, which is "
                   f"{log10(hi/2e-5):.2f} orders finer than "
                   f"the slowest line here")
    return "\n".join(out)


if __name__ == "__main__":
    print(sizing_report())
    print()
    print("density x volume cross-check:")
    print(density_cross_check())
    print()
    print(edge_class_report())
    print()
    print(latency_report())
    print()
    for fn, label in ((fan_in_map, "connectivity"), (step, "scheduler"), (learn, "learning")):
        try:
            fn(MEDIODORSAL) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
    for struct, sub in ((MEDIODORSAL, "magnocellular"), (INTRALAMINAR, "centromedian")):
        try:
            allocate(struct, sub)
        except NotImplementedError as exc:
            print(f"{'allocation':14} blocked: {exc}")
