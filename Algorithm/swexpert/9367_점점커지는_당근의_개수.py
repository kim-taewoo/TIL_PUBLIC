T = int(input())

for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    max_cnt = 1
    cnt = 1
    for i in range(1,n):
        if a[i] > a[i-1]:
            cnt += 1
        else:
            if cnt > max_cnt:
                max_cnt = cnt
            cnt = 1
    if cnt > max_cnt:
        max_cnt = cnt
    print("#{} {}".format(t, max_cnt))