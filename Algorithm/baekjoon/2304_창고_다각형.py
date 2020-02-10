n = int(input())

a = sorted([list(map(int, input().split())) for _ in range(n)])
maxi = max(a, key=lambda x: x[1])
maxi_idx = a.index(maxi)

result = maxi[1]
print(a)
height = 0
for i in range(maxi_idx):
    if a[i][1] > height:
        height = a[i][1]
    print(height, (a[i+1][0] - a[i][0]))
    result += (a[i+1][0] - a[i][0]) * height
height = 0
for i in range(-1, maxi_idx-n, -1):
    if a[i][1] > height:
        height = a[i][1]
    print(height, (a[i][0]+1 - (a[i-1][0]+1)))
    result += (a[i][0]+1 - (a[i-1][0]+1)) * height
print(result)
