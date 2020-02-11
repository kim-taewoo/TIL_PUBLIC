from itertools import combinations as cb
a = [int(input()) for _ in range(9)]

l = list(cb(a, 7))
for i in l:
    if sum(i) == 100:
        result = sorted(i)
        break
for i in result:
    print(i)