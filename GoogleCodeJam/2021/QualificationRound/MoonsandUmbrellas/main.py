import re

T = int(input())

for case in range(T):
    x, y, mural = input().split()
    X = int(x)
    Y = int(y)

    # 複数回の?を1回にまとめる
    mural = re.sub('[?]+', '?', mural)
    mural = list(mural)

    cost = 0
    for i in range(len(mural)):
        if mural[i] == '?':
            if i == 0:
                if i != len(mural) - 1:
                    # 一番後ろでなければ次の文字と同じにする
                    mural[i] = mural[i + 1]
                else:
                    # ?しかない場合なので、どっちでもいい
                    mural[i] = 'C'
            else:
                mural[i] = mural[i - 1]

        if i > 0:
            if mural[i - 1] == 'C' and mural[i] == 'J':
                cost += X
            elif mural[i - 1] == 'J' and mural[i] == 'C':
                cost += Y
    print("Case #%d: %d" % (case + 1, cost))
