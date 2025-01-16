import queue
# 크기가 20인 stack을 생성
s = queue.LifoQueue(maxsize = 20)

# 문자열을 입력 받아 하나의 문자를 스택에 삽입
msg = input('문자열 입력 : ')
for c in msg:
    s.put(c)

# 스택에 있는 요소들을 하나씩 출력
print('문자열 출력 : ', end="")
while not s.empty():
    print(s.get(), end="")
print()
