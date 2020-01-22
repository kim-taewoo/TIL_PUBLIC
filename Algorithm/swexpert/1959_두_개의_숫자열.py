T = int(input())

for t in range(1, T+1):

    n, m = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    if n < m :
        s,l = a,b
    else:
        s,l = b,a
    
    max_result = 0
    for i in range(len(l) - len(s) +1):
        result = 0
        for j in range(len(s)):
            result += s[j] * l[j+i]
        if max_result < result:
            max_result = result
    print("#{} {}".format(t, max_result))

    