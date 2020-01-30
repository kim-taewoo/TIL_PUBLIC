T = int(input())    

for t in range(1, T+1):
    n, l = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    a = sorted(a, key=lambda x: x[1])

    d = {}
    for t, k in a:
        d[k] = d.get(k, 0) + t
