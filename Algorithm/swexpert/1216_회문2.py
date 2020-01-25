T = 10
def chk_ver(x, y):
    for j in reversed(range(x+max_length+1, 101)):
        l = [a[i][y] for i in range(x, j)]
        for i in range(len(l)//2):
            if l[i] != l[-1-i]:
                return 0
        return len(l)


def chk_hor(x,y):
    for j in reversed(range(y+max_length+1, 101)):
        l = a[x][y:j]
        for i in range(len(l)//2):
            if l[i] != l[-1-i]:
                return 0
        return len(l)


for _ in range(1, T+1):
    t = int(input())

    a = [list(input()) for _ in range(100)]

    max_length = 0
    for r in range(100):
        for c in range(100):
            if 100-r > max_length :
                chk = chk_ver(r, c)
                if chk > max_length:
                    max_length = chk
            if 100-c > max_length:
                chk = chk_hor(r, c)
                if chk > max_length:
                    max_length = chk

    print("#{} {}".format(t, max_length))
