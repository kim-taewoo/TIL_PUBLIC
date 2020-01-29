T = int(input())

for t in range(1,T+1):
    n, k = map(int, input().split())

    chk = [False] * (n+1)

    a = list(map(int, input().split()))

    for i in a:
        chk[i] = True
    
    result = " ".join(map(str,[i for i,el in enumerate(chk[1:], start = 1) if not el]))

    print("#{} {}".format(t, result))

