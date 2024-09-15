import cmath
import numpy as np

letterArr = ['a','b','c','d','e']

# nqs: number of sub-questions
def q1():
    z = complex(1,2)
    w = complex(2,-1)

    ansDict = {}

    ansDict['q1a'] = z + 3*w
    ansDict['q1b'] = w.conjugate() - z
    ansDict['q1c'] = z**3
    ansDict['q1d'] = (w**2 + w).real
    ansDict['q1e'] = z**2 + z.conjugate() + complex(0,1)

    return ansDict

print(q1())