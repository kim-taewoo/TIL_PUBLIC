T = int(input())
for t in range(1, T+1):
    print("#{}".format(t))
    n, d = input().split()
    n = int(n)
    ll = [list(map(int, input().split())) for _ in range(n)]
    if d == 'up' or d == 'down':
        ll = zip(*ll)
    results = []
    for j in ll:
        result = []
        c1 = 0
        if d == 'left' or d == 'up':
            direction = j
        else:
            direction = reversed(j)
        for i in direction: 
            if i:
                if not c1: 
                    c1 = i
                else:
                    if c1 == i:
                        result.append(c1*2)
                        c1 = 0
                    else: 
                        result.append(c1)
                        c1 = i
        if c1: 
            result.append(c1)
        shorter = n - len(result)
        if shorter:
            if d == 'left' or d == 'up':
                result += [0] * shorter
            else:
                result = [0] * shorter + list(reversed(result))
        results.append(result)
    if d == 'up' or d == 'down':
        results = zip(*results)
    print('\n'.join(map(lambda t: ' '.join(map(str, t)), results)))