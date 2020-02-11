n = int(input())
a = list(map(int, input().split()))

max_inc_length = 1
length = 1
for i in range(1, n):
    if a[i] >= a[i-1]:
        length += 1
        if length > max_inc_length: max_inc_length = length
    else:
        length = 1
max_dec_length = 1
length = 1
for i in range(1, n):
    if a[i] <= a[i-1]:
        length += 1
        if length > max_dec_length: max_dec_length = length
    else:
        length = 1

print(max(max_dec_length, max_inc_length))