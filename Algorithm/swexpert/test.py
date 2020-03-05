ss = set()
ss.add((1, 2, 3))
ss.add((1, 2, 4))
ss.add((1, 2, 3))

xx = set()
xx.add((5, 6))
xx.add((5, 8))
print(ss|xx)
