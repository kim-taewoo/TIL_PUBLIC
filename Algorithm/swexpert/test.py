def pick_another(start_r, start_c):
    for r in range(start_c, n):
        for c in range(start_c, n):
            print(r, c)
        start_c = 0

n = 5
pick_another(2, 3)
