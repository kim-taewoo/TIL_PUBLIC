def dfs(now,goal):
    global flag
    if flag : return
    if now == goal:
        flag = 1
        return
    for node in vs[now]:
        if not chk[node]:
            chk[node] = True
            dfs(node,goal)

T = int(input())
for t in range(1, T+1):
    v, e = map(int, input().split())
    vs = [list() for _ in range(v+1)]
    for i in range(e):
        a, b = map(int, input().split())
        vs[a].append(b)
    
    s,g = map(int, input().split())
    flag = 0
    chk = [False for _ in range(v+1)]
    chk[s] = True
    dfs(s,g)
    print("#{} {}".format(t, flag))