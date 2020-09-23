def solution(n, computers):
    cnt = 0
    chk = [False for _ in range(n)]
    for i in range(n):
        if not chk[i]:
            q = [i]
            chk[i] = True
            while q:
                now = q.pop(0)
                for idx, j in enumerate(computers[now]):
                    if j and not chk[idx]:
                        q.append(idx)
                        chk[idx] = True
            cnt += 1
    return cnt

n = 3
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
print(solution(n, computers))
[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
