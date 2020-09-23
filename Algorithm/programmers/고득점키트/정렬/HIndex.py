def solution(citations):
    cnts = {-1: 1001}
    for c in citations:
        cnts[c] = cnts.get(c, 0) + 1
    accu = 0
    keys = sorted(cnts.keys(), reverse=True)
    last = keys[-2]
    for k in keys:
        accu += cnts[k]
        if accu == k:
            return k
        if accu > k:
            return last
        last = accu

citations = [3,0,6,1,5]
print(solution(citations))
citations = [0,0,0,0]
print(solution(citations))
