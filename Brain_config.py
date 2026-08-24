"""Brain — declarations shared by every numbered module.

This file carries no history: no versions, no provenance, no "changed since", no
reference to prior files, no changelog, no commented-out prior version.

What lives here is the vocabulary, not the content.  An edge that leaves section nn
is declared at both ends, in two files, and two files cannot describe one edge in
agreement when the type describing it is defined twice.  So the types are defined
once, here, and the counts, shapes and extents of any structure stay in the numbered
module for the section that describes them, beside the entry they were derived from.

Two things this file deliberately does not provide.

There is no forward operation.  Whether a unit emits a graded value or a binary one
is not settled, and a comparator written here would settle it by assertion.  The
sizing model charges each neuron log2(fan-in) bits, which is what a threshold over
equal-weight inputs would store, and the bit width is therefore usable while the
arithmetic that consumes it is not.

There is no scheduler, no loop, no step counter and no notion of a tick.  Every edge
carries a nonzero, finite, heterogeneous latency in real time, and those delays are
what make a re-entrant loop well defined: a loop with real heterogeneous delays
settles by its own dynamics, while the same loop broken by registers becomes an
iterated map whose trajectory depends on the update rate.  Those are two different
systems computing two different things.  Latency is seconds, never steps.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from math import ceil, log2

# --------------------------------------------------------------------------
# Element classes.
#
# Four kinds of element appear across the sections and only the first has a
# specified computation.  Charging a threshold to any of the other three asserts
# a mechanism it does not have.
# --------------------------------------------------------------------------

THRESHOLD_GATE = "threshold_gate"
"""Spikes.  Stores a threshold at log2(fan-in) bits, bounded at the 16-bit ceiling
where the fan-in itself is underived."""

TRANSDUCER = "transducer"
"""Converts a physical stimulus.  Not a threshold gate, stores no threshold, and the
log2 cost does not apply.  Its input edge is not a projection, so fan-in is not
applicable rather than underived."""

GRADED = "graded"
"""Computes, is not a transducer, and does not cross a threshold: responds with
graded membrane potential and generates no action potential, or releases transmitter
from dendrites without one.  What such an element stores is not settled by the
threshold-gate model.  It is neither zero, which would assert it holds nothing, nor
log2(fan-in), which would assert a threshold it does not have."""

TRANSMISSION = "transmission"
"""Carries other structures' edges and computes nothing.  No synapse occurs, so
fan-in and fan-out are none rather than underived, parameter memory is zero, and the
shape is a routing index rather than an activity array.  Load-bearing anyway: a tract
is where the physical substrate of a latency lives."""

# --------------------------------------------------------------------------
# The states a quantity can be in.
#
# These are distinct and actionable and must not collapse into one another.
# Writing TO_DERIVE over NOT_APPLICABLE asserts something is there to derive; over
# RESISTED it discards a finding; over CONTESTED it asserts nobody has looked when
# the problem is that several people have and disagree.
# --------------------------------------------------------------------------

TO_DERIVE = "to derive"          # the rung above has not supplied it
NOT_APPLICABLE = "not applicable"  # the property does not exist here
UNKNOWN = "unknown"              # it exists and has not been measured
OWED = "owed"                    # described but not yet typed
RESISTED = "resisted"            # decoded, and yielding no shared format
CONTESTED = "contested"          # measured, and yielding readings that disagree

OPEN_STATES = (TO_DERIVE, NOT_APPLICABLE, UNKNOWN, OWED, RESISTED, CONTESTED)

# --------------------------------------------------------------------------
# Counting basis.  Not uniform within a section, let alone across them, so it is
# carried on the population rather than assumed.
# --------------------------------------------------------------------------

PER_EYE = "per eye"
BOTH_EYES = "both eyes"
PER_EAR = "per ear"
PER_SIDE = "per side"
PER_HEMISPHERE = "per hemisphere"
WHOLE = "whole"

# --------------------------------------------------------------------------
# Endpoints.
#
# A cross-file endpoint carries the far file's stem, never its number alone.  The
# number fixes data-flow position and the section names the structure; a bare
# number goes silently wrong the moment a file is split, merged or renumbered, and
# the code has no reader to notice.
#
# An endpoint with no stem is not a claim that no far end exists.  Three distinct
# things wear that appearance and they are told apart here, because collapsing them
# loses the difference between work not yet done and a gap inherited from above.
# --------------------------------------------------------------------------

LOCAL = "local"          # the far end is a structure in this same file
CLASS_ENDPOINT = "class"  # names a class and no structure; needs splitting at the source
NO_ENTRY = "no entry"    # names a structure that has no entry in any file

PENDING = "pending"      # a structure in this same file whose entry is not yet written
"""Distinct from LOCAL, which asserts an entry exists to resolve against, and from
NO_ENTRY, which asserts none exists anywhere.  A module written while its own design
file is partial declares edges whose far end is inside it and not yet reachable, and
typing those as either of the other two states something false."""

UNSTEMMED = "unstemmed"  # a named far end whose file has not been opened beside this one
"""Not a claim that no far end exists.  The stem is written only where the far file has
been read against this one, so an endpoint without one is a reading not yet done rather
than a gap in the map.  Inventing the stem here would derive connectivity at the wrong
rung: the endpoint would resolve, and nothing would have checked that it resolves right."""

ROUTE_ENDPOINT = "route"  # names a circuit or arc rather than a structure
"""Worse than a class endpoint in one specific respect, which is why it is not folded
into it.  A class is visibly unresolved and invites splitting; a route reads as a
complete description while naming nothing that can declare an input back, so no diff at
either end can pair the edge and it reads as terminating outside scope."""


@dataclass(frozen=True)
class Endpoint:
    """One end of an edge.

    `stem` is the far file's <nn>_<section> string where the far end lives in another
    file, and empty where it is LOCAL, a CLASS_ENDPOINT, or NO_ENTRY.  `sub` names
    the sub-element the edge terminates on where the biology terminates on one:
    collapsing four geniculate edges to "-> V1" would delete a structural claim about
    where each channel arrives, and one of those four does not reach layer 4 at all.
    """

    name: str
    kind: str = LOCAL
    stem: str = ""
    sub: str | None = None

    def __post_init__(self):
        if self.kind == LOCAL and self.stem:
            raise ValueError(f"{self.name}: a local endpoint carries no stem")
        if self.stem and not self.stem[:2].isdigit():
            raise ValueError(f"{self.name}: stem {self.stem!r} must begin <nn>_")


def far(name, stem, sub=None):
    """An endpoint in another file, named by that file's stem."""
    return Endpoint(name, kind="cross", stem=stem, sub=sub)


