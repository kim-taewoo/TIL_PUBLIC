def solution(relation):
    result = 0
    len_columns = len(relation[0])
    column_idxs = [i for i in range(len_columns)]
    len_records = len(relation)

    result_list = []
    q = [[i] for i in column_idxs]
    while q:
        comb_now = q.pop(0)
        flag = False
        for x in result_list:
            if set(x).issubset(set(comb_now)):
                flag = True
        if flag:
            continue
        tmp = []
        flag = True
        for i in range(len_records):
            now = [j for idx, j in enumerate(relation[i]) if idx in comb_now]
            if now in tmp:
                flag = False
                break
            else:
                tmp.append(now)
        if flag:
            result += 1
            result_list.append(comb_now[:])
        else:
            maxi = max(comb_now)
            for j in range(maxi+1, len_columns):
                q.append(comb_now[:]+[j])

    return result
