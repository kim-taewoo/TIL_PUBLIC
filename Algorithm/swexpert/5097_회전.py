T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    q = list(map(int, input().split()))
    for i in range(m):
        first = q.pop(0)
        q.append(first)
    print("#{} {}".format(t, q[0]))
