def growp(t, h):
    if t == 0:
        return h
    else:
        if t % 2 == 0:
            return growp(t - 1, h) + 1
        else:
            return growp(t - 1, h) * 2

n = int(input().strip())
for i in range(n):
    print(growp(int(input().strip()), 1))
