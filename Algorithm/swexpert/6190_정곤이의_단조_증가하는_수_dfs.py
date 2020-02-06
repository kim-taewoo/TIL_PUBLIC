# dfs & 백트래킹 패스 코드
def chk_danjo(num):
    while num >= 10:
        num, r = divmod(num, 10)
        if not num % 10 <= r:
            return False
    return True
def dfs(level):
    global max_result
    if len(selected) == 2: # 종료조건 1
        if not chk[selected[0]][selected[1]]:
            chk[selected[0]][selected[1]] = True
            product = ns[selected[0]] * ns[selected[1]]
            if product < max_result:
                return
            if chk_danjo(product):
                max_result = product
        return
    if level == n: # 종료조건 2
        return
    # 현재 level(노드) 선택 o
    selected.append(level)
    dfs(level+1)
    selected.pop() # 백트래킹
    # 현재 level(노드) 선택 x
    dfs(level+1)
T = int(input())
for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))
    chk = [[0] * n for _ in range(n)]
    max_result = 0
    selected = []
    dfs(0)
    if max_result < 10:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))