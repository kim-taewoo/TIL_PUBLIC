for tc in range(10):
    t = input()
    a = [list(map(int, input().split())) for _ in range(100)]

    min_length = 10000
    min_start = -1
    for idx, el in enumerate(a[0]):
        if el: # 시작컬럼이 0 이 아닌 경우에만 출발
            length = 0
            cur_c = idx
            for r in range(100):
                right_flag = False
                left_flag = False
                while cur_c+1 < 100 and a[r][cur_c+1]:
                    right_flag = True
                    cur_c += 1
                    length += 1
                if right_flag: continue
                while cur_c-1 >= 0 and a[r][cur_c-1]:
                    left_flag = True
                    cur_c -= 1
                    length += 1
                if left_flag: continue
            if length <= min_length:
                min_length = length
                min_start = idx
    print("#{} {}".format(t, min_start))
                  
