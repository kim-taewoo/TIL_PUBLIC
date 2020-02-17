def find(x):
    if node_root[x] == x:
        return x
    else:
        return find(node_root[x])


def union(b, c):
    b = find(b)
    c = find(c)
    if b != c:
        node_root[c] = b # c 의 위치에 c의 선수작업 저장.

T = 2
for t in range(1, T+1):
    v, e = map(int, input().split())
    a = list(map(int, input().split()))

    node_root = [i for i in range(v+1)] # 1 부터임에 주의

    for i in range(0, len(a)-1, 2):
        union(a[i+1], a[i])

    result = []
    chk_node = [False for _ in range(v+1)]
    for i in range(1, v+1):
        if chk_node[i]: continue
        tmp = i
        chk_node[tmp] = True
        l = [tmp]
        while True:
            if node_root[tmp] == tmp: break
            tmp = node_root[tmp]
            chk_node[tmp] = True
            l.append(tmp)
        result.extend(reversed(l))

    result = " ".join(map(str, result))
    print("#{} {}".format(t, result))