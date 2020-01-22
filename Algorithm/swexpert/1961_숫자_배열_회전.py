T = int(input())

'''
1 2 3
4 5 6
7 8 9

7 4 1
8 5 2
9 6 3

90 도 회전하면 
[0][0] 은 [0][n-1]
[0][1] 은 [1][n-1]
[0][2] 은 [2][n-1]

[1][0] 은 [0][1]
[1][1] 은 [1][1]
[1][2] 은 [2][1]
'''

def rotate(r,c):
    pass


for t in range(1,T+1):
    print("#{}".format(t))
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]


    for r in range(n):
        for c in range(n):
            print(, end=" ")
