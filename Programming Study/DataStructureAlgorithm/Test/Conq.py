def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right

    while low < high:
        while low <= right and A[low] <= pivot:
            low += 1

        while high >= left and A[high] > pivot:
            high -= 1
        
        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high


def quick_select(A, left, right, k):
    pos = partition(A, left, right)

    if pos+1 == left+k:
        return A[pos]
    elif pos+1 > left+k:
        return quick_select(A, left, pos-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))
    

def merge_sort(A, left, right):
    if left < right:
        mid = (left+right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    i = left
    k = left
    j = mid+1

    while i <= mid and j <= right:
        if A[i] <= A[j]:
            sorted[k] = A[i]
            i, k = i+1, k+1

        else:
            sorted[k] = A[j]
            j, k = j+1, k+1

    if i > mid:
        sorted[k:k+right-j+1] = A[j:right+1]
    else:
        sorted[k:k+mid-i+1] = A[i:mid+1]

    A[left:right+1] = sorted[left+right+1]

    