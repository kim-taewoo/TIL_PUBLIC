import heapq


def solution(operations):
    Q = []
    for i in operations:
        command, num = i.split()
        num = int(num)

        if command == 'I':
            heapq.heappush(num)
        else:
            if not Q:
                continue
            if num == 1:
                Q.remove(max(Q))
            else:
                heapq.heappop(Q)
    if not Q:
        return [0, 0]
    return [max(Q), Q[0]]


operations = ["I 7", "I 5", "I -5", "D -1"]
print(solution(operations))
