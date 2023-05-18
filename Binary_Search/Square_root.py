'''
@artimule
Square Root

Given an integer X, find its square root. If X is not a perfect square, then return floor(√x).

Examples : 

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2.

Input: x = 11
Output: 3
Explanation:  The square root of 11 lies in between 3 and 4 so floor of the square root is 3.
Complexity Analysis: 

Time Complexity: O(log(X)). 
Auxiliary Space: O(1).
Square root an integer using Binary search:
The idea is to find the largest integer i whose square is less than or equal to the given number. The values of i * i is monotonically increasing, so the problem can be solved using binary search.

Below is the implementation of the above idea: 

Base cases for the given problem are when the given number is 0 or 1, then return X;
Create some variables, for storing the lower bound say l = 0, and for upper bound r = X / 2 (i.e, The floor of the square root of x cannot be more than x/2 when x > 1).
Run a loop until l <= r, the search space vanishes
Check if the square of mid (mid = (l + r)/2 ) is less than or equal to X, If yes then search for a larger value in the second half of the search space, i.e l = mid + 1, update ans = mid
Else if the square of mid is more than X then search for a smaller value in the first half of the search space, i.e r = mid – 1
Finally, Return the ans
'''
def floorSqrt(x):
	# Base cases
	if (x == 0 or x == 1):
		return x
	# Do Binary Search for floor(sqrt(x))
	start = 1
	end = x//2
	while (start <= end):
		mid = (start + end) // 2
		# If x is a perfect square
		if (mid*mid == x):
			return mid
		# Since we need floor, we update answer when mid*mid is smaller than x, and move closer to sqrt(x)
		if (mid * mid < x):
			start = mid + 1
			ans = mid
		else:
			# If mid*mid is greater than x
			end = mid-1
	return ans
# driver code
x = 100
print(floorSqrt(x))
