T = int(input())

for t in range(1,T+1):
    n = int(input())
    s = input().split()
    print("#{}".format(t), end="")
    cnt = 0
    for i in s:
        if i[-1] == '.' or i[-1] == '?' or i[-1] == '!':
            if 65 <= ord(i[0]) <= 90: 
                flag = True
                for j in i[1:-1]:
                    if not 97 <= ord(j) <= 122: 
                        flag = False
                        break
                if flag :
                    cnt += 1
            print(" {}".format(cnt), end="")
            cnt = 0
            continue

        if not 65 <= ord(i[0]) <= 90: continue

        flag = True
        for j in i[1:]:
            if not 97 <= ord(j) <= 122: 
                flag = False
                break
        if flag :
            cnt += 1
    print()