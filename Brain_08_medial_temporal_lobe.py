"""Brain — medial temporal lobe: hippocampal formation, amygdala, bed nucleus.

Three structures.  The hippocampal formation binds what is present into a
retrievable episode; the amygdala and its forebrain extension, the bed nucleus of
the stria terminalis, assign significance to what is present and act on it.  They
are reciprocally connected, and the direction of that connection is the
architecture: episodic context goes to the amygdala, a valence tag comes back as a
gain on encoding.

Each neuron is a threshold gate over equal-weight inputs: it fires when the count
of active inputs crosses a stored threshold, so the only value held per neuron is
that threshold, at log2(fan-in) bits.  No weights, no multiply, no gradient.

Counting basis is uniform: per hemisphere, verified human stereology for two of the
three structures.

This file carries no history: no versions, no provenance, no "changed since", no
reference to sessions or prior files, no changelog, no "formerly", no commented-out
prior version.

A cross-file endpoint carries the far file's stem, <nn>_<section>, never its number
alone.  A bare number goes silently wrong the moment a file is split, merged or
renumbered, and unlike a document the code has no reader to notice.

This is the first section where allocation is not wholly blocked.  Two of the three
structures partition to their sub-elements and the partitions close: the
hippocampal formation's five divisions sum to 43.5M against a stated ~43M headline,
and the amygdala's five counted nuclei sum to 12.21M against ~12.2M.  Nine of the
eleven sub-elements can therefore be sized.  The two that cannot are the amygdala's
medial nucleus and its intercalated cells, which sit inside an aggregated remainder
and are both edge endpoints.  Allocation succeeding does not unblock wiring: the
connection topology is still unset, so an array can be sized and not filled.

CA3 carries the only measured fan-in in the section, ~6,000-12,000 recurrent
contacts per cell, which is the one place outside V1 where the log2 bound bites
below 16 bits.

Every edge latency reads None.  None means "to derive" and is not a licence to
substitute zero or a uniform step.  The section does contain one real-time figure —
the 4-12 Hz theta rhythm, a period of 83-250 ms — and it is a payload on one input
edge, not a schedule.  Reading it as an update rate would substitute a global clock
for the heterogeneous delays the invariant exists to protect, and it is the most
inviting place in the project so far to do exactly that.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2

# --------------------------------------------------------------------------
# Element classes.  Only the first is instantiated here: every neuron in this
# section spikes, and no transducer or graded non-spiking element appears.
# --------------------------------------------------------------------------

THRESHOLD_GATE = "threshold_gate"
TRANSDUCER = "transducer"
GRADED = "graded"

# Sub-element state, kept distinct because collapsing them loses which repair each
# one needs.  A count that exists needs nothing; owed needs writing up from a
# literature that has it; unknown needs a measurement; aggregated needs the
# stereology re-cut, not re-run.
COUNTED = "counted"
AGGREGATED = "inside an aggregated remainder"
OWED = "owed"
UNKNOWN = "unknown"
NOT_APPLICABLE = "not applicable"


@dataclass(frozen=True)
class SubElement:
    name: str
    count: int | None            # None where no count is recorded
    state: str
    fan_in: int | None = None    # None where the biology has not fixed it
    fan_in_hi: int | None = None # upper end where the source gives a range
    note: str = ""

    def bits(self, upper: bool = False) -> int:
        """Stored bits per neuron under the threshold-gate model."""
        f = (self.fan_in_hi if upper and self.fan_in_hi else self.fan_in)
        if f is None:
            return 16                # log2 ceiling: any fan-in under ~65,000 fits
        if f <= 1:
            return 0                 # nothing to threshold against a single input
        return ceil(log2(f))

    def parameter_bytes(self, upper: bool = False) -> int | None:
        if self.count is None:
            return None
        return self.count * self.bits(upper) // 8


@dataclass(frozen=True)
class Structure:
    name: str
    kind: str
    shape_class: str
    subelements: tuple[SubElement, ...]
    stated_total: int | None = None   # the source's headline, for the closure check
    laminae: str = ""
    tangential: str = ""
    volume_cm3: tuple[float, ...] = ()
    volume_note: str = ""

    @property
    def counted(self) -> tuple[SubElement, ...]:
        return tuple(s for s in self.subelements if s.count is not None)

    def total_neurons(self) -> int | None:
        if not self.counted:
            return None
        return sum(s.count for s in self.counted)

    def parameter_bytes(self, upper: bool = False) -> int | None:
        """None if any sub-element's store is unstated — a partial sum reads as a total."""
        total = 0
        for s in self.subelements:
            b = s.parameter_bytes(upper)
            if b is None:
                return None
            total += b
        return total

    def partition_closes(self) -> tuple[bool, float]:
        """Does the sum of the parts meet the stated headline?"""
        t = self.total_neurons()
        if t is None or self.stated_total is None:
            return (False, 0.0)
        return (abs(t - self.stated_total) / self.stated_total < 0.02,
                (t - self.stated_total) / 1e6)


PER_HEMISPHERE = "per hemisphere"

HIPPOCAMPAL_FORMATION = Structure(
    "hippocampal formation",
    "allocortex, three-layered",
    "sheet, rank 4: (lamina, division, H, W)",
    (
        SubElement("entorhinal cortex", 6_000_000, COUNTED,
                   note="the input and output port; layer II carries the grid code"),
        SubElement("dentate gyrus, granule cells", 15_000_000, COUNTED,
                   note="sparse pattern separation"),
        # The one measured fan-in in the section.  A 2x spread in contacts costs one
        # bit, which is the log2 bound absorbing a dispute again.
        SubElement("CA3", 2_500_000, COUNTED, 6_000, 12_000,
                   note="recurrent autoassociator; the brain's largest associational "
                        "recurrent network; human pyramidal-cell refinement ~1.7M "
                        "against this ~2.5M total, pyramidal-versus-total, not a conflict"),
        SubElement("CA1", 16_000_000, COUNTED, note="comparator and main output"),
        SubElement("subiculum", 4_000_000, COUNTED, note="the principal output"),
    ),
    stated_total=43_000_000,
    laminae="three, names and per-division differences owed; not the eight-layer block",
    tangential="unknown, except the grid in entorhinal layer II, which is owed",
    # Primary anchor 3.81 +/- 0.46; ex-vivo ~3.3; young-adult ~2.8-2.9; full span
    # 1.7-5.7.  Right exceeds left by a few percent.
    volume_cm3=(3.3, 3.55, 3.8),
    volume_note="hippocampus proper, excluding the separately-located entorhinal cortex",
)

