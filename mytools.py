#-*- coding: utf-8 -*-
#!/usr/bin/env python

class H_math:
    '''自己写的数学函数，方便计算用'''
    def __init__(self):
        pass

    def add(self, a=(0,1), b=(0,1)):
        '''计算两个分数的和，返回一个分数
        a1/a2 + b1/b2 = (a1*b2+a2*b1)/(a2*b2)
        例：
        计算3/5+6/4
        add((3,5),(6,4))
        结果为(42,20)
        '''
        self.a = 'hello'
        (aNum, aDiv) = a
        (bNum, bDiv) = b
        return tuple([aNum*bDiv+aDiv*bNum, aDiv*bDiv])

    # 产生3个数的最大公约数
    def gcd3(self, a, b, c):
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
    # 连分数中产生下一个项
    def continuedFractionStep1(self, a,b,c,x):
        m = int((a*x**0.5+b)/c)
        b = b - c*m
        a2 = a*c
        b2 = -b*c
        c2 = a**2*x-b**2
        if c2 == 0:    #if x is the square number
            return (m, 0, 0, 1)
        g = gcd3(a2,b2,c2)
        return (m, a2/g, b2/g, c2/g)

    # 产生sqrt(x)的连分数表达式，返回值的第一个为首项，第二项到最后一项为循环节
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

    # 计算a[0]/a[1]+b[0]/b[1]，并返回分数表示式
    def add(a = (0,1), b = (0,1)):
        numerator = a[0]*b[1]+a[1]*b[0]
        divider = a[1]*b[1]
        g = gcd3(0,numerator,divider)
        return (numerator/g,divider/g)

    # 计算sqrt(x)的第n个连分数近似
    def approxContinuedFraction(x, n):
        rep = continuedFraction(x)
        N = n
        s = [rep[0]]
        lo = rep[1:]
        L = len(lo)
        count = 1
        i = 0
        while count < N:
            s.append(lo[i%L])
            i += 1
            count += 1
        s.reverse()
        result = (s[0],1)
        if len(s) == 1:
            return result
        else:
            for item in s[1:]:
                result = add((item,1), (result[1],result[0]))
            return result

if __name__ == '__main__':
    print '自己重构的工具，方便计算'
