# list()객체 생성
s = list() #s = []

# 문자열 입력받아 변수에 저장
msg = input("문자열 입력 : ")

for c in msg:
    s.append(c)

print("출력 문자열 : ", end="")

while len(s) > 0:
    print(s.pop(), end="")
    