T = int(input())

for t in range(1, T+1):

    n = int(input())

    nums = [0] * 10
    k = 0
    while sum(nums) != 10:
        cur = n * (k+1)
        while cur > 0:
            cur, r = divmod(cur, 10)
            nums[r] = 1
        k+=1
    print("#{} {}".format(t, k * n))