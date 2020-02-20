def RCP(lt, rt):
    if lt < rt: # lt >= rt 이면 분할 종료 (1개 짜리면 종료)
        mid = (lt + rt) // 2
        RCP(lt, mid)   # 분할
        RCP(mid+1, rt) # 분할
        if a[mid] == a[rt]:
            tmp[rt] = tmp[mid]
            a[rt] = a[mid]
        else:
            if (a[mid]+1) % 3 == a[rt]:
                tmp[rt] = tmp[rt]
                a[rt] = a[rt]
            else:
                tmp[rt] = tmp[mid]
                a[rt] = a[mid]


for t in range(1, int(input())+1):
    n = int(input())
    a = [x-1 for x in list(map(int, input().split()))]
    tmp = [i for i in range(1,n+1)]
    RCP(0, n-1)
    print("#{} {}".format(t, tmp[-1]))