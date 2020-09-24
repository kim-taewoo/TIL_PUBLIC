def solution(tickets):
    routes = {}
    for a, b in tickets:
        routes[a] = routes.get(a, []) + [b]
    for r in routes:
        routes[r].sort(reverse=True)
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
    return path[::-1]
