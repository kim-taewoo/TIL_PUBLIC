T = int(input())

days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1,T+1):
    m,d = map(int, input().split())
    day = sum(days[:m-1]) + d - 1

    r = (day % 7 + 4) % 7

    print("#{} {}".format(t, r))