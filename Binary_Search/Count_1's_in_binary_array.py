'''
@artimule
Given a binary sorted non-increasing array of 1s and 0s. You need to print the count of 1s in the binary array.

Example 1:

Input:
N = 8
arr[] = {1,1,1,1,1,0,0,0}
Output: 5
Explanation: Number of 1's in given 
binary array : 1 1 1 1 1 0 0 0 is 5.
Example 2:

Input:
N = 8
arr[] = {1,1,0,0,0,0,0,0}
Output: 2
Explanation: Number of 1's in given 
binary array : 1 1 0 0 0 0 0 0 is 2.
Your Task:
The task is to complete the function countOne() which takes the array arr[] and its size N as inputs and returns the count of 1s in the input array.

Expected Time Complexity: O(LogN).
Expected Auxiliary Space: O(1).

Constraint:
1 <= N <= 5*106
arr[i] = 0,1
'''
#Solution
class Solution:
    def countO(self,arr,low,high): 
          
        if high>=low: 
              
            # get the middle index 
            mid = int(low + (high-low)/2)
              
            # check if the element at middle index is last 1 
            if ((mid == high or arr[mid+1]==0) and (arr[mid]==1)): 
                return mid+1
                  
            # If element is not last 1, recur for right side 
            if arr[mid]==1: 
                return self.countO(arr, (mid+1), high) 
                  
            # else recur for left side 
            return self.countO(arr, low, mid-1) 
          
        return 0
        
    def countOnes(self,A,N):
        return self.countO(A,0,len(A)-1)
      
      
