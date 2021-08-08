X = list(map(int, list(input())))

if X[0] == X[1] == X[2] == X[3]:
    print('Weak')
    exit()

weak = True
for i in range(3):
    if (X[i] + 1) % 10 == X[i + 1]:
        continue
    else:
        weak = False
if weak:
    print('Weak')
else:
    print('Strong')
