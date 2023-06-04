# solving polar coordinates challenge in python 3 in hackerrank

import cmath

complexNumber = complex(input())
r = abs(complexNumber)
phi = cmath.phase(complexNumber)

print(r)
print(phi)
