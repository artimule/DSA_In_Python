import math
class Solution:
    def sumUnderModulo(self,a,b):
        # code here
        res = a+b
        res = res%(pow(10,9)+7)
        return res
        
        # or 
        # mod=pow(10,9)+7;
        # return ((a%mod)+(b%mod))%mod;
