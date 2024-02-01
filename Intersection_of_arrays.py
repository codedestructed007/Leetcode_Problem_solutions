"""
You are given an array having inside it having n numbers of array where n is the
length of array (nums).
Return the list of sorted elements which are common in all the array in side nums
"""

class Solution():
    def insertection_of_arrays(self, nums):

        first_set = set(nums[0])

        for i in range(1,len(nums)):
            first_set = first_set.intersection(set(nums[i]))

        common_elements = sorted(list(first_set))

        return common_elements


"""
Time complexity is O(N),
Space Complexity is Constant

"""
