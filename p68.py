
# coding: utf-8
#!/usr/bin/env python

count = 1
for i in range(1,11):
    count *= i
print count

#用itertools中的全排列函数暴力解决

import itertools

def catList(L):
    s = ''
    for item in L:
        s += repr(item)
    return s

M = range(5)
L = range(5)
resultMax = 0
count = 0
for item in itertools.permutations(range(1,11), 10):
    M[0] = [item[0] , item[5] , item[6]]
    M[1] = [item[1] , item[6] , item[7]]
    M[2] = [item[2] , item[7] , item[8]]
    M[3] = [item[3] , item[8] , item[9]]
    M[4] = [item[4] , item[9] , item[5]]
    for i in range(5):
        L[i] = sum(M[i])
    if (max(L) != min(L)) or (10 in item[5:]):
        continue
    else:
        s = range(5)
        for i in range(5):
            s[i] = catList(M[(i+0)%5]) + catList(M[(i+1)%5]) + catList(M[(i+2)%5]) + catList(M[(i+3)%5]) + catList(M[(i+4)%5])
            if s[i][0] == '1':
                s[i] = '9999999999999999'
            s[i] = int(s[i])
        sMax = min(s)
        if sMax > resultMax:
            resultMax = sMax
            print resultMax, item, s

