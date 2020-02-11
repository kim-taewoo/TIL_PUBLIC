w, h = map(int, input().split())
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

cd, cdist = map(int, input().split())

near = [[],[3,4],[3,4],[1,2],[1,2]]

btw = 0
for d, dist in a:
    if d == cd:
        btw += abs(dist - cdist)
    elif d in near[cd]:
        if d == near[cd][0]:
            btw += cdist
        else:
            if cd == 1 or cd == 2:
                btw += w - cdist
            else:
                btw += h - cdist

        if cd == near[d][0]:
            btw += dist
        else:
            if d == 1 or d == 2:
                btw += w - dist
            else:
                btw += h - dist
    else:
        if cd == 1 or cd == 2:
            lt = cdist + h + dist
            rt = w - cdist + h + w - dist
            btw += min(lt, rt)
        elif cd == 3 or cd == 4:
            lt = cdist + w + dist
            rt = h-cdist + w + h-dist
            btw += min(lt, rt)

print(btw)