T = int(input())

for t in range(1,T+1):
    n, m = map(int, input().split())

    a = [[0] * n for _ in range(n)]

    for i in range(m):
        x, y = map(int, input().split())
        a[x-1][y-1] = 1
        a[y-1][x-1] = 1
    
    result = 0
    for i in range(n):
        tmp = []
        for j in range(n):
            if a[i][j]:
                tmp.append(j)
        for j in tmp:
            for k in tmp:
                if a[j][k]:
                    result += 1

    result //= 6
    print("#{} {}".format(t, result))


