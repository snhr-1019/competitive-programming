n = int(input())
s = input()
exist_o = False
for i in range(n):
    if s[i] == 'o':
        exist_o = True
    if s[i] == 'x':
        print("No")
        exit()
if exist_o:
    print("Yes")
else:
    print("No")
