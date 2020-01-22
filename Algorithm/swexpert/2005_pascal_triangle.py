T = int(input())

for t in range(1, T+1):
    n = int(input())

    a = [[1] * (i+1) for i in range(n)]

    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i-1][j-1] + a[i-1][j]

    print("#{}".format(t))
    for i in range(n):
        for j in range(i+1):
            print(a[i][j], end=" ")
        print()
    
    
            
        
            
        