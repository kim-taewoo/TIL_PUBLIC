T = int(input())

for t in range(1, T+1):
    a = list(map(int, input().split()))
    result = sum([i for i in a if i!=max(a) and i!=min(a)])
    print("#{} {}".format(t, round(result/8)))