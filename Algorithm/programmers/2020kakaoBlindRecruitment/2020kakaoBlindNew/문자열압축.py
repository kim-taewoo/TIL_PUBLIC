def go(s, curr_size):
    shorten = 0
    start_idx = 0
    compare_start_idx = start_idx + curr_size

    cnt = 1
    while compare_start_idx + curr_size <= len(s):
        base_substring = s[start_idx:start_idx+curr_size]
        compare_substring = s[compare_start_idx:compare_start_idx+curr_size]
        if base_substring == compare_substring:
            cnt += 1
            compare_start_idx += curr_size
        else:
            if cnt > 1:
                shorten += (cnt-1) * curr_size - len(str(cnt))
            cnt = 1
            start_idx = compare_start_idx
            compare_start_idx = compare_start_idx + curr_size
    if cnt > 1:
        shorten += (cnt-1) * curr_size - len(str(cnt))
    
    return len(s) - shorten
    
def solution(s):
    min_length = len(s)

    for curr_size in range(1, len(s)//2+1):
        length = go(s, curr_size)
        min_length = min(min_length, length)

    return min_length


print(solution("aabbaccc"))
