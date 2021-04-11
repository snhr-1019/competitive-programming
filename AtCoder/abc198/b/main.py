import re

N = input()
match = re.search(r'0+$', N)
if match:
    N = match.group() + N

if N == N[::-1]:
    print("Yes")
else:
    print("No")
