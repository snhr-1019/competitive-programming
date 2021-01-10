N, C = map(int, input().split())

event = []

for i in range(N):
    ai, bi, ci = map(int, input().split())
    bi += 1
    event.append((ai, ci))
    event.append((bi, -ci))

event.sort()

sum_cost = 0
day_cost = 0
t = 0
for x, y in event:
    if x != t:
        sum_cost += min(day_cost, C) * (x - t)
        t = x
    day_cost += y

print(sum_cost)
