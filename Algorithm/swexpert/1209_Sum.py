T = 10

for _ in range(1, T+1):

    t = int(input())

    max_result = -3000000

    a = [list(map(int, input().split())) for _ in range(100)]

    for r in range(100):
        result = sum(a[r])
        if result > max_result:
            max_result = result

    for c in list(zip(*a)):
        result = sum(c)
        if result > max_result:
            max_result = result
    
    result = 0
    for m in range(100):
        result += a[m][m]
    if result > max_result:
        max_result = result

    result = 0
    for m in range(-1, -100, -1):
        result += a[m][m]
    if result > max_result:
        max_result = result

    print("#{} {}".format(t, max_result))
