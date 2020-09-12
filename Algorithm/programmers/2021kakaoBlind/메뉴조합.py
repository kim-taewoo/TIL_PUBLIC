from itertools import combinations as cb

def solution(orders, course):
    u_menus = set(''.join(orders))

    answer = []
    for n_menu in course:
        max_cnt = 2
        new_comb = []
        combs = cb(u_menus, n_menu)
        for comb in combs:
            cnt = 0
            for order in orders:
                found = False
                if len([menu for menu in comb if menu in order]) == len(comb):
                    cnt += 1
                    found = True
                if found:
                    if cnt > max_cnt:
                        max_cnt = cnt
                        new_comb = [comb]
                    elif cnt == max_cnt:
                        new_comb.append(comb)
        
        for comb in new_comb:
            answer.append(''.join(sorted(comb)))
    
    answer.sort()
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2,3,4]
print(solution(orders, course))

