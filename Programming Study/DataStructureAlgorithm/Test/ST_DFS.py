vtx = ['U', 'V', 'W', 'X', 'Y']

alist = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 0, 1],
        [0, 0, 1, 1, 0]]

visited = [False] * len(vtx)

def ST_DFS(vtx, adj, s, visited):
    visited[s] = True
    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                print("(", vtx[s], vtx[v], ")", end=" ")
                ST_DFS(vtx, adj, v, visited)

ST_DFS(vtx, alist, 0, visited)