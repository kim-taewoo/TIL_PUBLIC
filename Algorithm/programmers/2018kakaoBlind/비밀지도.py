def solution(n, arr1, arr2):
    overwrapped = list(map(lambda x,y: x|y, arr1, arr2))
    result = list(map(lambda x: x[2:].zfill(n), list(map(bin, overwrapped))))
    answer = []
    for i in result:
        now = ''
        for j in i:
            x = ' ' if j == '0' else '#'
            now += x
        answer.append(now)
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30,1,21,17,28]
print(solution(n,arr1,arr2))
