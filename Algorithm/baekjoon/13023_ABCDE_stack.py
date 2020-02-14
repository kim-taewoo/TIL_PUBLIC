found = False
import sys
input = lambda: sys.stdin.readline()
def dfs(v, cnt, origin):
    global found
    if found: 
        return
    if cnt == 5:
        found = True
        return
    if cnt > chk_max[origin]:
        chk_max[origin] = cnt
    for i in board[v]:
        if not chk[i]:
            if chk_max[i]:
                if cnt + chk_max[i] < 5: continue
            chk[i] = True
            dfs(i, cnt + 1, origin)
            chk[i] = False
n,m = map(int, input().split())
board = [list() for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
chk_max = [0 for _ in range(n)]
chk = [False for _ in range(n)]
for i in range(n):
    if found: 
        break
    chk[i] = True
    dfs(i, 1, i)
    chk[i] = False
if found: 
    print(1)
else: 
    print(0)