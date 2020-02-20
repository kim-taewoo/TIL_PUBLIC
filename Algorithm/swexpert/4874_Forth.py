for t in range(1, int(input())+1):
    s = input().split()
    opers = {'+':lambda x,y: x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x//y}
    stack = []
    flag = True
    for i in s[:-1]:
        if i not in opers:
            stack.append(int(i))
        else:
            if len(stack) >= 2:
                y, x = stack.pop(), stack.pop()
                stack.append(opers[i](x,y))
            else:
                flag = False
                break
    result = 'error' if not flag or len(stack) > 1 else stack[0]
    print("#{} {}".format(t, result))

