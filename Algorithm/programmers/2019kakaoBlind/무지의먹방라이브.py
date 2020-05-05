# 시간초과
def solution(food_times, k):
    idx = 0
    while k:
        if idx >= len(food_times):
            idx = idx % len(food_times)
        if food_times[idx] != 0:
            food_times[idx] -= 1
            k -= 1
        idx += 1

    cnt = 0
    while cnt <= len(food_times):
        if idx >= len(food_times):
            idx = idx % len(food_times)
        if food_times[idx]:
            return idx+1
        idx += 1
        cnt += 1
        
    return -1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
