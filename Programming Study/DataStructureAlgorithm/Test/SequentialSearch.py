def sequential_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return -1


def seq_search_tr(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            if i > low:
                A[i], A[i-1] = A[i-1], A[i]
                i = i-1
            return i
    return -1
    
def seq_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            return i
    return -1

def seq_tr_search(A, key, low, high):
    for i in range(low, high+1):
        if A[i] == key:
            if i > low:
                A[i], A[i-1] = A[i-1], A[i]
                i = i-1
            return i
    return -1