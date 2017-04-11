# TODO fix time out

def solution(a):
    ok = True
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1] and abs(a[j] - a[j + 1]) == 1:
                a[j], a[j + 1] = a[j + 1], a[j]

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