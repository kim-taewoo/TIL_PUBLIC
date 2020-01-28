T = int(input())
for t in range(1,T+1):
    n = input()
    if int(n[-1]) % 2:
        print("#{} {}".format(t, 'Odd'))
    else:
        print("#{} {}".format(t, 'Even'))

