n = int(input().strip())

result = 'min(int, int)'

for i in range(n - 2):
    result = 'min(int, ' + result + ')'

print(result)
