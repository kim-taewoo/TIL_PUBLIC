# 실패율: 스테이지에 도달했응나 아직 클리어하지 못한 플레이어 수/스테이지 도달 플레이어 수

# 목적: 실패율이 `높은` 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return


def solution(N, stages):
    stuck = [0 for _ in range(N+2)]
    accu = [0 for _ in range(N+1)]
    for stage in stages:
        stuck[stage] += 1
    for i in range(1, N+1):
        passed = sum(stuck[i:])
        if passed:
            accu[i] = (i, stuck[i] / passed)
        else:
            accu[i] = (i, 0)
    if len(accu) == 2:
        return [accu[1][0]]
    accu = sorted(accu[1:], key=lambda x: (-x[1], x[0]))
    result = [i[0] for i in accu]
    return result


# 다른 사람 풀이. try except 쓰지만 깔끔함

def solution(N, stages):
    fail = {}
    for i in range(1, N+1):
        try:
            fail_ = len([a for a in stages if a == i]) / \
                len([a for a in stages if a >= i])
        except:
            fail_ = 0
        fail[i] = fail_
    answer = sorted(fail, key=fail.get, reverse=True)
    return answer

N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]
print(solution(N, stages))
