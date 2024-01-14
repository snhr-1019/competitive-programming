n = int(input()) - 1

l = []
if n == 0:
    print(0)
    exit()

while n:
    l.append(str((n % 5) * 2))
    n //= 5
l.reverse()
print(''.join(l))
