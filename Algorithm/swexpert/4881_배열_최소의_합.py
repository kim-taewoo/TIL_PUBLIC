def dfs(row_level, ssum):
    global min_ssum
    if ssum >= min_ssum: # 가지치기
        return
    if row_level == n:
        if ssum < min_ssum:
            min_ssum = ssum
        return
    for c in range(n):
        if not chk[c]:
            chk[c] = True
            dfs(row_level+1, ssum + board[row_level][c])
            chk[c] = False

for t in range(1, int(input())+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    chk = [False for _ in range(n)]
    min_ssum = 2147000000
    dfs(0,0)
    print("#{} {}".format(t, min_ssum))