s = set(map(int, input().split()))
if len(s) == 2:
    for i in range(1, 4):
        if i not in s:
            print(i)
else:
    print("-1")