AMYGDALA = Structure(
    "amygdala",
    "subcortical nuclei",
    "non-laminated nucleus, rank 2: (cell class, N)",
    (
        SubElement("lateral nucleus", 4_000_000, COUNTED,
                   note="the main sensory-input zone"),
        SubElement("basal nucleus", 3_240_000, COUNTED,
                   note="intermediate processing; most two-way cortical traffic"),
        SubElement("accessory basal nucleus", 1_280_000, COUNTED),
        SubElement("central nucleus", 360_000, COUNTED,
                   note="the main subcortical output; the smallest counted nucleus"),
        SubElement("remaining nuclei", 3_330_000, COUNTED,
                   note="an aggregate, not a sub-element the edges use"),
        # Both of these are edge endpoints and neither has a count: the lateral
        # olfactory tract terminates on the medial nucleus, and the intercalated
        # cells are the source of an internal inhibitory edge.
        SubElement("medial nucleus", None, AGGREGATED,
                   note="olfactory and social; inside 'remaining nuclei'"),
        SubElement("intercalated cells", None, AGGREGATED,
                   note="inhibitory gates; inside 'remaining nuclei'"),
    ),
    stated_total=12_200_000,
    laminae=NOT_APPLICABLE + " — subcortical nuclei, not cortex",
    tangential=UNKNOWN,
    volume_cm3=(1.2, 1.26, 1.7),
    volume_note="ex-vivo histology ~1.26; in-vivo magnetic resonance imaging 1.2-1.7",
)

BED_NUCLEUS = Structure(
    "bed nucleus of the stria terminalis",
    "basal-forebrain nucleus",
    "non-laminated nucleus, rank 2: (cell class, N)",
    (
        # The Function field makes the sustained mode depend on this population,
        # which is a claim that a cell class and not the structure as a whole
        # carries the payload the Outputs describe.
        SubElement("corticotropin-releasing-factor-expressing cells", None, OWED,
                   note="load-bearing; owed whether the four output edges leave from it"),
        SubElement("anterior and posterior divisions", None, OWED,
                   note="described in the literature, written nowhere here"),
    ),
    stated_total=None,
    laminae=NOT_APPLICABLE + " — a basal-forebrain nucleus, not cortex",
    tangential=UNKNOWN,
    volume_cm3=(),
    volume_note="small, sub-cm3, sexually dimorphic; no single verified human figure",
)

STRUCTURES = (HIPPOCAMPAL_FORMATION, AMYGDALA, BED_NUCLEUS)

# --------------------------------------------------------------------------
# The theta rhythm.
#
# The section's only real-time figure, and it is not an edge latency.  Recorded
# here as data so that the one place a scheduler could be smuggled in is visible
# rather than implicit.
# --------------------------------------------------------------------------

THETA_HZ = (4.0, 12.0)


def theta_period_ms() -> tuple[float, float]:
    lo, hi = THETA_HZ
    return (1000.0 / hi, 1000.0 / lo)


THETA_IS_NOT_A_CLOCK = (
    "The theta rhythm is a payload on one input edge, not a schedule. Its tick is "
    "an intrinsic membrane oscillation in the septal pacemaker cells, generated by "
    "the hyperpolarization-activated cyclic-nucleotide-gated channel and its "
    "current; the pacemakers frequency-lock to one rhythm by mutual inhibition; "
    "and it paces one structure's principal cells, not the system. A phase "
    "arriving on a wire with a propagation delay is content. A shared beat that "
    "advances every structure together is a register, and there is none here."
)

# --------------------------------------------------------------------------
# Edges.
#
# Three rungs count these edges and the two figures that differ are of different
# quantities, so the module computes its own rather than carrying one.  The source's
# header states 72 edge lines, 36 in and 36 out, and a count of its edge bullets
# returns 72.  The architecture declares 81, from 84 arrow-headed endpoints less
# three claustral endpoints it declines as edges.  edge_count_report() reports all
# three.  More edges are declared here than the source has bullets because ten
# bullets name more than one target structure and one names five at once; the arity
# is explicit in the source in every case, so splitting invents nothing.
#
# One endpoint in the source is a class that does not resolve to a named structure
# and is therefore not written as an edge: see UNRESOLVED_CLASS_ENDPOINTS.
#
# `latency_s` is real time in seconds and is None on every edge.  Never steps: a
# latency stated in steps has assumed a clock.
# --------------------------------------------------------------------------

NAMED = "named without units, range or frame"
PARTIAL = "one component named, the rest owed"
PAYLOAD_OWED = "owed"
ROUTING = "routing statement, no synapse"


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    source_sub: str | None = None
    target_sub: str | None = None
    latency_s: float | None = None
    far_end_file: str = ""
    far_end_state: str = ""
    payload_state: str = PAYLOAD_OWED
    carries: str = ""
    internal: bool = False


HF, AM, BN = ("hippocampal formation", "amygdala",
              "bed nucleus of the stria terminalis")

