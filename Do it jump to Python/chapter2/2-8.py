# 변수

a = 1
b = "python"
c = [1,3,4]

print(id(a))

#리스트를 복사할 때
a = [1, 2, 3]
b = a
print(b)
print(id(a) == id(b))
print(a is b)

a[1] = 4
print(a)
print(b)

#1. [:] 사용
a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

#2. copy 모듈 사용
from copy import copy
a = [1, 2, 3]
b = copy(a)
print(a is b)


# 변수를 만드는 여러 가지 방법
a, b = ('python', 'life')
(a, b) = 'python', 'life'
print(a, b)
print((a, b))