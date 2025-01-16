# 이진 탐색 트리를 위한 노드
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
         # (키, 값)
         return f"({self.key},{self.value})"    


# 이진탐색 트리의 탐색연산(순환구조)
def search_bst(n, key):
        if n == None: # 탐색실패
            return None 
        elif key == n.key: # 탐색성공
            return n
        elif key < n.key:
            return search_bst(n.left, key)
        else:
            return search_bst(n.right, key)    
        

# 이진탐색 트리의 값을 이용한 탐색연산(전위순회)
def search_value_bst(n, value):
        if n == None: # 탐색실패
            return None
        elif value == n.value: # 탐색성공
            return n
        res = search_value_bst(n.left, value)
        if res is not None:
            return res
        else:
            return search_value_bst(n.right, value)


# 이진탐색 트리의 삽입연산
def insert_bst(root, node):
    if root == None:
        return node
    if node.key == root.key:
        return root         
    if node.key < root.key:
        root.left = insert_bst(root.left, node)
    else:
        root.right = insert_bst(root.right, node)
    return root

def preorder(n):
    if n is not None:
        print("{", end="")
        print(n, end="")
        preorder(n.left)
        preorder(n.right)
        print("}", end="")

def print_tree(msg, r):
    print(msg, end="")
    preorder(r)
    print()

# 노드 출력 함수
def print_node(msg, n):
    print(msg, n if n!= None else "탐색실패")


# 이진탐색 트리의 삭제 연산
def delete_bst (root, key):
    if root == None:
        return root
    
    if key < root.key:
        root.left = delete_bst(root.left, key)
    elif key > root.key:
        root.right = delete_bst(root.right, key)

    else:
        if root.left == None:
            return root.right

        if root.right == None:
            return root.left

        succ = root.right
        while succ.left != None:
            succ = succ.left

        root.key = succ.key
        root.value = succ.value
        root.right = delete_bst(root.right, succ.key)

    return root    



data = [(6, "여섯"), (8, "여덟"), (2, "둘"), (4, "넷"), (7, "일곱"), (5, "다섯")]

root = None

# 삽입연산
for i in range(0, len(data)):
    root = insert_bst(root, BSTNode(data[i][0], data[i][1]))

print_tree("최초 이진탐색 트리:", root)    


# 탐색연산
n = search_bst(root, 2)
print_node("search 2:", n)

n = search_bst(root, 10)
print_node("search 10:", n)

n = search_value_bst(root, "넷")
print_node("search 4:", n)

n = search_value_bst(root, "열")
print_node("search 10", n)


# 삭제연산
root = delete_bst(root, 7); print_tree("del 7: ", root)
root = delete_bst(root, 8); print_tree("del 8: ", root)
root = delete_bst(root, 2); print_tree("del 2: ", root)
root = delete_bst(root, 6); print_tree("del 6: ", root)

print("---------------------------------------------")

root2 = None
data2 = [35, 24, 16, 31 ,53, 67, 43, 87, 55, 9]
for i in range(0, len(data2)):
    root2 = insert_bst(root2, BSTNode(data2[i][0], data2[i][1]))

print_tree("최초 이진탐색 트리:", root2)
root2 = delete_bst(root2, 55); print_tree("del 9: ", root2)
root2 = delete_bst(root2, 16); print_tree("del 9: ", root2)
root2 = delete_bst(root2, 53); print_tree("del 9: ", root2)