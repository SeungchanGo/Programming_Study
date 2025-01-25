#내장 함수

#1. abs - 어떤 숫자를 입력받았을 때, 그 숫자의 절댓값을 돌려주는 함수
print(abs(3))
print(abs(-3))
print(abs(-1.2))

#2. all - 반복 가능한 자료형 x를 입력 인수로 받으며 이 x가 모두 참이면 True, 거짓이 하나라도 있으면 False를 돌려준다.
print(all([1,2,3]))
print(all([1,2,3,0]))

#3. any - x 중 하나라도 참이 있으면 True를 돌려주고, x가 모두 거짓일 때에만 False를 돌려준다.
print(any([1,2,3,0]))
print(any([0, ""]))

#4. chr - 아스키 코드 값을 입력받아 그 코드에 해당하는 문자를 출력
print(chr(65))
print(chr(97))

#5. dir - 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
print(dir([1,2,3]))

#6. divmod - 2개의 숫자를 입력으로 받아 a를 b로 나눈 몫과 나머지를 튜플 형태로 돌려준다.
print(divmod(7,3)) 

#7. enumerate - 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 돌려준다.
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

#8. eval - 실행 가능한 문자열을 입력으로 받아 문자열을 실행한 결괏값을 돌려주는 함수이다.
print(eval('1+2'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4,3)'))   

#9. filter - 첫 번째 인수로 함수 이름을, 두 번쨰 인수로 그 함수에 차례
def positive(l):
    result = []
    for i in l:
        if i>0:
            result.append(i)
    return result

print(positive([1,-3,2,0,-5,6]))


def positive(x):
    return x>0
print(list(filter(positive, [1,-3,2,0,-5,6])))


#10. hex - 정수 갑슬 입력받아 16진수로 변환하여 돌려주는 함수
a = hex(234)
print(a)
print(hex(3))

#11. id - 객체를 입력받아 객체의 고유 주소 값을 돌려주는 함수
a = 3
print(id(a))
b = a
print(id(b))
print(id(3))

#12. input - 사용자 입력을 받는 함수
#a = input()
#print(a)
#b = input("Enter: ")
#print(b)

#13. int - 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 돌려주는 함수로, 정수를 입력으로 받으면 그대로 돌려준다.
a = int('3')
print(a)
print(int(3.4))

#14. instanceof(object, class) - 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False
class Person: pass
a = Person()
print(isinstance(a, Person))

b= 3
print(isinstance(b, Person))

#15. len(s) - 입력값 s의 길이를 돌려주는 함수
print(len('python'))
print(len([1,2,3]))
print(len((1, 'a')))

#16. list(s) - 반복 가능한 자료형 s를 입력받아 리스트로 만들어 돌려주는 함수
print(list('python'))
print(list((1,2,3)))

#17. map(f, iterable)은 함수(f)와 반복 가능한(iterable) 자료형을 입력으로 받는다. map은 입력 받은 자료형의 각 요소를 함수 f가 수행한 결과를 묶어서 돌려주는 함수
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1,2,3,4]) 
print(result)

def two_times(x): return x*2
b = list(map(two_times, [1,2,3,4]))
print(b)


#18. max(iterable) - 인수로 반복 가능한 자료형을 입력받아 그 최댓값을 돌려주는 함수
print(max([1,2,3]))
print(max('python'))

#19. min(iterable) - 인수로 반복 가능한 자료형을 입력받아 그 최솟값을 돌려주는 함수
print(min([1,2,3]))
print(min('python'))

#20. oct(x) - 정수 형태의 숫자를 8진수 문자열로 바꾸어 돌려주는 함수
print(oct(34))
print(oct(12345))

#21. ord(c) - 문자의 아스키 코드 값을 돌려주는 함수
print(ord('a'))
print(ord('0'))

#22. pow(x,y) - x의 y 제곱한 결과값을 돌려주는 함수
print(pow(2,4))
print(pow(3,3))

#23. range([start,] stop [,step]) - for문과 함께 자주 사용하는 함수. 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 돌려줌
print(list(range(5)))
print(list(range(5,10)))
print(list(range(1,10,2)))
print(list(range(0,-10,-1)))

#24. round(number[,ndigits]) - 숫자를 입력받아 반올림해 주는 함수
print(round(4.6))
print(round(4.2))
print(round(5.677, 2))

#25. sorted(iterable) - 입력값을 정렬한 후 그 결과를 리스트로 돌려주는 함수
print(sorted([3,1,2]))
print(sorted(['a','c','b']))

#26. str(object) - 문자열 형태로 객체를 변환하여 돌려주는 함수
print(str(3))
print(str('hi'))
print('hi'.upper())

#27. sum(iterable) - 입력받은 리스트나 튜플의 모든 요소의 합을 돌려주는 함수
print(sum([1,2,3]))
print(sum((4,5,6)))

#28. tuple(iterable) - 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 돌려주는 함수
print(tuple('abc'))
print(tuple([1,2,3]))
print(tuple((1,2,3)))

#29. type(object) - 입력값의 자료형이 무엇인지 알려주는 함수
print(type('abc'))
print(type([]))
print(type(open("test", 'w')))

#30. zip(*iterable) - 동일한 개수로 이루어진 자료형을 묶어 주는 역할을 하는 함수
print(list(zip([1,2,3], [4,5,6])))
print(list(zip([1,2,3], [4,5,6], [7,8,9])))
print(list(zip("abc", "def")))