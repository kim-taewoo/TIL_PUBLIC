dr = [-1,0,1,0]
dc = [0,1,0,-1]

stack = []
def push(x,y):
    stack.append((x,y))

def pop():
    return stack.pop()

def dfs(a,b,ssum,depth):
    global max_result

    ssum += board[a][b]

    if depth == 1:
        if ssum > max_result:  
            max_result = ssum
        return

    push(a,b)
    chk[a][b] = True

    for k in stack:
        for d in range(4):
            na, nb = k[0] + dr[d], k[1] + dc[d]
            if na < 0 or nb < 0 or na >= n or nb >= m or chk[na][nb]: continue
            dfs(na, nb, ssum, depth - 1)
    chk[a][b] = 0
    pop()


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for __ in range(n)]
max_result = 0
for r in range(n):
    for c in range(m):
        dfs(r,c,0,4)
print(max_result)