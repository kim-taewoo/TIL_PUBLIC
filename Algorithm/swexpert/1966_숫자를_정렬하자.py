T = int(input())

for t in range(1, T+1):

    n = int(input())
    a = list(map(int, input().split()))

    print("#{}".format(t), end=" ")
    for i in sorted(a):
        print(i, end=" ")
    print()