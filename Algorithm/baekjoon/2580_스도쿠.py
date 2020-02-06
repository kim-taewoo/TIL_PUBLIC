def chk_sudoku():
    for i in range(3):
        for r in range(9): 
            # r 과 c 라고 해서 꼭 row, column 은 아니고 상황에 맞게 사용되는 9*9 숫자일 뿐.
            # 숫자 자체를 이용할 생각을 해야지 숫자에 하나의 역할만을 부여하며
            # 딱딱하게 생각하면 문제를 유연하게 풀 수 없다. 
            sudoku = [0] * 9
            for c in range(9):
                if i == 0: # 가로 체크
                    cur = a[r][c]
                elif i == 1: # 세로 체크
                    cur = a[c][r]
                else: # 사각형 체크
                    # 9개의 작은 정사각형 0~8 인덱스(왼쪽위부터 오른쪽 아래방향), 해당 사각형 내에서 0~8 인덱스.
                    cur = a[(r // 3 * 3) + (c // 3)][(r % 3 * 3) + (c % 3)]
                if cur == 0: continue
                if sudoku[cur - 1]: return False
                sudoku[cur - 1] = True
    return True


def solve(idx):
    if idx == 81: return True
    r = idx // 9
    c = idx % 9
    cur = a[r][c]
    if cur != 0: 
        return solve(idx+1)
    else:
        for i in range(1, 10):
            a[r][c] = i
            if chk_sudoku():
                if solve(idx+1):
                    return True
        a[r][c] = 0 
        return False


a = [list(map(int, input().split())) for _ in range(9)]

solve(0)

for x in a:
    print(*x)