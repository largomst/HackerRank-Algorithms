t = int(input().strip())
for t0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = int(n), int(m), int(s)
    result = ((m + s) - 1) % n
    if result == 0:
        result = n
    print(result)

# error
# 499999999 999999997 2
# 0
# 499999999 999999998 2
# 1
# 999999999 999999999 1
# 0
# right
# 499999999
# 1
# 999999999
# 当恰好分到最后一人时，会出现 result = 0