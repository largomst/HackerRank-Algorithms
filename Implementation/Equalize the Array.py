n = int(input())
arr = list(map(lambda x: int(x), input().strip().split(' ')))

print(n - max([arr.count(t) for t in set(arr)]))
