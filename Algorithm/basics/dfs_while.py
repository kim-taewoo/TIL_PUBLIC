edges = [
    [1,2],
    [1,3],
    [2,4],
    [2,5],
    [3,5],
    [4,6],
    [5,6],
    [6,7]
]
board = [list() for _ in range(8)]
for x, y in edges:
    board[x].append(y)
    board[y].append(x)
result = []
chk = [False for _ in range(8)]
stack = [1]
while stack:
    top = stack[-1]
    chk[top] = True
    flag = False
    print(top, sorted(board[top]), result)
    for i in sorted(board[top]):
        if not chk[i]:
            flag = True
            stack.append(i)
            break
    if not flag:
        result.append(stack.pop())
mapping = ['','A','B','C','D','E','F','G']
print(*[mapping[x] for x in list(reversed(result))])
