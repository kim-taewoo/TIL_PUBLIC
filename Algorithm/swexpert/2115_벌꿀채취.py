T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # n 개 중에 연속해서 m 개를 선택해야 한다면
    # 선택 가능한 마지막 컬럼의 인덱스는
    # n-1 - m + 1, 즉 n-m 이다. range 는 1 을 더해서 넣어야 하므로 n-m+1 까지 range 함수에 넣어줘야 한다.
    max_table = [[0 for _ in range(N)] for __ in range(N)]

    def calc_max_price(r, c):
        to_pick = board[r][c:c+M]

        maxi = 0

        def dfs(level, max_level, current, allowed, price):
            nonlocal maxi
            if level == max_level:
                if price > maxi:
                    maxi = price
                    max_table[r][c] = maxi
                return

            dfs(level+1, max_level, current, allowed, price)
            if current + to_pick[level] <= allowed:
                dfs(level+1, max_level, current +
                    to_pick[level], allowed, price + to_pick[level]**2)

        if max_table[r][c]:
            maxi = max_table[r][c]
        else:
            dfs(0, len(to_pick), 0, C, 0)

        # if to_pick == [8, 5]:
        #     print(maxi)
        #     print('here')
        return maxi

    def pick_another(start_r, start_c):
        maxi = 0
        for r in range(start_r, N):
            for c in range(start_c, N-M+1):
                tmp = calc_max_price(r, c)
                if tmp > maxi:
                    maxi = tmp
            start_c = 0
        return maxi

    maxi_result = 0
    for r in range(N):
        for c in range(N-M+1):
            worker1 = calc_max_price(r, c)
            worker2 = pick_another(r, c+M)
            if worker1 + worker2 > maxi_result:
                maxi_result = worker1 + worker2

    print("#{} {}".format(t, maxi_result))
