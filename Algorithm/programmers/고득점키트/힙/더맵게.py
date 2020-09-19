import heapq

def solution(scoville, K):
    answer = 0
    heap = scoville
    heapq.heapify(heap)
    while heap[0] < K:
        first, second = heapq.heappop(heap), heapq.heappop(heap)
        new = first + second * 2
        heapq.heappush(heap, new)
        answer += 1
    return answer
