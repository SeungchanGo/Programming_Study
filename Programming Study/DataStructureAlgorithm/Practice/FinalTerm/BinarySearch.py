def binary_search(A, key, low, high):
    if (low <= high):
        middle = (low + high) // 2
        print(middle, end = " ")
        if key == A[middle]:
            return middle
        elif (key < A[middle]):
            return binary_search(A, key, low, middle-1)
        else:
            return binary_search(A, key, middle+1, high)
    return -1


data = [3, 5, 8, 15, 16, 19, 22, 25, 27, 31, 32, 36, 39, 40, 43, 45]
print("탐색 값의 인덱스:", binary_search(data, 32, 0, len(data)-1))
