n = int(input())
arr = [int(a) for a in input().strip().split(' ')]

for i in range(1,len(arr)-1,-1):
    if arr[i] < arr[i-1]:
        e = arr[i]
    print(' '.join([str(a) for a in arr]))
        

print(arr)
