s = input()

if s[0].isalpha() and s[-1].isalpha() and s[1:7].isnumeric() and 100000 <= int(s[1:7]) <= 999999:
    print("Yes")
else:
    print("No")
