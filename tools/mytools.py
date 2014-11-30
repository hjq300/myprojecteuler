#-*- coding: utf-8 -*-
#!/usr/bin/env python

class H_math:
    '''自己写的数学函数，方便计算用'''

    def add(a=(0,1), b=(0,1)):
        '''计算两个分数的和，返回一个分数
        a1/a2 + b1/b2 = (a1*b2+a2*b1)/(a2*b2)
        例：
        计算3/5+6/4
        add((3,5),(6,4))
        结果为(42,20)
        '''
        (aNum, aDiv) = a
        (bNum, bDiv) = b
        return tuple([aNum*bDiv+aDiv*bNum, aDiv*bDiv])

if __name__ == '__main__':
    print '自己重构的工具，方便计算'
