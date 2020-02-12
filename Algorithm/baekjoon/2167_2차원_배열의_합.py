n, m = map(int, input().split())
a = [[0] + list(map(int, input().split())) for _ in range(n)]
k = int(input())
a = [[0 for _ in range(m+1)]] + a
b = [[0 for _ in range(m+1)] for __ in range(n+1)]
for r in range(1,n+1):
    for c in range(1,m+1):
        b[r][c] = b[r-1][c] + b[r][c-1] - b[r-1][c-1] + a[r][c]


for x in range(k):
    i,j,x,y = map(int, input().split())

    print(b[x][y] - b[i-1][y] - b[x][j-1] + b[i-1][j-1])
