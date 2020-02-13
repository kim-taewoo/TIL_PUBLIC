def dfs(now, big):
    global result
    if now > n:
        return
    if now == n:
        if big:
            result += 2 **big
        else:
            result += 1
        return
    dfs(now + 10, big)
    dfs(now + 20, big + 1)

T = int(input())
for t in range(1, T+1):
    result = 0
    n = int(input())
    dfs(0, 0)
    print("#{} {}".format(t, result))
