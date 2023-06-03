from math import floor

n = input()

l = len(n)
if l < 4:
    print(n)
else:
    k = 10 ** (l - 3)
    print(int(n) // k * k)
