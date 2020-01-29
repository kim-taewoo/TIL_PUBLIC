'''
    a, c -> a, b
    b, d -> c, d
    
    a -> b : a - b
    a -> c : a - b - c
    a -> d : a - b - d

    b -> a : b - c - a
    b -> c : b - c
    b -> d : b - d

    c -> a : c - a
    c -> b : c - b
    c -> d : c - b - d

    d -> a : d - c - a
    d -> b : d - c - b
    d -> c : d - c
'''
T = int(input())
for t in range(1, T+1):
    a,b,c,d = map(int, input().split())
    if a != 0 and d != 0:
        if b == 0 and c == 0:
            result = 'impossible'
    elif 
    

    