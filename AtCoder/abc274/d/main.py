n, x, y = map(int, input().split())
A = list(map(int, input().split()))

x_list = []
y_list = []
for i in range(1, n):
    if i % 2 == 0:
        x_list.append(A[i])
    else:
        y_list.append(A[i])

dp = set()
dp.add(A[0])
for a in x_list:
    new_dp = set()
    for cur in dp:
        new_dp.add(cur + a)
        new_dp.add(cur - a)
    dp = new_dp

if x not in dp:
    print("No")
    exit()

dp = set()
dp.add(0)
for a in y_list:
    new_dp = set()
    for cur in dp:
        new_dp.add(cur + a)
        new_dp.add(cur - a)
    dp = new_dp
if y not in dp:
    print("No")
    exit()
print("Yes")
