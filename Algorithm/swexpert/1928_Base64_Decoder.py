T = int(input())

'''
24비트에 한 바이트씩 3 바이트 문자를 넣었다면
총 3개의 문자
그런데 6비트씩 잘랐다면 4개로 나뉘어졌을 것. 
4개로 나뉜 걸 표에 따라 encode 한 문자열을
다시 비트로 변환해서 8비트씩 묶은 뒤 문자열로 출력한다.
'''

for t in range(1, T+1):
    s = input()

    result = ""
    four_c = ""
    for i in range(0, len(s)):
        if 65<= ord(s[i]) <= 90:
            num = ord(s[i]) - 65
        elif 97 <= ord(s[i]) <= 122:
            num = ord(s[i]) - 71
        elif 48 <= ord(s[i]) <= 57:
            num = ord(s[i]) + 4
        elif ord(s[i]) == 43:
            num = ord(s[i]) + 19
        elif ord(s[i]) == 47:
            num = ord(s[i]) + 16

        binary = format(num, '06b')
        four_c += binary

        if not (i+1) % 4:
            for j in range(3):
                d_c = chr(int(four_c[8*j:8*(j+1)], 2))
                result += d_c
            four_c = ""
    print("#{} {}".format(t, result))