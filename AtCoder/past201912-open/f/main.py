s = input()
n = len(s)
start = -1
words = []
for i in range(n):
    if s[i].islower():
        continue

    if start == -1:
        start = i
    else:
        end = i + 1
        words.append(s[start:end])
        start = -1
print(*sorted(sorted(words), key=str.lower), sep='')
