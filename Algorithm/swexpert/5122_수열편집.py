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

    def popAt(self, pos):
        if pos < 0 or pos > self.nodeCount-1:
            raise IndexError

        if pos == 0:
            curr = self.head
            self.head = self.head.next
            if self.nodeCount == 1:
                self.tail = None
        else:
            prev = self.getAt(pos-1)
            curr = prev.next
            prev.next = curr.next
            if pos == self.nodeCount-1:
                self.tail = prev

        self.nodeCount -= 1
        return curr.data

    def changeAt(self, pos, data):
        node = self.getAt(pos)
        node.data = data


T = int(input())
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    l = LinkedList()
    a = list(map(int, input().split()))
    for i in range(len(a)):
        l.insertAt(i, Node(a[i]))
    for _ in range(M):
        cmd = input().split()
        if cmd[0] == 'D':
            l.popAt(int(cmd[1]))
        elif cmd[0] == 'C':
            l.changeAt(int(cmd[1]), int(cmd[2]))
        else:
            l.insertAt(int(cmd[1]), Node(int(cmd[2])))

    try:
        answer = l.getAt(L).data
    except:
        answer = -1
    print("#{} {}".format(t, answer))
