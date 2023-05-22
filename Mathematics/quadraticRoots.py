
import math
def quadraticRoots(a,b,c):
    D = b**2 - 4*a*c
    l =[]
    if D>0:
        root1 = math.floor((-b+D**0.5)/(2*a))
        root2 = math.floor((-b-D**0.5)/(2*a))
        
        if root1>root2:
            return root1,root2
        else:
            return root2,root1
    elif D==0:
        return int(-b/(2*a)),int(-b/(2*a))
    else:
        l.append(-1)
        return 1
print(quadraticRoots(1,-7,12))
