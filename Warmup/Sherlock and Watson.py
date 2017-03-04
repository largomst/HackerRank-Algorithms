n, k, q = [int(a) for a in input().strip().split(' ')]
arr = [int(a) for a in input().strip().split(' ')]
m = []
for i in range(q):
    m.append(int(input().strip()))

for i in range(k):
    arr.insert(0, arr.pop())

for i in range(q):
    print(arr[i])

# TODO　性能问题待解决
