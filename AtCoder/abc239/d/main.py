a, b, c, d = map(int, input().split())
prime = [True] * 300

for i in range(2, 30):
    j = 2
    while True:
        if i * j >= 300:
            break
        prime[i * j] = False
        j += 1

aoki_d = d - c

# 素数がない区間の最大
max_d = 0

prev_prime = a + c - 1
for i in range(a + c, b + d + 1):
    if prime[i]:
        max_d = max(max_d, i - prev_prime - 1)
        prev_prime = i
max_d = max(max_d, b + d + 1 - prev_prime - 1)
if max_d > aoki_d:
    print('Takahashi')
else:
    print('Aoki')
