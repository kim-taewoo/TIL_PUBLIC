# 조항래 님 코드

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())//10
    l= [0,1,3]
    i=3
    while i <=n:
        l.append(l[i-1]+2 * l[i-2])
        i+=1
    print('#{} {}'.format(test_case, l[n]))