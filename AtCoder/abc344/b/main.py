import sys
a = []
for line in sys.stdin.readlines():
    a.append(line)

for i in range(len(a)):
    print(a[~i])
