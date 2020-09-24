def validate(now, toChk):
    cnt = 0
    for i in range(len(now)):
        if now[i] != toChk[i]:
            cnt += 1
        if cnt > 1:
            return False
    return True


def go(now, target, chk, words, cnt):
    global mini

    if cnt > len(words):
        return

    if now == target:
        mini = min(mini, cnt)
        return

    for i in range(len(words)):
        if not chk[i]:
            if validate(now, words[i]):
                chk[i] = True
                go(words[i], target, chk, words, cnt+1)
                chk[i] = False


mini = 2147000000


def solution(begin, target, words):
    chk = [False for _ in range(len(words))]
    go(begin, target, chk, words, 0)
    if mini == 2147000000:
        return 0
    return mini

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
print(solution(begin, target, words))
