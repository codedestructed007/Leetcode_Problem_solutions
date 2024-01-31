"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
"""



class Solution():
    def threeSumClosest(self, nums, target):
        if len(nums) < 3 :
            return None

        if len(nums) == 3:
            return sum(nums)


        nums.sort()
        closed_sum = float('inf')


        for i in range(len(nums) -2):
            left, right =i + 1, len(nums) -1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                current_diff = abs(current_sum - target)

                if current_diff < abs(closed_sum - target):
                    closed_sum = current_sum

                if current_sum < target:
                    left+=1
                elif current_sum > target:
                    right -=1

                else:
                    return current_sum
        return closed_sum




"""
Time complexity  - O(N^2)
Space Complexity - O(1)

Approach used  - Two poitners
main logic - check minimum value after subtracting the target value


For detailed explanation contact me

Thank you-----------------------------
"""
