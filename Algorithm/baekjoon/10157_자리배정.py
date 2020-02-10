C, R = map(int, input().split()) # 7 6
k = int(input())

# 가로 C
# 세로 R
cnt = 0
i = 0
while cnt < k:
    if not i % 2:
        cnt += (R-i)
    else:
        cnt += (C-i)
    i += 1
print(cnt)
print(i)
i -= 1
print(i)