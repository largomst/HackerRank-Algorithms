n = int(input())
arr = list(map(lambda x: int(x), input().strip().split(' ')))

arr_count = dict()
for i in arr:
    arr_count[i] = 0

for i in arr:
    arr_count[i] += 1

aim = max(arr_count.items(), key=lambda x: x[1])[0]

count = 0
for i in arr:
    if i != aim:
        count += 1

print(count)
