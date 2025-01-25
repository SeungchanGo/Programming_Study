# 클래스를 사용하여 스택 구현

class ArrayStack:
    # 생성자
    def __init__(self, capacity):
        self.capacity = capacity # 스택의 최대용량
        self.array = [None]*self.capacity # 요소를 가지는 스택
        self.top = -1 # 스택 상단에 있는 요소의 인덱스

    def isFull(self):
        return self.top == self.capacity - 1
    
    def isEmpty(self):
        return self.top == -1
    
    def push(self, item):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = item
        else:
            print("overflow")

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]         
        else:
            print("underflow")

    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            pass

    def size(self):
        return self.top + 1
    
    def clear(self):
        self.top = -1

    def display(self):
        print("[ ", end="")
        for i in range(0, self.top+1):
            print(self.array[i], end=" ")
        print("]")     

## 20개의 요소를 저장하는 스택 객체 선언
##s = ArrayStack(20)
##
## 사용자로부터 문자열을 입력받아 글자 하나씩 스택에 저장
##msg = input("문자열 입력 : ")
##for c in msg:
##    s.push(c)
##
## 스택에 있는 요소를 꺼내 출력
##print("문자열 출력 : ", end = "")
##while not s.isEmpty():
##    print(s.pop(), end = "")
##print()
  
    
        

