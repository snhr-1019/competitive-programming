x = int(input())

for l in range(len(str(x)), 19):
    for first in range(1, 10):
        for d in range(-9, 9):
            ok = True
            a = []
            for i in range(l):
                tmp = first + d * i
                a.append(tmp)
                if tmp > 9 or tmp < 0:
                    ok = False
                    break
            if ok:
                candidate = int(''.join(map(str, a)))
                if x <= candidate:
                    print(candidate)
                    exit()
