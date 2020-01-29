T = int(input())

for t in range(1, T+1):
    n = int(input())
    avg = 0
    for i in range(n):
        p, x = map(float, input().split())
        avg += p * x
    
    print("#{} {}".format(t, avg))
