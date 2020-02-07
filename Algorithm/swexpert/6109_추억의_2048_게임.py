T = int(input())
for t in range(1, T+1):
    print("#{}".format(t))
    n, d = input().split()
    n = int(n)
    a = [list(map(int, input().split())) for _ in range(n)]
    results = []
    if d == 'right' or d == 'left':
        ll = a
    else:
        ll = list(zip(*a))
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
        if len(result) < n:
            if d == 'left' or d == 'up':
                result += [0] * (n - len(result))
            else:
                result = [0] * (n - len(result)) + list(reversed(result))
        results.append(result)
    if d == 'up' or d == 'down':
        results = zip(*results)
    print('\n'.join(map(lambda t: ' '.join(map(str, t)), results)))