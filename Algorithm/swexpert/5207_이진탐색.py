T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    ans = 0
    for i in b:
        lt = 0
        rt = n-1
        pre = None
        while lt <= rt:
            mid = (lt+rt) // 2
            if a[mid] == i:
                ans += 1
                break
            elif a[mid] > i:
                if pre == 1:
                    break
                pre = 1
                rt = mid - 1
            else:
                if pre == 0:
                    break
                pre = 0
                lt = mid + 1

    print(f'#{t} {ans}')
