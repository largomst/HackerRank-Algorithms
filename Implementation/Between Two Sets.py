n, m = input().strip().split(' ')
n, m = int(n), int(m)
a = [int(arr_temp) for arr_temp in input().strip().split(' ')]
b = [int(arr_temp) for arr_temp in input().strip().split(' ')]


def factor(n):
    factor_list = set()
    for i in range(1, n + 1):
        if n % i == 0:
            factor_list.add(i)
    return factor_list


# **x** is a factor of all elements in **B**.

a_factor_of_B = factor(b[0])

for i in b:
    a_factor_of_B = a_factor_of_B.intersection(factor(i))

result = set()

a_factor = set(a)
for i in a_factor_of_B:
    if a_factor.intersection(factor(
            i)) == a_factor:  # All elements in **A** are factors of **x**.
        result.add(i)

print(len(result))
