n = int(input().strip())

sum = 0
next_suc = 5

for i in range(n):
    cur_suc = next_suc // 2
    fail = next_suc - cur_suc
    sum += cur_suc
    next_suc = cur_suc * 3

print(sum)
