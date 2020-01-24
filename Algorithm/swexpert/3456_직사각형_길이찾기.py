T = int(input())

for t in range(1, T+1):
    a = list(map(int, input().split()))
    d = {}
    for i in a:
        d[i] = d.get(i, 0) + 1

    result = -1
    for i in d:
        if d[i] % 2:
            result = i
            break
    print("#{} {}".format(t, result))