class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.next = next
        self.prev = prev

    def append(self, node):
        if node is not None:
            node.next = self.next
            node.prev = self
            if node.next is not None:
                node.next.prev = node
            self.next = node

    def popNext(self):
        node = self.next
        if node is not None:
            self.next = node.next
            if self.next is not None:
                self.next.prev = self
        return node
    

    def getNode(self, pos):
        if pos < 0: 
            return None
        ptr = self.head
        for i in range(pos):
            if ptr == None:
                return None
            ptr = ptr.link
        return ptr
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None:
            return None
        else:
            return node.data
            
class DbLinkedList:
    def __init__(self):
        self.head = None

    # 삽입연산: 머리노드(0번 위치)로 삽입 or 중간에 삽입 or 마지막 삽입
    def insert(self, pos, elem):
        node = DNode(elem)
        before = self.getNode(pos-1)
        if before == None: # 머리노드로 삽입하는 경우
            node.next = self.head
            if node.next is not None:
                node.next.prev = node
            self. head = node
        else:
            before.append(node)

    # 삭제연산: 머리노드를 삭제 or 중간 삭제 or 마지막 삭제
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None: # 머리노드를 삭제하는 경우
            if self.head is not None:
                self.head = self.head.next
                self.head.prev = None
        else:
            before.popNext()



