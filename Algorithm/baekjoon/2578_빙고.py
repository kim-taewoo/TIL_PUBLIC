def chk_bingo():
    bingo = 0
    for i in range(5):
        if sum(chk_h[i]) == 5:
            bingo += 1
        if sum(chk_v[i]) == 5:
            bingo += 1
    for i in range(2):
        if sum(chk_d[i]) == 5:
            bingo += 1
    if bingo >= 3:
        return True
    return False

a = [list(map(int, input().split())) for _ in range(5)]

chk_h = [[False for _ in range(5)] for __ in range(5)] # 가로 체크
chk_v = [[False for _ in range(5)] for __ in range(5)] # 세로 체크
chk_d = [[False for _ in range(5)] for __ in range(2)] # 대각선 오른아래, 오른위 방향 체크

b = []
for i in range(5):
    b += list(map(int, input().split()))

cnt = 0
for i in b:
    if cnt >= 12:
        result = chk_bingo()
        if result: 
            print(cnt)
            break
    for r in range(5):
        try:
            idx = a[r].index(i)
        except:
            idx = -1
        if idx != -1:
            chk_h[r][idx] = True
            chk_v[idx][r] = True
            if r == idx:
                if r == 2:
                    chk_d[0][2] = True
                    chk_d[1][2] = True
                else:
                    chk_d[0][idx] = True
            elif r + idx == 4:
                chk_d[1][idx] = True
    cnt += 1
    