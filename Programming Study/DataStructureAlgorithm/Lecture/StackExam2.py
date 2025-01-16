import Stack2 
import random
colorList = ['빨강', '주황', '노랑', '초록', '파랑', '보라']

q = Stack2.ArrayStack(6)

random.shuffle(colorList)

print("과자집에 가는길 :", end=" ")
for c in colorList:
        print(c, end=" → ")
        q.push(c)
print('과자집')

q.display()

print("우리집에 오는길 : ", end=" ")
while not q.isEmpty():       
        print(q.pop(), end=" → ")
print('우리집')


