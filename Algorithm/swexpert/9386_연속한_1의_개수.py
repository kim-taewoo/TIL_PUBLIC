T = int(input())
for t in range(1, T+1):
    n = int(input())
    num = int(input())
    maxi = 0
    con = 0
    while num > 0:
        num, r = divmod(num, 10)
        if r:
            con += 1
        else:
            if con > maxi:
                maxi = con
            con = 0
    if con > maxi:
        maxi = con
    print("#{} {}".format(t, maxi))
