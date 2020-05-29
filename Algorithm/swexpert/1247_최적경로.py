# visited 는 현재까지 방문한 고객들을 비트연산의 1로 표현한 것으로,
# 맨 처음은 00000001 같이 0번째만 1인 상태로 시작한다.
def f(now, visited):
    global res
    # 1번째(집) 을 제외하고 모든 곳을 방문한 경우.
    # 고객 수 n 명에 회사, 집까지 n + 2 개인데, 
    # 2진수의 특성상 만약 n == 2 라면
    # 총 n+2 개를 1번째(집) 외에 모두 방문했다면
    # 1101 의 형태가 되고, 이것은 2**4 - 1 - 2**1 이다.
    if visited == 2**(n+2)-1-2:
        res = min(res, cache[now][visited] + dist_map[now][1])
        return

    for i in range(2, n+2):
        # 아직 i 번째 고객을 방문하지 않았다면
        if (1 << i) & visited == 0:
            # 현재까지의 visited 비트 상태의 경로 길이에 지금 i 번째 고객으로 가는 거리를 더한 게,
            # 이미 cache 에 저장되어 있는 i 까지 도달한 상태의 길이보다 짧다면
            # 갱신해준다.
            new_dist = cache[now][visited]+dist_map[now][i]
            current_mini = cache[i][visited | (1 << i)]
            if new_dist < current_mini:
                cache[i][visited | (1 << i)] = new_dist
                f(i, visited | (1 << i))


T = int(input())
for t in range(1, T+1):
    n = int(input())
    coors = list(map(int, input().split()))
    coors = [(coors[i*2], coors[i*2+1]) for i in range(n+2)]

    dist_map = [[0]*(n+2) for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            calc = abs(coors[i][0]-coors[j][0]) + abs(coors[i][1]-coors[j][1])
            dist_map[i][j] = calc
            dist_map[j][i] = calc

    res = 2147000000
    cache = [[2147000000] * (2**(n+2)) for _ in range(n+2)]
    cache[0][1] = 0

    f(0, 1)
    print('#{} {}'.format(t, res))
