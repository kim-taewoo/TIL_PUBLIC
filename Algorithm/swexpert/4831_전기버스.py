T = int(input())
for t in range(1, T+1):
    k, n, m = map(int, input().split())
    a = list(map(int, input().split()))
    cnt = 0
    i = 0
    dis = k
    while i+dis < n:
        if dis <= 0:
            cnt = 0
            break
        if i+dis in a:
            i += dis
            cnt += 1
            dis = k
        else:
            dis -= 1
    print("#{} {}".format(t, cnt))
