T = int(input())

for t in range(T):
    s = input()
    length = len(s)
    pattern1 = "." + ".#.." * length
    pattern2 = "." + "#." * length * 2
    pattern3 = "#"
    for i in s:
        pattern3 += ".{}.#".format(i)
    
    print(pattern1)
    print(pattern2)
    print(pattern3)
    print(pattern2)
    print(pattern1)