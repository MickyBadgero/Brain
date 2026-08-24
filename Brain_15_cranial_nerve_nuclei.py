"""Brain — cranial-nerve nuclei and finer brainstem detail.

Structures, edges and the threshold-gate forward operation for the ocular motor
nuclei, the branchiomotor and visceromotor pools, the trigeminal sensory complex,
and the pretectum with the gaze-integrator cell groups.  Each neuron is a
threshold gate over equal-weight inputs: it fires when the count of active inputs
crosses a stored threshold, so the only value held per neuron is that threshold,
at log2(fan-in) bits.  No weights, no multiply, no gradient.

This is the section where the map exits the nervous system.  Six endpoints are
peripheral - extraocular and orofacial striated muscle, the ciliary ganglion, the
cranial parasympathetic ganglia, the trigeminal ganglion, and the jaw-muscle
spindles and periodontal receptors - and each is a terminus rather than an owed
edge.  That is different from an endocrine terminal, which has no target region at
all: a motor terminus has a definite named target that is simply outside the scope
boundary, so a later rung has a well-defined interface to supply rather than
nothing to deliver to.

One described computation is implementable today, and it is the first on this
ladder.  The olivary pretectal nucleus converges a very wide retinal field onto a
branched dendritic tree and emits a scalar - how much light.  A count of active
inputs over a large fan-in against a threshold is that computation, not an
approximation of it, and spatial_integration() below runs it.

One is not implementable and is the strongest gap in the file.  A gaze integrator
holds eye position - the time integral of a velocity command - against decay,
between saccades.  Activity here is one bit per neuron and the threshold is a
parameter nothing writes; neither is a value stored and read back.  This is the
first structure in the map whose declared function is to store something.

All four entries are bundles, the highest rate anywhere in the map, and none is
split here: splitting invents the arity.  Counting basis is per side throughout,
except the spinal accessory nucleus, which is upper cervical cord and is gathered
here for its nerve.

Every edge latency is unstated in the biology and reads None.  Two edges carry a
timing requirement with no number: the vestibulo-ocular reflex is the fastest
gaze-stabilising reflex, and the jaw-jerk is monosynaptic.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2

# --------------------------------------------------------------------------
# Element classes.  The third is the mesencephalic nucleus's problem: its cells
# are primary sensory neurons with somata inside the central nervous system, the
# only ones in the body, so they transduce - and they also project monosynaptically,
# which the retina's photoreceptors do not.  The vocabulary assigns the cell to one
# class while its edges require another.
# --------------------------------------------------------------------------

THRESHOLD_GATE = "threshold_gate"
TRANSDUCER = "transducer"                       # stores no threshold; log2 cost does not apply
TRANSDUCER_PROJECTING = "transducer_projecting"  # transduces AND projects: no class fits

# --------------------------------------------------------------------------
# Endpoint classes.
# --------------------------------------------------------------------------

CENTRAL = "central"                      # a region with an entry somewhere in the map
MOTOR_TERMINUS = "motor_terminus"        # striated muscle: named target, outside scope by rule
AUTONOMIC_TERMINUS = "autonomic_terminus"  # peripheral ganglion and end organ
SENSORY_SOURCE = "peripheral_sensory_source"  # ganglion or receptor feeding in from outside
OWN_DENDRITE = "own_dendrite"            # not an edge: the cell is its own receptor

# --------------------------------------------------------------------------
# Count states.  File 14 needed two - uncounted, and borderless where a count may
# not be well posed.  This section needs a third, because every structure here has
# a border and two have a named route to a figure.
# --------------------------------------------------------------------------

COUNTED = "counted"
COUNTABLE_UNCOUNTED = "countable, not yet counted"   # border exists; the figure has not been looked up
SOFT_ORDER_ONLY = "soft: order of magnitude only"

PER_SIDE = "per side"


@dataclass(frozen=True)
class Population:
    name: str
    kind: str
    basis: str
    count: int | None
    count_state: str
    fan_in: int | None
    fan_in_bound: int = 16
    order_of_magnitude: str = ""
    note: str = ""

    @property
    def threshold_bits(self) -> int | None:
        if self.kind in (TRANSDUCER, TRANSDUCER_PROJECTING):
            return 0          # a transducer stores no threshold
        if self.fan_in is None:
            return self.fan_in_bound
        if self.fan_in <= 1:
            return 0
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
    bundle: bool = True          # all four entries in this section are bundles
    note: str = ""

    @property
    def parameter_bytes(self) -> int | None:
        total = 0
        for p in self.populations:
            b = p.parameter_bytes
            if b is None:
                return None
            total += b
        return total


OCULAR_MOTOR = Structure(
    "ocular motor nuclei",
    (Population("oculomotor nucleus (cranial nerve III)", THRESHOLD_GATE, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, order_of_magnitude="1e3-1e4"),
     Population("trochlear nucleus (cranial nerve IV)", THRESHOLD_GATE, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, order_of_magnitude="1e3-1e4"),
     Population("abducens nucleus (cranial nerve VI)", THRESHOLD_GATE, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, order_of_magnitude="1e3-1e4"),
     Population("Edinger-Westphal nucleus", THRESHOLD_GATE, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, order_of_magnitude="1e3-1e4",
                note="visceral partner; the light reflex targets a distinct pupillary "
                     "subpopulation, not the lens-accommodation cells sharing the nucleus")),
    note=("gathered by shared function, not neighbourhood: the oculomotor nucleus and the "
          "Edinger-Westphal are contiguous, but the trochlear and abducens sit at different "
          "brainstem levels. Inputs segregate by axis - horizontal to abducens, vertical to "
          "oculomotor and trochlear."),
)

BRANCHIOMOTOR_VISCEROMOTOR = Structure(
    "branchiomotor and visceromotor nuclei",
    (Population("facial nucleus (cranial nerve VII)", THRESHOLD_GATE, PER_SIDE, 10_000,
                COUNTED, None,
                note="the one firm human count in the section, corroborated by the matching "
                     "myelinated-axon count of the facial nerve"),
     Population("trigeminal motor nucleus (cranial nerve V)", THRESHOLD_GATE, PER_SIDE, None,
                COUNTABLE_UNCOUNTED, None, order_of_magnitude="1e3-1e4"),
     Population("hypoglossal nucleus (cranial nerve XII)", THRESHOLD_GATE, PER_SIDE, None,
                COUNTABLE_UNCOUNTED, None, order_of_magnitude="1e3-1e4"),
     Population("nucleus ambiguus (cranial nerves IX, X, XI)", THRESHOLD_GATE, PER_SIDE, None,
                COUNTABLE_UNCOUNTED, None),
     Population("superior salivatory nucleus (cranial nerve VII)", THRESHOLD_GATE, PER_SIDE,
                None, COUNTABLE_UNCOUNTED, None),
     Population("inferior salivatory nucleus (cranial nerve IX)", THRESHOLD_GATE, PER_SIDE,
                None, COUNTABLE_UNCOUNTED, None),
     Population("dorsal motor nucleus of the vagus (cranial nerve X)", THRESHOLD_GATE, PER_SIDE,
                None, COUNTABLE_UNCOUNTED, None,
                note="the largest parasympathetic preganglionic source of the lower brainstem"),
     Population("spinal accessory nucleus (cranial nerve XI)", THRESHOLD_GATE, "upper cervical cord",
                None, COUNTABLE_UNCOUNTED, None,
                note="technically cord; gathered here for the nerve, so it breaks the "
                     "section's per-side basis")),
    note=("eight pools from pons to upper cervical cord, sharing only the property of being "
          "cranial motor pools. Every one can in principle be cross-checked against the "
          "myelinated-axon count of its own nerve, which is how the facial figure was "
          "corroborated - the only cross-check in the map that closes against a different "
          "measurement rather than a second statement of the same one."),
)

TRIGEMINAL_SENSORY = Structure(
    "trigeminal sensory complex",
    (Population("mesencephalic nucleus", TRANSDUCER_PROJECTING, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, order_of_magnitude="1e3",
                note="primary sensory neurons with somata inside the central nervous system, "
                     "the only ones in the body; they transduce and also project monosynaptically"),
     Population("principal (pontine) nucleus", THRESHOLD_GATE, PER_SIDE, None,
                COUNTABLE_UNCOUNTED, None, note="discriminative touch"),
     Population("spinal trigeminal nucleus", THRESHOLD_GATE, PER_SIDE, None,
                COUNTABLE_UNCOUNTED, None,
                note="pain and temperature; subdivides into pars oralis, interpolaris and "
                     "caudalis, with pars caudalis continuous with the spinal dorsal horn")),
    note=("submodality is separated before the first synapse and maintained through the relay: "
          "the cranial mirror of the dorsal-column / anterolateral split, in different tissue "
          "and on a different nerve."),
)

PRETECTUM_AND_INTEGRATORS = Structure(
    "pretectum and gaze-integrator cell groups",
    (Population("olivary pretectal nucleus", THRESHOLD_GATE, PER_SIDE, None,
                COUNTABLE_UNCOUNTED, None,
                note="definite borders in macaque, projection cells already retrogradely "
                     "labelled, no human figure looked up in this pass - the most countable "
                     "structure left in the section"),
     Population("nucleus prepositus hypoglossi", THRESHOLD_GATE, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, note="horizontal gaze integrator"),
     Population("interstitial nucleus of Cajal", THRESHOLD_GATE, PER_SIDE, None,
                SOFT_ORDER_ONLY, None, note="vertical gaze integrator")),
    note=("two structures that share no edge with each other, gathered by anatomical "
          "neighbourhood rather than data flow. Inside the olivary pretectal nucleus the "
          "projecting somata sit at the periphery with dendrites branching into a core where "
          "retinal terminals concentrate, so the place a cell's body sits and the place it "
          "receives are different - and no second internal edge is written for it, because "
          "there is no second synapse."),
)

STRUCTURES = (OCULAR_MOTOR, BRANCHIOMOTOR_VISCEROMOTOR, TRIGEMINAL_SENSORY,
              PRETECTUM_AND_INTEGRATORS)

# --------------------------------------------------------------------------
# Edges.  One record per source bullet.  `is_edge=False` marks a bullet that
# occupies an edge line and records the ABSENCE of an edge - the same shape as
# file 14's parabrachial collateral bullet, and the reason a bullet count and an
# edge count differ by one here.
# --------------------------------------------------------------------------


@dataclass(frozen=True)
class Edge:
    source: str
    target: str
    listed_under: str                  # 'in', 'out' or 'internal'
    source_sub: str | None = None
    target_sub: str | None = None
    latency_s: float | None = None     # None = to derive
    endpoint_class: str = CENTRAL
    endpoint_is_class: bool = False
    is_edge: bool = True
    names_multiple: int = 1
    far_end_file: int | None = None
    carries: str = ""


EDGES: tuple[Edge, ...] = (
    # ---- ocular motor nuclei: in (5 bullets, 4 of them edges) ----
    Edge("brainstem saccade burst generators", "ocular motor nuclei", "in", None,
         "abducens (horizontal); oculomotor and trochlear (vertical)", None, CENTRAL, True,
         True, 2, 14,
         "a timed burst driving eye muscles, in temporal (rate) code - the output side of the "
         "superior colliculus's spatial-to-temporal conversion"),
    Edge("gaze neural integrators", "ocular motor nuclei", "in", None, None, None, CENTRAL,
         False, True, 2, 15,
         "an eye POSITION command: the time integral of the velocity command, which holds the "
         "eye still between saccades"),
    Edge("vestibular nuclei", "ocular motor nuclei", "in", None, None, None, CENTRAL, False,
         True, 1, 3,
         "the vestibulo-ocular reflex command, via the medial longitudinal fasciculus; "
         "an eye-velocity signal equal and opposite to head rotation. THE FASTEST "
         "gaze-stabilising reflex - a timing requirement with no number"),
    Edge("superior colliculus and frontal eye fields", "ocular motor nuclei", "in", None, None,
         None, CENTRAL, False, False, 2, 14,
         "NOT AN EDGE: recorded absence. The saccade goal reaches this nucleus only THROUGH "
         "the burst generators, not monosynaptically"),
    Edge("pretectum", "ocular motor nuclei", "in", "olivary pretectal nucleus",
         "Edinger-Westphal nucleus", None, CENTRAL, False, True, 1, 15,
         "the pupillary light reflex drive: a luminance scalar as a drive to constrict, "
         "monosynaptic, excitatory and bilateral"),

    # ---- ocular motor nuclei: out (2) ----
    Edge("ocular motor nuclei", "extraocular muscles and levator palpebrae", "out", None, None,
         None, MOTOR_TERMINUS, False, True, 1, None,
         "the motor command to the eye muscles - the terminus of the oculomotor loop"),
    Edge("ocular motor nuclei", "ciliary ganglion", "out", "Edinger-Westphal nucleus", None,
         None, AUTONOMIC_TERMINUS, False, True, 1, None,
         "the parasympathetic preganglionic command for pupil constriction and lens accommodation"),

    # ---- ocular motor nuclei: internal (1) ----
    Edge("ocular motor nuclei", "ocular motor nuclei", "internal",
         "abducens internuclear neurons", "contralateral oculomotor medial-rectus pool", None,
         CENTRAL, False, True, 1, 18,
         "the YOKING signal: a copy of the abducens's own lateral-rectus drive, carrying no "
         "independent command. The only midline crossing in the section"),

    # ---- branchiomotor and visceromotor: in (4) ----
    Edge("cerebral cortex", "branchiomotor and visceromotor nuclei", "in", None, "facial pool",
         None, CENTRAL, True, True, 1, 18,
         "the voluntary motor command via the corticobulbar tract. Upper-face motoneurons get "
         "BILATERAL input, lower-face CONTRALATERAL only - a fan-in fact on a payload line. "
         "The corticobulbar tract has no entry anywhere"),
    Edge("nucleus of the solitary tract", "branchiomotor and visceromotor nuclei", "in", None,
         "dorsal motor nucleus of the vagus", None, CENTRAL, False, True, 1, 14,
         "the afferent limb of vagal reflexes; payload otherwise owed"),
    Edge("spinal trigeminal nucleus", "branchiomotor and visceromotor nuclei", "in", None, None,
         None, CENTRAL, False, True, 1, 15,
         "the afferent limb of the corneal and jaw reflexes; payload owed"),
    Edge("reticular premotor pattern generators", "branchiomotor and visceromotor nuclei", "in",
         None, "the rhythmic pools", None, CENTRAL, False, True, 1, 14,
         "the rhythmic motor pattern sequencing chewing, swallowing, respiration and "
         "vocalisation; payload owed"),

    # ---- branchiomotor and visceromotor: out (2) ----
    Edge("branchiomotor and visceromotor nuclei", "orofacial striated muscle", "out", None,
         None, None, MOTOR_TERMINUS, False, True, 1, None,
         "the final common path for chewing, facial expression, swallowing, phonation and "
         "speech articulation"),
    Edge("branchiomotor and visceromotor nuclei", "cranial parasympathetic ganglia", "out",
         "dorsal motor vagus, nucleus ambiguus, salivatory nuclei", None, None,
         AUTONOMIC_TERMINUS, False, True, 3, None,
         "the cranial (vagal) parasympathetic outflow; the cardioinhibitory limb closes the "
         "baroreflex loop across this entry"),

    # ---- trigeminal sensory complex: in (2) ----
    Edge("trigeminal ganglion", "trigeminal sensory complex", "in", None,
         "principal (touch) and spinal (pain/temperature)", None, SENSORY_SOURCE, False, True,
         1, None,
         "face somatosensation split by submodality AT THE POINT OF ENTRY - the cranial mirror "
         "of the dorsal-column / anterolateral separation"),
    Edge("jaw-muscle spindles and periodontal receptors", "trigeminal sensory complex", "in",
         None, "mesencephalic nucleus", None, OWN_DENDRITE, False, True, 2, None,
         "NOT A SYNAPTIC INPUT: the mesencephalic cells ARE the primary sensory neurons, so "
         "the 'input' is the cell's own dendrite and there is no producer region"),

    # ---- trigeminal sensory complex: out (3) ----
    Edge("trigeminal sensory complex", "ventral posteromedial thalamus", "out",
         "principal and spinal nuclei", None, None, CENTRAL, False, True, 1, 12,
         "face somatosensation onward to the primary somatosensory cortex, the two "
         "submodalities kept separate. Two-ended for pain/temperature; owed for touch"),
    Edge("trigeminal sensory complex", "branchiomotor and visceromotor nuclei", "out",
         "mesencephalic nucleus", "trigeminal motor nucleus", None, CENTRAL, False, True, 1, 15,
         "the JAW-JERK: monosynaptic proprioceptive reflex - a latency claim expressed as anatomy"),
    Edge("trigeminal sensory complex", "branchiomotor and visceromotor nuclei", "out",
         "spinal nucleus", "the branchiomotor pools", None, CENTRAL, False, True, 1, 15,
         "the afferent limb of the corneal blink and jaw-opening reflexes; payload owed"),

    # ---- pretectum and gaze integrators: in (2) ----
    Edge("retina", "pretectum and gaze-integrator cell groups", "in",
         "melanopsin broad-field ganglion cells", "olivary pretectal nucleus", None, CENTRAL,
         False, True, 1, 1,
         "ambient luminance as a scalar. Does NOT carry hue, form, motion or a usable eye of "
         "origin. Fan-in high by construction - the substrate for ~31 degree receptive fields"),
    Edge("superior colliculus, frontal eye fields, vestibular nuclei and cerebellum",
         "pretectum and gaze-integrator cell groups", "in", None,
         "integrators and burst generators", None, CENTRAL, False, True, 4, None,
         "payload owed; eye-movement commands and head-velocity signals requiring the position hold"),

    # ---- pretectum and gaze integrators: out (3) ----
    Edge("pretectum and gaze-integrator cell groups", "ocular motor nuclei", "out",
         "olivary pretectal nucleus", "Edinger-Westphal, preganglionic, bilaterally", None,
         CENTRAL, False, True, 1, 15,
         "the luminance scalar as a drive to constrict, onto a DISTINCT pupillary "
         "subpopulation. Bilaterality here is where the consensual response comes from, and "
         "in macaque it comes from this projection rather than a commissure"),
    Edge("pretectum and gaze-integrator cell groups",
         "superior colliculus, periaqueductal grey, interstitial nucleus of Cajal, and the "
         "ventral lateral geniculate / intergeniculate leaflet", "out",
         "olivary pretectal nucleus", None, None, CENTRAL, False, True, 4, 14,
         "payload owed. Recorded because the entry previously declared ONE output and tracing "
         "shows several: the luminance signal reaches the orienting and circadian machinery "
         "as well as the pupil. Rat tracing, no macaque confirmation read"),
    Edge("pretectum and gaze-integrator cell groups", "ocular motor nuclei", "out",
         "prepositus hypoglossi, interstitial nucleus of Cajal, burst generators", None, None,
         CENTRAL, False, True, 1, 15,
         "an eye POSITION command: the time integral of the velocity command. The tract this "
         "rides is not stated at either end - owed at both"),
)

SOURCE_HEADER = {"in": 13, "out": 10, "internal": 1, "total": 24}

# --------------------------------------------------------------------------
# Forward operation.
# --------------------------------------------------------------------------


def threshold_gate(active_counts, thresholds):
    """Fire where the count of active inputs reaches the stored threshold."""
    if len(active_counts) != len(thresholds):
        raise ValueError("one threshold per neuron")
    return [c >= t for c, t in zip(active_counts, thresholds)]


def spatial_integration(retinal_activity, threshold):
    """The olivary pretectal nucleus's luminance computation, run as written.

    A wide field of retinal lines converges on one cell; the cell reports whether
    the count of active ones crosses its threshold.  Spatial resolution is
    discarded and a scalar - how much light - is what leaves.  This is the
    contract's operation unmodified, not an approximation of it, and it is the
    first described computation on this ladder that the sizing model expresses
    without extension.

    The ~31 degree mean receptive field the source reports is a statement about
    the size of fan_in.  The actual fan-in and the actual threshold are unknown,
    so a caller supplies them and the result is illustrative: what is being
    demonstrated is the operation, not the parameters.
    """
    count = sum(1 for a in retinal_activity if a)
    return count >= threshold, count


def graded_luminance(retinal_activity, thresholds):
    """The same convergence read by a bank of cells with different thresholds.

    A single threshold gate reports one bit.  A population of them over the same
    wide field, with thresholds spread across the range, reports a monotone code
    for how much light there is - which is what a scalar payload on a wire made of
    spiking lines has to look like.  Nothing here is added to the model: it is the
    same count compared against several stored thresholds, which is what having
    more than one neuron already means.
    """
    count = sum(1 for a in retinal_activity if a)
    return [count >= t for t in thresholds], count


# --------------------------------------------------------------------------
# What the model cannot express.
# --------------------------------------------------------------------------


def hold_value(*args, **kwargs):
    """Hold eye position against decay between saccades.

    Not implementable.  A gaze integrator's whole function is to store a
    continuously-valued quantity - the time integral of a velocity command - and
    read it back.  Activity here is one bit per neuron; the threshold is a
    parameter nothing writes.  Neither is a value stored and read back, so this is
    the first structure in the map whose declared function has no home in the
    representation at all.  The source records the internal mechanism as unknown
    and names it as work for a lower rung.

    A CANDIDATE, offered to be checked and not asserted: recurrence plus delay
    plus a sign gives an oscillator at one parity and a latch at the other, so
    this and file 14's intrinsic pacemaker may want one addition to the model
    rather than two - and it is the inverting term the sign gap has been asking
    for since the outer retina.  What would test it is whether a held eye position
    degrades gracefully or not at all, which the source does not say.
    """
    raise NotImplementedError(
        "no representation here holds a value that persists and is read back; and "
        "adding one is a decision about what a structure stores, which may belong on "
        "the surface-before-touching list and is not taken here"
    )


def weight_inhibition(*args, **kwargs):
    """Record that one population receives more inhibitory input than its neighbour.

    Not implementable.  The source carries a quantitative asymmetry: pupillary
    motoneurons receive more inhibitory input than the lens-accommodation
    motoneurons beside them in the same nucleus.  A count of active inputs has no
    inhibitory term, so it cannot record more or less of one.  Same gap as
    everywhere, arriving as a comparison rather than as an edge.
    """
    raise NotImplementedError(
        "a count of active inputs has no inhibitory term to be more or less of"
    )


def fan_in_map(structure: Structure, subelement: str | None = None):
    """Which source lines converge on each neuron.

    Not implementable: every fan-in on all twenty-four edges reads unknown.  One
    is qualified - the retinal input to the olivary pretectal nucleus is high by
    construction - which is a direction, not a number.
    """
    raise NotImplementedError("connection topology is not set, and no fan-in is stated")


def allocate(structure: Structure, population_name: str):
    """Size the threshold and activity arrays for one population."""
    for p in structure.populations:
        if p.name == population_name:
            if p.count is None:
                extra = (" - the border exists and the figure has simply not been looked up"
                         if p.count_state == COUNTABLE_UNCOUNTED else
                         f" - order of magnitude only ({p.order_of_magnitude})"
                         if p.order_of_magnitude else "")
                raise NotImplementedError(
                    f"{structure.name} / {population_name}: no count{extra}")
            return {"neurons": p.count, "threshold_bits": p.threshold_bits,
                    "threshold_bytes": p.parameter_bytes, "active_bits": p.count}
    raise ValueError(f"{population_name!r} is not a population of {structure.name}")


def step(*args, **kwargs):
    """There is no step.

    Every latency reads to derive and the scheduling discipline is not set.  This
    section names the tightest timing constraint in the map - the vestibulo-ocular
    reflex is the fastest gaze-stabilising reflex, and its loop delay must beat the
    head movement it corrects - and supplies no time.  The jaw-jerk's monosynaptic
    arc sets a floor as anatomy rather than as a figure.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set; this section states two timing "
        "requirements and no times"
    )


