def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1]) # math.ceil 사용하지 않고 올림 계산법. 음수의 // 값은 더 작아짐을 이용
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]

# 다른 사람 풀이.