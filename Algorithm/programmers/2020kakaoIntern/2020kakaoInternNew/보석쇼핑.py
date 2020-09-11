def check(gems_set, n_ugems):
    if len(gems_set) == n_ugems:
        return True
    return False

from collections import defaultdict


def solution(gems):
    answer = [1, len(gems)]
    gemset = set(gems)
    bag = defaultdict(int)

    s, e = 0, 0
    while e < len(gems):
        if len(bag) < len(gemset):
            bag[gems[e]] += 1
            e += 1
        else:
            if bag[gems[s]] == 1:
                del bag[gems[s]]
            else:
                bag[gems[s]] -= 1
            if answer[1] - answer[0] > e - s - 1:
                answer = [s + 1, e]
            s += 1
    return answer

def solution(gems):
    n_ugems = len(set(gems))

    size_lt = 0
    size_rt = len(gems)
    ans = []
    while size_lt <= size_rt:
        curr_size = (size_lt + size_rt) // 2

        sptr = 0
        eptr = curr_size-1
        gems_dict = {}
        gems_set = set()
        for gem in gems[sptr:eptr+1]:
            gems_dict[gem] = gems_dict.get(gem, 0) + 1
            gems_set.add(gem)
        
        qualified = False
        if check(gems_set, n_ugems):
            qualified = True
            ans = [sptr+1, eptr+1]

        for i in range(1, len(gems) - curr_size + 1):  # 0부터, curr_size 가능한 지점까지.
            if qualified: break
            removing_gem = gems[sptr]
            sptr += 1
            eptr += 1
            adding_gem = gems[eptr]
            if not gems_dict.get(adding_gem, 0):
                gems_dict[adding_gem] = 1
                gems_set.add(adding_gem)
            else:
                gems_dict[adding_gem] += 1
            if gems_dict.get(removing_gem, 0) == 1:
                gems_set.remove(removing_gem)
                gems_dict[removing_gem] -= 1
            else:
                gems_dict[removing_gem] -= 1
            if check(gems_set, n_ugems):
                qualified = True
                ans = [sptr+1, eptr+1]
                break

        if qualified:
            size_rt = curr_size - 1
        else:
            size_lt = curr_size + 1


    return ans


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
