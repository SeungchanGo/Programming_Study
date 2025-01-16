# 리스트의 인덱싱
a = [1, 2, 3]
print(a)
print(a[0])
print(a[1] + a[2])
print(a[-1])

b = [1, 2, 3, ['a', 'b', 'c']]
print(b[0])
print(b[-1])
print(b[-1][0])
print(b[3][2])


# 리스트의 슬라이싱
c = [1, 2, 3, 4, 5]
print(c[0:2])
print(c[:2])
print(c[2:])

d = "12345"
print(d[0:3])


# 리스트 연산하기
#1. 리스트 더하기 (+)
a = [1, 2, 3]
b = [4, 5, 6]
print(a + b)

#2. 리스트 반복하기 (*)
a = [1, 2, 3]
print(a * 3)

#3. 리스트 길이 구하기
a = [1, 2, 3, 4, 5]
print(len(a))


# 리스트의 수정과 삭제
#1. 리스트에서 값 수정하기
a = [1, 2, 3]
a[2] = 4
print(a)

#2. del 함수 사용해 리스트 요소 삭제하기
a = [1, 2, 3, 4]
del a[1]
print(a)

del a[2:]
print(a)


# 리스트 관련 함수
#1. 리스트에 요소 추가하기 (append)
a = [1, 2, 3]
a.append(4)
print(a)
a.append([5,6])
print(a)

#2. 리스트 정렬 (sort)
a = [1, 4, 3, 2]
a.sort()
print(a)

b = ['a', 'c', 'b']
b.sort()
print(b)

#3. 리스트 뒤집기 (reverse)
a = ['a', 'b', 'c']
a.reverse()
print(a)

#4. 위치 반환 (index)
a = [1,2,3]
print(a.index(3))
print(a.index(1))

#5. 리스트에 요소 삽입 (insert)
a = [1, 2, 3]
a.insert(0, 4)
print(a)

#6. 리스트 요소 제거 (remove)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
print(a)

#7. 리스트 요소 끄집어내기 (pop)
a = [1, 2, 3]
print(a.pop())
print(a)

b = [1, 2, 3]
b.pop(1)
print(b)

#8. 리스트에 포함된 요소 x의 개수 세기 (count)
a = [1, 2, 3, 1]
print(a.count(1))

#9. 리스트 확장 (extend)
a = [1, 2, 3]
a.extend([4, 5])
print(a)

b = [6, 7]
a.extend(b)
print(a)