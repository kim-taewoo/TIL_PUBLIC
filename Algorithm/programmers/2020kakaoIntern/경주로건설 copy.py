def solution(board):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    n = len(board)
    chk = [[0 for _ in range(n)] for __ in range(n)]
    def dfs(r,c,ld,total_cost):
        nonlocal mini
        if r == n-1 and c == n-1:
            mini = min(mini, total_cost)
            return
        
        for d in range(4):
            nr, nc = r+ dr[d], c+dc[d]
            if 0<=nr<n and 0<=nc<n and not board[nr][nc] and not chk[nr][nc]:
                chk[nr][nc] = 1
                added_cost = 100 if ld == d else 600
                dfs(nr,nc,d,total_cost+added_cost)
                chk[nr][nc] = 0


    mini = 2147000000
    chk[0][0] = 1
    dfs(0, 0, 1, 0)
    dfs(0, 0, 2, 0)
    answer = mini
    return answer


board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0],
         [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
print(solution(board))
