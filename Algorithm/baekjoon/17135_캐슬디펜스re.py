from itertools import combinations as cb
import copy


def per_archer(archer, enemies):
    archer_row, archer_col = archer
    matched_enemies = []
    min_dist = float('inf')
    for enemy in enemies:
        enemy_row, enemy_col = enemy
        dist = abs(archer_row-enemy_row) + abs(archer_col-enemy_col)
        if dist <= D:
            if dist > min_dist: continue
            if dist < min_dist:
                matched_enemies = []
                min_dist = dist
            matched_enemies.append(enemy)
    if matched_enemies:
        return sorted(matched_enemies, key=lambda x: x[1])[0]


def game_per_comb(archers, enemies, board):
    kill = 0
    while enemies:
        die_this_turn = set()
        for archer in archers:
            target = per_archer(archer, enemies)
            if target:
                die_this_turn.add(tuple(target))
        enemies = [enemy for enemy in enemies if tuple(
            enemy) not in die_this_turn]
        kill += len(die_this_turn)

        enemies = [[enemy[0]+1, enemy[1]]
                   for enemy in enemies if enemy[0]+1 < N]

    return kill
    

N, M, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

enemies = [[r, c] for r in range(N) for c in range(M) if board[r][c]]

archer_cols_combs = cb([i for i in range(M)], 3)

max_kill = 0
for cols in archer_cols_combs:
    archers = [[N, col] for col in cols]
    kill = game_per_comb(archers, copy.copy(enemies), copy.deepcopy(board))
    max_kill = max(max_kill, kill)

print(max_kill)
