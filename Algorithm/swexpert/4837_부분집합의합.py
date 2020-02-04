def dfs(level, el_cnt, total):
    # 종료, 분할, 해결
    global cnt
    if el_cnt == n:
        if total == k:
            cnt += 1 #해결
        return
    # if total > n: # 음수 원소가 있으면 쓸 수 없는 조건
    #     return
    if 12 - level + 1 < n - el_cnt: 
        return
    
    dfs(level+1, el_cnt+1, total + level) #분할
    dfs(level+1, el_cnt, total) #분할


T = int(input())
for t in range(1, T+1):
    n, k = map(int, input().split())
    cnt = 0
    dfs(1, 0, 0)
    print("#{} {}".format(t, cnt))