#!/usr/bin/env python3
"""
Brain edge index — regenerates the cross-file connection map from the architecture files.

Reads every Brain_architecture_NN_*.md in a directory, extracts the structure headings
and every edge line in the Inputs and Outputs fields, resolves each endpoint against the
set of structure names, and reports what did not resolve, bucketed.

It then reconciles each edge against its far end: an output declared in one file is paired
only if the structure it names declares a matching input back, and the reverse. Unpaired
edges are bucketed as producer-only or consumer-only, and the file-pair ranking is given
twice — once by edges declared, once by edges paired.

This is an instrument, not a document. It is regenerated, never stored: a stored index is
a second record of the edges with no mechanism keeping it true, and a stale one fails
silently. Run it; read the output; discard the output.

The endpoint matcher is deliberately crude and errs toward reporting a miss. A miss is a
candidate for reading, never a verdict that an edge dangles.

The reconciliation pass fails in the opposite direction, and that failure is silent. Two
different structures that fold to the same comparison key resolve to each other, so an
edge with no real far end can report as PAIRED. A pair is a candidate for reading exactly
as a miss is. Neither is a verdict.

Both directions read only the architecture rung. An architecture edge whose source file
does not carry the connection is invisible here, and a source file with no architecture
file — 19 and 20 — is invisible entirely.

Usage:  python3 Brain_edge_index_2026_08_11.py [directory]
"""

import re
import sys
import glob
import os
from collections import Counter

FIELDS = ('Function', 'Inputs', 'Outputs', 'Sizing', 'Shape',
          'Edge latency', 'Invariant', 'Justification')

FIELD_RE = re.compile(r'^- \*\*(' + '|'.join(FIELDS) + r')')
HEADING_RE = re.compile(r'^## (.+?)\s*$')

# Three edge-line forms are in use across the files: the arrow inside the bold run
# with a nested bullet, the arrow outside the bold run, and edges written inline in a
# prose paragraph with no bullet. All three are matched here.
ENDPOINT_RE = re.compile(r'(?:\*\*\s*([\u2190\u2192])\s*(.+?)\*\*)'
                         r'|(?:([\u2190\u2192])\s*\*\*(.+?)\*\*)')

# Headings that introduce commentary rather than a structure.
NOT_A_STRUCTURE = ('structural invariant', 'section total', 'sizing basis',
                   'the bundling question', 'endpoint kinds', 'what this section is',
                   'far-end dependencies', 'findings this file records',
                   'the two regions that are not here', 'the payload in this section',
                   'a correction to')

STOPWORDS = {'the', 'a', 'an', 'of', 'its', 'their', 'via', 'from', 'to', 'and'}

# How many unpaired edges to list per bucket. The counts above the lists are always
# complete; only the listing is cut.
LIST_CAP = 60


def is_structure(heading):
    h = heading.lower().lstrip('0123456789. ')
    return not any(h.startswith(p) or p in h for p in NOT_A_STRUCTURE)


def normalize(s):
    """Fold a name to a comparison key. Parentheticals and punctuation carry no
    identity; an abbreviation given in parentheses is a second label, not the name."""
    s = s.lower()
    s = re.sub(r'\(.*?\)', ' ', s)
    s = s.replace('\u2014', ' ').replace('\u2013', ' ').replace('-', ' ').replace('/', ' ')
    s = re.sub(r'[^a-z0-9 ]', ' ', s)
    return ' '.join(t for t in s.split() if t not in STOPWORDS)


