# 효율 안 따지고 생각나는 대로 바로 짠 코드. (효율성 통과 x)

def solution(words, queries):
    answer = []

    for query in queries:
        cnt = 0
        for word in words:
            if len(query) != len(word): 
                continue
            
            match = True
            for i in range(len(query)):
                if query[i] == '?':
                    continue
                if query[i] != word[i]:
                    match = False
                    break
            if match:
                cnt += 1
        answer.append(cnt)

    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))
