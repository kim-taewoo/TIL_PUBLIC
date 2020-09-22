import sys
sys.setrecursionlimit(1000000)


def go(curr, numbers, chk, cnt):
    global maxi
    if cnt == len(numbers):
        maxi = max(maxi, curr)
        return
    if curr[:cnt] >= maxi[:cnt]:
        for idx, num in enumerate(numbers):
            if chk[idx]:
                continue
            chk[idx] = True
            go(curr+num, numbers,chk, cnt + 1)
            chk[idx] = False


maxi = ""
def solution(numbers):
    global maxi
    chk = [False for _ in range(len(numbers))]
    numbers = sorted(list(map(str, numbers)), reverse = True)
    maxi = max(numbers)
    for i in range(len(numbers)):
        chk[i] = True
        go(numbers[i], numbers, chk, 1)
        chk[i] = False
    return maxi


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))
