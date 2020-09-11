def solution(gems):
    n = len(gems)
    n_gems = len(set(gems))
    lt = 0
    rt = len(gems)

    # 아래처럼 크기에 대한 이분탐색을 한 것 까지는 좋았다.
    # 그런데 이제 그 크기에 맞춰 sublist 를 만들 때,
    # sublist 하나당 새로 또 인덱스 슬라이싱을 하다보니 시간초과가 됐을 것이다...
    # '슬라이딩 윈도우' 라고 부르던데, 그냥 첫번째 접근 방식이었던 시작 포인터와 끝 포인터를 잡고
    # 한 칸씩 추가하고 빼는 방식으로 했다면 아마 통과가 되었을 것 같아서 많이 아쉬운 문제..
    # 이것까지만 풀면 4솔이었는데 ㅠㅠ
    answer = []
    while lt <= rt:
        mid = (lt + rt) // 2
        flag = False
        l_ptr, r_ptr = 0, mid
        sublist = gems[l_ptr:r_ptr]
        for i in range(n-mid+1):
            sublist = gems[i:i+mid]
            subset = set(sublist)
            if len(subset) == n_gems:
                answer = [i+1, i+mid]
                flag = True
                break
        if flag:
            rt = mid - 1
        else:
            lt = mid + 1

    return answer


gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))
