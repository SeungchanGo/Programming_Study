#if문
money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# 비교 연산자
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# and, or, not
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# x in s, x not in s
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])
print('a' in ('a', 'b', 'c'))
print('j' not in 'python')

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# 조건문에서 아무 일도 하지 않게 설정
pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    pass
else:
    print("걸어 가라")


# 다양한 조건을 판단하는 elif
pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고 가라")
elif card:
    print("택시를 타고 가라")
else:
    print("걸어 가라")


# 조건부 표현식
if score >= 60:
    message = "success"
else:
    message = "faliure"

message = "success" if score >= 60 else "faliure"

