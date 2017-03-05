n, m = input().strip().split(' ')
n, m = int(n), int(m)
a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
b = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def factor(n):
    factor_list = list()
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.append(i)
    return factor_list


factor_of_b = set()
for elem in b:
    for i in factor(elem):
        factor_of_b.add(i)

a_factor = set(a)

union = factor_of_b.intersection(a_factor)

print(len(union))
