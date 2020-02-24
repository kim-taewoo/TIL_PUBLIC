n = int(input())
relationship = [list() for _ in range(n+1)]  # 인덱스 번호 맞춰주기
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    relationship[x].append(y)
    relationship[y].append(x)

rank = [0 for _ in range(n+1)]
min_rank = 2147000000
for i in range(1, n+1):
    all_chk = [False for _ in range(n+1)]
    all_chk[i] = True
    now = relationship[i]
    for j in now:
        all_chk[j] = True
    depth = 1
    while True:
        # print(all_chk)
        if all(all_chk[1:]):
            rank[i] = depth
            if depth < min_rank:
                min_rank = depth
            break
        now = [y for x in now for y in relationship[x]]
        for j in now:
            all_chk[j] = True
        depth += 1

result = [x for x in range(1, n+1) if rank[x] == min_rank]
print(min_rank, len(result))
print(*result)
