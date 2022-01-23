n, m = map(int, input().split())

s = list(input().split())
t = set(list(input().split()))

for v in s:
    if v in t:
        print("Yes")
    else:
        print("No")
