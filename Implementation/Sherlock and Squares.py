import math
t = int(input().strip())

for t0 in range(t):
    a, b = input().strip().split(' ')
    a, b = int(a), int(b)

    a = math.sqrt(a)
    if a != int(a):
        a = int(a) + 1
    else:
        a = int(a)

    b = int(math.sqrt(b))
    lis = [x * x for x in range(a, b + 1)]
    print(len(lis))
