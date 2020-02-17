dr = (-1,0,1,0)
dc = (0,1,0,-1)
from pprint import pprint
def dfs(level, selected, total_cnt):
    global max_core
    global min_cnt
    if level == n_cores:
        if selected > max_core:
            max_core = selected
            min_cnt = total_cnt
        elif selected == max_core:
            if min_cnt > total_cnt:
                min_cnt = total_cnt
        return
    
    dfs(level+1, selected, total_cnt)

    r, c = cores[level]
    nr,nc = r,c
    for d in range(4):
        nr, nc = nr + dr[d], nc + dc[d]
        cnt = 1
        while not (nr < 0 or nc < 0 or nr >= n or nc >= n or chk[nr][nc] or a[nr][nc]):
            chk[nr][nc] = True
            nr, nc = nr + dr[d], nc + dc[d]
            cnt += 1
        nr, nc = nr - dr[d], nc - dc[d]        
        if nr == 0 or nc == 0 or nr == n-1 or nc == n-1:
            dfs(level+1, selected + 1, total_cnt + cnt)
        while nr != r or nc != c:
            chk[nr][nc] = False
            nr, nc = nr - dr[d], nc - dc[d]
            cnt -= 1

T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    cores = []
    for r in range(1, n-1):
        for c in range(1, n-1):
            if a[r][c]:
                cores.append((r, c))
    
    n_cores = len(cores)
    chk = [[False for _ in range(n)] for __ in range(n)]
    max_core = 0
    min_cnt = 2147000000
    dfs(0, 0, 0) # 코어 level, 선택된 코어 개수, 전선 길이
    print(max_core)
    print(min_cnt)
            
    