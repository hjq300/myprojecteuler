#!/usr/bin/env python

import sympy

def fun(n):
    x = 0
    for item in list(str(n)):
        x += sympy.factorial(item)
    return x

N = 1000000
d = {}
for i in range(1,N):
    if i % 100000 == 0:
        print i, len(d)
    if d.has_key(i):
        continue
    s = [i]
    while 1:
        c = fun(s[-1])
        if d.has_key(c):
            L = len(s)
            j = 0
            for item in s:
                d[item] = L + d[c] - j
                j += 1
            break
        elif c in s:
            start = s.index(c)
            part1 = s[:start]
            part2 = s[start:]
            part1L = len(part1)
            part2L = len(part2)
            j = 0
            for item in part1:
                d[item] = part1L - j + part2L
                j += 1
            for item in part2:
                d[item] = part2L
            break
        else:
            s.append(c)

count = 0
for item in d.keys():
    if 60 == d[item]:
        count += 1
        print item, d[item]

print count
