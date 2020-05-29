def swap_recursive(now):
    global max_result

    result = int("".join(a))
    if result > max_result[now]:
        max_result[now] = result
    else: return

    if now == n:
        return

    for i in range(length):
        for j in range(i+1, length):
            a[i], a[j] = a[j], a[i]
            swap_recursive(now+1)
            a[i], a[j] = a[j], a[i]

T = int(input())

for t in range(1, T+1):
    a, n = input().split()
    a = list(a)
    n = int(n)
    length = len(a)
    max_result = [0 for _ in range(n+1)]
    swap_recursive(0)
    print("#{} {}".format(t, max_result[-1]))
