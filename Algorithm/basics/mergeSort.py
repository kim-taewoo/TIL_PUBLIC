def mergeSort(lt, rt):
    global a
    global tmp

    if lt < rt: # rt <= lt 이면 종료
        mid = (lt + rt) // 2
        mergeSort(lt, mid) # 분할
        mergeSort(mid+1, rt) # 분할

        # 해결
        p1 = lt # 포인터1
        p2 = mid + 1 # 포인터2
        p3 = lt # 포인터 3
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

    #  병합정렬 응용 풀이
    mergeSort(0, n-1)
    print("#{} {}".format(t, a[n-1] - a[0]))