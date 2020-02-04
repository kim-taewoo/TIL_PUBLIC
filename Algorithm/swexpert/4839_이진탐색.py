def binary_search(l, r, target):
    cnt = 1
    while l <= r:
        mid = (l + r) // 2
        if mid == target: return cnt
        if mid < target: l = mid
        else: r = mid
        cnt += 1


T = int(input())
for t in range(1, T+1):
    p, pa, pb = map(int, input().split())
    result1, result2 = binary_search(1, p, pa), binary_search(1, p, pb)
    if result1 == result2:
        print("#{} {}".format(t, 0))
    elif result1 > result2:
        print("#{} {}".format(t, 'B'))
    else:
        print("#{} {}".format(t, 'A'))