# 시간초과 뜸.
def chk_danjo(num):
    while num > 0:
        num, r = divmod(num, 10)
        if not num % 10 <= r:
            return False
    return True

def dfs(level, selected, product):
    global max_result
    if selected == 2:
        if product < max_result: return
        if chk_danjo(product):
            max_result = product
            return
    if level == n: 
        return
    dfs(level+1, selected + 1, product * ns[level])
    dfs(level+1, selected, product)

T = int(input())
for t in range(1, T+1):
    n = int(input())
    ns = list(map(int, input().split()))

    max_result = 0
    dfs(0, 0, 1)

    if max_result == 0:
        print("#{} {}".format(t, -1))
    else:
        print("#{} {}".format(t, max_result))
            