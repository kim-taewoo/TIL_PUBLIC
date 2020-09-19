def solution(clothes):
    dic = {}
    for n, t in clothes:
        dic[t] = dic.get(t, 0) + 1
    answer = 1
    for v in dic.values():
        answer *= (v+1)
    return answer - 1