def learn(*args, **kwargs):
    """Nothing writes a threshold, because no learning rule is set."""
    raise NotImplementedError("no learning rule is set")


# --------------------------------------------------------------------------
# Reports.
# --------------------------------------------------------------------------


def sizing_report() -> str:
    lines = [f"{'structure / population':62} {'neurons':>9} {'bits':>5} {'store':>11}  state"]
    total, sized = 0, 0
    states: dict[str, int] = {}
    for s in STRUCTURES:
        for p in s.populations:
            b = p.parameter_bytes
            states[p.count_state] = states.get(p.count_state, 0) + 1
            count = f"{p.count:,}" if p.count is not None else "-"
            bits = "-" if p.threshold_bits is None else str(p.threshold_bits)
            if b is None:
                store = "to derive"
            else:
                store = f"{b/1e6:.3f} MB"
                total += b
                sized += 1
            lines.append(f"{s.name + ' / ' + p.name:62} {count:>9} {bits:>5} {store:>11}  "
                         f"{p.count_state}")
    lines.append("")
    lines.append(f"populations with a derivable store: {sized} of "
                 f"{sum(len(s.populations) for s in STRUCTURES)}")
    lines.append(f"stated total: {total/1e6:.3f} MB per side")
    for k, v in sorted(states.items()):
        lines.append(f"    {k:34} {v}")
    lines.append("Every structure here has a border, so no count is 'borderless' as three were")
    lines.append("in file 14. Two have a named route to a figure, which makes this the one")
    lines.append("section whose sizing gap has a method for closing it.")
    return "\n".join(lines)


