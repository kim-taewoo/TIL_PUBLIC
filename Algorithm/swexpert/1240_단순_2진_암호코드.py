T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())

    a = [input() for _ in range(n)]

    mapping = {
        '0001101': '0',
        '0011001': '1',
        '0010011': '2',
        '0111101': '3',
        '0100011': '4',
        '0110001': '5',
        '0101111': '6',
        '0111011': '7',
        '0110111': '8',
        '0001011': '9',
    }

    code = ""
    found = False
    for r in range(n):
        for c in range(m-1, 54, -1):
            if a[r][c] == '1':
                found = True
                l = a[r][c-55:c+1]
                for i in range(8):
                    s = mapping[l[7*i:7+7*i]]
                    code += s
                break
            if found: break
        if found: break

    odd_sum = 0
    even_sum = 0
    for i in range(7):
        if i % 2:
            even_sum += int(code[i])
        else:
            odd_sum += int(code[i])

    chk = (odd_sum * 3 + even_sum + int(code[7])) % 10
    if not chk:
        print("#{} {}".format(t, even_sum + odd_sum + int(code[7])))
    else:
        print("#{} {}".format(t, 0))
