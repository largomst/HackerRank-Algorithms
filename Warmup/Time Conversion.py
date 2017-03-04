#!/bin/python3

import re

12time = input().strip()
pattern = re.compile(r'(\d+):(\d+):(\d+)(\w+)')
match = pattern.match(time)
if match:
    groups = match.groups()
    groups = list(groups)
    if groups[3] == 'AM':
        if groups[0] == '12':
            groups[0] = '00'
    else:
        if groups[0] == '12':
            pass
        else:
            groups[0] = str(int(groups[0]) + 12)
    new_time = ':'.join(groups[:3])
    print(new_time)

# from datetime import datetime
# t = input()

# dt=datetime.strptime(t, '%I:%M:%S%p')
# print(dt.strftime('%H:%M:%S'))
