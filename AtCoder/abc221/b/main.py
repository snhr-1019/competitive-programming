S = input()
T = input()

for i in range(len(S) - 1):
    l = list(S)
    l[i], l[i + 1] = l[i + 1], l[i]
    if S == T or T == ''.join(l):
        print("Yes")
        exit()
print("No")
