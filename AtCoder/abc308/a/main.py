s = list(map(int, input().split()))

for i in range(len(s)):
    if i != 0:
        if s[i - 1] > s[i]:
            print("No")
            exit()

    if s[i] < 100 or s[i] > 675:
        print("No")
        exit()

    if s[i] % 25 != 0:
        print("No")
        exit()
print("Yes")
