# You are not stuck unless you have spent more than a day on a single problem

s = input()
for i in range(len(s)):
    if i != len(s) - 1 and s[i] == s[i + 1]:
        s[i] = 0
        count += 1
    else:
        if count % 2 == 0:
            pass
        else:
            s[i] = 0
        count = 0

for i in range(len(s)):
    if i = len(s)