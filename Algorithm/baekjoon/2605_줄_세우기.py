n = int(input())
a = list(map(int, input().split()))

line = []

for idx, el in enumerate(a, start = 1):
    l = len(line)
    line.insert(l - el,idx)

print(" ".join(map(str, line)))