# from pprint import pprint
m, n, k = map(int, input().split())

# 번호 매기는 방식이 다를 뿐이지 결국 형태는 다를게 없다는 걸 이용해
# 좌표를 굳이 변환시키지 않을 수 있다.
board = [[0 for _ in range(n)] for __ in range(m)]
for i in range(k):
    # 왼쪽 아래 점과 오른쪽 위 점
    x1, y1, x2, y2 = map(int, input().split())
    r1, c1, r2, c2 = m - y1, x1, m - y2, x2
    # print(r1, c1, r2, c2)
    for r in range(r2, r1):
        for c in range(c1, c2):
            board[r][c] = 1

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def bfs(r, c):
    q = [(r, c)]
    chk[r][c] = True
    cnt = 0
    while q:
        a, b = q.pop(0)
        cnt += 1
        for d in range(4):
            na, nb = a + dr[d], b + dc[d]
            if 0 <= na < m and 0 <= nb < n and not chk[na][nb] and not board[na][nb]:
                chk[na][nb] = True
                q.append((na, nb))
    return cnt


chk = [[False for _ in range(n)] for __ in range(m)]

areas = []
for r in range(m):
    for c in range(n):
        if not board[r][c] and not chk[r][c]:
            area = bfs(r, c)
            areas.append(area)

print(len(area))
print(*sorted(areas), sep=" ")
# print(" ".join(map(str,sorted(areas))))
