def sol(cnt, sum, cur_i):
    if cnt == 0:
        result.add(sum)
        return

    for i in range(cur_i + 1, len(a)):
        sum += a[i]
        sol(cnt-1, sum, i)
        sum -= a[i]


T = int(input())

for t in range(1,T+1):
    a = list(map(int, input().split()))
    result = set()

    sol(3, 0, -1)

    print("#{} {}".format(t, sorted(result)[-5]))