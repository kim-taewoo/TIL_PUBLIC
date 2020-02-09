T = 1
for tc in range(1, T+1):
    N = int(input())
    d = input().split('0')
    print(d)
    m = 0
    for data in d:
        if len(data) > m:
            m = len(data)
    print('#{} {}'.format(tc, m))
