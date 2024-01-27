import re

s = input()

if re.fullmatch(r'A*B*C*', s):
    print('Yes')
else:
    print('No')
