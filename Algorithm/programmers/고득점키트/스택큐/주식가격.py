def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = [(0, prices[0])]
    for i, price in enumerate(prices[1:], start=1):
        while stack:
            top = stack[-1]
            if top[1] > price:
                stack.pop()
                answer[top[0]] = i - top[0]
            else:
                break
        stack.append((i, price))
    while stack:
        top = stack.pop()
        answer[top[0]] = len(prices) - 1 - top[0]
    return answer


prices = [1, 2, 3, 2, 3]
print(solution(prices))
