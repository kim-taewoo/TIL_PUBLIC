class Node:

    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None

    def size(self):
        l = self.left.size() if self.left else 0
        r = self.right.size() if self.right else 0
        return l + r + 1


T = int(input())
for t in range(1, T+1):
    E, N = map(int, input().split())
    nodes = [Node(i) for i in range(E+2)]
    L = list(map(int, input().split()))
    for i in range(E):
        idx = 2 * i
        parent, child = nodes[L[idx]], nodes[L[idx+1]]
        if parent.left:
            parent.right = child
        else: parent.left = child

    print("#{} {}".format(t, nodes[N].size()))
