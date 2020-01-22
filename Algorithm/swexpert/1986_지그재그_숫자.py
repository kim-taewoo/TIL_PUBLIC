T = int(input())

for t in range(1, T+1):
    n = int(input())
    result = 0
    for i in range(1, n+1):
        if i % 2 :
            result += i
        else: 
            result -= i

    print("#{} {}".format(t, result))