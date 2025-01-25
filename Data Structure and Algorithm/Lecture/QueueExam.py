import queue
import random

q = queue.Queue(maxsize=8)

print("삽입 순서: ", end="")

while not q.full():
    v = random.randint(0, 100)
    print(v, end=" ")
    q.put(v)
print()    

print("출력 순서: ", end="")
while not q.empty():
    print(q.get(), end=" ")    
print()