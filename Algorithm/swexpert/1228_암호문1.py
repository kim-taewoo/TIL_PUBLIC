T = 10

for t in range(1, T+1):
    n = int(input())
    a =input().split()
    c = int(input())
    b = input().split()
    i = 0
    while i < len(b):
        idx, n_num = int(b[i+1]), int(b[i+2])

        l = [b[i+3+x] for x in range(n_num)]
        a = a[:idx] + l + a[idx:]

        i += 2 + n_num + 1
    
    print("#{} {}\n".format(t, " ".join(a[:10])))

