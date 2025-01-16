def DFS(vtx, adj, s, visited):
    visited[s] = True
    print(vtx[s], end=" ")

    for v in range(len(vtx)):
        if adj[s][v] != 0:
            if visited[v] == False:
                DFS(vtx, adj, v, visited)
                
                
vtx = ['U', 'V', 'W', 'X', 'Y']
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]]
visited = [False] * len(vtx)


print('DFS(출발: W): ', end = "")
DFS(vtx, edge, 2, [False]*len(vtx))
print()