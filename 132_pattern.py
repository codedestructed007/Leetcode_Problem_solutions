"""
Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

Return true if there is a 132 pattern in nums, otherwise, return false.
"""
class Solution:
    def Find123Pattern(self, nums):

        array = []
        check= float('-inf')

        for num in reversed(nums):

            if num < check:
                return True

            while array and num > array[-1]:
                check= array.pop()

            array.append(num)

        return True
