h, w = map(int, input().split())
r, c = map(int, input().split())

if [h, w] == [1, 1]:
    print(0)
    exit()

flag = (h == 1 or w == 1)
if [r, c] in [[1, 1], [1, w], [h, 1], [h, w]]:
    print(2 - flag)
elif r == 1 or r == h or c == 1 or c == w:
    print(3 - flag)
else:
    print(4 - flag)
