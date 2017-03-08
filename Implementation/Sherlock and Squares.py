import math
t = int(input().strip())

for t0 in range(t):
    a, b = input().strip().split(' ')
    a, b = int(a), int(b)

    a_sqrt = math.sqrt(a)
    if a_sqrt == int('%.0f' % a_sqrt):
        pass
    else:
        a_sqrt = int(a_sqrt) + 1
    li = [i * i for i in range(a_sqrt, int(math.sqrt(b)) + 1)]
    # print(li)
    print(len(li))
