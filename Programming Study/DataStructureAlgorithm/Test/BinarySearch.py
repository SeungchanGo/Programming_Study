def binary_search(A, key, low, high):
    if low <= high:
        middle = (low + high) // 2
        if key == A[middle]:
            return middle
        elif key < A[middle]:
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return -1

def binary_search_iter(A, key, low, high):
    while low <= high:
        middle = (low+high)//2
        if key == A[middle]:
            return middle
        elif key > A[middle]:
            low = middle + 1
        else:
            high = middle -1
    return -1


def binary_search(A, key, low, high):
    if low <= high:
        middle = (low + high) // 2
        if A[middle] == key:
            return middle
        elif key < A[middle]:
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
        
def binary_search_iter(A, key, low, high):
    while low <= high:
        middle = (low + high) // 2
        if A[middle] == key:
            return middle
        elif key < A[middle]:
            high = middle-1
        else:
            low = middle+1