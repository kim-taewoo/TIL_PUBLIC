T = int(input())
for t in range(1, T+1):
    n = int(input())
    tasks = []
    for i in range(n):
        s,e = map(int, input().split())
        tasks.append((s,e))
    tasks.sort(key=lambda x:x[1])
    last = 0
    answer = 0
    for i in range(n):
        if last <= tasks[i][0]:
            answer += 1
            last = tasks[i][1]
    print("#{} {}".format(t, answer))