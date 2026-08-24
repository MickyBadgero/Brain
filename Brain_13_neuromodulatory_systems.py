"""Brain — neuromodulatory systems: the four diffuse sources.

Structures, edges and the threshold-gate forward operation for the ventral
tegmental area, the locus coeruleus, the raphe nuclei and the basal forebrain.
Each neuron is a threshold gate over equal-weight inputs: it fires when the count
of active inputs crosses a stored threshold, so the only value held per neuron is
that threshold, at log2(fan-in) bits.  No weights, no multiply, no gradient.

Every element counted here is a threshold gate.  No transducer and no graded
non-spiking population is described in this section, so the three-code-path
problem of the visual line does not recur and log2(fan-in) applies to every
neuron.  All of the difficulty has moved from the elements to the edges.

Counting basis is not uniform, and two of the four structures declare no basis at
all: the locus coeruleus is counted per side, the raphe is midline and reported
whole, and the ventral tegmental area and basal forebrain carry order-of-magnitude
counts with no basis stated.  A factor of two sits between the two readings of an
undeclared basis, so it is recorded as unset rather than assumed to be per side.

Forty-five edges, twenty in and twenty-five out, and not one has both ends inside
this section: these four structures do not connect to each other.  Fourteen endpoints
name a class rather than a structure, inherited from the biology's own record,
which marks each of them as owed.

Five of the six surface-before-touching items are needed here and none is set: the
inter-structure connection topology, the tile geometry, the sparsity, the
scheduling discipline and the learning rule.  Where each is needed the module
raises rather than choosing.  The learning rule is the one that differs from the
visual line: there it left a runnable artifact that simply did not learn, and here
the reward-prediction-error edge exists in order to gate synaptic change, so with
no rule the structure's output is a no-op rather than a reduced effect.

Every edge latency is unstated in the biology and reads None.  None means "to
derive" and is not a licence to substitute zero or a uniform step.  This section
does contain a real oscillator - the 4-12 Hz theta reference on one edge between
the medial septum and the hippocampus - and it is a payload on that edge, not a
clock for this module.  The biology containing an oscillator is not the system
containing a clock.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2

# --------------------------------------------------------------------------
# Element classes.
#
# The vocabulary is carried from the visual line so the two modules classify the
# same way.  Only the first class occurs here: the dopaminergic, GABAergic,
# glutamatergic, noradrenergic, serotonergic and cholinergic populations of these
# four structures all generate action potentials.
# --------------------------------------------------------------------------

THRESHOLD_GATE = "threshold_gate"   # spikes; stores a threshold at log2(fan-in) bits
TRANSDUCER = "transducer"           # converts a physical stimulus; stores no threshold
GRADED = "graded"                   # computes without spiking; store not established

# --------------------------------------------------------------------------
# Edge classes.
#
# Most edges are conduction plus synaptic transmission.  One here is not: the
# cholinergic projection from the medial septum to the hippocampus is delivered
# largely by volume transmission, about 93% of its varicosities forming no classic
# synapse, so the transmitter reaches its targets by diffusion through the
# extracellular space.  A diffusion time and a conduction time are different
# quantities and do not scale the same way with distance, so the class is carried
# on the edge rather than assumed uniform.
# --------------------------------------------------------------------------

SYNAPTIC = "synaptic"               # conduction plus synaptic transmission
VOLUME = "volume_transmission"      # release into extracellular space; reaches a volume

# --------------------------------------------------------------------------
# Structures.
#
# Counts are the architecture's, carried with their basis.  `fan_in` is the
# convergence onto one neuron of this population where the biology fixes it, and
# None where it does not - which is everywhere in this section.  With no measured
# fan-in anywhere, every width below is the 16-bit log2 ceiling and not a measured
# value, and every store is therefore an upper bound.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Population:
    name: str
    kind: str
    basis: str
    count: int | None            # None where the biology has not fixed it
    fan_in: int | None           # None where the biology has not fixed it
    fan_in_bound: int = 16       # log2 cap: any fan-in under ~65,000 fits 16 bits

    @property
    def threshold_bits(self) -> int | None:
        """Stored bits per neuron under the threshold-gate model."""
        if self.kind == TRANSDUCER:
            return 0
        if self.kind == GRADED:
            return None          # not zero, and not log2(fan-in): not established
        if self.fan_in is None:
            return self.fan_in_bound
        if self.fan_in <= 1:
            return 0             # nothing to threshold against a single input
        return ceil(log2(self.fan_in))

    @property
    def parameter_bytes(self) -> int | None:
        bits = self.threshold_bits
        if bits is None or self.count is None:
            return None
        return self.count * bits // 8


@dataclass(frozen=True)
class Structure:
    name: str
    populations: tuple[Population, ...]
    subelements: tuple[str, ...] = ()

    @property
    def parameter_bytes(self) -> int | None:
        """None if any population's store is unstated - a partial sum would read as a total."""
        total = 0
        for p in self.populations:
            b = p.parameter_bytes
            if b is None:
                return None
            total += b
        return total


