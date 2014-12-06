#!/usr/bin/env python

from mytools import H_math

N = 1000001
f = 0
for i in range(2,N):
    f += H_math().phi(i)

print f
