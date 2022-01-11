from math import log2, ceil

n = int(input())

div = 0
i = 2
while i * i <= n:
    while n % i == 0:
        n //= i
        div += 1
    i += 1
if n != 1:
    div += 1
print(int(ceil(log2(div))))
