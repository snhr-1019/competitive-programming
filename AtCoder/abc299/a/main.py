n = int(input())
s = input()

is_start = False
for si in s:
    if si == '|':
        is_start = not is_start
    elif is_start and si == '*':
        print('in')
        exit()
print('out')
