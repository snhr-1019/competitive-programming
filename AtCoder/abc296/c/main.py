n, x = map(int, input().split())
a = set(map(int, input().split()))

for ai in a:
    if ai + x in a:
        print("Yes")
        exit()
print("No")
