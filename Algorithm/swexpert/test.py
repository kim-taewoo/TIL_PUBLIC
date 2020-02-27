from pprint import pprint
m, n, k = map(int, input().split())
board = [[0 for _ in range(n)] for __ in range(m)]

for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    # 대입을 잘해야 해.. 일단 행열이 반대고,
    # 행과 열에 1씩 빼주어야 하고,
    # 반대로 했을경우 행의 순서를 거꾸로 해주어야 함
    # 거꾸로라는건 0번째가 m-1, 1번째가 m-2 인 것이다.

    # 왼쪽 아래, 오른쪽 위
    r1, c1, r2, c2 = (m-1) - (y1-1), x1, (m-1) - (y2-1), x2
    for r in range(r2, r1):
        for c in range(c1, c2):
            board[r][c] = 1

pprint(board)
