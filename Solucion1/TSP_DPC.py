
import math
import heapq as hq

def dist(x1,y1,x2,y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

def findSet(parent, u):
    if parent[u]==u:
        return u
    parent[u] = findSet(parent, parent[u])
    return parent[u]

def unionSet(parent, rnk, u, v):
    u = findSet(parent, u)
    v = findSet(parent, v)
    if u != v:
        if rnk[u] < rnk[v]:
            temp = u
            u = v
            v = temp
        parent[v] = u
        if rnk[u] == rnk[v]:
            rnk[u]+=1

class Edge:
    def __init__(self, _u, _v, _w):
        self.u = _u
        self.v = _v
        self.w = _w
    def __lt__(self, E):
        return self.w < E.w

def TSP(node):
    
    n = len(node)
    
    # Repetir el ultimo nodo si la cantidad de nodos es par para no perderlos 
    if n % 2 != 0:
        node.append(node[n-1])
        n+=1
    
    # Crear aristas sin repetirlas
    edge = []
    ini = 0
    for u in range(n):
        for v in range(ini, n):
            if v != u:
                w = dist(node[u][0],node[u][1],node[v][0],node[v][1])
                hq.heappush(edge, Edge(u,v,w))
        ini += 1
    
    parent = [i for i in range(n)]
    rnk = [0 for i in range(n)]

    # Primer Disjoint Pair Clustering
    print("First Clustering in process")
    path = []
    restore = []
    vis = [False]*n
    cant = 0
    while cant < n/2:
        i = hq.heappop(edge)
        if findSet(parent, i.u) != findSet(parent, i.v) and not vis[i.u] and not vis[i.v]:
            vis[i.u] = vis[i.v] = True
            unionSet(parent, rnk, i.u, i.v)
            path.append((i.u,i.v))
            cant += 1
        else:
            restore.append(Edge(i.u,i.v,i.w))
    
    for i in restore:
        temp = Edge(i.u, i.v, i.w)
        hq.heappush(edge, temp)

    # Segundo Disjoint Pair Clustering
    """
        Con exepcion de la ultima arista
        ya que al estar todos en el mismo
        set no se podra encontrar
    """
    print("Second Clustering in process")
    vis = [False]*n
    cant = 0
    while cant < n/2-1:
        i = hq.heappop(edge)
        if findSet(parent, i.u) != findSet(parent, i.v) and not vis[i.u] and not vis[i.v]:
            vis[i.u] = vis[i.v] = True
            unionSet(parent, rnk, i.u, i.v)
            path.append((i.u,i.v))
            cant += 1

    # Buscar la ultima arista que encierra al ciclo (unir nodos no visitados)
    for i in range(n):
        if not vis[i]:
            for j in range(i+1, n):
                if not vis[j]:
                    path.append((i, j))
                    break
            break
    
    print("Calc distance")
    w = 0
    for i in path:
        w += dist(node[i[0]][0],node[i[0]][1],node[i[1]][0],node[i[1]][1])
    return path, w
