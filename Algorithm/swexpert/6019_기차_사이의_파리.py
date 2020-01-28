T = int(input())

for t in range(1, T+1):
    d, a, b, f = map(int, input().split())
    time = d / (a+b)
    result = time * f
    print("#{} {}".format(t, result))