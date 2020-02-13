T = int(input())
for t in range(1, T+1):
    s = input()
    stack = []
    flag = True
    for i in s:
        if i == '(':
            stack.append(1)
        elif i == ')':
            if stack and stack[-1] == 1:
                stack.pop()
            else:
                flag = False
                break
        elif i == '{':
            stack.append(2)
        elif i == '}':
            if stack and stack[-1] == 2:
                    stack.pop()
            else:
                flag = False
                break
    if flag and not stack:
        print("#{} {}".format(t, 1))
    else:
        print("#{} {}".format(t, 0))