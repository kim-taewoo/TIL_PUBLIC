w, h = map(int, input().split())
p, q = map(int, input().split()) # 열, 행
t = int(input())

pq = (p + t) // w
qq = (q + t) // h
pr = (p + t) % w
qr = (q + t) % h
if pq % 2:
    p = w - pr
else:
    p = pr
if qq % 2:
    q = h - qr
else:
    q = qr

print(p, q)