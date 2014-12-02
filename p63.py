# coding: utf-8
#!/usr/bin/env python
#p63

import math

for n in range(2,20):
    print math.log((10**n-1)/10**(n-1))/math.log(n), n


print math.log(10**8)/math.log(9)
print math.log(10**9-1)/math.log(9)


