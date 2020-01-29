import sys
sys.setrecursionlimit(100000)

def go(a,b,c,d,binary):
    global dp
    global dp_chk

    if dp_chk[a][b][c][d][binary]: return
    dp_chk[a][b][c][d][binary] = 1

    if a and not binary:
        go(a-1, b, c, d, 0)
        if dp[a-1][b][c][d][0]:
            dp[a][b][c][d][binary] = dp[a-1][b][c][d][0] + '0'
            return
    if b and binary:
        go(a, b-1, c, d, 0)
        if dp[a][b-1][c][d][0]:
            dp[a][b][c][d][binary] = dp[a][b-1][c][d][0] + '1'
            return
    if c and not binary:
        go(a, b, c-1, d, 1)
        if dp[a][b][c-1][d][1]:
            dp[a][b][c][d][binary] = dp[a][b][c-1][d][1] + '0'
            return
    if d and binary:
        go(a, b, c, d-1, 1)
        if dp[a][b][c][d-1][1]:
            dp[a][b][c][d][binary] = dp[a][b][c][d-1][1] + '1'
            return




T = int(input())
for t in range(1, T+1):
    dp = [[[[[0] * 2 for d in range(20)] for c in range(20)] for b in range(20)] for a in range(20)]
    dp_chk = [[[[[0] * 2 for d in range(20)] for c in range(20)] for b in range(20)] for a in range(20)]
    dp[1][0][0][0][0] = '00'
    dp[0][1][0][0][1] = '01'
    dp[0][0][1][0][0] = '10'
    dp[0][0][0][1][1] = '11'
    a,b,c,d = map(int, input().split())

    go(a,b,c,d,0)
    go(a,b,c,d,1)

    if dp[a][b][c][d][0]:
        print("#{} {}".format(t, dp[a][b][c][d][0]))
    elif dp[a][b][c][d][1]:
        print("#{} {}".format(t, dp[a][b][c][d][1]))
    else:
        print("#{} {}".format(t, 'impossible'))

