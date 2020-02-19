def answer_chk():
    for c in range(1,n+1):
        tmp = c
        for r in range(1, h+1):
            if board[r][tmp]:
                tmp+=1
            elif board[r][tmp-1]:
                tmp-=1
        if tmp != c:
            return False
    return True


def dfs(num, br, bc):
    global found
    if found: return
    if num == 0:
        if answer_chk():
            found = True
        return
    
    for r in range(br,h+1):
        for c in range(bc, n):
            if board[r][c]: continue
            board[r][c] = 1
            dfs(num-1, r, c+2)
            board[r][c] = 0
        bc = 1

n, m, h = map(int, input().split()) # 세로선, 가로선, 가로 수 놓을 수 있는 위치
board = [[0 for _ in range(n+2)] for __ in range(h+1)] 
for i in range(m):
    # 각 셀의 위쪽 변에 줄 그어지는 상황.
    a,b = map(int, input().split())
    board[a][b] = 1

if answer_chk():
    print(0)
else:
    found = False
    i = 0
    while not found and i < 3:
        i+=1
        dfs(i, 1, 1)
    if found:
        print(i)
    else:
        print(-1)
