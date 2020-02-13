T = int(input())
for t in range(T):
    s = input()
    flag = True
    cnt = 0
    for i in s:
        if i == '(': 
            cnt += 1
        else: cnt -= 1
        if cnt < 0:
            flag = False
            break
    
    if cnt:
        flag = False
    
    if flag: print("YES")
    else: print("NO")