from itertools import combinations

T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    subsets = combinations(range(1, 13), n)

    # cnt = 0
    # for subset in subsets:
    #     if sum(subset) == k:
    #         cnt += 1
    cnt = sum(1 for subset in subsets if sum(subset) == k)
    print("#{} {}".format(t, cnt))