PER_SIDE = "per side"
WHOLE_MIDLINE = "whole (midline)"
UNDECLARED = "to derive"

# The composition is stated as fractions of an order-of-magnitude total, so the
# partition is exact in shape and soft in extent.  It is one of the few counts on
# the map that partitions to its own cell classes at all.
VENTRAL_TEGMENTAL_AREA = Structure(
    "ventral tegmental area",
    (
        Population("dopaminergic (~65%)", THRESHOLD_GATE, UNDECLARED, 65_000, None),
        Population("GABAergic (~30%)", THRESHOLD_GATE, UNDECLARED, 30_000, None),
        Population("glutamatergic (~5%)", THRESHOLD_GATE, UNDECLARED, 5_000, None),
    ),
    subelements=("dopaminergic", "GABAergic", "glutamatergic"),
)

# The one firm human figure in the section.  The dorsal and ventral tiers are
# described as having partly different targets, which is the test for sub-element
# status, but no set is named and no partition of the count exists - so the extent
# is known and the first axis is not, the reverse of the usual case.
LOCUS_COERULEUS = Structure(
    "locus coeruleus",
    (Population("noradrenergic", THRESHOLD_GATE, PER_SIDE, 50_000, None),),
    subelements=("dorsal tier", "ventral tier"),
)

# The one count here is for a sub-element and not the structure: the dorsal raphe
# is the largest of three divisions with different projection targets, and the
# median and caudal divisions are uncounted.  Halving for a per-side figure would
# assert a symmetry the biology does not state.
RAPHE = Structure(
    "raphe nuclei",
    (
        Population("dorsal raphe, serotonergic", THRESHOLD_GATE, WHOLE_MIDLINE, 165_000, None),
        Population("dorsal raphe, non-serotonergic", THRESHOLD_GATE, WHOLE_MIDLINE, 70_000, None),
        Population("median raphe", THRESHOLD_GATE, WHOLE_MIDLINE, None, None),
        Population("caudal raphe", THRESHOLD_GATE, WHOLE_MIDLINE, None, None),
    ),
    subelements=("dorsal raphe", "median raphe", "caudal raphe"),
)

# The structure is named for its cholinergic population and that population is not
# the bulk of its output: the GABAergic and glutamatergic projections together are
# reported to be the majority, and neither has a count.  This is the one place in
# the section where the missing count is known to exceed the recorded one.
BASAL_FOREBRAIN = Structure(
    "basal forebrain",
    (
        Population("cholinergic", THRESHOLD_GATE, UNDECLARED, 100_000, None),
        Population("parvalbumin GABAergic", THRESHOLD_GATE, UNDECLARED, None, None),
        Population("glutamatergic", THRESHOLD_GATE, UNDECLARED, None, None),
    ),
    # Two crossed axes, not one nested one: three edges leave the medial septum on
    # three different transmitters, and two edges leave the parvalbumin population
    # for two different targets.
    subelements=("medial septum", "diagonal band", "nucleus basalis of Meynert",
                 "cholinergic", "parvalbumin GABAergic", "glutamatergic"),
)

STRUCTURES = (VENTRAL_TEGMENTAL_AREA, LOCUS_COERULEUS, RAPHE, BASAL_FOREBRAIN)

