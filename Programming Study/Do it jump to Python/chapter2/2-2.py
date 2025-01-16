#문자열 포매팅
#1. 숫자 바로 대입
a1 = "I eat %d apples." % 3
print(a1)

#2. 문자열 바로 대입
a2 = "I eat %s apples." % "five"
print(a2)

#3. 숫자 값을 나타내는 변수로 대입
number = 3
a3 = "I eat %d apples." % number
print(a3)

#4. 2개 이상의 값 넣기
number = 10
day = "three"
a4 = "I ate %d apples. so I was sick for %s days" % (number, day)
print(a4)

# 포매팅 연산 %d와 %를 같이 쓸 때는 %%
a5 = "Error is %d%%" %98
print(a5)


# 포맷 코드와 숫자 함꼐 사용하기
#1. 정렬과 공백
b1 = "%10s" % "hi"
print(b1)
b2 = "%-10sjane" % "hi"
print(b2)

#2. 소수점 표현하기
b3 = "%0.4f" % 3.42134234
print(b3)
b4 = "%10.3f" % 3.42134234
print(b4)


#format 함수를 사용한 포매팅
#1. 숫자 바로 대입하기
c1 = "I eat {0} apples".format(3)
print(c1)

#2. 문자열 바로 대입하기
c2 = "I eat{0} apples".format(" five")
print(c2)

#3. 숫자 값을 가진 변수로 대입하기
number = 3
c3 = "I eat {0} apples".format(number)
print(c3)

#4. 2개 이상의 값 넣기
number = 10
day = "three"
c4 = "I ate {0} apples. so I was sick for {1} days".format(number, day)
print(c4)

#5. 이름으로 넣기
c5 = "I ate {number} apples. so I was sick for {day} days".format(number = 20, day = 4)
print(c5)

#6. 인덱스와 이름을 혼용해서 넣기
c6 = "I ate {0} apples. so I was sick for {day} days".format(50, day = 5)
print(c6)

#7. 왼쪽 정렬
c7 = "{0:<10}".format("hi")
print(c7)

#8. 오른쪽 정렬
c8 = "{0:>10}".format("hi")
print(c8)

#9. 가운데 정렬
c9 = "{0:^10}".format("hi")
print(c9)

#10. 공백 채우기
c10 = "{0:=^10}".format("hi")
print(c10)
c11 = "{0:!^10}".format("hi")
print(c11)

#11. 소수점 표현하기
y = 3.42134234
c12 = "{0:0.4f}".format(y)
print(c12)
c13 = "{0:10.4f}".format(y)
print(c13)

#12. {또는} 문자 표현하기
c14 = "{{and}}".format()
print(c14)

# f문자열 포매팅
name = "홍길동"
age = 30
d1 = f"나의 이름은 {name}입니다. 나이는 {age}입니다."
print(d1)

d2 = f"나는 내년이면 {age+1}살이 된다."
print(d2)

d = {"name" : "홍길동", "age" : 30 }
d3 = f"나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다."
print(d3)

d4 = f"{"hi":<10}"
print(d4)

d5 = f"{"hi":>10}"
print(d5)

d6 = f"{"hi":^10}"
print(d6)

d7 = f"{"hi":=^10}"
print(d7)

y = 3.42134234
d8 = f"{y:0.4f}"
print(d8)

d9 = f"{{and}}"
print(d9)


#문자열 관련 함수
#1. 문자 개수 세기 (count)
a = "hobby"
print(a.count("b"))

#2. 위치 알려주기1 (find)
a = "Python is the best choice"
print(a.find("b"))
print(a.find("k"))

#3. 위치 알려주기2 (index)
a = "Life is too short"
print(a.index("t"))

#4. 문자열 삽입 (join)
print(",".join("abcd"))
print(",".join(["a", "b", "c", "d"]))

#5. 소문자를 대문자로 바꾸기 (upper)
a = "hi"
print(a.upper())

#6. 대문자를 소문자로 바꾸기 (lower)
a = "HI"
print(a.lower())

#7. 왼쪽 공백 지우기 (lstrip)
a = " hi "
print(a.lstrip())

#8. 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

#9. 양쪽 공백 지우기 (strip)
a = " hi "
print(a.strip())

#10. 문자열 바꾸기 (replace)
a = "Life is too short"
print(a.replace("Life", "your leg"))

#11. 문자열 나누기 (split)
a = "Life is too short"
print(a.split())
b = "a:b:c:d"
print(b.split(":"))