def isPrime(num):
    if num == 1 or num == 0:
        return False
    for i in range(2, int(num**0.5)+1):
        if not num % i:
            return False
    return True


def go(now, numbers, chk, n, cnt):
    global answer

    if cnt == n+1:
        return

    if now:
        num = int("".join(now))
        if isPrime(num):
            answer.add(num)

    for i in range(n):
        if not chk[i]:
            chk[i] = True
            go(now + [numbers[i]], numbers, chk, n, cnt + 1)
            chk[i] = False

answer = set()
def solution(numbers):
    numbers = list(numbers)
    chk = [False for _ in range(len(numbers))]
    go([], numbers, chk, len(numbers), 0)
    return len(answer)

numbers = "011"
print(solution(numbers))