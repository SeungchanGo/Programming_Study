## 1
x = 100
y = 200
sum = x + y
print(f'{x} 과 {y} 의 합은 {sum} 입니다.')

## 2
x, y = -1, 3
result = (-y)**3 + 2 * (x**2) * y
print(result)

## 3
print('Hello,\nWorld!\n\'하나!\'\n\"둘!\"')

print('''안녕하세여
저는 고승찬입니다.
안녕히 계세요.''')

## 4
print("안녕" + "하세요")
print("안녕하세요" * 3)
print("안녕하세요"[1:3])

## 5
s = "Hello Python"
print(s[6:10])
print(s[-6:-2])
print(s[0:9:2])
print(s[-1:-7:-2])

## 6
#x = int(input('첫 번째 정수를 입력: '))
#y = int(input('두 번째 정수를 입력: '))
#print(f'{x} + {y} =', x+y)
#print(f'{x} - {y} =', x-y)
#print(f'{x} * {y} =', x*y)
#print(f'{x} / {y} =', x/y)

## 7
p = "도서관에서 보자"
print(p)
print(p[-1::-1])

## 8
#def calc_part(t_cost, name):
#    cost = int(input(name + 'cost? '))
#    count = int(input(name + 'count? '))
#    return t_cost + cost * count

#total_cost = 0
#total_cost = calc_part(total_cost, "CPU")
#total_cost = calc_part(total_cost, "main board")    
#total_cost = calc_part(total_cost, "memory")
#total_cost = calc_part(total_cost, "hard disk")

## 9
def print_info(name, phone):
    print('이름: %s, 전화번호: %s' % (name, phone))
print_info('홍길동', '010111111')


## 10
#def inch_to_cm(inch):
#    cm = inch * 2.54
#    return cm

#num = int(input("인치 입력: "))
#result = inch_to_cm(num)
#print('%d inch -> %.2f cm' % (num, result))

## 11
#age = int(input('나이를 입력: '))
#if age >= 15:
#    print('영화 관람 가능')
#else:
#    print('영화 관람 불가')

## 12
#num = int(input('정수를 입력: '))
#if num >= 0:
#    if num == 0:
#        print('0입니다.')
#    else:
#        print('양수입니다.')
#else:
#    print('음수입니다.')


## 13
i = 1
sum = 0
while i <= 10:
    sum += i
    i += 1

print("합계:", sum)


## 14
#import turtle
#t = turtle.Turtle()
#for i in range(6):
#    t.circle(100)
#    t.right(60)	


## 15
#t1 = turtle.Turtle()
#num = int(input('몇각형: '))
#for i in range(num):
#    t.forward(100)
#    t.right(360/num)    

# ## 16
# for i in range(2, 10):
#     print(f'{i}단')
#     for j in range(1, 10):
#         print(f'{i} * {j} =' ,i*j)
#     print()

## 17
#fact = 1
#n = int(input("정수 입력: "))
#for i in range(1, n+1):
#    fact *= i    
#print(fact)


## 18
# for i in range(5):
#     for j in range(10):
#         print('*', end=" ")
#     print()


# for i in range(1, 6):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if j < i:
#             print(" ", end = " ")
#         else:
#             print("*", end = " ")
#     print()


# for i in range(5):
#     for j in range(5):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# for i in range(4, -1, -1):
#     for j in range(5):
#         if j >= i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()



## 19
#sign = True
#while sign:
#    light = input('색상 입력: ')
#    if light == 'blue':
#        break
#print("전진")


import turtle
t = turtle.Turtle()

v = 3
count = 1

while True:
    for i in range(v):
        t.forward(100)
        t.right(360/v)
    t.clear()

    v += count 
    if v == 6:
        count = -1
    elif v == 3:
        count = 1
