"""
Given an integer array nums, return the third distinct maximum number in this array. If the third maximum does not exist, return the maximum number.


"""

class Solution():
    def thirdMax(self, nums):
        if not nums:
            return []

        nums = list(set(nums))
        nums.sort()
        if len(nums) <= 2:
            return nums[len(nums)-1]
        else:
            return nums[-3]
