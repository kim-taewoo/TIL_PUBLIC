T = int(input())

for t in range(1, T+1):
    a = [input() for _ in range(5)]

    max_length = 0
    for i in range(5):
        length = len(a[i])
        if length > max_length:
            max_length = length
    
    print("#{} ".format(t), end ="")
    for i in range(max_length):
        for j in range(5):
            if len(a[j]) - 1 >= i:
                print(a[j][i], end="")
        
