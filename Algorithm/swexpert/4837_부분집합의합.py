def dfs(level, selected, total):
    global cnt
    if selected == n:
        if total == k:
            cnt += 1
        return
    # if total > n: # 음수 원소가 있어 쓸 수 없는 종료 조건
    #     return
    if 12 - level + 1 < n - selected: 
        return
    
    dfs(level+1, selected+1, total + level) # 선택o
    dfs(level+1, selected, total) # 선택x


T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    cnt = 0
    dfs(1, 0, 0)
    print("#{} {}".format(t, cnt))