# Internal edges.  Both ends inside one entry, so the two-ended diff does not
# apply to any of them and their payloads have to be read rather than diffed.
INTERNAL_EDGES: tuple[Edge, ...] = (
    Edge(HF, HF, "entorhinal cortex", "dentate gyrus, granule cells", None, "", "",
         NAMED, "the current multimodal scene plus a metric of space from the "
                "layer II grid code; the perforant path", True),
    Edge(HF, HF, "dentate gyrus, granule cells", "CA3", None, "", "",
         NAMED, "the same scene, sparsified; the payload change is the operation "
                "— pattern separation; the mossy fibres", True),
    Edge(HF, HF, "CA3", "CA3", None, "", "",
         NAMED, "the stored pattern under completion: a partial cue in, the whole "
                "pattern out; ~6,000-12,000 recurrent contacts per cell", True),
    Edge(HF, HF, "CA3", "CA1", None, "", "",
         NAMED, "the completed pattern; the Schaffer collaterals", True),
    Edge(HF, HF, "entorhinal cortex", "CA1", None, "", "",
         NAMED, "the unsparsified current scene, arriving alongside the completed "
                "pattern; the temporoammonic path — this edge is what makes the "
                "next one a comparison rather than a relay", True),
    Edge(HF, HF, "CA1", "subiculum", None, "", "",
         PAYLOAD_OWED, "the result of the comparison; what a comparison result is "
                       "on a wire is not stated anywhere, and the entry's claim to "
                       "be a comparator rests on this step", True),
    Edge(HF, HF, "subiculum", "entorhinal cortex", None, "", "",
         NAMED, "the completed episode, leaving by the port it came in by", True),

    Edge(AM, AM, "lateral nucleus", "basal nucleus", None, "", "",
         PARTIAL, "sensory identity codes entering intermediate processing; the "
                  "payload change is owed and is the step at which a stimulus "
                  "becomes a significance", True),
    Edge(AM, AM, "lateral nucleus", "accessory basal nucleus", None, "", "",
         PARTIAL, "as above", True),
    Edge(AM, AM, "basal nucleus", "central nucleus", None, "", "",
         PAYLOAD_OWED, "the evaluated signal on its way to the output stage", True),
    Edge(AM, AM, "accessory basal nucleus", "central nucleus", None, "", "",
         PAYLOAD_OWED, "as above", True),
    Edge(AM, AM, "intercalated cells", "central nucleus", None, "", "",
         NAMED, "inhibition — the gate on the output stage", True),
)

