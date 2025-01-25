def selectSort(A):
    n = len(A)
    for i in range(n-1):
        least = i
        for j in range(i+1, n):
            if A[least] > A[j]:
                least = j
        A[i], A[least] = A[least], A[i]
        print("Step %2d =" %(i+1), A)


# 테스트
data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("Original: ", data)
selectSort(data)
print("Selection: ", data)
print()


def insertSort(A):
    n = len(A)
    for i in range(1, n):
        key = A[i]
        j = i-1
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]
            j -= 1
        A[j+1] = key
        print("Step %2d =" %i, A)
        
data = [6, 3, 7, 4, 9, 1, 5, 2, 8]
print("Original: ", data)
insertSort(data)        
print("Insertion: ", data)


data1 = [80, 50, 20, 10, 30, 40, 90, 60, 70]
print(selectSort(data1))
data2 = [80, 50, 20, 10, 30, 40, 90, 60, 70]
print(insertSort(data2))