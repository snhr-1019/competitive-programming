A, B = input().split()


def getSum(str):
    sumval = 0
    for c in str:
        sumval += int(c)
    return sumval


print(max(getSum(A), getSum(B)))
