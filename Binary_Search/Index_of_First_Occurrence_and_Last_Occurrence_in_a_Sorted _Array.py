# Index of First Occurrence and Last Occurrence in a Sorted Array
'''
@artimule
Given a sorted array arr[] with possibly duplicate elements, the task is to find indexes of the first and last occurrences of an element x in the given array. 

Examples: 

Input : arr[] = {1, 3, 5, 5, 5, 5, 67, 123, 125}, x = 5
Output : First Occurrence = 2
              Last Occurrence = 5

Input : arr[] = {1, 3, 5, 5, 5, 5, 7, 123, 125 }, x = 7

Output : First Occurrence = 6
              Last Occurrence = 6
              
1. For the first occurrence of a number 

a) If (high >= low)
b) Calculate  mid = low + (high – low)/2;
c) If ((mid == 0 || x > arr[mid-1]) && arr[mid] == x)
        return mid;
d) Else if (x > arr[mid])
       return first(arr, (mid + 1), high, x, n);
e) Else
       return first(arr, low, (mid -1), x, n);
f) Otherwise return -1;

2. For the last occurrence of a number 

a) if (high >= low)
b) calculate mid = low + (high – low)/2;
c)if( ( mid == n-1 || x < arr[mid+1]) && arr[mid] == x )
        return mid;
d) else if(x < arr[mid])
       return last(arr, low, (mid -1), x, n);
e) else
      return last(arr, (mid + 1), high, x, n);      
f) otherwise return -1;
'''

# if x is present in arr[] then
# returns the index of FIRST
# occurrence of x in arr[0..n-1],
# otherwise returns -1

def first(l, low, high, x, n):
	while(low<=high):
		mid = low + (high - low) // 2
		if((mid == 0 or x > l[mid - 1]) and l[mid] == x):
			return mid
		elif(x > l[mid]):
			return first(l, (mid + 1), high, x, n)
		else:
			return first(l, low, (mid - 1), x, n)

	return -1

l = [1, 2, 2, 2, 2, 3, 4, 7, 8,8 ,8]
n = len(l)
x = 8
print("First Occurrence = ",
	first(l, 0, n - 1, x, n))

# if x is present in arr[] then
# returns the index of LAST occurrence
# of x in arr[0..n-1], otherwise
# returns -1
def last(l, low, high, x, n):
	while(low<=high):
		mid = low + (high - low) // 2
		if ((mid == n - 1 or x < l[mid + 1]) and l[mid] == x):
			return mid
		elif (x < l[mid]):
			return last(l, low, (mid - 1), x, n)
		else:
			return last(l, (mid + 1), high, x, n)

	return -1

# Driver program
l = [1, 2, 2, 2, 2, 3, 4, 7, 8,8 ,8]
n = len(l)
x = 8

print("Last Occurrence = ",
	last(l, 0, n - 1, x, n))
