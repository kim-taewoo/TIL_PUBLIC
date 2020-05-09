from itertools import permutations as pm

def solution(expression):
    operators = []
    numbers = []
    number = 0
    for i in expression:
        if i not in '+-*':
            number = number * 10 + int(i)
        else:
            numbers.append(number)
            number = 0
            operators.append(i)
    numbers.append(number)
    maxi = -21470000000
    for perm in list(pm(set(operators))):
        c_numbers = numbers[:]
        c_operators = operators[:]
        for oper in perm:
            while oper in c_operators:
                idx = c_operators.index(oper)
                operator = c_operators.pop(idx)
                num1 = c_numbers.pop(idx)
                num2 = c_numbers.pop(idx)
                if operator == '*':
                    result = num1 * num2
                elif operator == '+':
                    result = num1 + num2
                else:
                    result = num1 - num2
                c_numbers.insert(idx, result)
        maxi = max(maxi, abs(c_numbers[0]))

    answer = maxi
    return answer


expression = "50*6-3*2"

print(solution(expression))
