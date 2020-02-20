import sys
min_val = sys.maxsize
max_val = -sys.maxsize
def BT(n):
    # [+, -, X, /]
    global s, min_val, max_val
    if n == N:
        min_val = min(min_val, s)
        max_val = max(max_val, s)
    else:
        for i in range(4):
            if operator[i]:
                if i == 0:
                    operator[i] -= 1
                    s += d[n]
                    BT(n+1)
                    s -= d[n]
                    operator[i] += 1
                elif i == 1:
                    operator[i] -= 1
                    s -= d[n]
                    BT(n+1)
                    s += d[n]
                    operator[i] += 1
                elif i == 2:
                    operator[i] -= 1
                    s *= d[n]
                    BT(n+1)
                    s //= d[n]
                    operator[i] += 1
                else:
                    operator[i] -= 1
                    s //= d[n]
                    BT(n+1)
                    s *= d[n]
                    operator[i] += 1
if __name__ == '__main__':
    N = int(input())
    d = list(map(int,input().split()))
    operator = list(map(int,input().split()))
    s = d[0]
    BT(1)
    print(max_val)
    print(min_val)