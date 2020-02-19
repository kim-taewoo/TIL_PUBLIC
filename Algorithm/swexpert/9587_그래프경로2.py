T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    vs = [list() for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        vs[a].append(b)
    
    s,g = map(int, input().split())
    flag = False
    chk = [False for _ in range(v+1)]
    q = [s]
    chk[s] = True
    while q:
        if flag: break
        now = q.pop(0)
        for i in vs[now]:
            if not chk[i]:
                if i == g:
                    flag = True
                    break
                q.append(i)
                chk[i] = True
    if flag:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))