from collections import deque
import sys


def input(): return sys.stdin.readline()


def oob(a, b):
    if a < 0 or b < 0 or a >= n or b >= n:
        return True
    return False


directions = [(0, 1), (1, 0), (1, 1)]  # 오른쪽, 아래쪽, 오른아래대각선

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = 0
sr, sc = 0, 1
q = deque()
q.append((sr, sc, 0))
while q:
    r, c, t = q.popleft()
    if r == n-1 and c == n-1:
        result += 1
        continue
    nr = r + directions[0][0]
    nc = c + directions[0][1]
    nr2 = r + directions[1][0]
    nc2 = c + directions[1][1]
    nr3 = r + directions[2][0]
    nc3 = c + directions[2][1]
    impossible = [oob(nr, nc), oob(nr2, nc2), oob(nr3, nc3)]
    if t == 0:
        if not impossible[0] and not board[nr][nc]:
            q.append((nr, nc, 0))
        if not any(impossible) and not board[nr][nc] and not board[nr2][nc2] and not board[nr3][nc3]:
            q.append((nr3, nc3, 2))
    elif t == 1:
        if not impossible[1] and not board[nr2][nc2]:
            q.append((nr2, nc2, 1))
        if not any(impossible) and not board[nr][nc] and not board[nr2][nc2] and not board[nr3][nc3]:
            q.append((nr3, nc3, 2))
    else:
        if not impossible[0] and not board[nr][nc]:
            q.append((nr, nc, 0))
        if not impossible[1] and not board[nr2][nc2]:
            q.append((nr2, nc2, 1))
        if not any(impossible) and not board[nr][nc] and not board[nr2][nc2] and not board[nr3][nc3]:
            q.append((nr3, nc3, 2))
print(result)
