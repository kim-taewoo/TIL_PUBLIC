T = 10

for t in range(1, T+1):
    n_a = int(input())
    a = input().split()
    n_c = int(input())
    c = input().split()

    i = 0
    while i < len(c):
        if c[i] == 'I':
            x = int(c[i+1])
            y = int(c[i+2])
            ii = c[i+3:i+3+y]
            a = a[:x] + ii + a[x:]
            i += 2 + y + 1

        elif c[i] == 'D':
            x = int(c[i+1])
            y = int(c[i+2])
            a = a[:x] + a[x+y:]
            i += 3

    result = " ".join(a[:10])
    print("#{} {}".format(t, result))
