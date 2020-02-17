found = False
import sys
input = lambda: sys.stdin.readline()

n,m = map(int, input().split())
board = [list() for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
chk_max = [0 for _ in range(n)]
for i in range(n):
    if found: 
        break
    chk = [False for _ in range(n)]
    chk[i] = True
    cnt = 1
    origin = i
    while True:
        if found: 
            break
        if cnt == 5:
            found = True
            break
        if cnt > chk_max[origin]:
            chk_max[origin] = cnt
        for j in board[i]:
            if not chk[j]:
                if chk_max[j]:
                    if cnt + chk_max[j] < 5: continue
                chk[j] = True
                dfs(i, cnt + 1, origin)
                chk[i] = False
if found: 
    print(1)
else: 
    print(0)