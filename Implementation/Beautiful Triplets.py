n, d = input().strip().split(' ')
n, d = int(n), int(d)
a = list(map(int, input().strip().split(' ')))

pairs = list()

for i in range(n):
    for j in range(i, n):
        if d == a[j] - a[i]:
            pairs.append((a[j], a[i]))

result = []
for i in range(len(pairs)):
    for j in range(i, len(pairs)):
        if pairs[i][0] == pairs[j][1]:
            result.append((pairs[i][1], pairs[i][0], pairs[j][1]))

print(len(result))
