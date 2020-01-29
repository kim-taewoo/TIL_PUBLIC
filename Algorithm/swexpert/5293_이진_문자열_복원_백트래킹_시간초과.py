def sol(cur_i):
    global tmp
    global found
    global result

    if found: return

    if cur_i == length:
        s = "".join(tmp)
        subs = [0,0,0,0]
        for i in range(len(s)-1):
            sub = s[i:i+2]
            if sub == '00':
                subs[0] += 1
            elif sub == '01':
                subs[1] += 1
            elif sub == '10':
                subs[2] += 1
            elif sub == '11':
                subs[3] += 1
        if subs[0] == a and subs[1] == b and subs[2] == c and subs[3] == d:
            found = True
            result = s
        return

    for i in '01':
        tmp.append(i)
        sol(cur_i + 1)
        tmp.pop()


T = int(input())


for t in range(1, T+1):
    d = {}
    a,b,c,d = map(int, input().split())

    length = (a+b+c+d) * 2 - ((a+b+c+d) - 1)

    found = False
    result = ''
    tmp = []
    sol(0)

    if result:
        print("#{} {}".format(t, result))
    else:
        print("#{} {}".format(t, 'impossible'))




