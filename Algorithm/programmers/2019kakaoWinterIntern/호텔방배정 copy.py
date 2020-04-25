def solution(k, room_number):
    unf = {}

    def find(v):
        if v == unf.get(v, v):
            return v
        else:
            unf[v] = find(unf[v])
            return unf[v]

    # def union(a,b):
    #     # a 는 이미 find 의 결과이므로 다시 find 해줄 필요가 없다.
    #     b = find(b)
    #     if a != b:
    #         unf[a] = b

    answer = []

    for r in room_number:
        # print(unf)
        root = find(r)
        answer.append(root)
        unf[root] = root + 1
        # union(root, root+1)

    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]

print(solution(k, room_number))
