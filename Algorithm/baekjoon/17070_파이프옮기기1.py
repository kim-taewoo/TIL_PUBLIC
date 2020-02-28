def chk_move(r, c, status):
    if 0 <= r < n and 0 <= c < n and not a[r][c]:
        if status == 2:
            if a[r-1][c] == 0 and a[r][c-1] == 0:
                return True
            else: return False
        return True
    return False


def sol(status, coor_r, coor_c):
    global ans
    if coor_r == n-1 and coor_c == n-1:
        ans += 1
        return

    if status == 0:
        if coor_c == n-1:
            return
        #가로체크
        if chk_move(coor_r, coor_c+1, 0):
            sol(0, coor_r, coor_c+1)
        #대각선체크
        if chk_move(coor_r+1, coor_c+1, 2):
            sol(2, coor_r+1, coor_c+1)
    elif status == 1:
        if coor_r == n-1:
            return
        #세로체크
        if chk_move(coor_r+1, coor_c, 1):
            sol(1, coor_r+1, coor_c)
        #대각선체크
        if chk_move(coor_r+1, coor_c+1, 2):
            sol(2, coor_r+1, coor_c+1)
    elif status == 2:
        #가로체크
        if chk_move(coor_r, coor_c+1, 0):
            sol(0, coor_r, coor_c+1)
        #세로체크
        if chk_move(coor_r+1, coor_c, 1):
            sol(1, coor_r+1, coor_c)
        #대각선체크
        if chk_move(coor_r+1, coor_c+1, 2):
            sol(2, coor_r+1, coor_c+1)


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
sol(0, 0, 1)

print(ans)
