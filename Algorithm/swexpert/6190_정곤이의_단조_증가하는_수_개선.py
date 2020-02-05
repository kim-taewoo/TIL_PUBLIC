T = int(input())

for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))

    max_result = 0
    for i in range(n):
        for j in range(i+1, n):
            m = ns[i] * ns[j]
            tmp = m
            if tmp >= 10:
                flag = True
                while tmp > 0:
                    tmp, r = divmod(tmp, 10)
                    if not tmp % 10 <= r:
                        flag = False
                        break
                if flag:
                    if m > max_result:
                        max_result = m

    if max_result == 0:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))
            