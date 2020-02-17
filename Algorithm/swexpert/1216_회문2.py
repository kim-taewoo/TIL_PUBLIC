T = 10


def chk_palindrome(list_to_chk, length):
    for i in range(length//2):
        if list_to_chk[i] != list_to_chk[-1-i]:
            return False
    return True


for _ in range(1, T+1):
    t = int(input())
    a = [list(input()) for _ in range(100)]
    found = False
    for l in range(100, 0, -1): # 가장 긴 100부터 1칸씩 내려가며 검사
        for r in range(100): 
            if found: break
            for s in range(100-l+1):
                if found: break
                chk_list = a[r][s:s+l]  # 가로(각 행) 검사
                chk_list2 = [a[x][r] for x in range(s,s+l)] # 세로(각 열) 검사

                if chk_palindrome(chk_list, l) or chk_palindrome(chk_list2, l):
                    found = True
        if found: break
    
    print("#{} {}".format(t, l))