# --------------------------------------------------------------------------
# Edges.
#
# An edge names its target sub-element where the biology terminates on one.  Two
# edges run from the basal forebrain to the thalamic reticular nucleus with
# opposite behavioural consequences, separated only by which transmitter
# population they leave from, which is what makes the transmitter axis
# load-bearing rather than descriptive.
#
# `endpoint_is_class` marks the fourteen endpoints that name a class rather than a
# structure.  They are inherited from the biology's own record, which marks each
# owed, and they are not repaired at this rung.
#
# `latency_s` is real time in seconds.  It is None on every edge here because the
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
    far_end_file: int | None = None     # which section holds the other end
    carries: str = ""


EDGES: tuple[Edge, ...] = (
    # ---- ventral tegmental area, in ----
    Edge("nucleus accumbens / ventral striatum", "ventral tegmental area",
         None, None, None, False, SYNAPTIC, 9, "payload owed"),
    Edge("ventral pallidum", "ventral tegmental area",
         None, "GABAergic", None, False, SYNAPTIC, 9,
         "disinhibition of the dopamine cells; the motivational limb"),
    Edge("prefrontal cortex", "ventral tegmental area",
         None, None, None, True, SYNAPTIC, 11, "payload owed; endpoint names a class"),
    Edge("lateral hypothalamus", "ventral tegmental area",
         None, None, None, False, SYNAPTIC, 14, "payload owed"),
    Edge("laterodorsal and pedunculopontine tegmental nuclei", "ventral tegmental area",
         None, "dopaminergic", None, False, SYNAPTIC, 14,
         "a cholinergic and glutamatergic drive onto the dopamine cells"),
    Edge("lateral habenula, via the rostromedial tegmental nucleus", "ventral tegmental area",
         None, None, None, False, SYNAPTIC, 17,
         "a negative reward-prediction error; the opponent brake, sign-inverted by the relay"),
    Edge("amygdala", "ventral tegmental area",
         None, None, None, False, SYNAPTIC, 8,
         "a sustained threat / defence state, not a discrete stimulus"),

    # ---- ventral tegmental area, out ----
    Edge("ventral tegmental area", "nucleus accumbens / ventral striatum",
         "dopaminergic", None, None, False, SYNAPTIC, 9,
         "dopamine carrying a reward-prediction error; the mesolimbic limb"),
    Edge("ventral tegmental area", "striatal dopamine-modulated projection neurons",
         "dopaminergic", None, None, False, SYNAPTIC, 9,
         "the same error as a three-factor plasticity signal gating synaptic change"),
    Edge("ventral tegmental area", "prefrontal cortex",
         "dopaminergic", None, None, False, SYNAPTIC, 11,
         "dopamine setting the gain on working-memory and rule representations"),
    Edge("ventral tegmental area", "amygdala",
         "dopaminergic", None, None, False, SYNAPTIC, 8, "payload owed"),
    Edge("ventral tegmental area", "hippocampus",
         "dopaminergic", None, None, False, SYNAPTIC, 8,
         "a novelty / salience signal gating what is encoded"),

    # ---- locus coeruleus, in ----
    Edge("nucleus paragigantocellularis", "locus coeruleus",
         None, None, None, False, SYNAPTIC, 14,
         "the principal excitatory drive setting the firing mode; payload otherwise owed"),
    Edge("prefrontal cortex", "locus coeruleus",
         None, None, None, True, SYNAPTIC, 11, "payload owed; endpoint names a class"),
    Edge("hypothalamus", "locus coeruleus",
         None, None, None, False, SYNAPTIC, 14, "payload owed"),
    Edge("amygdala", "locus coeruleus",
         "central nucleus", None, None, False, SYNAPTIC, 8,
         "a threat / salience signal recruiting global arousal in proportion to threat"),
    Edge("ventrolateral periaqueductal grey", "locus coeruleus",
         None, None, None, False, SYNAPTIC, 14,
         "the periaqueductal limb of descending noradrenergic analgesia"),

    # ---- locus coeruleus, out ----
    Edge("locus coeruleus", "cerebral cortex",
         None, None, None, True, SYNAPTIC, None,
         "global gain / arousal plus a phasic salience transient; no stimulus content"),
    Edge("locus coeruleus", "hippocampus",
         None, None, None, False, SYNAPTIC, 8, "the gain and salience signal"),
    Edge("locus coeruleus", "amygdala",
         None, None, None, False, SYNAPTIC, 8,
         "the gain and salience signal; reciprocal with the central-nucleus input"),
    Edge("locus coeruleus", "cerebellar cortex",
         None, None, None, False, SYNAPTIC, 10, "noradrenaline setting global gain"),
    Edge("locus coeruleus", "thalamus",
         None, None, None, True, SYNAPTIC, 12,
         "the gain and arousal signal, no content; endpoint names a class"),
    Edge("locus coeruleus", "spinal cord",
         None, "dorsal horn", None, False, SYNAPTIC, 16,
         "part of descending modulation of the dorsal horn"),
    Edge("locus coeruleus", "further subcortical targets",
         None, None, None, True, SYNAPTIC, None,
         "the gain and arousal signal; the recorded remainder of the brain-wide reach"),

    # ---- raphe, in ----
    Edge("prefrontal cortex", "raphe nuclei",
         None, None, None, True, SYNAPTIC, 11, "payload owed; endpoint names a class"),
    Edge("hypothalamus", "raphe nuclei",
         None, None, None, False, SYNAPTIC, 14, "payload owed"),
    Edge("lateral habenula", "raphe nuclei",
         None, None, None, False, SYNAPTIC, 17,
         "a negative / aversive value signal; the same bad-outcome output that brakes dopamine"),
    Edge("amygdala", "raphe nuclei",
         "central nucleus", None, None, False, SYNAPTIC, 8, "payload owed"),

    # ---- raphe, out ----
    Edge("raphe nuclei", "cerebral cortex",
         None, None, None, True, SYNAPTIC, None,
         "the serotonergic modulatory state signal; no stimulus content"),
    Edge("raphe nuclei", "striatum",
         None, None, None, True, SYNAPTIC, 9, "the modulatory signal; endpoint names a class"),
    Edge("raphe nuclei", "limbic system",
         None, None, None, True, SYNAPTIC, 8,
         "the modulatory signal; endpoint names a class and does not resolve"),
    Edge("raphe nuclei", "spinal dorsal horn and intermediolateral cell column",
         "caudal raphe", None, None, False, SYNAPTIC, 16,
         "neuromodulatory state; part of descending pain modulation, the analgesia limb"),
    Edge("raphe nuclei", "further forebrain and limbic targets",
         None, None, None, True, SYNAPTIC, None,
         "the modulatory signal; the recorded remainder of the brain-wide reach"),

    # ---- basal forebrain, in ----
    Edge("limbic and prefrontal cortex", "basal forebrain",
         None, None, None, True, SYNAPTIC, None,
         "descending cortical control; payload owed; endpoint names a class"),
    Edge("amygdala", "basal forebrain",
         "central nucleus", None, None, False, SYNAPTIC, 8, "payload owed"),
    Edge("hypothalamus", "basal forebrain",
         None, None, None, False, SYNAPTIC, 14, "payload owed"),
    Edge("brainstem", "basal forebrain",
         None, None, None, True, SYNAPTIC, 14,
         "the ascending arousal drive; payload owed; endpoint names a class"),

    # ---- basal forebrain, out ----
    Edge("basal forebrain", "cerebral cortex",
         "nucleus basalis of Meynert", None, None, True, SYNAPTIC, None,
         "acetylcholine as a plasticity / learning-gain and attention signal, not content"),
    Edge("basal forebrain", "hippocampus",
         "medial septum, cholinergic", None, None, False, VOLUME, 8,
         "a tonic gain / arousal-state signal by diffusion; gates theta-vs-ripple, does not pace theta"),
    Edge("basal forebrain", "hippocampal inhibitory interneurons",
         "medial septum, parvalbumin GABAergic", None, None, False, SYNAPTIC, 8,
         "the theta timing reference: the phase of a 4-12 Hz intrinsic membrane oscillation"),
    Edge("basal forebrain", "hippocampus",
         "medial septum, glutamatergic", None, None, False, SYNAPTIC, 8,
         "a tonic excitatory gate toggling the pacemakers between theta and non-theta states"),
    Edge("basal forebrain", "cortical inhibitory interneurons",
         "parvalbumin GABAergic", None, None, False, SYNAPTIC, None,
         "inhibition onto inhibitory targets; net cortical effect is activation, entraining gamma"),
    Edge("basal forebrain", "thalamic reticular nucleus",
         "parvalbumin GABAergic", None, None, False, SYNAPTIC, 12,
         "inhibition of the gate, so disinhibition of the relay nuclei behind it"),
    Edge("basal forebrain", "thalamic reticular nucleus",
         "cholinergic", None, None, False, SYNAPTIC, 12,
         "payload owed; promotes sleep, opposite in sign to the parvalbumin edge"),
    Edge("basal forebrain", "further subcortical targets",
         None, None, None, True, SYNAPTIC, None,
         "the relevant population's signal; the recorded remainder"),
)

