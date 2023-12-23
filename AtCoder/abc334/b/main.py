a, m, l, r = map(int, input().split())


def count_trees(A, M, L, R):
    start = (L - A + M - 1) // M
    end = (R - A) // M
    trees = end - start + 1
    return trees


print(count_trees(a, m, l, r))
