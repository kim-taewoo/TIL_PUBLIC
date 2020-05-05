# 이래도 결국 실패하길래 멘탈 터져서 다른 사람 코드로 갈아탐
def solution(food_times, k):
    length = len(food_times)
    sorted_food_times = sorted(food_times)

    accu = 0
    last_idx = 0
    for i in range(length):
        if i != 0:
            remains = sorted_food_times[i] - sorted_food_times[i-1]
        else:
            remains = (sorted_food_times[i])
        to_add = (length - i) * remains
        accu += to_add
        if accu > k:
            last_idx = i - 1
            break

    # 바로 위 for 문이 break 되지 않고 끝까지 돌아버린 경우겠지? 그냥 else 문 써도 되려나
    if accu <= k:
        return -1

    lst = []
    for j in range(length-1, -1, -1):
        if food_times[j] - sorted_food_times[last_idx] > 0:
            lst.append(j+1)
    if len(lst):
        # 초과분: accu-k-1. -1 까지 하는 이유는 0 이 되는 순간까지는 초과한 것이 아니기 때문.
        # 나머지 연산: 초과하지 않고 잘 돌았던 마지막 인덱스 바퀴까지 살아남았던 food_times 의 개수가 몇바퀴 돌고 남은 나머지만큼 뒤에서 빼주어야 하니까
        return lst[(accu-k-1) % len(lst)]
    else:
        return k % length + 1


food_times = [3, 1, 2]
k = 5
print(solution(food_times, k))
