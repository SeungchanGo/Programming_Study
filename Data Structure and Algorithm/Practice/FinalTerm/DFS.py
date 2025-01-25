
visited = [False, False, False, False, False] # 방문한 노드를 표시할 리스트

def DFS(vtx, adj, s, visited):
    print(vtx[s], end=' ')
    visited[s] = True

    for v in range(len(vtx)):
        if adj[s][v] != 0: # 간선이 존재함
            if visited[v] == False: # 아직 방문하지 않음
                DFS(vtx, adj, v, visited) # 방문

vtx = ['U', 'V', 'W', 'X', 'Y']
edge = [[0, 1, 1, 0, 0],
        [1, 0, 1, 1, 0],
        [1, 1, 0, 0, 1],
        [0, 1, 0, 0, 0],
        [0, 0, 1, 0, 0]]


print('DFS(출발: W): ', end = "")
DFS(vtx, edge, 2, [False]*len(vtx))
print()