def here(name, sub=None):
    """An endpoint in this file."""
    return Endpoint(name, kind=LOCAL, sub=sub)


def class_endpoint(name):
    """An endpoint naming a class rather than a structure.

    It cannot carry a stem until it is split, and the split is a source decision.
    """
    return Endpoint(name, kind=CLASS_ENDPOINT)


def no_entry(name):
    """A named structure with no entry in any file.  Inherited, not repairable in code."""
    return Endpoint(name, kind=NO_ENTRY)


def pending(name, sub=None):
    """A structure in this file whose entry is not yet written."""
    return Endpoint(name, kind=PENDING, sub=sub)


def unstemmed(name, sub=None):
    """A named far end whose file has not been opened beside this one."""
    return Endpoint(name, kind=UNSTEMMED, sub=sub)


def route(name):
    """An endpoint naming a circuit rather than a structure."""
    return Endpoint(name, kind=ROUTE_ENDPOINT)


# --------------------------------------------------------------------------
# Representation — declared once per line and inherited by every consumer of it.
#
# Structure-level failure is omission and a diff finds it.  Composition-level
# failure is different: every structure satisfies its own contract and the whole
# still does not run, because two neighbours read one shared line correctly and
# disagree about what its numbers mean.  Pinning units, range, timing and frame at
# the line rather than at the structure makes that a mechanical check.
#
# Update timing is the rate at which the producer emits a new value, in real time,
# where the producer has a rate of its own.  Where it does not, a structure driven
# by its inputs emits when its inputs change, and event-driven is the honest answer.
# There is no system clock to borrow a rate from.
# --------------------------------------------------------------------------

EVENT_DRIVEN = "event-driven"
NO_FRAME = "none"        # the payload has no coordinate frame: a scalar, or a category


@dataclass(frozen=True)
class Representation:
    units: str = TO_DERIVE
    value_range: str = TO_DERIVE
    update_timing: str = EVENT_DRIVEN
    frame: str = TO_DERIVE


# --------------------------------------------------------------------------
# Populations and structures.
#
# `fan_in` is the convergence onto one neuron of this population where the biology
# fixes it, and None where it does not.  A fan-in of 1 costs zero bits: a neuron with
# a single input has no count to compare a threshold against.
# --------------------------------------------------------------------------

FAN_IN_CEILING_BITS = 16
"""The log2 bound used where a fan-in is underived.  Any fan-in under ~65,000 fits."""


