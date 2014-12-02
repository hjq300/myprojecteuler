
# coding: utf-8
#!/usr/bin/env python

def str2digit(Li):
    return [int(item) for item in Li]   #注意对item进行转换的时候不要用eval，因为eval('08')这种以0开头的数字会让eval认为这是个8进制数，从而报错。

f = open('p067_triangle.txt','r')
t = f.read()
f.close()
t = t.split('\n')
t.pop()
T = [item.split() for item in t]
T = [str2digit(item) for item in T]

T.reverse()
print T

for i in range(99):
    for j in range(len(T[i+1])):
        if T[i][j] > T[i][j+1]:
            T[i+1][j] += T[i][j]
        else:
            T[i+1][j] += T[i][j+1]

print T




