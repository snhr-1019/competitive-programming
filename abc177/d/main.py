n, m = map(int, input().split())

friend_list = [set()]
input_list = []

for i in range(m):
    a, b = map(int, input().split())
    input_list.append(sorted([a, b]))

input_list.sort()

for inp in input_list:
    found = False
    for friend_set in friend_list:
        if inp[0] in friend_set:
            friend_set.add(inp[1])
            found = True
            break
        # elif b in friend_set:
        #     friend_set.add(a)
        #     found = True
        #     break
    if not found:
        friend_set = set()
        friend_set.add(inp[0])
        friend_set.add(inp[1])
        friend_list.append(friend_set)

ans = 0
for friend_set in friend_list:
    ans = max(len(friend_set), ans)

print(ans)