n = int(input())
for i, c in enumerate(range(n), start=1):
    t = list(map(int, input().split()))
    if t[2] > t[1]:
        print('#{} -1'.format(i))
    elif t[2] >= t[0]:
        print('#{} 0'.format(i))
    else:
        print('#{} {}'.format(i, t[0]-t[2]))
