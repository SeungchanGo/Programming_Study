# x의 n 거듭제곱 구하기 (억지기법)
def slow_power(x, n):
    result = 1.0
    for i in range(n):
        result *= x
    return result


# x의 n 거듭제곱 구하기 (분할정복)
def power(x, n):
    if n == 1:
        return x
    elif n%2 == 0:
        return power(x*x, n//2)
    else:
        return power(x*x, (n-1)//2)
    

import time 
#print("억지기법(2**500) = ", slow_power(2.0, 500))
#print("분할정복(2**500) = ", power(2.0, 500))

#t1 = time.time()
#for i in range(1000000):
#    slow_power(2.0, 500)
#t2 = time.time()
#for i in range(1000000):
#    power(2.0, 500)
#t3 = time.time()  
#print(f"억지기법 : {t2-t1}")
#print(f"분할기법 : {t3-t2}")



# 분할정복을 이용한 k번째 작은 수 찾기
def quick_select(A, left, right, k):
    pos = partition(A, left, right)

    if (pos+1 == left+k):
        return A[pos]
    elif (pos+1 > left+k):
        return quick_select(A, left, pos-1, k)
    else:
        return quick_select(A, pos+1, right, k-(pos+1-left))
    
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


# 병합 정렬 알고리즘
def merge_sort(A, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid+1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right):
    k = left
    i = left 
    j = mid + 1

    while i<=mid and j<=right:
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
    
    A[left:right+1] = sorted[left:right+1]

    print(A)


data = [8, 1, 7, 3, 9, 2, 4, 5]
sorted = [0]*len(data)
merge_sort(data, 0, 7)