@dataclass(frozen=True)
class Population:
    name: str
    kind: str
    basis: str
    count: int | None = None
    fan_in: int | None = None
    fan_in_low: int | None = None     # where the literature disputes it across a range
    fan_in_high: int | None = None
    sign_inverting: bool = False      # hyperpolarisation is the excitatory response
    note: str = ""

    @property
    def threshold_bits(self) -> int | None:
        """Stored bits per neuron under the sizing model.

        None means the store is not established, which is not the same as zero.
        """
        if self.kind in (TRANSDUCER, TRANSMISSION):
            return 0
        if self.kind == GRADED:
            return None
        if self.fan_in is None:
            return FAN_IN_CEILING_BITS
        if self.fan_in <= 1:
            return 0
        return ceil(log2(self.fan_in))

    @property
    def threshold_bits_range(self) -> tuple[int, int] | None:
        """The disputed width, where the literature gives a range rather than a value."""
        if self.fan_in_low is None or self.fan_in_high is None:
            return None
        return ceil(log2(self.fan_in_low)), ceil(log2(self.fan_in_high))

    @property
    def parameter_bytes(self) -> int | None:
        bits = self.threshold_bits
        if bits is None or self.count is None:
            return None
        return self.count * bits // 8

    @property
    def realised_bytes(self) -> int | None:
        """The store as a machine integer type actually takes it.

        No integer type is 12 or 14 bits wide, so a derived width between 9 and 16
        realises at 16 unless it is bit-packed.  Bit-packing closes the gap and costs
        unpacking on every read; that is a compute-against-memory trade and it is the
        only reason this figure is carried.  It is never a reason to shrink anything:
        memory is a derived requirement, not a limit to design against.
        """
        bits = self.threshold_bits
        if bits is None or self.count is None:
            return None
        container = 0 if bits == 0 else (8 if bits <= 8 else 16)
        return self.count * container // 8


@dataclass(frozen=True)
class Structure:
    name: str
    populations: tuple[Population, ...]
    subelements: tuple[str, ...] = ()
    rank: int | None = None
    axes: tuple[str, ...] = ()
    partitions: bool = False
    """True where the neuron count partitions to the sub-elements.  Where it is
    False the entry names sub-elements the count does not divide among, and an array
    for one of them cannot be sized however well the sub-element is described."""

    @property
    def parameter_bytes(self) -> int | None:
        """None if any population's store is unstated: a partial sum reads as a total."""
        total = 0
        for p in self.populations:
            b = p.parameter_bytes
            if b is None:
                return None
            total += b
        return total


# --------------------------------------------------------------------------
# Edges.
# --------------------------------------------------------------------------

DRIVER = "driver"          # supplies the content
MODULATORY = "modulatory"  # sets whether, when and how strongly content passes; adds none
ROUTING = "routing"        # a transmission statement: no synapse at this joint


@dataclass(frozen=True)
class Edge:
    source: Endpoint
    target: Endpoint
    carries: str = TO_DERIVE
    role: str = DRIVER
    latency_s: float | None = None
    representation: Representation = field(default_factory=Representation)
    fan_out: int | None = None
    note: str = ""

    @property
    def crosses_file(self) -> bool:
        return bool(self.source.stem or self.target.stem)


def edge_storage_bytes(line_count, latency_s, update_interval_s, bytes_per_value):
    """Values in flight on one edge, which the per-edge-latency invariant creates.

    line_count * ceil(latency / update_interval) * bytes_per_value.

    The update interval waits on the scheduling discipline and the bytes per value
    wait on whether emission is graded or binary, so this returns None wherever a
    term is missing rather than substituting one.  It is never summed with parameter
    memory or with state; those are three separate quantities.
    """
    if None in (line_count, latency_s, update_interval_s, bytes_per_value):
        return None
    if update_interval_s <= 0:
        raise ValueError("an update interval of zero or less is not an interval")
    return line_count * ceil(latency_s / update_interval_s) * bytes_per_value


# --------------------------------------------------------------------------
# The unset decisions, in one place, so that a module reaches them by calling
# rather than by quietly choosing.  Each raises with what it is waiting on and who
# it belongs to.
# --------------------------------------------------------------------------


def emission(*args, **kwargs):
    """Whether a unit emits a graded value or a binary one, and how wide it is.

    Not set.  The sizing model charges log2(fan-in) bits per neuron, which is what a
    threshold over equal-weight inputs stores, and reading that as settling the
    question runs the inference backwards.  Several structures hold elements that
    cross no threshold at all: the outer retina's horizontal and bipolar cells
    respond with graded membrane potential, and the lateral geniculate interneuron
    releases transmitter from dendrites without an action potential.
    """
    raise NotImplementedError(
        "graded against binary emission is not set and is not this rung's to choose; "
        "no update equation may be written until it is"
    )


def fan_in_map(*args, **kwargs):
    """Which source lines converge on each neuron.

    Fan-in is given as a scalar per structure, mostly underived and bounded at 16
    bits, and a forward operation needs it as a map.  A convergence count is not a
    convergence pattern.  The pattern is not missing from the biology -- projections
    are described as point-to-point retinotopic, with space-variant compression -- but
    it is described in prose, and writing it means writing a receptive-field geometry
    with an eccentricity-dependent scale factor.  That is the connection topology.
    """
    raise NotImplementedError(
        "inter-structure connection topology is not set and must be surfaced before "
        "it is chosen"
    )


