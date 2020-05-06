import sys
sys.setrecursionlimit(10000000)

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
    
    def insert(self, key, data):
        if key < self.key:
            if self.left:
                self.left.insert(key, data)
            else:
                self.left = Node(key, data)
        else:
            if self.right:
                self.right.insert(key, data)
            else:
                self.right = Node(key, data)

    def preorder(self):
        lst = []
        lst.append(self.data)
        l = self.left.preorder() if self.left else []
        r = self.right.preorder() if self.right else []
        return lst + l + r
    
    def postorder(self):
        l = self.left.postorder() if self.left else []
        r = self.right.postorder() if self.right else []
        lst = l + r
        lst.append(self.data)
        return lst



class BinBinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, data):
        if self.root:
            self.root.insert(key, data)
        else:
            self.root = Node(key, data)
    
    def preorder(self):
        if self.root:
            return self.root.preorder()
        else:
            return []
    
    def postorder(self):
        if self.root:
            return self.root.postorder()
        else:
            return []


def solution(nodeinfo):
    nodeinfo = sorted([[idx, *i] for idx, i in enumerate(nodeinfo, start = 1)], key=lambda x:x[2], reverse=True)

    btree = BinBinaryTree()
    for i in nodeinfo:
        btree.insert(i[1],i[0])
    
    answer = []
    answer.append(btree.preorder())
    answer.append(btree.postorder())
    return answer

# x 값은 모두 다르고, y 값은 같은 레벨끼리 같다.
# 자식의 y 값은 항상 부모보다 작다.
# 왼쪽 서브트리의 x 값은 부모 x값보다 작다. 
# 오른쪽은 크다.
# 즉 x 가 key 라고 생각하면 된다. y 는 걍 level 이다.
# y 를 정렬해서 삽입순서로 하면 되지 않을까 싶다.
nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5],
            [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]

print(solution(nodeinfo))
