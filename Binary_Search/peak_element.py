'''
@artimule
An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. 


Example 1:

Input: 
N = 3
arr[] = {1,2,3}
Possible Answer: 2
Generated Output: 1
Explanation: index 2 is 3.
It is the peak element as it is 
greater than its neighbour 2.
If 2 is returned then the generated output will be 1 else 0.
Example 2:

Input:
N = 3
arr[] = {3,4,2}
Possible Answer: 1
Output: 1
Explanation: 4 (at index 1) is the 
peak element as it is greater than 
it's neighbor elements 3 and 2.
If 1 is returned then the generated output will be 1 else 0.
 

Your Task:
You don't have to read input or print anything. Complete the function peakElement() which takes the array arr[] and its size N as input parameters and return the index of any one of its peak elements.

Can you solve the problem in expected time complexity?

 

Expected Time Complexity: O(log N)
Expected Auxiliary Space: O(1)


Constraints:
1 ≤ N ≤ 105
1 ≤ A[] ≤ 106
'''
#Solution
class Solution:   
    def peakElement(self, arr, n):
        if n == 1:
            return 0
        low = 0
        high = n - 1
        while (low <= high):
            mid = low + (high - low) // 2
            if (mid > 0 and mid < n - 1):
                if (arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]):
                    return mid
                elif (arr[mid - 1] > arr[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            elif (mid == 0):
                if (arr[0] > arr[1]):
                    return 0
                else:
                    return 1
            elif (mid == n - 1):
                if (arr[n - 1] > arr[n - 2]):
                    return n - 1
                else:
                    return n - 2
        return 0
      
