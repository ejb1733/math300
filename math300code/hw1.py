import cmath
import numpy as np
import matplotlib.pyplot as plt

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

    x = [ele.real for ele in q1dict.values()]
    y = [ele.imag for ele in q1dict.values()]

    plt.scatter(x,y), plt.xlim(-15,15), plt.ylim(-15,15), plt.axhline(0),plt.axvline(0)
    for i in range(len(x)):
        plt.annotate(str(q1dict[f'q1{letterArr[i]}']), (x[i]+1,y[i]))
    plt.show()

    return q1dict

def q2():
    z = complex(3,5)/complex(1,7)
    w = (complex(-1,np.sqrt(3))/2)**3

    q2dict = ansDict['Q2']

    q2dict['q2b'] = f'Re(z): {z.real}, Im(z): {round(z.imag,3)}'
    q2dict['q2c'] = f'Re(w): {round(w.real,3)}, Im(z): {round(w.imag,3)}'

    return q2dict

q1dict = q1()
q2dict = q2()

def printAns(qnum='all'):
    if qnum == 'all':
        for q in ansDict:
            print('\n--=-- ' + q + ' --=--\n')
            for sub_q in ansDict[q]:
                print(f'{sub_q}: {ansDict[q][sub_q]}')
    else:
        print('\n--=-- Q' + qnum + ' --=--\n')
        for sub_q in ansDict[qnum]:
            print(f'{sub_q}: {ansDict[qnum][sub_q]}')

printAns()