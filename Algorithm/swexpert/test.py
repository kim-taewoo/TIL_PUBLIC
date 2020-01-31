
d = {}

for i in range(3):
    d[i] = d.get(i, []) + ['xx']

print(d)