w, h = map(int, input().split())
p, q = map(int, input().split()) # 열, 행
t = int(input())

dc = [1, -1, -1, 1] # 오위, 왼위, 왼아, 오아
dr = [1, 1, -1, -1]

time = 0
d = 0
while True:
    if time == t:
        print(p, q)
        break
    p, q = p + dc[d], q + dr[d]
    if p == w:
        if d == 0:
            d = 1
        elif d == 3:
            d = 2
    elif p == 0:
        if d == 1:
            d = 0
        elif d == 2:
            d = 3
    elif q == h:
        if d == 1:
            d = 2
        elif d == 0:
            d = 3
    elif q == 0:
        if d == 2:
            d = 1
        elif d == 3:
            d = 0
    time += 1
