T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    result = sum(sorted(a, reverse = True)[:k])
    print("#{} {}".format(t, result))