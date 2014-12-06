#!/usr/bin/env python
# use Farey sequence
N = 1000000
q = 1
a, b = 2, 5
c, d = 3, 7
while b < N:
    p = a+c
    q = b+d
    a = p
    b = q
    print p, q

