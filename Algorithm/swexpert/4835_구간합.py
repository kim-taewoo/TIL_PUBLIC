T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    
    min_result = 1000 * m
    max_result = 0
    
    for i in range(n-m+1):
        tmp = 0
        for j in range(i, i+m):
            tmp += a[j]
        if tmp > max_result:
            max_result = tmp
        if tmp < min_result:
            min_result = tmp
    
    print(max_result - min_result)