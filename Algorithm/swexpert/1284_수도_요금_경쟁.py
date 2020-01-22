T = int(input())

for t in range(1, T+1):
    p, q, r, s, w = map(int, input().split())
    a_price = w * p
    if (w-r) > 0:
        b_price = q + (w-r) * s
    else: 
        b_price = q
    if a_price > b_price:
        print("#{} {}".format(t, b_price))
    else:
        print("#{} {}".format(t, a_price))
