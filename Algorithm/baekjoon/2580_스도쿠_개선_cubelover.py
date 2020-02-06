a = [list(map(int, input().split())) for _ in range(9)]
b = [[0 for _ in range(9)] for _ in range(9)] # 가로 1~9 체크맵
c = [[0 for _ in range(9)] for _ in range(9)] # 세로 1~9 체크맵
d = [[0 for _ in range(9)] for _ in range(9)] # 사각형 1~9 체크맵
for i in range(9):
    for j in range(9):
        # 맵들 미리 채우고 시작하기.
        if a[i][j]:
            b[i][a[i][j] - 1] = 1
            c[j][a[i][j] - 1] = 1
            d[i // 3 * 3 + j // 3][a[i][j] - 1] = 1
def f(x, y): # x 가 행, y 가 열
    if x == 9: # 9 * 9 스도쿠 맵 순회 끝 (행의 인덱스가 8까지인데 9라는 건 다 돌았다는 뜻.)
        return True
    if y == 9: # 컬럼이 꽉 찼으면 한 행 넘어가고 컬럼 초기화
        return f(x + 1, 0)
    if a[x][y]:
        return f(x, y + 1) # 0 이 아니라면 한 칸 전진
    for i in range(9):
        if not b[x][i] and not c[y][i] and not d[x // 3 * 3 + y // 3][i]: # 그 어떤 맵에서도 체크되지 않은 숫자일 때(삽입 가능성이 있는 숫자)
            b[x][i] = 1
            c[y][i] = 1
            d[x // 3 * 3 + y // 3][i] = 1
            # 모든 맵에 다 체크하고 달리기 시작
            if f(x, y + 1):
                a[x][y] = i + 1 # i 가 인덱스였으니 1 더해줘서 넣어야 함
                return True
            b[x][i] = 0
            c[y][i] = 0
            d[x // 3 * 3 + y // 3][i] = 0
            # 백트래킹
    return False
f(0, 0)
print('\n'.join(map(lambda t: ' '.join(map(str, t)), a)))