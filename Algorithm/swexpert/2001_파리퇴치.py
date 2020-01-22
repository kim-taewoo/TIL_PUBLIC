T = int(input())

for t in range(1,T+1):
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]

    max_catch = 0
    
    for i in range(n-m+1):
        for j in range(n-m+1):
            catch = 0
            for k in range(m):
                for l in range(m):
                    catch+=a[i+k][j+l]
            if catch > max_catch : 
                max_catch = catch
    print("#{} {}".format(t, max_catch))
