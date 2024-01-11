"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 
"""
class Solution()
    def moveZeros(self, nums):
        i = 0
        j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i],nums[j] = nums[j],nums[i]
                i +=1
            j +=1

        return nums
