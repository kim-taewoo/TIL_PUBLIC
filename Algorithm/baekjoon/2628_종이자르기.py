m,n = map(int,input().split())

x = int(input())
vers = [0]
hors = [0]
for i in range(x):
    d, idx = map(int, input().split())
    if d:
        vers.append(idx)
    else:
        hors.append(idx)
vers = sorted(vers) + [m]
hors = sorted(hors) + [n]

diff_v = []
diff_h = []
for i in range(1, len(vers)):
    diff_v.append(vers[i] - vers[i-1])
for i in range(1, len(hors)):
    diff_h.append(hors[i] - hors[i-1])

maxi = 0
for i in diff_v:
    for j in diff_h:
        mul = i * j
        if mul > maxi: maxi = mul
print(maxi)