T = int(input())

for t in range(1, T+1):
    n = int(input())

    distances = list(map(abs, map(int,input())))

    min_v = 100001
    cnt = 0
    for d in distances:
        if d < min_v:
            min_v = d
            cnt = 1
        elif d == min_v:
            cnt += 1
    print("#{} {} {}".format(t, min_v, cnt))