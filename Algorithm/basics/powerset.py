def make_ten(level, total_sum):# level 은 우리가 사용할 수 있는 숫자들을 담은 nums 의 인덱스를 가리킨다. 즉 nums 의 원소가 10개이므로 인덱스는 9에서 끝난다. 
    if total_sum > 10: # 종료조건1 : 가지치기(백트래킹)
        return
    if total_sum == 10: # 종료 조건 2 (원하는 상황)
        result = [nums[i] for i in range(10) if selected_idx[i]]
        print(*result)
        return
    if level == 10: return # 종료조건 3. 10개 다 둘러봤는데도 10 을 넘거나 10이 되지 못했으면 자동 종료

    make_ten(level+1, total_sum) # 이번 인덱스(level) 은 고르지 않고 스킵하는 경우
    selected_idx[level] = True # 나중에 합이 10이 되었을 때 어떤 숫자를 사용했는지 알기 위한 체크배열
    make_ten(level+1, total_sum + nums[level]) # 이번 인덱스(level) 을 고르는 경우
    selected_idx[level] = False # 다음 조합을 위해 재귀함수를 출발시킨 이후에는 다시 초기화 해준다.


nums = [x for x in range(1, 11)]
selected_idx = [False for _ in range(10)]
make_ten(0, 0)