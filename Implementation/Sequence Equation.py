n = int(input().strip())
p = [int(arr_temp) for arr_temp in input().strip().split(' ')]
p.insert(0, None)
for x in range(1, len(p)):  # 先遍历 p 数组的值，再 p[p[y]] 中满足 p[p[y]] = x 的值
    for y in range(1, len(p)):
        if p[p[y]] == x:
            print(y)
