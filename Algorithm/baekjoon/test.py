# Problem [14888] : 연산자 끼워넣기
min_val = 100000000000000000
max_val = -100000000000000000
def dfs(start,n,result):
    global min_val
    global max_val
    if n == N:
        if min_val > result:
            min_val = result
        if max_val < result:
            max_val = result
        return

    for i in range(start,2*(N-1)):
        my_oper = oper[i]
        if my_oper == '+':
            result = result + data[n]
        elif my_oper == '-':
            result = result - data[n]
        elif my_oper == '*':
            result = result * data[n]
        else:
            if result < 0:
                result = -1 * (abs(result) // data[n])
            else:
                result = result // data[n]
        dfs(i+1,n+1, result)

operator = ['+', '-', '*', '//']
N = int(input())
data = list(map(int,input().split()))
num_oper = list(map(int,input().split()))
oper = list()
for i in range(4):
    if num_oper[i] != 0:
        for _ in range(num_oper[i]):
            oper.append(operator[i])
oper = oper * 2
dfs(0,1,data[0])
print(max_val)
print(min_val)