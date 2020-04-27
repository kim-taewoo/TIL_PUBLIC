dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)


def rotate90(coor, length):
    return [coor[1], (length-1) - coor[0]]


def solution(key, lock):
    lock_length = len(lock[0])
    key_length = len(key[0])

    lock_holes = [(r, c) for r in range(lock_length)
                  for c in range(lock_length) if not lock[r][c]]

    key_pins = [(r, c) for r in range(key_length)
                for c in range(key_length) if key[r][c]]

    combs = [(u, r, d, l) for u in range(key_length) for r in range(lock_length) for d in range(
        lock_length) for l in range(key_length) if not ((u and d) or (l and r))]

    for i in range(4):
        key_pins = [rotate90(coor, key_length) for coor in key_pins]
        for comb in combs:
            key_pins_moved = []
            for x, y in key_pins:
                nx = x + dx[0] * comb[0] + dx[2] * comb[2]
                ny = y + dy[1] * comb[1] + dy[3] * comb[3]
                key_pins_moved.append((nx, ny))

            cnt = len(lock_holes)
            no_match = False
            for k in key_pins_moved:
                if k in lock_holes:
                    cnt -= 1
                else:
                    if 0 <= k[0] < lock_length and 0 <= k[1] < lock_length:
                        no_match = True
                        break

            if not no_match and cnt == 0:
                return True

    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
