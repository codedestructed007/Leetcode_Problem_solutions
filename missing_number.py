"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_elements = len(nums)
        supposed_to_be_sum = (total_elements*(total_elements+1))/2
        actual_sum = sum(nums)
        return supposed_to_be_sum - actual_sum

