"""
Binary search is the best approach to find the integer in a sorted array .
Because of its time complexity
It takes, O(log N)
and space complexity is O(1) constant

Below is the algorithm of binary search
"""

class Solution():
    def binary_search(self,nums, target):
        l = 0
        r = len(nums) -1
        while l<=r:
            m = (l + r) //2
            if nums[m] == target:
                return m
            elif target < nums[m]:
                r = m-1
            else:
                l = m+1
        return -1
    
