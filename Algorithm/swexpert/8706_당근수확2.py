T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = [0] + list(map(int, input().split()))

    dist = 0
    capa = 0
    for i in range(1, n+1):
        while a[i]:
            a[i] -= 1
            capa += 1
            if capa == m:
                dist += i * 2
                capa = 0
    if capa:
        dist += i * 2

    print("#{} {}".format(t, dist))