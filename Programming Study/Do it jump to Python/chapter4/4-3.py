#파일 읽고 쓰기

#1. 파일 생성하기
f = open("새파일.txt", 'w')
f.close()

#2. 파일을 쓰기 모드로 열어 출력값 적기
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    print(data)