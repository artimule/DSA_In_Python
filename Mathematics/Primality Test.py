# prime number
from math import sqrt
def isPrime(N):
    if N<=1:
        return False
    for i in range(2,int(sqrt(N))+1):
        if N%i==0:
            return False
    return True
print(isPrime(22))
