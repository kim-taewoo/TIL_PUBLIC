T = 2
for t in range(1, T+1):
    v, e = map(int, input().split())
    a = list(map(int, input().split()))

    chk_node = [False for _ in range(v+1)] # 1 부터임에 주의
    chk_edge = [list() for _ in range(v+1)]

    for i in range(0, len(a)-1, 2):
        chk_edge[a[i]].append(a[i+1])

    result = []
    while True:
        if sum(chk_node[1:]) == v: break
        chk_root = [True for _ in range(v+1)]
        for i in range(1, v+1):
            if not chk_node[i]:
                for j in chk_edge[i]:
                    chk_root[j] = False
        roots = [i for i in range(1, v+1) if chk_root[i] and not chk_node[i]]
        result += roots
        for i in roots:
            chk_node[i] = True


    result = " ".join(map(str, result))
    print("#{} {}".format(t, result))