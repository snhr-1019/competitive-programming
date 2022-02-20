n = int(input())
a = sorted(list(map(int, input().split())))
if a == list(range(1, n + 1)):
    print("Yes")
else:
    print("No")
