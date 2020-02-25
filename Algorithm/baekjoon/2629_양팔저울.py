def dfs(level, ssum):
    if level == n:  # 종료조건 1
        comb_weights[ssum] = 1
        return

    chk = dp.get(level, [])
    if ssum in chk:  # 종료조건 2
        return
    else:
        dp[level] = chk + [ssum]  # 메모라이제이션

    if ssum + sum(weights[level:]) <= 0:  # 종료조건3 (불필요?)
        return

    # 가지뻗기
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
