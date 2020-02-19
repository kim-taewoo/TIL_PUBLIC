def permu(level):
    if level == 7:
        print(*selected)
        return

    for i in range(7):
        if chk[i]: continue
        selected[level] = ll[i]
        chk[i] = 1
        permu(level+1)
        chk[i] = 0

ll = [x for x in range(1, 8)]
selected = [0 for _ in range(7)]
chk = [0 for _ in range(7)]
permu(0)