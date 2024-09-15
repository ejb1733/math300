import cmath
import numpy as np

num_Qs = 9
ansDict = {}
letterArr = ['a','b','c','d','e']

for i in range(9):
    subq_dict = {}
    ansDict[f'Q{i+1}'] = subq_dict

def q1():
    z = complex(1,2)
    w = complex(2,-1)

    q1dict = ansDict['Q1']

    q1dict['q1a'] = z + 3*w
    q1dict['q1b'] = w.conjugate() - z
    q1dict['q1c'] = z**3
    q1dict['q1d'] = (w**2 + w).real
    q1dict['q1e'] = z**2 + z.conjugate() + complex(0,1)

def q2():
    z = complex(3,5)/complex(1,7)
    w = (complex(-1,np.sqrt(3))/2)**3

q1()
print(ansDict['Q1'])