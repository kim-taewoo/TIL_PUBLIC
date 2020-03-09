T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    scores = set()
    for i in range(0, 1 << n):
        score = 0
        for j in range(n):
            if i & (1 << j):
                score += a[j]
        scores.add(score)
    print("#{} {}".format(t, len(scores)))