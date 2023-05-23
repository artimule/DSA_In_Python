class Solution:    
    ##Complete this function
    def modInverse(self,a,m):
        ##Your code here
        for i in range(1,m):
            if(a*i)%m==1:
                return i
        return -1
