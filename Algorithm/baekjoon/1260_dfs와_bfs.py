def bfs(start):
    nodes_chk[start] = True
    q = [start]
    while q:
        n1 = q.pop(0)
        print(n1, end=" ")
        for n2 in nodes[n1]:
            if not nodes_chk[n2]:
                nodes_chk[n2] = True
                q.append(n2)
def dfs(node):
    nodes_chk[node] = True
    print(node, end=" ")
    for n2 in nodes[node]:
        if not nodes_chk[n2]:
            dfs(n2)

n, m, v = map(int, input().split())

nodes = [list() for _ in range(n+1)]

for i in range(m):
    n1, n2 = map(int, input().split())
    nodes[n2].append(n1)
    nodes[n1].append(n2)

for x in nodes[1:]:
    x.sort()

nodes_chk = [False for _ in range(n+1)]
dfs(v)
print()
nodes_chk = [False for _ in range(n+1)]
bfs(v)