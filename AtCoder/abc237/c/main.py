s = list(input())
s.reverse()
n = len(s)

i = 0
while True:
    if n // 2 < i:
        break
    front = i
    back = n - 1 - i
    if s[front] == 'a':
        if s[back] == 'a':
            pass
        else:
            s.append('a')
            n += 1
    else:
        if s[back] != s[front]:
            print("No")
            exit()
    i += 1

print("Yes")
