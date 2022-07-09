s = input()
t = input()

s_cnt = []
t_cnt = []

i = 0
j = 0

if s == t:
    print("Yes")
    exit()

if set(s) != set(t):
    print("No")
    exit()

while i < len(s):
    s_char = s[i]
    s_cnt = 0
    while i < len(s) and s[i] == s_char:
        i += 1
        s_cnt += 1

    if j >= len(t):
        print("No")
        exit()

    t_char = t[j]
    t_cnt = 0
    while j < len(t) and t[j] == t_char:
        j += 1
        t_cnt += 1

    if s_char != t_char:
        print("No")
        exit()

    if s_char > t_char or (s_cnt == 1 and s_cnt < t_cnt):
        print("No")
        exit()

if j != len(t):
    print("No")
else:
    print("Yes")
