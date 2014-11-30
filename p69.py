import sympy
# gen prime table
T = {}
N = 1000000
for i in range(2,N+1):
    if sympy.isprime(i):
        T[i] = True

