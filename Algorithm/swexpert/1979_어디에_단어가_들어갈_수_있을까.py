T = int(input())

def chk_hor(r,c):
    for i in range(k):
        nc = c + i
        if nc >=n : 
            return False
        if not a[r][nc]:
            return False
    if c+k < n:
        if a[r][c+k]: 
            return False
    return True


def chk_ver(r,c):
    for i in range(k):
        nr = r + i
        if nr >=n : 
            return False
        if not a[nr][c]:
            return False
    if r+k < n:
        if a[r+k][c]: 
            return False
    return True


for t in range(1, T+1):
    n, k = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(n)]
    # 검은 부분이 0임에 주의!

    cnt = 0
    for r in range(n):
        for c in range(n):
            if not a[r][c] : continue
            if c-1 < 0 or not a[r][c-1]:  
                if chk_hor(r,c): cnt+=1
            if r-1 < 0 or not a[r-1][c]:
                if chk_ver(r,c): cnt+=1
    print("#{} {}".format(t, cnt))