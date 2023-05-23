# LCM of two numbers

# LCM (Least Common Multiple) of two numbers is the smallest number which can be divided by both numbers. 

# For example, LCM of 15 and 20 is 60, and LCM of 5 and 7 is 35.

# A simple solution is to find all prime factors of both numbers, then find union of all factors present in both numbers. Finally, return the product of elements in union.

# An efficient solution is based on the below formula for LCM of two numbers ‘a’ and ‘b’. 

#    a x b = LCM(a, b) * GCD (a, b)

#    LCM(a, b) = (a x b) / GCD(a, b)
# Using GCD, we can find LCM.

# Below is the implementation of the above idea:

# Python program to find LCM of two numbers

# Recursive function to return gcd of a and b
def gcd(a,b):
	if a == 0:
		return b
	return gcd(b % a, a)

# Function to return LCM of two numbers
def lcm(a,b):
	return (a / gcd(a,b))* b

# Driver program to test above function
a = 15
b = 20
print('LCM of', a, 'and', b, 'is', lcm(a, b))


 

# Output

# LCM of 15 and 20 is 60
# Time Complexity: O(log(min(a,b))

# Auxiliary Space: O(log(min(a,b))

 
