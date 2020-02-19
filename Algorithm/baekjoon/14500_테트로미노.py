dr = [-1,0,1,0]
dc = [0,1,0,-1]

def dfs(a,b,cnt,result):
    global max_result
    if cnt == 4:
        if result > max_result:
            max_result = result
        return

    for d in range(4):
        na, nb = a + dr[d], b + dc[d]
        if na < 0 or nb < 0 or na >= n or nb >= m or chk[na][nb]: continue
        chk[na][nb] = True
        dfs(na,nb,cnt+1,result + board[na][nb])
        chk[na][nb] = False

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for __ in range(n)]
max_result = 0
for r in range(n):
    for c in range(m):
        chk[r][c] = True
        dfs(r,c,1,board[r][c])

print(max_result)