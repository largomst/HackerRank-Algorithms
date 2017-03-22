#!/bin/python3

import sys

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)
