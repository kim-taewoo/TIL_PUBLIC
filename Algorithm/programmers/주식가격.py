def solution(prices):
    stack = []
    result = [0 for _ in range(len(prices))]
    for i in range(len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            x = stack.pop()
            result[x] = i - x
        stack.append(i)
    while stack:
        x = stack.pop()
        result[x] = i - x
    return result