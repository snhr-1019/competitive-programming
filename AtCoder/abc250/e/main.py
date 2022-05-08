n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

mapping = {}
cur = -1
a_sets = [0] * n
for i in range(n):
    if a[i] not in mapping.keys():
        # 新しい要素が出てきた
        cur += 1
        mapping[a[i]] = cur
    a[i] = mapping[a[i]]
    a_sets[i] = cur

b_sets = [0] * n
b_set = set()
ng = False
for i in range(n):
    if a[i] not in mapping:
        is_ng = True
    else:
        mapping_b = mapping[b[i]]
    if is_ng:
        b_sets[i] = {}
        continue

    b_set.add(mapping_b)
    b_sets[i] = set(b_set)

print(b_sets)