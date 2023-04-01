for i in range(8, 0, -1):
    s = input()
    for j in range(8):
        if s[j] == "*":
            print(chr(j + ord('a')) + str(i))
