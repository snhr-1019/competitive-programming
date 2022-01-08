x = list(map(int, input()))

l = len(x)
if l == 1 or l == 2:
    print(''.join(map(str, x)))
    exit()

# 最初から等差数かどうか
ok = True
d = x[1] - x[0]
for i in range(2, l):
    if x[i] - x[i - 1] != d:
        ok = False
if ok:
    print(''.join(map(str, x)))
    exit()

# 2桁目が2桁目と同じか小さい場合、下がっていく等差数の可能性がある
if x[0] >= x[1]:
    d = min(x[0] // (len(x) - 1), x[1] - x[0])

    while d <= 9:
        print(d)
        candidate = x[:]
        ok = True
        for i in range(1, len(x)):
            tmp = candidate[i - 1] + d
            if tmp > 9 or tmp < 0 or tmp < x[i]:
                ok = False
                break
            candidate[i] = tmp

        if ok:
            print(''.join(map(str, candidate)))
            exit()
        d += 1

# 一番上の桁を上げずに等差数を作れるか
ok = True
d = max(0, x[1] - x[0])

candidate = x[:]
for i in range(1, l):
    tmp = candidate[i - 1] + d
    candidate[i] = tmp
    if tmp > 9 or tmp < 0:
        ok = False
        break

if ok:
    print(''.join(map(str, candidate)))
    exit()

# 一番上の桁を上げる場合
if x[0] == 9:
    x = [1] + x
    x[1] = 0
else:
    x[0] += 1

d = x[0] // (len(x) - 1)
candidate = x[:]

for i in range(1, len(x)):
    candidate[i] = candidate[i - 1] - d
print(''.join(map(str, candidate)))
