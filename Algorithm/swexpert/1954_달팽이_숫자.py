T = int(input())
'''
방향을 90도로 틀면서 개수가
n -> n-1 -> n-1 -> n-2 -> n-2 ... 1 -> 1 까지 진행

방향을 튼다는건
행 고정 -> 열 고정 -> 행 고정(reverse) -> 열 고정(reverse) -> 행 고정 순으로 바뀌는 것

'''

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for t in range(1, T+1):

    n = int(input())

    a = [[0] * n for _ in range(n)]

    # n 만큼 오른쪽
    d = 1
    r = 0
    c = -1
    num = 1
    for i in range(n):
        r += dr[d]
        c += dc[d]
        a[r][c] = num
        num += 1

    # n-1 만큼 아래쪽
    # n-1 만큼 왼쪽
    # n-2 만큼 위쪽
    # n-2 만큼 오른쪽
    for i in range(n-1, 0, -1):
        for _ in range(2):
            d = (d+1) % 4
            for j in range(i):
                r += dr[d]
                c += dc[d]
                a[r][c] = num
                num += 1
    
    print("#{}".format(t))
    for r in range(n):
        for c in range(n):
            print(a[r][c], end=" ")
        print()
        
