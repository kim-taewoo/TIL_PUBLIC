def solution(numbers):
    numbers = sorted(list(map(str, numbers)), key=lambda x: x*4,  reverse=True)
    return str(int("".join(numbers)))