def allocate(*args, **kwargs):
    """Size the arrays for one sub-element.

    Blocked wherever a structure's count does not partition to its sub-elements, and
    blocked everywhere by tile geometry and sparsity, both unset and both requiring
    agreement before they are touched.
    """
    raise NotImplementedError(
        "tile geometry and sparsity are not set and must be surfaced before they are "
        "chosen"
    )


def schedule(*args, **kwargs):
    """There is no scheduler, and this is the point rather than an omission.

    Setting every latency equal and choosing an interval short enough to carry the
    finest one is a legitimate thing this rung may eventually do.  It is an
    implementation choice and it is not made here, and where every latency on a
    section reads underived there is no finest one to size the interval against.
    """
    raise NotImplementedError(
        "the scheduling discipline is not set and is not this rung's to choose"
    )


def learn(*args, **kwargs):
    """Nothing writes a stored parameter, because no learning rule is set.

    A threshold that is never written is a construction cost rather than a memory,
    which is why a module is still coherent without this.
    """
    raise NotImplementedError("no learning rule is set")


# --------------------------------------------------------------------------
# Reporting shared by every module.
# --------------------------------------------------------------------------


def sizing_report(structures, title=""):
    """Recompute the store from counts and fan-ins rather than transcribing it."""
    out, total, unstated = [], 0, []
    if title:
        out.append(title)
    out.append(f"{'structure / population':46} {'basis':15} {'neurons':>13} {'bits':>5} {'store':>12}")
    for s in structures:
        for p in s.populations:
            bits = p.threshold_bits
            b = p.parameter_bytes
            count = f"{p.count:,}" if p.count is not None else TO_DERIVE
            label = f"{s.name} / {p.name}"
            if b is None:
                store = TO_DERIVE
                unstated.append(label)
            else:
                store = f"{b/1e6:.3f} MB"
                total += b
            out.append(f"{label:46} {p.basis:15} {count:>13} "
                       f"{'-' if bits is None else bits:>5} {store:>12}")
    out.append("")
    out.append(f"stated total: {total/1e6:.2f} MB = {total/1e9:.3f} GB   (mixed basis)")
    out.append(f"the total is a floor; stores not stated: {len(unstated)}")
    for u in unstated:
        out.append(f"    {u}")
    return "\n".join(out)


def edge_report(edges):
    """Counts only.  Every figure here is a count of declarations, not a check that
    any declaration is right."""
    cross = [e for e in edges if e.crosses_file]
    stems = sorted({e.source.stem or e.target.stem for e in cross})
    classes = [e for e in edges
               if CLASS_ENDPOINT in (e.source.kind, e.target.kind)]
    absent = [e for e in edges if NO_ENTRY in (e.source.kind, e.target.kind)]
    waiting = [e for e in edges if PENDING in (e.source.kind, e.target.kind)]
    unread = [e for e in edges if UNSTEMMED in (e.source.kind, e.target.kind)]
    routes = [e for e in edges if ROUTE_ENDPOINT in (e.source.kind, e.target.kind)]
    timed = [e for e in edges if e.latency_s is not None]
    out = [f"edges declared            : {len(edges)}",
           f"  crossing a file boundary: {len(cross)}",
           f"  endpoint is a class     : {len(classes)}   (needs splitting at the source)",
           f"  endpoint has no entry   : {len(absent)}   (inherited; not repairable in code)",
           f"  endpoint is a route     : {len(routes)}   (names a circuit; cannot declare back)",
           f"  far file not yet opened : {len(unread)}   (no stem; a reading not yet done)",
           f"  entry not yet written   : {len(waiting)}   (in this file; blocks nothing above)",
           f"  with a stated latency   : {len(timed)}",
           f"  latency to derive       : {len(edges) - len(timed)}",
           f"far files reached         : {len(stems)}"]
    for s in stems:
        n = sum(1 for e in cross if s in (e.source.stem, e.target.stem))
        out.append(f"    {s:42} {n:3d}")
    return "\n".join(out)


def representation_report(edges):
    """Lines whose payload or frame is not typed, which is where a consumer and a
    producer can each be right and still disagree about what the numbers mean."""
    out = []
    for e in edges:
        r = e.representation
        gaps = [n for n, v in (("units", r.units), ("range", r.value_range),
                               ("frame", r.frame)) if v in OPEN_STATES]
        if gaps:
            arrow = "->" if e.source.kind == LOCAL else "<-"
            near = e.source.name if e.source.kind == LOCAL else e.target.name
            far_name = e.target.name if e.source.kind == LOCAL else e.source.name
            out.append(f"  {near[:30]:30} {arrow} {far_name[:34]:34} {','.join(gaps)}")
    head = f"lines with an untyped units, range or frame: {len(out)}"
    return "\n".join([head] + out)
