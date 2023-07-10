#  Check if Array Is Sorted
def isSorted(n: int,  a: [int]) -> int:
    # Write your code here.
    for i in range(1,n):
        if a[i-1]>a[i]:
            return 0
    return 1

#  Check if Array Is Sorted and Rotated
class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1] > nums[i]:
                count += 1
        if nums[n-1] > nums[0]:
            count += 1
        return count <= 1
