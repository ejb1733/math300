import cmath

letterArr = ['a','b','c','d','e']

# nqs: number of sub-questions
def q1(nqs):
    z = complex(1,2)
    w = complex(2,-1)

    ansDict = {}

    for i in range(nqs):
        ansDict[f'q1{letterArr[i]}'] = 1
        
    # q1a = z + 3*w
    # q1b = w.conjugate() - z
    # q1c 

    return ansDict

ans = q1(4)

print(ans['q1a'])