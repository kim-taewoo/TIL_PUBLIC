# 1~5 숫자로 3자리 숫자 만들기
def permu(level, target_length): # 여기서 level 은 selected_nums 배열의 인덱스를 가리킨다. 즉 이 재귀함수는 실행될 때 현재 보고 있는 인덱스 자리에 들어갈 숫자를 고르는 작업을 수행한다.

    # 전역으로 선언된 배열인 selected_nums 와 nums 사용

    if level == target_length:
        print("".join(map(str, selected_nums)))
        return  # 저는 else 문 보다 그냥 조건마다 return 으로 종료시켜버리는 걸 선호합니다. 걍 취향

    for i in range(5):
        if used_num_chk[i]: continue # 중복 숫자는 허용하지 않기
        selected_nums.append(nums[i]) # 이번 level 에 담을 숫자를 고른다. 
        used_num_chk[i] = True # 사용한 숫자 체크
        permu(level+1,3) # 이 재귀 함수는 위에서 사용된 숫자가 체크된 상태의 chk 배열을 참조하여 실행된다.
        used_num_chk[i] = False # 사용한 숫자 초기화
        selected_nums.pop()
nums = [x for x in range(1, 6)] # 1부터 5까지의 숫자
used_num_chk = [False for _ in range(5)] # 숫자 중복을 막기 위한 체크 배열
selected_nums = [] # 인덱스가 아닌 실제로 골라진 숫자가 들어갈 공간. 아직 몇 개를 골라야되는지 모르므로 빈 리스트로 시작해 append 해나간다.
permu(0, 3) # 3자리 숫자를 조합해야 하는 경우