# --------------------------------------------------------------------------
# Forward operation.
#
# This is the whole of what the rungs above specify.  It is correct for every
# neuron in this section and it does not express what any of these four
# structures sends, which is the finding rather than a shortcoming of the code.
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


# --------------------------------------------------------------------------
# The four operations the payloads name and the model has no term for.
#
# Each raises.  Implementing any of them is a modelling decision that belongs
# above this rung, and the alternative - dropping the edge and letting these
# structures behave as ordinary threshold-gate populations - would be a faithful
# implementation of the arrays and an unfaithful one of the biology.
# --------------------------------------------------------------------------


def apply_gain(*args, **kwargs):
    """Multiply the effective strength of whatever other edges are active.

    Not implementable under the sizing model.  The locus coeruleus payload is
    described as a scalar that multiplies other edges' effective strength, and
    `count[j] = sum(active_source[i])` has no multiplicand.  Modelling the gain as
    one more active input is wrong in a checkable way: doubling arousal would move
    the count by one, and the sum saturates where a gain does not.  Writing
    `count[j] = g * sum(...)` is a different model - it reintroduces a multiply and
    a graded value, which is what the threshold-gate model was adopted to remove.
    """
    raise NotImplementedError(
        "a multiplicative gain has no term in a count of active inputs over a "
        "threshold; extending or replacing the model is not this rung's decision"
    )


