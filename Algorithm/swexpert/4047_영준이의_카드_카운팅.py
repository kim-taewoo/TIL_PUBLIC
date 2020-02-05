T = int(input())
for t in range(1, T+1):
    chk = [[False] * 14 for _ in range(4)]
    s = input()
    length = len(s)
    flag = True
    i = 0
    while i < length:
        num = int(s[i+1:i+3])
        if s[i] == 'S':
            if chk[0][num]:
                flag = False
                break
            else: chk[0][num] = True
        elif s[i] == 'D':
            if chk[1][num]:
                flag = False
                break
            else: chk[1][num] = True
        elif s[i] == 'H':
            if chk[2][num]:
                flag = False
                break
            else: chk[2][num] = True
        else:
            if chk[3][num]:
                flag = False
                break
            else: chk[3][num] = True
        i += 3
    if not flag:
        print("#{} {}".format(t, "ERROR"))
    else:
        result = " ".join(map(str, [sum(1 for j in i[1:] if not j) for i in chk])) 
        print("#{} {}".format(t, result))