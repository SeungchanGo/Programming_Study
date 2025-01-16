from queue import Queue

def BFS(vtx, alist, s):
    n = len(vtx)
    visited = [False] * n
    visited[s] = True
    Q = Queue()
    Q.put(s)

    while not Q.empty():
        s = Q.get
        print(vtx[s], end=" ")

        for v in alist[s]:
            if visited[v] == False:
                Q.put(v)
                visited[v] = True


vtx = ['U', 'V', 'W', 'X', 'Y']
aList = [[1, 2], 
         [0, 2, 3], 
         [0, 1, 4], 
         [1], 
         [2]] 
print('BFS_AL(출발: W): ', end="")
BFS(vtx, aList, 2)
print()             