def apply_plasticity_signal(*args, **kwargs):
    """Gate synaptic change with a reward-prediction error.

    Not implementable.  This payload does not change `active` at all - it changes
    what the receiving structure stores, which is `threshold`, and nothing writes
    `threshold` because no learning rule is set.  Unlike the visual line, where an
    unset rule still left a runnable module that simply did not learn, here the
    edge exists in order to gate change: with no rule the ventral tegmental area's
    striatal output is a no-op rather than a reduced effect.
    """
    raise NotImplementedError(
        "no learning rule is set, and this edge's entire declared function is to "
        "gate one; the learning rule is a surface-before-touching item"
    )


def deliver_by_volume(*args, **kwargs):
    """Release into the extracellular space and reach a volume.

    Not implementable, and not for want of a number.  About 93% of the cholinergic
    varicosities on this projection form no classic synapse, so the edge reaches a
    volume rather than a fan-in list.  There is no `fan_in(j)` to write for it even
    in principle: the missing thing is not a map, it is the wrong data structure.
    A spatial delivery model, and the geometry it would run on, are decisions above
    this rung.
    """
    raise NotImplementedError(
        "volume transmission reaches a volume, not a list of contacts; no "
        "connectivity representation here can hold it"
    )


def phase_reference(*args, **kwargs):
    """Carry the phase of the theta oscillation.

    Not implementable.  A phase is a time, not an amount, and neither `active` nor
    `threshold` holds one.  The tick is an intrinsic hyperpolarisation-activated
    membrane current in the pacemaker cells, so the oscillator is a property of the
    source population and not of the wire.

    This is also the module's live hazard: the rhythm is a real number with real
    units sitting in the contract, and adopting it as an update rate would convert
    loops with heterogeneous delays into an iterated map whose trajectory depends
    on that rate.  It paces the hippocampus and nothing else.  See `step`.
    """
    raise NotImplementedError(
        "a phase is not an activity bit and not a threshold; and the 4-12 Hz theta "
        "reference is a payload on one edge, not a clock for this module"
    )


