T = 1

for t in range(1,T+1):
    n_a = int(input())
    a = list(input().split())
    n_c = int(input())
    c = list(input().split())

    cnt = 0
    i = 0
    while i < len(c):
        if c[i] == 'I':
            idx = int(c[i+1])
            n = int(c[i+2])
            for j in range(n):
                a.insert(idx+j, c[i+2+j])
            i+= 2 + n + 1

            cnt += 1
        elif c[i] == 'D':
            idx = int(c[i+1])
            n = int(c[i+2])
            for j in range(n):
                a.pop(idx)
            i += 3
            cnt += 1
        elif c[i] == 'A':
            n = int(c[i+1])
            for j in range(n):
                a.append(c[i+2+j])
            i += 1 + n + 1
            cnt += 1
    result = " ".join(a[:10])
    print("#{} {}".format(t, result))
    print(cnt)