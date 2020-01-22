T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())

    scores = []
    for i in range(n):
        mid, final, homework = map(int, input().split())
        total = 0.35 * mid + 0.45 * final + 0.2 * homework
        scores.append(total)
        if i == k-1:
            target = total
    
    ranks = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'] 
    section = n // 10
    for idx, el in enumerate(sorted(scores, reverse=True)):
        if el == target:
            target_rank = ranks[(idx // section)]
            print("#{} {}".format(t, target_rank))
            break