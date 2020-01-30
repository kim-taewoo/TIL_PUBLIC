'''
최대 상금은 내림차순 정렬된 값이겠지.
그런데 횟수제한에 따라 최적값을 만족하지 못할 수 있다. 
한정된 제한 수 안에 가질 수 있는 최대값을 찾으려면
어떻게 해야되는지 고민.

방법1. 문제 해결을 위한 최적화된 룰을 찾아낸다.
방법2. 주어진 횟수 안에 가질 수 있는 모든 교환 경우의 수를 찾아보고 (브루트포스)
그 중 가장 큰 값을 해당 교환 수가 가질 수 있는 최대값이라고 한다.

결론: 특정 룰을 찾아보려 했으나 찾으면 찾을수록 명확한 룰이 안 보이고
계속해서 예외의 경우의 수가 생긴다. 
따라서 차라리 브루트 포스가 나을 수 있겠다는 결론.

그렇다면 모든 경우의 수는 어떻게 찾을 수 있을까?
단순 교환을 여러번 반복하는 것인데, 교환되는 인덱스의 조합을 달리하면 된다.
제한 조건을 생각해보면
1. 자기 자신과의 교환은 불가능
2. n 번의 교환을 모두 써야 한다.
'''

def swap_recursive(cur_i, n):
    global max_result

    if n == 0:
        result = int("".join(a))
        if result > max_result:
            max_result = result
        return
    
    if length == 1:
        max_result = int(a[0])
        return

    # 예외처리 해야 하는데 하면 테스트 케이스 1개 실패가 뜬다..
    # 뭘 놓쳤을까..?
    # if a == sorted_a: # n 다 쓰기 전에 정렬돼버린 경우
    #     if not n % 2:
    #         result = int("".join(a))
    #         if result > max_result:
    #             max_result = result
    #         return

    #     else:
    #         d = {}
    #         for i in a:
    #             d[i] = d.get(i, 0) + 1
    #         for i in d:
    #             if d[i] >= 2:
    #                 result = int("".join(a))
    #                 if result > max_result:
    #                     max_result = result
    #                 return

    #         a[-1], a[-2] = a[-2], a[-1]
    #         result = int("".join(a))
    #         if result > max_result:
    #             max_result = result
    #         return

    # cur_i 의 역할이 아주 중요하다.
    # 목표는 가장 큰 수를 만드는 것이다.
    # 따라서 첫번째 자리부터 가장 큰 수를 차곡차곡 쌓아야 한다.
    # n 번의 swap 가능 횟수 중에 가장 적합한 순간은
    # 첫번째 자리에 정렬됐을 때 가장 큰 수를 넣고, 
    # 두번째 자리에 두번째 수를 넣는 것이다. 
    # 다만 같은 숫자가 있거나 이미 최적 수가 완성된 경우 등
    # 다양한 경우의 수를 반영하기 위해
    # 방금 0번째 인덱스를 교환했는데 또 0번째 인덱스를 교환하는
    # 뻘짓까지 포함한 모든 경우의 수를 다 돌려보며
    # n 번의 기회 중 가장 큰 경우의 수를 찾는다. 
    for i in range(cur_i, length):
        for j in range(i+1, length):
            if a[i] <= a[j] :
                a[i], a[j] = a[j], a[i]
                swap_recursive(i, n-1)
                a[i], a[j] = a[j], a[i] # 백트래킹


T = int(input())

for t in range(1, T+1):
    a, n = input().split()
    a = list(a)
    n = int(n)
    sorted_a = sorted(a, reverse = True)
    length = len(a)
    max_result = 0
    swap_recursive(0, n)

    print("#{} {}".format(t, max_result))
