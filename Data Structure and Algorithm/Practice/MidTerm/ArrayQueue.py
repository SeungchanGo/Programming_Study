class ArrayQueue:
    # constructor
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0

    # method
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear+1)%self.capacity

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%self.capacity
            self.array[self.rear] = item
        else:
            pass

    def enqueue2(self, item): # 링 버퍼
        self.rear = (self.rear + 1) % self.capacity
        self.array[self.rear] = item
        if self.isEmpty():
            self.front =  (self.front + 1) % self.capacity    

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%self.capacity
            return self.array[self.front]
        else:
            pass
        
        
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front+1)%self.capacity]
        else:
            pass

    def size(self):
        count = (self.rear - self.front + self.capacity) % self.capacity
        return count
    
    def display(self, msg):
        print(msg + '[ ', end="")
        for i in range(self.front+1, self.front+1 + self.size()):
            print(self.array[i%self.capacity], end=" ")
        print(']')
            
    def clear(self):
        self.front = 0
        self.rear = 0       


# 링 버퍼 테스트
if __name__ == "__main__":
    q = ArrayQueue(8)
    q.display("초기상태 큐:")

    for i in range(6):
        q.enqueue2(i)

    q.display("삽입 0~5후 큐:")

    q.enqueue2(6)
    q.enqueue2(7)
    q.display("삽입 6~8후 큐:")

    q.enqueue2(8)
    q.enqueue2(9)
    q.display("삽입 8~9후 큐")        

    q.dequeue(); q.dequeue()
    q.display("삭제 x2")