n, k = map(int, input().split())
dp_map = [0 for _ in range(k+1)]
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, w-1, -1):
        if dp_map[i-w] + v > dp_map[i]:
            dp_map[i] = dp_map[i-w] + v
print(dp_map[-1])
