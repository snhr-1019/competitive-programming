S = input()
s = set(list(S))
if len(s) == 1:
    print(1)
elif len(s) == 2:
    print(3)
else:
    print(6)
