import sys
# sys.stdin = open('input.txt')
dy = [0] * 50


def dfs(n):
    if dy[n]:
        return dy[n]
    if n == 1 or n == 2:
        return n
    dy[n] = dfs(n-1) + dfs(n-2)
    return dy[n]

length = int(input())


print(dfs(length))
