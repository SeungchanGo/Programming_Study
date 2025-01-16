class Node:
    def __init__(self, elem):
        self.data = elem # 데이터 멤버 생성 및 초기화
        self.link = None # 링크 생성 및 초기화

    def append(self, node):
        if node is not None: # 삽입할 노드가 None이 아니면
            node.link = self.link
            self.link = node

    def popNext(self):
        next = self.link # 현재 노드의 다음 노드
        if next is not None: # next가 None이 아니면
            self.link = next.link
        return next # 다음 노드를 반환
    

class LinkedList:
    def __init__(self):
        self.head = None # head 선언 및 None으로 초기화

    def isEmpty(self):
        return self.head == None 
        
    def isFull(self):
        return False

    def getNode(self, pos):
        if pos < 0: # 잘못된 위치 > None 반환
            return None
        
        ptr = self.head # 시작 위치 > head 
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link    
        return ptr # 최종 노드를 반환

    def getEntry(self, pos):
        node = self.getNode(pos) # pos번째 노드를 수함

        if node is None: # 해당 노드가 없는 경우
            return None
        return node.data # 있는 경우 필드를 반환

    def insert(self, pos, elem):
        node = (elem, None) # 삽입할 새로운 노드를 만듬
        before = self.getNode(pos-1) # 삽입할 위치 이전 노드를 탐색

        if before == None: # before이 None이면 맨 앞에 추가 
            node.link = self.head.link
            self.head = node
        else:
            before.append(node) # 아닌 경우: before 뒤에 추가   

    def delete(self, pos):
        before = self.getNode(pos-1) # 삽입할 위치 이전 노드 탐색

        if before == None: # 머리 노드를 삭제하면 head가 다음 노드로 변경됨
            before = self.head
            if self.head is not None:
                self.head = self.head.link
            return before
        
        else:
            return before.popNext() # before의 다음 노드 삭제

    def size(self):
        ptr = self.head
        count = 0
        while ptr is not None:
            ptr = ptr.link
            count += 1
        return count

