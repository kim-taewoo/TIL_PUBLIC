def dfs(level, total):
    global maxi
    global mini
    if level == len(numbers):
        if total > maxi:
            maxi = total
        if total < mini:
            mini = total

    for i in range(4):
        if opers[i]:
            opers[i] -= 1
            if i == 0:
                dfs(level+1, total+numbers[level])
            elif i == 1:
                dfs(level+1, total-numbers[level])
            elif i == 2:
                dfs(level+1, total*numbers[level])
            else:
                if total < 0:
                    dfs(level+1, -(-total // numbers[level]))
                else:
                    dfs(level+1, total // numbers[level])
            opers[i] += 1

T = int(input())
for t in range(1, T+1):
    n = int(input())
    opers = list(map(int, input().split()))
    numbers = list(map(int, input().split()))

    mini = 2147000000
    maxi = -2147000000

    dfs(1, numbers[0])

    print("#{} {}".format(t, maxi-mini))
