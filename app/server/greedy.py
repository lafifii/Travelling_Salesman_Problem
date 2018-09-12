from __future__ import print_function, division
from itertools import islice
from array import array as pyarray
if "xrange" not in globals():
    xrange = range
else:
    pass
def optimize_solution( distances, connections, endpoints ):
    N = len(connections)
    path = restore_path( connections, endpoints )
    def ds(i,j):
        pi = path[i]
        pj = path[j]
        if pi < pj:
            return distances[pj][pi]
        else:
            return distances[pi][pj]

    d_total = 0.0
    optimizations = 0
    for a in xrange(N-1):
        b = a+1
        for c in xrange( b+2, N-1):
            d = c+1
            delta_d = ds(a,b)+ds(c,d) -( ds(a,c)+ds(b,d))
            if delta_d > 0:
                d_total += delta_d
                optimizations += 1
                connections[path[a]].remove(path[b])
                connections[path[a]].append(path[c])
                connections[path[b]].remove(path[a])
                connections[path[b]].append(path[d])

                connections[path[c]].remove(path[d])
                connections[path[c]].append(path[a])
                connections[path[d]].remove(path[c])
                connections[path[d]].append(path[b])
                path[:] = restore_path( connections, endpoints )

    return optimizations, d_total

def restore_path( connections, endpoints ):

    if endpoints is None:
        start, end = [idx
                      for idx, conn in enumerate(connections)
                      if len(conn)==1 ]
    else:
        start, end = endpoints

    path = [start]
    prev_point = None
    cur_point = start
    while True:
        next_points = [pnt for pnt in connections[cur_point]
                       if pnt != prev_point ]
        if not next_points: break
        next_point = next_points[0]
        path.append(next_point)
        prev_point, cur_point = cur_point, next_point
    return path

def _assert_triangular(distances):
    for i, row in enumerate(distances):
        if len(row) < i:
        	return

def pairs_by_dist(N, distances):
    indices = []
    for i in xrange(N):
        for j in xrange(i):
            indices.append(i*N+j)

    indices.sort(key = lambda ij: distances[ij//N][ij%N])
    return ((ij//N,ij%N) for ij in indices)

def solve_tsp( distances, optim_steps=3, pairs_by_dist=pairs_by_dist, endpoints=None ):
    N = len(distances)
    if N == 0: return []
    if N == 1: return [0]

    _assert_triangular(distances)
    node_valency = pyarray('i', [2])*N
    if endpoints is not None:
        start, end = endpoints
        if start == end: raise ValueError("start=end is not supported")
        node_valency[start]=1
        node_valency[end]=1

    connections = [[] for i in xrange(N)]

    def join_segments(sorted_pairs):
        segments = [ [i] for i in xrange(N) ]

        def possible_edges():
            for ij in sorted_pairs:
                i,j = ij
                if node_valency[i] and node_valency[j] and\
                   (segments[i] is not segments[j]):
                    yield ij

        def connect_vertices(i,j):
            node_valency[i] -= 1
            node_valency[j] -= 1
            connections[i].append(j)
            connections[j].append(i)
            seg_i = segments[i]
            seg_j = segments[j]
            if len(seg_j) > len(seg_i):
                seg_i, seg_j = seg_j, seg_i
                i, j = j, i
            for node_idx in seg_j:
                segments[node_idx] = seg_i
            seg_i.extend(seg_j)

        def edge_connects_endpoint_segments(i,j):
            si,sj = segments[i],segments[j]
            ss,se = segments[start], segments[end]
            return (si is ss) and (sj is se) or (sj is ss) and (si is se)

        edges_left = N-1
        for i,j in possible_edges():
            if endpoints and edges_left!=1 and edge_connects_endpoint_segments(i,j):
                continue #para que no terimne antes de lo que debe

            connect_vertices(i,j)
            edges_left -= 1
            if edges_left == 0:
                break

    join_segments(pairs_by_dist(N, distances))
    for passn in range(optim_steps):
        nopt, dtotal = optimize_solution( distances, connections, endpoints )
        if nopt == 0:
            break
    return restore_path( connections, endpoints=endpoints )
