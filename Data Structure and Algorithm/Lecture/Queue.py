## 용량이 고정된 원형 큐 클래스 

class ArrayQueue:
    # constructor
    def __init__(self, capacity = 10): # 생성자 정의
        self.capacity = capacity # 용량(고정)
        self.array = [None] * capacity # 요소들을 저장할 배열
        self.front = 0 # 전단 인덱스
        self.rear = 0 # 후단 인덱스
    
    # method
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1) % self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass    

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else:
            pass

    def peek(self):
        if not self.isEmprt():
            return self.array[(self.front+1) % self.capacity] 
        else:
            pass

    def size(self):
        count = (self.rear - self.front + self.capacity) % self.capacity
        return count

    def display(self, msg):
        print(msg, end=" = [ ")
        for i in range(self.front+1, self.front+1 + self.size()):
            print(self.array[i%self.capacity], end=" ")
        print("]") 

    def clear(self):
        self.front = 0
        self.rear = 0    


# 5개의 크기를 가지는 큐 생성 => 1~5까지의 숫자를 큐에 각각 저장 => 큐 출력
#q = ArrayQueue(5)
#q.display("초기상태") 

#for i in range(1, 6): # while not q.isFull():
#    q.enqueue(i)
#q.display("포화 상태")

#rint("삭제 순서 ", end="") 
#for _ in range(5): # while not q.isEmpty()
#    print(q.dequeue(), end = " ")
