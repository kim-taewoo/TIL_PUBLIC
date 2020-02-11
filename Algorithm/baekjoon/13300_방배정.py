n,k = map(int,input().split())
students = [[0 for _ in range(7)] for __ in range(2)]
for i in range(n):
    g, y = map(int, input().split())
    students[g][y] += 1

cnt = 0
for i in students:
    for j in i:
        q, r = divmod(j, k)
        cnt += q
        if r: 
            cnt += 1
print(cnt)