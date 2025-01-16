# 전역 변수와 함수로 스택 구현

## 함수
def isFull(): 
    return top == capacity - 1 

def isEmpty():
    return top == -1

def push(item):
    global top
    if isFull():
        print('overflow')
    else:
        top += 1 # top = top + 1
        array[top] = item

def pop():
    global top # top이라는 변수가 전역변수임
    if not isEmpty(): # if isEmpty() == False:
        top -= 1 # top = top - 1
        return array[top + 1]
    else:
        print('underflow')

def size():
    return top + 1

def peek():
    if not isEmpty():
        return array[top]
    else:
        print('underflow')
        



## 전역 변수
capacity = 10 # 스택이 가지는 최대 용량(크기)
array = [None] * capacity # 스택요소가 저장될 배열
top = -1


push("A")
push("B")
pop()
print(array)
