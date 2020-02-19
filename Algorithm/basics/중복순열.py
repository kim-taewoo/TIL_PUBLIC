# 1~5 순열
def permu(level): # 여기서 level 은 selected_nums 배열의 인덱스를 가리킨다. 즉 이 재귀함수는 실행될 때 현재 보고 있는 인덱스 자리에 들어갈 숫자를 고르는 작업을 수행한다.

    # 전역으로 선언된 배열인 selected_nums 와 nums 사용

    if level == 5:
        print(*selected_nums)
        return  # 저는 else 문 보다 그냥 조건마다 return 으로 종료시켜버리는 걸 선호합니다. 걍 취향

    for i in range(5):
        if used_num_chk[i]: continue # 중복 숫자는 허용하지 않기
        selected_nums[level] = nums[i] # 이번 level 에 숫자를 담는다. 어차피 다음 for 문에 덮어씌워지므로 굳이 다시 0으로 바꿀 필요 없다.
        used_num_chk[i] = True # 사용한 숫자 체크
        permu(level+1) # 이 재귀 함수는 위에서 사용된 숫자가 체크된 상태의 chk 배열을 참조하여 실행된다.
        used_num_chk[i] = False # 사용한 숫자 초기화

nums = [x for x in range(1, 6)] # 1부터 5까지의 숫자
selected_nums = [0 for _ in range(5)] # 인덱스가 아닌 실제로 골라진 숫자가 들어갈 공간
used_num_chk = [False for _ in range(5)] # 숫자 중복을 막기 위한 체크 배열
permu(0)