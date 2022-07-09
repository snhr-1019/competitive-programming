s = input()
t = input()


# Run Length Encoding
def rle(s):
    rle = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            rle.append((s[i - 1], cnt))
            cnt = 0
        cnt += 1
    rle.append((s[-1], cnt))
    return rle


rle_s = rle(s)
rle_t = rle(t)

if len(rle_s) != len(rle_t):
    print("No")
    exit()

for i in range(len(rle_s)):
    if rle_s[i][0] != rle_t[i][0]:
        print("No")
        exit()

    if rle_s[i][1] > rle_t[i][1]:
        print("No")
        exit()

    if rle_s[i][1] == 1 and rle_s[i][1] < rle_t[i][1]:
        print("No")
        exit()

print("Yes")
