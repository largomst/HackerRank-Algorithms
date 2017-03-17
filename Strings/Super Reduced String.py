s = input()
s_count_dict = dict()
s_new = list()
for i in s:
    s_count_dict[i] = 0
for i in s:
    s_count_dict[i] += 1

for i in s_count_dict:
    s_count_dict[i] = s_count_dict[i] % 2
for i in s:
    if s_count_dict[i] == 1:
        s_new.append(i)
        s_count_dict[i] = 0

s = ''.join(s_new)
if s == '':
    print('Empty String')
else:
    print(s)
