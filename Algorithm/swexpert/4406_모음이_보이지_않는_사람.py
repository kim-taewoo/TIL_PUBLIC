T = int(input())

for t in range(1,T+1):
    s = input()
    result = "".join([i for i in s if i not in 'aeiou'])
    print("#{} {}".format(t, result))