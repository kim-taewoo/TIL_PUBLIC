from functools import reduce

def solution(bridge_length, weight, truck_weights):
    Q = [[truck_weights[0], 0]]
    timer = 1
    i = 1
    while Q:
        top = Q[0]
        if top[1] + bridge_length == timer:
            Q.pop(0)
        weight_sum = reduce(lambda acc, curr: acc+curr[0], Q, 0)
        if i < len(truck_weights) and weight_sum + truck_weights[i] <= weight:
            Q.append([truck_weights[i], timer])
            i += 1
        timer += 1

    return timer


bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

print(solution(bridge_length, weight, truck_weights))
