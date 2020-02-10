coor_map = [[0] * 101 for _ in range(101)]

result = 0
for _ in range(4):
    a, b, c, d = map(int, input().split())
    for y in range(b, d):
        for x in range(a, c):
            if coor_map[y][x]:
                continue

            coor_map[y][x] = 1
            result += 1

print(result)