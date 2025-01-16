INF = 999

def getMinVertex(dist, selected):
    minv = 0
    mindist = INF

    for v in range(len(dist)):
        if selected[v] == False and dist[v] < mindist:
            mindist = dist[v]
            minv = v
    return minv

def Prim(vtx, adj):
    n = len(vtx)
    selected = [False] * n
    dist = [INF] * n
    dist[0] = 0

    for _ in range(n):
        u = getMinVertex(dist, selected)
        selected[u] = True

        for v in range(n):
            if adj[u][v] != INF and not selected[v]:
                if adj[u][v] < dist[v]:
                    dist[v] = adj[u][v]