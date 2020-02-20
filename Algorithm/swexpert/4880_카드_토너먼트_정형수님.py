import math

def rcp(a, b):
    if a[1]==b[1]:
        return a if a[0] <  b[0] else b
    if 1 not in [a[1], b[1]]:
        return a if a[1]==3 else b
    if 2 not in [a[1], b[1]]:
        return a if a[1]==1 else b
    if 3 not in [a[1], b[1]]:
        return a if a[1]==2 else b

    
def go(a):
    if len(a) == 1: return a[0]
    
    mid = math.ceil(len(a)/2)
    return rcp(go(a[:mid]), go(a[mid:]))


t = int(input())

for tc in range(1, 1+t):
    n = int(input())
    a = list(map(int, input().split()))
    a = [(i+1, a[i]) for i in range(n)]
    print('#{} {}'.format(tc, go(a)[0]))