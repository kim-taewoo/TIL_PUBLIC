n = int(input())

for x in range(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    an, al = a[0], a[1:]
    bn, bl = b[0], b[1:]
    ac = [0 for _ in range(5)]
    bc = [0 for _ in range(5)]
    for i in al:
        ac[i] += 1
    for i in bl:
        bc[i] += 1

    flag = False
    for i in range(4, 0, -1):
        if ac[i] > bc[i]:
            print('A')
            flag = True
            break
        elif ac[i] < bc[i]:
            print('B')
            flag = True
            break
    if not flag:
        print("D")

        
