from pprint import pprint

def go(i, key, seq, now):
    global total

    if key == '-':
        next_keys = now.keys()
        for k in next_keys:
            temp = now.get(k, {})
            if temp:
                go(i, k, seq, now)
    else:
        if i == len(seq) - 1:
            total += sum([now[x]['cnt'] for x in now.keys() if int(x) >= int(seq[i])])

        else:
            now = now.get(key, {})
            if not now: 
                return
            key = seq[i+1]
            go(i+1, key, seq, now)

total = 0
def solution(info, query):
    global total
    answer = []

    trie = {}
    for person in info:
        seq = person.split()
        now = trie
        for i in range(len(seq)+1):
            if i == len(seq):
                now['cnt'] = now.get('cnt', 0) + 1
                break
            now[seq[i]] = now.get(seq[i], {})
            now = now[seq[i]]

    for person in query:
        seq = [i for i in person.split() if i != 'and']
        now = trie
        key = seq[0]
        go(0, key, seq, now)
        answer.append(total)
        total = 0

    return answer


info = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
        "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]

print(solution(info, query))
