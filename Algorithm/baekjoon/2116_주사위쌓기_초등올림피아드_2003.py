n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]

'''
pair index
(0, 5)
(1, 3)
(2, 4)
윗면 아랫면만 맞춰주면 옆면은 그냥 가장 최대값들로 골라서 더해주면 된다.
즉 1번 주사위의 윗면이 무엇이 되냐만 고르면 나머지는 정해진다. 
'''
pair = [5,3,4,1,2,0]
def find_biggest(dice, used_index):
    return max(dice[x] for x in range(6) if x != used_index and x != pair[used_index])

# 첫번째 주사위의 6개 값 순서대로 대입
# 대입된 값에 따라 남은 주사위 모양 정하기
# 각 주사위 옆면의 최대값을 구해 더하기. 
# 6개 경우의 수 가장 큰 것이 답
max_side_sum = 0
for i in range(6):
    top = a[0][i]
    side_sum = find_biggest(a[0], i)
    for j in range(1, n):
        bottom_index = a[j].index(top)
        top = a[j][pair[bottom_index]]
        side_sum += find_biggest(a[j], bottom_index)
    if side_sum > max_side_sum:
        max_side_sum = side_sum
print(max_side_sum)