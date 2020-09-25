def solution(distance, rocks, n):
    rocks.append(distance)
    lt = 0
    rt = distance
    while lt <= rt:
        mid = (lt+rt)//2
        for i in range(1, len(rocks)):
            if rocks[i] - rocks[i-1] < mid:
                

    answer = 0
    return answer
