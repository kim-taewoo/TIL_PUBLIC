def sol(k):
    if k == 1:
        return n

    return n * sol(k - 1)

for _ in range(10):
    t = int(input())
    n, k = map(int, input().split())
    result = sol(k)

    print("#{} {}".format(t, result))