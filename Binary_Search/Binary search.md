**Binary Search : Explained** 
Let’s consider this simple problem statement:
You are given an array of integers and a key element, your task is to search for the key in the given array.
One simple approach you can follow is to traverse through the entire array and while traversing compare every element with the key, 
if the key is a match with current array element then you are done with your task. 
But what if the given array length is very large?
If you check every element with a key then it will take more time which is not optimal.

So, to optimise the search operation we will use “Binary Search”, that is an algorithm for searching and uses the “Divide and Conquer” technique.
Note: Binary Search will work only on Sorted numbers

**Divide and Conquer:**

Break down the problem into subproblems
Solve the sub problems
Merge the sub problems to get desired Output

Binary search algorithm will work, This algorithm will look for the number by dividing the array into half and 
check if the middle element is greater/lesser/equal to the Key value 
if the key is less than the middle element then the algorithm will look for key only from starting element to middle-1 position element, 
else if the key is greater than the mid then it will look from middle element +1 index position element to last element, 
else if the key is equal to the middle then the algorithm will terminate their itself. 
This process continues for every half of the array till starting index is less than the ending index.

This is how binary search works.

**Algorithm:**

Consider start index to be at 0 and last index to be n-1th index at starting      //n->length 
Find middle index(mid) of the array
If key is found to be less than mid index element then update last index of the array to mid -1
Else if key is found to be greater than mid index element then update start index of the array to mid +1
Else check for mid index element with key if not match repeat the above steps till start index is less than end index

![image](https://github.com/Artimule/DSA_In_Python/assets/53312100/dfd35cd8-c15f-4a27-91ea-59f31ee83897)
