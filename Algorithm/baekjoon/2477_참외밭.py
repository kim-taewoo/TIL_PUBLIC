k = int(input())

a = [list(map(int, input().split())) for _ in range(6)] * 2

for i in range(12):
    if a[i][0] == a[i+2][0] and a[i+1][0] == a[i+3][0]:
        square = a[i+1][1] * a[i+2][1]
        result = (a[i][1] + a[i+2][1]) * (a[i+1][1] + a[i+3][1]) - square
        break
print(result * k)