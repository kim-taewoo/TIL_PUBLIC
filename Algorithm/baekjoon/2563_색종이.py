n = int(input())
a = [[0 for _ in range(101)] for __ in range(101)]
for x in range(n):
    c, r = map(int, input().split())
    r = 100 - r
    for i in range(r - 10 + 1, r+1):
        for j in range(c, c+10):
            a[i][j] = 1

cnt = 0
for i in range(101):
    for j in range(101):
        if a[i][j]:
            cnt += 1
print(cnt)
