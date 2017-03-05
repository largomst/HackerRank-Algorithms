n, k = input().strip().split(' ')
n, k = int(n), int(k)
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
anna = int(input().strip())

mean = (sum(arr) - arr[k]) / 2
change_anna = anna - mean
if change_anna > 0:
    print(int(change_anna))
else:
    print('Bon Appetit')