EDGES: tuple[Edge, ...] = INTERNAL_EDGES + (
    # ---- hippocampal formation, in ----
    Edge("inferotemporal cortex", HF, None, "entorhinal cortex", None, "01_visual_pathway", "unchecked",
         NAMED, "object and scene identity, invariant to position, size, pose and lighting"),
    Edge("temporal pole", HF, None, "entorhinal cortex", None, "07_anterior_temporal_lobe", "two-ended",
         PAYLOAD_OWED, "an amodal concept; modality-loss is the only checkable property"),
    Edge("angular gyrus", HF, None, None, None, "06_posterior_parietal", "producer's end only",
         PAYLOAD_OWED, "the loudest owed payload in the producer's own file"),
    Edge("precuneus", HF, None, None, None, "06_posterior_parietal", "producer's end only; owes a split",
         PAYLOAD_OWED, ""),
    Edge("posterior cingulate cortex", HF, None, None, None, "17_insula_claustrum_habenula", "untyped there",
         PAYLOAD_OWED, ""),
    Edge("retrosplenial cortex", HF, None, "entorhinal cortex", None, "17_insula_claustrum_habenula", "producer's end only",
         PARTIAL, "the return arm of the spatial-memory loop: heading and landmark "
                  "information after the egocentric-to-allocentric translation"),
    Edge("perirhinal cortex", HF, None, None, None, "none", "no entry in any file",
         PAYLOAD_OWED, ""),
    Edge("parahippocampal cortex", HF, None, None, None, "none", "no entry in any file",
         PAYLOAD_OWED, ""),
    Edge("medial septum, parvalbumin GABAergic pacemakers", HF,
         None, "inhibitory interneurons of CA1, CA3 and the dentate gyrus", None,
         "13_neuromodulatory_systems", "reciprocal split owed there",
         NAMED, "the theta timing reference — the phase of a 4-12 Hz rhythm, not content"),
    Edge("medial septum, glutamatergic cells", HF, None, None, None, "13_neuromodulatory_systems",
         "reciprocal split owed there",
         NAMED, "a tonic excitatory gate: the drive that determines whether the "
                "pacemakers oscillate at all"),
    Edge("medial septum, cholinergic cells", HF, None, None, None, "13_neuromodulatory_systems",
         "reciprocal split owed there",
         NAMED, "tonic gain and arousal state, largely by volume transmission "
                "(~93% of varicosities form no classic synapse); gates the "
                "theta-versus-ripple regime and does not set theta frequency"),
    Edge("ventral tegmental area", HF, None, None, None, "13_neuromodulatory_systems", "producer's end only",
         PAYLOAD_OWED, "dopamine, in the producer's terms"),
    Edge("locus coeruleus", HF, None, None, None, "13_neuromodulatory_systems", "brain-wide class names this structure",
         PAYLOAD_OWED, "noradrenaline: global gain and salience or surprise"),
    Edge("raphe nuclei", HF, None, None, None, "13_neuromodulatory_systems", "class covers without naming; owed there",
         PAYLOAD_OWED, ""),
    Edge("nucleus reuniens", HF, None, "CA1 and the subiculum", None, "12_thalamus", "two-ended",
         PAYLOAD_OWED, "the return arm of the prefrontal loop: medial prefrontal "
                       "cortex has no direct projection here, so this is the stage "
                       "through which it reaches this structure"),
    Edge(AM, HF, "basal nucleus", None, None, "", "producer is in this file",
         NAMED, "the valence tag — a gain on perception, attention and memory "
                "encoding, carrying no identity information of its own"),
    Edge(AM, HF, "accessory basal nucleus", None, None, "", "producer is in this file",
         NAMED, "the valence tag"),

    # ---- hippocampal formation, out ----
    Edge(HF, "fornix", "subiculum", None, None, "18_white_matter_tracts", "the tract has its own entry",
         ROUTING, "the completed episode in transit; no synapse, fan-in and "
                  "fan-out none, and the regions it reaches are their own edges"),
    Edge(HF, "mammillary bodies", "subiculum", None, None, "14_brainstem_midbrain_hypothalamus", "sub-element of the hypothalamus entry",
         PARTIAL, "a completed episode: bound, retrievable, content-addressable, "
                  "which the upstream identity codes are not; no units and no frame"),
    Edge(HF, "anterior thalamic nuclei", "subiculum", None, None, "12_thalamus", "consumer declares it",
         PARTIAL, "the completed episode; the Papez circuit"),
    Edge(HF, "hypothalamus", None, None, None, "14_brainstem_midbrain_hypothalamus", "untyped there", PAYLOAD_OWED, ""),
    Edge(HF, "angular gyrus", "subiculum", None, None, "06_posterior_parietal", "consumer declares it",
         PARTIAL, "the completed episode"),
    Edge(HF, "precuneus", "subiculum", None, None, "06_posterior_parietal", "consumer names the medial temporal lobe",
         PARTIAL, "the completed episode"),
    Edge(HF, "posterior cingulate cortex", None, None, None, "17_insula_claustrum_habenula", "untyped there",
         PARTIAL, "the completed episode"),
    Edge(HF, "retrosplenial cortex", "subiculum", None, None, "17_insula_claustrum_habenula", "untyped there",
         PARTIAL, "the completed episode"),
    Edge(HF, AM, "entorhinal cortex", "lateral nucleus", None, "", "consumer is in this file",
         NAMED, "episodic context — where am I, what is going on — which is what "
                "makes the same stimulus threatening in one place and not another"),
    Edge(HF, BN, "subiculum", None, None, "", "consumer is in this file",
         PARTIAL, "context; payload otherwise owed"),
    Edge(HF, "nucleus reuniens", "CA1 and the subiculum", None, None, "12_thalamus", "two-ended",
         PAYLOAD_OWED, "the outgoing limb of the reuniens pair; termination density "
                       "is topographic — denser in rostral reuniens, and denser again "
                       "where the injection includes the subicular complex"),
    Edge(HF, "orbitofrontal / ventromedial prefrontal cortex",
         "subiculum, prosubiculum and distal CA1",
         "layer III of Brodmann areas 11, 13, 14 and 25", None, "11_frontal_lobe", "two-ended",
         PARTIAL, "the completed episode, via the fornix; it terminates by name in "
                  "four of the consumer's five previously unused divisional sub-elements"),
    Edge(HF, "anterior cingulate cortex", "subiculum",
         "layer III of Brodmann area 24a only", None, "11_frontal_lobe",
         "two-ended; the sub-element restriction is finer than the consumer's own divisional set",
         PARTIAL, "the completed episode, via the fornix"),
    Edge(HF, "ventral pallidum", "subiculum", None, None, "09_basal_ganglia", "consumer's end only",
         PAYLOAD_OWED, ""),
    Edge(HF, "basal forebrain", None, None, None, "13_neuromodulatory_systems", "class covers without naming; owed there",
         PAYLOAD_OWED, "the return limb of the theta loop"),
    Edge(HF, "septum", None, None, None, "13_neuromodulatory_systems", "class covers without naming; owed there",
         PAYLOAD_OWED, "the return limb of the theta loop"),

    # ---- amygdala, in ----
    Edge("inferotemporal cortex", AM, None, "lateral nucleus", None, "01_visual_pathway", "unchecked",
         NAMED, "fully-processed object and face identity; slow, and specific"),
    Edge("anterior superior temporal gyrus and sulcus", AM, None, None, None, "02_auditory_pathway", "unchecked",
         NAMED, "voice identity and vocal affect, not speech content"),
    Edge("auditory parabelt, rostral division", AM, None, None, None, "02_auditory_pathway", "unchecked",
         NAMED, "sound-object identity, invariant to talker, pitch and level; a "
                "third auditory route, one tier earlier and so faster"),
    Edge("medial geniculate nucleus, magnocellular division", AM, None, None, None, "02_auditory_pathway", "unchecked",
         NAMED, "a coarse, broadly-tuned, barely-processed signal; the payload is "
                "deliberately impoverished and that is what buys the speed"),
    Edge("posterior thalamus", AM, None, None, None, "12_thalamus",
         "the producer declares no such edge; owed there or withdraw", PAYLOAD_OWED, ""),
    Edge("lateral olfactory tract", AM, None, "medial nucleus", None, "03_other_senses", "unchecked",
         NAMED, "the odour object"),
    Edge("insula", AM, None, None, None, "17_insula_claustrum_habenula", "two-ended, owed at both", PAYLOAD_OWED, ""),
    Edge("gustatory pathway", AM, None, None, None, "03_other_senses", "unchecked",
         NAMED, "taste quality and intensity"),
    Edge(HF, AM, "entorhinal cortex", None, None, "", "producer is in this file",
         NAMED, "episodic context"),
    Edge("lateral parabrachial nucleus", AM, None, "central nucleus", None, "14_brainstem_midbrain_hypothalamus",
         "producer's end only; contested there",
         PARTIAL, "the affective dimension of pain — the unpleasantness, as "
                  "distinct from location and intensity; monosynaptic and excitatory"),
    Edge("temporal pole", AM, None, None, None, "07_anterior_temporal_lobe", "two-ended",
         PAYLOAD_OWED, "an amodal concept, for affective evaluation"),
    Edge("ventromedial and orbital prefrontal cortex", AM, None, None, None, "11_frontal_lobe", "untyped there",
         PARTIAL, "a regulatory signal: suppression or licensing of the response"),
    Edge("ventral tegmental area", AM, None, None, None, "13_neuromodulatory_systems", "producer's end only",
         PAYLOAD_OWED, ""),
    Edge("locus coeruleus", AM, None, None, None, "13_neuromodulatory_systems", "reciprocal, one limb written there",
         PAYLOAD_OWED, ""),
    Edge("nucleus reuniens", AM, None,
         "basal and basomedial (accessory basal) nuclei", None, "12_thalamus", "two-ended",
         PAYLOAD_OWED, "stronger in primate than in rat or mouse, which is a species "
                       "claim and not a payload"),
    Edge("claustrum", AM, None, None, None, "17_insula_claustrum_habenula", "declared in prose, not as a typed edge",
         PAYLOAD_OWED, ""),

    # ---- amygdala, out ----
    Edge(AM, "hypothalamus", "central nucleus", None, None, "14_brainstem_midbrain_hypothalamus", "untyped there",
         NAMED, "a valence and urgency signal — this is bad (or good), act now — "
                "carrying no identity information"),
    Edge(AM, "periaqueductal gray", "central nucleus", None, None, "14_brainstem_midbrain_hypothalamus",
         "consumer names the sub-element; untyped there",
         NAMED, "the same valence and urgency signal, driving the defensive response"),
    Edge(AM, "locus coeruleus", "central nucleus", None, None, "13_neuromodulatory_systems", "untyped there",
         NAMED, "the same signal"),
    Edge(AM, "lateral parabrachial nucleus", "central nucleus", None, None, "14_brainstem_midbrain_hypothalamus",
         "the consumer declares no such edge; owed there",
         PAYLOAD_OWED, "the return limb of the affective-pain input"),
    Edge(AM, "basal forebrain", "central nucleus", None, None, "13_neuromodulatory_systems",
         "class covers without naming; owed there", PAYLOAD_OWED, ""),
    Edge(AM, "nucleus of the solitary tract", None, None, None, "14_brainstem_midbrain_hypothalamus", "two-ended, owed at both",
         PAYLOAD_OWED, "descending"),
    Edge(AM, BN, "basal nucleus", None, None, "", "consumer is in this file",
         NAMED, "the valence / threat signal; the heaviest edge of the extended amygdala"),
    Edge(AM, "temporal pole", "basal nucleus", None, None, "07_anterior_temporal_lobe", "two-ended",
         NAMED, "the valence tag"),
    Edge(AM, "insula", "basal nucleus", None, None, "17_insula_claustrum_habenula", "consumer declares it", NAMED, "the valence tag"),
    Edge(AM, "anterior cingulate cortex", "basal nucleus", None, None, "11_frontal_lobe", "payload owed there",
         NAMED, "the valence tag"),
    Edge(AM, "midcingulate cortex", "basal nucleus", None, None, "17_insula_claustrum_habenula", "untyped there",
         NAMED, "the valence tag"),
    Edge(AM, "orbitofrontal / ventromedial prefrontal cortex", "basal nucleus", None, None, "11_frontal_lobe",
         "untyped there", NAMED, "the valence tag"),
    Edge(AM, "right inferior frontal gyrus", "basal nucleus", None, None, "11_frontal_lobe", "untyped there",
         NAMED, "the valence tag"),
    Edge(AM, "nucleus reuniens", "basal and basomedial (accessory basal) nuclei", None, None,
         "12_thalamus", "two-ended",
         PAYLOAD_OWED, "the stage where both structures of this section and their "
                       "medial-prefrontal target converge on one nucleus"),
    Edge(AM, "dorsolateral prefrontal cortex",
         "basal nucleus, intermediate and magnocellular divisions",
         "Brodmann area 9 medially and laterally, patchily area 46", None,
         "11_frontal_lobe", "two-ended",
         NAMED, "the valence tag; the lightest and least consistent of the four "
                "lateral limbs — the area 46 label was present in one hemisphere "
                "and absent in the other of the same animal"),
    Edge(AM, "ventrolateral prefrontal cortex",
         "basal nucleus, intermediate and magnocellular divisions",
         "Brodmann area 47 in deep layer I, layer II and layer VI, continuing into area 45",
         None, "11_frontal_lobe", "two-ended",
         NAMED, "the valence tag; the densest of the four lateral limbs"),
    Edge(AM, "premotor cortex",
         "basal nucleus, intermediate and magnocellular divisions",
         "ventral area 6, lighter in dorsal area 6", None, "11_frontal_lobe", "two-ended",
         NAMED, "the valence tag; which sub-element receives it is owed, since the "
                "consumer names F2, F4 and F5 and the study divides area 6 dorsally "
                "and ventrally"),
    Edge(AM, "precentral opercular cortex",
         "basal nucleus, intermediate and magnocellular divisions", None, None,
         "none", "no entry in any file",
         NAMED, "the valence tag; particularly dense, and continuous with the area 45 "
                "and ventral area 6 label rather than separate from it"),
    Edge(AM, "mediodorsal thalamus", None, None, None, "12_thalamus", "consumer's end only",
         PARTIAL, "limbic value / significance context"),
    Edge(AM, "zona incerta", "central nucleus", "parvalbumin neurons", None, "12_thalamus", "consumer's end only",
         PAYLOAD_OWED, "the producer's role given at the consumer's end as fear"),
    Edge(AM, "raphe nuclei", None, None, None, "13_neuromodulatory_systems", "consumer's end only", PAYLOAD_OWED, ""),
    Edge(AM, "ventral pallidum", None, None, None, "09_basal_ganglia", "consumer's end only", PAYLOAD_OWED, ""),
    Edge(AM, "ventral striatum", None, None, None, "09_basal_ganglia",
         "the consumer's class does not even cover it; owed there", NAMED, "the valence tag"),
    Edge(AM, HF, "basal nucleus", None, None, "", "consumer is in this file", NAMED, "the valence tag"),

    # ---- bed nucleus, in ----
    Edge(AM, BN, "basal nucleus", None, None, "", "producer is in this file",
         NAMED, "the valence / threat signal, via the stria terminalis and the "
                "ventral amygdalofugal pathway"),
    Edge(HF, BN, "subiculum", None, None, "", "producer is in this file",
         PARTIAL, "episodic context"),
    Edge("anterior insula", BN, None, None, None, "17_insula_claustrum_habenula",
         "the producer declares no such edge; owed there", PARTIAL, "interoceptive state"),
    Edge("ventromedial and orbital prefrontal cortex", BN, None, None, None, "11_frontal_lobe",
         "the producer declares no such edge; owed there",
         PARTIAL, "regulatory control: suppression or licensing of the sustained response"),
    Edge("lateral parabrachial nucleus", BN, None, None, None, "14_brainstem_midbrain_hypothalamus", "two-ended, owed at both",
         PAYLOAD_OWED, "the same nucleus supplies the central amygdala's "
                       "affective-pain input, so the phasic and sustained arms "
                       "share a producer"),

    # ---- bed nucleus, out ----
    Edge(BN, "hypothalamus", None, "paraventricular nucleus", None, "14_brainstem_midbrain_hypothalamus",
         "the consumer declares no such edge; owed there",
         PARTIAL, "a sustained threat state: the same valence the central amygdala "
                  "emits but held over time and not tied to a cue"),
    Edge(BN, "periaqueductal gray", None, None, None, "14_brainstem_midbrain_hypothalamus",
         "the consumer declares no such edge; owed there", PARTIAL, "the same sustained threat state"),
    Edge(BN, "lateral parabrachial nucleus", None, None, None, "14_brainstem_midbrain_hypothalamus",
         "the consumer declares no such edge; owed there", PARTIAL, "the same sustained threat state"),
    Edge(BN, "ventral tegmental area", None, None, None, "13_neuromodulatory_systems",
         "the consumer declares no such edge; owed there", PARTIAL, "the same sustained threat state"),
)

