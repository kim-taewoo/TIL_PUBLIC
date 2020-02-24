def dfs(level, cnt):
    global answer
    if cnt == m:
        survived = [chicken[x] for x in range(len(chicken)) if chk[x]]
        total = 0
        for i, j in house:
            mini = 2147000000
            for k, l in survived:
                dist = abs(i-k) + abs(j-l)
                if dist < mini:
                    mini = dist
            total += mini
        if total < answer:
            answer = total
        return

    if level == len(chicken):
        return

    dfs(level+1, cnt)
    chk[level] = True
    dfs(level+1, cnt + 1)
    chk[level] = False


n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

house = []
chicken = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 1:
            house.append((r, c))
        elif board[r][c] == 2:
            chicken.append((r, c))

answer = 2147000000
chk = [False for _ in range(len(chicken))]
dfs(0, 0)

print(answer)