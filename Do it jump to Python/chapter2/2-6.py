#집합 자료형
s1 = set([1,2,3])
print(s1)

s2 = set('hello')
print(s2)

#리스트로 변환
s1 = set([1,2,3])
l1 = list(s1)
print(l1)

#튜플로 변환
t1 = tuple(s1)
print(t1)


#교집합, 합집합, 차집합 구하기
s1 = set([1, 2, 3, 4, 5 ,6])
s2 = set([4, 5, 6, 7, 8, 9])

#1. 교집합
print(s1 & s2)
print(s1.intersection(s2))

#2. 합집합
print(s1 | s2)
print(s1.union(s2))

#3. 차집합
print(s1 - s2)
print(s2 - s1)
print(s1.difference(s2))
print(s2.difference(s1))


#집합 자료형 관련 함수
#1. 값 1개 추가하기 (add)
s1 = set([1, 2, 3])
s1.add(4)
print(s1)

#2. 값 여러 개 추가하기 (update)
s1 = set([1, 2, 3])
s1.update([4, 5, 6])
print(s1)

#3. 특정 값 제거하기 (remove)
s1 = set([1, 2, 3])
s1.remove(2)
print(s1)
