T = int(input())

for case in range(T):
    N = int(input())
    Xs = list(map(int, input().split()))

    ans = 0
    for i in range(1, N):
        # ソートされてる場合はそのまま
        if Xs[i - 1] < Xs[i]:
            pass
        else:
            if len(str(Xs[i - 1])) == len(str(Xs[i])):
                # 桁数は一緒のときは単純に0をつける
                ans += 1
                Xs[i] *= 10
            else:
                # 桁数が左のほうが大きい場合
                diff = len(str(Xs[i - 1])) - len(str(Xs[i]))

                if Xs[i-1] < Xs[i] * 10 ** diff:
                    # 0で桁数揃うようにうめてOKか
                    ans += diff
                    Xs[i] *= 10 ** diff
                elif str(Xs[i-1]).startswith(str(Xs[i])) and Xs[i-1] < int(str(Xs[i]) + ('9' * diff)):
                    # 9で桁数揃うようにうめてOKになるなら、左と同じ数字よりも1大きい数字
                    ans += diff
                    Xs[i] = Xs[i-1] + 1
                else:
                    # 上記以外は、桁数揃うように0埋めて
                    ans += diff
                    Xs[i] *= 10 ** diff

                    # それでも足りなければもう1桁
                    if Xs[i - 1] >= Xs[i]:
                        ans += 1
                        Xs[i] *= 10
#    print(Xs)
    print("Case #%d: %d" % (case + 1, ans))
