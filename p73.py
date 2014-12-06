#!/usr/bin/env python
# use Farey sequence

def fareyNum((a1,a2),(b1,b2)):
    a = [(a1,a2),(b1,b2)]
    L = len(a)
    i = 0
    N = 12000
    while i+1 <= L-1:
        q = a[i][1] + a[i+1][1]
        if q > N:
            i +=1
        else:
            p = a[i][0] + a[i+1][0]
            a.insert(i+1,(p,q))
            L = len(a)
    return L - 2  #reduce the head and end

a = fareyNum((1,3),(3,8))
b = fareyNum((3,8),(2,5))
c = fareyNum((2,5),(3,7))
d = fareyNum((3,7),(1,2))

print '1/3 ~ 3/8 : ', a
print '3/8 ~ 2/5 : ', b
print '2/5 ~ 3/7 : ', c
print '3/7 ~ 1/2 : ', d

print '1/3 ~ 1/2 : ', a+b+c+d+3
