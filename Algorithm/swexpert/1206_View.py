T = 10

for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    result = 0
    for i in range(n):
        if i < 2 or i > n - 3: continue

        tallest = max(a[i-2:i] + a[i+1:i+3])

        if tallest < a[i]:
            result += (a[i] - tallest)

    print("#{} {}".format(t, result))