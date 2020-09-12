
def search(comb, order):
    for menu in comb:
        if not menu in order:
            return False
    return True


def dfs(idx, comb, u_menus, course, orders):
    global answer
    global max_cnts
    global new_comb

    if idx == len(u_menus):
        return

    comb = comb + u_menus[idx]
    length = len(comb)
    max_course = max(course)
    if length > max_course:
        return

    if length in course:
        cnt = 0
        flag = False
        for order in orders:
            found = False
            if search(comb, order):
                cnt += 1
                found = True
            if found:
                if cnt > max_cnts[length]:
                    max_cnts[length] = cnt
                    new_comb[length] = [comb]
                elif cnt == max_cnts[length]:
                    new_comb[length].append(comb)
        if cnt >= 2:
            for i in range(idx+1, len(u_menus)):
                dfs(i, comb, u_menus, course, orders)
            return
        else:
            return

    else:
        for i in range(idx+1, len(u_menus)):
            dfs(i, comb, u_menus, course, orders)


answer = []
max_cnts = {}
new_comb = {}


def solution(orders, course):
    u_menus = sorted(list(set(''.join(orders))))
    for length in course:
        max_cnts[length] = 2
        new_comb[length] = []

    for i in range(len(u_menus)):
        dfs(i, '', u_menus, course, orders)

    for length in new_comb:
        for comb in new_comb[length]:
            answer.append(''.join(sorted(comb)))

    return sorted(answer)



orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2, 3, 5]
print(solution(orders, course))
