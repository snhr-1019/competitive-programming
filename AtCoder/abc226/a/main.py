X = input()
if '.' in X:
    l = X.split('.')
    if int(l[1][0]) >= 5:
        print(int(l[0]) + 1)
    else:
        print(int(l[0]))
else:
    print(X)
