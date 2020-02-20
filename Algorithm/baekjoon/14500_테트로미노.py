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


def up_sum(a, b):
    return board[a][b] + board[a][b+1] + board[a][b+2] + board[a-1][b+1]
def down_sum(a, b):
    return board[a][b] + board[a][b+1] + board[a][b+2] + board[a+1][b+1]
def right_sum(a, b):
    return board[a][b] + board[a+1][b] + board[a+2][b] + board[a+1][b+1]
def left_sum(a, b):
    return board[a][b] + board[a+1][b] + board[a+2][b] + board[a+1][b-1]


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
chk = [[False for _ in range(m)] for __ in range(n)]
max_result = 0
for r in range(n):
    for c in range(m):
        chk[r][c] = True
        dfs(r,c,1,board[r][c])
        chk[r][c] = False
    for c in range(m): 
        # ㅏ, ㅓ 모양 처리
        if r <= n - 1 - 3 + 1:
            if c == 0:
                result1 = right_sum(r,c)
                if result1 > max_result:
                    max_result = result1
            elif c == m-1:
                result1 = left_sum(r,c)
                if result1 > max_result:
                    max_result = result1
            else:
                result1, result2 = left_sum(r,c), right_sum(r,c)
                if result1 > max_result:
                    max_result = result1
                if result2 > max_result:
                    max_result = result2
        # ㅗ, ㅜ 모양 처리
        if c <= m - 1 - 3 + 1:
            if r == 0:
                result1 = down_sum(r,c)
                if result1 > max_result:
                    max_result = result1
            elif r == n-1:
                result1 = up_sum(r,c)
                if result1 > max_result:
                    max_result = result1
            else:
                result1, result2 = up_sum(r,c), down_sum(r,c)
                if result1 > max_result:
                    max_result = result1
                if result2 > max_result:
                    max_result = result2


print(max_result)