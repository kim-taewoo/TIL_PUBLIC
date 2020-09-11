def solution(words, queries):
    trie = {}
    trie_back = {}
    for word in words:
        length = len(word)
        seq = [length] + list(word)
        seq2 = [length] + list(reversed(word))
        now = trie
        now2 = trie_back
        for i in range(length+1):
            now[seq[i]] = now.get(seq[i], {})
            now['cnt'] = now.get('cnt', 0) + 1
            now = now[seq[i]]

            now2[seq2[i]] = now2.get(seq2[i], {})
            now2['cnt'] = now2.get('cnt', 0) + 1
            now2 = now2[seq2[i]]

    answer = []
    for query in queries:
        length = len(query)
        back = False

        if query[0] == '?':
            back = True

        if back:
            now = trie_back.get(length, {'cnt': 0})
            seq = query[::-1]
        else:
            now = trie.get(length, {'cnt': 0})
            seq = query

        for i in seq:
            if i == '?':
                cnt = now['cnt']
                break
            now = now.get(i, {})
            if not now:
                cnt = 0
                break
            cnt = now['cnt']

        answer.append(cnt)

    return answer

words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))
