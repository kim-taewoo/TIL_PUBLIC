T = int(input())
for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    
    cnt = 0
    length = 0
    maxi_length = 0
    potato = 0
    maxi_potato = 0
    flag = False
    for i in range(n-1):
        if a[i+1] > a[i]:
            if not flag:
                flag = True
                cnt += 1
                length = 2
                potato = a[i] + a[i+1]
            else:
                potato += a[i+1]
                length += 1
        else:
            flag = False
            if length > maxi_length: 
                maxi_length = length
                maxi_potato = potato
            elif length == maxi_length:
                if maxi_potato < potato:
                    maxi_potato = potato
    if length > maxi_length:
        maxi_length = length
        maxi_potato = potato
    elif length == maxi_length:
        if maxi_potato < potato:
            maxi_potato = potato
    print("#{} {} {}".format(t, cnt, maxi_potato))