# --------------------------------------------------------------------------
# Blocked on decisions above or beside this rung.
# --------------------------------------------------------------------------


def fan_in_map(structure: Structure, subelement: str | None = None):
    """Which source lines converge on each neuron.

    Not implementable, and less so than on the visual line.  There the biology gave
    fan-in as a scalar per structure and stated the pattern in prose - retinotopy,
    a space-variant compression ratio - so what was missing was a function to be
    written from a described geometry.  Here every fan-in and fan-out on all
    forty-five edges reads unknown, the projection is diffuse with single axons
    branching to multiple non-adjacent territories, and fourteen of the endpoints name
    a class rather than a structure.  There is no geometry to write and no target
    list to write it against.
    """
    raise NotImplementedError(
        "connection topology is not set; it must be surfaced before it is chosen. "
        "Every fan-in in this section reads unknown and fourteen endpoints name a class."
    )


def allocate(structure: Structure, subelement: str):
    """Size the threshold and activity arrays for one sub-element.

    Implementable for exactly one structure and not for the other three.  The
    ventral tegmental area's count partitions to its cell classes, because the
    composition is given as fractions.  The locus coeruleus has an extent and no
    named sub-element set; the raphe has a count for one of three divisions; the
    basal forebrain has two crossed axes and a count for one class on one of them,
    and the uncounted populations are reported to be the larger part.
    """
    if subelement not in structure.subelements:
        raise ValueError(f"{subelement!r} is not a sub-element of {structure.name}")
    for p in structure.populations:
        if p.name.startswith(subelement) and p.count is not None:
            bits = p.threshold_bits
            return {"neurons": p.count, "threshold_bits": bits,
                    "threshold_bytes": p.parameter_bytes, "active_bits": p.count}
    raise NotImplementedError(
        f"{structure.name} carries no count partitioned to {subelement!r}, so the "
        f"array cannot be sized. Tile geometry and sparsity are also unset and both "
        f"are surface-before-touching items."
    )


def step(*args, **kwargs):
    """There is no step, and this is the point rather than an omission.

    Every edge in this section has a nonzero, finite, heterogeneous latency in real
    time, and there is no global clock in the described system to replace them
    with.  A loop with real heterogeneous delays settles by its own dynamics; the
    same loop broken by registers becomes an iterated map whose trajectory depends
    on the update rate.  Uniform delay is a substitution, not an approximation.

    Setting every latency equal and choosing an interval short enough to carry the
    finest one is a legitimate thing this rung may do - but the finest one is not
    known here.  This section records no latency at all.  The 4-12 Hz theta rhythm
    is the one time constant in the contract and it is not a candidate: it is a
    payload on one edge between the medial septum and the hippocampus, it paces the
    hippocampus and nothing else, and adopting it would be inventing exactly the
    clock the invariant forbids.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose; "
        "every edge latency here reads 'to derive', and the theta rhythm in the "
        "contract is one edge's payload rather than an update rate"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set.

    On the visual line this still left a coherent module: thresholds are read-only
    construction constants and the pathway runs open-loop.  Here it does not leave
    the section coherent, because one of these four structures exists to carry the
    teaching signal that would drive the rule.  The module remains honest and what
    it is honest about has changed.
    """
    raise NotImplementedError("no learning rule is set")


# --------------------------------------------------------------------------
# Derived sizing - an independent recomputation, not a transcription.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    lines, total, unstated = [], 0, []
    lines.append(f"{'structure / population':46} {'basis':16} {'neurons':>11} {'bits':>5} {'store':>12}")
    for s in STRUCTURES:
        for p in s.populations:
            bits = p.threshold_bits
            b = p.parameter_bytes
            count = f"{p.count:,}" if p.count is not None else "to derive"
            bs = "-" if bits is None else str(bits)
            if b is None:
                store = "to derive"
                unstated.append(f"{s.name} / {p.name}")
            else:
                store = f"{b/1e6:.3f} MB"
                total += b
            lines.append(f"{s.name + ' / ' + p.name:46} {p.basis:16} {count:>11} {bs:>5} {store:>12}")
    lines.append("")
    lines.append(f"stated total: {total/1e6:.2f} MB   (mixed basis, every width at the 16-bit ceiling)")
    lines.append(f"unstated, so the total is a floor: {len(unstated)}")
    for u in unstated:
        lines.append(f"    {u}")
    return "\n".join(lines)


