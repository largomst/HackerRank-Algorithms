def solution(a):
    ok = True
    for i in range(len(a) - 2):
        if a[i] > a[i + 1] and abs(a[i] - a[i + 1]) == 1:
            a[i], a[i + 1] = a[i + 1], a[i]
        if a[i + 1] > a[i + 2] and abs(a[i + 1] - a[i + 2]) == 1:
            a[i + 1], a[i + 2] = a[i + 2], a[i + 1]

    for i in range(len(a) - 1):
        if a[i] > a[i + 1]:
            ok = False
            break

    return ok


q = int(input().strip())
for a0 in range(q):
    n = int(input().strip())
    a = list(map(int, input().strip().split(' ')))
    print('Yes' if solution(a) else 'No')
