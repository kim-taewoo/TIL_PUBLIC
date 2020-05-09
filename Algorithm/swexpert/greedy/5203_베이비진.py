T = int(input())

def chk(lst):
    cnt = 1
    for i in range(1, len(lst)):
        if lst[i] - lst[i-1] == 1:
            cnt += 1
            if cnt == 3:
                return True
        else:
            cnt = 1
    return False

def go(p, i, a):
    p[a[i]] = p.get(a[i], 0) + 1
    if p[a[i]] == 3:
        return True
    if len(p.keys()) >= 3 and chk(sorted(list(p.keys()))):
        return True
    return False


for t in range(1, T+1):
    a = list(map(int, input().split()))
    p1 = {}
    p2 = {}
    winner = 0
    for i in range(12):
        if i % 2:
            flag = go(p2, i, a)
            if flag: 
                winner = 2
                break
        else:
            flag = go(p1, i, a)
            if flag: 
                winner = 1
                break

    print("#{} {}".format(t, winner))
