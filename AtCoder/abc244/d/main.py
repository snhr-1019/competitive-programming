s = list(input().split())
t = list(input().split())

s_map = {s[0]: 0, s[1]: 1, s[2]: 2}

t_ls = [s_map[t[0]], s_map[t[1]], s_map[t[2]]]

if t_ls in [[0, 1, 2], [2, 0, 1], [1, 2, 0]]:
    print("Yes")
else:
    print("No")
