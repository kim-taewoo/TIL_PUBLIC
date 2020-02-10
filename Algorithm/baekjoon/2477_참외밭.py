k = int(input())

h, v = 0, 0
for i in range(6):
    d, dist = map(int, input().split())
    if d == 4:
        v += dist
    elif d == 3:
        v -= dist
    elif d == 2:
        h -= dist
    else:
        h += dist
