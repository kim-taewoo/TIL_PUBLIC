dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def solution(board):
    n = len(board)
    cost_board = [[2147000000 for _ in range(n)] for __ in range(n)]
    cost_board[0][0] = 0
    sr, sc = 0, 0
    q = []
    if not board[sr+1][sc]:
        q.append((sr+1, sc, 2, 100))
    if not board[sr][sc+1]:
        q.append((sr, sc+1, 1, 100))
    while q:
        r, c, pd, cost = q.pop()
        for d in range(4):
            nr, nc = r + dr[d], c + dc[d]
            if d != pd:
                ncost = cost + 600
            else:
                ncost = cost + 100
            if 0 <= nr < n and 0 <= nc < n and not board[nr][nc] and ncost < cost_board[nr][nc]:
                cost_board[nr][nc] = ncost
                q.append((nr, nc, d, ncost))

    answer = cost_board[n-1][n-1]
    return answer


board = [
    [0, 0, 0, 0, 0, 0, 0, 1], 
    [0, 0, 0, 0, 0, 0, 0, 0], 
    [0, 0, 0, 0, 0, 1, 0, 0], 
    [0, 0, 0, 0, 1, 0, 0, 0], 
    [0, 0, 0, 1, 0, 0, 0, 1], 
    [0, 0, 1, 0, 0, 0, 1, 0], 
    [0, 1, 0, 0, 0, 1, 0, 0], 
    [1, 0, 0, 0, 0, 0, 0, 0]
]
print(solution(board))
