def solution(relation):
    answer_list = list()
    # 컬럼 인덱스 조합
    for i in range(1, 1 << len(relation[0])):
        tmp_set = set()
        # 레코드 전체를 돌면서 i 와 겹치는 컬럼들 추가해서 set 에 저장
        for j in range(len(relation)):
            tmp = ''
            for k in range(len(relation[0])):
                if i & (1 << k):
                    tmp += str(relation[j][k])
            tmp_set.add(tmp)

        # 겹친 게 없는 경우 개수가 똑같겠지
        if len(tmp_set) == len(relation):
            not_duplicate = True
            for num in answer_list:
                # num 자체가 일종의 해시가 된다. 대박
                if (num & i) == num:
                    not_duplicate = False
                    break
            if not_duplicate:
                answer_list.append(i)
    return len(answer_list)
