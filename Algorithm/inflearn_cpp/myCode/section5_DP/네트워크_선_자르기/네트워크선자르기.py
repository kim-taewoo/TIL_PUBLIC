import sys
sys.stdin = open('input.txt')

length = int(input())

dy = [0] * 50

dy[1] = 1
dy[2] = 2

for i in range(3, length+1):
    dy[i] = dy[i-1] + dy[i-2]

print(dy[length])
