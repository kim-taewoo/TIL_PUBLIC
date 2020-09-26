def solution(n, edge):
    dic = {}
    for s, e in edge:
        dic[s] = dic.get(s, []) + [e]
        dic[e] = dic.get(e, []) + [s]
    answer = 0
    chk = [False for _ in range(n+1)]
    chk[1] = True
    q = []
    for node in dic[1]:
        q.append(node)
        chk[node] = True
    while q:
        answer = len(q)
        for _ in range(len(q)):
            node = q.pop(0)
            for nextNode in dic[node]:
                if not chk[nextNode]:
                    chk[nextNode] = True
                    q.append(nextNode)
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))