def edge_count_check() -> str:
    """Bullets against edges, because one bullet here records the ABSENCE of an edge."""
    counts = {"in": 0, "out": 0, "internal": 0}
    edges_only = {"in": 0, "out": 0, "internal": 0}
    for e in EDGES:
        counts[e.listed_under] += 1
        if e.is_edge:
            edges_only[e.listed_under] += 1
    non_edges = [e for e in EDGES if not e.is_edge]
    out = [
        f"  source file header:  {SOURCE_HEADER['in']} in, {SOURCE_HEADER['out']} out, "
        f"{SOURCE_HEADER['internal']} internal, {SOURCE_HEADER['total']} total",
        f"  this module, bullets:{counts['in']:3} in, {counts['out']} out, "
        f"{counts['internal']} internal, {sum(counts.values())} total",
        f"  this module, edges:  {edges_only['in']:3} in, {edges_only['out']} out, "
        f"{edges_only['internal']} internal, {sum(edges_only.values())} total",
        "",
    ]
    if counts == {k: SOURCE_HEADER[k] for k in counts}:
        out.append("  Bullet counts agree with the source header.")
    else:
        out.append("  BULLET COUNTS DISAGREE with the source header; do not smooth this over.")
    out.append(f"  Bullets that are not edges: {len(non_edges)}")
    for e in non_edges:
        out.append(f"    {e.source} -> {e.target}: {e.carries.split('.')[0]}")
    out.append("  File 14's parabrachial collateral bullet has the same shape. Two files running,")
    out.append("  two Inputs-list bullets that are not edges, and a count that does not know the")
    out.append("  difference drifts by one each time.")
    return "\n".join(out)


