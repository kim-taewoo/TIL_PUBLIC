T = int(input())

for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))

    max_result = 0
    for i in range(n):
        for j in range(i+1, n):
            r = str(ns[i] * ns[j])
            if len(r) >= 2:
                flag = True
                for k in range(1, len(r)):
                    if not r[k] >= r[k-1]:
                        flag = False
                        break
                if flag:
                    if int(r) > max_result:
                        max_result = int(r)

    if max_result == 0:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))
            