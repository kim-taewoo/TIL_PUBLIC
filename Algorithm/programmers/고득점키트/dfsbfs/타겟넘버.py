def go(now, numbers, target, idx):
    global answer

    if idx == len(numbers):
        if now == target:
            answer += 1
        return

    go(now + numbers[idx], numbers, target, idx + 1)
    go(now - numbers[idx], numbers, target, idx+1)


answer = 0


def solution(numbers, target):
    go(0, numbers, target, 0)
    return answer
