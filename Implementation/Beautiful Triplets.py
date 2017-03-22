n, d = input().strip().split(' ')
n, d = int(n), int(d)
a = list(map(int, input().strip().split(' ')))
count = 0
for i in range(n):
    for j in range(i, n):
        for k in range(j, n):
            if a[j] - a[i] == a[k] - a[j] and a[k] - a[j] == d:
                count += 1

print(count)
