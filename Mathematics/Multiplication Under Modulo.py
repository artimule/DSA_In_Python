class Solution:
    def multiplicationUnderModulo(self,a,b):
        '''
        :param a: given value of a
        :param b: given value of b
        :return: Integer , sum under modulo
        '''   
        # code here
        res = a*b
        res = res%(pow(10,9)+7)
        return res
        
        # or
        # mod= 1000000007
        # return ((a%mod)*(b%mod))%mod
