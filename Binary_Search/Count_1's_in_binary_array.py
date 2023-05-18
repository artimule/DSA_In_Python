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

def countOnes(arr, n):
    low = 0
    high = n - 1
    while (low <= high):  # get the middle index
        mid = int(low + (high-low) // 2)

        # else recur for left side
        if (arr[mid] < 1):
            high = mid - 1

        # If element is not last 1, recur for right side
        elif(arr[mid] > 1):
            low = mid + 1
        else:

            # check if the element at middle index is last 1
            if (mid == n - 1 or arr[mid + 1] != 1):
                return mid + 1
            else:
                low = mid + 1

    return 0


# Driver code
if __name__ == '__main__':

    arr = [1, 1, 1, 1, 0, 0, 0]
    n = len(arr)

    print("Count of 1's in given array is ", countOnes(arr, n))