SOURCE_EDGE_LINE_COUNT = 72      # the source counts bullets: 36 in, 36 out

# An endpoint the source names that is a class rather than a structure.  It is not
# written as an edge, because an edge names its target structure.
UNRESOLVED_CLASS_ENDPOINTS = (
    (BN, "brainstem autonomic and neuromodulatory centres",
     "a class; does not resolve to any named structure. Owed: name them."),
    (AM, "feedback to sensory areas",
     "the remainder of a class endpoint that was otherwise split into five named "
     "targets; the visual and auditory files are unchecked."),
)

# --------------------------------------------------------------------------
# Forward operation.
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


def allocate(structure: Structure, subelement: str):
    """Size the threshold and activity arrays for one sub-element.

    This is the first section in which this returns rather than raising.  Two of
    the three structures partition to their sub-elements and the partitions close,
    so nine of eleven sub-elements have a count to allocate against.

    What it returns is a size, not a usable array.  The threshold array can be
    sized because the count and the log2 bound are both in hand; the activity array
    can be sized for the same reason; neither can be *filled*, because the
    connection topology that would populate fan_in is unset.  Sizing and wiring are
    different blockers and only the first has cleared here.
    """
    for s in structure.subelements:
        if s.name == subelement:
            if s.count is None:
                raise NotImplementedError(
                    f"{structure.name} / {subelement}: no count. State is "
                    f"'{s.state}'. {s.note}"
                )
            lo, hi = s.parameter_bytes(False), s.parameter_bytes(True)
            return {
                "neurons": s.count,
                "threshold_bits": (s.bits(False), s.bits(True)),
                "threshold_bytes": (lo, hi),
                "active_bits": s.count,
                "active_bytes": s.count // 8,
                "fillable": False,
                "why_not_fillable": "connection topology is unset; the array can be "
                                    "sized and not populated",
            }
    raise ValueError(f"{subelement!r} is not a sub-element of {structure.name}")


