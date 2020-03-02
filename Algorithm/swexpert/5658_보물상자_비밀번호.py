T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    board = input()
    side_n = n // 4
    ss = set()
    for l in range(side_n):
        for i in range(4):
            start = side_n*i + l
            ss.add(int("".join([board[(start+j) % n]
                                for j in range(side_n)]), 16))
    print("#{} {}".format(t, sorted(ss)[-k]))
