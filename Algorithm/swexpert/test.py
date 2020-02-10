# dfs로 2차원 배열 미로찾기 구현
# 0 은 벽, 1 은 통로
size = 8
board = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
# 각 셀별로 다음과 같은 고유번호가 주어졌다고 했을 때
# board = [
#     [0, 1, 2, 3, 4, 5, 6, 7],
#     [8, 9, 10, 11, 12, 13, 14, 15],
#     [16, 17, 18, 19, 20, 21, 22, 23],
#     [24, 25, 26, 27, 28, 29, 30, 31],
#     [32, 33, 34, 35, 36, 37, 38, 39],
#     [40, 41, 42, 43, 44, 45, 46, 47],
#     [48, 49, 50, 51, 52, 53, 54, 55],
#     [56, 57, 58, 59, 60, 61, 62, 63],
# ]
# s : 출발, g : 도착
s = (1, 0)
g = (6, 7)
# dfs 방식 (길은 오른쪽, 아래, 왼쪽, 위 방향으로 탐색) 으로 길을 찾으면 다음과 같은 경로를 따르게 되며, print 문을 통해 경로를 확인할 수 있도록 구현하였음
# (s)8 - 9 - 10 - 11 - 19 - 20 - 21 - 22 - 14 - (되돌아가는 과정: 22 - 21) - 29 - 37 - 38 - (37) - 36 - (37 - 29 - 21 - 20 - 19) - 27 - 26 - 25 - 33 - 41 - 49 - 50 - 51 - 52 - 53 - 54 - 55(g)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
visited = [[False for _ in range(size)] for _ in range(size)]
stack = []
v = s
visited[v[0]][v[1]] = True
print(v[0]*size+v[1])
while v != g:
    if(v):  # 왔던 길을 거슬러 올라가면서 다른 경로가 있는지 확인하고 해당 경로로 진행
        for i in range(4):
            r_check = v[0] + dr[i]
            c_check = v[1] + dc[i]
            if 0 <= r_check < size and 0 <= c_check < size:  # indexError 핸들링
                # 인접한 셀 중 방문하지 않은 통로가 있는지 확인
                if board[r_check][c_check] == 1 and visited[r_check][c_check] == False:
                    w = (r_check, c_check)
                    stack.append(v)
                    break
        else:
            w = None  # 인접한 셀 중 방문하지 않은 통로가 없을 경우
        while(w):  # 해당 셀에서 더 이상 진행할 수 있는 통로가 없을 때까지 while 문 반복
            visited[w[0]][w[1]] = True
            print(w[0]*size+w[1])  # 방문한 지점의 고유 번호 출력
            stack.append(w)
            v = w
            for i in range(4):
                r_check = v[0] + dr[i]
                c_check = v[1] + dc[i]
                if 0 <= r_check < size and 0 <= c_check < size:  # indexError 핸들링
                    # 인접한 셀 중 방문하지 않은 통로가 있는지 확인
                    if board[r_check][c_check] == 1 and visited[r_check][c_check] == False:
                        w = (r_check, c_check)
                        break
            else:
                w = None
        v = stack.pop()  # 해당 셀에서 더 이상 진행할 수 있는 통로가 없을 경우에는 왔던 길을 거슬러 올라감
