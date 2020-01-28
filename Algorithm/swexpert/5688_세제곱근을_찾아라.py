T = int(input())

for t in range(1, T+1):
    n = int(input())
    result = 0
    for i in range(1, int(n ** (1/3))+2):
        if i ** 3 == n:
            result = i
            break
    
    if result:
        print("#{} {}".format(t, result))
    else:
        print("#{} {}".format(t, -1))
