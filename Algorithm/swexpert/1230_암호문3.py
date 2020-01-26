T = 10

for t in range(1,T+1):
    n_a = int(input())
    a = input().split()
    n_c = int(input())
    c = input().split()

    i = 0
    while i < len(c):
        if c[i] == 'I':
            x = int(c[i+1])
            y = int(c[i+2])
            ii = []
            for s in range(y):
                ii.append(c[i+2+s])
            a = a[:x] + ii + a[x:]
            i += 2 + y + 1

        elif c[i] == 'D':
            x = int(c[i+1])
            y = int(c[i+2])
            a = a[:x] + a[x+y-1 : ]
            i += 3
        elif c[i] == 'A':
            y = int(c[i+1])
            aa = []
            for s in range(y):
                aa.append(c[i+2+s])
            a = a + aa
            i += 1 + y + 1

    result = " ".join(a[:10])
    print("#{} {}".format(t, result))