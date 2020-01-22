T = int(input())

days= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

for t in range(1, T+1):

    m1, d1, m2, d2 = map(int, input().split())

    day = 0
    for i in range(m1, m2):
        day += days[i]

    day += (d2 - d1) + 1
    print("#{} {}".format(t, day))
