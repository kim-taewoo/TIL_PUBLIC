n,k = map(int, input().split())
a = list(map(int, input().split()))

i1 = 0
i2 = k-1
maxi = sum(a[i1:i2+1])
now = sum(a[i1:i2+1])
while i2 < n-1:
    i2+=1
    now = now - a[i1] + a[i2]
    if now > maxi:
        maxi = now
    i1 += 1
print(maxi)