from pprint import pprint
def solution(board):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    n = len(board)
    chk = [[2147000000 for _ in range(n)] for __ in range(n)]
    chk[0][0] = 0
    q = [(0, 0, 1, 0), (0, 0, 2, 0)]
    while q:
        r, c, ld, cost = q.pop(0)
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc]:
                ncost = cost + 100 if d == ld else cost+600
                if ncost <= chk[nr][nc]:
                    chk[nr][nc] = ncost
                    q.append((nr, nc, d, ncost))

    answer = chk[n-1][n-1]
    pprint(chk)
    return answer


board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]
print(solution(board))
