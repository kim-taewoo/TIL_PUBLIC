T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    house = [(r, c) for r in range(n) for c in range(n) if board[r][c]]

    max_cnt = 0
    for r in range(n):
        for c in range(n):
            k = 1
            while True:
                cost = k**2 + (k-1)**2
                cnt = 0
                for hr, hc in house:
                    if abs(hr - r) + abs(hc - c) <= k-1:
                        cnt += 1
                profit = cnt * m - cost
                if profit >= 0:
                    max_cnt = max(max_cnt, cnt)

                if cnt == len(house):
                    break
                k += 1

    print("#{} {}".format(t, max_cnt))
