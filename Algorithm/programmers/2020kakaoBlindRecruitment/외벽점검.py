from itertools import permutations as pm

# def permutation(candidates, Prepermuation, res):
#     if len(candidates) == 0: res.append(Prepermuation); return
#     else:
#         for i in range(len(candidates)):
#             permutation(candidates[:i]+candidates[i+1:], Prepermuation + [ candidates[i] ], res)
#         return

def solution(n, weak, dist):
    # complete search
    dist.sort(reverse = True)

    for i in range(1, len(dist)+1):
        pms = pm(dist[:i])
        for p in pms:
            for start in range(len(weak)):
                left = weak[:start]
                right = weak[start:]
                traverse_list = right + [x + n for x in left]
                candidates = list(p)
                while traverse_list and candidates:
                    cur = traverse_list.pop(0)
                    friend = candidates.pop(0);
                    coverage = cur + friend
                    while traverse_list and traverse_list[0] <= coverage: 
                        traverse_list.pop(0)

                if not traverse_list:
                    return i
    return -1



n = 12
weak = [1, 5, 6, 10]
dist = [1, 2, 3, 4]
print(solution(n, weak, dist))
