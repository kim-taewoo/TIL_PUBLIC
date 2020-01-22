T = int(input())

for t in range(1, T+1):
    n = int(input())
    result = ""
    for _ in range(n):
        c, k = input().split()
        result += c * int(k)

    print("#{}".format(t))

    for idx, i in enumerate(result, start = 1):
        print(i, end="")
        if not idx % 10:
            print()
    print()