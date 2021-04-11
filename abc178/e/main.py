N = int(input())

x_list = []
y_list = []

for i in range(N):
    x, y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

max_x = max(x_list)
min_x = min(x_list)
max_y = max(y_list)
min_y = min(y_list)

point_list = []
for i in range(N):
    if x_list[i] == max_x or x_list[i] == min_x or y_list[i] == max_y or y_list[i] == min_y:
        point_list.append([x_list[i], y_list[i]])

ans = 0
for i in range(len(point_list)):
    point_a = point_list[i]
    for j in range(i+1, len(point_list)):
        point_b = point_list[j]
        ans = max(ans, abs(point_a[0] - point_b[0]) + abs(point_a[1] - point_b[1]))

print(ans)