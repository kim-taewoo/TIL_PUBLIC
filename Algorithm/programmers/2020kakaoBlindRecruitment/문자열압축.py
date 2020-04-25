def solution(s):
    max_shorten = 0
    # 단위를 서서히 상승시키기
    for i in range(1, len(s)//2+1):
        # 주어진 s 문자열의 인덱스 범위 내에서 압축 가능성 조사
        shorten = 0
        base_pt = 0
        compare_pt = base_pt + i

        currentCnt = 1
        while compare_pt+i <= len(s):
            if s[base_pt: base_pt + i] == s[compare_pt: compare_pt+i]:
                currentCnt += 1
                compare_pt += i
            else:
                if currentCnt > 1:
                    shorten += (currentCnt-1) * i - len(str(currentCnt))
                currentCnt = 1
                base_pt = compare_pt
                compare_pt = compare_pt + i

        if currentCnt > 1:
            shorten += (currentCnt-1) * i - len(str(currentCnt))

        max_shorten = max(max_shorten, shorten)
    
    return len(s) - max_shorten


s = "abcabcabcabcdededededede"
print(solution(s))
