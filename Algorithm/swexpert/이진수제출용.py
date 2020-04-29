T = int(input())
for t in range(1, T+1):
    l, s = input().split()
    print("#{}".format(t), end=" ")
    for i in s:
        print("{:04b}".format(int(i, 16)), end="")
    print()