def raphe_cross_check() -> str:
    """Two independently recorded statements about one quantity, diffed.

    The dorsal raphe's serotonergic population is recorded at ~165,000, and
    separately as about a third of the brain's serotonergic neurons; the whole
    serotonergic system is recorded as order 1e5-1e6.  Multiplying the first by
    three should land inside the third.
    """
    dorsal_serotonergic = 165_000
    implied_total = dorsal_serotonergic * 3
    inside = 1e5 <= implied_total <= 1e6
    store = implied_total * 16 / 8
    return (f"  dorsal raphe serotonergic {dorsal_serotonergic:,} as ~1/3 of the system "
            f"-> {implied_total:,}\n"
            f"  stated order for the whole serotonergic system: 1e5 to 1e6 -> "
            f"{'closes' if inside else 'DOES NOT CLOSE'}\n"
            f"  whole serotonergic system at the 16-bit ceiling: {store/1e6:.2f} MB")


def payload_gap_report() -> str:
    """The operations the contract names and the model has no term for."""
    gaps = (
        ("multiplicative gain", "locus coeruleus -> everywhere", apply_gain),
        ("plasticity signal", "ventral tegmental area -> striatal projection neurons",
         apply_plasticity_signal),
        ("volume transmission", "medial septum, cholinergic -> hippocampus", deliver_by_volume),
        ("phase reference", "medial septum, parvalbumin -> hippocampal interneurons",
         phase_reference),
    )
    out = []
    for label, edge, fn in gaps:
        try:
            fn()
        except NotImplementedError as exc:
            out.append(f"  {label:22} on {edge}\n      {exc}")
    return "\n".join(out)


def edge_report() -> str:
    incoming = [e for e in EDGES if e.target in {s.name for s in STRUCTURES}]
    outgoing = [e for e in EDGES if e.source in {s.name for s in STRUCTURES}]
    internal = [e for e in EDGES
                if e.source in {s.name for s in STRUCTURES}
                and e.target in {s.name for s in STRUCTURES}]
    classes = [e for e in EDGES if e.endpoint_is_class]
    volume = [e for e in EDGES if e.edge_class == VOLUME]
    timed = [e for e in EDGES if e.latency_s is not None]
    return (f"  edges: {len(EDGES)}   in: {len(incoming)}   out: {len(outgoing)}   "
            f"both ends inside this section: {len(internal)}\n"
            f"  endpoints naming a class rather than a structure: {len(classes)}\n"
            f"  edges that are not conduction plus synapse: {len(volume)} "
            f"(volume transmission)\n"
            f"  edges with a stated latency: {len(timed)}   to derive: "
            f"{len(EDGES) - len(timed)}")


if __name__ == "__main__":
    print(sizing_report())
    print()
    print("cross-check against the biology's own second statement of one count:")
    print(raphe_cross_check())
    print()
    print("edges:")
    print(edge_report())
    print()
    print("payloads with no operation in the model:")
    print(payload_gap_report())
    print()
    print("blocked on decisions above or beside this rung:")
    for fn, label in ((fan_in_map, "connectivity"), (step, "scheduler"), (learn, "learning")):
        try:
            fn(VENTRAL_TEGMENTAL_AREA) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"  {label:14} blocked: {exc}")
    for structure, sub in ((VENTRAL_TEGMENTAL_AREA, "dopaminergic"),
                           (BASAL_FOREBRAIN, "parvalbumin GABAergic"),
                           (RAPHE, "median raphe")):
        try:
            got = allocate(structure, sub)
            print(f"  {'allocation':14} {structure.name} / {sub}: {got}")
        except NotImplementedError as exc:
            print(f"  {'allocation':14} blocked: {exc}")
