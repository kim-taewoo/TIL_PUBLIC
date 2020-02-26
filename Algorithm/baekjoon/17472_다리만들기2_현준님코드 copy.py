def check_island(x, y, n):  # 2번부터 섬 네이밍 + 좌표저장
    if not field[x][y]:
        DFS_island(x, y, n)
        return n + 1
    return n


def DFS_island(x, y, n):
    s = []
    v = []
    s.append((x, y))
    while s:
        x, y = s.pop()
        field[x][y] = n
        v.append((x, y))
        for k in range(4):  # 4방향서치
            nx, ny = x+dx[k], y+dy[k]
            if 0 <= nx <= N-1 and 0 <= ny <= M-1 and (not field[nx][ny]) and (nx, ny) not in v and (nx, ny) not in s:
                s.append((nx, ny))
    lands.append(v)


def check_bridge(n1, n2):
    ret = []
    for x, y in lands[n1]:
        for k in range(4):  # 4방향서치
            temp = []
            i = 1
            while 0 <= x+dx[k]*i <= N-1 and 0 <= y+dy[k]*i <= M-1:  # 경계끝까지
                # 태우: 중간에 다른 섬이 껴있는 경우에 뛰어넘어 갈 수 없으므로 종료해주어야 함. 
                if field[x+dx[k]*i][y+dy[k]*i] >= 2 and field[x+dx[k]*i][y+dy[k]*i] != n2:
                    break
                if field[x+dx[k]*i][y+dy[k]*i] == n1:  # 내 땅을 또 만나면 다음 방향 서치
                    break
                if field[x+dx[k]*i][y+dy[k]*i] == n2:  # 섬과 섬 이어지면, 다리 길이와 함께 저장
                    if (i-1) >= 2 and (not ret or (i-1) < ret[2]):
                        ret = [n1, n2, i-1]  # 섬과 섬 잇는 다리중, 최소 길이 구하기
                    break
                i += 1
    return ret


def getSubset(lst):  # 구해진 다리 후보를 가지고 부분 집합 출력
    n = len(lst)
    ret = []
    for i in range(1 << n):
        temp = []
        for j in range(n):
            t_f = i & (1 << j)
            if t_f:
                temp.append(lst[j])
        else:
            if len(temp) >= len(lands) - 3:  # X(len(lands)-2)의 섬을 잇기 위해선 최소 X-1(len(lands)-3)개 다리 필요
                ret.append(temp)
    return ret


def DFS2(v):  # poten의 다리들로 모든 섬을 연결 할 수 있는 지 >>> 가능하면
    s = []
    res = []
    V = []
    visted = (list(False for _ in range(len(lands))))
    s.append(v)
    while s:
        v = s.pop()
        visted[v] = True
        V.append(v)
        for w in range(2, len(G)):
            if not visted[w] and G[v][w] and w not in s:
                s.append(w)
                res.append((v, w))
    if len(V) >= len(lands)-2:
        return res
    else:
        return None


T = 1  # 제출시 1로, 테스트 케이스 여러개 넣을때 편리하도록 구성
for tc in range(1, T+1):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    N, M = map(int, input().split())
    field = [list(False if x == '1' else True for x in input().split())
             for _ in range(N)]
    lands = [[], []]
    bridges = []
    n = 2
    for x in range(N):
        for y in range(M):
            n = check_island(x, y, n)

    for n1 in range(2, len(lands)-1):
        for n2 in range(n1+1, len(lands)):
            temp = check_bridge(n1, n2)
            if temp:
                bridges.append(temp)
    # 다리들의 모임 완성

    potens = getSubset(bridges)  # 후보군 생성

    result = 1000000
    for poten in potens:
        G = [list(False for _ in range(len(lands))) for _ in range(len(lands))]
        for b in poten:
            G[b[0]][b[1]] = b[2]
            G[b[1]][b[0]] = b[2]

        lst = DFS2(2)  # poten의 다리들로 모든 섬을 연결 할 수 있는 지

        if lst:
            temp_res = 0
            for i1, i2 in lst:
                temp_res += G[i1][i2]
            result = temp_res if 0 < temp_res < result else result
    if result == 1000000:
        print(-1)
    else:
        print(result)