def endpoint_report() -> str:
    by_class: dict[str, int] = {}
    for e in EDGES:
        by_class[e.endpoint_class] = by_class.get(e.endpoint_class, 0) + 1
    lines = [f"  {k:28} {v}" for k, v in sorted(by_class.items())]
    peripheral = [e for e in EDGES if e.endpoint_class in
                  (MOTOR_TERMINUS, AUTONOMIC_TERMINUS, SENSORY_SOURCE, OWN_DENDRITE)]
    timed = [e for e in EDGES if e.latency_s is not None]
    lines.append(f"  {'peripheral in total':28} {len(peripheral)}")
    lines.append(f"  {'latency stated':28} {len(timed)}   to derive: {len(EDGES) - len(timed)}")
    lines.append("  A motor terminus has a definite named target outside the scope boundary;")
    lines.append("  file 14's endocrine terminal had no target region at all. Different builds.")
    return "\n".join(lines)


def spatial_integration_demo() -> str:
    """Run the one described computation this section can implement.

    Illustrative fan-in and thresholds: neither is stated in the biology.  What is
    being demonstrated is that the contract's forward operation produces the
    contract's payload - a wide field in, a scalar out - with nothing added.
    """
    fan_in = 500
    lines = ["  a wide retinal field converging on one nucleus (illustrative fan-in = 500):"]
    for lit in (10, 100, 250, 400, 490):
        activity = [True] * lit + [False] * (fan_in - lit)
        bits, count = graded_luminance(activity, thresholds=[50, 150, 300, 450])
        code = "".join("1" if b else "0" for b in bits)
        lines.append(f"    {lit:3} of {fan_in} lines active -> count {count:3} -> "
                     f"population code {code}")
    lines.append("  Spatial resolution is discarded and a monotone scalar leaves. This is the")
    lines.append("  operation the contract already specifies, not an extension of it.")
    return "\n".join(lines)


