'''
y 좌표의 시작은 y-1 좌표까지의 합 + 1과 같다.

# 그 시작점 이 후 x 좌표가 증가할 때마다 시작점 + (y+1) += 1 의 순으로 커진다.
# 예를 들어 (1,1) 은 sum(1 ~ (1-0)) + 1 즉 0 + 1 이므로 1 이다.
# (2,2) 는 1까지의 합인 1에 1 을 더한 2 가 시작 번호고, x 좌표가 2 이므로 한 칸 오른쪽으로 가면
# y 좌표 + 1 += 0 인 3 이 커져야 하므로 결과 좌표점은 2 + 3 인 5 가 된다.

이제 역변환을 생각해보자.
몇번째 y 좌표에 있는지 유추하고, x 좌표를 증가해가며 찾아낸다.
예를 들어 n 까지의 합은 n(1+n)//2 이다. 5 번을 찾고자 한다면,
2까지의 합이 3, 3까지의 합이 6 이기 때문에  3 번째 줄에 있음을 알 수 있다. (2까지의 합이란 건 2번째 줄 끝점까지 썼음을 말한다.)
3번째 줄의 시작 좌표가 (1 , 3) 이고, 그 시작 좌표의 번호는 4 이다. 우리가 찾는 번호는 5이기 때문에
(1, 3) 에서 대각선 오른쪽 아래 방향으로 한 칸 가는 (+1, -1) 을 해주면 (2, 2) 이다.
'''
def to_coor(num):
    y = 1
    while y*(1+y)//2 < num:
        y += 1
    coor = [1, y]
    n = (y-1)*y//2 + 1
    while n != num:
        n += 1
        coor[0] += 1
        coor[1] -= 1
    return coor


def to_n(coor):
    x, y = coor[0], coor[1]
    n = (y-1)*y//2 + 1
    for i in range(x-1):
        n += ((y+1) + i)
    return n


T = int(input())
for t in range(1, T+1):
    p, q = map(int, input().split())
    p_coor, q_coor = to_coor(p), to_coor(q)
    operated = [p_coor[0] + q_coor[0], p_coor[1] + q_coor[1]]
    result = to_n(operated)
    print("#{} {}".format(t, result))