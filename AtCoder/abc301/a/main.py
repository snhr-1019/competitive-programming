n = int(input())
s = input()
t = 0
a = 0
k = -(-n // 2)
for c in s:
    if c == "T":
        t += 1
    else:
        a += 1
    if t >= k:
        print("T")
        exit()
    if a >= k:
        print("A")
        exit()
