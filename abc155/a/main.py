a, b, c = map(int, input().split())

if (a == b and b != c) or (b == c and c != a) or (c == a and a != b):
    print("Yes")
else:
    print("No")