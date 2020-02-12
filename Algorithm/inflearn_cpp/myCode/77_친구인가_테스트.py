n, m = map(int, input().split())
l = []
for x in range(m):
    l.append(list(map(int, input().split())))

d = {}
for i in l:
    d[i[0]] = d.get(i[0], 0) + 1
    if d.get(i[0], 0) == 2:
        print(i)
        break