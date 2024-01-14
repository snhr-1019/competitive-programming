n = int(input())
s = str(bin(n))

for i in range(len(s)):
    if s[~i] == '1':
        print(i)
        exit()
print(len(s))
