T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, list(input()))) for _ in range(n)]

    half = n//2
    total = sum(sum(a[x]) for x in range(n))
    for r in range(half):
        for c in range(half - r):
            total -= a[r][c]
            total -= a[r][-c-1]
            total -= a[n-1-r][c]
            total -= a[n-1-r][-c-1]
    print("#{} {}".format(t, total))