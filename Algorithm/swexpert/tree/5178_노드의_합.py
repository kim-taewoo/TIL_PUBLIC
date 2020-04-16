class BinaryTree:
    def __init__(self, N):
        self.nodes = [0] * (N + 1)
        self.N = N

    def put(self, num, value):
        self.nodes[num] = value

    def get_leaf(self, node):
        if node * 2 > N:
            self.sum += self.nodes[node]
        else:  # branch
            self.get_leaf(node * 2) 
            if node * 2 != N:
                self.get_leaf(node * 2 + 1)

    def my_result(self, L):
        self.sum = 0
        self.get_leaf(L)
        return self.sum


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = BinaryTree(N)
    for _ in range(M):
        num, value = map(int, input().split())
        tree.put(num, value)
    print('#{} {}'.format(t, tree.my_result(L)))
