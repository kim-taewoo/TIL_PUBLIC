def solution(board):
    n = len(board[0])

    chk = [[[False, False] for _ in range(n)] for __ in range(n)]

    dr = [-1,0,1,0]
    dc = [0,1,0,-1]

    loc = [0, 0, [0,0], [0,1]]
    chk[0][0][0] = True
    chk[0][0][1] = True
    chk[0][1][0] = True
    chk[0][1][1] = True
    q = [loc]

    while q:
        # b 가 더 큰 쪽으로 하자.
        time, pos, a, b = q.pop(0)

        # 평범한 가로세로 방향 이동
        for d in range(4):
            trueCoors = []
            r, c = a
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0<= nc < n and not board[nr][nc]:
                trueCoors.append([nr,nc])
            
            r, c = b
            nr, nc = r+dr[d], c + dc[d]
            if 0<=nr < n and 0 <=nc<n and not board[nr][nc] and not chk[nr][nc][pos]:
                trueCoors.append([nr,nc])


            if len(trueCoors) == 2:
                for x, y in trueCoors:
                    chk[x][y][pos] = True
                q.append([time+1, pos, *trueCoors ])

        # a 기준의 회전
        r1, c1 = a
        r2, c2 = b
        if pos == 0:
            # a 가 더 커짐
            targetCoor1 = [r1-1, c1]
            chkCoor1 = [r1-1, c1+1]
            r, c = targetCoor1
            if not chk[r1][c1][pos] and board[targetCoor1[0]][targetCoor1[1]] and board[chkCoor1[0]][chkCoor1[1]]:
                q.append([time+1, 1, [targetCoor1[0], targetCoor1[1]], [r1,c1]])
            

            targetCoor2 = [r1+1, c1]
            chkCoor2 = [r1+1, c1+1]
            targetCoor3 = [r2-1, c2]
            chkCoor3 = [r2-1, c2-1]
            targetCoor4 = [r2+1, c2]
            chkCoor4 = [r2+1, c2-1]
        
        elif pos == 1:
            targetCoor1 = [r1, c1-1]
            chkCoor1 = [r1+1, c1-1]
            targetCoor2 = [r1, c1+1]
            chkCoor2 = [r1+1, c1+1]
            targetCoor3 = [r2, c2-1]
            chkCoor3 = [r2-1, c2-1]
            targetCoor4 = [r2, c2+1]
            chkCoor4 = [r2-1, c2+1]





board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
print(solution(board))
