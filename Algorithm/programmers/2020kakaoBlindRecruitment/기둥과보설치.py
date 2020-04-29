from pprint import pprint


def chk_board(n, board_ver, board_hor):
    for r in range(n):
        for c in range(n+1):
            if board_ver[r][c]:
                if not (r == n-1 or board_ver[r+1][c] or (c >= 1 and board_hor[r+1][c-1]) or board_hor[r+1][c]):
                    return False
            if board_hor[r][c]:
                if not (board_ver[r][c] or (c < n and board_ver[r][c+1]) or (c >= 1 and board_hor[r][c-1] and board_hor[r][c+1])):
                    return False
    return True


def solution(n, build_frame):
    board_ver = [[0 for _ in range(n+1)] for __ in range(n)]
    board_hor = [[0 for _ in range(n+1)] for __ in range(n)]
    for frame in build_frame:
        x, y, a, b = frame
        isPilar = True if a == 0 else False
        isBuild = True if b == 1 else False

        if isBuild:
            if isPilar:
                r, c = (n-1)-y, x
                if r == (n-1) or board_ver[r+1][c] or (c >= 1 and board_hor[r+1][c-1]) or (board_hor[r+1][c]):
                    board_ver[r][c] = 1
            else:
                r, c = (n-1)-y+1, x
                if board_ver[r][c] or board_ver[r][c+1] or ((c >= 1 and board_hor[r][c-1]) and board_hor[r][c+1]):
                    board_hor[r][c] = 1
        else:
            if isPilar:
                r, c = (n-1)-y, x
                board_ver[r][c] = 0
                chk = chk_board(n, board_ver, board_hor)
                if not chk:
                    board_ver[r][c] = 1
            else:
                r, c = (n-1)-y+1, x
                board_hor[r][c] = 0
                chk = chk_board(n, board_ver, board_hor)
                if not chk:
                    board_hor[r][c] = 1
        # print(frame)
        # print('hor')
        # pprint(board_hor)
        # print()
        # print('ver')
        # pprint(board_ver)
        # print()
    # pprint(board_hor)
    # print()
    # pprint(board_ver)
    answer = []
    for r in range(n):
        for c in range(n+1):
            if board_hor[r][c]:
                answer.append([c,(n-1) - r + 1,1])
            if board_ver[r][c]:
                answer.append([c,(n-1)-r,0])
    
    answer.sort(key=lambda x: (x[0], x[1]))
    return answer


# n = 5
# build_frame = [[1, 0, 0, 1],
#                [1, 1, 1, 1],
#                [2, 1, 0, 1],
#                [2, 2, 1, 1],
#                [5, 0, 0, 1],
#                [5, 1, 0, 1],
#                [4, 2, 1, 1],
#                [3, 2, 1, 1]]

n = 5
build_frame = [[0, 0, 0, 1],
               [2, 0, 0, 1],
               [4, 0, 0, 1],
               [0, 1, 1, 1],
               [1, 1, 1, 1],
               [2, 1, 1, 1],
               [3, 1, 1, 1],
               [2, 0, 0, 0],
               [1, 1, 1, 0],
               [2, 2, 0, 1]]

print(solution(n, build_frame))
