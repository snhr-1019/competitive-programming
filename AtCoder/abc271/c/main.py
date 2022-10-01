n = int(input())
a = list(map(int, input().split()))
set_a = set(a)

remain = n
target = 1
while remain > 0:
    # 最初から持っている場合
    if target in set_a:
        target += 1
        remain -= 1
    elif remain >= 2:
        target += 1
        remain -= 2
    else:
        break

print(target - 1)
