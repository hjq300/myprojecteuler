# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

#!/usr/bin/env python
# copy from the website
'''
XOR decryption
URL: https://projecteuler.net/problem=60
'''
import time
import networkx as nx
from itertools import combinations
from sympy.ntheory.generate import primerange,isprime

def pp(lst):
    return isprime(int("".join([str(lst[0])+str(lst[1])]))) and \
        isprime(int("".join([str(lst[1])+str(lst[0])])))

def main():
    starttime = time.clock()

    result = []
    G=nx.Graph()#we can consider every pair is a edge. then focus the edges
    lst = [comb for comb in combinations(primerange(1,10000),2) if pp(comb)]
    G.add_edges_from(lst)
    
    for e in G.edges():
        neig = set(G.neighbors(e[0])).intersection(set(G.neighbors(e[1])))
        if len(neig)>=3:
            for comb in combinations(neig,3):
                if G.has_edge(comb[0], comb[1]):
                    if G.has_edge(comb[0], comb[2]):
                        if G.has_edge(comb[1], comb[2]):
                            t = sorted((e[0],e[1],comb[0],comb[1],comb[2]))
                            if t not in result:result.append(t)
    print min(map(sum,result))
    print result

    endtime = time.clock()
    print "running time is %f second" % (endtime - starttime)

if __name__ == '__main__':
    main()

# <codecell>

#!/usr/bin/env python
'''
XOR decryption
URL: https://projecteuler.net/problem=60
'''
import time
import networkx as nx
from itertools import combinations
from sympy.ntheory.generate import primerange,isprime

def pp(lst):
    return isprime(int("".join([str(lst[0])+str(lst[1])]))) and \
        isprime(int("".join([str(lst[1])+str(lst[0])])))


starttime = time.clock()

result = []
G=nx.Graph()#we can consider every pair is a edge. then focus the edges
lst = [comb for comb in combinations(primerange(1,10000),2) if pp(comb)]
G.add_edges_from(lst)

for e in G.edges():
    neig = set(G.neighbors(e[0])).intersection(set(G.neighbors(e[1])))
    if len(neig)>=3:
        for comb in combinations(neig,3):
            if G.has_edge(comb[0], comb[1]):
                if G.has_edge(comb[0], comb[2]):
                    if G.has_edge(comb[1], comb[2]):
                        t = sorted((e[0],e[1],comb[0],comb[1],comb[2]))
                        if t not in result:result.append(t)
print min(map(sum,result))
print result

endtime = time.clock()
print "running time is %f second" % (endtime - starttime)

# <codecell>

a=set(G.neighbors(e[0]))

# <codecell>

dir(set)
set.intersection(

# <codecell>

a = 
primerange(2,100)

# <codecell>

a

# <codecell>

b.next()

# <codecell>


