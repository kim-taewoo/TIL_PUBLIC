T = int(input())

def chk_sudoku_squre():
    for r in range(0,9,3):
        for c in range(0,9,3):
            sudoku = [0] * 10
            for i in range(3):
                for j in range(3):
                    if sudoku[a[r+i][c+j]]:
                        return False
                    else:
                        sudoku[a[r+i][c+j]] = 1
    return True


def chk_sudoku_hor():
    for r in range(9):
        sudoku = [0] * 10
        for c in range(9):
            if sudoku[a[r][c]]:
                return False
            else:
                sudoku[a[r][c]] = 1
    return True


def chk_sudoku_ver():
    for c in range(9):
        sudoku = [0] * 10
        for r in range(9):
            if sudoku[a[r][c]]:
                return False
            else:
                sudoku[a[r][c]] = 1
    return True


for t in range(1, T+1):
    a = [list(map(int, input().split())) for _ in range(9)]

    if chk_sudoku_squre() and chk_sudoku_hor() and chk_sudoku_ver():
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))