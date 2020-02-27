# 속도 개선을 위한 작업
# 처음에는 그냥 max_table 을 작성하면서 동시에 가장 큰 값1, 두번째로 큰 값 2를 리턴 받아서 바로바로 유력 후보로 저장했는데,
# 그럴싸해 보였지만 계속 4 개 테스트 케이스에서 실패하길래 곰곰히 생각해보니 문제가 있었음.
# 가장 큰 값을 고르는 것까지는 성공하겠지만 그 옆에 그보다는 작지만
# 2명을 조합했을 때는 가장 클 수 있는 가능성이 있는 선택지를 선택할 수 없게 됨.

# 아래는 그냥 바이너리 연산을 쓴 잘 짠 사람의 코드
# calc 의 계산이 간지남.


def cal(temp):
    ret = 0
    # 각 원소를 고를지 말지의 조합이므로 2 ** M 개의 조합이 가능하다. 아예 안 고르는 건 말이 안되므로 1부터 시작.
    for i in range(1, (1 << M)):
        tsum = 0
        ttsum = 0
        for j in range(0, M):  # 고를지 말지 선택대상의 인덱스 번호 j
            if i & (1 << j):  # 2의 M 승까지 달리는 중에, 이 인덱스의 원소가 선택되는 경우에(& 연산)
                tsum += temp[j]  # 겹치는 모든 원소 더해주기
                ttsum += temp[j]**2  # 가격 더하기
        if tsum <= C and ret < ttsum:
            ret = ttsum  # 조건에 맞으면 릴리즈

    return ret


for tc in range(1, int(input()) + 1):
    N, M, C = list(map(int, input().split()))
    mat = [0] * N
    for i in range(N):
        mat[i] = list(map(int, input().split()))

    matt = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(N - M + 1):
            matt[i][j] = cal(mat[i][j:j + M])

    mattt = []
    for i in range(N):
        for j in range(N):
            mattt.append(matt[i][j]) # 일차원 리스트에 모두 더하기. 왜? 아래서 조합할거니까.

    ans = 0
    for i in range(len(mattt) - M): # 꼴랑 2개 조합하는 것이므로 dfs 대신 2중 for 문으로 해결
        for j in range(i + M, len(mattt)):
            if ans < mattt[i] + mattt[j]:
                ans = mattt[i] + mattt[j]

    print("#%d" % tc, ans)