def parse(directory):
    """Return (structures, edges). structures: list of (filenum, heading).
    edges: list of (filenum, owner, 'in'|'out', endpoint)."""
    structures, edges = [], []
    paths = sorted(glob.glob(os.path.join(directory, 'Brain_architecture_[0-9]*.md')))
    if not paths:
        sys.exit(f'no Brain_architecture_NN_*.md files found in {directory}')

    for path in paths:
        num = int(re.search(r'_(\d\d)_', os.path.basename(path)).group(1))
        owner, field = None, None
        for line in open(path, encoding='utf-8'):
            head = HEADING_RE.match(line)
            if head:
                name = head.group(1).strip()
                owner = name if is_structure(name) else None
                if owner:
                    structures.append((num, owner))
                field = None
                continue
            match = FIELD_RE.match(line)
            if match:
                field = {'Inputs': 'in', 'Outputs': 'out'}.get(match.group(1))
            elif line.startswith('#'):
                field = None
            if owner and field:
                for a1, n1, a2, n2 in ENDPOINT_RE.findall(line):
                    name = (n1 if a1 else n2)
                    name = re.sub(r'\s+', ' ', name).strip().strip('.,')
                    if name:
                        edges.append((num, owner, field, name))
    return structures, edges


def build_struct_resolver(structures):
    """Resolve an endpoint name to the set of (filenum, heading) it may name.

    This is the single matching rule. The file-number resolver below is derived from
    it rather than written twice, so the two cannot disagree."""
    index = {}
    for num, heading in structures:
        index.setdefault(normalize(heading), set()).add((num, heading))
        stem = normalize(re.split(r'[\u2014\u2013,:]', heading)[0])
        if stem:
            index.setdefault(stem, set()).add((num, heading))

    def resolve_struct(name):
        key = normalize(name)
        if key in index:
            return index[key]
        best = None
        for k, v in index.items():
            if len(k) < 6:
                continue
            if k in key or key in k:
                if best is None or len(k) > len(best[0]):
                    best = (k, v)
        return best[1] if best else None

    return resolve_struct


def build_resolver(structures):
    """Resolve an endpoint name to the set of file numbers it may land in."""
    resolve_struct = build_struct_resolver(structures)

    def resolve(name):
        hit = resolve_struct(name)
        return {num for num, _ in hit} if hit else None

    return resolve


def reconcile(edges, resolve_struct):
    """Pair each edge against its far end.

    An output declared by structure S in file a, naming endpoint E, is PAIRED when some
    structure the endpoint resolves to declares an input whose own endpoint resolves back
    to S. Unpaired outputs are producer-only; unpaired inputs are consumer-only."""
    declared = {}
    for num, owner, field, name in edges:
        declared.setdefault((num, owner), {'in': [], 'out': []})[field].append(name)

    def declares_back(far, direction, home):
        entry = declared.get(far)
        if not entry:
            return False
        for name in entry[direction]:
            hit = resolve_struct(name)
            if hit and home in hit:
                return True
        return False

    paired, producer_only, consumer_only = [], [], []
    for num, owner, field, name in edges:
        far_set = resolve_struct(name)
        if not far_set:
            continue                      # already reported as unresolved
        home = (num, owner)
        opposite = 'in' if field == 'out' else 'out'
        hits = sorted(f for f in far_set if declares_back(f, opposite, home))
        row = (home, field, name, sorted(far_set), hits)
        if hits:
            paired.append(row)
        elif field == 'out':
            producer_only.append(row)
        else:
            consumer_only.append(row)
    return paired, producer_only, consumer_only


def show(rows, title, note):
    print(f'{title} ({len(rows)})')
    print(f'  {note}')
    cross = [r for r in rows if any(f != r[0][0] for f, _ in r[3])]
    for (num, owner), field, name, far_set, _ in cross[:LIST_CAP]:
        arrow = '->' if field == 'out' else '<-'
        far = ','.join(f'{f:02d}' for f, _ in far_set)
        print(f'  {num:02d} {owner[:40]:40} {arrow} {name[:44]:44} [{far}]')
    if len(cross) > LIST_CAP:
        print(f'  ... and {len(cross) - LIST_CAP} more crossing a file')
    print()


