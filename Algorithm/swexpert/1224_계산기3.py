class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]


def splitTokens(exprStr):
    tokens = []
    val = 0
    valProcessing = False
    for c in exprStr:
        if c == ' ':
            continue
        if c in '0123456789':
            val = val * 10 + int(c)
            valProcessing = True
        else:
            if valProcessing:
                tokens.append(val)
                val = 0
            valProcessing = False
            tokens.append(c)
    if valProcessing:
        tokens.append(val)

    return tokens


def infixToPostfix(tokenList):
    prec = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }

    opStack = ArrayStack()
    postfixList = []
    for i in tokenList:
        if type(i) == int:
            postfixList.append(i)
        else:
            if i == ')':
                while opStack.peek() != '(':
                    postfixList.append(opStack.pop())
                opStack.pop()

            else:
                if opStack.isEmpty():
                    opStack.push(i)
                elif i in prec:
                    if i == '(':
                        opStack.push(i)
                    elif prec[opStack.peek()] >= prec[i]:
                        postfixList.append(opStack.pop())
                        opStack.push(i)
                    else:
                        opStack.push(i)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())

    return postfixList


def postfixEval(tokenList):
    chk_list = []
    for i in tokenList:
        if type(i) == str:
            b = chk_list.pop()
            a = chk_list.pop()
            if i == '+':
                chk_list.append(a + b)
            elif i == '-':
                chk_list.append(a - b)
            elif i == '*':
                chk_list.append(a*b)
            else:
                chk_list.append(a/b)
        else:
            chk_list.append(i)

    return chk_list[-1]


def solution(expr):
    tokens = splitTokens(expr)
    postfix = infixToPostfix(tokens)
    val = postfixEval(postfix)
    return val


for t in range(1, 11):
    l = input()
    s = input()
    print("#{} {}".format(t, solution(s)))