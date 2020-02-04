a = [list(map(int, input().split())) for _ in range(9)]

for r in range(9):
    for c in range(9):
        if a[r][c] == 0:
            chk_r()
            chk_c()
            chk_square()