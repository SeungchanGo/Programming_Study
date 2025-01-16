def quick_sort(A, left, right):
    if left < right:
        q = partition(A, left, right)
        quick_sort(A, left, q-1)
        quick_sort(A, q+1, right)

def partition(A, left, right):
    pivot = A[left]
    low = left + 1
    high = right
    
    while (low < high): # low와 high가 역전되지 않는 한 반복
        while low <= right and A[low] <= pivot:
            low += 1 # A[low] <= pivot 이면 low를 오른쪽으로 진행
        
        while high >=left and A[high] > pivot:
            high -= 1 # A[high] > pivot 이면 high를 왼쪽으로 진행

        if low < high:
            A[low], A[high] = A[high], A[low]

    A[left], A[high] = A[high], A[left]
    return high

    data = [71, 49, 92, 55, 38, 28, 72, 53]
    quick_sort(data)





