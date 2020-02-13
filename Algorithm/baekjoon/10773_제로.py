import sys
input = lambda: sys.stdin.readline().rstrip()

k = int(input())
stack = []
for i in range(k):
    n = int(input())
    if n:
        stack.append(n)
    else:
        stack.pop()

print(sum(stack))