import sys
input = lambda: sys.stdin.readline().rstrip()
n, m = map(int, input().split())
matrix = [[0 for _ in range(n)] for _ in range(n)]    # 인접 행렬
# link = {node: [] for node in range(n)}    # 인접 리스트
link = [[] for _ in range(n)]
friendship = []
for _ in range(m):
    a, b = map(int, input().split())
    # 1. 인접 행렬
    # [[]]
    # matrix[a].append(b)
    matrix[a][b] = matrix[b][a] = 1    # 다중할당, 친구는 양방향
    # 2. 인접 리스트
    # key=숫자인 경우 2차원 배열
    # key=문자인 경우 딕셔너리
    link[a].append(b)
    link[b].append(a)
    # 3. edge list: 모든 간선 표현
    friendship.append([a, b])
    friendship.append([b, a])
# print(matrix)
# print(link)
# print(friendship)
for e1 in friendship:
    a, b = e1
    for e2 in friendship:
        c, d = e2
        if a == b or a == c or a == d or b == c or b == d or c == d:
            continue
        if not matrix[b][c]:
            continue
        for e in link[d]:
            if e == a or e == b or e == c or e == d:
                continue
            print(1)