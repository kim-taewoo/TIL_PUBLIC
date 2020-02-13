T = int(input())
for t in range(1, T+1):
    s = input()
    stack = []
    for i in s:
        if stack and stack[-1] == i:
            while stack and stack[-1] ==i:
                stack.pop()
        else:
            stack.append(i)
    print("#{} {}".format(t, len(stack)))
        