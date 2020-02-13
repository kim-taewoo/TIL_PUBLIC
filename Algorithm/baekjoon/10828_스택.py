import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
stack = []
for i in range(n):
    data = input().split()
    c = data[0]
    if c == 'push':
        stack.append(data[1])
    elif c == 'top':
        if stack:
            print(stack[-1])
        else: print(-1)
    elif c == 'size':
        print(len(stack))
    elif c == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    else:
        if stack:
            print(0)
        else:
            print(1)
