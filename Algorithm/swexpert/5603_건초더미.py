T = int(input())

for t in range(1,T+1):
    n = int(input())
    a = sorted([int(input()) for _ in range(n)])
    avg = sum(a) / n
    cnt = 0
    j = n-1
    for i in range(n):
        if a[i] < avg:
            diff = avg - a[i]
            while diff > 0:
                remain = a[j] - avg
                if remain >= diff:
                    a[j] -= diff
                    a[i] = avg
                    cnt += diff
                    diff = 0
                else:
                    diff -= remain
                    a[j] = avg
                    a[i] += remain
                    j -= 1
                    cnt += remain
    print("#{} {}".format(t, int(cnt)))