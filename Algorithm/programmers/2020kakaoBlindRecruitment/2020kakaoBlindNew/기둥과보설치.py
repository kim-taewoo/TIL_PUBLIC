arr = [[[0, 0] for _ in range(110)] for __ in range(110)]  # 기둥, 보
result = []


def check():
    for y in range(110):
        for x in range(110):
            if arr[y][x][0] == 1:
                if not (y == 0 or arr[y - 1][x][0] == 1 or arr[y][x][1] == 1 or (x - 1 >= 0 and arr[y][x - 1][1] == 1)):
                    return False
            if arr[y][x][1] == 1:
                if not (arr[y - 1][x][0] == 1 or arr[y - 1][x + 1][0] == 1 or (x - 1 >= 0 and arr[y][x - 1][1] == 1 and arr[y][x + 1][1] == 1)):
                    return False
    return True





def answer():
    for i in range(110):
        for j in range(110):
            if arr[i][j][0] == 1:
                result.append([j, i, 0])
                arr[i][j][0] = 0
            if arr[i][j][1] == 1:
                result.append([j, i, 1])
                arr[i][j][1] = 0


def build(build_frame):
    for build in build_frame:
        x, y, a, b = build
        if a == 0:  # 기둥
            if b == 0:  # 삭제
                arr[y][x][0] = 0
                if not check():
                    arr[y][x][0] = 1
            elif b == 1:  # 설치
                arr[y][x][0] = 1
                if not check():
                    arr[y][x][0] = 0
        elif a == 1:  # 보
            if b == 0:  # 삭제
                arr[y][x][1] = 0
                if not check():
                    arr[y][x][1] = 1
            elif b == 1:  # 설치
                arr[y][x][1] = 1
                if not check():
                    arr[y][x][1] = 0
    else:
        answer()


def solution(n, build_frame):
    build(build_frame)
    return sorted(result)
        
n = 5
build_frame = [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]

print(solution(n, build_frame))
