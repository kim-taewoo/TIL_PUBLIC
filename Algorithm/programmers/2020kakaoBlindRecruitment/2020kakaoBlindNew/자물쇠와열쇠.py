def rotate90(pin, length):
    return [pin[1], (length-1) - pin[0]]


def moveKey(pins, lock_not_pins, len_key, len_lock):
    for r in range(-len_key+1, len_lock):
        for c in range(-len_key+1,len_lock):
            moved_pins = list(filter(lambda pinn: (0 <= pinn[0] < len_lock) and 0 <= pinn[1] < len_lock, map(
                lambda pin: [pin[0] + r, pin[1] + c], pins)))
            if sorted(moved_pins) == sorted(lock_not_pins):
                return True
    return False


def solution(key, lock):
    len_key = len(key)
    pins = [[r, c] for r in range(len_key)
            for c in range(len_key) if key[r][c]]
    len_lock = len(lock)
    lock_not_pins = [[r, c] for r in range(
        len_lock) for c in range(len_lock) if not lock[r][c]]
    if len(lock_not_pins) > len(pins):
        return False
    for d in range(4):
        pins = list(map(lambda pin: rotate90(pin, len(key)), pins))
        if moveKey(pins, lock_not_pins, len(key), len(lock)):
            return True
    return False


key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))
