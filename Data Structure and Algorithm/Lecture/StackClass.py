class ArrayStack :
    def __init__( self, capacity ):	    # 생성자 정의
        self.capacity = capacity		    # 용량(고정)
        self.array = [None]*self.capacity	# 요소들을 저장할 배열
        self.top = -1			            # 스택 상단의 인덱스


    def isEmpty( self ) : return self.top == -1
    def isFull( self ) : return self.top == self.capacity-1

    def push( self, item ):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = item
        else: pass              # overflow 예외는 처리하지 않았음

    def pop( self ):
        if not self.isEmpty():
            self.top -= 1
            return self.array[self.top+1]
        else: pass              # underflow 예외는 처리하지 않았음

    def peek( self ):
        if not self.isEmpty():
            return self.array[self.top]
        else: pass              # underflow 예외는 처리하지 않았음

    def size(self) : return self.top + 1

    def clear(self):
        self.top = -1

    def display(self):
        print("[ ", end="")
        for i in range(0, self.top+1):
            print(self.array[i], end=" ")
        print("]")        



