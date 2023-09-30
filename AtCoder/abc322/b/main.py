n, m = map(int, input().split())
s = input()
t = input()

pre = t.startswith(s)
suf = t.endswith(s)
if pre and suf:
    print(0)
elif pre:
    print(1)
elif suf:
    print(2)
else:
    print(3)
