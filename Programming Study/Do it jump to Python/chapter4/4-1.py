#함수
def add(a, b): #a와 b는 매개변수
    return a + b

c = 3
d = 4
e = add(c, d)
print(e)
print(add(4,5)) #4와 5는 인수


#입력값과 결과값에 따른 함수의 형태
def add(a, b):
    result = a + b
    return result

print(add(5,6))

#1. 입력값이 없는 함수
def say():
    return 'Hi'
print(say())

#2. 결과값이 없는 함수
def add(a, b):
    print("%d, %d의 합은 %d입니다." % (a, b, a+b))
add(3,4) # print(add(3,4)) -> None

#3. 입력값도 결과값도 없는 함수
def say():
    print('hi')
say()    

#4. 매개변수 지정하여 호출하기
def add(a,b):
    return a+b

result1 = add(a=3, b=7)
print(result1)
result2 = add(b=5, a=3)
print(result2)

#5. 입력값이 몇 개가 될지 모를 때는 어떻게 해야 할까?
def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result 
result1 = add_many(1,2,3)
print(result1)
result2 = add_many(1,2,3,4,5,6,7,8,9,10)
print(result2)


def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == 'mul':
        result = 1
        for i in args:
            result = result * i
    return result        
a = add_mul('add', 1,2,3,4,5)
print(a)
b = add_mul('mul', 1,2,3,4,5)
print(b)

#6. 함수의 결과값은 언제나 하나이다
def add_and_mul(a,b):
    return a+b, a*b
result1 = add_and_mul(3,4)
print(result1)

result2, result3 = add_and_mul(7,9)
print(result2)
print(result3)

#7. 매개변수에 초기값 미리 설정하기
def say_myself(name, old, man=True):
    print("나의 이름은 %s입니다." % name)
    print("나이는 %d살입니다." % old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)  
say_myself("박응선", 27, False)

#8. 함수 안에서 선언한 변수의 효력 범위
a = 1
def vartest(a):
    a = a + 1
vartest(a)
print(a)

def vartest(hello):
    hello = hello+1
vartest(5)


# 함수 안에서 함수 밖의 변수를 변경하는 방법
#1. return 사용하기
a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

#2. global 명령어 사용하기
b = 2
def vartest():
    global b
    b = b + 1

vartest()
print(b)    
