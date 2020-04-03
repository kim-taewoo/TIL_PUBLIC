T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    q = []
    remains = []
    for idx, el in enumerate(a, start=1):
        if idx <= n:
            q.append([idx, el])
        else:
            remains.append([idx, el])
    while len(q) > 1:
        print(q)
        print(remains)
        now = q.pop(0)
        now[1] //= 2
        if not now[1] and remains:
            q.append(remains.pop(0))
        elif now[1]:
            q.append(now)
    print("#{} {}".format(t, q[0][0]))
