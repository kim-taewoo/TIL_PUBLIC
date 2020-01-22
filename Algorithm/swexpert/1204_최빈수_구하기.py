T = int(input())

for t in range(1, T+1):
    n = int(input())

    scores = list(map(int, input().split()))
    score_dict = {}

    for s in scores:
        score_dict[s] = score_dict.get(s, 0) + 1
    
    max_v = 0
    ks = []
    for k, v in score_dict.items():
        if v > max_v:
            max_v = v
            ks = [k]
        elif v == max_v:
            ks.append(k)

    print("#{} {}".format(t, max(ks)))