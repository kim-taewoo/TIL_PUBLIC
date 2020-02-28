T = int(input())
for t in range(1, T+1):
    n, b = map(int, input().split())
    hs = list(map(int, input().split()))
    mini = 2147000000
    for i in range(1, (1 << n)):
        sum_height = 0
        for j in range(0, n):  # 고를지 말지 선택대상의 인덱스 번호 j
            if i & (1 << j):  # 2의 M 승까지 달리는 중에, 이 인덱스의 원소가 선택되는 경우에(& 연산)
                sum_height += hs[j]  # 겹치는 모든 원소 더해주기
            if sum_height > mini:
                break
        if sum_height >= b and sum_height < mini:
            mini = sum_height  # 조건에 맞으면 릴리즈
        if sum_height == b:
            break
    print("#{} {}".format(t, mini - b))
