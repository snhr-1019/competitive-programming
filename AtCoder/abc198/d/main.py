import itertools

S1 = input()
S2 = input()
S3 = input()

n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for v in itertools.permutations(n, 10):
    lv = list(v)
    chars = dict()

    i1 = 0
    for i, s in enumerate(S1[::-1]):
        if not chars.get(s):
            if not lv:
                print("UNSOLVABLE")
                exit()
            chars[s] = lv.pop()

        i1 += chars[s] * 10 ** i

    i2 = 0
    for i, s in enumerate(S2[::-1]):
        if not chars.get(s):
            if not lv:
                print("UNSOLVABLE")
                exit()
            chars[s] = lv.pop()

        i2 += chars[s] * 10 ** i

    i3 = 0
    for i, s in enumerate(S3[::-1]):
        if not chars.get(s):
            if not lv:
                print("UNSOLVABLE")
                exit()
            chars[s] = lv.pop()

        i3 += chars[s] * 10 ** i

    if chars[S1[0]] == 0 or chars[S2[0]] == 0 or chars[S3[0]] == 0:
        continue

    if i1 + i2 == i3:
        print(str(i1) + "\n" + str(i2) + "\n" + str(i3))
        exit()

print("UNSOLVABLE")

