T = int(input())

for t in range(1, T+1):
    s = input()
    mid = len(s) // 2
    pal = True
    for i in range(mid):
        print(s[i], s[len(s)-1-i])
        if s[i] != s[len(s) - 1 - i]:
            pal = False
            break
    if pal:
        print("#{} 1".format(t))
    else:
        print("#{} 0".format(t))
