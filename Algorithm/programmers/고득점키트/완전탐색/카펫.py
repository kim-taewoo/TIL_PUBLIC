def solution(brown, yellow):
    ssum = brown + yellow
    for i in range(3, int(ssum**0.5) + 1):
        if ssum % i == 0:
            q = ssum // i
            if (i - 2) * (q-2) == yellow:
                return [q, i]
