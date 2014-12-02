# -*- coding: utf-8 -*-

#!/usr/bin/env python
#p61

import itertools

p3 = []
n = 1
y = n*(n+1)/2
while y < 10000:
    if y>=1000:
        p3 += [y]
#        print y,n
    y = n*(n+1)/2
    n += 1

p4 = []
n = 1
y = n**2
while y < 10000:
    if y>=1000:
        p4 += [y]
#        print y,n
    y = n**2
    n += 1

p5 = []
n = 1
y = n*(3*n-1)/2
while y < 10000:
    if y>=1000:
        p5 += [y]
#        print y,n
    y = n*(3*n-1)/2
    n += 1

p6 = []
n = 1
y = n*(2*n-1)
while y < 10000:
    if y>=1000:
        p6 += [y]
#        print y,n
    y = n*(2*n-1)
    n += 1

p7 = []
n = 1
y = n*(5*n-3)/2
while y < 10000:
    if y>=1000:
        p7 += [y]
#        print y,n
    y = n*(5*n-3)/2
    n += 1

p8 = []
n = 1
y = n*(3*n-2)
while y < 10000:
    if y>=1000:
        p8 += [y]
#        print y,n
    y = n*(3*n-2)
    n += 1

def main(p):
    for order in itertools.permutations(p,6):
        for a in order[0]:
            ax = int(a / 100)
            ay = int(a % 100)
            for b in order[1]:
                bx = int(b / 100)
                if ay!=bx: continue
                by = int(b % 100)
                for c in order[2]:
                    cx = int(c / 100)
                    if by!=cx: continue
                    cy = int(c % 100)
                    for d in order[3]:
                        dx = int(d / 100)
                        if cy!=dx: continue
                        dy = int(d % 100)
                        for e in order[4]:
                            ex = int(e / 100)
                            if dy!=ex: continue
                            ey = int(e % 100)
                            for f in order[5]:
                                fx = int(f / 100)
                                if ey!=fx: continue
                                fy = int(f % 100)
                                if ax!=fy:continue
                                else: print a,b,c,d,e,f,'sum=',sum([a,b,c,d,e,f])

if __name__ == '__main__':
    p = [p3,p4,p5,p6,p7,p8]
    main(p)

