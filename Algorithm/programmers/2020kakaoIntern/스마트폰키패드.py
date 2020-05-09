def solution(numbers, hand):
    locs = {
        1: (0, 0),
        2: (0, 1),
        3: (0, 2),
        4: (1, 0),
        5: (1, 1),
        6: (1, 2),
        7: (2, 0),
        8: (2, 1),
        9: (2, 2),
        0: (3, 1)
    }
    lnow = None
    rnow = None

    answer = ''
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            lnow = number
        elif number in [3, 6, 9]:
            answer += 'R'
            rnow = number
        else:
            ldist = abs(locs[lnow][0] - locs[number][0]) + \
                abs(locs[lnow][1]-locs[number][1])
            rdist = abs(locs[rnow][0] - locs[number][0]) + \
                abs(locs[rnow][1]-locs[number][1])
            if ldist < rdist:
                answer += 'L'
                lnow = number
            elif ldist > rdist:
                answer += 'R'
                rnow = number
            else:
                if hand == 'left':
                    answer += 'L'
                    lnow = number
                else:
                    answer += 'R'
                    rnow = number
    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"

print(solution(numbers, hand))
