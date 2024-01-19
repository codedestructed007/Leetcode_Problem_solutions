"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
"""

"""
Approach -
Solve the problem using binary searh algorithm to attain time complexity O(log(N))
if we find the value equal to target then find the left most and right most index of the
same value .
Time complexity analysis
binary search - O(logN)
left_index adn right_index - O(m) and O(m)
where m is a smalll number
oveall time complexity - O(log N)
"""

class Solution():
    def first_last_in_sorted_array(self, nums, target):
        l = 0
        r= len(nums) -1
        while l<=r:
            m = (l+r) //2
            if nums[m] == target:
                # find the left most index of the target value
                left_most = m
                while left_most > 0 and nums[left_most-1] == target:
                    left_most-=1
                # find the right most index of the target value
                right_most = m
                while right_most < len(nums)-1 and nums[right_most +1] == target:
                    right_most +=1

                return [left_most,right_most]

            elif nums[m] > target:
                r = m-1
                
            else:
                l = m +1

        return [-1,-1]
