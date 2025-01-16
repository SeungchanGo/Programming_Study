from collections import deque

BUCKETS = 10
DIGITS = 2

def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(deque())

    n = len(A)
    factor = 1

    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor)%BUCKETS].append(A[i])

        i = 0

        for b in range(BUCKETS):
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1

        factor *= BUCKETS