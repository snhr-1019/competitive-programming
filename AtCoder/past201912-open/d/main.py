n = int(input())
cnt = {x: 0 for x in range(1, n + 1)}

for i in range(n):
    cnt[int(input())] += 1

before = -1
after = -1
for i in range(1, n + 1):
    if cnt[i] == 0:
        before = i
    if cnt[i] == 2:
        after = i

if before == -1:
    print("Correct")
else:
    print(after, before)
