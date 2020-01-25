T = 1

for _ in range(1, T+1):
    t = int(input())

    a = [list(input()) for _ in range(100)]

    max_length = 0
    for r in range(100):
        for c in range(100):
            if 100 - r > max_length:
                


    print("#{} {}".format(t, max_length))