if __name__ == "__main__":
    print(sizing_report())
    print()
    print("edge count, checked against the source header:")
    print(edge_count_check())
    print()
    print("endpoints by class:")
    print(endpoint_report())
    print()
    print("the one computation this section can run:")
    print(spatial_integration_demo())
    print()
    print("what the model cannot express:")
    for fn, label in ((hold_value, "hold a value"), (weight_inhibition, "weigh inhibition")):
        try:
            fn()
        except NotImplementedError as exc:
            print(f"  {label:18} {exc}")
    print()
    print("blocked:")
    for fn, label in ((fan_in_map, "connectivity"), (step, "scheduler"), (learn, "learning")):
        try:
            fn(OCULAR_MOTOR) if fn is fan_in_map else fn()
        except NotImplementedError as exc:
            print(f"  {label:14} {exc}")
    for structure, pop in ((BRANCHIOMOTOR_VISCEROMOTOR, "facial nucleus (cranial nerve VII)"),
                           (BRANCHIOMOTOR_VISCEROMOTOR, "hypoglossal nucleus (cranial nerve XII)"),
                           (PRETECTUM_AND_INTEGRATORS, "nucleus prepositus hypoglossi")):
        try:
            print(f"  {'allocation':14} {pop}: {allocate(structure, pop)}")
        except NotImplementedError as exc:
            print(f"  {'allocation':14} {exc}")
