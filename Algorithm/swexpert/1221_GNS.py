T = int(input())

mapping = {
    "ZRO": 0,
    "ONE": 1,
    "TWO": 2, 
    "THR": 3,
    "FOR": 4,
    "FIV": 5,
    "SIX": 6,
    "SVN": 7,
    "EGT": 8,
    "NIN": 9,
}

for _ in range(1, T+1):
    t, n = input().split()
    a = input().split()
    a = " ".join(sorted(a, key=lambda x: mapping[x]))

    print("{}\n{}".format(t, a))
