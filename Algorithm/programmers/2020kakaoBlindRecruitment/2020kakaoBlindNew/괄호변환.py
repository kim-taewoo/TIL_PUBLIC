def divide(p):
    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack == 0:
            return [p[:i+1], p[i+1:]]


def chk(p):
    stack = 0
    for i in range(len(p)):
        if p[i] == '(':
            stack += 1
        else:
            stack -= 1
        if stack < 0:
            return False
    return True


def solution(p):
    if not p:
        return ""
    if chk(p):
        return p
    u, v = divide(p)
    if chk(u):
        return u + solution(v)
    return "".join(
        [
            "(", 
            solution(v), 
            ")", 
            ''.join(list(map(lambda x: '(' if x == ')' else ')', u[1:-1])))
        ])