import heapq

def solution(jobs):
    n = len(jobs)
    heap = jobs
    heapq.heapify(heap)
    total_time_cost = 0
    time = 0
    while heap:
        works = []
        if heap[0][0] > time:
            time = heap[0][0]
        while heap and heap[0][0] <= time:
            s, cost = heapq.heappop(heap)
            heapq.heappush(works, (cost, s))
        while works:
            cost, s = heapq.heappop(works)
            time += cost
            total_time_cost += (time - s)

    answer = total_time_cost // n
    return answer


jobs = [[0, 10], [4, 10], [5, 11], [15, 2]]
print(solution(jobs))