def sign(source_sub, target_sub):
    """The sign an incoming edge contributes with.

    Not set at any rung, and this section has a named inhibitory edge that needs it:
    the amygdala's intercalated cells project inhibition onto the central nucleus, so
    at least one internal edge is subtractive and how it combines with the excitatory
    sum is stated nowhere.  threshold_gate() therefore takes counts the caller has
    summed rather than summing them itself, because a bare sum would silently assert
    that every input is excitatory.
    """
    raise NotImplementedError(
        "sign arithmetic is not set at any rung; the intercalated cells -> central "
        "nucleus edge is declared as inhibition and no rung says how an inhibitory "
        "contribution combines with an excitatory one in one sum"
    )


def edge_storage(edge: Edge):
    """Values in flight on one edge, which the per-edge-latency invariant creates.

    line_count * ceil(latency / update_interval) * bytes_per_value.  Four terms, and
    in this section at most one of them is ever available: the theta line carries a
    phase and every other payload is untyped, no fan-in or fan-out is recorded on any
    external edge, no latency is recorded anywhere, and the update interval waits on
    the scheduling discipline.  Recorded rather than estimated past, because a figure
    computed from assumed terms enters the file looking exactly like a derived one.
    Never summed with parameter memory or with state.
    """
    missing = ["line_count: no fan-in or fan-out is recorded on this edge",
               "latency: to derive, on every edge in this section",
               "update_interval: unset, and waiting on the scheduling discipline"]
    if edge.payload_state != NAMED:
        missing.append("bytes_per_value: the payload is not typed")
    raise NotImplementedError(
        f"{edge.source} -> {edge.target}: " + "; ".join(missing)
    )


def fan_in_map(structure: Structure):
    """Which source lines converge on each neuron.

    Still not implementable, and this section makes the shape of the gap sharper
    rather than closing it.  Two convergence *quantities* are recorded here — CA3's
    ~6,000-12,000 recurrent contacts per cell, and the amygdala's ~11:1 funnel from
    the 4.00M lateral nucleus to the 0.36M central nucleus — and neither is a
    convergence *pattern*.  A count of contacts does not say which cells they are
    from, and a population ratio does not either.

    The amygdala case is the pointed one: the source records the 11:1 ratio and
    notes that the fan-in slots ought to reflect it and do not.  So the constraint
    exists, is measured, and has no slot it can be written into that this rung
    could read.
    """
    raise NotImplementedError(
        "connection topology is not set; two convergence quantities are recorded "
        "in this section (CA3 recurrent contacts per cell, and the amygdala's "
        "11.11:1 lateral-to-central population funnel) and neither is a pattern"
    )


