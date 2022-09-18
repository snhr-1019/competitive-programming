n = bin(int(input()))
t = []
for i in range(len(n)):
    if n[-i - 1] == '1':
        t.append(i)
m = len(t)
for i in range(2 ** m):
    val = 0
    for j in range(m):
        if (i >> j) & 1:
            val += 2 ** t[j]
    print(val)
