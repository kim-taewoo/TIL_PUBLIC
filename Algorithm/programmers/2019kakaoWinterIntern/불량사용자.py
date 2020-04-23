def solution(user_id, banned_id):
    len_banned = len(banned_id)
    matchListAll = []
    for i in banned_id:
        matchList = []
        for j in user_id:
            if len(i) == len(j):
                match = True
                for k in range(len(i)):
                    if i[k] == '*':
                        continue
                    elif i[k] != j[k]:
                        match = False
                        break
                if match:
                    matchList.append(j)
        matchListAll.append(matchList)

    all_combs = []
    comb = []

    def dfs(idx):
        if idx == len_banned:
            sorted_comb = sorted(comb)
            if sorted_comb not in all_combs:
                all_combs.append(sorted_comb[:])
            return

        for i in matchListAll[idx]:
            if i not in comb:
                comb.append(i)
                dfs(idx+1)
                comb.pop()

    dfs(0)
    return (len(all_combs))


# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]
# print(solution(user_id, banned_id))