def step(*args, **kwargs):
    """There is no step, and in this section the temptation to write one is real.

    Every edge here has a nonzero, finite, heterogeneous latency in real time, and
    there is no global clock in the described system to replace them with.  A loop
    with real heterogeneous delays settles by its own dynamics; the same loop broken
    by registers becomes an iterated map whose trajectory depends on the update
    rate.  Those are two different systems computing two different things.

    This section contains a 4-12 Hz rhythm with a real period, 83-250 ms, and it
    would serve as an update rate if it were one.  It is not.  See
    THETA_IS_NOT_A_CLOCK.  Taking it as a step would set the whole system's tick
    from one structure's local pacemaker, which is the substitution the invariant
    exists to prevent, and it would also be wrong on its own terms: the rhythm's
    frequency is set by an intrinsic channel current, it paces one structure, and
    it arrives on an edge whose own latency is unrecorded.

    Three closed loops run inside this section and a fourth leaves it.  Every limb
    of all four is unmeasured, so even the sanctioned shortcut — set every latency
    equal and choose an interval short enough to carry the finest one — has no
    parameter to take.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; "
        "every edge latency in this section reads 'to derive'. The 4-12 Hz theta "
        "rhythm is a payload on one input edge and is not an update rate"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    This section is where that absence is most visible rather than most harmless.
    CA3 is described as a one-shot episodic binder — a recurrent autoassociator
    whose whole function is to store a pattern on a single presentation — and a
    structure that stores nothing on any presentation does not do that.  The module
    is still coherent: thresholds are read-only construction constants and the
    section runs open-loop.  But open-loop is not what CA3 is for, and the gap
    between the two is the learning rule.
    """
    raise NotImplementedError(
        "no learning rule is set; CA3's declared one-shot binding cannot be "
        "implemented by a structure whose thresholds are never written"
    )


# --------------------------------------------------------------------------
# Derived sizing — independent recomputation, not transcription.
# --------------------------------------------------------------------------


def edge_count_report() -> str:
    """Compute the edge count rather than carrying any rung's figure.

    Two of the three figures count different quantities and agree once that is said:
    the source counts bullets and some bullets name more than one target.  The third
    difference is real, is one edge wide, and its source is not established at either
    rung.

    SOURCE_EDGE_LINE_COUNT is checked against the source's own header rather than
    inherited.  A constant naming another file's count is the kind that goes stale
    silently, and a stale one reads as the other rung's error rather than as this
    file's own.
    """
    ext = [e for e in EDGES if not e.internal]
    out = [f"  edges declared in this module : {len(EDGES)}"
           f"   ({len(ext)} external, {len(INTERNAL_EDGES)} internal)"]
    out.append(f"  the source's header states {SOURCE_EDGE_LINE_COUNT} edge lines, "
               f"36 in and 36 out, and a")
    out.append("    count of its edge bullets returns the same")
    out.append("  the architecture declares 81: a count of its arrow-headed endpoints")
    out.append("    returns 84, of which three claustral endpoints are declined as edges")
    out.append(f"  so this module declares {len(ext)} between structures against that 81:")
    out.append("    the difference is one edge and its source is not established")
    out.append("  owed: find it, at whichever rung is wrong")
    return "\n".join(out)


# What this module still owes, recorded here rather than left implicit.
MIGRATION_OWED = (
    "SubElement, Structure and Edge are declared in this module and the last two are "
    "also declared in Brain_config, which is the drift Brain_config exists to prevent: "
    "every external edge here is declared in two files, and two files cannot describe "
    "one edge in agreement when the type describing it is defined twice. The sibling "
    "modules for 06 and 07 import the Brain_config types; this one does not yet. "
    "Migrating it is mechanical but touches all 94 edge declarations, so it is recorded "
    "rather than done half-way -- a half-migrated module carries both definitions at "
    "once, which is worse than either end.",
)


def partition_report() -> str:
    out = []
    for s in STRUCTURES:
        t = s.total_neurons()
        if t is None or s.stated_total is None:
            out.append(f"  {s.name}: no partition to check "
                       f"({len([x for x in s.subelements if x.count is None])} "
                       f"sub-elements without a count)")
            continue
        closes, diff = s.partition_closes()
        out.append(f"  {s.name}: parts sum to {t/1e6:.2f}M against a stated "
                   f"{s.stated_total/1e6:.1f}M — difference {diff:+.2f}M — "
                   f"{'closes' if closes else 'DOES NOT CLOSE'}")
    return "\n".join(out)


def sizing_report() -> str:
    lines = [f"{'structure / sub-element':52} {'neurons':>12} {'bits':>7} {'store':>18}"]
    tot_lo = tot_hi = 0
    unstated = []
    for s in STRUCTURES:
        for e in s.subelements:
            lo, hi = e.parameter_bytes(False), e.parameter_bytes(True)
            count = f"{e.count:,}" if e.count is not None else e.state
            if lo is None:
                lines.append(f"{s.name + ' / ' + e.name:52} {count:>12} {'-':>7} {'to derive':>18}")
                unstated.append(f"{s.name} / {e.name}")
                continue
            b = (f"{e.bits(False)}" if e.bits(False) == e.bits(True)
                 else f"{e.bits(False)}-{e.bits(True)}")
            store = (f"{lo/1e6:.2f} MB" if lo == hi else f"{lo/1e6:.2f}-{hi/1e6:.2f} MB")
            tot_lo += lo
            tot_hi += hi
            lines.append(f"{s.name + ' / ' + e.name:52} {count:>12} {b:>7} {store:>18}")
    lines.append("")
    lines.append(f"stated total: {tot_lo/1e6:.2f}-{tot_hi/1e6:.2f} MB   (per hemisphere)")
    lines.append(f"a floor, not a ceiling: {len(unstated)} sub-elements have no count")
    for u in unstated:
        lines.append(f"    {u}")
    return "\n".join(lines)


