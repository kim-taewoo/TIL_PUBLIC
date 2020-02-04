def dfs(chain):
    global max_result
    flag = False
    for i in range(n):
        if chk[i]: continue
        if bolts[chain[-1]][-1] == bolts[i][0]:
            flag = True
            chk[i] = True
            dfs(chain + [i])
            chk[i] = False
    if not flag:
        if len(chain) > len(max_result):
            max_result = chain

T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    bolts = [a[2*i : 2*i+2] for i in range(n)]
    chk = [False] * n
    max_result = []
    for i in range(n):
        chk[i] = True
        dfs([i])
        chk[i] = False
    
    print("#{}".format(t), end=" ")
    for i in max_result:
        print(*bolts[i], end=" ")
    print()