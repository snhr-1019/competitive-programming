n = int(input())
t = input()

for i in range(n):
    a = t[:i] + t[-(n - i):]
    b = t[i:i + n][::-1]
    if a == b:
        print(a, i)
        exit()
print(-1)