def allocation_report() -> str:
    out = []
    ok = blocked = 0
    for s in STRUCTURES:
        for e in s.subelements:
            try:
                a = allocate(s, e.name)
                ok += 1
                out.append(f"  {s.name + ' / ' + e.name:52} "
                           f"threshold {a['threshold_bytes'][0]/1e6:7.2f} MB   "
                           f"active {a['active_bytes']/1e6:6.2f} MB   sized, not fillable")
            except NotImplementedError:
                blocked += 1
                out.append(f"  {s.name + ' / ' + e.name:52} blocked — {e.state}")
    out.append(f"  allocatable: {ok} of {ok+blocked} sub-elements. "
               f"Every one of them is sized and none is fillable.")
    return "\n".join(out)


def density_cross_check() -> str:
    out = []
    # Hippocampus proper excludes entorhinal cortex, which is separately located.
    hp = HIPPOCAMPAL_FORMATION.total_neurons() - 6_000_000
    out.append(f"  hippocampus proper {hp/1e6:.1f}M ({HIPPOCAMPAL_FORMATION.volume_note}):")
    for v in HIPPOCAMPAL_FORMATION.volume_cm3:
        out.append(f"    {v:.2f} cm3 -> {hp/(v*1000):9,.0f} /mm3")
    out.append(f"    full literature span 1.7-5.7 cm3 -> {hp/5700:,.0f} to {hp/1700:,.0f} /mm3"
               f"  (a {(hp/1700)/(hp/5700):.1f}x spread)")
    am = AMYGDALA.total_neurons()
    out.append(f"  amygdala {am/1e6:.2f}M ({AMYGDALA.volume_note}):")
    for v in AMYGDALA.volume_cm3:
        out.append(f"    {v:.2f} cm3 -> {am/(v*1000):9,.0f} /mm3")
    out.append(f"  {BED_NUCLEUS.name}: no count and no volume figure — "
               f"no cross-check can be run")
    return "\n".join(out)


def convergence_report() -> str:
    lat = next(e for e in AMYGDALA.subelements if e.name == "lateral nucleus")
    cen = next(e for e in AMYGDALA.subelements if e.name == "central nucleus")
    return (f"  amygdala lateral {lat.count/1e6:.2f}M -> central {cen.count/1e6:.2f}M "
            f"= {lat.count/cen.count:.2f}:1 population funnel across the internal edges.\n"
            f"  Identity codes arrive at the lateral nucleus; a valence signal with no\n"
            f"  identity leaves the central one. The compression ratio and the payload\n"
            f"  loss are the same fact measured two ways.")


def theta_report() -> str:
    lo, hi = theta_period_ms()
    return (f"  {THETA_HZ[0]:.0f}-{THETA_HZ[1]:.0f} Hz -> a period of {lo:.1f}-{hi:.1f} ms.\n"
            f"  The only real-time figure in the section, and not an edge latency.\n  "
            + THETA_IS_NOT_A_CLOCK.replace(". ", ".\n  "))


def edge_report() -> str:
    internal = [e for e in EDGES if e.internal]
    external = [e for e in EDGES if not e.internal]
    stated = [e for e in EDGES if e.latency_s is not None]
    section = {HF, AM, BN}
    no_entry = sorted(({e.target for e in EDGES if e.far_end_file == "none"} |
                       {e.source for e in EDGES if e.far_end_file == "none"})
                      - section)
    inbound = [e for e in external if e.target in section and e.source not in section]
    outbound = [e for e in external if e.source in section and e.target not in section]
    within = [e for e in external if e.source in section and e.target in section]
    out = [f"  edges: {len(EDGES)}  ({len(external)} between structures, "
           f"{len(internal)} inside one structure)",
           f"    inbound from outside the section:  {len(inbound)}",
           f"    outbound to outside the section:   {len(outbound)}",
           f"    between two structures in the section: {len(within)}  "
           f"(each written at both ends, so counted twice in the source's bullets)",
           f"  the source counts {SOURCE_EDGE_LINE_COUNT} bullets, 36 in and 36 out; ten "
           f"bullets name more than one target structure",
           f"  with a stated latency: {len(stated)}    to derive: {len(EDGES) - len(stated)}"]
    for state in (NAMED, PARTIAL, PAYLOAD_OWED, ROUTING):
        n = len([e for e in EDGES if e.payload_state == state])
        out.append(f"  payloads {state}: {n}")
    out.append(f"  payloads with units, a range or a coordinate frame: 0 of {len(EDGES)}")
    out.append(f"  far ends with no entry in any file: {', '.join(no_entry)}")
    out.append("  endpoints that are classes and are not written as edges:")
    for src, name, why in UNRESOLVED_CLASS_ENDPOINTS:
        out.append(f"    {src} -> {name}: {why}")
    return "\n".join(out)


if __name__ == "__main__":
    print("partition closure:")
    print(partition_report())
    print()
    print(sizing_report())
    print()
    print("allocation:")
    print(allocation_report())
    print()
    print("density cross-check:")
    print(density_cross_check())
    print()
    print("internal convergence:")
    print(convergence_report())
    print()
    print("theta:")
    print(theta_report())
    print()
    print("edges:")
    print(edge_count_report())
    print()
    print(edge_report())
    print()
    for fn, label in ((fan_in_map, "connectivity"), (step, "scheduler"), (learn, "learning")):
        try:
            fn(HIPPOCAMPAL_FORMATION) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"{label:14} blocked: {exc}")
