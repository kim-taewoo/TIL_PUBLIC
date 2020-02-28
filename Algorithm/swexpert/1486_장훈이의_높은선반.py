def dfs(level, total):
    global mini
    if level == len(hs):
        if total >= b:
            if total < mini:
                mini = total
        return

    if total >= mini:
        return

    dfs(level+1, total)
    dfs(level+1, total + hs[level])


T = int(input())
for t in range(1, T+1):
    n, b = map(int, input().split())
    hs = list(map(int, input().split()))
    mini = 2147000000
    dfs(0, 0)
    print("#{} {}".format(t, mini - b))
