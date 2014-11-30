#!/usr/bin/env python

N = 100
t = {}
for i in range(2,N+1):
    t[i] = i
for i in range(1,N+1):
    print i
    for n in range(2,N+1):
        m = i*n
        if m > N:
            break
        else:
            t[m] -= 1
