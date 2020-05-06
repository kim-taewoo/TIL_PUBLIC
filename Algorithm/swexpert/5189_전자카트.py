def dfs(cnt, now, cost):
    global mini

    if cnt == n-1:
        cost += board[now][0]
        mini = min(cost, mini)
        return
    
    for i in range(1, n):
        if not chk[i]:
            chk[i] = 1
            dfs(cnt + 1, i, cost + board[now][i])
            chk[i] = 0


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    mini = 1e9
    chk = [0 for _ in range(n)]
    dfs(0, 0, 0)
    print("#{} {}".format(t, mini))
