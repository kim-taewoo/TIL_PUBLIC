n = int(input())
a = [0] + list(map(int, input().split()))
s_n = int(input())

switch = {0:1, 1:0}

for _ in range(s_n):
    g, num = map(int, input().split())
    if g == 1:
        for i in range(num, n+1, num):
            a[i] = switch[a[i]]
    else:
        a[num] = switch[a[num]]
        i = 1
        while (num - i >= 1) and (num + i <= n) and (a[num - i] == a[num + i]):
            a[num-i], a[num+i] = switch[a[num-i]], switch[a[num+i]]
            i+=1

for idx, el in enumerate(a[1:], start = 1):
    print(el, end=" ")
    if not idx % 20:
        print()