def chk_lane(board):
    lane = 0
    for i in range(n):
        flag = True
        cnt = 1
        j = 1
        while j < n:
            if board[i][j] == board[i][j-1]:
                cnt += 1
            elif board[i][j] == board[i][j-1] + 1:
                if cnt >= x:
                    cnt = 1
                else:
                    break
            elif board[i][j] == board[i][j-1] - 1:
                tmp = board[i][j]
                flag = True
                for k in range(x-1):
                    j += 1
                    if j >= n or board[i][j] != tmp:
                        flag = False
                        break
                if not flag:
                    break
                cnt = 0
            else:
                flag = False
                break
            j += 1
        if j == n and flag:
            lane += 1
    return lane


def rotate90(a):
    b = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            b[c][n-1-r] = a[r][c]
    return b


T = int(input())
for t in range(1, T+1):
    n, x = map(int, input().split())
    original_board = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    ans += chk_lane(original_board)
    ans += chk_lane(rotate90(original_board))

    print("#{} {}".format(t, ans))
