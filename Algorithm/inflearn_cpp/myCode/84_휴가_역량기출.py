def dfs(day, money):
    global max_money
    if day > n:
        if day == n+1:
            if money > max_money:
                max_money = money
        return
    if day + a[day][0] <= n+1:
        dfs(day + a[day][0], money + a[day][1]) # 선택 o
    else:
        if money > max_money :
            max_money = money
        return
    dfs(day + 1, money) # 선택 x


n = int(input())
a = [0] + [list(map(int, input().split())) for _ in range(n)]
max_money = 0
dfs(1, 0)
print(max_money)