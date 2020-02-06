def chk_danjo(num):
    if num >= 10:
        while num >= 10:
            num, r = divmod(num, 10)
            if not num % 10 <= r:
                return False
    return True

T = int(input())
for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))
  
    max_result = 0
    for i in range(n):
        for j in range(i+1, n):
            m = ns[i] * ns[j]
            if m > max_result:
                if chk_danjo(m):
                    if m > max_result:
                        max_result = m
  
    if max_result == 0:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))