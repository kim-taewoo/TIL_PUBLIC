def solution(board):
    n = len(board[0])

    # 가로, 세로
    chk = [[[False, False] for _ in range(n)] for __ in range(n)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    loc = [0, 0, [0, 0], [0, 1]]  # time, 가로세로pos, 합 작은 쪽, 합 큰 쪽
    chk[0][0][0] = True  # 더 작은 쪽 좌표의 가로 형태만 True 로 설정 (시작이 가로니까)
    q = [loc]  # 통째로 집어넣기
    answer = 0
    while q:
        # b 가 더 큰 쪽.
        time, pos, a, b = q.pop(0)

        if b[0] == n-1 and b[1] == n-1:
            answer = time
            break

        # 평범한 가로세로 방향 이동. 방향도 바뀌지 않고 둘 중 더 큰 곳이 바뀌지 않는다.(a,b 순서 유지)
        for d in range(4):
            trueCoors = []
            r, c = a
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc] and not chk[nr][nc][pos]:
                trueCoors.append([nr, nc])

            r, c = b
            nr, nc = r+dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]:
                trueCoors.append([nr, nc])

            if len(trueCoors) == 2:
                # 작은 좌표 기준으로만 체크를 해준다.
                chk[trueCoors[0][0]][trueCoors[0][1]][pos] = True
                q.append([time+1, pos, *trueCoors])

        # 회전

        # 복잡하니까 작은 좌표 기준으로 생각해보자.
        # 회전 후 좌표 합 순서가 바뀌는 게 있고 바뀌지 않는 경우가 있다.
        r, c = a

        hr = [-1, 1, -1, 1]
        hc = [0, 0, 1, 1]
        hcr = [-1, 1, -1, 1]
        hcc = [1, 1, 0, 0]

        vr = [0, 0, 1, 1]
        vc = [-1, 1, -1, 1]
        vcr = [1, 1, 0, 0]
        vcc = [-1, 1, -1, 1]
        # 가로 형태일 때
        if pos == 0:
            # a 가 더 커짐
            for d in range(4):

                nr, nc = r + hr[d], c + hc[d]
                cr, cc = r + hcr[d], c + hcc[d]
                if 0 <= nr < n and 0 <= nc < n and not board[nr][nc] and not board[cr][cc]:
                    if d == 0:
                        if not chk[nr][nc][1]:
                            chk[nr][nc][1] = True
                            q.append([time+1, 1, [nr, nc], [r, c]])
                    elif d == 1:
                        if not chk[r][c][1]:
                            chk[r][c][1] = True
                            q.append([time+1, 1, [r, c], [nr, nc]])
                    elif d == 2:
                        if not chk[nr][nc][1]:
                            chk[nr][nc][1] = True
                            q.append([time+1, 1, [nr, nc], [r, c+1]])
                    elif d == 3:
                        if not chk[r][c+1][1]:
                            chk[r][c+1][1] = True
                            q.append([time+1, 1, [r, c+1], [nr, nc]])

        elif pos == 1:
            for d in range(4):
                nr, nc = r + vr[d], c+vc[d]
                cr, cc = r+vcr[d], c+vcc[d]
                if 0 <= nr < n and 0 <= nc < n and not board[nr][nc] and not board[cr][cc]:
                    if d == 0:
                        if not chk[nr][nc][0]:
                            chk[nr][nc][0] = True
                            q.append([time+1, 0, [nr, nc], [r, c]])
                    elif d == 1:
                        if not chk[r][c][0]:
                            chk[r][c][0] = True
                            q.append([time+1, 0, [r, c], [nr, nc]])
                    elif d == 2:
                        if not chk[nr][nc][0]:
                            chk[nr][nc][0] = True
                            q.append([time+1, 0, [nr, nc], [r+1, c]])
                    elif d == 3:
                        if not chk[r+1][c][0]:
                            chk[r+1][c][0] = True
                            q.append([time+1, 0, [r+1, c], [nr, nc]])

    return answer


board = [[0, 0, 0, 1, 1],
         [0, 0, 0, 1, 0],
         [0, 1, 0, 1, 1],
         [1, 1, 0, 0, 1],
         [0, 0, 0, 0, 0]]
print(solution(board))
