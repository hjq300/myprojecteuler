# coding: utf-8
#!/usr/bin/env python
import sympy
import itertools

def phi(n):
    '''
    产生phi函数，输入为n，返回phi(n)，算法为：
    将n分解质因数，比如n的质因数有：a b c d
    则
    phi(n) = 
        n
        -       (n/a + n/b + n/c +n/d - 4)
        +       (n/ab + n/ac + n/ad + n/bc + n/bd + n/cd - 6)
        -       (n/abc + n/abd + n/acd + n/bcd - 4)
        +       (n/abcd - 1)
    '''
    N = n
    phiN = n
    s = sympy.factorint(N).keys()
    for i in range(len(s)):
        for item in itertools.combinations(s,i+1):
            x = 1
            for j in item:
                x *= j
            phiN += (-1)**(i+1)*(N/x)
    return phiN

if __name__ == '__main__':
    N = 1000000
    m = 1.0
    for n in range(2,N):
        x = n*1.0/phi(n)
        if x > m:
            m = x
            print n, phi(n), m
