def redirect(r, redirect_map):
    if redirect_map[r] == r:
        redirect_map[r] = redirect(r+1,redirect_map)
        return r
    else:
        redirect_map[r] = redirect(redirect_map[r],redirect_map)
        return redirect_map[r]




def solution(k, room_number):
    answer = []
    redirect_map = [i for i in range(k+1)]
    for r in room_number:
        answer.append(redirect(r, redirect_map))
            
    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]

print(solution(k, room_number))