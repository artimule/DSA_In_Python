'''
@artimule
You are given an interger I, find the absolute value of the interger I.

 

Example 1:

Input:
I = -32
Output: 32
Explanation: 
The absolute value of -32 is 32.
 

Example 2:

Input:
I = 45
Output: 45
Explanation: 
The absolute value of 45 is 45 itself.
 

Your Task:
You don't need to read input or print anything. Your task is to complete the function absolute() which takes an integer I as input parameter and return the absolute value of I.

 

Expected Time Complexity: O(1)
Expected Auxiliary Space : O(1)

 

Constraints:
-10^6 <= I <= 10^6
'''
#Solution:


class Solution:
    def absolute(self,I):
        # code here
        # if value is negative, then make it positive by multiplying it with -1
        # else return number as it is
        if(I < 0): 
            return -1 * I
        else:
            return I 
          
