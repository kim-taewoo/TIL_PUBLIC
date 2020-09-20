import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    dq = deque()
    for idx in range(len(progresses)):
        timeRemain = math.ceil((100-progresses[idx]) / speeds[idx])
        if len(dq) and timeRemain > dq[0]:
            answer.append(len(dq))
            dq.clear()
        dq.append(timeRemain)
    answer.append(len(dq))
    return answer



progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
print(solution(progresses, speeds))
