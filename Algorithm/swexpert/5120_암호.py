class Node:
    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None

    def traverse(self):
        result = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            result.append(curr.data)
        return result

    def reverseTraverse(self, n=1e9):
        result = []
        curr = self.tail
        i = 1
        while curr.prev.prev and i <= n:
            curr = curr.prev
            result.append(curr.data)
            i += 1
        return result

    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            raise IndexError

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True

    def insertBefore(self, next, newNode):
        prev = next.prev
        newNode.next = next
        newNode.prev = prev
        next.prev = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True

    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            raise IndexError

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)

    def popAfter(self, prev):
        curr = prev.next
        next = curr.next
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popBefore(self, next):
        curr = next.prev
        prev = curr.prev
        prev.next = next
        next.prev = prev
        self.nodeCount -= 1
        return curr.data

    def popAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            raise IndexError
        curr = self.getAt(pos)
        return self.popAfter(curr.prev)

    def findBigger(self, num):
        curr = self.head
        while curr.next.next:
            curr = curr.next
            if curr.data > num:
                return curr
        return self.tail

    def concatAtEnd(self, L):
        self.tail.prev.next = L.head.next
        L.head.next.prev = self.tail.prev
        self.tail = L.tail
        self.nodeCount += L.nodeCount
        return True

    def concatBefore(self, curr, L):
        if curr.next == None:
            return self.concatAtEnd(L)
        else:
            prev = curr.prev
            prev.next = L.head.next
            L.head.next.prev = prev
            L.tail.prev.next = curr
            curr.prev = L.tail.prev
            self.nodeCount += L.nodeCount
            return True


T = int(input())
for t in range(1, 1 + T):
    N, M, K = map(int, input().split())
    ll = DoublyLinkedList()
    for idx, i in enumerate(map(int, input().split()), start=1):
        ll.insertAt(idx, Node(i))

    target = ll.getAt(1)
    for _ in range(K):
        for i in range(M):
            if not target.data:
                target = ll.getAt(1)
            target = target.next
        if not target.data:
            val1 = ll.getAt(1).data
        else:
            val1 = target.data
        ll.insertBefore(target, Node(val1 + target.prev.data))
        target = target.prev

    answer = ll.reverseTraverse(10)
    answer = " ".join(map(str, answer))
    print("#{} {}".format(t, answer))
