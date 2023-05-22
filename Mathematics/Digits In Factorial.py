import math
class Solution:
    def digitsInFactorial(N):
        sum = 0.0
        j = 1
        while(j<=N):
            sum+=(math.log10(j))
            j+=1
            
        return 1+math.floor(sum)
    print(digitsInFactorial(120))
