def solution(stones, k):
    stones = [[idx, i] for idx, i in enumerate(stones)]
    stones.sort(key=lambda x: x[1])
    friends = 1
    while True:
        i = 0
        idxs = []
        while stones[i][1] - friends <= 0:
            idxs.append(stones[i][0])
            i += 1
        idxs.sort()
        print(idxs)
        accu = 1
        found = False
        for i in range(1, len(idxs)):
            if idxs[i] - idxs[i-1] == 1:
                accu += 1
                if accu == k:
                    found = True
                    break
            else:
                accu = 1
        if found:
            answer = friends
            break

        friends += 1

    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(solution(stones, k))
