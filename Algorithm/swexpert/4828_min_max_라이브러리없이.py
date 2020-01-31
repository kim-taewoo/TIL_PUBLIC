def mergeSort(lt, rt):
    global a
    global tmp

    if lt < rt: # 종료
        mid = (lt + rt) // 2
        mergeSort(lt, mid) # 분할
        mergeSort(mid+1, rt) # 분할

        # 해결
        p1 = lt
        p2 = mid + 1
        p3 = lt
        while p1 <= mid and p2 <= rt:
            if a[p1] < a[p2]:
                tmp[p3] = a[p1]
                p1 += 1
            else:
                tmp[p3] = a[p2]
                p2 += 1
            p3 += 1
        while p1 <= mid:
            tmp[p3] = a[p1]
            p1 += 1
            p3 += 1
        while p2 <= rt:
            tmp[p3] = a[p2]
            p2 += 1
            p3 += 1
        for i in range(lt, rt+1):
            a[i] = tmp[i]


T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    tmp = [0] * n

    #  병합정렬
    mergeSort(0, n-1)
    print("#{} {}".format(t, a[n-1] - a[0]))