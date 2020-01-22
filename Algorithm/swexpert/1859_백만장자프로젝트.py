T = int(input())

for t in range(T):
    n = int(input())
    p_list = list(map(int, input().split()))
    
    result = 0
    max_p = p_list[n-1]
    for i in range(n-1, -1, -1):
        if p_list[i] < max_p:
            result += max_p - p_list[i]
        else:
            max_p = p_list[i]
    print("#{} {}".format(t+1, result))
            