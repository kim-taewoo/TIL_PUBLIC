T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]

    total = board[0]
    for i in range(1, len(board)):
        now = board[i]
        found = False
        for j in range(len(total)):
            if total[j] > now[0]:
                found = True
                total = total[:j] + now + total[j:]
                break
        if not found:
            total.extend(now)

    print("#{} ".format(t), end="")
    print(*list(reversed(total[-10:])))
