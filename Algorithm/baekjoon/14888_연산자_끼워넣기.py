def dfs(level, total):
    global maxi
    global mini

    if level == n-1:
        if total > maxi:
            maxi = total
        if total < mini:
            mini = total
        return

    for i in range(4):
        if opers[i] > 0:
            opers[i] -= 1
            if i == 0:
                dfs(level+1, total + a[level+1])
            elif i == 1:
                dfs(level+1, total - a[level+1])
            elif i == 2:
                dfs(level+1, total * a[level+1])
            elif i == 3:
                if total < 0:
                    q = (-1) * (abs(total) // a[level+1])
                else: 
                    q = total // a[level + 1]
                dfs(level+1, q)
            opers[i] += 1


n = int(input())
a = list(map(int, input().split())) 
opers = list(map(int, input().split()))
mini = 2147000000
maxi = -2147000000

dfs(0, a[0])

print(maxi)
print(mini)