n, m, q = map(int, input().split()) 

a = [input().split() for _ in range(q)]

b = [[0]*(m+1) for _ in range(n+1)] # 팀 && 문제번호 & 시간 측정용
b_chk = [[False]*(m+1) for _ in range(n+1)] # 팀 && 문제번호 & 맞춘문제 확인용

for time, team, question, result in a:
    time, team, question = int(time), int(team), int(question)
    if not b_chk[team][question]:
        if result == 'AC':
            b[team][question] += time
            b_chk[team][question] = True
        else:
            b[team][question] += 20

final_list = []
for i in range(1, n+1):
    nn = 0 # 맞춘문제 개수
    tt = 0 # 맞춘 문제에 걸린 시간 (페널티 포함)
    for j in range(1, m+1):
        if b_chk[i][j]:
            nn += 1
            tt += b[i][j]
    final_list.append([i, nn, tt])

final_list = sorted(final_list, key=lambda x: (-x[1], x[2], x[0]))
for tn, nn, tt in final_list:
    print(tn, nn, tt)