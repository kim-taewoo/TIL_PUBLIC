def dfs(now):
    global max_result
    flag = False
    for i in range(n):
        if chk[i]: continue
        if bolts[now][-1] == bolts[i][0]:
            flag = True
            chk[i] = True
            result.append(i)
            dfs(i)
            chk[i] = False
            result.pop()
    if not flag:
        if len(result) > len(max_result):
            max_result = result[:]

T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    bolts = [a[2*i : 2*i+2] for i in range(n)]
    chk = [False] * n
    max_result = []
    result = []
    for i in range(n):
        chk[i] = True
        result.append(i)
        dfs(i)
        chk[i] = False
        result.pop()
    
    print("#{}".format(t), end=" ")
    for i in max_result:
        print(*bolts[i], end=" ")
    print()
    print(chk)