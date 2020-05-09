def solution(gems):
    n_gems = len(set(gems))
    sptr = 0
    eptr = n_gems
    ables = []
    while True:
        if eptr == len(gems)+1:
            break
        sublist = gems[sptr:eptr]
        subset = set(sublist)
        if len(subset) == n_gems:
            print(subset)
            while not (subset - set(gems[sptr:eptr])):
                sptr += 1
            sptr -= 1
            ables.append([sptr, eptr])
        eptr += 1
    
    answer = []
    mini = 2147000000
    for able in ables:
        if (able[1] - able[0]) < mini:
            mini = able[1] - able[0]
            answer = [able[0]+1,able[1]]
    return answer


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
