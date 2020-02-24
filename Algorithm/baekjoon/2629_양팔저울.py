def dfs(level, ssum):
    if level == n:
        comb_weights[ssum] = 1
        return

    chk = dp.get(level, [])
    if ssum in chk:
        return
    else:
        dp[level] = chk + [ssum]

    if ssum + sum(weights[level:]) <= 0:
        return

    dfs(level+1, ssum)
    dfs(level+1, ssum - weights[level])
    dfs(level+1, ssum + weights[level])


n = int(input())
weights = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

dp = {}
comb_weights = {}
dfs(0, 0)

result = []
for i in targets:
    if comb_weights.get(i, 0):
        result.append('Y')
    else:
        result.append('N')
print(*result)
