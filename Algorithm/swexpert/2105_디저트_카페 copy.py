direction = [(1, -1), (1, 1), (-1,1), (-1,-1)]

def dfs(oa,ob,a,b,d,visited, cnt):
    global max_result
    
    if d == 3 and b == ob:
        if a == oa:
            if cnt > max_result:
                max_result = cnt
        return

    if board[a][b] in visited:
        return

    visited.append(board[a][b])
    if d < 3:
        for i in range(2):
            na, nb = a + direction[d+i][0], b + direction[d+i][1]
            if na < 0 or nb < 0 or na >= n or nb >= n: continue
            dfs(oa, ob, na, nb, d+i,visited, cnt + 1)
    else:
        na, nb = a + direction[d][0], b + direction[d][1]
        if na < 0 or nb < 0 or na >= n or nb >= n: return
        dfs(oa,ob,na,nb,d,visited, cnt + 1)
    visited.pop()


T = int(input())
for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_result = -1
    for r in range(n):
        for c in range(n):
            dfs(r,c,r,c,0,[],0)
            
    print("#{} {}".format(t, max_result))