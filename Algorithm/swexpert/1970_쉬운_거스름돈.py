T = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(1, T+1):
    n = int(input())

    print("#{}".format(t))
    for m in money:
        cnt = 0
        while n >= m:
            n -= m
            cnt += 1
        print("{}".format(cnt), end=" ")
    print()
