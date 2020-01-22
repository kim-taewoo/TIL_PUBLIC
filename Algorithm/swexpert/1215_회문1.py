T = 10

def chk_hor(r,c):

    for i in range(n//2):
        if a[r][c+i] != a[r][c+n-1-i]:
            return False
    return True


def chk_ver(r, c):

    for i in range(n//2):
        if a[r+i][c] != a[r+n-1-i][c]:
            return False
    return True

for t in range(1, T+1):
    n = int(input())

    a = [list(input()) for _ in range(8)]

    cnt = 0
    for r in range(8):
        for c in range(8):
            if r < 8 - n + 1:
                if chk_ver(r, c) : cnt += 1
            if c < 8 - n + 1:
                if chk_hor(r, c) : cnt += 1
    print("#{} {}".format(t, cnt))
