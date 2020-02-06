import sys
input=sys.stdin.readline

def chk_sudoku(r,c):
    for x in range(3):
        for i in range(9):
            if x == 0:
                if i == c: continue
                cur = a[r][i] 
            elif x == 1:
                if i == r: continue
                cur = a[i][c] 
            else:
                row, col = divmod(i, 3)
                r1 = r // 3 * 3 + row
                c1 = c // 3 * 3 + col
                if r1 == r and c1 == c: continue
                cur = a[r1][c1]
            if cur == a[r][c]:
                return False
    return True

def solve(idx):
    global found
    global b
    if idx >= len(zeros):
        found = True
        b = [i[:] for i in a]
        return
    if found: return
    r = zeros[idx][0]
    c = zeros[idx][1]
    print(r,c)
    for i in range(1, 10):
        a[r][c] = i
        if chk_sudoku(r,c):
            solve(idx+1)
    a[r][c] = 0


a = [list(map(int, input().split())) for _ in range(9)]
found = False
b = []
zeros = []
for i in range(9):
    for j in range(9):
        if not a[i][j]:
            zeros.append((i,j))
solve(0)
for x in b:
    print(*x)