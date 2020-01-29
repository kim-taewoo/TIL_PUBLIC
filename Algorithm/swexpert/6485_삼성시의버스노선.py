T = int(input())

for t in range(1, T+1):
    n = int(input())
    b_route = [list(map(int, input().split())) for _ in range(n)]
    p = int(input())
    stations = [int(input()) for _ in range(p)]

    print("#{}".format(t), end="")
    for s in stations:
        cnt = 0
        for b in b_route:
            if b[0]<= s <=b[1]:
                cnt += 1
        print(" {}".format(cnt), end="")

    print()

