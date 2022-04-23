s = input()

exist_upper = False
exist_lower = False

for i in range(len(s)):
    if s[i].islower():
        exist_lower = True
    if s[i].isupper():
        exist_upper = True

if len(set(s)) == len(s) and exist_lower and exist_upper:
    print("Yes")
else:
    print("No")
