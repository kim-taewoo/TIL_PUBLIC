def dfs(i, result):
    global maxi

    if result <= maxi:
        return

    if i == n:
        maxi = max(maxi, result)
        return

    for j in range(n):
        if not chk[j]:
            chk[j] = True
            dfs(i+1, result * board[i][j])
            chk[j] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(lambda x: int(x) * 0.01, input().split())) for _ in range(n)]
    maxi = -2147000000
    chk = [False for _ in range(n)]
    dfs(0, 1)
    print("#{} {:.6f}".format(t, maxi * 100))