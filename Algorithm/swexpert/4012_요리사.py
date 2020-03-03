def dfs(level, cnt):
    global min_diff
    if level == n:
        return
    if cnt == n // 2:
        comb1 = [i for i in range(n) if selected[i]]
        comb2 = [i for i in range(n) if not selected[i]]
        comb1_sum = 0
        for x in range(cnt):
            for y in range(x+1, cnt):
                comb1_sum += board[comb1[x]][comb1[y]]
                comb1_sum += board[comb1[y]][comb1[x]]

        comb2_sum = 0
        for x in range(cnt):
            for y in range(x+1, cnt):
                comb2_sum += board[comb2[x]][comb2[y]]
                comb2_sum += board[comb2[y]][comb2[x]]
        diff = abs(comb1_sum - comb2_sum)

        min_diff = min(min_diff, diff)
        return

    dfs(level+1, cnt)
    selected[level] = True
    dfs(level+1, cnt + 1)
    selected[level] = False


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    min_diff = 2147000000
    selected = [False] * n
    dfs(0, 0)
    print("#{} {}".format(t, min_diff))
