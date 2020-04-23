def solution(s):
    answer = []
    sets = []
    s = s[1:-1]
    stack = ""
    opened = False
    for i in s:
        if i == '{':
            opened = True
        elif i == '}':
            nums = set(map(int, stack.split(',')))
            sets.append(nums)
            stack = ""
            opened = False
        else:
            if opened:
                stack += i
    sets = sorted(sets, key=lambda x: len(x))
    answer = [list(sets[0])[0]]
    for i in range(1, len(sets)):
        answer.append(list(sets[i] - sets[i-1])[0])
        
    return answer


s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))

print(s.lstrip('{'))
