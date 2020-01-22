T = int(input())
for i, c in enumerate(range(T), start=1):
    t = input()
    s = "0"
    count = 0
    for j in t:
        if j != s:
            count += 1
            s = j
    print('#{} {}'.format(i, count))
