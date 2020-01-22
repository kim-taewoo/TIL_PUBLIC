T = int(input())
primes = [2,3,5,7,11]
for t in range(1, T+1):
    print("#{}".format(t), end=" ")
    n = int(input())
    for p in primes:
        tmp = n
        cnt = 0
        while not tmp % p:
            tmp //= p
            cnt += 1
        print(cnt, end=" ")
    print()
