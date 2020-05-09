T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    containers = list(map(int, input().split()))
    truckCapa = list(map(int, input().split()))
    containers.sort(reverse = True)
    truckCapa.sort(reverse = True)
    answer = 0
    i = j = 0
    for x in range(m):
        if j >= n:
            break
        if truckCapa[i] >= containers[j]:
            answer += containers[j]
            i += 1
            j += 1
        else:
            j += 1
    print('#{} {}'.format(t, answer))
