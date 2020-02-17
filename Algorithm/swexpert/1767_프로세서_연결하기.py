# 프로세서 연결하기


def dfs(idx, coreCount, edge_len):
    global max_cores
    global min_edge
    if idx == len(cores):
        if max_cores < coreCount:
            max_cores = coreCount
            min_edge = edge_len
        elif max_cores == coreCount:
            if min_edge > edge_len:
                min_edge = edge_len
        return
    
    r, c = cores[idx]
    
    for d in range(4):
        count = 0
        nr = r
        nc = c
        origin_r = r
        origin_c = c
        while True:
            nr += dr[d]
            nc += dc[d]
            
            if (nr <0 or nr >=n or nc <0 or nc>=n):
                break
            if a[nr][nc] == 1:
                count = 0
                break
            count += 1
            
        for i in range(count):
            origin_r += dr[d]
            origin_c += dc[d]
            
            a[origin_r][origin_c] = 1
            
        if (count == 0):
            dfs(idx+1, coreCount, edge_len)
        else:
            dfs(idx+1, coreCount+1, edge_len+count)
            
            origin_r = r
            origin_c = c
            for i in range(count):
                origin_r += dr[d]
                origin_c += dc[d]
                a[origin_r][origin_c] = 0

T = int(input())

for t in range(T):
    n = int(input())
    a = [list(map(int,input().split())) for _ in range(n)]
    
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    
    cores = []
    
    for r in range(n):
        for c in range(n):
            if a[r][c] == 1:
                if (r==0 or r==n-1 or c==0 or c==n-1):
                    continue
                cores.append((r,c))
    max_cores = 0
    min_edge = 1e9

    dfs(0,0,0)
    
    print("#" + str(t+1) + " " + str(min_edge) )