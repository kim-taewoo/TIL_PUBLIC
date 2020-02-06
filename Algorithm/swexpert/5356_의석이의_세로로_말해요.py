T = int(input())
for t in range(1, T+1):
    print("#{} ".format(t), end ="")
    a = [input() for _ in range(5)]
    while a:
        zipped = list(zip(*a))
        length = len(zipped)
        for i in zipped:
            print("".join(i), end="")
        a = [i[length:] for i in a if i[length:]]
    print()