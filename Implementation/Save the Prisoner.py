t = int(input().strip())
for t0 in range(t):
    n, m, s = input().strip().split(' ')
    n, m, s = int(n), int(m), int(s)
    s = s - 1
    for i in range(m):
        s = (s + 1) % n
    print(s)
