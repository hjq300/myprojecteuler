
# coding: utf-8

#!/usr/bin/env python
#p62

data = {}

for i in range(100,10000):
    s = list(repr(i**3))   #s =  list(s)    #important skill
    s.sort()
    s = tuple(s)
    if data.has_key(s):
        data[s] += 1
    else:
        data[s]  = 1
    if data[s] == 5:
        print s
        break

for i in range(100,10000):
    s = list(repr(i**3))   #s =  list(s)    #important skill
    s.sort()
    s = tuple(s)
    if s == ('0', '1', '2', '3', '3', '4', '5', '5', '6', '7', '8', '9'):
        print i


