def go(num):
    global result, cnt
    while True:
        next = num * 2
        result += str(int(next))
        num = next - int(next)
        cnt += 1
        if num == 0.0:
            return
        if cnt > 13:
            return


T = int(int(input()))
for t in range(1, T+1):
    num = float(input())
    result = ''
    cnt = 0
    go(num)

    if cnt > 13:
        print('#{} {}'.format(t, 'overflow'))
    else:
        print('#{} {}'.format(t, result))
