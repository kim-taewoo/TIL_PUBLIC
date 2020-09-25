from collections import deque

def solution (numbers, target):
    answer = 0
    queue = deque([[numbers[0], 0], [-numbers[0], 0]])
    while queue:
        now = queue.popleft()
        if now[1] == len(numbers) - 1: 
            if now[0] == target: 
                answer += 1
            
            continue
        
        queue.append([now[0] + numbers[now[1] + 1], now[1] + 1])
        queue.append([now[0] - numbers[now[1] + 1], now[1] + 1])
    
    return answer


numbers = [1, 1, 1, 1, 1]
target = 3
print(solution(numbers, target))
