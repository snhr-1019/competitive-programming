n = input()

sum_val = 0
for i in range(len(n)):
    sum_val += int(n[i])

if sum_val % 9 == 0:
    print("Yes")
else:
    print("No")
