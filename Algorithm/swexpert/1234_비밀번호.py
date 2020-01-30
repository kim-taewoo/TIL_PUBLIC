T = 10

for t in range(1, T+1):

    n, s = input().split()
    n = int(n)
    s = list(s)

    while True:
        flag = False
        i = 1
        while i < n:
            if s[i-1] == s[i]:
                flag = True
                s = s[:i-1] + s[i+1:]
                n -= 2
            else: 
                i += 1
        if not flag:
            break

    result = "".join(s)

    print("#{} {}".format(t, result))