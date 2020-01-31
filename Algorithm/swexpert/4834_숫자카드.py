T = int(input())
for t in range(1, T+1):
    n = int(input())
    digits = input()
    d = {}
    for i in digits:
        d[i] = d.get(i, 0) + 1
    d = sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)
    print("#{} {} {}".format(t, d[0][0], d[0][1]))