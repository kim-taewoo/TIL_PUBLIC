def dfs(day, money):
    if day > n:
        return
    money_date[day] = money
    dfs(day+1, money)
    if money_date[day+a[day][0]-1] < money + a[day][1]:
        dfs(day + a[day][0] - 1, money + a[day][1])

n = int(input())
a = [0] + [list(map(int, input().split())) for _ in range(n)]
money_date = [0 for _ in range(n+1)]
dfs(1, 0)
print(max(money_date))