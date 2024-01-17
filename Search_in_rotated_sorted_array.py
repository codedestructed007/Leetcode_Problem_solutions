"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

"""
class Solution():
    def search_in_rotated_array(self, nums, target):
        l = 0
        r = len(nums) -1
        while l<=r:
            m = (l + r)//2
            if nums[m] == target:
                return m
            # case when the rotational factors value is greater than initial m vlaue
            elif nums[0] > nums[m]:
            # Now the target value can be both side either in left side or in right side
                if target > nums[m] and target <= nums[-1]:
                    l = m+1
                else:
                    r = m-1                              
            else:
                if nums[m] > target and nums[0] <= target:
                    r = m-1
                else:
                    l = m+1
        return -1


            
                            
