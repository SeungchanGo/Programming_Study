# collections 모듈의 deque 클래스 객체 생성
from collections import deque
dq = deque()

for i in range(9):
    if i%2 == 0:
        dq.append(i)
    else:
        dq.appendleft(i)

print(dq)     

for i in range(2):
    dq.popleft()
print("짝수는 후단, 홀수는 전단에 삽입", dq)

for i in range(3):
    dq.pop()
print(dq)    

for i in range(9, 14):
    dq.appendleft(i)
print(dq)    
