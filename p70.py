# -*- coding: utf-8 -*-
#!/usr/bin/env python

from mytools import H_math
from sympy.ntheory import primerange

if __name__ == '__main__':
    N = 10000000
    M = 5.0
    for n in range(2,N):
        phin = H_math().phi(n)
        s = list(str(phin))
        s.sort()
        m = list(str(n))
        m.sort()
        if m == s:
            x = n*1.0/phin
            if x < M:
                M = x
                print n,phin,M
