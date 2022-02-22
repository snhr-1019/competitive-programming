import re

s = input()
if re.search('[^0-9]', s):
    print("error")
else:
    print(int(s) * 2)
