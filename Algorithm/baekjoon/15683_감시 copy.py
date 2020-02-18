def oob(a, b):
    return a < 0 or b < 0 or a >= n or b >= m or room[a][b] == 6


def watch(a, b, directions):
    tmp = list()
    for d in directions:
        na, nb = a + dr[d], b + dc[d]
        while not oob(na, nb):
            if not (room[na][nb] or chk[na][nb]):
                chk[na][nb] = True
                tmp.append((na, nb))
            na, nb = na + dr[d], nb + dc[d]
    return tmp


def dfs(level, cnt):
    global max_cnt

    if level == n_cctv:
        if cnt > max_cnt:
            max_cnt = cnt
        return

    r, c, t = cctvs[level]
    if t == 5:
        new_watch = 0
        result = watch(r, c, [0, 1, 2, 3])
        new_watch += len(result)
        dfs(level+1, cnt + new_watch)
        for x, y in result:
            chk[x][y] = 0
    elif t == 1:
        for i in range(4):
            result = watch(r, c, [i])
            new_watch = len(result)
            dfs(level+1, cnt+new_watch)
            for x, y in result:
                chk[x][y] = 0
    elif t == 2:
        for i in range(2):
            new_watch = 0
            result = watch(r, c, [i, i+2])
            new_watch += len(result)
            dfs(level+1, cnt+new_watch)
            for x, y in result:
                chk[x][y] = 0
    elif t == 3:
        for i in range(4):
            new_watch = 0
            result = watch(r, c, [i, (i+1) % 4])
            new_watch += len(result)
            dfs(level+1, cnt+new_watch)
            for x, y in result:
                chk[x][y] = 0
    elif t == 4:
        for i in range(4):
            new_watch = 0
            result = watch(r, c, [i, (i+1) % 4, (i+2) % 4])
            new_watch += len(result)
            dfs(level+1, cnt+new_watch)
            for x, y in result:
                chk[x][y] = 0


# main()
n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 0, 1, 0]  # 위, 오른쪽, 아래쪽, 왼쪽
dc = [0, 1, 0, -1]

chk = [[False for _ in range(m)] for __ in range(n)]
cctvs = []
remains = 0
for r in range(n):
    for c in range(m):
        if room[r][c] == 0:
            remains += 1
        elif 1 <= room[r][c] <= 5:
            cctvs.append((r, c, room[r][c]))

n_cctv = len(cctvs)
max_cnt = 0
dfs(0, 0)

print(remains - max_cnt)
