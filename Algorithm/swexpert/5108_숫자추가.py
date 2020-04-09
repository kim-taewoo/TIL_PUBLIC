class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodeCount = 0

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount-1:
            raise IndexError

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr
    
    def insertAt(self, pos, newNode):
        if pos < 0 or pos > self.nodeCount:
            raise IndexError

        if pos == 0:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount:
            self.tail = newNode

        self.nodeCount += 1
        return True

T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    l = LinkedList()
    a = list(map(int, input().split()))
    for i in range(len(a)):
        l.insertAt(i, Node(a[i]))
    for _ in range(M):
        idx, data = map(int, input().split())
        l.insertAt(idx, Node(data))
    print("#{} {}".format(t,l.getAt(L).data))

