direction = [(1, -1), (1, 1), (-1,1), (-1,-1)]

def dfs(oa, ob, a, b, d, cnt):
    global max_eat
    if d == 3 and b == ob:
        if a == oa:
            print(oa, ob, a, b, cnt)
            if cnt > max_eat:
                max_eat = cnt

        return

    if dessert_chk[board[a][b]]:
        return

    dessert_chk[board[a][b]] = True

    if d != 3:
        for i in range(2):
            na, nb = a + direction[d+i][0], b + direction[d+i][1]
            if na < 0 or nb < 0 or na >= n or nb >= n: continue
            dfs(oa, ob, na, nb, d+i, cnt + 1)
    else:
        na, nb = a + direction[d][0], b + direction[d][1]
        if na < 0 or nb < 0 or na >= n or nb >= n: return
        dfs(oa,ob,na,nb,d, cnt + 1)

    dessert_chk[board[a][b]] = False
    

for t in range(1, int(input())+1):
    dessert_chk = [False for _ in range(101)]
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_eat = -1
    for r in range(n-2):
        for c in range(1,n-1):
            dfs(r,c,r,c,0,0)


    print("#{} {}".format(t, max_eat))