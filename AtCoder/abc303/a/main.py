n = int(input())
s = input()
t = input()

for i in range(n):
    if s[i] == t[i]:
        continue
    if {s[i], t[i]} == {'1', 'l'}:
        continue
    if {s[i], t[i]} == {'0', 'o'}:
        continue
    print("No")
    exit()
print("Yes")
