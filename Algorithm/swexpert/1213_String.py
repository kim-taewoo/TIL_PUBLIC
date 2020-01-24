for _ in range(1):
    t = int(input())

    sub = input()
    s = input()

    cnt = 0
    idx = s.find(sub)

    while idx != -1:
        print(idx)
        cnt += 1
        s = s[idx+1:]
        idx = s.find(sub)

    print("#{} {}".format(t, cnt))