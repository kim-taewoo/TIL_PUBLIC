T = int(input())

'''
90도 회전하면
0번째 행은 n-1번째 열이 되고,
1번째 행은 n-2번째 열이 되고,
n-1번째 행은 0번째 열이 된다.
같은 행 내에서 순서가 바뀌지는 않는다.
즉 본래 '열'번호가 순서대로 바뀐 곳의 '행'번호가 된다.
[0][0] -> [0][n-1]
[0][1] -> [1][n-1]
[n-1][0] -> [0][0]

코드상으로는 변환 결과 좌표에 대입하는 식으로 구현되므로
거꾸로 생각할 필요가 있다.
'''

def rotate90(a):
    b = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            b[c][n-1-r] = a[r][c]
    return b


for t in range(1,T+1):
    print("#{}".format(t))
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]

    r_90 = rotate90(a)
    r_180 = rotate90(r_90)
    r_270 = rotate90(r_180)

    for r in range(n):
        print("".join(map(str, r_90[r])), end=" ")
        print("".join(map(str, r_180[r])), end=" ")
        print("".join(map(str, r_270[r])))
