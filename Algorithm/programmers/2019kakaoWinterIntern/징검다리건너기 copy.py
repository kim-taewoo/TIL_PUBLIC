def solution(stones, k):
    answer = 0
    maxi = max(stones)
    lt = 1
    rt = maxi
    while lt <= rt:
        mid = (lt + rt) // 2
        # print(mid)
        found = False
        accu = 0
        for s in stones:
            if s - mid <= 0:
                accu += 1
                if accu >= k:
                    found = True
                    break
            else:
                accu = 0

        if found:
            answer = mid
            rt = mid - 1
        else:
            lt = mid + 1

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones, k))
