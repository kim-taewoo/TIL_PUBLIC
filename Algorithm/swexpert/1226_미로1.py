T = 10
def find_start():
    for r in range(16):
        for c in range(16):
            if board[r][c] == '2':
                return r, c

for _ in range(1, T+1):
    t = int(input())
    board = [input() for _ in range(16)]
    chk = [[False for _ in range(16)] for __ in range(16)]
    x = find_start()
    q = [(x[0], x[1])]  
    chk[x[0]][x[1]] = True
    flag = 0
    while q:
        if flag: break
        r, c = q.pop(0)
        for dr, dc in ((0,1),(1,0),(0,-1),(-1,0)):
            nr, nc = r + dr, c + dc
            if nr >=0 and nc >=0 and nr < 16 and nc < 16 and not chk[nr][nc] and board[nr][nc] != '1':
                if board[nr][nc] == '3':
                    flag = 1
                    break
                chk[nr][nc] = True
                q.append((nr,nc))
    print("#{} {}".format(t, flag))
