for i in range(4):
    a = list(map(int, input().split()))
    b, c = a[:4], a[4:]
    if b[0] <= c[0]:
        l, r = b,c
    else:
        l, r = c,b
    
    if l[2] > r[0]:
        if l[3] < r[1] or l[1] > r[3]:
            print('d')
        elif l[3] == r[1] or l[1] == r[3]: 
            print('b')
        else:
            print('a')
    elif l[2] == r[0]:
        if l[3] < r[1] or l[1] > r[3]:
            print('d')
        elif l[3] == r[1] or l[1] == r[3]: 
            print('c')
        else:
            print('b')
    else:
        print('d')
