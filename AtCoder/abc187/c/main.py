from collections import defaultdict
N = int(input())

str_set = defaultdict(int)
for i in range(N):
    s = input()
    if s.startswith("!"):
        s = s[1:]
        if str_set[s] != 2:
            str_set[s] += 2
    else:
        if str_set[s] != 1:
            str_set[s] += 1

    if str_set[s] == 3:
        print(s)
        exit(0)

print("satisfiable")
