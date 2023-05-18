'''
@artimule
Linear Search
Problem: Given an array arr[] of n elements, write a function to search a given element x in arr[].
Examples : 

Input : arr[] = {10, 20, 80, 30, 60, 50, 
110, 100, 130, 170}
x = 110;
Output : 6
Element x is present at index 6

Input : arr[] = {10, 20, 80, 30, 60, 50, 
110, 100, 130, 170}
x = 175;
Output : -1
Element x is not present in arr[].

A simple approach is to do a linear search, i.e 

1. Start from the leftmost element of arr[] and one by one compare x with each element of arr[]
2. If x matches with an element, return the index.
3. If x doesn’t match with any of elements, return -1.

Time Complexity : O(n)
Auxiliary Space: O(1)
'''

def search(arr, n, x):
    for i in range(0, n):
      if (arr[i] == x):
        return i
	return -1
# Driver Code
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
# Function call
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else :
    print("Element is present at index", result)

 
# Python3 program for linear search
def search(arr, search_Element):
    left = 0
    length = len(arr)
    position = -1
    right = length - 1

    # Run loop from 0 to right
    for left in range(0, right, 1):
      #If search_element is found with
      # left variable
      if (arr[left] == search_Element):
          position = left
          print("Element found in Array at ", position +
              1, " Position with ", left + 1, " Attempt")
          break

      # If search_element is found with# right variable
      if (arr[right] == search_Element):
          position = right
          print("Element found in Array at ", position + 1,
              " Position with ", length - right, " Attempt")
          break
      left += 1
      right -= 1

      # If element not found
    if (position == -1):
       print("Not found in Array with ", left, " Attempt")

# Driver code
arr = [1, 2, 3, 4, 5]
search_element = 5

# Function call
search(arr, search_element)

Output
('Element found in Array at ', 5, ' Position with ', 1, ' Attempt')




