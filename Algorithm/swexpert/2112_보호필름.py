def dfs(start_r, level_now, level_max):
    global answer
    if answer != 2147000000:
        return
    if level_now == level_max:
        for c in range(1, w+1):
            chain = 1
            start = board[1][c]
            for r in range(2, d+1):
                if board[r][c] == start:
                    chain += 1
                else:
                    start = board[r][c]
                    chain = 1
                if chain >= k:
                    break
            if chain < k:
                return
        answer = level_max
        return

    else:
        for i in range(start_r, d + 1):
            if not chk_r[i]:
                chk_r[i] = True
                # 0 으로 바꾸는 약물일 때
                switched = []
                for c in range(1, w+1):
                    if board[i][c] == 1:
                        board[i][c] = 0
                        switched.append(c)
                dfs(i+1, level_now + 1, level_max)
                # 되돌리기
                for x in switched:
                    board[i][x] = 1
                # 1 으로 바꾸는 약물일 때
                switched = []
                for c in range(1, w+1):
                    if board[i][c] == 0:
                        board[i][c] = 1
                        switched.append(c)
                dfs(i+1, level_now + 1, level_max)
                # 되돌리기
                for x in switched:
                    board[i][x] = 0

                chk_r[i] = False


T = int(input())
for t in range(1, T+1):
    d, w, k = map(int, input().split())
    board = [[0] * (w+1)] + [[0] + list(map(int, input().split()))
                             for _ in range(d)]

    answer = 2147000000
    i = 0
    while answer == 2147000000:
        chk_r = [False for _ in range(d+1)]
        dfs(1, 0, i)
        i += 1

    print("#{} {}".format(t, answer))
