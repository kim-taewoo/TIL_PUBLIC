def solution(N):
    binaryNum = bin(N)[2:]
    maxi = 0
    cnt = 0
    for i in binaryNum:
        if i == '0':
            cnt += 1
        else:
            if cnt > maxi:
                maxi = cnt
            cnt = 0
    return maxi

print(solution(32))