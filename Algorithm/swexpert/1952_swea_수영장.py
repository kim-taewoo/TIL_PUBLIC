def dfs(month, cost):
    global min_cost
    if month > 12:
        # 최소 비용 계산
        if cost < min_cost:
            min_cost = cost
        return
    if cost > min_cost:
        return
    if plan[month]:
        dfs(month+1, cost + plan[month] * d)
        dfs(month+1, cost + m)
        dfs(month+3, cost + t)
    else:
        dfs(month+1, cost)

T = int(input())
for tc in range(1, T+1):
    d,m,t,y = map(int, input().split())
    plan = [0] + list(map(int, input().split()))
    min_cost = y
    dfs(1, 0)
    print("#{} {}".format(tc, min_cost))