def report(structures, edges, resolve):
    matrix, unresolved = Counter(), []
    for num, owner, field, name in edges:
        far = resolve(name)
        if far:
            for f in far:
                matrix[(num, f)] += 1
        else:
            unresolved.append((num, owner, field, name))

    files = sorted({n for n, _ in structures})
    same = sum(v for (a, b), v in matrix.items() if a == b)
    cross = sum(v for (a, b), v in matrix.items() if a != b)
    near = sum(v for (a, b), v in matrix.items() if a != b and abs(a - b) <= 2)

    print(f'architecture files : {len(files)}')
    print(f'structures         : {len(structures)}')
    print(f'edge mentions      : {len(edges)}')
    print(f'  endpoint resolves: {len(edges) - len(unresolved)}')
    print(f'  unresolved       : {len(unresolved)}')
    print()
    print(f'resolved endpoints inside own file : {same}')
    print(f'resolved endpoints crossing a file : {cross}')
    if cross:
        print(f'  crossing with |i-j| <= 2         : {near}'
              f'   ({100 * near // cross}% -- what a sliding 3-file window sees)')
        print(f'  crossing with |i-j| >  2         : {cross - near}'
              f'   ({100 * (cross - near) // cross}% -- what it cannot see)')
    print()

    print('cross-file edge matrix (row = file, col = far end); . = none')
    print('     ' + ''.join(f'{c:4d}' for c in files))
    for r in files:
        cells = ''.join(f'{matrix.get((r, c), 0):4d}' if matrix.get((r, c)) and r != c
                        else '   .' for c in files)
        print(f'{r:3d}  {cells}')
    print()

    print('heaviest file pairs, by edges declared between them')
    pairs = Counter()
    for (a, b), v in matrix.items():
        if a != b:
            pairs[tuple(sorted((a, b)))] += v
    for (a, b), v in pairs.most_common(20):
        print(f'  {a:02d} <-> {b:02d}   {v:3d}   (apart by {abs(a - b)})')
    print()

    print(f'unresolved endpoints, most repeated first ({len(unresolved)} mentions)')
    for name, n in Counter(name for _, _, _, name in unresolved).most_common(40):
        print(f'  {n:3d}  {name[:90]}')
    print()
    print('Triage each against the source design file section 9 before touching anything.')
    print('  a hit listed there is inherited and is repaired at the source, not here')
    print('  a hit not listed there was introduced in derivation and is repaired here')
    print('  a sub-element endpoint is not a miss; this index carries no sub-element names')
    print()
    print('=' * 78)
    print()


def reconciliation_report(edges, resolve_struct):
    paired, producer_only, consumer_only = reconcile(edges, resolve_struct)
    total = len(paired) + len(producer_only) + len(consumer_only)

    print('EDGE RECONCILIATION -- each edge against its far end')
    print()
    print(f'edges with a resolved endpoint : {total}')
    print(f'  paired at both ends          : {len(paired)}')
    print(f'  producer-only                : {len(producer_only)}')
    print(f'  consumer-only                : {len(consumer_only)}')
    print()

    show(producer_only, 'PRODUCER-ONLY',
         'declared as an output; the far structure declares no matching input')
    show(consumer_only, 'CONSUMER-ONLY',
         'declared as an input; the far structure declares no matching output')

    print('file pairs by edges PAIRED at both ends -- the ranking for connection order')
    ranked = Counter()
    for (num, _), _, _, _, hits in paired:
        for f, _ in hits:
            if f != num:
                ranked[tuple(sorted((num, f)))] += 1
    if not ranked:
        print('  none')
    for (a, b), v in ranked.most_common(20):
        print(f'  {a:02d} <-> {b:02d}   {v:3d}   (apart by {abs(a - b)})')
    print()
    print('A pair is a candidate for reading, never a verdict that the edge is sound.')
    print('  the matcher is crude in both directions, and a false pair is silent')
    print('  two structures folding to one key resolve to each other and report PAIRED')
    print('  read both ends before acting on any row above, in either direction')
    print('An unpaired edge is likewise a candidate: the far end may name the structure')
    print('  by a synonym, or at a sub-element this index carries no name for.')


def main():
    directory = sys.argv[1] if len(sys.argv) > 1 else '.'
    structures, edges = parse(directory)
    report(structures, edges, build_resolver(structures))
    reconciliation_report(edges, build_struct_resolver(structures))


if __name__ == '__main__':
    main()
