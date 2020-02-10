n = int(input())

maxi = 0
maxi_result = []
for i in range(1, n+1):
    first = n
    second = i
    result = [first,second]
    length = 2
    third = 30001
    while third >= 0:
        third = first - second
        first, second = second, third
        result.append(third)
        length += 1
    result = result[:-1]
    length -= 1
    if length > maxi:
        maxi = length
        maxi_result = result
print(maxi)
print(" ".join(map(str, maxi_result)))
    