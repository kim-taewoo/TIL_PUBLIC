T = int(input())

for t in range(1, T+1):
    a = list(map(int, input().split()))

    total = 0
    for i in a:
        if i <= 40 :
            total += 40
        else:
            total += i

    result = total // 5

    print("#{} {}".format(t, result))