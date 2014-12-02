
# coding: utf-8
#!/usr/bin/env python

def gcd3(a,b,c):
    x = a
    y = b
    z = c
    minN = min(x,y,z)
    maxN = max(x,y,z)
    if sum((x,y,z)) == maxN:
        return maxN
    d = [x,y,z]
    d.sort()
    if minN == 0:
        return gcd3(0,    d[1],      d[2]-d[1])
    else:
        return gcd3(d[0], d[1]-d[0], d[2]-d[0])

# y = (a*sqrt(x) + b) / c
def continuedFractionStep1(a,b,c,x):
    m = int((a*x**0.5+b)/c)
    b = b - c*m
    a2 = a*c
    b2 = -b*c
    c2 = a**2*x-b**2
    if c2 == 0:    #if x is the square number
        return (m, 0, 0, 1)
    g = gcd3(a2,b2,c2)
    return (m, a2/g, b2/g, c2/g)

def continuedFraction(x):
    loop = {}
    rep = []
    (a,b,c) = (1,0,1)
    while 1:
        (m,a,b,c) = continuedFractionStep1(a,b,c,x)
        if loop.has_key((a,b,c)):
            rep.append(m)
            return rep
        else:
            rep.append(m)
            loop[(a,b,c)] = True

count = 0
for x in range(1,10001):
    cfList = continuedFraction(x)
    #print x,cfList
    if (len(cfList)%2==0) and (cfList[1]!=0):
        count += 1
print count

