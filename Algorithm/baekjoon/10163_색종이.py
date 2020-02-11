n = int(input())

a = [[0 for _ in range(101)] for __ in range(101)]

for x in range(1, n+1):
    c, r, w, h = map(int, input().split())
    r = 100 - r
    for i in range(r - h + 1, r+1):
        for j in range(c, c + w):
            a[i][j] = x

cnts = [0 for _ in range(n+1)]
for i in range(101):
    for j in range(101):
        cnts[a[i][j]] += 1

for i in cnts[1:]:
    print(i)
