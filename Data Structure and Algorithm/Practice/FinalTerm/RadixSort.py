from collections import deque

def radix_Sort(A):
    queues = []
    for i in range(BUCKETS): # BUCKETS: 10, 2진수 등
        queues.append(deque()) # 버킷 개의 큐(덱)을 만들어 버킷 리스트 queues에 추가
    
    n = len(A) # 원소의 개수
    factor = 1 # 가장 낮은 자리부터 시작

    for d in range(DIGITS): # DIGITS: 자릿수(1, 10, 100..)만큼 반복
        for i in range(n): # 모든 항목을  따라 큐 삽입
            queues[(A[i]//factor)%BUCKETS].append(A[i])

        i = 0
        for b in range(BUCKETS):
            while queues[b]:
                A[i] = queues[b].popleft()
                i += 1

        factor = factor * BUCKETS # factor *= BUCKETS
        print("step",d+1,A)


# 테스트
BUCKETS = 10
DIGITS = 2
data = [12, 42, 11, 56, 82]
print("정렬전", data)
radix_Sort(data)
print("정렬후", data)